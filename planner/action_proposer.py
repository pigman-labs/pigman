from __future__ import annotations

from state.action import AgentAction


class ActionProposer:
    def propose(self, goal: dict) -> list[AgentAction]:
        goal_text = str(goal.get("goal", goal)).lower()
        actions = [AgentAction("query_memory", {"query": goal_text}, verification_required=False)]
        if "file" in goal_text or "read" in goal_text:
            actions.append(AgentAction("observe", {"reason": "file_or_context_request"}))
        if "test" in goal_text:
            actions.append(AgentAction("run_shell", {"command": [".venv/bin/python", "-m", "pytest"]}, risk_score=0.25))
        return actions
