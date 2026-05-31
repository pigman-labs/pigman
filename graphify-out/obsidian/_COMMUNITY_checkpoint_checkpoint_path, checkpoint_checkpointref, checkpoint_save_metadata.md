---
type: community
cohesion: 0.50
members: 4
---

# checkpoint_checkpoint_path, checkpoint_checkpointref, checkpoint_save_metadata

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[CheckpointRef]] - code - core/checkpoint.py
- [[checkpoint.py]] - code - core/checkpoint.py
- [[checkpoint_path()]] - code - core/checkpoint.py
- [[save_metadata()]] - code - core/checkpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/checkpoint_checkpoint_path,_checkpoint_checkpointref,_checkpoint_save_metadata
SORT file.name ASC
```
