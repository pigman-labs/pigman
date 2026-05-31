use tool_sandbox::{classify_command, Permission};

fn main() {
    let command = std::env::args().skip(1).collect::<Vec<_>>().join(" ");
    let permission = classify_command(&command);
    let label = match permission {
        Permission::Allow => "allow",
        Permission::Ask => "ask",
        Permission::Deny => "deny",
    };
    println!("{label}");
}
