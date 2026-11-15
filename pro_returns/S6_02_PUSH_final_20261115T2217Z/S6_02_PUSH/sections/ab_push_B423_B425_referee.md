# Independent referee of B.4.23 and B.4.25

Reviewer: limits_ab. Full source read and mathematical PASS communicated to root and boundary_d before integration. This record was saved on 2026-11-15 after the eighth checkpoint. It does not add a numbered result.

## B.4.23: exact scope passes

The retained elliptic axis is disjoint from every modification in B.4.21. Thus its intersection with the generic exceptional curve is exactly `[-s^12]` in the smooth family `C*/a(s^12)^Z`. A holomorphic logarithm of the nonzero contraction gives a smooth marking of that elliptic family. The section has integral loop class `(12,0)`, multiplied by the positive degree of any finite base change. A section extending over the disc would null-homotope that loop, which is impossible.

For a hypothetical proper analytic divisor closure of the exceptional curves, its intersection with the elliptic axis is an analytic curve. The horizontal component has generic degree one. After normalization, properness and one-dimensionality make it finite of degree one over the nonsingular disc, hence an isomorphism. Vertical components cannot change this horizontal extension. Proper images under further finite modifications therefore cannot produce the missing closure. The same reasoning applies to a proper analytic graph of a generic blowdown after resolving that graph.

For the deformation assertion, the hypotheses on both the original base coordinate and the absence of conductor intersections are essential. They give the exact sequence

`0 -> O_P1(-1) -> N_(C/Y) -> O_P1^2 -> 0`.

Its extension class vanishes, and its map on global sections is an isomorphism. The unobstructed two-dimensional embedded deformation space therefore maps locally biholomorphically to the two original parameters. Every nearby fixed pair contains a rational curve, contradicting its being an ordinary complex two-torus. If an additional conductor is introduced along the persistent elliptic axis, the curve meets that conductor and the normal sequence changes. The proposition explicitly leaves that escape route open.

## B.4.25: exact scope passes

The equivariance of an anticanonical bivector is `f(alpha z,beta w)=alpha beta f(z,w)`. Under `0<|alpha|<|beta|<1`, the sole generic monomial is `zw`; the only extra monomial is `w^(N+1)` when `alpha=beta^N`, with at most one integer `N>=2` at each parameter. No Picard-sign convention enters this computation.

For `alpha=q^m kappa(q)` and a nonzero contracting limit `beta(0)`, the Rouché radius in the proof yields `m` nonzero resonant roots for every sufficiently large `N`. Different `N` give distinct roots. Nonresonant parameters also occur arbitrarily near zero because the resonance locus is a countable union of discrete sets. Hence `h^0(-K)` has infinitely many isolated upward jumps accumulating at zero.

On any smooth proper completion, `pi_* K_X^-1` is a torsion-free coherent sheaf on the disc and therefore a vector bundle. The torsion of `R^1 pi_* K_X^-1` has no punctured support after shrinking. The displayed multiplication-by-`q-a` exact sequence consequently forces `h^0(-K)` to be constant at every sufficiently small nonzero parameter. This is the required contradiction. Passing to the reduced unique dominating component and resolving it is legitimate: the resolution is an isomorphism over the entire smooth punctured family and remains proper. Singular or nonreduced central structure therefore cannot evade the argument. A finite base change preserves the two hypotheses on the multipliers.

The elementary basis conversion in the Oda comparison checks algebraically: if `v1=n`, `v2=-n+a n'`, then `a n'=v1+v2`, so `lambda=t^a` acts with both eigenvalues tending to zero. I did not independently reopen Oda's original pages; the primary-source verification of that comparison belongs to boundary_d. The main resonance/no-completion proof does not depend on the Oda comparison.

These results concern the specified auxiliary Kato/Hopf replacements. Neither is an unrestricted nonexistence theorem for the actual torus completion.
