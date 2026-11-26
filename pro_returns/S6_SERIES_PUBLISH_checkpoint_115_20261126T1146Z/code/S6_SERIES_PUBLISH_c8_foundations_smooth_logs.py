"""Publish the two wholly read smooth-log units in the owned fragment."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("elliptic_smooth_logs", "C8-FND-SMOOTH-")
    old = r"""\begin{theorem}[Smooth logarithmic modifications in four elliptic families]\hypertarget{tag-02KN}{}\label{maps:src:D.2.13}


Consider the following four marked rational elliptic surfaces,
with $G$ a Mordell--Weil generator:
"""
    new = r"""\subsection{Integral homology of smooth logarithmic modifications}

\begin{definition}[Four semistable logarithmic data]
\hypertarget{tag-Q117}{}\label{mapsIII:def:smooth-logarithmic-data}
{\normalfont\scriptsize tag Q117}\par
Use the four marked rational elliptic surfaces constructed from
rows $1,2,4,6$ of the Weierstrass models in the proof of
Theorem~\ref{maps:src:D.2.12}, with $G$ a Mordell--Weil generator:
"""
    e.replace(old, new, "D13", "maps:src:D.2.13",
              "Give the common four-profile construction a numbered definition before the homology theorem, with its exact one-way KM prerequisite and its own actual subsection.")
    e.replace(r"""Use $P=pG$, $Q=G$, and the degree-one linearization with zero
at $I_1^\bullet$. Keep the original four primitive one-node
fillings and the one-component hexagonal cusp. At an additional
smooth fibre, perform the logarithmic transformation of order
""", r"""Use $P=pG$, $Q=G$, and the degree-one linearization with zero
at $I_1^\bullet$. Fill the four unmarked singular fibres with
primitive one-node neighbourhoods and $I_1^\bullet$ with a
one-component hexagonal cusp. In the period lattice
$\Lambda=\mathbb Z\langle e_1,e_2,\delta,\gamma\rangle$,
$\delta$ is the positive line circle and $\gamma$ is the forward
period of the linearization covering $-Q$.
At an additional smooth fibre, perform the logarithmic transformation of order
""", "D20", "mapsIII:def:smooth-logarithmic-data",
              "Place the single period convention beside the full parameter input and specify which of the five fibres receives each geometric filling; preserve every filling and its marked position.")
    e.replace("The five-entry gcd is the freeness condition. Put\n", "Put\n",
              "D13", "mapsIII:def:smooth-logarithmic-data",
              "Move the proved freeness assertion to the following theorem, while retaining the five-entry gcd as the defining parameter condition.")
    e.replace(r"""The two factors in \eqref{maps:eq:D.S2} are coprime, and $t\mid m$.
""", r"""\end{definition}

\begin{theorem}[Homology of the four smooth logarithmic families]
\hypertarget{tag-02KN}{}\label{maps:src:D.2.13}
{\normalfont\scriptsize tag 02KN}\par
The logarithmic transformation of
Definition~\ref{mapsIII:def:smooth-logarithmic-data} is free.
The two factors in \eqref{maps:eq:D.S2} are coprime, and $t\mid m$.
""", "D10", "maps:src:D.2.13",
              "Restore the same theorem identity after its numbered input definition and print only the small permanent tag; freeness is now stated with the proved conclusions.")
    e.replace(r"""Put $\Lambda=\mathbb Z\langle e_1,e_2,\delta,\gamma\rangle$,
