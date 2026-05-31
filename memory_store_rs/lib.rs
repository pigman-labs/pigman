#[derive(Debug, Clone)]
pub struct MemoryRecord {
    pub id: String,
    pub kind: String,
    pub importance: f32,
    pub payload: String,
}

#[derive(Default)]
pub struct MemoryStore {
    records: Vec<MemoryRecord>,
}

impl MemoryStore {
    pub fn insert(&mut self, record: MemoryRecord) {
        self.records.push(record);
    }

    pub fn recent(&self, limit: usize) -> Vec<MemoryRecord> {
        self.records.iter().rev().take(limit).cloned().collect()
    }
}

pub fn encode_jsonl(record: &MemoryRecord) -> String {
    format!(
        "{{\"id\":\"{}\",\"kind\":\"{}\",\"importance\":{},\"payload\":\"{}\"}}",
        record.id.replace('"', "\\\""),
        record.kind.replace('"', "\\\""),
        record.importance,
        record.payload.replace('"', "\\\"")
    )
}

#[cfg(test)]
mod tests {
    use super::{encode_jsonl, MemoryRecord, MemoryStore};

    #[test]
    fn stores_recent_records() {
        let mut store = MemoryStore::default();
        store.insert(MemoryRecord {
            id: "1".to_string(),
            kind: "episode".to_string(),
            importance: 0.8,
            payload: "ok".to_string(),
        });
        assert_eq!(store.recent(1).len(), 1);
    }

    #[test]
    fn encodes_jsonl() {
        let line = encode_jsonl(&MemoryRecord {
            id: "1".to_string(),
            kind: "fact".to_string(),
            importance: 1.0,
            payload: "hello".to_string(),
        });
        assert!(line.contains("\"id\":\"1\""));
    }
}
