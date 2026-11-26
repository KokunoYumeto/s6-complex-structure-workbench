"""Write only the authorized III front fragment and exact local edit rows.

The section replacements are semantic editorial decisions after whole input
reading. The existing small-tag helper is used only for D10. No mathematical
check count, canonical file, global ledger or derived inventory is changed.
"""
from pathlib import Path
from hashlib import sha256
import csv
import re
from collections import Counter

import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'agents/continuation8_iii_integration/units/root/front_matter.tex'
RECORD = ROOT / 'agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_frontmatter_publication_defects.tsv'
EXPECTED = '4a214e656f0d3544b6a18e5f070fe34841af69eb69705ef7887c6f63d9b9a870'
original = PATH.read_text()
assert sha256(PATH.read_bytes()).hexdigest() == EXPECTED
text, small_tags, unresolved = presentation.statement_records_to_small_tags(original)
assert not unresolved
changes = [(e.kind, e.statement_label, e.old, e.new, e.reason) for e in small_tags]

def replace(start, end, new, kind, owner, reason):
    global text
    assert text.count(start) == 1, start
    i = text.index(start)
    j = text.index(end, i + len(start)) if end else len(text)
    old = text[i:j]
    new = new.rstrip() + '\n\n'
    changes.append((kind, owner, old, new, reason))
    text = text[:i] + new + text[j:]

replace(r'\begin{document}', r'\begin{abstract}', r'''
\begin{document}
\title{The $(3,4,\infty)$ family of complex six-spheres\\[.5em]III. Maps and the resulting manifolds}
\author{AI-produced mathematical text}
\date{25 November 2026}
\maketitle
'''.lstrip(), 'D15', 'sec:results', 'Date the current III candidate; retain the mathematical title and nonpersonal authorship.')

replace(r'\begin{abstract}', r'\clearpage', r'''
\begin{abstract}
We compute the homotopy classes of three maps associated with the
$(3,4,\infty)$ family of complex six-spheres. The torus quotient
represents the element of order two in $\pi_6(S^3)$, the holomorphic
map to $\mathbb P^1$ is null-homotopic, and the cusp map that keeps
the angular coordinate represents the nonzero element of $\pi_6(S^4)$.
Normal framings and integral attaching maps give these classes and a
finite cell model. For every cyclic universal cover we calculate the
integral cohomology ring and the complete smooth classification
invariant. We classify the natural section-line sphere fillings over
twenty-one elliptic profiles: there are $59$ marked patterns on $50$
initial data, with twelve profiles admitting unbounded multiplicity.
We also determine weighted smooth types and the homology of every free
OS49 affine cap, including its additional three-primary torsion. A
weighted OS45 member has zero refined Pontryagin class, as follows
from an embedded Hopf sphere and its critical-cycle linking number.
The local Kummer cover has no smooth compact global extension at
degree greater than one; an explicit finite flat normal extension
has additional components above the cusp. Finally, moving the zero
of the line-bundle linearization gives a conifold smoothing
diffeomorphic to $S^3\times S^3$, of algebraic dimension one.
\end{abstract}
'''.lstrip(), 'D15', 'sec:results', 'State the established mathematical outcomes within 250 words; remove production vocabulary and the obsolete unestablished-row sentence (D01/D08), and distinguish the smooth-extension obstruction from the normal construction.')

replace(r'\subsection{The series and this paper}', r'\subsection{The main theorems}', r'''
\subsection{The series and this paper}
The five papers study the periods, complex structures, maps and
degenerations of the $(3,4,\infty)$ torus-fibred family and the
manifolds obtained from its elliptic-surface construction. This paper
determines sphere-map classes, integral attachment invariants and
smooth types. The constructions include an ordered period lattice,
finite affine twists, positive normal circles and a cusp fan. The
table lists the principal results and their cross-paper inputs;
for Paper~III, the indicated uses are the quotient construction,
the section-line family and the return-map identification.
\begin{center}\small
\begin{tabularx}{\textwidth}{@{}lXX@{}}\toprule
Paper & Main result & Cross-paper inputs\\\midrule
I & Periods, moduli, fibre strata and the two ends of the family & ---\\
II & Cotangent obstruction and the sign theorem for degenerations & I, IV\\
III & Sphere-map classes, integral covers and elliptic smooth types &
I: \SeriesRef{mapsI:src:A.2.1}; II: \SeriesRef{push:src:A.1.2},
\SeriesRef{push:src:E.5.2}; IV: \SeriesRef{iv:correction:P3K.6},
\SeriesRef{night:P3K.7}\\
IV & Smooth return maps in $\Theta_7$ and cusp-fan calculations & I, II, III, V\\
V & Resolved fibre products and the marked rank-six fourfold family & I, III, IV\\
\bottomrule\end{tabularx}\end{center}
'''.lstrip(), 'D24', 'sec:results', 'Give the required one paragraph and one table; replace vague III input attribution by positively checked result-level I/II/IV uses. Preserve the other-paper entries for the joint verification without claiming that V has no use.')

replace(r'\subsection{The main theorems}', r'\hypertarget{main-III-A}{}', r'''
\subsection{The main theorems}
\hypertarget{tag-03KA}{}\label{series:III:main-theorems}
The marked family and its admissible twists are those of
Definition~\ref{mapsIII:def:marked-family}; its parameter range is
Definition~\ref{mapsIII:def:period-parameters}. We use the complex
orientation, positive normal circles and the outward stable framing.
The maps in Theorems~\ref{series:III:A}--\ref{series:III:C} have the
domains and based sphere identifications stated there. Each elliptic
construction in Theorem~\ref{series:III:F} includes its section line,
linearization zero, fan and affine cap data.
'''.lstrip(), 'D26', 'series:III:main-theorems', 'Remove the inaccurate common claim that the first four theorems use sphere twists; point to the existing numbered data and state individual domains below.')

replace(r'\hypertarget{main-III-A}{}', r'\hypertarget{main-III-B}{}', r'''
\hypertarget{main-III-A}{}
\begin{maintheorem}[Relative realization of the sphere quotient]
\hypertarget{tag-03KB}{}\label{series:III:A}
{\normalfont\scriptsize tag 03KB}\par
Let $X_p$ be an original sphere member, with its fixed oriented
identification with $S^6$, let $N$ be an open neighbourhood of
its cusp, and fix the quotient target $Q$
and a homeomorphism $\varphi:Q\to S^3$ as in
\SeriesRef{mapsI:src:A.1.3}. The cusp replacement of
\SeriesRef{mapsI:src:A.2.1}, with its prescribed outer collar and
image in the designated solid torus, defines the quotient homotopy
class used in this paper.

Every element of $[S^6,S^3]=\mathbb Z/12$ is represented by
$\varphi q$, where $q:X_p\to Q$ is smooth and agrees with the
torus quotient on $X_p\setminus N$. For the designated cusp
solid torus $T\subset Q$ and every $y\in T$,
\[
 \operatorname{im}\bigl(\pi_6(T,y)\longrightarrow
          \pi_6(S^3,\varphi(y))\bigr)=\{0\}.
\]
These relative assertions are proved in \cref{maps:src:A.2.2}.
\end{maintheorem}
\textit{Mechanism.} A map supported in an interior six-ball changes
the homotopy class by any element of $\pi_6(S^3)$, while the chosen
solid-torus target has zero sixth homotopy group.
\textit{Literature status.} New relative realization for the quotient
of \cite[Remark~8.3, pp.~22--23]{E26}.
'''.lstrip(), 'D26', 'series:III:A', 'State J3’s original-sphere exterior-agreement domain, fixed sphere identification and zero-image assertion; relative uniqueness is cited from I rather than inferred solely from pi6(T)=0. Remove process/navigation paragraphs (D08/D10/D15).')

