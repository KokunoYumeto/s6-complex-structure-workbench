#!/usr/bin/env python3
"""Recompute all 50 filling inputs and 8 clutch inputs from pinned cochains.

Run under the task-local Sage 10.9 Python. The external backend/data remain
outside the checkpoint. Retained per-input files are exact computed matrix
inputs, assembled cones and verification certificates. No geometric local
model is newly identified by this algebraic replay.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
from collections import Counter
import hashlib
import json
import os
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parents[1] / "tmp/c9_computation_backend"
OUT = ROOT / "agents/continuation9_computation_method"
MATRICES = OUT / "matrix_replay"
MATRICES.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("DOT_SAGE", str(ROOT.parents[1] / "tmp/c9_sage_runtime/dot_sage"))
sys.path.insert(0, str(WORK))

import sage.all as s
import sage.version
import os_monodromy as om
import threefold_topology as top
from fiberwise_narrow import explore_fiberwise_narrow
from local_model_database import LocalModelDatabase, encode
from explorer_api import _json_value

PIN = "cfe53e0454fdd167adfab00c69e602341b105e40"
assert sage.version.version == "10.9", sage.version.version
meta = json.loads((OUT / "S6_SERIES_PUBLISH_c9_backend_sources.json").read_text())
assert meta["repository_commit"] == PIN
for item in meta["sources"]:
    assert hashlib.sha256((WORK / item["name"]).read_bytes()).hexdigest() == item["sha256"]
print("Sage", sage.version.version, "pinned backend", PIN, flush=True)
print("Actual source-file SHA-256 matches verified metadata for", len(meta["sources"]), "files.", flush=True)

PROFILES = {
    43: (2, ("default", "II")), 45: (8, ("default", "II")),
    46: (4, ("default", "II")), 47: (14, ("default", "II", "III")),
    49: (6, ("default", "II", "III")), 50: (12, ("default", "II", "IV")),
    55: (20, ("default", "II")), 56: (30, ("default", "II", "III", "IV")),
}
ORDERS = {"II": 6, "III": 4, "IV": 3, "III*": 4, "IV*": 3, "I1*": 2, "I3*": 2}


def canonical(payload):
    logs = tuple(None if value is None else tuple(str(Fraction(x)) for x in value)
                 for value in payload["log_data"])
    return (payload["os_entry"], payload["profile"], tuple(payload["P"]), tuple(payload["Q"]),
            tuple(payload["linearization_divisor"]), logs, payload["coordinates"])


archive = {}
for path in sorted((ROOT / "agents/continuation7_iii_ku/raw_responses").glob("*.json")):
    record = json.loads(path.read_text())
    key = canonical(record["input"])
    assert key not in archive
    archive[key] = (path, record)
assert len(archive) == 58

inputs = []
for entry, (n, profiles) in PROFILES.items():
    for profile in profiles:
        types = [row["type"] for row in om._model(entry, profile)["fibers"]]
        additive = [i for i, kind in enumerate(types) if kind in ORDERS]
        zero = types.index("I1") if "I1" in types else min(
            (int(kind[1:]), i) for i, kind in enumerate(types)
            if kind.startswith("I") and kind[1:].isdigit())[1]
        for bits in product((0, 1), repeat=len(additive)):
            logs = [None] * len(types)
            for index, bit in zip(additive, bits):
                if bit:
                    logs[index] = ["0", "1/%d" % ORDERS[types[index]]]
            inputs.append({"os_entry": entry, "profile": profile, "P": [1], "Q": [n],
                           "linearization_divisor": [int(i == zero) for i in range(len(types))],
                           "log_data": logs, "coordinates": "invariant"})
assert len(inputs) == 50
assert {canonical(x) for x in inputs} == {k for k, (p, _) in archive.items() if p.name.startswith("all21_")}
print("Independently generated finite slice equals all 50 archived exact inputs.", flush=True)
for entry, n in [(45, 8), (47, 14), (55, 20), (56, 30)]:
    assert len(om._model(entry, "default")["fibers"]) == 5
    for clutch in (0, 1):
        inputs.append({"os_entry": entry, "profile": "default", "P": [n], "Q": [1],
                       "linearization_divisor": [0, 0, 0, 0, 1, 0],
                       "log_data": [None] * 5 + [[0, 0, 0, clutch]], "coordinates": "ambient"})
assert {canonical(x) for x in inputs} == set(archive)
print("Four generated clutch pairs equal the remaining 8 archived exact inputs.", flush=True)


def rank(model, q):
    return int(model["ranks"][q]) if 0 <= q < len(model["ranks"]) else 0


def differential(model, q):
    return s.matrix(s.ZZ, model["differentials"].get(q, s.zero_matrix(s.ZZ, rank(model, q + 1), rank(model, q))))


def assemble(model):
    """Independent block assembly in source then shifted-boundary coordinates."""
    sources = [model["complement"]] + model["fillings"]
    boundaries = model["boundaries"]
    maximum = max([len(a["ranks"]) - 1 for a in sources] + [len(b["ranks"]) for b in boundaries])
    ranks = [sum(rank(a, q) for a in sources) + sum(rank(b, q - 1) for b in boundaries)
             for q in range(maximum + 1)]
    ds = {}
    for q in range(maximum):
        D = s.zero_matrix(s.ZZ, ranks[q + 1], ranks[q])
        column = row = 0
        offsets = []
        for a in sources:
            offsets.append(column)
            D[row:row + rank(a, q + 1), column:column + rank(a, q)] = differential(a, q)
            row += rank(a, q + 1)
            column += rank(a, q)
        for i, b in enumerate(boundaries):
            D[row:row + rank(b, q), column:column + rank(b, q - 1)] = -differential(b, q - 1)
            D[row:row + rank(b, q), :rank(sources[0], q)] = model["complement_maps"][i].get(q, s.zero_matrix(s.ZZ, rank(b, q), rank(sources[0], q)))
            D[row:row + rank(b, q), offsets[i + 1]:offsets[i + 1] + rank(sources[i + 1], q)] = -model["filling_maps"][i].get(q, s.zero_matrix(s.ZZ, rank(b, q), rank(sources[i + 1], q)))
            row += rank(b, q)
            column += rank(b, q - 1)
        assert D.dimensions() == (ranks[q + 1], ranks[q])
        ds[q] = D
    for q in range(maximum - 1):
        assert ds[q + 1] * ds[q] == 0
    return {"ranks": tuple(ranks), "differentials": ds}


def independent_groups(cone):
    """SNF of each incoming differential, plus exact outgoing ranks.

    For these checked complexes the map C^q/im D(q-1) -> im D(q) has
    kernel H^q. Its target is a free subgroup of C^(q+1), so its splitting
    preserves precisely all torsion and subtracts rank D(q). This computes
    the group via a separate Smith calculation from the backend kernel basis.
    """
    answer = []
    for q, dim in enumerate(cone["ranks"]):
        previous = differential(cone, q - 1)
        following = differential(cone, q)
        assert following * previous == 0
        diagonal = previous.smith_form(transformation=False)
        factors = [int(abs(diagonal[j, j])) for j in range(min(diagonal.dimensions())) if diagonal[j, j]]
        assert all(b % a == 0 for a, b in zip(factors, factors[1:]))
        outgoing = int(following.rank())
        answer.append({"degree": q, "rank": int(dim) - len(factors) - outgoing,
                       "torsion": [d for d in factors if d > 1],
                       "incoming_smith_nonzero": factors, "outgoing_rank": outgoing})
    return answer


db = LocalModelDatabase(WORK / "local_model_database")
summary = []
models = {}
for number, payload in enumerate(inputs, 1):
    started = time.monotonic()
    path, archived = archive[canonical(payload)]
    name = path.stem
    print("START", number, name, flush=True)
    result = explore_fiberwise_narrow(payload["os_entry"], tuple(payload["P"]), tuple(payload["Q"]),
             tuple(payload["linearization_divisor"]), payload["log_data"],
             profile=payload["profile"], coordinates=payload["coordinates"],
             database=db, recognition_seconds=0, verbose=False)
    assert result["status"] == "computed from database cochains"
    assert result["closed_oriented_checks"] and result["end_to_end_complete"]
    plan = result["database_plan"]
    cone = assemble(plan["mv_model"])
    assert cone["ranks"] == result["mayer_vietoris"]["ranks"]
    assert all(D == result["mayer_vietoris"]["differentials"][q] for q, D in cone["differentials"].items())
    groups = independent_groups(cone)
    actual = [{"degree": q, "rank": int(result["outcome"]["cohomology"][q]["rank"]),
               "torsion": list(map(int, result["outcome"]["cohomology"][q]["torsion"]))} for q in range(7)]
    assert actual == [{k: g[k] for k in ("degree", "rank", "torsion")} for g in groups[:7]]
    expected = [{k: g[k] for k in ("degree", "rank", "torsion")} for g in archived["response"]["cohomology"]]
    assert actual == expected, (name, actual, expected)
    pi = result["pi1"]
    assert pi["abelian_proved"] is True
    actual_pi = {"description": pi["description"], "trivial": pi["trivial"],
                 "order": str(pi["order"]), "abelianization": pi["abelianization"]["label"]}
    assert actual_pi == archived["response"]["fundamental_group"], (name, actual_pi)
    killed = pi["fiber_relations"]
    central_witnesses = []
    if pi["fiber_central"]:
        for T in result["data"]["matrices"]:
            coordinates = s.matrix(s.ZZ, killed.solve_right(T - 1))
            assert killed * coordinates == T - 1
            central_witnesses.append(coordinates)
    sites = []
    for site, row, peripheral, saved in zip(result["data"]["sites"], plan["sites"], plan["peripheral_records"], archived["response"]["local_models"]):
        stored = db.get(row["model_id"])
        selection = {k: v for k, v in row["selection"].items() if k != "geometric_comparison"}
        assert site["index"] == saved["index"] and site["type"] == saved["type"]
        assert row["model_id"] == saved["model_id"] and selection["family"] == saved["family"]
        assert _json_value(selection["parameters"]) == saved["parameters"]
        assert int(peripheral["multiplicity"]) == saved["fiber_multiplicity"]
        assert all(selection.get(k) == saved[k] for k in ("component_orbits", "component_orbit_length"))
        models.setdefault(row["model_id"], {"family": selection["family"],
                          "parameters": _json_value(selection["parameters"]),
                          "filling_ranks": list(stored["pair"]["filling"]["ranks"]),
                          "boundary_ranks": list(stored["pair"]["boundary"]["ranks"]),
                          "occurrences": []})["occurrences"].append([name, int(site["index"])])
        sites.append({"input": site, "selection": selection, "model_id": row["model_id"],
                      "local_pair": stored["pair"], "boundary_normalization": stored.get("boundary_normalization"),
                      "attachment_comparison": row["attachment"]["comparison"],
                      "transport": row["attachment"].get("transport"),
                      "divisor_base_clutch": row["attachment"].get("divisor_base_clutch"),
                      "peripheral": peripheral})
    item = {"input_name": name, "payload": payload, "backend_pin": PIN,
            "archive_input_file": str(path.relative_to(ROOT)),
            "matrix_model": plan["mv_model"], "cone": cone, "sites": sites,
            "cohomology": groups, "fundamental_group": actual_pi,
            "pi1_certificate": {"fiber_relations": killed, "fiber_central": pi["fiber_central"],
              "central_containment_coordinates": central_witnesses, "orbifold": pi["orbifold"],
              "abelian_proved": pi["abelian_proved"],
              "relators": [tuple(map(int, rel.Tietze())) for rel in pi["group"].relations()],
              "abelian_relations": pi["abelianization"]["relations"]},
            "geometric_derivations_reverified": False}
    data = (json.dumps(encode(item), separators=(",", ":"), ensure_ascii=False) + "\n").encode()
    output = MATRICES / ("S6_SERIES_PUBLISH_c9_KU_" + name + ".json")
    output.write_bytes(data)
    sphere = actual == [{"degree": q, "rank": int(q in (0, 6)), "torsion": []} for q in range(7)]
    row = {"input_name": name, "payload": payload, "cohomology": actual, "fundamental_group": actual_pi,
           "sphere_cohomology": sphere, "cochain_ranks": list(cone["ranks"]),
           "fiber_central": bool(pi["fiber_central"]), "abelian_proved": bool(pi["abelian_proved"]),
           "orbifold_order": str(pi["orbifold"]["order"]),
           "models": [{"index": int(x["input"]["index"]), "type": x["input"]["type"],
                       "family": x["selection"]["family"], "parameters": encode(x["selection"].get("parameters")),
                       "model_id": x["model_id"]} for x in sites],
           "matrix_output_file": output.name,
           "seconds": round(time.monotonic() - started, 3)}
    summary.append(row)
    (OUT / "S6_SERIES_PUBLISH_c9_ku_matrix_replay_summary.json").write_text(json.dumps(summary, indent=2) + "\n", newline="\n")
    print("PASS", number, name, "H", [(g["rank"], g["torsion"]) for g in actual],
          "pi1", actual_pi["description"], "central", pi["fiber_central"],
          "abelian_proved", pi["abelian_proved"], "seconds", row["seconds"], flush=True)

fifty = [r for r in summary if r["input_name"].startswith("all21_")]
assert len(fifty) == 50 and len(summary) == 58
assert sum(r["fundamental_group"]["trivial"] for r in fifty) == 24
assert sum(r["sphere_cohomology"] for r in fifty) == 3
(OUT / "S6_SERIES_PUBLISH_c9_ku_model_index.json").write_text(json.dumps(models, indent=2) + "\n", newline="\n")
print("ALL 58 PASSED: actual matrix-derived cohomology, independently assembled cones, independent incoming-SNF checks and proved abelian pi1 match archived outputs.", flush=True)
print("All current local model IDs, parameters, multiplicities and component-orbit fields match archived bindings.", flush=True)
print("Unique local models", len(models), "site occurrences", sum(len(m["occurrences"]) for m in models.values()), flush=True)
print("50-input pi1 counts", dict(Counter(r["fundamental_group"]["description"] for r in fifty)), flush=True)
print("50-input sphere cases", [r["input_name"] for r in fifty if r["sphere_cohomology"]], flush=True)
print("Geometry scope: pinned local cochain/attachment models used; no new proof of unpublished local geometric derivations.", flush=True)
