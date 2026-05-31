from __future__ import annotations

from collections.abc import Callable
from typing import Any, TypeVar


T = TypeVar("T")


class Registry:
    def __init__(self) -> None:
        self._items: dict[str, Any] = {}

    def register(self, name: str) -> Callable[[T], T]:
        def decorator(item: T) -> T:
            if name in self._items:
                raise KeyError(f"{name!r} is already registered")
            self._items[name] = item
            return item

        return decorator

    def get(self, name: str) -> Any:
        try:
            return self._items[name]
        except KeyError as exc:
            available = ", ".join(sorted(self._items)) or "<empty>"
            raise KeyError(f"Unknown registry item {name!r}. Available: {available}") from exc

    def names(self) -> list[str]:
        return sorted(self._items)


ENCODERS = Registry()
PLANNERS = Registry()
DECODERS = Registry()
VERIFIERS = Registry()

