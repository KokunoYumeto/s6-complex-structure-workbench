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
# These derivative identities are diagnostics only. The actual cap arrow
# holds the Cox quaternion fixed and is not the derivative of this base map.
matzero('diagnostic_full_ball_derivative', derivative-expected)
zero('diagnostic_ball_derivative_trace', S.trace(derivative))
zero('diagnostic_cotangent_vs_tangent_positive_ratio',
     (r**2/S.conjugate(d))/(d/r**2)-r**4/(dr**2+di**2))

x, y, xb, yb = S.symbols('x y xbar ybar', nonzero=True)
U = S.Matrix([[1,-xb/yb],[x/y,1]])
raw_g = S.Matrix([[y,-xb],[x,yb]])
matzero('actual_Cartier_Cox_product', U*S.diag(y,yb)-raw_g)
swap = S.Matrix([[0,1],[1,0]])
matzero('historical_linear_ordering_algebra_only',
        U*swap*S.diag(yb,y)-raw_g*swap)
zero('spinor_determinant', raw_g.det()-(x*xb+y*yb))
matzero('spinor_norm',
        S.Matrix([[yb,xb],[-x,y]])*raw_g-(x*xb+y*yb)*S.eye(2))
normal = S.Matrix([[ss,S.conjugate(w)],[w,-ss]])
swapped = S.Matrix([[-ss,w],[S.conjugate(w),ss]])
matzero('historical_linear_swap_algebra_only', swap*normal*swap-swapped)
real_swap = S.diag(-1,1,-1)  # gamma, Re ell, Im ell
zero('historical_linear_swap_determinant', real_swap.det()-1)
actual_antilinear_swap = S.diag(-1,1,1)
zero('actual_antilinear_normal_determinant', actual_antilinear_swap.det()+1)
Qreal=S.Matrix([[0,0,1,0],[0,0,0,-1],[-1,0,0,0],[0,1,0,0]])
zero('actual_antilinear_real_four_determinant',Qreal.det()-1)
matzero('actual_quaternionic_square',Qreal**2+S.eye(4))

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
Z = (s-rho)/(s+rho)
zero('retained_Cartier_canonical_determinant',
     (s+rho)**2*S.diff(Z,s)-2*rho)
zero('literal_outer_GL_determinant',
     S.Matrix([[1,-rho],[1,rho]]).det()-2*rho)
q0, q1, circle = S.symbols('q0 q1 circle', nonzero=True)
# The literal product cap leaves q_H fixed; applying its physical right
# circle before or after the base map gives identical normal coordinates.
matzero('product_cap_circle_equivariance',
        S.Matrix([q0*circle,q1*circle])-S.Matrix([q0,q1])*circle)
F = S.Matrix([s**2-rho**2, s*(s**2-rho**2), rho])
cross = F.diff(s).cross(F.diff(rho))
covector = S.Matrix([3*s**2-rho**2, -2*s, 2*rho*(s**2-rho**2)])
matzero('actual_normal_covector', cross-covector)
XX, YY, uu, uprime = S.symbols('X Y u uprime')
numerator_q = YY**2-XX**2*(XX+rho**2)
physical_q = numerator_q/(XX+uu)
gradient_q = S.Matrix([S.diff(physical_q,XX),S.diff(physical_q,YY),
                      S.diff(physical_q,rho)+S.diff(physical_q,uu)*uprime])
gradient_q = gradient_q.subs({XX:s**2-rho**2,YY:s*(s**2-rho**2)})
factor_q = -(s**2-rho**2)/(s**2-rho**2+uu)
matzero('physical_q_normal_arrow', gradient_q-factor_q*covector)
zero('first_Cox_normal_unit', factor_q/Z+(s+rho)**2/(s**2-rho**2+uu))
zero('second_Cox_normal_unit', factor_q*Z+(s-rho)**2/(s**2-rho**2+uu))
phase = S.symbols('unit_phase',nonzero=True)
cc0, cc1, cbar1 = S.symbols('c0 c1 cbar1')
zero('residual_inverse_gauge_product', (phase*cc0)*(cc1/phase)-cc0*cc1)
# On the unit circle conjugate(phase^-1)=phase. Both right-complex
# spinor coordinates therefore acquire the same physical scalar phase.
matzero('residual_gauge_physical_circle',
        S.Matrix([phase*cc0,phase*cbar1])-S.Matrix([cc0,cbar1])*phase)
zero('complex_linear_Hopf_degree_matrix', S.Matrix([[1,1],[1,-1]]).det()+2)

e2, signature = S.symbols('Euler_square signature')
solution = S.solve([e2-signature-8, e2+3*signature+4], (e2,signature))
zero('local_Euler_square', solution[e2]-5)
zero('local_signature', solution[signature]+3)
local_pair = (solution[e2], 3*solution[signature]+solution[e2])
zero('local_index', (4*local_pair[0]-local_pair[1])/24-1)
sphere_pair = (p1/4,p1)
zero('normal_sphere_index', (4*sphere_pair[0]-sphere_pair[1])/24)
thom_pair = tuple(a+b for a,b in zip(local_pair,sphere_pair))
pair = tuple(-a for a in thom_pair)
zero('source_physical_k', pair[0]+6)
zero('source_ell', pair[1])
A = (4*pair[0]-pair[1])/24
zero('source_physical_A', A+1)
relative = (pair[0]-6*A, 6*A)
zero('actual_relative_left', relative[0])
zero('actual_relative_right', relative[1]+6)

report = {
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status': 'PASS',
    'scope': 'Actual F54/F56 positive rho source loop, initial physical fixed-edge fan only.',
    'checks_count': len(checks),
    'checks': checks,
    'local_surgery_pair_U': list(map(int,local_pair)),
    'relative_c2': int(c2),
    'normal_Pontryagin': int(p1),
    'normal_sphere_pair_U': list(map(int,sphere_pair)),
    'source_pair_U':list(map(int,thom_pair)),
    'source_pair_M':list(map(int,pair)),
    'source_physical_A':int(A),
    'source_physical_class_mod_28':int(A)%28,
    'central_coordinate':-1,
    'line_convention':'M is the physical nonzero-vector line; U=M inverse is the meridian-one Thom line. Exact K68 cap and inverse-clutch maps retained.',
    'source_pair': list(map(int,pair)),
    'relative_pair': list(map(int,relative)),
    'uncomputed': ['other cusp-edge normal products', 'all-fan variation and derivative matrices'],
    'proof': 'notes/part3_source_cusp_characteristic_pair_working.md'
}
report['superseded_attempt'] = 'code/part3/attempts/source_cusp_pair_cotangent_factor_omission/'
report['outer_cap_arrow'] = '(P,q_H,rho) -> (B_rho(P),q_H,rho), with actual q_H retained'
report['diagnostic_warning'] = 'The derivative matrix is algebraically correct but does not supply the actual Cox normal comparison; det(A_rho)=2rho is retained explicitly.'
out = ROOT/'code/part3/source_cusp_characteristic_pair.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(f'PASS: {len(checks)} exact identities; local pair={local_pair}, '
      f'normal c2={c2}, sphere pair={sphere_pair}, source pair={pair}, relative={relative}.')