replace(r'\hypertarget{main-III-B}{}', r'\hypertarget{main-III-C}{}', r'''
\hypertarget{main-III-B}{}
\begin{maintheorem}[The quotient and algebraic-reduction classes]
\hypertarget{tag-03KC}{}\label{series:III:B}
{\normalfont\scriptsize tag 03KC}\par
For a sphere member of the marked $(3,4,\infty)$ family, let
$e:X_p\to S^3$ be the quotient replacement with the target and
collar data of \SeriesRef{mapsI:src:A.2.1}. Then
\[
 [e]=6\nu'=\eta_3\eta_4\eta_5\ne0
       \quad\text{in }\pi_6(S^3)=\mathbb Z/12.
\]
Its stabilization is $12\nu\in\pi_3^{\mathrm S}=\mathbb Z/24$,
and its real Adams invariant is $1/2\in\mathbb Q/\mathbb Z$.
A regular inverse image is a three-torus with its Lie stable
framing, by \cref{maps:src:B.1.1,maps:src:B.1.2}.

The holomorphic map $f:X_p\to\mathbb P^1$ is null-homotopic.
Compatible frames of the two divisor line bundles give functions
$a,b$ with no common zero and
\[
 \begin{gathered}
 M f=[a^3:b^4]\simeq\eta_2 P_{3,4}G,\\
 G=\frac{(a,b)}{\sqrt{|a|^2+|b|^2}},
 \qquad M[x:y]=[x:y-x].
 \end{gathered}
\]
where $P_{3,4}(z_1,z_2)=(z_1^3,z_2^4)/\|(z_1^3,z_2^4)\|$
has degree twelve. The frame changes, homotopy and inverse
$M^{-1}[a:b]=[a:a+b]$ are given in \cref{maps:src:B.2.1}.
\end{maintheorem}
\textit{Mechanism.} The quotient framing gives the Lie-framed
three-torus, and the divisor-section homotopy factors the base map
through a degree-twelve map that kills $\pi_6(S^3)$.
\textit{Literature status.} New computations for these maps, using
\cite[Theorem~4.1 and Corollaries~4.2--4.3, pp.~76--77]{mapsToda52}
and \cite[Theorem~4.14, p.~423]{mapsAPS2}.
'''.lstrip(), 'D25', 'series:III:B', 'Replace the asserted exact factorization through e by the proved M f homotopy through the divisor-section map G, retaining the inverse base coordinate and every homotopy class and Adams value.')

replace(r'\hypertarget{main-III-C}{}', r'\hypertarget{main-III-D}{}', r'''
\hypertarget{main-III-C}{}
\begin{maintheorem}[The cusp map and an integral cell model]
\hypertarget{tag-03KD}{}\label{series:III:C}
{\normalfont\scriptsize tag 03KD}\par
For every sphere member in
Definition~\ref{mapsIII:def:retained-angle-cusp-data}, let
$H:X_p\to S^4$ be the based cusp map of
Definition~\ref{mapsIII:def:cusp-suspension-maps}. It keeps the
base angle and collapses the coordinate two-skeleton of the
three-torus before reduced suspension. Then
\[
 [H]=\eta_4\eta_5\ne0\in\pi_6(S^4)=\mathbb Z/2.
\]
Its regular inverse image is the vanishing two-torus with Lie stable
framing and Arf invariant one, as proved in \cref{maps:src:B.3.1}.

For the $p=-1$ three-filling datum of
Definition~\ref{mapsIII:def:three-filling-datum}, with zero cusp
translation drift, the mapping cylinders of the regular torus bundle,
the finite affine caps and the triangular cusp have a finite CW
homotopy model with cell counts
\[
 (c_0,c_1,c_2,c_3,c_4,c_5,c_6)=(5,20,45,56,42,17,3).
\]
Its integral attaching maps give $\pi_1=1$ and the integral homology
of $S^6$, hence the homotopy type of $S^6$
(\cref{maps:src:B.5.1,maps:src:B.5.2}).
\end{maintheorem}
\textit{Mechanism.} A periodic contraction of the normal-frame
comparison identifies the Lie torus, and the marked finite and cusp
attachments determine the integral cell complex.
\textit{Literature status.} New framing and cell calculations for
the sphere construction of \cite[Theorem~4.1, p.~12]{E26}.
'''.lstrip(), 'D26', 'series:III:C', 'Keep the full defined admissible |p|=1 retained-angle scope, and attach the numerical cell model to its actual p=-1, zero-drift datum; distinguish the CW homotopy model from a literal unaltered cell decomposition.')

replace(r'\hypertarget{main-III-D}{}', r'\hypertarget{main-III-E}{}', r'''
\hypertarget{main-III-D}{}
\begin{maintheorem}[Local Kummer maps and global extensions]
\hypertarget{tag-03KE}{}\label{series:III:D}
{\normalfont\scriptsize tag 03KE}\par
For the marked cusp of Definition~\ref{mapsIII:def:kummer-data}
and every integer $N\ge1$, the coordinate power map gives
\[
 \kappa_N:N_0^{\langle N\rangle}\longrightarrow N_0,
 \qquad (\xi_1,\xi_2,v)\longmapsto(\xi_1^N,\xi_2^N,v^N),
\]
a finite flat map of degree $N^3$ between smooth threefolds.
The source uses the correction $C_N(v)=C(v^N)/N$ and the same
triangular fan. Its factor over the normal base change $q=v^N$ is
\[
 Q_N:N_0^{\langle N\rangle}\longrightarrow
 N_0\mathbin{\times}_{\Delta_q}\Delta_v,
 \qquad \deg Q_N=N^2.
\]
For $N>1$, this factor is quasi-\'etale and its nonflat and
non-\'etale loci are the inverse images of the double and triple
strata; for $N=1$ both maps are identities.

For $N>1$, $\kappa_N$ is never the restriction, even to one cusp
component, of a finite map to $X$ from a connected smooth compact
complex source. It also has no normal compact extension whose
entire cusp preimage is this single prescribed map. There is,
however, a connected finite flat cover $Y_N\to X$ with normal
compact source, branched only over $S_1\cup S_2\cup W$, of degree
\[
 N^2|G_N|,\qquad
 G_N=\langle(A_1,-1),(A_2,0)\rangle
       \subset\operatorname{GL}_4(\mathbb Z/N)\times\mathbb Z/N.
\]
One component over the cusp is exactly $\kappa_N$; for $N>1$
another component contains a singular point. These statements,
including the identity extension for $N=1$, are
\cref{maps:src:C.1.1,maps:src:C.1.2,maps:src:C.1.3,maps:src:C.1.4,maps:src:C.1.5}.
\end{maintheorem}
\textit{Mechanism.} Smoothness on adjacent fan cones forces a scalar
toric lattice, while monodromy changes the Kummer lattice and a
finite semidirect quotient supplies the normal global cover.
\textit{Literature status.} New obstruction and completion for this
cusp, using the covering classification in
\cite[Theorem~1.38, pp.~67--68]{Hatcher2002}.
'''.lstrip(), 'D26', 'series:III:D', 'Name each absolute, relative and global map with its own domain, base change and degree; preserve both obstruction scopes, every N endpoint and the additional cusp-component conclusion. Do not call the relative degree-N^2 map flat.')

