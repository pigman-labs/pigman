from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AgentBudget:
    max_steps: int = 8
    max_risk: float = 3.0
    steps_used: int = 0
    risk_used: float = 0.0

    def allow(self) -> bool:
        return self.steps_used < self.max_steps and self.risk_used <= self.max_risk

    def consume(self, risk: float = 0.0) -> None:
        self.steps_used += 1
        self.risk_used += max(0.0, float(risk))

    def snapshot(self) -> dict:
        return {
            "max_steps": self.max_steps,
            "max_risk": self.max_risk,
            "steps_used": self.steps_used,
            "risk_used": self.risk_used,
            "allowed": self.allow(),
        }


class BudgetManager:
    def __init__(self, default: AgentBudget | None = None) -> None:
        self.default = default or AgentBudget()
        self._budgets: dict[str, AgentBudget] = {}

    def set(self, agent: str, budget: AgentBudget) -> None:
        self._budgets[agent] = budget

    def get(self, agent: str) -> AgentBudget:
        if agent not in self._budgets:
            self._budgets[agent] = AgentBudget(self.default.max_steps, self.default.max_risk)
        return self._budgets[agent]

    def allow(self, agent: str) -> bool:
        return self.get(agent).allow()

    def consume(self, agent: str, risk: float = 0.0) -> None:
        self.get(agent).consume(risk)

    def snapshot(self) -> dict[str, dict]:
        return {agent: budget.snapshot() for agent, budget in sorted(self._budgets.items())}
