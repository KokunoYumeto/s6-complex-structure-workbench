#!/usr/bin/env python3
"""Integrate independently audited K23 and retain its precise fixed-edge scope."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[2]
names = ['notes/part3_fixed_edge_flop.md',
         'code/part3_fourfold/export_trace_tex.py',
         'code/part3_fourfold/results_mapping.json']
with (root/'records/literature_fourfold.md').open('a') as f:
    for name in names:
        f.write('\n- '+datetime.now(timezone.utc).isoformat()+
                ' — Opened current-team '+name+
                '; reason: export independently audited P3K23; material: exact Cox products, actual-family conjugation, integral Gysin coefficient, signed plumbing and fixed-edge return classes.\n')
p = root/'code/part3_fourfold/export_trace_tex.py'
s = p.read_text()
include = "source+='\\n'+(root/'notes/part3_fixed_edge_flop.md').read_text()\n"
if include not in s:
    s = s.replace("source+='\\n'+(root/'notes/part3_primitive_sources.md').read_text()\n",
                  "source+='\\n'+(root/'notes/part3_primitive_sources.md').read_text()\n"+include)
s = s.replace('2[0-2]', '2[0-3]').replace('assert len(parts)==67', 'assert len(parts)==70')
branch = """    elif ident=='P3K.23':
        marker='**Proof: the actual two local products and the parameter clutch.**'
        statement,proof=body.split(marker,1)
        proof,after=proof.split('**End of proof.**',1)
        proof=marker+proof
"""
if "elif ident=='P3K.23':" not in s:
    s = s.replace("    elif ident in {'P3K.20','P3K.21'}:", branch+"    elif ident in {'P3K.20','P3K.21'}:")
s = s.replace('Exported P3K.1--22', 'Exported P3K.1--23')
p.write_text(s)
p = root/'code/part3_fourfold/results_mapping.json'
data = json.loads(p.read_text())
data['results'] = [r for r in data['results'] if r['id'] != 'P3K.23']
data['results'].append({
    'id': 'P3K.23', 'status': 'Proved', 'item_of_prompt': '3.4',
    'proof_file': 'notes/part3_fixed_edge_flop.md',
    'latex_file': 'notes/part3_fourfold.tex',
    'statement': 'The actual toric flop of a semifree fixed (-1,-1) curve changes the oriented return sphere class from A to -5A modulo 28.',
    'own_value': {
        'fixed_edge_formula': '-5*A mod 28',
        'K22_by_height_denominator': {'8': 15, '14': 2, '20': 17, '30': 14},
        'earlier_degree_four_OS47': 20, 'zero_index_examples': 0,
    },
    'codes': ['code/part3_fourfold/fixed_edge_signs.py',
              'code/part3_fourfold/commutator_orientation.py'],
    'certificates': ['code/part3_fourfold/fixed_edge_signs.json',
                     'code/part3_fourfold/commutator_orientation.json'],
    'exact_maps': ['Cox quaternion normal products',
                   'tau(h,q)=(q^-1*h*q,q) and its exterior extension',
                   'parameter-independent Cox intertwiner, including odd loop',
                   'relative L/R generators and central conjugation',
                   'integral actual-circle Gysin map and adjoint Jin clutch',
                   'signed (+,-,+) three-disc plumbing',
                   'lambda(F)=-Sigma_(F^-1) oriented factor exchange'],
    'scope': 'The changed curve is a semifree fixed edge. The new two-isolated-fixed-point action is assigned a Theta7 class, not a new Jin integer. Subsequent flops at other toric edges are not covered.',
})
p.write_text(json.dumps(data, indent=2)+'\n')
print('Finalized P3K23 with signed fixed-edge formula and explicit arbitrary-edge limitation.')
