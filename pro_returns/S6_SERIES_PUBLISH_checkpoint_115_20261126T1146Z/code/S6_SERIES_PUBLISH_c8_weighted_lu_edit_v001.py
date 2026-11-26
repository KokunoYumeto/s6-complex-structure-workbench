"""Publication consolidation of LU against the wholly read preceding LS/LT."""
import csv
from datetime import datetime, timezone
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation

root = Path(__file__).resolve().parent.parent
path = root / "agents/continuation8_iii_integration/units/weighted/height_integral_pairs.tex"
lane = root / "agents/continuation8_iii_weighted_units"
original = path.read_text()
text = original
edits = []


def replace(old, new, kinds, reason, count=1):
    global text
    assert text.count(old) == count, (old[:180], count, text.count(old))
    for _ in range(count):
        at = text.index(old)
        edits.append((kinds, text.count("\n", 0, at) + 1, old, new, reason))
        text = text[:at] + new + text[at+len(old):]


replace(r"""\begin{theorem}[all height-integral initial pairs with corrected original additive caps]\hypertarget{tag-02LU}{}\label{maps:src:D.2.52}
\textup{\scriptsize[02LU]}

Fix any of the twenty-one marked Mordell--Weil rank-one
profiles, write $\langle G,G\rangle=1/d_0$, and take
""", r"""\subsection{Height-integral initial pairs}

\begin{definition}[Height-integral filling data]\hypertarget{tag-Q204}{}\label{maps:def:height-integral-data}
{\normalfont\scriptsize tag Q204}\par
Choose one of the twenty-one marked Mordell--Weil rank-one
profiles of \ref{maps:src:D.2.19}, write
$\langle G,G\rangle=1/d_0$, and take
""", "D04;D05;D10;D13;D14;D16", "Give the unit its descriptive subsection and put the complete actual input domain into Q204 before the single theorem.")
replace("There is a finite exact integral algorithm for the fundamental\ngroup and every integral homology group with the following fillings:", "At each site choose a filling from the following list, retaining\nits indicated markings:", "D11;D13;D14", "Keep the five complete cap choices in the input definition; the algorithm conclusion moves into the theorem.")
replace("algorithm. For an original additive cap the test is the\nliteral orbit condition $h=1$, or the unchanged zero-degree\ncase with its specified relative marking.\n\nThe canonical corrections", "construction. An original additive cap has either $h=1$, or\nzero degree with its unchanged extending frame and relative marking.\nThese choices are the \\emph{height-integral filling data}.\n\\end{definition}\n\n\\begin{theorem}[Height-integral fillings]\\hypertarget{tag-02LU}{}\\label{maps:src:D.2.52}\n{\\normalfont\\scriptsize tag 02LU}\\par\nFor every datum of Definition~\\ref{maps:def:height-integral-data},\nthere is a finite exact integral algorithm for the fundamental group\nand every integral homology group. The canonical corrections", "D10;D13;D14;D16;D26", "State the algorithm once, after every cap/line/frame input is defined. The original additive sectors are unchanged.")
replace("newly non-narrow additive positions", "additive positions where both section classes are nonzero", "D01;D20", "Name the exact local condition by its actual component classes.")
replace("newly non-narrow multiplicative positions", "multiplicative positions where both classes are nonzero", "D01;D20", "Use the same exact local condition for the prescribed Mumford filling.")
replace("Thus the initial pair\nneed not satisfy the narrowness-OR condition of\n\\ref{maps:src:D.2.46}.", "The initial-pair range is all positive $(a,b)$ with $d_0\\mid ab$.", "D02;D08;D26", "State the complete positive height-integral range directly; its forty-five extra residue pairs and CRT proof remain.")
replace("The algorithm applies to every finite list and all permitted\nsection multiples, weights, logarithmic orders and affine\nnumerators. Its original-cap choices specify the line and\nrelative frame: a whole-fibre change carries the meridian\nshear proved below. A corrected original multiplicative cap\nwith a different supplied relative marking, or an additive\ncap with $h>1$, requires its own complete local boundary map\nbefore it is an input to this algorithm.", "The algorithm applies to every finite list and all section multiples,\nweights, logarithmic orders and affine numerators in the defined input.\nThe line and relative frame are part of each original-cap datum;\na whole-fibre tensor change transports its meridian by the explicit\nframe map in the proof.", "D02;D08;D11;D26", "Retain the exact original-cap input boundary in the complete numbered definition and state its actual frame transport positively. No h>1 or differently marked original cap is added.")

