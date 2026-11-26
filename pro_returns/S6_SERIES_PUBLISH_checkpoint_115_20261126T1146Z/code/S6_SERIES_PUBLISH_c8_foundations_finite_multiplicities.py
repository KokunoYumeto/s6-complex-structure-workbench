"""Exact edits after complete KK/KL source reading and the admitted KK comparison."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("elliptic_finite_multiplicities", "III-C8-FND-FINITE-")
    inputs_start = e.text.index("Fix positive integers $R,k,l$.")
    inputs_end = e.text.index("For integers $n_j,r_j$", inputs_start)
    inputs = e.text[inputs_start:inputs_end]
    e.replace(inputs, "For the marked data of Definition~\\ref{mapsIII:def:yang-finite-data},\n",
              "D13", "maps:src:D.2.10",
              "Move the complete Type B/C table, positive integer parameters, lattice and ell_1 into a numbered definition before use; no input or ordering is changed.")
    matrix_start = e.text.index("In the stated marking the finite deck\nmatrices and forward transports are\n")
    matrix_end = e.text.index("Their orders are $d,6$", matrix_start)
    matrices = e.text[matrix_start:matrix_end]
    e.replace(matrices, "", "D13", "maps:src:D.2.10",
              "Place the two complete finite deck matrices and inverse transports with the common marked data used by KK and the following Type C specialization; their order and fixed-lattice proof remains here.")
    e.replace("We use clockwise meridians. Their orders are $d,6$",
              "We use clockwise meridians. The matrices $A_1,A_2$ of\nDefinition~\\ref{mapsIII:def:yang-finite-data} have orders $d,6$",
              "D13", "maps:src:D.2.10",
              "Bind the proof to the preceding complete matrices after their relocation.")
    definition = (
        "\\subsection{Finite multiplicities in Yang's two families}\n\n"
        "\\begin{definition}[Marked Type B and Type C data]\n"
        "\\hypertarget{tag-Q113}{}\\label{mapsIII:def:yang-finite-data}\n"
        "{\\normalfont\\scriptsize tag Q113}\\par\n" + inputs + "\n" + matrices +
        "\\end{definition}\n\n"
    )
    e.replace("\\begin{theorem}[Finite multiplicities in the two Yang families]\n",
              definition+"\\begin{theorem}[Finite multiplicities in the two Yang families]\n",
              "D14", "mapsIII:def:yang-finite-data; maps:src:D.2.10",
              "Create a genuine complete subsection for the two Yang families and place their shared marking before the theorem.")
    e.replace("\\label{maps:src:D.2.10}\nFor the marked data", "\\label{maps:src:D.2.10}\n{\\normalfont\\scriptsize tag 02KK}\\par\nFor the marked data",
              "D10", "maps:src:D.2.10", "Print the retained theorem tag in the common small style.")
    e.replace("For Type B, $P=2$ and $h=\\gcd(R,2)$; the invariant factors\nare those of $\\mathbb Z/R\\oplus\\mathbb Z/2$.",
              "For Type B, $P=2$ and $h=\\gcd(R,2)$. For even $R$,\ninterchanging the two cyclic coordinates identifies\n$\\mathbb Z/2\\oplus\\mathbb Z/R$ with the stated group, and\nthe same interchange is its inverse. For odd $R$, the map\n$[x]_{2R}\\mapsto([x]_R,[x]_2)$ has inverse\n$([a]_R,[b]_2)\\mapsto[2ua+Rvb]_{2R}$, where $2u+Rv=1$.\nBoth composite maps are the identity modulo their indicated orders.",
              "D22", "maps:src:D.2.10",
              "Supply the exact integral isomorphism and inverse between the proved invariant factors and the cited original Type B group for both parities of R, instead of relying on unnamed equality of invariant factors.")

    e.replace(r"\begin{theorem}[all orders $3k$ for $IV^*+II+I_2$]",
              "\\subsection{A component-supported zero on the $IV^*+II+I_2$ profile}\n\n" + r"\begin{theorem}[Logarithmic multiplicities with a component-supported zero]",
              "D14", "maps:src:D.2.11",
              "Give the actual component-supported construction and its complete coprime-cap proof a separate mathematical subsection. Root will settle its possible consolidation with the later P3F.26--29 chain only after exact parameter-map comparison.")
    surface_start = e.text.index("The rational elliptic surface\n")
    surface_end = e.text.index("has fibres $IV^*,II,I_2$", surface_start)
    surface = e.text[surface_start:surface_end]
    e.replace(surface, "The surface of Definition~\\ref{mapsIII:def:os49-component-zero}\n",
              "D13", "maps:src:D.2.11",
              "Move the explicit Weierstrass model and marked section before the theorem into a numbered construction definition; retain the theorem's fibre and generator assertions for proof.")
    additional = "Put $M=\\mathcal O(P-O)$ and\n$Q=3P$. Let $C_0$ be the identity component of the $I_2$ fibre.\n"
    e.replace(additional, "", "D13", "maps:src:D.2.11",
              "Move the named section line, translated section and zero component into the same numbered model definition.")
    surface = surface.replace("The rational elliptic surface\n", "Let $f:S\\to\\mathbb P^1$ be the minimal regular model of\n", 1)
    definition = (
        "\\begin{definition}[A component-supported elliptic datum]\n"
        "\\hypertarget{tag-Q114}{}\\label{mapsIII:def:os49-component-zero}\n"
        "{\\normalfont\\scriptsize tag Q114}\\par\n" + surface +
        "Write $O$ for its zero section, put $M=\\mathcal O(P-O)$ and\n"
        "$Q=3P$, and let $C_0$ be the component met by $O$ in the fibre\n"
        "over infinity.\n\\end{definition}\n\n"
    )
    e.replace(r"\begin{theorem}[Logarithmic multiplicities with a component-supported zero]",
              definition+r"\begin{theorem}[Logarithmic multiplicities with a component-supported zero]",
              "D13", "mapsIII:def:os49-component-zero",
              "Number the concrete Weierstrass/section/line datum before its existence and homology theorem, preserving the old equation label and tag.")
    e.replace(r"\qquad k>0,\quad n,r\in\mathbb Z,", r"\qquad k\in\mathbb Z_{>0},\quad n,r\in\mathbb Z,",
              "D26", "maps:src:D.2.11",
              "Make the positive-integer pullback degree explicit while retaining the coprimality condition and every signed n and integer r.")
    e.replace("Viaclovsky's Question 4. The linearization is supported on one\n$I_2$ component, so the local-narrowness restriction of the public\nengine does not include this input.",
              "\\cite[Question~4, p.~2]{manViaclovskyLogs26}.",
              "D02", "maps:src:D.2.11",
              "Remove the unneeded API-exclusion comparison and cite the stated published question precisely; the component divisor and its full geometric construction remain explicit.")
    e.replace("\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=*]\n\\item \\emph{The explicit elliptic surface and linearization.}",
              "\\emph{The elliptic surface and component-supported linearization.}",
              "D04", "maps:src:D.2.11",
              "Replace the research-style tagged proof-item sequence by mathematical proof paragraphs, preserving every argument.")
    old = "Its height is $2-4/3-1/2=1/6$. The Shioda--Tate rank is one,\nand OS entry 49 has height lattice $\\langle1/6\\rangle$ and\nno torsion, as checked in \\CompendiumRef{III}{maps:src:D.2.1}; hence $P$ is a generator."
    new = r"""Its height is $2-4/3-1/2=1/6$. The Shioda--Tate formula gives
