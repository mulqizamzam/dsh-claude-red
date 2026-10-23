---
name: incident-triage
description: "Triage security alerts and suspicious artifacts, preserve evidence, build a defensible timeline, scope impact, and recommend containment and recovery actions."
---

# Incident Triage and Evidence Handling

## Workflow
1. Record alert source, detection time and timezone, affected system, reporter, incident lead, and acquisition permissions. Distinguish event time from report time.
2. Preserve relevant logs and artifacts with hashes, acquisition timestamps, source identifiers, and chain-of-custody notes. Avoid modifying the system under investigation unless approved containment requires it.
3. Establish a timeline from identity, endpoint, application, network, cloud, and CI/CD logs. Normalize timestamps and annotate clock drift, gaps, retention limits, and confidence.
4. Separate observed facts, hypotheses, and unknowns. Correlate events without treating temporal coincidence as proof of causation.
5. Determine potentially affected accounts, assets, data classes, privileges, and persistence indicators using authorized telemetry. Minimize collection of unrelated personal or customer data.
6. Recommend proportional containment options, required approver, operational impact, preservation implications, rollback, and monitoring. Escalate immediately when safety, regulated data, or broad privilege is involved.
7. Identify root-cause hypotheses and evidence required to confirm or reject each. Keep investigation notes distinct from verified findings.
8. Define recovery validation, credential rotation through the owner's approved process, integrity checks, enhanced monitoring, and closure criteria.

## Output
Executive incident summary; confirmed facts; timeline with evidence pointers; scope and confidence; affected assets/data; containment decision log; open hypotheses; recovery tasks, owners and deadlines; legal/compliance escalation questions.

## Guardrails
Do not erase logs, destroy artifacts, disable defensive controls, or disclose incident details broadly. Use approved channels and redact credentials, tokens, personal identifiers, and customer content in shared reports.
