"""Publish the assigned cyclic characteristic-class unit with exact edit rows."""
import re

from S6_SERIES_PUBLISH_c8_foundations_editing import Editor
from S6_SERIES_PUBLISH_c8_integrate_presentation import (
    statement_records_to_small_tags, remove_manual_equation_tags,
    unresolved_literal_equation_references,
)

e = Editor("cyclic_invariants", "c8-III-foundations-cyclic-classes-", group="root")
starts = list(re.finditer(
    r"^\\begin\{(?:proposition|theorem|lemma)\}[^\n]*\\hypertarget\{tag-(02K[EFGHI89A])\}",
    e.original, re.M,
))
if [m.group(1) for m in starts] != ["02KE", "02KF", "02KG", "02KH", "02KI", "02K8", "02KA", "02K9"]:
    raise ValueError("The reviewed eight-statement source order has changed")
blocks = {
    m.group(1): e.original[m.start():starts[i+1].start() if i+1 < len(starts) else len(e.original)]
    for i, m in enumerate(starts)
}
ka_head = blocks["02KA"].splitlines(keepends=True)[0]
ki_head = blocks["02KI"].splitlines(keepends=True)[0]

# These bounded relocations preserve the complete original statement/proof bytes.
e.replace(blocks["02KG"], "", "D14", "maps:src:D.1.7",
          "Move the whole proper-family proof after the cohomological invariants and before the recognition theorem that uses its canonical admissible parameter. The destination insertion is the next exact row; no proof text changes in this move.")
e.replace(ka_head, "\\subsection{Smooth recognition and cyclic complex families}\n" + blocks["02KG"] + ka_head,
          "D14", "maps:src:D.1.7",
          "Insert the unchanged KG statement and sole proof at the start of the smooth-family subsection, after the full cubic/fundamental-class input.")
e.replace(blocks["02K9"], "", "D14", "maps:src:D.1.11",
          "Move the whole smooth-recognition theorem before the cyclic-action theorem that chooses its oriented representative. The exact next row inserts the same bytes.")
e.replace(ka_head, blocks["02K9"].rstrip() + "\n\n" + ka_head,
          "D14", "maps:src:D.1.11",
          "Place the unchanged recognition statement/proof between KG and KA, realizing the actual KG to K9 to KA prerequisite order.")
e.replace(ki_head, "\\subsection{Finite-coefficient cubics and the fundamental class}\n" + ki_head,
          "D14", "maps:src:D.1.9",
          "Give the coefficient-ring cubic and full K(A,2) fundamental-class calculation their own mathematical subsection after the integral ring and characteristic classes.")
e.replace("The complete credited statement and re-derivation are in \\cref{maps:src:D.1.11}.\n", "",
          "D13", "maps:src:D.1.10",
          "Remove the orphan production/credit pointer; the full recognition theorem now directly follows its family input and the preceding fundamental-class result retains every conclusion.")

e.replace("\\subsection{Characteristic classes and smooth classifications of cyclic covers}\n", r"""\subsection{Cohomology products and characteristic classes of cyclic covers}
\begin{definition}[Marked divisors and ruling classes]\hypertarget{tag-Q142}{}\label{mapsIII:def:cyclic-cohomology-data}
{\normalfont\scriptsize tag Q142}\par
Let $\pi:M=\widetilde X_p\to X_p$ be the cyclic cover of
Definition~\ref{mapsIII:def:cyclic-cover}, with $d=|p|$ and its
complex orientation. For $d>1$, index the cusp divisor cycles
$D_j$, $j\in\mathbb Z/d$, by positive $e_2$ translation, and
write $\nu_j:\overline D_j\to M$ for their normalization maps.
All component and curve classes have their complex orientations.
On $\overline D_j\cong dP_6$, let $H_j$ be the pullback of a line
and let $E_{A,j},E_{B,j},E_{C,j}$ be the exceptional classes of
rays $e_2,-e_1,e_1-e_2$, respectively. In the normalization basis
$(H,E_1,E_2,E_3)$ of Theorem~\ref{maps:src:D.1.2}, this is the
coordinate map
\[
 (a,b_1,b_2,b_3)\longmapsto(a,b_2,b_1,b_3)
 \quad\text{in the basis }(H,E_A,E_B,E_C);
\]
its inverse is the same permutation. Put
\[
 x_j=\operatorname{PD}\bigl((\nu_j)_*[\overline D_j]\bigr),
 \qquad r_j=(\nu_j)_*(H_j-E_{B,j}),
 \qquad \kappa=\operatorname{PD}(r_0).
\]
\end{definition}

""", "D13", "mapsIII:def:cyclic-cohomology-data",
          "Create the numbered common input definition with the exact self-inverse exceptional-basis permutation. Divisor/ruling notation precedes use; equality of the ruling images and their torsion order remain proved conclusions in KF.")
