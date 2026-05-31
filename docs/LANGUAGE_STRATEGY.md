# Language Strategy

Use Python and Rust together.

## Python Owns

Python should own the fast-changing research layer:

```text
model composition
training loops
dataset pipelines
evaluation harnesses
planner experiments
verifier orchestration
notebook/prototype workflows
PyTorch/JAX integration
```

Reasons:

```text
best ML ecosystem
fast iteration
easy distributed training integration
strong eval/prototyping story
```

## Rust Owns

Rust should own the stable, high-throughput systems layer:

```text
tool sandbox runtime
filesystem/event watchers
memory/index services
trajectory log storage
streaming telemetry
rollout execution service
browser/tool gateways
safety policy enforcement
custom CPU kernels
future PyO3 bindings
```

Reasons:

```text
predictable performance
safe concurrency
excellent systems boundaries
single static binaries
good sandboxing/process control
```

## Boundary

Python calls Rust through:

```text
local process RPC first
JSON/MessagePack schemas
then PyO3/maturin for hot paths
then gRPC if distributed services are needed
```

Avoid binding everything early. Start with process boundaries because they are easier to debug and safer to evolve.

## Repo Rule

Python packages live directly at the repository root:

```text
core/
jepa/
dynamics/
planner/
memory/
```

Rust crates also avoid the default `src/` layout by setting explicit paths in `Cargo.toml`:

```toml
[lib]
path = "lib.rs"
```

