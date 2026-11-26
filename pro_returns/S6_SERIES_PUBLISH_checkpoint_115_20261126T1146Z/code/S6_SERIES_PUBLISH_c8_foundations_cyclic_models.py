"""Publish the complete family, recognition and cyclic-action unit."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor
from S6_SERIES_PUBLISH_c8_integrate_presentation import (
    statement_records_to_small_tags, remove_manual_equation_tags,
    unresolved_literal_equation_references,
)

e = Editor("cyclic_invariants", "c8-III-foundations-cyclic-models-", group="root")
e.replace(r"\subsection{Smooth recognition and cyclic complex families}", r"""\subsection{Smooth recognition and cyclic complex families}
\begin{definition}[Canonical cyclic models and complex parameters]\hypertarget{tag-Q145}{}\label{mapsIII:def:canonical-cyclic-model}
{\normalfont\scriptsize tag Q145}\par
For each $d\ge1$ with $\gcd(d,6)=1$, take the marked datum
\[
 \mathcal A_d=(\ell_0,\ell_1,\ell_2,k_1,k_2,\sigma)
             =(0,-d,d,0,0,0).
\]
Write $\mathcal P=\{\operatorname{Im}c<-M\}$ for the admissible
half-plane of Definition~\ref{mapsIII:def:period-parameters},
and let $X_{d,c}=X(c;\mathcal A_d)$. Put $X_d=X_{d,-i}$ and
let $Z_d$ be its universal cover with the pulled-back complex
structure. The oriented smooth manifold $M_d$ is the underlying
manifold of $Z_d$: the identification is the identity on points,
with each complex chart read as a real chart, and its inverse is
the same identity.

For an arbitrary marked datum and the parameter $w=e^{-\pi ic}$
of Definition~\ref{mapsIII:def:period-parameters}, set
\[
 W=(-1)^{k_2}w=e^{-\pi i(c+k_2)},\qquad
 u=w^2=e^{-2\pi ic}=W^2.
\]
For fixed integral $k_2$, the inverse coordinate change is
$w=(-1)^{k_2}W$. In the canonical datum $k_2=0$, so $W=w$.
\end{definition}
""", "D13", "mapsIII:def:canonical-cyclic-model",
          "Number the full canonical datum, existing parameter domain, canonical member/cover and underlying smooth model before use. Md is defined by the actual cover, without presupposing its later invariant uniqueness. The w/W conversion and inverse retain every twist and the scale u.")
e.replace("[dependence of the smooth type and the count]", "[Smooth type and complex parameter]", "D16", "maps:src:D.1.7", "Use a mathematical title for the smooth classification and full complex parameter family.")
e.replace(r"""oriented diffeomorphism type for each $d$. This statement identifies
dependence on the construction data. The complete Zhubr classifying
invariant and a canonical cyclic action are supplied in \ref{maps:src:D.1.9}--\ref{maps:src:D.1.12}.""", r"""oriented diffeomorphism type for each $d$.""", "D11", "maps:src:D.1.7",
          "Remove the closing process/forward-scope recap. The complete parameter and cover conclusions remain here; the full invariant and canonical action have their sole later statements in this subsection.")
e.replace(r"""Put $\mathcal P=\{\operatorname{Im}c<-M\}$. For each positive
$d$ coprime to six, take the canonical data
\[
 (\ell_0,\ell_1,\ell_2,k_1,k_2,\sigma)=(0,-d,d,0,0,0)
\]
and denote the resulting member by $X_{d,c}$. These data have $p=d$.""", r"""Use the canonical data and parameter half-plane of
Definition~\ref{mapsIII:def:canonical-cyclic-model}. They satisfy
$p=4d-3d=d$, and $3\nmid d$, $2\nmid d$ give the two finite
admissibility conditions.""", "D13", "maps:src:D.1.7",
          "Use the unique numbered canonical definition and give the exact p and finite-divisibility reasons at its first use.")
e.replace("The actual action on these real coordinates is\n", "The action on these real coordinates is\n", "D08", "maps:src:D.1.7", "State the displayed logarithmic action directly, preserving its exact formula and uniform bounds.")

k9_head = r"\begin{theorem}[The diffeomorphism type of every cover]\hypertarget{tag-02K9}{}\label{maps:src:D.1.11}"
e.replace(k9_head, r"""\begin{definition}[Complete invariant data of the cyclic model]\hypertarget{tag-Q146}{}\label{mapsIII:def:cyclic-classifying-data}
{\normalfont\scriptsize tag Q146}\par
For $d\ge1$ prime to six, put $A_d=\mathbb Z^{d-1}\oplus\mathbb Z/d$.
For $d>1$, use the cross-product generators of
Lemma~\ref{maps:src:D.1.10}, indexing the free basis by
$0,\ldots,d-2$. Index $i$ here corresponds to index $i+1$ in
Definition~\ref{mapsIII:def:fundamental-class-invariant}; this
renaming and its inverse preserve every group element and product.
Set
\[
 \mu_d=
 \sum_{0\le i\le j\le d-2}C_{ij}(\gamma_{ij}\times z_1)
 -12\sum_{i=0}^{d-2}(\beta_i\times z_2)
 \in H_6(K(A_d,2);\mathbb Z).
\]
Here $C$ is the principal submatrix on $0,\ldots,d-2$ of
Definition~\ref{mapsIII:def:cyclic-coefficient-data}: its diagonal
is $-2$, its two neighbouring diagonals are $1$, and its other
entries are zero. The free coordinates and the $z_3$ coefficient
of $\mu_d$ are zero. For $d=1$, put $A_1=0$ and $\mu_1=0$.
The cyclic classifying datum is
\[
 \mathcal I_d=(A_d,\ b_3=0,\ p=0,\ \mu_d),
\]
where $p$ is the refined Pontryagin class and the group-valued
invariants are expressed by a marking $H_2\to A_d$.
\end{definition}

