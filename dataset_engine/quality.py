from __future__ import annotations

from dataset_engine.records import DatasetRecord


class QualityScorer:
    def score(self, record: DatasetRecord) -> float:
        payload_text = str(record.payload)
        score = 0.2
        if len(payload_text) > 20:
            score += 0.25
        if any(key in record.payload for key in ("state", "action", "next_state", "goal", "result")):
            score += 0.35
        if record.license not in {"unknown", "restricted"}:
            score += 0.2
        return min(1.0, score)


class Deduplicator:
    def __init__(self) -> None:
        self.seen: set[str] = set()

    def accept(self, record: DatasetRecord) -> bool:
        if record.id in self.seen:
            return False
        self.seen.add(record.id)
        return True

