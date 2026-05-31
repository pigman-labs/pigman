from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from time import time


@dataclass(frozen=True)
class MemoryNode:
    id: str
    kind: str
    label: str
    properties: dict
    updated_at: float


@dataclass(frozen=True)
class MemoryEdge:
    source: str
    target: str
    relation: str
    weight: float
    updated_at: float


class GraphMemory:
    def __init__(self, path: str = "artifacts/memory/graph.json") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.nodes: dict[str, MemoryNode] = {}
        self.edges: list[MemoryEdge] = []
        self.load()

    def upsert_node(self, node_id: str, kind: str, label: str, properties: dict | None = None) -> MemoryNode:
        node = MemoryNode(node_id, kind, label, dict(properties or {}), time())
        self.nodes[node_id] = node
        self.save()
        return node

    def connect(self, source: str, target: str, relation: str, weight: float = 1.0) -> MemoryEdge:
        edge = MemoryEdge(source, target, relation, float(weight), time())
        self.edges = [
            existing
            for existing in self.edges
            if not (
                existing.source == source
                and existing.target == target
                and existing.relation == relation
            )
        ]
        self.edges.append(edge)
        self.save()
        return edge

    def neighbors(self, node_id: str, relation: str | None = None) -> list[MemoryNode]:
        candidates = [
            edge.target
            for edge in self.edges
            if edge.source == node_id and (relation is None or edge.relation == relation)
        ]
        return [self.nodes[target] for target in candidates if target in self.nodes]

    def search(self, query: str, limit: int = 10) -> list[MemoryNode]:
        lowered = query.lower()
        terms = {term for term in lowered.split() if term}
        matches = [
            node
            for node in self.nodes.values()
            if not terms
            or any(term in node.label.lower() or term in json.dumps(node.properties).lower() for term in terms)
        ]
        return sorted(matches, key=lambda node: node.updated_at, reverse=True)[:limit]

    def save(self) -> None:
        payload = {
            "nodes": [asdict(node) for node in self.nodes.values()],
            "edges": [asdict(edge) for edge in self.edges],
        }
        self.path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")

    def load(self) -> None:
        if not self.path.exists():
            return
        payload = json.loads(self.path.read_text(encoding="utf-8") or "{}")
        self.nodes = {row["id"]: MemoryNode(**row) for row in payload.get("nodes", [])}
        self.edges = [MemoryEdge(**row) for row in payload.get("edges", [])]
