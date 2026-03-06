# Quick Start

Get started fixing security vulnerabilities in under 5 minutes.

---

## Step 1: Identify a Vulnerability

Suppose your SAST tool (Checkmarx, SonarQube, Snyk) reports:

```
CWE-89: SQL Injection in UserService.java:45
```

---

## Step 2: Find the Skill

Navigate to the skill folder:

```bash
cd ~/.augment/skills/java-cwe-security-skills/cwe-89-sql-injection
cat SKILL.md
```

Or browse online: [CWE-89 Skill](https://github.com/DevelopersCoffee/java-cwe-security-skills/tree/main/cwe-89-sql-injection)

---

## Step 3: Understand the Pattern

The skill shows the **vulnerable pattern**:

```java
// ❌ Vulnerable - String concatenation
String query = "SELECT * FROM users WHERE id=" + userId;
ResultSet rs = stmt.executeQuery(query);
```

---

## Step 4: Apply the Fix

The skill provides the **secure implementation**:

```java
// ✅ Secure - Parameterized query
PreparedStatement pstmt = conn.prepareStatement(
    "SELECT * FROM users WHERE id=?");
pstmt.setString(1, userId);
ResultSet rs = pstmt.executeQuery();
```

---

## Step 5: Verify

Run the detection command to ensure no more vulnerable patterns exist:

```bash
grep -rn "executeQuery.*+" --include="*.java" src/
# Should return no results
```

Re-run your SAST scan to confirm CWE-89 is resolved.

---

## Using with AI Assistants

### Augment Code Prompt

```
Fix the SQL injection vulnerability in UserService.java using the CWE-89 skill.
Show me the before and after code.
```

### Generic Prompt

```
I have a SQL injection vulnerability (CWE-89) in this Java code:

[paste your code]

Apply the secure remediation pattern using parameterized queries.
```

---

## Common Workflows

### Workflow 1: Single File Fix

```bash
# 1. Find vulnerable files
grep -rn "executeQuery.*+" --include="*.java" src/

# 2. Open in editor and apply fix
# 3. Re-run SAST scan
```

### Workflow 2: Batch Fix with AI

```
Scan this repository for CWE-89 (SQL Injection) vulnerabilities.
For each occurrence, apply the secure remediation pattern.
Show me all changes as a unified diff.
```

### Workflow 3: CI/CD Integration

Add to your pipeline:

```yaml
- name: Check for SQL Injection patterns
  run: |
    if grep -rn "executeQuery.*+" --include="*.java" src/; then
      echo "Potential SQL injection found!"
      exit 1
    fi
```

---

## Next Steps

- [Skills Catalog](../skills/index.md) - Browse all 54+ skills
- [Contributing](../contributing.md) - Add new skills

