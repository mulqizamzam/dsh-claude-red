---
name: secure-code-review
description: "Review code and diffs for exploitable security defects by tracking untrusted data, trust boundaries, authorization decisions, secret handling, state transitions, and error paths; produce evidence-backed minimal fixes."
---

# Secure Code Review

## Workflow
1. Confirm repository, commit or diff range, language/framework, security objective, and whether generated/vendor files are in scope.
2. Map entry points and trust boundaries: HTTP or queue workers, files, deserialization, plugin boundaries, command execution, database queries, template rendering, and external integrations.
3. Trace untrusted values to sensitive sinks. Inspect validation order, canonicalization, encoding, parameterization, path handling, serialization, and error handling.
4. Review authorization at resource and action level. Test whether caller identity, tenant, role, ownership, and object state are checked on every path, including async/background jobs.
5. Review authentication/session design, CSRF/CORS assumptions, token storage, password/secret lifecycle, cryptographic API use, logging/redaction, and unsafe defaults.
6. Inspect concurrency and state changes for replay, race, TOCTOU, idempotency, and transaction-boundary bugs.
7. Check dependency usage and configuration assumptions. Separate code-proven findings from issues that need runtime confirmation.
8. For each plausible finding, gather minimal reproducible evidence, affected file/line, preconditions, impact, and a minimal corrective patch. Do not claim exploitability from a suspicious function name only.
9. Recommend targeted unit, integration, property, or regression tests that fail before the fix and pass after it.

## Finding quality
Include title, severity rationale, affected component/lines, attacker prerequisites, data/control-flow reasoning, actual vs. potential impact, safe reproduction, recommended patch, regression test, and confidence. Avoid duplicating one root cause across multiple findings without explaining distinct impacts.

## Guardrails
Do not run code against production systems as a substitute for review. Do not generate credential stealers, persistence, stealth/evasion, or exploit payloads against live targets. If proof requires a dangerous action, explain the gap and use a local fixture or a non-destructive test.

## Completion criterion
Every reported issue is linked to code evidence and a verification path; uncertainties and unreviewed areas are explicit.
