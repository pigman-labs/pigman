from __future__ import annotations

from decoders.tool_decoder import ToolCall, ToolDecoder
from state.action import AgentAction


class ActionDecoder:
    def __init__(self) -> None:
        self.tool_decoder = ToolDecoder()

    def decode(self, action: AgentAction) -> ToolCall:
        return self.tool_decoder.decode(action)
