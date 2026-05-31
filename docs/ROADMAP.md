# Roadmap

## Now Real

- Root-level Python package layout
- Rust workspace with root-level crate files
- NumPy trainable JEPA reference
- PyTorch trainable JEPA backend
- PyTorch latent dynamics backend
- EMA target encoder
- residual MLP/RMSNorm/dropout blocks
- MoE feed-forward block
- JSONL metrics
- checkpoint save/load
- persistent memory via JSONL and SQLite
- planner evals for MPC, beam, MCTS, CEM
- shell/filesystem/API/browser/patch tool surfaces
- verifier ensemble expansion
- full local verification script

## Still Prototype

- No real multimodal dataset pipeline
- No distributed training
- No large Transformer/SSM stack
- No GPU cluster launchers
- No production serving
- No learned planner trained from large trajectories
- No real browser automation backend
- No human preference or RLHF/RLAIF loop
- No serious red-team or safety eval suite

## Next Serious Milestones

1. Add real trajectory datasets for code/tool/browser tasks.
2. Train dynamics on actual state/action/result triples.
3. Replace synthetic planner evals with benchmark tasks.
4. Add proper experiment tracking and checkpoint versioning.
5. Add FSDP/DeepSpeed or JAX equivalent for scale.
6. Add a real browser environment and task suite.
7. Train value/risk heads from verifier outcomes.

