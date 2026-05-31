from __future__ import annotations

from dataclasses import dataclass, field

from multi_agent.base import BaseAgent


@dataclass
class AgentRegistry:
    agents: dict[str, BaseAgent] = field(default_factory=dict)

    def add(self, agent: BaseAgent) -> None:
        if agent.name in self.agents:
            raise KeyError(f"agent already registered: {agent.name}")
        self.agents[agent.name] = agent

    def get(self, name: str) -> BaseAgent:
        return self.agents[name]

    def names(self) -> list[str]:
        return sorted(self.agents)

