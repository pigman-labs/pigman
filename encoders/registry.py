from __future__ import annotations

from data.schemas import Observation
from encoders.base import Encoder
from encoders.file_encoder import FileEncoder
from encoders.text_encoder import TextEncoder
from encoders.tool_trace_encoder import ToolTraceEncoder


class EncoderRegistry:
    def __init__(self) -> None:
        self._encoders: dict[str, Encoder] = {
            "user_text": TextEncoder(),
            "file": FileEncoder(),
            "shell": ToolTraceEncoder(),
            "api": ToolTraceEncoder(),
            "browser": ToolTraceEncoder(),
            "simulator": ToolTraceEncoder(),
        }

    def encode(self, observation: Observation):
        encoder = self._encoders.get(observation.source)
        if encoder is None:
            encoder = TextEncoder()
        return encoder.encode_observation(observation)
