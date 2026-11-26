"""Exact publication restructuring of the wholly read L7/L8/L9 units."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def interval(e, start, end):
    if e.text.count(start) != 1 or e.text.count(end) != 1:
        raise ValueError(("Stale or ambiguous read interval", start, end))
    a, b = e.text.index(start), e.text.index(end)
    if a >= b:
        raise ValueError("Reversed interval")
    return e.text[a:b]


def main():
    e = Editor("original_cap_homology", "C8-FND-ORIGINAL-CAPS-")
    old = interval(e, r"\begin{theorem}[all zero-degree original caps and their free defects]", "The only nonzero local defects in this catalogue are\n")
    new = r"""\subsection{Original additive caps with zero component Chern class}

\begin{definition}[Zero-Chern original additive data]
\hypertarget{tag-Q126}{}\label{mapsIII:def:zero-chern-original-data}
{\normalfont\scriptsize tag Q126}\par
Use the natural initial rows of Theorem~\ref{maps:src:D.2.22},
with $P=aG$, $Q=bG$, $a,b>0$, $\gcd(a,b)=1$, and the periods of
Definition~\ref{mapsIII:def:elliptic-marked-data}. Write
$\omega=a e_1^*\wedge e_2^*-b\delta^*\wedge\gamma^*$.
Retain any original additive cap at which $P$ is narrow, with
any number of component orbits. At $I_n^*$ use the original cap;
at the finite good-reduction additive sites allow all choices and
free affine twists of Theorem~\ref{maps:src:D.2.30}. Keep the
preceding marked zero-free multiplicative and unique rank-two
zero models. Allow any number of regular logarithmic sites,
every permitted positive order and an integer clutch $e$.
For an original additive cap let $\rho_i$ be the number of
orbits of $Q$ on its components, and put
\[
 D=\sum_{i\text{ original additive}}(\rho_i-1).
\]
\end{definition}

\begin{theorem}[Zero-Chern original additive caps and component summands]
\hypertarget{tag-02L7}{}\label{maps:src:D.2.31}
{\normalfont\scriptsize tag 02L7}\par
The data of Definition~\ref{mapsIII:def:zero-chern-original-data}
give $228$ additive-filling patterns on $160$ natural initial rows.
Exactly $30$ patterns have a positive original component defect.
"""
    e.replace(old, new, "D13", "maps:src:D.2.31",
              "Give the original-cap choices, shared marking, all parameter domains and component-defect statistic one numbered definition and their own subsection; retain the enumerative assertions in the theorem.")
    e.replace("$N_M$ defined in Theorem~\\ref{maps:src:D.2.14}.",
              "$N_M$ defined in Definition~\\ref{mapsIII:def:twisted-smale-suspension}.",
              "D06", "maps:src:D.2.31", "Point the model to its actual preceding numbered definition.")
    old = interval(e, "Use the natural initial data of Theorem~\\ref{maps:src:D.2.22}\nand the period marking", r"\item \emph{The natural rows and additive choices.}")
    new = r"""Use Definition~\ref{mapsIII:def:zero-chern-original-data} and put
\(\chi=\gamma^*\) and
\(J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\).
The component point map \(+Q\), forward arrow \(-Q\), and pullback
on line coefficients use the corresponding maps below.

"""
    e.replace(old, new, "D20", "maps:src:D.2.31",
              "Use the one numbered period and area definition, preserving the explicit distinction and maps between point translation, forward return and pullback.")
    old = interval(e, r"For a profile of height \(1/d\), select a multiplicative \(I_\nu\)", "At each finite additive place its options are\n")
    new = r"""The $172$ natural rows and their exhaustive divisor/component
