"""02YD prerelease Euler computation from cells and Poincare ranks.

The variables g, k and b are symbolic integers.  Coefficient dictionaries
certify the identities for every allowed value, without numerical sampling.
"""
import json


def plus(a, b):
    c = dict(a)
    for monomial, coefficient in b.items():
        c[monomial] = c.get(monomial, 0) + coefficient
        if c[monomial] == 0:
            del c[monomial]
    return c


def times(a, b):
    out = {}
    for p, c in a.items():
        for q, d in b.items():
            exponent = tuple(x + y for x, y in zip(p, q))
            out[exponent] = out.get(exponent, 0) + c*d
    return {e: c for e, c in out.items() if c}


def scale(a, n):
    return {e: n*c for e, c in a.items() if n*c}


def euler(degree_ranks):
    result = {}
    for degree, rank in degree_ranks.items():
        result = plus(result, scale(rank, (-1)**degree))
    return result


def show(a):
    return [{'g_power':e[0], 'k_power':e[1], 'b_power':e[2], 'coefficient':c}
            for e, c in sorted(a.items())]


ONE = {(0, 0, 0): 1}
G = {(1, 0, 0): 1}
K = {(0, 1, 0): 1}
B = {(0, 0, 1): 1}

base_cells = {0: ONE, 1: scale(G, 2), 2: ONE}
sphere_cells = {0: ONE, 2: ONE}
ruled_cells = {}
for i, base_count in base_cells.items():
    for j, sphere_count in sphere_cells.items():
        ruled_cells[i+j] = plus(ruled_cells.get(i+j, {}), times(base_count, sphere_count))
ruled_cells[2] = plus(ruled_cells[2], K)
ruled_euler = euler(ruled_cells)
assert ruled_euler == plus(plus(scale(ONE, 4), scale(G, -4)), K)

projective_plane_cells = {0: ONE, 2: plus(ONE, K), 4: ONE}
projective_plane_euler = euler(projective_plane_cells)
assert projective_plane_euler == plus(scale(ONE, 3), K)

# Class VII: real oriented four-manifold ranks (1,1,b,1,1),
# with one additional degree-two class for each point blowup.
class_vii_ranks = {0: ONE, 1: ONE, 2: plus(B, K), 3: ONE, 4: ONE}
class_vii_euler = euler(class_vii_ranks)
assert class_vii_euler == plus(B, K)

# The point-blowup local replacement is point -> P1, so the change is 2-1.
local_difference = plus(euler(sphere_cells), scale(ONE, -1))
assert local_difference == ONE

print(json.dumps({
    'target':'02YD / night:P4R.2',
    'algorithm':'Degree convolution of base/fibre cell ranks; alternating coefficient sums; local blowup cell replacement',
    'symbolic_scope':'g>=0, k>=0, b>=0 integers; all displayed identities are coefficient identities',
    'ruled_degree_ranks':{str(d):show(r) for d,r in sorted(ruled_cells.items())},
    'ruled_euler':show(ruled_euler),
    'projective_plane_degree_ranks':{str(d):show(r) for d,r in projective_plane_cells.items()},
    'projective_plane_euler':show(projective_plane_euler),
    'class_vii_betti_ranks':{str(d):show(r) for d,r in class_vii_ranks.items()},
    'class_vii_euler':show(class_vii_euler),
    'point_blowup_euler_increment':show(local_difference),
    'topological_map':'Finite bijective normalization ν:T→S is a homeomorphism; q:T→T0 is the given sequence of point blowups.',
    'limits':'The genus exclusion and the classification/equality implications are proved geometrically in the frozen derivation; this program computes only Euler identities.'
},indent=2))
