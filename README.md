# Java CWE Security Skills 🔐

**java-cwe-security-skills** is an open-source library of **deterministic security remediation skills for Java applications**, mapped directly to the **MITRE Common Weakness Enumeration (CWE)** framework.

The repository provides structured **`SKILL.md` definitions** that enable AI coding assistants and security agents to **detect, analyze, and fix vulnerabilities automatically** in Java codebases.

These skills are designed for integration with modern **AI developer platforms**, including:

* **Augment Code**
* **skills.sh**
* **Claude Code**
* **Cursor AI**
* **LobeHub Skills Marketplace**
* **DevSecOps automation pipelines**

---

# Why This Project Exists

Modern development teams rely heavily on **SAST tools** such as:

* Checkmarx
* SonarQube
* Snyk
* CodeQL
* OWASP Dependency Check

While these tools identify vulnerabilities, they often lack **deterministic remediation patterns**.

This repository bridges that gap by providing **AI-readable remediation skills** that allow coding agents to:

1. Detect vulnerable code patterns
2. Map them to **specific CWE weaknesses**
3. Apply **secure code transformations**
4. Verify the fix through deterministic rules

This enables **AI-assisted vulnerability remediation** directly inside development workflows.

---

# Features

✔ Deterministic remediation for **Java security vulnerabilities**
✔ Coverage for **100+ Java-relevant CWE weaknesses**
✔ Designed for **AI coding assistants and security agents**
✔ Compatible with **Augment Code skill workflows**
✔ Supports **automated vulnerability fixing in repositories**
✔ Based on **MITRE CWE, OWASP, CodeQL, and secure coding best practices**

---

# Repository Structure

```id="7x4ihr"
java-cwe-security-skills
│
├── cwe-79-xss
│   └── SKILL.md
│
├── cwe-89-sql-injection
│   └── SKILL.md
│
├── cwe-611-xxe
│   └── SKILL.md
│
├── cwe-918-ssrf
│   └── SKILL.md
│
├── cwe-502-insecure-deserialization
│   └── SKILL.md
│
└── ...
```

Each folder represents a **single vulnerability remediation skill**.

---

# Example Skill

Example: **CWE-89 SQL Injection**

The skill defines:

* vulnerable Java patterns
* deterministic remediation logic
* secure implementation examples
* verification rules

AI coding assistants can automatically transform vulnerable SQL queries into **secure prepared statements**.

---

# Supported Vulnerability Categories

The library includes remediation skills for major vulnerability classes.

### Injection

* SQL Injection (CWE-89)
* LDAP Injection (CWE-90)
* XPath Injection (CWE-643)
* Expression Language Injection (CWE-917)

### Web Security

* Cross-Site Scripting (CWE-79)
* HTTP Response Splitting (CWE-113)
* Clickjacking / Missing Security Headers (CWE-693)

### Cryptography

* Weak Cryptography (CWE-327)
* Hardcoded Cryptographic Keys (CWE-321)
* Missing Random IV (CWE-329)

### Data Exposure

* Information Exposure (CWE-200)
* Sensitive Data in Logs (CWE-532)
* Privacy Violations (CWE-359)

### Deserialization

* Insecure Deserialization (CWE-502)

### Resource Management

* Resource Exhaustion (CWE-400)
* Uncontrolled Memory Allocation (CWE-789)

### Input Validation

* Path Traversal (CWE-22)
* Regex Denial of Service (CWE-1333)
* Unchecked Loop Condition (CWE-606)

---

# Using These Skills with Augment Code

Augment Code can use these skills to perform **AI-assisted vulnerability remediation** during development.

Typical workflow:

1. Augment scans the repository for vulnerable patterns
2. The vulnerability is mapped to a **CWE skill**
3. The skill provides **deterministic remediation steps**
4. Augment generates a **secure code transformation**

Example prompt inside Augment:

```
Fix SQL injection vulnerabilities in this Java service.
```

The agent loads the **CWE-89 skill** and applies the secure remediation.

---

# Sources

Security knowledge in this repository is derived from:

* MITRE CWE Database
* OWASP Security Cheat Sheets
* GitHub CodeQL Security Queries
* Snyk Vulnerability Database
* OWASP VulnerableApp

---

# Contributing

Contributions are welcome.

You can contribute by:

* adding new CWE skills
* improving remediation patterns
* adding secure code examples
* expanding coverage for Java frameworks

---

# Vision

The goal of this project is to create the **largest open-source library of AI security remediation skills for Java**.

By combining **CWE knowledge + deterministic remediation patterns**, AI agents can evolve from **vulnerability detection → automatic secure code remediation**.
