"""Apply the admitted KD support repair and publish the complete cyclic unit.

The separate KD dependency was outside required_progress_III and therefore
was not selected by the earlier required-packet application. Its admitted
event is already central. No independent-check credit is added here.
"""
from __future__ import annotations

from datetime import datetime, timezone
import json
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

path = u.WORK / "root/cyclic_homology.tex"
before = path.read_text(encoding="utf-8")
after = before
fields, defects = r.table(r.DEFECTS)
new_rows = []

def change(key, kind, old, new, reason, statement="maps:src:D.1.1"):
    global after
    ident = "III-C8-CYCLIC-" + key
    assert not any(row["change_id"] == ident for row in defects)
    assert after.count(old) == 1, key
    after = after.replace(old, new, 1)
    new_rows.append(dict(change_id=ident, type=kind, statement_id=statement,
        old_location="cyclic homology unit before publication pass", old_page="pending page concordance",
        new_location="Cyclic covers and integral homology", new_page="pending final PDF",
        old_text=old, new_text=new, reason=reason,
        review_status="source edit applied; whole readback and final page reading pending"))

guards = json.loads((u.ROOT / "agents/continuation5_iii_02kd/S6_SERIES_PUBLISH_III_02KD_guards.json").read_text())
assert len(guards) == 1
guard = guards[0]
change("KD-ADMITTED-COMPLETE-PROOF", "D22", guard["old"], guard["new"],
    "Apply the separately admitted support proof, omitted by the required-target-only packet selector. The central event publish:c5:III:02KD:completed-preserved-targeted-check records its prior whole admission. Root now read the complete current 6716-character proof, all 418 comparison lines, and all 400 receiving lines. Exact covering and finite-fibre maps, signed attachment and cycle-level splitting prove the unchanged full-range homology formula.",
    "maps:src:D.1.4")
change("HEADING", "D14",
    "\\section{The other six-manifolds}\n\\subsection{The cyclic covers: a necessary correction}",
    r"\subsection{Cyclic covers and integral homology}",
    "Move this complete prerequisite unit into the sphere-map section before the framing result which uses KD. Remove the research-oriented correction heading.")
opening = r"\begin{theorem}[Euler and homology of cyclic universal covers]"
definition = r"""\begin{definition}[The cyclic-cover notation]
\hypertarget{tag-Q008}{}\label{mapsIII:def:cyclic-cover}
{\normalfont\scriptsize tag Q008}\par
For an admissible marked member $X_p$, put
$p=12\ell_0-4\ell_1-3\ell_2$ and $d=|p|$.
Write $\widetilde X_p\to X_p$ for its universal covering and
$\widetilde W_p$ for the inverse image of the cusp $W$.
\end{definition}

"""
change("INPUT-DEFINITION", "D13", opening, definition + opening,
    "Give the shared admissible member, parameter and covering notation a numbered definition before all four results. The degree and compactness remain proved in K7, not assumed in the definition.")
for tag, label, title, new_title, dependencies in (
    ("02K7", "maps:src:D.1.1", "Euler and homology of cyclic universal covers", "Euler characteristic of cyclic covers", "the definitions and constructions stated in the proof"),
    ("02KB", "maps:src:D.1.2", "the cusp of the cyclic cover", "The cusp of a cyclic cover", r"\cite[Theorem~7.17, p.~57]{AC26}"),
    ("02KC", "maps:src:D.1.3", "the rational homology of the cover", "Rational homology and deck characters", "the definitions and constructions stated in the proof"),
    ("02KD", "maps:src:D.1.4", "the integral homology of the universal cover", "Integral homology of the universal cover", r"\SeriesRef{maps:src:D.1.3}"),
):
    change(tag + "-TITLE", "D16", "[" + title + "]", "[" + new_title + "]",
        "Use the mathematical subject and exact scope as the result title.", label)
    old = r"\StatementRecord{" + label + "}{proved}{" + tag + "}{" + dependencies + "}"
    change(tag + "-TAG", "D10", old, r"{\normalfont\scriptsize tag " + tag + r"}\par",
        "Replace the machine header by its existing small tag, keeping every anchor and label.", label)
change("K7-REPEATED-SCOPE", "D11",
    "For $d>1$, no universal cover in this family satisfies the\nvanishing-second-homology hypothesis of such a connected-sum criterion.\n", "",
    "The preceding positive-rank conclusion already gives the exact nonvanishing. Remove its second formulation as an exclusion from an unspecified criterion; keep the stated connected-sum obstruction and its Euler proof.")
change("K7-PROOF-OPEN", "D23",
    "\\begin{proof}\n\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=*]\n\\item Put $p=12\\ell_0-4\\ell_1-3\\ell_2$. Admissibility gives",
    "\\begin{proof}\nAdmissibility gives",
    "Remove the one-item machine-style enumeration and the parameter definition already supplied in Q008.")
change("K7-PROOF-END", "D23",
    "$\\#^4(S^3\\times S^3)$ has Euler characteristic $-6$.\n\\end{enumerate}\n\\end{proof}",
    "$\\#^4(S^3\\times S^3)$ has Euler characteristic $-6$.\n\\end{proof}",
    "Close the same single proof after its preserved complete admissible example.")
change("KB-ENUMERATION", "D23",
    r"\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]",
    r"\begin{enumerate}[label=\arabic*.,leftmargin=*]",
    "The two mathematical proof parts retain an ordinary numbered list.", "maps:src:D.1.2")