replace(r'\hypertarget{main-III-E}{}', r'\hypertarget{main-III-F}{}', r'''
\hypertarget{main-III-E}{}
\begin{maintheorem}[The cyclic universal covers]
\hypertarget{tag-03KF}{}\label{series:III:E}
{\normalfont\scriptsize tag 03KF}\par
For every admissible member $X_p$ of the marked family, put $d=|p|$;
then $d\ge1$ and $\gcd(d,6)=1$. Its fundamental group is
$\mathbb Z/d$, and its simply connected universal cover has
\[
 H_2(\widetilde X_p)=\mathbb Z^{d-1}\oplus\mathbb Z/d,
 \qquad H_3(\widetilde X_p)=\mathbb Z/d,
 \qquad \chi(\widetilde X_p)=2d.
\]
It is spin, $c_2=p_1=0$ integrally, and its refined Pontryagin
class is zero. For $d>1$, the $d$ cusp-divisor classes $x_i$ have
sole relation $\sum_i x_i=0$ and satisfy
\[
 x_i x_j=C_{ij}\kappa,\qquad
 C_{ij}=\mathbf1_{j=i+1}+\mathbf1_{j=i-1}-2\mathbf1_{j=i},
\]
with indices modulo $d$ and $\kappa$ a generator of the order-$d$
subgroup of $H^4$. There is a marked cyclic coordinate
$u\in H^2(\widetilde X_p;\mathbb Z/d)$ for which the integral
cubic is zero and
\[
 \langle ux_ix_j,[\widetilde X_p]\rangle=C_{ij},\qquad
 \langle u^2x_i,[\widetilde X_p]\rangle=-12,\qquad
 \langle u^3,[\widetilde X_p]\rangle=0\pmod d.
\]
These give the complete fundamental-class invariant, including
all zero coordinates, in
Definition~\ref{mapsIII:def:cyclic-classifying-data}.

The canonical manifold $M_d$ of
Definition~\ref{mapsIII:def:canonical-cyclic-model} realizes these
data and is the unique oriented smooth type with them among closed
simply connected spin six-manifolds. Every admissible cover satisfies
$\widetilde X_p\cong M_d$, and $M_1=S^6$
(\cref{maps:src:D.1.4,maps:src:D.1.6,maps:src:D.1.8,maps:src:D.1.9,maps:src:D.1.10,maps:src:D.1.11}).
\end{maintheorem}
\textit{Mechanism.} Integral cusp and cap maps determine the groups,
and the divisor products and finite-coefficient cubic determine the
complete marked spin-bordism invariant.
\textit{Literature status.} New cover invariants for the family of
\cite[Theorems~7.17 and~7.22, pp.~57, 60]{AC26}, recognized by
\cite[Theorem~3, p.~795; \S4.1, p.~809]{manZhubr75}.
'''.lstrip(), 'D26', 'series:III:E', 'Expose the full admissible d domain, canonical realization and complete classifying data; retain every group and type assertion with the actual b3=0 marked-recognition proof rather than an unspecified classification invocation.')

replace(r'\hypertarget{main-III-F}{}', r'\hypertarget{main-III-G}{}', r'''
\hypertarget{main-III-F}{}
\begin{maintheorem}[Elliptic sphere fillings and weighted smooth types]
\hypertarget{tag-03KG}{}\label{series:III:F}
{\normalfont\scriptsize tag 03KG}\par
\begin{enumerate}[label=(\alph*),leftmargin=*]
\item For the natural line $M=\mathcal O(P-O)$, allow all section
pairs, component-supported linearization zeros, original and Mumford
fillings, additive and regular logarithms, multiplicities and affine
twists in the sector of \cref{maps:src:D.2.22}. With the marked
patterns of Definition~\ref{maps:def:marked-filling-pattern}, there
are exactly $59$ sphere patterns on $50$ initial rows over the
twenty-one profiles in \cref{maps:src:D.2.28}. Twelve profiles admit
unbounded sphere multiplicities, four require every logarithmic
order to be one, and five admit none. Every sphere output is
orientation-preservingly diffeomorphic to $S^6$; the complete affine
and multiplicity conditions are \eqref{maps:eq:D.HY3}--\eqref{maps:eq:D.HY5}.

\item For every positive weight $d$, the Engel data of
Definition~\ref{maps:def:weighted-engel-data}, with
$m_0=3k$, $m_1=4\ell$, $k,\ell>0$ and
$m_1n_0+m_0n_1=\pm1$, give one oriented smooth type $M_d$ for
all the allowed affine twists. It has
\[
 H_2=\mathbb Z^{d-1}\oplus\mathbb Z/d,\quad
 H_3=\mathbb Z/d,\quad c_1=c_2=\lambda=P_{\rm ref}=0.
\]
Its full fundamental-class invariant is
\eqref{maps:eq:D.WI15}, including the Pontryagin square modulo
$d\gcd(d,2)$ and third power modulo $d\gcd(d,3)$, with values
$-12$ and $0$. For $d$ prime to six this is the type of
Theorem~\ref{series:III:E}, under the marking of
\cref{maps:src:D.2.48}.

\item For the OS45 data of Definition~\ref{maps:def:weighted-os45-data},
namely $P=2G$, $Q=8G$, weights $(2,0,0,0,0)$ at $I_8,4I_1$,
the triangular Mumford caps and ordinary clutch $e=1$, the
manifold is simply connected and satisfies
\[
 H_2=\mathbb Z^{15}\oplus\mathbb Z/8,
 \qquad H_3=\mathbb Z/8,
 \qquad c_1=c_2=\lambda=P_{\rm ref}=0.
\]
Its primitive integral cubic and complete fundamental-class
invariant are given in \cref{maps:src:D.2.53}.

\item For the OS49 affine cap with $m=3k$, $k>0$ and
$\ell=n(e_\gamma-e_u)+d\delta$, $n,d\in\mathbb Z$, freeness
is equivalent to
\[
 \gcd(k,n,d)=1,\qquad 3\nmid n\ \text{or}\ 3\mid k.
\]
Its fundamental group is $\mathbb Z/|n|$, with
$\mathbb Z/0=\mathbb Z$. For $n\ne0$, putting
$g=\gcd(3k,n,3d)\in\{1,3\}$ gives
\[
 H_1=H_4=\mathbb Z/|n|,\qquad
 H_2=H_3=\mathbb Z/|n|\oplus\mathbb Z/g,\qquad H_5=0.
\]
For $n=0$, freeness is $3\mid k$ and $\gcd(k,d)=1$, and
\[
 H_1=H_5=\mathbb Z,\quad
 H_2=H_3=\mathbb Z^2\oplus\mathbb Z/3,\quad H_4=\mathbb Z^2.
\]
In both cases $H_0=H_6=\mathbb Z$. The sphere sector is exactly
$n=\pm1$. In the coprime sector $\gcd(n,3k)=1$ one has $g=1$;
the free triple $(m,n,d)=(9,3,1)$ has $g=3$ and
$H_2=H_3=(\mathbb Z/3)^2$
(\cref{night:P3F.33,night:P3F.34}).
\end{enumerate}
\end{maintheorem}
\textit{Mechanism.} Primitive specialization and oriented normal-torus
maps give the integral attachment groups, while cusp intersections
and framed critical-cycle linkings determine their smooth invariants.
\textit{Literature status.} New classifications for these explicit
data within the section-line construction of
\cite[Remark~8.5, p.~24]{E26}.
'''.lstrip(), 'D26', 'series:III:F', 'State all four proved domains: the natural-line pattern sector, all positive simply connected Engel weights, the fixed OS45 datum, and the complete SA free affine sector including n=0. The (9,3,1) example remains valid in the last sector; no new SB refutation. Move the residual-type references to the descriptive further-results list (D12/D15), retaining their exact owners.')

