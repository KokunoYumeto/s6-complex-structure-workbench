"""Resolve explicit reviewed-config input paths to their exact current hashes."""
from pathlib import Path
import hashlib,json,sys
R=Path(__file__).resolve().parents[1]
def bound(p):
    actual=dict(path=p if isinstance(p,str) else p['path'])
    actual['sha256']=hashlib.sha256((R/actual['path']).read_bytes()).hexdigest()
    if isinstance(p,dict):assert actual==p
    return actual
c=json.loads((R/sys.argv[1]).read_text())
for k in ['prior_admission','proposal','event_proposal','root_review']:c[k]=bound(c[k])
c['source_applications']=[bound(p) for p in c['source_applications']]
assert bound('CHECK_EVENTS.tsv')['sha256']==c['before_ledger_sha256']
assert bound('S6_SERIES_PUBLISH_II.tex')['sha256']==c['source_sha256']
p=R/sys.argv[2];assert not p.exists();p.write_text(json.dumps(c,indent=2)+'\n')
print(json.dumps(bound(str(p.relative_to(R)))))
