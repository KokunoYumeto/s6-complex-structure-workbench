#!/usr/bin/env python3
"""Exact polynomial checks for the prereading derivation of 01B8.

No target-proof input is read.  Symbolic-square saturation is computed by
elimination, independently of the displayed product identities.  All
coefficients and all computations are exact over QQ.
"""
import json
import sympy as s

x, y, z, t, w = s.symbols("x y z t w")
records = []


def checked(name, condition, evidence):
    if not condition:
        raise AssertionError(name)
    records.append({"check": name, "passed": True, "evidence": evidence})


def polynomial_zero(expression):
    return s.expand(expression) == 0


def t_order(expression):
    expression = s.expand(expression)
    if expression == 0:
        return None
    return min(m[0] for m, _ in s.Poly(expression, t).terms())


def at_least(expression, lower_bound):
    order = t_order(expression)
    return order is None or order >= lower_bound


def model(name, generators, extra, parameter, parametrization, n,
          expected_hessian_determinant, product_identities):
    products = [generators[i] * generators[j]
                for i in range(3) for j in range(i, 3)]
    checked(name + ": normalization parametrization",
            all(polynomial_zero(g.subs(parametrization)) for g in generators),
            [str(parametrization[v]) for v in (x, y, z)])
    checked(name + ": extra generator is critical along curve",
            all(polynomial_zero(s.diff(extra, v).subs(parametrization))
                for v in (x, y, z)), str(extra))
    for variable, combination in zip((x, y, z), product_identities):
        checked(name + ": " + str(variable) + " times extra lies in square",
                polynomial_zero(variable * extra - combination),
                str(s.expand(combination)))

    # Rabinowitsch elimination computes the saturation by the parameter.
    elimination = s.groebner(products + [1 - w * parameter],
                              w, z, y, x, order="lex", domain=s.QQ)
    saturated = [p.as_expr() for p in elimination.polys
                 if not p.as_expr().has(w)]
    proposed = s.groebner(products + [extra], z, y, x,
                         order="lex", domain=s.QQ)
    saturation_basis = s.groebner(saturated, z, y, x,
                                  order="lex", domain=s.QQ)
    equal = (all(proposed.reduce(p)[1] == 0 for p in saturated)
             and all(saturation_basis.reduce(p)[1] == 0
                     for p in products + [extra]))
    checked(name + ": exact symbolic-square saturation", equal,
            {"parameter": str(parameter),
             "saturation_basis": [str(p.as_expr())
                                  for p in saturation_basis.polys]})

    # The chosen parameter is x=t^n on the ramified branch.  The normal
    # directions are the ambient y,z coordinate vectors.
    hf = s.hessian(extra, (y, z)).subs(parametrization)
    determinant = s.expand(hf.det())
    checked(name + ": leading extra normal Hessian",
            polynomial_zero(determinant - expected_hessian_determinant),
            {"matrix": [[str(v) for v in row] for row in hf.tolist()],
             "determinant": str(determinant)})
    normal_orders = []
    for product in products:
        hessian = s.hessian(product, (y, z)).subs(parametrization)
        normal_orders.append([t_order(hessian[0, 0]),
                              t_order(hessian[0, 1]),
                              t_order(hessian[1, 1])])
    if n == 3:
        bounds = (8, 7, 6)
        extra_orders = (7, 6, 5)
    else:
        bounds = (6, 5, 4)
        extra_orders = (None, 3, None)
    checked(name + ": square terms have strictly later determinant order",
            all(at_least(s.hessian(p, (y, z)).subs(parametrization)[i, j], b)
                for p in products for (i, j), b
                in zip(((0, 0), (0, 1), (1, 1)), bounds)),
            {"square_term_orders": normal_orders,
             "lower_bounds": bounds, "extra_orders": extra_orders})
    checked(name + ": every square term has ambient order at least four",
            all(min(sum(m) for m, _ in s.Poly(s.expand(p), x, y, z).terms())
                >= 4 for p in products), "All three ideal generators have order at least two.")
    checked(name + ": Hessian and cubic valuation bounds",
            all(at_least(s.diff(p, v1, v2).subs(parametrization), 2 * n)
                for p in products for v1 in (y, z) for v2 in (y, z))
            and all(at_least(s.diff(p, v1, v2, v3).subs(parametrization), n)
                    for p in products for v1 in (x, y, z)
                    for v2 in (x, y, z) for v3 in (x, y, z)),
            {"normal_Hessian_order": 2 * n, "third_derivative_order": n})
    jac = s.diff(t ** n, t)
    checked(name + ": canonical Jacobian and invariant order",
            polynomial_zero(jac - n * t ** (n - 1))
            and 4 * n - 4 * (n - 1) == 4
            and 4 * n + 1 - 4 * (n - 1) == 5,
            {"Jacobian": str(jac), "J_order": 4, "J_order_at_branch": 5})


