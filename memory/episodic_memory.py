from __future__ import annotations

from dataclasses import dataclass, field
from time import time

from data.schemas import ExecutionResult


@dataclass
class Episode:
    goal: dict
    results: list[ExecutionResult] = field(default_factory=list)
    summary: str = ""
    trace_id: str = ""
    success: bool | None = None
    importance: float = 0.5
    created_at: float = 0.0

    def finish(self, summary: str, success: bool, importance: float | None = None) -> None:
        self.summary = summary
        self.success = success
        if importance is not None:
            self.importance = importance


@dataclass
class EpisodicMemory:
    episodes: list[Episode] = field(default_factory=list)

    def start(self, goal: dict, trace_id: str = "", importance: float = 0.5) -> Episode:
        episode = Episode(goal=goal, trace_id=trace_id, importance=importance, created_at=time())
        self.episodes.append(episode)
        return episode

    def recent(self, limit: int = 5) -> list[Episode]:
        return sorted(self.episodes, key=lambda episode: episode.created_at, reverse=True)[:limit]

    def important(self, limit: int = 5) -> list[Episode]:
        return sorted(self.episodes, key=lambda episode: episode.importance, reverse=True)[:limit]
