---
type: community
cohesion: 0.07
members: 43
---

# episodic_memory_episode, episodic_memory_episodicmemory, episodic_memory_episodicmemory_recent

**Cohesion:** 0.07 - loosely connected
**Members:** 43 nodes

## Members
- [[.__init__()_3]] - code - memory/retrieval.py
- [[.add()_2]] - code - memory/procedural_memory.py
- [[.add()]] - code - memory/vector_index.py
- [[.add_trace()]] - code - memory/retrieval.py
- [[.forward()_3]] - code - torch_backend/world_model.py
- [[.forward()_4]] - code - torch_backend/world_model.py
- [[.insert()]] - code - memory_store_rs/lib.rs
- [[.match()]] - code - memory/procedural_memory.py
- [[.recent()_1]] - code - memory/episodic_memory.py
- [[.recent()_2]] - code - memory_store_rs/lib.rs
- [[.retrieve()_1]] - code - memory/retrieval.py
- [[.retrieve()]] - code - memory/semantic_memory.py
- [[.search()]] - code - memory/vector_index.py
- [[.start()]] - code - memory/episodic_memory.py
- [[.upsert()]] - code - memory/semantic_memory.py
- [[Episode]] - code - memory/episodic_memory.py
- [[EpisodicMemory]] - code - memory/episodic_memory.py
- [[InMemoryVectorIndex]] - code - memory/vector_index.py
- [[MemoryBundle]] - code - memory/retrieval.py
- [[MemoryRecord]] - code - memory_store_rs/lib.rs
- [[MemoryStore]] - code - memory_store_rs/lib.rs
- [[MemorySystem]] - code - memory/retrieval.py
- [[ProceduralMemory]] - code - memory/procedural_memory.py
- [[Procedure]] - code - memory/procedural_memory.py
- [[SemanticMemory]] - code - memory/semantic_memory.py
- [[Small deterministic embedding fallback for local end-to-end tests.]] - rationale - kernels/vector_math.py
- [[VectorRecord]] - code - memory/vector_index.py
- [[cosine_mse_loss()]] - code - torch_backend/losses.py
- [[cosine_similarity()]] - code - kernels/vector_math.py
- [[encode_jsonl()]] - code - memory_store_rs/lib.rs
- [[encodes_jsonl()]] - code - memory_store_rs/lib.rs
- [[episodic_memory.py]] - code - memory/episodic_memory.py
- [[l2_norm()]] - code - kernels/vector_math.py
- [[lib.rs_3]] - code - memory_store_rs/lib.rs
- [[normalize()]] - code - kernels/vector_math.py
- [[procedural_memory.py]] - code - memory/procedural_memory.py
- [[retrieval.py]] - code - memory/retrieval.py
- [[semantic_memory.py]] - code - memory/semantic_memory.py
- [[stable_hash_embedding()]] - code - kernels/vector_math.py
- [[stores_recent_records()]] - code - memory_store_rs/lib.rs
- [[test_memory_retrieval()]] - code - tests/unit/test_smoke.py
- [[vector_index.py]] - code - memory/vector_index.py
- [[vector_math.py]] - code - kernels/vector_math.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/episodic_memory_episode,_episodic_memory_episodicmemory,_episodic_memory_episodicmemory_recent
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_action_agentaction, action_agentaction_to_record, action_policy_actionpolicy]]
- 6 edges to [[_COMMUNITY_abc, base_encode, base_encoder]]
- 5 edges to [[_COMMUNITY_activations_l2_normalize, activations_tanh, activations_tanh_grad]]
- 3 edges to [[_COMMUNITY_agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier]]
- 1 edge to [[_COMMUNITY_adapter_fixed_width, adapter_neuralworldmodeladapter, adapter_neuralworldmodeladapter_predict_vector]]
- 1 edge to [[_COMMUNITY_alignment_dpo_py, alignment_preferences_py, build_dataset_main]]
- 1 edge to [[_COMMUNITY_basehttprequesthandler, decoders_text_decoder_py, filesystem_filesystemtool_read]]

## Top bridge nodes
- [[MemorySystem]] - degree 14, connects to 2 communities
- [[.retrieve()_1]] - degree 9, connects to 2 communities
- [[normalize()]] - degree 9, connects to 2 communities
- [[stable_hash_embedding()]] - degree 9, connects to 2 communities
- [[.add_trace()]] - degree 6, connects to 2 communities