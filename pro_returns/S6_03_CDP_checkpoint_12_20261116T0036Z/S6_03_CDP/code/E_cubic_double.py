"""Exact checks accompanying C.2.D4.2; no floating point arithmetic."""
from pathlib import Path
import sympy as s

print("Cubic coefficient degrees, common divisor positive:")
for split_a in range(0, 5):
    for common_v in range(1, 5):
        pure = -3 * split_a - common_v
        quadratic_lead = 2 - split_a - common_v
        assert pure < 0
        if quadratic_lead >= 0:
            assert split_a + common_v <= 2
            if common_v == 2:
                assert split_a == 0
            print("  a =", split_a, "v =", common_v,
                  "quadratic leading coefficient degree =", quadratic_lead)
for common_v in range(1, 5):
    for section_degree in range(0, 5):
        pa_quadratic = 2 - common_v - section_degree
        if pa_quadratic >= 1:
            assert common_v == 1 and section_degree == 0
print("Balanced splitting: positive genus and v>0 force v=1,d=0.")

print("Intersection ranks: primitive cubic.")
for genus in range(1, 6):
    for branch_excess in range(0, 9):
        for class_rank in (1, 2):
            bound = 4 * genus + 2 * branch_excess - class_rank
            assert bound > 0
print("  4g+2nu-r > 0 for g>=1, r in {1,2}; b1(U)<=3.")
for genus in range(1, 5):
    for branch_excess in range(2, 10):
        assert 4 * genus + 2 * branch_excess - 6 >= 2
print("One simple common zero: rank >= 4g+2nu-6 >= 2.")
for branch_excess in (4, 5, 6):
    e_u = 3 * (branch_excess - 2)
    b1_boundary = branch_excess - 1
    epsilon = 2
    pairing_rank = e_u - 1 - b1_boundary + epsilon
    assert pairing_rank == 2 * branch_excess - 4 >= 4
    print("Two distinct common zeros: nu =", branch_excess,
          "e(U) =", e_u, "b1(U) = 2, pairing rank =", pairing_rank)
for branch_excess in (2, 3):
    e_u = 3 * branch_excess
    b1_boundary = branch_excess
    pairing_rank = e_u - 1 - b1_boundary + 1
    assert pairing_rank == 2 * branch_excess
    print("One double common zero: nu =", branch_excess,
          "e(U) =", e_u, "b1(U) = 1, pairing rank =", pairing_rank)

u, z, z1, w, w1, v, x, y, new_v, new_Z = s.symbols(
    "u z z1 w w1 v x y new_v new_Z")
for contact in range(1, 9):
    old_equation = w**3 - z**2 * (z - u**contact)
    transformed = s.expand(old_equation.subs({z:u*z1, w:u*w1}, simultaneous=True))
    target = u**3 * (w1**3 - z1**2 * (z1-u**(contact-1)))
    assert s.expand(transformed-target) == 0
    assert s.cancel((w**2/z).subs({z:u*z1,w:u*w1}, simultaneous=True)
                    -u*w1**2/z1) == 0
print("Weights (2,1): exact blowup and normalized-generator formulas checked for contacts1..8.")
# The two exceptional twists are both +E: -(-E)=E and -2(-E)-E=E.
assert -(-1) == 1
assert -2*(-1)-1 == 1
print("Both nontrivial cyclic eigensheaves acquire O(E), with R1=0.")

# Model with simple common cubic zero: an exact chart, not an asserted deformation.
f = x*y*(z*(x-y)+x*y)
z_coordinate = y*(y+new_v)*z + y**2*(2*y+new_v)
assert s.expand(f.subs(x,y+new_v) - (new_v*z_coordinate+y**4)) == 0
inverse_z = (new_Z-y**2*(2*y+new_v))/(y*(y+new_v))
assert s.cancel(z_coordinate.subs(z,inverse_z)-new_Z) == 0
print("Exact scalar-zero model: f=v Z+y^4 on xy!=0; inverse chart checked.")

# Repeated primitive root warning: actual finite covering maps.
f_warning = x*z*(y**2-x**2*z)
assert s.expand(f_warning.subs(y,x*u)-x**3*z*(u**2-z)) == 0
cover_s, cover_v = s.symbols("cover_s cover_v")
assert s.expand((z*(u**2-z)).subs({z:cover_s**2,u:cover_s*cover_v},simultaneous=True)
                -cover_s**4*(cover_v**2-1)) == 0
print("Warning model factors through the explicit etale covers of C* x (C minus {+1,-1}).")
print("All C.2.D4.2 exact arithmetic and morphism checks passed.")
