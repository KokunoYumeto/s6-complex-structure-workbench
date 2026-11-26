"""Publication pass for the wholly read all-parity integral theorem."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def interval(e, start, end):
    if e.text.count(start) != 1 or e.text.count(end) != 1:
        raise ValueError(("Stale or ambiguous read interval", start, end))
    a, b = e.text.index(start), e.text.index(end)
    if a >= b:
        raise ValueError("Reversed interval")
    return e.text[a:b]


def main():
    e = Editor("weighted_integral_homology", "C8-FND-INTEGRAL-WEIGHTS-")
    owner = "maps:src:D.2.41"
    old = interval(e, r"\begin{theorem}[Integral homology at every positive weight]", "For $u,v\\in\\Lambda=\\mathbb Z^4$ set\n")
    new = r"""\subsection{Integral bar coordinates at every positive weight}

\begin{definition}[All-weight data and integral cochains]
\hypertarget{tag-Q140}{}\label{mapsIII:def:all-weight-integral-data}
{\normalfont\scriptsize tag Q140}\par
Choose a natural initial row of Theorem~\ref{maps:src:D.2.22},
with $P=aG$, $Q=bG$, $a,b>0$ and $\gcd(a,b)=1$, and choose
any positive integer $d$. Use its $d$th translation iterate,
norm linearization, original chart units and period subgroup.
Take either cap set $\mathcal P$ or
$\mathcal P_{\mathrm{all\ star\ O}}$ of
Definition~\ref{mapsIII:def:weighted-natural-data}, every free
finite-good affine logarithm, every finite list of free regular
logarithms and every integer clutch $e$. Keep the same formulas
for the component counts $L$ and $\beta$ as in
Definition~\ref{mapsIII:def:odd-weighted-data}, evaluated at this $d$.

Use the ordered periods
$\Lambda=\mathbb Z\langle e_1,e_2,\delta,\gamma\rangle$
of Definition~\ref{mapsIII:def:elliptic-marked-data}, with
$e_3=\delta$ and $e_4=\gamma$. Index the boundary matrices,
including added regular and auxiliary clutch sites, by
$A_0,\ldots,A_r$. These denote the weighted matrices
$A_i(d)=S_d^{-1}A_i(1)S_d$, where
$S_d=\operatorname{diag}(1,1,1,d)$ and $A_0\cdots A_r=I$.
Place an unfilled site last, and take the first $r$ base loops
as independent generators. The based insertions $J_i$ use
these same stems and the final inverse word.

For $u,v\in\Lambda$ set
"""
    e.replace(old, new, "D13", owner,
              "Create a real subsection and numbered all-positive-weight input/cochain definition, with all original units, cap choices, free affine/regular data and clutches. Fix the four basis names, last-site ordering and weighted matrix convention before every formula; no oddness condition is imported.")
    e.replace("The bilinear map $D_A$ is symmetric. Define its\nintegral quadratic primitive by\n", "Define the integer-valued quadratic map\n", "D13", owner,
              "Move the cochain formula into its numbered definition while leaving symmetry and the primitive identity as proved theorem conclusions.")
    old = "The transported reversed word in the second line\nis part of the formula.\n\nKeep every fibre relation"
    new = r"""The transported reversed word in the second line uses the
displayed order, including the final factor $A_r$.
For commuting based loops $x,y$ in the graph exterior, write
$\mathsf T(x,y)$ for the image of the positively oriented fundamental
class of $T^2$ under the map induced by
$(1,0)\mapsto x$, $(0,1)\mapsto y$ on fundamental groups.
The ordered pair fixes its orientation.
\end{definition}

\begin{theorem}[Integral homology at every positive weight]
\hypertarget{tag-02LI}{}\label{maps:src:D.2.41}
{\normalfont\scriptsize tag 02LI}\par
For every datum in Definition~\ref{mapsIII:def:all-weight-integral-data},
the following integral presentation computes the full homology.
Across the $172$ natural rows, the broad cap set has $495$
patterns and the all-star-original subset has $459$. Their
inclusion $j$ and the map $\pi$ replacing finite-good
$\mathrm{III}^*,\mathrm{IV}^*$ caps by their originals satisfy
$\pi j=1$; $j\pi$ performs precisely those replacements.

