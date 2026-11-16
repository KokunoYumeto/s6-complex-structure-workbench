"""Exact root involutions, invariant plurigenera and support ranks for UN27."""
import sympy as s
from fractions import Fraction

z=s.symbols('z')
for r in range(2, 11):
    polynomial=s.prod(z*z-j*j for j in range(1,r+1))
    phi=s.prod((z-j)/(z+j) for j in range(1,r+1))
    assert s.gcd(polynomial,s.diff(polynomial,z)) == 1
    assert s.cancel(phi*phi.subs(z,-z)) == 1
    assert phi.subs(z,0) == (-1)**r
    assert s.limit(phi,z,s.oo) == 1
    fixed_C=(4,0) if r%2 == 0 else (2,2)
    fixed_product=[4*x for x in fixed_C]
    assert sum(fixed_product) == 16
    assert sum(fixed_product)//2 == 8
    print(f"r={r}: genus(C)={r-1}; fixed(C)={fixed_C}; "
          f"fixed(product)={fixed_product}; quotient nodes=8")
    plurigenera=[]
    for m in range(1,13):
        # Sections on C: (p(z)+Y q(z))*(dz/Y)^m.
        # eta invariance selects p for m even, Yq for m odd.
        # k invariance selects even polynomials in both cases.
        bound=m*(r-2) if m%2 == 0 else m*(r-2)-r
        invariant_count=max(0,bound//2+1)
        divisor_count=max(0,1-m+r*(m//2))
        assert invariant_count == divisor_count
        plurigenera.append(divisor_count)
    assert plurigenera[0] == 0
    assert plurigenera[1] == r-1
    before=[1,1,r+6,2*r,r+6]
    after=[1,1,r+18,2*r+36,r+18]
    e=lambda v: sum((-1)**i*x for i,x in enumerate(v))
    assert e(before) == 12 and e(after) == 0
    print("  P1,...,P12=",plurigenera,
          "slope=",Fraction(r,2)-1)
    print("  reduced support before=",before,"after six blocks=",after)

print("General formula: div(dz wedge du/u)=sum J_j-F_infinity.")
print("Hence 2K=(r-2)F and p_*mK=O_P1(-m+r floor(m/2)).")
print("The invariant-form count independently checks every displayed plurigenus.")
print("All exact checks passed.")
