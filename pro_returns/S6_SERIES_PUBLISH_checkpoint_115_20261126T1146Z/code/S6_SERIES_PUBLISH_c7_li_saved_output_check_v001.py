"""Post-exposure LI: independently check every stored historical sample.

The historical algorithm and its imported target algorithms are not run.
The new descending-word implementation reconstructs the defining inputs.
All stored matrices are parsed and their Smith groups are recalculated.
This does not claim to reproduce the unsaved 1953 historical executions.
"""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json
import math
import sympy as S
import S6_SERIES_PUBLISH_c7_li_ordered_words_v02 as N

ROOT = Path(__file__).resolve().parents[1]
OLD = Path('/tmp/S6_SERIES_PUBLISH_c7_LI_historical/S6_SERIES_PUBLISH_manifolds_all_weighted_profiles.json')
saved = json.loads(OLD.read_text())
raw = json.loads(N.RAW.read_text())
rows = {r['key']: r for r in N.reconstruct_rows(raw['rows'])}
assert len(rows) == 172
assert set(saved) == {'scope', 'chainchecks', 'wordchecks', 'checks',
                      'even_checks', 'overlap_comparisons', 'samples'}
assert saved['checks'] == saved['even_checks'] + saved['overlap_comparisons']
assert len(saved['samples']) == 35
counts = Counter()


def matrix(value):
    result = S.Matrix(value)
    assert all(z.is_Integer for z in result)
    return result


def group(M):
    free, torsion = N.cokernel(M)
    return {'free': free, 'torsion': list(torsion)}


for number, sample in enumerate(saved['samples'], 1):
    os, profile, a, b, selected = sample['key']
    row = rows[(os, profile, a, b, selected+1)]
    weight = sample['weight']
    assert weight > 0 and sample['common_factor'] == math.gcd(a, weight)
    assert sample['common_factor'] % 2 == 0
    Sd = S.diag(1, 1, 1, weight)
    mats = [S.eye(4)] + [N.integral(Sd.inv()*A*Sd) for A in row['matrices']]
    assert N.product(mats) == S.eye(4)
    corrections = sample['bar_corrections']
    assert len(corrections) == len(mats)-1
    for A, coefficients in zip(mats[:-1], corrections):
        lift = N.Lift(A)
        diagonal = [-lift.f(2*S.eye(4)[:,i]) for i in range(4)]
        mixed = [-lift.f(S.eye(4)[:,i]+S.eye(4)[:,j]) for i,j in N.PAIRS]
        assert coefficients == {
            'diagonal': [list(map(int, v)) for v in diagonal],
            'mixed': [list(map(int, v)) for v in mixed]}
        for coords in ([1,-2,3,-1], [-2,1,-1,2], [2,2,-3,-2]):
            u = S.Matrix(coords)
            v, z = lift.forward(u, S.zeros(6,1))
            ui, zi = lift.inverse(v, z)
            assert ui == u and zi == S.zeros(6,1)
        counts['full_quadratic_coefficient_blocks'] += 1

    R = S.Matrix.hstack(*(N.ext(A)-S.eye(6) for A in mats))
    M = matrix(sample['H2_matrix'])
    assert M[:6,:R.cols] == R
    assert M[6:,:R.cols] == S.zeros(M.rows-6,R.cols)
    assert group(R) == sample['regular_fibre_coinvariant']
    actual = group(M)
    H = sample['homology']
    assert len(H) == 7
    H1 = group(matrix(sample['H1_matrix']))
    assert H1 == H[1]
    r = H1['free']
    assert r in (0,1)
    assert actual['free'] == (r if sample['L'] == 0 else 0)
    b2 = weight-1+sample['beta']+sample['L']+r+actual['free']
    b3 = 2+2*b2-2*r-2*weight
    assert H[0] == H[6] == {'free':1,'torsion':[]}
    assert H[2] == {'free':b2,'torsion':actual['torsion']}
    assert H[3] == {'free':b3,'torsion':actual['torsion']}
    assert H[4] == {'free':b2,'torsion':H1['torsion']}
    assert H[5] == {'free':r,'torsion':[]}
    assert sum((-1)**i*h['free'] for i,h in enumerate(H)) == 2*weight

    seifert = sample['seifert_relations']
    nlogs = len(seifert)
    SM = S.zeros(nlogs+1)
    for i,(m,n) in enumerate(seifert):
        SM[i,0], SM[i,i+1], SM[-1,i+1] = -n,m,1
    assert SM == matrix(sample['H1_matrix'])
    assert seifert[0] == [1,-sample['e']]
    local = sample['local']
    assert sorted(v['site'] for v in local) == list(range(len(row['sites'])))
    finite_values = []
    for entry in local:
        i = entry['site']
        if entry['kind'] != 'finite':
            continue
        A, v, m = mats[i+1], S.Matrix(entry['v']), entry['m']
        h = N.FINITE[row['sites'][i]['kind']]
        assert m > 0 and m % h == 0 and A**h == S.eye(4) and A*v == v
        assert math.gcd(m,*map(int,v)) == 1
        # Torus fixed points are detected by the primitive integer
        # annihilator of the moving real image of A^j-I.
        for j in range(1,m):
            kernel, *_ = N.smith_split((A**j-S.eye(4)).T)
            obstruction = kernel.T*(S.Rational(j,m)*v)
            assert any(z.q != 1 for z in obstruction), (number,i,j,m)
            counts['actual_nonidentity_power_tests'] += 1
        finite_values.append([m,int(v[3])])
    assert seifert[1:] == finite_values
    counts['saved_samples'] += 1
    print('PASS sample',number,'pattern',sample['pattern_index'],'key',sample['key'],
          'D',weight,'full_fibre_group',sample['regular_fibre_coinvariant'],
          'H1',H1,'H2',H[2],'finite_caps',len(finite_values),flush=True)

print('COUNTS',json.dumps(dict(counts),sort_keys=True))
print('SAVED_HISTORICAL_COUNTS',json.dumps({k:saved[k] for k in
      ('chainchecks','wordchecks','checks','even_checks','overlap_comparisons')},sort_keys=True))
print('DATA_SHA256',sha256(OLD.read_bytes()).hexdigest())
print('SCOPE all35 saved matrices, full stored quadratic coefficients and all powers of their finite caps checked; historical algorithms not executed; unsaved historical runs not reproduced; no manual reading of every serialized entry claimed.')
