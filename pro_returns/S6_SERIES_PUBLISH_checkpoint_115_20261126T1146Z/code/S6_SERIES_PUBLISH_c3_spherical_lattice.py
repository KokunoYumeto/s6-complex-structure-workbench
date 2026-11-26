from S6_SERIES_PUBLISH_c3_edit import *

text=SOURCE.read_text()
a=text.rfind('\\begin{proposition}',0,text.index('\\label{night:P4.16}'))
b=text.index('\\subsection{Ordinary double curves and normal surface alternatives}',a)
old=text[a:b]
normalization_start=old.index('\\item We specify the normalization morphism.')
normalization_end=old.index('\\end{enumerate}',normalization_start)
normalization=old[normalization_start:normalization_end]
new=r"""\begin{proposition}[Spherical intersection lattices]
\hypertarget{tag-02WN}{}\label{night:P4.16}\label{stmt:P4.16}
\StatementRecord{night:P4.16}{proved}{02WN}{}
\hypertarget{tag-02WO}{}\label{night:P4.17}\label{stmt:P4.17}
\StatementRecord{night:P4.17}{proved}{02WO}{}
For integers $a\ge2$ and $n\ge1$, the affine surface
$F_{a,n}=\{x^a-zy^n=1\}$ is simply connected and has compact
second-homology intersection lattice $A_{a-1}(-n)$.
Every class in this lattice is spherical.
The reduced hypersurface germ $x^a-zy^n=0$, with any positive
common multiplicity, is excluded from a fibre of a proper
holomorphic degeneration of complex two-tori with smooth total
threefold. For $a=2$ the spherical generator has square $-2n$;
this includes the Whitney umbrella at $n=2$.
The case $a=n=3$ gives the order-three cyclic-ramification germ.
The normalization morphisms below also include singular
normalizations.
\end{proposition}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Let $\zeta_1,\ldots,\zeta_a$ be the distinct roots of
$x^a=1$. The open subset $U=\{y\ne0\}$ of $F_{a,n}$ is
$\mathbb C^*\times\mathbb C$ in coordinates $(y,x)$.
For $0<\delta<1$, its complement is covered by the disjoint
graph neighbourhoods
\[
 N_i:\quad x=\zeta_i(1+zy^n)^{1/a},\qquad |zy^n|<\delta.
\]
The chosen root is holomorphic on the displayed disc.
Each $(y,z)$ domain contracts by simultaneous real scaling.
The intersection $N_i\cap U$ has coordinates $(y,zy^n)$
in $\mathbb C^*\times\{|w|<\delta\}$, and its generating
$y$-loop maps to the generating $y$-loop in $U$.
Van Kampen \cite[Theorem~1.20, p.~43]{Hatcher2002} gives
$\pi_1(F_{a,n})=0$. Mayer--Vietoris
\cite[\S2.2, pp.~149--150]{Hatcher2002} gives
\[
 H_2(F_{a,n};\mathbb Z)
 =\ker\bigl(\mathbb Z^a
       \xrightarrow{(c_i)\mapsto\sum_i c_i}\mathbb Z\bigr).
\]
The Hurewicz theorem \cite[Theorem~4.32, pp.~366--367]{Hatcher2002}
makes every class spherical.

\item Blow up $\mathbb P^1_x\times\mathbb P^1_y$ successively
$n$ times above each $(\zeta_i,0)$. At that point
$b=y$ and $c=x^a-1$ are local coordinates. The successive
charts are
\[
 c=b^j c_j,\qquad z=\frac{c_j}{b^{n-j}}.
\]
For $j<n$, the next centre is $c_j=b=0$.
At $j=n$, $z=c_n$ is regular. The last exceptional curve,
minus its point on the preceding boundary, is the line
$y=0,x=\zeta_i$ in $F_{a,n}$; every earlier exceptional
curve is a pole divisor of $z$.
Thus $F_{a,n}=T_{a,n}\setminus B$, where $T_{a,n}$ is the
resulting smooth projective surface and $B$ consists of the
two infinity divisors, the strict transform of $y=0$,
and the first $n-1$ exceptional curves on each chain.

\item In the total-transform basis $H_x,H_y,E_{i,j}$,
the nonzero products are $H_xH_y=1$ and $E_{i,j}^2=-1$.
The boundary classes are
\[
 H_x,\ H_y,\ H_y-\sum_iE_{i,1},\qquad
 E_{i,j}-E_{i,j+1}\quad(1\le i\le a,\ 1\le j<n).
\]
Their curves form a connected tree of rational curves, so
$H^1(B;\mathbb Z)=0$. Compact-support duality
\cite[Theorem~3.35, p.~245]{Hatcher2002} and the exact sequence
of $(T_{a,n},B)$ identify compact $H_2(F_{a,n};\mathbb Z)$
integrally with the kernel of intersection against these
boundary classes in $H_2(T_{a,n};\mathbb Z)$.
Orthogonality to $H_x,H_y$ removes the ruling coefficients;
orthogonality to the exceptional differences makes the
coefficients constant along each chain. The strict transform
of $y=0$ makes the sum of these constants zero.
The primitive integral basis is therefore
\[
 v_i=\sum_{j=1}^nE_{i,j}-\sum_{j=1}^nE_{i+1,j}
       \quad(1\le i<a).
\]
It has $v_i^2=-2n$, $v_iv_{i+1}=n$, and all other
off-diagonal products zero, giving $A_{a-1}(-n)$.
For $a=2$, this is precisely the difference of the two
exceptional chains and has square $-2n$.
The integral-kernel computation from the displayed boundary
classes is listed in \cref{tab:II:programs}.

\item The polynomial $g=x^a-zy^n$ has positive weights
$(n+1,a,a)$ and degree $d=a(n+1)$. The map
\[
 (x,y,z)\longmapsto
 (\varepsilon^{n+1}x,\varepsilon^a y,\varepsilon^a z)
\]
takes $F_{a,n}$ to the fibre of value $\varepsilon^d$.
It carries a compact spherical representative of $v_1$
and a compact transverse representative for its square
into an arbitrarily small neighbourhood of the origin.

For a local defining function $ug^m$, where $u$ is a unit,
choose a holomorphic root $h^m=u$ and a logarithm of $h$.
The holomorphic map
\[
 \Phi(x,y,z)=
 (h^{(n+1)/d}x,h^{a/d}y,h^{a/d}z)
\]
has invertible derivative at the origin and satisfies
$g\circ\Phi=hg$. Hence $ug^m=(g\circ\Phi)^m$.
After shrinking, $\Phi^{-1}$ embeds the scaled local fibre
in the corresponding smooth compact torus fibre.
The spherical representative becomes null-homotopic there,
because the torus has contractible universal cover
$\mathbb C^2$. Its homology class and square are consequently
zero. The two compact representatives compute the same
intersection in the open local fibre and in the torus,
whereas their square is $-2n$. This contradiction proves
the exclusion for every $a,n,m$ in the statement.

""" + normalization + r"""\end{enumerate}
\end{proof}

"""
apply_edit(old,new,'II-C3-SPHERICAL-ONE-OWNER',['D12','D14'],
    'night:P4.16; night:P4.17','Spherical classes at nonimmersive normalization points',
    'The a=2 construction and the already proved a-root construction have one statement/proof owner. The exact specialization a=2 sends the general root set to {1,-1}, the a exceptional chains to the two old chains, and the primitive basis to their difference. Its square remains -2n. The general proof retains the graph cover, blowup charts, integral kernel, weighted unit-removal map and torus inclusion. The complete normalization morphism from P4.17 is byte-identical. Both permanent statement identifiers and tags remain at this owner.',
    'Root read both complete original proofs, compared each map and lattice specialization, and will reread the receiving proof in full; no independent-check claim.')
