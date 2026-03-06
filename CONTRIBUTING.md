# Contributing to Java CWE Security Skills

Thank you for your interest in contributing! This guide explains how to create new CWE security skills.

---

## 📋 Prerequisites

- Familiarity with Java security vulnerabilities
- Understanding of MITRE CWE framework
- Knowledge of secure coding practices

---

## 🗂️ Skill Folder Structure

Each skill lives in its own folder following this naming convention:

```
cwe-{number}-{short-name}/
└── SKILL.md
```

**Examples:**
- `cwe-89-sql-injection/`
- `cwe-79-xss/`
- `cwe-327-weak-cryptography/`

---

## 📝 SKILL.md Template

Every skill must contain a `SKILL.md` file with this structure:

```markdown
---
name: cwe-{number}-{short-name}
description: Brief description of the vulnerability
version: 1.0.0
tags:
  - security
  - java
  - cwe-{number}
  - {category}
---

# CWE-{number} {Official CWE Name}

## Description

{Detailed description of the vulnerability}

Reference: https://cwe.mitre.org/data/definitions/{number}.html

**OWASP Category**: {OWASP Top 10 category if applicable}

---

## Vulnerable Pattern

### ❌ Example 1

```java
// Vulnerable code example
```

### ❌ Example 2

```java
// Another vulnerable pattern
```

---

## Deterministic Fix

### ✅ Secure Implementation

```java
// Correct, secure code
```

---

## Detection Pattern

```bash
# grep/regex commands to find vulnerable code
grep -rn "pattern" --include="*.java" src/
```

---

## Remediation Steps

1. Step one
2. Step two
3. Step three

---

## Key Imports

```java
import required.packages;
```

---

## Verification

- Re-run SAST scan
- Test with attack payloads
- Verify functionality preserved

---

## References

- [CWE-{number}](https://cwe.mitre.org/data/definitions/{number}.html)
- [OWASP Cheat Sheet](link)
```

---

## 🚀 Creating a New Skill

### Step 1: Choose a CWE

Pick a CWE from the [MITRE CWE List](https://cwe.mitre.org/data/definitions/699.html) that:
- Affects Java applications
- Has deterministic remediation patterns
- Is not already covered in this repository

### Step 2: Create the folder

```bash
mkdir cwe-XXX-short-name
touch cwe-XXX-short-name/SKILL.md
```

### Step 3: Research the vulnerability

- Read the official CWE description
- Find vulnerable code examples
- Document the secure fix pattern

### Step 4: Write the SKILL.md

Use the template above. Include:
- At least 2 vulnerable code examples
- At least 1 secure implementation
- grep commands for detection
- Step-by-step remediation

### Step 5: Test your skill

Verify the skill works with an AI coding assistant:

```
Fix CWE-XXX in this code: [paste vulnerable code]
```

---

## ✅ Pull Request Checklist

- [ ] Folder follows naming convention: `cwe-{number}-{name}/`
- [ ] SKILL.md uses the required template
- [ ] YAML frontmatter is valid
- [ ] At least 2 vulnerable code examples
- [ ] At least 1 secure implementation
- [ ] Detection commands work
- [ ] References include CWE link
- [ ] Tested with AI assistant

---

## 📌 Code Style

- Use 4-space indentation in Java examples
- Include complete, compilable code snippets
- Add comments explaining the vulnerability/fix
- Use realistic, production-like examples

---

## 🏷️ Tagging Guidelines

Use these standard tags in your SKILL.md frontmatter:

| Tag | When to use |
|-----|-------------|
| `security` | Always |
| `java` | Always |
| `cwe-{number}` | Always |
| `injection` | SQL, XSS, Command, etc. |
| `cryptography` | Crypto-related |
| `authentication` | Auth/session issues |
| `access-control` | Authorization issues |

---

## 💬 Questions?

Open an issue or discussion on GitHub.

