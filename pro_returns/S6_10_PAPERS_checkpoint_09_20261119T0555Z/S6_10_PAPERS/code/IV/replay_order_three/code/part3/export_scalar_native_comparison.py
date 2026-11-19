#!/usr/bin/env python3
"""Export the audited actual scalar C1/C2 comparisons as K62."""
from pathlib import Path
from datetime import datetime, timezone
import re, subprocess, json, hashlib, shutil

ROOT=Path(__file__).resolve().parents[2]
source=ROOT/"notes/part3_scalar_c1_native_arrow_working.md"
target=ROOT/"notes/part3_scalar_native_comparison.tex"
cert=json.loads((ROOT/"code/part3/scalar_c1_outer_marking.json").read_text())
assert cert["status"]=="PASS" and cert["check_count"]==39
stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
archive=ROOT/"records/attempts"/("k62_export_"+stamp)
archive.mkdir(parents=True,exist_ok=True)
shutil.copy2(source,archive/source.name)
if target.exists():shutil.copy2(target,archive/target.name)
text=source.read_text()
body=text[text.index("## SCN.1."):]
historical=body[body.index("## SCN.4."):body.index("## SCN.5.")]
body=body.replace(historical,"")
intro="""The preceding SCN.4 sentence saying that the missing map has not
been identified is retained as the earlier stage of this audit.
The following calculation now identifies an explicit outer
normal-line mismatch. The pre-addition file is retained under
records/attempts/scalar_c1_before_outer_marking.

"""
assert intro in body
body=body.replace(intro,"The following calculation identifies the outer normal-line mismatch.\n\n")
audit_paragraph=body[body.index("Root has passed the complete SCN.1--9 audit,"):]
body=body.replace(audit_paragraph,"")
body=re.sub(r"(?m)^## (.+)$",lambda m:r"\par\medskip\noindent\textbf{"+m.group(1)+r"}\par\nobreak",body)
body=re.sub(r"(?<![\w{/])(code/[A-Za-z0-9_./-]+|notes/[A-Za-z0-9_./-]+)",
 lambda m:r"\path{"+m.group(1).rstrip(".")+"}"+("." if m.group(1).endswith(".") else ""),body)
converted=subprocess.run(["pandoc","-f","markdown+tex_math_single_backslash+raw_tex","-t","latex","--wrap=preserve"],input=body,text=True,capture_output=True,check=True).stdout
statement=r"""
Retain the actual fixed-source whole-zero \(I_1\) scalar families,
their source and Cartier line, finite-root and annular cap maps,
physical delta circle, and specified forward parameter closing.
On their protected cusp disc the full marked periods are
\[
 h:(Z,V)\mapsto(\kappa(q)qZ,\alpha(q)V),\qquad
 B:(Z,V)\mapsto(g(q)Z,q\lambda\beta(q)V),
\]
with the displayed units independent of the scalar parameter.
Use the initial physical-vertical-edge fan and its labelled native
stars \(C_1,C_2\), with the coordinates constructed below.
For an integral scalar winding \(J\), including the actual
\(\lambda=r^M\) covers and either norm sign, the single native
relative free pairs are
\[
 (m_{C_1},n_{C_1})=(J,-J),\qquad
 (m_{C_2},n_{C_2})=(0,0).
 \tag{P3K.62.0}
\]
The actual first \(C_1\) flop changes the oriented central return
by \(-J\) in \(\Theta_7\cong\mathbb Z/28\). The actual first
\(C_2\) flop preserves that return and its integer characteristic
index. In particular the initial and reflected fan scalar
indices used in P3K.58 are equal by this explicit \(C_2\) map.

For \(C_1\), the two outer positive-Hopf normal coordinate maps
have determinant windings \(0\) and \(-2J\). This is the missing
outer line marking in P3K.25's earlier zero-correction argument.
For \(J\ne0\), the actual labelled delta-equivariant simultaneous
three-curve plumbing product invoked in P3K.29 is obstructed by
its full normal determinant square. The local topology and
single-star frame maps remain the ones used below. This statement
does not assign a universal all-fan formula.
"""
out=r"\subsection{The actual scalar native stars and the outer line correction}"+"\n"+r"\begin{statement}{P3K.62}{Proved}"+"\n"+statement+r"\end{statement}"+"\n"+r"\begin{proof}"+"\n"+converted+r"\end{proof}"+"\n"
for bad in (r"\^{}",r"\textbackslash",r"\textsuperscript{"):assert bad not in out,bad
target.write_text(out)
pre=(ROOT/"code/part3/k60_standalone.tex").read_text().split(r"\begin{document}")[0]
(ROOT/"code/part3/k62_standalone.tex").write_text(pre+"\n"+r"\begin{document}"+"\n"+r"\input{notes/part3_scalar_native_comparison.tex}"+"\n"+r"\end{document}"+"\n")
manifest={"utc":datetime.now(timezone.utc).isoformat(),"statement":"P3K.62","source":str(source.relative_to(ROOT)),"source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),"latex":str(target.relative_to(ROOT)),"proof_sections":["SCN.1","SCN.2","SCN.3","SCN.5","SCN.6","SCN.7","SCN.8","SCN.9","SCN.10"],"historical_only_section_retained_in_archive":"SCN.4","proof_content_omitted":False,"audit_provenance_retained_in_working_source_and_manifest":audit_paragraph,"archive":str(archive.relative_to(ROOT)),"certificate":"code/part3/scalar_c1_outer_marking.json","main_input_modified":False}
(ROOT/"records/k62_export_manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
p=ROOT/"code/part3/results_mapping.json"
mapping=json.loads(p.read_text())
extra=mapping.setdefault("additional_source_loop_results",[])
detail={"id":"P3K.62","status":"Proved","item_of_prompt":"3.4","proof":str(source.relative_to(ROOT)),"latex_file":str(target.relative_to(ROOT)),"certificate":manifest["certificate"],"statement":"Actual first scalar C1 and C2 native returns and outer line marking; initial/reflected C2 characteristic equality.","C1_native_pair":"(J,-J)","C2_native_pair":"(0,0)","first_flop_changes":"C1:-J; C2:0","scope":"Exact initial native stars; no universal all-fan formula."}
if isinstance(extra,list):
 extra[:]=[row for row in extra if not isinstance(row,dict) or row.get("id")!="P3K.62"]
 extra.append(detail)
else:extra["P3K.62"]=detail
p.write_text(json.dumps(mapping,indent=2)+"\n")
print("Exported full K62, actual C1/C2 comparison; maininput untouched.")
