# Independent referee note on B.4.3

**Verdict: the stated obstruction and its carefully restricted scope follow from the cited primary statements.** This review does not extend the result to arbitrary self-crossing analytic central fibres with merely prescribed normalization strata, and does not assert that every unknown vertical component is Moishezon.

## Primary-source checks

Chen, K.-W. (2026), *On the Hodge Structures of Global Smoothings of Normal Crossing Varieties*, arXiv:2404.19229v2, was opened at the version-specific arXiv HTML URL. The PDF fetch failed in this browser tool; the complete version-specific primary HTML was accessible. Definition 2.3 imposes K1 on every nonempty intersection of irreducible components, including individual components. In Theorem 2.4 the K1 qualifier appears explicitly between parts (2) and (3), and applies to both parts (3) and (4). Part (4) asserts E1 degeneration for the nearby ordinary Hodge–de Rham sequence, after shrinking the parameter disc. Neither the stronger K2 hypothesis nor a local invariant-cycle hypothesis is needed for this particular conclusion. Those extra conditions concern stronger Hodge-theoretic conclusions elsewhere in the source.

Graf, P., & Kovács, S. J. (2014), *Potentially Du Bois spaces*, Journal of Singularities, 8, 117–134, DOI 10.5427/jsing.2014.8i, was opened in the original author-hosted journal PDF. Section 1.D, printed page 120, states that proper Du Bois varieties have the canonical surjection from singular to coherent cohomology and lists normal-crossings singularities among Du Bois singularities. The statement uses properness; projectivity of the central fibre or total space is unnecessary. The conclusion applies to self-intersections of an algebraic component as well, since the Du Bois property is local and the singularities are normal crossings.

Raw search/open records are retained in `evidence/E_C_search17.json` through `E_C_search20.json`. The existing root bibliography keys and metadata were independently checked against the primary results.

## Mathematical derivation

Conditional on the proved specialization-surjection statement B.4.2, simple connectivity of the smooth six-sphere fibre gives H¹(D;C)=0. The root-curve direct images O⊕O(−1) give h¹(X,O)=1 by the Leray edge sequence, because the weighted projective line has no H¹ or H² of O and O(−1) has no section. Proper flat upper semicontinuity therefore gives h¹(D,O_D)≥1. Flatness follows directly from the reduced normal-crossings local equation of the central divisor in the smooth total space.

The independent lower-bound argument also checks: H² and H⁴ of S⁶ vanish, so c₁=c₂=0 and analytic Riemann–Roch gives χ(O)=0. A holomorphic top form is closed, exact by H³(S⁶;C)=0, and has zero L² norm by Stokes; hence h⁰(K)=h³(O)=0. Consequently h¹(O)=1+h²(O)≥1. This avoids any inference from tangent-bundle cohomology.

The algebraic contradiction follows from the proper Du Bois surjection in degree one. For a simple-NC central fibre satisfying K1, Chen's Theorem 2.4(4) gives b₁=h⁰(Ω¹)+h¹(O) on a nearby fibre, contradicting b₁=0 and h¹(O)≥1.

If all components are Kähler, their closed smooth strata are Kähler. If all are Moishezon, take a projective modification of a component; an inverse-image component dominating a closed stratum is projective, and general relative hyperplane sections give a generically finite projective cover of the stratum. Meromorphic function fields then have the same transcendence degree, proving that the stratum is Moishezon. Smooth Moishezon manifolds satisfy the ddbar lemma; Chen §2.1 explicitly recalls the dominance implication. Thus the two component hypotheses really imply K1.

Finite base change leaves the nearby fibre biholomorphism type unchanged. Every contradiction therefore applies for all positive exponents. No gap was found in this stated scope.
