"""Inflation Research Agent - Agno Framework Implementation"""

import json
import os
import time
from typing import Optional
from uuid import uuid4

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai.like import OpenAILike
from agno.run.agent import RunEvent
from agno.run.team import TeamRunEvent
from agno.team import Team

from encyclopedia_rag import EncyclopediaRAG
from tools import analyze_potential, plot_potential
from sr_search import search_potential


# ============================================================================
# System Prompts
# ============================================================================

MAIN_AGENT_PROMPT = r"""You are an expert inflation cosmology assistant specialized in analyzing inflation potentials and discovering models via symbolic regression. Use tools or sub-agents to gather data, then provide clear answers.

# WORKFLOW (ReAct Pattern)
1. **Thought**: What information is needed?
2. **Action**: Call appropriate tool(s) or delegate to sub-agent
3. **Observation**: Examine results
4. Repeat until ready to answer

# DELEGATION

## SR Agent
**PRIMARY METHOD** of this agent team. Used for discovering potentials matching target observables or physics constraints via symbolic regression. (slow, 1-5 min).
**Delegate when**: User asks to find/discover potential, or wants models compatible with observational data.
**Input**: the task based on user's request (target observables, potential characteristics, constraints and time budget).
**Output**: Config summary and ranked candidates with expressions and predictions.

# TOOLS

## analyze_potential(expression)
Compute inflation observables (ns, r, A_s) for all valid trajectories of V(φ).
**Expression format**: Only 'phi' variable + numeric values (e.g., 'phi^2', '(1-exp(-0.816*phi))^2')
**Invalid**: Symbolic parameters like 'M*phi^2', 'V0*phi^2'

## plot_potential(expression, output_path)
Generate 3-panel diagnostic plot: V(φ) with trajectories | ε,η vs φ | ns-r vs Planck+BK18
**Expression format**: Same as analyze_potential
**Returns**: Absolute file path

## search_knowledge_base (built-in)
Search Encyclopædia Inflationaris using hybrid retrieval (semantic + keyword).
**Use for**: Model names, physics concepts, theory background, potential expressions
**NOT for**: Finding models from observables (delegate to SR Agent instead)
**NOTE**: Only quiry with English text (No LaTeX, code, or math symbols)

# OUTPUT PRINCIPLES
- Focus on answering the user's question.
- The final answer should be concise and relevant.
- Use proper Markdown commands with $...$ for math.
- Always base the final answer on tool results, not assumptions. Do not invent data.
- For PLOTTING, provide file path to saved image.
"""

SR_AGENT_PROMPT = r"""You are a symbolic regression expert for inflation cosmology.
As a sub-agent, you should run the `search_potential` tool based on the main agent's delegation.
Note that you should run the `search_potential` tool once at a time, and return the config summary and results imediately unless instructed otherwise.

# YOUR TASK
1. **Interpret** the user's intent → extract observable targets and constraints
2. **Configure** PySR search parameters based on the guide below
3. **Run** search_potential with your configuration
4. **Return** both the config summary and the search results

# SYMBOLIC REGRESSION (PYSR) CONFIG

Construct `config_json` based on user's physics goals and computational budget.

## Physics Targets
The scalar spectral index (ns), the tensor-to-scalar ratio (r), and number of e-folds (N_obs) to guide the search.
**ns_target**, **ns_sigma**, **r_target**, **r_sigma**, **N_obs** 
- Defaults: ns=0.9649±0.0042, r=0.0±0.014, N_obs=60
- set r_target = 0 if no detection of tensor modes is desired
- Adjust sigma to control tolerance (widen for exploration, tighten for precision)

## Operator Selection (defines search space)

Choose operators based on expected physics. Each additional operator increases search complexity.

**binary_operators** (must provide): Available `["+", "-", "*", "/", "^"]`
**unary_operators** (default `[]`): Available `["exp", "log", "sqrt", "sin", "cos", "square", "cube", "neg", "tanh]`

**Selection strategy**: Start simple, add complexity only as needed
- Always include ["+", "*"] for basic forms
- Include either `^` or ['square', 'cube'] for polynomial terms (not both)
- Be cautious with "/", "tanh", "sin", "cos", include only if necessary

## Complexity Control (guides search efficiency and interpretability)

**maxsize**: Expression tree size limit (typical: 12-30)
- Lower → simpler, faster; Higher → more expressive

**constraints**: `{operator: [arg1_max, arg2_max]}` or `{operator: max_complexity}` (use -1 for no limit)
- **Use JSON array syntax `[a, b]` for tuple constraints** (automatically converted to tuples)
- Example: `{"^": [-1, 1]}` limits exponent to constants, prevents `phi^(exp(x))`
- Example: `{"/": [-1, 3]}` allows any complexity numerator, max 3 denominator
- Use to avoid pathological forms (variable exponents, deep fractions)

**nested_constraints**: `{outer_op: {inner_op: max_depth}}`
- Example: `{"exp": {"exp": 0}}` prevents `exp(exp(x))`
- Example: `{"exp": {"log": 0}}` prevents `exp(log(x))`
- Use to forbid unphysical compositions

**complexity_of_operators**: `{operator: cost}` (default: 1 for all)
- Example: `{"exp": 3, "^": 2}` biases toward polynomials
- Use to prefer simpler functional forms

### Configuration Principles

- Constraints must only reference operators you included in binary_operators/unary_operators.
- Always constrain `^` exponents: `{"^": [-1, 1]}` when using `^`; Always constrain `/` denominators when using `/`: `{"/": [-1, 3]}`
- Always limit nested complex ops, e.g. `{"exp": {"exp": 0}}`; Always prevent inappropriate nesting (e.g. `{"exp": {"log": 0}}`)

## Evolution Parameters (controls search effort)

**populations**: Parallel search populations (typical: 15-50, default: 31)
**niterations**: Evolution cycles (typical: 20-60, default: 40)
**population_size**: Individuals per population (default: 27, usually sufficient)

Adjust based on time budget: quick (<1min), balanced (1-3min), thorough (5-10min)

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
This is just an example. Adapt operators/constraints/targets to actual physics requirements. (Do not copy blindly.)

# SR RESULT POST-PROCESSING

When `search_potential` returns multiple candidates:
- Select top 3-10: Prioritize lowest loss + interpretability + structural diversity.
- Simplify: Round coefficients, apply algebraic simplification (conservatively), identify duplicates
- Present the final results as described below.

# OUTPUT FORMAT

Return in this format:
```
**Search Config**: ns={ns_target}±{ns_sigma}, r={r_target}±{r_sigma}, N_obs={N_obs}, ... [operators, constraints summary]

**Results**:
{search_potential output}
```
"""


