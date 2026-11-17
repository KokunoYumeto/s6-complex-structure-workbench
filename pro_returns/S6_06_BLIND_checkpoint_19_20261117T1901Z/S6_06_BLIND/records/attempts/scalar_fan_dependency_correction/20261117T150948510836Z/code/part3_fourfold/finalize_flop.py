#!/usr/bin/env python3
"""Promote the independently audited real flop comparison and export K17."""
from pathlib import Path
from datetime import datetime,timezone
import json
root=Path(__file__).resolve().parents[2]
src=root/'notes/part3_flop_cobordism.md'
history=root/'code/part3_fourfold/history'
history.mkdir(exist_ok=True)
history.joinpath('part3_flop_cobordism_audit.md').write_text(src.read_text())
with (root/'records/literature_fourfold.md').open('a') as f:
 for name in ['notes/part3_flop_cobordism.md','code/part3_fourfold/cox_flop.py',
              'code/part3_fourfold/export_trace_tex.py','code/part3_fourfold/results_mapping.json']:
  f.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened current-team `'+name+'`; reason: record root and blind-control audit acceptance and export K17; material: exact Cox quotient, charged cap, family gauge and oriented characteristic comparison.\n')
s=src.read_text()
start=s.index('## 1. The real master space')
s='''# P3K.17. Proved: the actual Cox flop comparison with its two charged caps

The negative- and positive-diagonal OS49 families have equal
actual return index for every cap order \\(m=3k\\),
\\(k>0\\), every signed primitive twist \\(n=\\pm1\\),
and every additional integral delta twist \\(d\\delta\\).
Their index is zero, their oriented return class is zero, and
their actual mapping tori are products as in P3F.24.
The comparison is an oriented bordism carrying the actual
Euler line; it imposes no spin hypothesis on the comparison
bordism.  The endpoint index structures are the prescribed
ones from the original families.

'''+s[start:]
headings={
 '## 1. The real master space, with its two actual resolution maps':'**Proof: the real master space and its actual resolution maps.**',
 '## 2. Its circle orbit, its line, and the explicit joint cap':'**Proof: the circle orbit, its line, and the explicit joint cap.**',
 '## 3. The actual parameter gauge on the master space':'**Proof: the actual parameter gauge on the master space.**',
 '## 4. The additional normal-sphere boundary in the surgery bordism':'**Proof: the additional normal-sphere boundary in the surgery bordism.**'}
for a,b in headings.items(): s=s.replace(a,b)
s=s.replace('period-origin calculation in P3F.32 gives the primitive',
'''extra twist \\(d\\delta/m\\) contributes only a parameter-independent
scalar to the finite-cap line map.  Its source coordinate is unchanged;
the same scalar extends in the Cox lift and across the joint cap.
It therefore introduces no parameter-crossing line class.  The
period-origin calculation in P3F.32 gives the primitive''')
s=s.replace('Together with P3F.32 this\nwould identify the negative-diagonal return value with zero.',
'''Together with P3F.32 this identifies the negative-diagonal
return index with zero for all the stated orders and twists.
The exact Hopf transfer P3F.22 gives its oriented zero class,
and P3F.24 gives the product mapping torus.''')
end=s.index('## Audit boundary')
s=s[:end]+'''**End of proof.**

## Audit record

The initial draft and its explicit audit boundary are preserved in
`code/part3_fourfold/history/part3_flop_cobordism_audit.md`.
Independent blind-control audit checked the residual semifree weights,
both associated-line signs, the common Cox delta gauge, and the extra
normal-sphere term.  Root audit additionally required and then accepted
the transported truncations and the free period-orbit quotient before
the two-overlap Cech gauge cancellation.  The orientation transport
between the two complex fixed-sphere markings was explicitly retained.
The exact matrix and gauge certificate is `code/part3_fourfold/cox_flop.json`.
This proof treats the two stated OS49 diagonal fans; it does not assign
the same quotient model to every periodic unimodular fan.
'''
src.write_text(s)
p=root/'code/part3_fourfold/cox_flop.py';s=p.read_text()
s=s.replace("proof_draft='P3K.17'","proof='P3K.17'")
s=s.replace("scope='No final return equality is inferred by code; the oriented family and collar proof is in the draft.'",
            "scope='Code certifies exact local matrices and cap maps. P3K.17 proves the oriented family/collar comparison; no spin assumption is imposed on that comparison bordism.'")
p.write_text(s)
p=root/'code/part3_fourfold/export_trace_tex.py';s=p.read_text()
s=s.replace("source+='\\n'+(root/'notes/part3_seifert_scope.md').read_text().replace('# P3K.16.','## P3K.16.',1)\n",
            "source+='\\n'+(root/'notes/part3_seifert_scope.md').read_text().replace('# P3K.16.','## P3K.16.',1)\nsource+='\\n'+(root/'notes/part3_flop_cobordism.md').read_text().replace('# P3K.17.','## P3K.17.',1)\n")
s=s.replace('[1-9]|1[0-6]','[1-9]|1[0-7]').replace('assert len(parts)==49','assert len(parts)==52')
s=s.replace("    else:\n        statement,proof=body.split('**Proof.**',1)",
            "    elif ident=='P3K.17':\n        marker='**Proof: the real master space and its actual resolution maps.**'\n        statement,proof=body.split(marker,1)\n        proof,after=proof.split('**End of proof.**',1)\n        proof=marker+proof\n    else:\n        statement,proof=body.split('**Proof.**',1)")
s=s.replace('Exported P3K.1--16','Exported P3K.1--17')
p.write_text(s)
p=root/'code/part3_fourfold/results_mapping.json';data=json.loads(p.read_text())
data['results']=[r for r in data['results'] if r['id']!='P3K.17']
data['results'].append(dict(id='P3K.17',status='Proved',item_of_prompt='3.4',
 proof_file='notes/part3_flop_cobordism.md',latex_file='notes/part3_fourfold.tex',
 statement='The actual Cox real bordism compares both OS49 diagonal fans, retaining two opposite fixed-sphere base charges and the additional normal-sphere boundary.',
 own_value='For every m=3k>0, n=+1 or -1 and every integer delta twist d: return index A=0, oriented Theta7 class0, product mapping torus.',
 parameter='lambda=r^m; one signed primitive K-turn from the exact period origins.',
 code='code/part3_fourfold/cox_flop.py',certificate='code/part3_fourfold/cox_flop.json',
 exact_morphisms=['Cox moment-level resolution maps','Free transitive period action on square cells','Global physical-delta lift of the parameter gauge','Two actual charged cap line maps','Oriented surgery-collar bordism with its retained sphere-bundle boundary'],
 spin_scope='The comparison uses oriented characteristic bordism with a line; endpoint spin/index structures remain prescribed.',
 fan_scope='The specified positive- and negative-diagonal OS49 fans. General periodic fans are not identified by this statement.',
 audit_history='code/part3_fourfold/history/part3_flop_cobordism_audit.md'))
p.write_text(json.dumps(data,indent=2)+'\n')
print('Promoted and mapped P3K.17; exact audit history retained.')
