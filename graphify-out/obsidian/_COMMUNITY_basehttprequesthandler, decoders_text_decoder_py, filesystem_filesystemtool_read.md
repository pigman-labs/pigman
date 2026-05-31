---
type: community
cohesion: 0.11
members: 23
---

# basehttprequesthandler, decoders_text_decoder_py, filesystem_filesystemtool_read

**Cohesion:** 0.11 - loosely connected
**Members:** 23 nodes

## Members
- [[.__init__()_13]] - code - serving_api/server.py
- [[.__init__()_12]] - code - serving_api/server.py
- [[.decode()_2]] - code - decoders/text_decoder.py
- [[.do_POST()]] - code - serving_api/server.py
- [[.handle()]] - code - serving_api/server.py
- [[.log_message()]] - code - serving_api/server.py
- [[.read()]] - code - tools/filesystem.py
- [[.request()]] - code - tools/http_api.py
- [[.start_background()]] - code - serving_api/server.py
- [[.stop()]] - code - serving_api/server.py
- [[AgentHandler]] - code - serving_api/server.py
- [[AgentServer]] - code - serving_api/server.py
- [[AgentService]] - code - serving_api/server.py
- [[BaseHTTPRequestHandler]] - code
- [[HttpApiTool]] - code - tools/http_api.py
- [[HttpResult]] - code - tools/http_api.py
- [[TextDecoder]] - code - decoders/text_decoder.py
- [[http_api.py]] - code - tools/http_api.py
- [[main()_4]] - code - scripts/serve_api.py
- [[serve_api.py]] - code - scripts/serve_api.py
- [[server.py]] - code - serving_api/server.py
- [[test_serving_api_service_smoke()]] - code - tests/unit/test_frontier_subsystems.py
- [[text_decoder.py]] - code - decoders/text_decoder.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/basehttprequesthandler,_decoders_text_decoder_py,_filesystem_filesystemtool_read
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_action_agentaction, action_agentaction_to_record, action_policy_actionpolicy]]
- 3 edges to [[_COMMUNITY_action_decoder_actiondecoder, action_decoder_actiondecoder_decode, action_decoder_actiondecoder_init]]
- 2 edges to [[_COMMUNITY_activations_l2_normalize, activations_tanh, activations_tanh_grad]]
- 1 edge to [[_COMMUNITY_agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier]]
- 1 edge to [[_COMMUNITY_episodic_memory_episode, episodic_memory_episodicmemory, episodic_memory_episodicmemory_recent]]
- 1 edge to [[_COMMUNITY_abc, base_encode, base_encoder]]
- 1 edge to [[_COMMUNITY_alignment_dpo_py, alignment_preferences_py, build_dataset_main]]

## Top bridge nodes
- [[.do_POST()]] - degree 6, connects to 3 communities
- [[.handle()]] - degree 5, connects to 2 communities
- [[.decode()_2]] - degree 4, connects to 2 communities
- [[AgentServer]] - degree 6, connects to 1 community
- [[AgentHandler]] - degree 5, connects to 1 community