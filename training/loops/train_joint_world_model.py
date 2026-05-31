from __future__ import annotations

from dataclasses import dataclass

from torch_backend.config import TorchModelConfig, TorchTrainConfig
from training.loops.train_torch_dynamics import TorchDynamicsReport, train_dynamics_torch
from training.loops.train_torch_jepa import TorchTrainReport, train_jepa_torch


@dataclass(frozen=True)
class JointWorldModelReport:
    jepa: TorchTrainReport
    dynamics: TorchDynamicsReport


def train_joint_world_model(steps: int = 100) -> JointWorldModelReport:
    model_cfg = TorchModelConfig()
    jepa = train_jepa_torch(TorchTrainConfig(steps=steps, checkpoint="artifacts/checkpoints/joint_torch_jepa.pt", metrics_path="artifacts/runs/joint_torch_jepa.jsonl"), model_cfg)
    dynamics = train_dynamics_torch(TorchTrainConfig(steps=steps, checkpoint="artifacts/checkpoints/joint_torch_dynamics.pt", metrics_path="artifacts/runs/joint_torch_dynamics.jsonl"), model_cfg)
    return JointWorldModelReport(jepa=jepa, dynamics=dynamics)

