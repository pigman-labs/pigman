from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass, field

from multi_agent.messages import Message


@dataclass
class MessageBus:
    queues: dict[str, deque[Message]] = field(default_factory=lambda: defaultdict(deque))
    history: list[Message] = field(default_factory=list)

    def publish(self, message: Message) -> None:
        queue = self.queues[message.recipient]
        inserted = False
        for index, existing in enumerate(queue):
            if message.priority > existing.priority:
                queue.insert(index, message)
                inserted = True
                break
        if not inserted:
            queue.append(message)
        self.history.append(message)

    def drain(self, recipient: str, limit: int | None = None) -> list[Message]:
        queue = self.queues[recipient]
        messages = []
        while queue and (limit is None or len(messages) < limit):
            messages.append(queue.popleft())
        return messages

    def pending(self, recipient: str | None = None) -> int:
        if recipient is not None:
            return len(self.queues[recipient])
        return sum(len(queue) for queue in self.queues.values())

    def trace(self, trace_id: str) -> list[Message]:
        return [message for message in self.history if message.trace_id == trace_id]

