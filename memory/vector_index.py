from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path

from kernels.vector_math import cosine_similarity


@dataclass
class VectorRecord:
    id: str
    vector: tuple[float, ...]
    payload: dict


@dataclass
class InMemoryVectorIndex:
    records: list[VectorRecord] = field(default_factory=list)

    def add(self, record: VectorRecord) -> None:
        self.records.append(record)

    def search(self, _query: tuple[float, ...], limit: int = 5) -> list[VectorRecord]:
        query = list(_query)
        scored = sorted(
            self.records,
            key=lambda record: cosine_similarity(list(record.vector), query),
            reverse=True,
        )
        return scored[:limit]


class PersistentVectorIndex(InMemoryVectorIndex):
    def __init__(self, path: str = "artifacts/memory/vector_index.json") -> None:
        super().__init__()
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.load()

    def add(self, record: VectorRecord) -> None:
        self.records = [item for item in self.records if item.id != record.id]
        super().add(record)
        self.save()

    def save(self) -> None:
        rows = [
            {"id": record.id, "vector": list(record.vector), "payload": record.payload}
            for record in self.records
        ]
        self.path.write_text(json.dumps(rows, sort_keys=True), encoding="utf-8")

    def load(self) -> None:
        if not self.path.exists():
            return
        rows = json.loads(self.path.read_text(encoding="utf-8") or "[]")
        self.records = [
            VectorRecord(str(row["id"]), tuple(float(item) for item in row["vector"]), dict(row["payload"]))
            for row in rows
        ]
