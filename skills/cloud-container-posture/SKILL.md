---
name: cloud-container-posture
description: "Review cloud IAM, storage exposure, network boundaries, container images, Kubernetes policy, workload identity, and deployment hardening using authorized configuration and read-only evidence."
---

# Cloud and Container Posture Review

## Workflow
1. Confirm the account, project, tenant, cluster, namespaces, image registries, environment, and read-only audit permissions. Do not enumerate resources outside the stated boundary.
2. Inventory identity roles and trust policies. Identify wildcard scopes, privilege combinations, long-lived credentials, and workload identities that inherit human access.
3. Review storage and data services for public exposure, cross-tenant policy mistakes, encryption defaults, backup controls, and audit logging. Use configuration evidence before considering any access test.
4. Inspect network ingress/egress, security groups/firewalls, metadata access, private endpoints, DNS, TLS, and control-plane boundaries.
5. Review container base-image age, non-root execution, capabilities, writable filesystems, pinned digests, provenance, vulnerability reports, and secret inclusion risks.
6. For Kubernetes, review RBAC, service accounts, admission policy, pod security, namespace isolation, privileged pods, hostPath, secret mounts, network policy, and audit logs.
7. Check image-pull and deployment identities, CI-to-cloud federation, runtime permissions, resource limits, readiness/liveness, and rollback strategy.
8. Rank issues by reachability, blast radius, privilege, data sensitivity, and recovery options. Propose a minimal configuration diff and safe verification plan.

## Evidence and boundaries
Prefer supplied policy/configuration snapshots and results from an authorized read-only identity. Do not retrieve customer data or secret values. A `public` policy flag indicates a configuration risk, not proof that sensitive content was accessed.

## Required output
Scope and inventory; evidence source and date; misconfiguration; plausible impact; confidence; least-privilege correction; validation command or policy assertion; rollback consideration.

## Stop conditions
Stop if unexpected write/delete permissions are required, sensitive data is returned, cross-account ownership is ambiguous, or the review creates billable or disruptive resources.
