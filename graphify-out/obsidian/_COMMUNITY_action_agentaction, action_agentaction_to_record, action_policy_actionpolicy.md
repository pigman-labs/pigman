---
type: community
cohesion: 0.04
members: 83
---

# action_agentaction, action_agentaction_to_record, action_policy_actionpolicy

**Cohesion:** 0.04 - loosely connected
**Members:** 83 nodes

## Members
- [[.__init__()_31]] - code - orchestration/agent_loop.py
- [[.__init__()_20]] - code - planner/beam.py
- [[.__init__()_23]] - code - world_model/belief_update.py
- [[.__init__()_19]] - code - planner/router.py
- [[.__init__()_1]] - code - serving/runtime.py
- [[.add()_1]] - code - memory/working_memory.py
- [[.add_contradiction()]] - code - state/belief.py
- [[.add_edge()]] - code - causal/graph.py
- [[.append()_1]] - code - storage/trajectory_log.py
- [[.causes_of()]] - code - causal/graph.py
- [[.effects_of()]] - code - causal/graph.py
- [[.fuse()]] - code - encoders/fusion.py
- [[.plan()_2]] - code - planner/beam.py
- [[.plan()_3]] - code - planner/mpc.py
- [[.propose()]] - code - planner/action_proposer.py
- [[.recent()]] - code - memory/working_memory.py
- [[.run_once()]] - code - orchestration/agent_loop.py
- [[.score()_1]] - code - planner/risk_model.py
- [[.score()]] - code - planner/value_model.py
- [[.select_next()]] - code - policies/action_policy.py
- [[.step()]] - code - serving/runtime.py
- [[.to_record()]] - code - state/action.py
- [[.update()]] - code - world_model/belief_update.py
- [[.update_from_result()]] - code - causal/learner.py
- [[.write_jsonl()]] - code - storage/trajectory_log.py
- [[ActionPolicy]] - code - policies/action_policy.py
- [[ActionProposer]] - code - planner/action_proposer.py
- [[ActionRecord]] - code - data/schemas.py
- [[AgentAction]] - code - state/action.py
- [[AgentLoop]] - code - orchestration/agent_loop.py
- [[AgentLoopResult]] - code - orchestration/agent_loop.py
- [[AgentRuntime]] - code - serving/runtime.py
- [[BeamPlanner]] - code - planner/beam.py
- [[BeliefGraph]] - code - state/belief.py
- [[BeliefState]] - code - dynamics/latent_state.py
- [[BeliefUpdater]] - code - world_model/belief_update.py
- [[CausalEdge]] - code - causal/graph.py
- [[CausalGraph]] - code - causal/graph.py
- [[CausalLearner]] - code - causal/learner.py
- [[CrossModalFusion]] - code - encoders/fusion.py
- [[FusedLatent]] - code - encoders/fusion.py
- [[Hypothesis]] - code - state/belief.py
- [[LatentState]] - code - dynamics/latent_state.py
- [[MPCPlanner]] - code - planner/mpc.py
- [[Plan]] - code - planner/base.py
- [[Planner_1]] - code - planner/base.py
- [[Planner]] - code
- [[PlannerRouter]] - code - planner/router.py
- [[PlannerTrainStats]] - code - training/loops/train_planner.py
- [[RiskModel]] - code - planner/risk_model.py
- [[TrajectoryLog]] - code - storage/trajectory_log.py
- [[ValueModel]] - code - planner/value_model.py
- [[WorkingMemory]] - code - memory/working_memory.py
- [[_python_command()]] - code - planner/mpc.py
- [[action.py]] - code - state/action.py
- [[action_policy.py]] - code - policies/action_policy.py
- [[action_proposer.py]] - code - planner/action_proposer.py
- [[agent_benchmark.py]] - code - benchmarks/agent_benchmark.py
- [[agent_loop.py]] - code - orchestration/agent_loop.py
- [[base.py]] - code - planner/base.py
- [[beam.py]] - code - planner/beam.py
- [[belief.py]] - code - state/belief.py
- [[belief_update.py]] - code - world_model/belief_update.py
- [[fusion.py]] - code - encoders/fusion.py
- [[graph.py]] - code - causal/graph.py
- [[latent_state.py]] - code - dynamics/latent_state.py
- [[learner.py]] - code - causal/learner.py
- [[main()_1]] - code - scripts/run_goal.py
- [[main()_8]] - code - scripts/serve_agent.py
- [[mpc.py]] - code - planner/mpc.py
- [[risk_model.py]] - code - planner/risk_model.py
- [[rollout()]] - code - dynamics/rollout.py
- [[rollout.py]] - code - dynamics/rollout.py
- [[router.py]] - code - planner/router.py
- [[run_benchmark()]] - code - benchmarks/agent_benchmark.py
- [[run_goal.py]] - code - scripts/run_goal.py
- [[runtime.py]] - code - serving/runtime.py
- [[serve_agent.py]] - code - scripts/serve_agent.py
- [[train_planner.py]] - code - training/loops/train_planner.py
- [[train_planner_smoke()]] - code - training/loops/train_planner.py
- [[trajectory_log.py]] - code - storage/trajectory_log.py
- [[value_model.py]] - code - planner/value_model.py
- [[working_memory.py]] - code - memory/working_memory.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/action_agentaction,_action_agentaction_to_record,_action_policy_actionpolicy
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_action_decoder_actiondecoder, action_decoder_actiondecoder_decode, action_decoder_actiondecoder_init]]
- 13 edges to [[_COMMUNITY_adapter_fixed_width, adapter_neuralworldmodeladapter, adapter_neuralworldmodeladapter_predict_vector]]
- 12 edges to [[_COMMUNITY_agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier]]
- 12 edges to [[_COMMUNITY_abc, base_encode, base_encoder]]
- 9 edges to [[_COMMUNITY_episodic_memory_episode, episodic_memory_episodicmemory, episodic_memory_episodicmemory_recent]]
- 8 edges to [[_COMMUNITY_activations_l2_normalize, activations_tanh, activations_tanh_grad]]
- 5 edges to [[_COMMUNITY_basehttprequesthandler, decoders_text_decoder_py, filesystem_filesystemtool_read]]
- 3 edges to [[_COMMUNITY_alignment_dpo_py, alignment_preferences_py, build_dataset_main]]
- 2 edges to [[_COMMUNITY_evals_planner_eval_py, planner_eval_run_planner_eval, planner_search_py]]
- 1 edge to [[_COMMUNITY_config_agentconfig, config_load_yaml, config_modelconfig]]

## Top bridge nodes
- [[.append()_1]] - degree 26, connects to 8 communities
- [[AgentRuntime]] - degree 32, connects to 6 communities
- [[.step()]] - degree 16, connects to 6 communities
- [[.__init__()_1]] - degree 15, connects to 5 communities
- [[LatentState]] - degree 17, connects to 3 communities