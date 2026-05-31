from __future__ import annotations

from dataclasses import dataclass

from affect.state import AffectState


@dataclass(frozen=True)
class CurriculumDecision:
    action: str
    difficulty_delta: float
    reason: str


class CurriculumEngine:
    def decide(self, state: AffectState, current_difficulty: float = 0.5) -> CurriculumDecision:
        if state.fear > 0.65:
            return CurriculumDecision("reduce_risk", -0.15, "fear is high; prefer safer probes")
        if state.frustration > 0.6:
            return CurriculumDecision("switch_strategy", -0.05, "frustration is high; retrieve alternate skill")
        if state.boredom > 0.55 and state.curiosity < 0.5:
            return CurriculumDecision("increase_novelty", 0.15, "boredom is high; introduce novelty")
        if state.curiosity > 0.65 and state.fear < 0.4:
            return CurriculumDecision("increase_difficulty", 0.10, "curiosity is high and risk is manageable")
        if state.happiness > 0.65 and state.trust > 0.55:
            return CurriculumDecision("consolidate_skill", 0.0, "successful state; consolidate current skill")
        return CurriculumDecision("continue", 0.0, f"maintain difficulty {current_difficulty:.2f}")

