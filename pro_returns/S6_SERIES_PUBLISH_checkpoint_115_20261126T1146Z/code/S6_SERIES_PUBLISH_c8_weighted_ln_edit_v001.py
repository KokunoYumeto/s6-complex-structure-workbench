"""Publication edit of the fully read, repaired LN fragment only.

The exact replacements below follow the whole proof comparison.  Mechanical
validation preserves permanent identifiers and reports numbering issues; it
does not close a publication criterion or write a shared table.
"""
from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path

import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation

ROOT = Path(__file__).resolve().parent.parent
UNIT = ROOT / "agents/continuation8_iii_integration/units/weighted/whole_fibre_initial_pairs.tex"
WORK = ROOT / "agents/continuation8_iii_weighted_units"
text = UNIT.read_text(encoding="utf-8")
original = text
edits = []


def replace(old, new, criterion, reason, count=1):
    global text
    if text.count(old) != count:
        raise ValueError(f"Exact edit guard: {criterion}: expected {count}, found {text.count(old)}: {old[:100]!r}")
    for _ in range(count):
        start = text.index(old)
        edits.append((criterion, text.count("\n", 0, start) + 1, old, new, reason))
        text = text[:start] + new + text[start + len(old):]


replace(r"""\begin{theorem}[arbitrary whole-fibre initial pairs and weights]\hypertarget{tag-02LN}{}\label{maps:src:D.2.46}
\textup{\scriptsize[02LN]}


Fix any of the $21$ marked rational elliptic profiles with
""", r"""\begin{definition}[Whole-fibre data]\hypertarget{tag-Q200}{}\label{maps:def:whole-fibre-data}
{\normalfont\scriptsize tag Q200}\par
Choose one of the $21$ marked rational elliptic profiles with
""", "D13;D14;D16;structure", "Move the complete construction domain into a numbered definition before the theorem; preserve the old compatibility equation and every parameter.")
replace("logarithmic cap. Retain the original cap at $I_n^*$.", "logarithmic cap. Use the original cap at $I_n^*$.", "D08", "State the cap choice directly; original is the mathematical cap type, not a draft history.")
replace(r"""integer are allowed.

There is a finite exact integral algorithm for the fundamental
group and every integral homology group of every such threefold.
It includes pairs not obtained by iterating any of the $172$
initial rows, several zero fibres, noncyclic toric period
lattices, and all their boundary torsion. The algorithm below applies to every finite input list and all
integers $a,b,w_i$, logarithmic orders and affine numerators satisfying
the stated conditions.

Here are the complete data of the algorithm. Use the lattice
""", r"""integer are allowed. These choices constitute \emph{whole-fibre data}.
\end{definition}

\begin{theorem}[Homology of whole-fibre constructions]\hypertarget{tag-02LN}{}\label{maps:src:D.2.46}
{\normalfont\scriptsize tag 02LN}\par
Every threefold determined by Definition~\ref{maps:def:whole-fibre-data}
has the following finite integral presentation of its fundamental group
and integral homology. The construction includes positive weights at
several fibres and noncyclic toric period lattices. It also includes
marked pairs beyond the scalar iterates of the $172$ natural initial
constructions of \ref{maps:src:D.2.22}.

Use the lattice
""", "D04;D10;D11;D12;D14;D16;D26;structure", "Separate inputs from the result, print the permanent tag in the requested form, replace internal rows by their numbered mathematical catalogue, and state the same unbounded domain once.")
replace(r"""$\operatorname{sat}$ denotes saturation only where it is
explicitly written.
""", r"""$\operatorname{sat} L=(L\otimes\mathbb Q)\cap\Lambda^2\Lambda$.
""", "D02;D20", "Give the saturation operation positively; the distinct kernels in the table retain their precise integral definitions.")
replace(r"""and the following fibre relations:
""", r"""and the following fibre relations; here $T_1=\operatorname{Tor}H_1(X)$:
""", "D20", "Name the degree-one torsion group independently of the monodromy matrix A_1; the identity map identifies T_1 with the formerly named finite group.")
replace(r"\oplus A_1", r"\oplus T_1", "D20", "Rename only the finite homology summand by its identity isomorphism; no monodromy matrix is changed.", count=6)
replace("Then $q\\ge0$ and the complete answer is", "Then $q\\ge0$ and", "D08", "Remove a rhetorical lead-in to the homology table.")
replace(r"""Products in the last row are exterior products.
""", r"""Products in the last row are exterior products. Coordinates on
$\Lambda^2\Lambda$ are ordered as $12,13,14,23,24,34$.
""", "D20", "Specify the coordinate order used by the six-entry area row and subsequent integral maps.")
replace(r"""\smallskip\noindent\emph{The line and its marked return.}
Let \(N\to\mathbb P^1\) be one of the 21 marked elliptic surfaces,
\(P=aG,\ Q=bG\), with \(a,b>0\), and put
\(\langle G,G\rangle=1/d_0\). The marked data of \ref{maps:src:D.2.19} give the ordered elliptic matrices \(B_i\), the generator cocycle \(g_i\), and the component markings. All subsequent lattice bases are bases of these periods.
""", r"""\smallskip\noindent\emph{The line and its return.}
Write \(N\to\mathbb P^1\) for the chosen elliptic surface and
\(M=\mathcal O(P-O)\). The matrices \(B_i\), cocycle \(g_i\),
and component markings are those of \ref{maps:src:D.2.19}.
""", "D11;D12;D20", "Use the preceding input definition without repeating it and explicitly name the section line used in the cap calculations.")
replace(r"\cite[Section 11.8]{manSS10}", r"\cite[Section 11.8, arXiv:0907.0298v3, pp.~50--52]{manSS10}", "D18", "Bind the height formula to the exact author version and consulted page range in the admitted primary-source record.")
replace(r"""Use
\(\Lambda=\mathbb Z\langle e_1,e_2,\delta,\gamma\rangle\),
\(J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\),
\(p_i=ag_i,\ q_i=bg_i\), and choose
\((B_i-I)z_i=q_i\). The Poincar\'e period map in \ref{maps:src:D.2.22} gives
\[
 r_i=-p_i^tJB_i,\qquad
 A_i=\begin{pmatrix}B_i&0&q_i\\r_i&1&r_iz_i+w_i\\0&0&1\end{pmatrix}.
\]
""", r"""Put \(J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\).
The Poincar\'e period map in \ref{maps:src:D.2.22} gives
\(r_i=-p_i^tJB_i\) and the return matrix \eqref{maps:eq:D.GI2}.
""", "D12", "Cite the single displayed return formula while keeping its symplectic derivation and the following integrality argument.")
replace("Literal positive-weight period lattices and all boundary torsion.", "Positive-weight period lattices.", "D08;D16", "Use a short mathematical proof-step title; the full torsion maps remain in the argument.")
replace("For reference, the full cap groups are", "The cap groups are", "D08", "Remove a metatextual lead-in without changing the cap groups.")
replace("Rank-one Mumford caps at all parameters.", "Rank-one Mumford caps.", "D11;D16", "The quantified input definition already fixes the parameter scope.")
start = text.index(r"\smallskip\noindent\emph{The full bar presentation and all logarithmic caps.}")
end = text.index(r"\smallskip\noindent\emph{The complete fundamental group and the exceptional extension.}", start)
old = text[start:end]
new = r"""\smallskip\noindent\emph{Bar coordinates and logarithmic caps.}

We apply the integral comparison in the proof of
\ref{maps:src:D.2.41}. Its mapping-cone differential
\eqref{maps:eq:D.BC9}, comparison \eqref{maps:eq:D.BC10},
and ordered bar-polygon inverse use the lattice \(\Lambda\),
integral matrices \(A_i\), and their ordered product relation.
Those are the lattice and matrices constructed above. The period
exponential and its inverse logarithm identify each vertex torus,
each edge cylinder, and its origin section with this graph model.
On the fibre lattice and peripheral paths the identification and
its inverse are the identity. Thus the comparison carries the
markings of \eqref{maps:eq:D.GI2} to the bar markings.

Put \(B=\Lambda^2\Lambda\). For \(N\) boundary sites set
\[
 D_\Gamma=(A_0-I,\ldots,A_{N-2}-I),\qquad K=\ker D_\Gamma,
 \qquad C=B/\sum_i\operatorname{im}(\Lambda^2A_i-I).
\]
An integer Smith map \(UD_\Gamma V=\Delta\) gives a primitive
basis \(K_0\) from the zero columns of \(V\), with inverse the
corresponding rows \(K_0^\vee\) of \(V^{-1}\). Consequently
\(K_0^\vee K_0=I\), and \(K_0K_0^\vee\) is the identity on \(K\).
The comparison and its bar-polygon inverse identify the exterior
degree-two group with \(C\oplus K\).

Use the integer polynomial \(f_A\) of \eqref{maps:eq:D.BC2},
whose coboundary is \eqref{maps:eq:D.BC8}. The peripheral data are
\[
 \begin{aligned}
 c_i(x)&=f_{A_i}(x) &&(i<N-1),\\
 c_{N-1}(x)&=-\sum_{j<N-1}f_{A_j}(A_{j+1}\cdots A_{N-1}x)
                                                   &&\text{in }C,\\
 J_i(x)&=(0,\ldots,x,\ldots,0) &&(i<N-1),\\
 J_{N-1}(x)&=-(A_1\cdots A_{N-1}x,\ldots,A_{N-1}x).
 \end{aligned}
\]
The identity \(D_\Gamma J_i(x)=(A_i-I)x\) follows by telescoping.
These are \eqref{maps:eq:D.BC3} and \eqref{maps:eq:D.BC14}
with the index change \(r=N-1\), whose inverse is \(N=r+1\).
A fixed normal therefore has coordinates
\((c_i(v),J_i(v))\), as in \eqref{maps:eq:D.BC5}.

At a finite-good or regular logarithm, let \(m>0\) be the root
order and \(v\in\Lambda\) its fixed power. An affine lift
\(x\mapsto A_ix+\eta\) is carried to \(x\mapsto A_ix+v/m\)
by subtracting \((I-A_i)^{-1}(\eta-v/m)\) on the moving subspace;
addition is the inverse. The averaging map in
\ref{maps:src:D.2.29} gives the same change on the root disc
with its line units, and preserves the marked root and power.

For the arithmetic test let \(h\mid m\) be the order of \(A_i\),
let \(F\) be a primitive basis of its fixed lattice, and put
\(N_h=\sum_{j<h}A_i^j\). If \(H\) is a basis of the integer
image \(F^\vee N_h\), the projected lattice is
\(F(H/h)\mathbb Z^{\operatorname{rank}F}\).
Write \(v=Fz\) and \(w=hH^{-1}z\). The freeness criterion is
\[
 \gcd(m,v_1,v_2,v_3,v_4)=1,\qquad h\mid m/\gcd(m,w).
\]
Indeed the order of the projected translation is
\(m/\gcd(m,w)\). A nonidentity moving-plane power has a fixed
point precisely when this projected translation vanishes; its
fixed point is obtained with \((A_i^j-I)^{-1}\).
An identity moving-plane power is a pure translation and has a
fixed point precisely when \(jv/m\in\Lambda\).
These are the two tests proved in \ref{maps:src:D.2.41}, applied
to the present conjugacy. For a regular logarithm \(h=1\) and
\(F=I_4\); all four coordinates enter the gcd.

The degree-three Thom image is given by all five columns
\eqref{maps:eq:D.BC4}. The ordered cochains and maps above
identify its four fibre columns and its root column with the
present boundary. The norm sums have at most \(h\) distinct
terms and are multiplied by \(m/h\). The positive normal
convention is fixed by
\[
 (y,\tau)\longmapsto
 \bigl(y+(\tau/m)v,\exp(2\pi i\tau/m)\bigr),
 \qquad s\longmapsto(y-sv,\tau_0+ms).
\]
The inverse chooses a root sheet and subtracts \((\tau/m)v\);
changing the sheet is the deck identification. The radial
coordinate is \(q=z^m\). Thus the Thom map uses the whole
core \(H_1\), including its torsion, with the same normal sign
as \eqref{maps:eq:D.BC4}.

The core group has the presentation
\[
 \langle\Lambda,\tau\mid[\Lambda,\Lambda]=1,\
       \tau x\tau^{-1}=A_ix,\ \tau^m=v\rangle.
\]
The generators map to the fibre loops and deck path; the inverse
reads the unique sheet index \(0\le j<m\) and the remaining
cover lattice vector. Both composites fix these generators.
An ordinary clutch has \(m=1, A=I, v=-e\gamma\).

"""
replace(old, new, "D12;D14;D17;D20;structure", "Use the earlier general bar chain comparison once. Its complete assumptions map by the identity on Lambda and marked peripheral paths, r=N-1 with inverse N=r+1, and the established period exponential/logarithm. Preserve the nonsaturated C, K and inverse Smith coordinates, transported last cochain, projected-lattice freeness data, normal map/inverse and finite-core presentation. All five Thom columns, including torsion and even quadratic terms, are cited at their existing exact labels. No label or mathematical domain is removed.")
replace("The complete fundamental group and the exceptional extension.", "The fundamental group.", "D16", "Shorten the proof-step title; the entire exceptional extension remains.")
replace(r"""\smallskip\noindent\emph{The complete integral algorithm.}

The input is a marked profile, compatible positive \(a,b\), a
finite list of nonnegative weights of total \(ab/d_0\), the
specified original or Mumford choices, a finite list of free
finite-good and regular logarithms, and an integer clutch.
""", r"""\smallskip\noindent\emph{The integral algorithm.}
""", "D11;D12;D16", "Use the numbered input definition instead of restating its domain in the proof.")
replace("all five columns of the displayed Thom formula.", r"all five columns of \eqref{maps:eq:D.BC4}.", "D06;D12", "Point to the single retained Thom formula at its mathematical equation label.")
table_start = text.index(r"   For \(H_1(X)\) additionally kill each nonlogarithmic meridian")
table_end = text.index("\n\n\\end{enumerate}", table_start)
replace(text[table_start:table_end], r"""   For \(H_1(X)\), additionally kill each nonlogarithmic meridian
   and the fibre subgroup in \eqref{maps:eq:D.GI5}.
   The short/long quotient, the rank-one quotient and \((\phi,\chi)\)
   prove the first two rows; the additive and multiplicative Gysin maps
   prove the last two. Their inverse sections were specified above.""", "D12", "Remove the second copy of the four-row degree-one kernel table; retain its derivation and exact reference.")
