"""Retain the preceding master PDF/log before the checkpoint13 rebuild."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil

root=Path(__file__).resolve().parents[1]
dest=root/'records/checkpoint13_prior_master46'
dest.mkdir(exist_ok=True)
names=['S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log']
record={'utc':datetime.now(timezone.utc).isoformat(),'master_build':46,
        'reason':'Preserve the actual previous master and layout log before adding the four newly audited proofs. All prior review records and rendered pages remain at their original paths.',
        'files':{}}
for name in names:
    source=root/name
    target=dest/name
    assert not target.exists(),target
    shutil.copy2(source,target)
    record['files'][name]={'bytes':source.stat().st_size,'sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
assert record['files']['S6_06_BLIND_paper.pdf']['sha256']=='5c21b266929ea470a0c6af977ad05a5bd8264ead00dd299d5f117012229f57ef'
(dest/'preservation.json').write_text(json.dumps(record,indent=2)+'\n')
print('Preserved master46 PDF and final log; no archive was created.')
