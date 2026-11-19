# A.3.4 — clean root-cover residual packet

This packet gives actual construction data, already-proved inputs, and assertions to establish. It contains no receiving proof or derivation of the requested assertions. Do not open A3_4_target_after_freeze.tex or the A.3.4 proof in Paper II until your own derivation has been frozen. The ledger reviewer already has a complete before-reading alternative assertion proof; your scope is the extra retained root-cover route below, not that alternative or the analytic-locus replacement.

## Actual construction

Y is the smooth compact complex threefold in the stated CDP20 hypotheses, g:Y->P^1 is its proper holomorphic map with connected fibres, H^1(Y,Z)=H^2(Y,Z)=0, and mS is one scheme-theoretic full fibre with m>=2 and smooth connected reduced support S. Choose a sufficiently small disc Delta about its value, set U=g^{-1}(Delta), and choose the base coordinate t vanishing at that value. On any sufficiently small chart meeting S, take a reduced equation z for S and retain the actual holomorphic unit u in t o g=u z^m.

Form the fibre product with the disc map Delta'->Delta, s->t=s^m, and then its normalization U'. Denote the induced maps by p:U'->U and g':U'->Delta'. Their conclusions below are targets to prove, not assumed properties of this construction.

## Exact named inputs allowed

1. The D.1.9 family is L_r=exp(2 pi i r beta), with beta fixed by its integral/coherent Leray construction. On U the integral section gamma has a lift gamma_U in H^1(U,Z), and beta|U is its coefficient image in H^1(U,O_U). Its associated rank-one local system is the actual character

   A_U: pi_1(U)->S^1, a -> exp(2 pi i r <gamma_U,a>).

   Its associated holomorphic line is L_r|U. Here r is a real irrational number; gamma_U restricts to a nonzero integral class on every nearby smooth fibre.

2. The already-proved smooth-fibre part of A.4.9 gives H^0(F,A_U|F)=H^1(F,A_U|F)=0 on every nearby smooth fibre F. This is an allowed conclusion, not a claim that you are rederiving its surface classification or group-cohomology proof.

3. A.4.7 gives the actual natural injection H^0(T,Omega_T^1 tensor A)->H^1(T,A_top) for a compact smooth complex surface T and a unitary local system A_top with associated holomorphic line A.

4. A.3.1 supplies, for a Cartier divisor T and a locally free sheaf E, the actual ideal-power sequences 0->E|T tensor(N_T^*)^(k-1)->E|kT->E|(k-1)T->0. The first map is multiplication by the (k-1)-st power of a local Cartier generator; the last is reduction. You may use these already-proved maps.

5. Proper smooth local triviality is allowed as a classical theorem. Please write the actual transport/local-system maps used here, rather than identifying groups without their map.

## Assertions to derive before target reading

A. Establish the normalization of the specified base change locally, retaining the unit u. Prove that p is finite étale of degree m and show how the actual local maps glue. Prove that S'=g'^{-1}(0) is smooth and reduced, that g' is a submersion near S', and that p^*(mS)=mS' as Cartier divisors. Justify the needed properness and shrinking of the disc.

B. Describe the actual map from each nearby noncentral fibre of g' onto the corresponding fibre of g and the induced pullback of A_U. Transport its degree-zero and degree-one local-system cohomology to S' using the actual proper smooth trivialization, including any component issue. Establish the resulting vanishings on S'.

C. Derive the unitary-flat section/parallel-section comparison needed for H^0(S',p^*L_r), use the allowed A.4.7 injection for the cotangent group, and write the reduced-fibre conormal map and its actual trivialization. Deduce the ambient restricted-section vanishing on S'.

D. Write every graded factor for mS' and use the exact input sequences to deduce its full scheme-theoretic ambient vanishing. Establish the actual étale cotangent isomorphism and the injection/descent from sections on mS to sections on mS'; provide the scalar-extension map and a trace or faithfully-flat left-inverse argument, with the degree factor retained.

E. The receiving proof contains a final scope statement about singular supports. For an arbitrary reduced Cartier support T=(h=0) in the same smooth ambient situation t=u h^m, establish precisely what the same unit-root base change does to T and its singularities. For the hypersurface cotangent kernel K=N^* tensor J^(-1), where J is the actual Jacobian ideal, show that the relevant étale pullback preserves this term through the actual differential/base-change maps. This is a scope check, not a request to prove vanishing on a singular support.

The analytic exceptional-locus argument is separate and owned by the ledger reviewer; do not infer it from upper semicontinuity alone. The current full-row gate remains pending until the retained routes and the specified replacement are actually compared and registered.
