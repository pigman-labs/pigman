from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ToolSpec:
    name: str
    operations: tuple[str, ...]
    description: str
    side_effects: bool


class ToolRegistry:
    def __init__(self) -> None:
        self._specs: dict[str, ToolSpec] = {}

    def register(self, spec: ToolSpec) -> None:
        self._specs[spec.name] = spec

    def get(self, name: str) -> ToolSpec:
        return self._specs[name]

    def list(self) -> list[ToolSpec]:
        return [self._specs[name] for name in sorted(self._specs)]

    @classmethod
    def default(cls) -> "ToolRegistry":
        registry = cls()
        registry.register(ToolSpec("shell", ("run", "classify"), "subprocess execution with timeouts", True))
        registry.register(ToolSpec("filesystem", ("read", "write", "list", "diff"), "local file operations", True))
        registry.register(ToolSpec("patch", ("replace", "rollback"), "text patch application", True))
        registry.register(ToolSpec("http", ("request",), "stdlib HTTP request", False))
        registry.register(ToolSpec("browser", ("navigate", "click", "type", "screenshot"), "schema browser stub", True))
        registry.register(ToolSpec("memory", ("retrieve",), "memory retrieval", False))
        registry.register(ToolSpec("text", ("emit",), "text output", False))
        return registry
