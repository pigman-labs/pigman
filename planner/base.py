from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from dynamics.latent_state import BeliefState
from state.action import AgentAction


@dataclass(frozen=True)
class Plan:
    actions: list[AgentAction]
    score: float
    risk: float
    rationale: str
    predicted_outcomes: list[dict] | None = None


class Planner(ABC):
    @abstractmethod
    def plan(self, belief: BeliefState, goal: dict) -> Plan:
        raise NotImplementedError
