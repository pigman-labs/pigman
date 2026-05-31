from __future__ import annotations

from affect.state import AffectState


class AffectPolicyModulator:
    def score_action(self, base_score: float, risk: float, novelty: float, state: AffectState) -> float:
        curiosity_bonus = state.curiosity * novelty * (1.0 - state.fear)
        fear_penalty = state.fear * risk
        frustration_penalty = state.frustration * 0.2
        boredom_bonus = state.boredom * novelty * 0.3
        trust_bonus = state.trust * 0.05
        return base_score + curiosity_bonus + boredom_bonus + trust_bonus - fear_penalty - frustration_penalty