replace(r'\hypertarget{main-III-G}{}', r'\paragraph{Further results.}', r'''
\hypertarget{main-III-G}{}
\begin{maintheorem}[A conifold smoothing on $S^3\times S^3$]
\hypertarget{tag-03KH}{}\label{series:III:G}
{\normalfont\scriptsize tag 03KH}\par
Let $S\to\mathbb P^1$ have fibres $IV^*,III,I_1$ at $0,1,\infty$,
let $L=\mathcal O_S(P-O)$, and use $T=t_{6P}$ and
$L\otimes T^*L^{-1}\simeq\pi^*\mathcal O(1)$ with the direction
and sphere twists of \cref{maps:src:D.3.1}. Choose sections
$\phi_0,\phi_1$ vanishing at $\infty,0$, with
$\phi_0=q\phi_1$ near infinity, and put
$\phi_s=\pi^*(\phi_0-s\phi_1)$.

For every sufficiently small fixed $u\ne0$ there is a proper flat
family $\mathcal Y_u\to\Delta_s$, also proper and flat over
$\mathbb P^1\times\Delta_s$. Its central fibre contracts one
$(-1,-1)$-curve of the original sphere to an ordinary double point;
its local equation is
\[
 xy=u(zv-s),\qquad q=zv.
\]
For $0<|s|\ll1$ its complex-oriented smooth fibre is
orientation-preservingly diffeomorphic to $S^3\times S^3$ and has
algebraic dimension one. The surgery replaces $S^2\times D^4$ by
$D^3\times S^3$, with primitive boundary maps. Its middle form is
the standard integral skew form and $w_2=p_1=0$
(\cref{maps:src:D.3.1,maps:src:D.3.2,maps:src:D.3.3}).
\end{maintheorem}
\textit{Mechanism.} The moving section gives the node equation,
and the oriented boundary maps of its smoothing determine the
middle homology and smooth surgery type.
\textit{Literature status.} New moving-zero family from
\cite[Proposition~2.4 and Propositions~2.7--2.8, pp.~5--7]{E26},
with smooth recognition by \cite[Theorem~2.6, p.~8]{BHS19}.
'''.lstrip(), 'D26', 'series:III:G', 'Specify the same elliptic surface, directed line, sphere twists and fixed nonzero u/s domains as M0–M2; keep properness, local equation, surgery, orientation and algebraic dimension.')

replace(r'\paragraph{Further results.}', r'\subsection{The proofs in outline}', r'''
\paragraph{Further results.}
\begin{itemize}[leftmargin=*]
\item \Cref{maps:src:B.3.2,maps:src:B.3.3}: angle-forgetting maps are
null-homotopic, and the cusp-core map has class $(6\nu',0,0)$ in its
specified $S^3\vee S^2$ cofiber coordinates.
\item \Cref{mapsaudit:finite-degree-three}: the two finite pullback
lattices in degree three have indices one and two, with all transfer maps.
\item \Cref{maps:src:D.1.7,maps:src:D.1.12}: the cyclic models have
the parameter disc $0<|W|<216$ and explicit cyclic quotient actions.
\item \Cref{maps:src:D.2.22}: height and component tests give
$172$ natural section-line initial data and $226$ with vertical corrections.
\item \Cref{maps:src:D.2.18}: the three-component cusp gives the
flag-manifold summand in the oriented type of its sphere-group sector.
\item \Cref{maps:src:D.2.20,maps:src:D.2.21}: integral groups and
oriented smooth types for six primitive original families and mixed fillings.
\item \Cref{maps:src:D.2.29,maps:src:D.2.30}: finite additive caps
with arbitrary contracting-character index and affine twists.
\item \Cref{maps:src:D.2.31,maps:src:D.2.32,maps:src:D.2.33}:
integral cap maps for the full natural catalogue with original fillings.
\item \Cref{maps:src:D.2.35,maps:src:D.2.36,maps:src:D.2.38,
maps:src:D.2.42,maps:src:D.2.44,maps:src:D.2.45}: smooth types of
the enumerated minimal and residual families from their full integral invariants.
\item \Cref{maps:src:D.2.46,maps:src:D.2.47}: whole-fibre
attachment groups and the trilinear divisor formula for finite-index cusp lattices.
\item \Cref{maps:src:D.2.51,maps:src:D.2.52}: invariant-Chern
original caps, their marked kernels and height-integral section pairs.
\item \Cref{night:P3F.31,night:P3F.32}: zero smooth return for
the OS49 sphere caps, with product mapping tori.
\item \Cref{wb:cusp-cover-extension-theorem,wb:cusp-cover-naive-action-failure}:
normalization, conductor and deck action for arbitrary holomorphic cusp corrections.
\item \Cref{wb:cusp-spec-globalization-obstruction}: global torus
quotients, their intrinsic distances and their extension obstructions.
\item \Cref{wb:cusp-cone-target-homotopy-types}: the compact cusp
carriers have explicit wedge and smash decompositions with marked homology generators.
\item \Cref{wb:cusp-null:thm,wb:cusp-s12-one-copy-invariant}:
a framed cusp nullbordism and the coefficient calculation for the sphere carriers.
\item \Cref{wb:sphere-metric-scaling-trichotomy,
wb:cusp-cone-sharp-global-R4-scope}: radial scaling limits and the
correspondence between Euclidean cells, compact targets and boundary fibres.
\item \Cref{maps:src:E.2.2}: transverse pullbacks realize
$S^6\times N$ with the stated complex and topological data.
\end{itemize}
'''.lstrip(), 'D15', 'series:III:main-theorems', 'Replace the tag-only result table by selected descriptive one-line results. Every formerly listed statement remains in its complete body home; the old table contained no additional theorem, hypothesis or proof. Preserve the residual-family scope through its corrected body owners.')

