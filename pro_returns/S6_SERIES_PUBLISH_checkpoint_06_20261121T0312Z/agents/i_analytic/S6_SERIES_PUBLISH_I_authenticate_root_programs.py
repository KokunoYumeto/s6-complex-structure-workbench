"""Authenticate requested root-scope code; no historical program execution."""
from pathlib import Path
import json,hashlib,datetime,urllib.request,concurrent.futures
B=Path(__file__).parent
commit='83d76022bcd442278b760db9ff438afceed6c6ea'
base='https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/'+commit+'/'
cp10='pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/'
cp15='pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/code/I/'
manifest={}
for line in Path('/workspace/scratch/653608133b22/source/S6_SERIES_GRIND_filelist.tsv').read_text().splitlines():
 a=line.split('\t')
 if len(a)==3 and a[1].isdigit():manifest[a[0]]=(int(a[1]),a[2])
names=['priority_rows_exact.py','adjacent_exact.py','main_D_double_complex.py']
paths=['code/current_audits/audit_paper_i/code/'+x for x in names]
paths+=['code/current_audits/audit_paper_i/open_atlas/'+x for x in ['exact_regular_atlas.py','cusp_and_finite_exact.py','finite_collar_jet_verifier.py']]
jobs=[{'path':cp10+p,'manifest_key':p,'expected_size':manifest[p][0],'expected_sha256':manifest[p][1]} for p in paths]
tree=json.loads((B/'S6_SERIES_PUBLISH_I_program_tree_receipt.json').read_text())['tree']['tree']
x=next(x for x in tree if x['path']=='replay_invariants/d_koszul.py')
jobs.append({'path':cp15+x['path'],'expected_size':x['size'],'expected_git_blob_sha1':x['sha']})

def get(url):
 with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'S6-Series-publication-source-check'}),timeout=45) as r:
  return r.status,r.read()
def fetch(j):
 status,data=get(base+j['path']);sha=hashlib.sha256(data).hexdigest()
 gitsha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 assert len(data)==j['expected_size'],j
 if 'expected_sha256' in j:assert sha==j['expected_sha256'],j
 if 'expected_git_blob_sha1' in j:assert gitsha==j['expected_git_blob_sha1'],j
 local=B/'programs'/('S6_SERIES_PUBLISH_I_root_primary_'+Path(j['path']).name);local.write_bytes(data)
 return dict(j,url=base+j['path'],http_status=status,bytes=len(data),sha256=sha,git_blob_sha1=gitsha,local_path=str(local.resolve()),executed=False)
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:rows=list(ex.map(fetch,jobs))
receipt={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':commit,'programs':rows,'executed':False}
(B/'S6_SERIES_PUBLISH_I_root_program_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
url='https://api.github.com/repos/KokunoYumeto/s6-complex-structure-workbench/git/trees/'+commit+'?recursive=1'
status,data=get(url);j=json.loads(data);wanted={'d_division_polynomials.py','b_families.py','b_topology.py'}
matches=[x for x in j.get('tree',[]) if Path(x['path']).name in wanted]
inventory={'url':url,'http_status':status,'response_sha256':hashlib.sha256(data).hexdigest(),'truncated':j.get('truncated'),'matches':matches,'root_tree_sha':j.get('sha')}
(B/'S6_SERIES_PUBLISH_I_root_program_search_receipt.json').write_text(json.dumps(inventory,indent=2)+'\n')
assert {Path(x['path']).name for x in matches}==wanted
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 rows+=list(ex.map(fetch,[{'path':x['path'],'expected_size':x['size'],'expected_git_blob_sha1':x['sha']} for x in matches]))
receipt['programs']=rows
receipt['old_source_path_receipt']='S6_SERIES_PUBLISH_I_root_program_search_receipt.json'
receipt['search_limit']='The root recursive tree is truncated, but all three requested legacy paths occur in its returned primary entries and their raw bytes match those Git blob hashes. No claim of complete repository enumeration.'
(B/'S6_SERIES_PUBLISH_I_root_program_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'verified':len(rows),'all_http200':all(x['http_status']==200 for x in rows),'legacy_path_matches':matches,'tree_truncated':j.get('truncated'),'executed':False},indent=2))
