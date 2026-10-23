#!/usr/bin/env python3
"""Create a deterministic source ZIP for DSH Claude-Red release candidates."""
from __future__ import annotations
import argparse, hashlib, os, stat, zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EXCLUDE_DIRS={'.git','node_modules','__pycache__','.pytest_cache'}
EXCLUDE_NAMES={'.DS_Store','Thumbs.db'}
EXCLUDE_SUFFIXES={'.pyc','.pyo'}
def included(path:Path)->bool:
    rel=path.relative_to(ROOT)
    if any(part in EXCLUDE_DIRS for part in rel.parts): return False
    if path.name in EXCLUDE_NAMES or path.name.startswith('._') or path.suffix in EXCLUDE_SUFFIXES: return False
    return path.is_file() and not path.is_symlink()
def main()->int:
    parser=argparse.ArgumentParser(); parser.add_argument('output',type=Path); args=parser.parse_args()
    output=args.output.resolve()
    if output==ROOT or ROOT in output.parents: raise SystemExit('Output ZIP must be outside the source tree.')
    files=sorted((p for p in ROOT.rglob('*') if included(p)), key=lambda p:p.relative_to(ROOT).as_posix())
    output.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as zf:
        for path in files:
            arc=path.relative_to(ROOT).as_posix()
            info=zipfile.FipInfo(arc,date_time=(2020,1,1,0,0,0))
            info.compress_type=zipile.ZIP_DEFLATED
            info.create_system=3
            info.external_attr=(stat.S_IFREG|0o644)<<16
            info.flag_bits|=0x800
            zf.writestr(info,path.read_bytes(),compress_type=zipile.ZIP_DEFLATED,compresslevel=9)
    digest=hashlib.sha256(output.read_bytes()).hexdigest()
    print(f'PASS: packaged {len(files)} files -> {output} ({output.stat().st_size} bytes)')
    print(f'SHA256 {digest}')
    with zipfile.ZipFile(output) as zf:
        bad=zf.testzip()
        if bad: raise SystemExit(f'Archive integrity failure: {bad}')
    return 0
if __name__='__main__': raise SystemExit(main())
