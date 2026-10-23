# Security policy

## Intended use

Use this plugin for defensive security engineering, code review, authorized assessments, lab/staging validation, incident triage, and remediation. Test only assets you own or have explicit written authorization to assess. Respect scope, rate limits, data-handling obligations, and stop conditions.

The plugin provides instructions only; it does not authorize access, run scanners by itself, or grant operating-system permissions. DSH's active tools, workspace, permission policy, and user approvals govern real actions.

## Safe handling

- Start with read-only discovery and validate scope before changes.
- Prefer local fixtures and staging; keep tests time-bounded and non-destructive.
- Do not request, copy, commit, or publish secrets, access tokens, private keys, customer data, or production records.
- Preserve logs and evidence during incidents; do not erase traces or disable defensive controls.
- Obtain explicit approval before mutating source, infrastructure, identity controls, or production configuration.

## Reporting issues

Please report a reproducible bug or unsafe instruction through the repository's GitHub Issues with the minimum evidence needed. Redact secrets and personal/customer data before posting. For a vulnerability in the DSH runtime itself, report it to the official DeepSeek Harness project rather than attributing it to this independent plugin.

## Scope

This repository contains a local skill provider and Markdown instruction files. It has no network client, telemetry, credential handling, or bundled third-party executable. This statement describes the current repository implementation and should be rechecked for every release.
