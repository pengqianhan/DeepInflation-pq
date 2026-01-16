"""Encyclopedia RAG: Parent Document Retrieval with LanceDB hybrid search.

Architecture:
- Small chunks for precise semantic matching
- Parent documents (sections or full files) for complete context
- Retrieval: search chunks -> score parents by RRF -> return top-N parents
"""

import asyncio
import json
import os
from hashlib import md5
from pathlib import Path

import tiktoken
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.vectordb.lancedb import LanceDb, SearchType

# Configuration
_PROJECT_ROOT = Path(__file__).parent.parent
MODELS_DIR = _PROJECT_ROOT / "data/models"
MODEL_LIST_PATH = _PROJECT_ROOT / "data/model_list.json"
LANCEDB_DIR = _PROJECT_ROOT / "tmp/lancedb"
TABLE_NAME = "encyclopedia_chunks"
CONFIG_FILE = "embedding_config.json"
CHUNK_TOKENS = 500  # Small chunks for precise matching
PARENT_MAX_TOKENS = 5000  # Files larger than this are split by H1 sections
VERBOSE = True

_enc = tiktoken.get_encoding("cl100k_base")


def _print(*args, **kwargs):
    if VERBOSE:
        print(*args, **kwargs)


def _tokens(text: str) -> int:
    return len(_enc.encode(text))


class EncyclopediaRAG:
    """Parent Document RAG: search small chunks, return full parent documents."""

    def __init__(
        self,
        api_key: str,
        base_url: str | None = None,
        embedding_model: str = "text-embedding-3-small",
    ):
        self.embedding_model = embedding_model
        self.config_path = Path(LANCEDB_DIR) / CONFIG_FILE
        self.parent_store: dict[str, dict] = {}

        _print("[Encyclopedia] Initializing...")

        # Initialize embedder
        self.embedder = OpenAIEmbedder(
            id=embedding_model,
            api_key=api_key,
            base_url=base_url,
            enable_batch=True,
            batch_size=300,
        )
        self.embedder.dimensions = len(self.embedder.get_embedding("test"))
        print(f"[Encyclopedia] Embedding: '{embedding_model}' (dim={self.embedder.dimensions})")

        # Initialize vector database
        self.vector_db = LanceDb(
            uri=LANCEDB_DIR,
            table_name=TABLE_NAME,
            search_type=SearchType.hybrid,
            embedder=self.embedder,
            use_tantivy=False,  # to retrive formulas ?
        )

        # Load existing index or build new one
        saved = json.load(open(self.config_path, encoding="utf-8")) if self.config_path.exists() else {}
        count = self.vector_db.get_count()

        if count > 0 and saved.get("embedding_model") == embedding_model:
            self.parent_store = saved.get("parent_store", {})
            _print(f"[Encyclopedia] Loaded {count} chunks, {len(self.parent_store)} parents")
        else:
            if count > 0:
                _print("[Encyclopedia] Config changed, rebuilding...")
                self.vector_db.drop()
                self.vector_db.create()
            self._build_index()

        _print(f"[Encyclopedia] Ready ({len(self.parent_store)} parents)")

    def _build_index(self):
        """Build chunk index and parent store from markdown files."""
        _print("[Index] Building...")

        # Load potential metadata from model_list.json
        potentials = {}
        meta_path = Path(MODEL_LIST_PATH)
        if meta_path.exists():
            for entry in json.load(open(meta_path, encoding="utf-8")):
                potentials[entry["Model"]] = {
                    "potential_latex": entry.get("Potential $V(\\phi)$", ""),
                    "parameters": entry.get("Parameters", ""),
                }
            _print(f"[Index] Loaded {len(potentials)} potential metadata")

        all_chunks = []  # List of (chunk_content, parent_id)

        for md_file in sorted(Path(MODELS_DIR).glob("*.md")):
            content = md_file.read_text(encoding="utf-8").strip()
            if len(content) < 100:
                continue

            model_name = md_file.stem
            metadata = potentials.get(model_name, {})

            # Split into parents: whole file for short, by sections for long
            if _tokens(content) <= PARENT_MAX_TOKENS:
                parents = [(model_name, content)]
            else:
                parents = self._split_by_sections(content, model_name)

            # Process each parent
            for title, text in parents:
                parent_id = md5(title.encode()).hexdigest()[:16]
                self.parent_store[parent_id] = {
                    "title": title,
                    "content": text,
                    "metadata": metadata,
                    "model": model_name,
                }

                # Remove header line for chunking
                lines = text.split("\n")
                body = "\n".join(lines[1:]).strip() if lines[0].startswith("# ") else text

                for chunk in self._chunk_by_paragraphs(body):
                    all_chunks.append((chunk, parent_id))

            _print(f"[Index] {model_name}: {len(parents)} parent(s)")

        _print(f"[Index] Total: {len(all_chunks)} chunks from {len(self.parent_store)} parents")

        # Batch embed all chunks
        _print("[Index] Batch embedding...")
        contents = [c[0] for c in all_chunks]
        embeddings, _ = asyncio.run(self.embedder.async_get_embeddings_batch_and_usage(contents))
        _print(f"[Index] Got {len(embeddings)} embeddings")

        # Insert into LanceDB
        _print("[Index] Inserting into LanceDB...")
        data = []
        for i, (chunk, parent_id) in enumerate(all_chunks):
            parent = self.parent_store[parent_id]
            data.append(
                {
                    "id": md5(chunk.encode()).hexdigest(),
                    "vector": embeddings[i],
                    "payload": json.dumps(
                        {
                            "name": parent["title"],
                            "meta_data": {
                                "parent_id": parent_id,
                                "model": parent["model"],
                            },
                            "content": chunk.replace("\x00", "\ufffd"),
                            "usage": None,
                            "content_id": None,
                            "content_hash": "encyclopedia",
                        }
                    ),
                }
            )
        self.vector_db.table.add(data)

        # Save config with parent store
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        json.dump(
            {
                "embedding_model": self.embedding_model,
                "parent_store": self.parent_store,
            },
            open(self.config_path, "w", encoding="utf-8"),
            ensure_ascii=False,
        )

        _print(f"[Index] Built {self.vector_db.get_count()} chunks -> {LANCEDB_DIR}/")

    def _split_by_sections(self, content: str, model_name: str) -> list[tuple[str, str]]:
        """Split markdown by H1 headers into sections."""
        sections = []
        current_lines = []
        current_title = model_name
        is_first = True

        for line in content.split("\n"):
            if line.startswith("# "):
                # Save previous section
                if current_lines:
                    text = "\n".join(current_lines).strip()
                    if _tokens(text) > 50:
                        sections.append((current_title, text))
                # Start new section
                current_title = model_name if is_first else f"{model_name} - {line[2:].strip()}"
                is_first = False
                current_lines = [line]
            else:
                current_lines.append(line)

        # Last section
        if current_lines:
            text = "\n".join(current_lines).strip()
            if _tokens(text) > 50:
                sections.append((current_title, text))

        return sections or [(model_name, content)]

    def _chunk_by_paragraphs(self, text: str) -> list[str]:
        """Split text into chunks respecting paragraph boundaries."""
        if _tokens(text) <= CHUNK_TOKENS:
            return [text]

        chunks = []
        current = []
        current_tokens = 0

        for para in text.split("\n\n"):
            para = para.strip()
            if not para:
                continue

            para_tokens = _tokens(para)

            # Large paragraph: flush current and add as-is
            if para_tokens > CHUNK_TOKENS:
                if current:
                    chunks.append("\n\n".join(current))
                    current, current_tokens = [], 0
                chunks.append(para)
                continue

            # Would exceed limit: flush current
            if current_tokens + para_tokens > CHUNK_TOKENS and current:
                chunks.append("\n\n".join(current))
                current, current_tokens = [], 0

            current.append(para)
            current_tokens += para_tokens

        if current:
            chunks.append("\n\n".join(current))

        return chunks

    def search(self, query: str, num_chunks: int = 10, num_parents: int = 3) -> list[dict]:
        """Search using Reciprocal Rank Fusion (RRF) scoring.

        RRF score = sum(1/(k+rank)) for each matched chunk, where k=1.
        """
        chunk_results = self.vector_db.search(query, limit=num_chunks)
        if not chunk_results:
            return []

        # Score parents using RRF (k=1)
        scores: dict[str, float] = {}
        for rank, doc in enumerate(chunk_results):
            parent_id = doc.meta_data.get("parent_id")
            if parent_id:
                scores[parent_id] = scores.get(parent_id, 0) + 1.0 / (rank + 1 + 1)

        # Return top parents sorted by score
        ranked = sorted(scores.keys(), key=lambda p: scores[p], reverse=True)
        return [
            {**self.parent_store[pid], "score": scores[pid]} for pid in ranked[:num_parents] if pid in self.parent_store
        ]


