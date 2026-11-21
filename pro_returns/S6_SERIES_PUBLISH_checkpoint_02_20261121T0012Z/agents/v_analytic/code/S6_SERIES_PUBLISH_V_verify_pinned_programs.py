"""Verify the original pinned public computational sources byte for byte."""
from pathlib import Path
import csv,hashlib,json,urllib.request,concurrent.futures

base=Path(__file__).resolve().parent.parent
workspace=base.parents[2]
root=workspace/'source/S6_PUBLISH_programs'
commit='83d76022bcd442278b760db9ff438afceed6c6ea'
prefix='pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/'
repo='KokunoYumeto/s6-complex-structure-workbench'
specs=[
 ('code/paper_v/fresh_frobenius.py','night:P1.16, night:P1.18','Root connection derivation, normalized intertwiner, three endpoint height enclosures; exact intertwiner existence is an input from night:P1.15','proof certificate'),
 ('code/paper_v/fresh_local_domains.py','night:P1.18','Four central Hessian squares and the complete inner cusp determinant inequality','proof certificate'),
 ('code/paper_v/fresh_global_cover.py','night:P1.18','Complete four-region outer cover; calls the endpoint and local programs','proof certificate'),
 ('code/paper_v/verify_saved_certificate.py','night:P1.18','Finite verification of complete saved cover, exclusions, strict bounds and local signs','certificate verifier'),
 ('code/current_audits/audit_corrections/code/independent_V_connection_spectra_06.py','night:P1.1, night:P1.15','Exact connection, root spectra and rank-six matrix calculations','exact check'),
 ('code/current_audits/audit_corrections/code/independent_V_markings_06.py','night:P1.2, night:P1.4, night:P1.7, night:P1.8, night:P1.17','Integral quotient/marking, companion wedge/cusp identities and antiholomorphic anti-intertwiner/fan obstruction','exact check'),
 ('code/current_audits/audit_corrections/code/independent_V_extension_06.py','night:P1.3, night:P1.15, night:P1A.4','Root regularity, extension rows, gauge coboundary, residue normalization, scalar centralizer and finite-cap H1','exact check'),
 ('code/current_audits/audit_corrections/code/independent_V_analytic_06.py','night:P1.9, night:P1A.1, night:P1A.2, night:P1A.3, night:P1A.4, night:P1A.5, night:P1A.6','Kuhn dual complex, root-line cohomology, residue/deformation matrices, translation quotient, Cayley and Riemann-Roch substitutions','exact check'),
 ('code/current_audits/audit_paper_i/closure_07/period_loop_comparison.py','night:P1.16','Independent Fuchsian loop/regular-root numerical comparison retained in the check record','record comparison'),
 ('code/current_audits/audit_paper_i/closure_07/validate_saved_period_comparison.py','night:P1.16','Finite verification of the saved Fuchsian/root comparison outputs','record comparison verifier'),
]
manifest={}
with (workspace/'source/S6_SERIES_GRIND_filelist.tsv').open() as f:
 for row in csv.reader(f,delimiter='\t'):
  if len(row)>=3:manifest[row[0]]={'bytes':row[1],'sha256':row[2]}

def fetch(spec):
 path,ids,scope,kind=spec
 url=f'https://raw.githubusercontent.com/{repo}/{commit}/{prefix}{path}'
 local=(root/path).read_bytes()
 local_hash=hashlib.sha256(local).hexdigest()
 rec=dict(path=path,statement_ids=ids,scope=scope,kind=kind,commit=commit,
  url=f'https://github.com/{repo}/blob/{commit}/{prefix}{path}',
  raw_url=url,local_bytes=len(local),local_sha256=local_hash,
  manifest=manifest.get(path))
 try:
  with urllib.request.urlopen(url,timeout=45) as r:
   remote=r.read();rec['http_status']=r.status
  rec['remote_bytes']=len(remote);rec['remote_sha256']=hashlib.sha256(remote).hexdigest()
  rec['remote_matches_attached']=remote==local
  rec['manifest_matches_attached']=manifest[path]['sha256']==local_hash
 except Exception as e:
  rec['error']=str(e)
 return rec
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 rows=list(ex.map(fetch,specs))
out=base/'S6_SERIES_PUBLISH_V_pinned_program_receipt.json'
out.write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:
 print(r['path'],r.get('http_status'),r.get('remote_matches_attached'),r.get('manifest_matches_attached'),r.get('error',''))
assert all(r.get('remote_matches_attached') and r.get('manifest_matches_attached') for r in rows)
