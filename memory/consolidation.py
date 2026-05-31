from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from memory.graph_memory import GraphMemory
from memory.persistent import SqliteMemoryStore


@dataclass(frozen=True)
class ConsolidationReport:
    facts_written: int
    procedures_written: int
    graph_edges_written: int
    contradictions: list[dict]


class MemoryConsolidationEngine:
    def __init__(self, store: SqliteMemoryStore, graph: GraphMemory) -> None:
        self.store = store
        self.graph = graph

    def consolidate_trace(self, trace: dict[str, Any]) -> ConsolidationReport:
        facts = 0
        procedures = 0
        edges = 0
        contradictions = []
        goal = str(trace.get("goal", trace.get("task", "")))
        action = trace.get("action") or trace.get("selected_action") or {}
        action_type = str(getattr(action, "type", action.get("type", "unknown")))
        success = bool(trace.get("success", True))
        if goal:
            contradiction = self.store.detect_contradiction(f"goal:{goal}", f"success={success}")
            contradictions.extend(contradiction)
            self.store.upsert_fact(f"goal:{goal}", f"success={success}", 0.7 if success else 0.4)
            facts += 1
            self.graph.upsert_node(f"goal:{goal}", "goal", goal, {"success": success})
        if action_type != "unknown":
            self.store.upsert_fact(f"action:{action_type}", f"success={success}", 0.8 if success else 0.3)
            facts += 1
            self.store.upsert_procedure(
                f"procedure:{action_type}",
                action_type,
                {"action_type": action_type, "payload": getattr(action, "payload", action.get("payload", {}))},
                0.6 if success else 0.2,
            )
            procedures += 1
            self.graph.upsert_node(f"action:{action_type}", "action", action_type, {"success": success})
            if goal:
                self.graph.connect(f"goal:{goal}", f"action:{action_type}", "used_action", 1.0 if success else 0.3)
                edges += 1
        return ConsolidationReport(facts, procedures, edges, contradictions)
