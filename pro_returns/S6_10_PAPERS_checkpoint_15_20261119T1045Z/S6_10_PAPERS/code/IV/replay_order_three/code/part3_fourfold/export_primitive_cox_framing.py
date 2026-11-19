#!/usr/bin/env python3
"""Export the full reviewed K27 comparison and its rotating clutch."""
from pathlib import Path
from datetime import datetime, timezone
import json
import re

ROOT=Path(__file__).resolve().parents[2]
def read(rel, reason):
    with (ROOT/"records/literature_fourfold.md").open("a") as log:
        log.write("\n- "+datetime.now(timezone.utc).isoformat()
                  +" — Opened own "+rel+"; reason: "+reason
                  +"; material: complete reviewed K27 normal comparison and actual degree-one clutch.\n")
    return (ROOT/rel).read_text()

rel="notes/part3_primitive_cox_framing.md"
source=read(rel,"export the independently root-audited proof separately")
rotating=read("notes/part3_primitive_rotating_integers.md",
              "include the full actual rotating-frame calculation rather than cite it")
clutch=rotating.split("## The actual frame comparison\n",1)[1].split(
    "## Characteristic numbers in this framing",1)[0].strip()
source=source.replace(
    "# P3K.27. Primitive scalar families: rotating/Cox normal comparison submitted for audit",
    "# P3K.27. Proved: primitive scalar families and their actual rotating Cox normal framing"
)
source=source.replace(
    "This draft identifies the normal product used in the K22 rotating\n"
    "calculation with the actual cusp product used in the K23 fixed-edge\n"
    "comparison. It retains the real orbit extension of the radial\n"
    "\\(|q|^\\theta\\) factor through the node. The statement is not yet\n"
    "exported to the manuscript.\n\n",
    ""
)
old=("The full degree-one normal-clutch calculation, saved in\n"
     "notes/part3_primitive_rotating_integers.md, gives\n"
     "\\(p_1(\\bar\\nu)=0\\). The actual K22 page has\n")
new=("We include the complete degree-one normal-clutch calculation "
     "in the actual matched framing.\n\n"+clutch+"\n\n"
     "The actual K22 page has\n")
if old in source:
    source=source.replace(old,new)
else:
    assert "We include the complete degree-one normal-clutch calculation" in source
source=source.replace("This proves the proposed\n","This proves the\n")
source=source.split("## Audit boundary",1)[0].split("## Audit record",1)[0]
source+=(
    "\n## Audit record\n\n"
    "Root independently checked the exact origins, representative-cell "
    "closing, annular transition, positive node product, quaternion "
    "overlap, physical Hopf orientation, and complete rotating clutch. "
    "Checks independently verified the same actual family comparison and "
    "the literal bounded unitary identity \\(q_{\\rm H}\\mapsto A q_{\\rm H}B\\). "
    "The root audit passed before export. The exact symbolic certificate "
    "is code/part3_fourfold/primitive_cox_framing.py and its JSON output; "
    "the degree-one clutch is also independently executed in "
    "code/part3_fourfold/primitive_normal_clutch.py.\n"
)
(ROOT/rel).write_text(source)

body=source.split("\n",1)[1]
statement,proof=body.split("## 1. The actual two products and their literal transition",1)
proof="## 1. The actual two products and their literal transition\n"+proof
proof,audit=proof.split("## Audit record",1)
def tex(text):
    text=re.sub(r"(?m)^## (.+)$",
                lambda m:r"\par\medskip\noindent\textbf{"+m.group(1)+r".}\enspace",
                text)
    text=re.sub(r"(?m)^# (.+)$",lambda m:r"\subsection{"+m.group(1)+"}",text)
    tick=chr(96)
    text=re.sub(tick+"([^"+tick+"]+)"+tick,
                lambda m:r"\path{"+m.group(1)+"}",text)
    text=re.sub(r"(?<![A-Za-z{])(?:notes|code)/[A-Za-z0-9_./-]+",
                lambda m:r"\path{"+m.group(0)+"}",text)
    return text.strip()+"\n"
output=(
    r"\begin{statement}{P3K.27}{Proved}"+"\n"+tex(statement)
    +r"\end{statement}"+"\n"
    +r"\begin{proof}"+"\n"+tex(proof)+r"\end{proof}"+"\n"
)
assert "#" not in output and "submitted" not in output.lower()
(ROOT/"notes/part3_primitive_cox_framing.tex").write_text(output)

mapping=json.loads(read("code/part3_fourfold/results_mapping.json",
                        "append the K27 actual framing result without changing prior rows"))
mapping["results"]=[row for row in mapping["results"] if row.get("id")!="P3K.27"]
mapping["results"].append({
    "id":"P3K.27","status":"Proved","item_of_prompt":"3.4",
    "statement":"The actual K22 cusp Cox product and rotating framing have zero free normal-gauge difference; k=-3d, ell=-24 and relative coordinates (6,3d-6,1-d/2).",
    "proof_file":rel,
    "latex_file":"notes/part3_primitive_cox_framing.tex",
    "code":"code/part3_fourfold/primitive_cox_framing.py",
    "output":"code/part3_fourfold/primitive_cox_framing.json",
    "rotating_clutch_code":"code/part3_fourfold/primitive_normal_clutch.py",
    "denominators":[8,14,20,30],
    "k":[-24,-42,-60,-90],"ell":[-24,-24,-24,-24],
    "relative_m":[6,6,6,6],"relative_n":[18,36,54,84],
    "central_classes_mod_28":[25,22,19,14],
    "retained_limit":"The actual relative four-cycle of a different finite-isotropy edge remains unassigned.",
    "audit":"Root checked the full marked normal comparison before export."
})
(ROOT/"code/part3_fourfold/results_mapping.json").write_text(json.dumps(mapping,indent=2)+"\n")
print("Exported complete root-audited P3K.27 separately, including the full degree-one clutch calculation.")
