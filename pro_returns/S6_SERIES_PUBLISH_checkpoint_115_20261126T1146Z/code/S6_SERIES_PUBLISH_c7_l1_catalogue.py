#!/usr/bin/env python3
"""Fresh L1 catalogue, fixed lattices and graph constants from raw definitions.

Only the permitted 21-profile construction cache is read.  No L1 original,
prior pattern table/program, root finite-lattice code, or its outputs is read.
All reductions use elementary integer Euclidean operations implemented here.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product
from functools import reduce
from math import gcd
from hashlib import sha256
import csv
import io
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "agents/continuation7_iii_nonstar"
RAW = ROOT / "agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json"
ROWS = json.loads(RAW.read_text())["rows"]
PAIRS = list(combinations(range(4), 2))
J = [[0, 1], [-1, 0]]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def zeros(m, n):
    return [[0]*n for _ in range(m)]


def tr(A):
    return [list(x) for x in zip(*A)]


def mul(A, B):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*B)] for row in A]


def add(A, B):
    return [[x+y for x, y in zip(a, b)] for a, b in zip(A, B)]


def sub(A, B):
    return [[x-y for x, y in zip(a, b)] for a, b in zip(A, B)]


def scale(c, A):
    return [[c*x for x in row] for row in A]


def hstack(*matrices):
    return [sum((list(A[i]) for A in matrices), []) for i in range(len(matrices[0]))]


def vstack(*matrices):
    return sum(([list(row) for row in A] for A in matrices), [])


def cols(A, indices):
    return [[row[j] for j in indices] for row in A]


def inverse(A):
    n = len(A)
    W = [list(map(F, row))+list(map(F, e)) for row, e in zip(A, eye(n))]
    for k in range(n):
        p = next(i for i in range(k, n) if W[i][k])
        W[k], W[p] = W[p], W[k]
        pivot = W[k][k]
        W[k] = [x/pivot for x in W[k]]
        for i in range(n):
            if i != k:
                c = W[i][k]
                W[i] = [x-c*y for x, y in zip(W[i], W[k])]
    out = [row[n:] for row in W]
    assert mul(A, out) == eye(n) == mul(out, A)
    return out


def integral(A):
    assert all(F(x).denominator == 1 for row in A for x in row), A
    return [[int(x) for x in row] for row in A]


def smith(A):
    """Return D,U,V with D=U A V; every operation and inverse is integral."""
    a = [row[:] for row in A]
    m, n = len(a), len(a[0])
    U, V = eye(m), eye(n)
    def rowswap(i, j):
        a[i], a[j] = a[j], a[i]
        U[i], U[j] = U[j], U[i]
    def colswap(i, j):
        for B in (a, V):
            for row in B:
                row[i], row[j] = row[j], row[i]
    def rowadd(i, j, c):
        a[i] = [x+c*y for x, y in zip(a[i], a[j])]
        U[i] = [x+c*y for x, y in zip(U[i], U[j])]
    def coladd(i, j, c):
        for B in (a, V):
            for row in B:
                row[i] += c*row[j]
    for k in range(min(m, n)):
        nonzero = [(abs(a[i][j]), i, j) for i in range(k, m)
                   for j in range(k, n) if a[i][j]]
        if not nonzero:
            break
        _, i, j = min(nonzero)
        rowswap(k, i)
        colswap(k, j)
        while True:
            entry = next((i for i in range(k+1, m) if a[i][k]), None)
            if entry is not None:
                rowadd(entry, k, -(a[entry][k]//a[k][k]))
                if a[entry][k]:
                    rowswap(entry, k)
                continue
            entry = next((j for j in range(k+1, n) if a[k][j]), None)
            if entry is not None:
                coladd(entry, k, -(a[k][entry]//a[k][k]))
                if a[k][entry]:
                    colswap(entry, k)
                continue
            bad = next(((i, j) for i in range(k+1, m)
                        for j in range(k+1, n) if a[i][j] % a[k][k]), None)
            if bad is None:
                break
            rowadd(k, bad[0], 1)
        if a[k][k] < 0:
            a[k] = [-x for x in a[k]]
            U[k] = [-x for x in U[k]]
    assert mul(mul(U, A), V) == a
    diagonal = [a[i][i] for i in range(min(m, n)) if a[i][i]]
    assert all(diagonal[i+1] % diagonal[i] == 0 for i in range(len(diagonal)-1))
    assert all(a[i][j] == 0 for i in range(m) for j in range(n) if i != j)
    return diagonal, U, V


def fixed_basis(T):
    diagonal, _, V = smith(sub(T, eye(4)))
    V_inv = integral(inverse(V))
    K = cols(V, range(len(diagonal), 4))
    L = V_inv[len(diagonal):]
    delta = [[0], [0], [1], [0]]
    dcoords = mul(L, delta)
    diag, U, _ = smith(dcoords)
    assert diag == [1]
    K = mul(K, integral(inverse(U)))
    L = mul(U, L)
    assert mul(L, K) == eye(len(K[0]))
    assert cols(K, [0]) == delta
    assert mul(sub(T, eye(4)), K) == zeros(4, len(K[0]))
    return K, L


def wedge(A):
    return [[A[i][k]*A[j][l]-A[i][l]*A[j][k]
             for k, l in PAIRS] for i, j in PAIRS]


def xgcd(a, b):
    if b == 0:
        return abs(a), int(a >= 0)-int(a < 0), 0
    g, x, y = xgcd(b, a % b)
    return g, y, x-(a//b)*y


def bezout(values):
    coeff = []
    g = 0
    for value in values:
        new_g, u, v = xgcd(g, value)
        coeff = [u*x for x in coeff]+[v]
        g = new_g
    assert sum(x*y for x, y in zip(coeff, values)) == g
    return g, coeff


def multiplicative(typ):
    m = re.fullmatch(r"I(\d+)", typ)
    return int(m[1]) if m else None


def local_raw(typ, A, g):
    nu = multiplicative(typ)
    if nu is not None:
        N = sub(A, eye(2))
        c = next(list(x) for x in zip(*N) if any(x))
        content = gcd(*c)
        u = [x//content for x in c]
        if next(x for x in u if x) < 0:
            u = [-x for x in u]
        assert N == scale(nu, mul([[x] for x in u], mul([u], J)))
        one, x, y = xgcd(u[0], u[1])
        assert one == 1
        r = [-y, x]
        kappa = next(F(g[i], u[i]) for i in range(2) if u[i])
        assert kappa.denominator == 1 and g == [int(kappa)*x for x in u]
        z = [F(kappa, nu)*x for x in r]
        return {"nu": nu, "u": u, "r": r, "kappa": int(kappa), "z": z}
    z = [x[0] for x in mul(inverse(sub(A, eye(2))), [[x] for x in g])]
    return {"nu": None, "z": z}


def narrow(local, coefficient):
    return all((coefficient*x).denominator == 1 for x in local["z"])


def build_tuple(row, loc, a, b, selected):
    Ts = []
    for i, (A, g, local) in enumerate(zip(row["elliptic_matrices"],
                                         row["generator_section_cocycle"], loc)):
        beta = scale(-a, mul(mul([g], J), A))[0]
        zq = [b*x for x in local["z"]]
        w = F(1, loc[selected]["nu"]) if i == selected else 0
        central = sum(x*y for x, y in zip(beta, zq))+w
        T = eye(4)
        for j in range(2):
            T[j][:2] = A[j][:]
            T[j][3] = b*g[j]
        T[2][:2] = beta
        T[2][3] = central
        Ts.append(integral(T))
    assert reduce(mul, Ts, eye(4)) == eye(4)
    return Ts


def graph_certificate(Ts):
    N = len(Ts)
    D = hstack(*(sub(T, eye(4)) for T in Ts[:-1]))
    js = []
    for i in range(N-1):
        j = zeros(4*(N-1), 4)
        j[4*i:4*i+4] = eye(4)
        js.append(j)
    js.append(vstack(*(scale(-1, reduce(mul, Ts[i+1:-1], eye(4)))
                       for i in range(N-1))))
    bases = [fixed_basis(T) for T in Ts]
    Jcols = hstack(*(mul(j, K) for j, (K, _) in zip(js, bases)))
    assert mul(D, Jcols) == zeros(4, len(Jcols[0]))
    d, _, _ = smith(D)
    normal, U, V = smith(Jcols)
    assert len(d) == 3
    assert normal == [1]*(4*N-7)
    assert len(Jcols[0]) == len(normal)+1
    relation = sum(([1]+[0]*(len(K[0])-1) for K, _ in bases), [])
    assert mul(Jcols, [[x] for x in relation]) == zeros(len(Jcols), 1)
    return {"D": D, "fixed_bases": [K for K, _ in bases],
            "fixed_left_inverses": [L for _, L in bases],
            "normal_columns": Jcols, "normal_U": U, "normal_V": V,
            "delta_relation": relation}


def finite_certificate(A, g, local, T, a, b):
    zq = [b*x for x in local["z"]]
    gamma_index = reduce(lambda x, y: x*y//gcd(x, y),
                         (x.denominator for x in zq), 1)
    q = abs(sub(A, eye(2))[0][0]*sub(A, eye(2))[1][1]
            -sub(A, eye(2))[0][1]*sub(A, eye(2))[1][0])
    d = next(k for k in range(1, 13) if reduce(mul, [A]*k, eye(2)) == eye(2))
    assert d % gamma_index == 0
    answer = {"gamma_index": gamma_index, "monodromy_order": d, "component_order": q}
    if gamma_index != 1:
        return answer
    ell = [-int(zq[0]), -int(zq[1]), 0, 1]
    B = eye(4)
    for i in range(4):
        B[i][3] = ell[i]
    R4 = mul(mul(integral(inverse(B)), T), B)
    R = [row[:3] for row in R4[:3]]
    assert R4 == [row+[0] for row in R]+[[0, 0, 0, 1]]
    rho = integral([[q*a*local["z"][1], -q*a*local["z"][0], q]])[0]
    assert mul([rho], R) == [rho]
    one, beta = bezout(rho)
    assert one == 1
    diag, _, _ = smith(sub(R, eye(3)))
    assert diag == [1, 1]
    pairs3 = list(combinations(range(3), 2))
    W = [[R[i][k]*R[j][l]-R[i][l]*R[j][k] for k, l in pairs3]
         for i, j in pairs3]
    assert smith(sub(W, eye(3)))[0] == [1, 1]
    norm = zeros(4, 4)
    power = eye(4)
    for _ in range(d):
        norm = add(norm, power)
        power = mul(power, T)
    assert power == eye(4)
    beta4 = beta+[0]
    assert mul(norm, [[x] for x in beta4]) == [[0], [0], [d//q], [0]]
    assert mul(norm, [[x] for x in ell]) == [[d*x] for x in ell]
    omega_beta_ell = a*(beta4[0]*ell[1]-beta4[1]*ell[0])-b*beta4[2]
    assert -omega_beta_ell == F(b, q)
    assert b % q == 0
    answer.update({"ell": ell, "B": B, "B_inverse": integral(inverse(B)),
                   "R": R, "rho": rho, "beta": beta4, "norm_d": norm,
                   "vertical_index": q, "minus_omega_beta_ell": b//q})
    return answer


def original_orbits(typ, local, b):
    nu = local["nu"]
    if nu is not None:
        return gcd(nu, b*local["kappa"])
    if typ == "II":
        return 1
    comp = {"III": 2, "IV": 3, "III*": 2, "IV*": 3}[typ]
    zero = narrow(local, b)
    return ({"III": 2, "IV": 3, "III*": 8, "IV*": 7}[typ] if zero
            else {"III": 1, "IV": 1, "III*": 5, "IV*": 3}[typ])


natural = []
minimal = []
spheres = []
counts = {}
for row in ROWS:
    loc = [local_raw(t, A, g) for t, A, g in
           zip(row["fibers"], row["elliptic_matrices"], row["generator_section_cocycle"])]
    denominator = 1/F(row["height_of_generator"])
    assert denominator.denominator == 1
    d0 = int(denominator)
    nonstar = not any(re.fullmatch(r"I\d+\*", t) for t in row["fibers"])
    profile_key = f"{row['OS']}/{row['profile']}"
    profile_natural = 0
    for selected, chosen in enumerate(loc):
        nu = chosen["nu"]
        if nu is None or d0 % nu:
            continue
        degree = d0//nu
        for a in range(1, degree+1):
            if degree % a:
                continue
            b = degree//a
            p, q = a*chosen["kappa"] % nu, b*chosen["kappa"] % nu
            if gcd(q, nu) != 1:
                continue
            degree_vector = [int(j == p)-int(j == 0)-int(j == (p-q) % nu)
                             +int(j == (-q) % nu) for j in range(nu)]
            matches = []
            for marker in range(nu):
                col = [-2*int(j == marker)+int(j == (marker-1) % nu)
                       +int(j == (marker+1) % nu) for j in range(nu)]
                if col == degree_vector:
                    matches.append(marker)
            if not matches:
                continue
            if any(i != selected and not (narrow(x, a) or narrow(x, b))
                   for i, x in enumerate(loc)):
                continue
            assert matches == [0] and gcd(a, b) == 1
            Ts = build_tuple(row, loc, a, b, selected)
            assert len(smith(hstack(*(sub(T, eye(4)) for T in Ts)))[0]) == 3
            record = {"OS": row["OS"], "profile": row["profile"],
                      "a": a, "b": b, "zero_index": selected+1,
                      "zero_type": row["fibers"][selected], "zero_component": 0,
                      "zero_kappa": chosen["kappa"], "T": Ts, "nonstar": nonstar}
            profile_natural += 1
            if not nonstar:
                natural.append(record)
                continue
            record["graph"] = graph_certificate(Ts)
            exterior = hstack(*(sub(wedge(T), eye(6)) for T in Ts))
            diag, U, V = smith(exterior)
            assert diag == [1]*5
            omega = [[a, 0, 0, 0, 0, -b]]
            assert mul(omega, exterior) == zeros(1, len(exterior[0]))
            record["fibre_quotient_U"] = U
            record["fibre_quotient_V"] = V
            record["omega"] = omega[0]
            additive = [i for i, x in enumerate(loc) if x["nu"] is None]
            finite = {i: finite_certificate(row["elliptic_matrices"][i],
                       row["generator_section_cocycle"][i], loc[i], Ts[i], a, b)
                      for i in additive}
            record["finite"] = finite
            natural.append(record)
            choices = []
            for i in additive:
                options = []
                if narrow(loc[i], a) and original_orbits(row["fibers"][i], loc[i], b) == 1:
                    options.append("original")
                if finite[i]["gamma_index"] == 1:
                    options.append("finite")
                choices.append(options)
            if any(not x for x in choices):
                continue
            for modes in product(*choices):
                fidx = [i for i, mode in zip(additive, modes) if mode == "finite"]
                oidx = [i for i, mode in zip(additive, modes) if mode == "original"]
                Q = reduce(lambda x, y: x*y,
                           (finite[i]["vertical_index"] for i in fidx), 1)
                assert b % Q == 0
                orders = [finite[i]["monodromy_order"] for i in fidx]
                eligible = len(fidx) <= 2 and all(gcd(x, y) == 1 for x, y in combinations(orders, 2))
                multi_choices = []
                for i, local in enumerate(loc):
                    if i != selected and local["nu"] is not None:
                        can_original = narrow(local, a) and original_orbits(row["fibers"][i], local, b) == 1
                        multi_choices.append({"index": i+1, "type": row["fibers"][i],
                                              "original_allowed": can_original,
                                              "primitive_Mumford_allowed": True})
                pattern = {k: record[k] for k in ["OS", "profile", "a", "b",
                           "zero_index", "zero_type", "zero_component", "zero_kappa"]}
                pattern.update({"finite_indices": [i+1 for i in fidx],
                                "original_additive_indices": [i+1 for i in oidx],
                                "finite_orders": orders, "Q_f": Q, "c": b//Q,
                                "simple_order_feasible": eligible,
                                "other_multiplicative_choices": multi_choices})
                minimal.append(pattern)
                if b == Q and eligible:
                    assert all(x["original_allowed"] for x in multi_choices)
                    spheres.append(pattern)
    counts[profile_key] = profile_natural

natural_counts = sum(counts.values())
nonstar_count = sum(x["nonstar"] for x in natural)
sphere_counts = {}
for p in spheres:
    key = f"{p['OS']}/{p['profile']}"
    sphere_counts[key] = sphere_counts.get(key, 0)+1
initial_keys = {(p["OS"], p["profile"], p["a"], p["b"], p["zero_index"], p["zero_component"])
                for p in spheres}
print("RAW INPUT SHA256", sha256(RAW.read_bytes()).hexdigest())
print("NATURAL ROWS", natural_counts, "NONSTAR ROWS", nonstar_count)
print("MINIMAL-FILLING PATTERNS", len(minimal), "SPHERE PATTERNS", len(spheres),
      "DISTINCT SPHERE INITIAL ROWS", len(initial_keys))
for key, n in counts.items():
    print("PROFILE", key, "natural", n, "sphere", sphere_counts.get(key, 0))
for index, p in enumerate(spheres, 1):
    print("SPHERE", index, f"{p['OS']}/{p['profile']}",
          f"a={p['a']}", f"b={p['b']}", f"zero={p['zero_index']}:{p['zero_type']}:C0",
          "finite="+",".join(map(str, p["finite_indices"])),
          "original="+",".join(map(str, p["original_additive_indices"])),
          "orders="+",".join(map(str, p["finite_orders"])))
assert natural_counts == 172 and nonstar_count == 148
assert len(spheres) == 59 and len(initial_keys) == 50
assert len([x for x in spheres if len(x["finite_indices"]) == 2]) == 1
assert all(x["OS"] == 49 and x["profile"] == "III"
           for x in spheres if len(x["finite_indices"]) == 2)
DEST.mkdir(exist_ok=True)
data = {"scope": "Fresh independent L1 construction-only enumeration and integer constants.",
        "raw_sha256": sha256(RAW.read_bytes()).hexdigest(),
        "natural": natural, "minimal_patterns": minimal, "sphere_patterns": spheres,
        "counts": counts, "sphere_counts": sphere_counts}
(DEST / "S6_SERIES_PUBLISH_III_02L1_fresh_catalogue.json").write_text(
    json.dumps(data, indent=2)+"\n", newline="\n")
buffer = io.StringIO(newline="")
fields = ["pattern", "OS", "profile", "a", "b", "zero_index", "zero_type",
          "zero_component", "finite_indices", "original_additive_indices",
          "finite_orders", "Q_f", "c", "other_multiplicative_choices"]
writer = csv.DictWriter(buffer, fields, lineterminator="\n")
writer.writeheader()
for i, pattern in enumerate(spheres, 1):
    out = {k: pattern[k] for k in fields if k != "pattern"}
    out["pattern"] = i
    for key in ["finite_indices", "original_additive_indices", "finite_orders",
                "other_multiplicative_choices"]:
        out[key] = json.dumps(out[key], separators=(",", ":"))
    writer.writerow(out)
(DEST / "S6_SERIES_PUBLISH_III_02L1_fresh_sphere_patterns.csv").write_text(
    buffer.getvalue(), newline="\n")
print("PASS all natural tuples; nonstar primitive graph bases and one delta relation;")
print("PASS primitive fibre quotients, fixed gamma indices, finite norms and exact pairings;")
print("PASS complete 59-pattern construction-only enumeration, with all 50 initial rows.")
