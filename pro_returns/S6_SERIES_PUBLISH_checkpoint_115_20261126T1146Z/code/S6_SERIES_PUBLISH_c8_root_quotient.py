"""Publish the fully compared relative sphere-map proposition.

Every exact source change is recorded. This operation gives no proof or
unit-completion credit; the full resulting proof is read separately.
"""
from __future__ import annotations

from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

path = u.WORK / "root/quotient_core.tex"
before = path.read_text(encoding="utf-8")
after = before
fields, defects = r.table(r.DEFECTS)
new_rows = []

def change(key, kind, old, new, reason):
    global after
    ident = "III-C8-QUOTIENT-" + key
    assert not any(row["change_id"] == ident for row in defects)
    assert after.count(old) == 1, key
    after = after.replace(old, new, 1)
    new_rows.append(dict(change_id=ident, type=kind,
        statement_id="maps:src:A.2.2", old_location="relative quotient unit before publication pass",
        old_page="pending page concordance", new_location="Relative realization of sphere maps",
        new_page="pending final PDF", old_text=old, new_text=new, reason=reason,
        review_status="source edit applied; whole readback and final page reading pending"))

change("SUBSECTION", "D14",
    r"\section{Sphere maps, framings and homotopy classes}\hypertarget{tag-034K}{}\label{sec:III:maps}",
    r"\section{Sphere maps, framings and homotopy classes}\hypertarget{tag-034K}{}\label{sec:III:maps}" + "\n\\subsection{Relative realization of sphere maps}",
    "The complete proposition and its exact supported-replacement proof form a descriptive subsection. The new boundary alone gives no completion credit.")
change("TITLE", "D03",
    "[Counterexample: as an unrestricted uniqueness assertion]",
    "[Relative realization of the twelve homotopy classes]",
    "State the proved full relative-realization conclusion in the title; the mathematical content is supplied by the same complete proof.")
change("TAG", "D10",
    r"\StatementRecord{maps:src:A.2.2}{proved}{02J3}{the definitions and constructions stated in the proof}",
    r"{\normalfont\scriptsize tag 02J3}\par",
    "Print only the existing permanent tag; its anchor and label are unchanged.")
change("STATEMENT", "D02",
    r"""Agreement with the literal quotient outside a neighbourhood
of $W$, without a condition on the image of that neighbourhood,
does not determine a homotopy class $S^6\to S^3$.  All twelve
classes occur among maps satisfying that bare agreement
condition.""",
    r"""Let $N$ be an open neighbourhood of the cusp $W$ in an original
sphere member, and fix the quotient homeomorphism $\varphi:Q\to S^3$.
Every class in $[S^6,S^3]\cong\mathbb Z/12$ has a representative
$\varphi q$, where $q:S^6\to Q$ is smooth and agrees with the literal
quotient on $S^6\setminus N$.
For the designated cusp solid torus $T\subset Q$ and any basepoint
$y\in T$, the inclusion followed by $\varphi$ induces
\[
 (\varphi|_T)_*:\pi_6(T,y)\longrightarrow\pi_6(S^3,\varphi(y)),
 \qquad \operatorname{im}(\varphi|_T)_*=\{0\}.
\]""",
    "Give the positive realization statement with its original-member, exterior and target scope. The final displayed local image is already proved explicitly in the final part of the same admitted proof; it is not a global uniqueness inference.")
change("PROOF-OPEN", "D23",
    r"""\begin{proof}
\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]
\item Fix the neighbourhood $N$ in the statement.  By""",
    r"""\begin{proof}
By""",
    "Remove the one-item enumeration and its machine-style index; preserve the proof in its original logical order.")
change("QUOTIENT-NAME", "D08", "choose the smooth repaired quotient", "choose the smooth quotient replacement",
    "Name the mathematically defined cusp replacement without revision language.")
change("SMOOTH-HOMOTOPY", "D02",
    r"""Composing the homotopy with $\varphi$ preserves the class in
$[S^6,S^3]$; no regularity of $\varphi$ is used in this step.""",
    r"""Composing this continuous homotopy with $\varphi$ preserves the
class in $[S^6,S^3]$.""",
    "State the exact continuity mechanism already used by the proof, removing its defensive repetition.")
change("LOCAL-IMAGE", "D11",
    r"""has image $\{0\}$.  A nonzero target sphere class therefore
cannot be inserted by a sphere map factoring through $T$;
the zero class is represented by the constant map in $T$.
This computes the local sphere contribution under the requirement
that the replacement image remain in the designated solid torus.
\end{enumerate}
\end{proof}""",
    r"""has image $\{0\}$, represented by the constant map in $T$.
\end{proof}""",
    "The complete displayed based contraction proves the image assertion once. Remove repeated interpretations and the obsolete enumeration end.")
change("CUSP-REMARK", "D13",
    r"""The corrected content of \cite[Remark 8.3]{mapsEngel} is
therefore a quotient over the regular part and the two finite
fillings, followed by a replacement within its circle homotopy
class over a cusp collar.  The literal character does not
extend.  The replacement gives a canonical homotopy class
when the solid-torus image condition is retained.""",
    r"""\begin{remark}[The cusp replacement]
\hypertarget{tag-Q007}{}\label{mapsIII:rem:cusp-replacement}
{\normalfont\scriptsize tag Q007}\par
The quotient construction of \cite[Remark~8.3, pp.~22--23]{mapsEngel}
is literal over the regular part and the two finite fillings.
At the cusp, \SeriesRef{mapsI:src:A.2.1} constructs its replacement
with prescribed outer collar and image in the designated solid torus,
and proves independence of that replacement in its stated relative
homotopy class. That relative result supplies the homotopy class
of the quotient map used below.
\end{remark}""",
    "Place the orphan scope paragraph in a numbered remark and identify the exact closed Paper I input for global relative independence. The local pi6(T) calculation alone is not used for that conclusion. The literal-character extension obstruction remains fully proved in 039U(v), avoiding its duplicate assertion here.")

u.check_permanent_identifiers(before, after,
    ["mapsIII:rem:cusp-replacement"], ["tag-Q007"])
canonical_path = u.repairs.SOURCE
canonical = canonical_path.read_text(encoding="utf-8")
assert canonical.count(before) == 1, "Canonical relative-map unit guard"
candidate = canonical.replace(before, after, 1)
u.check_permanent_identifiers(canonical, candidate,
    ["mapsIII:rem:cusp-replacement"], ["tag-Q007"])
path.write_text(after, encoding="utf-8", newline="\n")
canonical_path.write_text(candidate, encoding="utf-8", newline="\n")
r.write_table(r.DEFECTS, fields, defects + new_rows)
print("UTC", datetime.now(timezone.utc).isoformat())
print("EXACT_EDIT_ROWS", len(new_rows))
print("EXISTING_LABELS_AND_TARGETS_PRESERVED")
print("NEW_ID", "Q007 mapsIII:rem:cusp-replacement")
print("CANONICAL_AND_FRAGMENT_APPLIED; NO_REVIEW_CREDIT")