# ============================================================================
# Singleton and Tool
# ============================================================================

_rag: EncyclopediaRAG | None = None


def init_rag(
    api_key: str,
    base_url: str | None = None,
    embedding_model: str = "text-embedding-3-small",
) -> EncyclopediaRAG:
    """Initialize the RAG singleton."""
    global _rag
    _rag = EncyclopediaRAG(api_key, base_url, embedding_model)
    return _rag


def search_encyclopedia(query: str, top_k: int = 3) -> str:
    """Search the Encyclopaedia Inflationaris for inflation models.

    This tool searches a knowledge base of 70+ inflation models from physics literature.
    Use it to find information about specific inflation models, their potentials,
    predictions, and theoretical background.

    Args:
        query: Search query in plain English (no LaTeX or math symbols).
        top_k: Number of documents to return (default 3, max 5).

    Returns:
        JSON string containing matched inflation models with full documentation.
    """
    if _rag is None:
        return json.dumps({"success": False, "error": "Encyclopedia not initialized"})

    top_k = max(1, min(5, top_k))

    try:
        results = _rag.search(query, num_chunks=4 * top_k, num_parents=top_k)
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})

    if not results:
        return json.dumps(
            {
                "success": False,
                "message": "No matching models found. Try different keywords.",
                "results": [],
            }
        )

    return json.dumps(
        {
            "success": True,
            "count": len(results),
            "results": [
                {
                    "title": r["title"],
                    "content": r["content"],
                    "potential_latex": r["metadata"].get("potential_latex", ""),
                    "parameters": r["metadata"].get("parameters", ""),
                }
                for r in results
            ],
        },
        ensure_ascii=False,
    )
