#!/usr/bin/env python3
"""Dependency-free structural and safety checks for the DSH plugin package."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "engagement-scope", "secure-code-review", "web-api-assessment",
    "dependency-supply-chain", "ci-cd-security", "cloud-container-posture",
    "identity-access-review", "fuzzing-crash-triage", "incident-triage",
    "threat-modeling", "security-reporting", "remediation-retest",
}
errors: list[str] = []

def fail(message: str) -> None:
    errors.append(message)

try:
    package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
except Exception as exc:
    print(f"FAIL: package.json cannot be parsed: {exc}")
    raise SystemExit(1)

if package.get("name") != "dsh-claude-red":
    fail("unexpected package name")
if package.get("version") != "0.2.1-rc.2":
    fail("version must equal 0.2.1-rc.2")
if package.get("engines", {}).get("node") != ">=20.19.0":
    fail("Node.js engine declaration mismatch")
if package.get("dsh", {}).get("bundle", {}).get("patch") != "./cordis.patch.yml":
    fail("DSH bundle patch declaration missing or incorrect")

patch_path = ROOT / "cordis.patch.yml"
if not patch_path.is_file():
    fail("missing cordis.patch.yml")
elif "name: 'dsh-claude-red'" not in patch_path.read_text(encoding="utf-8"):
    fail("patch does not insert provider row dsh-claude-red")

index_path = ROOT / "index.js"
if not index_path.is_file():
    fail("missing index.js")
else:
    source = index_path.read_text(encoding="utf-8")
    for token in ("export const name = 'dsh-claude-red'",
                  "export const inject = ['skills']", "registerProvider", "source: 'bundled'"):
        if token not in source:
            fail(f"index.js missing provider contract marker: {token}")

actual_skills: set[str] = set()
skills_root = ROOT / "skills"
for path in sorted(skills_root.iterdir()) if skills_root.exists() else []:
    if path.is_symlink():
        fail(f"symlink not permitted: {path.relative_to(ROOT)}")
        continue
    if not path.is_dir():
        fail(f"unexpected item under skills/: {path.name}")
        continue
    actual_skills.add(path.name)
    skill_file = path / "SKILL.md"
    if not skill_file.is_file() or skill_file.is_symlink():
        fail(f"missing regular SKILL.md: {path.name}")
        continue
    content = skill_file.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.S)
    if not match:
        fail(f"invalid frontmatter/body structure: {path.name}")
        continue
    front, body = match.groups()
    name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", front, re.M)
    description = re.search(r'^description:\s*"(.+)"\s*$', front, re.M)
    if not name or name.group(1) != path.name:
        fail(f"frontmatter name must match folder: {path.name}")
    if not description or len(description.group(1)) < 30:
        fail(f"missing or short description: {path.name}")
    if len(body.strip()) < 500:
        fail(f"skill body too short: {path.name}")
    for marker in ("TODO_REPLACE_ME", "<YOUR_TOKEN>", "/Users/", "/home/"):
        if marker in content:
            fail(f"placeholder or local absolute path in {path.name}: {marker}")

if actual_skills != EXPECTED_SKILLS:
    fail(f"skill inventory mismatch; missing={sorted(EXPECTED_SKILLS-actual_skills)}, "
         f"extra={sorted(actual_skills-EXPECTED_SKILLS)}")

for required in ("README.md", "COMPATIBILITY.md", "PORTING.md", "SECURITY.md",
                 "NOTICE.md", "LICENSE", "CHANGELOG.md", "tests/smoke-provider.mjs",
                 "scripts/package_release.py", ".github/workflows/validate.yml"):
    if not (ROOT / required).is_file():
        fail(f"missing required file: {required}")

for path in ROOT.rglob("*"):
    rel = path.relative_to(ROOT)
    if path.is_symlink():
        fail(f"symlink is not permitted in public package: {rel}")
        continue
    if not path.is_file():
        continue
    parts = {p.lower() for p in rel.parts}
    name = path.name.lower()
    if "__pycache__" in parts or path.suffix in {".pyc", ".pyo"}:
        fail(f"transient Python artifact: {rel}")
    if name in {".env", ".env.local", "id_rsa", "id_ed25519", "credentials.json"}:
        fail(f"secret-shaped filename: {rel}")
    if name.endswith((".pem", ".p12", ".pfx")):
        fail(f"private-key/certificate material not permitted: {rel}")
    if len(rel.as_posix()) > 240:
        fail(f"path too long for a portable archive: {rel}")

if errors:
    print(f"FAIL: {len(errors)} issue(s)")
    for error in errors:
        print(f" - {error}")
    raise SystemExit(1)

print(f"PASS: package metadata, DSH bundle declaration, safe paths, license/notice, and "
      f"{len(actual_skills)} skill files validated.")
