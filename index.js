import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

/** Cordis plugin identity used by cordis.patch.yml. */
export const name = 'dsh-claude-red';
/** The DSH skill registry is provided by base-backed profiles. */
export const inject = ['skills'];

const PROVIDER_NAME = 'dsh-claude-red';
const SKILLS_ROOT_URL = new URL('./skills/', import.meta.url);
const SKILLS_ROOT = fileURLToPath(SKILLS_ROOT_URL);
const RESOURCE_BASE = Object.freeze({ kind: 'directory', path: SKILLS_ROOT });
const INVOCATION = Object.freeze({ modelInvocable: true, userInvocable: true });
const RANK = 600;

const SPECS = Object.freeze([
  ['engagement-scope', 'Set an authorized assessment boundary, rules of engagement, safety limits, and stop conditions before testing.'],
  ['secure-code-review', 'Review application code for security defects using trust boundaries, data flow, authorization, input validation, and evidence-led remediation.'],
  ['web-api-assessment', 'Assess owned or explicitly authorized web applications and APIs with non-destructive checks for authentication, authorization, validation, and business-logic flaws.'],
  ['dependency-supply-chain', 'Audit dependency manifests, lockfiles, provenance, dependency confusion exposure, and known-vulnerability findings; prioritize safe remediation.'],
  ['ci-cd-security', 'Review CI/CD workflows, build permissions, secret handling, artifact provenance, and deployment controls without extracting credentials.'],
  ['cloud-container-posture', 'Review cloud IAM, storage exposure, container configuration, Kubernetes policy, and hardening evidence in authorized environments.'],
  ['identity-access-review', 'Review identity, authentication, authorization, privileged access, and directory controls with least-privilege recommendations.'],
  ['fuzzing-crash-triage', 'Plan bounded fuzz tests for software you own or are authorized to test, then minimize crashes and document root causes without weaponizing them.'],
  ['incident-triage', 'Triage security alerts and suspicious artifacts, preserve evidence, build a timeline, and recommend containment and recovery actions.'],
  ['threat-modeling', 'Create a practical threat model from system boundaries, assets, trust transitions, abuse cases, mitigations, and verification steps.'],
  ['security-reporting', 'Turn verified assessment evidence into executive summaries, reproducible findings, severity rationale, remediation guidance, and retest criteria.'],
  ['remediation-retest', 'Translate confirmed findings into actionable fixes and design non-destructive retests that prove whether remediation worked.']
].map(([name, description]) => Object.freeze({
  name,
  description,
  invocation: INVOCATION,
  provider: PROVIDER_NAME,
  source: 'bundled',
  rank: RANK,
  resourceBase: RESOURCE_BASE,
  locator: new URL(`./skills/${name}/SKILL.md`, import.meta.url)
})));

const BY_NAME = new Map(SPECS.map((candidate) => [candidate.name, candidate]));

function stripFrontmatter(markdown) {
  return markdown.replace(/^---\s*\r?\n[\s\S]*?\r?\n---\s*\r?\n/, '').trimStart();
}

const provider = Object.freeze({
  name: PROVIDER_NAME,
  list: async () => [...SPECS],
  async get(candidate) {
    const spec = BY_NAME.get(candidate?.name);
    if (!spec) throw new Error(`Unknown dsh-claude-red skill: ${String(candidate?.name ?? '')}`);
    const raw = await readFile(spec.locator, 'utf8');
    return {
      name: spec.name,
      description: spec.description,
      invocation: spec.invocation,
      provider: spec.provider,
      source: spec.source,
      resourceBase: spec.resourceBase,
      content: stripFrontmatter(raw)
    };
  }
});

/** Register the immutable, package-local skill catalog with DSH. */
export function apply(ctx) {
  if (!ctx?.skills || typeof ctx.skills.registerProvider !== 'function') {
    throw new TypeError('dsh-claude-red requires the DSH ctx.skills registry (use a base-backed profile).');
  }
  ctx.skills.registerProvider(() => provider);
}
