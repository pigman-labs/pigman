---
type: community
cohesion: 0.07
members: 43
---

# abc, base_encode, base_encoder

**Cohesion:** 0.07 - loosely connected
**Members:** 43 nodes

## Members
- [[.__init__()_28]] - code - encoders/registry.py
- [[.encode()_1]] - code - encoders/file_encoder.py
- [[.encode()]] - code - encoders/registry.py
- [[.encode()_2]] - code - encoders/text_encoder.py
- [[.encode()_3]] - code - encoders/tool_trace_encoder.py
- [[.encode_observation()]] - code - encoders/base.py
- [[.observe_text()]] - code - serving/runtime.py
- [[ABC]] - code
- [[EncodedObservation]] - code - data/schemas.py
- [[Encoder_1]] - code - encoders/base.py
- [[Encoder]] - code
- [[EncoderRegistry]] - code - encoders/registry.py
- [[ExecutionResult]] - code - data/schemas.py
- [[FileEncoder]] - code - encoders/file_encoder.py
- [[FileLatent]] - code - encoders/file_encoder.py
- [[Observation]] - code - data/schemas.py
- [[TextEncoder]] - code - encoders/text_encoder.py
- [[TextLatent]] - code - encoders/text_encoder.py
- [[ToolTraceEncoder]] - code - encoders/tool_trace_encoder.py
- [[ToolTraceLatent]] - code - encoders/tool_trace_encoder.py
- [[TrajectoryStep]] - code - data/schemas.py
- [[base.py_2]] - code - encoders/base.py
- [[cosine_distance()_1]] - code - jepa/losses.py
- [[ema.py]] - code - jepa/ema.py
- [[ema_update()]] - code - jepa/ema.py
- [[encode()]] - code - encoders/base.py
- [[event_id()]] - code - core/ids.py
- [[file_encoder.py]] - code - encoders/file_encoder.py
- [[id()]] - code - dataset_engine/records.py
- [[ids.py]] - code - core/ids.py
- [[jepa_loss()]] - code - training/objectives/jepa_loss.py
- [[jepa_loss.py]] - code - training/objectives/jepa_loss.py
- [[losses.py_1]] - code - jepa/losses.py
- [[registry.py_1]] - code - encoders/registry.py
- [[schemas.py]] - code - data/schemas.py
- [[stable_id()]] - code - core/ids.py
- [[test_cosine_distance_identical_vectors()]] - code - tests/unit/test_smoke.py
- [[test_ema_update()]] - code - tests/unit/test_smoke.py
- [[test_runtime_step()]] - code - tests/unit/test_smoke.py
- [[test_smoke.py]] - code - tests/unit/test_smoke.py
- [[test_text_encoder_has_vector()]] - code - tests/unit/test_smoke.py
- [[text_encoder.py]] - code - encoders/text_encoder.py
- [[tool_trace_encoder.py]] - code - encoders/tool_trace_encoder.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/abc,_base_encode,_base_encoder
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_action_agentaction, action_agentaction_to_record, action_policy_actionpolicy]]
- 6 edges to [[_COMMUNITY_episodic_memory_episode, episodic_memory_episodicmemory, episodic_memory_episodicmemory_recent]]
- 5 edges to [[_COMMUNITY_agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier]]
- 3 edges to [[_COMMUNITY_action_decoder_actiondecoder, action_decoder_actiondecoder_decode, action_decoder_actiondecoder_init]]
- 1 edge to [[_COMMUNITY_basehttprequesthandler, decoders_text_decoder_py, filesystem_filesystemtool_read]]
- 1 edge to [[_COMMUNITY_activations_l2_normalize, activations_tanh, activations_tanh_grad]]
- 1 edge to [[_COMMUNITY_alignment_dpo_py, alignment_preferences_py, build_dataset_main]]

## Top bridge nodes
- [[.encode()_3]] - degree 9, connects to 4 communities
- [[ExecutionResult]] - degree 6, connects to 3 communities
- [[Observation]] - degree 7, connects to 2 communities
- [[test_smoke.py]] - degree 6, connects to 2 communities
- [[test_runtime_step()]] - degree 3, connects to 2 communities