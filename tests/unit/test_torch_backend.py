from pathlib import Path

import torch

from neural.synthetic_data import SyntheticWorldDataset
from torch_backend.config import TorchModelConfig, TorchTrainConfig
from torch_backend.world_model import TorchJEPAModel, TorchLatentDynamics
from training.loops.train_torch_dynamics import train_dynamics_torch
from training.loops.train_torch_jepa import train_jepa_torch


def test_torch_jepa_forward_shapes() -> None:
    cfg = TorchModelConfig(latent_dim=16, hidden_dim=32, depth=1)
    model = TorchJEPAModel(cfg)
    batch = SyntheticWorldDataset(cfg.input_dim, cfg.action_dim).batch(4)
    output = model(
        torch.tensor(batch.context, dtype=torch.float32),
        torch.tensor(batch.action, dtype=torch.float32),
        torch.tensor(batch.target, dtype=torch.float32),
    )
    assert output["prediction"].shape == (4, cfg.latent_dim)
    assert output["target"].shape == (4, cfg.latent_dim)


def test_torch_dynamics_forward_shapes() -> None:
    cfg = TorchModelConfig(latent_dim=16, hidden_dim=32, depth=1)
    model = TorchLatentDynamics(cfg)
    output = model(torch.randn(4, cfg.latent_dim), torch.randn(4, cfg.action_dim))
    assert output["next_state"].shape == (4, cfg.latent_dim)
    assert output["value"].shape == (4,)
    assert output["risk"].shape == (4,)


def test_torch_training_writes_checkpoints(tmp_path: Path) -> None:
    jepa_report = train_jepa_torch(
        TorchTrainConfig(
            steps=3,
            batch_size=8,
            checkpoint=str(tmp_path / "jepa.pt"),
            metrics_path=str(tmp_path / "jepa.jsonl"),
        ),
        TorchModelConfig(latent_dim=16, hidden_dim=32, depth=1),
    )
    dyn_report = train_dynamics_torch(
        TorchTrainConfig(
            steps=3,
            batch_size=8,
            checkpoint=str(tmp_path / "dyn.pt"),
            metrics_path=str(tmp_path / "dyn.jsonl"),
        ),
        TorchModelConfig(latent_dim=16, hidden_dim=32, depth=1),
    )
    assert Path(jepa_report.checkpoint).exists()
    assert Path(dyn_report.checkpoint).exists()

