# Independent referee: E.2.16

Reviewer: boundary_d. 15 November 2026. Full source reviewed:
`sections/E_cusp_reducedness.tex`, together with
`code/e_push_interior_cusp.py/.out/.json`.

**Conclusion: PASS at the stated scope.** The conclusion is reducedness
and irreducibility of the actual remaining cusp surface, with Euler
characteristic two and first rational Betti number two. It does not yet
classify that surface analytically.

1. E.2.14 and E.2.15 exclude the finite-root and ordinary constant-image
   degenerations respectively, while E.2.12 excludes a cusp constant
   image. A nondegenerate limiting projective transformation therefore
   preserves the three distinct labelled values. E.2.13 supplies exact
   finite multiplicities, not merely divisibility.

2. The degree-one Leray calculation is over the punctured projective
   line, which has cohomological dimension one for these local systems.
   Its invariant H1 space has rank one. Alexander duality on the actual
   S6 gives the number of irreducible components: top-degree rational
   cohomology of a compact pure complex surface has one generator per
   irreducible component, also when the surface is nonnormal. Thus the
   total of three components forces one in each fibre.

3. The meridian quotient is valid without a stack structure. The singular
   subsets of the reduced divisors have real codimension at least four
   in the smooth threefold; a generic null-homotopy disc avoids them and
   meets only smooth divisor points. The normal generation by meridians
   follows. The local defining function has the exact multiplicity of
   its divisor, so the induced quotient is the triangle presentation
   displayed in the proof.

4. For d at least two, the stated hyperbolic inequality fails only at
   (m,n,d)=(3,4,2). In the hyperbolic cases the displayed cosh is strictly
   larger than one: this is equivalent to alpha+beta+theta<pi. The
   product trace is -2 cos(theta); its eigenangle pi-theta has exact
   projective order d. The two factors have exact projective orders m
   and n. The exceptional permutations have product (24), with the
   stated composition convention. Hence the quotient cannot be trivial.

5. Euler additivity uses the proper smooth fibration off three points
   and zero Euler characteristic for ordinary tori and the two finite
   free quotients. It therefore gives chi(S)=2. For b1(S), I reopened
   the original Honda--Viaclovsky arXiv v1 PDF at
   https://arxiv.org/pdf/2504.14420 (tool refs turn493view0/turn493view1).
   Printed page 11, Corollary 3.7 and its proof (3.22)--(3.23) give the
   H1 invariant-cycle equality under exactly the irreducibility now
   proved. The equality is independent of their incorrect unrestricted
   converse in Theorem 1.2/Theorem 3.2, audited in B.4.17. The cusp
   invariant rank is two, so the asserted value follows.

No use of a Kahler completion, unproved meromorphic comparison, or
classification of nonnormal cusp surfaces enters this proposition.
