from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from orchestration.agent_loop import AgentLoop


loop = AgentLoop()
print(loop.run_once({"goal": "demo"}))
