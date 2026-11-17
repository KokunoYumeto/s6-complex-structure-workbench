#!/usr/bin/env python3
"""Exact algebra for the actual selected-cusp normal-frame comparison.

The geometric interpretation and orientations are proved in
notes/part3_source_cusp_characteristic_pair_working.md. No fan other
than its specified initial physical fixed-edge fan is evaluated.
"""
from pathlib import Path
import datetime
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
checks = []

def zero(name, expression):
    reduced = S.simplify(S.expand(expression))
    assert reduced == 0, (name, reduced)
    checks.append({"name": name, "difference": str(reduced), "pass": True})

def matzero(name, matrix):
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            zero(f"{name}[{i},{j}]", matrix[i,j])

r = S.symbols('r', positive=True, real=True)
zr, zi, dr, di, ss, wr, wi, eps = S.symbols(
    'zr zi dr di s wr wi eps', real=True)
z, d, w = zr + S.I*zi, dr + S.I*di, wr + S.I*wi
C = S.Matrix([[r,z],[0,d/r]])
P = S.diag(1,0)
K = S.Matrix([[ss,S.conjugate(w)],[w,-ss]])
numerator = C*(P+eps*K)*C.conjugate().T
trace = S.trace(numerator)
derivative = (numerator.diff(eps)*trace - numerator*trace.diff(eps))/trace**2
derivative = derivative.subs(eps,0)
sp = (dr**2+di**2)*ss/r**4
wp = d*w/r**2 - d*S.conjugate(z)*ss/r**3
expected = S.Matrix([[sp,S.conjugate(wp)],[wp,-sp]])
matzero('full_ball_derivative', derivative-expected)
zero('ball_derivative_trace', S.trace(derivative))
zero('cotangent_vs_tangent_positive_ratio',
     (r**2/S.conjugate(d))/(d/r**2)-r**4/(dr**2+di**2))

x, y, xb, yb = S.symbols('x y xbar ybar', nonzero=True)
U = S.Matrix([[1,-xb/yb],[x/y,1]])
raw_g = S.Matrix([[y,-xb],[x,yb]])
matzero('actual_Cartier_Cox_product', U*S.diag(y,yb)-raw_g)
swap = S.Matrix([[0,1],[1,0]])
matzero('fixed_ordering_arrow',
        U*swap*S.diag(yb,y)-raw_g*swap)
zero('spinor_determinant', raw_g.det()-(x*xb+y*yb))
matzero('spinor_norm',
        S.Matrix([[yb,xb],[-x,y]])*raw_g-(x*xb+y*yb)*S.eye(2))
normal = S.Matrix([[ss,S.conjugate(w)],[w,-ss]])
swapped = S.Matrix([[-ss,w],[S.conjugate(w),ss]])
matzero('fixed_real_swap', swap*normal*swap-swapped)
real_swap = S.diag(-1,1,-1)  # gamma, Re ell, Im ell
zero('fixed_real_swap_oriented', real_swap.det()-1)

I = S.diag(S.I,-S.I)
J = S.Matrix([[0,-1],[1,0]])
K0 = S.Matrix([[0,S.I],[S.I,0]])
matzero('right_complex_IJ', I*J+K0)
zero('positive_complex_trace', S.trace(I*J*K0)-2)
import itertools
trace_cube = 0
for perm in itertools.permutations(range(3)):
    inversions = sum(perm[a] > perm[b] for a in range(3) for b in range(a+1,3))
    matrices = (I,J,K0)
    trace_cube += (-1)**inversions*S.trace(
        matrices[perm[0]]*matrices[perm[1]]*matrices[perm[2]])
zero('trace_cube_positive_volume', trace_cube-12)
zero('Chern_Simons_coefficient', 1-S.Rational(2,3)-S.Rational(1,3))
c2 = -S.Rational(1,24)/S.pi**2*(24*S.pi**2)
zero('relative_second_Chern', c2+1)
p1 = -4*c2
zero('adjoint_Pontryagin', p1-4)

s, rho = S.symbols('source_s rho')
F = S.Matrix([s**2-rho**2, s*(s**2-rho**2), rho])
cross = F.diff(s).cross(F.diff(rho))
covector = S.Matrix([3*s**2-rho**2, -2*s, 2*rho*(s**2-rho**2)])
matzero('actual_normal_covector', cross-covector)
zero('complex_linear_Hopf_degree_matrix', S.Matrix([[1,1],[1,-1]]).det()+2)

e2, signature = S.symbols('Euler_square signature')
solution = S.solve([e2-signature-8, e2+3*signature+4], (e2,signature))
zero('local_Euler_square', solution[e2]-5)
zero('local_signature', solution[signature]+3)
local_pair = (solution[e2], 3*solution[signature]+solution[e2])
zero('local_index', (4*local_pair[0]-local_pair[1])/24-1)
sphere_pair = (p1/4,p1)
zero('normal_sphere_index', (4*sphere_pair[0]-sphere_pair[1])/24)
pair = tuple(a+b for a,b in zip(local_pair,sphere_pair))
zero('source_k', pair[0]-6)
zero('source_ell', pair[1])
A = (4*pair[0]-pair[1])/24
zero('source_A', A-1)
relative = (6*A-pair[0], -6*A)
zero('actual_relative_left', relative[0])
zero('actual_relative_right', relative[1]+6)
zero('first_fixed_edge_class', A+relative[1]+5)

report = {
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status': 'PASS',
    'scope': 'Actual F54/F56 positive rho source loop, initial physical fixed-edge fan only.',
    'checks_count': len(checks),
    'checks': checks,
    'local_surgery_pair': list(map(int,local_pair)),
    'relative_c2': int(c2),
    'normal_Pontryagin': int(p1),
    'normal_sphere_pair': list(map(int,sphere_pair)),
    'source_pair': list(map(int,pair)),
    'relative_pair': list(map(int,relative)),
    'uncomputed': ['other cusp-edge normal products', 'all-fan variation and derivative matrices'],
    'proof': 'notes/part3_source_cusp_characteristic_pair_working.md'
}
out = ROOT/'code/part3/source_cusp_characteristic_pair.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(f'PASS: {len(checks)} exact identities; local pair={local_pair}, '
      f'normal c2={c2}, sphere pair={sphere_pair}, source pair={pair}, relative={relative}.')