e.replace("[characteristic and rational ring constraints]", "[Characteristic classes and rational products]",
          "D16", "maps:src:D.1.5", "Give the proposition its short mathematical title.")
e.replace("[the integral cohomology ring]", "[Integral cohomology ring]",
          "D16", "maps:src:D.1.6", "Give the theorem its short mathematical title.")
e.replace("[the integral Pontryagin class]", "[Vanishing of the integral characteristic classes]",
          "D16", "maps:src:D.1.8", "The title describes the proved zero degree-four pullback and both integral c2 and p1 conclusions.")

e.replace(r"""\begin{proof}
\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]
\item Put $M=\widetilde X_p$, and let $\pi:M\to X_p$ be the covering
with deck group $G=\mathbb Z/d$.""", r"""\begin{proof}
\emph{Characteristic classes.}
Use the cover of Definition~\ref{mapsIII:def:cyclic-cohomology-data}
and write $G=\mathbb Z/d$ for its deck group.""",
          "D04", "maps:src:D.1.5", "Replace the inherited proof-step numbering by a descriptive proof heading and use the single numbered cover notation.")

begin = e.text.index("\\item We give the actual restriction map used for the ring assertion.")
end = e.text.index("For a nontrivial character $\\chi$, applying the exact projector", begin)
e.replace(e.text[begin:end], r"""\emph{The rational product.}
Use the cusp tube $N_0$, its complement with finite fillings $U$,
their overlap $B_0$, and the central fibre from the proof of
Theorem~\ref{maps:src:D.1.3}. Set
$N=\pi^{-1}(N_0)$, $Z=\pi^{-1}(U)$, $E=\pi^{-1}(B_0)$,
and let $W$ denote the covered central fibre. These are the same
subspaces and covering restrictions as in that proof.
Its cochain map sends a local-system cochain to the lifted cochain
$\varphi$ with $\varphi(g\sigma)=\lambda\varphi(\sigma)$;
the inverse assigns its value to the coefficient fibre of the
downstairs simplex. Both maps commute with restriction.
Thus its contraction on the regular fibre and its finite-cover
transfer prove that the nontrivial-character cohomology of $Z$
and $E$ vanishes. Its lifted cusp homotopy gives a
$G$-equivariant retraction $r:N\to W$: restriction along
$W\hookrightarrow N$ and $r^*$ are inverse on cohomology.

""", "D12", "maps:src:D.1.5",
          "Use KC's fully read identical cusp tube, exterior and boundary restrictions, coefficient-lift inverse, finite transfer and equivariant homotopy. This removes the repeated flow/graph derivation while retaining the exact maps that make the following character restriction injective.")
e.replace("The actual normalization resolution in \\ref{maps:src:D.1.2} gives", "The normalization resolution in Theorem~\\ref{maps:src:D.1.2} gives",
          "D08", "maps:src:D.1.5", "Name the mathematical normalization map and its proved theorem owner directly.")
e.replace("restriction matrix $B(\\lambda)$ of \\ref{maps:src:D.1.2}.", "restriction matrix $B(\\lambda)$ of Theorem~\\ref{maps:src:D.1.2}.",
          "D04", "maps:src:D.1.5", "Identify the exact normalization-matrix theorem by its number and kind.")
e.replace("Thus its component vector lies in the kernel of the actual\n", "Thus its component vector lies in the kernel of the\n",
          "D08", "maps:src:D.1.5", "State the component-kernel assertion directly; its complete row reduction remains.")
