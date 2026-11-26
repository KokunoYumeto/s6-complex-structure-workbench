"""Exact publication edits after the complete LH original/receiver reading."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def interval(e, start, end):
    if e.text.count(start) != 1 or e.text.count(end) != 1:
        raise ValueError(("Stale or ambiguous read interval", start, end))
    a, b = e.text.index(start), e.text.index(end)
    if a >= b:
        raise ValueError("Reversed interval")
    return e.text[a:b]


def main():
    e = Editor("weighted_odd_cap_kernels", "C8-FND-ODD-WEIGHTED-")
    owner = "maps:src:D.2.40"
    old = interval(e, r"\begin{theorem}[Shared odd factors in weighted profiles]", "The full relation matrix has target")
    new = r"""\subsection{Shared odd factors and saturated cap kernels}

\begin{definition}[Weighted data with odd common factor]
\hypertarget{tag-Q138}{}\label{mapsIII:def:odd-weighted-data}
{\normalfont\scriptsize tag Q138}\par
Choose one of the $172$ natural marked rows of
Theorem~\ref{maps:src:D.2.22}, with $P=aG$, $Q=bG$,
$a,b>0$ and $\gcd(a,b)=1$. Take the $d$th positive iterate
of its contracting line map, with
\[
                         g=\gcd(a,d)\text{ odd}.
 \tag{D.OW1}\hypertarget{tag-022W}{}\label{maps:eq:D.OW1}
\]
Use the norm linearization, original chart units and period
subgroup of that iterate. Let $\mathcal P$ and
$\mathcal P_{\mathrm{all\ star\ O}}$ be the two sets of ordered
cap choices defined in Definition~\ref{mapsIII:def:weighted-natural-data}:
the latter keeps every starred cap original, while the former
also permits finite-good $\mathrm{III}^*,\mathrm{IV}^*$ fillings.
Odd $I_\nu^*$ caps remain original in both sets. Retain every
permitted original or marked Mumford choice, every free finite
logarithm, every finite list of free regular logarithms, and
every integer clutch $e$.

In the periods of Definition~\ref{mapsIII:def:elliptic-marked-data}, put
\[
 \Lambda=\mathbb Z\langle e_1,e_2,\delta,\gamma\rangle,
 \qquad S_d=\operatorname{diag}(1,1,1,d),
 \qquad A_i(d)=S_d^{-1}A_iS_d.
\]
Include the added regular sites in the ordered list of $N$ sites
and represent clutch $e$ by an auxiliary order-one regular site
with power $-e\gamma$. Omit an unfilled site, such as the
selected cusp, from the bouquet. Write
\[
 K=\ker\bigl([A_i(d)-I]_{i<N-1}:\Lambda^{N-1}\longrightarrow\Lambda\bigr).
\]
For $F_i=\ker(A_i(d)-I)$, let $J_i:F_i\longrightarrow K$ be
the based peripheral insertion with the fixed stems; its block
and inverse-word coordinates are given in the proof.

Let $L$ count nonzero-Chern originals. Let $\beta$ be the sum,
away from the selected cusp, of $\gcd(d,\nu_i)-1$ at a narrow
zero-free rank-one site, zero at a non-narrow Mumford site,
$\rho_i(d)-1$ at a zero-Chern additive original, and $s_i-2$
or $\nu_i-2$ at a nonzero-Chern additive or multiplicative
original. Here $s_i$ is the number of Kodaira components,
$\nu_i$ is the multiplicative index, and $\rho_i(d)$ is the
number of orbits of the actual $d$th component permutation.
\end{definition}

\begin{theorem}[Shared odd factors in weighted profiles]
\hypertarget{tag-02LH}{}\label{maps:src:D.2.40}
{\normalfont\scriptsize tag 02LH}\par
For the data of Definition~\ref{mapsIII:def:odd-weighted-data},
the following integral algorithm applies to both cap sets.
They contain $495$ and $459$ patterns, respectively. Inclusion
fixes every labelled choice; retraction replaces each
finite-good $\mathrm{III}^*$ or $\mathrm{IV}^*$ filling by its
original cap. Their composite on the smaller set is the identity.
In particular, the algorithm applies to every positive iterate
of every row with odd $a$.

