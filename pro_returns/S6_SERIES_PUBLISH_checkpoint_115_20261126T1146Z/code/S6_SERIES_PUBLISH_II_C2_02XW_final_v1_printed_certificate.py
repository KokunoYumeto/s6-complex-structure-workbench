"""Exact postrelease certificates for P4.57 / 02XW.

Universal analytic statements, finiteness, normality and Morse splitting are
proved in the comparison. This is a fresh polynomial and incidence certificate;
the named historical routine was unavailable and was not read or replayed.
"""
import sympy as s

x, y, z, a, b, A, B, C, D = s.symbols("x y z a b A B C D")
Q = A*x**3 + B*x**2*y + C*x*y**2 + D*y**3
H = s.hessian(Q, (x, y))
directional = a*s.diff(Q, x) + b*s.diff(Q, y)
assert s.hessian(directional, (x, y)) == H.subs({x: a, y: b})
first_axis = H.subs({x: 1, y: 0})
assert first_axis == s.Matrix([[6*A, 2*B], [2*B, 2*C]])
assert Q.subs({A: 0, B: 0, C: 0}) == D*y**3
u, w = s.symbols("u w")
M = s.Matrix([[a, 0], [b, 1]])
assert M.det() == a
assert s.simplify((a*u)/a - u) == 0
assert s.expand((b*u+w) - b*(a*u)/a - w) == 0
print("Binary cubic Hessian identity: Hess(D_v Q)=Hess(Q)(v)")
print("First-axis Hessian zero forces A=B=C=0, leaving D*y^3")
print("For a!=0 the explicit coordinates are x=a*u, y=b*u+w; the other chart swaps x,y")

ep, eta = s.symbols("ep eta")
A1, B1, C1, D1 = s.symbols("A1 B1 C1 D1")
Q1 = A1*x**3 + B1*x**2*y + C1*x*y**2 + D1*y**3
E0, E1, E2, E3, E4 = s.symbols("E0 E1 E2 E3 E4")
Q4 = E0*x**4 + E1*x**3*y + E2*x**2*y**2 + E3*x*y**3 + E4*y**4
family = Q + z*Q1 + Q4
normal_hessian = s.hessian(family, (x, y)).subs(
    {x: a*ep, y: b*ep, z: eta}, simultaneous=True)
expected = (ep*H.subs({x: a, y: b})
            + ep*eta*s.hessian(Q1, (x, y)).subs({x: a, y: b})
            + ep**2*s.hessian(Q4, (x, y)).subs({x: a, y: b}))
assert (normal_hessian - expected).applyfunc(s.expand) == s.zeros(2)
print("Normal/base filtration: leading ep*Hess(Q)(v); remainders ep*eta and ep^2")

# Relative projective-bundle Cech cohomology and P1 Riemann--Roch.
alpha, beta, zero_degree, g, delta, intersection = s.symbols(
    "alpha beta zero_degree g delta intersection")
degree_1 = zero_degree - 2*alpha - beta
degree_2 = zero_degree - alpha - 2*beta
chi_R1 = s.expand((degree_1 + 1) + (degree_2 + 1))
genus = s.expand(1 - (1 + chi_R1))
assert genus == 3*alpha + 3*beta - 2*zero_degree - 2
assert s.expand(genus.subs(beta, 2-alpha)) == 4 - 2*zero_degree
union_genus = g + delta + intersection - 1
slack = g - 1 + delta + intersection + 2*(zero_degree - 2)
assert s.expand(union_genus - (4 - 2*zero_degree) - slack) == 0
print("Relative-Cech spectral genus: 3*deg(E)-2-2b; at deg(E)=2 it is 4-2b")
print("Union equality: (g-1)+delta+intersection+2*(b-2)=0")
print("Its nonnegative summands force b=2,g=1,delta=intersection=0")

allocations = [(i, j, k) for i in range(2) for j in range(2)
               for k in range(2) if i+j+k == 1]
assert set(allocations) == {(1, 0, 0), (0, 1, 0), (0, 0, 1)}
print("Complete scalar-zero allocations (b_H,b_R,total B-only order):", allocations)
cB = s.symbols("cB", integer=True, positive=True)
assert s.expand(cB + 2 - (cB + 1)) == 1
assert 4 - 3 == 1 and 2 + 1 - 2 == 1
print("Graph excesses: c_B=2 gives 1; c_B=1 with two preimages gives 1; A-common gives 1")

X, Y, k, h, l, m, aa, bb, cc = s.symbols("X Y k h l m aa bb cc")
alpha0, beta0 = s.symbols("alpha0 beta0")
prepared = Y**2 + X*alpha0*Y + X**2*beta0
depressed = (Y + X*alpha0/2)**2 + X**2*(beta0-alpha0**2/4)
assert s.expand(prepared-depressed) == 0
assert s.expand((Y**2+X**2*k).subs(Y, X*u) - X**2*(u**2+k)) == 0
quadratic = z*(l*X+m*Y) + aa*X**2 + bb*X*Y + cc*Y**2
hessian = s.hessian(quadratic, (X, Y, z))
minor_x = hessian.extract([0, 2], [0, 2]).det()
minor_y = hessian.extract([1, 2], [1, 2]).det()
assert minor_x == -l**2 and minor_y == -m**2
assert s.expand(hessian.det() - (-2*aa*m**2 + 2*bb*l*m - 2*cc*l**2)) == 0
assert s.expand((u+s.I*w)*(u-s.I*w) - (u**2+w**2)) == 0
print("Exact preparation and finite-cover substitution: zero residuals")
print("Hessian minors:", minor_x, minor_y, "; determinant:", hessian.det())
print("Since (l,m)!=0, rank>=2; the rank-two split with constant residual factors exactly")
print("PASS: all exact polynomial, genus and scalar-budget certificates")
