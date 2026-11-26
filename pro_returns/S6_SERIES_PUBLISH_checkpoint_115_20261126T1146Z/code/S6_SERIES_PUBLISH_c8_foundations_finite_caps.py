"""Exact edits after the complete L4/L6 source and receiving comparisons."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def interval(e, start, end):
    if e.text.count(start) != 1 or e.text.count(end) != 1:
        raise ValueError("Stale or ambiguous wholly read interval")
    a, b = e.text.index(start), e.text.index(end)
    if a >= b:
        raise ValueError("Reversed interval")
    return e.text[a:b]


def main():
    e = Editor("finite_primitive_caps", "C8-FND-FINITE-CAPS-")
    old = interval(e, r"\begin{theorem}[Finite caps with primitive fixed quotient]", "The cyclic affine action with this power vector is free exactly\n")
    new = r"""\subsection{Finite caps with a primitive contracting period}

\begin{definition}[Primitive fixed finite-cap data]
\hypertarget{tag-Q121}{}\label{mapsIII:def:primitive-fixed-finite-data}
{\normalfont\scriptsize tag Q121}\par
Take a natural initial row of Theorem~\ref{maps:src:D.2.22}, with
section pair $(P,Q)=(aG,bG)$ and the marked period lattice of
Definition~\ref{mapsIII:def:elliptic-marked-data}. Write
$\omega=a\,e_1^*\wedge e_2^*-b\,\delta^*\wedge\gamma^*$.
At a finite additive position with a marked integral fixed vector
$\ell_i$ satisfying $\gamma^*(\ell_i)=1$, take $(d_i,q_i)$ from
\eqref{maps:eq:D.HY2} and set
\[
 m_i=d_i k_i,\qquad v_i=n_i\ell_i+r_i\delta,\qquad
 t_i=\gcd(m_i,n_i,q_i r_i),\qquad
 k_i\in\mathbb Z_{>0},\quad n_i,r_i\in\mathbb Z.
\]
For a global filling, use a nonstar initial row, the minimal
original and Mumford caps of Theorem~\ref{maps:src:D.2.26}, any
number of regular logarithmic caps with their free affine vectors,
and an integer clutch $e\in\mathbb Z$.
\end{definition}

\begin{theorem}[Finite caps with primitive fixed quotient]
\hypertarget{tag-02L4}{}\label{maps:src:D.2.29}
{\normalfont\scriptsize tag 02L4}\par
There are $68$ finite additive positions with the primitive fixed
vector of Definition~\ref{mapsIII:def:primitive-fixed-finite-data}.
The local assertions below hold at all of them. Their restriction
to the nonstar initial rows consists of $62$ positions; the global
assertions concern those rows and the fillings in that definition.
"""
    e.replace(old, new, "D13", "maps:src:D.2.29",
              "Separate the exact marked input, area convention and all integer domains into a numbered definition before the local/global theorem; retain the proved 68/62 scope distinction in the theorem.")
    e.replace("We first retain the integral marking of one finite site, suppressing\n",
              "Fix the integral marking of one finite site, suppressing\n", "D08", "maps:src:D.2.29",
              "State the actual local choice directly without workflow retention language.")
    e.replace("The actual $\\delta$ circle over the cut base supplies its\n",
              "The $\\delta$ circle over the cut base supplies its\n", "D08", "maps:src:D.2.29",
              "Use the named geometric circle directly; its explicit bounding-chain assertion is retained.")
    e.replace("For example, take the $IV^*,II,I_2$ sphere initial row\n", r"""\begin{remark}[Torsion-core and zero-Euler examples]
\hypertarget{tag-Q122}{}\label{mapsIII:rem:finite-torsion-examples}
{\normalfont\scriptsize tag Q122}\par
With clutch $e=0$, take the $IV^*,II,I_2$ sphere initial row
""", "D13", "maps:src:D.2.29",
              "Keep the two actual endpoint examples in a numbered remark and state the zero clutch used by their displayed groups.")
    e.replace("Extrapolating the former primitive-numerator formula would\nmiss one order-three summand. For a $III^*$ sphere initial\nrow with $b=2$, the free data $(q,m,n,r)=(2,8,0,1)$ instead\n", r"""Here the global relation is $D=0$, and the full Thom relations
