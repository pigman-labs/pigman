# Graph Report - .  (2026-05-23)

## Corpus Check
- Corpus is ~22,561 words - fits in a single context window. You may not need a graph.

## Summary
- 860 nodes · 1452 edges · 40 communities detected
- Extraction: 61% EXTRACTED · 39% INFERRED · 0% AMBIGUOUS · INFERRED: 565 edges (avg confidence: 0.71)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_concept_affect, concept_agi, concept_alignment|concept_affect, concept_agi, concept_alignment]]
- [[_COMMUNITY_activations_l2_normalize, activations_tanh, activations_tanh_grad|activations_l2_normalize, activations_tanh, activations_tanh_grad]]
- [[_COMMUNITY_doc_jepa_world_model_architecture_md, doc_jepa_world_model_architecture_md_h_0_executive_summary, doc_jepa_world_model_architecture_md_h_10_1_working_memory|doc_jepa_world_model_architecture_md, doc_jepa_world_model_architecture_md_h_0_executive_summary, doc_jepa_world_model_architecture_md_h_10_1_working_memory]]
- [[_COMMUNITY_action_agentaction, action_agentaction_to_record, action_policy_actionpolicy|action_agentaction, action_agentaction_to_record, action_policy_actionpolicy]]
- [[_COMMUNITY_agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier|agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier]]
- [[_COMMUNITY_episodic_memory_episode, episodic_memory_episodicmemory, episodic_memory_episodicmemory_recent|episodic_memory_episode, episodic_memory_episodicmemory, episodic_memory_episodicmemory_recent]]
- [[_COMMUNITY_abc, base_encode, base_encoder|abc, base_encode, base_encoder]]
- [[_COMMUNITY_alignment_dpo_py, alignment_preferences_py, build_dataset_main|alignment_dpo_py, alignment_preferences_py, build_dataset_main]]
- [[_COMMUNITY_action_decoder_actiondecoder, action_decoder_actiondecoder_decode, action_decoder_actiondecoder_init|action_decoder_actiondecoder, action_decoder_actiondecoder_decode, action_decoder_actiondecoder_init]]
- [[_COMMUNITY_adapter_fixed_width, adapter_neuralworldmodeladapter, adapter_neuralworldmodeladapter_predict_vector|adapter_fixed_width, adapter_neuralworldmodeladapter, adapter_neuralworldmodeladapter_predict_vector]]
- [[_COMMUNITY_alignment_init_py, causal_init_py, core_init_py|alignment_init_py, causal_init_py, core_init_py]]
- [[_COMMUNITY_evals_planner_eval_py, planner_eval_run_planner_eval, planner_search_py|evals_planner_eval_py, planner_eval_run_planner_eval, planner_search_py]]
- [[_COMMUNITY_basehttprequesthandler, decoders_text_decoder_py, filesystem_filesystemtool_read|basehttprequesthandler, decoders_text_decoder_py, filesystem_filesystemtool_read]]
- [[_COMMUNITY_lib_allows_read_only_commands, lib_approve_read_only, lib_approves_observe|lib_allows_read_only_commands, lib_approve_read_only, lib_approves_observe]]
- [[_COMMUNITY_jepa_kernels_rs_lib_rs, lib_cosine_distance, lib_dot|jepa_kernels_rs_lib_rs, lib_cosine_distance, lib_dot]]
- [[_COMMUNITY_config_agentconfig, config_load_yaml, config_modelconfig|config_agentconfig, config_load_yaml, config_modelconfig]]
- [[_COMMUNITY_browser_browseraction, browser_browsertool, browser_browsertool_execute|browser_browseraction, browser_browsertool, browser_browsertool_execute]]
- [[_COMMUNITY_checkpoint_checkpoint_path, checkpoint_checkpointref, checkpoint_save_metadata|checkpoint_checkpoint_path, checkpoint_checkpointref, checkpoint_save_metadata]]
- [[_COMMUNITY_expert_router_expertrouter, expert_router_expertrouter_init, expert_router_expertrouter_route|expert_router_expertrouter, expert_router_expertrouter_init, expert_router_expertrouter_route]]
- [[_COMMUNITY_null_world_nullworld, null_world_nullworld_step, simulators_null_world_py|null_world_nullworld, null_world_nullworld_step, simulators_null_world_py]]
- [[_COMMUNITY_jepa_masking_py, masking_block_mask, masking_maskspec|jepa_masking_py, masking_block_mask, masking_maskspec]]
- [[_COMMUNITY_interfaces_messages_py, messages_agentresponse, messages_runtimemessage|interfaces_messages_py, messages_agentresponse, messages_runtimemessage]]
- [[_COMMUNITY_core_tensor_types_py, tensor_types_shapespec|core_tensor_types_py, tensor_types_shapespec]]
- [[_COMMUNITY_causal_interventions_py, interventions_intervention|causal_interventions_py, interventions_intervention]]
- [[_COMMUNITY_schedules_cosine_with_warmup, training_optimizers_schedules_py|schedules_cosine_with_warmup, training_optimizers_schedules_py]]
- [[_COMMUNITY_goal_goal, state_goal_py|goal_goal, state_goal_py]]
- [[_COMMUNITY_events_event, telemetry_events_py|events_event, telemetry_events_py]]
- [[_COMMUNITY_collators_identity_collate, data_collators_py|collators_identity_collate, data_collators_py]]
- [[_COMMUNITY_tools_init_py|tools_init_py]]
- [[_COMMUNITY_serving_init_py|serving_init_py]]
- [[_COMMUNITY_planner_init_py|planner_init_py]]
- [[_COMMUNITY_training_init_py|training_init_py]]
- [[_COMMUNITY_training_objectives_init_py|training_objectives_init_py]]
- [[_COMMUNITY_training_optimizers_init_py|training_optimizers_init_py]]
- [[_COMMUNITY_training_loops_init_py|training_loops_init_py]]
- [[_COMMUNITY_verifiers_init_py|verifiers_init_py]]
- [[_COMMUNITY_storage_init_py|storage_init_py]]
- [[_COMMUNITY_examples_smoke_agent_py|examples_smoke_agent_py]]
- [[_COMMUNITY_scripts_init_py|scripts_init_py]]
- [[_COMMUNITY_decoders_init_py|decoders_init_py]]

