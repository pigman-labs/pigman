---
source_file: "scripts/verify_all.py"
type: "code"
community: "agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier"
location: "L10"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/agent_eval_run_agent_eval,_agent_loop_agentloop_run,_code_codeverifier
---

# main()

## Connections
- [[.compile_python()]] - `calls` [INFERRED]
- [[.pytest()]] - `calls` [INFERRED]
- [[.run()_2]] - `calls` [INFERRED]
- [[CodeVerifier]] - `calls` [INFERRED]
- [[ShellTool]] - `calls` [INFERRED]
- [[TorchModelConfig]] - `calls` [INFERRED]
- [[TorchTrainConfig]] - `calls` [INFERRED]
- [[train_jepa_torch()]] - `calls` [INFERRED]
- [[train_neural_jepa()]] - `calls` [INFERRED]
- [[verify_all.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/agent_eval_run_agent_eval,_agent_loop_agentloop_run,_code_codeverifier