criterion are those of Theorem~\ref{maps:src:D.2.22}. The row
identification fixes the ordered profile, selected zero, positive
section pair $(a,b)$ and every component coordinate; its inverse
reads that same tuple. It therefore fixes every marked monodromy
and cocycle in Definition~\ref{mapsIII:def:elliptic-marked-data}.
"""
    e.replace(old, new, "D12", "maps:src:D.2.31",
              "Use KX as the sole owner of the already proved natural-row enumeration, with the explicit identity on every ordered input; retain the new additive option rule and full 228-pattern table.")
    old = interval(e, "The Hopf chart and the preceding trivialization reconstruct \\(X\\) as\n", "The enumeration gives precisely \\(D=0,1,2,4\\) when \\(b=1\\).\n")
    new = r"""Apply the precisely framed reconstruction in the proof of
Theorem~\ref{maps:src:D.2.16}. Its quotient, component-basis count
and torsion parameter are here \(\mathcal Q,D,R\), respectively;
the count called \(b\) in that reconstruction is \(D\), while
the section coefficient in the present theorem is \(b=1\).
The preceding parts have supplied its scalar normal product,
primitive free section spheres, zero exterior Euler class,
simply connected spin quotient and complete integral linking data.
The geometric maps are the following ones with those actual inputs.

The Hopf charts and the exterior trivialization give
\[
 M_-(\mathcal Q)=((\mathcal Q\setminus\mathring D^5)\times S^1)
                 \cup_g(S^4\times D^2),\qquad
 g(x,z)=(\alpha_zx,z),
\]
where \(g\) goes from complement to attached boundary and its
inverse uses \(\alpha_z^{-1}\). The cap action is
\(t(x,w)=(\alpha_tx,tw)\), with boundary orbit coordinate
\(\alpha_z^{-1}x\); this is the same quotient-disc coordinate.
The rotation lifts to \(\cos(\pi t)+\sin(\pi t)e_1e_2\),
with endpoints \(1,-1\), so the framing loop is nontrivial.
The matrix and collar map from that reconstruction satisfy
\[
 A=\operatorname{diag}(1,-1,-1,1,1),\qquad
 A\alpha_zA^{-1}=\alpha_z^{-1},\qquad
 F_{\mathcal Q}|_{\partial}=A.
\]
The maps \(F_{\mathcal Q}\times\mathrm{id}\) and
\(A\times\mathrm{id}\) therefore glue to the oriented map
\(X\to\widetilde\Sigma_0\mathcal Q\); their inverse rotations
glue by the same boundary identity.

