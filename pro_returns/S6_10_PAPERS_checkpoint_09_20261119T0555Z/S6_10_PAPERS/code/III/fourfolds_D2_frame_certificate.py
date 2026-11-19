"""Exact local identities and an independent degree check for D.2.44.

This certificate verifies polynomial identities and the integral relation
between the actual critical-cycle preimages and the auxiliary fibre form.
Brown's and Zhubr's geometric arguments are proved in the accompanying TeX;
they are not inferred from this finite calculation.

Run after manifolds_even_critical_cycles.py.  Bounds are exactly the fourteen
marked rows (seven initial rows, each ordinary clutch sign).
"""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parent


def main():
    x, y, z = s.symbols("x y z")
    kernels = [
        (x * y, s.Matrix([[x, 0], [-y, 0], [0, 1]])),
        (x * y * z, s.Matrix([[x, 0], [-y, y], [0, -z]])),
    ]
    for f, K in kernels:
        df = s.Matrix([[s.diff(f, u) for u in (x, y, z)]])
        assert df * K == s.zeros(1, 2)

    xr, xi, yr, yi = s.symbols("xr xi yr yi", real=True)
    xx, yy = xr + s.I * xi, yr + s.I * yi
    M = s.Matrix([[xx, s.conjugate(yy)], [-yy, s.conjugate(xx)]])
    norm = xr**2 + xi**2 + yr**2 + yi**2
    assert s.simplify(M.conjugate().T * M - norm * s.eye(2)) == s.zeros(2)
    assert s.expand(M.det() - norm) == 0
    degrees = s.Matrix([[0, -1, 0], [1, 1, -1], [-1, 0, 0]])
    assert degrees.det() == -1
    assert degrees * s.ones(3, 1) == s.Matrix([-1, 1, -1])

    source = ROOT / "manifolds_even_critical_cycles.json"
    rows = json.loads(source.read_text())["rows"]
    assert len(rows) == 14
    outputs = []
    expected = {(45, 1): 4, (45, 2): 4, (45, 3): 4, (45, 4): 4,
                (55, 2): 37, (55, 3): 7, (55, 4): 27}
    for row in rows:
        entry, profile, a, b, zero = row["key"]
        assert profile == "default" and b == row["c"]
        e = row["e"]
        assert e in (-1, 1)
        curve = s.Matrix(row["critical_cycle"])
        functional = s.Matrix([[a, 0, 0, 0, 0, -b]])
        local_degrees = [int((functional * s.Matrix(q["curve_lift"]))[0])
                         for q in row["local_critical_lifts"]]
        assert sum(local_degrees) == int((functional * curve)[0])
        degree = sum(local_degrees)
        link = row["critical_linking"]
        assert degree == -b * e * link
        assert link == e * expected[entry, zero]
        assert s.gcd(row["torsion_linking_loop"][2], b) == 1
        refined = (b // 2) * (link % 2)
        assert refined == (2 if entry == 55 else 0)
        outputs.append(dict(key=row["key"], e=e, critical_link=link,
                            local_auxiliary_degrees=local_degrees,
                            total_auxiliary_degree=degree,
                            refined_value_given_D44_proof=refined))
        print(row["key"], "e", e, "degrees", local_degrees,
              "sum", degree, "link", link, "P", refined, flush=True)
    record = dict(scope=__doc__, source=str(source.relative_to(ROOT)),
                  source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  exact_checks=dict(kernel_identities=2, Bott_identities=2,
                                    cusp_degree_identities=2, marked_rows=14),
                  rows=outputs)
    (ROOT / "fourfolds_D2_frame_certificate.json").write_text(
        json.dumps(record, indent=2) + "\n")
    print("PASS: exact local identities and all fourteen degree/link comparisons")


if __name__ == "__main__":
    main()
