"""Authenticate pinned source files; do not execute historical mathematics code."""
from pathlib import Path
import concurrent.futures, datetime, hashlib, json, urllib.request

B=Path(__file__).parent
tree=json.loads((B/'S6_SERIES_PUBLISH_I_program_tree_receipt.json').read_text())['tree']['tree']
by_path={x['path']:x for x in tree if x['type']=='blob'}
commit='83d76022bcd442278b760db9ff438afceed6c6ea'
prefix='pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/code/I/'
groups=[
 ('division','ari:C.4.3;ari:C.4.4;ari:C.5.1;ari:C.8.4','Exact division recurrences and resultants',[
  'replay_special/Cspecial_division.py','replay_special/Cspecial_relations.py']),
 ('cm_models','ari:C.6.3','Rational CM models, local reductions and finite heights',[
  'replay_arithmetic/C_cm_models.gp','replay_arithmetic/C_cm_local_heights.gp']),
 ('cm_heights','ari:C.6.5','Outward interval enclosures for CM heights and singular moduli',[
  'replay_arithmetic/C_cm_height_arb.py']),
 ('ranks','ari:C.6.R1','Exact descent, local rank data and saturation',[
  'replay_arithmetic/C_cm_rank_lvalues.gp','replay_arithmetic/Crank_saturation.cpp']),
 ('derivatives','I:CM-coefficient-series;ari:C.6.R2','Integer coefficient streams, derivative sums and full-real-period enclosures',[
  'replay_arithmetic/Crank_coefficients.gp','replay_arithmetic/Crank_derivatives.cpp',
  'replay_arithmetic/Crank_cm_stream.cpp','certify_all_period_ratios.py']),
 ('coarse_height','ari:C.6.R4','Exact Bezout height bounds, six rational doublings and integer isolation',[
  'replay_arithmetic/C_height_coarse_certificate.py']),
 ('leading_factors','ari:C.6.R5','Genus data, modular symbols, central sums and rational denominator isolation',[
  'replay_arithmetic/B_C6_gz_exact_metadata.gp','replay_arithmetic/B_C6_manin_2.gp',
  'replay_arithmetic/B_C6_manin_4.gp','replay_arithmetic/B_C6_manin_6.gp',
  'replay_arithmetic/B_C6_manin_9.gp','replay_arithmetic/B_C6_manin_10.gp',
  'replay_arithmetic/B_C6_central_stream.cpp','replay_arithmetic/B_C6_exact_factors.py',
  'replay_arithmetic/auxiliary_coefficients.gp']),
 ('torsion','ari:C.6.T1;ari:C.6.T2','Exact local data, torsion and two-isogeny descent over Q(sqrt(3))',[
  'replay_torsion/Crank_torsion_local.gp','replay_torsion/Crank_torsion_final.gp',
  'replay_torsion/Crank_torsion_descent.gp','replay_torsion/Crank_Sage_ell.gp',
  'replay_torsion/Crank_Sage_ellcommon.gp']),
 ('critical','ari:C.8.14','Rational power-series recurrence and Bernstein coefficient inequalities',[
  'replay_arithmetic/Ccritical_rational_certificate.py','replay_arithmetic/Ccritical_scalar.py'])
]
out=B/'programs';out.mkdir(exist_ok=True)
jobs=[]
for group,ids,scope,paths in groups:
 for path in paths:
  assert path in by_path,path
  jobs.append(dict(group=group,statement_ids=ids,mathematical_scope=scope,path=path))
jobs.append(dict(group='cm_witness',statement_ids='ari:C.7.10',
 mathematical_scope='Exact CM endomorphism, kernel polynomial and compact-point witness identities',
 path='code/current_audits/audit_paper_i/arithmetic_06/cm_witness_exact.py',
 alternate_prefix='pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/',
 expected_sha256='436bbf5bde54211ad5f5fc74f1574937f79e500d50713eee446707ef77326ca6',
 expected_size=4979))

def fetch(job):
 x=by_path.get(job['path'])
 full=job.get('alternate_prefix',prefix)+job['path']
 url='https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/'+commit+'/'+full
 req=urllib.request.Request(url,headers={'User-Agent':'S6-Series-publication-source-check'})
 with urllib.request.urlopen(req,timeout=45) as r:
  data=r.read();status=r.status
 gitsha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 if x:
  assert gitsha==x['sha'],(job['path'],gitsha,x['sha'])
  assert len(data)==x['size'],job['path']
 else:
  assert hashlib.sha256(data).hexdigest()==job['expected_sha256'],job['path']
  assert len(data)==job['expected_size'],job['path']
 local=out/('S6_SERIES_PUBLISH_I_primary_'+job['path'].replace('/','__'))
 local.write_bytes(data)
 return dict(**job,repository_path=full,commit=commit,url=url,http_status=status,
  git_blob_sha1=gitsha,expected_git_blob_sha1=x['sha'] if x else None,sha256=hashlib.sha256(data).hexdigest(),
  bytes=len(data),local_path=str(local.resolve()),executed=False,
  verification_basis='Authenticated immutable I tree Git blob/size' if x else 'Attached S6_SERIES_GRIND_filelist.tsv rows740/1829 SHA256/size')

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
 rows=list(ex.map(fetch,jobs))
receipt=dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 method='Primary raw files at the pinned commit: 28 byte sizes/Git blob hashes checked against the authenticated recursive I tree; one current-audit file checked against the attached manifest SHA256/size. Files not executed. No mathematical check credit.',
 tree_receipt=str((B/'S6_SERIES_PUBLISH_I_program_tree_receipt.json').resolve()),programs=rows)
(B/'S6_SERIES_PUBLISH_I_operative_program_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'verified':len(rows),'groups':len(set(x['group'] for x in rows)),'all_http200':all(x['http_status']==200 for x in rows),'executed':False}))
