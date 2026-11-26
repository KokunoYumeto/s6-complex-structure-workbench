"""Final corrections found by the complete edited logarithmic-family reread."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("elliptic_basic_families", "III-C8-FND-BASIC-FINAL-")
    e.replace("In the marking of Definition~\\ref{mapsIII:def:two-finite-fibre-marking},\nThus $A_0A_1A_\\infty=I$",
              "In the marking of Definition~\\ref{mapsIII:def:two-finite-fibre-marking},\n$A_0A_1A_\\infty=I$",
              "D23", "maps:src:D.2.5",
              "Correct the sentence join after moving the named marking; the complete matrix identity is unchanged.")
    e.replace(r"Every member of \ref{maps:src:D.2.7} with",
              r"Every member of \cref{maps:src:D.2.7} with",
              "D23", "maps:src:D.2.8",
              "Print the theorem cross-reference with its statement kind.")
    e.replace("Let $\\Gamma\\subset\\mathbb{CP}^3$ be the conic in the statement.",
              "Let $\\Gamma\\subset\\mathbb{CP}^3$ be the conic of\nDefinition~\\ref{mapsIII:def:conic-surgery}.",
              "D13", "maps:src:D.2.8",
              "Update the sole surgery proof to the numbered definition that now owns the complete embedding and framing choice.")
    lw = r"""Negating the relative source generators and replacing $t$
by $-t$ gives the exact alternative coordinate matrix
\[
 \begin{pmatrix}1&0\\0&-1\end{pmatrix}
 B_+(-I_2)
 =\begin{pmatrix}n&-2r\alpha\\0&1\end{pmatrix}.
\]
Both source and target changes are integral involutions.
"""
    e.replace(lw, "", "D20", "maps:src:D.2.6",
              "Keep positive geometric normal circles throughout the LW proof; move the complete alternative signed-coordinate conversion into the following numbered remark.")
    lw_remark = r"""\begin{remark}[Signed coordinates for the $III^*+3I_1$ boundary map]
\hypertarget{tag-Q111}{}\label{mapsIII:rem:iii-star-boundary-orientation}
{\normalfont\scriptsize tag Q111}\par
In the finite boundary calculation of \cref{maps:src:D.2.6}, choose
$m\alpha+n\beta=1$. The positive geometric matrix is
$B_+=\left(\begin{smallmatrix}-n&2r\alpha\\0&1\end{smallmatrix}\right)$.
""" + lw + r"""The source map negates both relative generators; the target map fixes
the fibre class $s$ and negates its peripheral sweep $t$. Each map
is its own inverse.
\end{remark}

"""
    e.replace("\\subsection{Wang's primitive $I_2$ filling}\n", lw_remark+"\\subsection{Wang's primitive $I_2$ filling}\n",
              "D20", "mapsIII:rem:iii-star-boundary-orientation",
              "Preserve the exact signed matrix relation with named source and target involutions in a numbered conversion remark; the main proof uses only its positive geometric convention.")
    lx = r"""Negating both relative generators and replacing $t$ by
$-t$ gives the exact alternative convention
\[
 \operatorname{diag}(1,-1)\,B_+(-I_2)
 =\begin{pmatrix}-2n&-6r\alpha\\0&1\end{pmatrix}.
\]
Both changes are integral involutions.
"""
    e.replace(lx, "", "D20", "maps:src:D.2.7",
              "Keep the LX proof in its positive normal-circle convention, relocating the complete signed-coordinate comparison to a numbered remark.")
    lx_remark = r"""\begin{remark}[Signed coordinates for the primitive $I_2$ boundary map]
\hypertarget{tag-Q112}{}\label{mapsIII:rem:wang-boundary-orientation}
{\normalfont\scriptsize tag Q112}\par
In the finite boundary calculation of \cref{maps:src:D.2.7}, choose
$3k\alpha+n\beta=1$. The positive geometric matrix is
$B_+=\left(\begin{smallmatrix}2n&6r\alpha\\0&1\end{smallmatrix}\right)$.
""" + lx + r"""The source map negates both relative generators; the target map fixes
$s=[e_1\wedge e_2]$ and negates $t$. The reverse maps are the same
two involutions.
\end{remark}

"""
    e.replace("\\subsection{The oriented type of the Wang family}\n", lx_remark+"\\subsection{The oriented type of the Wang family}\n",
              "D20", "mapsIII:rem:wang-boundary-orientation",
              "Give the complete source and target morphisms, with their inverses, for the second normal-circle convention in its own numbered conversion remark.")
    e.finish(labels=("mapsIII:rem:iii-star-boundary-orientation", "mapsIII:rem:wang-boundary-orientation"), tags=("Q111", "Q112"))


if __name__ == "__main__":
    main()
