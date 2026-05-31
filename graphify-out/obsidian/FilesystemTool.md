---
source_file: "tools/filesystem.py"
type: "code"
community: "agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier"
location: "L7"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/agent_eval_run_agent_eval,_agent_loop_agentloop_run,_code_codeverifier
---

# FilesystemTool

## Connections
- [[.__init__()]] - `calls` [INFERRED]
- [[.diff_text()]] - `method` [EXTRACTED]
- [[.list_files()]] - `method` [EXTRACTED]
- [[.read()]] - `method` [EXTRACTED]
- [[.write()]] - `method` [EXTRACTED]
- [[ToolExecutor]] - `uses` [INFERRED]
- [[filesystem.py]] - `contains` [EXTRACTED]
- [[run_tool_eval()]] - `calls` [INFERRED]
- [[test_tool_and_patch()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/agent_eval_run_agent_eval,_agent_loop_agentloop_run,_code_codeverifier