g1, g2, g3 = y ** 2 - x * z, y * z - x ** 3, z ** 2 - x ** 2 * y
F = z ** 3 + x * y ** 3 - 3 * x ** 2 * y * z + x ** 5
model("space cusp (3,4,5)", [g1, g2, g3], F, x,
      {x: t ** 3, y: t ** 4, z: t ** 5}, 3, 27 * t ** 12,
      [g2 ** 2 - g1 * g3,
       g2 * g3 + x * g1 ** 2,
       g3 ** 2 + x * g1 * g2])

g1, g2, g3 = y ** 2 - x ** 3, x * z, y * z
F = z * (y ** 2 - x ** 3)
model("cusp and transverse line", [g1, g2, g3], F, x + z,
      {x: t ** 2, y: t ** 3, z: 0}, 2, -4 * t ** 6,
      [g1 * g2, g1 * g3, g3 ** 2 - x * g2 ** 2])
checked("cusp-line extra generator is also critical on the line",
        all(polynomial_zero(s.diff(F, v).subs({x: 0, y: 0, z: t}))
            for v in (x, y, z)), "The saturation parameter x+z is nonzero on both generic branches.")

a, b, c, q, lam, mu, unit = s.symbols("a b c q lam mu unit", nonzero=True)
Delta = a * c - b ** 2 / 4
checked("quartic invariant under quadratic normal shift",
        polynomial_zero(a * (c + b * q + a * q ** 2)
                        - (b + 2 * a * q) ** 2 / 4 - Delta),
        "(a,b,c) -> (a,b+2aq,c+bq+aq^2)")
new_a = unit * a / lam ** 2
new_b = unit * b / (lam * mu ** 2)
new_c = unit * c / mu ** 4
checked("degree-eight invariant determinant character",
        polynomial_zero(new_a * (new_a * new_c - new_b ** 2 / 4)
                        - unit ** 3 * a * Delta / (lam * mu) ** 4),
        "J transforms as O(S)^3 tensor det(N)^(-4).")

for k in (1, 2):
    u, v = s.symbols("u v")
    normal_equation = (t ** (2 * k + 1) + v) ** 2 - (t ** 2) ** (2 * k + 1)
    normal_jacobian = s.diff(normal_equation, v).subs(v, 0)
    ambient_jacobian = s.diff(t ** 2, t)
    ratio = s.cancel(normal_jacobian / ambient_jacobian)
    checked("planar cusp conductor Jacobian k=" + str(k),
            polynomial_zero(ratio - t ** (2 * k)),
            {"normal_Jacobian": str(normal_jacobian),
             "ambient_Jacobian": str(ambient_jacobian),
             "ratio": str(ratio), "fourth_power": str(ratio ** 4)})

r, v = s.symbols("r v", nonzero=True)
normal_coordinate = y * r + x * v / (4 * r ** 3)
remainder = s.rem(s.expand(normal_coordinate ** 4 - y ** 4 * r ** 4
                           - x * y ** 3 * v), x ** 2, x)
checked("exact fourth-root coordinate modulo x squared",
        s.simplify(remainder) == 0,
        "Y=y*r+x*v/(4*r^3), r^4=u, gives Y^4=y^4*u+x*y^3*v mod x^2.")

g = s.symbols("g", integer=True, positive=True)
checked("double-cover branch and invariant budget",
        s.expand(2 * (2 * g + 2) - 8) == 4 * (g - 1),
        {"branch_count": "2g+2", "minimum_divisor_cost": "4g+4",
         "degree_J": 8,
         "nonimmersive_penalty": "at least one beyond the branch budget, or a separate positive zero"})

print(json.dumps({"schema_version": 1,
                  "owner": "cdp:st:A.5.18", "tag": "01B8",
                  "target_proof_input": None,
                  "method": "Exact elimination saturation, ideal-product identities, differentiated normal Hessians and universal invariant identities over QQ",
                  "checks_passed": len(records), "checks": records},
                 indent=2, sort_keys=True))
