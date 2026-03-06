# Contributing

Thank you for your interest in contributing to Java CWE Security Skills!

---

## Quick Links

- 📖 [Full Contributing Guide](https://github.com/DevelopersCoffee/java-cwe-security-skills/blob/main/CONTRIBUTING.md)
- 🐛 [Report an Issue](https://github.com/DevelopersCoffee/java-cwe-security-skills/issues/new)
- 💡 [Request a Skill](https://github.com/DevelopersCoffee/java-cwe-security-skills/issues/new?labels=enhancement)

---

## Ways to Contribute

### 1. Add a New CWE Skill

Create remediation skills for CWE vulnerabilities not yet covered.

```bash
# Create skill folder
mkdir cwe-XXX-vulnerability-name
touch cwe-XXX-vulnerability-name/SKILL.md

# Use the SKILL.md template from CONTRIBUTING.md
```

### 2. Improve Existing Skills

- Add more vulnerable code examples
- Improve secure implementation patterns
- Add detection commands
- Fix typos or errors

### 3. Documentation

- Improve getting started guides
- Add framework-specific examples
- Translate documentation

### 4. Testing

- Test skills with different AI assistants
- Report compatibility issues
- Verify detection patterns work

---

## Skill Template

Every skill needs a `SKILL.md` with:

```markdown
---
name: cwe-XXX-name
description: Brief description
version: 1.0.0
tags: [security, java, cwe-XXX]
---

# CWE-XXX Vulnerability Name

## Vulnerable Pattern
[Code examples]

## Deterministic Fix
[Secure implementations]

## Detection Pattern
[grep commands]

## Remediation Steps
[Step-by-step instructions]
```

---

## Pull Request Process

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b add-cwe-XXX`
3. **Add** your skill following the template
4. **Test** with an AI assistant
5. **Submit** a pull request

---

## Labels

| Label | Description |
|-------|-------------|
| `security` | Security-related changes |
| `cwe` | New CWE skill |
| `enhancement` | Improvements |
| `documentation` | Doc changes |
| `good first issue` | Great for newcomers |

---

## Code of Conduct

Be respectful, inclusive, and constructive. We're all here to make security better.

