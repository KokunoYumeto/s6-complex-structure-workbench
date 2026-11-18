#!/usr/bin/env python3
"""Export the complete two-fan OS49 correction without altering the master."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'notes/part3_os49_corrected_returns_working.md'
now=datetime.now(timezone.utc).isoformat()
with (ROOT/'records/literature_fourfold.md').open('a') as log:
 log.write('\n- '+now+' — Opened '+str(source.relative_to(ROOT))+' and own results_mapping.json. Reason: separate K65 complete manuscript export. Material: actual two-fan source/cap/seam maps, independent positive page, full native trace, signed flop and shorter cyclic endpoint; no arbitrary-fan or negative integer claim.\n')
raw=source.read_text()
status='Proved' if '\n**Proved.**' in raw else 'Audit draft'
statement=raw.split('## Statement\n',1)[1].split('## OR65.1.',1)[0]
body='## OR65.1.'+raw.split('## OR65.1.',1)[1]
def tex(s):
 s=s.replace(r'\tag{OR65.',r'\tag{P3K.65.OR.').replace('(OR65.','(P3K.65.OR.')
 s=s.replace(')--(P3K.65.',')--\\allowbreak (P3K.65.')
 s=re.sub(r'^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'.}\par\nopagebreak[4]',s,flags=re.M)
 s=re.sub(r'`([^`]+)`',lambda m:r'\path{'+m.group(1)+'}',s)
 return s.strip()+'\n'
out='\\begin{statement}{P3K.65}{'+status+'}\n'+tex(statement)+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex(body)+r'\end{proof}'+'\n'
assert not re.search(r'(?<!\\)#',out)
(ROOT/'notes/part3_os49_corrected_returns.tex').write_text(out)
(ROOT/'notes/part3_os49_corrected_returns.md').write_text('# P3K.65. The two actual OS49 fan returns\n\n'+statement+'\n\n**Proof.**\n\n'+body+'\n\n**End of proof.**\n')
mapping_path=ROOT/'code/part3_fourfold/results_mapping.json'
mapping=json.loads(mapping_path.read_text())
mapping['results']=[x for x in mapping['results'] if x.get('id')!='P3K.65']
mapping['results'].append(dict(id='P3K.65',status=status,item_of_prompt='3.4',
 statement='The actual positive OS49 r-loop has negative/positive fan classes (-3k,0); the constructed shorter w-loop has (-k,0), for m=3k, both norm signs and every fixed delta character.',
 proof_file='notes/part3_os49_corrected_returns.md',latex_file='notes/part3_os49_corrected_returns.tex',
 working_proof=str(source.relative_to(ROOT)),source_sha256=hashlib.sha256(raw.encode()).hexdigest(),
 positive_fan_Jin_integer=0,negative_r_class='-3*k mod28',negative_w_class='-k mod28',
 norm_signs=[-1,1],delta_character='every fixed integer d',
 native_r_free_pair=['-3*k','3*k'],native_w_free_pair=['-k','k'],
 scalar_witness={'k':1,'parameter':'lambda=w','negative_fan_class':27},
 realized_shorter_negative_residues=list(range(28)),
 exact_certificate='code/part3_fourfold/os49_corrected_returns.json',
 correction_scope='Replaces the K17 outer-line equality by the actual native C2 flop, retaining the missing determinant winding -2m.',
 remaining_scope='No arbitrary-fan formula or negative-fan integer lift is assigned.'))
mapping_path.write_text(json.dumps(mapping,indent=2)+'\n')
print(json.dumps(dict(id='P3K.65',status=status,source_sha256=hashlib.sha256(raw.encode()).hexdigest(),
 tex_file='notes/part3_os49_corrected_returns.tex'),indent=2))
