from __future__ import annotations

from dataset_engine.records import DatasetRecord
from dataset_engine.store import JsonlDatasetStore


def main() -> None:
    records = [
        DatasetRecord("synthetic_web", "train", {"state": "home", "action": "click", "next_state": "details"}, "synthetic"),
        DatasetRecord("synthetic_code", "train", {"repo": "demo", "action": "patch", "result": "tests_pass"}, "synthetic"),
    ]
    print(JsonlDatasetStore().ingest("synthetic_agent", "v1", records, min_quality=0.5))


if __name__ == "__main__":
    main()

