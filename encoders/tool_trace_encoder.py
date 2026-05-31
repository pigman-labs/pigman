from __future__ import annotations

from dataclasses import dataclass
from ast import literal_eval
from typing import Any

from encoders.base import Encoder
from kernels.vector_math import stable_hash_embedding


@dataclass(frozen=True)
class ToolTraceLatent:
    command: str
    exit_code: int
    success: bool
    vector: list[float]


class ToolTraceEncoder(Encoder):
    modality = "tool_trace"

    def encode(self, observation: Any) -> ToolTraceLatent:
        if not isinstance(observation, dict):
            try:
                parsed = literal_eval(str(observation))
                observation = parsed if isinstance(parsed, dict) else {"raw": str(observation)}
            except (ValueError, SyntaxError):
                observation = {"raw": str(observation)}

        exit_code = int(observation.get("exit_code", 0))
        return ToolTraceLatent(
            command=str(observation.get("command", "")),
            exit_code=exit_code,
            success=exit_code == 0,
            vector=stable_hash_embedding(str(observation)),
        )
