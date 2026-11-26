"""Dependency-ordered editing of the wholly read KT/KX/KY catalogue."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("elliptic_catalogue", "c8-III-foundations-catalogue-")
    kt, kx, ky = "maps:src:D.2.19", "maps:src:D.2.22", "maps:src:D.2.23"
    data_start = e.text.index(r"\emph{The marked component data.}")
    data_end = e.text.index("\nAt an $I_n$ write\n", data_start)
    old_data = e.text[data_start:data_end]
    data = old_data.split("\n", 1)[1]
    data = data.replace(r"\mathrm{def}", r"\mathrm{base}")
    data = data.replace("and $g_i=(p,q)^t$; $\\mathrm{base}$ denotes the default profile.\nThe index $i$ is the peripheral order within that profile.",
        "and $g_i=(p,q)^t$. The symbol $\\mathrm{base}$ denotes the profile\nwith the largest number of singular fibres in its OS entry; an\nunadorned OS number denotes this same ordered profile. The index\n$i$ is its peripheral order. The height denominators are\n\\[\n\\begin{array}{c|rrrrrrrr}\n\\mathrm{OS}&43&45&46&47&49&50&55&56\\\\\\hline\nd&2&8&4&14&6&12&20&30.\n\\end{array}\n\\]\n")
    if "default" in data:
        raise ValueError("Marked-profile introduction did not match")
    definition = (r"\subsection{Marked elliptic profiles and whole-fibre linearizations}" + "\n\n"
                  + r"\begin{definition}[Ordered elliptic profile data]" + "\n"
                  + r"\hypertarget{tag-Q110}{}\label{mapsIII:def:elliptic-marked-data}" + "\n"
                  + r"{\normalfont\scriptsize tag Q110}\par" + "\n" + data
                  + "\n" + r"\end{definition}" + "\n\n")
    e.replace(old_data, r"""Use the lattice and ordered profile data of