replace(r'\subsection{The proofs in outline}', r'\hypertarget{outline-III-A}{}', r'''
\subsection{The proofs in outline}
'''.lstrip(), 'D10', 'series:III:main-theorems', 'Keep the required outline subsection without navigation apparatus.')

replace(r'\hypertarget{outline-III-A}{}', r'\hypertarget{outline-III-B}{}', r'''
\hypertarget{outline-III-A}{}
\subsubsection*{Theorem A: relative sphere quotients}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item\hypertarget{step-III-A-1}{} The primitive invariant character
gives the fibrewise circle quotient, and the integral period maps fix
its signed meridian (\SeriesRef{mapsI:src:A.1.1}).
\item\hypertarget{step-III-A-2}{} The cusp replacement has its image
in the designated solid torus and is fixed on the outer collar;
its relative homotopy assertion is \SeriesRef{mapsI:src:A.2.1}.
\item\hypertarget{step-III-A-3}{} A based collapse $c:S^6\to S^6$,
homotopic to the identity, is constant off an interior six-ball.
Quaternionic multiplication gives
$e_g(x)=e(x)e(c(x))^{-1}g(c(x))$, which equals $e$ on the exterior
and is homotopic to any chosen $g$ (\cref{maps:src:A.2.2}).
\item\hypertarget{step-III-A-4}{} Relative smooth approximation
keeps the exterior fixed. A based map into $S^1\times D^2$
contracts by lifting its circle coordinate and contracting its disc
coordinate, proving the zero image in degree six
(\cref{maps:src:A.2.2}).
\end{enumerate}
'''.lstrip(), 'D25', 'series:III:A', 'Use the actual multiplication/collapse homotopy and separate the proved relative cusp assertion from the pi6(T)=0 calculation; retain all four outline anchors.')

replace(r'\hypertarget{outline-III-B}{}', r'\hypertarget{outline-III-C}{}', r'''
\hypertarget{outline-III-B}{}
\subsubsection*{Theorem B: the two map classes}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item\hypertarget{step-III-B-1}{} The common invariant mod-two
covectors are generated by $\gamma$. The framing difference therefore
lifts to $\operatorname{Spin}(7)$ on every coset of $\ker\gamma$
(\cref{maps:src:B.1.1}).
\item\hypertarget{step-III-B-2}{} Integral duality identifies the
common degree-three invariant with $\gamma u w$, whose restriction
to that kernel is zero. Transfer and torsion-freeness of $H^3(T^3)$
kill the remaining lifted framing obstruction
(\cref{maps:src:B.1.1}).
\item\hypertarget{step-III-B-3}{} The framed regular fibre is the
Lie torus, with stable class $\eta^3=12\nu$; its periodic Dirac
operator has paired nonzero eigenvalues and a two-dimensional kernel,
giving real Adams invariant $1/2$ (\cref{maps:src:B.1.2}).
\item\hypertarget{step-III-B-4}{} Stabilization sends
$\nu'\mapsto2\nu$ and is injective on $\mathbb Z/12$.
It therefore identifies the quotient class with $6\nu'$ and
$\eta_3\eta_4\eta_5$ (\cref{maps:src:B.1.2}).
\item\hypertarget{step-III-B-5}{} The divisor multiplicities
$3S_1,4S_2$ and $H^1(X)=H^2(X)=0$ give compatible line frames:
$e'_j=e^{-b_j/m_j}e_j$, with inverse $e_j=e^{b_j/m_j}e'_j$.
Their sections satisfy $M f=[a^3:b^4]$ (\cref{maps:src:B.2.1}).
\item\hypertarget{step-III-B-6}{} With
$r=(|a|^2+|b|^2)^{1/2}$, the homotopy
$[a^3e^{-3s\log r}:b^4e^{-4s\log r}]$ joins $M f$ to
$\eta_2P_{3,4}G$. The radial coordinate of $P_{3,4}$ is strictly
increasing and its phase degrees are three and four, so its degree
is twelve (\cref{maps:src:B.2.1}).
\item\hypertarget{step-III-B-7}{} Degree classification identifies
$P_{3,4}$ with the quaternionic power map $q\mapsto q^{12}$,
whose induced action is multiplication by twelve on $\pi_6(S^3)$.
Composing the resulting null-homotopy with $\eta_2$ and then
$M^{-1}$ proves $[f]=0$ (\cref{maps:src:B.2.1}).
\end{enumerate}
'''.lstrip(), 'D25', 'series:III:B', 'Replace the false equality f=H P e by J6’s exact divisor frames, G, explicit homotopy and inverse M; keep all seven anchors, quotient framing and real Adams normalization.')

replace(r'\hypertarget{outline-III-C}{}', r'\hypertarget{outline-III-D}{}', r'''
\hypertarget{outline-III-C}{}
\subsubsection*{Theorem C: the cusp frame and cell attachments}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item\hypertarget{step-III-C-1}{} The period-dependent unit change
and its inverse place the full regular inverse-image torus in one
triple-point chart; differentiation includes the bounded period term
(\cref{wb:h24:ret:chart-lemma,mapsIII:lem:retained-angle-differential}).
\item\hypertarget{step-III-C-2}{} The ordered normal and tangent
frame is $D(a,b)G_0$, with
$D=\operatorname{diag}(e^{-i(a+b)},e^{ia},e^{ib})$.
Two periodic $\operatorname{SU}(2)$ contractions identify its stable
framing with the Lie framing (\cref{wb:h24:ret:framing-proposition}).
\item\hypertarget{step-III-C-3}{} The Lie torus has Arf invariant
one. Based smoothing protects the full regular fibre, and
Freudenthal injectivity gives $[H]=\eta_4\eta_5$
(\cref{mapsIII:lem:lie-torus-spin-invariant,maps:src:B.3.1}).
\item\hypertarget{step-III-C-4}{} The torus-extension homotopy
contracts both angle-forgetting maps. The cusp-core collapse is
homotopic to the quotient followed by its core cofiber map, giving
$(6\nu',0,0)$ in the specified wedge coordinates
(\cref{maps:src:B.3.2,maps:src:B.3.3}).
\item\hypertarget{step-III-C-5}{} For the $p=-1$ datum, the finite
map $[x,\theta]\mapsto[x+\theta v_j/m_j]$ includes the logarithmic
drift, and the cusp seam is
$[a,b,\theta]\mapsto[a,b-\theta(B_0a-v(a))]$.
The coordinate identifications give the three mapping cylinders
(\cref{maps:src:B.5.1}).
\item\hypertarget{step-III-C-6}{} The marked boundary tori meet
the product-collar criterion of
\cite[Theorem~6.1, p.~77]{mapsWaldhausen68}. Cellular approximation
of the torus return and attaching maps gives the displayed cell
counts, whose alternating sum is two (\cref{maps:src:B.5.1}).
\item\hypertarget{step-III-C-7}{} The integral finite and cusp maps
kill the fundamental group and the degree-two attachment cokernel.
Duality and the Euler number give sphere homology; Hurewicz and
Whitehead give the homotopy sphere (\cref{maps:src:B.5.2}).
\end{enumerate}
'''.lstrip(), 'D26', 'series:III:C', 'Match each outline claim to the current single-owner framing, nullity and cell proofs; preserve the p=-1 restriction for counts and the exact wedge comparison. All seven anchors remain.')

