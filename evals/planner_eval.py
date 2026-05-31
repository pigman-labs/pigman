from __future__ import annotations

from planner.search import BeamSearchPlanner, CEMPlanner, LearnedMPCPlanner, MCTSPlanner, SyntheticAction, SyntheticControlWorld


def run_planner_eval() -> dict:
    actions = [SyntheticAction("small", 0.2), SyntheticAction("best", 1.0), SyntheticAction("overshoot", 2.0, risk=0.1)]
    world = SyntheticControlWorld(target=1.0)
    return {
        "mpc": LearnedMPCPlanner(actions, horizon=1).choose(world, 0.0).name,
        "beam": BeamSearchPlanner(actions, width=2, depth=1).choose(world, 0.0).name,
        "mcts": MCTSPlanner(actions, simulations=32).choose(world, 0.0).name,
        "cem_delta": round(CEMPlanner(iterations=3, samples=32).choose_delta(world, 0.0), 2),
    }
