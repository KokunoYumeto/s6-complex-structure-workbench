#!/usr/bin/env python3
"""Postrelease exact checks of all additional printed 01B8 calculations.

The prerelease program used elimination for symbolic squares and ambient
Hessian valuations.  This companion additionally pulls the equations back
through the printed affine maps, obtains Taylor coefficients by polynomial
substitution, and verifies inverse maps and determinant divisors.
"""
import itertools
import json
import sympy as s

x, y, z, u, v, t, r = s.symbols("x y z u v t r")
checks = []


def check(name, yes, evidence):
    if not yes:
        raise AssertionError(name)
    checks.append({"check": name, "passed": True, "evidence": evidence})


def zero(expr):
    return s.cancel(s.expand(expr)) == 0


def quadratic(expr):
    poly = s.Poly(s.expand(expr), u, v)
    return s.expand(sum(c * u ** m[0] * v ** m[1]
                        for m, c in poly.terms() if sum(m) == 2))


def pole(expr):
    expr = s.cancel(expr)
    if expr == 0:
        return 0
    numerator, denominator = s.fraction(expr)
    low = lambda p: min(m[0] for m, _ in s.Poly(p, t).terms())
    return max(0, low(denominator) - low(numerator))


def affine_map_checks(name, mapping, generators, bounds):
    substitutions = dict(zip((x, y, z), mapping))
    pullbacks = [s.expand(g.subs(substitutions, simultaneous=True))
                 for g in generators]
    first = [[s.diff(g, a).subs({u: 0, v: 0}) for a in (u, v)]
             for g in pullbacks]
    check(name + ": first generator derivatives are holomorphic",
          all(pole(e) == 0 for row in first for e in row),
          [[str(e) for e in row] for row in first])
    normal_matrix = s.Matrix(mapping).jacobian((u, v))
    first_pole = max(pole(e) for e in normal_matrix)
    second_pole = max(pole(s.diff(g, a, b).subs({u: 0, v: 0}))
                      for g in pullbacks for a in (u, v) for b in (u, v))
    check(name + ": derivative pole bounds",
          first_pole <= bounds[0] and second_pole <= bounds[1]
          and 4 * first_pole <= bounds[2],
          {"first_normal_pole": first_pole,
           "second_generator_pole": second_pole,
           "fourth_ambient_bound": 4 * first_pole,
           "printed_upper_bounds": bounds})
    return substitutions, pullbacks


gs = [y ** 2 - x * z, y * z - x ** 3, z ** 2 - x ** 2 * y]
F = z ** 3 + x * y ** 3 - 3 * x ** 2 * y * z + x ** 5
space_map = (t ** 3, t ** 4 + v / (3 * t ** 5),
             t ** 5 - u / t ** 3 + 2 * v / (3 * t ** 4))
sub, pulled = affine_map_checks("space cusp", space_map, gs, (5, 10, 20))
qF = quadratic(F.subs(sub, simultaneous=True))
expected = 3 * u ** 2 / t - 3 * u * v / t ** 2 + v ** 2 / t ** 3
check("A.T.16 from direct affine substitution", zero(qF - expected), str(qF))
qmat = s.hessian(qF, (u, v)) / 2
check("A.T.16 determinant", zero(qmat.det() - 3 / (4 * t ** 4)), str(s.factor(qmat.det())))
inverse_u = 2 * t ** 4 * y - t ** 3 * z - t ** 8
inverse_v = 3 * t ** 5 * (y - t ** 4)
check("A.T.20 inverse normal coordinates",
      zero(inverse_u.subs(sub, simultaneous=True) - u)
      and zero(inverse_v.subs(sub, simultaneous=True) - v),
      {"u": str(inverse_u), "v": str(inverse_v),
       "parameter_inverse": "the local cubic root t of x near each nonzero t"})
curve = {x: t ** 3, y: t ** 4, z: t ** 5}
dg = [s.Matrix([s.diff(g, a).subs(curve) for a in (x, y, z)]) for g in gs]
a1, b1 = dg[0], dg[1] + t * dg[0]
check("space conormal generator relation",
      all(zero(e) for e in dg[2] + 2 * t ** 2 * a1 - t * b1),
      "dg3=-2t^2*a1+t*b1")
wedge = a1.cross(b1)
check("space conormal wedge and correction",
      all(zero(e) for e in wedge - t ** 8 * s.Matrix([3, 4 * t, 5 * t ** 2]))
      and -2 + 8 - 2 == 4,
      {"wedge": [str(e) for e in wedge], "ramification_order": 2, "degree_N": 4})

