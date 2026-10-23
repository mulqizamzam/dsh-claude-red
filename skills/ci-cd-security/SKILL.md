---
name: ci-cd-security
description: "Review source-control workflows, build permissions, secret handling, untrusted pull-request behavior, artifact provenance, release controls, and deployment gates without extracting credentials."
---

# CI/CD Security Review

## Workflow
1. Inventory CI workflows, reusable workflows, build scripts, deployment manifests, environments, runners, artifact stores, and publishing identities.
2. Classify trigger sources: trusted branch pushes, protected releases, fork pull requests, issue/comment events, scheduled jobs, and manual dispatch. Trace which events execute untrusted code.
3. Apply least privilege to token permissions. Prefer read-only defaults; grant write, package-publish, or cloud deploy access only to the exact job requiring it.
4. Trace secrets from source to sinks. Check whether fork PRs, logs, command-line arguments, artifacts, caches, debug output, or model prompts could expose them. Report variable names and locations, not values.
5. Inspect injection boundaries in workflow expressions, shell commands, branch/tag inputs, artifact names, path filters, and outputs. Prefer environment variables and validated inputs over string interpolation into commands.
6. Check action/plugin pinning, third-party action provenance, runner isolation, cache key trust, artifact download integrity, and separation of build/test/deploy privileges.
7. Verify environment protection, required reviews, branch protections, approval gates, provenance/attestation, signing, version/tag immutability, and rollback procedures.
8. Recommend small, independently testable workflow changes. Ensure pipeline changes cannot reveal credentials or allow untrusted jobs to deploy.
9. Test only on a fork, sandbox runner, or non-production workflow where possible; preserve ixsting build/deploy behavior and document any required secret/config names.

## Finding output
State trigger, trust boundary, vulnerable workflow lines, attacker-controlled input, permission/secret impact, confidence, minimal fix, and a regression test. Never reveal secret values even if found in logs or fixtures.

## Guardrails
No secret exfiltration, runner compromise, persistence, or live deployment probes. A suspected exposed secret should be redacted, scoped to the minimum evidence, and rotated via the authorized owner process.

## Completion criterion
Each finding explains what untrusted actor can influence which privileged job and how to reduce that path without breaking legitimate releases.
