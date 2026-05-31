from __future__ import annotations

from verifiers.code import CodeVerifier
from training.loops.train_neural_jepa import train_neural_jepa
from training.loops.train_torch_jepa import train_jepa_torch
from torch_backend.config import TorchModelConfig, TorchTrainConfig
from tools.shell import ShellTool


def main() -> None:
    verifier = CodeVerifier()
    shell = ShellTool()
    compile_result = verifier.compile_python()
    pytest_result = verifier.pytest()
    neural_result = train_neural_jepa(steps=40, batch_size=32, checkpoint="artifacts/checkpoints/verify_neural_jepa.npz")
    torch_result = train_jepa_torch(
        TorchTrainConfig(
            steps=5,
            batch_size=16,
            checkpoint="artifacts/checkpoints/verify_torch_jepa.pt",
            metrics_path="artifacts/runs/verify_torch_jepa.jsonl",
        ),
        TorchModelConfig(latent_dim=16, hidden_dim=32, depth=1),
    )
    cargo_test = shell.run(["cargo", "test"])
    cargo_build = shell.run(["cargo", "build", "--workspace"])
    print(
        {
            "compile": compile_result.approved,
            "pytest": pytest_result.approved,
            "neural_loss_improved": neural_result.final_loss < 0.2,
            "neural_final_loss": neural_result.final_loss,
            "torch_checkpoint": torch_result.checkpoint,
            "torch_final_loss": torch_result.final_loss,
            "cargo_test": cargo_test.returncode == 0,
            "cargo_build": cargo_build.returncode == 0,
            "issues": compile_result.issues + pytest_result.issues,
        }
    )
    if not (
        compile_result.approved
        and pytest_result.approved
        and neural_result.final_loss < 0.2
        and cargo_test.returncode == 0
        and cargo_build.returncode == 0
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
