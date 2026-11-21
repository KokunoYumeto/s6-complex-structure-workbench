"""Exact checks for C.2.UN.4; the universal proof is in the section text."""
import sympy as s

X, Y, Z = s.symbols("X Y Z")
quartic = X**4 + Y**4 + Z**4
partials = [s.diff(quartic, q) for q in (X, Y, Z)]
assert partials == [4*X**3, 4*Y**3, 4*Z**3]
line_polynomial = quartic.subs({X: 0, Z: 1})
assert s.gcd(line_polynomial, s.diff(line_polynomial, Y)) == 1
assert quartic.subs({X: 0, Y: 1, Z: 0}) == 1
degree = 4
genus = (degree-1)*(degree-2)//2
curve_euler = 2-2*genus
assert genus == 3 and curve_euler == -4
print("Fermat quartic: smooth by its partials, genus", genus)
print("Line intersection:", line_polynomial, "; derivative gcd = 1; no point at infinity")

r, u, v, w = s.symbols("r u v w")
for multiplicity in range(1, 13):
    point_chart = (r*u)**multiplicity
    curve_r_chart = point_chart
    curve_v_chart = s.expand(point_chart.subs(r, v*w))
    assert curve_r_chart == (r*u)**multiplicity
    assert curve_v_chart == u**multiplicity*v**multiplicity*w**multiplicity
print("Exact point/curve chart identities passed for multiplicities 1 through 12")
print("Universal second chart: r=v*w, t=(r*u)^m=(u*v*w)^m")

point_delta = (3-1)*1
curve_delta = (2-1)*curve_euler
negative_delta = point_delta + curve_delta
assert (point_delta, curve_delta, negative_delta) == (2, -4, -2)
point_betti = [0, 0, 1, 0, 1, 0, 0]
curve_betti = [0, 0, 1, 2*genus, 1, 0, 0]
negative_betti = [a+b for a, b in zip(point_betti, curve_betti)]
assert negative_betti == [0, 0, 2, 6, 2, 0, 0]
assert sum((-1)**i*b for i, b in enumerate(negative_betti)) == -2
print("Euler changes: point =", point_delta, ", curve =", curve_delta, ", pair =", negative_delta)
print("Integral free cohomology increments of the pair:", negative_betti)
zero_betti = [a+b for a, b in zip(point_betti, negative_betti)]
assert zero_betti == [0, 0, 3, 6, 3, 0, 0]
assert sum((-1)**i*b for i, b in enumerate(zero_betti)) == 0
print("Zero-Euler three-blowup refinement increments:", zero_betti,
      "; central component increment = 3")

number_checked = 0
for initial_half_euler in range(-20, 21):
    for target_half_euler in range(-20, 21):
        positive_steps = max(target_half_euler-initial_half_euler, 0)
        negative_steps = max(initial_half_euler-target_half_euler, 0)
        result = 2*initial_half_euler + 2*positive_steps - 2*negative_steps
        assert result == 2*target_half_euler
        number_checked += 1
print("Exact realization arithmetic passed for", number_checked, "initial/target pairs")
for initial_half_euler in (-5, -1, 0, 1, 5):
    positive_steps = max(-initial_half_euler, 0)
    negative_steps = max(initial_half_euler, 0)
    print("Zero-Euler refinement of e =", 2*initial_half_euler,
          ": point operations =", positive_steps,
          ", point-plus-quartic operations =", negative_steps)
print("All exact checks passed.")
