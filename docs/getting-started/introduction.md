# Introduction

## What are CWE Security Skills?

**CWE Security Skills** are structured, machine-readable definitions that enable AI coding assistants to automatically remediate security vulnerabilities in Java applications.

Each skill is mapped to a specific **Common Weakness Enumeration (CWE)** identifier from the [MITRE CWE Database](https://cwe.mitre.org/).

---

## Why This Approach?

Modern SAST tools like **Checkmarx**, **SonarQube**, **Snyk**, and **CodeQL** are excellent at **detecting** vulnerabilities. However, they often lack **deterministic remediation patterns**.

This repository bridges that gap by providing:

| Component | Purpose |
|-----------|---------|
| **Vulnerable Patterns** | Code patterns that trigger the vulnerability |
| **Secure Implementations** | Correct code that eliminates the vulnerability |
| **Detection Commands** | grep/regex patterns to find vulnerable code |
| **Remediation Steps** | Step-by-step fix instructions |
| **Verification Rules** | How to confirm the fix works |

---

## How AI Agents Use These Skills

When an AI coding assistant (Augment Code, Claude, Cursor) encounters a security vulnerability:

1. **Detection**: The agent identifies the vulnerable pattern
2. **Mapping**: The vulnerability is mapped to a CWE skill
3. **Transformation**: The skill provides the secure code transformation
4. **Verification**: The agent confirms the fix resolves the issue

---

## Skill Format

Each skill follows a standardized `SKILL.md` format:

```markdown
---
name: cwe-89-sql-injection
description: SQL Injection via string concatenation
version: 1.0.0
tags: [security, java, cwe-89, sql-injection]
---

# CWE-89 SQL Injection

## Vulnerable Pattern
[Code examples showing the vulnerability]

## Deterministic Fix
[Secure code implementations]

## Detection Pattern
[Commands to find vulnerable code]

## Remediation Steps
[Step-by-step fix instructions]

## Verification
[How to confirm the fix]
```

---

## Coverage Categories

The library covers these major vulnerability categories:

- **Injection Flaws** (SQL, XSS, Command, LDAP, XPath)
- **Cryptographic Issues** (Weak algorithms, hardcoded keys)
- **Access Control** (Path traversal, authentication bypass)
- **Data Exposure** (Log injection, sensitive data leaks)
- **Resource Management** (DoS, race conditions)

---

## Next Steps

- [Installation Guide](installation.md) - Set up the skills in your environment
- [Quick Start](quickstart.md) - Use skills to fix your first vulnerability
- [Skills Catalog](../skills/index.md) - Browse all available skills

