"""Independent exact audit of the p=1 common Cayley extension.

The independent geometric test separates every pair of upper triangles
inside each original factor parent. Together with exact per-parent area
and interval coverage this checks full coverage, rather than only volume.
It also checks both directions of each stored full-unit period map.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from collections import defaultdict, Counter
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / 'code/part3_fourfold/e6_p_one_common_cayley.json'
PROOF = ROOT / 'notes/part3_e6_p_one_cayley_working.md'
d = json.loads(INPUT.read_text())
checks = []


def ck(value, label):
    assert bool(value), label
    checks.append(label)


def matrix(rays):
    return S.Matrix.hstack(*(S.Matrix(r) for r in rays))


def integers(m):
    return [[int(x) for x in row] for row in m.tolist()]


def face_key(rays):
    return tuple(sorted(tuple(r) for r in rays))


def triangle(cone):
    rays = [r for r in cone['rays'] if r[3] == 0]
    ck(len(rays) == 3, 'upper star has three upper rays')
    return tuple((Q(z, h), Q(w, h)) for z, w, h, _ in rays)


def twice_area(t):
    a, b, c = t
    return abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))


def separated(a, b):
    # Exact separating-axis criterion for two closed convex triangles.
    # Equality permits a common edge or vertex and rules out open overlap.
    for t in (a, b):
        for i in range(3):
            p, q = t[i], t[(i+1) % 3]
            normal = (q[1]-p[1], p[0]-q[0])
            pa = [normal[0]*x+normal[1]*y for x, y in a]
            pb = [normal[0]*x+normal[1]*y for x, y in b]
            if max(pa) <= min(pb) or max(pb) <= min(pa):
                return True
    return False


cones = d['cones']
ck(len(cones) == 558, '558 saved four-cones')
ck(len({face_key(c['rays']) for c in cones}) == len(cones), 'no repeated cone')
by_parent = defaultdict(list)
matrices = []
volume_by_parent = defaultdict(Q)
for number, co in enumerate(cones):
    n = matrix(co['rays'])
    matrices.append(n)
    p = matrix(d['parents'][co['parent']]['rays'])
    ck(n.det() == 1, f'{number}: positive unimodular orientation')
    a = p.inv()*n
    ck(integers(a) == co['parent_monomial_matrix'] and
       all(v.is_Integer and v >= 0 for v in a), f'{number}: parent ring morphism')
    ck(integers(n.inv()) == co['dual_characters'], f'{number}: dual characters')
    ck(list(n.inv()*S.Matrix([0, 1, 0, 0])) == co['physical_weights'],
       f'{number}: physical action in the actual integral lattice')
    z = list((S.Matrix([[1, 0, 0, 0]])*n))
    w = list((S.Matrix([[-1, 0, 3, 0]])*n))
    ck(z == co['source_projection']['Z_exponents'] and
       w == co['source_projection']['Q_over_Z_exponents'] and
       min(z+w) >= 0, f'{number}: source monomial square')
    ck(co['source_projection']['Q_over_Z_p_unit'] == 1,
       f'{number}: exact source p coefficient')
    ck(co['point_line']['retained_P_divisor'] == 3,
       f'{number}: original Cartier factor')
    ck([2*r[2]+r[3]-1 for r in co['rays']] == co['original_canonical_orders'],
       f'{number}: original marked volume orders')
    v = Q(1, 6)
    for ray in co['rays']:
        v /= ray[2]+ray[3]
    volume_by_parent[co['parent']] += v
    for ref in co['generic_references']:
        r, s = ref['period_shift']
        f = S.Matrix([[-1, 1, 5*r+s, 4*(2*r+s)],
                      [1, 0, r+2*s, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        ck(integers(f*n) == ref['chart_common_character_exponents'],
           f'{number}: independently recomputed common monomials')
        ck(ref['p_unit_exponents'] == [-6-3*r-3*s, r+s, 0, 0] and
           ref['c_unit_exponents'] == [2*r+s, 0, 0, 0],
           f'{number}: full p,c coefficient after b substitution')
    if co['kind'] == 'upper_star':
        by_parent[co['parent']].append((number, triangle(co)))

pair_count = 0
for name, rows in by_parent.items():
    old = [r for r in d['parents'][name]['rays'] if r[3] == 0]
    t = tuple((Q(r[0], r[2]), Q(r[1], r[2])) for r in old)
    ck(sum(twice_area(x[1]) for x in rows) == twice_area(t),
       name+': exact upper area in this original parent')
    for (i, a), (j, b) in combinations(rows, 2):
        ck(separated(a, b), f'upper {i},{j}: interiors separated by an exact edge axis')
        pair_count += 1

for name, parent in d['parents'].items():
    v = Q(abs(int(matrix(parent['rays']).det())), 6)
    for ray in parent['rays']:
        v /= ray[2]+ray[3]
    ck(volume_by_parent[name] == v, name+': full four-dimensional volume')

for row in d['edge_refinements']:
    intervals = []
    cell = row['source_cell']
    for edge in row['edges']:
        a, b = edge['rays']
        ck(a[1] == 3*a[2] and b[1] == 3*b[2], 'top edge retains W height 3')
        intervals.append(tuple(sorted((Q(a[0], a[2]), Q(b[0], b[2])))))
    intervals.sort()
    ck(intervals[0][0] == cell and intervals[-1][1] == cell+1,
       f'cell {cell}: exact top-edge endpoints')
    ck(all(a[1] == b[0] for a, b in zip(intervals, intervals[1:])),
       f'cell {cell}: top edge has neither overlap nor gap')

incidence = Counter(face_key(f) for co in cones for f in combinations(co['rays'], 3))
ck(Counter(incidence.values()) == Counter({2: 842, 1: 548}), 'complete facet incidence')
boundary = {f for f, n in incidence.items() if n == 1}
generic = {f for f in boundary if all(r[3] == 0 for r in f)}
ck(len(generic) == 510, 'generic interface consists of all upper cones')
ck({face_key(r['face']) for r in d['period_facets']} == boundary-generic,
   'every remaining boundary facet is in the full period atlas')

h = S.Matrix([[1, 0, 3, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
b = S.Matrix([[1, 0, -1, 0], [0, 1, 3, 4], [0, 0, 1, 0], [0, 0, 0, 1]])
maps = d['full_period_chart_maps']
index = {(r['source_cone'], r['target_cone'], r['word_h'], r['word_B']): r for r in maps}
ck(len(index) == len(maps) == 38, '38 distinct directed full period chart maps')
for number, r in enumerate(maps):
    source, target, a, e = r['source_cone'], r['target_cone'], r['word_h'], r['word_B']
    ns, nt = matrices[source], matrices[target]
    m = S.Matrix(r['monomial_matrix'])
    pu, cu = S.Matrix(r['p_unit_exponents']), S.Matrix(r['c_unit_exponents'])
    ck(nt*m == (h**a*b**e)*ns and nt*pu == S.Matrix([a, -2*a, 0, 0]) and
       nt*cu == S.Matrix([0, e, 0, 0]), f'period {number}: full original torus square')
    rev = index[(target, source, -a, -e)]
    mr = S.Matrix(rev['monomial_matrix'])
    ck(mr*m == S.eye(4) and mr*pu+S.Matrix(rev['p_unit_exponents']) == S.zeros(4, 1)
       and mr*cu+S.Matrix(rev['c_unit_exponents']) == S.zeros(4, 1),
       f'period {number}: inverse map including both units')
    inverted = set(r['invertible_source_columns'])
    ck(all(m[i, j] >= 0 for i in range(4) for j in range(4) if j not in inverted),
       f'period {number}: localization uses only a face-complement coordinate')
    ck(S.Matrix([[0, 0, 2, 1]])*(h**a*b**e) == S.Matrix([[0, 0, 2, 1]]),
       f'period {number}: original volume character preserved')

P, p, Z = S.symbols('P p Z', nonzero=True)
Q_tate = P**3*p
theta_reindex = Z**2/(Q_tate**3*p**-4)
ck(S.cancel(P**3*P**6*Z**-2*theta_reindex-p) == 0,
   'twice-reindexed theta point-line identity keeps the exact P cubed divisor')

out = {
    'status': 'PASS_INDEPENDENT_P_ONE_COMMON_CAYLEY',
    'utc': datetime.now(timezone.utc).isoformat(),
    'input_sha256': hashlib.sha256(INPUT.read_bytes()).hexdigest(),
    'proof_sha256': hashlib.sha256(PROOF.read_bytes()).hexdigest(),
    'checks': len(checks), 'check_labels': checks,
    'upper_triangle_pairs_checked_for_disjoint_interiors': pair_count,
    'original_factor_parents': len(d['parents']), 'cones': len(cones),
    'directed_full_unit_period_maps': len(maps),
    'scope': 'Independent parent coverage and disjoint-interior audit; exact full-unit inverse maps, source, physical and original volume character squares.',
    'unassigned': 'Global fixed-component assembly, boundary relative classes and characteristic return.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k: v for k, v in out.items() if k != 'check_labels'}, indent=2))
