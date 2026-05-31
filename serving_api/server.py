from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from serving.runtime import AgentRuntime


class AgentService:
    def __init__(self) -> None:
        self.runtime = AgentRuntime()

    def handle(self, payload: dict) -> dict:
        result = self.runtime.step({"goal": payload.get("goal", "")})
        execution = result["execution"]
        return {
            "approved": result["verification"].approved,
            "action": result["action"].__dict__,
            "success": execution.success if execution else False,
            "stdout": execution.stdout if execution else "",
        }


class AgentHandler(BaseHTTPRequestHandler):
    service = AgentService()

    def do_POST(self) -> None:
        length = int(self.headers.get("content-length", "0"))
        payload = json.loads(self.rfile.read(length) or b"{}")
        body = json.dumps(self.service.handle(payload), default=str).encode("utf-8")
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args) -> None:
        return


class AgentServer:
    def __init__(self, host: str = "127.0.0.1", port: int = 8765) -> None:
        self.server = HTTPServer((host, port), AgentHandler)
        self.thread: Thread | None = None

    def start_background(self) -> None:
        self.thread = Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def stop(self) -> None:
        self.server.shutdown()
        if self.thread:
            self.thread.join(timeout=2)
