# DeepInflation

AI agent for inflation cosmology research using Agno framework.

## Setup

### 1. Python

```bash
# pip
pip install -r requirements.txt

# or uv
uv sync
```

### 2. Julia

Install Julia first: <https://julialang.org/downloads/>

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
export OPENAI_BASE_URL="https://api.your-provider.com/v1"
```

**Ollama** (local):

```bash
export OPENAI_BASE_URL="http://localhost:11434/v1"
# Then set model in UI
```

## Architecture

```text
agent.py           # Agno Team (main + SR sub-agent)
tools.py           # analyze_potential, plot_potential
sr_search.py       # search_potential (ProcessPoolExecutor isolation)
inflation.py       # Python inflation calculations
encyclopedia_rag.py# LanceDB hybrid search (Vector + BM25)
app.py             # Gradio web interface
```

## Quick Example

```python
from agent import DeepInflation
agent = DeepInflation(model="gpt-5.2")
response = agent.run("What is ns for V = phi^2?")
```
