#[derive(Debug, Clone)]
pub struct RuntimeAction {
    pub action_type: String,
    pub payload: String,
    pub risk_score: f32,
}

#[derive(Debug, Clone)]
pub struct RuntimeDecision {
    pub approved: bool,
    pub reason: String,
}

pub fn approve_read_only(action: &RuntimeAction) -> RuntimeDecision {
    let approved = matches!(
        action.action_type.as_str(),
        "observe" | "read_file" | "query_memory" | "simulate"
    );

    RuntimeDecision {
        approved,
        reason: if approved {
            "read-only action approved".to_string()
        } else {
            "action requires higher-level verifier".to_string()
        },
    }
}

#[cfg(test)]
mod tests {
    use super::{approve_read_only, RuntimeAction};

    #[test]
    fn approves_observe() {
        let decision = approve_read_only(&RuntimeAction {
            action_type: "observe".to_string(),
            payload: "{}".to_string(),
            risk_score: 0.0,
        });
        assert!(decision.approved);
    }

    #[test]
    fn rejects_write_action() {
        let decision = approve_read_only(&RuntimeAction {
            action_type: "edit_file".to_string(),
            payload: "{}".to_string(),
            risk_score: 0.3,
        });
        assert!(!decision.approved);
    }
}