reduce to $3s=3L'=0$. The quotient map sends $xs+yL'$ to
$(x\bmod3,y\bmod3)$; lifting these residues gives its inverse.
For a $III^*$ sphere initial row with $b=2$ and $e=0$, the free
data $(q,m,n,r)=(2,8,0,1)$
""", "D01", "mapsIII:rem:finite-torsion-examples",
              "Replace the retrospective comparison by the exact two-generator quotient and inverse, and make the second example's same zero-clutch endpoint explicit.")
    e.replace("$H_4=\\mathbb Z^2$, $H_5=\\mathbb Z$.\n\nThe exact program\n", "$H_4=\\mathbb Z^2$, $H_5=\\mathbb Z$.\n\\end{remark}\n\nThe exact program\n",
              "D13", "mapsIII:rem:finite-torsion-examples",
              "Close the complete numbered example remark before the separate finite-computation scope.")
    old = interval(e, "The exact program\n", r"\begin{theorem}[Finite additive lattices and free affine twists]")
    new = r"""\begin{remark}[Finite affine-power and attachment calculations]
\hypertarget{tag-Q123}{}\label{mapsIII:rem:primitive-finite-calculations}
{\normalfont\scriptsize tag Q123}\par
A finite comparison evaluates \eqref{maps:eq:D.UF1} and the
affine-power fixed-point equations for all $68$ marked matrices,
$1\le k\le6$ and every pair $(n,r)\bmod m$; the $150059$ exact
results agree. For $305$ choices, the full unreduced graph and
normal Smith matrices give the reduced presentation above,
including $99$ torsion-cap instances and $55$ zero-rational-Euler
instances. The all-parameter argument is the proof of
Theorem~\ref{maps:src:D.2.29}.
\end{remark}

"""
    e.replace(old, new, "D09", "mapsIII:rem:primitive-finite-calculations",
              "Retain the exact finite inputs, method, ranges and results in a numbered mathematical remark; move the executable path and run attribution to the common program proposal table and historical records.")
    old = interval(e, r"\begin{theorem}[Finite additive lattices and free affine twists]", "The positive generator $g$ equals $1$ at $68$ positions and\n")
    new = r"""\subsection{All finite additive lattices and affine twists}

\begin{definition}[General finite additive-cap data]
\hypertarget{tag-Q124}{}\label{mapsIII:def:general-finite-additive-data}
{\normalfont\scriptsize tag Q124}\par
Take a finite additive position on a natural initial row of
Theorem~\ref{maps:src:D.2.22}, with the section pair, lattice and
area form of Definition~\ref{mapsIII:def:primitive-fixed-finite-data}.
Let $A$ have order $d$, let $q$ have the value in
\eqref{maps:eq:D.HY2}, and let $g$ be the positive generator in
\[
 \gamma^*(\operatorname{Fix}A)=g\mathbb Z,\qquad q_v=q/g.
 \tag{D.AF1}\hypertarget{tag-01XI}{}\label{maps:eq:D.AF1}
\]
Write $m=dk$ with $k\in\mathbb Z_{>0}$, and use integer
coefficients $r,n$ for the power vector $v=r\delta+n\ell$
in the fixed basis below. Put $t=\gcd(m,q_vr,gn)$.
\end{definition}

\begin{theorem}[Finite additive lattices and free affine twists]
\hypertarget{tag-02L6}{}\label{maps:src:D.2.30}
{\normalfont\scriptsize tag 02L6}\par
There are $102$ finite additive positions on the $172$ natural
initial rows. At each one, the invariant in
Definition~\ref{mapsIII:def:general-finite-additive-data} satisfies
$g\in\{1,q\}$.
"""
    e.replace(old, new, "D13", "maps:src:D.2.30",
              "Put the general fixed-lattice invariant and parameter definitions before their theorem in a new actual subsection; keep the 102-position enumeration and two possible values as theorem conclusions.")
    e.replace("Here $m=dk>0$ and the bases carry their integral quotient\ncoordinates.\n\nFor a power vector $v=r\\delta+n\\ell$, set\n$t=\\gcd(m,q_vr,gn)$. The cyclic affine action is free exactly for\n",
              "These bases carry their integral quotient coordinates.\nFor the power vector in Definition~\\ref{mapsIII:def:general-finite-additive-data},\nthe cyclic affine action is free exactly for\n", "D13", "maps:src:D.2.30",
              "Use the single preceding numbered parameter definition while retaining every fixed and coinvariant basis assertion.")
    old = e.text[e.text.index(r"The exact program \path{code/III/manifolds_all_finite_logs.py}"):]
    new = r"""\begin{remark}[Finite lattice and one-site calculations]
