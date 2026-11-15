"""Exact divisor budgets and the local coordinate calculation in A.5.18."""
from itertools import product
import sympy as sp

q, delta = sp.symbols('q delta', integer=True)
c = 2*delta
r = -2+c-q
assert sp.expand(-2*q-4*r+4*c) == 8+2*q
print('Cleared discriminant degree = -2q - 4(-2+2delta-q) + 8delta = 8+2q.')

survivors = set()
for genus in range(1, 31):
    for qq in range(-50, 1):
        for ss in range(4):
            branch = 2*genus+2
            if branch <= 8+2*qq and branch <= -2*qq+ss:
                survivors.add((genus, qq))
assert survivors == {(1,-2), (1,-1)}
print('Integer cases before local obstructions:', sorted(survivors))

remaining = []
for qq in (-2,-1,0):
    for singular_branch in range(4):
        smooth_branch = 4-singular_branch
        if smooth_branch <= -2*qq and 3*smooth_branch+singular_branch <= 8+2*qq:
            remaining.append((qq,singular_branch,smooth_branch))
assert remaining == [(-1,3,1)]
print('After forbidding a smooth simple discriminant zero:', remaining)
assert 4*2+1 > 6
assert 2*(4*1+1) > 6
print('Cusp unit order >=9; node two-unit order >=10; both exceed the remaining degree6.')

# Polynomial representatives exercise the exact divisibilities underlying
# the analytic normal form. No truncation is used in the two ideal tests.
x, X, y, z, Z = sp.symbols('x X y z Z')
tests = 0
for aa, bb, cc in product((1,2), repeat=3):
    a = z
    b = z*(aa+bb*z)
    A = aa + x + y*z
    B = bb + z + x*y
    C = cc + x*z + y
    E = 1 + y + z + x
    f = a*x**2+x**2*(x*A+y*B)+x*y**2*b+x*y**3*C+y**4*E
    shifted = sp.Poly(sp.expand(f.subs(x, X-b*y**2/(2*a))), X)
    f0 = shifted.nth(0)
    f1 = shifted.nth(1)
    C1 = sp.cancel(f0/y**4)
    B1 = sp.cancel(f1/y**3)
    assert sp.denom(C1).is_number and sp.denom(B1).is_number
    assert sp.simplify(C1.subs({y:0,z:0})) == 1
    # For Y=y C1^(1/4)+X B1/(4 C1^(3/4)), its coefficients
    # of X^0 and X^1 are exactly y^4 C1 and y^3 B1.
    U,V=sp.symbols('U V', nonzero=True)
    trial=sp.Poly(sp.expand((y*U+X*V)**4),X)
    assert trial.nth(0)==y**4*U**4
    assert trial.nth(1)==4*y**3*U**3*V
    # H(0,0,z) is the unchanged quadratic coefficient a(z).
    assert shifted.nth(2).subs(y,0)==a
    tests += 1
print(f'Exact X-shift and fourth-power ideal divisibilities checked in {tests} polynomial families.')

# The equality germ is precisely an instance of A.5.15.
normal_form = y**4 + X**2*Z
assert sp.expand(normal_form.subs(Z,-z)) == y**4-X**2*z
print('Final equation Y^4+X^2 Z is Hirzebruch (a,b,c)=(4,2,1).')
genus_zero_nonlci=[qq for qq in range(-20,1) if 2<=4+2*qq and 2<=-2*qq+1]
assert genus_zero_nonlci==[-1]
print('Space-cusp connected genus-zero double cover forces q=-1 and two simple discriminant zeros; one must be smooth and is forbidden.')
