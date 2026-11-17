#!/usr/bin/env python3
"""Export only the independently audited K29 scope."""
from pathlib import Path
from datetime import datetime, timezone
import json
import re

ROOT=Path(__file__).resolve().parents[2]
def read(rel, reason):
    with (ROOT/"records/literature_fourfold.md").open("a") as log:
        log.write("\n- "+datetime.now(timezone.utc).isoformat()+" — Opened own "
                  +rel+"; reason: "+reason
                  +"; material: audited K29 chain orientations, circle trace, "
                  "variation matrix, and original nonfixed derivative.\n")
    return (ROOT/rel).read_text()

rel="notes/part3_common_exterior_meridians.md"
source=read(rel,"export the scope independently passed by root before checkpoint09")
body=source.split("## 1. The common exterior and its oriented bases",1)[1]
body="## 1. The common exterior and its oriented bases"+body
body=body.split("## Audit record",1)[0]
statement=r"""
For the actual index-one cusp with its three complex double curves,
use positive complex normal meridians \(m_i\) and the relative dual
basis \(m_j\cdot D_i=\delta_{ji}\). The literal common-exterior map
under the flop of \(C_0\) is
\[
 m'_0=-m_0+2m_1+2m_2,\quad m'_1=m_1,\quad m'_2=m_2,
 \qquad D'_0=-D_0,\quad D'_j=D_j+2D_0\ (j=1,2).
\]
In a fan retaining the physical delta edge, the actual relative
return has variation \(\operatorname{diag}(v,0,0)\), where
\(v=k_{\rm Jin}\) in the stated complex-meridian dual basis.
For K22--27, \(v=-3d\). After the fixed-edge flop its exact
variation matrix is
\[
 v\begin{pmatrix}1&-2&-2\\-2&4&4\\-2&4&4\end{pmatrix}.
\]
The two original nonfixed curves have integer relative derivative
coefficient \(n_{\rm rel}=0\) in K23's specified product framing.
No relative Pontryagin coefficient after the fixed-edge flop is
assigned by this statement.
"""
audit=(
    "Root independently passed the reciprocal-section chain and its "
    "complex normal signs, the integral circle-trace kernel, variation "
    "symmetry, the corrected dual-cycle versus ordered-product sign, "
    "and the original nonfixed stable derivative. The frame recurrence "
    "after the fixed-edge flop is retained separately and is not included "
    "in this export."
)
(ROOT/rel).write_text(
    "# P3K.29. Proved: common-exterior meridians, circle trace, and relative variation\n\n"
    +statement.strip()+"\n\n"+body.strip()+"\n\n## Audit record\n\n"+audit+"\n")
def tex(text):
    text=re.sub(r"(?m)^## (.+)$",
        lambda m:r"\par\medskip\noindent\textbf{"+m.group(1)+r".}\enspace",text)
    text=re.sub(r"(?<![A-Za-z{])(?:notes|code)/[A-Za-z0-9_./-]+",
        lambda m:r"\path{"+m.group(0).rstrip(".")+"}"+("." if m.group(0).endswith(".") else ""),text)
    return text.strip()+"\n"
output=(r"\begin{statement}{P3K.29}{Proved}"+"\n"+tex(statement)
        +r"\end{statement}"+"\n"+r"\begin{proof}"+"\n"+tex(body)
        +r"\end{proof}"+"\n")
assert "#" not in output and "submitted" not in output.lower()
(ROOT/"notes/part3_common_exterior_meridians.tex").write_text(output)
mapping=json.loads(read("code/part3_fourfold/results_mapping.json",
                        "append only proved K29 maps and derivative vanishing"))
mapping["results"]=[r for r in mapping["results"] if r.get("id")!="P3K.29"]
mapping["results"].append({
    "id":"P3K.29","status":"Proved","item_of_prompt":"3.4",
    "statement":"Actual common-exterior flop meridian matrix, integral circle-trace variation kernel, exact transformed variation, and zero original nonfixed relative derivative.",
    "proof_file":rel,
    "latex_file":"notes/part3_common_exterior_meridians.tex",
    "code":"code/part3_fourfold/common_exterior_meridians.py",
    "output":"code/part3_fourfold/common_exterior_meridians.json",
    "meridian_matrix":[[-1,0,0],[2,1,0],[2,0,1]],
    "relative_matrix":[[-1,2,2],[0,1,0],[0,0,1]],
    "variation_initial":"diag(k_Jin,0,0)",
    "variation_after_fixed_flop_factor":[[1,-2,-2],[-2,4,4],[-2,4,4]],
    "nonfixed_relative_n":[0,0],
    "retained_limit":"No relative Pontryagin coefficient after the fixed-edge flop is assigned.",
    "audit":"Root independent audit passed before export."
})
(ROOT/"code/part3_fourfold/results_mapping.json").write_text(json.dumps(mapping,indent=2)+"\n")
print("Exported audited P3K.29 separately; retained the unassigned post-flop frame correction.")
