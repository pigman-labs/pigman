from __future__ import annotations

from dataclasses import dataclass, field
from time import time


@dataclass(frozen=True)
class SemanticFact:
    key: str
    value: str
    importance: float = 0.5
    confidence: float = 1.0
    source: str = "local"
    updated_at: float = 0.0

    def score(self, query: str = "") -> float:
        lowered = query.lower()
        text_match = 1.0 if lowered and (lowered in self.key.lower() or lowered in self.value.lower()) else 0.0
        recency = 0.1 if self.updated_at else 0.0
        return self.importance * 0.5 + self.confidence * 0.3 + text_match + recency


@dataclass
class SemanticMemory:
    facts: dict[str, SemanticFact] = field(default_factory=dict)

    def upsert(
        self,
        key: str,
        value: str,
        importance: float = 0.5,
        confidence: float = 1.0,
        source: str = "local",
    ) -> SemanticFact:
        fact = SemanticFact(key, value, importance, confidence, source, time())
        self.facts[key] = fact
        return fact

    def retrieve(self, query: str, limit: int = 10) -> dict[str, str]:
        lowered = query.lower()
        terms = {term for term in lowered.split() if term}
        matches = [
            fact
            for fact in self.facts.values()
            if not terms
            or any(term in fact.key.lower() or term in fact.value.lower() for term in terms)
        ]
        matches.sort(key=lambda fact: fact.score(query), reverse=True)
        return {fact.key: fact.value for fact in matches[:limit]}

    def contradictions(self, key: str, proposed_value: str) -> list[SemanticFact]:
        existing = self.facts.get(key)
        if existing is None:
            return []
        if existing.value.strip().lower() == proposed_value.strip().lower():
            return []
        return [existing]
