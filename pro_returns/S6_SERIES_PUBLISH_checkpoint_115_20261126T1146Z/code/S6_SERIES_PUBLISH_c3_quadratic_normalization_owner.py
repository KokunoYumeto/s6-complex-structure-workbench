"""One quadratic normalization proof and its exact nodal/triple-axis maps."""
from S6_SERIES_PUBLISH_c3_edit import *

lemma=r'''\begin{lemma}[Quadratic conductor algebras and their local fibres]\hypertarget{tag-P257}{}\label{lem:II:quadratic-conductor-normalization}
\StatementRecord{lem:II:quadratic-conductor-normalization}{proved}{P257}{\cref{lem:II:conductor-duality}}
Let $R$ be a reduced complex analytic local ring with maximal ideal
$\mathfrak m$ and finite normalization $B$. A local fibre algebra
$B/\mathfrak mB$ makes $R$ a domain.

More specifically, let $S$ be the regular local analytic ring of a
smooth threefold, let $G,H$ be a regular sequence in its maximal ideal,
and let
\[
 R=S/(f),\qquad f=G^2+UH^2
\]
be reduced. Suppose its conductor ideal in $R$ is $I=(G,H)$.
The finite-duality identification with the total quotient ring gives
\[
 B=\operatorname{Hom}_R(I,R)=R+Rt,\qquad
 t=G/H,\qquad t^2=-U.
\]
For $U(0)=0$, the reduced equation $f$ is irreducible. For $U(0)\ne0$,
the equations $G-H\sqrt{-U}$ and $G+H\sqrt{-U}$ are its two
irreducible factors.
\end{lemma}
\begin{proof}
Every maximal ideal of the finite integral algebra $B$ lies over
$\mathfrak m$, and hence corresponds to one of $B/\mathfrak mB$.
A local fibre makes $B$ local. A normal local ring is a domain,
and the normalization inclusion $R\hookrightarrow B$ then makes
$R$ a domain as well.

For the displayed hypersurface, a common prime divisor of $H$ and
$f$ would divide $G$, contrary to the regular sequence. Thus $H$
is a nonzerodivisor in $R$. The finite-duality multiplier map and
Gorenstein biduality in \cref{lem:II:conductor-duality} identify
$B$ with $\operatorname{Hom}_R(I,R)$, every homomorphism being
multiplication in the total quotient ring. The equations
$tH=G$, $tG=-UH$ and $t^2=-U$ give $R+Rt\subset B$.

Conversely, let a multiplier $\theta$ satisfy $\theta H=r$ and
$\theta G=s$ in $R$. Lifting $r,s$ to $S$, the relation
$rG-sH=0$ in $R$ is
\[
 rG-sH=v(G^2+UH^2),\qquad G(r-vG)=H(s+vUH).
\]
The regular sequence gives $r-vG\in(H)$, so division by the
nonzerodivisor $H$ yields $\theta=vt+w$ with $v,w\in R$.
This proves the displayed algebra equality. Its nonzero fibre is
a quotient of $\mathbb C[t]/(t^2+U(0))$. For $U(0)=0$ it is local,
and the first assertion applies. For $U(0)\ne0$, the two displayed
nonunit factors have no common irreducible factor, since a common
factor would divide both $G$ and $H$. There are at most two
normalization points by the fibre algebra and at least one for
each irreducible factor. Consequently each displayed factor is
irreducible and these are all the factors.
\end{proof}

'''
anchor=r'\begin{proposition}[Hessian defect at a nodal critical curve]'
apply_edit(anchor,lemma+anchor,'II-C3-QUADRATIC-NORMALIZATION-OWNER',['D12','D25'],
 'lem:II:quadratic-conductor-normalization; night:P4.41','Before the nodal-Hessian proposition',
 'Extract the complete already printed two-generator multiplier proof with H arbitrary, retaining its finite duality, regular-sequence syzygy and exact local-fibre factor criterion. The first criterion also records the elementary finite-normalization implication used by the cubic algebra, with its full proof.')
s=SOURCE.read_text();i=s.index(r'Put $R=\C\{x,y,z\}/(f)$. Since $z$ divides neither');j=s.index(r'\item In the locally irreducible case',i)
old=s[i:j]
new=r'''Apply \cref{lem:II:quadratic-conductor-normalization} with this
same $R$, $G$, $H=z^2$, $U=D$ and conductor $I=(G,z^2)$.
The sequence $(G,z^2)$ is regular because $G(x,y,0)$ is $xy$
times a unit. Its exact multiplier is $t=G/z^2$, and the lemma gives
\[
 \overline R=R+Rt,\qquad t^2=-D.
\]
For $D(0)=0$ the reduced germ is locally irreducible. For $D(0)\ne0$,
the two original irreducible factors are exactly
$G-z^2\sqrt{-D}$ and $G+z^2\sqrt{-D}$.

'''
apply_edit(old,new,'II-C3-NODAL-QUADRATIC-OWNER-MAP',['D12'],'night:P4.41','Exact two-generator normalization paragraph',
 'The identity substitution H=z^2, U=D gives precisely the preceding complete proof at its single earlier owner. Every full-function deformation after this paragraph is byte-identical.')
s=SOURCE.read_text();i=s.index(r'If $a,b,c,d$ all vanish at the origin');j=s.index(r'In this case take $s=1$',i)
old=s[i:j]
new=r'''If $a,b,c,d$ all vanish at the origin, the matrix $M$ has
zero reduction modulo the maximal ideal, so
$\overline R/\mathfrak m\overline R$ has basis $1,\omega,\nu$.
By \eqref{eq:II:triple-normalization-products} its span of
$\omega,\nu$ is a square-zero ideal and the fibre algebra is
local. Apply the local-fibre assertion of
\cref{lem:II:quadratic-conductor-normalization} to this same
$R$ and $B=\overline R=J$. It makes $R$ a domain, so $f$ is irreducible.
'''
apply_edit(old,new,'II-C3-CUBIC-LOCAL-FIBRE-OWNER',['D12'],'lem:II:ordinary-triple-factor-lifts','Zero cubic fibre',
 'Use the general finite-local-fibre criterion with the explicitly constructed three-generator normalization; no quadratic hypothesis is used in this first assertion.')
add_event('lem:II:quadratic-conductor-normalization; night:P4.41; lem:II:ordinary-triple-factor-lifts',
 'II-C3-ROOT-QUADRATIC-NORMALIZATION-OWNER','used and rechecked in this run',
 'Root reread the full existing nodal normalization calculation and the complete receiving shared proof. The exact syzygy rG-sH=vf gives the identical multiplier algebra for arbitrary regular sequence (G,H), and the proof states the finite-algebra local-fibre criterion separately. P4.41 substitutes H=z^2,U=D; P280 uses only that general local-fibre assertion on its independently constructed J. Every original factor conclusion and subsequent full-function deformation is preserved. The proof is an exposed extraction, with no independent credit.',
 'S6_SERIES_PUBLISH_II.tex: quadratic conductor normalization and exact applications',source=__file__)
print('P257 admitted with the complete shared multiplier proof; nodal and cubic applications compared.')
