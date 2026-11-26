#!/usr/bin/env python3
"""Fresh LH complete 495/459 enumeration and full raw-fibre matrices.

Input: the new LH exterior/local maps, admitted raw defining row matrices,
and the admitted LD pattern list solely for a final set comparison.
No LH original, historical executable, or historical target table is read.
"""
from collections import Counter
from itertools import product
from math import gcd
from pathlib import Path
import json
import re
from sympy import Matrix, ZZ, eye, zeros
from sympy.matrices.normalforms import smith_normal_form
from S6_SERIES_PUBLISH_c7_lh_integral import integral, rows, exterior, wedge, kernel, smith

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_odd_weighted"
LD = ROOT/"agents/continuation7_iii_weighted_catalogue"
source = json.loads((LD/"S6_SERIES_PUBLISH_III_02LD_fresh_exterior_data.json").read_text())["rows"]
fresh = json.loads((LANE/"S6_SERIES_PUBLISH_III_02LH_fresh_local_data.json").read_text())
local = {(tuple(r["key"]), r["D"]): r for r in fresh["records"]}
FINITE = {"II": 6, "III": 4, "IV": 3, "III*": 4, "IV*": 3}
WEIGHTS = (1, 3, 5, 7, 15)
DELTA, GAMMA = eye(4)[:, 2], eye(4)[:, 3]
patterns, results, maps = [], [], []
totals, profiles, examples = Counter(), Counter(), []
graph_cache = {}


def snf(A):
    diagonal = smith_normal_form(integral(A), domain=ZZ)
    ds = [abs(int(diagonal[i, i])) for i in range(min(diagonal.shape)) if diagonal[i, i]]
    assert all(y % x == 0 for x, y in zip(ds, ds[1:]))
    return A.rows-len(ds), [x for x in ds if x > 1], ds


def graph_data(row, D, regular_count):
    cache_key = (tuple(row["key"]), D, regular_count)
    if cache_key in graph_cache:
        return graph_cache[cache_key]
    data = local[(tuple(row["key"]), D)]
    As = [Matrix(A) for A in data["matrices"]]+[eye(4)]*(regular_count+1)
    relation = Matrix.hstack(*((A-eye(4))[:3, :] for A in As[:-1]))
    K, KL = kernel(relation)
    N = len(As)
    insertions = []
    for i in range(N):
        J = zeros(4*(N-1), 4)
        if i < N-1:
            J[4*i:4*i+4, :] = eye(4)
        else:
            suffix = eye(4)
            for j in reversed(range(N-1)):
                J[4*j:4*j+4, :] = -suffix
                suffix = As[j]*suffix
        insertions.append(J)
    assert K.cols == 4*N-7
    graph_cache[cache_key] = (As, K, KL, insertions)
    return graph_cache[cache_key]


