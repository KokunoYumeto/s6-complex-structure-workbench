"""Exact publication edits for the wholly read product/star units."""
import re
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def span(e, start, end):
    if e.text.count(start) != 1 or e.text.count(end) != 1:
        raise ValueError("A wholly read interval boundary is stale or ambiguous")
    a, b = e.text.index(start), e.text.index(end)
    if a >= b:
        raise ValueError("Reversed interval")
    return e.text[a:b]


def main():
    e = Editor("elliptic_product_star", "C8-FND-PRODUCT-STAR-")
    e.replace(r"""\begin{theorem}[Logarithmic families with smooth type $S^2\times S^4$]\hypertarget{tag-02KP}{}\label{maps:src:D.2.15}
""", r"""\subsection{Logarithmic families with smooth type $S^2\times S^4$}

\begin{definition}[The two-component OS56 family]
\hypertarget{tag-Q119}{}\label{mapsIII:def:two-component-os56}
{\normalfont\scriptsize tag Q119}\par
""", "D13", "maps:src:D.2.15",
              "Give the precise input family a numbered definition before its homology/smooth-type theorem, in its own actual subsection.")
    e.replace(r"""two-component toroidal filling there, the original primitive one-node
fillings at $I_5,I_3$, and the logarithmic filling at $II$ with
""", r"""two-component toroidal filling there, the primitive one-node
fillings at $I_5,I_3$, and the logarithmic filling at $II$.
In the period convention of Definition~\ref{mapsIII:def:elliptic-marked-data}, take
""", "D20", "mapsIII:def:two-component-os56",
              "Point the period symbols to their numbered common definition and specify the same three filling types directly.")
    e.replace(r""" k>0,\quad \gcd(n,6k)=1,\quad r\in\mathbb Z.
""", r""" k\in\mathbb Z_{>0},\quad n,r\in\mathbb Z,\quad \gcd(n,6k)=1.
""", "D26", "mapsIII:def:two-component-os56",
              "Make all established positive and signed integer parameter domains explicit; the complete proof already covers exactly this range.")
    e.replace("The resulting compact smooth threefold has\n", r"""\end{definition}

\begin{theorem}[Logarithmic families with smooth type $S^2\times S^4$]
\hypertarget{tag-02KP}{}\label{maps:src:D.2.15}
{\normalfont\scriptsize tag 02KP}\par
The compact smooth threefold of Definition~\ref{mapsIII:def:two-component-os56} has
""", "D10", "maps:src:D.2.15",
              "Restore the complete theorem after its input definition and print its small permanent tag.")
    e.replace(r"""\begin{theorem}[Original odd-star fillings and all regular logs]
\hypertarget{tag-02KQ}{}\label{maps:src:D.2.16}
Take one of the following marked configurations:
""", r"""\subsection{Odd-star fillings and regular logarithmic transformations}

\begin{definition}[The two odd-star families]
\hypertarget{tag-Q120}{}\label{mapsIII:def:odd-star-logarithmic-data}
{\normalfont\scriptsize tag Q120}\par
Take one of the following marked configurations, with generator $G$
and the period convention of Definition~\ref{mapsIII:def:elliptic-marked-data}:
""", "D13", "maps:src:D.2.16",
              "Give the two exact star profiles, rank parameter and full logarithmic data a numbered definition and their own subsection.")
    e.replace(r"""regular fibre perform a free log of order $m>0$ with vector
$v=a e_1+b'e_2+c\delta+n\gamma$, where
$\gcd(m,a,b',c,n)=1$. Put
""", r"""regular fibre perform a logarithmic transformation of order
$m\in\mathbb Z_{>0}$ with vector
$v=a e_1+b'e_2+c\delta+n\gamma$, where
$a,b',c,n\in\mathbb Z$ and $\gcd(m,a,b',c,n)=1$. Put
""", "D26", "mapsIII:def:odd-star-logarithmic-data",
              "State every positive/signed integer range and the actual freeness condition explicitly, with the mathematical operation named in full.")
    e.replace("For $n\\ne0$ the integral groups are\n", r"""\end{definition}

\begin{theorem}[Homology and smooth types of the odd-star families]
\hypertarget{tag-02KQ}{}\label{maps:src:D.2.16}
{\normalfont\scriptsize tag 02KQ}\par
For the family of Definition~\ref{mapsIII:def:odd-star-logarithmic-data},
the logarithmic action is free. For $n\ne0$ the integral groups are
""", "D10", "maps:src:D.2.16",
              "Keep the full homology and oriented classification assertion after its definition, with a descriptive title and permanent small tag.")
    e.replace(r"""Here the spin Smale manifold $N_m$ and the precisely framed twisted
suspension are those of \ref{maps:src:D.2.14}. In particular
""", r"""Here $N_m$ and its directed twisted suspension are those of
Definition~\ref{mapsIII:def:twisted-smale-suspension}. In particular
""", "D06", "maps:src:D.2.16",
              "Use the actual numbered model definition now preceding the theorem.")
    e.replace(r"""Write $\Lambda=\mathbb Z\langle e_1,e_2,\delta,\gamma\rangle$,
$\chi=\gamma^*$, and
$J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.
The positive $\gamma$ period is the contracting linearization, whose
map on the elliptic surface is translation by $-Q$. A positive base
meridian is denoted by $x_i$. We orient fibre products fibre first
and use the complex orientation of $X$.
""", r"""In the period convention of Definition~\ref{mapsIII:def:odd-star-logarithmic-data},
write $\chi=\gamma^*$ and
$J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.
Denote a positive base meridian by $x_i$. We orient fibre products
fibre first and use the complex orientation of $X$.
""", "D20", "maps:src:D.2.16",
              "Use the single numbered period convention while preserving every orientation needed by the star, normal and transfer maps.")
    old = span(e, "Multiplication by $p$ kills the stated component residues, so $P$ is\n", "The narrow\nheight formula gives $P.O=p/2-1$")
    new = r"""Multiplication by $p$ kills the stated component residues, so $P$ is
narrow at every fibre. Proposition~\ref{maps:src:D.2.19}, with
$(P,Q)=(pG,G)$ and $\langle P,Q\rangle=p(1/p)=1$, identifies
$\operatorname{Hom}(t_Q^*M,M)$ with the pullback of the degree-one
base line. Its multiplication by the specified divisor/base functions
and inverse multiplication by their reciprocals preserve this marking.
Choose the base section with its sole simple zero at $I_1^\bullet$
and multiply it by a sufficiently small constant to make it contracting.
"""
    e.replace(old, new, "D12", "maps:src:D.2.16",
              "Use the earlier whole-fibre line criterion for this exact narrow pair and marker, with its actual function/inverse maps, instead of repeating its height/intersection proof.")
    old = span(e, "Put $d_1=\\gcd(m,n,a,b')$ and $d_2=\\gcd(m,n,p,c)$. A prime\n", "For literal quotient maps, keep the integer row and column operations\n")
    new = r"""The coefficient map
\[
 \mathbb Z[p,m,n,a,b,c]\longrightarrow\mathbb Z[m,n,a,b',c],
 \qquad b\longmapsto b',\quad p\longmapsto4\text{ or }12
\]
carries the transfer and source relation in
\eqref{maps:eq:D.S7} to $R$ and $q_0$ here, in the same ordered
free source and target bases. The letter change $b\leftrightarrow b'$
is inverted by the reverse change. The prime-local calculation in
the proof of Theorem~\ref{maps:src:D.2.13} uses only integrality of
$p$, $m>0$ and the five-entry freeness condition. Its pivot identities
therefore specialize under this coefficient map. At each prime the
same unit cases are exhaustive, and the inverse row additions,
permutations and reciprocal units remain defined.

Put $d_1=\gcd(m,n,a,b')$ and $d_2=\gcd(m,n,p,c)$.
A common prime divisor would divide all five entries of the freeness
condition, so $\gcd(d_1,d_2)=1$ and $t=d_1d_2$ divides $m,n$.
The resulting determinantal divisors are
\[
 1,\quad t,\quad mt,\quad m^2|n|.
\]
Thus the Smith entries are $(1,t,m,m|n|/t)$ for $n\ne0$ and
$(1,t,m,0)$ for $n=0$. Expanding the five signed maximal minors
also gives the polynomial identity
$m^2n(-a,-b',-c,-n,m)$.
"""
    e.replace(old, new, "D12", "maps:src:D.2.16",
              "The full R/q0 matrices and exact coefficient specialization identify the duplicated Smith calculation with KN's all-integer pivot argument. The map, unit-case hypotheses, endpoint and all original factors/maximal minors remain explicit; no geometric identification of different families is asserted.")
    old = span(e, "The exact cusp matrix $H_3$ identifies $\\delta$ with $(0,1)$ in\n", "The canonical line on the star has a holomorphic trivialization.\n")
    new = r"""The cusp angular map and its inverse are
\[
 H_3(x,0,y,0)\longmapsto(x,y),\qquad
 (x,y)\longmapsto H_3(x,0,y,0).
\]
They carry $\delta$ to $(0,1)$ and the full primitive short lattice
to $\mathbb Z^2$. The corresponding character maps, fixing the base
coordinate, identify the triangle cones with those used in the
fixed-curve calculation of Theorem~\ref{maps:src:D.2.14}.
Their inverse character maps extend on the same affine charts.
The complete period group acts by translations of this fan, with
its nonzero unit factors unchanged. That calculation therefore gives
one fixed curve $C\simeq\mathbb P^1$ and trivial stabilizers elsewhere.

In these characters the two adjacent normal charts have transition
$(x',y',w')=(wx,wy,w^{-1})$, with inverse
$(x,y,w)=(w'x',w'y',(w')^{-1})$. Thus the normal bundle is exactly
\eqref{maps:eq:D.S11}. The positive rescaling, negative-weight
conjugation and displayed $SU(2)$ map $U$ in that proof, inverted by
division, conjugation and $U^*$, respectively, supply the scalar
normal framing here. Reverse the core parametrization together with
the negative-weight conjugation, preserving the complex orientation.
The invariant normal exponential and its inverse identify the
neighbourhood with $C\times D^4$ carrying scalar multiplication.

"""
    e.replace(old, new, "D12", "maps:src:D.2.16",
              "Use the already proved primitive fan/normal calculation through the exact H3 angular maps and inverse character maps. Keep the actual transition, all unit factors, the oriented framing and its explicit inverse operations; remove only their repeated derivation.")
    e.replace("The normal push-off also maps under $\\Theta$ to\n$[C_Q]=0$. Hurewicz makes the parametrized sphere nullhomotopic.\n",
              "Hurewicz makes the parametrized sphere nullhomotopic.\n",
              "D12", "maps:src:D.2.16",
              "Keep the complete specialization/ns argument for the fixed curve and remove its second proof via the already established quotient push-off; that map remains in the admitted comparison.")
    # The last proof terminator is selected only after its wholly read unique paragraph.
    start = "Finally, when $m=1$, the model with $Q=S^5$ maps to\n"
    a = e.text.index(start)
    b = e.text.index("\\end{proof}\n", a)
    old = e.text[a:b]
    new = r"""For $m=1$, Definition~\ref{mapsIII:def:twisted-smale-suspension}
has $N_1=S^5$. The oriented boundary map, its inverse and radial
projection in Theorem~\ref{maps:src:D.2.14} identify
$\widetilde\Sigma_0N_1$ with $S^6$ in this same directed gluing
convention. Removing this connected summand uses the oriented disc
identification, inverted by inserting the same disc. This gives the
stated $m=1$ specialization.
"""
    e.replace(old, new, "D12", "maps:src:D.2.16",
              "Use KO's exact oriented m=1 boundary map in the same directed model and retain the inverse disc operation for the distinct connected-sum specialization.")
    e.replace("onto their orthogonal complement is inverted by adding the recorded\ncoefficients. Repetition gives pairs $A_i,B_i$, with inverse maps\n",
              "onto their orthogonal complement is inverted by adding these two\nintersection coefficients. Repetition gives pairs $A_i,B_i$, with inverse maps\n",
              "D08", "maps:src:D.2.16",
              "Name the actual two intersection coefficients in the inverse map.")
    for old, new, owner in [
        (r"\cite[Theorem 5]{manZhubr75}", r"\cite[Theorem 5, p.~796]{manZhubr75}", "maps:src:D.2.15"),
        (r"Theorem 3 and the middle-surgery construction in"+"\n"+r"\cite[\S4.1]{manZhubr75}", r"Theorem~3, p.~795, and the middle-surgery construction in"+"\n"+r"\cite[\S4.1, p.~809]{manZhubr75}", "maps:src:D.2.15"),
        (r"\cite[\S2.4 and Proposition 3.5(1),(3)]{manUU21}", r"\cite[\S2.4, pp.~6--7; Proposition~3.5(1),(3), pp.~8--10]{manUU21}", "maps:src:D.2.16"),
        (r"\cite[\S\S7.6--7.7]{manSS10}", r"\cite[\S\S7.6--7.7, pp.~33--34]{manSS10}", "maps:src:D.2.16"),
        (r"\cite[Theorem B(2) and Proposition 5.6]{manGR25}", r"\cite[Theorem~B(2), p.~3; Proposition~5.6, pp.~22--23]{manGR25}", "maps:src:D.2.16"),
    ]:
        e.replace(old, new, "D18", owner,
                  "Supply the printed page of the exact existing result after opening the primary version and reading the cited statement/proof scope; no bibliography identity is inferred from a similar title.")
    kinds = {
        "mapsD:repair:collision-realization": "Theorem",
        "maps:src:D.2.19": "Proposition",
        "maps:src:D.2.12": "Theorem",
        "maps:src:D.1.2": "Theorem",
        "maps:src:D.2.47": "Theorem",
        "maps:src:D.2.13": "Theorem",
        "maps:src:D.2.14": "Theorem",
    }
    # Every owner/kind above was inspected, and each context becomes its own exact defect row.
    for label, kind in kinds.items():
        token = r"\ref{" + label + "}"
        for match in reversed(list(re.finditer(re.escape(token), e.text))):
            if e.text[:match.start()].endswith(kind + "~"):
                continue
            lo = max(0, match.start() - 90)
            hi = min(len(e.text), match.end() + 90)
            old = e.text[lo:hi]
            if e.text.count(old) != 1:
                raise ValueError("Nonunique reference context")
            offset = match.start() - lo
            new = old[:offset] + kind + "~" + old[offset:]
            owner = "maps:src:D.2.16" if match.start() > e.text.index(r"\label{maps:src:D.2.16}") else "maps:src:D.2.15"
            e.replace(old, new, "D04", owner,
                      "Print the inspected statement kind and generated number at this exact reference; preserve its permanent label.")
    issues = e.presentation()
    if issues:
        raise ValueError(issues)
    e.finish(labels=("mapsIII:def:two-component-os56", "mapsIII:def:odd-star-logarithmic-data"), tags=("Q119", "Q120"))


if __name__ == "__main__":
    main()
