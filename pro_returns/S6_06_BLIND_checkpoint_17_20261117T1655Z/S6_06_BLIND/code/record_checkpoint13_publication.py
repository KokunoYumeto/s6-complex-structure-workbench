"""Retain the immutable thirteenth archive and successful publication receipt."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, zipfile

root = Path(__file__).resolve().parents[1]
created = json.loads((root.parent / 'checkpoint13_create.out').read_text())
uploaded = json.loads((root.parent / 'checkpoint13_upload.out').read_text())['results'][0]
assert uploaded['status'] == 'succeeded'
p = Path(uploaded['local_path'])
assert p.name == 'S6_06_BLIND_checkpoint_13.zip'
digest = hashlib.sha256(p.read_bytes()).hexdigest()
assert digest == created['sha256']
assert p.stat().st_size == created['bytes']
with zipfile.ZipFile(p) as z:
    entries = len(z.infolist())
assert 'Done testing' in (root / 'records/checkpoint13_archive_integrity.out').read_text()
record = {
    'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'archive': created, 'upload': uploaded, 'zip_entries': entries,
    'integrity': 'PASS: python3 -m zipfile -t completed with exit0',
    'url': 'https://chatgpt.com/library?file_id=' + uploaded['library_file_id'] + '&account_id=personal',
    'scope': 'Checkpoint13 is immutable; this post-publication receipt is retained for checkpoint14.'
}
(root / 'records/checkpoint13_publication.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'zip_entries': entries, 'url': record['url'],
                  'bytes': created['bytes'], 'sha256': digest}, indent=2))
