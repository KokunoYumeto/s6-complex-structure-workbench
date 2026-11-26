#!/usr/bin/env python3
"""Post-exposure LN: independent verification of every stored constant/example.

Only the definitions of the already frozen fresh LN implementation are loaded;
its 64-case main is not rerun. No historical Python module is imported/run.
All archived JSON entries are parsed; the mathematical comparisons below are
reported completely. This is a new post-exposure check, not fresh LN credit.
"""
from pathlib import Path
from hashlib import sha256
from math import gcd
from collections import Counter
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
FRESH = ROOT/'code/S6_SERIES_PUBLISH_c7_ln_integral_gluing_v001.py'
assert sha256(FRESH.read_bytes()).hexdigest() == '9639dd5997dd9868224ca1ac308d286642f008f975fc6911af7fd52583413f26'
source = FRESH.read_text().split("print('LN INTEGRAL GLUING v001:", 1)[0]
ns = {'__file__':str(FRESH), '__name__':'ln_frozen_definitions_only'}
exec(compile(source, str(FRESH)+'[definitions only]', 'exec'), ns)
for name in ('ROWS','E4','E6','J','integer','smith','kernel','saturated_image',
             'invariants','wedge_matrix','local_raw','make_local','regular_zero',
             'regular_log','cap_data','free_log','run','hermite_normal_form'):
    globals()[name] = ns[name]
STORE = Path('/tmp/S6_SERIES_PUBLISH_c7_LN_historical')
CONSTANTS = STORE/'S6_SERIES_PUBLISH_manifolds_general_initial_constants.json'
AUDIT = STORE/'S6_SERIES_PUBLISH_manifolds_general_initial_audit.json'
assert sha256(CONSTANTS.read_bytes()).hexdigest() == '330f50ff61d62f7e91d06ce1f5cec06796c82750f64241d38a636b44532e4acf'
assert sha256(AUDIT.read_bytes()).hexdigest() == 'bbf7d1cf25140a3c1a011bb0061a37fd72a133fe8c0a1201390a5f273d672d87'
constants, audit = json.loads(CONSTANTS.read_text()), json.loads(AUDIT.read_text())
rows = {(r['OS'],r['profile']):r for r in ROWS}
counts = Counter()

# Rationally constructed primitive columns must be rebuilt over ZZ for HNF.
_raw_hnf = hermite_normal_form
def hermite_normal_form(M):
    assert all(x.q == 1 for x in M)
    return _raw_hnf(sp.Matrix(M.rows,M.cols,[int(x) for x in M]))


def group(M):
    free, torsion = invariants(M)
    return {'free':free, 'torsion':list(torsion)}


def same_lattice(A, B):
    assert A.rows == B.rows
    assert hermite_normal_form(integer(A)) == hermite_normal_form(integer(B))


def closure(columns, matrices):
    L = hermite_normal_form(sp.Matrix.hstack(*columns))
    while True:
        next_L = hermite_normal_form(sp.Matrix.hstack(L, *(A*L for A in matrices)))
        if next_L == L:
            return L
        L = next_L


print('LN POST-EXPOSURE CONSTANTS/EXAMPLES v004: historical code is not executed.', flush=True)
# Exact index sets establish the claimed exhaustive finite constant enumeration.
expected_residues = {(r['OS'],r['profile'],a) for r in ROWS
                     for a in range(int(1/sp.Rational(r['height_of_generator'])))}
assert len(expected_residues) == 284
assert {(r['entry'],r['profile'],r['a_mod']) for r in constants['residues']} == expected_residues
assert len(constants['residues']) == 284
local_records = {(r['entry'],r['profile'],r['a_mod'],r['site']):r
                 for r in constants['rank_one_local']}
expected_local = {(r['OS'],r['profile'],a,i) for r in ROWS
                  for a in range(int(1/sp.Rational(r['height_of_generator'])))
                  for i,k in enumerate(r['fibers']) if k.startswith('I') and k[1:].isdigit()}
assert set(local_records) == expected_local and len(local_records) == 912
for item in constants['common_elliptic_relations']:
    row = rows[item['entry'],item['profile']]
    Bs = [sp.Matrix(B) for B in row['elliptic_matrices']]
    gs = [sp.Matrix(g) for g in row['generator_section_cocycle']]
    relation = sp.Matrix.hstack(*(B-sp.eye(2) for B in Bs))
    assert relation == sp.Matrix(item['relation_matrix'])
    assert group(relation) == {'free':0,'torsion':[]}
    product = E4
    for B,g,kind in zip(Bs,gs,row['fibers']):
        z,mult = local_raw(B,g,kind)
        if mult is not None:
            assert gcd(mult[0],mult[1]) == 1
        r = -g.T*J*B
        A = sp.eye(4)
        A[:2,:2],A[:2,3],A[2,:2],A[2,3] = B,g,r,(r*z)[0]
        product *= A
    expected = sp.eye(4)
    expected[2,3] = -sp.Rational(row['height_of_generator'])
    assert product == expected
    assert str(product[2,3]) == item['generator_central_product']
    counts['products_and_rim_unit_lattices'] += 1
