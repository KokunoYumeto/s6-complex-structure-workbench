"""Publication restructuring of the wholly read positive-weight Engel unit."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def interval(e, start, end):
    if e.text.count(start) != 1 or e.text.count(end) != 1:
        raise ValueError(("Stale or ambiguous read interval", start, end))
    a, b = e.text.index(start), e.text.index(end)
    if a >= b:
        raise ValueError("Reversed interval")
    return e.text[a:b]


def main():
    e = Editor("positive_engel_weights", "C8-FND-POSITIVE-ENGEL-")
    old = interval(e, r"\begin{theorem}[Every positive Engel weight]", "The exact degree-two matrix has target $(s,t,t_0',t_1')$.\n")
    new = r"""\subsection{All positive weights of the Engel construction}

\begin{definition}[Positive-weight Engel data]
\hypertarget{tag-Q133}{}\label{mapsIII:def:positive-engel-data}
{\normalfont\scriptsize tag Q133}\par
On the $IV^*,III,I_1$ rational elliptic surface of
Theorem~\ref{maps:src:D.2.5}, let $G$ generate the
Mordell--Weil group. Use $M_S=\mathcal O(G-O)$, translation
$6dG$ and linearization zero $dI_1$, where $d$ is a positive
integer. At $I_1$ use the period subgroup
$\mathbb Ze_1+d\mathbb Ze_2$ of the infinite marked hexagonal
toric model. Number the $IV^*$ and $III$ sites by $0$ and $1$.
At either site choose its original cap or a finite logarithmic
action with parameters
\[
 m_0=3k,\qquad m_1=4\ell,\qquad k,\ell>0,\qquad
 v_i=r_i\delta+n_i u_i,\quad r_i,n_i\in\mathbb Z,
\]
where, in the marked period basis $(\delta,a,b,\gamma)$ of that theorem,
\[
 u_0=\gamma+2d(a+b),\qquad u_1=\gamma+3d(a+b).
\]
At an original site put $(\overline m_i,\overline n_i)=(1,0)$;
at a logarithmic site put $(\overline m_i,\overline n_i)=(m_i,n_i)$.
Define
\[
 P=\overline m_1\overline n_0+
   \overline m_0\overline n_1,\qquad
 R=\begin{pmatrix}
  -\overline n_0&\overline m_0\\
  -\overline n_1&-\overline m_1
 \end{pmatrix},\qquad
 \mathbb Z^r\oplus A_1=\operatorname{coker}R.
 \tag{D.WE2}\hypertarget{tag-026U}{}\label{maps:eq:D.WE2}
\]
\end{definition}

\begin{theorem}[Every positive Engel weight]
\hypertarget{tag-02LA}{}\label{maps:src:D.2.34}
{\normalfont\scriptsize tag 02LA}\par
The data of Definition~\ref{mapsIII:def:positive-engel-data}
give a smooth $d$-period hexagonal cap for every $d>0$.
The exact freeness conditions at the chosen finite sites are
\[
\begin{aligned}
 t_0&=\gcd(m_0,n_0,3r_0),&
 &\gcd(m_0,n_0,r_0)=1,\quad 3\mid m_0/t_0,\\
 t_1&=\gcd(m_1,n_1,2r_1),&
 &\gcd(m_1,n_1,r_1)=1,\quad 4\mid m_1/t_1 .
\end{aligned}                                             \tag{D.WE1}\hypertarget{tag-026O}{}\label{maps:eq:D.WE1}
\]
All noninvariant parts of affine translations are included
through the marked translation conjugacy. For every free choice,
the full fundamental group is $\mathbb Z^r\oplus A_1$ of
\eqref{maps:eq:D.WE2}, and $r=1$ precisely when $P=0$.

"""
    e.replace(old, new, "D13", "maps:src:D.2.34",
              "Create one actual subsection and a numbered definition of all marked weighted inputs, effective parameters and the presentation matrix R; retain exact finite freeness as the theorem conclusion and preserve WE1/WE2 identities and every parameter domain.")
    e.replace("In particular $\\chi(X)=2d$ for every choice.\n",
              "In particular $\\chi(X)=2d$ for every choice. At $d=1$ the\nconstruction is the natural row with section multipliers $(1,6)$;\nat $d>1$ its Euler characteristic is greater than two.\n",
              "D14", "maps:src:D.2.34",
              "Retain the admitted natural-catalogue endpoint explicitly in the theorem after relocating the inputs; the proof still supplies its identity covering maps and exact Euler obstruction.")
    e.replace("In positive root coordinates the boundary map is\n",
              "Use the positive-root generator of\nTheorem~\\ref{maps:src:D.2.29}, with\n$(y,\\tau)\\sim(A_i y,\\tau+1)$. In these coordinates the boundary map is\n",
              "D20", "maps:src:D.2.34",
              "Name the precise positive-root mapping-cylinder convention imported from L4 before its boundary chart; preserve all displayed norm, area and normal-orientation signs.")
    old = interval(e, "For the full affine scope, let $\\mathcal R$ be the linear\n", "\\smallskip\n\\emph{The original additive fillings.}\n")
    new = r"""The whole-root-disc translation conjugacy of
