# Java CWE Security Skills 🔐

**Deterministic security remediation skills for Java applications, mapped to MITRE CWE vulnerabilities.**

[![GitHub Stars](https://img.shields.io/github/stars/DevelopersCoffee/java-cwe-security-skills?style=social)](https://github.com/DevelopersCoffee/java-cwe-security-skills)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

---

## What is This?

This repository provides **AI-readable remediation skills** that enable coding agents to:

1. 🔍 **Detect** vulnerable code patterns
2. 🗺️ **Map** them to specific CWE weaknesses
3. 🔧 **Apply** secure code transformations
4. ✅ **Verify** the fix through deterministic rules

---

## Quick Start

### For AI Agents (Augment Code, Claude, Cursor)

```bash
# Clone and use as skill repository
git clone https://github.com/DevelopersCoffee/java-cwe-security-skills.git ~/.augment/skills/java-cwe-security-skills
```

### For Manual Reference

Browse the [Skills Catalog](skills/index.md) to find remediation patterns for specific vulnerabilities.

---

## Supported Platforms

| Platform | Integration |
|----------|-------------|
| **Augment Code** | Native skill support |
| **skills.sh** | Marketplace ready |
| **Claude Code** | Context injection |
| **Cursor AI** | Rules file |
| **DevSecOps Pipelines** | CI/CD integration |

---

## Coverage

**54+ CWE vulnerabilities** covered across major security categories:

| Category | Skills |
|----------|--------|
| 💉 Injection | SQL, XSS, Command, LDAP, XPath, EL |
| 🔐 Cryptography | Weak algos, hardcoded keys, weak PRNG |
| 🚪 Access Control | Path traversal, open redirect, SSRF |
| 📝 Data Exposure | Log injection, privacy violation |
| ⚡ Resource Management | DoS, race conditions, integer overflow |

---

## Example: Fix SQL Injection

**Before (Vulnerable):**

```java
String query = "SELECT * FROM users WHERE id=" + userId;
ResultSet rs = stmt.executeQuery(query);
```

**After (Secure):**

```java
PreparedStatement pstmt = conn.prepareStatement(
    "SELECT * FROM users WHERE id=?");
pstmt.setString(1, userId);
ResultSet rs = pstmt.executeQuery();
```

---

## Contributing

We welcome contributions! See our [Contributing Guide](contributing.md) for:

- How to create new CWE skills
- Skill folder structure and naming conventions
- Pull request process

---

## Links

- 📖 [Full Documentation](https://developerscoffee.github.io/java-cwe-security-skills/)
- 💻 [GitHub Repository](https://github.com/DevelopersCoffee/java-cwe-security-skills)
- 🏢 [Developers Coffee](https://developerscoffee.github.io/)

---

<p align="center">
  <strong>Built with ☕ by <a href="https://developerscoffee.github.io">Developers Coffee</a></strong>
</p>

