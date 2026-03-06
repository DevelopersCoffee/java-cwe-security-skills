<div align="center">

# 🛡️ Java CWE Security Skills

### The Largest Open-Source AI Security Skill Library for Java

[![Install with npx skills](https://img.shields.io/badge/npx%20skills-add-blueviolet?style=for-the-badge&logo=npm)](https://github.com/vercel-labs/skills)
[![Skills Count](https://img.shields.io/badge/Skills-53-success?style=for-the-badge)](./index.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-orange?style=flat-square&logo=anthropic)](https://claude.ai)
[![GitHub Copilot](https://img.shields.io/badge/GitHub_Copilot-Compatible-blue?style=flat-square&logo=github)](https://github.com/features/copilot)
[![Cursor](https://img.shields.io/badge/Cursor-Compatible-purple?style=flat-square)](https://cursor.com)
[![Augment](https://img.shields.io/badge/Augment-Compatible-green?style=flat-square)](https://augmentcode.com)
[![40+ Agents](https://img.shields.io/badge/40%2B_Agents-Supported-teal?style=flat-square)](https://github.com/vercel-labs/skills#supported-agents)

**Deterministic Vulnerable → Secure code transformations for AI coding assistants**

[Quick Start](#-quick-start) | [All Skills](#-available-skills) | [How It Works](#-how-it-works) | [Contributing](#-contributing)

</div>

---

## 🚀 Quick Start

### Install All 53 Skills (Recommended)

```bash
npx skills add DevelopersCoffee/java-cwe-security-skills --all
```

### Install to Specific Agents

```bash
# Claude Code only
npx skills add DevelopersCoffee/java-cwe-security-skills --all -a claude-code

# Multiple agents
npx skills add DevelopersCoffee/java-cwe-security-skills --all -a claude-code -a cursor -a augment
```

### Install Specific Skills

```bash
# List available skills
npx skills add DevelopersCoffee/java-cwe-security-skills --list

# Install specific skills
npx skills add DevelopersCoffee/java-cwe-security-skills \
  --skill cwe-89-sql-injection \
  --skill cwe-79-xss
```

---

## 🎯 What This Library Does

This repository provides **53 deterministic remediation patterns** for common Java security vulnerabilities. Each skill contains:

- ❌ **Vulnerable Code** - The exact insecure pattern to identify
- ✅ **Secure Code** - The deterministic fix to apply
- 📖 **Explanation** - Why the vulnerability exists and how the fix works

### Why Deterministic?

AI coding assistants can hallucinate fixes. Our skills provide **exact code transformations** that eliminate guesswork:

```java
// ❌ VULNERABLE - SQL Injection (CWE-89)
String query = "SELECT * FROM users WHERE id = " + userId;
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery(query);

// ✅ SECURE - Parameterized Query
String query = "SELECT * FROM users WHERE id = ?";
PreparedStatement pstmt = conn.prepareStatement(query);
pstmt.setString(1, userId);
ResultSet rs = pstmt.executeQuery();
```

---

## 📋 Available Skills

| Category | CWEs Covered |
|----------|-------------|
| **Injection** | CWE-77, 78, 89, 90, 91, 93, 94, 643, 917 |
| **XSS & Output** | CWE-79, 113 |
| **Authentication** | CWE-287, 295, 306, 307, 522, 798 |
| **Authorization** | CWE-284, 501 |
| **Cryptography** | CWE-259, 321, 326, 327, 328, 329, 330, 780 |
| **Data Protection** | CWE-200, 209, 311, 319, 359, 532 |
| **File Handling** | CWE-22, 377, 434, 552, 732 |
| **Session Management** | CWE-347, 613 |
| **Concurrency** | CWE-362, 367, 820, 833 |
| **Resource Management** | CWE-190, 191, 369, 400, 606, 1333 |
| **XML Security** | CWE-776 |
| **Web Security** | CWE-601, 693 |

📄 **[View Complete Index →](./index.md)**

---

## 🔧 How It Works

1. **Install skills** to your AI agent using `npx skills`
2. **Agent loads** skill descriptions into context
3. **When reviewing code**, the agent matches vulnerability patterns
4. **Skill activates** and provides deterministic remediation

Each skill uses the **"Use this skill when..."** trigger pattern for accurate activation.

---

## 🤝 Contributing

We welcome contributions! To add a new CWE skill:

1. **Fork** this repository
2. **Create** a folder: `cwe-XXX-vulnerability-name/`
3. **Add** `SKILL.md` following the existing template
4. **Submit** a Pull Request

---

## 📚 Sources

- [MITRE CWE Database](https://cwe.mitre.org/)
- [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/)
- [GitHub CodeQL](https://github.com/github/codeql)
- [SonarSource Rules](https://rules.sonarsource.com/java/)

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

<div align="center">

**Built with ❤️ by [DevelopersCoffee](https://github.com/DevelopersCoffee)**

⭐ **Star this repo** if it helps secure your Java applications!

[![GitHub Stars](https://img.shields.io/github/stars/DevelopersCoffee/java-cwe-security-skills?style=social)](https://github.com/DevelopersCoffee/java-cwe-security-skills)

</div>
