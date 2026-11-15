# Independent referee of C.3.12

**Verdict: the stated Hausdorff-target collapse theorem is proved by the written argument.** This is a theorem about the literal regular-fibre translational leaves. It does not prohibit a cusp quotient obtained after changing those leaves, and it does not affect the genuine smooth delta-circle quotient used in C.3.10.

The period formula is exact: the u column of `Z=sB0+C(q)` is `(s+C12(q), mu(q))`, so real translation by r u multiplies the two toric characters by `q^r exp(2πir C12(q))` and `exp(2πir mu(q))`. The cone over the edge joining 0 to e1 has character coordinates `x=z1`, `y=q/z1`, `z=z2`, giving `xy=q`, with z invertible. Thus the claimed local chart is the actual toric chart, with the period units retained.

For fixed x,z nonzero and 0<r<1, a path `(x,q/x,z)` approaching the dense component point P(x,z) is translated to a path approaching the double-curve point `Q(exp(2πir mu0)z)`. Equality of the h-images on each regular fibre, continuity, and uniqueness of limits in a Hausdorff space give the stated limiting equality. Comparing two r values yields invariance under `z -> exp(2πia mu0)z` for all real a, first for |a|<1 and then by iteration. Delta-circle translations supply arbitrary phases. Since Im(mu0) is nonzero, the combined multipliers exhaust C*. Hence the dense component image, and by density the entire irreducible W, is constant.

The separate variable-r argument for independence of x is valid: q_n=e^(-n), r_n=-lambda/n gives q_n^(r_n)=e^lambda, while both holomorphic-unit powers converge to one. The w direction supplies phases. In fact, the fixed-r limiting equality already proves independence of x, but retaining the separate argument creates no gap.

The displayed cusp value satisfies sin²(πmu0)=3 and is nonreal. The proof only needs its nonzero imaginary part, not the selected logarithm branch or numerical value. The raw-coordinate comparison at the end is also correct: `(Im Z)^(-1)(0,rT)=(-r,0)+O(T^(-1))`, whereas all paths converge to the same toric edge point.

## Provenance and correction of the attempt report

The supplied background already records nonextension of the fixed raw character coordinate: `background/notes/A1_notes.md`, candidate A1-1, and `background/S6_SURVEY_20261112.md`, item F9, give distinct limiting character values at one triple point. Those background notes are not treated as authoritative proofs; the local toric calculations above were independently checked. C.3.12 has the stronger stated scope of every Hausdorff-valued continuous map retaining the regular translational leaves. No novelty claim is made.

My earlier attempt report asserted an actual S6-to-S3 rank-three quotient and thereby identified a marked (3,4) attaching knot. That assertion is superseded and withdrawn. The abstract finite Seifert multiplicities and the algebraic (3,4) Milnor cover do not identify a marked global cusp knot or the annular twist's framing. The genuine delta quotient and C.3.10 remain valid.

Referee completed 15 November 2026, independently of the source's informal quotient assertion.