first = text.index(r"\smallskip\noindent\emph{Corrected lines and marked periods.}")
last = text.index(r"\smallskip\noindent\emph{The original additive cap as a mapping cone.}", first)
replace(text[first:last], r"""\begin{enumerate}
\item \emph{Corrected lines and marked periods.}
Use Theorem~\ref{maps:src:D.2.50} with the same marked surface,
$P=aG$, $Q=bG$, divisor $D$, and whole-fibre weights as in
Definition~\ref{maps:def:height-integral-data}. Its local coefficient
column $z$ is the present column $d$, and its pullback matrix
$\mathsf S$ is the present $S$. Thus the identity coordinate maps
carry \eqref{maps:eq:D.VC3} to
\[
 C(I-S)d=-(I-S)(e_p-e_0).
\]
The remaining left multiplication is $-I$, with inverse $-I$.
The entire solution ambiguity is therefore the same integral
orbit-constant lattice, with its representative-coordinate inverse.

The line bundles are literally
$M_0=\mathcal O(P-O)$ and $M_D=M_0\otimes\mathcal O(D)$.
On the complement of the singular fibres, the comparison is
\[
 I_{D,p}(v)=v\otimes\sigma_D(p),\qquad
 I_{D,p}^{-1}(v\otimes\sigma_D(p))=v,
\]
and the difference-line map multiplies by
$\sigma_D(p)/\sigma_D(p+Q)$, with reciprocal inverse.
The arrow $A_{D,p}:M_{D,p+Q}\to M_{D,p}$ covers $-Q$; its
conjugate is
\[
 I_{D,p}^{-1}A_{D,p}I_{D,p+Q}
   =j_D(p)\frac{\sigma_D(p+Q)}{\sigma_D(p)}.
\]
These are exactly the tensor, group-law and base-line maps in
Theorem~\ref{maps:src:D.2.50}. A coefficient $q^{w_i}u_i(q)$
uses the same nonzero base unit $u_i$ in both directions.
Consequently the given boundary marking
$(e_1,e_2,\delta,\gamma)$ has precisely the monodromy
\eqref{maps:eq:D.GI2}, now on the entire height-integral range
proved there. Its period shear and inverse act on the same
transported lattices: $z_G$ solves $(B-I)z_G=g$, the elliptic
translation is $bz_G$, and the line row is
$-ag^{\mathsf t}JB=az_G^{\mathsf t}J(B-I)$.
The component order divides $d_0$, so $abz_G$ is integral.
The proved inverse monodromy is integral, and the same ordered
base-degree cocycle gives
\[
 \prod_iT_i=I+\left(\sum_iw_i-ab/d_0\right)\delta\gamma^*=I.
\]
Thus every hypothesis of the integer bar construction is satisfied
with these actual periods and units.

For an invariant orbit divisor $E$, multiplication by $\sigma_E$
and division by it are inverse maps on the punctured family.
Its arrow ratio cancels through the canonical trivialization
$\sigma_E/T_Q^*\sigma_E$ of the difference line. The period
blocks and specified base weights therefore agree under that map
on the complement of the zeros and poles of $\sigma_E$.

""", "D11;D12;D14;D17;D20;D22", "Replace the duplicated LS derivation only after mapping every input: identical profile,P,Q,D,weights,units and period basis; z=d and mathsf S=S; -I is the inverse equation transport. Retain the actual tensor/arrow inverses, component-denominator integrality and ordered product. LS proves the full signed range and hence these positive inputs; no narrowness hypothesis is imported from LN.")

