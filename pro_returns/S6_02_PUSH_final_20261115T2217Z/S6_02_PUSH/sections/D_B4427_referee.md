# Independent referee of B.4.27

Referee: boundary_d. Full source read: `sections/B_log_base_modification.tex`, 2026-11-15, approximately 21:04 UTC.

**Verdict: PASS in the stated category of usual-analytic-topology torsors under the specified associated logarithmic torus.**

The bounded character sheaf is correctly computed, rather than replaced by the full logarithmic torus. At the strict R-axis, the first character has zero normal order, because its bounding period is q. The second period q r^12 has positive order there and on every other boundary component. At a crossing, a character with nonzero second coefficient is bounded above and below by suitable signed multiples of that period; if its second coefficient is zero, exactly the first-character support condition remains. This gives the two displayed divisor-unit sheaves, also after blowups at non-toric points of the exceptional boundary.

The exceptional curves form a tree of rational curves. Proper base change computes H2 of the blown-up bidisc by restriction to those curves, with H1, H3, and H4 zero. Higher coherent cohomology vanishes under point blowups; the given local Laurent splitting is consistent with the usual calculation. The exponential sequence therefore identifies Picard with the integral exceptional lattice and kills H2 and H3 of O*. The strict-transform exceptional divisor classes form an integral basis because their intersection matrix is unimodular.

The divisor-order sequence has the direct sum of constant sheaves on individual components, so it introduces no additional graph-cohomology term. Its H1 is zero; its H2 consists exactly of the exceptional-curve summands. Both support divisors contain every exceptional curve, making the order-to-Picard map surjective. Thus each divisor-unit sheaf has H1 zero and H2 equal to one copy of Z per exceptional curve, via the actual order map.

In these coordinates the period map on H2 has, at each exceptional curve, the diagonal block with entries 12m ord(Q) and 12m ord(Q)+12n ord(R). Both are positive integers. Unit factors have no hidden contribution because the H2 order map is an isomorphism. The resulting integral injection gives H1 of the associated logarithmic torus zero by its exact quotient sequence. This includes the unblown bidisc as the zero-rank case.

The final restriction contradiction is valid: a torsor extending to the blown-up base would be trivial there, and hence trivial on the original punctured bidisc, contradicting B.4.24. No claim that an arbitrary proper analytic cap or its flattening supplies such a torsor has been made. Local multisections after flattening are not silently promoted to a global finite multisection over the exceptional tree.