$\chi=\gamma^*$ and $J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.
The period $\delta$ is the positive line circle, and $\gamma$ is the
forward period of the linearization covering $-Q$.
""", r"""In the marking of Definition~\ref{mapsIII:def:smooth-logarithmic-data},
put $\chi=\gamma^*$ and
$J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.
""", "D20", "maps:src:D.2.13",
              "Refer to the single unchanged period definition instead of repeating it in the proof.")
    e.replace("The two fibres are $I_2$ and $I_1$. Every old simple root continues;\n",
              "The two fibres are $I_2$ and $I_1$. Every simple root of $\\Delta_0$ continues;\n",
              "D23", "maps:src:D.2.13",
              "Identify the polynomial whose simple roots continue under the displayed deformation.")
    e.replace("formula for $T_i$ above. One may construct every inverse without\nchoosing a rational complement: for integer coefficients $a_I$ with\n",
              "formula for $T_i$ above. To construct the integral inverse, choose\ninteger coefficients $a_I$ with\n",
              "D02", "maps:src:D.2.13",
              "State the actual minor-adjugate construction positively; the integral maps and their proofs are unchanged.")
    e.replace(r"""$H_3=\mathbb Z^2\oplus\mathbb Z/t\oplus\mathbb Z/m$
with no unspecified extension.
""", r"""$H_3=\mathbb Z^2\oplus\mathbb Z/t\oplus\mathbb Z/m$
with the displayed free-coordinate and torsion-linking inverse maps.
""", "D02", "maps:src:D.2.13",
              "Name the complete inverse splitting maps actually proved instead of a defensive closing clause.")
    old = r"""\begin{theorem}[the twisted Smale suspension]\hypertarget{tag-02KO}{}\label{maps:src:D.2.14}
Let $N_m$ be the closed simply connected spin five-manifold with
"""
    new = r"""\subsection{Twisted suspensions and oriented smooth types}

\begin{definition}[Twisted Smale suspension]
\hypertarget{tag-Q118}{}\label{mapsIII:def:twisted-smale-suspension}
{\normalfont\scriptsize tag Q118}\par
For a positive integer $m$, let $N_m$ be the closed simply connected
spin five-manifold with
"""
    e.replace(old, new, "D13", "maps:src:D.2.14",
              "Give the five-manifold and exact directed gluing construction their numbered definition before the smooth-classification statement, in a separate actual subsection.")
    e.replace(r"""\cite[Definition 5.1, p.~17]{manGR25}.
Every simply connected member of the four families in
\ref{maps:src:D.2.13}, with $m\geq1$ and $n=\pm1$, is oriented
""", r"""\cite[Definition 5.1, p.~17]{manGR25}.
\end{definition}

\begin{theorem}[Oriented smooth types of the four semistable families]
\hypertarget{tag-02KO}{}\label{maps:src:D.2.14}
{\normalfont\scriptsize tag 02KO}\par
Every simply connected member of the four families in
Theorem~\ref{maps:src:D.2.13}, with $m\geq1$ and $n=\pm1$, is oriented
""", "D10", "maps:src:D.2.14",
              "Keep the whole original smooth-type assertion after its definition, with a descriptive title and the permanent small tag.")
    e.replace(r"""By \ref{maps:src:D.2.13}, $X$ is simply connected and
""", r"""By Theorem~\ref{maps:src:D.2.13}, $X$ is simply connected and
""", "D04", "maps:src:D.2.14", "Print the kind and generated number of the homology prerequisite.")
    e.replace(r"""The integral local model in
\ref{maps:src:D.2.13} gives
""", r"""The integral local model in
Theorem~\ref{maps:src:D.2.13} gives
""", "D04", "maps:src:D.2.14", "Resolve the primitive local model to the preceding theorem by kind and label.")
    e.replace(r"""Consequently $\delta=(0,1)$ in the angular marking of the
primitive triangular cusp of \ref{maps:src:D.2.6}.
""", r"""Consequently $\delta=(0,1)$ in the angular marking of the
primitive triangular cusp in Theorem~\ref{maps:src:D.2.6},
with the fan and period quotient of
Definition~\ref{mapsIII:def:triangular-cusp}.
""", "D14", "maps:src:D.2.14",
              "Name the earlier actual primitive cusp and its common fan/period definition before the fixed-curve calculation; the full H and multiplicative inverse maps remain immediately before this use.")
    issues = e.presentation()
    if issues:
        raise ValueError(issues)
    e.finish(labels=("mapsIII:def:smooth-logarithmic-data", "mapsIII:def:twisted-smale-suspension"), tags=("Q117", "Q118"))


if __name__ == "__main__":
    main()
