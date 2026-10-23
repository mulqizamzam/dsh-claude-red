---
name: web-api-assessment
description: "Assess owned or explicitly authorized web applications and APIs with non-destructive checks for authentication, authorization, input validation, session boundaries, security headers, and business logic."
---

# Authorized Web and API Assessment

## Workflow
1. Verify the engagement scope and prefer a staging environment, test tenant, and synthetic records. Record base URLs, allowed accounts/roles, request ceilings, and the testing window.
2. Build a route and API inventory from supplied OpenAPI schemas, application routes, authorized proxy logs, or normal navigation. Do not expand scope to discovered third-party hosts.
3. Map anonymous, authenticated, low-privilege, and administrative roles to expected actions and object-level permissions.
4. Check authentication/session controls: login and logout behavior, session invalidation, MFA enforcement expectations, token expiry, cookie attributes, and safe error messages.
5. For each business object, verify server-side authorization for read/write/delete/export actions and tenant isolation using records owned by test accounts.
6. Examine input handling for parameterized queries, output encoding, schema validation, upload restrictions, path normalization, redirects, template boundaries, and safe parsing.
7. Review CSRF, CORS, cache controls, rate limiting, security headers, TLS configuration evidence, and sensitive-data exposure in responses and logs.
8. Test multi-step business rules with bounded, reversible changes; keep idempotency, replay protection, quota enforcement, and race conditions in view.
9. Capture request/response excerpts with tokens and personal data redacted. Distinguish confirmed behavior from hypotheses.
10. Convert observations into prioritized findings, fixes, and deterministic retests. Clean up test objects and confirm no unexpected state remains.

## Safe verification
Use harmless marker values and accounts explicitly provided for the test. Do not dump records, brute-force credentials, bypass access against third-party users, conduct denial-of-service testing, or execute destructive actions. If a defect would expose someone else's data, demonstrate the authorization failure with controlled synthetic records and stop before collecting unrelated data.

## Required output
Scope summary; endpoints/roles covered; checks performed; evidence; confirmed findings and confidence; not-tested areas; business impact; remediation; regression/retest steps; cleanup status.

## Stop conditions
Pause for any production degradation, unscoped host, real personal data, unexpected privileged access, or mismatch between the observed system and signed scope.
