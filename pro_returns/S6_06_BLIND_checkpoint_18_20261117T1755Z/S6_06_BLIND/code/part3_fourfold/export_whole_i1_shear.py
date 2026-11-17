#!/usr/bin/env python3
"""Export audited P3K.25 separately, preserving the existing main include."""
from pathlib import Path
from datetime import datetime, timezone
import json
import re

ROOT = Path(__file__).resolve().parents[2]
def read_logged(rel, reason):
    with (ROOT / "records/literature_fourfold.md").open("a") as log:
        log.write("\n- " + datetime.now(timezone.utc).isoformat()
                  + " — Opened own " + rel + "; reason: " + reason
                  + "; material: the exact reviewed P3K.25 proof and result metadata.\n")
    return (ROOT / rel).read_text()

source = read_logged(
    "notes/part3_whole_i1_shear.md",
    "export the root-audited statement in a separate TeX include"
)
body = source.split("\n", 1)[1]
marker = "**Proof: the literal square chart and the unchanged period group.**"
statement, proof = body.split(marker, 1)
proof, after = proof.split("**End of proof.**", 1)
proof = marker + proof

def tex(text):
    text = re.sub(
        r"\*\*Proof: (.*?)\.\*\*",
        lambda m: r"\par\medskip\noindent\textbf{"
                  + m.group(1)[0].upper() + m.group(1)[1:]
                  + r".}\enspace",
        text
    )
    tick = chr(96)
    text = re.sub(tick + "([^" + tick + "]+)" + tick,
                  lambda m: r"\path{" + m.group(1) + "}", text)
    text = re.sub(r"(?m)^## (.+)$", lambda m: r"\subsection{" + m.group(1) + "}", text)
    text = text.replace("notes/part3_nodal_page_repair.md",
                        r"\path{notes/part3_nodal_page_repair.md}")
    text = text.replace("code/part3_fourfold/whole_i1_shear.py",
                        r"\path{code/part3_fourfold/whole_i1_shear.py}")
    return text.strip() + "\n"

output = (
    r"\begin{statement}{P3K.25}{Proved}" + "\n" + tex(statement)
    + r"\end{statement}" + "\n"
    + r"\begin{proof}" + "\n" + tex(proof)
    + r"\end{proof}" + "\n"
    + tex(after)
)
assert "#" not in output
assert "submitted" not in output.lower()
(ROOT / "notes/part3_whole_i1_shear.tex").write_text(output)

mapping = json.loads(read_logged(
    "code/part3_fourfold/results_mapping.json",
    "append the separately audited shear theorem without altering previous rows"
))
mapping["results"] = [r for r in mapping["results"] if r.get("id") != "P3K.25"]
mapping["results"].append({
    "id": "P3K.25",
    "status": "Proved",
    "item_of_prompt": "3.4",
    "statement": (
        "For every K10/K22 scalar family, all cusp fans retaining the physical "
        "delta edge have the same actual return index and oriented seven-sphere class."
    ),
    "fan_directions": ["e2", "e1-j*e2", "e1-(j+1)*e2"],
    "parameter_scope": "The actual positive scalar loop and original period/cap maps",
    "indices": [-3, -6, -9, -14],
    "oriented_classes_mod_28": [25, 22, 19, 14],
    "proof_file": "notes/part3_whole_i1_shear.md",
    "latex_file": "notes/part3_whole_i1_shear.tex",
    "code": "code/part3_fourfold/whole_i1_shear.py",
    "output": "code/part3_fourfold/whole_i1_shear.json",
    "retained_limit": "No return value or Jin integer assigned to finite-isotropy fan branches.",
    "audit": "Root independently passed the exact period/Cox/joint-cap comparison."
})
(ROOT / "code/part3_fourfold/results_mapping.json").write_text(
    json.dumps(mapping, indent=2) + "\n"
)
print("Exported root-audited P3K.25 separately and appended its result mapping.")


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
    ['code/part3_fourfold/results_mapping.json'], ['notes/part3_whole_i1_shear.tex'], origin='code/part3_fourfold/export_whole_i1_shear.py')
# END POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