Definition~\ref{mapsIII:def:elliptic-marked-data}. Put
\[
 J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
The natural ordered pairs, zero components and their contracting
line isomorphisms are those of Theorem~\ref{maps:src:D.2.22}.""",
              "D13", ky,
              "Move all 82 ordered elliptic matrix/cocycle entries and their common lattice data into Q110 before KT. All numerical entries and peripheral orders remain unchanged; base is the explicitly defined label for the formerly named default profile.")
    header = r"\begin{proposition}[finite initial data for the whole-fibre problem]\hypertarget{tag-02KT}{}\label{maps:src:D.2.19}"
    e.replace(header, definition + r"\begin{proposition}[Degree-one whole-fibre linearizations]\hypertarget{tag-02KT}{}\label{maps:src:D.2.19}" + "\n"
              + r"{\normalfont\scriptsize tag 02KT}\par", "D14", kt,
              "Place the common marked table before its first use and give the whole-fibre criterion a complete mathematical subsection with its preserved visible tag.")

    duplicate_start = e.text.index("\nAt an $I_n$ write\n", e.text.index(r"\label{maps:src:D.2.23}"))
    duplicate_end = e.text.index(r"\emph{The four-period marking.}", duplicate_start)
    old_duplicate = e.text[duplicate_start:duplicate_end]
    replacement = r"""
At the chosen $I_n$ write
\[
 A=I+n uu^tJ,\qquad g=\kappa u,\qquad \det(u,r)=1.
\]
The component criterion in Theorem~\ref{maps:src:D.2.22} gives
$ab=d/n$ and, for $n>1$, $a\kappa=b\kappa=\pm1\pmod n$.
For $n=1$ there is one component. At every other reducible fibre
one of $P,Q$ is narrow. The same theorem provides the complete
172 marked choices and the elliptic-inversion map for simultaneous
sign reversal.

"""
    e.replace(old_duplicate, replacement, "D12", ky,
              "KX already proves the identical natural component criterion, rational-function line isomorphism, 172-row count and inversion map for these same ordered data. Cite that single owner and retain the exact hypotheses needed by KY's distinct four-period and normal-closure calculation.")

    scope_start = e.text.index("Finally, the scope of these initial data")
    scope_end = e.text.index(r"\end{proof}", scope_start)
    scope = e.text[scope_start:scope_end]
    remark = r"""\begin{remark}[Integral vertical changes of the section line]
\hypertarget{tag-Q116}{}\label{mapsIII:rem:vertical-section-lines}
{\normalfont\scriptsize tag Q116}\par
For an integral vertical divisor $V$, the line
$M'=M\otimes\mathcal O(V)$ has linearization line
\[
 J'=J\otimes\mathcal O(V-t_Q^*V).
\]
Tensoring by $\mathcal O(-V)$ reverses this change, and
intersection with each component gives its degree change.
For the OS49 datum $P=G,Q=3G$ of
Theorem~\ref{maps:src:D.2.11}, the mixed height is $1/2$ and
the linearization line is $\mathcal O(C_0)$. At its $I_2$ fibre
the degree vector is $(-2,2)$. The whole-fibre line
$\mathcal O(C_0+C_1)=f^*\mathcal O([\infty])$ has degree
vector $(0,0)$, and tensoring by $\mathcal O(C_1)$ gives the
map from the component line to this whole-fibre line; tensoring
by $\mathcal O(-C_1)$ is its inverse.
\end{remark}

"""
    e.replace(scope, "", "D20", kt,
              "Move the full useful vertical-line conversion into its numbered remark Q116; remove the repeated closing finite-index/attachment-scope narration, already stated in the propositions.")
    kx_header = r"\begin{theorem}[Finite section-line data for homotopy six-spheres]"
    e.replace(kx_header, remark + r"\subsection{Finite section-line data for homotopy six-spheres}" + "\n\n" + kx_header,
              "D14", kx,
              "Put the complete necessary-data classification in its own subsection after the whole-fibre prerequisite and the numbered vertical-line conversion.")
    scope_start = e.text.index(r"\paragraph{Scope after \ref{maps:src:D.2.22}.}")
    scope_end = e.text.index(r"\begin{theorem}[uniform all-order fundamental groups", scope_start)
    e.replace(e.text[scope_start:scope_end], "", "D13", kx,
              "Remove the orphan scope paragraph from between proofs. Its exact Viaclovsky Question 4 and Engel Remark 8.5 inputs and the remaining all-order gluing task are sent to root/lg_fresh for the single final open synthesis; the theorem's exact initial-data scope remains.")
    old_ky = r"\begin{theorem}[uniform all-order fundamental groups on the natural catalogue]\hypertarget{tag-02KY}{}\label{maps:src:D.2.23}"
    e.replace(old_ky, r"\subsection{Fundamental groups of the natural section-line families}" + "\n\n"
              + r"\begin{theorem}[Fundamental groups for all logarithmic orders]\hypertarget{tag-02KY}{}\label{maps:src:D.2.23}" + "\n"
              + r"{\normalfont\scriptsize tag 02KY}\par", "D14", ky,
              "Give the all-order group theorem its own complete subsection after the finite initial-data classification and print the permanent small tag.")

    changes = [
        ("Restrict to the uncorrected line\n", "Use the section line\n", "D08", kt,
         "Name the exact geometric line by its formula without a correction-history qualifier."),
        (r"For the marked profiles of \CompendiumRef{III}{maps:src:D.2.1} they are",
         r"For the marked profiles of Definition~\ref{mapsIII:def:elliptic-marked-data} they are", "D06", kt,
         "Replace the unresolved compendium pointer by the complete relocated common data definition."),
        ("ordered factor-pair candidates, exactly 88 of which", "ordered factor pairs with $ab=d$, exactly 88 of which", "D08", kt,
         "Describe the enumerated finite set by its defining equation rather than candidate terminology."),
        ("marked integral monodromy tuples are recorded exactly.\nEach finite index specifies", "marked integral monodromy tuples are given by the formula in the proof.\nEach datum specifies", "D08", kt,
         "Point to the actual printed formula and the mathematical datum, not an external record."),
        (r"\cite[Section 11.8]{manSS10}", r"\cite[Section~11.8, pp.~51--52]{manSS10}", "D18", kt,
         "Use the exact primary height-formula pages opened in this foundations pass."),
        ("We next calculate the finite list from the marked profile data.\nThe matrices and section vectors are displayed in the component-data\ntable in the proof of \\ref{maps:src:D.2.23}; the calculations here\nstart from those entries.",
         "For the finite list, use the ordered matrices and section vectors of\nDefinition~\\ref{mapsIII:def:elliptic-marked-data}.", "D14", kt,
         "Remove the forward dependence on KY's later proof; the identical data now precede this calculation."),
        ("The normalized Poincare line construction in\n\\ref{maps:src:D.2.12} gives",
         "The normalized Poincar\\'e line construction in\nTheorem~\\ref{maps:src:D.2.12} gives", "D23", kt,
         "Restore the accent and print the correct theorem kind at the period-formula prerequisite."),
        ("Poincare frames", "Poincar\\'e frames", "D23", kt,
         "Restore the accent at the central winding calculation."),
        (r"\textnormal{\small tag02KX.}", r"{\normalfont\scriptsize tag 02KX}\par", "D10", kx,
         "Use the common small-tag presentation with the existing target and readable spacing."),
        ("elliptic profiles of \\ref{maps:src:D.2.2}, with Mordell--Weil group", "elliptic profiles of Definition~\\ref{mapsIII:def:elliptic-marked-data}, with Mordell--Weil group", "D06", kx,
         "Point the geometric profile hypothesis to its actual complete input definition, rather than the separate cohomology-output theorem."),
        (r"\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]", r"\begin{enumerate}[label=\arabic*.,leftmargin=*]", "D04", kx,
         "Remove the inherited research-stage prefix from the proof's mathematical step numbers."),
        ("This is the component-supported zero of \\ref{maps:src:D.2.11}.", "This is the component-supported zero of Theorem~\\ref{maps:src:D.2.11}.", "D04", kx,
         "Print the correct statement kind for the concrete component-zero example."),
        ("For the minimal quotient $U_0$", "For the minimal quotient $U_0$", "NONE", kx, ""),
        ("\\ref{maps:src:D.1.2} at \\(d=1\\) give", "Theorem~\\ref{maps:src:D.1.2} at \\(d=1\\) give", "D04", kx,
         "Identify the earlier cyclic cusp conductor theorem by kind and permanent label."),
        ("\\ref{maps:src:D.2.19}, its central entry is", "Proposition~\\ref{maps:src:D.2.19}, its central entry is", "D04", kx,
         "Identify the whole-fibre period formula by its correct proposition kind."),
        ("\\ref{maps:src:D.2.19} identify the base degree", "Proposition~\\ref{maps:src:D.2.19} identify the base degree", "D04", kx,
         "Identify the narrow height and line-map prerequisite by its correct proposition kind."),
        ("\\ref{maps:src:D.2.22}, retain any", "Theorem~\\ref{maps:src:D.2.22}, use any", "D04", ky,
         "Print the classification theorem kind and state the permitted geometric fillings directly."),
        ("The Poincare line marking in \\ref{maps:src:D.2.12} gives this", "The Poincar\\'e line marking in Theorem~\\ref{maps:src:D.2.12} gives this", "D23", ky,
         "Restore the accent and the precise statement kind for the signed four-period formula."),
        ("These are the primitive cusp charts of \\ref{maps:src:D.2.6}.", "These are the primitive cusp charts of Theorem~\\ref{maps:src:D.2.6}.", "D04", ky,
         "Print the correct theorem kind for the exact chart prerequisite."),
    ]
    for old, new, kind, label, reason in changes:
        if kind != "NONE":
            e.replace(old, new, kind, label, reason)

    # Change only the three explicitly read table blocks still using the old
    # profile abbreviation. This is a named index conversion, not prose substitution.
    blocks = [
        ("\\begin{array}{c|l|l|r|r}", "\\end{array}", r"\text{default}", kt),
        ("\\begin{array}{clr|cccrr}", "\\end{array}", r"\mathrm{def}", ky),
    ]
    for begin, end, old_symbol, label in blocks:
        starts = []
        pos = 0
        while True:
            pos = e.text.find(begin, pos)
            if pos < 0:
                break
            starts.append(pos)
            pos += len(begin)
        for start in reversed(starts):
            stop = e.text.index(end, start) + len(end)
            old = e.text[start:stop]
            if old_symbol in old:
                new = old.replace(old_symbol, r"\mathrm{base}")
                e.replace(old, new, "D20", label,
                          "Use Q110's explicitly defined base-profile label in this exact table. Every ordered numerical entry, coefficient and count is unchanged.")

    old = r"""For a column $(x,y)^t$ and
$\alpha x+\beta y=g=\gcd(x,y)$, the row map and inverse"""
    new = r"""Start with a nonzero column, exchanging the two columns when
necessary; the exchange is its own inverse. Such a column exists
because $(m_1,-m_2)^t$ is nonzero. Zero columns are skipped.
For a nonzero column $(x,y)^t$, choose
$\alpha x+\beta y=g=\gcd(x,y)>0$. The row map and inverse"""
    e.replace(old, new, "D22", ky,
              "Specify the nonzero domain and initialization of the Bezout reduction. The first column may vanish when n1=n2=e=0, while the second always provides a nonzero pivot. The explicit swap/inverse and zero-column convention preserve all endpoint groups.")
    issues = e.presentation()
    if issues:
        raise ValueError(issues)
    e.finish(labels=("mapsIII:def:elliptic-marked-data", "mapsIII:rem:vertical-section-lines"), tags=("Q110", "Q116"))


if __name__ == "__main__":
    main()
