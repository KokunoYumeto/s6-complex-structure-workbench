#!/usr/bin/env python3
"""Export the full audited canonical scalar vertical-fan proof as K64."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,shutil,subprocess

ROOT=Path(__file__).resolve().parents[2]
source=ROOT/"notes/part3_scalar_vertical_fans_working.md"
target=ROOT/"notes/part3_scalar_vertical_fans.tex"
cert=json.loads((ROOT/"code/part3/scalar_vertical_fans.json").read_text())
assert cert["status"]=="PASS" and cert["check_count"]==14 and len(cert["samples"])==425
audit=json.loads((ROOT/"records/checks_audit_scalar_vertical_fans.json").read_text())
assert audit["status"]=="PASS"
stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
archive=ROOT/"records/attempts"/("k64_export_"+stamp)
archive.mkdir(parents=True,exist_ok=True)
shutil.copy2(source,archive/source.name)
if target.exists():shutil.copy2(target,archive/target.name)
text=source.read_text()
body=text[text.index("## SV.1."):]
body=body.replace(r"\begin{split}",r"\begin{aligned}").replace(r"\end{split}",r"\end{aligned}")
body=re.sub(r"(?m)^## (.+)$",lambda m:r"\par\medskip\noindent\textbf{"+m.group(1)+r"}\par\nobreak",body)
body=re.sub(r"(?<![\w{/])(code/[A-Za-z0-9_./-]+)",
 lambda m:r"\path{"+m.group(1).rstrip(".")+"}"+("." if m.group(1).endswith(".") else ""),body)
converted=subprocess.run(["pandoc","-f","markdown+tex_math_single_backslash+raw_tex","-t","latex","--wrap=preserve"],input=body,text=True,capture_output=True,check=True).stdout
statement=r"""
Retain the actual canonical fixed-source scalar loops of the whole-zero
\(I_1\) constructions K22, K26, K28 and K32, with their source,
Cartier line, finite-root cap characters and complete annular maps.
The ordinary forward closing is its specified \(q^e\) times the
bounded source-independent unit, with the original cap arrow.
Write \(J\in\mathbb Z\) for the actual scalar winding, including
integer powers and inverse traversals of these constructed loops.
On the protected cusp disc keep
\[
 h:(Z,V)\mapsto(\kappa qZ,\alpha V),\qquad
 B:(Z,V)\mapsto(gZ,q\lambda\beta V),
\]
where \(\kappa,\alpha,g,\beta\) are independent of the scalar.
For every \(n\in\mathbb Z\), use the actual periodic fan \(T_n\)
whose edge directions are
\[
                    e_2,\qquad (1,n),\qquad(1,n-1).
\]
The actual positive return on this fan has class
\[
        A_n=A_0-J\,\frac{n(n-1)}2
                  \quad\text{in }\Theta_7\cong\mathbb Z/28,
 \tag{P3K.64.0}
\]
where \(A_0\) is the independently constructed initial return.
Its native relative free pairs on the two nonfixed stars are
\[
 \begin{array}{c|cc}
  &m_{\rm rel}&n_{\rm rel}\\ \hline
 C_1&J(1-n)&J(n-1)\\
 C_2&nJ&-nJ.
 \end{array}
\]
The actual \(C_1\) flip goes from \(T_n\) to \(T_{n-1}\);
the actual \(C_2\) flip goes from \(T_n\) to \(T_{n+1}\).
All periods, bounded-unit seams and cap maps are retained by
the explicit arrows in the proof. This statement covers this
vertical line of fans and these canonical closing maps; it
does not supply an arbitrary-fan formula or a shorter-loop
comparison with an additional source-translation endpoint.
"""
out=r"\subsection{Canonical scalar returns on all physical-vertical-edge fans}"+"\n"+r"\begin{statement}{P3K.64}{Proved}"+"\n"+statement+r"\end{statement}"+"\n"+r"\begin{proof}"+"\n"+converted+r"\end{proof}"+"\n"
for bad in (r"\^{}",r"\textbackslash",r"\textsuperscript{"):assert bad not in out,bad
target.write_text(out)
pre=(ROOT/"code/part3/k62_standalone.tex").read_text().split(r"\begin{document}")[0]
(ROOT/"code/part3/k64_standalone.tex").write_text(pre+"\n"+r"\begin{document}"+"\n"+r"\input{notes/part3_scalar_vertical_fans.tex}"+"\n"+r"\end{document}"+"\n")
manifest={"utc":datetime.now(timezone.utc).isoformat(),"statement":"P3K.64","source":str(source.relative_to(ROOT)),"source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),"latex":str(target.relative_to(ROOT)),"proof_sections":["SV.1","SV.2","SV.3"],"proof_content_omitted":False,"archive":str(archive.relative_to(ROOT)),"certificate":"code/part3/scalar_vertical_fans.json","peer_audit":"records/checks_audit_scalar_vertical_fans.json","root_audit":"records/root_audit_scalar_vertical_fans.json","layout_changes":["Replace split by aligned in display groups with multiple alignment pairs; all mathematical tokens and ordering retained."],"main_input_modified":False}
(ROOT/"records/k64_export_manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
p=ROOT/"code/part3/results_mapping.json"
mapping=json.loads(p.read_text())
extra=mapping.setdefault("additional_source_loop_results",[])
detail={"id":"P3K.64","status":"Proved","item_of_prompt":"3.4","proof":str(source.relative_to(ROOT)),"latex_file":str(target.relative_to(ROOT)),"certificate":manifest["certificate"],"peer_audit":manifest["peer_audit"],"statement":"Actual canonical scalar family on the complete physical-vertical-edge fan line.","class":"A_n=A_0-J*n*(n-1)/2 mod28","C1_native_pair":"(J*(1-n),J*(n-1))","C2_native_pair":"(n*J,-n*J)","scope":"Canonical q^e closing with prescribed source-independent unit; no arbitrary-fan or additional source-translation endpoint claim."}
if isinstance(extra,list):
 extra[:]=[row for row in extra if not isinstance(row,dict) or row.get("id")!="P3K.64"]
 extra.append(detail)
else:extra["P3K.64"]=detail
p.write_text(json.dumps(mapping,indent=2)+"\n")
print("Exported full K64 / SV.1–3, 14 exact checks and 425 signed instances; maininput untouched.")
