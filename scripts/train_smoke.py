from __future__ import annotations

from training.loops.pretrain_jepa import run_pretrain_smoke
from training.loops.train_dynamics import train_dynamics_smoke
from training.loops.train_planner import train_planner_smoke


def main() -> None:
    print(
        {
            "jepa": run_pretrain_smoke(),
            "dynamics": train_dynamics_smoke(),
            "planner": train_planner_smoke(),
        }
    )


if __name__ == "__main__":
    main()
