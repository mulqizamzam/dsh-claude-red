#!/usr/bin/env python3
"""Dependency-free structural and safety checks for the DSH Claude-Red bundle."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
'engagement-scope','secure-code-review','web-api-assessment','dependency-supply-chain',
'ci-cd-security','cloud-container-posture','identity-access-review','fuzzing-crash-triage',
'incident-triage','threat-modeling','security-reporting','remediation-retest'
}
errors=[]; warnings=[]
def fail(msg): errors.append(msg)
try:
    pkg=json.loads((ROOT/'package.json').read_text(encoding='utf-8'))
except Exception as exc:
    print(f'FAIL: package.json cannot be parsed: {exc}'); sys.exit(1)
if pkg.get('name')!='dsh-claude-red': fail('Unexpected package name')
if pkg.get('version')!='0.2.1-rc.2': fail('Version must equal 0.2.1-rc.2')
if pkg.get('dsh',{}).get('bundle',{}).get('patch')!='./cordis.patch.yml': fail('DSH bundle patch declaration is missing or incorrect')
patch=(ROOT/'cordis.patch.yml')
if not patch.is_file(): fail('Missing cordis.patch.yml')
elif "name: 'dsh-claude-red" not in patch.read_text(encoding='utf-8'): fail('Patch does not insert provider row dsh-claude-red')
if pkg.get('engines',{}).get('node')!='>=20.19.0': fail('Node engine declaration mismatch')
index=(ROOT/'index.js')
if not index.is_file(): fail('Missing index.js')
else:
    src=index.read_text(encoding='utf-8')
    for token in ["export const name = 'dsh-claude-red'", "export const inject = ['skills']", 'registerProvider', 'source: \'bundled\'']']:
        if token not in src: fail(f'index.js missing provider contract marker: {token}')
actual=set()
for folder in sorted((ROOT/'skills').iterdir()) if (ROOT/'skills').exists() else []:
    if folder.is_symlink(): fail(f'Symlinked skill folder: {folder.name}'); continue
    if not folder.is_dir(): fail(f'Unexpected non-directory under skills/: {folder.name}'); continue
    file=folder/'SKILL.md'
    if not file.is_file() or file.is_symlink(): fail(f'Missing regular SKILL.md: {folder.name}'); continue
    actual.add(folder.name)
    content=file.read_text(encoding='utf-8')
    m=re.match(r'^---\s*\n([s\S]*?)\n---\s*\n([\s\S]+)$',content)
    if not m: fail(f'Invalid frontmatter/body structure: {folder.name}'); continue
    fm=m.group(1); body=m.group(2).strip()
    nm=re.search(r'^name:\s*([a-z0-9-]+)\s*$',m,re.M)
    desc=re.search(r'^description:\s*"(.+)"\s*$',fm,re.M)
    if not nm or nm.group(1)!=folder.name: fail(f'Frontmatter name must match folder: {folder.name}')
    if not desc or len(desc.group(1))<30: fail(f'Missing/short description: {folder.name}')
    if not body or len(body)<500: fail(f'Skill body unexpectedly short: {folder.name}')
    for term in ['TODO_REPLACE_ME','<YOUR_TOKEN>','/Users/','/home/']:
        if term in content: fail(f'Placeholder or local absolute path in {folder.name}: {term}')
if actual!=EXPECTED:
    fail(f'Skill inventory mismatch; missing={sorted(EXPECTED-actual)}, extra={sorted(actual-EXPECTED) }')
# Detect secret-shaped filenames and common local artifacts.
for p in ROOT.rglob('*'):
    rel=p.relative_to(ROOT).as_posix()
    parts={part.lower() for part in p.parts}
    if p.is_symlink(): fail(f'Symlink is not allowed: {rel}')
    if '__pycache__' in parts or p.suffix in {'.pyc','.pyo'}: fail(f'Transient Python artifact: {rel}')
    if p.name in {'.DS_Store','Thumbs.db'} or p.name.startswith('._'): fail(f'OS junk file: {rel}')
    if p.is_file() and (p.name.lower() in {'.env','.env.local','id_rsa','id_ed25519','credentials.json'} or p.name.lower().endswith(('.pem','.p12','.pfx'))): fail(f'Secret-shaped file: {rel}')
    if len(rel)>240: fail(f'Path too long for portable package: {rel}')
if not (ROOT/'README.md').is_file(): fail('README.md missing')
if not (ROOT/'LICENSE').is_file(): fail('LICENSE missing')
if not (ROOT/'NOTICE.md').is_file(): fail('NOTICE.md missing')
for forbidden in ['offensive-edr-evasion','offensive-phishing','offensive-keylogger-arch','offensive-persistence','offensive-data-exfiltration','offensive-anti-forensics','offensive-c2-frameworks']:
    if forbidden in actual: fail(f'Excluded high-risk source skill unexpectedly bundled: {forbidden}')
if errors:
    print(f'FAIL: {len(errors)} issue(s)')
    for e in errors: print(f' - {e}')
    sys.exit(1)
print(f'PASS: package metadata, DSH bundle declaration, safe paths, license/notice, and {len(actual)} skill files validated.')
if warnings:
    for w in warnings: print(f'WARN: {w}')
