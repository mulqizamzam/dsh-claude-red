---
name: threat-modeling
description: "Create a practical threat model from system boundaries, assets, data flows, trust transitions, abuse cases, mitigations, and testable security requirements."
---

# Practical Threat Modeling

## Workflow
1. Define the business purpose, system owner, architecture version, scope, assumptions, non-goals, and review participants.
2. Inventory assets and security objectives: confidentiality, integrity, availability, privacy, accountability, and recovery.
3. Draw components, users, services, data stores, external dependencies, trust boundaries, and data flows. Mark authentication, authorization, and privilege transitions.
4. Enumerate realistic abuse cases against each flow: spoofing, tampering, repudiation, information disclosure, denial of service, privilege escalation, unsafe deserialization, and workflow abuse as applicable.
5. Identify preconditions, attacker capability, reachable entry point, control gaps, blast radius, and assumptions that need evidence.
6. Map each threat to preventive, detective, and recovery controls. Prefer enforceable server-side controls and secure defaults to policy statements alone.
7. Prioritize by likelihood, impact, exposure, exploit preconditions, and mitigation cost. Explain uncertainty rather than presenting a numeric risk score as fact.
8. Convert prioritized threats into engineering requirements, acceptance criteria, owners, and verification tests. Revisit after material architecture or dependency changes.

## Deliverables
Architecture/data-flow diagram or textual equivalent; assets and trust boundaries; threat register; assumptions and evidence gaps; mitigations with owners; tests and residual risk; approval record.

## Guardrails
Model realistic risk without generating weaponized exploit chains or instructions for unauthorized access. Use synthetic data and isolated fixtures for proof-of-concept testing. Label unverified assumptions explicitly.

## Completion criterion
A developer can map each high-priority threat to a concrete control and a reproducible test that verifies the control.
