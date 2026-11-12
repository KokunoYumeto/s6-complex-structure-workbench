"""Finite exact arithmetic checks accompanying the all-integer written proof."""
import json

cases = [(3, 2), (4, 1)]
assert [m-1-a for m,a in cases] == [0, 2]
for m,a in cases:
    exponents = [n for n in range(4*m) if (n+1+a) % m == 0]
    assert exponents == [m-1-a+j*m for j in range(4)]
    assert (m-1-a)-(m-1) == -a
for k in range(-64, 65):
    for order in range(-24, 25):
        assert (4*order+k >= 0) == (order >= -(k//4))
for m in range(65):
    monomials = [(m-2*j,j) for j in range(m//2+1)]
    assert all(a+2*b == m for a,b in monomials)
    assert len(monomials) == m//2+1 == (2*m)//4+1
assert 3*4 == 4*3 == 12
assert -12+2*3 == -6
assert -2*(-6) == 12
print(json.dumps({'status':'PASS', 'finite_canonical_exponents':[0,2],
                  'vertical_order_cases':129*49, 'ring_degrees_checked':65,
                  'proof_scope':'The TeX proves all integers; these are finite arithmetic checks only.'},indent=2))
