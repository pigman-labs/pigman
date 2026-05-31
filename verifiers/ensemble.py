from __future__ import annotations

from decoders.tool_decoder import ToolCall
from state.action import AgentAction
from verifiers.base import VerificationResult
from verifiers.policy import PolicyVerifier
from verifiers.safety import SafetyVerifier
from verifiers.tool import ToolVerifier


class VerifierEnsemble:
    def __init__(self) -> None:
        self.safety = SafetyVerifier()
        self.tool = ToolVerifier()
        self.policy = PolicyVerifier()

    def check(self, action: AgentAction, call: ToolCall) -> VerificationResult:
        result = VerificationResult.pass_("ensemble")
        for item in [self.safety.check(action), self.policy.check(action), self.tool.check(call)]:
            result = result.merge(item)
        return result
