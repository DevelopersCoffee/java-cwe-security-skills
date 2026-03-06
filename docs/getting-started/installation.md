# Installation

## Prerequisites

- Git installed on your system
- An AI coding assistant that supports skills (Augment Code, Claude, Cursor, etc.)

---

## Installation Methods

### Method 1: Augment Code (Recommended)

Clone the skills into your Augment skills directory:

```bash
git clone https://github.com/DevelopersCoffee/java-cwe-security-skills.git \
  ~/.augment/skills/java-cwe-security-skills
```

The skills will be automatically available in Augment Code.

---

### Method 2: skills.sh Marketplace

If using [skills.sh](https://skills.sh), install directly:

```bash
skills install DevelopersCoffee/java-cwe-security-skills
```

---

### Method 3: Cursor AI

Add to your `.cursorrules` file:

```
# Security Skills
Include security remediation patterns from:
https://github.com/DevelopersCoffee/java-cwe-security-skills

When fixing security vulnerabilities, reference the appropriate CWE skill.
```

---

### Method 4: Claude Code / Claude Desktop

Add to your project context or MCP configuration:

```json
{
  "context_repositories": [
    {
      "url": "https://github.com/DevelopersCoffee/java-cwe-security-skills",
      "purpose": "Security vulnerability remediation skills"
    }
  ]
}
```

---

### Method 5: Local Reference

Clone anywhere and reference manually:

```bash
git clone https://github.com/DevelopersCoffee/java-cwe-security-skills.git
cd java-cwe-security-skills

# Browse skills
ls cwe-*/SKILL.md
```

---

## Verifying Installation

### For Augment Code

```bash
ls ~/.augment/skills/java-cwe-security-skills/cwe-89-sql-injection/
# Should show: SKILL.md
```

### Test with a prompt

```
Fix SQL injection vulnerability in this Java code:
String query = "SELECT * FROM users WHERE id=" + userId;
```

The AI should reference the CWE-89 skill and provide a parameterized query fix.

---

## Keeping Updated

Pull the latest skills regularly:

```bash
cd ~/.augment/skills/java-cwe-security-skills
git pull origin main
```

Or set up a cron job:

```bash
# Update weekly
0 0 * * 0 cd ~/.augment/skills/java-cwe-security-skills && git pull
```

---

## Next Steps

- [Quick Start Guide](quickstart.md) - Fix your first vulnerability
- [Skills Catalog](../skills/index.md) - Browse all available skills

