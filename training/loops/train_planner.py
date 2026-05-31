from __future__ import annotations

from dataclasses import dataclass

from dynamics.latent_state import BeliefState, LatentState
from planner.router import PlannerRouter


@dataclass(frozen=True)
class PlannerTrainStats:
    goals: int
    executable_actions: int


def train_planner_smoke() -> PlannerTrainStats:
    planner = PlannerRouter()
    belief = BeliefState(LatentState())
    goals = [{"goal": "run tests"}, {"goal": "explain architecture"}]
    plans = [planner.plan(belief, goal) for goal in goals]
    return PlannerTrainStats(
        goals=len(goals),
        executable_actions=sum(1 for plan in plans for action in plan.actions if action.type != "say"),
    )
