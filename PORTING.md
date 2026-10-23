# Source review and porting decisions

## Source reviewed

- Upstream: [SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red), default branch `main`.
- Supporting files inspected: `README.md`, `CONTRIBUTING.md`, `LICENSE`, `install.sh`, `convert_skills.py`, plus representative reporting, rapid-triage, and bug-identification skills.
- Runtime contract: the official [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) release tag `dsh-v0.2.1-rc.2`, including profile-bundle manifests, `ctx.skills`, the filesystem skill provider, and the model-facing skill loader.

## Architecture

This port is an installable DSH profile bundle plus an embedded skills provider. The package declares `dsh.bundle.patch`, inserts a Cordis plugin row, and registers a package-local provider through the DSH `ctx.skills` registry. It relies on the existing registry and model-facing skill loader in a base-backed profile; it does not ship a second registry or a standalone runtime service.

## Workflow disposition

| Upstream workflow | Disposition | Port decision |
|---|---|---|
| Rapid triage and assessment checklists | Transformed | Reframed around written scope, bounded checks, safe triage, and stop conditions. |
| Bug identification and code review | Preserved and enhanced | Data-flow, authorization, validation, evidence, minimal patch, and regression tests. |
| Web and API security | Preserved and enhanced | Authorized, non-destructive checks; synthetic test data; no unauthorized exploitation chain. |
| Fuzzing and crash analysis | Preserved and enhanced | Owned/staging targets, bounded runtime/resource budget, crash minimization, root-cause analysis. |
| Cloud, container, Kubernetes, identity | Transformed | Configuration review, least privilege, exposure evidence, and hardening instead of takeover playbooks. |
| CI/CD and dependency review | Preserved and enhanced | Secret-exposure prevention, provenance, build isolation, permissions, and dependency remediation. |
| Reporting and incident response | Preserved and enhanced | Evidence integrity, defensible timelines, risk communication, remediation, and retesting. |
| Threat modeling | Folded into reusable workflow | Abuse cases, trust boundaries, mitigations, ownership, and testable requirements. |
| Phishing execution, credential theft, keylogging, stealth/evasion, persistence, C2, anti-forensics, exfiltration, exploit weaponization | Excluded from public bundle | These operational playbooks are not copied. Defensive detection and incident-triage perspectives remain. |
| Claude-specific installer/converter | Replaced | The DSH-native bundle contract and provider replace Claude-only installation mechanisms. |
| License and attribution | Preserved | Upstream MIT notice retained; attribution and derivative scope are documented in `NOTICE.md`. |

## Public package hygiene

The intended package contains no credentials, private customer data, internal-only callback endpoint, bundled network client, telemetry path, or destructive automation. Skills are Markdown instructions loaded on demand and do not execute target commands by themselves. DSH's active tools, workspace, permission profile, and approvals still govern actions.

## Validation boundary

Local metadata validation and the provider stub smoke test are useful contract checks, not proof of live compatibility. Before calling the release candidate production-ready, install it into a clean DeepSeek Harness `0.2.1-rc.2` profile, confirm the catalog contains all twelve skills, load each skill, restart DSH, and confirm no compatibility warnings. Runtime network access and live installation were not available as part of the local validation pass.

This is a curated adaptation, not a byte-for-byte mirror of upstream. The curation is deliberate and should not be described as preserving every upstream operational capability.
