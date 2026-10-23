---
name: fuzzing-crash-triage
description: "Plan bounded fuzz tests for software owned by the user or explicitly authorized for testing, minimize crashes, identify root causes, and document fixes without weaponizing vulnerabilities."
---

# Fuzzing and Crash Triage

## Workflow
1. Identify the target parser/component, supported inputs, source/build commit, runtime/compiler, and written authorization. Prefer a local target or isolated staging build.
2. Choose a fuzzing strategy suited to the interface: mutation-based, grammar-aware, property-based, or coverage-guided. Set duration, worker count, memory/CPU budgets, and disk limits before launch.
3. Build with suitable diagnostics when available (address/undefined behavior sanitizers, assertions, debug symbols, coverage instrumentation). Keep production credentials and network access out of the test environment.
4. Seed with representative valid/invalid inputs and redact proprietary or personal data. Preserve seeds and corpus provenance.
5. Define observable failure oracles: crash, sanitizer report, invariant violation, timeout, unexpected resource growth, or differential mismatch.
6. Run within the agreed budget. Stop at the time/resource cap, on instability beyond the lab, or if a target contacts external systems unexpectedly.
7. Deduplicate crashes by stack trace, signal, sanitizer class, and minimized reproducer. Save the original artifact and a minimization log.
8. Reduce each case to a small deterministic fixture and reproduce with the same build/runtime. Distinguish reproducible defects from environmental noise.
9. Trace the root cause, affected code, triggering preconditions, data integrity/availability impact, and a minimal patch. Avoid constructing a weaponized exploit or testing against a third-party service.
10. Add regression/property tests and rerun the minimized cases against fixed and baseline builds when authorized.

## Deliverables
Target and budget, tool/build config, corpus provenance, coverage trend if available, deduplicated crashes, minimized input hashes, root-cause notes, patch/test, unresolved cases, and cleanup.

## Guardrails
No internet-scale fuzzing, denial-of-service against live systems, exploit-chain development, or publication of sensitive crash data before responsible disclosure coordination.

## Completion criterion
Each prioritized crash is reproducible with a minimal local fixture or explicitly marked unconfirmed and has a clear engineering next step.
