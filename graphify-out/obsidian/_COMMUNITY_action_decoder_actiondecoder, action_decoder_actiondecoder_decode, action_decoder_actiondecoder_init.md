---
type: community
cohesion: 0.08
members: 39
---

# action_decoder_actiondecoder, action_decoder_actiondecoder_decode, action_decoder_actiondecoder_init

**Cohesion:** 0.08 - loosely connected
**Members:** 39 nodes

## Members
- [[.__init__()_29]] - code - decoders/action_decoder.py
- [[.__init__()_22]] - code - verifiers/ensemble.py
- [[.__init__()_2]] - code - core/registry.py
- [[.check()_1]] - code - verifiers/ensemble.py
- [[.check()_2]] - code - verifiers/safety.py
- [[.check()_3]] - code - verifiers/source.py
- [[.check()_4]] - code - verifiers/tool.py
- [[.check()]] - code - verifiers/world_state.py
- [[.decode()]] - code - decoders/action_decoder.py
- [[.decode()_1]] - code - decoders/tool_decoder.py
- [[.get()]] - code - core/registry.py
- [[.names()]] - code - core/registry.py
- [[.plan()_1]] - code - planner/router.py
- [[.register()]] - code - core/registry.py
- [[.route()]] - code - routing/tool_router.py
- [[ActionDecoder]] - code - decoders/action_decoder.py
- [[Registry]] - code - core/registry.py
- [[SafetyVerifier]] - code - verifiers/safety.py
- [[SourceProvenanceVerifier]] - code - verifiers/source.py
- [[ToolCall]] - code - decoders/tool_decoder.py
- [[ToolDecoder]] - code - decoders/tool_decoder.py
- [[ToolRouter]] - code - routing/tool_router.py
- [[ToolVerifier]] - code - verifiers/tool.py
- [[VerificationResult]] - code - verifiers/base.py
- [[VerifierEnsemble]] - code - verifiers/ensemble.py
- [[WorldStateVerifier]] - code - verifiers/world_state.py
- [[action_decoder.py]] - code - decoders/action_decoder.py
- [[base.py_1]] - code - verifiers/base.py
- [[classify_risk()]] - code - security/policy.py
- [[ensemble.py]] - code - verifiers/ensemble.py
- [[policy.py]] - code - security/policy.py
- [[registry.py]] - code - core/registry.py
- [[safety.py]] - code - verifiers/safety.py
- [[source.py]] - code - verifiers/source.py
- [[test_world_state_verifier_accepts_runtime_state()]] - code - tests/unit/test_smoke.py
- [[tool.py]] - code - verifiers/tool.py
- [[tool_decoder.py]] - code - decoders/tool_decoder.py
- [[tool_router.py]] - code - routing/tool_router.py
- [[world_state.py]] - code - verifiers/world_state.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/action_decoder_actiondecoder,_action_decoder_actiondecoder_decode,_action_decoder_actiondecoder_init
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_action_agentaction, action_agentaction_to_record, action_policy_actionpolicy]]
- 8 edges to [[_COMMUNITY_agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier]]
- 3 edges to [[_COMMUNITY_basehttprequesthandler, decoders_text_decoder_py, filesystem_filesystemtool_read]]
- 3 edges to [[_COMMUNITY_abc, base_encode, base_encoder]]
- 1 edge to [[_COMMUNITY_activations_l2_normalize, activations_tanh, activations_tanh_grad]]

## Top bridge nodes
- [[.get()]] - degree 20, connects to 4 communities
- [[test_world_state_verifier_accepts_runtime_state()]] - degree 5, connects to 3 communities
- [[ToolCall]] - degree 7, connects to 2 communities
- [[VerificationResult]] - degree 16, connects to 1 community
- [[VerifierEnsemble]] - degree 10, connects to 1 community