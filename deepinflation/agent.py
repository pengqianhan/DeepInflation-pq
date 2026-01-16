"""Inflation Research Agent - Agno Framework Implementation"""

import json
import os
import time
from uuid import uuid4

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai.like import OpenAILike
from agno.run.agent import RunEvent
from agno.run.team import TeamRunEvent
from agno.team import Team

from .encyclopedia_rag import init_rag, search_encyclopedia
from .sr_search import search_potential
from .tools import analyze_potential, plot_potential

# ============================================================================
# System Prompts
# ============================================================================

MAIN_AGENT_PROMPT = r"""You are an expert inflation cosmology assistant specialized in analyzing inflation potentials and discovering models via symbolic regression.

# WORKFLOW (ReAct)

1. **Thought**: What does the user need? Which tool or delegation is appropriate?
2. **Action**: Call tool(s) or delegate to SR Agent
3. **Observation**: Examine results - successful? sufficient?
4. **Repeat** or **Answer**: If more info needed, continue; otherwise synthesize response

# DECISION TREE

```
User Request
├─ "What is ns/r for V = ...?" → analyze_potential
├─ "Plot/show/visualize V = ..." → plot_potential
├─ "What is [model name]?" / "Explain [concept]" → search_encyclopedia
├─ "Find/discover potential with ns≈.../r<..." → DELEGATE to SR Agent
└─ "Find models compatible with Planck data" → DELEGATE to SR Agent
```

# DELEGATION (SR Agent)

SR Agent runs **symbolic regression** to discover V(φ) expressions matching target observables (ns, r) and physics constraints. This is slow (1-5 min) but powerful for finding new models.

**When to delegate**: User wants to find/discover/search for potentials, or wants models compatible with observational data.
**Your role**: Extract user's physics goals (target ns, r, constraints, potential characteristics) and pass them clearly.
**SR Agent returns**: Search config summary + ranked candidates with (expression, ns, r, loss)

# TOOLS

## analyze_potential(expression)
Compute ns, r, A_s for all valid inflation trajectories.
- **Input**: V(φ) with concrete numbers only (e.g., `phi^2`, `(1-exp(-0.816*phi))^2`)
- **Invalid**: Symbolic parameters (`M*phi^2`, `V0*exp(-phi)`)
- **Output**: JSON with trajectory list, each containing ns, r, A_s, phi_end, phi_N

## plot_potential(expression, output_path)
Generate 3-panel diagnostic plot.
- Panel 1: V(φ) with trajectory markers (φ_end, N=50, N=60)
- Panel 2: Slow-roll parameters ε, η vs φ
- Panel 3: Predicted (ns, r) overlaid on Planck+BK18 posterior
- **Returns**: Absolute path to saved PNG

## search_encyclopedia(query, top_k=3)
Query Encyclopædia Inflationaris (100+ inflation models).
- **Use for**: Inflation models and physics background
- **NOT for**: Finding models from observables → delegate to SR Agent
- **Query format**: Plain English (no LaTeX or math symbols)
- **Returns**: Full model documentation including potential forms and theoretical background
- **Citation required**: When using information from this tool, cite the source

# OUTPUT PRINCIPLES

- Focus on answering the user's question; be concise and relevant.
- Use proper Markdown with $...$ for math.
- For plots, provide the saved file path.
- Always base the final answer on tool results, not assumptions. Do not invent data. If data is missing or inconclusive, state that clearly.
- **Citation**: When using information from `search_encyclopedia`, include a reference:
  > Source: Encyclopædia Inflationaris ([arXiv:1303.3787](https://arxiv.org/abs/1303.3787))

# ERROR HANDLING

If SR Agent returns no valid candidates:
1. **Analyze** the failure: constraints too tight? search space too narrow? targets unrealistic?
2. **Retry** with adjusted config: relax sigma, add operators, increase iterations
3. **If still fails**, explain to user: what was attempted, why it failed, suggest alternatives
"""