rank_start = text.index("The local cap calculations show that these groups are free, with\n")
rank_end = text.index("For the cusp,", rank_start)
replace(text[rank_start:rank_end], r"""The local cap calculations give the ranks \(h_i\) in
\eqref{maps:eq:D.GI3}.
""", "D12", "Keep the single rank table in the theorem and the local proofs of each rank.")
hom_start = text.index(r"Put \(b_2=g+q\). Poincar\'e duality and the integral universal")
hom_end = text.index("For each Smith factor", hom_start)
replace(text[hom_start:hom_end], r"""Put \(b_2=g+q\). Poincar\'e duality and the integral universal
coefficient sequence identify \(\operatorname{Tor}H_3(X)\) with
\(\operatorname{Tor}H_2(X)=T\), and \(\operatorname{Tor}H_4(X)\)
with \(\operatorname{Tor}H_1(X)=T_1\). Their free ranks are paired
in complementary dimensions; \(H_5(X)\) is free of rank \(r\).
The Euler identity gives \(b_3=2+2b_2-2r-\chi(X)\).
""", "D12;D14", "Replace the duplicate six-row homology conclusion by the duality/UCT derivation of the single table GI7. Preserve every rank and torsion group, with the following exact Ext-generator map.")
replace(r"""Thus the torsion identifications in \eqref{maps:eq:D.GI7} give the cyclic factors computed by the Smith quotient \(\mathbb Z^g\oplus T\) and \eqref{maps:eq:D.GI5}. The free middle rank follows from the Euler identity. This proves every formula of
the statement, with all its quantified parameters.
""", r"""These maps give the torsion identifications in \eqref{maps:eq:D.GI7}.
""", "D08;D11;D12", "Remove the closing recapitulation after retaining its explicit homological argument.")
replace("A pair beyond the scalar-iteration catalogue.", "Positive support at the \(I_8\) fibre.", "D16", "Use a mathematical proof-step title for the example proving the scope assertion.")
replace(r"\(I_8\) support. This proves the claimed extension of the" , r"\(I_8\) support. Thus this pair extends the", "D08", "State the proved marked-family conclusion without claim-verification language.")

