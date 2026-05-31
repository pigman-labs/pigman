# Memory System

The `memory/` package is the local persistence and retrieval layer for the
agent. It now has separate episodic, semantic, procedural, vector, and graph
memory surfaces with consolidation between them.

## What Is Real

- JSONL episodic event store.
- SQLite semantic/procedural store using only stdlib `sqlite3`.
- Persistent vector index backed by JSON.
- Persistent graph memory backed by JSON.
- In-memory semantic/procedural stores for fast local use.
- Contradiction detection by semantic key.
- Recency, relevance, importance, and confidence scoring.
- Trace consolidation that writes facts, procedures, and graph edges.
- Retrieval bundles that combine facts, procedures, vectors, graph hits, recent
  episodes, and per-item scores.

## Files

- `retrieval.py`: high-level `MemorySystem` facade.
- `persistent.py`: JSONL and SQLite persistence.
- `vector_index.py`: in-memory and persistent vector indexes.
- `graph_memory.py`: node/edge graph store.
- `consolidation.py`: execution trace to facts/procedures/graph.
- `scoring.py`: retrieval scoring.
- `semantic_memory.py`: fact store and contradiction checks.
- `procedural_memory.py`: procedure matching and reliability.
- `episodic_memory.py`: episode lifecycle.
- `working_memory.py`: short-term scratch memory.

## Retrieval Flow

```text
query
  -> stable hash embedding
  -> vector search
  -> semantic fact search
  -> procedure search
  -> graph search
  -> score persistent facts
  -> MemoryBundle
```

## Limits

This is still not frontier-scale memory. It does not yet use learned dense
embeddings, ANN indexes, distributed object storage, automatic data governance,
or privacy-preserving deletion across replicas. It is a runnable local research
memory substrate that those pieces can replace later.