replace(r'\hypertarget{outline-III-D}{}', r'\hypertarget{outline-III-E}{}', r'''
\hypertarget{outline-III-D}{}
\subsubsection*{Theorem D: Kummer lattices and normal completion}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item\hypertarget{step-III-D-1}{} On $q=v^N$ the source correction
$C(v^N)/N$ makes the power map equivariant. The chart basis gives
absolute degree $N^3$; the invariant-ring factor over the base change
has degree $N^2$ and image lattice
$\langle\widehat\gamma,\widehat u,N\widehat w,N\widehat\delta\rangle$
(\cref{maps:src:C.1.1}).
\item\hypertarget{step-III-D-2}{} Adjacent unimodular triangles
give reciprocal divisibility conditions on the primitive ray indices.
Their equality forces the cocharacter lattice of a smooth cover of
the entire cusp fan to be $n\mathbb Z^3$
(\cref{maps:src:C.1.2}).
\item\hypertarget{step-III-D-3}{} The order-four meridian carries
$L_N$ to a lattice with toric intersection
$\mathbb Z\widehat w\oplus N\mathbb Z\widehat\delta$.
The primitive first generator forces a scalar index one, while the
second has index $N$; this excludes a smooth compact extension for
$N>1$ (\cref{maps:src:C.1.3}).
\item\hypertarget{step-III-D-4}{} The lattices
$D^aM_0^bL_N$, $0\le a,b<N$, for
$D=A_2^2A_1A_2^2A_1^{-1}$, are distinct. A normal extension with
only the prescribed cusp component would have Stein base degree
$N$, contradicting its orbit of at least $N^2$ sheets
(\cref{maps:src:C.1.4}).
\item\hypertarget{step-III-D-5}{} The subgroup of
$(\mathbb Z/N)^4\rtimes G_N$ generated by the two long periods
has index $N^2|G_N|$ and the required cusp intersection.
Fractional monomials in each half-open fundamental box form a free
basis of its normal completion; uniqueness of normalization glues
the charts and their inverse overlaps (\cref{maps:src:C.1.5}).
\end{enumerate}
'''.lstrip(), 'D26', 'series:III:D', 'Keep the five anchors and each distinct map/degree/domain. Separate K5’s orbit obstruction from K6’s semidirect cover; the latter’s global degree is N^2|G_N|.')

replace(r'\hypertarget{outline-III-E}{}', r'\hypertarget{outline-III-F}{}', r'''
\hypertarget{outline-III-E}{}
\subsubsection*{Theorem E: integral invariants of the cyclic covers}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item\hypertarget{step-III-E-1}{} The cyclic character identifies
the cusp cover with the period sublattice
$\mathbb Z\widehat u\oplus d\mathbb Z\widehat\gamma$.
Its normalization has $d$ components and its Laurent relation
matrix reduces to $\operatorname{diag}(1,t-1,t-1,0)$
(\cref{maps:src:D.1.2}).
\item\hypertarget{step-III-E-2}{} The nontrivial deck characters
give acyclic regular-fibre complexes. The integral finite pullbacks
and cusp sweeps determine the free groups and the order-$d$
torsion in degrees two and three
(\cref{maps:src:D.1.3,maps:src:D.1.4}).
\item\hypertarget{step-III-E-3}{} Positive normal Thom classes
give the divisor relation $\sum x_i=0$; restrictions to each
normalized component give $x_ix_j=C_{ij}\kappa$
(\cref{maps:src:D.1.6}).
\item\hypertarget{step-III-E-4}{} A class evaluating to one on
the fixed $\delta$-curve pulls back to the cyclic coordinate $u$.
The component restrictions give the mixed cubic values
$C_{ij},-12,0$, and the full $H_6(K(H_2,2))$ decomposition
identifies every coordinate (\cref{maps:src:D.1.9,maps:src:D.1.10}).
\item\hypertarget{step-III-E-5}{} Degree-four pullback kills
$c_2$ and $p_1$; multiplication by four is injective on
$\mathbb Z^{d-1}\oplus\mathbb Z/d$, so the refined class is zero.
The marked spin-bordism classification with $b_3=0$ identifies
the cover with the constructed canonical $M_d$
(\cref{maps:src:D.1.8,maps:src:D.1.11}).
\item\hypertarget{step-III-E-6}{} Euler multiplicativity gives
$\chi=2d$. A connected sum of $g$ copies of $S^3\times S^3$
has Euler number $2-2g$; equality for $d>1$ would require the
negative value $g=1-d$. Thus these covers are excluded from
those connected-sum types (\cref{maps:src:D.1.1}).
\end{enumerate}
'''.lstrip(), 'D18', 'series:III:E', 'Correct the first outline’s supplying label to the cusp theorem KB; specify K8 full-coordinate detection and K9 canonical-member/b3=0 classification scope and exact retained obstruction. No H2/H3 rank mistranscription is repeated.')