## God Nodes (most connected - your core abstractions)
1. `AgentRuntime` - 32 edges
2. `Stable interface schemas between Python, Rust, tools, and services.` - 27 edges
3. `train_jepa_torch()` - 22 edges
4. `Linear` - 21 edges
5. `train_dynamics_torch()` - 20 edges
6. `TrainableJEPA` - 20 edges
7. `AgentAction` - 19 edges
8. `LatentState` - 17 edges
9. `VerificationResult` - 16 edges
10. `MemorySystem` - 14 edges

## Surprising Connections (you probably didn't know these)
- `test_planner_eval_selects_best_action()` --calls--> `run_planner_eval()`  [INFERRED]
  tests/unit/test_planning_memory_tools.py → evals/planner_eval.py
- `test_multimodal_stack_forward()` --calls--> `MultimodalWorldStack`  [INFERRED]
  tests/unit/test_frontier_subsystems.py → multimodal_stack/torch_modules.py
- `train_dynamics_torch()` --calls--> `normalize()`  [INFERRED]
  training/loops/train_torch_dynamics.py → kernels/vector_math.py
- `DynamicsTrainStats` --uses--> `LatentState`  [INFERRED]
  training/loops/train_dynamics.py → dynamics/latent_state.py
- `WorldStateVerifier` --uses--> `LatentState`  [INFERRED]
  verifiers/world_state.py → dynamics/latent_state.py

## Communities

### Community 0 - "concept_affect, concept_agi, concept_alignment"
Cohesion: 0.02
Nodes (150): Affect, AGI, Alignment, Chat, Continual Learning, Curriculum, Dataset Engine, Distributed Training (+142 more)

### Community 1 - "activations_l2_normalize, activations_tanh, activations_tanh_grad"
Cohesion: 0.04
Nodes (47): l2_normalize(), tanh(), tanh_grad(), load_npz(), save_npz(), TorchModelConfig, TorchTrainConfig, seed_everything() (+39 more)

### Community 2 - "doc_jepa_world_model_architecture_md, doc_jepa_world_model_architecture_md_h_0_executive_summary, doc_jepa_world_model_architecture_md_h_10_1_working_memory"
Cohesion: 0.02
Nodes (99): 0. Executive Summary, 10.1 Working Memory, 10.2 Episodic Memory, 10.3 Semantic Memory, 10.4 Procedural Memory, 10.5 Graph Memory, 10.6 Memory Retrieval, 10. Memory Architecture (+91 more)

### Community 3 - "action_agentaction, action_agentaction_to_record, action_policy_actionpolicy"
Cohesion: 0.04
Nodes (34): AgentAction, ActionPolicy, ActionProposer, run_benchmark(), AgentLoop, AgentLoopResult, Plan, Planner (+26 more)

### Community 4 - "agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier"
Cohesion: 0.05
Nodes (24): run_agent_eval(), CodeVerifier, main(), FrontierSafetySuite, SafetyCase, ToolExecutor, FilesystemTool, run_memory_eval() (+16 more)

