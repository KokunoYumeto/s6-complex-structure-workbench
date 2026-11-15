# A local torsion-canonical finite-monodromy caution

Working note, 15 November 2026. No numbered result or S6 comparison is
claimed here. This checks the scope of a possible local good-reduction
argument in the remaining interior-limit problem.

There are explicit local proper torus degenerations with trivial
canonical bundle, finite degree-one monodromy, and non-Kähler central
components. Their Euler number remains zero because a compact elliptic
action survives. Thus the global topology or the actual extended
delta action is essential; a local torsion-canonical hypothesis alone
must not be treated as a good-reduction theorem.

Take the compact Weierstrass cubic family over a small t-disc with
affine equation y²=x³+tx and resolve its unique total-space singular
point. Setting t'=t+x² makes that singularity y²=xt', an A1 singularity.
In a chart of the minimal resolution,

`x=rho, y=rho s, t'=rho s², t=rho(s²−rho)`.

The central fibre consists of two smooth rational curves C1 and C2
meeting with tangency order two: rho=0 and rho=s². Their intersection
is two and, since C1+C2 is a fibre divisor, their self-intersections
are both minus two. The original cuspidal cubic has rational
normalization, so the strict component also completes to P1. This is
the usual KodairaIII local model. The form dt wedge dx/y pulls back
to a nonzero constant multiple of d rho wedge ds and extends across
the resolution. The local elliptic surface therefore has trivial
canonical bundle. Its j-invariant is constantly1728 and its smooth
elliptic fibres have order-four linear monodromy.

Let E=C/(Z+iZ), and use L=O(C1) to form a principal E bundle over this
resolved surface by the transition cocycle [log(l_ab)/(2 pi i)].
This is the explicit Cartier logarithmic-transform cocycle used in
B.4.7; no classification of a new surface is necessary. Its total
space is smooth and proper over the t-disc, and is flat there.
The relative canonical bundle of a principal elliptic bundle is
trivial, so its total canonical bundle is trivial as well.

Outside the central fibre L has its canonical trivialization. The
punctured family is consequently the product of E with the original
elliptic family, and its H1 monodromy is identity on H1(E) and the
order-four elliptic operator on the second summand. The restrictions
of L to C1,C2 have degrees minus two and plus two. Each corresponding
principal E bundle over P1 is a secondary scalar Hopf surface: its
fundamental group is Z plus Z/2 and its first Betti number is one.
The two surfaces meet along an elliptic curve with tangency, so the
centre is not a normal-crossings surface in this model.

The compact elliptic group E acts freely on the whole total space.
Every fibre therefore has Euler number zero. This construction is
fully consistent with the new global E.2.14 obstruction on S6. It
does not identify this local model with an actual prescribed finite
root torus, does not construct a compact S6 fibration, and supplies
no uniqueness failure at the marked six-sphere interior limit.

For context, I opened Nishiguchi's original MPI88-48 preprint,
*Degeneration of K3 surfaces, II*:
<https://archive.mpim-bonn.mpg.de/id/eprint/3390/1/preprint_1988_48.pdf>.
Printed pp.7–12 distinguish torsion/trivial-canonical non-Kähler
types from the algebraic Kulikov classification. Printed p.12,
Conjecture1.9, explicitly leaves the corresponding nilpotent-monodromy
classification conjectural in that source. It therefore cannot be
cited as a general finite-monodromy good-reduction theorem. Retrieval
reference: turn465view0. No later resolution of that conjecture is
asserted or needed for the explicit check above.
