from __future__ import annotations

import argparse

from training.loops.train_neural_jepa import train_neural_jepa


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=250)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--checkpoint", default="artifacts/checkpoints/neural_jepa.npz")
    args = parser.parse_args()

    report = train_neural_jepa(args.steps, args.batch_size, args.checkpoint)
    print(report)
    if report.final_loss >= 0.2:
        raise SystemExit("training did not reach the expected loss threshold")


if __name__ == "__main__":
    main()