rank $10-2-6-1=1$. The N\'eron--Severi lattice of this rational
surface has absolute discriminant one, while the trivial lattice
has absolute discriminant $3\cdot2=6$. Let $G$ generate the free
Mordell--Weil quotient, let $t_0$ be the order of its torsion group,
and write $P=sG+T$ with $T$ torsion. The discriminant formula gives
\[
 h(G)=t_0^2/6,\qquad 1/6=h(P)=s^2t_0^2/6.
\]
Thus $|s|=t_0=1$, so $P$ generates the whole Mordell--Weil group.
The rank, unimodularity, height and discriminant identities used here
are \cite[Corollary~6.13; \S8.8; \S\S11.8 and 11.10, (22)]{manSS10}."""
    e.replace(old, new, "D06", "maps:src:D.2.11",
              "Replace the stale compendium pointer by the exact rank-one discriminant argument from the printed surface. The primary Schuett--Shioda v3 text was opened at Corollary 6.13, section 8.8 and sections 11.8/11.10 equation 22; h(P)=1/6 forces both index and torsion order to one. No later catalogue dependency is introduced.")
    e.replace("\\item The section $Q=3P$", "The section $Q=3P$", "D04", "maps:src:D.2.11",
              "Continue the same component-divisor argument as a mathematical paragraph after removing its internal research item number.")
    e.replace("$J\\simeq\\mathcal O(C_0)$, supplying the asserted effective\nlinearization. Its norm under the component exchange has divisor",
              r"""$J\simeq\mathcal O(C_0)$. The line isomorphism can be given explicitly.
