"""Exact comb tangent checks by character descent and splitting cohomology.

Run: python code/d_comb.py.  No numerical period or choice of smoothing is
assumed.  The proof in E2.2 explains why these invariant calculations apply
to every member in the stated comb construction.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def descended_degree(det_weight, exponents_3, exponents_4):
    numerator = det_weight - 4*sum(exponents_3) - 3*sum(exponents_4)
    assert numerator % 12 == 0
    return numerator // 12


def line_cohom(degree):
    return (max(degree+1, 0), max(-degree-1, 0))


report = {}
for m in [12, 13, 20, 100]:
    d = 2*m-1
    degrees = {
        "E": descended_degree(24*m-1, [0, 2], [0, 1]),
        "G": descended_degree(24*m-1, [0, 2], [0, 1]),
        "EG": descended_degree(96*m-4, [0, 2, 2, 1], [0, 1, 1, 2]),
        "L": descended_degree(-5, [1], [1]),
        "LG": descended_degree(24*m-11, [1, 0], [1, 2]),
        "E_detG": descended_degree(72*m-3, [2, 1], [1, 2]),
        "R2T_free": descended_degree(24*m+6, [0], [2]),
        "E_dual": descended_degree(1-24*m, [0, 1], [0, 3]),
        "cotangent_KS_target": descended_degree(24*m+9, [2, 1], [3, 0]),
        "E_dual_G": descended_degree(0, [0, 2, 1, 0], [0, 1, 3, 0]),
        "cotangent_KS1_target": descended_degree(24*m+4, [1], [0]),
    }
    assert degrees["E"] == degrees["G"] == d
    assert degrees["EG"] == 8*m-3
    assert degrees["L"] == -1
    assert degrees["LG"] == 2*m-2
    assert degrees["E_detG"] == 6*m-2
    assert degrees["R2T_free"] == 2*m
    assert degrees["E_dual"] == -2*m-1
    assert degrees["cotangent_KS_target"] == 2*m-1
    assert degrees["E_dual_G"] == -2
    assert degrees["cotangent_KS1_target"] == 2*m

    # Independent method: exhaust all nonnegative splitting degrees for the
    # two rank-two coarse bundles.  Their tensor product has the same h^0,
    # and the single upper modification adds exactly one global section.
    possibilities = set()
    for a in range(d//2+1):
        for b in range(d//2+1):
            tensor_degrees = [a+b, a+d-b, d-a+b, 2*d-a-b]
            cohom = [line_cohom(k) for k in tensor_degrees]
            assert sum(v[1] for v in cohom) == 0
            possibilities.add(sum(v[0] for v in cohom)+1)
    assert possibilities == {8*m+1}
    torsion_length = degrees["E_detG"]-degrees["LG"]
    tangent = [2*m+1, 8*m+1, line_cohom(2*m)[0]+torsion_length, 0]
    assert tangent == [2*m+1, 8*m+1, 6*m+1, 0]
    assert tangent[0]-tangent[1]+tangent[2]-tangent[3] == 1
    # Derived directly from the injective cotangent cup map.
    hodge_torsion = degrees["cotangent_KS_target"]-degrees["E_dual"]
    assert hodge_torsion == 4*m
    report[str(m)] = {
        "coarse_bundle_degrees": degrees,
        "all_nonnegative_splittings_agree": True,
        "splitting_pairs_checked": (d//2+1)**2,
        "upper_modification_length": 1,
        "tangent_h0_h1_h2_h3": tangent,
        "R2_tangent_torsion_length": torsion_length,
        "h11_lower_bound": 4*m+1,
        "h12_lower_bound": 4*m,
        "Kuranishi_dimension_bounds": [8*m-8, 8*m+1],
        "unresolved": "h0(K_m), Kuranishi bracket and higher obstructions",
    }

(OUT / "d_comb.json").write_text(json.dumps(report, indent=2)+"\n")
print("Exact coarse degrees agree with all nonnegative splitting possibilities.")
for m, values in report.items():
    print("m="+m, "h(T)=", values["tangent_h0_h1_h2_h3"],
          "length Q=", values["R2_tangent_torsion_length"],
          "Kuranishi dimension bounds=", values["Kuranishi_dimension_bounds"])
print("Wrote outputs/d_comb.json.")
