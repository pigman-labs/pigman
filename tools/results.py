from __future__ import annotations

from dataclasses import dataclass, field
from time import time
from typing import Any


@dataclass(frozen=True)
class RollbackRecord:
    kind: str
    target: str
    before: str | None = None
    after: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ToolResult:
    ok: bool
    tool: str
    operation: str
    stdout: str = ""
    stderr: str = ""
    data: dict[str, Any] = field(default_factory=dict)
    rollback: RollbackRecord | None = None
    started_at: float = field(default_factory=time)
    ended_at: float = field(default_factory=time)

    @property
    def duration_ms(self) -> float:
        return max(0.0, (self.ended_at - self.started_at) * 1000.0)

    def to_metadata(self) -> dict[str, Any]:
        return {
            "tool": self.tool,
            "operation": self.operation,
            "ok": self.ok,
            "duration_ms": self.duration_ms,
            "data": self.data,
            "rollback": None if self.rollback is None else self.rollback.__dict__,
        }