"""
    e.replace(old, new, "D13", owner,
              "Create a real subsection and numbered complete odd-weight input definition. Keep the 495/459 counts as theorem conclusions, preserve OW1, state all positive/signed parameters, ordered cap sets and the full fixed-domain peripheral maps, and define every component-count symbol before use.")
    old = interval(e, "Let \\(L\\) count nonzero-Chern originals. Define \\(\\beta\\) by summing\n", "The free ranks are\n")
    e.replace(old, "Use $L$ and $\\beta$ from\nDefinition~\\ref{mapsIII:def:odd-weighted-data}.\nThe selected cusp has $d$ components.\n", "D12", owner,
              "Give the weighted component counts one numbered owner while retaining every contribution and the separately proved d-component cusp.")
    old = "Write \\(B_i,g_i\\) for the defining elliptic matrix and section\ncocycle of \\ref{maps:src:D.2.23}. Put\n"
    new = "Write $B_i,g_i$ for the ordered elliptic matrix and section\ncocycle in Definition~\\ref{mapsIII:def:elliptic-marked-data}. Put\n"
    e.replace(old, new, "D06", owner,
              "Use Q110's preceding ordered input table rather than locate raw data inside the later construction proof; every matrix and cocycle is unchanged.")
    old = "The identity follows by telescoping. Translation by \\(y_0\\)\nand its negative are the holomorphic conjugacy and\ninverse. The line gauges and root collars retain\ntheir nonzero units.\n"
    new = r"""This is the finite-operator identity in the proof of
Theorem~\ref{maps:src:D.2.29}, with the same operator $R$, order
$m$, norm-zero holomorphic term $b_0$ and root coordinate.
The identification fixes every term of the finite sum and has
itself as inverse. Translation by $y_0$ and by $-y_0$ gives the
holomorphic conjugacy and its inverse. The line gauges and root
collars retain their nonzero units.
"""
    e.replace(old, new, "D12", owner,
              "Assign the common finite-operator conjugacy proof to L4 through the exact operator, order, holomorphic term and root-coordinate map. Retain its displayed formula, identity, inverse and weighted affine data.")
    old = "The boundary map and its inverse are\n"
    new = r"""Use the positive-root convention of
Theorem~\ref{maps:src:D.2.29}, with boundary identification
$(y,\tau)\sim(Ay,\tau+1)$ for this same $A,m,v$.
The boundary map and its inverse are
"""
    e.replace(old, new, "D20", owner,
              "Identify the actual positive-root finite-cap convention with L4's same mapping cylinder before the signed normal formula. The original family's different chart convention is not silently imported.")
    old = "Subtracting columns and then rows reduces it to a unit and two\ncopies of \\(t-1\\). Equal coefficients give the kernel of \\(t-1\\);\nfor a zero-sum vector its successive partial sums give an inverse\npreimage. The remaining vertex and dual-torus cells give\n"
    new = r"""Identify this coefficient ring with $\mathcal A_d$ in
