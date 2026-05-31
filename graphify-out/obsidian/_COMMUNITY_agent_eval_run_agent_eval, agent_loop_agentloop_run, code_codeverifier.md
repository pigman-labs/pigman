---
type: community
cohesion: 0.05
members: 61
---

# agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier

**Cohesion:** 0.05 - loosely connected
**Members:** 61 nodes

## Members
- [[.__init__()_21]] - code - verifiers/code.py
- [[.__init__()_25]] - code - safety_frontier/evals.py
- [[.__init__()]] - code - tools/executor.py
- [[.__init__()_4]] - code - memory/persistent.py
- [[.__init__()_5]] - code - memory/persistent.py
- [[.append()]] - code - memory/persistent.py
- [[.apply_replace()]] - code - tools/patch.py
- [[.check_command()]] - code - verifiers/shell.py
- [[.compile_python()]] - code - verifiers/code.py
- [[.consolidate_execution()]] - code - memory/persistent.py
- [[.diff_text()]] - code - tools/filesystem.py
- [[.execute()_1]] - code - tools/executor.py
- [[.facts()]] - code - memory/persistent.py
- [[.list_files()]] - code - tools/filesystem.py
- [[.procedures()]] - code - memory/persistent.py
- [[.pytest()]] - code - verifiers/code.py
- [[.read_recent()]] - code - memory/persistent.py
- [[.run()_2]] - code - orchestration/agent_loop.py
- [[.run()_1]] - code - safety_frontier/evals.py
- [[.run()]] - code - tools/shell.py
- [[.upsert_fact()]] - code - memory/persistent.py
- [[.upsert_procedure()]] - code - memory/persistent.py
- [[CodeVerifier]] - code - verifiers/code.py
- [[FilesystemTool]] - code - tools/filesystem.py
- [[FrontierSafetySuite]] - code - safety_frontier/evals.py
- [[JsonlEpisodicStore]] - code - memory/persistent.py
- [[MemoryConsolidator]] - code - memory/persistent.py
- [[PatchTool]] - code - tools/patch.py
- [[PersistentFact]] - code - memory/persistent.py
- [[SafetyCase]] - code - safety_frontier/evals.py
- [[ShellResult]] - code - tools/shell.py
- [[ShellSafetyVerifier]] - code - verifiers/shell.py
- [[ShellTool]] - code - tools/shell.py
- [[SqliteMemoryStore]] - code - memory/persistent.py
- [[ToolExecutor]] - code - tools/executor.py
- [[agent_eval.py]] - code - evals/agent_eval.py
- [[code.py]] - code - verifiers/code.py
- [[eval_agent.py]] - code - scripts/eval_agent.py
- [[evals.py]] - code - safety_frontier/evals.py
- [[executor.py]] - code - tools/executor.py
- [[filesystem.py]] - code - tools/filesystem.py
- [[main()_10]] - code - scripts/eval_agent.py
- [[main()_11]] - code - scripts/verify_all.py
- [[memory_eval.py]] - code - evals/memory_eval.py
- [[patch.py]] - code - tools/patch.py
- [[persistent.py]] - code - memory/persistent.py
- [[run_agent_eval()]] - code - evals/agent_eval.py
- [[run_memory_eval()]] - code - evals/memory_eval.py
- [[run_tool_eval()]] - code - evals/tool_eval.py
- [[run_verifier_eval()]] - code - evals/verifier_eval.py
- [[shell.py]] - code - tools/shell.py
- [[shell.py_1]] - code - verifiers/shell.py
- [[test_memory_eval()]] - code - tests/unit/test_planning_memory_tools.py
- [[test_persistent_memory()]] - code - tests/unit/test_planning_memory_tools.py
- [[test_planner_eval_selects_best_action()]] - code - tests/unit/test_planning_memory_tools.py
- [[test_planning_memory_tools.py]] - code - tests/unit/test_planning_memory_tools.py
- [[test_shell_safety()]] - code - tests/unit/test_planning_memory_tools.py
- [[test_tool_and_patch()]] - code - tests/unit/test_planning_memory_tools.py
- [[tool_eval.py]] - code - evals/tool_eval.py
- [[verifier_eval.py]] - code - evals/verifier_eval.py
- [[verify_all.py]] - code - scripts/verify_all.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agent_eval_run_agent_eval,_agent_loop_agentloop_run,_code_codeverifier
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_action_agentaction, action_agentaction_to_record, action_policy_actionpolicy]]
- 9 edges to [[_COMMUNITY_activations_l2_normalize, activations_tanh, activations_tanh_grad]]
- 8 edges to [[_COMMUNITY_action_decoder_actiondecoder, action_decoder_actiondecoder_decode, action_decoder_actiondecoder_init]]
- 5 edges to [[_COMMUNITY_abc, base_encode, base_encoder]]
- 3 edges to [[_COMMUNITY_episodic_memory_episode, episodic_memory_episodicmemory, episodic_memory_episodicmemory_recent]]
- 2 edges to [[_COMMUNITY_evals_planner_eval_py, planner_eval_run_planner_eval, planner_search_py]]
- 2 edges to [[_COMMUNITY_alignment_dpo_py, alignment_preferences_py, build_dataset_main]]
- 1 edge to [[_COMMUNITY_adapter_fixed_width, adapter_neuralworldmodeladapter, adapter_neuralworldmodeladapter_predict_vector]]
- 1 edge to [[_COMMUNITY_basehttprequesthandler, decoders_text_decoder_py, filesystem_filesystemtool_read]]

## Top bridge nodes
- [[.execute()_1]] - degree 14, connects to 5 communities
- [[ToolExecutor]] - degree 12, connects to 4 communities
- [[main()_10]] - degree 10, connects to 3 communities
- [[.run()_2]] - degree 9, connects to 2 communities
- [[FilesystemTool]] - degree 9, connects to 2 communities