first = text.index(r"\smallskip\noindent\emph{The original additive cap as a mapping cone.}")
last = text.index(r"\smallskip\noindent\emph{The literal odd-star correction and the count.}", first)
replace(text[first:last], r"""\item \emph{Original additive caps and their marked maps.}
At an original additive site the weight is zero, the same line
$M_D$ has invariant degree vector $c$, and the supplied orbit
condition is $h=1$. Theorem~\ref{maps:src:D.2.51} therefore applies
to this actual original cap with its line arrow and extending frames.
Here is the exact transport between return conventions.

For the unit-circle return $\phi$, write
$\mathcal T(\phi)=(E\times[0,1])/((x,1)\sim(\phi x,0))$.
The two roof presentations are related by
\[
 j:\mathcal T(\phi)\longrightarrow\mathcal T(\phi^{-1}),
 \quad [x,t]\longmapsto[\phi x,1-t],\qquad
 j^{-1}[y,s]=[\phi^{-1}y,1-s].
\]
The endpoint relations prove that both maps are well-defined and
that both composites are the identity. At roof zero the target
identification makes $j$ the identity on the component and scalar
cells. It reverses the roof marking: $\widehat\gamma=-\gamma$,
$\widehat\delta=\delta$, and $\widehat t=-t$.
For the cone of a component return $\sigma$, the induced chain maps
to the cone of $\sigma^{-1}$, in degrees zero through four, are
\[
 1,\quad \operatorname{diag}(1,-1),\quad
 \operatorname{diag}(I_v,-1),\quad
 \operatorname{diag}(I_v,-\sigma),\quad -\sigma.
\]
Their inverses replace $\sigma$ by $\sigma^{-1}$.
For example
$(\sigma^{-1}-I)(-\sigma)=\sigma-I$ and
$c^{\mathsf t}(-\sigma)=-c^{\mathsf t}$; these are the two
degree-three boundary identities, and the degree-four identity is
$(I-\sigma^{-1})(-\sigma)=I-\sigma$.
The return inversion carries the marked section cocycle and its
logarithm to $\widehat q=-q$ and $\widehat z=-z$.
The corresponding fibre basis change is
$\operatorname{diag}(I_2,1,-1)$, its own inverse.
Consequently each mixed term has two cancelling sign changes:
\[
 \widehat y_{12}+\widehat z_2\widehat y_{14}
       -\widehat z_1\widehat y_{24}
 =y_{12}+z_2y_{14}-z_1y_{24}.
\]
The scalar normal is fixed and the other fixed-normal generator
changes sign. Both retain the bounding chains of
Theorem~\ref{maps:src:D.2.51}, with the displayed inverse chain maps.
Thus that theorem's positive-return calculation and a forward-arrow
calculation give the same marked maps in the chosen period basis.
All line units occur in $\phi$ and its actual inverse.

In this basis put $z=bz_G$ and let $q_0$ be its least positive
denominator. Write $R$ for orbit sums and
$w=R\mu/q_0$. These are exactly
\eqref{maps:eq:IC_local_27}--\eqref{maps:eq:IC_local_30};
the weighted diagrams there prove $q_0=\gcd(\ell_j\mu_j)$.
The primitive class $W$ has orbit coordinates $w$; the section
$w\mapsto[(sw,0)]$ and its inverse $[(x,t)]\mapsto Rx$
are the $h=1$ specialization of
\eqref{maps:eq:IC_local_15}--\eqref{maps:eq:IC_local_19}.
The complete fibre map is therefore
\[
 \bigwedge\nolimits^2\Lambda\longrightarrow H_2(U),\qquad
 y\longmapsto q_0(y_{12}+z_2y_{14}-z_1y_{24})W,
 \quad\Lambda=\mathbb Z\langle e_1,e_2,\delta,\gamma\rangle.
\]
Its integral primitive row has the B\'ezout section and inverse
kernel coordinates of \eqref{maps:eq:IC_local_31}--\eqref{maps:eq:IC_local_34}.
The actual fixed lattice has basis
$\delta$ and $(-q_0z_1,-q_0z_2,0,q_0)$.
For a normal image $(x,t)$, its component projection is $Rx=0$.
With $y=\mathcal Kx$ and invariant $\eta$ satisfying
$c^{\mathsf t}\eta=1$, the complete bounding chain is
\[
 d_3\bigl(0,y+(t-c^{\mathsf t}y)\eta\bigr)=(x,t),
\]
as in \eqref{maps:eq:IC_local_46}; it includes every frame prism.
The fibre kernel and these two normals are the complete boundary
kernel. The degree-one map reads the primitive $\gamma$ coordinate,
with its roof-loop section. The groups are
\[
 H_0(U)=H_1(U)=\mathbb Z,\quad H_2(U)=\mathbb Z^{\rho-1},
 \quad H_3(U)=\mathbb Z^{2\rho-1},\quad H_4(U)=\mathbb Z^\rho,
 \qquad\chi(U)=0.
\]
The cone's orbit inclusions and inverse coefficient readings provide
the component-disc and higher-degree maps used below.

""", "D11;D12;D14;D17;D20;D22;D26", "Consolidate the repeated LT cone/homology/cover/normal proofs after matching the identical actual M_D,zero weight,invariant c,h=1 and frames. Supply a based actual roof reversal with inverse and every chain map; its q,z,gamma,t sign transport proves preservation of the marked mixed-area row. Keep the h=1 quotient, primitive row, full normal chain and gamma section explicitly; c=0 is not folded into this argument.")

