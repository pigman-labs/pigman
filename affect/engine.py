from __future__ import annotations

from dataclasses import dataclass

from affect.curriculum import CurriculumDecision, CurriculumEngine
from affect.dynamics import AffectDynamics
from affect.intrinsic_reward import IntrinsicReward
from affect.salience import MemorySalience, SalienceInputs
from affect.state import AffectInputs, AffectState
from affect.trust import TrustLedger


@dataclass(frozen=True)
class AffectUpdateResult:
    before: AffectState
    after: AffectState
    intrinsic_reward: float
    memory_salience: float
    curriculum: CurriculumDecision


class AffectEngine:
    def __init__(self) -> None:
        self.dynamics = AffectDynamics()
        self.reward = IntrinsicReward()
        self.salience = MemorySalience()
        self.curriculum = CurriculumEngine()
        self.trust = TrustLedger()
        self.state = AffectState()

    def update(self, inputs: AffectInputs, *, entity: str | None = None) -> AffectUpdateResult:
        before = self.state
        if entity is not None:
            trust_score = self.trust.update(
                entity,
                competence=1.0 if inputs.verifier_success else 0.2 if inputs.verifier_success is False else 0.5,
                risk=inputs.risk,
            )
            inputs = AffectInputs(**{**inputs.__dict__, "trust_signal": trust_score - before.trust})
        after = self.dynamics.update(before, inputs)
        self.state = after
        intrinsic_reward = self.reward.compute(after)
        memory_salience = self.salience.score(
            before,
            after,
            SalienceInputs(
                verifier_impact=1.0 if inputs.verifier_success is not None else 0.0,
                novelty=inputs.novelty,
            ),
        )
        curriculum = self.curriculum.decide(after)
        return AffectUpdateResult(before, after, intrinsic_reward, memory_salience, curriculum)

