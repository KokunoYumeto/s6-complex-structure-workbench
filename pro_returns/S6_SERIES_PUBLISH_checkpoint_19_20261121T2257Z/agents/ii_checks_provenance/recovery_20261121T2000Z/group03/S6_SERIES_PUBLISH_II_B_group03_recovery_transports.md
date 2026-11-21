# Group 03: new recovery comparisons and exact computation transports

This record was written after the reset and after historical exposure to all
nine target proofs. The original derivations and freeze receipts dated
19:10:25–26 UTC survive in checkpoint 14. This text neither replaces their
dates nor represents itself as recovered historical bytes. The target proofs
have now been reopened and read in full. No event is created by this record.

## 01AP: correction to the frozen draft

The frozen draft calls a local analytic ring of a globally irreducible
reduced component a domain. Local analytic branches need not be irreducible.
The printed proof supplies the required stronger local statement: the
restriction of an equation of a distinct global component is a
nonzerodivisor. A zero on an entire local branch would, by analytic
continuation of that component, imply equality of the two global prime
divisors. Reduced hypersurface local rings have their minimal primes as
associated primes, so avoiding every branch gives a nonzerodivisor. The
Cartier ideal and its powers are therefore the actual ideal used in the
filtration. Krull intersection applies in the Noetherian local ring; it
does not require that ring to be a domain. The finite-dimensional descending
spaces, exponential-sequence Picard-component transport, local Picard-family
semicontinuity, repeated-component filtration and finite fibre intersection
then give exactly the printed argument. The frozen text is retained, and
this correction is attributed to the postrelease comparison. No defect in
the printed proposition is inferred from that draft error.

## 01AQ: exact standard-family scope

The safe setup identifies the standard (3,4,infinity) six-sphere member X and
its full reduced fibre W, with normalization dP6. The supplied integral
homology theorem gives H1(X,Z)=H2(X,Z)=0, hence cohomological H2(X,Z)=0 by
universal coefficients. Restriction, pullback and naturality of c1 send each
ambient line to a line with zero Chern class on dP6. The exponential sequence
is injective on Pic(dP6), because H1(dP6,O)=0. It therefore trivializes the
pulled-back line. No equality of that line with a line on W is asserted.
The normal-crossing K formula, projection formula and the injection of the
torsion-free quotient into normalization differentials give the actual
one-dimensional ambient section space. The proposed statement names this
standard member explicitly. The existing AC2026 credit is retained; no new
verification of that source's theorem is claimed in this recovery record.

## 01AR: journal locator and a different finite computation

The publisher PDF of CDP2020, Proposition 7.3, printed p.693, explicitly
allows the normalized line family to be constant and begins Step 1 with the
genus-at-least-two inference. The product E x P1 with constant trivial
line family and the pullback of an invariant elliptic differential supplies
the precise counterexample to that inference. It asserts no example with
all of the proposition's ambient threefold hypotheses.

The printed calculation uses the two product summands and Kunneth. The new
recovery program instead multiplies ch(Omega)=2-c1+(c1^2-2c2)/2 by
td=1+c1/2+(c1^2+c2)/12 in degree two. This gives
chi(Omega)=(c1^2-5c2)/6. For E x P1 both Chern numbers are zero. The cotangent
splitting gives h0=1. Serre duality identifies h2 with h0(T tensor K)=1:
the latter bundle is the sum of O_E external O(-2) and O_E external O.
Thus h1=h0+h2-chi=2. This supplies the tuple (1,2,1) by Riemann--Roch and
Serre duality. It is postrelease verification, not a new blind derivation.

## 01AS, 01AT and 01AU: complete proof comparisons

For 01AS, the base pullback is the adjunction isomorphism
p^*p_*(eta^*A) -> eta^*A, verified fibrewise. The cotangent sequence kills
the relative O(-2) quotient on sections. The sole base differential descends
under the actual translation exactly when its constant gluing multiplier
is one; the same constant trivialization then descends to A=O_S.

For 01AT, evaluation of the rank-one canonical direct image gives a vertical
effective Cartier zero divisor. On the irreducible full reduced fibre it is
a multiple of that fibre, whose conormal is trivial. Adjunction and Serre
duality give h0=h2=1. The ideal sequence and divisor Riemann--Roch give chi=0,
and hence h1=2. The new source guard changes only the iteration marker;
that typography edit supplies no separate editorial event.

For 01AU, the local critical ideals (x,y) and (xy,xz,yz) identify the first
deformation sheaf with the reduced singular-locus structure sheaf. Together
with trivial dualizing line this gives exactly Definition 2.1 of SS2002.
The source uses the notation X_SS=S and S_SS=the normalization. Propositions
2.4–2.6 give the normalization types; Proposition 3.1 gives diagonal Hopf
normalization, and Proposition 4.1 gives translation gluing in the ruled
case. The rational and Hopf differential vanishings, the ruled descent
criterion, and the unitary maximum-principle argument agree with the frozen
derivation and have been read throughout in the printed proof.

