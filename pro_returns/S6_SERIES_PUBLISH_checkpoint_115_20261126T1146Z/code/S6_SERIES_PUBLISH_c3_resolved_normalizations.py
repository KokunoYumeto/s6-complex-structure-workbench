from S6_SERIES_PUBLISH_c3_edit import *

apply_edit(r'''At a reverse point blowup, a centre of multiplicity $\mu$
gives exceptional coefficient $\mu-1$. At a crossing,
$\mu\ge2$, so the exceptional curve subdivides the edge of
the reduced divisor. At a smooth point, it adds a rational
leaf when $\mu\ge2$ and leaves the reduced divisor unchanged
when $\mu=1$. Thus $A=D_{\rm red}$ is the strict transform
of $H$ with rational trees attached, and is connected.
Collapsing those trees to their attachment points induces
an isomorphism on fundamental groups by van Kampen.
The ruling and point blowdowns also induce isomorphisms
on fundamental groups. Their composite restricts on the
strict transform of $H$ to the section isomorphism with
the ruling base. Therefore the inclusion
$j:A\hookrightarrow T$ induces an isomorphism
$j_*:\pi_1(A)\to\pi_1(T)$.''',
    r'''Apply \cref{lem:II:canonical-boundary-blowup} at every reverse
point blowup to the pushed-forward divisor and its strict transform.
Its coefficient $\mu-1$ gives exactly the reduced incidence operations
there: subdivision at a crossing, attachment of a rational leaf at
a smooth point of multiplicity at least two, and no boundary
component at multiplicity one. Thus $A=D_{\rm red}$ is connected
and consists of the strict transform of $H$ with rational trees.
The maps in \cref{lem:II:boundary-blowup-groups} identify the
boundary and surface fundamental groups with those on $T_0$,
commuting with inclusion. On $T_0$, the ruling restricted to $H$
is the section isomorphism to the base, and its rational-fibre
trees add no generators by \cref{lem:II:curve-normalization-graph}.
Consequently inclusion $j:A\hookrightarrow T$ induces an
isomorphism $j_*:\pi_1(A)\to\pi_1(T)$.''',
    'II-C3-RESOLVED-RULED-BOUNDARY',['D12'],'night:P4R.7','Step 1',
    'Applies P232/P246 to exactly the resolution boundary and blowdowns; the ruling-section map and P245 graph comparison identify the unchanged inclusion homomorphism.')

apply_edit(r'''Let $c$ be the number of irreducible
components of $C$, let $g_i$ be their normalization genera,
and let $b$ be the cycle rank of its normalization incidence
graph. The calculation in \cref{night:P4R.3} gives
\[
 \pi_1(C)\simeq
   \Bigl(*_i\pi_1(C_i^{\rm norm})\Bigr)*F_b,
 \qquad e(C)=c+1-2\sum_i g_i-b.
\]
Virtual abelianness permits either all $g_i=0$ with
$b\le1$, or one $g_i=1$ with $b=0$. These give respectively
$e(C)=c+(1-b)\ge0$ and $e(C)=c-1\ge0$.''',
    r'''The curve $C$ is connected as the image of $A$.
Apply \cref{lem:II:curve-normalization-graph} to its normalization
and the virtually abelian group just identified. Its curve-group
and Euler comparison gives $e(C)\ge0$.''',
    'II-C3-RESOLVED-RULED-GRAPH',['D12'],'night:P4R.7','Step 2',
    'Uses the earlier complete graph lemma for the identical connected conductor image; retains the proper-resolution pushout, its explicit inverse on both vertex groups and Euler additivity.')

apply_edit(r'''Then $e(C)=c+s-2g-b$, $r\ge g$, and
$c\ge g$.''',
    r'''Apply \cref{lem:II:curve-normalization-graph} to each connected
component of $C$. Its Euler formula gives
$e(C)=c+s-2g-b$. Every elliptic image component receives one
of the elliptic roots, so $r\ge g$ and $c\ge g$.''',
    'II-C3-RESOLVED-HOPF-GRAPH',['D12'],'night:P4R.8','Step 2',
    'Specifies the disconnected componentwise graph comparison and the existing root-to-image map counting inequalities.')

apply_edit(r'''\item Apply the local hypersurface argument in the proof of
\cref{night:P4R.5} to the conductor germs on $N$. Two different
curve germs of $C$ would require two
different normalization points, because
each point has just one conductor germ.
Their corresponding hypersurface
branches intersect in a curve germ.
That germ belongs to both conductor
images and forces the two chosen germs
to coincide. Thus $C$ is locally
unibranch with disjoint irreducible
components.''',
    r'''\item Apply the hypersurface-branch argument in the proof of
\cref{night:P4R.5} to the finite normalization $\nu:N\to S\subset Y$.
The preceding step gives its required single conductor germ at
each normalization point, including points under the exceptional
fibres. That argument identifies any two image germs through the
intersection of their surface branches. Thus $C$ is locally
unibranch with disjoint irreducible components.''',
    'II-C3-RESOLVED-HOPF-GERMS',['D12'],'night:P4R.8','Step 6',
    'The original finite-normalization local argument is applied to nu on N, after the unchanged exceptional-block argument establishes its exact germ hypothesis. No smoothness of N is imported.')