first = text.index(r"\smallskip\noindent\emph{The literal odd-star correction and the count.}")
last = text.index("The component orders in the table are pairwise coprime", first)
replace(text[first:last], r"""\item \emph{Odd-star corrections and the residue count.}
For the affine $D_5,D_7$ diagrams, use the chain and outer-first
component maps \eqref{maps:eq:IC_local_47}--\eqref{maps:eq:IC_local_49}.
They give the actual divisor $d_{\rm can}=-e_0$ at
$(\overline P,\overline Q)=(2,2)$, its degree
$e_0+e_1-e_2$, both inverse index permutations and the degree vectors
\eqref{maps:eq:D.IC8}. The outer-first return is $(01)(23)$,
and $\eta=-e_4$ proves $h=1$.
The alternative divisor $e_1$ differs by $e_0+e_1$.
Multiplication by the canonical section of
$\mathcal O(-C_0-C_1)$ and its reciprocal compare these punctured
lines, conjugating the arrows by the same section ratio.
Each original cap keeps its own supplied line and extending frame.

The nontrivial component orders $n_i$ in the marked profiles of
Theorem~\ref{maps:src:D.2.50} are pairwise coprime
""", "D01;D11;D12;D14;D20;D22", "Use the earlier complete D5/D7 divisor/degree/permutation proof at its exact identities, retaining the actual alternate divisor and reciprocal frame comparison. Name component orders n_i to separate them from orbit h and later component-disc ranks.")
replace("The component orders in the table are pairwise coprime\nand their product is $d_0$.", "and their product is $d_0$.", "D11", "Join the retained CRT proof to its explicit preceding component-order input without a duplicate table.")
# Component-order notation is changed only in this CRT argument.
first = text.index("The nontrivial component orders $n_i$")
last = text.index(r"\smallskip\noindent\emph{Global relation maps", first)
before = text[first:last]
after = before.replace("h_i", "n_i")
assert before.count("h_i") == 9
replace(before, after, "D20", "Transport all nine local component-order symbols h_i to n_i by the identity; CRT, count and inverse formulas are unchanged. The later h_i=b4(U_i) remains a separate defined variable.")
replace("This proves the full initial-pair scope; a multiplicative\nnewly non-narrow position takes its prescribed Mumford cap.", "This proves the stated initial-pair range. At a multiplicative\nsite where both section classes are nonzero, use its prescribed\nMumford cap.", "D01;D08;D20", "State the actual local cap choice and the proved complete range directly.")
for old, new in [
    ("Global relation maps and the fundamental group.", "Global relations and the fundamental group."),
    ("The integral splitting and all homology groups.", "Integral splitting and homology."),
    ("Relative frames for supplied corrections.", "Relative frames."),
]:
    replace("\\smallskip\\noindent\\emph{" + old + "}", "\\item \\emph{" + new + "}", "D13;D16", "Use a numbered step inside the sole proof with a short mathematical title.")
