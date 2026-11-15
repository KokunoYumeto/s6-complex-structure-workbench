# C.1--C.5 work record

All five assigned items are resolved by statements C.1.1--C.5.1 in sections/C_special.tex. No priority claim is made. The distribution and Siegel identities are classical; the family evaluations and expansions are explicit derivations in the supplied normalization.

## Read and checked

- S6_02_PUSH_D_push.tex: K1 mean-zero/isogeny proof; K2 Albanese nome and natural-boundary proof; K3 local coefficient identities; K4 differentiated theta formula.
- S6_02 return CD.tex C.1.1 and AB.tex A.1--A.5, B.4.2: special phase, Albanese projection lattices, exact2Z classification, reflection affine corrections and extension.
- Du--Guo--Kusakabe--Xie v1: p2:thm:exact-period (Theorem1.4); corresponding v2 omits it. Both attached sources and arXiv pages opened. No inference from the omission.
- Bourdon--Clark--Stankewicz, arXiv1411.2742v3: Theorem4.15(a) p23 and definition of Olson groups p2; applies to all orders and all curves over Q(j). Hypotheses verified for the actual rational twist.
- Shin, arXiv1009.2253v6: equation1, Remark2.2, Proposition2.3; modular-unit normalization checked against our theta product.
- Sutherland 18.783 Fall2023 Lecture20: Theorem20.12 and Corollary20.13, including proof via modular polynomials for arbitrary imaginary quadratic orders.

## Exact calculations run

Cspecial_division.py computes division polynomials through9, discriminant, primitive exact-order factors, squarefreeness and candidate CM minimal polynomials. Cspecial_relations.py proves both sixth-order closed forms and writes an exact resultant relation for all seventh-order norm values, including complex parameters. Cspecial_psi16.py computes a factored sixteen-division polynomial for the main analytic workstream. Cspecial_reflection.py verifies integral conjugation identities, finite affine vectors, norm equations, rational local corrections and the integral cusp cocycle.

## Numerical calculations run

Cspecial_torsion_numerics.py evaluates every root of exact order2 through8 (13 smooth roots) at110 decimal digits by elliptic integrals and theta functions independently of the local-height formula. The output supplies at least70 digits of t,tau,v,N,N^12 and both norm and lattice-relation residuals. All discrepancies are below1e-90; the largest norm discrepancy is below2e-108. It checks the two central values and phases as well. Cspecial_expansion_checks.py compares the independently solved wp zero with the new i and rho Taylor coefficients. These checks support exact proofs, and are not labelled numerical certificates.

## Corrections and refinements

Lead12's holomorphy domain is a punctured open disc; the first invariant has a pole at w=0 and a natural boundary at its larger radius. No claim of inclusive boundary holomorphy is made. The rho point is neither a maximum nor a minimum; its first coarse-base term is (7/192)Re(t) in logN, followed by a negative |t|^(4/3) term. The universal endomorphism distribution formula requires a nonzero endomorphism; it in fact holds for all nonzero isogenies with distinct source/target lattices, with the discriminant scaling explicitly included. The Q(j) torsion theorem is Parish's result as precisely recorded in BCS Theorem4.15(a), rather than an unsupported reference to the different Bourdon--Clark Galois-representation paper.

## Literature searches, 15 November2026

Queries: CM elliptic curve Q(j) torsion Parish theorem; Bourdon Clark Parish Theorem; Siegel functions12N modular units theorem Kubert Lang; generation class fields Siegel Ramachandra; Cox Theorem11.1 j algebraic integer; MIT j invariant CM algebraic integer. Sources are listed in references_Cspecial.bib, each with verification status. These searches locate classical sources for the methods; they do not establish a novelty claim for the explicit family formulas. The numerical output and source expansions are independent evidence for the prompt's already conjectured special values.
