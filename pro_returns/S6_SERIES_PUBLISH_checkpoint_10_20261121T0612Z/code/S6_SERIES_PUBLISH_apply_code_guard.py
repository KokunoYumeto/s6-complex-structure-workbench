#!/usr/bin/env python3
"""Apply a reviewed exact code guard and bind its before/after bytes."""
from pathlib import Path
import argparse, datetime, hashlib, json

ap=argparse.ArgumentParser()
ap.add_argument('guard',type=Path)
ap.add_argument('--receipt',type=Path,required=True)
a=ap.parse_args()
sha=lambda b:hashlib.sha256(b).hexdigest()
g=json.loads(a.guard.read_text())
p=Path(g['target'])
before=p.read_bytes()
assert sha(before)==g['target_sha256']
text=before.decode()
for x in g['guards']:
    assert text.count(x['old'])==1
    text=text.replace(x['old'],x['new'],1)
compile(text,str(p),'exec')
assert not a.receipt.exists()
p.write_text(text)
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'guard':str(a.guard),'guard_sha256':sha(a.guard.read_bytes()),
         'target':str(p),'before_sha256':sha(before),'after_sha256':sha(p.read_bytes()),
         'changes':g['guards'],'events_added':0}
a.receipt.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'target':str(p),'after_sha256':receipt['after_sha256'],'changes':len(g['guards'])}))
