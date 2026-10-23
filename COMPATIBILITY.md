# Compatibility and validation

## Target

- DeepSeek Harness: `@deepseek-ai/dsh@0.2.1-rc.2`
- Runtime channel: pre-release / developer preview
- Plugin package version: `0.2.1-rc.2`
- Node.js: package minimum `20.19.0`; Node.js 22+ recommended
- Format: ESM Cordis plugin plus a profile-bundle patch (`dsh.bundle.patch` → `cordis.patch.yml`)

## Runtime contract used

The implementation follows the DSH `0.2.1-rc.2` source contract: an installable profile bundle declares `dsh.bundle.patch`; the patch inserts a Cordis plugin row; and the plugin registers an embedded skill provider with the base profile's `ctx.skills` registry. It relies on the normal skill catalog/loader already active in a base-backed profile and adds no new network service or runtime package dependency.

## Validation matrix

| Check | Command/evidence | Status semantics |
|---|---|---|
| Package metadata / paths / skill frontmatter | `python3 scripts/validate_package.py` | Locally verified when exit code is 0 |
| Provider registration / list / load | `node tests/smoke-provider.mjs` | Stubbed provider contract; not a live DSH integration test |
| Combined local suite | `npm run check` | Executes both local checks |
| Reproducible source archive | Run `scripts/package_release.py` twice and compare SHA-256 | Validates deterministic archive creation |
| Install into a clean DSH profile | `dsh plugin --profile web add github:mulqizamzam/dsh-claude-red#main`, then restart DSH | Must be run against actual DSH `0.2.1-rc.2`; not implied by local tests |
| Clean-session skill invocation | Invoke a skill in a fresh `web` session | Must be run against actual runtime; verify catalog and full-body loading |
| GitHub Actions | `.github/workflows/validate.yml` | CI result must be read from the target repository after push |

## Upgrade policy

This version is a release candidate for one explicitly targeted DSH runtime. Do not treat it as compatible with later or older DSH versions without rerunning install, provider, skill-load, and profile-restart checks. Do not force-allow an incompatible plugin version to bypass runtime checks.
