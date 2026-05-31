from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from kernels.vector_math import stable_hash_embedding
from memory.consolidation import ConsolidationReport, MemoryConsolidationEngine
from memory.episodic_memory import EpisodicMemory
from memory.graph_memory import GraphMemory
from memory.persistent import JsonlEpisodicStore, SqliteMemoryStore
from memory.procedural_memory import ProceduralMemory
from memory.scoring import MemoryScorer
from memory.semantic_memory import SemanticMemory
from memory.vector_index import InMemoryVectorIndex, PersistentVectorIndex, VectorRecord


@dataclass
class MemoryBundle:
    facts: dict[str, str] = field(default_factory=dict)
    procedures: list[str] = field(default_factory=list)
    vector_hits: list[dict] = field(default_factory=list)
    recent_episodes: list[str] = field(default_factory=list)
    graph_hits: list[dict] = field(default_factory=list)
    persistent_facts: list[dict] = field(default_factory=list)
    persistent_procedures: list[dict] = field(default_factory=list)
    scores: dict[str, float] = field(default_factory=dict)


class MemorySystem:
    def __init__(self, root: str | None = None, persistent: bool = False) -> None:
        self.root = Path(root or "artifacts/memory")
        self.root.mkdir(parents=True, exist_ok=True)
        self.semantic = SemanticMemory()
        self.procedural = ProceduralMemory()
        self.episodic = EpisodicMemory()
        self.vector = (
            PersistentVectorIndex(str(self.root / "vector_index.json"))
            if persistent
            else InMemoryVectorIndex()
        )
        self.episodes = JsonlEpisodicStore(str(self.root / "episodes.jsonl"))
        self.store = SqliteMemoryStore(str(self.root / "memory.sqlite3"))
        self.graph = GraphMemory(str(self.root / "graph.json"))
        self.scorer = MemoryScorer()
        self.consolidator = MemoryConsolidationEngine(self.store, self.graph)

    def add_trace(self, trace_id: str, text: str, payload: dict) -> None:
        if isinstance(text, bytes):
            text = text.decode("utf-8", errors="replace")
        else:
            text = str(text)
        text = self._truncate(text)
        payload = self._sanitize_payload(payload)
        event = {"trace_id": trace_id, "text": text, **payload}
        self.episodes.append(event)
        self.vector.add(VectorRecord(trace_id, tuple(stable_hash_embedding(text)), event))
        if text:
            self.graph.upsert_node(f"trace:{trace_id}", "trace", text[:120], payload)

    def _truncate(self, text: str, limit: int = 8000) -> str:
        if len(text) <= limit:
            return text
        return text[:limit] + f"\n...[truncated {len(text) - limit} chars]"

    def _sanitize_payload(self, payload: dict, limit: int = 2000) -> dict:
        clean = {}
        for key, value in payload.items():
            if isinstance(value, str):
                clean[key] = self._truncate(value, limit)
            elif isinstance(value, bytes):
                clean[key] = self._truncate(value.decode("utf-8", errors="replace"), limit)
            elif isinstance(value, dict):
                clean[key] = self._sanitize_payload(value, limit)
            elif isinstance(value, list):
                clean[key] = [
                    self._truncate(item, limit) if isinstance(item, str) else item for item in value[:50]
                ]
            else:
                clean[key] = value
        return clean

    def consolidate_trace(self, trace: dict) -> ConsolidationReport:
        self.episodes.append(trace)
        return self.consolidator.consolidate_trace(trace)

    def remember_fact(
        self,
        key: str,
        value: str,
        importance: float = 0.5,
        confidence: float = 1.0,
        source: str = "local",
    ) -> list[dict]:
        contradictions = self.store.detect_contradiction(key, value)
        self.semantic.upsert(key, value, importance, confidence, source)
        self.store.upsert_fact(key, value, importance, confidence, source)
        self.graph.upsert_node(f"fact:{key}", "fact", key, {"value": value, "importance": importance})
        self.vector.add(
            VectorRecord(
                f"fact:{key}",
                tuple(stable_hash_embedding(f"{key} {value}")),
                {"key": key, "value": value, "type": "fact"},
            )
        )
        return contradictions

    def retrieve(self, query: str, limit: int = 5) -> MemoryBundle:
        vector = tuple(stable_hash_embedding(query))
        persistent_facts = self.store.facts(query)[:limit]
        persistent_procedures = self.store.procedures(query)[:limit]
        graph_hits = self.graph.search(query, limit=limit)
        scores = {}
        for fact in persistent_facts:
            score = self.scorer.score(
                query,
                f"{fact.key} {fact.value}",
                fact.importance,
                fact.confidence,
                fact.updated_at,
            )
            scores[f"fact:{fact.key}"] = score.total
        return MemoryBundle(
            facts=self.semantic.retrieve(query),
            procedures=[procedure.name for procedure in self.procedural.match(query)],
            vector_hits=[record.payload for record in self.vector.search(vector, limit=limit)],
            recent_episodes=[episode.summary for episode in self.episodic.recent(limit) if episode.summary],
            graph_hits=[node.__dict__ for node in graph_hits],
            persistent_facts=[fact.__dict__ for fact in persistent_facts],
            persistent_procedures=persistent_procedures,
            scores=scores,
        )
