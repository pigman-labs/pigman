from __future__ import annotations

from memory.retrieval import MemorySystem


def run_memory_eval(root: str = "artifacts/evals/memory") -> dict:
    memory = MemorySystem(root, persistent=True)
    contradictions = memory.remember_fact("pytest", "tests pass", 0.9, source="eval")
    memory.add_trace("trace-memory-eval", "pytest tests pass", {"goal": "test", "success": True})
    consolidation = memory.consolidate_trace(
        {
            "goal": "run pytest",
            "action": {"type": "run_shell", "payload": {"command": ["python", "-m", "pytest"]}},
            "success": True,
        }
    )
    bundle = memory.retrieve("pytest", limit=5)
    return {
        "episodes": len(memory.episodes.read_recent()),
        "facts": len(memory.store.facts("pytest")),
        "vector_hits": len(bundle.vector_hits),
        "graph_hits": len(bundle.graph_hits),
        "persistent_facts": len(bundle.persistent_facts),
        "contradictions": len(contradictions) + len(consolidation.contradictions),
    }
