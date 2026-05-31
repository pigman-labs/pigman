---
type: community
cohesion: 0.50
members: 4
---

# browser_browseraction, browser_browsertool, browser_browsertool_execute

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.execute()]] - code - tools/browser.py
- [[BrowserAction]] - code - tools/browser.py
- [[BrowserTool]] - code - tools/browser.py
- [[browser.py]] - code - tools/browser.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/browser_browseraction,_browser_browsertool,_browser_browsertool_execute
SORT file.name ASC
```
