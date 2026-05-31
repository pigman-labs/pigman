#[derive(Debug, Clone, PartialEq, Eq)]
pub enum Permission {
    Allow,
    Ask,
    Deny,
}

pub fn classify_command(command: &str) -> Permission {
    let dangerous = ["rm -rf", "git reset --hard", "drop table", "shutdown"];
    let lower = command.to_lowercase();

    if dangerous.iter().any(|needle| lower.contains(needle)) {
        return Permission::Deny;
    }

    if lower.contains("deploy") || lower.contains("push") {
        return Permission::Ask;
    }

    Permission::Allow
}

#[cfg(test)]
mod tests {
    use super::{classify_command, Permission};

    #[test]
    fn allows_read_only_commands() {
        assert_eq!(classify_command("python -m pytest"), Permission::Allow);
    }

    #[test]
    fn asks_for_pushes() {
        assert_eq!(classify_command("git push origin main"), Permission::Ask);
    }

    #[test]
    fn denies_destructive_commands() {
        assert_eq!(classify_command("rm -rf /"), Permission::Deny);
    }
}
