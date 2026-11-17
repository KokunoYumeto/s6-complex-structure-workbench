#!/usr/bin/env python3
"""Record the analytic check and include the owned TeX without rewriting others."""
from pathlib import Path
from datetime import datetime,timezone
import json
root=Path(__file__).resolve().parents[2]
p=root/'code/part3_fourfold/results_mapping.json'
d=json.loads(p.read_text())
entry={
    'id':'P3K.8','status':'Proved','original_return_index':0,
    'method':'Actual sphere-bundle symbol factorization; explicit marked-cap switch with difference S1 times S3; Dolbeault acyclicity of M+nF.',
    'numerically_independent_of':'No evaluation of page signature, relative M-square, or Pontryagin number.'
}
d['results']=[x for x in d['results'] if x['id']!='P3K.8']+[entry]
p.write_text(json.dumps(d,indent=2)+'\n')
target=root/'notes/part3.tex'
s=target.read_text()
inc=r'\input{notes/part3_fourfold.tex}'
if inc not in s:
    target.write_text(s.rstrip()+'\n\n% Independent local obstruction and complete real-trace return proof.\n'+inc+'\n')
with (root/'records/literature_fourfold.md').open('a') as f:
    f.write('\n## '+datetime.now(timezone.utc).isoformat()+' — real-trace integration\n\n')
    f.write('Read current-team `notes/part3.tex` and selected current `notes/part3_family.md` statements to attach the owned P3K.1–8 proof and verify its preceding labels. Material taken: current P3F.22–23 return/parameter conventions, P3F.6 and P3F.10 page line data, and source A_E,B_E monodromy for the integral vanishing-cycle check. Added only an input of the owned LaTeX file to `notes/part3.tex`; no preceding text was rewritten. The earlier unsuccessful algebraic-corner route remains explicitly historical and is superseded by the actual real trace.\n')
print('P3K.1--8 exported and included once in notes/part3.tex; result mapping updated.')
