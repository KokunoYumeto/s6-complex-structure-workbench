# Independent derivation before target-proof release

Checker: i_provenance_recovery. Created: 2026-11-21T21:04:53.862060+00:00. The target printed proof, its historical check outcomes, and other agents’ argument records have not been opened. Related Paper I mathematics and already released Paper II inputs were previously read; those exposures do not include this target proof. Inputs below are exact statement-only packets and their supplements. The proofs here are my own current derivations. No source, event ledger or canonical defect record is changed.

Owner: wbII:lem:extending-gluing.

Use the exact family in input B1: y^2 z=x^2(x+z)+t z^3. On the finite chart z=1 the branch b(t)=sqrt(36+t) with b(0)=6 is holomorphic for a small disc, and (3,b(t)) lies on the curve because3^2(3+1)+t=36+t. The section O=[0:1:0] is disjoint from this finite section. Both are Cartier on the total surface: near P,2y is a unit and x-3 cuts out the section; near O in chart y=1, the equation z=x^3+x^2z+t z^3 has derivative1 in z at O, so x is the fibre coordinate and x=0 cuts out O. The total surface is smooth also on the finite chart, since the derivative of its equation in t is-1. Thus B=O_C(P-O) is an invertible sheaf on the whole family.

At t=0 the exact normalization is x=u^2-1,y=u(u^2-1). Its projective form is [u:v] -> [v(u^2-v^2):u(u^2-v^2):v^3]. Substitution gives the cubic equation identically; on x!=0 its inverse is u=y/x, and the two preimages of the node are u=1,-1. The point P0 is u=2; O is u=infinity. The pullback divisor P0-O is (2)-(infinity), the divisor of f(u)=u-2. The line-bundle isomorphism nu^*B -> O_P1 is multiplication by f: a local meromorphic section s of O((2)-(infinity)) maps to f*s. Its inverse maps h to h/f. Their orders cancel at2 and infinity, so both are holomorphic bundle maps.

At the node the original Cartier bundle B has the common local frame1 because P and O avoid it. A local section s therefore has equal branch values. Writing h=f*nu^*s in the global normalized trivialization gives h(1)/(-1)=h(-1)/(-3), or h(1)=(1/3)h(-1). This is exactly the input B1 gluing convention, so B|C0 is A_{1/3}. Reversing the naming of the two branches changes the parameter to its inverse; the displayed convention fixes1/3. The3-adic valuation of(1/3)^m is-m for every positive m, proving that this scalar is never1.

Pullback by pr1:CxP1 -> C sends B to an invertible sheaf whose restriction to S=C0xP1 is pr1^*A_{1/3}; the restriction/pullback map is induced by the cartesian square, or directly by pulling the same transition functions back to the product. This gives the asserted extending non-torsion choice. The claim here is this explicit choice, not an unproved extension theorem for arbitrary twists.

A new prerelease program uses sparse integer homogeneous coefficient multiplication to certify the projective normalization identity, rational evaluation of the bundle trivialization at the two node branches, and the exact divisor/prime-valuation certificate. The analytic existence of the sections and all-m argument are proved above; finite sample calculations do not replace them.

## Bound inputs

- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_03I9_statement_inputs.tex SHA256 b33187161932b65cf6a328a87ba0f2be211f0d5333795b7dae42fff8e6c603b8
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_03I9_cited_input_supplement.tex SHA256 0658c58a838f003d4db46023c0807f652c895f1d2d7f98abf7e36b8b523ecc30

- agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_03I9_preproof_normalization.py SHA256 1550be1dabf06e7a6bffd0ffc80ba5b63fd594156d098cc8f4798bfebee7fb24
- agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_03I9_preproof_normalization.output.json SHA256 be058f26d79613d658878b01a2de65481b139a513fe21b5bbd1a0f2a4ceb9f29