candidate, header_changes, header_issues = presentation.statement_records_to_small_tags(text)
if header_changes or header_issues:
    raise ValueError("The completely read LN fragment has no remaining machine statement header")
candidate, equation_changes, equation_issues, aliases = presentation.remove_manual_equation_tags(candidate)
for change in equation_changes:
    edits.append(("D19", text.count("\n", 0, change.start) + 1, change.old, change.new, change.reason))
issues = equation_issues + presentation.unresolved_literal_equation_references(candidate, aliases)
if issues:
    raise ValueError(repr(issues))
presentation.units.check_permanent_identifiers(original, candidate,
    allowed_labels=("maps:def:whole-fibre-data",), allowed_targets=("tag-Q200",))
if candidate.count(r"\begin{theorem}") != 1 or candidate.count(r"\begin{proof}") != 1:
    raise ValueError("LN must contain one theorem and one proof")
if "\r" in candidate:
    raise ValueError("LF-only text required")
WORK.mkdir(parents=True, exist_ok=True)
path = WORK / "S6_SERIES_PUBLISH_LN_publication_defects.tsv"
fields = ["change_id", "type", "statement_id", "old_location", "old_page", "new_location", "new_page", "old_text", "new_text", "reason", "review_status"]
with path.open("w", encoding="utf-8", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(fields)
    for number, (criterion, line, old, new, reason) in enumerate(edits, 1):
        writer.writerow([f"III-C8-LN-PUB-{number:03}", criterion, "maps:src:D.2.46",
            f"whole_fibre_initial_pairs.tex, exact sequential edit at line {line}",
            "pending page concordance", "weighted/whole_fibre_initial_pairs.tex",
            "pending final build", old, new, reason,
            "source edit; full human-readable comparison and root admission required"])
UNIT.write_text(candidate, encoding="utf-8", newline="\n")
print("UTC", datetime.now(timezone.utc).isoformat())
print("UNIT", UNIT.relative_to(ROOT), "lines", len(original.splitlines()), "->", len(candidate.splitlines()))
print("EXACT_EDITS", len(edits), "OLD_IDENTIFIERS_PRESERVED", "new tag Q200; new label maps:def:whole-fibre-data")
print("NUMBERING_HELPER", len(equation_changes), "edits; unresolved", len(issues))
print("SHARED_WRITES", 0, "CRITERIA_AUTOMATICALLY_CLOSED", 0, "INDEPENDENT_CHECK_CREDIT", 0)
