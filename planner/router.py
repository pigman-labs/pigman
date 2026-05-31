from __future__ import annotations

from dynamics.latent_state import BeliefState
from planner.base import Plan
from planner.beam import BeamPlanner
from planner.mpc import MPCPlanner


class PlannerRouter:
    def __init__(self) -> None:
        self.mpc = MPCPlanner()
        self.beam = BeamPlanner()

    def plan(self, belief: BeliefState, goal: dict) -> Plan:
        goal_text = str(goal.get("goal", goal)).lower()
        if any(word in goal_text for word in ("run", "test", "build", "architecture")):
            return self.mpc.plan(belief, goal)
        return self.beam.plan(belief, goal)