replace("At the new original additive caps", "At the corrected $h=1$ original additive caps", "D01;D20", "Use the exact admitted cap condition rather than chronology.")
replace("At a new $h=1$ cap", "At a corrected $h=1$ cap", "D01", "Use the mathematical correction description.")
replace("The new additive caps have Euler number zero", "The corrected $h=1$ additive caps have Euler number zero", "D01;D20", "State precisely which inserted cap calculation supplies the zero Euler term.")
replace("A_1", "T_1", "D20", "Rename the finite torsion summand of H1 by T1 via identity, consistently with the earlier whole-fibre unit and without overloading a possible first monodromy matrix.", count=4)
replace("For completeness its vertical normal closure is a terminating", "The vertical normal closure is a terminating", "D08", "Introduce the actual terminating subgroup procedure directly.")
replace("\\end{proof}\n", "\\end{enumerate}\n\\end{proof}\n", "D13", "Close the numbered steps of the single proof.")
replace("\n\n\n\\begin{proof}", "\n\n\\begin{proof}", "D23", "Remove the extraction-only blank line.")

candidate, changes, issues = presentation.statement_records_to_small_tags(text)
assert not changes and not issues
candidate, changes, issues, aliases = presentation.remove_manual_equation_tags(candidate)
assert not issues
for change in changes:
    edits.append(("D19", text.count("\n", 0, change.start)+1, change.old, change.new, change.reason))
assert not presentation.unresolved_literal_equation_references(candidate, aliases)
presentation.units.check_permanent_identifiers(original, candidate,
    allowed_labels=("maps:def:height-integral-data",), allowed_targets=("tag-Q204",))
assert candidate.count(r"\begin{definition}") == 1
assert candidate.count(r"\begin{theorem}") == candidate.count(r"\begin{proof}") == 1
assert candidate.count(r"\begin{enumerate}") == candidate.count(r"\end{enumerate}") == 2
assert "\r" not in candidate
fields = ["change_id", "type", "statement_id", "old_location", "old_page", "new_location", "new_page", "old_text", "new_text", "reason", "review_status"]
rows = []
for number, (kinds, line, old, new, reason) in enumerate(edits, 1):
    for kind in kinds.split(";"):
        rows.append([f"III-C8-LU-PUB-{number:03}-{kind}", kind, "maps:src:D.2.52",
            f"height_integral_pairs.tex, sequential edit at line {line}", "pending page concordance",
            "weighted/height_integral_pairs.tex", "pending final build", old, new, reason,
            "source edit; complete publication readback and root admission pending"])
with (lane / "S6_SERIES_PUBLISH_LU_publication_defects.tsv").open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(fields)
    writer.writerows(rows)
path.write_text(candidate, newline="\n")
print("UTC", datetime.now(timezone.utc).isoformat())
print("LU_LINES", len(original.splitlines()), "->", len(candidate.splitlines()), "SEQUENTIAL_EDITS", len(edits), "DEFECT_ROWS", len(rows))
print("NEW_ID Q204 / maps:def:height-integral-data; OLD_IDENTIFIERS_PRESERVED; D19_EDITS", len(changes), "UNRESOLVED0")
print("SHARED_WRITES0; AUTOMATIC_CRITERION_CREDIT0; INDEPENDENT_CHECK_CREDIT0")
