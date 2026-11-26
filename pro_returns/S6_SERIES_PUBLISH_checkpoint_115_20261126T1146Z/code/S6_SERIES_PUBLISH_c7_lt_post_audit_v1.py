"""Read every retained historical JSON field and check it by fresh orbit maps."""
from pathlib import Path
from itertools import product
from math import gcd
from functools import reduce
from datetime import datetime, timezone
import importlib.util
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_invariant_chern_receiving"
P = "S6_SERIES_PUBLISH_III_02LT_"
spec = importlib.util.spec_from_file_location(
    "lt_fresh_orbit_maps", ROOT / "code/S6_SERIES_PUBLISH_c7_lt_invariant_cone_v1.py")
F = importlib.util.module_from_spec(spec)
spec.loader.exec_module(F)


def cone_check(lengths, values):
    p, c, at = [], [], 0
    for length, value in zip(lengths, values):
        p.extend(at + (i + 1) % length for i in range(length))
        c.extend([value] * length)
        at += length
    c = sp.Matrix(c)
    n, rho = len(c), len(lengths)
    cycles, R, S, I, K = F.orbit_matrices(p)
    A = F.perm_matrix(p) - sp.eye(n)
    X, Xi = F.kernel_row(list(c))
    H, Hi = F.kernel_row(values)
    g, h = F.gcd_all(c), F.gcd_all(l * v for l, v in zip(lengths, values))
    M = (Xi * A).col_join(c.T)
    free = (Hi * R * X).row_join(sp.zeros(H.cols, 1))
    tors = (-c.T * K * (sp.eye(n) - S * R) * X).row_join(sp.ones(1))
    Phi = free.col_join(tors)
    section = sp.diag(Xi * S * H, sp.ones(1))
    assert Phi * section == sp.eye(H.cols + 1)
    image = Phi * M
    assert image[:-1, :] == sp.zeros(H.cols, n)
    assert F.gcd_all(image[-1, :]) == h
    basis = sp.diag(X, sp.ones(1))
    error = basis * (sp.eye(X.cols + 1) - section * Phi)
    lift = K * error[:-1, :]
    assert A * lift == error[:-1, :] and c.T * lift == error[-1:, :]
    split = None
    if g:
        _, B, _ = F.row_completion(list(c))
        beta = B[:, 0]
        _, E, _ = F.row_completion([l * v for l, v in zip(lengths, values)])
        eta = I * E[:, 0]
        assert (c.T * beta)[0] == g and (c.T * eta)[0] == h
        assert A * eta == sp.zeros(n, 1)
        D = h // g
        # The finite-kernel generator in coker(A on ker c) is -A beta.
        generator = -A * beta
        assert A * (eta - D * beta) == D * generator
        assert (c.T * (eta - D * beta))[0] == 0
        z = (sp.eye(n) - S * R) * X
        coordinate = -(c.T * K * z) / g
        assert all(x.q == 1 for x in coordinate)
        Csection = S * R * X + generator * coordinate
        preimage = K * z + beta * coordinate
        assert A * preimage == X - Csection
        assert c.T * preimage == sp.zeros(1, X.cols)
        image_generator = Phi * sp.Matrix.vstack(Xi * generator, sp.zeros(1, 1))
        assert image_generator[:-1, :] == sp.zeros(H.cols, 1)
        assert (int(image_generator[-1]) - g) % h == 0
        possible = [k for k in range(h) if k % g == 1 % g and (g * k) % h == 0]
        split = gcd(g, D) == 1
        assert bool(possible) == split
        if split:
            one, a, b = F.bezout(D, g)
            assert one == 1 and a * D + b * g == 1
            k = a * D
            assert k % g == 1 % g and (g * k) % h == 0
    return g, h, rho + 1 if not g else rho - 1, split


