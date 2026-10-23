#!/usr/bin/env python3
"""Create a deterministic ZIP release archive without build dependencies."""
from __future__ import annotations

import argparse
import hashlib
import stat
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_PARTS = {".git", "node_modules", "__pycache__", ".pytest_cache"}
EXCLUDE_NAMES = {".DS_Store", "Thumbs.db"}
EXCLUDE_SUFFIXES = {".pyc", ".pyo"}

def included(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if any(part in EXCLUDE_PARTS for part in rel.parts):
        return False
    if path.name in EXCLUDE_NAMES or path.name.startswith("._"):
        return False
    if path.suffix in EXCLUDE_SUFFIXES or path.is_symlink():
        return False
    return path.is_file()

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="output ZIP path (outside the source tree)")
    args = parser.parse_args()
    output = args.output.resolve()
    if output == ROOT or ROOT in output.parents:
        parser.error("output ZIP must be outside the source tree")
    files = sorted((p for p in ROOT.rglob("*") if included(p)),
                   key=lambda p: p.relative_to(ROOT).as_posix())
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED,
                         compresslevel=9) as archive:
        for path in files:
            name = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED,
                             compresslevel=9)
    with zipfile.ZipFile(output) as archive:
        bad = archive.testzip()
        if bad:
            raise SystemExit(f"Archive integrity failure: {bad}")
    print(f"PASS: packaged {len(files)} files -> {output} ({output.stat().st_size} bytes)")
    print(f"SHA256 {hashlib.sha256(output.read_bytes()).hexdigest()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
