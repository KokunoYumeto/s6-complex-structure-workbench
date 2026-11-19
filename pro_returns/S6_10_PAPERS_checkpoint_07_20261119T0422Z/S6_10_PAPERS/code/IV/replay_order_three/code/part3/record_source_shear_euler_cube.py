#!/usr/bin/env python3
"""Record the completed mathematical and direct visual checks of K66."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
R=Path(__file__).resolve().parents[2]
def sha(name):return hashlib.sha256((R/name).read_bytes()).hexdigest()
def save(name,obj):
 p=R/name
 tmp=p.with_name(p.name+'.tmp')
 tmp.write_text(json.dumps(obj,indent=2)+'\n')
 tmp.replace(p)
utc=datetime.now(timezone.utc).isoformat()
tex='notes/part3_source_shear_euler_cube.tex'
pdf='code/part3/k66_standalone.pdf'
cert='code/part3/source_shear_euler_cube.json'
log=(R/'code/part3/k66_standalone.log').read_text()
assert 'Output written on k66_standalone.pdf (6 pages' in log
assert not re.search(r'Overfull|Undefined control|undefined|Missing character',log)
reviewed=json.loads((R/'code/part3/k66_reviewed_render_hashes.json').read_text())
current={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
         for p in (R/'records/render_k66_standalone').glob('page-*.png')}
assert reviewed==current and len(current)==6
qa={
 'utc':utc,'reviewer':'checks','status':'PASS','statement':'P3K.66',
 'pdf':pdf,'page_count':6,'full_size_pages':list(range(1,7)),
 'render_dir':'records/render_k66_standalone',
 'findings':[
  'All six standalone pages directly inspected in full size.',
  'Final second-pass render is pixel-identical to the six directly reviewed images.',
  'No clipping, collisions, missing symbols or malformed equations observed.',
  'The Cech frame convention, literal section-disc arrow, full boundary matrix dictionary, inverse-line signs and oriented cubic formulas render correctly.'
 ],
 'log_scan':{'overfull_boxes':0,'undefined':0,'missing_characters':0},
 'sha256':{p:sha(p) for p in [tex,pdf,cert]},
 'render_sha256':current
}
save('records/k66_standalone_visual_qa.json',qa)
entry={
 'utc':utc,'id':'P3K.66','status':'Proved','item_of_prompt':'3.4',
 'statement':'Exact integer Euler cube, Pontryagin pairing and Jin index on every selected-cusp source-loop physical-vertical-edge shear fan.',
 'own_values':{
  'fan':'T_n=T(e1+n e2,e2), n any integer',
  'k':'6-18*n*(n-1)','ell':0,'A_integer':'1-3*n*(n-1)',
  'native_fixed_pair':'(0,-6+18*n*(n-1))',
  'ordinary_V00':'-18*n*(n-1)',
  'ordinary_delta0':'-12+18*n*(n-1)'
 },
 'latex_file':tex,
 'proof':'notes/part3_source_shear_euler_cube_working.md',
 'certificate':cert,'certificate_checks':41,
 'audit':[
  'Root full EC.1--5 audit PASS communicated on 17 November 2026; exact Cech convention added as requested.',
  'records/blind_audit_source_shear_euler_cube.json'
 ],
 'visual_qa':'records/k66_standalone_visual_qa.json',
 'scope_limit':'Fixed actual source/scalar/finite caps and physical-vertical-edge shear line. No separate nonvertical-fan integer is assigned by this statement.',
 'earlier_proof_clarification':'code/part3/attempts/k63_inverse_line_convention/clarification.json'
}
save('code/part3/source_shear_euler_cube_mapping.json',entry)
mp=R/'code/part3/results_mapping.json'
mapping=json.loads(mp.read_text())
key='additional_source_loop_results'
mapping[key]=[x for x in mapping.get(key,[]) if x.get('id')!='P3K.66']
mapping[key].append(entry)
for x in mapping[key]:
 if x.get('id')=='P3K.63':
  x['connection_sign_clarification']='code/part3/attempts/k63_inverse_line_convention/clarification.json'
  x['integer_refinement']='P3K.66'
save('code/part3/results_mapping.json',mapping)
print('Recorded P3K.66, complete six-page visual QA, and the precise owned mapping.')
print('TeX SHA256',sha(tex))
print('PDF SHA256',sha(pdf))
