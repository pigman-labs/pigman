from __future__ import annotations

import argparse

from training.loops.train_joint_world_model import train_joint_world_model


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=100)
    args = parser.parse_args()
    print(train_joint_world_model(args.steps))


if __name__ == "__main__":
    main()
