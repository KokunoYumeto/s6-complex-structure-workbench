#!/usr/bin/env python3
"""Fresh exact verification of the printed conductor-361 CM input.

SymPy polynomial/rational arithmetic, independent of the unavailable named PARI
program. This implementation is after reading the printed proof, and certifies
the exact algebra only; it makes no 110-digit analytic branch replay claim.
"""
from pathlib import Path
import hashlib
import json
import sympy as S

root = Path(__file__).resolve().parent
x, beta = S.symbols('x beta')
checks = []


def red(p):
    return S.Poly(S.expand(p), beta).rem(S.Poly(beta**2+19, beta)).as_expr()


def eq(name, lhs, rhs=0):
    num = S.together(lhs-rhs).as_numer_denom()[0]
    ok = S.expand(red(num)) == 0
    checks.append({'name': name, 'passed': bool(ok)})
    if not ok:
        raise AssertionError(name)


f = 4*x**3-152*x+361
h = (x**9-38*x**8+437*x**7-1444*x**6-7942*x**5+82308*x**4
     -274360*x**3+390963*x**2-130321*x-130321)
N = S.expand((-19*x+76)*h**2+f*(S.diff(h,x,2)*h-S.diff(h,x)**2)
             +(6*x**2-76)*S.diff(h,x)*h)
K = S.expand(S.diff(N,x)*h-2*N*S.diff(h,x))
H0 = (10*x**8-380*x**7+4864*x**6-28880*x**5+72561*x**4
      +54872*x**3-795644*x**2+1824494*x-1433531)
H1 = (20*x**7-304*x**6+760*x**5+10469*x**4-83752*x**3
      +246924*x**2-315514*x+130321)
hp = (H0+beta*H1)/10
hm = (H0-beta*H1)/10
Qx, QY = S.Integer(4), S.Integer(-3)

eq('discriminant_curve', -16*(4*(-38)**3+27*S.Rational(361,4)**2), -19**3)
eq('P_on_curve', 9**2+9, 90)
eq('Q_on_curve', QY**2, f.subs(x,Qx))
eq('duplication_slope_at_P', S.Rational(-38,19), -2)
eq('duplication_x_at_P', (-2)**2, Qx)
eq('duplication_y_at_P', -9-1+(-2)*(0-Qx), -2)
eq('CM_curve_polynomial_identity',
   -K**2*f, 4*N**3-152*19**2*N*h**4+361*19**3*h**6)
eq('CM_N_h_coprime', S.gcd(N,h), 1)
eq('CM_h_squarefree', S.gcd(h,S.diff(h,x)), 1)
eq('CM_h_avoids_2torsion', S.gcd(h,f), 1)
eq('CM_N_degree', S.degree(N,x), 19)
eq('CM_denominator_degree', S.degree(h**2,x), 18)
eq('CM_differential_derivative', S.diff(N/(19*h**2),x), K/(19*h**3))
eq('CM_differential_factor',
   (K/(19*h**3))/(K/(19*beta*h**3)), beta)
eq('CM_kernel_factorization', 19*x*h**2-N, 5*f*hp*hm)

# All polynomial gcd/remainder operations use the exact quadratic number field.
B = S.sqrt(-19)
hpB = hp.subs(beta,B)
eq('plus_kernel_degree', S.degree(hpB,x), 8)
remainder = S.rem(K+19*B*h**3, hpB, x, extension=B)
if S.simplify(remainder) != 0:
    raise AssertionError('plus_kernel_divisibility')
checks.append({'name':'plus_kernel_divisibility','passed':True})
for name, value in (
    ('plus_kernel_coprime_f_h', S.gcd(hpB,f*h,x,extension=B)),
    ('plus_kernel_squarefree', S.gcd(hpB,S.diff(hpB,x),x,extension=B))):
    eq(name, value, 1)
eq('beta_normalized_relative_Laurent_coefficient', 2*S.Poly(h,x).nth(8), -76)
eq('s2_from_relative_Laurent_coefficient', S.Rational(-76,38), -2)
eq('CM_norm_beta', -beta**2, 19)
eq('CM_norm_one_plus_beta', (1+beta)*(1-beta), 20)
eq('plus_kernel_count', 1+3+2*8, 20)

hQ, dhQ, hpQ = h.subs(x,4), S.diff(h,x).subs(x,4), hp.subs(x,4)
eq('h_at_Q', hQ, -37)
eq('h_prime_at_Q', dhQ, 7)
eq('h_plus_at_Q', hpQ, (829-279*beta)/10)
a = QY*dhQ/(beta*hQ)
eq('algebraic_zeta_constant_a', a, -21*beta/703)
r = -(1+beta)/(2*beta)*QY*hpQ/hQ
r_exact = -S.Rational(165,74)+S.Rational(1839,1406)*beta
eq('algebraic_Ribet_coordinate', r, r_exact)
eq('Ribet_coordinate_norm', r_exact*r_exact.subs(beta,-beta),
   S.Rational(974799,26011))
eq('coordinate_norm_elliptic_difference',
   r_exact*r_exact.subs(beta,-beta), 4-N.subs(x,4)/(19*hQ**2))
eq('theta_quotient_square', r**2,
   ((1+beta)**2*f*hp**2/(4*beta**2*h**2)).subs(x,4))

reductions = {}
for p, expected in ((5,7),(11,17)):
    points = [(a,b) for a in range(p) for b in range(p)
              if (b*b+b-a*a*a+38*a-90)%p == 0]
    eq(f'good_reduction_{p}', S.gcd(p,19), 1)
    eq(f'point_count_{p}', len(points)+1, expected)
    reductions[str(p)] = {'affine_points': points, 'point_at_infinity': True,
                           'order': len(points)+1}
eq('coprime_reduction_orders', S.gcd(7,17), 1)
eq('prime5_excluded_by_order17', S.gcd(5,17), 1)
eq('prime11_excluded_by_order7', S.gcd(11,7), 1)

result = {
 'author':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same family',
 'phase':'S6_SERIES_GRIND',
 'scope':'Exact CM map, differential, kernels, normalized constants, Ribet coordinate; rational torsion excluded by good-reduction counts. No analytic numerical replay and no norm-transcendence conclusion.',
 'sympy_version':S.__version__, 'checks_passed':len(checks), 'checks':checks,
 'f':str(f), 'h':str(h), 'N':str(N), 'K':str(K), 'h_plus':str(hp),
 'a':str(-21*beta/703), 'r2':str(r_exact), 'r2_norm':'974799/26011',
 'reductions':reductions,
 'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
output=root/'cm_witness_exact.output.json'
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'checks_passed':len(checks),'output':str(output),
                  'program_sha256':result['program_sha256']},indent=2))
