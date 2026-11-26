"""Publish the complete coefficient-cubic and fundamental-class unit."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor
from S6_SERIES_PUBLISH_c8_integrate_presentation import (
    statement_records_to_small_tags, remove_manual_equation_tags,
    unresolved_literal_equation_references,
)

e = Editor("cyclic_invariants", "c8-III-foundations-cyclic-cubics-", group="root")
e.replace(r"\subsection{Finite-coefficient cubics and the fundamental class}", r"""\subsection{Finite-coefficient cubics and the fundamental class}
\begin{definition}[Coefficient cubic and the fixed edge]\hypertarget{tag-Q143}{}\label{mapsIII:def:cyclic-coefficient-data}
{\normalfont\scriptsize tag Q143}\par
For the cyclic cover of Definition~\ref{mapsIII:def:cyclic-cohomology-data}
with $d>1$, put $R=\mathbb Z/d$ and use $x_j$ also for the
reduction in $H^2(M;R)$ of its integral divisor class.
Let $C_\delta$ be the image in $X_p$ of the complex toric curve
on the edge $\{0,e_2\}$ and its translates in the cusp cover.
For indices in $\mathbb Z/d$, set
\[
 C_{ii}=-2,\qquad C_{i,i+1}=C_{i,i-1}=1,
 \qquad C_{ij}=0\quad(j\notin\{i,i-1,i+1\}).
\]
The coefficient cubic is the symmetric trilinear pairing
$(a,b,c)\mapsto\langle abc,[M]\rangle$ on $H^2(M;R)$,
using the complex fundamental class.
\end{definition}
""", "D13", "mapsIII:def:cyclic-coefficient-data",
          "Give the coefficient ring, reduced divisor classes, geometric edge image, full cyclic matrix and cubic pairing a numbered definition. Uniqueness of the fixed curve and existence of its normalized cohomology class remain theorem conclusions.")
e.replace("[the finite-coefficient cubic]", "[Finite-coefficient cubic]", "D16", "maps:src:D.1.9", "Use the short mathematical theorem title.")
e.replace(r"""Let $d>1$ and let $C_\delta$ be the complex-oriented fixed curve of
the $\delta$ action downstairs. There is a class
$v\in H^2(X_p;\mathbb Z/d)$ with $v(C_\delta)=1$.
For $u=\pi^*v$ and the reductions of the classes $x_j$ in \ref{maps:src:D.1.6},
the full degree-two cubic, evaluated on the complex fundamental
class of $\widetilde X_p$, is""", r"""For $d>1$, the curve $C_\delta$ of
Definition~\ref{mapsIII:def:cyclic-coefficient-data} is the
complex-oriented fixed curve of the $\delta$ action on $X_p$.
There is a class $v\in H^2(X_p;R)$ with $v(C_\delta)=1$.
For $u=\pi^*v$, the full coefficient cubic is""", "D13", "maps:src:D.1.9",
          "Use the numbered input and keep both the geometric fixed-curve conclusion and the normalized class existence in the theorem, before their full proofs.")
e.replace("where $C_{ii}=-2$, $C_{i,i\\pm1}=1$ and all other entries are zero.\n", "",
          "D12", "maps:src:D.1.9", "The same complete cyclic matrix is defined once in Q143, with no numerical change.")
e.replace(r"""Put $M=\widetilde X_p$ and $R=\mathbb Z/d$. The marked normalized
component has boundary classes
\[
\begin{array}{c|cccccc}
\text{ray}&e_1&e_2&e_2-e_1&-e_1&-e_2&e_1-e_2\\
\text{class}&H-E_A-E_C&E_A&H-E_A-E_B&E_B&H-E_B-E_C&E_C.
\end{array}
\]
Their two branch pushforwards give $H=E_A+E_B+E_C$ in the cusp.
The ruling in \cref{maps:src:D.1.6} is $r=H-E_B=E_A+E_C$.""", r"""Use the marked normalization and coefficient data of
Definitions~\ref{mapsIII:def:cyclic-cohomology-data} and
\ref{mapsIII:def:cyclic-coefficient-data}. The six boundary classes
are those in Theorem~\ref{maps:src:D.1.6}, through the identity
on the same component and its complex-oriented rays. Its branch
pushforwards give $H=E_A+E_B+E_C$ in the cusp and
$r=H-E_B=E_A+E_C$.""", "D12", "maps:src:D.1.9",
          "Use KF's identical normalized component, ray classes and branch maps as the single owner of the repeated six-curve table; retain the two precise equalities needed here.")
e.replace(r"""Here $\mu_q$ is the positive base meridian. As in the relative
calculation of \cref{maps:src:D.1.6}, the inclusion of the dense
torus $T$ into a maximal affine chart contracts its three coordinates
radially inside the tube. Hence
$H_2(Y;\mathbb Z)\to H_2(Y,T;\mathbb Z)$ is injective.""", r"""Here $\mu_q$ is the positive base meridian. Under the identity
of the pair $(Y,T)$ with the pair in Theorem~\ref{maps:src:D.1.6},
the classes $N_v$ are its $n_v$ and $\mu_q$ is its $q$-circle.
Thus the relative homology map is that theorem's injective map
$H_2(Y;\mathbb Z)\to H_2(Y,T;\mathbb Z)$.""", "D12", "maps:src:D.1.9",
          "Identify the exact pair, normal-disc basis and positive meridian with KF's proven injection, retaining the two distinct delta-direction period chains that follow.")
e.replace("Evaluation on the actual fibre tori gives, respectively, $2h,0,12h$", "Evaluation on the fibre tori gives, respectively, $2h,0,12h$",
          "D08", "maps:src:D.1.9", "State the three explicit torus evaluations directly.")
e.replace(r"""makes $u$ deck invariant. For the normalization
$\eta_j:\mathrm dP_6\to D_j\subset M$, the period translation
from the component at $je_2$ to that at zero preserves the labeled
rays and commutes with projection downstairs. Hence""", r"""makes $u$ deck invariant. Use the normalization map
$\nu_j:\overline D_j\to M$ of
Definition~\ref{mapsIII:def:cyclic-cohomology-data}; it is the
same component map used here. The period translation from $je_2$
to zero preserves its labelled rays and commutes with projection
downstairs. Hence""", "D20", "maps:src:D.1.9",
          "Use the single normalization symbol nu_j for the identical component-domain map, preserving its ray and downstairs identifications.")
e.replace(r"\qquad \eta_j^*u=-5H-E_A+6E_B", r"\qquad \nu_j^*u=-5H-E_A+6E_B",
          "D20", "maps:src:D.1.9", "The pullback uses the identical normalization map now named nu_j; all coefficients and the intersection form remain.")
e.replace(r"=\langle(\eta_j^*u)^2,[\mathrm dP_6]\rangle", r"=\langle(\nu_j^*u)^2,[\overline D_j]\rangle",
          "D20", "maps:src:D.1.9", "Identify both the map and its positive normalized domain with Q142; the degree-one projection formula and value -12 remain unchanged.")

k8_head = r"\begin{lemma}[the cubic detects the complete fundamental-class invariant]\hypertarget{tag-02K8}{}\label{maps:src:D.1.10}"
e.replace(k8_head, r"""\begin{definition}[Cubic coordinates and the fundamental-class invariant]\hypertarget{tag-Q144}{}\label{mapsIII:def:fundamental-class-invariant}
{\normalfont\scriptsize tag Q144}\par
Let $r\ge0$, let $d\in\mathbb Z$ satisfy $\gcd(d,6)=1$, and put
$A=\mathbb Z^r\oplus\mathbb Z/d$. Write $e_1,\ldots,e_r$
for its free basis and $t=[1]$ for its cyclic generator.
Under the degree-two universal coefficient isomorphism, the
integral classes $x_i$ on $K(A,2)$ are the homomorphisms dual
to $e_i$. The class $u_0\in H^2(K(A,2);\mathbb Z/d)$ is the
cyclic projection. For arbitrary $a_i\in\mathbb Z/d$, put
$u=u_0+\sum_i a_ix_i$, using the same symbols for the reductions
of the integral $x_i$. These are exactly the classes with $u(t)=1$.

