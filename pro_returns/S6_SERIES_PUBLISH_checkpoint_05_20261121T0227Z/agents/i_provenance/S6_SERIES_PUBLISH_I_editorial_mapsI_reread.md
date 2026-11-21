# Paper I real-forms and circle-quotient comparison

Completed 2026-11-21T02:24:48.985896+00:00. Source inspected for unique guards: `b383f09cdc0dbc6db268c002659369715208fa01c9bbf61fd494880c257f2c5b`. The full old real-forms proof span, full B4.2 proof, and full circle-quotient span were read. Every proposed replacement (including the moved full B4.2 proof) was then read against its old text.

The protected topology-agent push:C3.5 block and following figures are outside every guard. Root source was not written. All old labels and tags are preserved, including the relocated B4 section alias. New wrappers use IP04–IP08.

## Exact proof scope

- **fam:src:B.4.2**: Full seven-step reflection/base/period/lattice/affine-root/toric-cusp/normalization/involutive-splitting proof retained and moved. Scalar square translation renamed b0 to avoid colliding with lattice d. No known comparison replaced by an unsupported identification.
- **mapsI:src:A.3.1**: Repeated complete automorphism/reflection derivation replaced by its retained local B4.2 source. Exact z/bar(z) involution and |y|^2 conjugacy calculation remains, as do Illman/Smith and semifree fixed-locus arguments.
- **mapsI:src:A.3.2**: The repeated H matrix and initial target affine datum refer to the retained exact B4.2 formulas. All explicit normalizing translations, finite period defects, logarithmic collar/cusp cancellations, square periods, branch matrices, fixed-coset equations, Hermite/Smith factors, denominator24 enumeration, toric units and edge signs remain.
- **mapsI:src:A.3.3**: Complete surface-decomposition/Heegaard proof retained: odd-root lift k2, C=B1^2, transport of u+w, A2^2 exchange and meridian determinant are unchanged.
- **mapsI:src:A.3.4**: Complete invariant-lift averaging, relative collar agreement, orbit-space null-homotopy and exact two character values remain. Only repaired/process prose removed.
- **mapsI:src:A.1.1**: Common A1/A2/v1/v2 matrices referenced to their exact earlier definition. M0 remains displayed. Complete primitive fixed-vector/covector/kernel calculation and finite Seifert coordinate maps remain. Independent diagnostic moved to records.
- **mapsI:src:A.1.2**: All radial and arbitrary-path cusp limits and both triple-point types remain. Final unattributed correction prose replaced by the already explicit toric action and the two coordinate loci.
- **mapsI:quotient-eq-5**: Existing unnumbered toric-meridian/deck-group proof read and moved into IP07 lemma; both long-period covector extensions and global H1 factorization obstruction preserved. This is a reread of an exposed input, not the strict A2.1 independent check and not fresh independent credit.
- **mapsI:src:A.1.3**: All oriented meridian slopes, Bezout choice, q0 congruence, determinant and Seifert orbit comparison retained. Coordinate exchange explicitly written (z1,z2)->(z2,z1).
- **mapsI:src:A.2.1**: Complete K(Z,1)/collar-extension/smooth-approximation construction and relative H1 uniqueness proof retained. Smoothness follows from the two smooth components, including at critical f-points.

## Consolidation and ordering

The full B4.2 proof now precedes A3.1/A3.2 in the real section. The old B4.1 appendix-navigation paragraph is removed because the parent has retained the full credited automorphism theorem under its old alias. The two duplicated reflection/automorphism derivations are replaced by exact references to that retained proof; all unique real representative/normalization formulas remain. The entire corrected circle section should move immediately before the real section, after fam:C4, so A3.4 uses an already constructed e_q.

IP07 is the existing cusp π1 input, formerly an unnumbered paragraph with equation mapsI:quotient-eq-5. Its numbering does not create historical independent-check credit. The strict A2.1 check deliberately took this input as given; that limitation remains.

## Before/after log

