#!/usr/bin/env python3
"""Post-exposure LN: rebuild all 90 recorded LI overlaps from exact inputs.

The archived default finite-vector rule is input data: the first free vector
F(x,y) in lexicographic [-3,3]^2, where F is the recorded Smith kernel rule.
Its defining helper pages were read; no historical module is imported/run.
The full gluing uses only the frozen independent LN functions.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
FRESH=ROOT/'code/S6_SERIES_PUBLISH_c7_ln_integral_gluing_v001.py'
assert sha256(FRESH.read_bytes()).hexdigest()=='9639dd5997dd9868224ca1ac308d286642f008f975fc6911af7fd52583413f26'
ns={'__file__':str(FRESH),'__name__':'ln_frozen_definitions_only'}
exec(compile(FRESH.read_text().split("print('LN INTEGRAL GLUING v001:",1)[0],str(FRESH)+'[definitions only]','exec'),ns)
for name in ('ROWS','E4','kernel','make_local','regular_log','free_log','run'):
    globals()[name]=ns[name]
STORE=Path('/tmp/S6_SERIES_PUBLISH_c7_LN_historical')
ARCHIVE=STORE/'S6_SERIES_PUBLISH_manifolds_general_initial_audit.json'
assert sha256(ARCHIVE.read_bytes()).hexdigest()=='bbf7d1cf25140a3c1a011bb0061a37fd72a133fe8c0a1201390a5f273d672d87'
records=json.loads(ARCHIVE.read_text())['old_overlap']
selected=json.loads((ROOT/'agents/continuation7_iii_general_initial_receiving/S6_SERIES_PUBLISH_III_02LN_historical_overlap_inputs.json').read_text())
inputs={r['index']:r['pattern'] for r in selected}
rows={(r['OS'],r['profile']):r for r in ROWS}
admitted=json.loads((ROOT/'agents/continuation7_iii_weighted_catalogue/S6_SERIES_PUBLISH_III_02LD_fresh_patterns.json').read_text())['patterns']
admitted={(tuple(r['key']),tuple(r['choices'])) for r in admitted}
assert len(records)==90 and len(inputs)==30
assert {(r['pattern'],r['weight']) for r in records}==set(product(inputs,(1,2,3)))


def default_input(A):
    h=next(h for h in range(1,7) if A**h==E4)
    F,L=kernel(A-E4)
    assert F.cols==2
    for x,y in product(range(-3,4),repeat=2):
        v=F*sp.Matrix([x,y])
        try:free_log({'A':A,'m':h,'v':v})
        except AssertionError:continue
        return h,v
    raise AssertionError('No vector in the exact archived input rule')


def homology(r):
    return [{'free':1,'torsion':[]},{'free':r['r'],'torsion':list(r['A1'])},
            {'free':r['b2'],'torsion':list(r['T'])},{'free':r['b3'],'torsion':list(r['T'])},
            {'free':r['b2'],'torsion':list(r['A1'])},{'free':r['r'],'torsion':[]},
            {'free':1,'torsion':[]}]


print('LN POST-EXPOSURE OVERLAPS v001: 30 exact marked inputs, weights1,2,3.',flush=True)
for number,old in enumerate(records,1):
    index,d=old['pattern'],old['weight'];p=inputs[index]
    row=rows[p['entry'],p['profile']]
    selected_site=p['zero_index']
    assert row['fibers'][selected_site]==p['zero_type']=='I1'
    assert p['a']*p['b']*sp.Rational(row['height_of_generator'])==1
    originals={i for i,c in p['additive_choices']+p['multiplicative_choices'] if c=='original'}
    originals|={i for i,k in enumerate(row['fibers']) if k.startswith('I') and k.endswith('*') and k[1:-1].isdigit()}
    pattern=[]
    for i,k in enumerate(row['fibers']):
        if i==selected_site:pattern.append('C')
        elif i in originals:pattern.append('O')
        elif k.startswith('I') and k[1:].isdigit():pattern.append('M')
        else:pattern.append('F')
    key=(p['entry'],p['profile'],p['a'],p['b'],selected_site+1)
    assert (key,tuple(pattern)) in admitted
    caps=make_local(row,p['a'],d*p['b'],{selected_site:d},'original')
    powers=[]
    for i,c in enumerate(caps):
        if i==selected_site:continue
        if i in originals:c['cap']='original'
        elif c['mult'] is not None:c['cap']='mumford'
        else:
            m,v=default_input(c['A'])
            c.update(cap='log',m=m,v=v)
            powers.append((i,m,list(map(int,v))))
    e=(d%3)-1
    caps=[regular_log(1,[0,0,0,-e],'ordinary')]+caps
    result=run(caps)
    assert homology(result)==old['homology'],(index,d,result,old['homology'])
    print('OVERLAP PASS',number,'pattern',index,'key',key,'D',d,'e',e,
          'finite_powers',powers,'H1',old['homology'][1],
          'H2',old['homology'][2],'H3',old['homology'][3],flush=True)
print('COMPLETE all90 stored full homology tables agree with the independent LN gluing; exact finite input powers printed; all30 construction keys/choices belong to the admitted495 pattern set.',flush=True)
print('SCOPE historical algorithms not executed; default-vector selection is explicitly inherited input data, not an independent historical input derivation; fresh main not rerun.',flush=True)
