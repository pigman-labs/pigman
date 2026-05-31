from __future__ import annotations

from dynamics.latent_state import BeliefState
from planner.base import Plan, Planner
from state.action import AgentAction


class BeamPlanner(Planner):
    def __init__(self, width: int = 3) -> None:
        self.width = width

    def plan(self, belief: BeliefState, goal: dict) -> Plan:
        goal_text = str(goal.get("goal", goal)).lower()
        candidates = [
            AgentAction("query_memory", {"query": goal_text}, risk_score=0.0, verification_required=False),
            AgentAction("observe", {"reason": "collect_more_context"}, risk_score=0.0, verification_required=False),
            AgentAction("say", {"text": f"Current belief has {len(belief.current.events)} events."}, risk_score=0.0),
        ][: self.width]
        return Plan(
            actions=candidates,
            score=0.4,
            risk=max(action.risk_score for action in candidates),
            rationale="Beam planner produced low-risk exploratory candidates.",
        )
