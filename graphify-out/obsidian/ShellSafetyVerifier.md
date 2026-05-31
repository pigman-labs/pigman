---
source_file: "verifiers/shell.py"
type: "code"
community: "agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier"
location: "L6"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/agent_eval_run_agent_eval,_agent_loop_agentloop_run,_code_codeverifier
---

# ShellSafetyVerifier

## Connections
- [[.__init__()_25]] - `calls` [INFERRED]
- [[.check_command()]] - `method` [EXTRACTED]
- [[FrontierSafetySuite]] - `uses` [INFERRED]
- [[SafetyCase]] - `uses` [INFERRED]
- [[VerificationResult]] - `uses` [INFERRED]
- [[run_verifier_eval()]] - `calls` [INFERRED]
- [[shell.py_1]] - `contains` [EXTRACTED]
- [[test_shell_safety()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/agent_eval_run_agent_eval,_agent_loop_agentloop_run,_code_codeverifier