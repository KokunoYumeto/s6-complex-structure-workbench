"""Retrieve the exact positively indexed E-counterexample source for scoped comparison."""
from pathlib import Path
import datetime, hashlib, json, urllib.request
R=Path(__file__).resolve().parents[1]
T=R/'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_pinned_program_tree.json'
t=json.loads(T.read_text());commit=t['sha']
assert commit=='83d76022bcd442278b760db9ff438afceed6c6ea'
path='pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/E_counterexamples.py'
expected=next(x for x in t['tree'] if x['path']==path)
url=f'https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/{commit}/{path}'
req=urllib.request.Request(url,headers={'User-Agent':'S6-publication-primary-source-check'})
with urllib.request.urlopen(req,timeout=45) as response:
 body=response.read();status=response.status
assert status==200 and len(body)==expected['size']
blob=hashlib.sha1(b'blob '+str(len(body)).encode()+b'\0'+body).hexdigest()
assert blob==expected['sha']
o=R/'records/S6_SERIES_PUBLISH_II_E_counterexamples_01';assert not o.exists();o.mkdir()
(o/'E_counterexamples.py').write_bytes(body)
r=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),url=url,http_status=status,
 commit=commit,git_blob_sha1=blob,sha256=hashlib.sha256(body).hexdigest(),bytes=len(body),
 pinned_tree_exact_blob_match=True,scope='Retrieved by root. Unreleased targets remain closed to their checkers; a separate exact E17 slice will be supplied.',check_events_added=0)
(o/'receipt.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2));print(body.decode())
