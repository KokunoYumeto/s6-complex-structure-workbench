#!/usr/bin/env python3
"""Export the fully audited actual-fan recurrence as separate P3K.31."""
from pathlib import Path
from datetime import datetime, timezone
import json
import re

ROOT=Path(__file__).resolve().parents[2]
def read(rel,reason):
    with (ROOT/"records/literature_fourfold.md").open("a") as log:
        log.write("\n- "+datetime.now(timezone.utc).isoformat()
                  +" — Opened own "+rel+"; reason: "+reason
                  +"; material: fully audited actual stable-frame morphisms, "
                  "complex-normal reset, integral recurrence and all-fan class formula.\n")
    return (ROOT/rel).read_text()
rel="notes/part3_common_exterior_frame_recurrence.md"
source=read(rel,"promote the root/blind/checks independently passed recurrence as P3K.31")
body="## 1. The three exact objects that must be transported"+source.split(
    "## 1. The three exact objects that must be transported",1)[1]
body=body.split("## Audit record",1)[0]
body=body.replace(
    "This is a derived consequence of (CF.18), still submitted\n"
    "for audit with that recurrence.\n",
    "We now derive the closed formula from the actual recurrence.\n")
body=body.replace(
    "No formula in this working note is\n"
    "promoted before the literal frame comparisons above\n"
    "have passed independent audit.",
    "The actual frame and periodic flop morphisms above prove these values.")
body=body.replace(
    "These arithmetic outputs have the same working\n"
    "geometric-audit status as (CF.18). Their executable\n",
    "These are the exact arithmetic ranges of the proved\n"
    "geometric formula. Their executable\n")
body=body.replace("(CF.", "(P3K.31.").replace(r"\tag{CF.",r"\tag{P3K.31.")
body=body.replace("in this note.", "in this statement.")
statement=r"""
For every actual family and positive parameter loop of P3K.27 or
P3K.30, retain its physical delta cocharacter and all exterior
gluings, and use any allowed index-one periodic unimodular cusp
fan \(T(v,w)\). Write
\[
 \delta_{\rm circle}=r v+s w,\qquad
 S=r^2-rs+s^2,\qquad \gcd(r,s)=1.
\]
Let \(k,\ell,A=(4k-\ell)/24\) be the initial vertical-edge
integers in the actual Cox framing of those statements.
The oriented return class for the specified fan is
\[
 [\Sigma_{\Phi,T}]
    =A+\frac{\ell}{8}(S-1)-\frac{k}{8}(S^2-1)
        \pmod{28}.                                      \tag{P3K.31.0}
\]
The expression is integral. It is computed by the actual common
exterior, stable tangent-frame change, and complex normal reset
through every periodic flop.

For K27 this becomes
\[
           4-3S+\frac d8(3S^2-7)\pmod{28},
       \qquad d=8,14,20,30.
\]
For K30, with its proved \(H=Ma^2/d\) and page Euler characteristic
\(\chi\), it becomes
\[
                 \chi(4-3S)+\frac H8(3S^2-7)\pmod{28}.
\]
The letter \(a\) in \(H\) retains K30's line-section coefficient;
the displayed cocharacter coordinates are the coordinates of the
chosen fan. The exact finite ranges for K27 are given in the proof.
 The original construction's single \(w\)-loop is treated separately
 in P3K.33 by its explicit simultaneous endpoint descent. No cover
 class is divided.
"""
# Avoid reusing a for the source line and the fan coordinate in the formal theorem.
statement=statement.replace(
    r"\delta_{\rm circle}=a v+b w,"+"\n"+r" S=a^2-ab+b^2,\qquad \gcd(a,b)=1.",
    r"\delta_{\rm circle}=r v+s w,"+"\n"+r" S=r^2-rs+s^2,\qquad \gcd(r,s)=1.")
statement=statement.replace(
    "The letter \\(a\\) in \\(H\\) retains K30's line-section coefficient;\n"
    "the displayed cocharacter coordinates are the coordinates of the\n"
    "chosen fan. ","")
