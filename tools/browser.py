from __future__ import annotations

from dataclasses import dataclass
from time import time

from tools.results import ToolResult


@dataclass(frozen=True)
class BrowserAction:
    type: str
    selector: str | None = None
    text: str | None = None
    url: str | None = None


class BrowserTool:
    def execute(self, action: BrowserAction) -> dict:
        return {"ok": True, "action": action.__dict__, "note": "schema-compatible browser stub"}

    def execute_structured(self, action: BrowserAction) -> ToolResult:
        started = time()
        result = self.execute(action)
        return ToolResult(
            ok=bool(result["ok"]),
            tool="browser",
            operation=action.type,
            data=result,
            started_at=started,
            ended_at=time(),
        )
