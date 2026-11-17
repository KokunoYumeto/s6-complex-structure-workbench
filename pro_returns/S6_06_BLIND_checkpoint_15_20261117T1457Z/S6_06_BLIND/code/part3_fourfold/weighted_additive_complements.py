#!/usr/bin/env python3
"""Exact complementary good-root source complements, retaining torsion."""
from pathlib import Path
from functools import reduce
from math import gcd
from datetime import datetime, timezone
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parents[2]
rel = "code/part3_fourfold/primitive_source_translation.json"
with (ROOT / "records/literature_fourfold.md").open("a") as log:
    log.write("\n- " + datetime.now(timezone.utc).isoformat()
              + " — Opened current-team " + rel
              + "; reason: exact powers of the marked suspension translation "
              "for the three complementary good-root sectors; material: "
              "full integral NS Gram, section, and translation matrices.\n")
data = json.loads((ROOT / rel).read_text())
cases = {a["row"]: a for a in data["cases"]}

def ints(A):
    assert all(s.denom(x) == 1 for x in A)
    return [[int(x) for x in row] for row in A.tolist()]

def primitive(v):
    v = v*s.ilcm(*[s.denom(x) for x in v])
    v = v/reduce(gcd, [abs(int(x)) for x in v])
    for x in v:
        if x:
            if x < 0:
                v = -v
            break
    return v

