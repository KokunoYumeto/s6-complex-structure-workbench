#!/usr/bin/env python3
"""Exact common-exterior meridian, dual-cycle, and variation matrices.

The geometric proof of the transfer-chain coefficients and the circle-trace
vanishing is in notes/part3_common_exterior_meridians.md. This certificate
checks every change-of-basis and the primitive integral lattices used there.
It does not assign a relative Pontryagin coefficient after a fixed-edge flop.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parents[2]
v = S.symbols("v", integer=True)
I = S.eye(3)
V = S.diag(v, 0, 0)
data = {
    "scope": "Index-one cusp; three complex double curves and their common exterior",
    "basis": {
        "absolute": ["positive complex meridian m0", "m1", "m2"],
        "relative": ["D0 paired with m0", "D1 paired with m1", "D2 paired with m2"],
    },
    "flops": [],
}
for i in range(3):
    M = S.eye(3)
    for j in range(3):
        M[j, i] = -1 if j == i else 2
    Q = M.inv().T
    W = M.inv() * V * Q
    assert M.det() == -1
    assert M*M == I
    assert M.T*Q == I
    assert W == W.T
    assert smith_normal_form(M, domain=ZZ).det() in (-1, 1)
    assert M * W == V * Q
    data["flops"].append({
        "selected_edge": i,
        "new_meridians_as_old_columns": [list(map(int, M.row(j))) for j in range(3)],
        "new_relative_cycles_as_old_columns": [list(map(int, Q.row(j))) for j in range(3)],
        "new_variation": [[str(W[j,k]) for k in range(3)] for j in range(3)],
    })
assert data["flops"][0]["new_variation"] == [
    ["v", "-2*v", "-2*v"], ["-2*v", "4*v", "4*v"],
    ["-2*v", "4*v", "4*v"]
]
assert all(
    S.Matrix(data["flops"][i]["new_meridians_as_old_columns"])*S.Matrix([1,0,0])
        == S.Matrix([1,0,0])
    for i in (1,2)
)

# On E=P1_a x P1_c with four balls removed, the small boundary classes
# have the sole primitive relation p00+p01+p10+p11=0. Circle transfer
# of c1(O(1,1)) supplies m0'+m0=sum of these section lifts in S(O(-1,-1)).
puncture_relation = S.Matrix([[1,1,1,1]])
assert smith_normal_form(puncture_relation, domain=ZZ)[0,0] == 1
# The two punctures on each nonselected curve have the same positive
# complex normal orientation; these are the exact incidence columns.
punctures_to_other_meridians = S.Matrix([[1,0,1,0], [0,1,0,1]])
assert punctures_to_other_meridians*S.ones(4,1) == S.Matrix([2,2])
data["reciprocal_section_boundary"] = {
    "transfer_class_on_exceptional_surface": [1,1],
    "four_puncture_incidence": [list(map(int, punctures_to_other_meridians.row(j))) for j in range(2)],
    "other_meridian_coefficients": [2,2],
    "oriented_chain": "T[a]+T[c]-mu00-mu01-mu10-mu11",
}
data["primitive_scalar_cases"] = [
    {"d": d, "k_Jin": -3*d, "product_variation_K23": 3*d, "dual_cycle_variation_v": -3*d,
     "initial_variation": [[-3*d,0,0],[0,0,0],[0,0,0]],
     "after_fixed_edge_variation":
         [[-3*d,6*d,6*d],[6*d,-12*d,-12*d],[6*d,-12*d,-12*d]],
     "nonfixed_edge_relative_n_before_fixed_edge_flop": [0,0],
     "finite_isotropy_pontryagin_coefficient": "not assigned"}
    for d in (8,14,20,30)
]
data["checks"] = {
    "unimodular_meridian_changes": "PASS",
    "dual_relative_changes": "PASS",
    "variation_conjugation": "PASS",
    "primitive_four_puncture_relation": "PASS",
    "geometric_chain_and_trace_are_proved_in_note": True,
}
(ROOT/"code/part3_fourfold/common_exterior_meridians.json").write_text(
    json.dumps(data, indent=2)+"\n")
with (ROOT/"records/literature_fourfold.md").open("a") as log:
    log.write("\n- "+datetime.now(timezone.utc).isoformat()
              +" — Executed own code/part3_fourfold/common_exterior_meridians.py; "
              "reason: certify the exact K29 meridian/relative-cycle changes; "
              "material: all three integral matrices, primitive puncture relation, "
              "and common-exterior variation conjugation. No new web source opened.\n")
print("PASS: exact meridian, dual-cycle, and variation matrices for all three cusp edges.")
print("No finite-isotropy relative Pontryagin coefficient has been assigned.")


# BEGIN POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
import importlib.util as _scalar_scope_importlib
from pathlib import Path as _ScalarScopePath
_scalar_scope_root = _ScalarScopePath(__file__).resolve().parents[2]
_scalar_scope_spec = _scalar_scope_importlib.spec_from_file_location(
    "_scalar_dependency_scope",
    _scalar_scope_root / "code/part3/scalar_dependency_scope.py")
_scalar_scope_module = _scalar_scope_importlib.module_from_spec(_scalar_scope_spec)
_scalar_scope_spec.loader.exec_module(_scalar_scope_module)
_scalar_scope_module.postprocess_generated(
    ['code/part3_fourfold/common_exterior_meridians.json'], [], origin='code/part3_fourfold/common_exterior_meridians.py')
# END POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
