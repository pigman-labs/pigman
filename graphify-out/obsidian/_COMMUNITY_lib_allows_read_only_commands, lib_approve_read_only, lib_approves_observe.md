---
type: community
cohesion: 0.15
members: 15
---

# lib_allows_read_only_commands, lib_approve_read_only, lib_approves_observe

**Cohesion:** 0.15 - loosely connected
**Members:** 15 nodes

## Members
- [[Permission]] - code - tool_sandbox_rs/lib.rs
- [[RuntimeAction]] - code - runtime_rs/lib.rs
- [[RuntimeDecision]] - code - runtime_rs/lib.rs
- [[allows_read_only_commands()]] - code - tool_sandbox_rs/lib.rs
- [[approve_read_only()]] - code - runtime_rs/lib.rs
- [[approves_observe()]] - code - runtime_rs/lib.rs
- [[asks_for_pushes()]] - code - tool_sandbox_rs/lib.rs
- [[classify_command()]] - code - tool_sandbox_rs/lib.rs
- [[denies_destructive_commands()]] - code - tool_sandbox_rs/lib.rs
- [[lib.rs_1]] - code - runtime_rs/lib.rs
- [[lib.rs_2]] - code - tool_sandbox_rs/lib.rs
- [[main()]] - code - tool_sandbox_rs/main.rs
- [[main.rs]] - code - runtime_rs/main.rs
- [[main.rs_1]] - code - tool_sandbox_rs/main.rs
- [[rejects_write_action()]] - code - runtime_rs/lib.rs

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/lib_allows_read_only_commands,_lib_approve_read_only,_lib_approves_observe
SORT file.name ASC
```
