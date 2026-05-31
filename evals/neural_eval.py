from __future__ import annotations

from neural.jepa_model import TrainableJEPA
from neural.synthetic_data import SyntheticWorldDataset


def evaluate_checkpoint(path: str = "artifacts/checkpoints/neural_jepa.npz", batches: int = 8) -> dict:
    model = TrainableJEPA()
    model.load(path)
    dataset = SyntheticWorldDataset(seed=101)
    losses = []
    for _ in range(batches):
        batch = dataset.batch(64)
        pred = model.predict(batch.context, batch.action)
        target = model.encode_target(batch.target)
        losses.append(float(((pred - target) ** 2).mean()))
    return {"loss": sum(losses) / len(losses), "batches": batches, "checkpoint": path}
