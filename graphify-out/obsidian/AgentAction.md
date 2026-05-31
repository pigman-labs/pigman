---
source_file: "state/action.py"
type: "code"
community: "action_agentaction, action_agentaction_to_record, action_policy_actionpolicy"
location: "L22"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/action_agentaction,_action_agentaction_to_record,_action_policy_actionpolicy
---

# AgentAction

## Connections
- [[.plan()_2]] - `calls` [INFERRED]
- [[.plan()_3]] - `calls` [INFERRED]
- [[.propose()]] - `calls` [INFERRED]
- [[.select_next()]] - `calls` [INFERRED]
- [[.to_record()]] - `method` [EXTRACTED]
- [[ActionDecoder]] - `uses` [INFERRED]
- [[ActionPolicy]] - `uses` [INFERRED]
- [[ActionProposer]] - `uses` [INFERRED]
- [[ActionRecord]] - `uses` [INFERRED]
- [[BeamPlanner]] - `uses` [INFERRED]
- [[MPCPlanner]] - `uses` [INFERRED]
- [[Plan]] - `uses` [INFERRED]
- [[Planner_1]] - `uses` [INFERRED]
- [[RiskModel]] - `uses` [INFERRED]
- [[SafetyVerifier]] - `uses` [INFERRED]
- [[ToolCall]] - `uses` [INFERRED]
- [[ToolDecoder]] - `uses` [INFERRED]
- [[VerifierEnsemble]] - `uses` [INFERRED]
- [[action.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/action_agentaction,_action_agentaction_to_record,_action_policy_actionpolicy