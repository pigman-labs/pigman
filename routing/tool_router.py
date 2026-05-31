from __future__ import annotations


class ToolRouter:
    def route(self, action_type: str) -> str:
        mapping = {
            "run_shell": "shell",
            "edit_file": "filesystem",
            "click": "browser",
            "api_call": "api",
            "simulate": "simulator",
        }
        return mapping.get(action_type, "noop")