def boundary_matrix(row, choices, D, e, regular):
    data = local[(tuple(row["key"]), D)]
    As, K, KL, Js = graph_data(row, D, len(regular))
    n_original, target_rank = len(row["fibres"]), 6+K.cols
    columns = []
    logs, beta, L, component_domain = [], 0, 0, D
    for A in As:
        columns.append(Matrix.vstack(exterior(A)-eye(6), zeros(K.cols, 6)))

    def normal(site, m, power, h):
        A = As[site]
        assert A*power == power and A**h == eye(4) and m % h == 0
        norm = (m//h)*sum((A**j for j in range(h)), zeros(4, 4))
        assert gcd(m, *(int(x) for x in power)) == 1
        for j in range(4):
            sweep = norm[:, j]
            assert (A-eye(4))*sweep == zeros(4, 1)
            raw_edge = Js[site]*sweep
            assert K*(KL*raw_edge) == raw_edge
            columns.append(Matrix.vstack(-wedge(eye(4)[:, j], power), KL*raw_edge))
        edge = Js[site]*power
        assert K*(KL*edge) == edge
        columns.append(Matrix.vstack(zeros(6, 1), KL*edge))
        logs.append((m, int(power[3])))

    for i, (choice, info, kind) in enumerate(zip(choices, data["local"], row["fibres"])):
        q, residue = row["components"][i]
        a = row["key"][2]
        nonzero = a*residue % q != 0
        if choice == "F":
            h = FINITE[kind]
            # A primitive invariant delta and m=h^2 are always free:
            # projected-coordinate content divides h, so h divides m/t.
            normal(i, h*h, DELTA, h)
            continue
        F = Matrix(info["fixed"])
        edge = Js[i]*F
        assert K*(KL*edge) == edge
        columns.append(Matrix.vstack(zeros(6, F.cols), KL*edge))
        kernel_name = "original_nonzero" if choice == "O" and nonzero else "ordinary"
        Ki = Matrix(info["kernels"][kernel_name]["kernel"])
        columns.append(Matrix.vstack(Ki, zeros(K.cols, Ki.cols)))
        if choice == "C":
            continue
        if choice == "O" and nonzero:
            defect = len(info["component_multiplicities"])-2
            beta += defect
            L += 1
            component_domain += defect+2
        elif re.fullmatch(r"I\d+", kind):
            n = info.get("rank_one_components", 1)
            beta += n-1
            component_domain += n
        else:
            rho = len(info["component_orbits"])
            beta += rho-1
            component_domain += rho
    for j, (m, power) in enumerate(regular):
        normal(n_original+j, m, power, 1)
    # The last identity site is the actual order-one clutch, even at e=0.
    normal(len(As)-1, 1, -e*GAMMA, 1)
    assert logs[-1] == (1, -e)
    actual_logs = logs[:-1]
    B = Matrix.hstack(*columns)
    assert B.rows == target_rank
    seifert = zeros(len(actual_logs)+1, len(actual_logs)+1)
    for i, (m, mu) in enumerate(actual_logs):
        seifert[i, 0] = -mu
        seifert[i, i+1] = m
    seifert[-1, 0] = -e
    for i in range(len(actual_logs)):
        seifert[-1, i+1] = 1
    r, A1, _ = snf(seifert)
    assert r in (0, 1)
    free, torsion, diagonals = snf(B)
    assert free == (r if L == 0 else 0), (row["key"], choices, D, e, free, r, L)
    unfilled = sum(c != "F" for c in choices)
    assert component_domain == D+(unfilled-1)+beta+L
    bridge = component_domain-(unfilled-r)
    assert bridge == D-1+beta+L+r
    b2 = free+bridge
    b3 = 2*b2+2-2*r-2*D
    assert b2 == (D-1+beta+2*r if not L else D-1+beta+L+r)
    assert b3 == (2*beta+2*r if not L else 2*beta+2*L)
    assert 2-2*r+2*b2-b3 == 2*D
    g = data["g"]
    free_quotient = Matrix(data["fibre_quotient"])[0, :]
    projection = zeros(1+K.cols, target_rank)
    projection[0, :6] = free_quotient
    projection[1:, 6:] = eye(K.cols)
    reduced_free, reduced_torsion, _ = snf(projection*B)
    assert reduced_free == free
    changed = reduced_torsion != torsion
    if changed and len(examples) < 18:
        examples.append({"key": row["key"], "choices": choices, "D": D, "g": g,
                         "e": e, "regular": len(regular), "full": torsion,
                         "discarded_fibre_torsion": reduced_torsion})
    return {
        "key": row["key"], "choices": choices, "D": D, "g": g, "e": e,
        "regular": [{"m": m, "power": rows(v)} for m, v in regular],
        "B": rows(B), "Seifert": rows(seifert), "B_smith_nonzero": diagonals,
        "T": torsion, "H1_free": r, "A1": A1, "beta": beta, "L": L,
        "bridge": bridge, "b2": b2, "b3": b3, "Euler": 2*D,
        "torsion_changes_if_fibre_torsion_discarded": changed,
    }, B


for row in source:
    key, selected = row["key"], row["key"][4]-1
    options = []
    for i, kind in enumerate(row["fibres"]):
        q, residue = row["components"][i]
        if i == selected:
            opts = ("C",)
        elif kind in FINITE:
            opts = ("O", "F")
        elif kind.endswith("*"):
            opts = ("O",)
        elif row["key"][2]*residue % q == 0:
            opts = ("M",)  # The zero-Chern original has the proved same kernel.
        else:
            opts = ("M", "O")
        options.append(opts)
    for choice_tuple in product(*options):
        choices = list(choice_tuple)
        all_star = all(c == "O" for c, kind in zip(choices, row["fibres"]) if kind.endswith("*"))
        projected = ["O" if kind in ("III*", "IV*") and c == "F" else c
                     for c, kind in zip(choices, row["fibres"])]
        patterns.append({"key": key, "choices": choices, "all_star_original": all_star,
                         "all_star_projection": projected})
        profiles[(key[0], key[1], "patterns")] += 1
        profiles[(key[0], key[1], "all_star")] += all_star
        for D in WEIGHTS:
            for e in (0, 1):
                rec, B = boundary_matrix(row, choices, D, e, [])
                assert rec["H1_free"] == 1-e
                results.append(rec)
                totals["full_matrices"] += 1
                totals["shared_full_matrices"] += rec["g"] > 1
                totals["torsion_changed"] += rec["torsion_changes_if_fibre_torsion_discarded"]
                totals["zero_Euler"] += e == 0
                totals["nonzero_Euler"] += e != 0
                if rec["g"] > 1 and e == 1 and len(maps) < 24:
                    diagonal, U, V, Ui, Vi, rank = smith(B)
                    maps.append({"key": key, "choices": choices, "D": D, "e": e,
                                 "diagonal": rows(diagonal), "left": rows(U),
                                 "right": rows(V), "left_inverse": rows(Ui),
                                 "right_inverse": rows(Vi)})
    # Extra complete-vector regular examples on every row; both Euler values.
    canonical_choices = [opts[0] for opts in options]
    regular = [(5, Matrix([2, -1, 3, 5])), (7, Matrix([-1, 1, -2, -7]))]
    for D in (3, 5, 7, 15):
        for e in (0, 1):
            rec, B = boundary_matrix(row, canonical_choices, D, e, regular)
            assert rec["H1_free"] == 1-e
            results.append(rec)
            totals["regular_full_vector_matrices"] += 1
            totals["torsion_changed"] += rec["torsion_changes_if_fibre_torsion_discarded"]

assert len(patterns) == 495
assert sum(p["all_star_original"] for p in patterns) == 459
new_set = {(tuple(p["key"]), tuple(p["choices"])) for p in patterns}
assert len(new_set) == 495
small_set = {(tuple(p["key"]), tuple(p["choices"])) for p in patterns if p["all_star_original"]}
for p in patterns:
    image = (tuple(p["key"]), tuple(p["all_star_projection"]))
    assert image in small_set
    if p["all_star_original"]:
        assert p["choices"] == p["all_star_projection"]
old = json.loads((LD/"S6_SERIES_PUBLISH_III_02LD_fresh_patterns.json").read_text())["patterns"]
assert new_set == {(tuple(p["key"]), tuple(p["choices"])) for p in old}
for os, profile in sorted({(p["key"][0], p["key"][1]) for p in patterns}):
    print("PROFILE", os, profile, "BROAD", profiles[(os, profile, "patterns")],
          "ALL_STAR_ORIGINAL", profiles[(os, profile, "all_star")])
print("PASS 495 distinct decorated kernel families; 459 all-star-original families; 36 explicitly retracted alternatives.")
print("PASS every broad family at weights 1,3,5,7,15, with BOTH zero and nonzero rational Euler values.")
print("PASS", totals["full_matrices"], "complete raw-fibre matrices;", totals["shared_full_matrices"], "with shared odd factors.")
print("PASS", totals["regular_full_vector_matrices"], "additional full-vector regular examples on all 172 rows.")
print("PASS every B corank, Seifert rank, component defect, bridge rank, Betti number, and Euler identity.")
print("PASS", len(maps), "complete reversible Smith certificates, with both integer inverses, for shared-factor matrices.")
print("PASS", totals["torsion_changed"], "matrices detect a loss of torsion when the fibre Z/g coordinate is discarded.")
for example in examples:
    print("TORSION_EXAMPLE", json.dumps(example, sort_keys=True))
print("COUNTS", json.dumps(dict(sorted(totals.items())), sort_keys=True))
print("SCOPE new arithmetic supports the separate unbounded proof; no historical LH program or target original was read.")
(LANE/"S6_SERIES_PUBLISH_III_02LH_fresh_patterns.json").write_text(json.dumps(patterns, indent=2)+"\n")
(LANE/"S6_SERIES_PUBLISH_III_02LH_fresh_global_data.json").write_text(
    json.dumps({"scope": "Complete new raw-fibre matrices and exact Smith invariants.",
                "counts": dict(totals), "results": results, "torsion_examples": examples,
                "complete_smith_maps": maps}, indent=2)+"\n")
