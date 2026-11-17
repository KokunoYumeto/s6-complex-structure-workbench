#!/usr/bin/env python3
"""Export independently audited K22, with its complete matrices and scope."""
from pathlib import Path
from datetime import datetime,timezone
import json
root=Path(__file__).resolve().parents[2]
names=['notes/part3_primitive_sources.md','code/part3_fourfold/export_trace_tex.py',
       'code/part3_fourfold/results_mapping.json']
with (root/'records/literature_fourfold.md').open('a') as f:
 for name in names:
  f.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened current-team `'+name+'`; reason: export root-audited K22; material: exact primitive-source matrices, inversion, all orbit/Hopf gluing maps, ten sphere constructions and their signed return indices.\n')
p=root/'code/part3_fourfold/export_trace_tex.py';s=p.read_text()
s=s.replace("source+='\\n'+(root/'notes/part3_source_reduction.md').read_text()\n",
            "source+='\\n'+(root/'notes/part3_source_reduction.md').read_text()\nsource+='\\n'+(root/'notes/part3_primitive_sources.md').read_text()\n")
s=s.replace('2[01]','2[0-2]').replace('assert len(parts)==64','assert len(parts)==67')
s=s.replace("    body=[' & '.join(c.strip() for c in row)+r' \\\\' for row in rows]\n",
            "    def cell(c):\n        c=c.strip()\n        return r'\\('+c.replace('−','-')+r'\\)' if re.fullmatch('[−-][0-9]+',c) else c\n    body=[' & '.join(cell(c) for c in row)+r' \\\\' for row in rows]\n    spec='c p{0.48\\\\textwidth} c c c' if len(rows[0])==5 else 'c l l'\n")
s=s.replace("r'\\begin{center}\\small\\begin{tabular}{c l l}\\hline'",
            "r'\\begin{center}\\small\\begin{tabular}{'+spec+r'}\\hline'")
s=s.replace("    elif ident in {'P3K.20','P3K.21'}:",
            "    elif ident=='P3K.22':\n        marker='**Proof: the source automorphisms and the line lift.**'\n        statement,proof=body.split(marker,1)\n        proof,after=proof.split('**End of proof.**',1)\n        proof=marker+proof\n    elif ident in {'P3K.20','P3K.21'}:")
s=s.replace('Exported P3K.1--21','Exported P3K.1--22')
p.write_text(s)
p=root/'code/part3_fourfold/results_mapping.json';data=json.loads(p.read_text())
data['results']=[r for r in data['results'] if r['id']!='P3K.22']
data['results'].append(dict(id='P3K.22',status='Proved',item_of_prompt='3.4',
 proof_file='notes/part3_primitive_sources.md',latex_file='notes/part3_fourfold.tex',
 statement='Ten primitive-translation source profiles give explicit complex six-sphere families; exact inversion removes the integral boundary linking coefficients and all Mayer–Vietoris maps are exported.',
 own_value={'OS45':{'profiles':2,'A':-3,'Theta7':25},'OS47':{'profiles':3,'A':-6,'Theta7':22},'OS55':{'profiles':2,'A':-9,'Theta7':19},'OS56':{'profiles':3,'A':-14,'Theta7':14}},
 codes=['code/part3_fourfold/primitive_source_translation.py','code/part3_fourfold/primitive_orbit_filling.py'],
 certificates=['code/part3_fourfold/primitive_source_translation.json','code/part3_fourfold/primitive_orbit_filling.json'],
 exact_maps=['extended source inversion and translation','canonical chord line lift','source Wang complex','primitive Thom maps','literal inversion on every boundary torus','all cap exterior-power maps','all orbit and Hopf Mayer–Vietoris matrices','degree-one norm-shell page with original Picard line'],
 additional_obstruction='A primitive smooth cap of multiplicity m contributes (Z/m)^2 to orbit H2 when the H1 Seifert matrix is unimodular; sphere members in this smooth-site scope have only order-one caps.',
 scope='Specified standard vertical-edge fan and one positive gamma cap for the return table; arbitrary order-one smooth-site collars for the topology statement. Singular-source cap replacements and general fan-return changes retain separate comparisons.'))
p.write_text(json.dumps(data,indent=2)+'\n')
print('Finalized root-audited K22 with all ten source profiles and exact construction scope.')
