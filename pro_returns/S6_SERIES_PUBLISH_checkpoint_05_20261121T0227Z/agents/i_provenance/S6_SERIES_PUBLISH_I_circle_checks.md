# Three circle-quotient target checks

Completed 2026-11-21T02:00:43.687017+00:00. The source-bound intake, the two frozen preread derivations, fresh exact kernel/Smith computation, and post-freeze printed-proof captures are adjacent files.

## Exposure and independence

The statement extractor correctly isolated mapsI:A.1.1, A.1.2 and A.2.1. It omitted `remark` and accidentally displayed night:P5.7's proof; that failure was immediately disclosed to the parent, the capture was retained, and **no independent credit for night:P5.7 is claimed here**. The parent assigned it separately. The circle proofs were not exposed by that failure.

The full A.1.1/A.1.2 derivation was frozen at 01:39:56 UTC, SHA44ebf9826a6eab1d926c819b3f6de46c4e716482ccc8116d6701450d5cb38b80, before opening those two proofs. A.2.1's full derivation was frozen at 01:59:49 UTC, SHA14c954b249d085201e6672bbbca3bc45e260b4802c5080b83b8e8ceb3c7f6295, before its proof. Its cited input eq-5, including the unnumbered proof of the cusp fundamental-group map, was read as an input and receives no preread credit.

## A.1.1 — PASS, full statement

The independently derived simultaneous kernels give Zd and Z gamma. The exact cusp image is Z<w,d>; A1w=u−w forces its invariant closure to be L=Z<u,w,d>=ker gamma. Three unit Smith factors verify integral saturation. The real period map identifies each regular fibre with Lambda_R/Lambda, and the explicitly induced character has connected kernel L_R/L. For the finite fillings, gamma(v1)=1 and gamma(v2)=−1 give the exact clockwise residues. The norm sums are m_jv_j, and every intermediate circle translation is nonintegral. The free diagonal quotients therefore yield the claimed smooth proper T³-bundles. The printed proof's additional invariant coordinates (s exp(2pi i r theta),exp(2pi i m theta)), r epsilon=1 mod m, explicitly exhibit the same Seifert solid tori. Its gluing statement applies gamma to the specified gluing translation, agreeing with our equivariant descent.

Fresh exact calculation: code/S6_SERIES_PUBLISH_I_circle_primitive_check.py and S6_SERIES_PUBLISH_I_circle_primitive_check.json. This supports the same targeted check and is **not counted again** as a separate computation.

## A.1.2 — PASS, full statement

Inverting Im(sB0+C(q)) gives the independently derived uniform character asymptotic −b2/(b0+b1+b2) mod Z. Bounded chart coordinates make each logarithmic ratio bounded, so the discarded error is O(1/Im(s)) for all convergent paths, not just a selected radial family. This proves zero limit on smooth components and the horizontal double curve, and distinct limits on the other two double curves and both triangle types. The independently chosen coordinates on the second triangle are a cyclic permutation of the printed ones: (z0,z1,z2)_printed=(z2,z0,z1)_preread. Under that explicit permutation both monomial descriptions coincide. The action in direction d is exactly (lambda^−1 z0,z1,lambda z2), fixing the different double curve z0=z2=0. All assertions match.

## A.2.1 — PASS, full statement relative to its cited input

The surjection pi1(boundary N)→pi1(N)=Lambda/K makes the character class extend and the restriction on H¹ injective. The preread proof constructed a smooth circle representative by an integral-period one-form, corrected it on a collar by an explicit real logarithm and cutoff, and paired it with the unchanged f. The printed proof uses K(Z,1), homotopy extension and relative smooth approximation for the same construction. For two replacements the ratio has a global real logarithm zero on the connected collar; h_t=h0 exp(2pi i t phi) is the required actual homotopy. This agrees with the printed relative-H¹ argument. The over-B condition, fixed gluing, designated solid-torus image, arbitrary small support and original-sphere specialization are all preserved. No pointwise extension of the original character is used.

## Events and editorial follow-up

Exactly three scoped targeted-proof-check rows are supplied, one for each target. They share one declared evidence group for this coordinated preread/comparison bundle. No independent reproof, extra computational, source-locator or presentation event is added. No mathematical correction is needed.

The eq-5 input is currently an unnumbered proved paragraph; the editorial batch will number it without changing its proof. The A.1.2 ending refers to an incorrect earlier construction without a precise citation, and A.1.1 ends with a literal program path; those are publication defects to be handled separately.
