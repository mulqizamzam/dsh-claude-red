---
name: remediation-retest
description: "Translate confirmed security findings into minimal fixes and safe regression tests, then verify remediation without causing new production impact."
---

# Remediation and Retest

## Workflow
1. Gather the canonical finding, affected revision and environment, evidence, severity rationale, prerequisites, and previously agreed scope.
2. Identify the root cause and the control that should prevent the condition. Separate symptoms from the underlying trust, validation, authorization, or configuration defect.
3. Propose the smallest maintainable change. Prefer established framework controls and deny-by-default behavior; note migration, performance, compatibility, and rollback risks.
4. Define a failing regression test that reproduces the reported condition using a local or staging fixture and synthetic data. Add boundary cases and a test of legitimate behavior that must remain supported.
5. Review related code paths, permissions, logging, deployment configuration, dependencies, and feature flags for adjacent regressions.
6. Run the focused test, relevant unit/integration suites, static analysis, and build checks. Record exact commands, versions, outcomes, and any checks not run.
7. Retest the original observable condition with the same preconditions in an approved environment. Confirm both that the defect is blocked and expected functionality still works.
8. Update finding status only from evidence: fixed and verified, fixed with residual risk, partially mitigated, not fixed, or unable to retest. Assign remaining actions and dates.

## Output
Root cause; proposed patch; failing-before/passing-after test evidence; regression coverage; deployment/rollback steps; retest environment and date; remaining risk and owner.

## Guardrails
Do not apply changes to production without approval. Do not use destructive payloads, bypass live controls, or collect unrelated data. When a safe reproduction is unavailable, report the verification gap instead of inferring success.

## Completion criterion
A maintainer can review the minimal patch, reproduce the regression test, confirm expected behavior remains intact, and track remaining risk to closure.