Put $D=P-O-(P-Q)+(-Q)$. On the generic cubic, the line through
$P,-Q$ divided by the vertical line through $P-Q$ has divisor $D$.
The resulting rational function $F$ on $S$ has
$\operatorname{div}(F)=D+V$ with $V$ vertical. The multidegrees
above imply $V+C_0=\sum a_vF_v$, and the intersection with $O$
gives $\sum a_v=0$. Choose a rational base function $B$ with
divisor $\sum a_v[v]$. Then
\[
 \rho=F/(B\circ f),\qquad \operatorname{div}(\rho)=D-C_0,
 \qquad
 \mathcal O(D)\xrightarrow{\ \rho\ }\mathcal O(C_0),
 \qquad
 \mathcal O(C_0)\xrightarrow{\ \rho^{-1}\ }\mathcal O(D)
\]
are inverse line maps. Pulling back the canonical section of
$\mathcal O(C_0)$ supplies the effective linearization.
Its norm under the component exchange has divisor""",
              "D22", "maps:src:D.2.11",
              "Give the actual rational-function line map and inverse for the already-proved component divisor. The vertical-fibre correction has degree zero by the existing O-intersection calculation, so the base function exists; no numerical divisor comparison substitutes for the line isomorphism.")
    e.replace("\\item \\emph{Identification with the actual Type C periods.}",
              "\\emph{The Type C period marking.}", "D04", "maps:src:D.2.11",
              "Give the next proof phase its mathematical title without the research item marker.")
    e.replace("normalized $dP_6$ component.", "normalized $dP_6$ component\n\\cite[Appendix~B.4]{manYang26}.",
              "D17", "maps:src:D.2.11",
              "Keep the former closing paragraph's exact cusp source attribution at the local model where it is used.")
    e.replace("\\item An exact integral check of the marking is also available.",
              "The period marking has the following integral comparison.",
              "D08", "maps:src:D.2.11",
              "Introduce the actual period morphism instead of describing it as a check.")
    old = "Then $\\det S=-1$, $U^{-t}S=ST_1$ and $V^{-t}S=ST_2$,\nwhere $T_1,T_2$ are precisely Yang's displayed Type C\ncohomological matrices. This is the finite Hurwitz reorder\nfollowed by an integral change of basis, not merely a rational\ncomparison of eigenvalues."
    new = r"""For the Type C matrices of Definition~\ref{mapsIII:def:yang-finite-data}