for old, new in [
    (r"By \ref{maps:src:D.1.3}, their images", r"By Theorem~\ref{maps:src:D.1.3}, their images"),
    (r"By \ref{maps:src:D.1.4}, the integral", r"By Theorem~\ref{maps:src:D.1.4}, the integral"),
    (r"Since \ref{maps:src:D.1.3} gives no invariant", r"Since Theorem~\ref{maps:src:D.1.3} gives no invariant"),
]:
    e.replace(old, new, "D04", "maps:src:D.1.5", "Print the internal theorem reference with its correct kind and number.")
e.replace(r"""also follows directly from $H^2(M;\mathbb Q)=0$.
\end{enumerate}
\end{proof}""", r"""also follows directly from $H^2(M;\mathbb Q)=0$.
\end{proof}""", "D04", "maps:src:D.1.5", "Close the descriptive two-part proof after removing its inherited step-numbering environment.")

e.replace(r"""Suppose $d>1$, so in this construction $d\geq5$. Number the cusp
components $D_j$, $j\in\mathbb Z/d$, by the positive $e_2$ deck
translation, and give all complex subvarieties their complex orientations.
Write $x_j=\operatorname{PD}[D_j]\in H^2(\widetilde X_p;\mathbb Z)$.
These classes generate, with the sole relation $\sum_jx_j=0$.
There is a distinguished generator $\kappa$ of the torsion subgroup of
$H^4(\widetilde X_p;\mathbb Z)$, namely the dual of the complex-oriented
ruling class $H-E_1$ in any normalized cusp component. The products are""", r"""For $d>1$, the classes $x_j$ of
Definition~\ref{mapsIII:def:cyclic-cohomology-data} generate
$H^2(M;\mathbb Z)$ with the sole relation $\sum_jx_j=0$.
Here $d\ge5$, since admissibility gives $\gcd(d,6)=1$.
All ruling classes $r_j$ have the same image $r$, and
$\kappa=\operatorname{PD}(r)$ generates the torsion subgroup of
$H^4(M;\mathbb Z)$. The products are""",
          "D13", "maps:src:D.1.6", "Move the divisor, orientation and ruling definitions to Q142 while keeping every proved generation, component-independence and torsion assertion. The d>=5 reason is explicit.")
e.replace(r"""In the marked blowup basis of \cref{maps:src:D.1.2}, write
$E_A,E_B,E_C$ for the exceptional rays $e_2,-e_1,e_1-e_2$.
Thus the $E_1$ in the statement is $E_B$.""", r"""Use the marked exceptional classes of
Definition~\ref{mapsIII:def:cyclic-cohomology-data}.""",
          "D12", "maps:src:D.1.6", "Use the unique numbered exceptional-basis definition and its explicit inverse permutation; the following six curve classes and branch maps are unchanged.")
for old, new in [
    ("order $d$. Poincare duality", "order $d$. Poincar\\'e duality"),
    ("Poincare duality gives the perfect orientation pairing", "Poincar\\'e duality gives the perfect orientation pairing"),
]:
    e.replace(old, new, "D23", "maps:src:D.1.6", "Restore the accent in the name of integral oriented duality.")

# Apply the common presentation helper only to the completed first subsection.
limit = e.text.index("\\subsection{Finite-coefficient cubics and the fundamental class}")
region = e.text[:limit]
_, edits, issues = statement_records_to_small_tags(region)
if issues:
    raise ValueError(issues)
for edit in edits:
    e.replace(edit.old, edit.new, edit.kind, edit.statement_label, edit.reason)
limit = e.text.index("\\subsection{Finite-coefficient cubics and the fundamental class}")
region = e.text[:limit]
_, equation_edits, issues, aliases = remove_manual_equation_tags(region)
if issues or equation_edits:
    raise ValueError((issues, "Unexpected manual equation tags in the wholly read first unit", equation_edits))
print("First-unit unresolved literal equation references:", unresolved_literal_equation_references(region, aliases))
e.finish(labels=("mapsIII:def:cyclic-cohomology-data",), tags=("Q142",))
