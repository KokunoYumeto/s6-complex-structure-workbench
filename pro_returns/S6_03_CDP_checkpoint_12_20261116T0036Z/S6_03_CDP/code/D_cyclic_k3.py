"""Exact fixed-isogeny and exceptional-chain counts for C.2.UN.24.

The integral matrices have the H1 characteristic polynomial of each
symplectic cyclic two-torus action. Determinants therefore compute the
actual fixed-isogeny degrees for every power, without floating point.
"""

from sympy import Matrix, eye, divisors, symbols, expand

x = symbols("x")
expected = {
    2: {2: 16},
    3: {3: 9},
    4: {2: 6, 4: 4},
    6: {2: 5, 3: 4, 6: 1},
}

print("n | characteristic polynomial | fixed points of g^k (1<=k<n)")
print("  | exact stabilizer points | quotient singularities | e(quotient), exceptional rank, e(resolution)")

for n, s in ((2, -2), (3, -1), (4, 0), (6, 1)):
    if n == 2:
        T = -eye(4)
    else:
        C = Matrix([[0, -1], [1, s]])
        T = Matrix.diag(C, C)
    assert T**n == eye(4)
    assert all(T**k != eye(4) for k in range(1, n))
    polynomial = T.charpoly(x).as_expr()
    assert expand(polynomial - (x*x-s*x+1)**2) == 0
    fixed = {k: int((eye(4)-T**k).det()) for k in range(1, n)}
    exact = {}
    orbits = {}
    for d in reversed([d for d in divisors(n) if d > 1]):
        subgroup_fixed = int((eye(4)-T**(n//d)).det())
        exact[d] = subgroup_fixed - sum(v for e, v in exact.items() if e % d == 0)
        assert exact[d] >= 0
        assert exact[d] % (n//d) == 0
        orbits[d] = exact[d] // (n//d)
    assert orbits == expected[n]
    quotient_euler = sum(fixed.values()) // n
    assert sum(fixed.values()) % n == 0
    exceptional_rank = sum(count*(d-1) for d, count in orbits.items())
    assert quotient_euler + exceptional_rank == 24
    assert sum(orbits.values()) >= 4
    signature = " + ".join(f"{orbits[d]} A{d-1}" for d in sorted(orbits, reverse=True))
    print(f"{n} | {polynomial} | {fixed}")
    print(f"  | {dict(sorted(exact.items()))} | {signature} | {quotient_euler}, {exceptional_rank}, 24")

print("All exact cyclic orders, fixed-point counts, orbit divisions, and resolution Euler numbers verified.")
