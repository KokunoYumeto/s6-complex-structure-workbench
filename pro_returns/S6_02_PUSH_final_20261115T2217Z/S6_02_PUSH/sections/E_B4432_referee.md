# Independent referee of B.4.32

**Verdict: PASS at the stated global proper-filling scope.** Reviewed by classification_e, 15 November 2026. The final TeX `B_global_loop_defect.tex` has also been read in full; it includes the requested clarification that semistable reductions are local in the ordinary base, with common refinements for comparisons.

I read the full working proof in `D_global_loop_defect_working.md` and checked its dependencies against B.4.19, B.4.24, B.4.30, and B.4.31. The radial connecting class is correctly taken in the cokernel of `T−I` before projecting to `Lambda_Q/Q delta`; no single-valued additive lift on the puncture is assumed. Restriction to an `e`-fold root is the sum `1+T+...+T^(e−1)`, which becomes multiplication by `e` in that quotient. This justifies normalized roots and traces.

The ordinary-reference overlap calculation uses the actual triangular Lie-frame changes, fixed delta column, and finite-root connector cancellation. Its remaining scalar powers have radial defect only in the delta line. The cusp change `G(s)+6v delta` likewise has zero projected defect; it does not identify the two axial extending origins and does not discard the separate F clutching term.

The local comparison is valid because B.4.31 forces every angular meridian into the primitive delta line. The saturated normalized logarithmic forms therefore have residues `(0, integer)`, so the finite chart chain gives an actual bounded logarithmic difference of any two extending sections of the same connected cap. Connectedness follows from proper Stein factorization over the normal base. Norms and further roots preserve the normalized comparison. An arbitrary unknown common origin can still have essential translation growth, which the statement correctly leaves uncontrolled.

The local normalized classes patch to a global flat section in the actual quotient local system. The two displayed peripheral fixed lines have zero intersection. The optional finite-orbit argument is also correct: averaging first kills the gamma coefficient, and the two elliptic unipotents then kill the remaining coordinates.

The stronger initial scope follows from the revised B.4.4 and B.4.31: retain the main component of any proper analytic filling, normalize and resolve it without changing the puncture, extend the marked map, and resolve its graph and central support with multiplicities retained. Only local one-parameter semistable constructions are subsequently used. No global threefold semistable reduction is needed.

This referee establishes the loop-defect statement only. B.4.33 must separately construct the cap-derived associated-log-torus torsor on the whole modified cusp base and compare its global origin with both reference origins.
