# Independent referee: B.4.15 regular-place Hopf insertion

Referee: boundary_d. 15 November 2026, 18:36 UTC.

**Verdict: PASS at the exact local, two-parameter scope of the working statement.**
I read `sections/ab_push_regular_cap_working.md` in full and inspected the
exact assertions in `code/ab_push_regular_cap.py`, its output and its JSON.
The argument gives a proper replacement over the bidisc, isomorphic to the
actual prescribed model off the base origin, with smooth total fourfold and
reduced normal-crossings divisor over the degeneration parameter. It does
not assert joint flatness, properness over the noncompact parameter disc
alone, a one-parameter compact-surface degeneration, or a global S6 filling.
Those qualifications are necessary and are correctly retained.

## 1. Actual semiabelian action and the closing period

The rank-three quotient is the analytic group

\[
G_z=\mathbb C^2/(\mathbb Z u(z)+\mathbb Z w+\mathbb Z\delta),
\quad u(z)=(\tau(z),\mu(z)),\quad w=(1,0),\quad\delta=(0,1).
\]

It is the actual degree-zero punctured line bundle over the actual elliptic
curve. The formula

\[
\chi_z(t)=\left[\frac{\log t}{2\pi i}u(z)\right]
\]

is a single-valued holomorphic group homomorphism because a logarithm
change adds an integral multiple of the actual period u. No algebraicity
of this homomorphism, closedness of its image, splitting of G, or torsion
of the degree-zero line bundle is required. In particular, its existence
does not contradict simplicity of a generic compact two-torus.

Here is a useful explicit version of the equivariance check. Before
quotienting by the closing period, a translation represented by (a,b)
acts in additive/multiplicative coordinates by

\[
(\xi,W)\longmapsto(\xi+a,e^{-2\pi i b}W).
\]

This descends through the three fixed periods. The closing period is
another translation of this same commutative group, with its scalar
coordinate containing the factor r^12. Thus the two actions commute
exactly, not just on the elliptic quotient. Each unfolded compactification
is G times, over the scalar C* subgroup, P1. The zero and infinity sections
are preserved. At a node the two fibre directions are paired dually; their
factors cancel in xy=r. The toric subdivision of the W/r direction is
equivariant under scalar multiplication. Consequently the action extends
to the entire twelve-cycle resolution and keeps each component label.
This is precisely the action needed for the later twisting and ideal
blow-ups; an action on the smooth generic fibres alone would not suffice.

## 2. The affine-to-Jacobian comparison is valid locally

For B=Delta times Delta*, the actual lattice system Lambda has H2(B,Lambda)=0:
B has the homotopy type of a circle, also for these local coefficients.
The relative Lie algebra is a coherent vector bundle. The exponential
sequence of sheaves of local holomorphic sections

\[
0\longrightarrow\Lambda\longrightarrow\mathcal V
\longrightarrow\mathcal T\longrightarrow0
\]

and Cartan B on this Stein base give H1(B,T)=0. The actual affine torus
family is a torsor under its Jacobian and therefore has a holomorphic
section on this punctured local base. This provides the required actual
comparison. Nothing in this argument extends that section across r=0 or
asserts that an affine torsor is globally split over the elliptic base.

## 3. The ideal and both component calculations

In the base-blow-up chart r=zs, the pullback node is xy=zs. A central
component of the original smooth total space is Cartier. Hence its
pulled-back ideal and O(-F) are honest invertible ideals, and their sum is
globally meaningful. With the even branch labelled x=0, this sum is
(x,z). It is invariant under G because the component and the base
exceptional divisor are invariant. Its non-Cartier locus is exactly
x=y=z=s=0, with the elliptic coordinate free. The twelve such loci are
disjoint. Thus the six even-component prescriptions do not introduce an
overlap choice.

The blow-up of (x,z), after the requisite strict-transform cancellation,
has the two smooth charts