\begin{theorem}[Smooth recognition of the cyclic covers]\hypertarget{tag-02K9}{}\label{maps:src:D.1.11}
{\normalfont\scriptsize tag 02K9}\par""", "D13", "mapsIII:def:cyclic-classifying-data",
          "Place the entire abstract group and marked fundamental class in a numbered input before recognition, including its exact principal matrix, index map, zero coordinates and d=1 endpoint. Print K9's small permanent tag with its unchanged anchors.")
e.replace(r"""For each $d\geq1$ prime to six, let $M_d$ denote the oriented
simply connected spin six-manifold with second homology
$A_d=\mathbb Z^{d-1}\oplus\mathbb Z/d$, third Betti number zero,
and refined Pontryagin class zero. For $d>1$, its full
fundamental-class invariant is determined by the zero integral
cubic and the finite-coefficient cubic of \ref{maps:src:D.1.9}
in the basis $x_0,\ldots,x_{d-2},u$, with $u$ evaluating to one
on the chosen cyclic generator. For $d=1$, the fundamental-class
invariant is zero. These data specify a unique oriented
diffeomorphism type, and""", r"""For each $d\ge1$ prime to six, the canonical manifold $M_d$ of
Definition~\ref{mapsIII:def:canonical-cyclic-model} is simply
connected and spin, and realizes the complete marked data
$\mathcal I_d$ of Definition~\ref{mapsIII:def:cyclic-classifying-data}.
These data specify a unique oriented diffeomorphism type among
closed simply connected spin six-manifolds. Every admissible
cover satisfies""", "D13", "maps:src:D.1.11",
          "State invariant realization and uniqueness for the explicitly constructed canonical Md, using the complete numbered data. This keeps every homology, spin, refined class, full cubic, all-cover and sphere conclusion without defining a unique object before uniqueness is proved.")
e.replace(r"""The derivative of the covering is the bundle isomorphism
\[
 TM\longrightarrow\pi^*TX_p,
 \qquad v_m\longmapsto(m,D\pi_m(v_m)),
\]
whose local inverse is the derivative of a covering-chart inverse.
It follows that $w_2(TM)=\pi^*w_2(TX_p)=0$, so $M$ is spin.""", r"""The covering derivative
$v_m\mapsto(m,D\pi_m(v_m))$, with inverse given in a covering
chart by the derivative of its local inverse, is the same complex
bundle map used in Proposition~\ref{maps:src:D.1.5}.
That proposition gives $w_2(TM)=0$, so $M$ is spin.""", "D12", "maps:src:D.1.11",
          "Use KE as the single owner of the covering spin-class conclusion through the identical derivative and its explicit inverse. Keep the distinct full downstairs mod-two UCT computation and unique-spin argument.")
e.replace(r"""Let $f_M:M\to K(H_2(M),2)$ induce the identity on $H_2$.
The intrinsic and marked fundamental-class invariants are
\[
 \mu(M)=(f_M)_*[M],
 \qquad \mu_d=K(\psi^{-1},2)_*\mu(M).
\]""", r"""Use $f_M$ and $\mu(M)$ from
Definition~\ref{mapsIII:def:fundamental-class-invariant}.
The marked class is $K(\psi^{-1},2)_*\mu(M)$.""", "D12", "maps:src:D.1.11",
          "Use the sole canonical definition of the intrinsic class and preserve the exact marking pushforward whose coefficients are proved next.")
start = e.text.index("The pullbacks of the marked coordinate classes are exactly\n", e.text.index("\\label{maps:src:D.1.11}"))
end = e.text.index("For $d=1$, \\ref{maps:src:D.1.4} gives $H_2=H_3=0$;", start)
e.replace(e.text[start:end], r"""The pullbacks of the marked coordinate classes are exactly
$x_0,\ldots,x_{d-2},u$. Lemma~\ref{maps:src:D.1.10} identifies
their full integral and finite-coefficient evaluation maps with
the cross-product coordinates of
Definition~\ref{mapsIII:def:cyclic-classifying-data}.
The integral cubic vanishes by Theorem~\ref{maps:src:D.1.6}.
Theorem~\ref{maps:src:D.1.9} gives mixed coefficients $C_{ij}$
and $-12$, and zero coefficient for $z_3$. Each cross-product
generator pairs to one with its own monomial and to zero with
the others. Thus the complete marked class is
$K(\psi^{-1},2)_*\mu(M)=\mu_d$ as defined there, including all
zero free coordinates. It depends only on $d$.
""", "D12", "maps:src:D.1.11",
          "Keep the full proof of every marked coefficient and the evaluation isomorphism, while giving the explicit mu_d formula its single numbered owner Q146. The map psi, cyclic normalization and zero coordinates are unchanged.")
e.replace(r"""Existence for every positive $d$ prime to six follows from
the canonical datum
\[
 (\ell_0,\ell_1,\ell_2,k_1,k_2,\sigma)
 =(0,-d,d,0,0,0).
\]
It is admissible and has
$p=12\ell_0-4\ell_1-3\ell_2=d$. Its member at $c=-i$
has $W=e^{-\pi}\in(0,216)$, so it lies in the domain of
the family in \ref{maps:src:D.1.7}.
Its universal cover realizes the data just computed.""", r"""For every positive $d$ prime to six, the canonical datum of
Definition~\ref{mapsIII:def:canonical-cyclic-model} is admissible
and has $p=4d-3d=d$. Its member at $c=-i$ has
$W=e^{-\pi}\in(0,216)$, in the parameter domain of
Theorem~\ref{maps:src:D.1.7}. Its cover $Z_d$, whose underlying
oriented manifold is $M_d$, realizes the data just computed.""", "D12", "maps:src:D.1.11",
          "Use the single canonical input/model definition and retain the complete realization reason, including both arithmetic and strict analytic parameter conditions.")

for old, new in [
    ("By \\ref{maps:src:D.1.4},\n", "By Theorem~\\ref{maps:src:D.1.4},\n"),
    ("in \\ref{maps:src:D.1.8} therefore gives $p(M)=0$.", "in Theorem~\\ref{maps:src:D.1.8} therefore gives $p(M)=0$."),
    ("\\ref{maps:src:D.1.6}. The class $u$ in \\ref{maps:src:D.1.9}", "Theorem~\\ref{maps:src:D.1.6}. The class $u$ in Theorem~\\ref{maps:src:D.1.9}"),
    ("For $d=1$, \\ref{maps:src:D.1.4} gives $H_2=H_3=0$;", "For $d=1$, Theorem~\\ref{maps:src:D.1.4} gives $H_2=H_3=0$;"),
]:
    e.replace(old, new, "D04", "maps:src:D.1.11", "Name the exact earlier theorem with its correct kind and permanent label.")

ka_head = r"\begin{theorem}[A canonical cyclic action and its quotient]\hypertarget{tag-02KA}{}\label{maps:src:D.1.12}"
e.replace(ka_head, ka_head + "\n{\\normalfont\\scriptsize tag 02KA}\\par", "D10", "maps:src:D.1.12", "Restore the required small tag after the existing title and number while preserving both permanent anchors.")
e.replace(r"""The complex structures on this quotient supplied by the
multiplicity-$(3,4)$ construction form the punctured-disc family
of \ref{maps:src:D.1.7},""", r"""The complex structures on this quotient arising from the
multiplicity-$(3,4)$ construction form the punctured-disc family
of Theorem~\ref{maps:src:D.1.7},""", "D08", "maps:src:D.1.12",
          "State the exact family scope directly and name its proved theorem, retaining the fixed-u count and every endpoint.")
e.replace(r"""Take the canonical datum
\[
 (\ell_0,\ell_1,\ell_2,k_1,k_2,\sigma)=(0,-d,d,0,0,0),
 \qquad c=-i.
\]
It is admissible: $p=4d-3d=d$, $3\nmid d$, $d$ is odd, and
$W=e^{-\pi}$ lies in $0<|W|<216$. Denote this member by $X_d$
and its universal-cover construction by $Z_d$.""", r"""Use the canonical member $X_d$ and its cover $Z_d$ from
Definition~\ref{mapsIII:def:canonical-cyclic-model}. The
admissibility and strict parameter conditions for this same
datum are verified in Theorems~\ref{maps:src:D.1.7} and
\ref{maps:src:D.1.11}.""", "D12", "maps:src:D.1.12",
          "Use the already defined identical canonical member and cover, with their actual arithmetic and analytic premise owners before this action proof. All action, quotient and inverse formulas remain.")

start = e.text.index("\\subsection{Smooth recognition and cyclic complex families}")
_, edits, issues = statement_records_to_small_tags(e.text[start:])
if issues:
    raise ValueError(issues)
for edit in edits:
    e.replace(edit.old, edit.new, edit.kind, edit.statement_label, edit.reason)
region = e.text[start:]
_, equation_edits, issues, aliases = remove_manual_equation_tags(region)
if issues or equation_edits:
    raise ValueError((issues, equation_edits))
print("Model-unit unresolved literal equation references:", unresolved_literal_equation_references(region, aliases))
e.finish(labels=("mapsIII:def:canonical-cyclic-model", "mapsIII:def:cyclic-classifying-data"), tags=("Q145", "Q146"))