def component_maps(row, model):
    kind = row["type"]
    _, muf, pf, Cf, Bf, qf, order = model
    vertex = {
        "II": [0], "III": [0, 1], "IV": [0, 1, 2],
        "IV*": [0, 1, 4, 2, 5, 3, 6],
        "III*": [3, 2, 1, 0, 4, 5, 6, 7],
        "I1*": list(range(6)), "I3*": list(range(8)),
    }[kind]
    R = sp.zeros(len(vertex))
    for old, new in enumerate(vertex):
        R[new, old] = 1
    assert R * R.T == sp.eye(len(vertex))
    oldC, mu = -R.T * Cf * R, sp.Matrix(row["multiplicities"])
    j = row["component_class"]
    oldP = sp.Matrix(row["permutation_matrix"])
    assert R * mu == muf and oldC * mu == sp.zeros(len(mu), 1)
    assert R * oldP == F.perm_matrix(pf) ** j * R
    assert oldP.T * oldC * oldP == oldC
    orbits = F.cycles_of([next(i for i in range(oldP.rows) if oldP[i, k])
                         for k in range(oldP.cols)])
    assert orbits == row["orbits"]
    content = F.gcd_all(len(o) * mu[o[0]] for o in orbits)
    assert content == row["area_content"] == order // gcd(order, j)
    B = sp.Matrix(row["monodromy"])
    q = sp.Matrix(row["marked_cocycle"])
    z = sp.Matrix([sp.Rational(x) for x in row["marked_logarithm"]])
    assert (B - sp.eye(2)) * z == q == sp.Matrix([0, j])
    assert sp.ilcm(*(x.q for x in z)) == content
    period = {
        "II": sp.Matrix([[0, 1], [1, 0]]),
        "III": sp.diag(1, -1), "IV": sp.diag(-1, 1),
        "IV*": sp.diag(-1, 1), "III*": sp.diag(1, -1),
        "I1*": sp.eye(2), "I3*": sp.eye(2),
    }[kind]
    assert abs(period.det()) == 1 and period * B == Bf * period
    shift = (Bf - sp.eye(2)).inv() * (period * sp.Matrix([0, 1]) - qf)
    assert all(x.q == 1 for x in shift)
    assert period * z == j * ((Bf - sp.eye(2)).inv() * qf + shift)
    zero = next(i for i in range(len(mu)) if mu[i] == 1)
    generator_P = R.T * F.perm_matrix(pf) * R
    e0 = sp.eye(len(mu))[:, zero]
    generator = generator_P * e0 - e0
    rest = [i for i in range(len(mu)) if i != zero]
    if rest:
        minor = oldC.extract(rest, rest)
        assert minor.det() == order
        inverse = minor.inv()
        component_coordinate = inverse * generator.extract(rest, [0])
        assert sp.ilcm(*(x.q for x in component_coordinate)) == order
        if order > 1:
            k = next(k for k, x in enumerate(component_coordinate)
                     if gcd(int(order * x), order) == 1)
            unit = pow(int(order * component_coordinate[k]), -1, order)
            functional = unit * order * inverse[k, :]
            assert all(x.q == 1 for x in functional)
            assert int((functional * generator.extract(rest, [0]))[0]) % order == 1
        else:
            functional = sp.zeros(1, len(rest))
        # Exact inverse on the full component lattice: set the zero coefficient to 0.
        for i in rest:
            vector = sp.eye(len(mu))[:, i] - mu[i] * e0
            a = int((functional * vector.extract(rest, [0]))[0]) % order
            difference = vector - a * generator
            coefficients = inverse * difference.extract(rest, [0])
            assert all(x.q == 1 for x in coefficients)
            lift = sp.zeros(len(mu), 1)
            for k, i0 in enumerate(rest):
                lift[i0] = coefficients[k]
            assert oldC * lift == difference
        difference = oldP * e0 - e0 - j * generator
        coefficients = inverse * difference.extract(rest, [0])
        assert all(x.q == 1 for x in coefficients)
    else:
        functional = sp.zeros(1, 0)
        assert order == 1
    A = B - sp.eye(2)
    assert abs(A.det()) == order
    Ainv, e2 = A.inv(), sp.Matrix([0, 1])
    if order > 1:
        values = Ainv * e2
        k = next(k for k, x in enumerate(values) if gcd(int(order * x), order) == 1)
        unit = pow(int(order * values[k]), -1, order)
        torus_functional = unit * order * Ainv[k, :]
        assert all(x.q == 1 for x in torus_functional)
        assert int((torus_functional * e2)[0]) % order == 1
    else:
        torus_functional = sp.zeros(1, 2)
    for i in range(2):
        vector = sp.eye(2)[:, i]
        a = int((torus_functional * vector)[0]) % order
        coefficients = Ainv * (vector - a * e2)
        assert all(x.q == 1 for x in coefficients)
        assert A * coefficients == vector - a * e2
    return {
        "vertex_hist_to_fresh": vertex,
        "vertex_fresh_to_hist": [vertex.index(i) for i in range(len(vertex))],
        "period_H": period.tolist(), "period_H_inverse": period.inv().tolist(),
        "integer_log_shift": list(shift), "component_order": order,
        "component_functional_on_nonzero_vertices": list(functional),
        "torus_component_functional": list(torus_functional),
    }


print("START", datetime.now(timezone.utc).isoformat())
data = json.loads((LANE / (P + "historical_III_invariant_chern_cone_fresh.json")).read_text())
assert set(data) == {"status", "assertions", "counts", "sympy_version", "scope",
                     "cases", "multiplicity_cycles", "component_class_models"}