apply_edit('\\item \\SeriesRef{night:P4.16}\\quad A spherical intersection obstruction.\n\\item \\SeriesRef{night:P4.17}\\quad The lattice of $x^a-zy^n=1$.',
    '\\item \\SeriesRef{night:P4.16}\\quad Spherical intersection lattices of $x^a-zy^n=1$ and the torus-fibre obstruction.',
    'II-C3-SPHERICAL-FURTHER-RESULT',['D12'],'night:P4.16; night:P4.17',
    'Further results',
    'The two permanent labels now resolve to one owner covering the general lattice and its a=2 specialization, so list that result once.')
apply_edit(r'(\cref{night:P4.16,night:P4.17}) &',
    r'(\cref{night:P4.16}) &',
    'II-C3-SPHERICAL-PROGRAM-REFERENCE',['D12'],'night:P4.16; night:P4.17',
    'Programs table, boundary-kernel computation',
    'The two labels have one receiving theorem number; keep one reference to that exact owner.')
apply_edit('Proposition~\\ref{night:P4.16}, with $n=2$,\ngives a compact spherical class',
    'Proposition~\\ref{night:P4.16}, with $a=2$ and $n=2$,\ngives a compact spherical class',
    'II-C3-CROSSCAP-LATTICE-PARAMETERS',['D22'],'night:P4.20',
    'Ordinary double strata and normal crossings, item5',
    'The target permutation already gives x^2-zy^2. Spell out its exact pair (a,n) in the consolidated theorem; the spherical square stays -4.')
text=SOURCE.read_text()
a=text.index('\\paragraph{Exact source locations used here.}',text.index('\\label{night:P4.20}'))
b=text.index('\\subsection{',a+1)
apply_edit(text[a:b],'','II-C3-SPHERICAL-SOURCE-RECAP',
    ['D07','D09','D11','D13'],'night:P4.20',
    'After the ordinary-double-strata proof',
    'Remove the orphan source-reading/process recap. It contains no additional mathematical assertion beyond the explicitly scoped results and source applications already proved; those proofs and their citations remain. Source-opening and reading-type distinctions belong to the records.')
