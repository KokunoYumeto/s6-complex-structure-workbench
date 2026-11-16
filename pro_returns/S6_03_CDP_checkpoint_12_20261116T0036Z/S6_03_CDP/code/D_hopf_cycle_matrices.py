"""Exact logarithmic and integral checks for UN46 and UN48."""
import sympy as s
from functools import reduce
from math import gcd
from sympy.matrices.normalforms import hermite_normal_form

c1, c2, k1, k2 = s.symbols("c1 c2 k1 k2")
L1 = s.Matrix([[0, c1], [-1, k1]])
L2 = s.Matrix([[0, c2], [-1, k2]])
product = L2 * L1
assert product == s.Matrix([[-c2, c2*k1], [-k2, -c1+k2*k1]])
sol = s.solve(list(product-s.eye(2)), (c1,c2,k1,k2), dict=True)
assert sol == [{c1:-1,c2:-1,k1:0,k2:0}]
print("Two-component product:", product.tolist())
print("Its unique identity solution:", sol)

# An explicit three-component compatible cycle. Entries of n are the
# coefficients of the outgoing meridians in 2*pi*i*Z^2.
n = [s.Matrix([1,0]), s.Matrix([1,-1]), s.Matrix([0,-1])]
P = [s.Matrix.hstack(n[i],-n[i-1]) for i in range(3)]
L = [P[(i+1)%3].inv()*P[i] for i in range(3)]
assert all(x[0,0] == 0 and x[1,0] == -1 for x in L)
assert reduce(lambda a,b:b*a,L,s.eye(2)) == s.eye(2)
common_contraction = s.Matrix([-1,-s.sqrt(2)])
signs = [1,-1,-1]
contractions = [signs[i]*P[i].inv()*common_contraction for i in range(3)]
assert all(v.is_negative for z in contractions for v in z)
# Basis on each rank-three logarithmic lattice: its two angular
# generators followed by the chosen contracting vector.
integral_edges = []
for i in range(3):
    M = s.zeros(3)
    M[:2,:2] = L[i]
    M[2,2] = signs[i]//signs[(i+1)%3]
    assert M.det() == 1
    integral_edges.append(M)
assert reduce(lambda a,b:b*a,integral_edges,s.eye(3)) == s.eye(3)
u = -sum(n,s.zeros(2,1))
d = s.igcd(*list(u))
assert list(u) == [-2,2] and d == 2
print("Three-component outgoing angular vectors:", [list(v) for v in n])
print("Exact edge matrices:", [m.tolist() for m in L])
print("Actual contraction logarithms:", [list(v) for v in contractions])
print("Integral rank-three transitions:", [m.tolist() for m in integral_edges])
print("Cycle product: I_3")
print("Logarithmic monodromy vector u/(2*pi*i):", list(u))
print("Primitive divisor d:", d)

# The two independent normal-product constants span all affine
# translations, while every central elliptic base translation is fixed.
e0,e1,e2 = s.symbols("e0 e1 e2")
d0,d1,d2 = s.symbols("d0 d1 d2")
translation = sum((P[(i+1)%3]*s.Matrix([di,ei])
                   for i,(di,ei) in enumerate(zip((d0,d1,d2),(e0,e1,e2)))),
                  s.zeros(2,1))
adjusted = s.solve(list(translation), (e0,e1), dict=True)
assert len(adjusted) == 1
assert translation.subs(adjusted[0]) == s.zeros(2,1)
log_vector = sum((P[(i+1)%3]*s.Matrix([0,1]) for i in range(3)),
                 s.zeros(2,1))
assert log_vector == u
print("Exact affine translation:", list(translation))
print("Two-constant solution retaining d0,d1,d2:", adjusted[0])
print("Log-period vector agrees with minus the outgoing-meridian sum.")

def angular_basis(order, a, b):
    """Basis of Z^2+Z*(a,b)/order, using its actual integer image."""
    generators = s.Matrix([[order,0,a],[0,order,b]])
    return hermite_normal_form(generators)/order

def divisibility_in_lattice(v, basis):
    coefficients = basis.inv()*v
    assert all(x.q == 1 for x in coefficients)
    return abs(s.igcd(*[int(x) for x in coefficients]))

tests = 0
for order in range(1,25):
    for a in range(order):
        for b in range(order):
            if gcd(a,order) != 1 or gcd(b,order) != 1:
                continue
            basis = angular_basis(order,a,b)
            for repeat in range(1,7):
                # A 2*repeat cycle has outgoing vectors e1,-e2,
                # repeated, in the common minus-swap convention.
                v = repeat*s.Matrix([-1,1])
                actual = divisibility_in_lattice(v,basis)
                expected = repeat*gcd(order,a+b)
                assert actual == expected
                tests += 1
print("Repeated two-component secondary cycles checked by HNF:", tests)
print("Verified formula d = k*gcd(n,a+b) for a free mu_n action, 2k components.")
for order,a,b,repeat in [(1,0,0,3),(5,1,4,1),(5,1,4,3),(5,1,2,2)]:
    B = angular_basis(order,a,b)
    v = repeat*s.Matrix([-1,1])
    print("Secondary example (n,a,b,k) =", (order,a,b,repeat),
          "angular basis =", B.tolist(),
          "period coefficients =", list(B.inv()*v),
          "d =", divisibility_in_lattice(v,B))

# All three components in the explicit three-cycle remain smooth free
# secondary Hopf quotients exactly when a,b,a+b are units modulo n.
triple_tests = 0
for order in range(2,25):
    for a in range(order):
        for b in range(order):
            if not all(gcd(v,order)==1 for v in (a,b,a+b)):
                continue
            weights = [P_i.inv()*s.Matrix([a,b]) for P_i in P]
            assert all(gcd(int(v),order)==1 for pair in weights for v in pair)
            B = angular_basis(order,a,b)
            assert divisibility_in_lattice(u,B) == 2
            triple_tests += 1
B = angular_basis(5,1,2)
weights = [[int(v)%5 for v in P_i.inv()*s.Matrix([1,2])] for P_i in P]
print("Three-component free secondary cycles checked:", triple_tests)
print("Explicit mu_5 three-cycle weights:", weights,
      "actual angular basis:", B.tolist(),
      "period coefficients:", list(B.inv()*u),
      "primitive divisor:", divisibility_in_lattice(u,B))
print("PASS: all symbolic, integral, contraction, affine and finite-secondary checks.")