## 01AV: exact pair map for the different Euler computation

The reopened author PDF of SS2002 has SHA-256
88c238a3151ae5e4fa68bee7dfd6158b6075f2a72d407d16e9262a7ac7dbcfec.
Proposition 2.6 on printed p.6 specifies a Hirzebruch surface, two disjoint
sections, two distinct ruling fibres, and a blowup point on the union of
the sections in each of those fibres. The conductor is precisely the two
strict transforms of the sections, the two strict transforms of the fibres,
and the two exceptional curves. These are boundary blowups for the
following explicitly chosen coordinates.

The two disjoint sections give two quotient line bundles of the rank-two
bundle on P1. Their joint quotient is a fibrewise isomorphism to their direct
sum. Projectivizing supplies a bundle isomorphism carrying the two sections
to zero and infinity. A Mobius coordinate sends the two distinguished base
points to zero and infinity. On the remaining G_m, both line bundles are
trivial; their fibre-coordinate ratio gives

  (base coordinate, fibre ratio):
  Hirzebruch surface minus those four curves -> (C*)^2.

Both blowup centres are in the deleted boundary. Each blowup is an
isomorphism over its complement, and the complete inverse-image boundary
is exactly the conductor hexagon. Thus the displayed map identifies the
actual pair complement T minus C with (C*)^2. No arbitrary hexagon is
substituted for this pair.

For the actual normalization quotient eta:T->S with double image D, the
induced quotient map T/C -> S/D is a continuous bijection between compact
Hausdorff spaces, hence a homeomorphism. Both are the one-point
compactification of the common complement. Since (C*)^2 is homeomorphic to
T^2 x R^2 by polar coordinates, its compactification is the Thom space of
the trivial oriented real plane bundle on T^2. Its reduced cells have
counts (1,2,1) in dimensions (2,3,4), and relative Euler number zero.

The actual D is three copies of P1 with all three zero points identified
and all three infinity points identified, as specified at the beginning of
Section 5, printed pp.16–17. Taking two vertices, two arcs and two faces on
each P1 induces cells (2,6,6) on D and Euler number two. The exact pair
therefore has e(S)=e(D)+e(S,D)=2+0=2. This differs from the printed
normalization-subtraction calculation 6-6+2. No assertion is made that the
entire original S has any particular minimal CW attaching maps.

## 01AW and 01AX: local maps and the signed exterior-basis transport

For 01AW, the printed proof's resolution, Stokes identity, zero periods on
plumbing neighbourhoods, normal direct-image descent, finite fibre-product
agreement, and topological quotient descent were all read. Its primitives
are continuous on S and holomorphic on the normalization. Their differences
are flat locally constant sections. The resulting Cech class is independent
of primitive constants, and its kernel vanishes by the unitary maximum
principle on compact resolved components. Holomorphic descent to O_S is
not used.

For 01AX, the frozen draft uses support cohomology and a sufficiently small
tube. In the comparison, the printed proof supplies a direct argument that
avoids any unproved fixed-tube retraction claim: pi1(U*) -> pi1(U) is
surjective by general position off a divisor; the crossed-homomorphism
formula gives injectivity on H1 with the exact local coefficients. Koszul
acyclicity gives H1(U*)=0. The assertion is repeated on every small disc,
and proper base change identifies the direct-limit stalk with H1(S,A).
The integral-to-holomorphic Leray edge map and exponentiation identify the
holomorphic line with the actual unitary character. Applying 01AW then
gives the torsion-free cotangent group. The complete printed comparison is
postrelease and is recorded as such.

The durable preproof program checks the homotopy identity on all sixteen
exterior basis vectors. The new program uses nonzero minors and square-zero
rank bounds instead. With nonzero coordinate a0, choose columns indexed by
k-subsets of {1,2,3} and rows obtained by adjoining 0. These submatrices are
a0 times the identity, with determinants a0, a0^3, a0^3, a0. The relations
d_(k+1)d_k=0 and dimensions (1,4,6,4,1) force ranks (1,3,3,1), hence zero
cohomology in every degree.

For a nonzero coordinate aj, let sigma exchange 0 and j. On exterior degree
k define P_k(e_I)=sign(sigma|I)e_sorted(sigma(I)). Put a'_i=a_sigma(i).
The code verifies for each j and every k that

  D_k(a) P_k = P_(k+1) D_k(a'),  and  P_k^t P_k = identity.

This is the exact chain isomorphism that transports the pivot calculation;
no unsigned basis permutation is assumed.

## Bounded earlier-program search

The restored canonical ledger associations for A.4.2, A.4.6 and A.4.8 were
read after release. They describe historical proof/intake/source checks and
the printed product, normalization-additivity and Koszul calculations. They
identify no old target program. This is a conclusion about those selected
rows only. The new computations are compared with the displayed methods;
no global assertion that earlier programs do not exist is made.