Theorem~\ref{maps:src:D.2.34} by $[p(t)]\mapsto[p(t)]$.
Send every ordered component, branch and dual-torus cell with
coefficient $t^j$ to the identically indexed cell with that
coefficient. The displayed matrix, the degree-zero dual-torus
complex and the degree-four group-ring row agree under this
chain map; the inverse reads the same coordinates. The unit
and $t-1$ reductions, their partial-sum inverse and the free
extension section proved there therefore give
"""
    e.replace(old, new, "D12", owner,
              "Give the common cyclic-cusp normalization reduction its earlier LA owner by the explicit identity of coefficient rings and every ordered chain-cell basis. All distinct cusp period, torsion, normal-disc and transfer calculations remain.")
    e.replace(" H_j(U_d)=\n (\\mathbb Z,\\mathbb Z^2,\\mathbb Z^{d+3},", " H_*(U_d)=\n (\\mathbb Z,\\mathbb Z^2,\\mathbb Z^{d+3},", "D20", owner,
              "Use H_* for the ordered list of all homology degrees; the seven groups and their order are unchanged.")
    e.replace("The fibre quotient in the cusp fibre quotient and section injects into \\(H_2(U_d)\\).", "The fibre quotient with coordinates $Q$ and section $\\sigma$\ninjects into $H_2(U_d)$.", "D02", owner,
              "Name the exact displayed quotient and section instead of the repeated assembly phrase; the preceding integral-kernel proof and injection are unchanged.")
    e.replace("Together with the four fibre\nclasses in the cusp fibre quotient and section, they give a free integral basis of\n", "Together with the four fibre\nclasses specified by $Q$ and $\\sigma$, they give a free integral basis of\n", "D02", owner,
              "Locate the four actual fibre basis vectors by their displayed inverse-coordinate maps.")
    old = interval(e, "Profile & All star caps original & Broad finite-good scope", "Total & 459 & 495")
    new = old.replace("/default", "/base")
    e.replace(old, new, "D20", owner,
              "Apply the already established default-to-base profile-name bijection to this exact table; its inverse restores the former name. Every ordered row, cap choice and numerical entry is fixed.")
    e.replace("Take the natural OS43/default row\n", "Take the natural OS43/base row\n", "D20", owner,
              "Carry the same explicit profile-name bijection into the order-two example, preserving the exact selected site and all integer data.")
    old = e.text[e.text.index("The exact implementation computes the saturated\n"):]
    new = r"""\begin{remark}[Integral comparisons and finite calculations]
\hypertarget{tag-Q139}{}\label{mapsIII:rem:odd-weighted-calculations}
{\normalfont\scriptsize tag Q139}\par
Compute each saturated preimage in \eqref{maps:eq:D.OW4} before
forming the full Smith quotient. All nonunit return factors and
the complete graph coordinates remain in that presentation.
For $g=1$, its comparison with Theorem~\ref{maps:src:D.2.37}
is induced by
\[
 (\eta,k)\longmapsto(\omega_d(\eta),k),\qquad
 (n,k)\longmapsto
 \bigl(n(u e_{12}-v\delta\gamma),k\bigr),\quad ua+vdb=1.
\]
The second map is the inverse modulo the return columns, by
the explicit fibre quotient proved above. Each logarithmic
column maps to $(-\omega_d(\lambda,v_i),J_iN_{m_i}\lambda)$,
and every fixed-normal column keeps its graph coordinate.
The nonzero-Chern fibre generator has value $-db/q_i$ or
$-db/\nu_i$; multiplying that source generator by $-1$ gives
the positive generator used there, with the same sign change
as inverse. These maps commute with every boundary column.

The finite calculations use the permitted odd-common-factor
weights among $1,2,3,5,7,9,15,21,25,35,45,105,315,1001$.
They include $2334$ exterior presentations, $12249$ saturated
local kernels, $1386$ projected finite lattices and $33264$
finite-action candidates with all their proper powers.
The $6326$ complete global matrices include $4950$ matrices
on the two Euler values and $1376$ matrices with two additional
full-vector regular logarithms. The full written argument
establishes every allowed positive weight and all finite,
regular and clutch parameters in \eqref{maps:eq:D.OW1}.

Theorem~\ref{maps:src:D.2.41} supplies the integral algorithm
for every positive weight. The inclusion of the present input
set fixes the natural row, weight, ordered cap choices, every
logarithmic pair $(m_i,v_i)$ and the clutch; its inverse on
that subset reads the same tuple.
\end{remark}