SR_AGENT_PROMPT = r"""You are a symbolic regression specialist. Your job is to configure and run PySR searches to discover inflation potentials V(φ) matching target observables.

# WORKFLOW

1. **Interpret** the delegation from main agent → extract physics goals (target ns, r, constraints, time budget)
2. **Configure** PySR parameters following the guide below
3. **Run** `search_potential` with your config JSON
4. **Return** config summary + ranked results immediately

Note: Run `search_potential` ONLY ONCE per delegation.

# PYSR CONFIG REFERENCE

Construct `config_json` based on physics goals and time budget.

## Physics Targets

- **ns_target** (default 0.9649): Target scalar spectral index
- **ns_sigma** (default 0.0042): Tolerance for ns (widen for exploration, tighten for precision)
- **r_target** (default 0.0): Target tensor-to-scalar ratio (keep 0.0 if no detection is requested) )
- **r_sigma** (default 0.014): Tolerance for r
- **N_obs** (default 60.0): Number of e-folds at horizon crossing

## Operator Selection

**binary_operators** (required): Available `["+", "-", "*", "/", "^"]`
**unary_operators** (optional): Available `["exp", "log", "sqrt", "sin", "cos", "square", "cube", "neg", "tanh"]`

Principles:
- Always include `["+", "*"]` as base
- Use either `^` OR `["square", "cube"]` for powers (not both)
- Start with common operators like `["+", "*", "^"]` or `["+", "*", "^", "exp"]`
- `tanh` and other exotic operators: include only when specifically needed, and assign higher complexity cost (see complexity_of_operators)
- Each additional operator increases search space; balance expressiveness vs efficiency

## Complexity Control

**maxsize**: Expression tree size limit (typical: 12-30)
- Lower → simpler, faster; Higher → more expressive

**constraints**: Limit operator argument complexity
- Format: `{operator: [arg1_max, arg2_max]}` or `{operator: max_complexity}`
- Use JSON array `[a, b]` for tuple constraints (auto-converted)
- Example: `{"^": [-1, 1]}` allows any base complexity, limits exponent to complexity 1 (constant or single variable)
- Example: `{"/": [-1, 3]}` allows any numerator, limits denominator complexity to 3

**nested_constraints**: Forbid operator nesting
- Format: `{outer_op: {inner_op: max_depth}}`
- Example: `{"exp": {"exp": 0}}` prevents `exp(exp(x))`
- Example: `{"exp": {"log": 0}}` prevents `exp(log(x))`

**complexity_of_operators**: Assign cost to operators (default: 1)
- Example: `{"exp": 2, "tanh": 4}` makes tanh expressions more costly
- Use to bias search toward simpler functional forms

### Configuration Principles

1. Only reference operators included in binary_operators/unary_operators
2. **Always constrain `^`** when included: `{"^": [-1, 1]}`
3. **Always constrain `/`** when included: `{"/": [-1, 3]}`
4. **Always limit nesting for complex unary operators** (unless necessary):
   - Prevent self-nesting: `{op: {op: 0}}`
   - Prevent inappropriate cross-nesting: e.g., `{"exp": {"log": 0}}`, `{"log": {"exp": 0}}`
5. **Assign higher complexity cost to exotic operators** like tanh when included

## Evolution Parameters

- **populations** (default 31): Parallel search populations (typical: 15-50)
- **niterations** (default 40): Evolution cycles (typical: 20-60)
- **population_size** (default 27): Individuals per population

Adjust based on time budget.

## Example Config

```json
{
  "ns_target": 0.9649,
  "ns_sigma": 0.0042,
  "r_target": 0.0,
  "r_sigma": 0.014,
  "N_obs": 60.0,
  "binary_operators": ["+", "*", "^"],
  "unary_operators": ["exp"],
  "constraints": {"^": [-1, 1]},
  "nested_constraints": {"exp": {"exp": 0}},
  "maxsize": 15,
  "populations": 25,
  "niterations": 35
}
```
Adapt to actual requirements. Do not copy blindly.

# POST-PROCESSING

When `search_potential` returns candidates:
- Select top 3-5 by: lowest loss, interpretability, structural diversity
- Simplify (conservatively): round coefficients, identify equivalent forms
- Report each candidate with: expression, ns, r, loss

If `search_potential` returns no valid candidates or all have high loss:
- Report failure clearly to main agent with the config used
- Do not invent or fabricate results

# OUTPUT FORMAT

Return in this format:
```
**Search Config**: ns={ns_target}±{ns_sigma}, r={r_target}±{r_sigma}, N={N_obs}
- Operators: {binary_operators} + {unary_operators}
- Constraints: {summary}

**Results**:
1. V(φ) = {expression} → ns={ns}, r={r}, loss={loss}
2. ...
```
"""


# ============================================================================
# UI Helpers
# ============================================================================

# Tool display config: tool_name -> (emoji, display_title, is_long_running)
TOOL_DISPLAY_CONFIG = {
    "analyze_potential": ("🔬", "Analyzing", False),
    "plot_potential": ("📊", "Plotting", False),
    "search_encyclopedia": ("📚", "Encyclopedia", False),
    "search_potential": ("🧬", "Symbolic Regression", True),
}


def _format_tool_info(tool_name: str, args: dict) -> dict:
    """Format tool info for UI display."""
    if tool_name == "delegate_task_to_member":
        member_name = args.get("member_id", "member").replace("-", " ").title()
        return {
            "tool_name": tool_name,
            "title": f"🤝 Delegate to {member_name}",
            "log": "",
        }

    emoji, title, long_running = TOOL_DISPLAY_CONFIG.get(tool_name, ("🔧", tool_name, False))
    result = {"tool_name": tool_name, "title": f"{emoji} {title}", "log": ""}
    if long_running:
        result["long_running"] = True
    return result


