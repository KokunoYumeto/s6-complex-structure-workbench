#!/usr/bin/env python3
"""Export the independently audited K16 and its exact scope."""
from pathlib import Path
from datetime import datetime,timezone
import json
root=Path(__file__).resolve().parents[2]
paths=['notes/part3_seifert_scope.md','notes/part3_log_caps.md',
       'code/part3_fourfold/export_trace_tex.py','code/part3_fourfold/results_mapping.json']
with (root/'records/literature_fourfold.md').open('a') as f:
 for name in paths:
  f.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened current-team `'+name+'`; reason: export root-audited K16 and retain its exact fan/cap scope; material: Seifert maps, signed meridians, status records.\n')
p=root/paths[0]
t=p.read_text().replace(',qquad',',\\qquad')
t=t.replace('The scope of this reduction is the actual whole-fibre cusp',
            'The scope of this reduction is the actual whole-fibre cusp')
t += '\nAn arbitrary periodic unimodular fan need not have this fixed-sphere\nmodel.  The present map and its use of P3F.8 are not asserted for\nsuch a fan without its separate orbit comparison.\n'
p.write_text(t)
p=root/paths[2];t=p.read_text()
t=t.replace("source+='\\n'+(root/'notes/part3_log_caps.md').read_text().replace('# P3K.15.','## P3K.15.',1)\n",
            "source+='\\n'+(root/'notes/part3_log_caps.md').read_text().replace('# P3K.15.','## P3K.15.',1)\nsource+='\\n'+(root/'notes/part3_seifert_scope.md').read_text().replace('# P3K.16.','## P3K.16.',1)\n")
t=t.replace('[1-9]|1[0-5]','[1-9]|1[0-6]').replace('assert len(parts)==46','assert len(parts)==49')
t=t.replace("    else:\n        statement,proof=body.split('**Proof.**',1)",
            "    elif ident=='P3K.16':\n        marker='**Proof: construction of the map.**'\n        statement,proof=body.split(marker,1)\n        proof,after=proof.split('**End of proof.**',1)\n        proof=marker+proof\n    else:\n        statement,proof=body.split('**Proof.**',1)")
t=t.replace('Exported P3K.1--15','Exported P3K.1--16')
p.write_text(t)
p=root/paths[3];data=json.loads(p.read_text())
data['results']=[r for r in data['results'] if r['id']!='P3K.16']
data['results'].append(dict(id='P3K.16',status='Proved',item_of_prompt='3.4',
    proof_file='notes/part3_seifert_scope.md',latex_file='notes/part3_fourfold.tex',
    statement='The actual whole-fibre I1 orbit projection with K15 caps has a simply connected Seifert base; at most two effective gamma multiplicities are nontrivial.',
    own_value='m1*m2*b+m2*n1+m1*n2=+1 or -1, with gcd(m1,m2)=1.',
    exact_maps='Root u=z^g, disc mapping torus, path-lifting surjection, explicit reflection representation, signed Heegaard meridian matrix, and A_i -> A_i*B_i^k.',
    code='code/part3_fourfold/seifert_scope.py',certificate='code/part3_fourfold/seifert_scope.json',
    scope='The P3F.9 whole-fibre I1 fixed-sphere orbit model. Arbitrary fans need a separate orbit map. Order-one clutches and finite zero-gamma source/line data remain retained.'))
p.write_text(json.dumps(data,indent=2)+'\n')
print('Finalized and mapped K16; source fan scope retained.')
