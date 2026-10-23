---
name: engagement-scope
description: "Create a written rules-of-engagement plan before any security assessment, including assets, ownership, allowed techniques, test windows, rate limits, data boundaries, contacts, and stop conditions."
---

# Authorized Assessment Scope

## Objective
Produce a test plan that makes the authorization boundary concrete enough for a second operator to follow without guessing.

## Workflow
1. Identify the commissioning party, the technical owner, and the person who can pause testing.
2. Enumerate exact in-scope hosts, applications, accounts, cloud tenants, repositories, and environments. Record exclusions explicitly; do not infer that a related domain or IP is included.
3. Record the authorization evidence, dates, time zone, testing window, source addresses, allowed test accounts, and change/incident contact paths.
4. Classify techniques as **allowed**, **prohibited**, or **requires written approval**. Treat denial-of-service, destructive state changes, social engineering, physical access, persistence, credential collection, and production data access as prohibited unless a specifically reviewed scope says otherwise.
5. Define safe ceilings: request rate, concurrency, payload sizes, run duration, target count, and resource budget.
6. Define evidence handling: minimum data collected, redaction, secure storage, retention/deletion date, and who may receive the report.
7. Add explicit stop triggers: service degradation, unexpected customer data, scope ambiguity, access to another tenant, critical exposure, incident response request, or contact unavailability.
8. Require written confirmation from the asset owner and a kickoff check before active testing.

## Required output
Return a concise engagement card with: objective, authorization evidence, exact scope, excluded targets, allowed methods, approval gates, schedule/time zone, test accounts, ceilings, evidence policy, incident contacts, stop conditions, and sign-off status.

## Decision rules
- Missing authorization or ambiguous ownership means **planning only**; do not run tests.
- A new host discovered during testing is not automatically in scope.
- A request to broaden scope requires a recorded change and approval before action.
- If the target is production, prefer passive/read-only checks and staging reproduction for disruptive validations.

## Completion criterion
A reviewer can determine exactly what may be tested, when, how aggressively, what evidence may be kept, and when work must stop.
