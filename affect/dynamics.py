from __future__ import annotations

from dataclasses import dataclass

from affect.state import AffectInputs, AffectState, clamp01


@dataclass(frozen=True)
class AffectDynamicsConfig:
    inertia: float = 0.82
    surprise_gain: float = 0.85
    curiosity_gain: float = 0.7
    fear_gain: float = 0.8
    boredom_decay_from_novelty: float = 0.65
    frustration_gain: float = 0.12
    anger_gain: float = 0.5
    trust_gain: float = 0.18
    happiness_gain: float = 0.35
    greed_gain: float = 0.15
    bond_gain: float = 0.12


class AffectDynamics:
    """Bounded, interpretable MANU affect update.

    This is computational affect: control variables for motivation and safety,
    not a claim that the system literally feels.
    """

    def __init__(self, config: AffectDynamicsConfig | None = None) -> None:
        self.config = config or AffectDynamicsConfig()

    def update(self, state: AffectState, inputs: AffectInputs) -> AffectState:
        c = self.config
        threat = clamp01(inputs.risk * (1.0 - inputs.coping_capacity))
        success = 1.0 if inputs.verifier_success is True else 0.0
        failure = 1.0 if inputs.verifier_success is False else 0.0
        learning_progress = clamp01(inputs.learning_progress * 4.0)
        safe_surprise = clamp01(inputs.prediction_error) * (1.0 - threat)
        novelty = clamp01(inputs.novelty)
        blockage = clamp01(inputs.goal_blockage)
        repeated_failure_pressure = clamp01(inputs.repeated_failures / 5.0)
        reward_prediction = inputs.immediate_reward - inputs.delayed_reward / max(1.0, inputs.delay)

        target = AffectState(
            happiness=clamp01(0.45 + c.happiness_gain * (success + inputs.goal_progress + reward_prediction) - 0.25 * failure),
            curiosity=clamp01(0.25 + c.curiosity_gain * max(learning_progress, safe_surprise, novelty) - 0.35 * threat),
            greed=clamp01(state.greed + c.greed_gain * max(0.0, inputs.immediate_reward - inputs.delayed_reward)),
            fear=clamp01(c.fear_gain * threat + 0.2 * failure),
            anger=clamp01(c.anger_gain * blockage * (0.5 + repeated_failure_pressure)),
            trust=clamp01(state.trust + c.trust_gain * inputs.trust_signal + 0.08 * success - 0.12 * failure),
            boredom=clamp01(0.55 * (1.0 - novelty) - c.boredom_decay_from_novelty * learning_progress),
            surprise=clamp01(c.surprise_gain * inputs.prediction_error),
            bond=clamp01(state.bond + c.bond_gain * inputs.bond_signal + 0.04 * success),
            frustration=clamp01(c.frustration_gain * inputs.repeated_failures + 0.35 * failure + 0.25 * blockage),
        )

        return self._blend(state, target, c.inertia).bounded()

    def _blend(self, old: AffectState, target: AffectState, inertia: float) -> AffectState:
        values = [
            inertia * old_value + (1.0 - inertia) * target_value
            for old_value, target_value in zip(old.vector(), target.vector(), strict=True)
        ]
        return AffectState(*values)

