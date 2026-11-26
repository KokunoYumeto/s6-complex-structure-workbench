"""Restructure the radial prerequisites and relocate their global consumer."""
from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path

import S6_SERIES_PUBLISH_c8_integrate_units as units

ROOT = units.ROOT
WORK = units.WORK / "root"
path = WORK / "radial_coordinates.tex"
source = path.read_text(encoding="utf-8")
boundary = source.index(r"\begin{theorem}[The maximal regular-locus")
early, regular = source[:boundary], source[boundary:]
old_early, old_regular = early, regular
regular_path = WORK / "regular_quotients.tex"
if regular_path.exists():
    raise ValueError("Global quotient unit already exists")
rows_to_add = []


def record(suffix, kind, old, new, reason, statement="mapsIII:carrier-radial-prerequisites"):
    rows_to_add.append(dict(change_id="III-C8-RADIAL-" + suffix, type=kind,
        statement_id=statement, old_location="radial_coordinates before restructuring",
        old_page="pending page concordance", new_location="radial_coordinates / regular_quotients",
        new_page="pending final PDF", old_text=old, new_text=new, reason=reason,
        review_status="source change applied; whole-proof comparison and final page review open"))


old_intro = early[early.index("The carrier constructions"):early.index(r"\begin{proposition}")]
new_intro = r"""\begin{definition}[Radial cusp data]
\hypertarget{tag-Q005}{}\label{mapsIII:def:radial-cusp-data}
{\normalfont\scriptsize tag Q005}\par
In the cusp coordinate of the marked period family, write
\[
 \Pi=[Z\mid I_2],\qquad
 Z=s\begin{pmatrix}0&1\\-1&0\end{pmatrix}
       +\begin{pmatrix}6\mu(t)&h(t)\\b(t)-h(t)&\mu(t)\end{pmatrix},
 \qquad t=e^{2\pi i s}.
\]
The functions $\mu,b,h$ are holomorphic on a disc containing zero.
On the positive radial ray we put $t=e^{-2\pi T}$ and $s=iT$, and set
\begin{equation}
 \begin{aligned}
 \mu_T&=\alpha_T+im_T,& h_T&=\eta_T+iH_T,& b_T&=\xi_T+iB_T,\\
 c_T&=\xi_T-\eta_T,& L_T&=T+H_T,& q_T&=L_T-B_T,\\
 D_T&=L_Tq_T+6m_T^2.
 \end{aligned}
 \hypertarget{tag-03A3}{}\label{wb:cusp-spec-radial-notation}
\end{equation}
All these quantities are real. Write
$m=\operatorname{Im}\mu(0)$, $H=\operatorname{Im}h(0)$ and
$B=\operatorname{Im}b(0)$. Choose $T_0$ so that the radial ray is in
the holomorphic coordinate disc and $D_T>0$ for $T\geq T_0$.
We identify $\mathbb C^2$ with $\mathbb R^4$ in the order
$(x_1,y_1,x_2,y_2)$ and use the Euclidean metric and its flat quotient
metrics.
\end{definition}

\begin{proof}
For a holomorphic function $g$ near zero, the function
$(g(t)-g(0))/t$ extends holomorphically to zero and is bounded on
a smaller closed disc. Substitution of $t=e^{-2\pi T}$ gives
\begin{equation}
 m_T=m+O(e^{-2\pi T}),\qquad
 H_T=H+O(e^{-2\pi T}),\qquad
 B_T=B+O(e^{-2\pi T}),
 \hypertarget{tag-039V}{}\label{wb:cusp-spec-holomorphic-errors}
\end{equation}
and the same estimates for the real parts. Hence
$D_T=T^2+O(T)$, which is positive for all sufficiently large $T$.
This proves the existence of the stated choice of $T_0$.
\end{proof}

"""
early = early.replace(old_intro, new_intro, 1)
record("RADIAL-DEFINITION", "D13", old_intro, new_intro,
       "Make the cusp coordinates and the Euclidean metric a numbered definition. Give its T0 choice a single proof from the holomorphic difference quotient, retaining both pre-existing equation identities. The convention now states the exact local data used by the two following propositions; the obsolete compendium pointer supplies no additional premise.")
record("HISTORICAL-POINTER", "D06", r"\CompendiumRef{I}{wb:prop:period-input-audit}",
       "The displayed cusp period matrix and the explicitly defined holomorphic residual functions",
       "The attached current tags mark this old target as absent from Paper I. The complete local cusp form is stated here, and the two quotient propositions are proved directly from it. The application to the marked family uses the period parameters already defined in the preceding subsection.")
