---
type: community
cohesion: 0.40
members: 6
---

# config_agentconfig, config_load_yaml, config_modelconfig

**Cohesion:** 0.40 - moderately connected
**Members:** 6 nodes

## Members
- [[AgentConfig]] - code - core/config.py
- [[ModelConfig]] - code - core/config.py
- [[RuntimeConfig]] - code - core/config.py
- [[_parse_scalar()]] - code - core/config.py
- [[config.py]] - code - core/config.py
- [[load_yaml()]] - code - core/config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/config_agentconfig,_config_load_yaml,_config_modelconfig
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_action_agentaction, action_agentaction_to_record, action_policy_actionpolicy]]

## Top bridge nodes
- [[load_yaml()]] - degree 3, connects to 1 community