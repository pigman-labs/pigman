from __future__ import annotations

from pathlib import Path
from time import time

from tools.results import RollbackRecord, ToolResult


class PatchTool:
    def apply_replace(self, path: str, old: str, new: str) -> dict:
        target = Path(path)
        original = target.read_text(encoding="utf-8")
        if old not in original:
            return {"ok": False, "reason": "old text not found"}
        target.write_text(original.replace(old, new, 1), encoding="utf-8")
        return {"ok": True, "rollback": {"path": path, "old": new, "new": old}}

    def apply_replace_structured(self, path: str, old: str, new: str) -> ToolResult:
        started = time()
        target = Path(path)
        original = target.read_text(encoding="utf-8")
        if old not in original:
            return ToolResult(
                ok=False,
                tool="patch",
                operation="replace",
                stderr="old text not found",
                data={"path": path},
                started_at=started,
                ended_at=time(),
            )
        updated = original.replace(old, new, 1)
        target.write_text(updated, encoding="utf-8")
        return ToolResult(
            ok=True,
            tool="patch",
            operation="replace",
            data={"path": path, "old": old, "new": new},
            rollback=RollbackRecord("replace_text", path, before=old, after=new),
            started_at=started,
            ended_at=time(),
        )
