from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import blake2b
from time import time


@dataclass(frozen=True)
class DatasetRecord:
    source: str
    split: str
    payload: dict
    license: str = "unknown"
    quality: float = 0.5
    created_at: float = field(default_factory=time)

    @property
    def id(self) -> str:
        digest = blake2b(str((self.source, self.payload)).encode("utf-8"), digest_size=12).hexdigest()
        return f"{self.source}_{digest}"


@dataclass(frozen=True)
class DatasetManifest:
    name: str
    version: str
    records: int
    sources: dict[str, int]
    licenses: dict[str, int]

