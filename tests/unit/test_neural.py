from pathlib import Path

from evals.neural_eval import evaluate_checkpoint
from neural.adapter import NeuralWorldModelAdapter
from training.loops.train_neural_jepa import train_neural_jepa


def test_neural_jepa_trains_and_loads(tmp_path: Path) -> None:
    checkpoint = tmp_path / "neural_jepa.npz"
    report = train_neural_jepa(steps=50, batch_size=32, checkpoint=str(checkpoint))
    assert checkpoint.exists()
    assert report.final_loss < 0.2

    adapter = NeuralWorldModelAdapter(str(checkpoint))
    prediction = adapter.predict_vector([0.1] * 64, {"type": "test"})
    assert prediction is not None
    assert len(prediction) == 24


def test_neural_eval_reads_checkpoint(tmp_path: Path) -> None:
    checkpoint = tmp_path / "neural_jepa.npz"
    train_neural_jepa(steps=30, batch_size=32, checkpoint=str(checkpoint))
    result = evaluate_checkpoint(str(checkpoint), batches=2)
    assert result["loss"] < 0.2
