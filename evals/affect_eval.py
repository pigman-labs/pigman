from __future__ import annotations

from affect.engine import AffectEngine
from affect.state import AffectInputs


def run_affect_eval() -> dict:
    engine = AffectEngine()
    success = engine.update(
        AffectInputs(prediction_error=0.7, novelty=0.8, verifier_success=True, risk=0.1, goal_progress=1.0),
        entity="tool:pytest",
    )
    failure = engine.update(
        AffectInputs(
            prediction_error=0.4,
            novelty=0.1,
            verifier_success=False,
            risk=0.7,
            coping_capacity=0.2,
            repeated_failures=2,
            goal_blockage=0.8,
        ),
        entity="tool:dangerous",
    )
    return {
        "success_affect": success.after.as_dict(),
        "failure_affect": failure.after.as_dict(),
        "success_intrinsic_reward": success.intrinsic_reward,
        "failure_intrinsic_reward": failure.intrinsic_reward,
        "failure_curriculum": failure.curriculum.action,
        "salience": failure.memory_salience,
    }

