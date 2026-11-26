"""Rewrite the ruled-fibre leaf proof with its exact cyclic-cover maps."""
from S6_SERIES_PUBLISH_c3_edit import *

apply_edit(
 r'''\StatementRecord{night:P4R.12}{proved}{02Y5}{\SeriesRef{night:P4R.3}, \SeriesRef{night:P4R.6}, \SeriesRef{night:P4R.9}}''',
 r'''\StatementRecord{night:P4R.12}{proved}{02Y5}{\cref{lem:II:irrational-ruled-boundary,night:P4R.6,night:P4R.7}}''',
 'II-C3-RULED-LEAVES-INPUTS',['D22'],'night:P4R.12','Statement input declaration',
 'Apply the common boundary lemma on the same ruling and pole divisor, followed by the combined R7/R9 owner.',
 'Complete old unit read; exact receiving maps checked during the full rewrite.')
apply_edit(
 r'''Let $T\to N\to S$ be the minimal normalization resolution of an
irreducible support in Part~4.2 with ruled minimal model of positive
base genus. Let $r:T\to B_0$ be its ruling, and let $D$ be the
effective integral pole divisor of P4R.6.''',
 r'''Let $T\to N\to S$ be the minimal normalization resolution of an
irreducible support in \cref{def:II:standing-torus-fibration}, with ruled minimal model of positive
base genus. Let $r:T\to B_0$ be its ruling, and let $D$ be the
effective integral pole divisor of \cref{night:P4R.6}.''',
 'II-C3-RULED-LEAVES-SCOPE',['D04','D06'],'night:P4R.12','Statement hypotheses',
 'Replace the production numbering by the exact standing setting and numbered pole-divisor proposition; all hypotheses remain.',
 'Complete original statement and proof read; receiving hypotheses compared word for word.')
apply_edit(
 r'''These assertions retain the multiplicities of the ruling fibre
and do not require the multiplicity of $E$ to be one.''',
 r'''The full ruling-fibre multiplicities are arbitrary positive integers.''',
 'II-C3-RULED-LEAVES-MULTIPLICITIES',['D02','D08'],'night:P4R.12','End of statement',
 'State the original unrestricted multiplicity domain positively; the proof continues to use the full fibre sum.',
 'Original and receiving statement scope compared; no multiplicity restriction introduced.')
apply_edit(
 r'''\item A reduced horizontal pole divisor occurs here only over an
elliptic base, by P4R.3, and P4R.9 then makes the normalization
smooth and minimal. In that case there is no reducible ruling
fibre. We may therefore work in the double-horizontal-section
case throughout the proof.
A ruling fibre on $T$ is obtained from a smooth $\mathbb P^1$
by the actual sequence of point blowups. Its reduced support is
a normal-crossing tree of smooth rational curves. Each component
of a reducible fibre has negative self-intersection. One can
verify the latter assertion without a contraction criterion:
if $F_b=\sum m_iE_i$ is the full fibre, then''',
 r'''\item Write $\beta:T\to T_0$ for the blowdowns to the minimal ruling and $D_0=\beta_*D$. Proposition~\ref{night:P4R.6} gives $K_T+D\equiv0$. Apply \cref{lem:II:irrational-ruled-boundary} to this same $\beta$ and $D$. In its reduced-horizontal case, \cref{night:P4R.7} makes $N$ smooth and minimal; its minimal resolution $T\to N$ is then an isomorphism. Every ruling fibre is irreducible. The stated reducible fibre therefore belongs to the double-horizontal-section case.

A ruling fibre on $T$ is obtained from a smooth $\mathbb P^1$
by the point blowups inverse to $\beta$. Its reduced support is
a normal-crossing tree of smooth rational curves. Each component
of a reducible fibre has negative self-intersection: for the full fibre $F_b=\sum m_iE_i$, with every $m_i>0$, we have''',
 'II-C3-RULED-LEAVES-BOUNDARY-APPLICATION',['D04','D08','D02','D22'],'night:P4R.12','First proof step',
 'Use the already-proved boundary alternative with its exact blowdown and divisor, and keep the complete full-fibre intersection proof.',
 'Complete original proof and exact common-lemma hypotheses read; receiving first step compared in full.')
apply_edit(
 r'''so $E$ is disjoint from the full pole support. The map to $S$
then identifies a neighbourhood of this compact curve with a
neighbourhood in $S_{\rm reg}$, by P4R.6. The local cyclic
base change which removes the multiplicity of the support is
unramified over this regular locus. Its restriction to $E$ is
a disjoint union of copies of $\mathbb P^1$, because
$\pi_1(\mathbb P^1)=0$. A chosen copy has the same normal
degree $-2$. A smooth local trivialization over a sufficiently
small parameter disc transports it into a nearby four-torus,
still with self-intersection $-2$. Every map from $S^2$ to that
torus is null-homotopic, since its universal cover is
$\mathbb R^4$; its homology class and self-intersection must
therefore be zero. This contradiction leaves $E^2=-1$ and
$DE=1$.''',
 r'''so $E$ is disjoint from the full pole support. Proposition~\ref{night:P4R.6} identifies a neighbourhood of $E$ under $T\to S$ with a neighbourhood in $S_{\rm reg}$. Write the original full fibre as $mS$ and a base parameter as $t$. On this regular locus the full function has the form $t=uz^m$, where $u$ is a unit. Choose a local root and set $w=u^{1/m}z$; the inverse is the unique local solution of this equation. Normalize the base change $t=s^m$. Its charts are $w=\zeta s$, with $\zeta^m=1$; the projection to the original neighbourhood is unramified and its map to $s$ is a submersion. These charts glue to a finite unramified cover near $E$.

The restriction of this cover to $E\simeq\mathbb P^1$ is a disjoint union of copies of $E$, since $\pi_1(\mathbb P^1)=0$. Fix one copy $E'$. The unramified projection identifies its normal bundle in the central surface with that of $E$, of degree $-2$. Lift a constant real base vector field near this compact $E'$ through the submersion. Its flow is defined uniformly for sufficiently small time on a neighbourhood of $E'$ and gives an orientation-preserving identification with a neighbourhood in a nonzero fibre. That fibre is the original torus $Y_{s^m}$, because the normalized base change over $s\ne0$ has that same fibre. The image of $E'$ is consequently a sphere of square $-2$ in this torus. Its map lifts to the contractible universal cover $\mathbb R^4$, so it is null-homotopic and has zero homology class and square. This contradiction gives $E^2=-1$ and $DE=1$.''',
 'II-C3-RULED-LEAVES-FULL-FIBRE-MAP',['D04','D22'],'night:P4R.12','Exclusion of an outside curve of square minus two',
 'Exhibit the same full-function cyclic base change and the compact neighbourhood flow, including the root inverse, unramified normal-bundle identification and exact target torus. No reduced/full-function identification is assumed.',
 'Complete original transport argument read and the full receiving map and normal-degree comparison checked directly.')
print('Ruled-fibre leaf proof rewritten; complete receiving unit read remains to be recorded.')
