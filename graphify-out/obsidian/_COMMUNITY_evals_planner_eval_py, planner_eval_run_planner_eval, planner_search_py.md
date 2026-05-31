---
type: community
cohesion: 0.13
members: 27
---

# evals_planner_eval_py, planner_eval_run_planner_eval, planner_search_py

**Cohesion:** 0.13 - loosely connected
**Members:** 27 nodes

## Members
- [[.__init__()_16]] - code - planner/search.py
- [[.__init__()_18]] - code - planner/search.py
- [[.__init__()_15]] - code - planner/search.py
- [[.__init__()_17]] - code - planner/search.py
- [[.__init__()_14]] - code - planner/search.py
- [[.__post_init__()]] - code - planner/search.py
- [[._backprop()]] - code - planner/search.py
- [[._expand()]] - code - planner/search.py
- [[._rollout()]] - code - planner/search.py
- [[._select()]] - code - planner/search.py
- [[.choose()_1]] - code - planner/search.py
- [[.choose()]] - code - planner/search.py
- [[.choose()_2]] - code - planner/search.py
- [[.choose_delta()]] - code - planner/search.py
- [[.forward()_5]] - code - torch_backend/world_model.py
- [[.step()_1]] - code - planner/search.py
- [[.value()]] - code - planner/search.py
- [[BeamSearchPlanner]] - code - planner/search.py
- [[CEMPlanner]] - code - planner/search.py
- [[LearnedMPCPlanner]] - code - planner/search.py
- [[MCTSNode]] - code - planner/search.py
- [[MCTSPlanner]] - code - planner/search.py
- [[SyntheticAction]] - code - planner/search.py
- [[SyntheticControlWorld]] - code - planner/search.py
- [[planner_eval.py]] - code - evals/planner_eval.py
- [[run_planner_eval()]] - code - evals/planner_eval.py
- [[search.py]] - code - planner/search.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/evals_planner_eval_py,_planner_eval_run_planner_eval,_planner_search_py
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier]]
- 2 edges to [[_COMMUNITY_action_agentaction, action_agentaction_to_record, action_policy_actionpolicy]]
- 1 edge to [[_COMMUNITY_activations_l2_normalize, activations_tanh, activations_tanh_grad]]

## Top bridge nodes
- [[run_planner_eval()]] - degree 11, connects to 1 community
- [[._expand()]] - degree 5, connects to 1 community
- [[.choose()_1]] - degree 4, connects to 1 community
- [[.forward()_5]] - degree 2, connects to 1 community