\[
z=xQ,\quad y=Qs,\quad r=xQs;
\qquad
x=zX,\quad s=Xy,\quad r=zXy.
\]

All displayed factors occur once. In the other base chart z=r zeta, the
ideal is (x,r)=(x,xy)=(x), so the operation is an isomorphism. Away from
the node loci it is likewise Cartier and has no effect.

For the vertical even branch V_x, the two induced maps to its original
normalization with coordinates (y,s) are

\[
(Q,s)\mapsto(Qs,s),\qquad (X,y)\mapsto(y,Xy).
\]

These are exactly the blow-up charts of (y,s). The untouched elliptic
coordinate makes the centre an elliptic curve. V_y is unchanged. The
horizontal odd branch H_y has the corresponding blow-up, whereas H_x
is unchanged. Applying this at the two distinct conductor sections of
each component gives two disjoint elliptic-curve blow-ups on every even
vertical component and none on an odd vertical component. The claimed
horizontal parity is the opposite. This agrees with the exact twelve-edge
incidence calculation in the code.

## 4. Cartier twisting, separation and properness

The transition functions of O(F) are holomorphic units on their overlaps.
Applying the holomorphic homomorphism chi gives actual automorphisms of
the resolved model satisfying an exact cocycle. Invariance of the ideals
proves that resolving and twisting commute. The gluing is a locally
trivial form of the given proper model over each base open set. Two points
over the same base point are separated in one such chart, and points over
different base points are separated by the base. Thus the result is
Hausdorff. Properness is local on the target and is preserved under
composition with the proper base blow-up.

The canonical section of O(F) is nowhere zero off F and therefore
trivializes the twisting there. The small resolutions are also
isomorphisms there. This supplies an actual specified holomorphic
isomorphism with the original model off the base origin, in particular
over every r nonzero. It is stronger than just an isomorphism of generic
fibres or equality of their periods.

The total space is smooth, r is a nonzero divisor, and a torsion-free
module over the one-dimensional regular local parameter ring is flat.
This proves the asserted flatness over r. The vertical threefolds over a
point of the bidisc correctly preclude an assertion of joint flatness.

## 5. Compact vertical normalization and its topology

On F, O(F) restricts to O_P1(-1). With the usual associated-bundle
convention, the elliptic quotient is

\[
H=\mathcal O_{\mathbb P^1}(-1)^\times/\ker(\chi\colon\mathbb C^*\to E).
\]

Dividing the elliptic additive coordinate by tau0 changes its lattice to
Z+eta Z, eta=-1/tau0 in the upper half-plane. The projected homomorphism
then has kernel a'^Z, a'=exp(2 pi i eta), with absolute value less than one.
Thus H is exactly the scalar Hopf surface

\[
(\mathbb C^2\setminus\{0\})/\langle a'\operatorname{id}\rangle.
\]

The associated G-bundle over P1 maps to H with free scalar C* fibre.
Compactifying this principal C* bundle produces the actual projective
bundle P_H(O plus M_H), with both conductor sections globally defined.
This argument retains the original degree-zero line bundle on each
elliptic fibre and does not replace it by a product. The two curve centres
are the two conductor sections over the one distinguished point of F,
hence disjoint compact elliptic curves.

The universal cover of H is C2 minus zero, so pi1(H)=Z. A P1 bundle has
the same fundamental group as its base, and blow-up along a smooth
complex codimension-two centre preserves fundamental group. Therefore
every final vertical normalization has b1=1 and fails the ddbar lemma.

## Scope and source use

This is a genuine local counterexample to an attempted exclusion of
non-ddbar central components based only on generic simplicity in this
two-parameter setting. It preserves the actual punctured torus family.
It leaves the original component permutations unchanged, and therefore
does not evade B.3.1. The explicit analytic gluing proves the needed
extension of the Cartier construction; no unsupported enlargement of
Fujimoto's original principal-elliptic hypotheses is being used. No new
global compactification or uniqueness theorem is imported in this
referee report.