outputs = []
for row, p, block, kind, line_multiple in [
    (47, 2, 1, "III", 7),
    (56, 2, 2, "III", 15),
    (56, 3, 1, "IV", 10),
]:
    a = cases[row]
    gram = s.Matrix(a["gram"])
    T0 = s.Matrix(a["actual_suspension_translation"])
    T = T0**p
    eye = s.eye(10)
    F, O = eye[:, 1], eye[:, 0]
    roots = [i for i, name in enumerate(a["basis"])
             if name.startswith(f"I{p}_{block}_C")]
    assert len(roots) == p-1
    deleted = [1] + roots
    retained = [i for i in range(10) if i not in deleted]
    K = gram.inv()[:, retained]
    P = gram[retained, :]
    constraint = gram[deleted, :]
    assert abs(gram.det()) == 1
    assert P*K == s.eye(10-p)
    assert constraint*K == s.zeros(p, 10-p)
    Tv = P*T*K
    assert K*Tv == T*K
    D = Tv-s.eye(10-p)
    SD = smith_normal_form(D, domain=ZZ)
    smith = [abs(int(SD[i, i])) for i in range(10-p)]
    assert D.nullspace().__len__() == 1
    Fc = P*F
    ker = primitive(D.nullspace()[0])
    assert ker == Fc or ker == -Fc
    free = primitive(D.T.nullspace()[0])

    # The actual pG section is on the identity component at the removed fibre.
    Z0 = T*O-O
    correction = -(gram[roots, roots].inv()*gram[roots, :]*Z0)
    Z = Z0+eye[:, roots]*correction
    assert all(s.denom(x) == 1 for x in correction)
    assert constraint*Z == s.zeros(p, 1)
    Zc = P*Z
    zfree = (free.T*Zc)[0]
    # Do not identify an ordinary section divisor with a compact cycle if
    # it has nonzero degree on a component removed from the source.
    M = (T0**(-line_multiple))*O-O
    line_restriction = K.T*gram*M
    line_component_degrees = constraint*M
    assert T.T*gram*T == gram
    assert T*M-M == -F

    # Quotient by the actual q-boundary image. These invariant factors retain
    # precisely the finite group still requiring the other boundary columns.
    DZ = D.row_join(Zc)
    Splus = smith_normal_form(DZ, domain=ZZ)
    smith_with_q = [abs(int(Splus[i, i])) for i in range(10-p)]
    # Include the fibre column as well, to expose any additional boundary
    # torsion independently of an unnamed cap generator.
    DZF = DZ.row_join(Fc)
    SF = smith_normal_form(DZF, domain=ZZ)
    smith_with_qF = [abs(int(SF[i, i])) for i in range(10-p)]

    # The affine component-plumbing boundary, with its actual translation
    # chain homotopy obtained from the full unimodular source decomposition.
    U = s.eye(p)
    for ii in range(1, p):
        U[ii, 0] = -1
    J = eye[:, deleted]*U
    Q = J.T*gram*J
    assert T*J == J
    L = gram.inv()[:, deleted]
    assert K*P+L*constraint == eye
    A_boundary = P*J
    H_boundary = -P*T*L*U.inv().T
    assert D*A_boundary == H_boundary*Q
    alpha = s.eye(p)[:, 0]
    eta = s.eye(p)[:, 1]-alpha
    q_boundary = -H_boundary*alpha
    eta_boundary = -H_boundary*eta
    assert q_boundary-Zc == -D*(P*O)
    SQ = smith_normal_form(Q, domain=ZZ)
    affine_smith = [abs(int(SQ[i, i])) for i in range(p)]
    Dqeta = D.row_join(q_boundary).row_join(eta_boundary)
    SDqeta = smith_normal_form(Dqeta, domain=ZZ)
    smith_qeta = [abs(int(SDqeta[i, i])) for i in range(10-p)]

    outputs.append({
        "row": row, "removed_fibre": kind,
        "translation_section_multiple": p,
        "line_section_multiple": line_multiple,
        "NS_basis": a["basis"],
        "NS_gram": ints(gram),
        "actual_translation": ints(T),
        "constraint_rows": ints(constraint),
        "integral_kernel_basis": ints(K),
        "kernel_left_inverse": ints(P),
        "translation_restriction": ints(Tv),
        "wang_matrix": ints(D),
        "smith": smith,
        "intersection_matrix": ints(K.T*gram*K),
        "kernel_F_coordinates": ints(Fc),
        "primitive_free_cokernel_functional": ints(free),
        "relative_Wang_source_cycle": ints(Z),
        "relative_Wang_removed_root_correction": ints(correction),
        "relative_Wang_kernel_coordinates": ints(Zc),
        "relative_Wang_free_value": int(zfree),
        "line_divisor_class": ints(M),
        "line_component_degrees": ints(line_component_degrees),
        "line_cohomology_on_complement": ints(line_restriction),
        "wang_plus_actual_q_column": ints(DZ),
        "smith_with_actual_q_column": smith_with_q,
        "smith_with_q_and_F_columns": smith_with_qF,
        "central_component_inclusion_J": ints(J),
        "affine_boundary_differential_Q": ints(Q),
        "affine_boundary_smith": affine_smith,
        "source_boundary_degree2_map_A": ints(A_boundary),
        "actual_pair_translation_homotopy_H": ints(H_boundary),
        "boundary_base_meridian_alpha": ints(alpha),
        "boundary_torsion_eta": ints(eta),
        "mapping_torus_q_column": ints(q_boundary),
        "mapping_torus_eta_gamma_column": ints(eta_boundary),
        "smith_with_q_and_eta_gamma": smith_qeta,
        "scope": (
            "Exact source complement and actual relative-Wang q column. "
            "The line is recorded as cohomology on the complement; "
            "its divisor is not silently made into a compact cycle. "
            "The remaining torsion boundary/cap maps require their actual charts."
        ),
    })
    print(f"OS{row}, {kind}, Q={p}G, M={line_multiple}G-O: "
          f"Smith {smith}; q free value {zfree}; "
          f"after q {smith_with_q}; after q,F {smith_with_qF}; "
          f"after q,eta*gamma {smith_qeta}")

Path(__file__).with_suffix(".json").write_text(
    json.dumps({"status": "PASS", "cases": outputs}, indent=2)+"\n"
)
print("PASS: exact NS powers, full integral kernels, source-Wang columns, line degrees, and retained torsion.")
