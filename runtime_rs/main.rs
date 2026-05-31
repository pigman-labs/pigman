use jepa_runtime::{approve_read_only, RuntimeAction};

fn main() {
    let action = RuntimeAction {
        action_type: "observe".to_string(),
        payload: "runtime smoke test".to_string(),
        risk_score: 0.0,
    };
    let decision = approve_read_only(&action);
    println!(
        "{{\"approved\":{},\"reason\":\"{}\"}}",
        decision.approved, decision.reason
    );
}
