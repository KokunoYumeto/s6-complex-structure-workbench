# OS49: current page and index comparison work

This file records unfinished work after P3F.30. It does not assign an
OS49 return index. The exact topology, angular clutch, source complexes,
all-order cap lattices, and norm quotient are in P3F.26--30.

## Exact regular-band cohomology

Let D be a closed half-disc whose straight edge lies on the boundary
of a compact surface, and let A be its inner semicircular edge. The
inclusion A into D is a homotopy equivalence. Therefore

\[
 H^*(T^2\times D,T^2\times A;\mathbb Z)=0.
\]

This applies to each actual regular torus band attached to a page
boundary, once the whole homotopy support has been placed in such
bands. The relative long exact sequence then makes restriction of
line Chern classes to the complement injective. Thus a graph-normal
line and an outer-page line agreeing off these bands agree on the
whole page. A possible difference of relative lifts still lies in
the image of boundary H1; its square and its product with a class
restricting to zero on the boundary vanish by the relative cup
product formula used in P3F.10 and P3K.5.

Fourfold audited this algebraic-topology step. It does not supply the
required page, the support localization, or the cusp line comparison.

## An attempted phase-gap page and its unresolved orientation

In a product cusp orbit E'_(I1) times S1_K, a smooth long-angle map
a:E'_(I1) to S1 and the K angle b give the submersion
psi=2b-a. Its level is the connected double cover corresponding to
2Z in the fundamental group Z of the nodal neighbourhood. It has
the I2 source topology, with the exact boundary cycle u=2H+K.

An attempted construction placed all three page phases in a gap in
psi(F_fix). If the real lift of a on the normalized fixed sphere
has endpoint difference one and the two b endpoints have positive
gap epsilon, then choosing a=g/epsilon for b|F=g gives
psi|F=(2epsilon-1)a. Its image misses (0,2epsilon). Three distinct
phases can be placed there by reparametrizing the suspension circle.
This calculation records the precise needed endpoint order; that
order has not been proved for the marked toric fan. It is not a
construction of the actual required page.

The fixed-edge charts supplied and independently checked by fourfold
make the concern concrete. For the two adjacent triangles
(0,0),(1,0),(0,1) and (0,0),(0,1),(-1,1), write

\[
 q=X_0X_1X_2,\quad Z=X_1,\quad V=X_2,
 \qquad
 Y_0=X_0X_1,\quad Y_2=X_2X_1,\quad Y_3=X_1^{-1}.
\]

The weights are (-1,0,+1) in the first chart, and the two normal
lines transform by multiplication by X1. On the balancing normal
section |X0|=|X2| the exact identity is

\[
 \frac{2\log|V|}{\log|q|}
 =1-\frac{\log|Z|}{\log|q|}.
\]

Thus the raw marked coordinates have a negative slope. Their full
comparison with the smooth product angle at q=0 remains necessary.
Replacing the diagonal by its flop has not been authorized as an
identification of the same family, and is not done here.

The boundary identity psi=-a+2b must also not be silently promoted
to a particular smooth extension through the fixed locus. A chosen
smooth long-angle extension need not be the period-defined angle.

## Exact source-line alternatives after an actual page construction

The actual source line has multidegrees (-1,+1) on the I2 components.
Its elementary transform M(-C0) has (+1,-1), and P3F.28 supplies the
actual morphism between them, whose cone is O_(C0)(-1). Both squares
are -2. On the compact degree-three source pullback, an arbitrary
selection of these three elementary transforms has the same square
as M because the selected (-2)-curves are disjoint and M.C0=-1.
Boundary gluing gauges have square zero as above.

A proposed way to identify these two alternatives uses homotopies
of the two component spheres to a common constant-K normalization.
The opposite node preimages can contribute local Hopf degrees +1
and -1; their sum is a regular elliptic fibre of degree zero, forcing
the common background degree to vanish. Fourfold correctly noted
that a homotopy kept entirely inside the central nodal fibre has
nontransverse intersection with the fixed sphere. An actual q-normal
pushoff and its two local Thom signs must be written before using
that argument. Those maps are not yet supplied.

## The norm quotient retains the unresolved correction

P3F.30 provides a completed morphism, in contrast with the unfinished
page attempt: the actual quadratic quotient X to X/mu2, its A1
resolution, and the two opposite Hopf-line base shifts +1,-1.
The ordinary formula is v mapped to v tensor phi_p^{-1}(v), and the
norm source line is N=M^2(-C0), with whole-fibre linearization.
The scalar is lambda^2. Its two resolved fixed sections have normal
bundles O(-2) plus O, with opposite assignments of weights.

One cannot cap those two sections separately by the old zero-charge
D3 times S1 cap while extending the line: their base degrees are
nonzero. A joint cap or a local symbol comparison retaining both
charges is the current target. Acyclicity of N or of the O(-1)
source cones does not by itself give that comparison. No return
value is inferred from their numerical cancellation.

## Literature lead consulted

Moriyama, *An Invariant of Embeddings of 3-Manifolds in 6-Manifolds
and Milnor's Triple Linking Number*, J. Math. Sci. Univ. Tokyo18
(2011),193--237, is retained as
records/primary_sources/Moriyama11.pdf. Its e-class and quasi-e-class
framework, Theorems1.2 and8.1, keeps the self-linking form explicitly.
The boundary e-class hypotheses must be checked for any use here;
the two nonzero norm charges prevent simply discarding them. The
paper is a consulted lead, not a proof of the OS49 comparison.
