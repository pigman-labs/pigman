from __future__ import annotations

from dataclasses import dataclass

from neural.jepa_model import TrainableJEPA
from neural.optim import OptimizerConfig
from neural.synthetic_data import SyntheticWorldDataset


@dataclass(frozen=True)
class NeuralTrainReport:
    initial_loss: float
    final_loss: float
    improvement: float
    checkpoint: str


def train_neural_jepa(
    steps: int = 250,
    batch_size: int = 64,
    checkpoint: str = "artifacts/checkpoints/neural_jepa.npz",
) -> NeuralTrainReport:
    dataset = SyntheticWorldDataset()
    model = TrainableJEPA()
    cfg = OptimizerConfig(lr=0.08, weight_decay=1e-5, ema_tau=0.98)

    initial_loss = None
    final_loss = 0.0
    for step in range(steps):
        batch = dataset.batch(batch_size)
        stats = model.train_step(batch.context, batch.action, batch.target, cfg)
        if step == 0:
            initial_loss = stats.loss
        final_loss = stats.loss

    if initial_loss is None:
        initial_loss = final_loss

    model.save(checkpoint)
    return NeuralTrainReport(
        initial_loss=initial_loss,
        final_loss=final_loss,
        improvement=initial_loss - final_loss,
        checkpoint=checkpoint,
    )
