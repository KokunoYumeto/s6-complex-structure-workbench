#!/usr/bin/env python3
"""Finalize reviewed K12--15 scope statements, exporter, and status map."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[2]
log = root / 'records/literature_fourfold.md'
paths = ['notes/part3_log_caps.md', 'notes/part3_vertical_scope.md',
         'code/part3_fourfold/export_trace_tex.py',
         'code/part3_fourfold/results_mapping.json']
with log.open('a') as f:
    for name in paths + ['notes/part3_fourfold.md']:
        f.write('\n- ' + datetime.now(timezone.utc).isoformat()
                + ' — Opened current-team file `' + name
                + '`; reason: finalize independently audited K12–15 and compare the graph-line proof; '
                  'material: exact local morphisms, scope, exporter and result statuses.\n')

p = root / paths[0]
s = p.read_text()
s = s.replace('action.  For a cyclic affine log cap written on a smooth root\nsource as a linearized line quotient,',
              'action.  For a cyclic affine log cap at a nonzero-linearization\nsite, written on a smooth root source as a linearized line quotient,')
s = s.replace('linearized root line and affine action.  For any proposed broader',
              'linearized root line and affine action at a nonzero-linearization\nsite.  Scalar-zero Mumford fillings are treated separately.  For any proposed broader')
p.write_text(s)

p = root / paths[1]
s = p.read_text()
start = s.index('## Remaining scope after these reductions')
s = s[:start] + '''## Remaining scope after these reductions

P3K.15 below transports the component cycles, the line, and its integer
delta character through a supplied affine cap on an actual extending
root line.  Applying it to a proposed new cap still requires constructing
that root source, its line, and the complete cyclic affine norm.  Partial
roots may leave a reduced reducible fibre, and zero-gamma finite kernels
must be retained.  Thus neither the retained-neighbourhood obstruction
nor the cap comparison alone is a complete enumeration of the literal
arbitrary-site scope.
'''
p.write_text(s)

p = root / paths[2]
s = p.read_text()
s = s.replace("source+='\\n'+vertical\n", "source+='\\n'+vertical\nsource+='\\n'+(root/'notes/part3_log_caps.md').read_text().replace('# P3K.15.','## P3K.15.',1)\n")
s = s.replace('[1-9]|1[0-4]', '[1-9]|1[0-5]').replace('assert len(parts)==43', 'assert len(parts)==46')
s = s.replace("    else:\n        statement,proof=body.split('**Proof.**',1)",
              "    elif ident=='P3K.15':\n        marker='**Proof: semifreeness from the actual fixed sphere.**'\n        statement,proof=body.split(marker,1)\n        proof,after=proof.split('**End of proof.**',1)\n        proof=marker+proof\n    else:\n        statement,proof=body.split('**Proof.**',1)")
s = s.replace('Exported P3K.1--14', 'Exported P3K.1--15')
p.write_text(s)

p = root / paths[3]
data = json.loads(p.read_text())
new = [
    dict(id='P3K.12', status='Proved', item_of_prompt='3.4',
         statement='A smooth descended scalar-zero filling over a potentially good fibre has an elliptic circle-fixed component and cannot be a six-sphere.',
         proof_file='notes/part3_vertical_scope.md',
         exact_comparison='Faithful root-base character, linearized stabilizer invariant ring, smooth quotient criterion, and actual elliptic double-curve quotient.',
         citations=['Satriano2012 Corollary 1.8 and Proposition 2.2', 'Floyd1952 Theorem 4.4'],
         scope='The scalar-zero potential-good local construction; no exclusion of distant nonzero-linearization log caps.'),
    dict(id='P3K.13', status='Proved', item_of_prompt='3.4',
         statement='The actual orbit of a retained contracting line quotient is the marked source mapping torus. Its compact component cycles force a transitive component permutation when H2 of the global orbit vanishes.',
         proof_file='notes/part3_vertical_scope.md',
         own_value='For an I_n fibre and translation component c, gcd(n,c)=1 is necessary.',
         code='code/part3_fourfold/vertical_scope.py',
         certificate='code/part3_fourfold/vertical_scope.json'),
    dict(id='P3K.14', status='Proved', item_of_prompt='3.4',
         statement='The whole-fibre Hom degree is ab*h(G), independent of the vertical line divisor. At a transitive retained I_n fibre the line has multidegree zero and its vertical ambiguity is an integral whole-fibre divisor.',
         proof_file='notes/part3_vertical_scope.md',
         own_value='For the explicitly marked source-table generator components, n divides a; the annular comparison is multiplication by t^j.',
         source_markings='P3F.2: I8 3/5, I7 2/5, OS55 I5 2/3, OS56 I5 1/4, I4 1/3, I3 1/2, I2 1.',
         code='code/part3_fourfold/vertical_scope.py'),
    dict(id='P3K.15', status='Proved', item_of_prompt='3.4',
         statement='A standard fixed S2 with circle weights (-1,+1) forces global semifreeness. Every supplied nonzero-linearization affine root-line cap has the exact finite-kernel/source-mapping-torus comparison with its actual circle line.',
         proof_file='notes/part3_log_caps.md',
         exact_group='AB=BA, A^m=B^n from the full cyclic norm; C=A^(m/g)B^(-n/g), H=A^rB^s, A=C^s H^(n/g), B=C^(-r)H^(m/g).',
         own_value='The smooth finite source quotient carries the descended line; H2(Y)=0 forces component transitivity, multidegree zero, and vertical rigidity modulo the primitive fibre and its recorded delta character.',
         code='code/part3_fourfold/finite_cap_group.py',
         certificate='code/part3_fourfold/finite_cap_group.json',
         scope='Requires the actual extending root source, line, and affine action; it does not enumerate or supply every proposed cap.')
]
data['results'] = [r for r in data['results'] if r['id'] not in {r['id'] for r in new}] + new
p.write_text(json.dumps(data, indent=2) + '\n')
print('Finalized K12--15 scope, exporter, and result mappings.')