at $R=1$, put $T_j=A_j^{-t}$. Direct multiplication gives
$\det S=-1$, $U^{-t}S=ST_1$ and $V^{-t}S=ST_2$. Its inverse is
\[
 S^{-1}=\begin{pmatrix}
 -3&0&0&-1\\-1&-1&1&0\\-1&0&0&0\\0&0&1&0
 \end{pmatrix}.
\]
Thus $S^{-t}$ sends the Type C homology coordinates to the displayed
period coordinates, with inverse $S^t$, and
$US^{-t}=S^{-t}A_1$, $VS^{-t}=S^{-t}A_2$.
The preceding Hurwitz reorder sends the pair $(M_{II},M_{IV})$
to $(U,U^{-1}M_{II}U)$; its inverse sends $(U,V)$ to
$(UVU^{-1},U)$. These maps give the ordered integral comparison."""
    e.replace(old, new, "D20", "maps:src:D.2.11",
              "Replace the unsupported rhetorical contrast by the exact inverse period matrix, homological conjugacies and inverse Hurwitz move. The newly written small symbolic program verified every displayed product and inverse; no historical module was imported.")
    e.replace("\\item \\emph{The unchanged type-$II$ filling with its integral marking.}",
              "\\emph{The product type-$II$ filling and its integral marking.}",
              "D04", "maps:src:D.2.11",
              "Use a mathematical proof-phase heading for the actual product construction.")
    e.replace("with $3P$ in place of its translation section; we check all the\nneeded ingredients.",
              "with translation section $3P$, as the following explicit product\nconstruction shows.",
              "D08", "maps:src:D.2.11",
              "State the role of the ensuing geometric argument directly.")
    old = "The translations extend over the cuspidal cubic and fix its\ncusp. Combining this isotopy with the logarithm of $\\lambda$\ntrivializes the circle-bundle mapping torus of a fundamental\nannulus. Thus this filling is homeomorphic over its base disc\nto $E\\times T^2$, with angular circle $\\delta$ and a primitive\nsecond circle of $\\gamma^*$-value one."
    new = r"""The translations extend over the cuspidal cubic and fix its cusp.
Write $L=\log\lambda$, and let $q$ be the logarithm of $-Q$.
On $E\times S^1$, the return map of a fundamental annulus is
$h(x,\theta)=(t_{-Q}x,\theta+\operatorname{Im}L(x))$.
The isotopy
\[
 h_t(x,\theta)=
 (t_{\exp(tq)}x,\theta+t\operatorname{Im}L(x)),\qquad 0\le t\le1,
\]
has inverse
$(y,\phi)\mapsto(t_{-\exp(tq)}y,
\phi-t\operatorname{Im}L(t_{-\exp(tq)}y))$.
Here $\exp$ is the relative exponential and its group inverse is
written additively. The mapping-torus identification
$(z,1)\sim(h(z),0)$ gives the product map
\[
 [z,t]\longmapsto(h_t(z),e^{2\pi it}),\qquad
 (w,e^{2\pi it})\longmapsto[h_t^{-1}(w),t].
\]
The endpoint identities make these mutually inverse maps well defined.
Thus the filling is homeomorphic over its base disc to $E\times T^2$,
with angular circle $\delta$ and a primitive second circle of
$\gamma^*$-value one."""
    e.replace(old, new, "D22", "maps:src:D.2.11",
              "Spell out the existing isotopy argument as an actual mapping-torus product map and its inverse, retaining the base and angular markings. The real radial factor determines the fundamental annulus; its return map is the displayed angular map.")
    e.replace("\\item Its regular specialization", "Its regular specialization", "D04", "maps:src:D.2.11",
              "Keep the complete specialization calculation within the same product-filling proof phase.")
    e.replace("There is no index-six factor: this is the unchanged filling,\nnot a free order-six affine quotient.\n", "",
              "D02", "maps:src:D.2.11",
              "Remove the unsupported comparison to a different quotient; the product homeomorphism, primitive area maps and exact pullback lattice positively establish the coefficient one used below.")
    e.replace("\\item \\emph{All orders and all displayed twists.}",
              "\\emph{The logarithmic quotient and integral homology.}",
              "D04", "maps:src:D.2.11",
              "Give the final full-parameter argument its mathematical heading.")
    e.replace("are those of \\ref{maps:src:D.2.10} with", "are those of \\cref{maps:src:D.2.10} with",
              "D23", "maps:src:D.2.11", "Print the prerequisite statement kind with its existing label.")
    e.replace("$\\pi_1(X)=\\mathbb Z/|n|$.",
              "$\\pi_1(X)=\\mathbb Z/|n|$. The quotient map sends\n$\\gamma$ to $[1]_n$, and its inverse sends $[1]_n$ to\n$[\\gamma]$ in this presentation.",
              "D22", "maps:src:D.2.11",
              "State the explicit inverse homomorphisms for the final one-generator van Kampen presentation.")
    e.replace("\\item The first finite pullback matrix", "The first finite pullback matrix", "D04", "maps:src:D.2.11",
              "Continue the complete integral attachment calculation within its proof phase.")
    e.replace("Its Smith factors are $(1,1,|n|)$ for arbitrary allowed\nintegers, independently of $r$.",
              r"""The preceding target/source maps for the augmented matrix specialize
