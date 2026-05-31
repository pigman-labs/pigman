from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from pathlib import Path
from time import time
from typing import Any


class TraceRecorder:
    def __init__(self, path: str | Path = "artifacts/runs/multi_agent_trace.jsonl") -> None:
        self.path = Path(path)

    def record(self, trace_id: str, event: str, payload: dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        row = {
            "time": time(),
            "trace_id": trace_id,
            "event": event,
            "payload": self._jsonable(payload),
        }
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(row, sort_keys=True) + "\n")

    def _jsonable(self, value: Any) -> Any:
        if is_dataclass(value):
            return self._jsonable(asdict(value))
        if isinstance(value, dict):
            return {str(key): self._jsonable(item) for key, item in value.items()}
        if isinstance(value, (list, tuple)):
            return [self._jsonable(item) for item in value]
        if isinstance(value, (str, int, float, bool)) or value is None:
            return value
        if hasattr(value, "__dict__"):
            return self._jsonable(value.__dict__)
        return str(value)
