from __future__ import annotations

from state.action import AgentAction


class RiskModel:
    def score(self, action: AgentAction) -> float:
        if action.type in {"run_shell", "edit_file", "api_call"}:
            return max(action.risk_score, 0.25)
        return action.risk_score
