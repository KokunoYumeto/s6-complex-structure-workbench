#!/usr/bin/env python3
"""Independent bounded denominator and powered-orbit checks for LH."""
from collections import Counter
from hashlib import sha256
from math import gcd, lcm
from pathlib import Path
import json
import re
from sympy import Matrix, eye
from S6_SERIES_PUBLISH_c7_lh_integral import component_data, permutation_power, cycles

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT/"agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json"
LD = ROOT/"agents/continuation7_iii_weighted_catalogue"
raw = {(r["OS"], r["profile"]): r for r in json.loads(RAW.read_text())["rows"]}
rows = json.loads((LD/"S6_SERIES_PUBLISH_III_02LD_fresh_exterior_data.json").read_text())["rows"]
count = Counter()
for row in rows:
    data = raw[tuple(row["key"][:2])]
    a, b = row["key"][2:4]
    for i, kind in enumerate(row["fibres"]):
        if re.fullmatch(r"I\d+", kind):
            continue
        B = Matrix(data["elliptic_matrices"][i])
        sec = Matrix(data["generator_section_cocycle"][i])
        z = (B-eye(2)).inv()*sec
        denominator = lcm(*(int(x.q) for x in z))
        q, residue = row["components"][i]
        assert denominator == q
        sigma, multiplicities = component_data(kind)
        orbit_orders = [len(o) for o in cycles(sigma)]
        assert lcm(*orbit_orders) == q
        assert all(multiplicities[j] == multiplicities[sigma[j]] for j in range(len(sigma)))
        for D in (1, 2, 3, 4, 5, 7, 9, 15, 105, 1001):
            if gcd(a, D) % 2 == 0:
                continue
            gd = lcm(*(int((D*b*x).q) for x in z))
            assert gd == q//gcd(q, D*b)
            powered = permutation_power(sigma, -D*b*residue)
            assert lcm(*(len(o) for o in cycles(powered))) == gd
            count["weighted_denominator_orbit_maps"] += 1
        count[kind] += 1
        count["all_additive_positions"] += 1
for kind in ("II", "III", "IV", "III*", "IV*", "I1*", "I3*"):
    print("TYPE", kind, "POSITIONS", count[kind])
print("PASS every raw additive denominator equals the component-action order.")
print("PASS every powered denominator equals q/gcd(q,Db), including shared odd factors.")
print("PASS every powered permutation has the exact orbit-return order; all multiplicities are preserved.")
print("COUNTS", json.dumps(dict(sorted(count.items())), sort_keys=True))
print("SCOPE only raw/admitted defining data read; LH original and historical programs remain closed.")