For the linking realization, use the component basis \(V_j\)
and, for \(R>1\), choose \(x,y\) with
\(\lambda(x,y)=1/R\). The explicit mutually inverse coordinates are
\[
 z\longmapsto(\operatorname{num}_R\lambda(z,y),
                  -\operatorname{num}_R\lambda(z,x)),\qquad
 (r,s)\longmapsto rx+sy.
\]
At \(R=1\) use the unique maps of the zero group. The alternating
linking form and \(w_2=0\) meet exactly the oriented realization
conditions of \cite[Lemma F, p.~372; Theorems 2.2--2.3,
pp.~376--377]{manBarden65}. This gives
\(\mathcal Q\to\#^D(S^2\times S^3)\#N_R\) inducing those
coordinates. The parametrized-disc adjustment and product/cap
maps in the cited reconstruction lift it to the suspensions;
the inverse uses the inverse base diffeomorphism on the same disc.

Use its same rotational dumbbell, radial map and inverse to
separate the connected-sum factors. On the separating hypersurface
the maps are \((x,z)\mapsto(\alpha_z^{-1}x,z)\) and identity
on \(S^3\times D^2\); their inverse uses \(\alpha_z\).
Cutting and rejoining the same collars, with the stated transverse
reflection, give the oriented connected sum. This construction
uses one such neck for each of the \(D\) component factors and
uses no neck when \(D=0\).
For each product factor, the trivial-clutch maps of
\cite[Theorem B(2), p.~3; Proposition 5.6, pp.~22--23]{manGR25},
with base \(S^3\) and fibre \(S^2\), give
\((S^2\times S^4)\#(S^3\times S^3)\); inverse clutch maps
and the even-dimensional product swaps preserve the orientation.
These maps prove \eqref{maps:eq:D.OD3}, with \(R=M\).
At \(M=1\), the map \((x,z)\mapsto(\alpha_zx,z)\) on
\(D^5\times S^1\), identity on \(S^4\times D^2\), and radial
corner rounding identify the last factor with the oriented
\(S^6\). The inverse uses the inverse rotation.

"""
    e.replace(old, new, "D12", "maps:src:D.2.31",
              "Give the verified role/parameter correspondence to KQ's sole framed reconstruction, keeping the actual gluing, inverse rotations, linking coordinates, neck maps and D=0/R=1 endpoints instead of re-proving its general construction.")
    e.replace("same statement for a retained zero-Chern\noriginal, with a free component complement, is proved in Section 4.",
              "same statement for a zero-Chern\noriginal, with a free component complement, is proved in part 4.",
              "D04", "maps:src:D.2.31", "Correct the internal locator to the actual fourth proof part and state the cap type directly.")
    e.replace("spheres of Section 4.", "spheres of part 4.", "D04", "maps:src:D.2.31",
              "Correct the second internal component-basis locator; no fixed global section number is introduced.")
    old = interval(e, r"The exact program \path{code/III/manifolds_original_zero_degree.py}", r"\begin{theorem}[all original additive choices on the natural catalogue]")
    new = r"""\begin{remark}[Finite zero-Chern original-cap calculations]
\hypertarget{tag-Q127}{}\label{mapsIII:rem:zero-chern-original-calculations}
{\normalfont\scriptsize tag Q127}\par
The finite calculation covers all $396$ unselected zero-Chern
original-cap lattices and folded intersection ranks, the $228$
additive patterns, and $144$ primitive scalar-circle pairs in
the $b=1$ patterns that can be simply connected. The orbit
coordinates in part 4 specialize to the odd-star component
coordinates of Theorems~\ref{maps:src:D.2.16} and
\ref{maps:src:D.2.17}; the inverse reads
the same labelled orbit coefficients. Every permitted narrow-$P$
section pair is included in the option rule above.
\end{remark}

"""
    e.replace(old, new, "D09", "mapsIII:rem:zero-chern-original-calculations",
              "Retain the exact finite lattice/pattern/scalar-pair scope in a numbered remark, and move the executable path and historical execution attribution to the one program table; remove the orphan scope disclaimer.")
    l8_defs = interval(e, "Let $L$ be the number of such nonzero-Chern original caps,\n", "Let $T$ be the torsion subgroup of the cokernel of the matrix in\nTheorem~\\ref{maps:src:D.2.30}, adding\n")
    e.replace(l8_defs, "", "D13", "maps:src:D.2.32",
              "Move the named component statistic and its permanent equation identity into the preceding numbered input definition.")
    old = interval(e, r"\begin{theorem}[all original additive choices on the natural catalogue]", "At a nonzero-Chern original cap let $s_i$ be the number of\n")
    new = r"""\subsection{All original additive caps and their integral homology}

\begin{definition}[General original additive data]
\hypertarget{tag-Q128}{}\label{mapsIII:def:all-original-additive-data}
{\normalfont\scriptsize tag Q128}\par
Use the $172$ natural initial rows and common marking of
Definition~\ref{mapsIII:def:zero-chern-original-data}. At $I_n^*$
choose the original cap; at every finite good-reduction additive
site choose the original cap or any free logarithmic cap. Use the
marked Mumford models at multiplicative sites and the zero-Chern
original alternatives of Theorem~\ref{maps:src:D.2.31}.
All permitted positive orders, free affine twists, regular
logarithmic sites and integer clutches remain parameters.
For a nonzero-Chern original additive cap, let $s_i$ be its
number of Kodaira components and $q_i^c$ its component-group order.
""" + l8_defs + r"""\end{definition}

\begin{theorem}[All original additive choices on the natural catalogue]
\hypertarget{tag-02L8}{}\label{maps:src:D.2.32}
{\normalfont\scriptsize tag 02L8}\par
The data of Definition~\ref{mapsIII:def:all-original-additive-data}
give exactly $282$ additive-filling patterns on all $172$ initial
rows. Of them, $54$ involve a nonzero component Chern class.
"""
    e.replace(old, new, "D13", "maps:src:D.2.32",
              "Put the full additive choice domain and component statistics in a numbered definition and give the general homology theorem its own actual subsection.")
    e.replace("At a nonzero-Chern original cap let $s_i$ be the number of\nKodaira components, and let $q_i^c$ be its component-group\norder. Its full boundary kernel adds the fibre relation\n",
              "At each nonzero-Chern original additive cap, the full boundary\nkernel adds the fibre relation\n", "D13", "maps:src:D.2.32",
              "Use the component symbols from the preceding numbered definition without redefining them in the conclusion.")
    old = interval(e, r"Use \(\Lambda=\mathbb Z\langle e_1,e_2,\delta,\gamma\rangle\),", "Theorem~\\ref{maps:src:D.2.31} gives the zero-Chern original maps,\n")
    new = r"""Use the marking and area form of
Definition~\ref{mapsIII:def:all-original-additive-data}, and put
\(J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\).
"""
    e.replace(old, new, "D20", "maps:src:D.2.32",
              "Use the one numbered common period, section and area convention before the new nonzero-line calculation.")
    e.replace("To find the complete boundary map, not just this component\nrank, put\n", "For the complete boundary map put\n", "D02", "maps:src:D.2.32",
              "Introduce the complete map directly; its source, target, kernel and section remain fully proved.")
    e.replace("\\mathbb Z k\\ \\oplus\\ \\mathbb Zt(\\delta)\\ \\oplus\\ \\mathbb Zt(\\ell),\n\\]\nIts complete cokernel is", "\\mathbb Z k\\ \\oplus\\ \\mathbb Zt(\\delta)\\ \\oplus\\ \\mathbb Zt(\\ell).\n\\]\nIts complete cokernel is",
              "D23", "maps:src:D.2.32", "End the displayed kernel sentence before its next complete sentence.")
    old = interval(e, "For the untwisted original Engel input $P=G,Q=6G$, the\n", r"The exact program \path{code/III/manifolds_original_chern.py}")
    new = r"""\begin{remark}[Engel and mixed-filling specializations]
\hypertarget{tag-Q129}{}\label{mapsIII:rem:original-additive-specializations}
{\normalfont\scriptsize tag Q129}\par
For the untwisted Engel row $P=G,Q=6G$ with $e=0$ and no
logarithmic sites, the $IV^*$ and $III$ original caps have
$s_i=7,2$ and $h_i=2,3$. Hence $\beta=5$, $L=2$, $T=0$ and
$r=1$, and \eqref{maps:eq:D.OC3} gives
$(1,1,8,14,8,1,1)$. This is the marked Engel row of
Theorem~\ref{maps:src:D.2.20} with its trivial regular logarithm
$(m,v)=(1,0)$: identity on the period lattice and on every original
cap, together with the ordinary-disc identification at that
order-one site, gives the input map and its inverse. That theorem
identifies the named member of \SeriesRef{push:src:A.4.2}.

For a mixed row of Theorem~\ref{maps:src:D.2.21}, write $d_0$
for its height denominator and $q_0$ for its finite monodromy order.
Its parameters here are
\[
 a=1,\quad b=d_0,\quad d_i=q_0,\quad g_i=1,\quad
 m_i=q_0k,\quad n_i=n,\quad r_i=r,\quad e=0,
\]
with no regular logarithmic site and the same original additive cap.
The inverse reads $k=m_i/q_0,n=n_i,r=r_i$. Both constructions
use the fixed vector
$\ell_i=(-d_0z_{G,1},-d_0z_{G,2},0,1)$ and the same section line,
so identity on the marked periods carries their finite Thom,
original-cap and exterior maps to each other. Their five homology
specializations are therefore the formulas of that theorem.
\end{remark}

"""
    e.replace(old, new, "D13", "mapsIII:rem:original-additive-specializations",
              "Replace the orphan recovery claim by a numbered specialization remark with the exact Engel order-one input map and all five mixed-row parameter maps and inverses; preserve the series reference for root's final expansion.")
    old = interval(e, r"The exact program \path{code/III/manifolds_original_chern.py}", r"\begin{theorem}[Original multiplicative fillings]")
    new = r"""\begin{remark}[Finite original additive calculations]
\hypertarget{tag-Q130}{}\label{mapsIII:rem:all-original-additive-calculations}
{\normalfont\scriptsize tag Q130}\par
The finite calculation includes all $46$ primitive Chern vectors,
their logarithm vectors, full area kernels and primitive fibre
images, and the complete $282$-pattern table. For the new patterns,
the unreduced graph, normal and fibre-kernel Smith matrices agree
with the reduced presentation in $74$ comparisons, including
$9$ torsion-cap and $54$ zero-rational-Euler instances.
\end{remark}

"""
    e.replace(old, new, "D09", "mapsIII:rem:all-original-additive-calculations",
              "Retain every finite input, method and result in a numbered remark; move the path to the program table and remove the prompt-request disclaimer.")
    l9_defs = interval(e, "Let $L$ count all nonzero-Chern original fillings, and set\n", "Write the Seifert abelianization of Theorem~\\ref{maps:src:D.2.23}\n")
    e.replace(l9_defs, "", "D13", "maps:src:D.2.33",
              "Relocate the named all-original component statistic to the numbered input definition.")
    old = interval(e, r"\begin{theorem}[Original multiplicative fillings]", "There are $120$ marked zero-free multiplicative positions with\n")
    new = r"""\subsection{Original multiplicative caps and the full natural catalogue}

\begin{definition}[Natural data with original multiplicative choices]
\hypertarget{tag-Q131}{}\label{mapsIII:def:original-multiplicative-data}
{\normalfont\scriptsize tag Q131}\par
At every zero-free multiplicative fibre of the $172$ natural
initial rows, choose the original filling or the marked primitive
Mumford filling. At additive fibres use the original or finite
logarithmic choices of Definition~\ref{mapsIII:def:all-original-additive-data},
with the original filling at each $I_n^*$. Allow every permitted
positive finite or regular order, every free affine lift and
every integer clutch.
""" + l9_defs + r"""\end{definition}

\begin{theorem}[Original multiplicative fillings]
\hypertarget{tag-02L9}{}\label{maps:src:D.2.33}
{\normalfont\scriptsize tag 02L9}\par
Identifying the equal marked boundary kernels at zero-Chern
multiplicative fibres in Definition~\ref{mapsIII:def:original-multiplicative-data}
gives $495$ integral homology presentation patterns.
"""
    e.replace(old, new, "D13", "maps:src:D.2.33",
              "Separate the full choices and component statistics into a numbered definition before the original multiplicative theorem, preserving its count and all parameter scope.")
    old = interval(e, "$\\bar p=-a\\kappa\\bmod\\nu$. For a cached cyclic component\n", "arrows. The line class on the original neighbourhood $N$ is\n")
    new = r"""$\bar p=-a\kappa\bmod\nu$. In the negative Abel--Jacobi
component coordinate of Definition~\ref{mapsIII:def:elliptic-marked-data}
and Theorem~\ref{maps:src:D.2.22}, the section has coordinate
$a\kappa$. The map $j\mapsto-j$, with itself as inverse,
therefore carries that marking to the positive Tate indexing.
It fixes $C_0$, preserves the component cycle and intersection
matrix, and carries both section components and translation
"""
    e.replace(old, new, "D20", "maps:src:D.2.33",
              "Use the actual current negative-cocycle component convention and its already proved self-inverse sign map; remove the unused unspecified cached-coordinate symbol without changing a component or arrow.")
    old = interval(e, "For a positive roof $R(y)$,\n", "Connection transport along the retraction to $K$ now gives\n")
    new = r"""For a positive roof $R(y)$ use the variable-roof map $F_y$
in the proof of Theorem~\ref{maps:src:D.2.31}, part 3, with
$r(y)=R(y)$ and the same forward angular arrow. Its positive
derivative and equal endpoint derivatives give the smooth
identification; $F_y^{-1}$ is its inverse. This map uses the
given circle-bundle point as $y$ and changes only its roof coordinate.
"""
    e.replace(old, new, "D12", "maps:src:D.2.33",
              "Use the earlier explicitly proved positive-roof map on these same bundle points, with the exact roof renaming and inverse; retain the distinct graph-winding and line-lift proof in full.")
    old = interval(e, "At a finite logarithmic site use the bases of\n", "At every original filling set its full fixed sweeps to zero\n")
    new = r"""At each finite and regular logarithmic site, the marked lattice,
power vector, root coordinate and normal orientation are those of
Theorem~\ref{maps:src:D.2.31}, part 6. Identity on these coordinates
and its inverse carry the full cap diagrams to the ones used here.
In particular a finite site has $m_i=d_i k_i>0$,
$v_i=r_i\delta+n_i\ell_i$ and
\[
 \gcd(m_i,r_i,n_i)=1,\qquad d_i\mid m_i/\tau_i,\qquad
 \tau_i=\gcd(m_i,q_{v,i}r_i,g_i n_i).
\]
Its complete Thom columns, in the identical ordered coordinates
$(s,D_i=t_i(\delta),L_i=t_i(\ell_i))$, are
\[
 \begin{pmatrix}b g_i n_i/q_{v,i}\\m_i/q_{v,i}\\0\end{pmatrix},
 \qquad\begin{pmatrix}-br_i\\0\\m_i/g_i\end{pmatrix},
 \qquad\begin{pmatrix}0\\r_i\\n_i\end{pmatrix}.
\]
The boundary root-argument map and its inverse in that proof give
the normal projection $N_{m_i}\lambda$, vertical class
$-\lambda\wedge v_i$, and root sweep $v_i$. Thus the full
normal character of order $\tau_i$ and the core torsion are retained.
The holomorphic finite-sum conjugacy in
Theorem~\ref{maps:src:D.2.29} applies to the same root-disc operator
and power class, with its inverse translation; it covers every
holomorphic affine lift, including the central point.
At a regular site, $m_j>0$, $v_j=(x_j,y_j,z_j,\mu_j)$ and
$\gcd(m_j,x_j,y_j,z_j,\mu_j)=1$. Its complete relations are
\[
 m_jt_j(u)-\omega(u,v_j)s=0,\qquad t_j(v_j)=0.
\]
They use the same normal-sector maps and integral central-lattice
quotient, including $m_j=1$.
"""
    e.replace(old, new, "D12", "maps:src:D.2.33",
              "Identify every unchanged finite/regular diagram literally with the earlier full proof, retaining all freeness data and complete columns while removing its repeated fixed-lattice, root-map and whole-disc conjugacy derivations.")
    old = interval(e, "A finite peripheral lift change is $v_i\\mapsto v_i+N_{m_i}\\lambda_i$.\n", "\\smallskip\n\\emph{Global groups.}\n")
    new = r"""The peripheral-lift maps in Theorem~\ref{maps:src:D.2.31}, part 6,
fix the present original-cap diagrams and act on the unchanged
finite/regular diagrams by
\[
 v_i\mapsto v_i+N_{m_i}\lambda_i,\qquad
 t'_i(u)\mapsto t_i(u)+\omega(u,\lambda_i)s,
 \qquad e\mapsto e+\sum_i\chi(\lambda_i).
\]
Their inverse uses $-\lambda_i$ and subtracts the sweep shear.
The norm-pairing identities proved there preserve every root
column and the global relation; at a regular site $N_m=mI$.
This gives every permitted peripheral marking on the present fillings.

"""
    e.replace(old, new, "D12", "maps:src:D.2.33",
              "Use the single preceding proof of the full norm-map peripheral shear with its exact action on the present diagrams and inverse, preserving all finite and regular marking scope.")
    old = interval(e, "For each profile of generator height $1/d$ and each selected\n", "On a row let $f$ count finite additive sites, let $c$ count\n")
    new = r"""Use the $172$ natural rows of Theorem~\ref{maps:src:D.2.22},
identified by the ordered profile, selected zero, section pair and
all marked component coordinates as in Theorem~\ref{maps:src:D.2.31}.
The identification and its inverse fix those coordinates.

"""
    e.replace(old, new, "D12", "maps:src:D.2.33",
              "Cite the one exhaustive natural-row derivation through the exact identity of ordered inputs; retain the distinct 495-pattern quotient, full table and inverse choice rule.")
    start = r"The exact program \path{code/III/manifolds_original_multiplicative.py}"
    old = e.text[e.text.index(start):]
    new = r"""\begin{remark}[Finite original multiplicative calculations]
\hypertarget{tag-Q132}{}\label{mapsIII:rem:original-multiplicative-calculations}
{\normalfont\scriptsize tag Q132}\par
The finite calculation covers all $120$ integral normal forms,
primitive fibre and monodromy kernels, values of $\omega$, and
primitive Chern and component-multiplicity vectors. The occurrences
are $I_8$ in $6$ cases, $I_7$ in $14$, $I_2$ in $31$, $I_3$ in
$23$, $I_5$ in $38$ and $I_4$ in $8$. The unreduced graph,
normal and fibre matrices agree with the reduced presentation in
$213$ Smith comparisons for the new patterns, including $18$
torsion-cap and $172$ zero-rational-Euler instances. The proof
above gives the full range of orders and free affine parameters.
\end{remark}

"""
    e.replace(old, new, "D09", "mapsIII:rem:original-multiplicative-calculations",
              "Retain every finite input type, exact count, method and result in a numbered remark; put the historical executable path in the program table and remove run credit and prompt-scope narration from the body.")
    for opening, ending, label in [
        (r"\begin{tabular}{llllll}", r"\end{tabular}", "maps:src:D.2.31"),
        (r"\begin{tabular}{lllll}", r"\end{tabular}", "maps:src:D.2.32"),
        (r"\begin{array}{cc|rrrr}", r"\end{array}", "maps:src:D.2.33"),
    ]:
        start = e.text.index(opening)
        stop = e.text.index(ending, start) + len(ending)
        old = e.text[start:stop]
        new = old.replace("& default &", "& base &").replace(r"\mathrm{default}", r"\mathrm{base}")
        if old == new:
            raise ValueError("Expected exact profile-table designation absent")
        e.replace(old, new, "D20", label,
                  "Use Q110's base-profile name in this one wholly read table; the forward designation map default-to-base and its reverse fix every profile, site and numeric entry.")
    e.replace("\\cite[Section 2.4, equation (2.2), p.~6; Proposition 3.5,\npp.~8--10]{manUU21}",
              "\\cite[Section 2.4, equation (2.2), pp.~6--7;\nProposition 3.5(1),(3), pp.~8--10]{manUU21}",
              "D18", "maps:src:D.2.31",
              "Restrict the invariant-leaf citation to the actual used parts and verified primary pages, all read during the KQ unit review.")
    e.replace("\\cite[Sections 7.5--7.7, pp.~33--34]{manSS10}",
              "\\cite[Sections 7.6--7.7, pp.~33--34]{manSS10}",
              "D18", "maps:src:D.2.31",
              "Cite the exact primary sections on translation and torsion quotients read in the KQ pass.")
    issues = e.presentation()
    if issues:
        raise ValueError(issues)
    e.finish(labels=("mapsIII:def:zero-chern-original-data", "mapsIII:rem:zero-chern-original-calculations", "mapsIII:def:all-original-additive-data", "mapsIII:rem:original-additive-specializations", "mapsIII:rem:all-original-additive-calculations", "mapsIII:def:original-multiplicative-data", "mapsIII:rem:original-multiplicative-calculations"),
             tags=("Q126", "Q127", "Q128", "Q129", "Q130", "Q131", "Q132"))


if __name__ == "__main__":
    main()