# ============================================================================
# UI Helpers
# ============================================================================

# Tool display config: tool_name -> (emoji, display_title, is_long_running)
TOOL_DISPLAY_CONFIG = {
    "analyze_potential": ("🔬", "Analyzing", False),
    "plot_potential": ("📊", "Plotting", False),
    "search_knowledge_base": ("📚", "Encyclopedia", False),
    "search_potential": ("🧬", "Symbolic Regression", True),
}


def _format_tool_info(tool_name: str, args: dict) -> dict:
    """Format tool info for UI display."""
    if tool_name == "delegate_task_to_member":
        member_name = args.get("member_id", "member").replace("-", " ").title()
        return {"tool_name": tool_name, "title": f"🤝 Delegate to {member_name}", "log": ""}

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
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
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
        self._rag = EncyclopediaRAG(
            api_key=self._api_key,
            base_url=self._base_url,
            embedding_model=embedding_model
        )
        self._db = SqliteDb(
            db_file="tmp/agent_storage.db",
            session_table="inflation_agent_sessions",
        )

        # Set verbose flag for submodules
        import encyclopedia_rag
        import tools as tools_module
        tools_module.VERBOSE = encyclopedia_rag.VERBOSE = verbose

        if verbose:
            print(f"[Agent] Initializing with model={model}, base_url={self._base_url or 'default'}")

        # Session state
        self.session_id = str(uuid4())
        self.last_plot_path: Optional[str] = None
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
            tools=[analyze_potential, plot_potential],
            instructions=MAIN_AGENT_PROMPT,
            show_members_responses=True,
            markdown=True,
            db=self._db,
            add_history_to_context=True,
            num_history_runs=5,
            knowledge=self._rag.knowledge,
            search_knowledge=True,
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
                if event.event in (TeamRunEvent.tool_call_started, RunEvent.tool_call_started):
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
                    yield {"type": "tool_start", "call_id": call_id, "info": info, "args": tool_args}

                    # SR config display (member only)
                    if is_member and tool_name == "search_potential":
                        sr_config = _extract_sr_config(tool_args.get("config_json", "{}"))
                        if sr_config:
                            yield {"type": "sr_config", "config": sr_config}

                # Tool call completed (Team or Member)
                elif event.event in (TeamRunEvent.tool_call_completed, RunEvent.tool_call_completed):
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
                    call_id = next((cid for cid, (name, *_) in pending_tools.items() if name == tool_name), None)
                    if call_id:
                        _, _, _, start_time = pending_tools.pop(call_id)
                        duration = time.time() - start_time

                        if self.verbose:
                            prefix = "[Member Tool]" if is_member else "[Tool]"
                            output_str = str(result)[:500] if result else ""
                            print(f"{prefix} {tool_name} {'✓' if success else '✗'} ({duration:.1f}s)\n  Output: {output_str}{'...' if len(str(result)) > 500 else ''}")

                        yield {"type": "tool_end", "call_id": call_id, "duration": duration, "success": success}

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

            yield {"type": "response", "content": accumulated_text, "plot_path": self.last_plot_path}

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
                        print(f"    Config: ns={config.get('ns_target')}±{config.get('ns_sigma')}, "
                              f"r={config.get('r_target')}±{config.get('r_sigma')}")
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