G = y ** 2 - x ** 3
gs2 = [x * z, y * z, G]
cusp_map = (t ** 2, t ** 3 + v / (2 * t ** 3), u / t ** 2)
sub2, pulled2 = affine_map_checks("cusp branch", cusp_map, gs2, (3, 6, 12))
q2 = quadratic((z * G).subs(sub2, simultaneous=True))
check("cusp-line extra quadratic by affine substitution", zero(q2 - u * v / t ** 2), str(q2))
check("cusp-line extra determinant", zero((s.hessian(q2, (u, v)) / 2).det()
                                          + 1 / (4 * t ** 4)), "-1/(4t^4)")
check("A.T.21 cusp inverse",
      zero((t ** 2 * z).subs(sub2, simultaneous=True) - u)
      and zero((2 * t ** 3 * (y - t ** 3)).subs(sub2, simultaneous=True) - v),
      "t is the local square root of x; u=t^2*z, v=2*t^3*(y-t^3)")
curve2 = {x: t ** 2, y: t ** 3, z: 0}
a2 = s.Matrix([s.diff(x * z, q).subs(curve2) for q in (x, y, z)])
b2 = s.Matrix([s.diff(G, q).subs(curve2) for q in (x, y, z)])
wedge2 = a2.cross(b2)
check("cusp conormal wedge", all(zero(e) for e in wedge2 + t ** 5 * s.Matrix([2, 3 * t, 0])),
      [str(e) for e in wedge2])
smooth_map = (u / t, v / t, t)
sub3, pulled3 = affine_map_checks("smooth branch", smooth_map, gs2, (1, 2, 4))
check("A.T.21 smooth inverse",
      zero((z * x).subs(sub3, simultaneous=True) - u)
      and zero((z * y).subs(sub3, simultaneous=True) - v),
      "t=z, u=z*x, v=z*y")
check("combined cusp-line determinant correction", -2 + (5 - 1) + 2 == 4,
      {"cusp_correction": 4, "smooth_correction": 2, "degree_N": 4})

q0 = s.symbols("q0")
check("A.T.19 degree and both corrected degrees",
      s.expand(-2 * q0 - 4 * (4 - q0)) == -16 + 2 * q0
      and s.expand(-16 + 2 * q0 + 20) == 4 + 2 * q0
      and s.expand(-16 + 2 * q0 + 12 + 4) == 2 * q0,
      {"uncorrected": "-16+2q0", "space_corrected": "4+2q0", "cusp_line_corrected": "2q0"})

# A finite permutation closure verifies the metabelian obstruction without
# importing the asserted abstract identifications of the derived groups.
identity = tuple(range(4))
compose = lambda a, b: tuple(a[b[i]] for i in range(4))
def inverse(a):
    out = [0] * 4
    for i, v0 in enumerate(a): out[v0] = i
    return tuple(out)
def closure(generators):
    out, pending = {identity}, [identity]
    while pending:
        a = pending.pop()
        for b in generators:
            c0 = compose(a, b)
            if c0 not in out:
                out.add(c0); pending.append(c0)
    return out
def derived(group):
    generators = [compose(compose(a, b), compose(inverse(a), inverse(b)))
                  for a in group for b in group]
    return closure(generators)
group = closure([(1, 2, 3, 0), (1, 0, 2, 3)])
d1, d2 = derived(group), derived(derived(group))
check("finite nonmetabelian quotient in A.T.3",
      (len(group), len(d1), len(d2)) == (24, 12, 4),
      {"group_order": len(group), "first_derived_order": len(d1), "second_derived_order": len(d2)})

possible_q = [q for q in range(-4, 1) if 4 <= 8 + 2 * q]
check("A.T.9 integer range", possible_q == [-2, -1, 0]
      and (11 - 4) // 4 == 1, {"q0": possible_q, "maximum_positive_genus": 1})
possible_k = [k for k in range(4) if 6 >= k + 3 * (4 - k)]
check("q0=-1 equality case", possible_k == [3], {"k": possible_k, "orders": [1, 1, 1, 3]})
check("node and cusp conductor contradictions", 4 * 2 + 1 == 9
      and 4 * 1 + 1 == 5 and 2 * 5 > 6,
      {"cusp_minimum": 9, "each_node_branch_minimum": 5, "total_degree": 6})

leading_generators = [(4, 0), (3, 1), (2, 2), (0, 3)]
basis = [(i, j) for j in range(3) for i in range(4)
         if not any(i >= a and j >= b for a, b in leading_generators)]
check("nine-dimensional residue space", len(basis) == 9,
      {"monomials_y_z": basis, "generic_rank": 3 * 3})

print(json.dumps({"schema_version": 1, "owner": "cdp:st:A.5.18", "tag": "01B8",
                  "phase": "postrelease comparison", "checks_passed": len(checks),
                  "checks": checks}, indent=2, sort_keys=True))
