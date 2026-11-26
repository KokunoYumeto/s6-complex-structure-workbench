"""Retrieve two exact pinned source files after the four Milnor target freezes."""
from pathlib import Path
import datetime,hashlib,json,urllib.request
R=Path(__file__).resolve().parents[1]
t=json.loads((R/'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_pinned_program_tree.json').read_text())
commit='83d76022bcd442278b760db9ff438afceed6c6ea';assert t['sha']==commit
entries={x['path']:x for x in t['tree']}
o=R/'records/S6_SERIES_PUBLISH_II_Milnor_programs_01';assert not o.exists();o.mkdir()
rows=[]
for name in ['milnor_intersection.py','binomial_milnor.py']:
 path='pro_returns/S6_06_BLIND_checkpoint_15_20261117T1457Z/S6_06_BLIND/code/part4/'+name
 expected=entries[path]
 url=f'https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/{commit}/{path}'
 with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'S6-publication-primary-source-check'}),timeout=45) as response:
  body=response.read();status=response.status
 assert status==200 and len(body)==expected['size']
 blob=hashlib.sha1(b'blob '+str(len(body)).encode()+b'\0'+body).hexdigest();assert blob==expected['sha']
 (o/name).write_bytes(body)
 rows.append(dict(name=name,url=url,http_status=status,bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),git_blob_sha1=blob,pinned_tree_exact_blob_match=True,local_path=str((o/name).relative_to(R))))
record=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),commit=commit,programs=rows,scope='Root will inspect the complete source before assigning any checker exposure.',check_events_added=0)
(o/'receipt.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
