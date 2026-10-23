# Source review and porting decisions

## Source reviewed

- Upstream: [SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red), default branch `main`
- Supporting source files inspected: `README.md`, `CONTRIBUTING.md`, `LICENSE`, `install.sh`, `convert_skills.py`, and representative reporting, rapid-triage, and bug-identification Skills
- DSH API/format baseline: official [`deepseek-ai/deepsek-harness`](https://github.com/deepseek-ai/deepseek-harness) tag `dsh-v0.2.1-rc.2`, including the profile bundle template, bundle manifest, skill registry, filesystem provider, and model-facing skill loader documentation

## Architecture decision

**Native DSH bundle + embedded skill provider.** A skills-only instruction dump would not be a DSH installable profile plugin. This package declares `dsh.bundle.patch`, inserts its own Cordis plugin row, and registers bundled skills using `ctx.skills`. It depends on the existing base-backed profile skill registry and loader rather than bundling a second registry or duplicating the DSH runtime.

## Candidate disposition

| Upstream workflow | Disposition | Port decision |
|---|---|---|
| Fast checking / assessment checklists | `compile_skill` | Reframed as explicit scoping and safe triage; no broad unauthenticated scanning recipe. |
| Bug identification / code review | `compile_skill` | Preserved as secure code review with data-flow, authorization, validation, evidence, and remediation focus. |
| Web and API security | `compile_skill` | Preserved as authorized, non-destructive testing; no credential theft or exploitation chains. |
| Fuzzing and crash analysis | `compile_skill` | Preserved for owned/staging targets, bounded runs, crash minimization, and root-cause analysis; no weaponization. |
| Cloud, container, Kubernetes | `compile_skill` | Reframed toward posture review, least privilege, exposure checks, and hardening. |
| Active Directory / privilege escalation | `compile_skill` | Reframed as identity, directory, privileged-access, and least-privilege review; no credential-dumping or takeover procedures. |
| CI/CD and dependency review | `compile_skill` | Preserved as build-pipeline hardening, secret exposure prevention, provenance, and dependency remediation. |
| Cryptography and transport security | `reference_only` / folded into secure review | Coverage is represented through the relevant review workflows rather than copied as an attack cookbook. |
| Incident evidence and reporting | `compile_skill` | Preserved as evidence integrity, timelines, impact, reporting, and safe retesting. |
| AI security | `reference_only` / folded into threat modeling | Prompt injection and data-boundary concerns are handled as threat-model topics, not as jailbreak or model-extraction instructions. |
| Phishing execution, credential capture, keylogging, stealth/EDR evasion, persistence, command-and-control, anti-forensics, exfiltration, exploit weaponization | `discard` from public bundle | Not mirrored as operational procedures. Defensive detection and response perspectives remain covered by incident triage and threat modeling. |
| Claude-specific installer and converter | `discard` / `reference_only` | Replaced by DSH's native `dsh.bundle.patch` and provider contract; no Claude-only install paths are included. |
| MIT License and attribution | `preserve` | Full license retained and attribution documented. |

## Public exclusions

No secrets, tokens, private organization instructions, customer data, hidden telemetry, external callback endpoints, destructive automation, or credential-collection logic are included. The plugin itself makes no network requests and has no side effects beyond registering skills and reading its package-local Markdown files when a skill is loaded.

## Preservation limit

This is not a byte-for-byte mirror of the upstream catalog. The upstream repository's highest-risk operational playbooks are intentionally excluded or transformed into defensive review guidance. The curated port focuses on workflows suitable for a general-purpose public engineering assistant.
