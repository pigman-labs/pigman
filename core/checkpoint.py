from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class CheckpointRef:
    path: Path
    step: int | None = None
    metrics: dict[str, float] | None = None


def checkpoint_path(root: str | Path, name: str, step: int) -> Path:
    return Path(root) / name / f"step_{step:09d}"


def save_metadata(path: str | Path, metadata: dict[str, Any]) -> None:
    target = Path(path)
    target.mkdir(parents=True, exist_ok=True)
    (target / "metadata.json").write_text(str(metadata), encoding="utf-8")

