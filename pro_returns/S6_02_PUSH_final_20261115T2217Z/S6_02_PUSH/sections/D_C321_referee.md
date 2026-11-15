# Independent referee: C.3.21, actual delta-line square

**Result:** pass, with a suggested expansion of the final local Weierstrass checks. Referee: boundary_d. The proof concerns the actual line on the actual Lefschetz four-manifold, not the auxiliary normalization of Part B.

## Actual geometric comparison

The weighted-rescaling formulas identify the actual page interior with `b^3=a^4+1` and its marked map with `t_epsilon=(a^4+1)/(1+epsilon a^4)`. The change from the cover ramified over the original cusp to the cover with twelve unramified cusp preimages is retained explicitly. The added point is over the ordinary value `1/epsilon`, not over the cusp. The genus-three compactification has one point at infinity.

Keeping the cusp product modification inside `r0<epsilon` makes its intersection with the page exactly twelve nodal neighbourhoods. The remainder is the original marked torus quotient. On that remainder the explicit eta coordinate gives the varying Picard section P, including its mixed base--fibre class. A smooth translation origin exists because the punctured page retracts onto a graph. The argument uses smooth dependence in the base and fibrewise holomorphic lines; it does not assert holomorphic dependence of the origin or of the affine torsor.

## Excision and extension

For a full I1 neighbourhood E, Poincare--Lefschetz duality gives `H^2(E,boundary E;Z)=H_2(E;Z)=Z`. The primitive generator is the class of the reduced irreducible fibre. Its image in the page surface is the pullback of a point on a surface with boundary, hence zero. Therefore restriction of absolute H2 cohomology to the untouched exterior is injective. This excludes an additional absolute Chern class in the twelve nodal clutching regions.

The remaining regular boundary has an actual trivial marked line. It can be capped with the product extension whose Picard section is P near the added point. Boundary gauge changes lie in the radical of the relative intersection pairing, as proved in C.3.20, so this choice cannot alter the square. No global diffeomorphism of the actual surface with its Jacobian is assumed.

## Integral Leray comparison

For both surfaces the local invariant-cycle calculation gives `R^1 pi_* Z=j_* Lambda`, `R^2 pi_* Z=Z`, with the same integral fibre intersection pairing. The filtration-one mixed term is `E_infty^(1,1)=H^1(C,j_*Lambda)`: there is no possible incoming or outgoing differential in this bidegree. The map to the smooth-locus group is injective by the low-degree Leray sequence for the open immersion j. Thus the exterior Picard calculation identifies the actual mixed class with the Jacobian Poincare mixed class, up to dualization.

In total degree four the only nonzero graded term is `E_infty^(2,2)=H^2(C,Z)=Z`. Multiplicativity identifies the square with the cup square of the mixed term, using the fibre pairing. Filtration-two base twists contribute no square or cross term, because filtration three is zero on this base. Integral differentials elsewhere in Leray do not affect this argument. Dualization changes the sign of the mixed class and preserves its square.

## Explicit final local checks

The original model, obtained directly by reversing the substitutions in B.3.4, is

`y^2=x^3-3 t^3(t-1)x+2 t^4(t-1)^2`,

with `P=(0,-sqrt(2)t^2(t-1))` and discriminant `1728 t^8(t-1)^3`.

* At `t=s^3`, use `x=s^4 X`, `y=s^6 Y`. The new fibre is good; P is `(0,-sqrt(2)(s^3-1))` and is away from O.
* At `t=1+s^4`, use `x=s^2 X`, `y=s^3 Y`. The new fibre is good; P is `(0,-sqrt(2)s(1+s^4)^2)` and is away from O, including its limit `(0,0)` on the smooth fibre `Y^2=X^3-3X`.
* At `q=1/t`, use `x0=q^2 x`, `y0=q^3 y`. The I1 model has P `(0,-sqrt(2)(1-q))`, which limits to a smooth nonidentity point of the nodal cubic. It is disjoint from O.

The units in the actual `t_epsilon` cover preserve these local conclusions. The added ramification point lies over a good fibre, so introduces no new intersection. All twelve bad fibres of the minimal Jacobian are I1, and the two finite bad fibres become good. Consequently its Euler number is 12, its holomorphic Euler characteristic is one, and P and O are disjoint sections of square minus one. Thus `(P-O)^2=-2`, with no component correction. The actual relative Euler square is therefore minus two.

## Scope

This audit validates C.3.21. It does not by itself identify a one-loop monodromy class. Combining it with the independently calibrated common-sign lemma C.3.22 gives the six-loop cap integer zero. Passing from that six-loop integer to the original one-loop mapping class still requires the integer-level additivity and relative-normalization argument.

Primary height/intersection reference used in the containing manuscript is Shioda (1990), Theorems 8.4 and 8.6; the local disjointness checks above avoid inferring the needed intersections from an auxiliary numerical height alone.