assert counts['products_and_rim_unit_lattices'] == 21
for item in constants['residues']:
    key = item['entry'],item['profile']
    row = rows[key]
    d0 = int(1/sp.Rational(row['height_of_generator']))
    residue = item['a_mod']; a = residue or d0
    assert item['period'] == d0
    caps = make_local(row,a,d0,{},'original')
    Bs = [c['B'] for c in caps]
    mult_columns, star_columns = [], []
    local_count = 0
    for i,c in enumerate(caps):
        if c['mult'] is not None:
            old = local_records[(*key,residue,i)]
            A = c['A']; F = saturated_image(A-E4)
            nu,kappa,u,r = c['mult']
            coefficient = nu//gcd(nu,a*kappa)
            assert coefficient == nu//gcd(nu,a) == old['coefficient']
            assert old['period'] == d0 and old['type'] == c['kind']
            assert sp.Matrix(old['actual_matrix']) == A
            same_lattice(F,sp.Matrix(old['primitive_full_vanishing']))
            projected = hermite_normal_form(F[:2,:])
            expected = hermite_normal_form(sp.Matrix([[int(x)] for x in coefficient*u]))
            assert projected == expected == sp.Matrix(old['projected_line'])
            mult_columns.extend(projected.columnspace())
            counts['local_projection_records'] += 1; local_count += 1
        elif c['kind'].startswith('I') and c['kind'].endswith('*') and c['kind'][1:-1].isdigit():
            F2,fixed,F1,h4,s = cap_data(c)
            projected = hermite_normal_form(F1[:2,:])
            assert projected == sp.eye(2)
            star_columns.extend(projected.columnspace())
    bare, actual = closure(mult_columns,Bs),closure(mult_columns+star_columns,Bs)
    assert bare == sp.Matrix(item['raw_elliptic_closure'])
    assert actual == sp.Matrix(item['original_star_elliptic_closure']), (key,residue,actual,item)
    assert group(actual) == item['vertical_quotient_after_delta']
    exceptional = key == (49,'II') and residue%2 == 1
    assert actual == (2 if exceptional else 1)*sp.eye(2)
    if exceptional:
        i = row['fibers'].index('I2')
        u = caps[i]['mult'][2]
        assert closure(mult_columns+[u],Bs) == sp.eye(2)
        for j,c in enumerate(caps):
            if j != i:
                assert int((Bs[j]-sp.eye(2)).det())%2 == 1
                assert Bs[j]**3 % 2 == sp.eye(2)
                assert all(int(x)%2 == 0 for x in c['A'][:2,3])
    counts['normal_closure_records'] += 1
# One line per profile covers each exact complete residue interval and its locals.
for row in ROWS:
    key = row['OS'],row['profile']; d0=int(1/sp.Rational(row['height_of_generator']))
    nlocal=sum(k.startswith('I') and k[1:].isdigit() for k in row['fibers'])
    print('CONSTANT PASS',key,'a residues 0..',d0-1,'local projections',d0*nlocal,flush=True)
assert counts['normal_closure_records']==284 and counts['local_projection_records']==912


def make_example(saved):
    row=rows[saved['entry'],saved['profile']]
    a,b=saved['P'],saved['Q']; weights=saved['weights']
    assert a>0 and b>0 and sum(weights)==a*b*sp.Rational(row['height_of_generator'])
    caps=make_local(row,a,b,{i:w for i,w in enumerate(weights[:len(row['fibers'])])},'original')
    caps.extend(regular_zero(w) for w in weights[len(row['fibers']):])
    assert len(caps)==len(saved['local'])
    for i,(c,old) in enumerate(zip(caps,saved['local'])):
        assert old['site']==i
        assert old['type']==c['kind'] or old['type']=='I0' and c['kind']=='regular'
        k=old['kind']
        if k=='finite':
            c.update(cap='log',m=old['m'],v=sp.Matrix(old['v']))
            free_log(c)
        else:
            if k=='rank_two_mumford': c['cap']='positive'
            elif k=='rank_one_mumford': c['cap']='positive' if c['w'] else 'mumford'
            else: c['cap']='original'
            F,fixed,F1,h4,s=cap_data(c)
            assert h4==old['components']
            same_lattice(F,sp.Matrix(old['fibre_kernel']))
            same_lattice(fixed,sp.Matrix(old['normal_vectors']))
            same_lattice(F1,sp.Matrix(old['pi1_kernel']))
            if k=='original_zero_chern': assert c['narrow_p']
            if k=='original_nonzero_chern': assert not c['narrow_p'] and c['narrow_q']
            counts['exact_local_kernel_lattices']+=1
    # Preserve the archived peripheral order: ordinary disc, then profile/support.
    caps=[regular_log(1,[0,0,0,-saved['e']],'ordinary')]+caps
    return row,caps


