from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from time import time


@dataclass(frozen=True)
class PersistentFact:
    key: str
    value: str
    importance: float = 0.5
    updated_at: float = 0.0
    confidence: float = 1.0
    source: str = "local"


class JsonlEpisodicStore:
    def __init__(self, path: str = "artifacts/memory/episodes.jsonl") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, event: dict) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(event, default=str) + "\n")

    def read_recent(self, limit: int = 10) -> list[dict]:
        if not self.path.exists():
            return []
        lines = self.path.read_text(encoding="utf-8").splitlines()
        return [json.loads(line) for line in lines[-limit:]]


class SqliteMemoryStore:
    def __init__(self, path: str = "artifacts/memory/memory.sqlite3") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.execute(
            "create table if not exists facts (key text primary key, value text, importance real, updated_at real, confidence real default 1.0, source text default 'local')"
        )
        self.conn.execute(
            "create table if not exists procedures (name text primary key, trigger text, payload text, importance real, updated_at real)"
        )
        self.conn.commit()
        self._migrate()

    def _migrate(self) -> None:
        columns = {row[1] for row in self.conn.execute("pragma table_info(facts)").fetchall()}
        if "confidence" not in columns:
            self.conn.execute("alter table facts add column confidence real default 1.0")
        if "source" not in columns:
            self.conn.execute("alter table facts add column source text default 'local'")
        self.conn.commit()

    def upsert_fact(
        self,
        key: str,
        value: str,
        importance: float = 0.5,
        confidence: float = 1.0,
        source: str = "local",
    ) -> None:
        self.conn.execute(
            "insert into facts values (?, ?, ?, ?, ?, ?) on conflict(key) do update set value=excluded.value, importance=excluded.importance, updated_at=excluded.updated_at, confidence=excluded.confidence, source=excluded.source",
            (key, value, importance, time(), confidence, source),
        )
        self.conn.commit()

    def facts(self, query: str = "") -> list[PersistentFact]:
        terms = [term for term in query.split() if term]
        if not terms:
            rows = self.conn.execute(
                "select key, value, importance, updated_at, confidence, source from facts order by importance desc, updated_at desc"
            ).fetchall()
        else:
            clauses = " or ".join(["key like ? or value like ?" for _ in terms])
            params = [f"%{term}%" for term in terms for _ in (0, 1)]
            rows = self.conn.execute(
                f"select key, value, importance, updated_at, confidence, source from facts where {clauses} order by importance desc, updated_at desc",
                params,
            ).fetchall()
        return [PersistentFact(*row) for row in rows]

    def get_fact(self, key: str) -> PersistentFact | None:
        row = self.conn.execute(
            "select key, value, importance, updated_at, confidence, source from facts where key = ?",
            (key,),
        ).fetchone()
        return PersistentFact(*row) if row else None

    def detect_contradiction(self, key: str, value: str) -> list[dict]:
        existing = self.get_fact(key)
        if existing is None:
            return []
        if existing.value.strip().lower() == value.strip().lower():
            return []
        return [
            {
                "key": key,
                "existing": existing.value,
                "proposed": value,
                "existing_confidence": existing.confidence,
                "source": existing.source,
            }
        ]

    def upsert_procedure(self, name: str, trigger: str, payload: dict, importance: float = 0.5) -> None:
        self.conn.execute(
            "insert into procedures values (?, ?, ?, ?, ?) on conflict(name) do update set trigger=excluded.trigger, payload=excluded.payload, importance=excluded.importance, updated_at=excluded.updated_at",
            (name, trigger, json.dumps(payload), importance, time()),
        )
        self.conn.commit()

    def procedures(self, query: str = "") -> list[dict]:
        terms = [term for term in query.split() if term]
        if not terms:
            rows = self.conn.execute(
                "select name, trigger, payload, importance, updated_at from procedures order by importance desc, updated_at desc"
            ).fetchall()
        else:
            clauses = " or ".join(["name like ? or trigger like ?" for _ in terms])
            params = [f"%{term}%" for term in terms for _ in (0, 1)]
            rows = self.conn.execute(
                f"select name, trigger, payload, importance, updated_at from procedures where {clauses} order by importance desc, updated_at desc",
                params,
            ).fetchall()
        return [
            {"name": name, "trigger": trigger, "payload": json.loads(payload), "importance": importance, "updated_at": updated_at}
            for name, trigger, payload, importance, updated_at in rows
        ]


class MemoryConsolidator:
    def consolidate_execution(self, store: SqliteMemoryStore, event: dict) -> None:
        action = event.get("action") or event.get("selected_action") or {}
        success = event.get("success", True)
        key = f"action:{getattr(action, 'type', action.get('type', 'unknown'))}"
        store.upsert_fact(key, f"success={success}", importance=0.8 if success else 0.4)