change("KB-GROUP-OWNER", "D12",
    r"""\item The presentation of the fundamental group in
\cite[Theorem~7.17, p.~57]{AC26} sends the regular-fibre lattice onto
$\mathbb Z/d$ by its primitive $\gamma$ coordinate. Write $z$ for that primitive generator. In this presentation,
$x=(4\ell_0-\ell_1-\ell_2)z$ and
$y=(\ell_1+\ell_2-3\ell_0)z$, and $z\mapsto1$ gives the inverse
cyclic identification. Admissibility makes $d$ coprime to six.""",
    r"""\item The presentation and inverse cyclic maps in
\cref{maps:src:D.1.1} send the regular-fibre lattice onto
$\mathbb Z/d$ by its primitive $\gamma$ coordinate.
Admissibility makes $d$ coprime to six.""",
    "Use the preceding complete group proof and its exact inverse maps instead of repeating its two solved peripheral words. The covering character and all subsequent branch maps are unchanged.", "maps:src:D.1.2")
for key, old, new in (
    ("QUOTIENT", "therefore the actual\nquotient map", "therefore the\nquotient map"),
    ("BASES", "The actual changes of component and edge bases are", "The changes of component and edge bases are"),
):
    change("KB-" + key, "D08", old, new,
        "State the displayed quotient or basis map directly; its complete inverse and proof remain.", "maps:src:D.1.2")

lifted = r"""\begin{definition}[The lifted fibre marking]
\hypertarget{tag-Q009}{}\label{mapsIII:def:lifted-fibre}
{\normalfont\scriptsize tag Q009}\par
Put
\[
 \Lambda_d=\mathbb Z\langle d\widehat\gamma,\widehat u,
                   \widehat w,\widehat\delta\rangle,
 \qquad F_d=\Lambda_{\mathbb R}/\Lambda_d.
\]
The coefficient map $L=\operatorname{diag}(d,1,1,1)$ identifies
$\mathbb Z^4$ with $\Lambda_d$; its inverse on that sublattice
divides the first coefficient by $d$. In this basis,
\[
 A_1^{(d)}=\begin{pmatrix}1&0&0&0\\6d&0&1&0\\-6d&-1&-1&0\\-2d&1&0&1\end{pmatrix},
 \qquad
 A_2^{(d)}=\begin{pmatrix}1&0&0&0\\0&0&-1&0\\-6d&1&0&0\\3d&0&1&1\end{pmatrix},
 \qquad A_j^{(d)}=L^{-1}A_jL.
\]
\end{definition}

"""
opening = r"\begin{theorem}[Integral homology of the universal cover]"
change("KD-MATRIX-DEFINITION", "D13", opening, lifted + opening,
    "Preserve the original proof's explicit two covering matrices, used by later invariant arguments, in a numbered input definition. Give both coefficient maps and the conjugation identity; the admitted replacement proof then uses that same lifted lattice.", "maps:src:D.1.4")
change("KD-PARAMETER-ELL", "D20",
    r"b_1=4l_0-l_1-l_2,\qquad b_2=l_1+l_2-3l_0.",
    r"b_1=4\ell_0-\ell_1-\ell_2,\qquad b_2=\ell_1+\ell_2-3\ell_0.",
    "Use the established glyph for the identical ordered parameter tuple; the coefficient map and its inverse are the identity on (ell0,ell1,ell2).", "maps:src:D.1.4")
for key, old, new in (
    ("TWIST", r"v_j=l_j\varepsilon_j+k_j\delta", r"v_j=\ell_j\varepsilon_j+k_j\delta"),
    ("RELATIONS", r"3b_1-l_1=p$, $4b_2-l_2=-p", r"3b_1-\ell_1=p$, $4b_2-\ell_2=-p"),
    ("SUM", "$b_1+b_2=l_0$", "$b_1+b_2=\\ell_0$"),
):
    change("KD-ELL-" + key, "D20", old, new,
        "Apply the same identity renaming of the unchanged integer parameter tuple at this exact occurrence.", "maps:src:D.1.4")
change("KD-REPEATED-CRITERION", "D11",
    "In particular a torsion-free classification theorem\ncannot be applied to these covers.\n", "",
    "The displayed integral torsion and proved connected-sum obstruction already specify the mathematical conclusion. Remove the repeated reference to an unnamed classification criterion.", "maps:src:D.1.4")

allowed_labels = ["maps:eq:finite_h2_extension", "mapsIII:def:cyclic-cover", "mapsIII:def:lifted-fibre"]
allowed_targets = ["tag-Q008", "tag-Q009"]
u.check_permanent_identifiers(before, after, allowed_labels, allowed_targets)
canonical_path = u.repairs.SOURCE
canonical = canonical_path.read_text(encoding="utf-8")
assert canonical.count(before) == 1, "Current cyclic source guard"
candidate = canonical.replace(before, "", 1)
following = (u.WORK / "root/framed_class.tex").read_text(encoding="utf-8")
assert candidate.count(following) == 1, "Framing insertion guard"
candidate = candidate.replace(following, after + following, 1)
u.check_permanent_identifiers(canonical, candidate, allowed_labels, allowed_targets)
path.write_text(after, encoding="utf-8", newline="\n")
canonical_path.write_text(candidate, encoding="utf-8", newline="\n")
r.write_table(r.DEFECTS, fields, defects + new_rows)
print("UTC", datetime.now(timezone.utc).isoformat())
print("EXACT_EDIT_ROWS", len(new_rows))
print("KD_SUPPORT_REPAIR_APPLIED_WITH_EXISTING_ADMISSION")
print("CYCLIC_UNIT_PRECEDES_FRAMING; EXISTING_IDENTITIES_PRESERVED")
print("NEW_LABELS", allowed_labels)
print("NO_NEW_CHECK_OR_CRITERION_CREDIT")