def homology(answer):
    return [{'free':1,'torsion':[]}, {'free':answer['r'],'torsion':list(answer['A1'])},
            {'free':answer['b2'],'torsion':list(answer['T'])},
            {'free':answer['b3'],'torsion':list(answer['T'])},
            {'free':answer['b2'],'torsion':list(answer['A1'])},
            {'free':answer['r'],'torsion':[]}, {'free':1,'torsion':[]}]


assert len(audit['new_examples'])==148
for number,saved in enumerate(audit['new_examples'],1):
    row,caps=make_example(saved)
    answer=run(caps)
    assert homology(answer)==saved['homology'],(number,answer,saved['homology'])
    assert answer['chi']==saved['euler'] and answer['q']==saved['relative_free_rank']
    assert {'free':answer['b1E'],'torsion':list(answer['AE'])}==saved['exterior_H1']
    assert group(sp.Matrix(saved['H1_matrix']))==saved['homology'][1]
    assert group(sp.Matrix(saved['H2_matrix']))=={'free':answer['g'],'torsion':list(answer['T'])}
    returns=sp.Matrix.hstack(*(wedge_matrix(c['A'])-E6 for c in caps))
    assert group(returns)==saved['regular_coinvariant_H2']
    presentation=saved['fundamental_group']
    assert [c['A'].tolist() for c in caps]==presentation['conjugation_matrices']
    assert presentation['fibre_generators']==['e1','e2','delta','gamma']
    assert presentation['fibre_abelian'] and presentation['base_product']=='1'
    assert presentation['base_generators']==[f't{i}' for i in range(len(caps))]
    finite=[{'site':i,'m':c['m'],'v':list(map(int,c['v']))} for i,c in enumerate(caps) if c['cap']=='log']
    assert finite==presentation['finite_power_relations']
    vertical=[]; unchanged=[]
    for i,c in enumerate(caps):
        if c['cap']!='log':
            F,fixed,F1,h4,s=cap_data(c);vertical.extend(F1.columnspace())
            unchanged.append((i,F1))
    assert len(unchanged)==len(presentation['unchanged_caps'])
    for (i,F1),old in zip(unchanged,presentation['unchanged_caps']):
        assert i==old['site'] and old['base_loop_killed']
        same_lattice(F1,sp.Matrix(old['killed_vectors']))
    Z=closure(vertical,[c['A'] for c in caps])
    assert Z==sp.Matrix(presentation['vertical_normal_closure'])
    assert group(Z[:3,:])==presentation['vertical_quotient']
    counts['complete_new_examples']+=1
    print('EXAMPLE PASS',number,'OS',saved['entry'],saved['profile'],
          'a,b',saved['P'],saved['Q'],'weights',saved['weights'],'original',saved['original_sites'],
          'H1',saved['homology'][1],'H2',saved['homology'][2],
          'H3',saved['homology'][3],'chi',answer['chi'],flush=True)
last=audit['new_examples'][-1]
assert (last['entry'],last['profile'],last['P'],last['Q'],last['e'])==(45,'default',2,8,1)
assert last['weights']==[2,0,0,0,0]
assert last['homology']==[{'free':1,'torsion':[]},{'free':0,'torsion':[]},
                         {'free':15,'torsion':[8]},{'free':0,'torsion':[8]},
                         {'free':15,'torsion':[]},{'free':0,'torsion':[]},{'free':1,'torsion':[]}]
assert last['fundamental_group']['vertical_quotient']=={'free':0,'torsion':[]}
assert last['fundamental_group']['finite_power_relations']==[{'site':0,'m':1,'v':[0,0,0,-1]}]
print('OS45 EXPLICIT: C=[[8,24],[-6,-16]], determinant16, Smith(2,8); positive support I8; pi1=1 by the ordinary e=1 relation.',flush=True)
print('COUNTS',json.dumps(dict(counts),sort_keys=True),flush=True)
print('SCOPE all284+912+21 constant records and all148 full examples checked; 90 LI overlaps are reserved for a separate exact input-marking check; no historical algorithm or fresh main rerun.',flush=True)
