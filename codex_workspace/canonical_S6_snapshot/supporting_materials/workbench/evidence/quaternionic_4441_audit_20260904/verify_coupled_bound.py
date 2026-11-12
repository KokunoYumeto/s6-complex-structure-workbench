"""Exact algebra supporting, not replacing, the analytic form proof."""
import json
import sympy as S

checks = []
def check(name, expr):
    assert S.simplify(expr) == 0, (name, expr)
    checks.append(name)

x, d, u, s = S.symbols('x d u s', real=True)
lj, lk = (-x+d)/2, (-x-d)/2
check('trace zero retained', x+lj+lk)
check('trace square retained', x*x+lj*lj+lk*lk-(3*x*x+d*d)/2)
check('cubic vertex identity', x*lj*lk-u*x-(x**3-x*((3*x*x+d*d)/2+2*u)/2))
positive_s = S.symbols('s_positive', positive=True)
for sign in (-1, 1):
    r = sign*S.sqrt(positive_s/6)
    check(f'critical derivative {sign}', 3*r*r-positive_s/2)
    check(f'critical cubic value {sign}', (r**3-positive_s*r/2)**2-positive_s**3/54)
    r = sign*S.sqrt(2*positive_s/3)
    check(f'endpoint cubic value {sign}', (r**3-positive_s*r/2)**2-positive_s**3/54)

alpha, Gamma, kappa = S.symbols('alpha Gamma kappa', positive=True)
t = S.symbols('t', real=True)
f = Gamma*t**4/8-alpha*t**3
check('quartic-cubic minimizer derivative', S.diff(f,t).subs(t,6*alpha/Gamma))
check('quartic-cubic minimum value', f.subs(t,6*alpha/Gamma)+54*alpha**4/Gamma**3)
check('scalar shift coefficient', (54*alpha**4/Gamma**3).subs(alpha,kappa/(3*S.sqrt(6)))-kappa**4/(54*Gamma**3))

hbar, g2, volume, eta = S.symbols('hbar g2 volume eta', positive=True)
ag, bg = hbar**2*g2/(4*volume), volume/g2
check('gauge product retains hbar', ag*bg-hbar**2/4)
check('full confinement coefficient squared', (2*S.sqrt(6*(1-eta)*ag*bg))**2-hbar**2*6*(1-eta))
check('half kinetic confinement coefficient', 2*S.sqrt(3*ag*bg)-S.sqrt(3)*hbar)
check('mass metric volume', ((2*volume/g2)**24*volume**8*(2*volume)**6)-(2**15*volume**19/g2**12)**2)
check('gauge energy-origin bound cubed', (9*(S.Rational(3,2))**S.Rational(1,3)*ag**S.Rational(2,3)*bg**S.Rational(1,3))**3-9**3*3*hbar**4*g2/(32*volume))

z, q, y = S.symbols('z q y', real=True)
cos_moments = {0:1,1:0,2:S.Rational(1,2),3:0,4:S.Rational(3,8)}
p = S.Poly((q+y*z)**4,z)
avg = sum(coeff*cos_moments[power[0]] for power,coeff in p.terms())
check('two-Fourier-coordinate quartic cross term', avg-(q**4+3*q*q*y*y+S.Rational(3,8)*y**4))

print(json.dumps({'status':'pass','assertions':len(checks),'checks':checks,
 'scope':'Exact coefficients and polynomial identities only; analytic compactness and spectral assertions have separate proofs.'},indent=2))
