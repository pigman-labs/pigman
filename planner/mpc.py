from __future__ import annotations

from dynamics.latent_state import BeliefState
from planner.base import Plan, Planner
from state.action import AgentAction
import sys


def _python_command() -> list[str]:
    return [sys.executable, "-m", "pytest"]


class MPCPlanner(Planner):
    def plan(self, belief: BeliefState, goal: dict) -> Plan:
        goal_text = str(goal.get("goal", goal.get("description", ""))).lower()
        if "test" in goal_text or "pytest" in goal_text:
            action = AgentAction(
                type="run_shell",
                payload={"command": _python_command()},
                reversible=True,
                risk_score=0.25,
                expected_effects=["test_results"],
                timeout_seconds=120,
            )
        elif "cargo" in goal_text or "rust" in goal_text:
            action = AgentAction(
                type="run_shell",
                payload={"command": ["cargo", "test"]},
                reversible=True,
                risk_score=0.25,
                expected_effects=["rust_test_results"],
                timeout_seconds=120,
            )
        elif "architecture" in goal_text:
            action = AgentAction(
                type="edit_file",
                payload={
                    "path": "artifacts/architecture_digest.txt",
                    "content": str(belief.current.global_state),
                },
                reversible=True,
                risk_score=0.35,
                expected_effects=["write_architecture_digest"],
            )
        else:
            action = AgentAction(
                type="say",
                payload={"text": "I need more concrete execution criteria for this goal."},
                reversible=True,
                risk_score=0.0,
                verification_required=False,
            )
        return Plan(
            actions=[action],
            score=0.6,
            risk=action.risk_score,
            rationale="MPC selected the lowest-risk concrete next action for the goal.",
            predicted_outcomes=[{"effect": effect} for effect in action.expected_effects],
        )
