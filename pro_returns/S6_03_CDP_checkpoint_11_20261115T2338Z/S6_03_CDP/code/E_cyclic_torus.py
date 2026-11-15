"""Exact local quotient-form and crepant-fan checks for C.2.UN.23."""
from fractions import Fraction as F
from math import gcd, lcm

checked = 0
for n in range(2, 41):
    for r in range(1, n):
        if gcd(r, n) != 1:
            continue
        # Least power of dz1 wedge dz2 invariant under weights (1,r).
        m = n // gcd(n, 1+r)
        height = F(1+r, n)
        order = m * (height-1)
        assert order.denominator == 1
        assert (order == 0) == (r == n-1)
        assert order <= 0
        # Pairing character m(1,1) with the primitive ray, minus m.
        assert m*(1+r) % n == 0
        assert order == F(m*(1+r), n)-m
        checked += 1
    # The SL(2) case: consecutive height-one rays form lattice bases.
    rays = [(F(n-k, n), F(k, n)) for k in range(n+1)]
    assert all(x+y == 1 for x, y in rays)
    for (x,y), (u,v) in zip(rays, rays[1:]):
        assert x*v-y*u == F(1,n)
    # Each interior point lies in Z² + Z(1/n,(n-1)/n):
    for x,y in rays:
        assert (y-(n-1)*x).denominator == 1
    print(f"n={n}: height-one fan has {n-1} exceptional rays; "
          f"all adjacent determinants=1/{n}; all canonical orders=0")

print(f"Checked {checked} effective no-pseudoreflection cyclic weight pairs.")
print("Every non-SL pair has a strictly negative invariant canonical order.")
print("The argument for all n is the exact formula m((1+r)/n-1).")
print("Branch curves are handled separately by the Jacobian order m(e-1).")
print("All exact checks passed.")
