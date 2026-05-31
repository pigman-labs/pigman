from __future__ import annotations

from collections.abc import Iterator, MutableMapping
from dataclasses import dataclass, field
from time import time
from typing import Any


@dataclass(frozen=True)
class BlackboardEvent:
    key: str
    operation: str
    timestamp: float
    actor: str = "system"
    value_type: str = "unknown"


class Blackboard(MutableMapping[str, Any]):
    """Mutable shared state with auditable writes.

    It intentionally behaves like a normal dictionary so existing subsystem code
    can keep using `state["key"]` and `state.get("key")`. The extra history is
    for debugging coordination failures and later training execution traces.
    """

    def __init__(self, initial: dict[str, Any] | None = None) -> None:
        self._data: dict[str, Any] = dict(initial or {})
        self._events: list[BlackboardEvent] = []
        for key, value in self._data.items():
            self._events.append(
                BlackboardEvent(key=key, operation="init", timestamp=time(), value_type=type(value).__name__)
            )

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.put(key, value)

    def __delitem__(self, key: str) -> None:
        del self._data[key]
        self._events.append(BlackboardEvent(key=key, operation="delete", timestamp=time()))

    def __iter__(self) -> Iterator[str]:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def put(self, key: str, value: Any, actor: str = "system") -> None:
        operation = "update" if key in self._data else "create"
        self._data[key] = value
        self._events.append(
            BlackboardEvent(
                key=key,
                operation=operation,
                timestamp=time(),
                actor=actor,
                value_type=type(value).__name__,
            )
        )

    def snapshot(self) -> dict[str, Any]:
        return dict(self._data)

    def events(self, key: str | None = None) -> list[BlackboardEvent]:
        if key is None:
            return list(self._events)
        return [event for event in self._events if event.key == key]

    def last_writer(self, key: str) -> str | None:
        events = self.events(key)
        if not events:
            return None
        return events[-1].actor
