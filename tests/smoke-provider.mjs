import assert from 'node:assert/strict';
import { apply, inject, name } from '../index.js';

const providers = [];
const ctx = { skills: { registerProvider(factory) { providers.push(factory()); } } };
assert.equal(name, 'dsh-claude-red');
assert.deepEqual(inject, ['skills']);
apply(ctx);
assert.equal(providers.length, 1);
const provider = providers[0];
assert.equal(provider.name, 'dsh-claude-red');
const skills = await provider.list();
assert.equal(skills.length, 12);
assert.equal(new Set(skills.map(s => s.name)).size, 12);
for (const skill of skills) {
  assert.ok(skill.description.length > 20, `description missing: ${skill.name}`);
  assert.equal(skill.invocation.modelInvocable, true);
  assert.equal(skill.invocation.userInvocable, true);
  const loaded = await provider.get(skill);
  assert.equal(loaded.name, skill.name);
  assert.ok(loaded.content.includes('# '), `content missing heading: ${skill.name}`);
  assert.ok(!loaded.content.startsWith('---'), `frontmatter was not stripped: ${skill.name}`);
}
await assert.rejects(() => provider.get({ name: 'not-a-skill' }), /Unknown dsh-claude-red skill/);
assert.throws(() => apply({}), /requires the DSH ctx.skills registry/);
console.log(`PASS: registered ${skills.length} skills; catalog, on-demand loading, errors, and prerequisites verified.`);
