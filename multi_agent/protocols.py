from __future__ import annotations

from dataclasses import dataclass

from multi_agent.messages import AgentResult


@dataclass(frozen=True)
class Vote:
    agent: str
    score: float
    reason: str


class DebateProtocol:
    def rank(self, results: list[AgentResult]) -> list[Vote]:
        votes = []
        for result in results:
            score = result.confidence - result.risk + (0.2 if result.ok else -0.5)
            votes.append(Vote(result.agent, score, result.summary))
        return sorted(votes, key=lambda vote: vote.score, reverse=True)


class MergeProtocol:
    def merge(self, results: list[AgentResult]) -> dict:
        return {
            "ok": all(result.ok for result in results if result.agent != "safety_governor"),
            "summaries": [result.summary for result in results],
            "payloads": {result.agent: result.payload for result in results},
            "confidence": sum(result.confidence for result in results) / max(1, len(results)),
            "risk": max((result.risk for result in results), default=0.0),
        }

