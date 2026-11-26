"""Exact publication edits to the wholly read weighted-natural-profile unit."""
import re
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def interval(e, start, end):
    if e.text.count(start) != 1 or e.text.count(end) != 1:
        raise ValueError(("Stale or ambiguous read interval", start, end))
    a, b = e.text.index(start), e.text.index(end)
    if a >= b:
        raise ValueError("Reversed interval")
    return e.text[a:b]


def main():
    e = Editor("weighted_natural_profiles", "C8-FND-WEIGHTED-PROFILES-")
    old = interval(e, r"\begin{theorem}[Weighted natural profiles]", "For $N$ sites, ordered with\n")
    new = r"""\subsection{Weighted natural profiles and their integral cap maps}

\begin{definition}[Weighted natural data]
\hypertarget{tag-Q136}{}\label{mapsIII:def:weighted-natural-data}
{\normalfont\scriptsize tag Q136}\par
Choose one of the $172$ natural initial rows of
Theorem~\ref{maps:src:D.2.22}, with $P=aG$, $Q=bG$,
$a,b>0$, $\gcd(a,b)=1$, and weight
\[
 d>0,\qquad\gcd(a,d)=1.
 \tag{D.WP1}\hypertarget{tag-027O}{}\label{maps:eq:D.WP1}
\]
Take the $d$th iterate of its contracting line map: the
translation is $dbG$, and the linearization is the norm of the
initial linearization. Use the same unimodular Mumford fan with
the resulting period subgroup and its unchanged chart units.

Let $\mathcal P$ be the marked cap patterns of
Theorem~\ref{maps:src:D.2.33}: original or finite-good fillings
at $\mathrm{II},\mathrm{III},\mathrm{IV},\mathrm{III}^*,\mathrm{IV}^*$,
original fillings at odd $I_n^*$, and the original or Mumford
choices at the specified multiplicative sites. Write
$\mathcal P_{\mathrm{all\ star\ O}}$ for the subset in which
$\mathrm{III}^*$ and $\mathrm{IV}^*$ are also original.
Allow every free finite-good logarithm at an allowed site,
every finite list of free regular logarithms, and every integer
clutch $e$.

Use the periods of Definition~\ref{mapsIII:def:elliptic-marked-data},
in the order $\Lambda=\mathbb Z\langle e_1,e_2,\delta,\gamma\rangle$.
For the initial matrices $A_i$ put
\[
 A_i(d)=S_d^{-1}A_iS_d,\qquad S_d=\operatorname{diag}(1,1,1,d),
 \tag{D.WP2}\hypertarget{tag-027S}{}\label{maps:eq:D.WP2}
\]
and set
\[
 \omega_d=a e_1^*\wedge e_2^*-db\,\delta^*\wedge\gamma^*.
 \tag{D.WP3}\hypertarget{tag-027T}{}\label{maps:eq:D.WP3}
\]
Each regular site has identity monodromy. Represent clutch $e$
by an auxiliary order-one regular site with power $-e\gamma$.

Let $L$ count the nonzero-Chern originals. Define $\beta$ by
summing $\gcd(d,n_i)-1$ at a zero-free rank-one site with
narrow $P$, zero at a non-narrow marked Mumford filling,
$\rho_i(d)-1$ at a zero-Chern additive original, and $s_i-2$
or $n_i-2$ at a nonzero-Chern additive or multiplicative original,
respectively. Here $s_i$ is the number of Kodaira components,
and $\rho_i(d)$ is the number of component orbits under the
$d$th power of the translation by $Q$. The selected rank-two
cusp is excluded from $\beta$.
\end{definition}

\begin{theorem}[Weighted natural profiles]
\hypertarget{tag-02LD}{}\label{maps:src:D.2.37}
{\normalfont\scriptsize tag 02LD}\par
For the data of Definition~\ref{mapsIII:def:weighted-natural-data},
the set $\mathcal P$ has $495$ patterns and
$\mathcal P_{\mathrm{all\ star\ O}}$ has $459$.
Its inclusion preserves every site label; the retraction replaces
only the finite-good $\mathrm{III}^*$ and $\mathrm{IV}^*$ choices
by their original fillings. The following integral algorithm
applies to both sets and every stated parameter.

The matrices $A_i(d)$ are integral and retain their ordered
product identity. The change multiplies precisely the first
three entries of each $\gamma$ column by $d$.
The functional $\omega_d$ is primitive and invariant under them.
The selected cusp has $d$ normalized components.

"""
    e.replace(old, new, "D13", "maps:src:D.2.37",
              "Create an actual subsection and one numbered input definition for all weighted rows, cap sets, period/area data, regular/clutch inputs and component counts. Preserve WP1-WP3 identities; keep the 495/459 counts, integrality, primitivity and cusp count as proved theorem conclusions.")
    old = interval(e, "Define $\\beta$ by summing the following local contributions:\n", "For the logarithms other than the auxiliary clutch site put\n")
    e.replace(old, "Use $L$ and $\\beta$ from\nDefinition~\\ref{mapsIII:def:weighted-natural-data}.\n\n", "D12", "maps:src:D.2.37",
              "Use the single numbered component-count definition; all five local contributions and the separate weighted cusp count retain their exact domains.")
    old = interval(e, "The finite selection of the 172 rows is as follows. At a\n", "The defining component coordinate and the positive Tate indexing\n")
    new = r"""The $172$ natural rows are the complete rows of
Theorem~\ref{maps:src:D.2.22}. Their identification here fixes
the ordered profile, selected zero, positive pair $(a,b)$ and
every component coordinate in Definition~\ref{mapsIII:def:elliptic-marked-data};
the inverse reads that same tuple. Thus the displayed raw
matrices use exactly those marked elliptic matrices and section
cocycles, including the cases in which component terms coincide.

"""
    e.replace(old, new, "D12", "maps:src:D.2.37",
              "Use KX as the sole owner of the already proved natural-row factor/component enumeration, through identity on every ordered datum. Retain every new weighted raw matrix, lattice calculation and cap-pattern count.")
    old = "Integer row and column operations reduce it to two \\(t-1\\)\nentries and one unit. Equal coefficients give the kernel of\n\\(t-1\\); successive partial sums give the inverse on its\nzero-sum image. Together with the dual-torus cells this yields\n"
    new = r"""Identify $\mathcal R_d$ with the coefficient ring $\mathcal A_d$
in Theorem~\ref{maps:src:D.2.34} by $[p(t)]\mapsto[p(t)]$.
On the normalization complex, send each marked component,
branch and dual-torus cell with coefficient $t^j$ to the cell
with that same index and coefficient. In the displayed ordered
bases the degree-two matrix is identical; the degree-zero row
is the same dual-torus complex and the degree-four row is the
same group ring. The inverse reads those identical coordinates.
This chain isomorphism carries the unit and $t-1$ reductions,
their partial-sum inverse and the free extension section proved
there to this complex. Consequently
"""
    e.replace(old, new, "D12", "maps:src:D.2.37",
              "Give the common periodic-cusp normalization computation its earlier LA owner through the explicit identity of coefficient rings and every ordered branch-cell complex, with inverse; retain the full input matrix and all cusp groups.")
    e.replace(r"period matrix \(R_d=(e_1,e_2,\delta,\ell_d)\), whose inverse" + "\n",
              r"period matrix \(\mathcal B_d=(e_1,e_2,\delta,\ell_d)\), whose inverse" + "\n",
              "D20", "maps:src:D.2.37",
              "Name the local four-by-four additive period basis separately from the earlier rectangular exterior right inverse R_d; the coordinate map and its inverse are unchanged.")
    e.replace(r"\(\beta_0=R_d(v_0,0)\), and \(k_d=\beta_0\wedge\ell_d\)." + "\n",
              r"\(\beta_0=\mathcal B_d(v_0,0)\), and \(k_d=\beta_0\wedge\ell_d\)." + "\n",
              "D20", "maps:src:D.2.37",
              "Carry the same local period-basis name to its actual vector image; identity on every basis column supplies the inverse renaming.")
    old = interval(e, "In the zero-degree component frames, the two opposite\n", "For P non-narrow the primitive vector is instead\n")
    new = r"""Use the zero-degree component frames and their node units.
The node charts and their inverses in
Theorem~\ref{maps:src:D.2.33} carry this period basis and its units.
For both the original and the marked Mumford filling, the fibre
map in the basis $(u',r',\delta,\ell')$ has coordinates
\[
 Q_d(y)=(y_{12},y_{23},y_{24},y_{34}),\qquad
 \sigma_d(z)=z_1e_{12}+z_2e_{23}+z_3e_{24}+z_4e_{34}.
\]
They are the ruled fibre, two gluing-circle products and base
torus. Cutting the gluing and reading these coordinates gives
the cap-coordinate inverse, and $Q_d\sigma_d=I$.
The three fixed-normal sweeps bound in both fillings.
For their full boundary maps $f_O,f_M$, let $\sigma_O,\sigma_M$
be the resulting boundary sections after reading each cap's
four coordinates. Then $f_M\sigma_O$ and $f_O\sigma_M$ are
inverse target isomorphisms and commute with the common marked
boundary map. This proves their marked kernel and primitive-image
agreement. Their local free cokernel is
$\gcd(d,\nu)-1=0$ in the present scope.

"""
    e.replace(old, new, "D20", "maps:src:D.2.37",
              "State the zero-Chern original/Mumford comparison at its proved integral boundary-map scope with the full quotient/section and inverse target maps, preserving the actual period and node units. No stronger cap diffeomorphism is inferred.")
    old = "For each defining profile the finite factor enumeration given by the component-degree equation\nis exhaustive: a ranges through the positive divisors\nof \\(d_0/n_*\\), which is at most 30 in the defining profile data. For each resulting row take the Cartesian product\n"
    new = "For each defining profile the exhaustive factor enumeration of\nTheorem~\\ref{maps:src:D.2.22} has $a$ among the positive divisors\nof $d_0/n_*$, at most $30$ in the marked data. For each resulting\nrow take the Cartesian product\n"
    e.replace(old, new, "D06", "maps:src:D.2.37",
              "Point the final exhaustive pattern construction to KX's exact component/factor owner after removing its repeated derivation; retain the bound, every Cartesian choice and the inverse tuple map.")
    for start, end in [
        ("OS & Profile & R & K & P & S & A \\\\\n", "\\textbf{Total} &  & \\textbf{172}"),
        ("OS & Profile & Omitted patterns \\\\\n", "\\end{tabular}\n\\end{center}\n\nThe local map changed by this projection"),
    ]:
        old = interval(e, start, end)
        new = old.replace(" & default & ", " & base & ")
        if old == new:
            raise ValueError("Expected the read base-profile table labels")
        e.replace(old, new, "D20", "maps:src:D.2.37",
                  "Use the same explicit default-to-base profile-name bijection as Q110/KX and the earlier catalogues, with inverse restoring the former name; every numerical value, site choice and ordered row stays fixed.")
    old = e.text[e.text.index("The program verifies all $172$ weight-zero\n"):]
    new = r"""\begin{remark}[Finite weighted-profile calculations]
\hypertarget{tag-Q137}{}\label{mapsIII:rem:weighted-profile-calculations}
{\normalfont\scriptsize tag Q137}\par
The finite computation includes all $172$ constant-specialization
relation matrices and $1626$ full weighted graph presentations on
the $495$ patterns, of which $1131$ have weight greater than one.
The full parameter range follows from the integer right inverses,
complete local kernels and integral relative splitting in the proof.
Definition~\ref{mapsIII:def:weighted-natural-data} specifies the
initial translation iterates and every permitted cap choice.

Theorem~\ref{maps:src:D.2.41} gives the integral algorithm for all
positive weights, including weights sharing factors with $a$.
The inclusion of the present input set fixes the initial marked
row, $d$, every ordered cap choice, all logarithmic $(m,v)$ data
and the clutch; its inverse on that subset reads the same list.
\end{remark}

"""
    e.replace(old, new, "D13", "maps:src:D.2.37",
              "Give the orphan finite calculation and range pointer a numbered remark, preserve all 172/1626/1131 results, identify the actual constructive all-parameter proof, and state the exact input inclusion into LI. Redundant negative scope and smooth-inference framing are replaced by the positive input definition; executable paths belong in the common program table.")

    # Each listed target's actual theorem header has been read in this pass
    # or its earlier wholly read owned unit; only these labels are changed.
    known = {"maps:src:D.2.22", "maps:src:D.2.23", "maps:src:D.2.29",
             "maps:src:D.2.30", "maps:src:D.2.31", "maps:src:D.2.32",
             "maps:src:D.2.33", "maps:src:D.2.41"}
    pattern = re.compile(r"(?<!~)\\ref\{(maps:src:[^}]+)\}")
    for old in list(e.text.splitlines(keepends=True)):
        matches = list(pattern.finditer(old))
        if not matches:
            continue
        if any(m.group(1) not in known for m in matches):
            raise ValueError("Unreviewed statement kind in: " + old)
        new = pattern.sub(lambda m: "Theorem~" + m.group(0), old)
        e.replace(old, new, "D04", "maps:src:D.2.37",
                  "Print the verified theorem kind at this exact preserved-label reference; all target scopes and proof contents are unchanged.")
    issues = e.presentation()
    if issues:
        raise ValueError(issues)
    e.finish(labels=("mapsIII:def:weighted-natural-data", "mapsIII:rem:weighted-profile-calculations"),
             tags=("Q136", "Q137"))


if __name__ == "__main__":
    main()
