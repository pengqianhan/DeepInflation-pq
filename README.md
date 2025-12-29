# DeepInflation

AI Agent for Inflationary Cosmology Research and Model Discovery, based on [Agno](https://github.com/agno-agi/agno).

## Setup

### 1. Python

```bash
# pip
pip install -r requirements.txt

# or uv
uv sync
```

### 2. Julia

Symbolic regression requires Julia. Install from <https://julialang.org/downloads/>.

```bash
# Initialize Julia packages (~3-5 min first time)
python setup_julia.py
```

### 3. Run

```bash
python app.py  # → http://127.0.0.1:7860
```

## API Configuration

Configure in web UI or via environment variables. UI settings take priority.

**OpenAI:**

```bash
export OPENAI_API_KEY="sk-..."
```

**Custom provider** (OpenAI-compatible API):

```bash
export OPENAI_API_KEY="your-key"
export BASE_URL="https://api.your-provider.com/v1"
```

**Ollama** (local):

```bash
export BASE_URL="http://localhost:11434/v1"
# Then set model in UI
```

## Usage

### Web UI

Natural language queries via the chat interface:

| Query                                       | Tool                          |
| ------------------------------------------- | ----------------------------- |
| "What is ns for V = phi^2?"                 | `analyze_potential`           |
| "Plot V = (1-exp(-sqrt(2/3)*phi))^2"        | `plot_potential`              |
| "Find potentials with ns ≈ 0.965, r < 0.01" | `search_potential` (SR)       |
| "What is Starobinsky inflation?"            | `search_knowledge_base` (RAG) |

### Python API

```python
from agent import DeepInflation

agent = DeepInflation(model="gpt-5.2")
response = agent.run("What is ns for V = phi^2?")
```

## Acknowledgments

- [Agno](https://github.com/agno-agi/agno) — Agent framework
- [PySR](https://github.com/MilesCranmer/PySR) — Symbolic regression
- [Encyclopædia Inflationaris](https://arxiv.org/abs/1303.3787) — Knowledge base.
