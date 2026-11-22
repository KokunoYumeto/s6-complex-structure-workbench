# Independent recovery derivation: cdp:st:A.5.1, tag 01AZ

Checker identity: ii_check_a_recovery_blind. The target printed proof, B's reconstruction and B's proposed block have not been opened. This derivation uses the original target statement packet, its supplement, and root's exact notation/input packet `S6_SERIES_PUBLISH_II_01AZ_notation_inputs.tex`, SHA256 02cc9a9b24f63e39cdf2d35a27c4c7750f961fe473df2e7478b3f04128799c3f. The latter contains only the notation paragraph and statements A.1.1, A.2.1, A.2.2. It identifies the ambient group as H0(S,V tensor A), with V=Omega_Y^1 restricted to S, N*=O_Y(-S)|S, T the kernel of restriction of Omega_S^1 to its regular locus, Q=Omega_S^1/T and K=ker(V to Q). The finite analytic normalization is eta:Tilde S to S and B=eta_*O_Tilde S.

The input A.2.2 gives the canonical inclusion eta_*eta*N* to K; its concrete local map, using A.2.1, is b tensor [F] to b dF. The input J subset conductor ensures that every coefficient b F_xj belongs to O_S, so this expression lies in V even at the singular locus. On a change F'=uF, the conormal frame changes by u and dF'|S=u dF|S, so these local maps glue. At the dense regular locus they are ordinary conormal inclusions, and the input asserts their injectivity on the full reduced hypersurface. Composition with K to V is therefore injective.

Tensor this injection by the invertible sheaf A. Tensoring with A is exact, and the finite projection formula gives

    eta_* eta*(N* tensor A) = (eta_*eta*N*) tensor A -> K tensor A -> V tensor A.

Every arrow displayed is the same O_S-linear map just described, tensored with the identity of A. The global-section functor is left exact, and finite pushforward does not change H0. Hence there is a canonical injective linear map

    H0(Tilde S, eta*(N* tensor A)) -> H0(S,K tensor A) -> H0(S,V tensor A).

This is the canonical image asserted in the target. Its construction does not use a trivialization of eta*A; those choices are needed only to identify its source with a familiar vector space.

Let b be the base point of this full reduced fibre. Choose a holomorphic coordinate t on a disc about b, with t(b)=0. On the inverse image of that disc the function F=t composed with f defines the full scheme fibre. The hypothesis that this full fibre is reduced says that its Cartier divisor is exactly S, with all component multiplicities one. Thus [F] is a nowhere-zero frame of the conormal line N*=I_S/I_S² over S. Its pullback is a frame on Tilde S. Choose the assumed trivialization alpha:eta*A to O_Tilde S. The tensor frame [F] together with alpha identifies eta*(N* tensor A) with O_Tilde S. The preceding canonical image is thereby identified with H0(Tilde S,O_Tilde S). A change of base coordinate or alpha changes this chosen identification by an invertible scalar on each connected normalization component, but leaves the canonical image of the original source sheaf map unchanged.

The normalization is nonempty and compact because the original fibre is nonempty and proper and eta is finite. Its constant function 1 is a nonzero global section, so this vector space and its injective image are nonzero. If the normalization has several connected components, the functions constant on each component give the corresponding direct sum; the argument did not assume connected normalization.

For the described subcase of the published Proposition 7.3, apply this same injection separately to A=L_t|S for each parameter with eta*A trivial. No deformation, generic-Picard or constancy argument is introduced: the statement follows by using the same normalization map and the same line bundle in the established injection.

Finally the image lands in H0(K tensor A), which is exactly the kernel of H0(V tensor A) to H0(Q tensor A) by the second exact sequence in A.1.1. Therefore the nonzero sections just constructed map to zero in the quotient group. In particular H0(Q tensor A)=0 leaves this kernel unrestricted; the exact map identifies the whole ambient group with H0(K tensor A) in that situation. The supplied example A.4.1 has exactly H0(Q tensor A)=0 and ambient group C. This verifies compatibility by the actual two maps and their kernel, rather than comparing unnamed groups. There is no numerical computation requiring a program in this derivation.

All claimed maps and all conclusions have now been derived from the stated inputs before opening the target proof.

## Exact prefreeze input and computation bindings

Binding written 2026-11-21T20:16:19.008816+00:00, before target proof release.

- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_01AZ_statement_inputs.tex — SHA256 bbf44fc989a74338aa84632030c1f01666fb7aa7ef6c0bdfa7cc793b54d81775.
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_01AZ_cited_input_supplement.tex — SHA256 f497beea987b0d0d33c8c486c81e8360cd3932ea7f4934237224f2b79003074b.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_01AZ_notation_inputs.tex — SHA256 02cc9a9b24f63e39cdf2d35a27c4c7750f961fe473df2e7478b3f04128799c3f.
