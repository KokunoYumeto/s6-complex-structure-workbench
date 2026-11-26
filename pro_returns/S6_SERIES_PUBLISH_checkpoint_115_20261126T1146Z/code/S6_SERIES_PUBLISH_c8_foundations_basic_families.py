"""Exact publication edits for the five fully read logarithmic-family units."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("elliptic_basic_families", "III-C8-FND-BASIC-")
    old = r"\begin{theorem}[arbitrary multiplicities in the original configuration]"
    e.replace(old, r"\begin{theorem}[Logarithmic multiplicities over $IV^*+III+I_1$]",
              "D16", "maps:src:D.2.5",
              "Name the precise elliptic profile rather than an unstated original configuration.")
    marking_start = e.text.index("Use the marked lattice\n")
    marking_end = e.text.index("Thus $A_0A_1A_\\infty=I$", marking_start)
    marking = e.text[marking_start:marking_end]
    e.replace(marking, "In the marking of Definition~\\ref{mapsIII:def:two-finite-fibre-marking},\n",
              "D13", "maps:src:D.2.5",
              "Move the complete lattice, three monodromy matrices and two named invariant vectors before the theorem that uses delta and u_i; the order and fixed-lattice verification stays in the sole proof.")
    marking = marking.replace("Use the marked lattice\n", "The marked lattice for the $IV^*+III+I_1$ profile is\n", 1)
    marking = marking.replace(". The homological\nmonodromies and invariant vectors are", ". Its homological\nmonodromies and distinguished vectors are", 1)
    source = (
        "These are the marking and local models of\n"
        "\\cite[Lemma~2.1 and equations (2.11)--(2.12), pp.~3--4;\n"
        "Propositions~2.3 and 3.1, pp.~5--7]{manViaclovskyLogs26}.\n"
    )
    e.replace(source, "", "D17", "maps:src:D.2.5",
              "Relocate the exact marking/local-model source credit with the numbered input definition; the proof retains the actual order and invariant-lattice equalities.")
    definition = (
        "\\section{Logarithmic families from rational elliptic surfaces}\n\n"
        "\\subsection{The $IV^*+III+I_1$ profile}\n\n"
        "\\begin{definition}[Marking for two finite-monodromy fibres]\n"
        "\\hypertarget{tag-Q107}{}\\label{mapsIII:def:two-finite-fibre-marking}\n"
        "{\\normalfont\\scriptsize tag Q107}\\par\n" + marking + source +
        "\\end{definition}\n\n"
    )
    e.replace(r"\begin{theorem}[Logarithmic multiplicities over $IV^*+III+I_1$]",
              definition + r"\begin{theorem}[Logarithmic multiplicities over $IV^*+III+I_1$]",
              "D14", "mapsIII:def:two-finite-fibre-marking; maps:src:D.2.5",
              "Create a real section and first profile subsection, placing the complete named marking before its first theorem use. Every matrix entry and ordered lattice vector is preserved.")
    e.replace("Consider the $IV^*,III,I_1$ configuration with its rank-two Mumford\nfilling, and the logarithmic data of",
              "Use the marking of Definition~\\ref{mapsIII:def:two-finite-fibre-marking}\nfor the $IV^*,III,I_1$ configuration, its rank-two Mumford filling,\nand the logarithmic data of",
              "D13", "maps:src:D.2.5",
              "Bind the theorem's delta and u_i to the complete preceding numbered marking.")
    e.replace(r"\gcd(n_i,m_i)=1,\qquad k,\ell>0.",
              r"\gcd(n_i,m_i)=1,\qquad k,\ell\in\mathbb Z_{>0}.",
              "D26", "maps:src:D.2.5",
              "State explicitly the positive-integer root degrees used throughout the admitted construction and comparison; the full unbounded domain is retained.")
    e.replace("We next retain the degree-one kernel in Mayer--Vietoris.",
              "We next compute the degree-one kernel in Mayer--Vietoris.",
              "D08", "maps:src:D.2.5",
              "Introduce the actual kernel calculation with its mathematical action; all P=0 and P!=0 maps remain unchanged.")
    old_note = "The logarithmic quotient and its marked local filling are those of \\cite[Proposition~2.3]{manViaclovskyLogs26}; the original integral homology case is \\cite[Proposition~4.1]{manViaclovskyLogs26}. The unrestricted determinant and torsion calculation above retains the complete integer boundary maps."
    new_note = r"""\begin{remark}[The initial logarithmic homology calculation]