at $R=1,m_1=3k,m_2=1,n_1=n,n_2=0$ to this unit elimination.
For the displayed three-by-three block $C$, the integral matrix
\[
 W=\begin{pmatrix}1&0&0\\0&0&1\\k&1&-3k\end{pmatrix},
 \qquad WC=\operatorname{diag}(1,1,-n),\qquad\det W=-1
\]
gives the cyclic quotient map
$[(a,b,c)]\mapsto[ka+b-3kc]_n$, with inverse
$[1]_n\mapsto[(0,1,0)]$. When $ka+b-3kc=nq$, the vector
$(a,c,-q)$ is its preimage under $C$. These formulas prove the
Smith factors $(1,1,|n|)$ for every allowed integer datum;
the displayed maps contain no $r$.""",
              "D22", "maps:src:D.2.11",
              "Give explicit unimodular reduction, cyclic quotient and inverse/kernel preimage for all parameters, replacing an unexpanded Smith-factor assertion. The small new symbolic map program verified the full augmented reduction and every identity.")
    e.replace("recognition applies exactly as in \\ref{maps:src:D.2.6}.",
              "recognition applies exactly as in \\cref{maps:src:D.2.6}.",
              "D23", "maps:src:D.2.11", "Print the previously proved sphere-recognition reference with its theorem kind.")
    old = "\\item The independent executable\n\\texttt{code/manifolds\\_type\\_c\\_ii.py} checks the Weierstrass\nidentity, section, $j$-function, integral monodromy conjugacy,\nsymbolic determinant, and 168 full augmented Smith forms.\nThe preceding proof has no upper bound on $k,n,r$.\n\\end{enumerate}\n"
    e.replace(old, "", "D09", "maps:src:D.2.11",
              "Move the executable path and historical sample-count bookkeeping to the single program proposal list. All named mathematical inputs, polynomial identities, exact conjugacy, full augmented matrix and unrestricted quotient result are printed in the proof, now with explicit inverses; no independent-execution credit is asserted.")
    old = "The local Type-C geometric input is supplied by \\cite[Propositions~3.1, 3.4, 3.6, 4.4 and Appendix~B.4]{manYang26}; the product type-$II$ marking is supplied by \\cite[Lemma~3.10 and Propositions~3.11, 3.13]{manLR26}. The unrestricted $3P$ calculations use the explicitly displayed boundary maps.\n\n"
    e.replace(old, "", "D13", "maps:src:D.2.11",
              "Remove the redundant orphan source summary: the Yang period, affine collar and cusp locators and the actual product-input locators occur at their mathematical uses. The all-parameter boundary calculation is the complete proof immediately above.")
    issues = e.presentation()
    unresolved = []
    for issue in issues:
        line = e.text.splitlines()[issue.line-1]
        if issue.kind == "literal-reference" and issue.token == "B.4" and line == r"\cite[Appendix~B.4]{manYang26}.":
            print("Resolved literal B.4 as the existing external Yang appendix citation, not an inherited local equation reference.")
        else:
            unresolved.append(issue)
    if unresolved:
        raise ValueError(unresolved)
    e.finish(labels=("mapsIII:def:yang-finite-data", "mapsIII:def:os49-component-zero"), tags=("Q113", "Q114"))


if __name__ == "__main__":
    main()