Theorem~\ref{maps:src:D.2.29} applies with lattice $\Lambda$,
matrix $A_i(d)$, order $m_i$ and power vector $v_i$ as displayed
here. Identity on these marked data and its inverse identify
the affine equations and the positive root coordinate.
In its Lie-bundle notation, the difference $b_0$ of two lifts
with aligned integral powers has zero norm, and the conjugating
translation is
\[
 h=-m_i^{-1}\sum_{j=0}^{m_i-1}j\mathcal R^j b_0,
                 \qquad (I-\mathcal R)h=b_0.
\]
Its inverse is translation by $-h$ over the entire disc.
A period change $\lambda$ changes the power by $N_{m_i}\lambda$,
with inverse subtraction. Thus these maps include every
noninvariant affine part and integral lift.

"""
    e.replace(old, new, "D12", "maps:src:D.2.34",
              "Use L4 as the single owner of the full holomorphic affine-conjugacy proof through the exact matrix/order/power/root-coordinate substitution; retain the actual finite-sum map, inverse and norm lift law.")
    old = interval(e, "For two logarithmic caps, a simply connected member\n", r"The executable \path{code/III/manifolds_weighted_engel.py}")
    new = r"""\begin{remark}[Simply connected and original-cap specializations]
\hypertarget{tag-Q134}{}\label{mapsIII:rem:positive-engel-specializations}
{\normalfont\scriptsize tag Q134}\par
For two logarithmic caps, a simply connected member has $P=\pm1$.
The two-by-two presentation has a unit determinant, so each
$\gcd(m_i,n_i)$ and $\gcd(m_0,m_1)$ divides one. Hence $g=1$, and
\[
 H_2=\mathbb Z^{d-1}\oplus\mathbb Z/d,\qquad
 H_3=\mathbb Z/d,\qquad H_4=\mathbb Z^{d-1}.
 \tag{D.WE14}\hypertarget{tag-026T}{}\label{maps:eq:D.WE14}
\]
These formulas include even and three-divisible $d$.
At the minimal orders $m_0=3,m_1=4$ and $\gcd(d,6)=1$,
the homology-coordinate comparison with
Theorem~\ref{maps:src:D.1.4} is
\[
 (z_1,\ldots,z_{d-1};[u]_d)
       \longmapsto(z_1,\ldots,z_{d-1};[u]_d)
\]
in the free and Smith coordinates of their respective proofs.
Its inverse is the same coordinate assignment. In degree three
use the corresponding cyclic linking coordinate, and in degree
four use the dual free coordinates; the orientation generators
agree in degrees zero and six.

With both original caps, \eqref{maps:eq:D.WE6} gives
\[
 \pi_1=\mathbb Z,\qquad
 H_2=\mathbb Z^{d+7}\oplus\mathbb Z/d,\qquad
 H_3=\mathbb Z^{14}\oplus\mathbb Z/d,\qquad
 H_4=\mathbb Z^{d+7},\quad H_5=\mathbb Z.
\]
At $d=1$, the identity suspension/toric maps and unchanged
original caps identify this datum with
Remark~\ref{mapsIII:rem:original-additive-specializations};
their inverse is identity in the same marked charts. At every
positive $d$ the construction uses the stated iterated translation.
\end{remark}

"""
    e.replace(old, new, "D13", "maps:src:D.2.34",
              "Give the orphan group specializations a numbered remark, retain WE14 and both-original groups, replace vague D.1 references by the explicit abstract homology-coordinate map and inverse, and cite Q129 for the already identified d=1 original Engel member. No new geometric or smooth identification is asserted by the group-coordinate comparison.")
    old = e.text[e.text.index(r"The executable \path{code/III/manifolds_weighted_engel.py}"):]
    new = r"""\begin{remark}[Integral weighted Engel calculations]
\hypertarget{tag-Q135}{}\label{mapsIII:rem:positive-engel-calculations}
{\normalfont\scriptsize tag Q135}\par
The integral computation takes integer parameters, tests
\eqref{maps:eq:D.WE1}, and returns the full group and homology
presentations. Polynomial identities verify the monodromies,
primitive exterior-square quotient and graph basis. The unreduced
graph and full area kernels are compared with
\eqref{maps:eq:D.WE3}--\eqref{maps:eq:D.WE4}. The finite outputs
include nonprimitive free twists, nontrivial cap torsion,
every original/logarithmic choice and zero-Euler cases.
\end{remark}

"""
    e.replace(old, new, "D09", "maps:src:D.2.34",
              "Move executable bookkeeping to the single program table while retaining every computational input, polynomial method, full-presentation output and endpoint class in a numbered remark; no historical execution claim is added.")
    issues = e.presentation()
    if issues:
        raise ValueError(issues)
    e.finish(labels=("mapsIII:def:positive-engel-data", "mapsIII:rem:positive-engel-specializations", "mapsIII:rem:positive-engel-calculations"),
             tags=("Q133", "Q134", "Q135"))


if __name__ == "__main__":
    main()