old_basis = r"""Let $e_1,\ldots,e_4$ denote the coordinate unit vectors in this real
order and let $v_{\gamma,T},v_{u,T}$ be the first two columns of $P_T$.
Then
\[
 P_T\mathbb Z^4=
 \mathbb Zv_{\gamma,T}\oplus\mathbb Zv_{u,T}
                 \oplus\mathbb Ze_1\oplus\mathbb Ze_3.
\]

"""
if early.count(old_basis) != 1:
    raise ValueError("Stale period-basis paragraph")
early = early.replace(old_basis, "", 1)
needle = "Define the orthogonal projection and its projected period matrix by"
new_basis = "Let $e_1,\\ldots,e_4$ be the coordinate unit vectors and\n$v_{\\gamma,T},v_{u,T}$ the first two columns of $P_T$.\nDefine the orthogonal projection and its projected period matrix by"
early = early.replace(needle, new_basis, 1)
proof_needle = "Put $\\Gamma_T=P_T\\mathbb Z^4$ and\n$V=\\mathbb Re_1\\oplus\\mathbb Re_3$."
proof_basis = proof_needle + r""" The columns of $P_T$ give
\[
 \Gamma_T=\mathbb Zv_{\gamma,T}\oplus\mathbb Zv_{u,T}
                 \oplus\mathbb Ze_1\oplus\mathbb Ze_3.
\]
"""
early = early.replace(proof_needle, proof_basis, 1)
record("PERIOD-BASIS", "D13", old_basis, new_basis + "\n" + proof_basis,
       "Put the coordinate-vector convention in the quotient statement and its lattice identity at the exact point in the quotient proof where it is used.", "wb:cusp-spec-native-quotient")
for tag, label in (("02QB", "mapsIII:carrier-real-periods"), ("039Y", "wb:cusp-spec-native-quotient")):
    needle = "\\hypertarget{tag-" + tag + "}{}\\label{" + label + "}\n"
    new = needle + "{\\normalfont\\scriptsize tag " + tag + "}\\par\n"
    if early.count(needle) != 1:
        raise ValueError("Missing exact statement heading: " + tag)
    early = early.replace(needle, new, 1)
    record("TAG-" + tag, "D10", needle, new, "Print the permanent small tag beside the statement heading.", label)
regular = "\\section{Global torus quotients and their extension obstructions}\n" + regular
record("GLOBAL-DEPENDENCY", "D14", old_regular, regular,
       "Move the entire global quotient theorem and its complete proof after the cell calculation and the conifold section, immediately before the later carrier constructions that use it. Its exact cell, group, sphere and monodromy inputs then precede it; no mathematical sentence is removed.", "wb:cusp-spec-globalization-obstruction")

allowed_labels = ["mapsIII:def:radial-cusp-data"]
allowed_targets = ["tag-Q005"]
units.check_permanent_identifiers(source, early + regular, allowed_labels, allowed_targets)
integration = ROOT / "code/S6_SERIES_PUBLISH_c8_integrate_units.py"
integration_text = integration.read_text(encoding="utf-8")
old = 'unit("radial_coordinates", "root", "02QB 039Y 039U"),'
new = 'unit("radial_coordinates", "root", "02QB 039Y"),'
if integration_text.count(old) != 1:
    raise ValueError("Stale radial-unit allocation")
integration_text = integration_text.replace(old, new, 1)
anchor = '    unit("further_cusp_carriers", "later",'
if integration_text.count(anchor) != 1:
    raise ValueError("Stale carrier allocation")
integration_text = integration_text.replace(anchor, '    unit("regular_quotients", "root", "039U"),\n' + anchor, 1)
defect_path = ROOT / "S6_SERIES_PUBLISH_defects_III.tsv"
with defect_path.open(encoding="utf-8", newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields, rows = reader.fieldnames, list(reader)
if {r["change_id"] for r in rows} & {r["change_id"] for r in rows_to_add}:
    raise ValueError("Radial edit already recorded")
path.write_text(early, encoding="utf-8", newline="\n")
regular_path.write_text(regular, encoding="utf-8", newline="\n")
integration.write_text(integration_text, encoding="utf-8", newline="\n")
with defect_path.open("w", encoding="utf-8", newline="") as stream:
    writer = csv.DictWriter(stream, fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows + rows_to_add)
print("RADIAL_PREREQUISITES_RESTRUCTURED", len(early.splitlines()))
print("GLOBAL_QUOTIENT_RELOCATED", len(regular.splitlines()))
print("DEFECT_ROWS", len(rows_to_add))
print("IDENTITIES_PRESERVED", "all original labels and targets")
print("UTC", datetime.now(timezone.utc).isoformat())
print("No progress/check/derived-table changes; semantic unit admission remains open.")
