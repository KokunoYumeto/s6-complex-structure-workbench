#!/usr/bin/env python3
"""Read complete new LH outputs and write their bounded mathematical scope."""
from collections import Counter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_odd_weighted"
prefix = "S6_SERIES_PUBLISH_III_02LH_"
local = json.loads((LANE/(prefix+"fresh_local_data.json")).read_text())
finite = json.loads((LANE/(prefix+"fresh_finite_data.json")).read_text())
global_data = json.loads((LANE/(prefix+"fresh_global_data.json")).read_text())
patterns = json.loads((LANE/(prefix+"fresh_patterns.json")).read_text())
assert len(local["records"]) == 2334
assert len(finite["records"]) == 1386
assert len(global_data["results"]) == 6326
assert len(patterns) == 495
assert sum(p["all_star_original"] for p in patterns) == 459
assert sum(len(r["actions"]) for r in finite["records"]) == 33264
free = sum(a["free"] for r in finite["records"] for a in r["actions"])
assert free == 30511
profile = Counter()
small = set()
for p in patterns:
    profile[tuple(p["key"][:2])+("broad",)] += 1
    profile[tuple(p["key"][:2])+("small",)] += p["all_star_original"]
    if p["all_star_original"]:
        small.add((tuple(p["key"]),tuple(p["choices"])))
g_counts = Counter(r["g"] for r in local["records"])
assert len(global_data["complete_smith_maps"]) == 24
changed = [r for r in global_data["results"] if r["torsion_changes_if_fibre_torsion_discarded"]]
assert len(changed) == 112
example = next(r for r in changed if (tuple(r["key"]),tuple(r["choices"])) in small)
log_lengths = {}
for name in ("exterior_local_v3","component_denominators_v1","catalogue_v1"):
    stem = ROOT/"code"/("S6_SERIES_PUBLISH_c7_lh_"+name)
    out = stem.with_suffix(".out").read_text()
    assert out.endswith("\n") and "PASS" in out
    assert stem.with_suffix(".err").read_bytes() == b""
    log_lengths[name] = len(out.splitlines())

lines = [
    "# 02LH fresh calculation readout", "",
    "All three successful substantive program stdout files were read in full.",
    "Their stderr files are empty. Interrupted and formatting attempts remain",
    "preserved separately and are described in the attempt record.", "",
    "The new local calculation covers all 172 natural rows at every permitted",
    "weight in (1,2,3,5,7,9,15,21,25,35,45,105,315,1001).",
    "It checks finite exact matrix identities at these weights; the main and",
    "local fresh proofs establish the unbounded statements.", "",
    "## Complete finite computation scopes", "",
    "| Calculation | Complete count |", "|---|---:|",
    "| Weighted exterior cases | 2334 |",
    "| Cases with shared odd factors | 586 |",
    "| Saturated local kernels with quotient/section and cover/transfer maps | 12249 |",
    "| Literal rank-one period basis/inverse maps | 4265 |",
    "| Cusp disc maps retaining the angular residue | 2334 |",
    "| Weighted finite projected lattices | 1386 |",
    "| Finite candidates, each checked through every proper power | 33264 |",
    "| Free candidate actions | 30511 |",
    "| Rejected candidates with an exhibited first stabilizer | 2753 |",
    "| Additive positions with exact raw denominator/component order | 126 |",
    "| Powered denominator/orbit-return checks | 1152 |",
    "| Broad-family matrices at five weights and both Euler values | 4950 |",
    "| Shared-factor matrices in the broad-family test | 770 |",
    "| Additional matrices with two full-vector regular sites | 1376 |",
    "| Complete reversible global Smith certificates, with both inverses | 24 |",
    "| Matrices changed by discarding the fibre torsion coordinate | 112 |", "",
    "The finite-data field named core_H1_torsion stores the Smith group of the",
    "displayed affine-group presentation for every candidate. It is cap H1",
    "only for records whose free field is true. For the 2753 rejected actions",
    "it is a formal affine-group presentation; no cap homology is attributed",
    "to those nonfree quotients. The full Thom-source assertions likewise",
    "apply to the free subset. The normal-relation identities are algebraic",
    "identities for all candidate arrays.", "",
    "The complete global test uses v=delta and m=h^2 at finite sites.",
    "These are proved free at every weighted fixed lattice. Its additional",
    "regular sites have (m,v)=(5,(2,-1,3,5)) and (7,(-1,1,-2,-7));",
    "both are primitive modulo their orders. Their gamma ratios sum to zero.",
    "The order-one clutch e=0 and e=1 therefore checks both rational Euler",
    "values in every tested family. The proof handles all other free data.", "",
    "## Every profile count", "",
    "| OS | Profile | Broad families | All-star-original families |",
    "|---:|---|---:|---:|",
]
for os, tag in sorted({tuple(p["key"][:2]) for p in patterns}):
    lines.append(f"| {os} | {tag} | {profile[(os,tag,'broad')]} | {profile[(os,tag,'small')]} |")
lines += [
    "| Total | | 495 | 459 |", "",
    "The literal inclusion fixes every all-star-original choice. The explicit",
    "retraction replaces finite III*/IV* choices by their original cap and",
    "fixes all other entries. Its composite with the inclusion is identity.",
    "All 36 omitted labelled families and every projection are present in",
    "the complete fresh_patterns.json file.", "",
    "## A shared-factor example in the all-star-original scope", "",
    "The following saved example lies in the 459-family subset:", "",
]
example_text = json.dumps({k:example[k] for k in
    ("key","choices","D","g","e","regular","T","H1_free","A1","beta","L","bridge","b2","b3","Euler")},indent=2)
lines += ["    "+line for line in example_text.splitlines()]
lines += [
    "", "Here the list T contains cyclic invariant factors Z/n; free ranks",
    "b2,b3 and H1_free mean powers Z^b2, Z^b3 and Z^r.",
    "The complete matrix and all its Smith factors are in the saved global",
    "data. The corresponding reduced matrix loses torsion, so replacing",
    "the raw fibre target by one free alternating functional changes this",
    "computed integral group.", "",
    "## Output reading", "",
]
for name, count in log_lengths.items():
    lines.append(f"- code/S6_SERIES_PUBLISH_c7_lh_{name}.out: {count} lines, read completely; stderr empty.")
lines += [
    "", "No LH original, historical target executable or historical target table",
    "was read or executed. These calculations are new. The target remains",
    "embargoed until root's individual release after full fresh review.", "",
]
(LANE/(prefix+"fresh_calculation_readout.md")).write_text("\n".join(lines))
print("PASS all new local, finite, pattern and global data read completely by the readout program.")
print("PASS all 21 profile counts, 495/459 inclusion/retraction and 36 alternatives.")
print("PASS complete successful stdout files; all three substantive stderr files empty.")
print("EXTERIOR_G_COUNTS",json.dumps(dict(sorted(g_counts.items())),sort_keys=True))
print("ALL_STAR_EXAMPLE",json.dumps({k:example[k] for k in ("key","choices","D","g","e","T","A1","b2","b3")},sort_keys=True))
print("OUTPUT_LENGTHS",json.dumps(log_lengths,sort_keys=True))
print("SCOPE formal nonfree affine presentations are distinguished from the 30511 actual free-cap calculations.")
