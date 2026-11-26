"""Apply the authorized first foundations-unit edits and their defect rows.

This edits one extracted fragment, never the canonical paper or central records.
Each mutation is recorded as a defects-table row.  No criterion is closed here.
"""
from __future__ import annotations

import csv
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import re

from S6_SERIES_PUBLISH_c8_integrate_presentation import (
    remove_manual_equation_tags,
    unresolved_literal_equation_references,
)

ROOT = Path(__file__).resolve().parents[1]
FRAGMENT = ROOT / "agents/continuation8_iii_integration/units/foundations/elliptic_marked_data.tex"
LANE = ROOT / "agents/continuation8_iii_foundations"
DEFECTS = LANE / "S6_SERIES_PUBLISH_c8_foundations_defects.tsv"
FIELDS = ["change_id", "type", "statement_id", "old_location", "old_page",
          "new_location", "new_page", "old_text", "new_text", "reason", "review_status"]
WHO = "GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed."


def identities(text, command):
    return Counter(re.findall(r"\\" + command + r"\{([^}]+)\}", text))


def main():
    source = FRAGMENT.read_text()
    current = source
    rows = []
    now = datetime.now(timezone.utc).isoformat()
    prefix = "III-C8-FND-MARKED-"
    if DEFECTS.exists():
        with DEFECTS.open(newline="") as stream:
            existing = list(csv.DictReader(stream, delimiter="\t"))
        if any(row["change_id"].startswith(prefix) for row in existing):
            raise SystemExit("This fragment edit has already been recorded; refusing replay.")
    else:
        existing = []

    def record(kind, label, old, new, line, reason):
        rows.append(dict(zip(FIELDS, [
            prefix + f"{len(rows)+1:03}", kind, label,
            str(FRAGMENT.relative_to(ROOT)) + f"; pre-edit fragment line {line}",
            "pending final page concordance",
            str(FRAGMENT.relative_to(ROOT)) + "; " + label,
            "pending final build", old, new, reason,
            "Applied to owned fragment " + now + ". " + WHO
            + " Full unit/proof review is recorded separately; root assembly and rendered-page gates remain pending.",
        ])))

    def change(old, new, kind, label, reason):
        nonlocal current
        if current.count(old) != 1:
            raise ValueError(("nonunique or stale exact guard", old[:100], current.count(old)))
        start = current.index(old)
        record(kind, label, old, new, current.count("\n", 0, start) + 1, reason)
        current = current[:start] + new + current[start+len(old):]

    change(
        r"\section{Geometric realization of two marked collision profiles}",
        r"\section{Marked elliptic models and triangular caps}",
        "D14", "mapsD:repair:modular-collisions",
        "The fragment contains the two marked surfaces, the all-lattice triangular cap, and its divisor products; the section title now describes all three mathematical parts.",
    )
    change(
        "We use positive base meridians and column vectors for integral elliptic\nhomology.",
        "\\subsection{Marked rational elliptic surfaces}\n\n"
        "\\begin{definition}[Marked monodromy and section cocycles]\n"
        "\\hypertarget{tag-Q100}{}\\label{mapsIII:def:marked-elliptic-cocycles}\n"
        "{\\normalfont\\scriptsize tag Q100}\\par\n"
        "We use positive base meridians and column vectors for integral elliptic\nhomology.",
        "D13", "mapsIII:def:marked-elliptic-cocycles",
        "The shared monodromy, cocycle and saturation conventions become one numbered definition before every use; the first descriptive subsection is a complete publication-review unit.",
    )
    change(
        "and $[T]=sr$.  Products of matrices are written in the order used for\nthe archived cocycles: $A_1\\cdots A_n=I$.  The section cocycle",
        "and $[T]=sr$.  Order the positive based meridians so that their\nmonodromy product is $A_1\\cdots A_n=I$.  The section cocycle",
        "D08", "mapsIII:def:marked-elliptic-cocycles",
        "State the positive based-meridian product convention itself; its ordered product and cocycle maps are unchanged.",
    )
    change(
        "with $\\mathbb Z^2$.\n\nThe fibre configurations and the rank-one Mordell--Weil lattices in\nthe next theorem are contained in Miranda's existence list and\nFukae's Table~3; they are not asserted to be new configurations\n\\cite[\\S4, pp.~206--210]{manMiranda90}\n\\cite[Table~3, rows~50 and~56]{manFukae02}.\nThe additional verification is the realization of the particular\nbased monodromy and section cocycles used in the calculations.",
        "with $\\mathbb Z^2$.\n\\end{definition}\n\n"
        "\\begin{remark}[The two fibre configurations]\n"
        "\\hypertarget{tag-Q101}{}\\label{mapsIII:rem:collision-configurations}\n"
        "{\\normalfont\\scriptsize tag Q101}\\par\n"
        "The fibre configurations and rank-one Mordell--Weil lattices below\n"
        "occur in Miranda's existence list\n"
        "\\cite[\\S4, pp.~206--210]{manMiranda90} and in Fukae's\n"
        "\\cite[Table~3, rows~50 and~56]{manFukae02}.\n"
        "Theorem~\\ref{mapsD:repair:collision-realization} gives their positive\n"
        "based monodromy and integral section cocycles explicitly.\n"
        "\\end{remark}",
        "D02", "mapsIII:rem:collision-configurations",
        "The bibliographic scope is stated positively once in a numbered remark, with the existing exact locators; the paragraph no longer answers an implied novelty objection.",
    )

    period = r"""\begin{remark}[Positive projective periods]
\hypertarget{tag-Q102}{}\label{mapsIII:rem:positive-projective-periods}
{\normalfont\scriptsize tag Q102}\par
On a simply connected regular base chart, choose periods
$\omega_1,\omega_2$ with $\tau=\omega_1/\omega_2\in\mathbb H$.
The map from the period quotient to its normalized form and its inverse are
\[
 [z]\longmapsto[z/\omega_2],\qquad
 [w]\longmapsto[\omega_2w],\qquad
 \mathbb C/(\mathbb Z\omega_1+\mathbb Z\omega_2)
       \longleftrightarrow\mathbb C/(\mathbb Z\tau+\mathbb Z).
\]
An oriented integral period change
$g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in SL_2(\mathbb Z)$
acts on the period column by $g$, with inverse $g^{-1}$, and sends
$\tau$ to $\tau'=(a\tau+b)/(c\tau+d)$. The normalized fibre map is
$w\mapsto w/(c\tau+d)$, with inverse multiplication by $c\tau+d$.
It maps the period lattices bijectively because
\[
 \frac1{c\tau+d}=a-c\tau',\qquad
 \frac{\tau}{c\tau+d}=-b+d\tau',\qquad ad-bc=1.
\]
The period map and functional invariant described in
\cite[p.~2]{manHerfurtner90} therefore identify the projective period
system with the pullback of the modular system by $J$.
For positive loops around $J=0,1$ we use
\[
 A=\begin{pmatrix}0&1\\-1&1\end{pmatrix},\qquad
 B=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
Their actions are $A(\tau)=1/(1-\tau)$ and $B(\tau)=-1/\tau$.
Their derivatives at $e^{\pi i/3}$ and $i$ are
$e^{2\pi i/3}$ and $-1$, fixing the positive local orientations.
The cusp conventions are related by the literal identities
\[
 A^{-1}B=T,\qquad
 -(AB)^{-1}=STS^{-1}=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
\]
Conjugation by $S$ has inverse conjugation by $S^{-1}$, so both
displayed cusp matrices are positive primitive Picard--Lefschetz
matrices in their indicated integral period bases.
\end{remark}

"""
    change(
        "\\begin{theorem}[Two marked rational elliptic surfaces]",
        period + "\\begin{theorem}[Two marked rational elliptic surfaces]",
        "D14", "mapsIII:rem:positive-projective-periods",
        "Place the common projective-period construction before OG. Its source is precisely KM proof lines 177–188 plus the explicit normalization maps and inverses; Herfurtner printed p. 2 was reopened and visually read in this run. OG uses no other KM conclusion here. KM will cite this common remark in its own later unit review.",
    )
    change(
        "\\hypertarget{tag-02OG}{}\\label{mapsD:repair:collision-realization}\n\n",
        "\\hypertarget{tag-02OG}{}\\label{mapsD:repair:collision-realization}\n"
        "{\\normalfont\\scriptsize tag 02OG}\\par\n",
        "D10", "mapsD:repair:collision-realization",
        "Print the existing permanent tag beside the statement; its anchor and label remain unchanged.",
    )

    alternate_start = current.index("An alternative coordinate $u$ for the first surface gives the model")
    alternate_end = current.index("\n\n\\emph{The exact covering and peripheral marking.}", alternate_start)
    alternate = current[alternate_start:alternate_end]
    change(alternate + "\n\n", "", "D20", "mapsD:repair:50-weierstrass",
           "Move the second Weierstrass normalization, with every forward/inverse map and endpoint chart, into one numbered conversion remark after the realization proof. The proof uses its first model throughout.")

    old_period = r"""Use the projective period matrices
\[
 A=\begin{pmatrix}0&1\\-1&1\end{pmatrix},\quad
 B=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
 T=A^{-1}B=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
The elliptic projective local system is their pullback by $J$, as in
\cite[p.~2]{manHerfurtner90} and the period construction in
Theorem~\ref{maps:src:D.2.12}.  The derivatives of $A(\tau)=1/(1-\tau)$
at $e^{\pi i/3}$ and $B(\tau)=-1/\tau$ at $i$ are
$e^{2\pi i/3}$ and $-1$.  They fix the positive conventions."""
    change(old_period,
           "Use the projective period matrices $A,B$ and the positive\n"
           "orientations of Remark~\\ref{mapsIII:rem:positive-projective-periods}.\n"
           "The elliptic projective local system is their pullback by $J$.",
           "D14", "mapsD:repair:collision-realization",
           "Replace OG's forward dependency on the later seven-family theorem by the common period remark, whose exact matrices, inverse uniformizations and positive local orientations now precede this proof.")

    verification_start = current.index("\\phantomsection\\hypertarget{tag-033V}{}")
    verification_end = current.index("\n\\begin{theorem}[A triangular cusp", verification_start)
    verification = current[verification_start:verification_end]
    alternate_remark = (
        "\\begin{remark}[A second Weierstrass coordinate for the first surface]\n"
        "\\hypertarget{tag-Q103}{}\\label{mapsIII:rem:collision-weierstrass-coordinate}\n"
        "{\\normalfont\\scriptsize tag Q103}\\par\n" + alternate + "\n\\end{remark}\n\n"
    )
    change(verification, alternate_remark, "D09", "qa:III:layout:4",
           "Remove the verifier/output bookkeeping paragraph. All computational inputs, finite matching method, graph method, exact counts, matrices, cocycles and heights remain in the proof; the verified repository path is supplied to root's program table. Place the complete alternative-coordinate calculation in its numbered remark. Anchor 033V is relocated to the matching computation below, not deleted.")
    change("Here is a finite identification of these coverings.",
           "\\phantomsection\\hypertarget{tag-033V}{}\\label{qa:III:layout:4}\n"
           "Here is a finite identification of these coverings.",
           "D13", "qa:III:layout:4",
           "Attach the preserved former verifier anchor to the actual finite covering calculation that supplies its inputs, method and result inside the proof.")

    fan_start = current.index("Write \\(B_0:\\mathbb Z^2\\longrightarrow\\mathbb Z^2\\) for an integer")
    fan_end = current.index("The determinant of the three ray columns", fan_start)
    fan = current[fan_start:fan_end]
    period_start = current.index("The two period generators translate the vertex by the columns")
    period_end = current.index("These maps commute and extend", period_start)
    action = current[period_start:period_end]
    definition = (
        "\\subsection{Triangular caps and their integral homology}\n\n"
        "\\begin{definition}[Triangular cusp neighbourhood]\n"
        "\\hypertarget{tag-Q104}{}\\label{mapsIII:def:triangular-cusp}\n"
        "{\\normalfont\\scriptsize tag Q104}\\par\n"
        "Let \\(L\\subset\\mathbb Z^2\\) be a full sublattice of index \\(D>0\\).\n"
        + fan + action +
        "For sufficiently small \\(\\epsilon>0\\), let \\(N_L\\) denote the quotient\n"
        "over \\(|q|\\leq\\epsilon\\) and put \\(M_L=\\partial N_L\\).\n"
        "The nearby torus has lattice \\(\\Lambda=\\mathbb Z^4\\), marked by\n"
        "the two short angular circles and the two long period circles.\n"
        "\\end{definition}\n\n"
    )
    change("\\begin{theorem}[A triangular cusp and its boundary kernel]",
           definition + "\\begin{theorem}[A triangular cusp and its boundary kernel]",
           "D13", "mapsIII:def:triangular-cusp",
           "Define the unit-triangle fan, full period sublattice, arbitrary holomorphic units and compact tube once before the cap theorem. The fan and period paragraphs are relocated verbatim from its proof; smoothness, properness and all inverse maps stay in that proof.")
    old_hypotheses = (
        "\\textup{\\small(tag 02LK)}\n"
        "Let \\(N_L\\) be the smooth triangular Mumford cusp for the unit-triangle\n"
        "fan and a full short-period sublattice \\(L\\subset\\mathbb Z^2\\).\n"
        "The two periods may have nonvanishing holomorphic unit factors.\n"
        "Write \\(s\\mid t\\) for the positive Smith factors of \\(L\\), and put\n"
        "\\(D=st\\). Let \\(M_L=\\partial N_L\\), and let \\(\\Lambda=\\mathbb Z^4\\)\n"
        "be the nearby torus lattice. Its return is \\(A=I+N\\), where\n"
    )
    new_hypotheses = (
        "{\\normalfont\\scriptsize tag 02LK}\\par\n"
        "The space \\(N_L\\) of Definition~\\ref{mapsIII:def:triangular-cusp}\n"
        "is a compact smooth neighbourhood of its central fibre.\n"
        "Write \\(s\\mid t\\) for the positive Smith factors of \\(L\\), so that\n"
        "\\(D=st\\). Its nearby-torus return on \\(\\Lambda\\) is \\(A=I+N\\), where\n"
    )
    change(old_hypotheses, new_hypotheses, "D13", "maps:src:D.2.43",
           "Use the numbered construction without duplicating its hypotheses. The full lattice/unit scope and D=st range are unchanged; the quotient's smooth compactness is now stated explicitly and remains proved in the first proof part. The existing visible tag uses the common small-tag style.")
    # These two strings now occur in the definition and proof; restrict deletion
    # to the already identified proof, rather than guessing a global occurrence.
    lk_proof = current.index("\\begin{proof}", current.index("\\begin{theorem}[A triangular cusp"))
    for moved, reason in (
        (fan, "The fan construction now precedes the theorem in its numbered definition; this proof begins with its determinant and inverse-chart verification."),
        (action, "The period action is now defined once before the theorem; its commutation, extension, inverse, freeness and properness are still proved here."),
    ):
        position = current.index(moved, lk_proof)
        record("D13", "maps:src:D.2.43", moved, "", current.count("\n", 0, position)+1, reason)
        current = current[:position] + current[position+len(moved):]
    change("\\begin{theorem}[Component intersections in a triangular cusp]",
           "\\subsection{Component intersections in triangular caps}\n\n"
           "\\begin{theorem}[Component intersections in a triangular cusp]",
           "D14", "maps:src:D.2.47",
           "Give the divisor-form calculation its own complete subsection, following the cap construction and homology and preceding every later characteristic/classification use.")
    change("\\hypertarget{tag-02LO}{}\\label{maps:src:D.2.47}\n\n",
           "\\hypertarget{tag-02LO}{}\\label{maps:src:D.2.47}\n"
           "{\\normalfont\\scriptsize tag 02LO}\\par\n",
           "D10", "maps:src:D.2.47",
           "Print the existing permanent tag beside the component-intersection theorem while retaining its exact anchor and label.")

    numbered, equation_edits, unresolved, aliases = remove_manual_equation_tags(current)
    if unresolved:
        raise ValueError(unresolved)
    for edit in equation_edits:
        record(edit.kind, "maps:src:D.2.47", edit.old, edit.new,
               current.count("\n", 0, edit.start)+1, edit.reason)
    current = numbered
    literal_references = unresolved_literal_equation_references(current, aliases)
    if literal_references:
        raise ValueError(literal_references)

    new_tags = {f"tag-Q10{i}" for i in range(5)}
    new_labels = {
        "mapsIII:def:marked-elliptic-cocycles",
        "mapsIII:rem:collision-configurations",
        "mapsIII:rem:positive-projective-periods",
        "mapsIII:rem:collision-weierstrass-coordinate",
        "mapsIII:def:triangular-cusp",
    }
    for command, allowed in (("hypertarget", new_tags), ("label", new_labels)):
        old_ids, new_ids = identities(source, command), identities(current, command)
        if old_ids - new_ids or new_ids - old_ids != Counter(allowed):
            raise ValueError((command, old_ids-new_ids, new_ids-old_ids))
    if current.count(r"\begin{proof}") != 3 or current.count(r"\end{proof}") != 3:
        raise ValueError("The fragment must retain exactly the three theorem proofs.")
    LANE.mkdir(exist_ok=True)
    with DEFECTS.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(existing + rows)
    FRAGMENT.write_text(current)
    print("Edited owned fragment:", FRAGMENT.relative_to(ROOT))
    print("Exact defect rows:", len(rows))
    print("Old labels and hypertarget multiplicities preserved; new tags Q100--Q104.")
    print("Three theorem proofs retained; no unresolved literal equation references.")
    print("No canonical source, shared ledger or central event table written.")


if __name__ == "__main__":
    main()
