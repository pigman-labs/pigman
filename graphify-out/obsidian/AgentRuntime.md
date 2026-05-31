---
source_file: "serving/runtime.py"
type: "code"
community: "action_agentaction, action_agentaction_to_record, action_policy_actionpolicy"
location: "L22"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/action_agentaction,_action_agentaction_to_record,_action_policy_actionpolicy
---

# AgentRuntime

## Connections
- [[.__init__()_1]] - `method` [EXTRACTED]
- [[.__init__()_12]] - `calls` [INFERRED]
- [[.__init__()_31]] - `calls` [INFERRED]
- [[.observe_text()]] - `method` [EXTRACTED]
- [[.step()]] - `method` [EXTRACTED]
- [[ActionDecoder]] - `uses` [INFERRED]
- [[ActionPolicy]] - `uses` [INFERRED]
- [[AgentHandler]] - `uses` [INFERRED]
- [[AgentLoop]] - `uses` [INFERRED]
- [[AgentLoopResult]] - `uses` [INFERRED]
- [[AgentServer]] - `uses` [INFERRED]
- [[AgentService]] - `uses` [INFERRED]
- [[BeliefState]] - `uses` [INFERRED]
- [[BeliefUpdater]] - `uses` [INFERRED]
- [[CausalGraph]] - `uses` [INFERRED]
- [[CausalLearner]] - `uses` [INFERRED]
- [[EncoderRegistry]] - `uses` [INFERRED]
- [[LatentState]] - `uses` [INFERRED]
- [[MemorySystem]] - `uses` [INFERRED]
- [[Observation]] - `uses` [INFERRED]
- [[PlannerRouter]] - `uses` [INFERRED]
- [[ToolExecutor]] - `uses` [INFERRED]
- [[TrajectoryLog]] - `uses` [INFERRED]
- [[VerifierEnsemble]] - `uses` [INFERRED]
- [[WorldModel]] - `uses` [INFERRED]
- [[main()_1]] - `calls` [INFERRED]
- [[main()_8]] - `calls` [INFERRED]
- [[run_agent_eval()]] - `calls` [INFERRED]
- [[run_benchmark()]] - `calls` [INFERRED]
- [[runtime.py]] - `contains` [EXTRACTED]
- [[test_runtime_step()]] - `calls` [INFERRED]
- [[test_world_state_verifier_accepts_runtime_state()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/action_agentaction,_action_agentaction_to_record,_action_policy_actionpolicy