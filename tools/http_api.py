from __future__ import annotations

from dataclasses import dataclass
from time import time
from urllib.request import Request, urlopen

from tools.results import ToolResult


@dataclass(frozen=True)
class HttpResult:
    status: int
    body: str


class HttpApiTool:
    def request(self, url: str, method: str = "GET", body: bytes | None = None, timeout: int = 10) -> HttpResult:
        req = Request(url, data=body, method=method)
        with urlopen(req, timeout=timeout) as response:
            return HttpResult(status=response.status, body=response.read().decode("utf-8", errors="replace"))

    def request_structured(self, url: str, method: str = "GET", body: bytes | None = None, timeout: int = 10) -> ToolResult:
        started = time()
        try:
            result = self.request(url, method, body, timeout)
        except Exception as exc:
            return ToolResult(
                ok=False,
                tool="http",
                operation="request",
                stderr=f"{type(exc).__name__}: {exc}",
                data={"url": url, "method": method},
                started_at=started,
                ended_at=time(),
            )
        return ToolResult(
            ok=200 <= result.status < 400,
            tool="http",
            operation="request",
            stdout=result.body,
            data={"url": url, "method": method, "status": result.status},
            started_at=started,
            ended_at=time(),
        )
