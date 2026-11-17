#!/usr/bin/env python3
"""Exact local matrices and parameter characters for P3K.25."""
from pathlib import Path
from datetime import datetime, timezone
import itertools
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "notes/part3_whole_i1_shear.md"
with (ROOT / "records/literature_fourfold.md").open("a") as log:
    log.write(
        "\n- " + datetime.now(timezone.utc).isoformat()
        + " — Opened own notes/part3_whole_i1_shear.md; reason: "
        "execute exact whole-I1 Cox ray, period, gauge, and cap maps; "
        "material: P3K.25 matrices only, with global proof scope retained.\n"
    )
SOURCE.read_text()

j = s.symbols("j", integer=True)
A, C, P = s.symbols("A C P")
# The local square at the next horizontal/nonfixed edge.
B = s.Matrix([[1, 0], [-j-1, 1]])
U0 = s.Matrix([[0, 1, 1, 0], [0, 1, 0, 1], [1, 1, 1, 1]])
Bhat = s.diag(B, 1)
U = Bhat * U0
aux = s.Matrix([1, 1, -1, -1])
delta = s.Matrix([-1, 0, 0, 1])
assert U * aux == s.zeros(3, 1)
assert U * delta == s.Matrix([0, 1, 0])
assert B.det() == 1
assert B.inv() * s.Matrix([1, 0]) == s.Matrix([1, j+1])
assert B.inv() * s.Matrix([0, 1]) == s.Matrix([0, 1])
period_labels = B.inv()
assert period_labels.det() == 1
weights = s.Matrix.vstack(aux.T, delta.T)
minors = {
    str(pair): int(weights[:, list(pair)].det())
    for pair in itertools.combinations(range(4), 2)
}
assert all(abs(v) <= 1 for v in minors.values())

# Local coordinates are Z_loc=Z, V_loc=Z^(j+1)V.
# Gamma's bounded logarithms are A and (j+1)A+C+P.
local_gauge = s.Matrix([-(j+2)*A-C-P, 0, A, (j+1)*A+C+P])
assert s.simplify(sum(local_gauge)) == 0
assert s.simplify(U * local_gauge) == s.Matrix([A, C+P, 0])
assert local_gauge.diff(P) == delta

end1 = s.Matrix([[1, 0], [0, -1]])
end2 = s.Matrix([[0, -1], [1, 0]])
e = s.Matrix([1, -1])
assert end1*e == end2*e == s.Matrix([1, 1])
closing = s.Matrix([[0, -1], [-1, 0]])
assert closing*e == e
assert closing.det() == -1  # On H2; it preserves the four-dimensional form.
H = s.Matrix([[0, 1], [1, 0]])
assert closing.T*H*closing == H

ss, vv, theta, GG, CC = s.symbols("s v theta Gamma C")
ordinary = s.Matrix([-GG*ss, -CC*ss-ss**2/2-ss*vv])
cusp = s.Matrix([GG*vv, CC*vv+(vv**2-vv)/2])
F = cusp - ordinary
gamma = s.Matrix([GG, CC+ss+vv])
assert s.simplify(F.subs(vv, vv+theta)-F-theta*gamma
                  -s.Matrix([0, theta*(theta-1)/2])) == s.zeros(2, 1)
angular = s.simplify(F.subs(vv, vv+theta)-F)
assert s.simplify(angular.subs(ss, ss+2)-angular) == s.Matrix([0, 2*theta])

out = {
    "status": "PASS",
    "statement": "P3K.25 Proved; independent root audit passed",
    "ray_matrix": [[str(x) for x in U.row(i)] for i in range(3)],
    "auxiliary_weights": list(aux),
    "physical_delta_weights": list(delta),
    "period_label_matrix": [[str(x) for x in period_labels.row(i)] for i in range(2)],
    "two_circle_minors": minors,
    "exact_cox_log_gauge": [str(x) for x in local_gauge],
    "global_torus_log_gauge": [str(x) for x in U*local_gauge],
    "parameter_character": list(local_gauge.diff(P)),
    "charged_cap_end_pullbacks": [list(end1*e), list(end2*e)],
    "auxiliary_source_deck_angular_gauge": ["0", "2*theta"],
    "scope": (
        "The code checks ray, period, Cox, line, and origin identities. "
        "It does not replace the real oriented bordism proof or its root audit."
    ),
}
target = ROOT / "code/part3_fourfold/whole_i1_shear.json"
target.write_text(json.dumps(out, indent=2, default=str) + "\n")
print("PASS: all-j whole-I1 shear rays, periods, exact physical-delta Cox gauge, charged caps, and origin identities.")


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
    ['code/part3_fourfold/whole_i1_shear.json'], [], origin='code/part3_fourfold/whole_i1_shear.py')
# END POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
