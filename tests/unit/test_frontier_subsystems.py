import torch

from alignment.dpo import DPOObjective
from alignment.preferences import PreferenceBuffer
from dataset_engine.records import DatasetRecord
from dataset_engine.store import JsonlDatasetStore
from distributed.config import DistributedConfig
from distributed.launcher import LaunchPlanner
from multimodal_stack.torch_modules import MultimodalWorldStack
from safety_frontier.evals import FrontierSafetySuite
from serving_api.server import AgentService


def test_dataset_engine_ingests_and_streams(tmp_path):
    store = JsonlDatasetStore(str(tmp_path))
    manifest = store.ingest(
        "agent",
        "v1",
        [DatasetRecord("web", "train", {"state": "a", "action": "b", "next_state": "c"}, "synthetic")],
        min_quality=0.5,
    )
    assert manifest.records == 1
    assert list(store.stream("agent", "v1"))[0]["source"] == "web"


def test_distributed_launch_plan():
    plan = LaunchPlanner().plan(DistributedConfig(strategy="fsdp", nodes=2, gpus_per_node=4))
    assert plan["world_size"] == 8
    assert plan["strategy"] == "fsdp"


def test_multimodal_stack_forward():
    model = MultimodalWorldStack(latent_dim=32, depth=1)
    output = model(torch.randn(2, 32), torch.randn(2, 48), torch.randn(2, 16))
    assert output.shape == (2, 32)


def test_alignment_preference_and_dpo():
    buffer = PreferenceBuffer()
    example = buffer.synthetic_from_scores("goal", [("good", 1.0), ("bad", 0.0)])
    loss = DPOObjective().loss_from_logps(-0.1, -1.0, -0.2, -0.8)
    assert example.chosen == "good"
    assert loss > 0


def test_frontier_safety_suite():
    result = FrontierSafetySuite().run()
    assert result["passed"] == result["total"]


def test_serving_api_service_smoke():
    payload = AgentService().handle({"goal": "explain architecture"})
    assert payload["approved"] is True
