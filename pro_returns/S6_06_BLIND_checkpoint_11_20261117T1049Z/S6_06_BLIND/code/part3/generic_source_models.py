#!/usr/bin/env python3
"""Exact marked-source and root-map identities for proposed P3F.51.

This verifies algebraic identities used by the geometric proof.  It does
not replace that proof's component, quotient, or source-pair arguments.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as S

x, y, t, r, A, X, Y, q, z = S.symbols('x y t r A X Y q z')
l = S.symbols('l', integer=True, nonnegative=True)
u = S.symbols('u')
checks = []

def zero(expr, label):
    expr = S.factor(S.cancel(expr))
    assert expr == 0, (label, expr)
    checks.append(label)

e7 = x**3 + 3*r*x**2 + t*x + 1
d7 = -4*t**3 + 9*r**2*t**2 + 54*r*t - 108*r**3 - 27
zero(S.discriminant(e7, x)-d7, 'E7 full marked discriminant')
disc7 = S.factor(S.discriminant(d7, t))
zero(disc7 - 314928*(r**3-1)**3, 'E7 discriminant collision locus')
zero(d7.subs(r, 1) + (t-3)**2*(4*t+15), 'E7 II and I1 at r=1')
xo, to = S.symbols('x_old t_old')
zero(e7.subs({r: 1, x: xo-1, t: to+3}) -
     (xo**3+to*xo-to), 'E7-B literal affine coordinate map')
s = S.symbols('s', nonzero=True)
zero(e7.subs({x:s**2*X,t:s**4*t})/s**6-
     (X**3+3*r/s**2*X**2+t*X+s**-6), 'E7 constant scaling')

e6 = x**3 + 3*r*x**2 + A*t*x + t**2
bracket = 9*r**2*(A**2-12*r)+(54*r*A-4*A**3)*t-27*t**2
zero(S.discriminant(e6,x)-t**2*bracket, 'E6 full marked discriminant')
zero(S.discriminant(bracket,t)-16*(A**2-9*r)**3,
     'E6 residual discriminant collision locus')
zero(e6.subs({x:s**2*X,t:s**3*t})/s**6-
     (X**3+3*r/s**2*X**2+(A/s)*t*X+t**2),
     'E6 literal scaling and III representative')

# The source-infinity substitutions retain every coefficient.
zero(q**6*e7.subs({x:X/q**2,t:1/q})-
     (X**3+3*r*q**2*X**2+q**3*X+q**6),
     'E7 global-to-local infinity map')
zero(q**6*e6.subs({x:X/q**2,t:1/q})-
     (X**3+3*r*q**2*X**2+A*q**3*X+q**4),
     'E6 global-to-local infinity map')

roots=[]
for name, m, k, want, section in [
    ('E7 good',4*l,3*l,(2*l,0,6*l),3*l),
    ('E7 reduced',4*l+3,3*l+2,(2*l+2,1,6*l+6),3*l+3),
    ('E6 good',3*l,2*l,(2*l,l,0),0),
    ('E6 reduced',3*l+2,2*l+1,(2*l+2,l+2,2),1),
]:
    star=7 if name.startswith('E7') else 6
    exps=(2*m-2*k,3*m-4*k,(6 if star==7 else 4)*m-6*k)
    for got,w in zip(exps,want):
        zero(got-w,name+' coefficient exponent '+str(w))
    zero((3 if star==7 else 2)*m-3*k-section,
         name+' actual section exponent')
    roots.append(dict(label=name,m=str(m),k=str(k),
                      coefficient_exponents=[str(S.expand(e)) for e in exps],
                      section_exponent=str(section)))
zero((-3*(3*l))-(-l)-(-2)*(4*l),'E7 good Y deck is -i')
zero((-2*(3*l))-(2*l)-(-2)*(4*l),'E7 good X deck is -1')
zero((-2*(2*l))-(-l)-(-1)*(3*l),'E6 good X deck is zeta3 squared')
zero(-(3*(2*l+1)+1)+2*(3*l+2),'E6 reduced blowup labels fixed by deck')

# Good E7 curve, with u=z^l.  The point is (0,u^3).
P7 = lambda xx: xx**3+3*r*u**2*xx**2+xx+u**6
sx7 = 1/(2*u**3)
x27 = 1/(4*u**6)-3*r*u**2
y27 = -1/(8*u**9)+(3*r/2)/u-u**3
zero(x27-(sx7**2-3*r*u**2),'E7 actual doubling x-coordinate')
zero(y27-(-u**3-sx7*x27),'E7 actual doubling y-coordinate')
zero(y27**2-P7(x27),'E7 doubled point lies on full root equation')
w27 = S.factor(-x27/y27)
zero(S.limit(w27/u**3,u,0)-2,'E7 formal parameter has leading +2')
zero(w27.subs(u,S.I*u)-(-S.I)*w27,'E7 minimal deck formal character')

# Good E6 curve, with u=z^l.  The point is (0,1).
P6 = lambda xx: xx**3+3*r*u**2*xx**2+A*u*xx+1
c = A**2/4-3*r
sx6 = A*u/2
x26 = c*u**2
y26 = -1-(A*c/2)*u**3
zero(x26-(sx6**2-3*r*u**2),'E6 actual doubling x-coordinate')
zero(y26-(-1-sx6*x26),'E6 actual doubling y-coordinate')
zero(y26**2-P6(x26),'E6 doubled point lies on full root equation')
sx36 = S.factor((y26-1)/x26)
x36 = S.factor(sx36**2-3*r*u**2-x26)
y36 = S.factor(-1-sx36*x36)
zero(y36**2-P6(x36),'E6 actual tripled point lies on full root equation')
w36 = S.factor(-x36/y36)
zero(S.limit(w36/u**2,u,0)-(12*r-A**2)/8,
     'E6 tripling formal parameter leading coefficient')
rho = S.symbols('rho')
num,den = S.fraction(S.together(w36.subs(u,rho*u)-rho**2*w36))
zero(S.rem(S.Poly(num,rho),S.Poly(rho**2+rho+1,rho)).as_expr(),
     'E6 minimal deck formal character')

rays={4:[(3,1),(2,1),(1,1),(1,2),(1,3)],
      3:[(2,1),(1,1),(1,2)]}
corrections={}
for order,rr in rays.items():
    coeff=[min(a,(order-1)*b) for a,b in rr]
    assert coeff==({4:[3,2,1,1,1],3:[2,1,1]}[order])
    corrections[str(order)]=dict(rays=rr,coefficients=coeff)
    checks.append('order '+str(order)+' exact toric Cartier pullback')

out=dict(status='PASS',timestamp_utc=datetime.now(timezone.utc).isoformat(),
         proof='notes/part3_generic_source_models.md',checks=checks,
         E7_discriminant=str(d7),E7_discriminant_discriminant=str(disc7),
         E6_discriminant=str(t**2*bracket),
         E6_residual_discriminant=str(16*(A**2-9*r)**3),roots=roots,
         E7_w2=str(w27),E6_w3=str(w36),toric_corrections=corrections,
         scope='Exact algebra only; geometric quotient, component, and topology maps are proved in the note.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
for item in checks:
    print('PASS:',item)
print('PASS:',len(checks),'exact marked-source, root, section and Cartier identities.')
