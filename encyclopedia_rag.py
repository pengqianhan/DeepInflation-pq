"""Encyclopedia RAG: Agno Knowledge with LanceDB hybrid search."""

import asyncio
import json
import os
from hashlib import md5
from pathlib import Path
from typing import Optional

import tiktoken

from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.lancedb import LanceDb, SearchType

# Configuration
MODELS_DIR = "data/models"
INFLATION_LIST_PATH = "data/inflation_list.json"
LANCEDB_DIR = "tmp/lancedb"
TABLE_NAME = "encyclopedia"
CONFIG_FILE = "embedding_config.json"
MAX_TOKENS = 8000
VERBOSE = True

_encoding = tiktoken.get_encoding("cl100k_base")


def _print(*args, **kwargs):
    if VERBOSE:
        print(*args, **kwargs)


class EncyclopediaRAG:
    """RAG system using Agno Knowledge with LanceDB hybrid search (Vector + BM25)."""

    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        embedding_model: str = "text-embedding-3-small",
        lancedb_dir: str = LANCEDB_DIR,
        models_dir: str = MODELS_DIR
    ):
        self.lancedb_dir = lancedb_dir
        self.models_dir = models_dir
        self.embedding_model = embedding_model
        self.config_path = Path(lancedb_dir) / CONFIG_FILE

        _print("[Encyclopedia] Initializing...")

        # Initialize embedder
        self.embedder = OpenAIEmbedder(
            id=embedding_model,
            api_key=api_key,
            base_url=base_url,
            enable_batch=True,
        )
        self.embedder.dimensions = len(self.embedder.get_embedding("test"))
        print(f"[Encyclopedia] Embedding: '{embedding_model}' (dim={self.embedder.dimensions})")

        # Initialize vector database
        self.vector_db = LanceDb(
            uri=lancedb_dir,
            table_name=TABLE_NAME,
            search_type=SearchType.hybrid,
            embedder=self.embedder,
        )

        # Initialize Knowledge
        self.knowledge = Knowledge(
            name="Encyclopaedia Inflationaris",
            description="RAG knowledge base for inflation cosmology models.",
            vector_db=self.vector_db,
            max_results=4,
        )

        # Check saved config, rebuild if model changed
        saved_model = None
        if self.config_path.exists():
            saved_model = json.load(open(self.config_path)).get("embedding_model")

        count = self.vector_db.get_count()
        if count > 0 and saved_model and saved_model != embedding_model:
            _print(f"[Encyclopedia] Model changed: '{saved_model}' → '{embedding_model}', rebuilding...")
            self.rebuild_index()
        elif count > 0:
            _print(f"[Encyclopedia] Loaded {count} documents")
        else:
            self._build_index()
            # Save config on first build
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            json.dump({"embedding_model": embedding_model}, open(self.config_path, 'w'))
        _print("[Encyclopedia] Ready")

    def _build_index(self):
        """Build LanceDB index with batch embedding.

        Note: We use direct table.add() instead of Knowledge.add_content() because
        add_content() calls insert() which re-embeds each document individually.
        """
        
        _print("[Index] Building...")
        chunks = self._load_and_chunk_documents()

        # Batch embed all contents in one API call
        _print(f"[Index] Batch embedding {len(chunks)} documents...")
        contents = [c[0] for c in chunks]
        embeddings, _ = asyncio.run(
            self.embedder.async_get_embeddings_batch_and_usage(contents)
        )
        _print(f"[Index] Got {len(embeddings)} embeddings")

        # Prepare data for LanceDB (same format as LanceDb.insert)
        _print("[Index] Inserting into LanceDB...")
        data = []
        for i, (content, name, metadata) in enumerate(chunks):
            cleaned_content = content.replace("\x00", "\ufffd")
            doc_id = md5(cleaned_content.encode()).hexdigest()
            payload = {
                "name": name,
                "meta_data": metadata,
                "content": cleaned_content,
                "usage": None,
                "content_id": None,
                "content_hash": "encyclopedia",
            }
            data.append({
                "id": doc_id,
                "vector": embeddings[i],
                "payload": json.dumps(payload),
            })

        # Direct insert via LanceDB table API (bypasses buggy insert())
        self.vector_db.table.add(data)

        count = self.vector_db.get_count()
        _print(f"[Index] Built {count} documents -> {self.lancedb_dir}/")

    def _load_and_chunk_documents(self) -> list:
        """Load markdown files and chunk by section/token limit.

        Returns list of (content, name, metadata) tuples.
        """
        _print(f"[Index] Loading documents from {self.models_dir}...")
        models_path = Path(self.models_dir)
        if not models_path.exists():
            raise FileNotFoundError(f"Models directory not found: {self.models_dir}")

        potential_list = self._load_potential_metadata()
        all_chunks = []
        intact_count, split_count = 0, 0

        for md_file in sorted(models_path.glob("*.md")):
            content = md_file.read_text(encoding='utf-8').strip()
            if len(content) < 100:
                continue

            model_name = md_file.stem
            token_count = len(_encoding.encode(content))
            base_metadata = potential_list.get(model_name, {})

            if token_count <= MAX_TOKENS:
                meta = {"model": model_name, "title": model_name, **base_metadata}
                all_chunks.append((content, model_name, meta))
                intact_count += 1
            else:
                _print(f"[Index] Splitting '{model_name}' ({token_count} tokens)")
                chunks = self._chunk_by_sections(content, model_name, base_metadata)
                all_chunks.extend(chunks)
                split_count += 1

        _print(f"[Index] Loaded {len(all_chunks)} chunks from {intact_count + split_count} models")
        return all_chunks

    def _load_potential_metadata(self) -> dict:
        """Load potential metadata from inflation_list.json."""
        json_path = Path(INFLATION_LIST_PATH)
        if not json_path.exists():
            return {}

        with open(json_path, encoding='utf-8') as f:
            data = json.load(f)

        potential_list = {
            entry['Model']: {
                'potential_latex': entry.get('Potential $V(\\phi)$', ''),
                'parameters': entry.get('Parameters', '')
            }
            for entry in data
        }
        _print(f"[Index] Loaded {len(potential_list)} potentials")
        return potential_list

    def _chunk_by_sections(self, content: str, model_name: str, base_metadata: dict) -> list:
        """Split markdown by sections, further chunk if exceeds MAX_TOKENS."""
        chunks = []
        lines = content.split('\n')
        current_section = []
        current_title = model_name

        for line in lines:
            if line.startswith('# ') and current_section:
                section_content = '\n'.join(current_section).strip()
                if section_content and len(_encoding.encode(section_content)) > 50:
                    chunks.extend(self._chunk_section(
                        section_content, current_title, model_name, base_metadata
                    ))
                current_section = [line]
                current_title = f"{model_name} - {line[2:].strip()}"
            else:
                current_section.append(line)

        # Last section
        if current_section:
            section_content = '\n'.join(current_section).strip()
            if section_content and len(_encoding.encode(section_content)) > 50:
                chunks.extend(self._chunk_section(
                    section_content, current_title, model_name, base_metadata
                ))

        return chunks

    def _chunk_section(self, content: str, title: str, model_name: str, base_metadata: dict) -> list:
        """Chunk a section by token limit if needed."""
        token_count = len(_encoding.encode(content))

        if token_count <= MAX_TOKENS:
            meta = {"model": model_name, "title": title, **base_metadata}
            return [(content, title, meta)]

        # Further chunk by paragraphs
        _print(f"[Index] - Chunking section '{title}' ({token_count} tokens)")
        chunks = []
        paragraphs = content.split('\n\n')
        current_chunk = []
        current_tokens = 0

        for para in paragraphs:
            para_tokens = len(_encoding.encode(para))
            if current_tokens + para_tokens > MAX_TOKENS and current_chunk:
                chunk_content = '\n\n'.join(current_chunk)
                chunk_title = f"{title} (part {len(chunks) + 1})"
                meta = {"model": model_name, "title": chunk_title, **base_metadata}
                chunks.append((chunk_content, chunk_title, meta))
                current_chunk = [para]
                current_tokens = para_tokens
            else:
                current_chunk.append(para)
                current_tokens += para_tokens

        if current_chunk:
            chunk_content = '\n\n'.join(current_chunk)
            chunk_title = f"{title} (part {len(chunks) + 1})" if chunks else title
            meta = {"model": model_name, "title": chunk_title, **base_metadata}
            chunks.append((chunk_content, chunk_title, meta))

        return chunks

    def rebuild_index(self):
        """Force rebuild the index and save config."""
        _print("[Encyclopedia] Rebuilding index...")
        if self.vector_db.exists():
            self.vector_db.drop()
        self.vector_db.create()
        self._build_index()
        # Save embedding model config
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        json.dump({"embedding_model": self.embedding_model}, open(self.config_path, 'w'))


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    print("=" * 60)
    print("Testing Encyclopedia RAG System (Agno + LanceDB)")
    print("=" * 60)

    rag = EncyclopediaRAG(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL"),
        embedding_model="text-embedding-3-small",
    )

    # Test search via Knowledge
    # results = rag.knowledge.search("Tip Inflation", max_results=4)
    # print(results)
    
    docs = rag.vector_db.search("Dual Inflation model 'dual inflation' inflationary cosmology potential", limit=4)

    results = [
                {
                    "title": doc.meta_data.get("title", "Unknown"),
                    # "content": doc.content,
                    "metadata": doc.meta_data
                }
                for doc in docs
            ]
    print(json.dumps(results, indent=2, ensure_ascii=False))