def _extract_sr_config(config_json_str: str) -> dict:
    """Extract key SR config info for display."""
    try:
        config = json.loads(config_json_str)
        iterations = config.get("niterations", 40)
        return {
            "ns_target": config.get("ns_target", 0.9649),
            "ns_sigma": config.get("ns_sigma", 0.0042),
            "r_target": config.get("r_target", 0.0),
            "r_sigma": config.get("r_sigma", 0.014),
            "N_obs": config.get("N_obs", 60.0),
            "operators": config.get("binary_operators", []) + config.get("unary_operators", []),
            "iterations": iterations,
            "populations": config.get("populations", 31),
            "estimated_time": f"~{iterations // 10} min",
        }
    except (json.JSONDecodeError, TypeError):
        return {}


# ============================================================================
# DeepInflation Agent
# ============================================================================


class DeepInflation:
    """Inflation cosmology research agent with conversation management.

    Manages Agno Team, RAG system, session state, and streaming interface.
    """

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str = "gpt-5.2",
        embedding_model: str = "text-embedding-3-small",
        temperature: float = 1.0,
        verbose: bool = True,
    ):
        self._api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self._api_key:
            raise ValueError("API key required. Set OPENAI_API_KEY or pass api_key.")
        self._base_url = base_url or os.getenv("BASE_URL")
        self.verbose = verbose

        self._model = OpenAILike(
            id=model,
            api_key=self._api_key,
            base_url=self._base_url,
            temperature=temperature,
        )

        # Set verbose flag for submodules
        from . import encyclopedia_rag as rag_module
        from . import sr_search as sr_module
        from . import tools as tools_module

        tools_module.VERBOSE = rag_module.VERBOSE = sr_module.VERBOSE = verbose

        # Initialize Encyclopedia RAG (singleton)
        init_rag(
            api_key=self._api_key,
            base_url=self._base_url,
            embedding_model=embedding_model,
        )

        self._db = SqliteDb(
            db_file="tmp/agent_storage.db",
            session_table="inflation_agent_sessions",
        )

        if verbose:
            print(f"[Agent] Initializing with model={model}, base_url={self._base_url or 'default'}")

        # Session state
        self.session_id = str(uuid4())
        self.last_plot_path: str | None = None
        self.team = self._create_team()

    def _create_team(self) -> Team:
        """Create Agno Team with SR sub-agent."""
        sr_agent = Agent(
            name="SR Agent",
            model=self._model,
            role="Configure and run symbolic regression for inflation potentials",
            instructions=SR_AGENT_PROMPT,
            tools=[search_potential],
            add_history_to_context=True,
            num_history_runs=3,
            markdown=True,
        )
        return Team(
            name="Inflation Research Team",
            model=self._model,
            members=[sr_agent],
            tools=[analyze_potential, plot_potential, search_encyclopedia],
            instructions=MAIN_AGENT_PROMPT,
            show_members_responses=True,
            markdown=True,
            db=self._db,
            add_history_to_context=True,
            num_history_runs=5,
        )

    async def stream(self, question: str):
        """Async streaming interface for Gradio.

        Yields:
            {"type": "tool_start", "call_id": str, "info": dict, "args": dict}
            {"type": "tool_end", "call_id": str, "duration": float}
            {"type": "sr_config", "config": dict}
            {"type": "text_delta", "delta": str}
            {"type": "response", "content": str, "plot_path": str|None}
        """
        self.last_plot_path = None
        pending_tools = {}  # call_id -> (tool_name, info, args, start_time)
        accumulated_text = ""

        try:
            async for event in self.team.arun(
                input=question,
                stream=True,
                stream_events=True,
                session_id=self.session_id,
            ):
                # Tool call started (Team or Member)
                if event.event in (
                    TeamRunEvent.tool_call_started,
                    RunEvent.tool_call_started,
                ):
                    tool_name = event.tool.tool_name
                    tool_args = event.tool.tool_args or {}
                    is_member = event.event == RunEvent.tool_call_started

                    if self.verbose:
                        prefix = "[Member Tool]" if is_member else "[Tool]"
                        args_str = str(tool_args)[:500]
                        print(f"{prefix} {tool_name}\n  Input: {args_str}{'...' if len(str(tool_args)) > 500 else ''}")

                    info = _format_tool_info(tool_name, tool_args)
                    call_id = f"{'member' if is_member else 'team'}_{tool_name}_{time.time()}"
                    pending_tools[call_id] = (tool_name, info, tool_args, time.time())
                    yield {
                        "type": "tool_start",
                        "call_id": call_id,
                        "info": info,
                        "args": tool_args,
                    }

                    # SR config display (member only)
                    if is_member and tool_name == "search_potential":
                        sr_config = _extract_sr_config(tool_args.get("config_json", "{}"))
                        if sr_config:
                            yield {"type": "sr_config", "config": sr_config}

                # Tool call completed (Team or Member)
                elif event.event in (
                    TeamRunEvent.tool_call_completed,
                    RunEvent.tool_call_completed,
                ):
                    tool_name = event.tool.tool_name
                    result = event.tool.result
                    is_member = event.event == RunEvent.tool_call_completed

                    # Parse success from JSON result
                    success = True
                    try:
                        output = json.loads(result) if isinstance(result, str) else result
                        if isinstance(output, dict):
                            success = output.get("success", True)
                    except (json.JSONDecodeError, TypeError):
                        output = None

                    # Find and pop matching pending tool
                    call_id = next(
                        (cid for cid, (name, *_) in pending_tools.items() if name == tool_name),
                        None,
                    )
                    if call_id:
                        _, _, _, start_time = pending_tools.pop(call_id)
                        duration = time.time() - start_time

                        if self.verbose:
                            prefix = "[Member Tool]" if is_member else "[Tool]"
                            output_str = str(result)[:2000] if result else ""
                            print(
                                f"{prefix} {tool_name} {'✓' if success else '✗'} ({duration:.1f}s)\n  Output: {output_str}{'...' if len(str(result)) > 2000 else ''}"
                            )

                        yield {
                            "type": "tool_end",
                            "call_id": call_id,
                            "duration": duration,
                            "success": success,
                        }

                        # Extract plot path on success
                        if tool_name == "plot_potential" and isinstance(output, dict) and output.get("success"):
                            path = output.get("plot_path")
                            if path and os.path.exists(path):
                                self.last_plot_path = path

                # Content streaming
                elif event.event == TeamRunEvent.run_content:
                    if event.content:
                        accumulated_text += event.content
                        yield {"type": "text_delta", "delta": event.content}

            yield {
                "type": "response",
                "content": accumulated_text,
                "plot_path": self.last_plot_path,
            }

        except Exception as e:
            if self.verbose:
                print(f"[Agent] Error: {e}")
                import traceback

                traceback.print_exc()
            yield {"type": "response", "content": f"Error: {e}", "plot_path": None}

    def run(self, question: str) -> str:
        """Synchronous interface - returns final response only."""
        import asyncio

        async def get_response():
            async for event in self.stream(question):
                if event["type"] == "response":
                    return event["content"]
            return ""

        return asyncio.run(get_response())

    def clear_history(self):
        """Clear conversation history by creating new session."""
        self.session_id = str(uuid4())
        self.last_plot_path = None
        if self.verbose:
            print("[Agent] History cleared (new session)")


