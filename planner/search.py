from __future__ import annotations

from dataclasses import dataclass
from math import log, sqrt
from random import Random


@dataclass(frozen=True)
class SyntheticAction:
    name: str
    delta: float
    risk: float = 0.0


class SyntheticControlWorld:
    def __init__(self, target: float = 1.0) -> None:
        self.target = target

    def step(self, state: float, action: SyntheticAction) -> float:
        return state + action.delta

    def value(self, state: float) -> float:
        return -abs(self.target - state)


class LearnedMPCPlanner:
    def __init__(self, actions: list[SyntheticAction], horizon: int = 3) -> None:
        self.actions = actions
        self.horizon = horizon

    def choose(self, world: SyntheticControlWorld, state: float) -> SyntheticAction:
        best = self.actions[0]
        best_score = float("-inf")
        for action in self.actions:
            rollout = state
            for _ in range(self.horizon):
                rollout = world.step(rollout, action)
            score = world.value(rollout) - action.risk
            if score > best_score:
                best = action
                best_score = score
        return best


class BeamSearchPlanner:
    def __init__(self, actions: list[SyntheticAction], width: int = 3, depth: int = 3) -> None:
        self.actions = actions
        self.width = width
        self.depth = depth

    def choose(self, world: SyntheticControlWorld, state: float) -> SyntheticAction:
        beams = [(state, [])]
        for _ in range(self.depth):
            candidates = []
            for current, seq in beams:
                for action in self.actions:
                    next_state = world.step(current, action)
                    candidates.append((next_state, [*seq, action]))
            candidates.sort(key=lambda item: world.value(item[0]), reverse=True)
            beams = candidates[: self.width]
        return beams[0][1][0]


@dataclass
class MCTSNode:
    state: float
    parent: "MCTSNode | None" = None
    action: SyntheticAction | None = None
    visits: int = 0
    value: float = 0.0
    children: list["MCTSNode"] = None

    def __post_init__(self) -> None:
        if self.children is None:
            self.children = []


class MCTSPlanner:
    def __init__(self, actions: list[SyntheticAction], simulations: int = 64, seed: int = 7) -> None:
        self.actions = actions
        self.simulations = simulations
        self.rng = Random(seed)

    def choose(self, world: SyntheticControlWorld, state: float) -> SyntheticAction:
        root = MCTSNode(state)
        for _ in range(self.simulations):
            node = self._select(root)
            if node.visits > 0:
                node = self._expand(world, node)
            reward = self._rollout(world, node.state)
            self._backprop(node, reward)
        if not root.children:
            return self.actions[0]
        return max(root.children, key=lambda child: child.visits).action or self.actions[0]

    def _select(self, node: MCTSNode) -> MCTSNode:
        while node.children:
            node = max(
                node.children,
                key=lambda child: child.value / max(1, child.visits)
                + 1.4 * sqrt(log(max(1, node.visits)) / max(1, child.visits)),
            )
        return node

    def _expand(self, world: SyntheticControlWorld, node: MCTSNode) -> MCTSNode:
        tried = {child.action.name for child in node.children if child.action}
        untried = [action for action in self.actions if action.name not in tried]
        if not untried:
            return node
        action = self.rng.choice(untried)
        child = MCTSNode(world.step(node.state, action), parent=node, action=action)
        node.children.append(child)
        return child

    def _rollout(self, world: SyntheticControlWorld, state: float) -> float:
        current = state
        for _ in range(4):
            current = world.step(current, self.rng.choice(self.actions))
        return world.value(current)

    def _backprop(self, node: MCTSNode, reward: float) -> None:
        while node is not None:
            node.visits += 1
            node.value += reward
            node = node.parent


class CEMPlanner:
    def __init__(self, iterations: int = 4, samples: int = 64, elite_frac: float = 0.2, seed: int = 7) -> None:
        self.iterations = iterations
        self.samples = samples
        self.elite_frac = elite_frac
        self.rng = Random(seed)

    def choose_delta(self, world: SyntheticControlWorld, state: float) -> float:
        mean = 0.0
        std = 1.0
        for _ in range(self.iterations):
            samples = [self.rng.gauss(mean, std) for _ in range(self.samples)]
            samples.sort(key=lambda delta: world.value(state + delta), reverse=True)
            elite = samples[: max(1, int(self.samples * self.elite_frac))]
            mean = sum(elite) / len(elite)
            std = max(0.01, (sum((x - mean) ** 2 for x in elite) / len(elite)) ** 0.5)
        return mean
