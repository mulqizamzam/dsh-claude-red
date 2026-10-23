---
name: security-reporting
description: "Turn verified security assessment evidence into prioritized, reproducible findings with impact, severity rationale, remediation, and retest criteria."
---

# Security Reporting

## Report structure
1. Executive summary: assessment context, scope, overall risk posture, finding counts, material business impact, and the top three program-level recommendations.
2. Engagement overview: authorization and scope, methodology, dates, assumptions, limitations, and test accounts.
3. Risk summary: findings by severity, status, affected asset classes, and business-critical exposure.
4. Technical findings: one finding per distinct root cause or materially different impact.
5. Remediation roadmap: quick wins, structural fixes, owners, milestones, dependencies, and retest plan.
6. Appendices: evidence index, tool versions, glossary, and references.

## Technical finding template
- Title: concise statement of the security condition and affected component.
- Severity: rating with a documented framework and explicit assumptions.
- Affected scope: exact application/service/version/path or resource identifier.
- Evidence: timestamps, redacted excerpts, hashes, relevant lines, and a repeatable safe test.
- Preconditions: required role, configuration, user interaction, and exposure.
- Analysis: observed behavior, expected control, root cause, impact, and confidence.
- Remediation: specific developer action and safe alternatives if a direct fix is unavailable.
- Verification: regression test, expected safe outcome, and retest prerequisites.

## Quality review
Draft technical findings before the executive summary. Check reproducibility, evidence provenance, duplicates, consistent severity, clear distinction between confirmed and suspected behavior, and whether each recommendation addresses root cause. Have a technical reviewer verify accuracy and a stakeholder-oriented reviewer verify clarity.

## Evidence hygiene
Redact credentials, tokens, personal information, customer identifiers, and unnecessary raw data. Preserve an evidence manifest and approved retention/deletion policy. Never fabricate proof, timelines, CVSS vectors, or affected versions.

## Completion criterion
A reader can understand the business risk, reproduce the verified finding safely, assign a fix, and determine whether remediation worked.
