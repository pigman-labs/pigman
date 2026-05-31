from __future__ import annotations

from pathlib import Path

from memory.consolidation import MemoryConsolidationEngine
from memory.graph_memory import GraphMemory
from memory.persistent import JsonlEpisodicStore, SqliteMemoryStore
from memory.procedural_memory import ProceduralMemory, Procedure
from memory.retrieval import MemorySystem
from memory.scoring import MemoryScorer
from memory.semantic_memory import SemanticMemory
from memory.vector_index import PersistentVectorIndex, VectorRecord


def test_semantic_memory_detects_contradictions() -> None:
    memory = SemanticMemory()
    memory.upsert("model.backend", "torch", importance=0.9)

    contradictions = memory.contradictions("model.backend", "jax")

    assert contradictions
    assert contradictions[0].value == "torch"
    assert memory.retrieve("backend")["model.backend"] == "torch"


def test_procedural_memory_scores_successful_procedure() -> None:
    memory = ProceduralMemory()
    memory.add(Procedure("run-tests", "test", ({"type": "run_shell"},), success_count=3))
    memory.add(Procedure("weak-test", "test", ({"type": "say"},), failure_count=3))

    matches = memory.match("please test this repo")

    assert matches[0].name == "run-tests"
    memory.record_outcome("weak-test", True)
    assert any(procedure.success_count == 1 for procedure in memory.procedures if procedure.name == "weak-test")


def test_persistent_vector_index_survives_reload(tmp_path: Path) -> None:
    path = tmp_path / "vectors.json"
    index = PersistentVectorIndex(str(path))
    index.add(VectorRecord("a", (1.0, 0.0), {"text": "alpha"}))

    reloaded = PersistentVectorIndex(str(path))
    hits = reloaded.search((1.0, 0.0), limit=1)

    assert hits[0].id == "a"
    assert hits[0].payload["text"] == "alpha"


def test_graph_memory_persists_nodes_and_edges(tmp_path: Path) -> None:
    path = tmp_path / "graph.json"
    graph = GraphMemory(str(path))
    graph.upsert_node("goal:test", "goal", "run tests")
    graph.upsert_node("action:pytest", "action", "pytest")
    graph.connect("goal:test", "action:pytest", "used_action")

    reloaded = GraphMemory(str(path))

    assert reloaded.neighbors("goal:test")[0].label == "pytest"
    assert reloaded.search("tests")[0].id == "goal:test"


def test_sqlite_memory_store_tracks_confidence_and_contradictions(tmp_path: Path) -> None:
    store = SqliteMemoryStore(str(tmp_path / "memory.sqlite3"))
    store.upsert_fact("backend", "torch", importance=0.9, confidence=0.8, source="test")

    facts = store.facts("backend")
    contradictions = store.detect_contradiction("backend", "jax")

    assert facts[0].confidence == 0.8
    assert facts[0].source == "test"
    assert contradictions[0]["existing"] == "torch"


def test_memory_system_persists_and_retrieves_full_bundle(tmp_path: Path) -> None:
    memory = MemorySystem(str(tmp_path), persistent=True)
    contradictions = memory.remember_fact("planner", "uses mpc", importance=0.9)
    memory.add_trace("trace-1", "planner uses mpc for tests", {"success": True})

    bundle = memory.retrieve("planner mpc", limit=5)

    assert contradictions == []
    assert bundle.facts["planner"] == "uses mpc"
    assert bundle.persistent_facts[0]["key"] == "planner"
    assert bundle.vector_hits
    assert bundle.graph_hits
    assert bundle.scores["fact:planner"] > 0.0


def test_memory_consolidation_writes_fact_procedure_and_graph(tmp_path: Path) -> None:
    store = SqliteMemoryStore(str(tmp_path / "memory.sqlite3"))
    graph = GraphMemory(str(tmp_path / "graph.json"))
    engine = MemoryConsolidationEngine(store, graph)

    report = engine.consolidate_trace(
        {
            "goal": "run tests",
            "action": {"type": "run_shell", "payload": {"command": ["python", "-m", "pytest"]}},
            "success": True,
        }
    )

    assert report.facts_written == 2
    assert report.procedures_written == 1
    assert report.graph_edges_written == 1
    assert store.facts("run tests")
    assert graph.neighbors("goal:run tests")[0].id == "action:run_shell"


def test_memory_scorer_combines_relevance_recency_importance() -> None:
    score = MemoryScorer().score("pytest tests", "pytest tests pass", importance=0.9, confidence=0.8)

    assert score.relevance == 1.0
    assert score.total > 0.7


def test_jsonl_store_reads_recent_events(tmp_path: Path) -> None:
    store = JsonlEpisodicStore(str(tmp_path / "episodes.jsonl"))
    for index in range(4):
        store.append({"index": index})

    recent = store.read_recent(limit=2)

    assert [item["index"] for item in recent] == [2, 3]