The map $D_A$ is symmetric, and $f_A$ is its integral quadratic
primitive in \eqref{maps:eq:D.BC8}. Keep every fibre relation"""
    e.replace(old, new, "D13", owner,
              "Close the numbered cochain definition and give the theorem its original permanent identity and proved assertions. Define the oriented torus notation by its actual induced T2 map, preserve the complete final suffix, and retain the two distinct pattern sets and their exact composites.")
    old = "Then the complete integral homology is \\eqref{maps:eq:D.WP9}\nwith this $T$, for every $d>0$, including all\nshared even factors.\n"
    new = r"""Enumerate the logarithmic sites other than the auxiliary clutch
in base order as $(m_j,v_j)$, $1\leq j\leq k$, and put
$\mu_j=\gamma^*(v_j)$. The full fundamental group is
\[
 \pi_1(X)=\left\langle\gamma,\zeta_1,\ldots,\zeta_k\ \middle|\
 [\gamma,\zeta_j]=1,\quad
 \zeta_j^{m_j}=\gamma^{\mu_j},\quad
 \zeta_1\cdots\zeta_k=\gamma^e\right\rangle .
\]
Write its abelianization as $\mathbb Z^{r_1}\oplus A_1$.
The free ranks and complete integral homology are
\eqref{maps:eq:D.WP8} and~\eqref{maps:eq:D.WP9}, using $r=r_1$
and the full torsion group $T$ just defined. These conclusions
hold for every $d>0$, including all shared even factors.
"""
    e.replace(old, new, "D18", owner,
              "Replace the inaccurate equation-only locator for the Seifert group by its exact full presentation, and explicitly substitute the H1 rank r1 into WP8/WP9. The base-loop count r, cochain corrections c_i and new names for the same root generators stay separate; no theorem scope changes.")
    old = "The line map is the product of the original line maps on these\nsheets, and its positive roof is the sum of their positive roofs.\nDivision by that roof and multiplication by it give the inverse\nperiod parametrizations. Thus the graph and peripheral maps carry\nthe same line units and the origin sections.\n"
    new = r"""The line map is the product of the original line maps on these
sheets, and its positive roof $r_d(x)$ is the sum of their
positive roofs. Use the smooth roof coordinate $f_x$ in the
zero-Chern cap part of the proof of Theorem~\ref{maps:src:D.2.40}:
the input map fixes $x$, $r_d$, the collar and its line units,
and sends $(x,t)$ to $(x,f_x(t))$. Its inverse is
$(x,s)\mapsto(x,f_x^{-1}(s))$. The identical endpoint slopes
proved there give the mapping-torus coordinates. Thus the graph
and peripheral maps carry the same line units and origin sections.
"""
    e.replace(old, new, "D20", owner,
              "Use the already proved smooth positive-roof map with its exact input identification and inverse, retaining all line norms and endpoint units. This supplies the explicit geometric graph coordinate without adding an unproved smoothness claim to simple roof division.")
    e.replace("relation in the normal-line case, as in\n\\ref{maps:src:D.2.29}--\\ref{maps:src:D.2.30}.\n", "relation in the normal-line case, as in\nTheorems~\\ref{maps:src:D.2.29} and~\\ref{maps:src:D.2.30}.\n", "D04", owner,
              "Name both verified finite-cap theorem owners at the full Thom-source reference.")
    e.replace(r"              [\lambda,\mu]=[\lambda,t_i^m]-[\lambda,v].",
              r"              \mathsf T(\lambda,\mu)=\mathsf T(\lambda,t_i^m)-\mathsf T(\lambda,v).",
              "D20", owner,
              "Use the numbered definition's oriented torus-class notation in BC15. It denotes the same induced T2 fundamental class with the same ordered loops and orientation; the identity on that class is the inverse renaming.")
    e.replace(r"The root pair gives $[t_i,\mu]=[v,t_i]$, and hence the fifth",
              r"The root pair gives $\mathsf T(t_i,\mu)=\mathsf T(v,t_i)$, and hence the fifth",
              "D20", owner,
              "Carry the same exact torus-class identity renaming to the root normal; its determinant-one basis change and Thom sign are unchanged.")
    old = "Telescoping gives $(I-R)y_0=b_0$; the inverse adds $y_0$.\nThe finite sum carries the original translation and line units.\n"
    new = r"""The finite-operator identity in the proof of