audit=(
    "The root audit passed the full proof, including the +1 first normal "
    "product, the reflected second normal product, the actual degree -2 "
    "adjoint derivative, the matrix order giving ambient degree +2, the "
    "anti-quaternion reset and its central orientation, the recurrence "
    "and the finite primitive-residue range. Blind and checks each "
    "independently passed Sections 2–4. The requested actual triangular "
    "source-normal derivative and its homotopy were added before promotion. "
    "P3K.33 subsequently supplies the explicit original single-w-loop descent."
)
(ROOT/rel).write_text(
    "# P3K.31. Proved: the actual return class for every index-one cusp fan\n\n"
    +statement.strip()+"\n\n"+body.strip()+"\n\n## Audit record\n\n"+audit+"\n")
def tex(text):
    lines=text.splitlines()
    out=[]; i=0
    while i<len(lines):
        line=lines[i]
        if line.startswith("|"):
            rows=[]
            while i<len(lines) and lines[i].startswith("|"):
                cells=[s.strip() for s in lines[i].strip("|").split("|")]
                if not all(re.fullmatch(r"[: -]+",s or "-") for s in cells):
                    rows.append(cells)
                i+=1
            out.append(r"\begin{center}\begin{tabular}{c p{0.78\linewidth}}\toprule")
            for j,cells in enumerate(rows):
                out.append(" & ".join(cells)+r"\\")
                if j==0: out.append(r"\midrule")
            out.append(r"\bottomrule\end{tabular}\end{center}")
            continue
        if line.startswith("## "):
            out.append(r"\par\medskip\noindent\textbf{"+line[3:]+r".}\enspace")
        else:
            out.append(line)
        i+=1
    value="\n".join(out)
    value=re.sub(r"(?<![A-Za-z{])(?:notes|code)/[A-Za-z0-9_./-]+",
                 lambda m:r"\path{"+m.group(0).rstrip(".")+"}"
                 +("." if m.group(0).endswith(".") else ""),value)
    return value.strip()+"\n"
output=(r"\begin{statement}{P3K.31}{Proved}"+"\n"+tex(statement)
        +r"\end{statement}"+"\n"+r"\begin{proof}"+"\n"+tex(body)
        +r"\end{proof}"+"\n")
assert "#" not in output
assert "submitted" not in output.lower() and "working" not in output.lower()
(ROOT/"notes/part3_common_exterior_frame_recurrence.tex").write_text(output)
mapping=json.loads(read("code/part3_fourfold/results_mapping.json",
                        "append proved K31 without changing other statements"))
mapping["results"]=[x for x in mapping["results"] if x.get("id")!="P3K.31"]
mapping["results"].append({
    "id":"P3K.31","status":"Proved","item_of_prompt":"3.4",
    "statement":"For every index-one cusp fan of the actual K27/K30 loop, the oriented return class is A+ell*(S-1)/8-k*(S^2-1)/8 mod28, with S the primitive physical-cocharacter Eisenstein norm.",
    "proof_file":rel,"latex_file":"notes/part3_common_exterior_frame_recurrence.tex",
    "code":"code/part3_fourfold/common_exterior_frame_recurrence.py",
    "output":"code/part3_fourfold/common_exterior_frame_recurrence.json",
    "ambient_frame_change":"2 e_i",
    "recurrence":["V'=M_i V M_i^T","delta'=M_i(delta-2V e_i)",
                  "s'=s+(delta_i-V_ii)/2 mod28"],
    "K27_class_ranges":{
        "8":[1,3,5,11,15,17,19,25],
        "14":list(range(0,28,2)),
        "20":[3,5,7,11,17,19,21,25],
        "30":[0,4,6,8,14,18,20,22]},
    "original_loop":"P3K.33 proves the original single-w-loop simultaneous Cox endpoint descent by actual integral cochains and chart maps, without dividing a cover class.",
    "audit":"Root, blind, and checks independently passed the exact frame maps and signs."
})
(ROOT/"code/part3_fourfold/results_mapping.json").write_text(json.dumps(mapping,indent=2)+"\n")
print("Exported fully audited P3K.31 separately, retaining the exact original-loop descent scope.")


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
    ['code/part3_fourfold/results_mapping.json'], ['notes/part3_common_exterior_frame_recurrence.tex'], origin='code/part3_fourfold/export_common_exterior_frame_recurrence.py')
# END POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