"""
    e.replace(old, new, "D13", owner,
              "Replace orphan implementation/certificate prose by a numbered remark preserving saturated-kernel computation and full-torsion comparison. Supply the exact g=1 quotient/section and Chern-generator sign map, retain the admitted finite input/output scope, and identify the full tuple inclusion into LI. Historical/current paths belong in the one program table; no new execution is claimed.")
    replacements = [
        ("from\n\\ref{maps:src:D.2.32}--\\ref{maps:src:D.2.33}.", "from\nTheorems~\\ref{maps:src:D.2.32} and~\\ref{maps:src:D.2.33}."),
        ("The maximal-minor calculations of \\ref{maps:src:D.2.37} give", "The maximal-minor calculations in Theorem~\\ref{maps:src:D.2.37} give"),
        ("Use the real-period map and its inverse from\n\\ref{maps:src:D.2.26} and \\ref{maps:src:D.2.31}.", "Use the real-period map and its inverse from\nTheorems~\\ref{maps:src:D.2.26} and~\\ref{maps:src:D.2.31}."),
        ("For the weight-one marked graph of \\ref{maps:src:D.2.31},", "For the weight-one marked graph of Theorem~\\ref{maps:src:D.2.31},"),
        ("by the exterior construction of \\ref{maps:src:D.2.31} and \\ref{maps:src:D.2.37},", "by the exterior construction of Theorems~\\ref{maps:src:D.2.31} and~\\ref{maps:src:D.2.37},"),
        ("These calculations use the normal parametrizations of \\ref{maps:src:D.2.29}", "These calculations use the normal parametrizations of Theorem~\\ref{maps:src:D.2.29}"),
        ("Use the root-disc construction of \\ref{maps:src:D.2.29} and \\ref{maps:src:D.2.34},", "Use the root-disc construction of Theorems~\\ref{maps:src:D.2.29} and~\\ref{maps:src:D.2.34},"),
        ("The normalization complex of \\ref{maps:src:D.2.34}", "The normalization complex of Theorem~\\ref{maps:src:D.2.34}"),
        ("the flat degree-zero ruled component of \\ref{maps:src:D.2.31};", "the flat degree-zero ruled component of Theorem~\\ref{maps:src:D.2.31};"),
        ("The lifted flow of \\ref{maps:src:D.2.32}--\\ref{maps:src:D.2.33},", "The lifted flows of Theorems~\\ref{maps:src:D.2.32} and~\\ref{maps:src:D.2.33},"),
        ("with\nthe inverse line flow of \\ref{maps:src:D.2.32}--\\ref{maps:src:D.2.33}", "with\nthe inverse line flow of Theorems~\\ref{maps:src:D.2.32} and~\\ref{maps:src:D.2.33}"),
        ("the geometric u-normal of \\ref{maps:src:D.2.33}", "the geometric $u$-normal of Theorem~\\ref{maps:src:D.2.33}"),
        ("the identical words in the group proof of \\ref{maps:src:D.2.37}.", "the identical words in the group proof of Theorem~\\ref{maps:src:D.2.37}."),
        ("The weight-one inverse of \\ref{maps:src:D.2.31}", "The weight-one inverse of Theorem~\\ref{maps:src:D.2.31}"),
    ]
    for old, new in replacements:
        e.replace(old, new, "D04", owner,
                  "Name the verified theorem owner at this exact dependency reference; its label and mathematical input remain unchanged.")
    e.replace("\\emph{Exact degree-one exterior image at every d.}", "\\emph{Exact degree-one exterior image at every positive weight.}", "D16", owner,
              "Give the proof-part heading its descriptive positive-weight scope.")
    issues = e.presentation()
    if issues:
        raise ValueError(("Semantic equation references require reading", issues))
    e.finish(labels=("mapsIII:def:odd-weighted-data", "mapsIII:rem:odd-weighted-calculations"),
             tags=("Q138", "Q139"))


if __name__ == "__main__":
    main()
