from __future__ import annotations

from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any

from multi_agent.runtime import MultiAgentRuntime


def _jsonable(value: Any) -> Any:
    if is_dataclass(value):
        return _jsonable(asdict(value))
    if isinstance(value, dict):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(item) for item in value]
    if hasattr(value, "__dict__"):
        return _jsonable(value.__dict__)
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def run_multi_agent_eval() -> dict:
    runtime = MultiAgentRuntime()
    result = runtime.run("architecture digest for the current world model")
    state = result.shared_state
    execution = state.get("execution")
    verification = state.get("verification")
    votes = state.get("votes", [])
    report = {
        "ok": bool(result.ok),
        "trace_id": result.trace_id,
        "messages": result.messages,
        "agents": sorted(result.agent_results.keys()),
        "has_plan": state.get("plan") is not None,
        "has_action": state.get("action") is not None,
        "has_prediction": state.get("prediction") is not None,
        "has_affect": state.get("affect") is not None,
        "execution_success": bool(getattr(execution, "success", False)),
        "execution_source": getattr(getattr(execution, "observation", None), "source", None),
        "verification_approved": bool(getattr(verification, "approved", False)),
        "vote_count": len(votes),
        "artifact_exists": Path("artifacts/architecture_digest.txt").exists(),
        "coordinator_summary": _jsonable(state.get("coordinator_summary", {})),
    }
    return report
