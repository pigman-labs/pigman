from __future__ import annotations

from dataclasses import asdict

from distributed.config import DistributedConfig


class LaunchPlanner:
    def plan(self, cfg: DistributedConfig) -> dict:
        if cfg.strategy not in {"single_process", "ddp", "fsdp", "deepspeed_zero"}:
            raise ValueError(f"unsupported strategy: {cfg.strategy}")
        return {
            "strategy": cfg.strategy,
            "world_size": cfg.world_size,
            "env": {
                "MIXED_PRECISION": cfg.mixed_precision,
                "GRAD_ACCUM_STEPS": str(cfg.gradient_accumulation_steps),
            },
            "config": asdict(cfg),
        }

