from __future__ import annotations


def classify_risk(action: dict) -> str:
    action_type = str(action.get("type", ""))
    if action_type in {"delete", "deploy", "purchase"}:
        return "high"
    if action_type in {"edit_file", "run_shell", "api_call"}:
        return "medium"
    return "low"

