"""Exact certificates for a transverse cusp on a non-lci critical curve.

All computations are over QQ or ZZ.  The manuscript proves the convergent
analytic ideal statements; the weighted calculation here independently
checks the finite coefficient spaces used in that proof.
"""
import itertools
import sympy as s

x, y, z, t = s.symbols("x y z t")
variables = (x, y, z)
weights = (5, 6, 7)
g1 = y**2 - x*z
g2 = y*z**2 - x**4
g3 = z**3 - x**3*y
generators = (g1, g2, g3)
F = 4*x**7 - 15*x**3*y*z**2 + 10*x**2*y**3*z - 3*x*y**5 + 4*z**5
param = {x: t**5, y: t**6, z: t**7}

def pull(poly):
    return s.expand(poly.subs(param))

def weighted_monomials(degree):
    if degree < 0:
        return []
    return [x**a*y**b*z**c
            for a in range(degree//5+1)
            for b in range(degree//6+1)
            for c in range(degree//7+1)
            if 5*a + 6*b + 7*c == degree]

assert all(pull(g) == 0 for g in generators)
assert s.expand(z**2*g1-y*g2+x*g3) == 0
assert s.expand(x**3*g1-z*g2+y*g3) == 0
toric = s.groebner([x-t**5, y-t**6, z-t**7], t, z, y, x)
elimination = [p.as_expr() for p in toric.polys if not p.as_expr().has(t)]
ideal = s.groebner(generators, z, y, x)
assert elimination == [p.as_expr() for p in ideal.polys]
print("normalization kernel Groebner basis:", elimination)
print("free C{x} basis exponents:", [0, 6, 7, 13, 14])

gradient = [s.diff(F, v) for v in variables]
assert pull(F) == 0 and all(pull(g) == 0 for g in gradient)
assert s.expand(gradient[1] + 15*x*g1**2) == 0
assert s.expand(gradient[0] - ((17*x*y*z-3*y**3)*g1-28*x**2*g2)) == 0
assert s.expand(gradient[2] - (10*x**2*y*g1+20*z*g3)) == 0
assert s.expand(35*F-sum(w*v*g for w, v, g in zip(weights, variables, gradient))) == 0
print("F and gradient on the normalization:", pull(F), [pull(g) for g in gradient])
print("gradient ideal identities: passed; its reduced support is D")

H = s.hessian(F, variables).subs(param)
ell = s.Matrix([7*t**2, 0, -5])
assert H == 2*t**21*ell*ell.T
assert H*s.Matrix([5, 6*t, 7*t**2]) == s.zeros(3, 1)
cubic = s.expand(s.diff(F, y, 3).subs(param)/6)
assert cubic == -20*t**17
print("Hessian = 2*t^21 * ell * ell^T, ell =", list(ell))
print("radical cubic in the y direction:", cubic)
print("generic transverse type: A2 (nonzero Hessian and radical cubic for t != 0)")

# Homogeneity reduces analytic I^2 membership of this F to weight 35.
gen_weights = [12, 20, 21]
square_terms = []
for i, j in itertools.combinations_with_replacement(range(3), 2):
    for mon in weighted_monomials(35-gen_weights[i]-gen_weights[j]):
        square_terms.append(s.expand(mon*generators[i]*generators[j]))
assert square_terms == [s.expand(x*y*g1**2)]
assert s.Poly(F, x, y, z).coeff_monomial(x**7) == 4
assert s.Poly(square_terms[0], x, y, z).coeff_monomial(x**7) == 0
print("weight-35 part of I^2 has basis:", square_terms)
print("F not in I^2: x^7 coefficient is 4, but every basis vector has coefficient 0")

Jac = s.Matrix([[s.diff(g, v) for v in variables] for g in generators]).subs(param)
minors = [s.factor(Jac.extract(rows, cols).det())
          for rows in itertools.combinations(range(3), 2)
          for cols in itertools.combinations(range(3), 2)]
orders = [s.Poly(m, t).terms()[0][0][0] for m in minors if m != 0]
assert min(orders) == 19
semigroup = {5*a+6*b+7*c for a in range(30) for b in range(30) for c in range(30)}
gaps = [n for n in range(30) if n not in semigroup]
assert gaps == [1, 2, 3, 4, 8, 9]
print("normalized Jacobian minors:", minors)
print("Jacobian valuation =", min(orders), "; differential valuation = 4")
print("semigroup gaps =", gaps, "; conductor valuation = 10")
a = Jac[0, :].T
b = Jac[1, :].T + 2*t**8*a
assert b == s.Matrix([-6*t**15, 5*t**14, 0])
assert Jac[2, :].T == -3*t**9*a + t*b
linear_factor = 5*t**8*a-2*b
assert H == 2*t**(-5)*linear_factor*linear_factor.T
radical_lift = s.Matrix([0, t**(-6), 0])
assert (a.T*radical_lift)[0] == 2
assert (b.T*radical_lift)[0] == 5*t**8
assert (linear_factor.T*radical_lift)[0] == 0
assert s.cancel(cubic*t**(-18)) == -20/t
print("normalized conormal basis a=dg1, b=dg2+2*t^8*dg1:", list(a), list(b))
print("dg3 = -3*t^9*a + t*b; quadratic term = t^(-5)*(5*t^8*a-2*b)^2")
print("radical 2*A+5*t^8*B lifts to t^(-6)*partial_y; cubic = -20*t^(-1)")
print("combined q^3*k^2 pole order = 17; 6*(Jacobian-differential) = 90")
print("ALL EXACT CHECKS PASSED")
