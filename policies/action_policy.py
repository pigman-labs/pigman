from __future__ import annotations

from planner.base import Plan
from state.action import AgentAction


class ActionPolicy:
    def select_next(self, plan: Plan) -> AgentAction:
        if not plan.actions:
            return AgentAction("ask_user", {"question": "No viable action found"}, risk_score=0.0)
        return sorted(plan.actions, key=lambda action: (action.risk_score, action.type))[0]
