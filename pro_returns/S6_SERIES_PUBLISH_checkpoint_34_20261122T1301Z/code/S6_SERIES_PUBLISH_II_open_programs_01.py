"""Open four precisely located historical program sources at the pinned commit."""
from pathlib import Path
import concurrent.futures,datetime,hashlib,json,urllib.request
R=Path(__file__).resolve().parents[1]
COMMIT='83d76022bcd442278b760db9ff438afceed6c6ea'
TREE=R/'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_pinned_program_tree.json'
DIRECTORY='pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/'
names=['D_exact_checks.py','A_vertical_pole.py','A_non_lci_cusp.py','root_unrestricted_euler.py']
tree=json.loads(TREE.read_text());assert tree['sha']==COMMIT
entries={x['path']:x for x in tree['tree']}
out=R/'records/S6_SERIES_PUBLISH_II_opened_programs_01';out.mkdir(exist_ok=True)
def get(name):
 path=DIRECTORY+name;expected=entries[path]
 url=f'https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/{COMMIT}/{path}'
 req=urllib.request.Request(url,headers={'User-Agent':'S6-publication-primary-source-check'})
 with urllib.request.urlopen(req,timeout=45) as response:
  body=response.read();status=response.status
 assert status==200 and len(body)==expected['size']
 blob=hashlib.sha1(b'blob '+str(len(body)).encode()+b'\0'+body).hexdigest()
 assert blob==expected['sha']
 p=out/name;assert not p.exists();p.write_bytes(body)
 return dict(name=name,url=url,http_status=status,bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),git_blob_sha1=blob,
             pinned_tree_exact_blob_match=True,local_path=str(p.relative_to(R)))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(get,names))
receipt=out/'receipt.json';assert not receipt.exists()
receipt.write_text(json.dumps(dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),commit=COMMIT,
 tree_path=str(TREE.relative_to(R)),tree_sha256=hashlib.sha256(TREE.read_bytes()).hexdigest(),
 tree_truncated=tree['truncated'],scope='Only the four positively present exact entries are used; no absence claim is made from the truncated tree.',programs=rows,check_events_added=0),indent=2)+'\n')
print(json.dumps(dict(receipt=str(receipt.relative_to(R)),programs=rows),indent=2))