\hypertarget{tag-Q109}{}\label{mapsIII:rem:initial-logarithmic-homology}
{\normalfont\scriptsize tag Q109}\par
The local logarithmic quotient is the construction of
\cite[Proposition~2.3]{manViaclovskyLogs26}. The integral homology
of the initial family is calculated in
\cite[Proposition~4.1]{manViaclovskyLogs26};
\cref{maps:src:D.2.5} gives the complete positive-integer
multiplicities and both determinant cases in the same marking.
\end{remark}"""
    e.replace(old_note, new_note, "D13", "mapsIII:rem:initial-logarithmic-homology",
              "Turn the source-credit paragraph into a numbered mathematical remark, retaining the Proposition 4.1 attribution and replacing the instruction to retain data by the precise range and determinant cases already proved.")
    e.replace(r"\begin{theorem}[infinitely many orders for $III^*+3I_1$]",
              "\\subsection{The $III^*+3I_1$ profile}\n\n" + r"\begin{theorem}[Logarithmic multiplicities over $III^*+3I_1$]",
              "D14", "maps:src:D.2.6",
              "Give the second construction and its entire integral proof a separate mathematical subsection and descriptive theorem title.")
    e.replace(r"k>0,\quad n,r\in\mathbb Z,\quad \gcd(n,4k)=1.",
              r"k\in\mathbb Z_{>0},\quad n,r\in\mathbb Z,\quad \gcd(n,4k)=1.",
              "D26", "maps:src:D.2.6",
              "Make the degree-k pullback's full positive-integer domain explicit, as in the admitted comparison; no multiplicity is removed.")
    e.replace(r"\begin{theorem}[all orders $3k$ for Wang's primitive $I_2$ filling]",
              "\\subsection{Wang's primitive $I_2$ filling}\n\n" + r"\begin{theorem}[Logarithmic multiplicities with a primitive $I_2$ filling]",
              "D14", "maps:src:D.2.7",
              "Separate the primitive I2 construction, its complete integer maps and its full 3k range into their own actual subsection.")
    old_note = "The order-three geometric model and its original surgery calculation are given in \\cite[Theorem~7.1 and Appendix~B]{manWang26}. The present comparison retains the primitive $I_2$ period $(2,1)$, which becomes $(1,0)$ under $(x,y)=(v,v^2/z)$; it is not replaced by the zero-weight $I_2$ archival API choice.\n\n"
    e.replace(old_note, "", "D02", "maps:src:D.2.7",
              "Remove the orphan process/API contrast. The exact determinant-one period map and inverse remain in the LX proof, and the known order-three surgery result is cited precisely in the immediately following LY proof.")
    conic_start = e.text.index("\\[\n M_{\\rm conic}=")
    conic_end = e.text.index("\nFor the nonzero class", conic_start)
    conic = e.text[conic_start:conic_end]
    e.replace(conic, "$M_{\\rm conic}$ of Definition~\\ref{mapsIII:def:conic-surgery}.",
              "D13", "maps:src:D.2.8",
              "Move the full conic embedding and oriented framed surgery construction into a numbered definition before the classification theorem; its normal framing and all trace maps are still proved in the theorem's sole proof.")
    conic_definition = (
        "\\subsection{The oriented type of the Wang family}\n\n"
        "\\begin{definition}[Conic surgery]\n"
        "\\hypertarget{tag-Q108}{}\\label{mapsIII:def:conic-surgery}\n"
        "{\\normalfont\\scriptsize tag Q108}\\par\n"
        "The conic-surgery manifold is\n" + conic +
        "\n\\end{definition}\n\n"
    )
    e.replace(r"\begin{theorem}[The oriented type of the simply connected Wang members]",
              conic_definition + r"\begin{theorem}[The oriented type of the simply connected Wang members]",
              "D14", "mapsIII:def:conic-surgery; maps:src:D.2.8",
              "Place the conic model and the complete all-k, all-r oriented classification in a separate subsection immediately after its LX homology prerequisite.")
    e.replace("\\label{maps:src:D.2.8}\nEvery member",
              "\\label{maps:src:D.2.8}\n{\\normalfont\\scriptsize tag 02LY}\\par\nEvery member",
              "D10", "maps:src:D.2.8",
              "Print the preserved 02LY identifier in the same small-tag style as the other statements; its old hyperlink target and label remain exact.")
    e.replace(r"\begin{theorem}[all orders $4k$ in the Liu--Rollenske configuration]",
              "\\subsection{The $III^*+II+I_1$ profile}\n\n" + r"\begin{theorem}[Logarithmic multiplicities over $III^*+II+I_1$]",
              "D14", "maps:src:D.2.9",
              "Give the Liu--Rollenske profile and its complete affine-origin, collar and integral-homology proof their own actual subsection.")
    e.replace("the Liu--Rollenske configuration also answers Viaclovsky's\nQuestion 4 affirmatively. The type-$II$ fibre is unchanged\nin this statement.",
              "the Liu--Rollenske configuration also answers\n\\cite[Question~4, p.~2]{manViaclovskyLogs26} affirmatively.",
              "D11", "maps:src:D.2.9",
              "Remove the repeated type-II scope sentence, already in the construction hypothesis, and use the exact Question 4 citation already supplied by the proof.")
    old_note = "The product type-$II$ cap and the original marked torus monodromy are established in \\cite[Lemma~3.10 and Propositions~3.11, 3.13]{manLR26}. The proof above gives the full indicated $3k$ family in that marking.\n\n"
    e.replace(old_note, "", "D23", "maps:src:D.2.9",
              "Delete the redundant orphan paragraph whose multiplicity 3k is a transcription error: the theorem and construction use 4k. The distinct affine shift q=r-3k and its inverse remain unchanged. All three source locators remain in the proof at the corresponding product and monodromy inputs.")
    issues = e.presentation()
    if issues:
        raise ValueError(issues)
    e.finish(labels=("mapsIII:def:two-finite-fibre-marking", "mapsIII:rem:initial-logarithmic-homology", "mapsIII:def:conic-surgery"),
             tags=("Q107", "Q109", "Q108"))


if __name__ == "__main__":
    main()
