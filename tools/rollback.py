from __future__ import annotations

from pathlib import Path

from tools.results import RollbackRecord


class RollbackManager:
    def apply(self, record: RollbackRecord) -> dict:
        if record.kind == "file_write":
            target = Path(record.target)
            if record.before is None:
                if target.exists():
                    target.unlink()
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(record.before, encoding="utf-8")
            return {"ok": True, "kind": record.kind, "target": record.target}
        if record.kind == "replace_text":
            target = Path(record.target)
            current = target.read_text(encoding="utf-8")
            if record.after is not None and record.after in current:
                target.write_text(current.replace(record.after, record.before or "", 1), encoding="utf-8")
                return {"ok": True, "kind": record.kind, "target": record.target}
            return {"ok": False, "reason": "rollback text not found", "target": record.target}
        return {"ok": False, "reason": f"unsupported rollback kind: {record.kind}"}
