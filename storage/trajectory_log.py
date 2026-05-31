from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path


@dataclass
class TrajectoryLog:
    events: list[dict] = field(default_factory=list)

    def append(self, event: dict) -> None:
        self.events.append(event)

    def write_jsonl(self, path: str) -> None:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("w", encoding="utf-8") as handle:
            for event in self.events:
                handle.write(json.dumps(event, default=str) + "\n")
