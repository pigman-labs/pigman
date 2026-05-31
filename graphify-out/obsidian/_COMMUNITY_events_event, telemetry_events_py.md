---
type: community
cohesion: 1.00
members: 2
---

# events_event, telemetry_events_py

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[Event]] - code - telemetry/events.py
- [[events.py]] - code - telemetry/events.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/events_event,_telemetry_events_py
SORT file.name ASC
```