\hypertarget{tag-Q125}{}\label{mapsIII:rem:general-finite-calculations}
{\normalfont\scriptsize tag Q125}\par
The finite calculation includes all $34$ additional lattice bases.
For $1\le k\le6$ and every residue pair, $38675$ exact
affine-power fixed-point tests agree with \eqref{maps:eq:D.AF3}.
The $175$ full unreduced normal and graph Smith matrices agree
with \eqref{maps:eq:D.AF4}, including $35$ torsion-cap instances.
The one-site calculation compares $725$ Smith forms, with five
integer clutch values, with
\eqref{maps:eq:D.AF6}--\eqref{maps:eq:D.AF7}; all agree.
Theorem~\ref{maps:src:D.2.30} proves the formulas for every
positive order and every free integer twist.
\end{remark}

"""
    e.replace(old, new, "D09", "mapsIII:rem:general-finite-calculations",
              "Keep every stated finite input range and output in a numbered remark, put the exact historical executable path in the shared program proposals, and remove the closing reference to the broader prompt request.")
    qualifications = [
        ("The integral local calculation in \\ref{maps:src:D.2.26}", "The integral local calculation in Theorem~\\ref{maps:src:D.2.26}"),
        ("in\n\\ref{maps:src:D.2.23} as", "in\nTheorem~\\ref{maps:src:D.2.23} as"),
        ("the full Seifert group of\n\\ref{maps:src:D.2.23}.", "the full Seifert group of\nTheorem~\\ref{maps:src:D.2.23}."),
        ("The integral exterior calculation in \\ref{maps:src:D.2.26}", "The integral exterior calculation in Theorem~\\ref{maps:src:D.2.26}"),
        ("in \\ref{maps:src:D.2.25} and \\ref{maps:src:D.2.26}.", "in Theorems~\\ref{maps:src:D.2.25} and \\ref{maps:src:D.2.26}."),
        ("This is the full group in \\ref{maps:src:D.2.23}.", "This is the full group in Theorem~\\ref{maps:src:D.2.23}."),
        ("$(a,b)=(1,3)$ of \\ref{maps:src:D.2.11},", "$(a,b)=(1,3)$ of Theorem~\\ref{maps:src:D.2.11},"),
        ("the full presentation in \\ref{maps:src:D.2.23}.", "the full presentation in Theorem~\\ref{maps:src:D.2.23}."),
        ("The simply connected classification in\n\\ref{maps:src:D.2.28}", "The simply connected classification in\nCorollary~\\ref{maps:src:D.2.28}"),
        ("from \\ref{maps:src:D.2.29} consequently give", "from Theorem~\\ref{maps:src:D.2.29} consequently give"),
        ("basis. The argument of \\ref{maps:src:D.2.29} therefore", "basis. The argument of Theorem~\\ref{maps:src:D.2.29} therefore"),
        ("\\ref{maps:src:D.2.29} gives all the other cap groups.", "Theorem~\\ref{maps:src:D.2.29} gives all the other cap groups."),
        ("of \\ref{maps:src:D.2.29} with these full kernels.", "of Theorem~\\ref{maps:src:D.2.29} with these full kernels."),
        ("coordinates of \\ref{maps:src:D.2.26}.", "coordinates of Theorem~\\ref{maps:src:D.2.26}."),
        ("gives the $164$ patterns of \\ref{maps:src:D.2.26};", "gives the $164$ patterns of Theorem~\\ref{maps:src:D.2.26};"),
        ("\\ref{maps:src:D.2.23}, excludes this common divisor", "Theorem~\\ref{maps:src:D.2.23}, excludes this common divisor"),
    ]
    for old, new in qualifications:
        label = "maps:src:D.2.29" if e.text.index(old) < e.text.index(r"\subsection{All finite") else "maps:src:D.2.30"
        e.replace(old, new, "D04", label,
                  "Name the actual kind of the cited mathematical statement at this wholly read use; all referenced permanent identities are unchanged.")
    for old, new, label in [
        ("An integral Bezout completion", r"An integral B\'ezout completion", "maps:src:D.2.29"),
        ("Integral Poincare duality", r"Integral Poincar\'e duality", "maps:src:D.2.29"),
        ("A Bezout completion of its primitive column", r"A B\'ezout completion of its primitive column", "maps:src:D.2.30"),
    ]:
        e.replace(old, new, "D23", label, "Correct the exact proper-name accent found in the whole proof reading.")
    issues = e.presentation()
    if issues:
        raise ValueError(issues)
    e.finish(labels=("mapsIII:def:primitive-fixed-finite-data", "mapsIII:rem:finite-torsion-examples", "mapsIII:rem:primitive-finite-calculations", "mapsIII:def:general-finite-additive-data", "mapsIII:rem:general-finite-calculations"),
             tags=("Q121", "Q122", "Q123", "Q124", "Q125"))


if __name__ == "__main__":
    main()