For a closed simply connected oriented six-manifold $N$, let
$f_N:N\to K(H_2(N),2)$ be the homotopy class corresponding to
$\operatorname{id}_{H_2(N)}$ under the degree-two universal
coefficient isomorphism. Its fundamental-class invariant is
\[
 \mu(N)=(f_N)_*[N]
 \in H_6(K(H_2(N),2);\mathbb Z),
\]
as defined in \cite[Sections~1.1--1.2, p.~794]{manZhubr75}.
\end{definition}

\begin{lemma}[Cubic detection of the fundamental-class invariant]\hypertarget{tag-02K8}{}\label{maps:src:D.1.10}""", "D13", "mapsIII:def:fundamental-class-invariant",
          "Number the full signed-d, nonnegative-rank coordinate data and Zhubr's exact classifying-map definition. The allowed u is written as the complete affine set of lifts, with the same evaluation condition used in the original proof.")
e.replace(r"""Let $A=\mathbb Z^r\oplus\mathbb Z/d$ with $\gcd(d,6)=1$.
The integral homology group of $K(A,2)$ in degree six is""", r"""For the group and coordinates of
Definition~\ref{mapsIII:def:fundamental-class-invariant},
the integral homology group of $K(A,2)$ in degree six is""", "D13", "maps:src:D.1.10",
          "State the detector theorem for its single numbered full input domain, including every rank and either sign of d.")
e.replace(r"""monomials $u x_i x_j$ ($i\leq j$), $u^2x_i$ and $u^3$, where
$u$ evaluates to one on the cyclic summand of $A$. Consequently
\ref{maps:src:D.1.9} and the integral cubic determine the complete class
$\mu(\widetilde X_p)$ in Zhubr's theorem.""", r"""monomials $u x_i x_j$ ($i\leq j$), $u^2x_i$ and $u^3$.
For cyclic covers with $d>1$, Theorem~\ref{maps:src:D.1.9}
and the integral cubic determine the complete class
$\mu(\widetilde X_p)$. For the cover with $d=1$, this class is zero.""", "D26", "maps:src:D.1.10",
          "Make the application of KI's d>1 hypothesis and the already proved trivial cyclic endpoint explicit in the statement; the generic signed-d detector range and every conclusion remain unchanged.")
e.replace(r"""Finally, for a simply connected oriented six-manifold $M$, the
degree-two universal coefficient isomorphism identifies
$\operatorname{id}_{H_2(M)}$ with the homotopy class of a map
$f_M:M\to K(H_2(M),2)$. Zhubr defines
\[
 \mu(M)=(f_M)_*[M]
 \quad\text{in }H_6(K(H_2(M),2);\mathbb Z)
\]
in \cite[Sections~1.1--1.2, p.~794]{manZhubr75}.""", r"""Apply the classifying map of
Definition~\ref{mapsIII:def:fundamental-class-invariant} to $M$.""",
          "D12", "maps:src:D.1.10", "Use the now numbered unique definition of the full classifying map and mu, keeping the following natural evaluation identity as its proof of detection.")
e.replace(r"cover with $d=1$, \ref{maps:src:D.1.4} gives $H_2=0$", r"cover with $d=1$, Theorem~\ref{maps:src:D.1.4} gives $H_2=0$",
          "D04", "maps:src:D.1.10", "Name the exact earlier integral-homology theorem that proves the endpoint.")

start = e.text.index("\\subsection{Finite-coefficient cubics and the fundamental class}")
end = e.text.index("\\subsection{Smooth recognition and cyclic complex families}")
_, edits, issues = statement_records_to_small_tags(e.text[start:end])
if issues:
    raise ValueError(issues)
for edit in edits:
    e.replace(edit.old, edit.new, edit.kind, edit.statement_label, edit.reason)
start = e.text.index("\\subsection{Finite-coefficient cubics and the fundamental class}")
end = e.text.index("\\subsection{Smooth recognition and cyclic complex families}")
region = e.text[start:end]
_, equation_edits, issues, aliases = remove_manual_equation_tags(region)
if issues or equation_edits:
    raise ValueError((issues, equation_edits))
print("Coefficient-unit unresolved literal equation references:", unresolved_literal_equation_references(region, aliases))
e.finish(labels=("mapsIII:def:cyclic-coefficient-data", "mapsIII:def:fundamental-class-invariant"), tags=("Q143", "Q144"))