Theorem~\ref{maps:src:D.2.29} gives $(I-R)y_0=b_0$.
Its input identification fixes $R,m,b_0$ and the root coordinate,
with the same tuple as inverse. The coordinate map subtracts
$y_0$ and its inverse adds $y_0$; the finite sum carries the
original translation and line units.
"""
    e.replace(old, new, "D12", owner,
              "Give the repeated abstract finite-operator proof its L4 owner by the exact R,m,b0 and root-coordinate map; preserve the actual affine map, inverse, norm law and units.")
    e.replace("Deleting its root $c_*=\\gamma^{-e}$ gives the asserted product\n", "Deleting its root $\\zeta_*=\\gamma^{-e}$ gives the asserted product\n", "D20", owner,
              "Use the identity renaming of root generators to zeta, leaving the scalar cochain corrections c_i and every clutch power unchanged.")
    old = "The local component, line and plumbing maps of\n\\ref{maps:src:D.2.40} identify the cap $H_2$ groups as free\nabelian groups at every positive weight. These local maps retain\nthe $d$th component permutation and the full norm of the line\nunits. Their fibre-kernel transport can be proved integrally as\nfollows. Put $W_d=\\Lambda^2S_d$ and let\n"
    new = r"""Use the geometric local maps in the proof of
Theorem~\ref{maps:src:D.2.40}: the period cover and transfer,
the cusp normalization, the zero-Chern and rank-one component
maps, and the nonzero-Chern line flow and Gysin sections.
Their input identification fixes the natural row, positive $d$,
fan, node units, powered component permutation and line norm;
reading the same tuple is its inverse. These displayed local
maps are defined for every positive $d$, and their component
and Gysin bases give free cap $H_2$ at every such weight.
The bounding geometric normal families in that proof are
evaluated here by $P_2$ below. Put $W_d=\Lambda^2S_d$ and let
"""
    e.replace(old, new, "D14", owner,
              "State the exact all-positive local hypotheses used from LH and identify every geometric input, excluding any dependence on its odd-half global marking. Retain the explicit local transfer, saturation and normal evaluation in the LI proof.")
    e.replace("The actual logarithmic root paths then give the Seifert presentation\nin \\eqref{maps:eq:D.WP8}: their powers are\n$c_i^{m_i}=\\gamma^{\\mu_i}$ and their product is $\\gamma^e$.\n", "The actual logarithmic root paths give the Seifert presentation\nin the statement: their powers are\n$\\zeta_i^{m_i}=\\gamma^{\\mu_i}$ and their product is $\\gamma^e$.\n", "D18", owner,
              "Point to the actual displayed Seifert group, not the Betti-number equation WP8, and carry the same root-generator identity renaming into its inverse path proof.")
    e.replace("of the component contributions in \\eqref{maps:eq:D.WP9}.\n", "of the component contributions in\nDefinition~\\ref{mapsIII:def:all-weight-integral-data}.\n", "D18", owner,
              "Locate the component-count definition itself rather than the integral homology table; all actual weighted orbit contributions are unchanged.")
    old = "All operations use integer polynomial identities, integer kernels,\nthe finite period sum of length $h$, and Smith or Hermite\ndecompositions of the full stated matrices. They apply to every\npositive $d$, every permitted affine power, every finite list of\nregular logarithms and every integer clutch on the natural rows.\n\\end{proof}\n\n\n"
    new = r"""\end{proof}

\begin{remark}[Integral computation and the odd-factor comparison]
\hypertarget{tag-Q141}{}\label{mapsIII:rem:all-weight-integral-calculation}
{\normalfont\scriptsize tag Q141}\par
The computation records the full quadratic coefficient vectors
of \eqref{maps:eq:D.BC2}, the ordered suffixes of
\eqref{maps:eq:D.BC3}, every fibre relation and all five normal
columns. Its operations are integer polynomial identities,
saturated integer kernels, the period sum of length $h$, and
Smith or Hermite decompositions of the full matrices. The
result is the complete Seifert abelianization and integral
homology for every positive $d$, every permitted affine power,
every finite regular-logarithm list and every integer clutch.

The odd-factor comparison uses the map
$(c,k)\mapsto(c-h(k)/2,k)$ and its addition inverse constructed
in the proof. It identifies the fibre, fixed-normal and full
norm columns with their involution coordinates in
Theorem~\ref{maps:src:D.2.40}. At every weight the integer
matrix of the present theorem retains all finite factors.
\end{remark}

"""
    e.replace(old, new, "D13", owner,
              "Give the original executable's mathematical inputs, coefficient-recording method and output scope a numbered remark, without file bookkeeping or an execution claim. Retain the proved exact odd-coordinate morphism and its inverse rather than infer equivalence from deleted central entries.")
    issues = e.presentation()
    if issues:
        raise ValueError(("Unresolved literal equation references", issues))
    e.finish(labels=("mapsIII:def:all-weight-integral-data", "mapsIII:rem:all-weight-integral-calculation"),
             tags=("Q140", "Q141"))


if __name__ == "__main__":
    main()