apply_edit(r'''a ruling fibre gives horizontal degree two. A reduced
horizontal component $H$ satisfies
\[
 0\le 2g(\widetilde H)-2
 \le 2p_a(H)-2
 =-(D_0-H)H\le0.
\]
The first inequality is
Riemann--Hurwitz over the elliptic
base. All inequalities are equalities:
every such component is smooth elliptic,
unramified over $E$, and disjoint from
the other components of $D_0$. Every
vertical fibre meets the horizontal
part, so no vertical component occurs.
The reduced-horizontal possibilities
are therefore one smooth elliptic
bisection or two disjoint elliptic
sections, each with coefficient one.''',
    r'''a ruling fibre gives horizontal degree two. The reduced-horizontal
calculation in the proof of \cref{night:P4.22} uses exactly this
minimal elliptic ruled surface $T_0$, the effective divisor $D_0$,
the identity $K_{T_0}+D_0\equiv0$, and coefficient one on each
horizontal component. Apply that calculation to these data.
It gives one smooth elliptic bisection or two disjoint elliptic
sections, unramified over $E$, each with coefficient one, and
no vertical component.''',
    'II-C3-RESOLVED-ELLIPTIC-NUMERICS',['D12'],'night:P4R.9','Step 1',
    'The complete earlier P4.22 proof was read; its same numerical adjunction/Riemann–Hurwitz calculation has no smooth-normalization input. Only that minimal ruled-boundary calculation is applied here, while the separate resolution-exceptional exclusion remains in full.')

apply_edit(r'''\item The reverse blowup formula $\mu-1$
then keeps $A=\operatorname{Supp}D$''',
    r'''\item The reverse point-blowup formula of
\cref{lem:II:canonical-boundary-blowup}, applied to this $D_0$,
has coefficient $\mu-1$ and keeps $A=\operatorname{Supp}D$''',
    'II-C3-RESOLVED-ELLIPTIC-BLOWUP',['D12'],'night:P4R.9','Step 2',
    'Cites the single earlier coefficient owner for the same reduced horizontal boundary.')

apply_edit(r'''inclusion in $T$ induces an
isomorphism on fundamental groups,
by the ruling and invariance under
point blowups.''',
    r'''inclusion in $T$ induces an isomorphism on fundamental groups:
the ruling restricts to an isomorphism on $H$, and
\cref{lem:II:boundary-blowup-groups} preserves that inclusion
map through each point blowup.''',
    'II-C3-RESOLVED-ELLIPTIC-GROUPS',['D12'],'night:P4R.9','Step 3',
    'Uses the same ruling-section map and the commuting group comparisons of P246.')

apply_edit(r'''The virtually abelian
curve-group calculation in that proof gives $e(C)\ge0$,
and \cref{night:P4.13} gives $e(S_{\rm reg})\ge0$.''',
    r'''The resulting group $\pi_1(C)$ is virtually abelian by
\cref{night:P4R.1}. Applying \cref{lem:II:curve-normalization-graph}
to this connected curve gives $e(C)\ge0$, and
\cref{night:P4.13} gives $e(S_{\rm reg})\ge0$.''',
    'II-C3-RESOLVED-ELLIPTIC-EULER',['D12'],'night:P4R.9','Step 3',
    'Makes the exact earlier specialization and normalization-graph inputs explicit; the proper pushout inverse is retained.')

add_event('night:P4R.7; night:P4R.8; night:P4R.9',
    'II-C3-ROOT-RESOLVED-NORMALIZATIONS','used and rechecked in this run',
    'Read all three complete original proofs, then compared their receiving substitutions with the exact earlier P232/P245/P246 and P4.22 owners. The proper map rho=nu composed with pi, its full exceptional fibres, the quotient homeomorphism, the amalgam inverse, the disconnected Hopf root counts and exceptional-subtree proof, and the reduced elliptic case exceptional-curve contradiction remain. All three statements are unchanged; no hypothesis of smooth normalization is transferred to the resolved cases. Complete final receiving-unit pass remains to follow.',
    'S6_SERIES_PUBLISH_II.tex',source='code/S6_SERIES_PUBLISH_c3_resolved_normalizations.py')
print('Resolved-normalization applications admitted.')
