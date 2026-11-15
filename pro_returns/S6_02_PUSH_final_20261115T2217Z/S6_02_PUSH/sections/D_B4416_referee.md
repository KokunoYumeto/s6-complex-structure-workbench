# Independent referee of B.4.16

15 November 2026. **PASS after the stated coefficient-system correction.**

I checked `sections/ab_push_regular_cap_dual.tex` against the two analytic
charts already independently verified in B.4.15, and inspected the exact
incidence/collapse code `code/ab_push_regular_cap_dual.py`.

The two triples at an even/odd node are exactly `(V_i,V_j,H_j)` and
`(V_i,H_i,H_j)`. Their diagonal is `V_i H_j`. Over the twelve nodes these
give the indicated cylinder. Each top edge is free at the first stage;
each diagonal is free after the top triangles have been removed; each
remaining new vertex then has just its vertical edge. Thus all 36
elementary collapses are valid relative to the old horizontal cycle.
The chain retraction and the primitive angular cocycle in the code agree
with this actual collapse, rather than merely reproducing Betti numbers.

When local horizontal branches acquire global identifications, the new
space is still the mapping cylinder attached along the existing local
cycle map. Its deformation retraction onto the original dual complex
does not require that attaching map to be injective. A connected
holomorphic group preserves the finite sets of component and connected
stratum labels; toroidal subdivisions preserve the underlying
polyhedral homotopy type. Consequently the result applies successively
to precisely the operations listed, with no assertion about arbitrary
analytic replacements.

The first version of the final spectral-sequence paragraph needed a
coefficient-system qualification for self-crossings. Ordered branch
tuples must be taken with the alternating/sign summand; unordered branch
strata carry the corresponding orientation local system. Ordinary
constant coefficients on unordered strata are not a substitute when
branches permute. The revised proof correctly uses complex coefficients
and alternating direct summands, so averaging over the finite
permutation group is available and the augmented local simplex complex
is exact. Its `E2^(1,0)` is the first cohomology of the dual complex,
and no higher differential enters or leaves that position. This gives
the needed injection into H1 of the central space. A nonzero integral
first cohomology class remains nonzero over C because first integral
cohomology of a finite complex is torsion-free. The combinatorial
collapse certificate itself remains integral.

Thus the resulting obstruction to a simply connected semistable centre
is valid. It is an obstruction only for the specified generated class of
insertions, connected-action twists and toroidal subdivisions; it does
not settle the unrestricted analytic filling question.
