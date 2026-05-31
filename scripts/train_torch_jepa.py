from __future__ import annotations

import argparse

from torch_backend.config import TorchTrainConfig
from training.loops.train_torch_jepa import train_jepa_torch


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=200)
    parser.add_argument("--device", default="auto")
    args = parser.parse_args()
    print(train_jepa_torch(TorchTrainConfig(steps=args.steps, device=args.device)))


if __name__ == "__main__":
    main()

