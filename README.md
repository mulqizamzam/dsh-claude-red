# DSH Claude-Red — DeepSeek Harness Plugin

**Target runtime:** DeepSeek Harness (`@deepseek-ai/dsh`) **`0.2.1-rc.2`**  
**Package version:** `0.2.1-rc.2` (release candidate; not a claim of compatibility with future DSH versions)

A DSH-native, load-on-demand skill bundle adapted from [SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red). It turns selected security-engineering workflows into first-class DSH skills for secure code review, authorized application assessment, supply-chain review, fuzzing triage, incident response, threat modeling, reporting, and remediation.

This is a **curated defensive port**, not a mirror of every upstream offensive playbook. The upstream MIT license and attribution are retained. Operational material focused on credential theft, phishing execution, stealth/evasion, persistence, command-and-control, anti-forensics, and data exfiltration is intentionally not bundled. See [PORTING.md](PORTING.md).

## Features

- Native DSH profile bundle declared with `dsh.bundle.patch`.
- Embedded ESM provider registers package-local skills with DSH's existing `ctx.skills` registry; skill bodies load on demand.
- Twelve focused workflows with explicit scope, evidence, stop conditions, and remediation.
- Standard-library validation, Node.js provider smoke test, CI, and reproducible ZIP packaging.
- Beginner-friendly installation and runtime compatibility notes.

No separate MCP server, API token, database, telemetry service, or third-party runtime dependency is required by this plugin. DSH itself still needs a configured model/provider.

## Prerequisites

1. **Node.js 22 or newer is recommended.** Package metadata declares Node.js `>=20.19.0`; use a version supported by your DSH distribution.
2. **DeepSeek Harness `0.2.1-rc.2`.** This is a developer preview; pin the runtime while validating this release candidate.
3. **pnpm** available on `PATH` for DSH's external profile-plugin installation workflow.
4. A base-backed profile such as `web`, which provides DSH's normal skill registry and model-facing skill tool.

## Install in DSH

Check Node and pnpm:

```bash
node --version
pnpm --version
```

Start the pinned DSH runtime once to initialize the default profile if you have not used it before:

```bash
npx @deepseek-ai/dsh@0.2.1-rc.2 web
```

Stop it, then install this public GitHub bundle into the `web` profile:

```bash
npx @deepseek-ai/dsh@0.2.1-rc.2 plugin --profile web add github:mulqizamzam/dsh-claude-red#main
```

Restart the profile:

```bash
npx @deepseek-ai/dsh@0.2.1-rc.2 --profile web
```

The bundle adds one provider row, `dsh-claude-red`. On a base-backed profile, the DSH skill registry and model-facing loader are provided by the base composition. Ask the model to load a skill by name or use the skill-invocation syntax supported by your profile (for example, `/secure-code-review`).

**Pinning:** these instructions track `main` until an immutable release tag exists. For repeatable production use, pin an immutable commit or validated release tag instead of tracking `main`.

## First tasks to try

```text
Use engagement-scope to draft rules of engagement for an internal staging assessment.
Load secure-code-review and review this diff for authorization, input-validation, and secret-handling defects. Cite affected lines and propose minimal fixes.
Use dependency-supply-chain to review my package manifest and lockfile; distinguish confirmed vulnerabilities from unverified advisories.
Use fuzzing-crash-triage to plan a time-bounded fuzz run against this local parser and define safe stop conditions.
Use security-reporting to turn these verified findings into a prioritized report with impact, remediation, and retest criteria.
```

Only test systems you own or are explicitly authorized to assess. Use staging or local fixtures where practical. Avoid destructive actions, real-user data, and production traffic unless the written scope specifically permits them.

## Configuration and troubleshooting

This release has no plugin-specific environment variables. DSH uses its normal configuration for model/provider credentials and the selected profile. **Do not place API keys in `package.json`, `cordis.patch.yml`, committed `.env` files, or skill content.** Use DSH's supported settings or credential store.

| Symptom | What to check |
|---|---|
| `pnpm` is missing | Install pnpm for your Node environment, reopen the terminal, and verify `pnpm --version`. |
| Skills do not appear | Confirm DSH is pinned to `0.2.1-rc.2`, installation targets `web`, and the provider row is enabled. Restart DSH after plugin changes. |
| `ctx.skills` is unavailable | Use a base-backed profile such as `web`; this is not a standalone DSH runtime. |
| Package reports incompatibility | Do not force-allow it. Back up profile data, confirm versions, and install only a bundle validated for that runtime. |
| Assessment could be destructive | Stop, narrow the scope, move to a local/staging fixture, and obtain explicit approval first. |
| Model credentials are missing | Configure a supported DSH model/provider in DSH settings. This repository provides no credentials. |

## Validate locally

With Node.js and Python 3 installed, run:

```bash
npm run check
python3 scripts/package_release.py /tmp/dsh-claude-red-a.zip
python3 scripts/package_release.py /tmp/dsh-claude-red-b.zip
sha256sum /tmp/dsh-claude-red-a.zip /tmp/dsh-claude-red-b.zip
cmp /tmp/dsh-claude-red-a.zip /tmp/dsh-claude-red-b.zip
```

The provider smoke test uses a local stub of the DSH skill registry. It checks registration, catalog completeness, and body loading for every skill. These checks **do not replace** an installation test against a real `@deepseek-ai/dsh@0.2.1-rc.2` runtime; report that separate result independently.

## Project files

- `package.json` — package metadata and DSH bundle declaration
- `cordis.patch.yml` — profile layer that inserts the provider
- `index.js` — provider implementation
- `skills/<name>/SKILL.md` — focused workflows
- `scripts/` and `tests/` — local validation and reproducible packaging
- `COMPATIBILITY.md` — runtime scope and evidence matrix
- `PORTING.md` — source disposition and curation choices
- `SECURITY.md`, `NOTICE.md`, `LICENSE`, `CHANGELOG.md` — policies and attribution

## License and attribution

MIT-licensed curated derivative; see [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md). Original source: [SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red), by SnailSploit / Kai Aizen. DeepSeek Harness is a separate project owned by DeepSeek; this repository is an independent community plugin, not an official DeepSeek product.