assert data["status"] == "PASS" and data["sympy_version"] == sp.__version__ == "1.14.0"
print("TOP", json.dumps({k: v for k, v in data.items() if not isinstance(v, list)}, separators=(",", ":")))
length_sets = [(1,), (2,), (3,), (1, 1), (1, 2), (2, 2), (1, 3), (2, 3), (1, 1, 2), (1, 2, 3)]
expected = [(l, c) for l in length_sets for c in product((-2, -1, 0, 1, 2), repeat=len(l))]
assert len(expected) == len(data["cases"]) == 390
zero = torsion = split_count = nonsplit_count = 0
for i, (row, (lengths, values)) in enumerate(zip(data["cases"], expected)):
    assert set(row) == {"lengths", "degrees", "g", "h", "H2_free_rank", "H2_torsion"}
    assert row["lengths"] == list(lengths) and row["degrees"] == list(values)
    g, h, free, split = cone_check(lengths, values)
    assert (g, h, free) == (row["g"], row["h"], row["H2_free_rank"])
    assert row["H2_torsion"] == ([h] if h > 1 else [])
    zero += (g == 0)
    torsion += (h > 1)
    split_count += (split is True)
    nonsplit_count += (split is False)
    print("CASE", i, json.dumps(row, separators=(",", ":")), "WANG_SPLIT", split)
area_expected = [(l, m) for l in [(1, 1), (1, 2), (2, 2), (1, 3), (2, 3), (3, 4)]
                 for m in product(range(1, 4), repeat=2)]
assert len(area_expected) == len(data["multiplicity_cycles"]) == 54
for i, (row, (lengths, mult)) in enumerate(zip(data["multiplicity_cycles"], area_expected)):
    assert set(row) == {"lengths", "mu", "degrees", "orbit_area", "content"}
    orbit = [l * m for l, m in zip(lengths, mult)]
    q = F.gcd_all(orbit)
    degrees = [orbit[1] // q] * lengths[0] + [-orbit[0] // q] * lengths[1]
    mu = [mult[0]] * lengths[0] + [mult[1]] * lengths[1]
    assert row == {"lengths": list(lengths), "mu": mu, "degrees": degrees,
                   "orbit_area": orbit, "content": q}
    assert sum(a * b for a, b in zip(mu, degrees)) == 0
    assert F.gcd_all(x // q for x in orbit) == 1
    print("AREA", i, json.dumps(row, separators=(",", ":")))
model_names = {"II": "II/q1", "III": "III/q2", "IV": "IV/q3",
               "IV*": "IVstar/q3", "III*": "IIIstar/q2",
               "I1*": "I1star/q4", "I3*": "I3star/q4"}
models = {m[0]: m for m in F.models()}
assert len(data["component_class_models"]) == 19
seen = []
for i, row in enumerate(data["component_class_models"]):
    assert set(row) == {"type", "component_class", "permutation_matrix", "multiplicities",
                       "orbits", "area_content", "monodromy", "marked_cocycle", "marked_logarithm"}
    seen.append((row["type"], row["component_class"]))
    maps = component_maps(row, models[model_names[row["type"]]])
    print("COMPONENT", i, json.dumps(row, separators=(",", ":")))
    print("EXACT_MAPS", i, json.dumps(maps, default=int, separators=(",", ":")))
assert seen == [(kind, j) for kind in model_names
                for j in range(models[model_names[kind]][-1])]
counts = {"models": 390, "nonzero_Chern": 390 - zero, "torsion_models": torsion,
          "zero_Chern": zero, "actual_additive_component_classes": 19}
assert counts == data["counts"]
assert 17 * (390 - zero) + 15 * zero + 2 * 54 + 6 * 7 + 3 * 19 == data["assertions"] == 6817
assert cone_check([1, 1], [2, -2]) == (2, 2, 1, True)
assert cone_check([2, 2, 1, 1], [2, -2, 0, 0]) == (2, 4, 3, False)
Cstar = models["I1star/q4"][3]
assert Cstar * sp.Matrix([0, 0, 2, 4, 3, 3]) == sp.Matrix([2, 2, 0, 0, -2, -2])
# In the product model, gamma wedge (mu + delta) has delta-gamma coefficient -1.
delta, gamma, meridian = sp.eye(3)[:, 0], sp.eye(3)[:, 1], sp.eye(3)[:, 2]
wedge = lambda x, y: sp.Matrix([x[i] * y[j] - x[j] * y[i] for i, j in ((0, 1), (0, 2), (1, 2))])
assert wedge(gamma, meridian + delta)[0] == -1
assert wedge(gamma, meridian - delta)[0] == 1
print("PASS COUNTS", json.dumps(counts), "ASSERTIONS", data["assertions"],
      "WANG_SPLIT_NONZERO", split_count, "WANG_NONSPLIT", nonsplit_count)
print("PASS EXACT_EXAMPLES III g=h=2 split; I1star g=2 h=4 nonsplit; c=0 normal=-t, inverse shear=+t")
print("PASS all stored JSON fields read through this bijective compact rendering and checked; no generic mixed torsion columns inferred")
print("END", datetime.now(timezone.utc).isoformat())
