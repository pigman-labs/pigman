from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from dataset_engine.quality import Deduplicator, QualityScorer
from dataset_engine.records import DatasetManifest, DatasetRecord


class JsonlDatasetStore:
    def __init__(self, root: str = "artifacts/datasets") -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.scorer = QualityScorer()
        self.dedup = Deduplicator()

    def ingest(self, name: str, version: str, records: list[DatasetRecord], min_quality: float = 0.0) -> DatasetManifest:
        accepted: list[DatasetRecord] = []
        for record in records:
            scored = DatasetRecord(
                source=record.source,
                split=record.split,
                payload=record.payload,
                license=record.license,
                quality=self.scorer.score(record),
                created_at=record.created_at,
            )
            if scored.quality >= min_quality and self.dedup.accept(scored):
                accepted.append(scored)

        path = self.root / name / version
        path.mkdir(parents=True, exist_ok=True)
        data_path = path / "data.jsonl"
        with data_path.open("w", encoding="utf-8") as handle:
            for record in accepted:
                handle.write(json.dumps(record.__dict__, default=str) + "\n")

        sources = Counter(record.source for record in accepted)
        licenses = Counter(record.license for record in accepted)
        manifest = DatasetManifest(name, version, len(accepted), dict(sources), dict(licenses))
        (path / "manifest.json").write_text(json.dumps(manifest.__dict__, indent=2), encoding="utf-8")
        return manifest

    def stream(self, name: str, version: str):
        data_path = self.root / name / version / "data.jsonl"
        with data_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                yield json.loads(line)

