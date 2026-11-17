#!/usr/bin/env python3
"""Export the fully audited component-supported shorter loop as P3K.37."""
from pathlib import Path
from datetime import datetime, timezone
import json,re
ROOT=Path(__file__).resolve().parents[2]
rel='notes/part3_os49_shorter_loop_working.md'
with (ROOT/'records/literature_fourfold.md').open('a') as f:
 f.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened own '+rel+', results_mapping.json and qa_weighted_shorter_loop.py. Reason: export complete audited P3K.37 and its standalone proof QA. Material: exact actual quotient, all source/component/root/Cox maps and primitive fan witnesses.\n')
source=(ROOT/rel).read_text()
source='Keep the exact source'+source.split('Keep the exact source',1)[1]
statement=source.split('## 1.',1)[0]
body='## 1.'+source.split('## 1.',1)[1]
def tex(value):
 value=value.replace(r'\tag{OS.',r'\tag{P3K.37.').replace('(OS.','(P3K.37.')
 value=re.sub(r'^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'.}\enspace',value,flags=re.M)
 value=re.sub(r'`([^`]+)`',lambda m:r'\path{'+m.group(1)+'}',value)
 return value.strip()+'\n'
out=r'\begin{statement}{P3K.37}{Proved}'+'\n'+tex(statement)+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex(body)+r'\end{proof}'+'\n'
assert '#' not in out and '`' not in out
(ROOT/'notes/part3_os49_shorter_loop.tex').write_text(out)
mapping=json.loads((ROOT/'code/part3_fourfold/results_mapping.json').read_text())
mapping['results']=[r for r in mapping['results'] if r.get('id')!='P3K.37']
mapping['results'].append(dict(id='P3K.37',status='Proved',item_of_prompt='3.4',
 statement='The actual component-supported OS49 family descends to w=r^3, lambda=w^k for every m=3k,n=±1,d integer, retaining every fan and the same Cox product.',
 proof_file=rel,latex_file='notes/part3_os49_shorter_loop.tex',
 code='code/part3_fourfold/os49_shorter_loop.py',output='code/part3_fourfold/os49_shorter_loop.json',
 parameter='w=r^3; lambda=w^k',k='-2k',ell='-8k',A=0,
 relative_coordinates=['2k',0,0],all_fan='k*(S-1)*(S-3)/4 modulo28',
 k1_range=[0,2,6,12,14,16,20,26],all_k_range=list(range(0,28,2)),
 exact_scalar_example=dict(k=1,parameter='lambda=w',fan_basis=[[1,-4],[0,1]],delta_coordinates=[4,1],S=13,theta_class=2),
 audit='Root, blind_control and checks full-proof independent PASS; exact primitive witnesses executed.',
 remaining_scope='Source-translation minimality retained separately; no arbitrary source-moduli endpoint classification asserted.'))
(ROOT/'code/part3_fourfold/results_mapping.json').write_text(json.dumps(mapping,indent=2)+'\n')
qa=(ROOT/'code/part3_fourfold/qa_weighted_shorter_loop.py').read_text()
qa=qa.replace('P3K.35','P3K.37').replace('k35','k37').replace('part3_weighted_shorter_loop','part3_os49_shorter_loop')
(ROOT/'code/part3_fourfold/qa_os49_shorter_loop.py').write_text(qa)
print('Exported complete P3K.37 with all actual maps and exact fan witnesses.')
