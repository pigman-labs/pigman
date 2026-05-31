from __future__ import annotations

import argparse

from torch_backend.config import TorchTrainConfig
from training.loops.train_torch_dynamics import train_dynamics_torch


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=200)
    parser.add_argument("--device", default="auto")
    args = parser.parse_args()
    print(
        train_dynamics_torch(
            TorchTrainConfig(
                steps=args.steps,
                device=args.device,
                checkpoint="artifacts/checkpoints/torch_dynamics.pt",
                metrics_path="artifacts/runs/torch_dynamics_metrics.jsonl",
            )
        )
    )


if __name__ == "__main__":
    main()
