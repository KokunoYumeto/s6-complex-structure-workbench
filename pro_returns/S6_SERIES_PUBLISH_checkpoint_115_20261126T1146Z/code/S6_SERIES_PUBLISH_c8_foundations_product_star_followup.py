"""Exact local follow-ups found in the full KP/KQ edited readback."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("elliptic_product_star", "C8-FND-PRODUCT-STAR-FOLLOW-")
    e.replace(r"""Set $P=pG$, $Q=G$, and place the degree-one linearization zero at
$I_1^\bullet$. Use the original $I_j^*$ filling, the primitive
""", r"""Set $P=pG$, $Q=G$ and $M=\mathcal O(P-O)$, and place the
degree-one linearization zero at $I_1^\bullet$. Use the original
$I_j^*$ filling, the primitive
""", "D05", "mapsIII:def:odd-star-logarithmic-data",
              "Name the line M in the numbered input definition before the consolidated whole-fibre linearization argument uses it.")
    e.replace(r""" \quad(n\ne0).
\]
\end{definition}

\begin{theorem}[Homology and smooth types of the odd-star families]
""", r""" \quad(n\ne0).
\]
For $n=0$ write $\mathcal T=\mathbb Z/t\oplus\mathbb Z/m$.
\end{definition}

\begin{theorem}[Homology and smooth types of the odd-star families]
""", "D13", "mapsIII:def:odd-star-logarithmic-data",
              "Place the named zero-parameter torsion group in the same numbered definition as the nonzero-parameter group.")
    e.replace(r"For $n=0$, put $\mathcal T=\mathbb Z/t\oplus\mathbb Z/m$; then",
              r"For $n=0$ the integral groups are", "D13", "maps:src:D.2.16",
              "Use the preceding numbered torsion-group definition in the theorem without an embedded second definition.")
    edits = [
        (r"The free quotient is \`etale, so the order", r"The free quotient is \'etale, so the order", "maps:src:D.2.15"),
        ("The narrow\nheight formula gives", "The narrow height formula gives", "maps:src:D.2.16"),
        ("trivial. Explicitly remove the integral Cech cocycle of its transition", r"trivial. Explicitly remove the integral \v{C}ech cocycle of its transition", "maps:src:D.2.16"),
        ("Successive two-row Bezout operations give", r"Successive two-row B\'ezout operations give", "maps:src:D.2.16"),
        ("A Bezout preimage $z_f$ of one is a section.", r"A B\'ezout preimage $z_f$ of one is a section.", "maps:src:D.2.16"),
        ("then $B_1$ with $I(A_1,B_1)=1$ by Bezout.", r"then $B_1$ with $I(A_1,B_1)=1$ by B\'ezout.", "maps:src:D.2.16"),
        ("entire punctured quotient. The Cech logarithm and partition-of-unity", r"entire punctured quotient. The \v{C}ech logarithm and partition-of-unity", "maps:src:D.2.16"),
        (r"model of Theorem~\ref{maps:src:D.2.14}. Their Cech cocycles give an", r"model of Theorem~\ref{maps:src:D.2.14}. Their \v{C}ech cocycles give an", "maps:src:D.2.16"),
    ]
    for old, new, label in edits:
        e.replace(old, new, "D23", label,
                  "Correct the exact accent or line join found while reading this proof in full; mathematical maps and scope are unchanged.")
    e.replace(r"""Theorem~3, p.~795, and the middle-surgery construction in
\cite[\S4.1, p.~809]{manZhubr75} then give an oriented diffeomorphism
""", r"""The classification and middle-surgery construction in
\cite[Theorem~3, p.~795; \S4.1, p.~809]{manZhubr75}
give an oriented diffeomorphism
""", "D18", "maps:src:D.2.15",
              "Attach the primary-source theorem and printed-page locators to the citation that supplies the classification; both locations were read in the opened English primary text.")
    e.finish()


if __name__ == "__main__":
    main()
