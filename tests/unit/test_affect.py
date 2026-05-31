from affect.curriculum import CurriculumEngine
from affect.dynamics import AffectDynamics
from affect.engine import AffectEngine
from affect.intrinsic_reward import IntrinsicReward
from affect.policy import AffectPolicyModulator
from affect.salience import MemorySalience
from affect.state import AffectInputs, AffectState
from affect.trust import TrustLedger
from serving.runtime import AgentRuntime


def test_affect_state_is_bounded() -> None:
    state = AffectState(happiness=2.0, fear=-1.0).bounded()
    assert state.happiness == 1.0
    assert state.fear == 0.0


def test_surprise_and_success_update_affect() -> None:
    updated = AffectDynamics().update(
        AffectState(),
        AffectInputs(prediction_error=0.9, verifier_success=True, novelty=0.8, risk=0.1, goal_progress=1.0),
    )
    assert updated.surprise > 0.0
    assert updated.curiosity > 0.5
    assert updated.happiness >= 0.5
    assert updated.fear < 0.25


def test_failure_increases_frustration_and_fear() -> None:
    updated = AffectDynamics().update(
        AffectState(),
        AffectInputs(verifier_success=False, risk=0.8, coping_capacity=0.2, repeated_failures=3, goal_blockage=0.8),
    )
    assert updated.frustration > 0.0
    assert updated.fear > 0.1
    assert updated.anger > 0.0


def test_intrinsic_reward_penalizes_fear() -> None:
    reward = IntrinsicReward()
    curious = reward.compute(AffectState(curiosity=0.9, fear=0.0, frustration=0.0))
    afraid = reward.compute(AffectState(curiosity=0.9, fear=0.9, frustration=0.0))
    assert curious > afraid


def test_trust_ledger_updates_entity_score() -> None:
    ledger = TrustLedger()
    low = ledger.update("shell", competence=0.0, risk=0.8)
    high = ledger.update("shell", competence=1.0, integrity=1.0, risk=0.1)
    assert high > low


def test_salience_increases_with_affect_delta() -> None:
    salience = MemorySalience().score(
        AffectState(),
        AffectState(surprise=0.9, curiosity=0.8, frustration=0.4),
    )
    assert salience > 0.3


def test_curriculum_reacts_to_affect() -> None:
    engine = CurriculumEngine()
    assert engine.decide(AffectState(fear=0.8)).action == "reduce_risk"
    assert engine.decide(AffectState(boredom=0.8, curiosity=0.2)).action == "increase_novelty"
    assert engine.decide(AffectState(curiosity=0.8, fear=0.1)).action == "increase_difficulty"


def test_policy_modulator_suppresses_risky_actions_when_afraid() -> None:
    modulator = AffectPolicyModulator()
    safe = modulator.score_action(1.0, risk=0.0, novelty=0.5, state=AffectState(fear=0.8))
    risky = modulator.score_action(1.0, risk=1.0, novelty=0.5, state=AffectState(fear=0.8))
    assert safe > risky


def test_affect_engine_returns_full_update_result() -> None:
    result = AffectEngine().update(
        AffectInputs(prediction_error=0.5, novelty=0.7, verifier_success=True, risk=0.1),
        entity="pytest",
    )
    assert result.intrinsic_reward != 0.0
    assert 0.0 <= result.memory_salience <= 1.0
    assert result.curriculum.action in {
        "reduce_risk",
        "switch_strategy",
        "increase_novelty",
        "increase_difficulty",
        "consolidate_skill",
        "continue",
    }


def test_runtime_records_affect() -> None:
    runtime = AgentRuntime()
    result = runtime.step({"goal": "explain architecture"})
    affect = result["affect"]
    assert affect.after.as_dict() == runtime.belief.current.global_state["affect"]
    assert "intrinsic_reward" in runtime.belief.current.global_state
    assert runtime.trajectory.events[-1]["memory_salience"] == affect.memory_salience
