from __future__ import annotations

from dataclasses import dataclass

from state.action import AgentAction


@dataclass(frozen=True)
class ToolCall:
    name: str
    args: dict
    permission_level: str = "safe"


class ToolDecoder:
    def decode(self, action: AgentAction) -> ToolCall:
        mapping = {
            "run_shell": "shell",
            "edit_file": "filesystem",
            "query_memory": "memory",
            "observe": "observe",
            "say": "text",
        }
        args = dict(action.payload)
        if action.type == "run_shell":
            args.setdefault("timeout", action.timeout_seconds)
        return ToolCall(
            name=mapping.get(action.type, action.type),
            args=args,
            permission_level="safe" if action.risk_score < 0.2 else "medium",
        )
