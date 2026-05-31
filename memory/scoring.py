from __future__ import annotations

from dataclasses import dataclass
from time import time


@dataclass(frozen=True)
class MemoryScore:
    relevance: float
    recency: float
    importance: float
    confidence: float
    total: float


class MemoryScorer:
    def __init__(self, recency_half_life_seconds: float = 86400.0) -> None:
        self.recency_half_life_seconds = recency_half_life_seconds

    def score(
        self,
        query: str,
        text: str,
        importance: float = 0.5,
        confidence: float = 1.0,
        updated_at: float = 0.0,
    ) -> MemoryScore:
        query_terms = {term for term in query.lower().split() if term}
        text_terms = {term for term in text.lower().split() if term}
        relevance = len(query_terms & text_terms) / max(1, len(query_terms))
        age = max(0.0, time() - updated_at) if updated_at else self.recency_half_life_seconds
        recency = 1.0 / (1.0 + age / self.recency_half_life_seconds)
        total = relevance * 0.45 + recency * 0.15 + importance * 0.25 + confidence * 0.15
        return MemoryScore(relevance, recency, importance, confidence, total)
