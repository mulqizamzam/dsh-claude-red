---
name: identity-access-review
description: "Review authentication, authorization, privileged access, directory settings, service principals, session controls, and least-privilege boundaries using configuration evidence and defensive recommendations."
---

# Identity and Access Review

## Workflow
1. Define the identity provider, tenant/domain, applications, account classes, and read-only review permissions. Use approved test identities only.
2. Map joiner/mover/leaver processes, MFA requirements, recovery methods, account lifecycle, session lifetime, device posture, and emergency-access procedures.
3. Review roles and permissions at user, group, application, service-principal, workload, and directory levels. Identify stale grants, role nesting, wildcard scopes, dormant accounts, and risky privilege combinations.
4. Check authorization enforcement at both UI and backend/API layers. Confirm tenant and object ownership are verified server-side rather than trusting client claims.
5. Review service identities, OAuth scopes, redirect URI configuration, token audience/issuer/expiry validation, signing-key rotation, and credential storage. Record configuration gaps, never token contents.
6. For directory services, inspect password and lockout policy, delegation configuration, certificate services, group policy, trust boundaries, audit coverage, and privileged administrator separation.
7. Compare effective access with documented responsibilities. Validate findings with the owner before revoking or changing access.
8. Recommend staged remediation, owner assignment, review deadlines, monitoring, and a rollback path for critical service identities.

## Finding format
Include principal/role, resource/scope, evidence, excess privilege or control gap, business impact, confidence, least-privilege change, owner, and verification plan. Aggregate identity details and avoid unnecessary personal data.

## Guardrails
Do not harvest or crack credentials, request password dumps, perform unauthorized impersonation, or make live access changes. Access changes require explicit approval and testing against documented service dependencies.

## Completion criterion
The access graph and highest-risk excessive privileges are understandable, evidenced, and paired with low-risk remediation steps.
