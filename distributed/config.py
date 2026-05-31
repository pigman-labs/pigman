from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DistributedConfig:
    strategy: str = "single_process"
    nodes: int = 1
    gpus_per_node: int = 0
    mixed_precision: str = "bf16"
    gradient_accumulation_steps: int = 1
    checkpoint_sharding: bool = False

    @property
    def world_size(self) -> int:
        return max(1, self.nodes * max(1, self.gpus_per_node))

