from __future__ import annotations

from serving_api.server import AgentServer


def main() -> None:
    server = AgentServer()
    server.start_background()
    print("serving on http://127.0.0.1:8765")
    try:
        while True:
            input()
    except (KeyboardInterrupt, EOFError):
        server.stop()


if __name__ == "__main__":
    main()