### Community 5 - "episodic_memory_episode, episodic_memory_episodicmemory, episodic_memory_episodicmemory_recent"
Cohesion: 0.07
Nodes (21): Episode, EpisodicMemory, encode_jsonl(), encodes_jsonl(), MemoryRecord, MemoryStore, stores_recent_records(), cosine_mse_loss() (+13 more)

### Community 6 - "abc, base_encode, base_encoder"
Cohesion: 0.07
Nodes (25): ABC, encode(), Encoder, ema_update(), Encoder, FileEncoder, FileLatent, event_id() (+17 more)

### Community 7 - "alignment_dpo_py, alignment_preferences_py, build_dataset_main"
Cohesion: 0.08
Nodes (17): main(), DistributedConfig, DPOObjective, sigmoid(), LaunchPlanner, PreferenceBuffer, PreferenceExample, Deduplicator (+9 more)

### Community 8 - "action_decoder_actiondecoder, action_decoder_actiondecoder_decode, action_decoder_actiondecoder_init"
Cohesion: 0.08
Nodes (13): ActionDecoder, VerificationResult, VerifierEnsemble, classify_risk(), Registry, SafetyVerifier, SourceProvenanceVerifier, test_world_state_verifier_accepts_runtime_state() (+5 more)

### Community 9 - "adapter_fixed_width, adapter_neuralworldmodeladapter, adapter_neuralworldmodeladapter_predict_vector"
Cohesion: 0.12
Nodes (15): fixed_width(), NeuralWorldModelAdapter, JEPAPredictor, Prediction, PretrainStats, run_pretrain_smoke(), test_neural_eval_reads_checkpoint(), test_neural_jepa_trains_and_loads() (+7 more)

### Community 10 - "alignment_init_py, causal_init_py, core_init_py"
Cohesion: 0.07
Nodes (1): Stable interface schemas between Python, Rust, tools, and services.

### Community 11 - "evals_planner_eval_py, planner_eval_run_planner_eval, planner_search_py"
Cohesion: 0.13
Nodes (8): run_planner_eval(), BeamSearchPlanner, CEMPlanner, LearnedMPCPlanner, MCTSNode, MCTSPlanner, SyntheticAction, SyntheticControlWorld

### Community 12 - "basehttprequesthandler, decoders_text_decoder_py, filesystem_filesystemtool_read"
Cohesion: 0.11
Nodes (9): BaseHTTPRequestHandler, HttpApiTool, HttpResult, main(), AgentHandler, AgentServer, AgentService, test_serving_api_service_smoke() (+1 more)

### Community 13 - "lib_allows_read_only_commands, lib_approve_read_only, lib_approves_observe"
Cohesion: 0.15
Nodes (8): approve_read_only(), approves_observe(), classify_command(), Permission, rejects_write_action(), RuntimeAction, RuntimeDecision, main()

### Community 14 - "jepa_kernels_rs_lib_rs, lib_cosine_distance, lib_dot"
Cohesion: 0.29
Nodes (0): 

### Community 15 - "config_agentconfig, config_load_yaml, config_modelconfig"
Cohesion: 0.4
Nodes (5): AgentConfig, load_yaml(), ModelConfig, _parse_scalar(), RuntimeConfig

### Community 16 - "browser_browseraction, browser_browsertool, browser_browsertool_execute"
Cohesion: 0.5
Nodes (2): BrowserAction, BrowserTool

### Community 17 - "checkpoint_checkpoint_path, checkpoint_checkpointref, checkpoint_save_metadata"
Cohesion: 0.5
Nodes (1): CheckpointRef

### Community 18 - "expert_router_expertrouter, expert_router_expertrouter_init, expert_router_expertrouter_route"
Cohesion: 0.5
Nodes (1): ExpertRouter

### Community 19 - "null_world_nullworld, null_world_nullworld_step, simulators_null_world_py"
Cohesion: 0.67
Nodes (1): NullWorld

### Community 20 - "jepa_masking_py, masking_block_mask, masking_maskspec"
Cohesion: 1.0
Nodes (2): block_mask(), MaskSpec

### Community 21 - "interfaces_messages_py, messages_agentresponse, messages_runtimemessage"
Cohesion: 0.67
Nodes (2): AgentResponse, RuntimeMessage

### Community 22 - "core_tensor_types_py, tensor_types_shapespec"
Cohesion: 1.0
Nodes (1): ShapeSpec

### Community 23 - "causal_interventions_py, interventions_intervention"
Cohesion: 1.0
Nodes (1): Intervention

### Community 24 - "schedules_cosine_with_warmup, training_optimizers_schedules_py"
Cohesion: 1.0
Nodes (0): 

