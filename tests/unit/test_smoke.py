from jepa.ema import ema_update
from jepa.losses import cosine_distance
from serving.runtime import AgentRuntime
from encoders.text_encoder import TextEncoder
from memory.retrieval import MemorySystem
from verifiers.world_state import WorldStateVerifier


def test_cosine_distance_identical_vectors() -> None:
    assert cosine_distance([1.0, 0.0], [1.0, 0.0]) == 0.0


def test_ema_update() -> None:
    assert ema_update(10.0, 0.0, 0.9) == 9.0


def test_runtime_step() -> None:
    runtime = AgentRuntime()
    result = runtime.step({"goal": "explain architecture"})
    assert result["verification"].approved is True


def test_text_encoder_has_vector() -> None:
    latent = TextEncoder().encode("run tests")
    assert latent.intent == "execute_or_verify"
    assert len(latent.vector) == 64


def test_memory_retrieval() -> None:
    memory = MemorySystem()
    memory.add_trace("t1", "pytest passed", {"ok": True})
    bundle = memory.retrieve("pytest")
    assert bundle.vector_hits


def test_world_state_verifier_accepts_runtime_state() -> None:
    runtime = AgentRuntime()
    runtime.step({"goal": "explain architecture"})
    assert WorldStateVerifier().check(runtime.belief.current).approved
