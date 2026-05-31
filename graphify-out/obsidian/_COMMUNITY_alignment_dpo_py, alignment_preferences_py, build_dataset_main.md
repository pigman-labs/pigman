---
type: community
cohesion: 0.08
members: 41
---

# alignment_dpo_py, alignment_preferences_py, build_dataset_main

**Cohesion:** 0.08 - loosely connected
**Members:** 41 nodes

## Members
- [[.__init__()_30]] - code - alignment/preferences.py
- [[.__init__()_27]] - code - dataset_engine/quality.py
- [[.__init__()_26]] - code - dataset_engine/store.py
- [[.accept()]] - code - dataset_engine/quality.py
- [[.add()_3]] - code - alignment/preferences.py
- [[.forward()]] - code - torch_backend/modules.py
- [[.forward()_7]] - code - multimodal_stack/torch_modules.py
- [[.ingest()]] - code - dataset_engine/store.py
- [[.loss_from_logps()]] - code - alignment/dpo.py
- [[.plan()]] - code - distributed/launcher.py
- [[.score()_2]] - code - dataset_engine/quality.py
- [[.score_example()]] - code - alignment/dpo.py
- [[.stream()]] - code - dataset_engine/store.py
- [[.synthetic_from_scores()]] - code - alignment/preferences.py
- [[DPOObjective]] - code - alignment/dpo.py
- [[DatasetManifest]] - code - dataset_engine/records.py
- [[DatasetRecord]] - code - dataset_engine/records.py
- [[Deduplicator]] - code - dataset_engine/quality.py
- [[DistributedConfig]] - code - distributed/config.py
- [[JsonlDatasetStore]] - code - dataset_engine/store.py
- [[LaunchPlanner]] - code - distributed/launcher.py
- [[PreferenceBuffer]] - code - alignment/preferences.py
- [[PreferenceExample]] - code - alignment/preferences.py
- [[QualityScorer]] - code - dataset_engine/quality.py
- [[build_dataset.py]] - code - scripts/build_dataset.py
- [[config.py_2]] - code - distributed/config.py
- [[dpo.py]] - code - alignment/dpo.py
- [[launcher.py]] - code - distributed/launcher.py
- [[main()_7]] - code - scripts/build_dataset.py
- [[preferences.py]] - code - alignment/preferences.py
- [[quality.py]] - code - dataset_engine/quality.py
- [[records.py]] - code - dataset_engine/records.py
- [[sigmoid()]] - code - alignment/dpo.py
- [[store.py]] - code - dataset_engine/store.py
- [[test_alignment_preference_and_dpo()]] - code - tests/unit/test_frontier_subsystems.py
- [[test_dataset_engine_ingests_and_streams()]] - code - tests/unit/test_frontier_subsystems.py
- [[test_distributed_launch_plan()]] - code - tests/unit/test_frontier_subsystems.py
- [[test_frontier_safety_suite()]] - code - tests/unit/test_frontier_subsystems.py
- [[test_frontier_subsystems.py]] - code - tests/unit/test_frontier_subsystems.py
- [[test_multimodal_stack_forward()]] - code - tests/unit/test_frontier_subsystems.py
- [[world_size()]] - code - distributed/config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/alignment_dpo_py,_alignment_preferences_py,_build_dataset_main
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_activations_l2_normalize, activations_tanh, activations_tanh_grad]]
- 3 edges to [[_COMMUNITY_action_agentaction, action_agentaction_to_record, action_policy_actionpolicy]]
- 2 edges to [[_COMMUNITY_agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier]]
- 1 edge to [[_COMMUNITY_episodic_memory_episode, episodic_memory_episodicmemory, episodic_memory_episodicmemory_recent]]
- 1 edge to [[_COMMUNITY_basehttprequesthandler, decoders_text_decoder_py, filesystem_filesystemtool_read]]
- 1 edge to [[_COMMUNITY_abc, base_encode, base_encoder]]

## Top bridge nodes
- [[.ingest()]] - degree 9, connects to 2 communities
- [[.add()_3]] - degree 6, connects to 2 communities
- [[test_frontier_subsystems.py]] - degree 6, connects to 1 community
- [[sigmoid()]] - degree 4, connects to 1 community
- [[test_distributed_launch_plan()]] - degree 4, connects to 1 community