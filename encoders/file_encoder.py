from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from encoders.base import Encoder
from kernels.vector_math import stable_hash_embedding


@dataclass(frozen=True)
class FileLatent:
    path: str
    exists: bool
    size_bytes: int
    summary: str
    vector: list[float]


class FileEncoder(Encoder):
    modality = "file"

    def encode(self, observation: str) -> FileLatent:
        path = Path(observation)
        if not path.exists() or not path.is_file():
            return FileLatent(
                path=str(path),
                exists=False,
                size_bytes=0,
                summary="missing file",
                vector=stable_hash_embedding(str(path)),
            )

        content = path.read_text(encoding="utf-8", errors="replace")
        summary = content[:2048]
        return FileLatent(
            path=str(path),
            exists=True,
            size_bytes=path.stat().st_size,
            summary=summary,
            vector=stable_hash_embedding(f"{path}\n{summary}"),
        )
