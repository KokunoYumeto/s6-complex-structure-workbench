"""Install the exact union of frozen P1.18 geometric and analytic proofs.

No original checking code is used.  This script changes only the named proof
block and its existing opening rung; every prior block is preserved verbatim.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
A = ROOT / "analysis/continuation_V"
sha = lambda b: hashlib.sha256(b).hexdigest()
prefix = (A / "P1_18_geometric_prefix.tex").read_text()
suffix = (A / "P1_18_geometric_suffix.tex").read_text()
insert_path = ROOT / "analysis/continuation_VI/P1_18_analytic_current_insert.tex"
insert = insert_path.read_text()
original_insert_sha = sha(insert.encode())
# Keep the scalar notation identical to the geometric proof: k=1/c_0.
insert = insert.replace("h=k(cv-d)", "h=c_0(cv-d)")
insert = insert.replace("$k=96/(625\\pi)$", "$c_0=96/(625\\pi)$")
insert = insert.replace("h_a&=k(", "h_a&=c_0(")
insert = insert.replace("h_{ab}&=k(", "h_{ab}&=c_0(")
# Preserve the meanings of the pre-existing manual equation tags.
needle = " U'=U\\frac{\\sum_{j=0}^{m-1}B_jz^j}{1+z^m},\\qquad U(0)=I.\n\\]"
assert needle in insert
insert = insert.replace(needle, needle[:-3] + "\\tag{1.18.2}\n\\]", 1)
needle = " \\tau_N(r;R)=K(R)\\frac{(r/R)^{N+1}}{1-r/R}.\n\\]"
assert needle in insert
insert = insert.replace(needle, needle[:-3] + "\\tag{1.18.3}\n\\]", 1)
needle = "For $M=B_{\\max}/D_{\\rm lower}$, radial Gronwall and Cauchy"
assert needle in insert
majorant = r"""The actual complete-domain code uses the further upper bound
\[
 \widehat B_{\max}=\sum_{k=0}^4\|B_k\|_w
                           (|z_c|+R_{\rm loc})^k.
\]
To see the exact comparison, substitute the displayed formula for
$\widetilde B_l$ in each row sum and use the triangle inequality.
Reindex the finite set $0\le l\le k\le4$ by $(l,k)\mapsto(k,l)$.
The sum in $l$ is
$\sum_{l=0}^k\binom kl|z_c|^{k-l}R_{\rm loc}^l
=(|z_c|+R_{\rm loc})^k$.
Each remaining row sum is at most $\|B_k\|_w$; taking the row
maximum afterward proves $B_{\max}\le\widehat B_{\max}$.
Thus the bound actually used below is
$M=\widehat B_{\max}/D_{\rm lower}$. Radial Gronwall and Cauchy"""
insert = insert.replace(needle, majorant, 1)
# End-of-proof computation attribution is already present in the suffix.
cut = "The complete domain certificate uses110-digit ball arithmetic and"
assert cut in insert
insert = insert[:insert.index(cut)].rstrip() + "\n"
proof = prefix.rstrip() + "\n\n" + insert + suffix
assert proof.count("\\begin{proof}") == proof.count("\\end{proof}") == 1
for n in range(2,7):
    assert proof.count(f"\\tag{{1.18.{n}}}") == 1
revision = ROOT / "papers/V/revisions/P1_18_global_minimum_proof.tex"
revision.write_text(proof)

receipt = {
    "installed_utc": datetime.now(timezone.utc).isoformat(),
    "label": "night:P1.18",
    "revision": str(revision.relative_to(ROOT)),
    "revision_sha256": sha(proof.encode()),
    "proof_sha256_without_final_newline": sha(proof.rstrip().encode()),
    "geometric_before_read": "analysis/continuation_root/P1_18_before_read.md",
    "analytic_before_read": "analysis/continuation_VI/P1_18_analytic_certificates_before_read.md",
    "majorant_before_read": "analysis/continuation_V_ledger/P1_18_polynomial_majorant_before_read.md",
    "analytic_insert_before_copy_sha256": original_insert_sha,
    "analytic_insert_changes": [
        "Scalar k in the implicit-system paragraph renamed c_0 to retain the reciprocal convention of the geometric proof.",
        "Existing connection and tail equation tags 1.18.2 and 1.18.3 retained with the same mathematical meanings.",
        "Actual unshifted collar numerator bound inserted from ledger's frozen finite reindexing derivation.",
        "Duplicated final computation-attribution paragraph moved to the final geometric item.",
    ],
    "replacement_reason": "Print the complete union of frozen geometric, analytic and finite-norm-map derivations, together with current independently authored numerical methods, counts, exact maps and precise endpoints. The former numerical proof routes and all prior constants are preserved; no invalidity claim follows merely from using a new independently derived route.",
    "equation_anchor_audit": {},
    "files": [],
    "status": "installed; current aggregate reviewer comparison pending",
}

for rel in ["papers/V/body.tex", "papers/V/body_source.tex", "S6_10_PAPERS_V.tex"]:
    p = ROOT / rel
    text = p.read_text()
    marker = "\\label{night:P1.18}"
    pos = text.index(marker)
    lo = text.index("\\begin{proof}", pos)
    hi = text.index("\\end{proof}", lo) + len("\\end{proof}")
    old = text[lo:hi]
    out = A / ("P1_18_superseded_" + rel.replace("/", "_"))
    assert not out.exists(), "Do not overwrite the preserved prior proof"
    out.write_text(old + "\n")
    receipt["equation_anchor_audit"][rel] = {
        str(n): [m.start() for m in re.finditer(re.escape(f"1.18.{n}"), text[:lo]+text[hi:])]
        for n in range(2,7)
    }
    changed = text[:lo] + proof.rstrip() + text[hi:]
    p.write_text(changed)
    receipt["files"].append({
        "path": rel,
        "old_proof_sha256": sha(old.encode()),
        "preserved_path": str(out.relative_to(ROOT)),
        "new_proof_sha256": sha(proof.rstrip().encode()),
        "file_sha256": sha(changed.encode()),
    })

opening = ROOT / "papers/V/opening.tex"
text = opening.read_text()
old = r"""\item The ball-arithmetic proof covers the two finite root discs,
  the intervening collar and the cusp annulus, and proves that $h_b$
  has its unique minimum at the infinity root point.  The local
  positive Hessian proves strictness there; the remaining rectangles
  have strict certified lower bounds.  Thus the transversality test
  gives exactly $\mathcal U$ (\cref{night:P1.18})."""
new = r"""\item The real coordinate and marked deck maps preserve the normalized
  height. The infinity-root rotation fixes its differential at zero;
  an invertible real system and the positive Hessian prove a strict
  local minimum. Convergent root and cusp series and exact collar
  continuation enclose all12911 leaves of the closed covers above
  that value. The actual cusp graph has a positive determinant on
  the remaining inner disc and tends to positive height without
  bound. These maps prove the unique global minimum and identify
  the transversality domain exactly with $\mathcal U$
  (\cref{night:P1.18}, proof, items1--7)."""
assert old in text
(A / "P1_18_superseded_opening_rung.tex").write_text(old + "\n")
opening.write_text(text.replace(old,new,1))
receipt["opening"] = {"old_sha256":sha(old.encode()),"new_sha256":sha(new.encode()),"current_path":"papers/V/opening.tex"}
(A / "P1_18_replacement_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({"status":receipt["status"],"proof_sha256":receipt["proof_sha256_without_final_newline"],"bytes":len(proof.encode()),"files":len(receipt["files"])}))
