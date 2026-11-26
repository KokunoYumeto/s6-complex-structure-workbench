#!/usr/bin/env python3
"""Post-reading preservation checks for three bounded editorial proposals.

The output checks the stated algebra. It does not prove the analytic transport,
normalization/resolution assertions, or the geometric blowup construction.
It is not a statement-first or independent whole-proof check.
"""
import hashlib
import json
from pathlib import Path
import sympy as s

t = s.symbols("t")
product = s.expand((1+t)**4*(1+t**2))
curve_blowup = s.expand(product+t**2*(1+4*t+t**2))
point_blowup = s.expand(curve_blowup+t**2+t**4)
betti = [[int(p.coeff(t,k)) for k in range(7)]
         for p in (product,curve_blowup,point_blowup)]
assert betti == [[1,4,7,8,7,4,1], [1,4,8,12,8,4,1], [1,4,9,12,9,4,1]]
assert [p.subs(t,-1) for p in (product,curve_blowup,point_blowup)] == [0,-2,0]
assert 0+2*(-2)-(-2) == -2
assert 1-4+3-(-2)-2 == 0

x,y,z,eps,lam = s.symbols("x y z eps lam")
A0,As,Az,B0,Bs,Bz,C0,Cs,Cz,D0,Ds,Dz,G = s.symbols("A0 As Az B0 Bs Bz C0 Cs Cz D0 Ds Dz G")
A=A0+As*eps+Az*z
B=B0+Bs*eps+Bz*z
C=C0+Cs*eps+Cz*z
D=D0+Ds*eps+Dz*z
quadratics = []
for k in (3,4):
    h=y**2-x**k-eps*x**2
    f=A*z*h+z**2*(B*x**2+C*x*y+D*y**2)+G*h**2
    quadratic=s.expand(f.subs({x:lam*x,y:lam*y})).coeff(lam,2)
    expected=(-eps*A*z+B*z**2)*x**2+C*z**2*x*y+(A*z+D*z**2)*y**2
    assert s.expand(quadratic-expected)==0
    qa=s.expand(quadratic).coeff(x,2).coeff(y,0)
    qb=s.expand(quadratic).coeff(x,1).coeff(y,1)
    qc=s.expand(quadratic).coeff(y,2).coeff(x,0)
    determinant=s.expand((qa*qc-qb**2/4)/z**2)
    linear=s.expand(determinant.subs({eps:lam*eps,z:lam*z})).coeff(lam,1)
    assert s.expand(linear-(A0*B0*z-A0**2*eps))==0
    quadratics.append({"k":k,"quadratic":str(quadratic),"determinant_linear_jet":str(s.factor(linear))})

X,Z,U,w,q,b0,b1,c0,c1,c2=s.symbols("X Z U w q b0 b1 c0 c1 c2")
Bh=X**2*(b0*X+b1*Z)
Ch=X**3*(c0*X**2+c1*X*Z+c2*Z**2)
Qh=X*U**2+Bh*U+Ch
affine=q**2+(b0+b1*w)*q+c0+c1*w+c2*w**2
assert s.expand(Qh.subs({Z:X*w,U:X**2*q})-X**5*affine)==0
residual=(b0*X+b1*Z)**2-4*(c0*X**2+c1*X*Z+c2*Z**2)
assert s.expand(s.discriminant(Qh,U)-X**4*residual)==0
assert s.Poly(residual,X,Z).total_degree()==2
monomial_bounds={}
for degree in (4,5):
    monomials=[(a,b,degree-a-b) for a in range(degree+1)
               for b in range(degree-a+1) if a+b>=3]
    polynomial=sum(s.Symbol(f"p{degree}_{a}_{b}_{c}")*x**a*U**b*Z**c
                   for a,b,c in monomials)
    chart=polynomial.subs({x:1,U:q,Z:w})
    if degree==4:
        monomial_bounds["degree4_restriction"]=s.Poly(chart.subs(q,0),w).degree()
        monomial_bounds["degree4_first_normal_coefficient"]=s.Poly(s.expand(chart).coeff(q,1),w).degree()
    else:
        monomial_bounds["degree5_restriction"]=s.Poly(chart.subs(q,0),w).degree()
assert monomial_bounds=={"degree4_restriction":1,"degree4_first_normal_coefficient":1,"degree5_restriction":2}
# The equation itself bounds d <= 4 and n <= 2 for d >= 3, n >= 1, a >= 0.
solutions=[(d,n,2-(d-2)*n) for d in (3,4) for n in (1,2) if 2-(d-2)*n>=0]
assert solutions==[(3,1,1),(3,2,0),(4,1,0)]

output={
    "scope":"Exposed, post-reading mathematical-preservation computations; no additional check event or independent derivation claim.",
    "program_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "FH":{"poincare_polynomials":[str(p) for p in (product,curve_blowup,point_blowup)],
           "betti_vectors":betti,"total_euler":[0,-2,0],"central_support_euler":[-2,0]},
    "XB":{"method":"Degree-two Taylor coefficient, with general first jets of coefficient functions in the parameter and axis coordinate.",
           "quadratics":quadratics,"implicit_root_first_coefficient":"A0/B0"},
    "XC":{"pole_solutions":solutions,"monomial_bounds":monomial_bounds,
           "homogeneous_quadratic":str(Qh),"coordinate_map":"Z=X*w, U=X^2*q",
           "pullback":str(X**5*affine),"discriminant":str(s.factor(s.discriminant(Qh,U))),
           "fourth_order_factor":"X^4","residual_total_degree":2},
    "all_assertions_passed":True,
}
print(json.dumps(output,indent=2))
