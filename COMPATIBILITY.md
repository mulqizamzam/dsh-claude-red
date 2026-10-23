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

| Check | Evidence | Result |
|---|---|---|
| Package metadata, paths, skill frontmatter and public-package hygiene | `python3 scripts/validate_package.py` in GitHub Actions | PASS |
| Provider registration, 12-skill catalog, full-body loading and error paths | `node tests/smoke-provider.mjs` in GitHub Actions | PASS; uses a local registry stub |
| Repeatable release archive | Two independently generated ZIPs compared with `cmp` and SHA-256 | PASS; identical SHA-256: `3f68be23fb77ad55f2b3be71b816257f8b5a294daefd5324716e9dc5a391d30a` |
| Install into a clean DSH web profile | GitHub Actions run [40003147618](https://github.com/mulqizamzam/dsh-claude-red/actions/runs/40003147618): install with `dsh plugin --profile web add`, then dump and inspect the composed profile | PASS |
| Import the installed package using Node in the DSH profile | Same GitHub Actions run: import `dsh-claude-red`, register the provider, list skills, and load all 12 bodies | PASS |
| Full model-session invocation | Requires a configured model credential and actual model request | NOT RUN; provider/profile checks do not prove model-call behavior |
| CI result on the published branch | [GitHub Actions run 40003147618](https://github.com/mulqizamzam/dsh-claude-red/actions/runs/40003147618) | PASS |

The GitHub Actions run validates the real DSH `0.2.1-rc.2` package-install and provider-load path without making a model API request. It does not claim an end-to-end model conversation has been tested.

## Upgrade policy

This version is a release candidate for one explicitly targeted DSH runtime. Do not treat it as compatible with later or older DSH versions without rerunning install, provider, skill-load, and profile-restart checks. Do not force-allow an incompatible plugin version to bypass runtime checks.
