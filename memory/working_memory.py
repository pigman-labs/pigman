from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class WorkingMemory:
    items: list[Any] = field(default_factory=list)

    def add(self, item: Any) -> None:
        self.items.append(item)

    def recent(self, limit: int = 8) -> list[Any]:
        return self.items[-limit:]

