from __future__ import annotations

from causal.graph import CausalGraph
from data.schemas import ExecutionResult


class CausalLearner:
    def update_from_result(self, graph: CausalGraph, result: ExecutionResult) -> None:
        source = f"action:{result.action.type}"
        target = f"observation:{result.observation.source}"
        relation = "produced_success" if result.success else "produced_failure"
        confidence = 0.7 if result.success else 0.5
        graph.add_edge(source, target, relation, confidence)
