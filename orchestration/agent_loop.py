from __future__ import annotations

from dataclasses import dataclass

from serving.runtime import AgentRuntime


@dataclass
class AgentLoopResult:
    steps: int
    final_action: object
    approved: bool
    stdout: str = ""


class AgentLoop:
    def __init__(self) -> None:
        self.runtime = AgentRuntime()

    def run_once(self, goal: dict) -> AgentLoopResult:
        result = self.runtime.step(goal)
        return AgentLoopResult(
            steps=1,
            final_action=result["action"],
            approved=result["verification"].approved,
            stdout=result["execution"].stdout if result["execution"] else "",
        )

    def run(self, goal: dict, max_steps: int = 3) -> list[AgentLoopResult]:
        results = []
        for _ in range(max_steps):
            current = self.run_once(goal)
            results.append(current)
            if current.approved and current.stdout:
                break
        return results
