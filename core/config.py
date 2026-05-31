from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class RuntimeConfig:
    seed: int = 7
    device: str = "cpu"
    precision: str = "bf16"
    max_rollout_horizon: int = 8
    verification_required: bool = True


@dataclass
class ModelConfig:
    latent_dim: int = 4096
    entity_slots: int = 256
    moe_experts: int = 16
    top_k_experts: int = 2
    use_state_space_layers: bool = True


@dataclass
class AgentConfig:
    runtime: RuntimeConfig = field(default_factory=RuntimeConfig)
    model: ModelConfig = field(default_factory=ModelConfig)


def load_yaml(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        lines = handle.readlines()

    data: dict[str, Any] = {}
    current_list_key: str | None = None

    for raw_line in lines:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- ") and current_list_key:
            data[current_list_key].append(line[2:].strip())
            continue
        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            data[key] = []
            current_list_key = key
            continue

        current_list_key = None
        data[key] = _parse_scalar(value)

    return data


def _parse_scalar(value: str) -> Any:
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value