### Community 25 - "goal_goal, state_goal_py"
Cohesion: 1.0
Nodes (1): Goal

### Community 26 - "events_event, telemetry_events_py"
Cohesion: 1.0
Nodes (1): Event

### Community 27 - "collators_identity_collate, data_collators_py"
Cohesion: 1.0
Nodes (0): 

### Community 28 - "tools_init_py"
Cohesion: 1.0
Nodes (0): 

### Community 29 - "serving_init_py"
Cohesion: 1.0
Nodes (0): 

### Community 30 - "planner_init_py"
Cohesion: 1.0
Nodes (0): 

### Community 31 - "training_init_py"
Cohesion: 1.0
Nodes (0): 

### Community 32 - "training_objectives_init_py"
Cohesion: 1.0
Nodes (0): 

### Community 33 - "training_optimizers_init_py"
Cohesion: 1.0
Nodes (0): 

### Community 34 - "training_loops_init_py"
Cohesion: 1.0
Nodes (0): 

### Community 35 - "verifiers_init_py"
Cohesion: 1.0
Nodes (0): 

### Community 36 - "storage_init_py"
Cohesion: 1.0
Nodes (0): 

### Community 37 - "examples_smoke_agent_py"
Cohesion: 1.0
Nodes (0): 

### Community 38 - "scripts_init_py"
Cohesion: 1.0
Nodes (0): 

### Community 39 - "decoders_init_py"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **247 isolated node(s):** `Small deterministic embedding fallback for local end-to-end tests.`, `BrowserAction`, `RuntimeConfig`, `ModelConfig`, `AgentConfig` (+242 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `core_tensor_types_py, tensor_types_shapespec`** (2 nodes): `tensor_types.py`, `ShapeSpec`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `causal_interventions_py, interventions_intervention`** (2 nodes): `interventions.py`, `Intervention`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `schedules_cosine_with_warmup, training_optimizers_schedules_py`** (2 nodes): `cosine_with_warmup()`, `schedules.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `goal_goal, state_goal_py`** (2 nodes): `Goal`, `goal.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `events_event, telemetry_events_py`** (2 nodes): `Event`, `events.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `collators_identity_collate, data_collators_py`** (2 nodes): `identity_collate()`, `collators.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `tools_init_py`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `serving_init_py`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `planner_init_py`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `training_init_py`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `training_objectives_init_py`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `training_optimizers_init_py`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `training_loops_init_py`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `verifiers_init_py`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `storage_init_py`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `examples_smoke_agent_py`** (1 nodes): `smoke_agent.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `scripts_init_py`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `decoders_init_py`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AgentRuntime` connect `action_agentaction, action_agentaction_to_record, action_policy_actionpolicy` to `agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier`, `episodic_memory_episode, episodic_memory_episodicmemory, episodic_memory_episodicmemory_recent`, `abc, base_encode, base_encoder`, `action_decoder_actiondecoder, action_decoder_actiondecoder_decode, action_decoder_actiondecoder_init`, `adapter_fixed_width, adapter_neuralworldmodeladapter, adapter_neuralworldmodeladapter_predict_vector`, `basehttprequesthandler, decoders_text_decoder_py, filesystem_filesystemtool_read`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Why does `evaluate_checkpoint()` connect `activations_l2_normalize, activations_tanh, activations_tanh_grad` to `adapter_fixed_width, adapter_neuralworldmodeladapter, adapter_neuralworldmodeladapter_predict_vector`, `action_agentaction, action_agentaction_to_record, action_policy_actionpolicy`, `agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier`?**
  _High betweenness centrality (0.030) - this node is a cross-community bridge._
- **Why does `train_dynamics_torch()` connect `activations_l2_normalize, activations_tanh, activations_tanh_grad` to `episodic_memory_episode, episodic_memory_episodicmemory, episodic_memory_episodicmemory_recent`, `alignment_dpo_py, alignment_preferences_py, build_dataset_main`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Are the 28 inferred relationships involving `AgentRuntime` (e.g. with `CausalGraph` and `CausalLearner`) actually correct?**
  _`AgentRuntime` has 28 INFERRED edges - model-reasoned connections that need verification._
- **Are the 20 inferred relationships involving `train_jepa_torch()` (e.g. with `TorchTrainConfig` and `TorchModelConfig`) actually correct?**
  _`train_jepa_torch()` has 20 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `Linear` (e.g. with `TrainableLatentDynamics` and `TrainStep`) actually correct?**
  _`Linear` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 18 inferred relationships involving `train_dynamics_torch()` (e.g. with `train_joint_world_model()` and `TorchTrainConfig`) actually correct?**
  _`train_dynamics_torch()` has 18 INFERRED edges - model-reasoned connections that need verification._