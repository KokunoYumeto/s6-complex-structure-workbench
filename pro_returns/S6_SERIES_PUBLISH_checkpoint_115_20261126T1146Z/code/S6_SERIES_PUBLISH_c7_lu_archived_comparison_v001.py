"""LU post-exposure complete archived-record comparison.

Uses only the frozen independent LN definition prefix, the fresh LU h=1
cap map and literal archived inputs. No historical module is imported.
The one historical input guard is executed alone from its exact AST.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from itertools import product
from math import gcd, lcm
import ast
import json
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form

ROOT = Path(__file__).resolve().parents[1]
FRESH = ROOT/'code/S6_SERIES_PUBLISH_c7_ln_integral_gluing_v001.py'
assert sha256(FRESH.read_bytes()).hexdigest() == '9639dd5997dd9868224ca1ac308d286642f008f975fc6911af7fd52583413f26'
ns = {'__file__': str(FRESH), '__name__': 'ln_definitions_only_for_lu'}
exec(compile(FRESH.read_text().split("print('LN INTEGRAL GLUING v001:", 1)[0],
             str(FRESH)+'[definitions only]', 'exec'), ns)
for name in ('ROWS', 'E4', 'E6', 'J', 'integer', 'kernel', 'local_raw',
             'wedge_matrix', 'regular_zero', 'regular_log', 'free_log', 'run'):
    globals()[name] = ns[name]
base_cap, base_invariants = ns['cap_data'], ns['invariants']
STORE = Path('/tmp/S6_SERIES_PUBLISH_c7_LU_historical')
archive = STORE/'S6_SERIES_PUBLISH_manifolds_corrected_initial_audit.json'
assert sha256(archive.read_bytes()).hexdigest() == '9a2a42f64554113985559bf8cbf78c70ae47fcf15461ece7b456a9cbc68722a0'
data = json.loads(archive.read_text())
rows = {(r['OS'], r['profile']): r for r in ROWS}
fresh_pairs = json.loads((ROOT/'agents/continuation7_iii_corrected_initial_receiving/S6_SERIES_PUBLISH_III_02LU_additional_residue_pairs_v001.json').read_text())['additional_pairs']


def hnf(M):
    M = S.Matrix(M)
    assert all(x.q == 1 for x in M)
    return hermite_normal_form(S.Matrix([[int(x) for x in row] for row in M.tolist()]))


def same_lattice(A, B):
    assert A.rows == B.rows and hnf(A) == hnf(B)


def group(M):
    r, t = base_invariants(M)
    return dict(free=r, torsion=list(t))


def geometry(kind, power):
    if kind == 'II':
        mu, perm, labels, C = [1], [0], [0], S.zeros(1)
    elif kind.startswith('I') and kind[1:].isdigit() or kind in ('III', 'IV'):
        n = {'III': 2, 'IV': 3}.get(kind, int(kind[1:]) if kind[1:].isdigit() else 0)
        mu, perm, labels = [1]*n, [(i+1) % n for i in range(n)], list(range(n))
        C = -2*S.eye(n)
        for i in range(n):
            C[i, (i-1) % n] += 1
            C[i, (i+1) % n] += 1
    elif kind in ('III*', 'IV*'):
        if kind == 'III*':
            mu, perm, labels = [1, 1, 2, 2, 3, 3, 4, 2], [1, 0, 3, 2, 5, 4, 6, 7], [0, 1]
            edges = [(0, 2), (2, 4), (4, 6), (6, 5), (5, 3), (3, 1), (6, 7)]
        else:
            mu, perm, labels = [1, 1, 1, 2, 2, 2, 3], [1, 2, 0, 4, 5, 3, 6], [0, 1, 2]
            edges = [(0, 3), (1, 4), (2, 5), (3, 6), (4, 6), (5, 6)]
        C = -2*S.eye(len(mu))
        for i, j in edges: C[i, j] = C[j, i] = 1
    else:
        assert kind in ('I1*', 'I3*')
        n = 6 if kind == 'I1*' else 8
        mu, labels = [1]*4+[2]*(n-4), [0, 2, 1, 3]
        perm = [2, 3, 1, 0]+[n+3-i for i in range(4, n)]
        C = -2*S.eye(n)
        edges = [(0, 4), (1, 4), (2, n-1), (3, n-1)]+[(i, i+1) for i in range(4, n-1)]
        for i, j in edges: C[i, j] = C[j, i] = 1
    T = S.zeros(len(mu))
    for i, j in enumerate(perm): T[j, i] = 1
    assert C*S.Matrix(mu) == S.zeros(len(mu), 1) and T*C == C*T
    Tp = T**power
    seen, orbits = set(), []
    for i in range(len(mu)):
        if i in seen: continue
        orbit, j = [], i
        while j not in seen:
            orbit.append(j); seen.add(j)
            j = next(k for k in range(len(mu)) if Tp[k, j])
        assert j == i
        orbits.append(orbit)
    return C, mu, labels, Tp, orbits


def corrections(row, a, b, archived=None):
    answer = {}
    for j, (kind, comp) in enumerate(zip(row['fibers'], row['component_coordinates'])):
        n = comp['moduli'][0] if comp['moduli'] else 1
        residue = comp['rows'][0][0] if comp['rows'] else 0
        p, q = a*residue % n, b*residue % n
        C, mu, labels, T, orb = geometry(kind, q)
        d = S.Matrix(archived[str(j)]['divisor']) if archived else S.zeros(C.rows, 1)
        c = S.eye(C.rows)[:, labels[p]]-S.eye(C.rows)[:, labels[0]]+C*d
        assert T*c == c and (c.T*S.Matrix(mu))[0] == 0
        h = gcd(*(abs(len(o)*int(c[o[0]])) for o in orb))
        result = dict(type=kind, P_component=p, Q_component=q, divisor=list(map(int, d)),
                      chern=list(map(int, c)), rho=len(orb), h=h, orbits=orb)
        if archived:
            old = archived[str(j)]
            assert all(old[k] == result[k] for k in result if k != 'orbits')
            assert sorted(map(sorted, old['orbits'])) == sorted(map(sorted, orb))
        answer[j] = result
    return answer


def local_caps(row, a, b, weights, original, corr):
    result = []
    for j, kind in enumerate(row['fibers']):
        B, g = S.Matrix(row['elliptic_matrices'][j]), S.Matrix(row['generator_section_cocycle'][j])
        z0, mult = local_raw(B, g, kind)
        order = lcm(*(int(x.q) for x in z0))
        r = -a*g.T*J*B
        A = E4.copy(); A[:2, :2] = B; A[:2, 3] = b*g; A[2, :2] = r
        A[2, 3] = (r*b*z0)[0]+weights[j]
        A = integer(A)
        cap = 'original' if j in original else ('positive' if weights[j] else 'mumford')
        if mult is None and j not in original: cap = 'log'
        result.append(dict(A=A, B=B, g=g, z=b*z0, kind=kind, mult=mult,
                           w=weights[j], b=b, narrow_p=a % order == 0,
                           narrow_q=b % order == 0, cap=cap, correction=corr[j]))
    result.extend(regular_zero(w) for w in weights[len(row['fibers']):])
    return result


def cap_data(c):
    if c['cap'] == 'original' and c['mult'] is None:
        cc = c['correction']
        if any(cc['chern']):
            assert cc['h'] == 1
            q = lcm(*(int(x.q) for x in c['z']))
            area = integer(q*S.Matrix([[1, 0, c['z'][1], 0, -c['z'][0], 0]]))
            F, unused = kernel(area)
            fixed, unused = kernel(c['A']-E4)
            return F, fixed, E4[:, :3], cc['rho'], None
        result = base_cap(c)
        assert result[3] == cc['rho']
        return result
    return base_cap(c)


captured = []
def capture_invariants(M):
    captured.append(M.copy())
    return base_invariants(M)
ns['cap_data'], ns['invariants'] = cap_data, capture_invariants


def default_power(A):
    h = next(h for h in range(1, 7) if A**h == E4)
    F, unused = kernel(A-E4)
    assert F.cols == 2
    for x, y in product(range(-3, 4), repeat=2):
        v = F*S.Matrix([x, y])
        try: free_log(dict(A=A, m=h, v=v))
        except AssertionError: continue
        return h, v
    raise AssertionError('No vector in the attributed archived default rule')


def homology(r):
    return [dict(free=1, torsion=[]), dict(free=r['r'], torsion=list(r['A1'])),
            dict(free=r['b2'], torsion=list(r['T'])), dict(free=r['b3'], torsion=list(r['T'])),
            dict(free=r['b2'], torsion=list(r['A1'])), dict(free=r['r'], torsion=[]),
            dict(free=1, torsion=[])]


print('START', datetime.now(timezone.utc).isoformat(), flush=True)
assert len(data['old_full_matrix_overlaps']) == 42
for index, old in enumerate(data['old_full_matrix_overlaps'], 1):
    row = rows[tuple(old['key'])]; a = int(1/S.Rational(row['height_of_generator'])); b = 1
    target = next(j for j, k in enumerate(row['fibers']) if k.startswith('I') and k[1:].isdigit())
    weights = [int(j == target) for j in range(len(row['fibers']))]
    original = {j for j, k in enumerate(row['fibers']) if k.startswith('I') and k.endswith('*') and k[1:-1].isdigit()}
    caps = local_caps(row, a, b, weights, original, corrections(row, a, b))
    powers = []
    for j, cap in enumerate(caps):
        if cap['cap'] == 'log':
            m, v = default_power(cap['A']); cap.update(m=m, v=v); powers.append([j, m, list(map(int, v))])
    caps.insert(0, regular_log(1, [0, 0, 0, -old['e']], 'ordinary'))
    captured.clear(); result = run(caps)
    assert homology(result) == old['homology']
    print('OLD_OVERLAP', index, old['key'], 'e', old['e'], 'powers', powers, 'PASS', flush=True)

coverage, local_count, comparisons = [], 0, []
for category in ('D50_examples', 'new_residue_cases', 'additional_weights_and_regular_logs'):
    for index, old in enumerate(data[category], 1):
        row = rows[old['entry'], old['profile']]
        corr = corrections(row, old['P'], old['Q'], old['vertical_corrections'])
        caps = local_caps(row, old['P'], old['Q'], old['weights'], set(old['original_sites']), corr)
        presentation = old['fundamental_group']; offset = len(presentation['conjugation_matrices'])-len(caps)
        powers = {p['site']: p for p in presentation['finite_power_relations']}
        regular = [regular_log(powers[i]['m'], powers[i]['v'], 'recorded-regular') for i in range(offset)]
        assert powers[offset-1] == dict(site=offset-1, m=1, v=[0, 0, 0, -old['e']])
        vertical, nonfinite = [], []
        for j, (cap, stored) in enumerate(zip(caps, old['local'])):
            assert stored['site'] == j and stored['type'] == ('I0' if cap['kind'] == 'regular' else cap['kind'])
            if cap['cap'] == 'log':
                p = powers[offset+j]; cap.update(m=p['m'], v=S.Matrix(p['v']))
                assert stored['kind'] == 'finite' and stored['m'] == p['m'] and stored['v'] == p['v']
            else:
                F, fixed, F1, h4, unused = cap_data(cap)
                same_lattice(F, S.Matrix(stored['fibre_kernel']))
                same_lattice(fixed, S.Matrix(stored['normal_vectors']))
                same_lattice(F1, S.Matrix(stored['pi1_kernel']))
                assert h4 == stored['components']
                vertical.extend(F1.columnspace()); nonfinite.append((offset+j, F1)); local_count += 1
        caps = regular+caps
        assert [c['A'].tolist() for c in caps] == presentation['conjugation_matrices']
        captured.clear(); result = run(caps)
        H2, H1E, H1 = captured[-3:]
        same_lattice(H2, S.Matrix(old['H2_matrix']))
        count = len(caps)
        P = S.zeros(4+count-1, 4+count); P[:4, :4] = S.eye(4)
        P[4:, 4:4+count-1] = S.eye(count-1); P[4:, -1] = -S.ones(count-1, 1)
        same_lattice(P*H1, S.Matrix(old['H1_matrix']))
        assert homology(result) == old['homology'] and result['q'] == old['relative_free_rank'] and result['chi'] == old['euler']
        assert group(S.Matrix(old['H1_matrix'])) == old['homology'][1]
        assert group(S.Matrix(old['H2_matrix'])) == dict(free=result['g'], torsion=list(result['T']))
        Z = hnf(S.Matrix.hstack(*vertical)); steps = 0
        while True:
            Znew = hnf(S.Matrix.hstack(Z, *(c['A']*Z for c in caps)))
            if Znew == Z: break
            Z = Znew; steps += 1
        for c in caps:
            same_lattice(c['A']*Z, Z); same_lattice(c['A'].inv()*Z, Z)
        assert Z == S.Matrix(presentation['vertical_normal_closure'])
        assert group(Z[:3, :]) == presentation['vertical_quotient']
        assert len(nonfinite) == len(presentation['unchanged_caps'])
        for (i, F1), saved in zip(nonfinite, presentation['unchanged_caps']):
            assert saved['site'] == i and saved['base_loop_killed']
            same_lattice(F1, S.Matrix(saved['killed_vectors']))
        assert presentation['fibre_generators'] == ['e1', 'e2', 'delta', 'gamma'] and presentation['fibre_abelian']
        assert presentation['base_generators'] == [f't{i}' for i in range(count)] and presentation['base_product'] == '1'
        if category == 'D50_examples':
            assert old['homology'][1] == dict(free=0, torsion=[])
            assert old['homology'][2] == old['homology'][3] == dict(free=0, torsion=[old['Q']])
            assert presentation['vertical_quotient'] == dict(free=0, torsion=[])
        if category == 'new_residue_cases':
            coverage.append((old['entry'], old['profile'], old['P'], old['Q'], tuple(old['weights']), tuple(old['original_sites'])))
        comparisons.append(dict(category=category, index=index, key=[old['entry'], old['profile'], old['P'], old['Q']],
                                H1=old['homology'][1], H2=old['homology'][2], H3=old['homology'][3], closure_steps=steps))
        print('FULL_RECORD', category, index, 'key', comparisons[-1]['key'], 'H1', old['homology'][1],
              'H2', old['homology'][2], 'H3', old['homology'][3], 'closure_steps', steps, 'PASS', flush=True)

expected = []
for p in fresh_pairs:
    row = rows[p['OS'], p['profile']]; kinds = row['fibers']; h = p['height']
    sites = [j for j, k in enumerate(kinds) if k.startswith('I') and k[1:].isdigit()]
    additive = set(range(len(kinds)))-set(sites)
    stars = {j for j, k in enumerate(kinds) if k.startswith('I') and k.endswith('*') and k[1:-1].isdigit()}
    for zero in sites:
        weights = tuple(h if j == zero else 0 for j in range(len(kinds)))
        for original in sorted({tuple(), tuple(sorted(additive))}):
            expected.append((p['OS'], p['profile'], p['a'], p['b'], weights, tuple(sorted(set(original)|stars))))
assert sorted(coverage) == sorted(expected) and len(coverage) == 212
assert len(data['D50_examples']) == 16 and len(data['additional_weights_and_regular_logs']) == 45
for old in data['additional_weights_and_regular_logs']:
    row = rows[old['entry'], old['profile']]; d0 = int(1/S.Rational(row['height_of_generator']))
    assert (old['entry'], old['profile'], old['P']-d0, old['Q']) in {(r['OS'], r['profile'], r['a'], r['b']) for r in fresh_pairs}
    assert old['weights'] == [0]*len(row['fibers'])+[old['P']*old['Q']//d0] and old['e'] == -1
    assert old['fundamental_group']['finite_power_relations'][0] == dict(site=0, m=2, v=[0, 0, 0, 1])

historical = STORE/'S6_SERIES_PUBLISH_manifolds_corrected_initial.py'
assert sha256(historical.read_bytes()).hexdigest() == '0b3e4521d88814db7b37cb4932d90b5f76fcc2e2290be1c1cac841e970b4ba9e'
text = historical.read_text(); tree = ast.parse(text)
guards = [n for n in ast.walk(tree) if isinstance(n, ast.If) and ast.unparse(n.test).startswith('is_original and semistable and any(local_correction')]
assert len(guards) == 1
fragment = compile(ast.Module(body=guards, type_ignores=[]), str(historical)+'[one guard only]', 'exec')
for divisor, reject in [([0]*8, False), ([1]*8, True)]:
    caught = False
    try: exec(fragment, {'is_original': True, 'semistable': True, 'local_correction': {'divisor': divisor}})
    except ValueError as error:
        caught = True; print('ACTUAL_GUARD_REJECTION', str(error), flush=True)
    assert caught == reject
print('ACTUAL_GUARD_SCOPE original multiplicative literal d=0 accepted; nonzero whole-fibre d rejected. Only this guard was executed.', flush=True)
destination = ROOT/'agents/continuation7_iii_corrected_initial_receiving/S6_SERIES_PUBLISH_III_02LU_archived_comparison_v001.json'
assert not destination.exists()
destination.write_text(json.dumps(dict(records=comparisons, local_kernel_comparisons=local_count,
                                      old_overlaps=42, full_records=len(comparisons), new_coverage=len(coverage)), indent=2)+'\n')
print('COMPLETE all42 old tables and273 full records, all212 prescribed new cases,45 extras,16 examples;', local_count, 'local maps.', flush=True)
print('DATA', destination.relative_to(ROOT), 'SHA256', sha256(destination.read_bytes()).hexdigest(), flush=True)
print('END', datetime.now(timezone.utc).isoformat(), flush=True)
