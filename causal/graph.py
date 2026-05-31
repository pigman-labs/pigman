from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class CausalEdge:
    source: str
    target: str
    relation: str
    confidence: float


@dataclass
class CausalGraph:
    nodes: set[str] = field(default_factory=set)
    edges: list[CausalEdge] = field(default_factory=list)

    def add_edge(self, source: str, target: str, relation: str, confidence: float) -> None:
        self.nodes.update({source, target})
        self.edges.append(CausalEdge(source, target, relation, confidence))

    def effects_of(self, source: str) -> list[CausalEdge]:
        return [edge for edge in self.edges if edge.source == source]

    def causes_of(self, target: str) -> list[CausalEdge]:
        return [edge for edge in self.edges if edge.target == target]
