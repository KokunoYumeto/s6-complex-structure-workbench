#!/usr/bin/env python3
"""Build and check the one final ZIP, retaining all authored audit evidence.

The original attachments and newly fetched third-party full texts are outside
this directory. Intermediate duplicate PDFs and local TeX generated runtime
files are omitted under the exclusion ledger in the main report. Build logs,
all final page renders and contact sheets, and the revised-source fragments
are included. The manifest covers every included file except itself.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT.parent/'Q03_DEPOSIT.zip'
MANIFEST = ROOT/'Q03_DEPOSIT_manifest.sha256'
OUTPUT = ROOT/'code/package_final_output.json'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def omitted(path):
    rel = path.relative_to(ROOT).as_posix()
    if path == MANIFEST or path == OUTPUT:
        return True
    if '__pycache__' in path.parts or path.suffix == '.pyc':
        return True
    if rel.startswith('work/tex_runtime/') and path.suffix not in ('.txt','.log'):
        return True
    if rel.startswith('work/') and path.suffix == '.pdf':
        return True
    return False

def main():
    gate = json.loads((ROOT/'code/final_validation.json').read_text())
    assert gate['verdict'] == 'PASS'
    files = sorted(p for p in ROOT.rglob('*') if p.is_file() and not omitted(p))
    skipped = sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
                     if p.is_file() and omitted(p) and p not in [MANIFEST,OUTPUT])
    OUTPUT.write_text(json.dumps({
        'archive':DEST.name,'created_UTC':datetime.now(timezone.utc).isoformat(),
        'member_count':len(files)+2,
        'manifest':'Q03_DEPOSIT_manifest.sha256',
        'retained':'All authored deliverables, scripts, outputs, logs, audit drafts and final visual-review evidence.',
        'excluded_workspace_files':skipped,
        'external_source_exclusions':'code/E_source_excluded_manifest.json',
        'archive_validation':'The program verifies CRCs and every manifest hash after writing the archive; success is required before returning.'
    },indent=2))
    files.append(OUTPUT)
    files.sort()
    expected={p.relative_to(ROOT).as_posix():sha(p.read_bytes()) for p in files}
    MANIFEST.write_text(''.join(f'{digest}  {name}\n' for name,digest in sorted(expected.items())))
    files.append(MANIFEST)
    files.sort()
    with zipfile.ZipFile(DEST,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for path in files:
            archive.write(path,path.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(DEST) as archive:
        assert archive.testzip() is None
        assert len(archive.namelist()) == len(files)
        assert len(set(archive.namelist())) == len(files)
        for name,digest in expected.items():
            assert sha(archive.read(name)) == digest, name
        assert all(not n.startswith('/') and '..' not in Path(n).parts for n in archive.namelist())
    print(json.dumps({'archive':str(DEST),'bytes':DEST.stat().st_size,
                      'members':len(files),'sha256':sha(DEST.read_bytes()),
                      'CRC_and_all_manifest_hashes':'PASS'},indent=2))

if __name__ == '__main__':
    main()
