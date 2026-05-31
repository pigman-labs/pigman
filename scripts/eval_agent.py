from __future__ import annotations

from evals.world_model_prediction import smoke_eval
from evals.agent_eval import run_agent_eval
from pathlib import Path

from evals.affect_eval import run_affect_eval
from evals.memory_eval import run_memory_eval
from evals.multi_agent_eval import run_multi_agent_eval
from evals.neural_eval import evaluate_checkpoint
from evals.planner_eval import run_planner_eval
from evals.tool_eval import run_tool_eval
from evals.verifier_eval import run_verifier_eval
from safety_frontier.evals import FrontierSafetySuite


def main() -> None:
    neural = None
    if Path("artifacts/checkpoints/neural_jepa.npz").exists():
        neural = evaluate_checkpoint()
    report = {
        "world_model": smoke_eval(),
        "affect": run_affect_eval(),
        "agent": run_agent_eval(),
        "multi_agent": run_multi_agent_eval(),
        "neural": neural,
        "planner": run_planner_eval(),
        "memory": run_memory_eval(),
        "tools": run_tool_eval(),
        "verifiers": run_verifier_eval(),
        "safety_frontier": FrontierSafetySuite().run(),
    }
    Path("artifacts/evals").mkdir(parents=True, exist_ok=True)
    Path("artifacts/evals/latest.json").write_text(str(report), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