# ============================================================================
# CLI Interface
# ============================================================================

if __name__ == "__main__":
    import asyncio

    from dotenv import load_dotenv

    load_dotenv()

    print("=" * 60)
    print("DeepInflation")
    print("=" * 60)
    print("\nExamples:")
    print("  • What is ns for V = phi^2?")
    print("  • Plot the Starobinsky model: (1 - exp(-sqrt(2/3)*phi))^2")
    print("  • Find a plateau potential with r < 0.01")
    print("\nType 'quit' to exit, 'clear' to reset conversation\n")

    async def main():
        agent = DeepInflation(verbose=False)
        pending_tools = {}  # call_id -> title

        while True:
            try:
                question = input("> ").strip()
                if not question:
                    continue
                if question.lower() in ("quit", "exit", "q"):
                    print("Goodbye!")
                    break
                if question.lower() == "clear":
                    agent.clear_history()
                    pending_tools.clear()
                    continue

                print("\n⏳ Thinking...")

                async for event in agent.stream(question):
                    if event["type"] == "tool_start":
                        info = event["info"]
                        call_id = event["call_id"]
                        title = info.get("title", "Tool")
                        log = info.get("log", "")
                        pending_tools[call_id] = title
                        print(f"  {title} {log}..." if log else f"  {title}...")
                    elif event["type"] == "sr_config":
                        config = event["config"]
                        print(
                            f"    Config: ns={config.get('ns_target')}±{config.get('ns_sigma')}, "
                            f"r={config.get('r_target')}±{config.get('r_sigma')}"
                        )
                        print(f"    Ops: {config.get('operators')}")
                        print(f"    Est: {config.get('estimated_time')}")
                    elif event["type"] == "tool_end":
                        call_id = event["call_id"]
                        duration = event.get("duration", 0)
                        title = pending_tools.pop(call_id, "Tool")
                        print(f"  {title} ✓ ({duration:.1f}s)")
                    elif event["type"] == "response":
                        print(f"\n{event['content']}\n")

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}\n")

    try:
        asyncio.run(main())
    except Exception as e:
        print(f"✗ Failed to initialize: {e}")
        import sys

        sys.exit(1)
