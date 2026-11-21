"""Apply already reviewed exact shared-bibliography guards and retain their receipt."""
import argparse,datetime,hashlib,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('guards',type=Path);p.add_argument('--receipt',type=Path,required=True);a=p.parse_args()
r=Path(__file__).resolve().parents[1];b=r/'S6_SERIES_PUBLISH_references.bib';before=b.read_text();text=before
data=json.loads(a.guards.read_text())
for g in data.get('changes',data.get('guards',[])):
 assert text.count(g['old'])==g.get('count',g.get('expected_count',1)),g.get('id')
 text=text.replace(g['old'],g['new'])
b.write_text(text)
sha=lambda s:hashlib.sha256(s).hexdigest()
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guard_file':str(a.guards),'guard_sha256':sha(a.guards.read_bytes()),'before_sha256':sha(before.encode()),'after_sha256':sha(text.encode()),'changes':data.get('changes',data.get('guards',[])),'math_check_events_added':0}
a.receipt.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'changes':len(receipt['changes']),'bibliography_sha256':receipt['after_sha256']}))
