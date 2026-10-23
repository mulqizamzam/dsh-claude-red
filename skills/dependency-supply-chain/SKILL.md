---
name: dependency-supply-chain
description: "Audit dependency manifests and lockfiles, known vulnerability advisories, maintainer and provenance signals, install scripts, dependency confusion risks, and remediation options without extracting secrets."
---

# Dependency and Supply-Chain Review

## Workflow
1. Inventory supported manifests and lockfiles; record package manager, runtime versions, registry sources, and exact commit.
2. Confirm the lockfile corresponds to the manifest. Identify unpinned, GiT, URL, local, optional, dev, peer, and transitive dependencies.
3. Prefer machine-readable audit/SBOM output from approved tooling. Record database/source, query date, package ecosystem, affected version range, and fixed version.
4. Validate each advisory against installed versions and reachable code paths. Separate direct vs. transitive dependencies, runtime vs. build-only exposure, and confirmed vs. uncertain results.
5. Inspect lifecycle/install scripts, registry scopes, lockfile integrity hashes, package provenance/signatures where supported, ownership/maintenance signals, dependency-name typos, and private/public namespace collisions.
6. Review CI install permissions, token scopes, lockfile mutation practices, release provenance, artifact signing, and whether untrusted PR code can access secrets or publish rights.
7. Prioritize by reachable vulnerability, privilege, internet exposure, business impact, exploit maturity, and availability of a safe patch or mitigation.
8. Propose a minimal update path; mention breaking changes, transitive resolution, compatibility risks, and rollback. Do not blindly bulk-upgrade or edit a lockfile without project test context.
9. Recommend CI controls: lockfile enforcement, provenance verification, least-privilege publishing, secret isolation, dependency review, and recurring scans.

## Evidence standard
For every issue include package/version, advisory identifier and source, vulnerable range, fixed version, evidence the installed graph includes it, exposure reasoning, urgency, remediation, and test plan. A scanner's severity is a signal, not a substitute for applicability analysis.

## Guardrails
Never print environment secrets, registry credentials, private package contents, or personal data. Do not attempt to publish a test package to public registries. Dependency confusion checks should be configuration review or isolated, owner-approved simulation only.

## Completion criterion
The report identifies actionable, verified dependency risks and safe updates while preserving the reproducible dependency graph.