replace(r'\hypertarget{outline-III-F}{}', r'\hypertarget{outline-III-G}{}', r'''
\hypertarget{outline-III-F}{}
\subsubsection*{Theorem F: specialization and characteristic invariants}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item\hypertarget{step-III-F-1}{} The height equality, component
equations and narrowness at every other reducible site give the
finite natural section-line initial set
(\cref{maps:src:D.2.22}).
\item\hypertarget{step-III-F-2}{} Primitive specialization and
the positive normal-torus maps identify the full integral cap
cokernels. For simply connected natural outputs their order is
$cR^2$, so the sphere condition is $c=R=1$ with the stated
fundamental-group criterion (\cref{maps:src:D.2.26}).
\item\hypertarget{step-III-F-3}{} The $I_3^*$ and $I_1^*$
obstructions eliminate five profiles. The remaining integral
presentations give $59$ patterns on $50$ initial rows and the
twelve/four/five multiplicity alternatives
(\cref{maps:src:D.2.24,maps:src:D.2.27,maps:src:D.2.28}).
\item\hypertarget{step-III-F-4}{} In the minimal and residual
families, the primitive cubic, refined class and full
fundamental-class image distinguish the stated surgeries and
smooth representatives (\cref{maps:src:D.2.35,maps:src:D.2.36,
maps:src:D.2.38,maps:src:D.2.42,maps:src:D.2.44,maps:src:D.2.45}).
\item\hypertarget{step-III-F-5}{} Component restrictions compute
the weighted cusp cubic, including loops and repeated incidences.
For the OS45 datum, the source-line Hopf sphere has differential
reference parity $\varepsilon_\rho=1$ and complete critical-cycle
linking number $-1$; the framed formula gives $P_{\rm ref}=0$
(\cref{maps:src:D.2.47,maps:src:D.2.53}).
\item\hypertarget{step-III-F-6}{} For the simply connected
weight-$d$ Engel data, the determinant $P=\pm1$ gives the primitive
groups. The refined class is zero and the complete coefficient
invariant contains the cyclic Cartan matrix, Pontryagin-square
value $-12$ and third-power value zero, proving the single type
$M_d$ for every $d>0$ (\cref{maps:src:D.2.48}).
\item\hypertarget{step-III-F-7}{} In the full free OS49 sector,
the invariant quotient coordinates $(\psi,-w+3\delta)$ give the
exact freeness criterion. The oriented normal circle and primitive
Gysin lattice have Smith factors $g,|n|$ for $n\ne0$; the
$n=0$ pair sequence gives the displayed free and order-three
summands (\cref{night:P3F.33,night:P3F.34}).
\end{enumerate}
'''.lstrip(), 'D26', 'series:III:F', 'Use the full revised natural, weighted and free-affine scopes; retain the completed residual smooth classifications with their individual owners, and use LV’s reference parity and complete linking value rather than a redundant global-frame shortcut.')

replace(r'\hypertarget{outline-III-G}{}', r'\subsection{Known and new}', r'''
\hypertarget{outline-III-G}{}
\subsubsection*{Theorem G: the conifold smoothing}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item\hypertarget{step-III-G-1}{} The section
$\phi_s=\phi_0-s\phi_1$ gives annular core and neck charts whose
overlap maps have reciprocal inverses and satisfy the line-bundle
cocycle (\cref{maps:src:D.3.1}).
\item\hypertarget{step-III-G-2}{} Their local equation is
$xy=u(zv-s)$. Uniform collars include the order-three and
order-four root caps in a proper flat family; its central node
has the stated small resolution (\cref{maps:src:D.3.1}).
\item\hypertarget{step-III-G-3}{} The quadric smoothing has an
explicit orientation-preserving identification with $TS^3$.
The complement of the exceptional sphere is two-connected,
and the primitive boundary column $(1,\pm1)^t$ gives
$H_3=\mathbb Z^2$, $H_2=H_4=0$ (\cref{maps:src:D.3.2}).
\item\hypertarget{step-III-G-4}{} The middle pairing is the
standard unimodular skew form and the normal invariant vanishes.
Wall's classification and $\Theta_6=0$ identify the complex-oriented
smoothing with $S^3\times S^3$ (\cref{maps:src:D.3.2}).
\item\hypertarget{step-III-G-5}{} The root canonical formula and
varying torus periods give algebraic dimension one; formal
cohomology across the exceptional curve gives
$(h^{0,0},h^{0,1},h^{0,2},h^{0,3})=(1,1,0,0)$.
The algebraic-reduction fibre maps also give the comparison with
Calabi--Eckmann deformations
(\cref{maps:src:D.3.3,maps:src:D.3.4}).
\end{enumerate}
'''.lstrip(), 'D26', 'series:III:G', 'Retain all five anchors and every construction, surgery and complex-invariant claim with the fixed nonzero parameter and primitive boundary maps of M0–M3.')

replace(r'\subsection{Known and new}', r'\subsection{Methodology}', r'''
\subsection{Known and new}
\begin{center}\small
\begin{tabularx}{\textwidth}{@{}lX@{}}\toprule
Theorem & Contribution and principal source relationship\\\midrule
A & New relative realization for Engel's quotient
\cite[Remark~8.3, pp.~22--23]{E26}.\\
B & New map classes; unstable suspension and the real Adams
formula are \cite[Theorem~4.1, pp.~76--77]{mapsToda52} and
\cite[Theorem~4.14, p.~423]{mapsAPS2}.\\
C & New cusp framing and marked cell presentation;
the sphere construction is \cite[Theorem~4.1, p.~12]{E26}.\\
D & New full-fan obstruction and normal extension;
covering classification is \cite[Theorem~1.38, pp.~67--68]{Hatcher2002}.\\
E & New complete cover invariant; marked smooth recognition uses
\cite[Theorems~3 and~5, pp.~795--796; \S4.1, p.~809]{manZhubr75}.\\
F & New natural-line and weighted classifications within
\cite[Remark~8.5, p.~24]{E26}.\\
G & New moving-zero family and its smooth type; the surgery
classification is \cite[Theorem~2.6, p.~8]{BHS19}.\\
\bottomrule\end{tabularx}\end{center}
'''.lstrip(), 'D12', 'sec:results', 'Replace verbatim repeated literature paragraphs by one short source-status row per main theorem, keeping exact primary locators and the bounded new contributions.')

replace(r'\subsection{Methodology}', r'\subsection{How the paper is organized}', r'''
\subsection{Methodology}
This text is AI-authored. GPT-5.6 Sol (OpenAI), in Codex at
reasoning effort ultra, produced the working edition during
24 August--9 September 2026. GPT-6 Astra (OpenAI), in ChatGPT Pro
mode, carried out the research of 12--16 November, independent
re-derivations during 16--18 November, writing during 16--20 November,
and publication work during 20--25 November 2026. Its numerical
reasoning-effort setting was not separately exposed. GPT-6 Astra Pro
(OpenAI), in ChatGPT Pro mode, continued the publication work on
25 November 2026, also without a separately exposed numerical
effort setting.

Claude Fable 5.2 (Anthropic), at effort high and at effort max,
and Claude Opus 5.5 (Anthropic), at effort max, performed readings,
intake checks and recomputations during 12--20 November 2026.
Claude Opus 5.5 at effort max rewrote Paper~V's abstract and
introduction on 20 November, read all of Paper~I on 21--22 November
and adjusted its deposited text and links, and read all of
Paper~II on 24 November. It also checked the publication material
received during 23--25 November, including arithmetic and
source-scope questions.

The models worked from explicit statements, marked geometric data
and primary sources. Proposed proofs and computations were passed
between them for comparison; disagreements were resolved at the
affected statement, map or parameter range. The checks include
derivations written before consulting earlier proofs, independent
proofs, exact arithmetic, interval computations and comparison with
the cited literature. Each computation is described mathematically
where it is used, and the programs are listed at the end of the paper.
During the publication work, existing proofs were reread in full
against their replacements, with coordinate maps, inverse maps and
exceptional parameters checked explicitly. Those readings record
their use and rechecking of existing arguments. The records state
the scope of each check and preserve every corrected assertion.
No human has checked the mathematics.

We dedicate this text to the public domain under
\href{https://creativecommons.org/publicdomain/zero/1.0/}{CC0 1.0 Universal}.
The \href{\SsixPublishRecords}{records page for Paper~III} gives
the statement checks, provenance and programs. The repository
commit is \texttt{\SsixRepositoryCommit}.
'''.lstrip(), 'D15', 'sec:results', 'Replace obsolete run labels, invented effort-Pro wording, stale numeric counts, local accompanying-file links and two historical repository addresses by evidenced model/date/method prose and exactly one prescribed records/commit macro use. Final counts and three-way provenance verification remain root-owned; no provisional totals or finished-paper claim is inserted.')

