# Derivation before target proof: 01AG

Owner: `cdp:st:A.2.2`. Checker: `i_provenance`.
Inputs read: the exact target statement, empty cited-input supplement, and
`S6_SERIES_PUBLISH_II_01AG_local_setup_supplement.tex` (SHA
eeb5875234261d21eff86129c0805fed7f38b3ba33a1bb346017c71b8af0888b).
The latter supplies the reduced Cartier hypersurface in dimension n+1, the
Jacobian convention, and the exact A.2.1 fractional-ideal identification.
No target proof or prior target check has been read.

Work locally with R=O_Y/(F), its total ring of fractions Q(R), and the finite
normalization B. The Jacobian ideal J contains a nonzerodivisor because its
restriction to the generic point of each reduced component is the unit ideal.
I first derive J contained in the conductor c=(R:B).

Choose a generic linear coordinate direction z making F, up to an analytic
unit, a monic Weierstrass polynomial f over the regular analytic ring
A=C{z_1,...,z_n}. Then R is finite free over A, and its generic algebra is a
product of separable field extensions. The trace-dual lattice of A[z]/(f) is
f'(z)^(-1)R. One direct justification is Lagrange interpolation at the generic
distinct roots: Tr(z^j/f') is zero for j<d-1 and one for j=d-1. The bases
1,z,...,z^(d-1) then give the perfect trace pairing with f'^(-1)R; the resulting
triangular coefficient matrix has unit antidiagonal. This identity descends
over A because f is monic.

For b in B and r in R, br is integral over A. Its trace is integral over A and
belongs to the fraction field of A, hence lies in A by normality of A.
Consequently B lies in the trace-dual f'^(-1)R, so f'B is contained in R.
In particular f' belongs to the conductor. Modulo F, differentiation of the
unit times f changes this derivative by a unit. The set of coordinate
directions for which this construction applies is open and spans the ambient
tangent-coordinate space. Choosing n+1 linearly independent such directions
expresses every F_xi as a constant linear combination of their derivatives.
Thus J is contained in c. This argument works for a reduced hypersurface with
several components as well, using the total product of fraction fields.

Primary algebraic input consulted during this derivation: Stacks Project
49.8, tag 0BW0, defines the complementary trace module and proves integrality
of traces over a normal base; 49.12, tag 0BWB, Example 49.12.5 gives the monogenic
different (f'). URLs https://stacks.math.columbia.edu/tag/0BW0 and
https://stacks.math.columbia.edu/tag/0BWB. The analytic application above is
the explicit Weierstrass finite-ring argument, not an unstated identification
of analytic and algebraic geometric objects.

Now bJ is contained in R for every b in B, proving B contained in J^(-1).
Tensoring this injection with the invertible N* and using the supplied A.2.1
isomorphism K=N* tensor J^(-1) gives the canonical injection
eta_*eta^*N*=N* tensor B -> K. The projection formula identifies its domain;
all maps restrict to the identity fractional inclusion on the regular locus.

For the kernel formula, every B-linear map JB->B extends after passage to
Q(R) to multiplication by a unique q in Q(R), because JB contains a
nonzerodivisor. Thus D=Hom_B(JB,B) is exactly the fractional set
{q:qJ subset B}. Since c is an ideal of both R and B contained in R,
(B/c)/(R/c) is canonically B/R. The displayed map sends q to j |-> qj mod R.
Its kernel consists exactly of q with qJ subset R, namely J^(-1). It is
R-linear and the quotient is independent of the representative modulo c.

Finally the conductor square is the exact sequence

0 -> R -> B direct-sum R/c -> B/c -> 0,
r |-> (r,r mod c), (b,rbar) |-> b mod c-rbar.

The last map is surjective from its first summand. A pair in its kernel has
b-r in c for a lift r in R, hence b in R, so the kernel is precisely the
diagonal copy of R. Tensoring with a locally free E preserves this sequence.
Finite analytic pushforward and the projection formula identify its terms
with eta_*eta^*E, E|D_c, and eta_*(eta^*E|tilde D_c). Taking global sections
is left exact and yields exactly the displayed difference map and its kernel.
For E=V tensor A the bundle is locally free, so the criterion applies and
vanishing is exactly injectivity of that difference map.

Every asserted inclusion and kernel has thus been derived with its actual
morphism. No separate finite numerical computation occurs. Prior Paper I
normalization/cohomology exposure is disclosed; target comparison remains
pending and no independent event has yet been claimed.