- **I-real-move-B42** (fam:src:B.4.2): Move the complete B4.2 statement and proof beside the real-form calculation; relocate the section tag/label too. Remove only the obsolete B4.1 appendix navigation paragraph, whose full credited theorem is already retained under its alias.
- **I-real-number-data-and-B42** (fam:src:B.4.2; I:def:real-period-data): Use the one common marking/period/finite-data definition; retain all local real notation and cusp formulas, and place the complete conjugation proof before its uses.
- **I-real-two-class-proof** (mapsI:src:A.3.1): Use the retained complete automorphism/reflection proof, then preserve the distinct two-class conjugacy calculation.
- **I-real-semifree-prose** (mapsI:src:A.3.1): Remove check-history wording.
- **I-real-number-representatives** (I:def:real-representatives): Number the exact roots/logarithms/branch choice and representative table, retaining both equation labels and the existing tag.
- **I-real-reflection-application** (mapsI:src:A.3.2): Refer to the single complete reflection proof and its exact integral/affine maps; retain every normalization and filling-extension step below.
- **I-real-cusp-application-prose** (mapsI:src:A.3.2): Keep the explicit ordinary defects, finite-root comparison and full cusp cancellation calculation, avoiding anticipatory check prose.
- **I-real-arithmetic-intro** (mapsI:src:A.3.2): State the exact mathematical method.
- **I-real-ordinary-program** (mapsI:src:A.3.2): Retain the integral solvability criterion, all square vectors/Smith factors and the correctly derived lift; cite the operative program once.
- **I-real-odd-root-conclusion** (mapsI:src:A.3.2): Keep the full root quotient scope in positive mathematical language.
- **I-real-finite-program** (mapsI:src:A.3.2): Retain the exhaustive-denominator argument and deck permutation; cite the operative finite enumeration once.
- **I-real-parameter-signs** (mapsI:src:A.3.2): Make the already specified imaginary-parameter signs explicit.
- **I-real-cusp-intro** (mapsI:src:A.3.2): The final totally-real argument still proves that no component is confined to a special fibre.
- **I-real-odd-transport** (mapsI:src:A.3.3): Keep the unique k=2 root-lift derivation and its exact transport matrix.
- **I-real-integral-conclusion** (mapsI:src:A.3.3): Name the conclusions established by the explicit Heegaard gluing.
- **I-real-quotient-title** (mapsI:src:A.3.4): Use a mathematical title.
- **I-real-quotient-statement** (mapsI:src:A.3.4): State the property proved by averaging the circle lift.
- **I-real-concluding-process** (mapsI:src:A.3.4): Remove a scope disclaimer; the statements already give the exact fixed-set and smooth-type conclusions.
- **I-circle-number-conventions** (I:def:circle-quotient-conventions): Number the existing exact basis and orientation conventions.
- **I-circle-common-matrices** (mapsI:src:A.1.1): Use the canonical matrices and affine vectors once; retain the explicit cusp monodromy needed for the kernel calculation.
- **I-circle-matrix-proof** (mapsI:src:A.1.1): Reference the established common marking; retain all exact kernel and fixed-covector arithmetic.
- **I-circle-program-record** (mapsI:src:A.1.1): The complete integral calculation is printed; retain the independent diagnostic program in check records.
- **I-circle-character-comparison** (I:rem:circle-character-comparison): Number the comparison, use the identical existing matrix by its exact lattice isomorphism, and specify the target-circle orientation map.
- **I-circle-cusp-title** (mapsI:src:A.1.2): Give a mathematical title.
- **I-circle-fixed-curve-conclusion** (mapsI:src:A.1.2): Replace an unattributed correction claim by the explicit morphism and limit calculation already proved.
- **I-circle-number-cusp-input** (I:lem:cusp-fundamental-group): Turn the already proved cusp π1/cohomology input into a numbered lemma before A2.1 uses it, preserving its group, exact relations, equation tag and global factorization obstruction.
- **I-circle-meridian-convention** (mapsI:src:A.1.3): State the specified orientation data directly.
- **I-circle-knot-comparison** (mapsI:src:A.1.3): Give the exact coordinate exchange and preserve the peripheral identification proved by the Seifert data.
- **I-circle-section-title** (mapsI:src:A.2.1): Use a mathematical section title.
- **I-circle-theorem-title** (mapsI:src:A.2.1): Use a mathematical theorem title.
- **I-circle-smooth-product** (mapsI:src:A.2.1): State the smooth-product argument positively.
- **I-B42-title** (fam:src:B.4.2): Title the retained classification.
- **I-B42-period-prose** (fam:src:B.4.2): State the algebraic calculation directly; retain both rational substitutions and the subsequent uniqueness argument.
- **I-B42-H-label** (fam:src:B.4.2): Give the retained integral reflection matrix a reference for its later application.
- **I-B42-middle-deck-prose** (fam:src:B.4.2): State the full compatibility supplied by the displayed period-matrix identity.
- **I-B42-affine-label** (fam:src:B.4.2): Name the exact target affine datum to avoid repeating its construction.
- **I-B42-target-prose** (fam:src:B.4.2): Remove process emphasis.
- **I-B42-splitting-prose** (fam:src:B.4.2): Keep the full square-translation correction proof and state its purpose positively.
- **I-B42-square-translation-name** (fam:src:B.4.2): Use b_0 for the scalar translation class so the fixed lattice vector d keeps its meaning after moving this proof into the real-form section.
- **I-B42-aut-reference** (fam:src:B.4.2): Refer to the parent-consolidated theorem through the preserved alias.

## Count semantics

Ten scoped used-and-rechecked associations share one evidence group. They record actual exposed-text editorial reading and comparison, not an independent derivation, a new computation, an applied-source reread, or final PDF certification. Metadata/label scans create no mathematical events.
