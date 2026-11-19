"""Independently extract and execute the complete standalone checkpoint25."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
archive = BASE/'S6_06_BLIND_checkpoint_25.zip'
expected = json.loads((BASE/'checkpoint25_encoding/checkpoint25_creation.json').read_text())
with archive.open('rb') as source:
    sha = hashlib.file_digest(source, 'sha256').hexdigest()
assert sha == expected['sha256']
dest = BASE/'checkpoint25_verify'
dest.mkdir(exist_ok=True)
with zipfile.ZipFile(archive) as z:
    for member in z.infolist():
        p = Path(member.filename)
        assert not p.is_absolute() and '..' not in p.parts
    z.extractall(dest)
subprocess.run([sys.executable, str(dest/'restore_checkpoint.py')], cwd=dest, check=True)
manifest = json.loads((dest/'checkpoint25_transport_manifest.json').read_text())
assert len(manifest['files']) == expected['snapshot_files']
rec = {'status': 'PASS', 'archive': str(archive), 'bytes': archive.stat().st_size,
       'sha256': sha, 'restored_and_verified_files': len(manifest['files']),
       'verification': 'Extracted the standalone ZIP and ran its delivered standard-library restorer; every frozen size and SHA256 and every retained predecessor content object passed.',
       'archive_unchanged': True}
(ROOT/'records/checkpoint25_verification.json').write_text(json.dumps(rec, indent=2)+'\n')
print(json.dumps(rec, indent=2), flush=True)