replace(r'\subsection{How the paper is organized}', None, r'''
\subsection{How the paper is organized}
The marked periods and relative sphere quotient come first. Integral
homology of the cyclic covers supplies the sphere framing; the base
map, angle-forgetting maps and cusp-frame calculation then determine
the homotopy classes. The three-filling cell model and finite-band
maps precede the Kummer construction and the complete cyclic
invariants. The elliptic-surface sections develop the initial data,
cap maps, sphere patterns and weighted smooth types, followed by the
OS49 family and the conifold smoothing. Global torus quotients lead
to the compact cusp carriers, their framed nullbordism and sphere-map
coefficients, and the metric scaling limits. The final part contains
the general section-line and multiplicity questions, auxiliary-cover
compactifications, the two raw carrier classes, and the remaining
cap-map and smooth-type classification in \cref{maps:src:D.2.4}.

\begin{figure}[htbp]\centering
\begin{tikzpicture}[>=stealth,every node/.style={font=\small,align=center},
 box/.style={draw,rounded corners,minimum width=2.25cm,minimum height=.7cm}]
\node[box] (P) at (1.5,0) {Marked periods\\and fillings};
\node[box] (L) at (6.5,0) {Elliptic surface\\and section line};
\node[box] (A) at (0,-1.35) {\hyperlink{main-III-A}{Theorem A}};
\node[box] (E) at (3.25,-1.35) {\hyperlink{main-III-E}{Theorem E}};
\node[box] (D) at (6.5,-1.35) {\hyperlink{main-III-D}{Theorem D}};
\node[box] (B) at (0,-2.75) {\hyperlink{main-III-B}{Theorem B}};
\node[box] (F) at (3.25,-2.75) {\hyperlink{main-III-F}{Theorem F}};
\node[box] (G) at (6.5,-2.75) {\hyperlink{main-III-G}{Theorem G}};
\node[box] (C) at (0,-4.1) {\hyperlink{main-III-C}{Theorem C}};
\draw[->,semithick] (P) -- (A);
\draw[->,semithick] (P) -- (E);
\draw[->,semithick] (P) to[bend left=13] (D);
\draw[->,semithick] (A) -- (B);
\draw[->,semithick] (E) -- node[above,sloped,font=\scriptsize]{homology} (B);
\draw[->,semithick] (B) -- (C);
\draw[->,semithick] (E) -- node[right,font=\scriptsize]{coprime weights} (F);
\draw[->,semithick] (L) to[bend right=18] (F);
\draw[->,semithick] (L.east) to[bend left=30] (G.east);
\end{tikzpicture}
\caption{Dependencies of the indicated arguments. The arrow from E
to B is the integral homology calculation in
\cref{maps:src:D.1.4} used by \cref{maps:src:B.1.1}; the arrow
from E to F is the marked coprime-weight identification in
\cref{maps:src:D.2.48}. The arrow from B to C uses the same
Hopf-circle class in \cref{maps:src:B.3.1}.}
\end{figure}
\clearpage
'''.lstrip(), 'D24', 'sec:results', 'Describe the actual root-approved body order, including early retained-angle frames and late nullbordism/carrier coefficients; replace the mostly isolated diagram by exact supplying-argument dependencies. Root retains final placement and render checks.')

def ids(s, command):
    return Counter(re.findall(r'\\' + command + r'\{([^}]+)\}', s))

assert ids(original, 'label') == ids(text, 'label')
assert ids(original, 'hypertarget') == ids(text, 'hypertarget')
assert '\\StatementRecord' not in text
assert text.count('\\SsixPublishRecords') == 1
assert text.count('\\SsixRepositoryCommit') == 1
assert '\r' not in text
abstract = text.split(r'\begin{abstract}', 1)[1].split(r'\end{abstract}', 1)[0]
assert len(abstract.split()) <= 250
assert len(re.findall(r'\\subsection\{', text)) == 6
assert len(re.findall(r'\\begin\{maintheorem\}', text)) == 7
PATH.write_text(text, newline='\n')

fields = ['change_id','type','statement_id','old_location','old_page',
          'new_location','new_page','old_text','new_text','reason','review_status']
with RECORD.open('w', newline='') as out:
    writer = csv.DictWriter(out, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    for i, (kind, owner, old, new, reason) in enumerate(changes, 1):
        old_pos = original.find(old)
        old_loc = (str(PATH.relative_to(ROOT)) + ':' + str(original.count('\n', 0, old_pos) + 1)
                   if old_pos >= 0 else str(PATH.relative_to(ROOT)) + '; after bounded D10 header removal')
        writer.writerow(dict(change_id=f'c8-III-frontmatter-{i:03}', type=kind,
            statement_id=owner, old_location=old_loc, old_page='pending final concordance',
            new_location=str(PATH.relative_to(ROOT)), new_page='pending final build',
            old_text=old, new_text=new, reason=reason,
            review_status='complete original front fragment read; final complete readback and substantive all-criteria review follow; source-local exposed comparison only; final counts, provenance, references, placement and PDF gates remain root-owned'))
print('FRONT_LINES', len(text.splitlines()))
print('FRONT_SHA256', sha256(PATH.read_bytes()).hexdigest())
print('ABSTRACT_WHITESPACE_WORDS', len(abstract.split()))
print('EXACT_EDIT_ROWS', len(changes))
print('LABEL_MULTIPLICITIES_PRESERVED', len(ids(text, 'label')))
print('TARGET_MULTIPLICITIES_PRESERVED', len(ids(text, 'hypertarget')))
print('SUBSECTIONS', 6, 'MAIN_THEOREMS', 7, 'NEW_TAGS', 0)
print('CANONICAL_WRITES', 0, 'DERIVED_WRITES', 0, 'CHECK_COUNT_CREDIT', 0)
