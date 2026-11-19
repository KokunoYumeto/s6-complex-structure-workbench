"""Retain the immutable twelfth archive and its successful publication receipt."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,zipfile

root=Path(__file__).resolve().parents[1]
created=json.loads((root.parent/'checkpoint12_create.out').read_text())
uploaded=json.loads((root.parent/'checkpoint12_upload.out').read_text())['results'][0]
assert uploaded['status']=='succeeded'
p=Path(uploaded['local_path'])
assert p.name=='S6_06_BLIND_checkpoint_12.zip'
digest=hashlib.sha256(p.read_bytes()).hexdigest()
assert digest==created['sha256']
assert p.stat().st_size==created['bytes']
with zipfile.ZipFile(p) as z:
    entries=len(z.infolist())
assert 'Done testing' in (root/'records/checkpoint12_archive_integrity.out').read_text()
record={
 'recorded_utc':datetime.now(timezone.utc).isoformat(),
 'archive':created,'upload':uploaded,'zip_entries':entries,
 'integrity':'PASS: python3 -m zipfile -t completed with exit0',
 'url':'https://chatgpt.com/library?file_id='+uploaded['library_file_id']+'&account_id=personal',
 'scope':'Checkpoint12 is immutable; this post-publication receipt is retained for checkpoint13.'
}
(root/'records/checkpoint12_publication.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
