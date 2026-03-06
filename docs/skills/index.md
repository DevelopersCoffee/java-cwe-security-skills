# Skills Catalog

Browse all available Java CWE Security Skills organized by vulnerability category.

!!! tip "Auto-Generated Index"
    This catalog is automatically updated when new skills are added to the repository.

---

## 💉 Injection Vulnerabilities

| CWE | Name | Description |
|-----|------|-------------|
| [CWE-77](cwe-77-command-injection.md) | Command Injection | OS command injection via user input |
| [CWE-78](cwe-78-os-command-injection.md) | OS Command Injection | Shell command execution vulnerabilities |
| [CWE-79](cwe-79-xss.md) | Cross-Site Scripting (XSS) | Reflected and stored XSS |
| [CWE-89](cwe-89-sql-injection.md) | SQL Injection | Database query manipulation |
| [CWE-90](cwe-90-ldap-injection.md) | LDAP Injection | Directory service injection |
| [CWE-91](cwe-91-xml-injection.md) | XML Injection | XML document manipulation |
| [CWE-93](cwe-93-crlf-injection.md) | CRLF Injection | HTTP header injection |
| [CWE-94](cwe-94-code-injection.md) | Code Injection | Dynamic code execution |
| [CWE-113](cwe-113-http-response-splitting.md) | HTTP Response Splitting | Response header manipulation |
| [CWE-643](cwe-643-xpath-injection.md) | XPath Injection | XML path query injection |
| [CWE-917](cwe-917-expression-language-injection.md) | Expression Language Injection | EL/OGNL injection |

---

## 🔐 Cryptographic Issues

| CWE | Name | Description |
|-----|------|-------------|
| [CWE-321](cwe-321-hardcoded-crypto-key.md) | Hardcoded Crypto Key | Keys embedded in source code |
| [CWE-326](cwe-326-inadequate-encryption-strength.md) | Inadequate Key Strength | Weak encryption key size |
| [CWE-327](cwe-327-weak-cryptography.md) | Weak Cryptography | Use of broken algorithms |
| [CWE-328](cwe-328-weak-hash-algorithm.md) | Weak Hash Algorithm | MD5/SHA1 for security |
| [CWE-329](cwe-329-missing-random-iv.md) | Missing Random IV | Predictable initialization vectors |
| [CWE-330](cwe-330-weak-prng.md) | Weak PRNG | Insecure random number generation |
| [CWE-780](cwe-780-rsa-without-oaep.md) | RSA Without OAEP | Missing padding in RSA |

---

## 🔑 Credentials & Authentication

| CWE | Name | Description |
|-----|------|-------------|
| [CWE-259](cwe-259-hardcoded-password.md) | Hardcoded Password | Passwords in source code |
| [CWE-287](cwe-287-improper-authentication.md) | Improper Authentication | Authentication bypass |
| [CWE-306](cwe-306-missing-authentication.md) | Missing Authentication | Unprotected endpoints |
| [CWE-307](cwe-307-brute-force-protection.md) | Brute Force Protection | Rate limiting missing |
| [CWE-347](cwe-347-jwt-signature-bypass.md) | JWT Signature Bypass | JWT validation issues |
| [CWE-522](cwe-522-insufficiently-protected-credentials.md) | Unprotected Credentials | Credential exposure |
| [CWE-613](cwe-613-insufficient-session-expiration.md) | Session Expiration | Long-lived sessions |
| [CWE-798](cwe-798-hardcoded-credentials.md) | Hardcoded Credentials | Credentials in code |

---

## 🚪 Access Control

| CWE | Name | Description |
|-----|------|-------------|
| [CWE-22](cwe-22-path-traversal.md) | Path Traversal | Directory traversal attacks |
| [CWE-284](cwe-284-improper-access-control.md) | Improper Access Control | Authorization bypass |
| [CWE-434](cwe-434-unrestricted-file-upload.md) | File Upload | Malicious file uploads |
| [CWE-552](cwe-552-files-accessible-externally.md) | External File Access | Exposed sensitive files |
| [CWE-601](cwe-601-open-redirect.md) | Open Redirect | URL redirect manipulation |
| [CWE-693](cwe-693-missing-security-headers.md) | Missing Headers | Security header omissions |
| [CWE-732](cwe-732-improper-file-permissions.md) | File Permissions | Overly permissive files |

---

## 📝 Data Exposure

| CWE | Name | Description |
|-----|------|-------------|
| [CWE-200](cwe-200-information-exposure.md) | Information Exposure | Sensitive data leakage |
| [CWE-209](cwe-209-error-message-exposure.md) | Error Message Exposure | Stack traces in responses |
| [CWE-311](cwe-311-non-encrypted-storage.md) | Unencrypted Storage | Plaintext sensitive data |
| [CWE-319](cwe-319-cleartext-transmission.md) | Cleartext Transmission | HTTP for sensitive data |
| [CWE-359](cwe-359-privacy-violation.md) | Privacy Violation | PII in logs |
| [CWE-501](cwe-501-trust-boundary-violation.md) | Trust Boundary | Trusted data contamination |
| [CWE-532](cwe-532-sensitive-info-in-logs.md) | Sensitive Info in Logs | Credentials in logs |

---

## ⚡ Resource Management

| CWE | Name | Description |
|-----|------|-------------|
| [CWE-190](cwe-190-integer-overflow.md) | Integer Overflow | Arithmetic overflow |
| [CWE-191](cwe-191-integer-underflow.md) | Integer Underflow | Arithmetic underflow |
| [CWE-369](cwe-369-divide-by-zero.md) | Divide by Zero | Division exceptions |
| [CWE-400](cwe-400-resource-exhaustion.md) | Resource Exhaustion | DoS via resource consumption |
| [CWE-606](cwe-606-unchecked-loop-condition.md) | Unchecked Loop | Infinite loop conditions |
| [CWE-776](cwe-776-xml-entity-expansion.md) | XML Entity Expansion | Billion laughs attack |
| [CWE-1333](cwe-1333-redos.md) | ReDoS | Regex denial of service |

---

## 🔄 Concurrency

| CWE | Name | Description |
|-----|------|-------------|
| [CWE-362](cwe-362-race-condition.md) | Race Condition | Thread safety issues |
| [CWE-367](cwe-367-race-condition-toctou.md) | TOCTOU Race Condition | Time-of-check time-of-use |
| [CWE-377](cwe-377-insecure-temporary-file.md) | Insecure Temp File | Predictable temp files |
| [CWE-820](cwe-820-unsynchronized-access.md) | Unsynchronized Access | Missing synchronization |
| [CWE-833](cwe-833-deadlock.md) | Deadlock | Thread deadlock conditions |

---

## 🌐 Web Security

| CWE | Name | Description |
|-----|------|-------------|
| [CWE-295](cwe-295-insecure-tls-trust-manager.md) | Insecure TLS | Certificate validation bypass |

---

## Statistics

- **Total Skills**: 54
- **Categories**: 8
- **Last Updated**: Auto-generated on each commit

