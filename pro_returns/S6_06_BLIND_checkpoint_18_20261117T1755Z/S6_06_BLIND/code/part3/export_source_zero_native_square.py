#!/usr/bin/env python3
"""Export the audited actual source-zero native square as P3K.60."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
source = ROOT/"notes/part3_source_zero_double_loop_product_working.md"
target = ROOT/"notes/part3_source_zero_native_square.tex"
cert_path = ROOT/"code/part3/source_zero_double_loop_product.json"
cert = json.loads(cert_path.read_text())
assert cert["status"] == "PASS_EXACT_IDENTITIES"
assert cert["checks"] == 59
assert cert["geometric_audit_status"] == "PASS root and checks"
for audit in ("records/root_audit_source_zero_native_square.json",
              "records/checks_audit_source_zero_double_loop_product.json"):
    assert json.loads((ROOT/audit).read_text())["status"] == "PASS"

stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
archive = ROOT/"records/attempts"/f"k60_export_{stamp}"
archive.mkdir(parents=True, exist_ok=True)
shutil.copy2(source, archive/source.name)
if target.exists():
    shutil.copy2(target, archive/target.name)

text = source.read_text()
body = text[text.index("## DZ.1."): ]
body = re.sub(
    r"(?m)^## (.+)$",
    lambda m: r"\par\medskip\noindent\textbf{"+m.group(1)+r"}\par\nobreak",
    body,
)
converted = subprocess.run(
    ["pandoc", "-f", "markdown+tex_math_single_backslash+raw_tex",
     "-t", "latex", "--wrap=preserve"],
    input=body, text=True, capture_output=True, check=True,
).stdout

statement = r"""
Retain P3K.58's actual marked source, section, scalar and selected height
\[
 Y^2=X^3+(1-2v)X^2+TX+v^2,\qquad G=(0,v),\qquad
 q=T-(v^2-2v),\qquad \lambda=v^{km}\lambda_0 .
\]
The one III-star cap has
\[
 (a,b,m)=(1,2,4p)\quad\text{or}\quad(2,1,4p-1),
 \qquad p,k\ge1,\qquad n=\pm1 .
\]
Keep its complete root, Cartier line, finite character, reference
annular map and integer cochain. No additional logarithmic disc
meets either colliding finite site. Let \(\mathcal T\) be the initial
physical-vertical-edge fan, and \(J\mathcal T\) its opposite-diagonal
reflection. The positive source-zero loop is the positive \(v\)-loop
with the literal scalar above.

In the single native diagonal-star product constructed below, its
actual relative return has free coordinates
\[
                              (m_{\rm rel},n_{\rm rel})=(1-a,a).
\]
The actual single-loop Cox flop therefore gives
\[
                   [Z_{J\mathcal T}]-[Z_{\mathcal T}]
                                  =a\quad\text{in }\Theta_7\cong\mathbb Z/28.
\]
The proof constructs the single native product, its literal pullback
to the double parameter cover, and a closed ordinary product of
the doubled three-curve plumbing. It identifies the actual relative
square before using the two torsion-free integer coordinates.

Together with P3K.58's proved paired sum and its P3K.57 dependency,
the pair of actual returns is constrained exactly to
\[
 \bigl([Z_{\mathcal T}],[Z_{J\mathcal T}]\bigr)
   =\bigl(-a+kA_{\rm scalar}+14e,\ kA_{\rm scalar}+14e\bigr),
       \qquad e\in\{0,1\},
\]
where
\[
 A_{\rm scalar}=
 \begin{cases}
 0,&(a,b,m)=(1,2,4p),\\
 1-3p,&(a,b,m)=(2,1,4p-1).
 \end{cases}
\]
The same \(e\) occurs in the two entries of a given pair. Its value
is not selected, and no class in \(\Theta_7\) is divided by two.
"""
out = (
    r"\subsection{The source-zero native square and the first diagonal flop}"
    "\n"+r"\begin{statement}{P3K.60}{Proved}"+"\n"
    +statement+r"\end{statement}"+"\n"
    +r"\begin{proof}"+"\n"+converted+r"\end{proof}"+"\n"
)
for forbidden in (r"\^{}", r"\textsuperscript{", r"\textbackslash"):
    assert forbidden not in out, forbidden
target.write_text(out)
pre = (ROOT/"code/part3/k58_standalone.tex").read_text().split(
    r"\begin{document}")[0]
(ROOT/"code/part3/k60_standalone.tex").write_text(
    pre+"\n"+r"\begin{document}"+"\n"
    +r"\input{notes/part3_source_zero_native_square.tex}"+"\n"
    +r"\end{document}"+"\n"
)

manifest = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "statement": "P3K.60",
    "source": str(source.relative_to(ROOT)),
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "latex": str(target.relative_to(ROOT)),
    "proof_sections": [f"DZ.{i}" for i in range(1, 7)],
    "proof_content_omitted": False,
    "layout_changes": [],
    "audits": ["records/root_audit_source_zero_native_square.json",
               "records/checks_audit_source_zero_double_loop_product.json"],
    "certificate": str(cert_path.relative_to(ROOT)),
    "archive": str(archive.relative_to(ROOT)),
    "main_input_modified": False,
}
(ROOT/"records/k60_export_manifest.json").write_text(
    json.dumps(manifest, indent=2)+"\n")
detail = {
    "id": "P3K.60", "status": "Proved", "item_of_prompt": "3.4",
    "proof": str(source.relative_to(ROOT)),
    "latex_file": str(target.relative_to(ROOT)),
    "certificate": str(cert_path.relative_to(ROOT)),
    "audits": manifest["audits"],
    "statement": "Actual single native C2 free pair, literal relative square, first diagonal-flop difference, and paired two-possibility corollary.",
    "native_free_pair": "(1-a,a)",
    "fan_difference": "Z_JT-Z_T=a mod28",
    "paired_values": "(-a+k*A_scalar+14e,k*A_scalar+14e), e in {0,1}",
    "unresolved": "The common order-two ambiguity e of each individual pair remains unselected.",
    "scope": "Exact one-III-star-cap initial/reflected source-zero families of P3K.58; no scalar C1 or broader-fan comparison.",
}
p = ROOT/"code/part3/results_mapping.json"
mapping = json.loads(p.read_text())
extra = mapping.setdefault("additional_source_loop_results", [])
if isinstance(extra, list):
    extra[:] = [row for row in extra
                if not isinstance(row, dict) or row.get("id") != "P3K.60"]
    extra.append(detail)
else:
    extra["P3K.60"] = detail
p.write_text(json.dumps(mapping, indent=2)+"\n")
print("Exported full audited P3K.60 / DZ.1–6, 59 exact checks; maininput untouched.")
