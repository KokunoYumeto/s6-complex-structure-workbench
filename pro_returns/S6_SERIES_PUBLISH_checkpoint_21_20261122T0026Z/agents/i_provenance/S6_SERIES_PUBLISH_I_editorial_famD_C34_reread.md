# Paper I D/C3/C4 editorial comparison

Completed 2026-11-21T02:12:44.340793+00:00. Original full source span and every affected statement/proof were read before the edits. Every proposed replacement was then read against its old guard. The remaining text is retained exactly.

Old span SHA256: `7138aaee00d11460d7946131872c12c1973734e124f3e2bd4bbe08044574d353`. Proposed span SHA256: `29590eb38e2ab320f244d8eb75751a26ec158ee3d9e04f1d51f7948f88ec36c0`. Current root source inspected for guard uniqueness: `e6df9c3c872142a86cf7b4961d514b17d14fcbc30e9cae77ca28a21e42612955`. All 41 guards occur exactly once.

## Mathematical scope

The D1.1 exact sixth-division polynomial, x(6P) numerator/denominator, both elliptic-quotient lattice maps, D1.2 Betti-Jacobian/density/isogeny/height proof, D1.3 order-four example and all period images, D1.4 wedge/Pfaffian/orientation/Hermitian proof, and all null-lattice/quotient and effective-divisor arguments remain. D1.5 replaces the duplicated AC Lemma9.3 derivation with that actual opened source and an explicit invertible five-coefficient map for beta_part+c; its countability application and complete explicit projective-family construction remain. The old full proof is retained in the old-span file and exact guard.

The existing Pi-to-Hermitian-form comparison and every sign/verification move from D1.6 to numbered Definition IP03 before D1.4. D1.6 and D2.3 use that precise definition. The rank-three quotient coordinate changes, degree-four covering, real closure and natural-boundary proof remain. C3.3 becomes a numbered remark with its existing tag and both labels. The cusp proof retains all six effective actions, exact character-sign transport, positive/negative obstruction and fixed-set argument.

All original labels and tags are preserved. The only new tag is IP03. Titles alone on D2.2/C3.1 do not produce reread events. Program diagnostics and deprecated appendix pointers move to records, while operative polynomial and fan-enumeration references point to tab:I:programs.

## Before/after dispositions

- **I-DC-title-D.1.1** (fam:src:D.1.1): Add a short mathematical title without changing the statement or its identifiers.
- **I-DC-title-D.1.2** (fam:src:D.1.2): Add a short mathematical title without changing the statement or its identifiers.
- **I-DC-title-D.1.4** (fam:src:D.1.4): Add a short mathematical title without changing the statement or its identifiers. Move the existing explicit Pi/H_E/Chern-form comparison before its first use; preserve every sign and verification.
- **I-DC-title-D.1.5** (fam:src:D.1.5): Add a short mathematical title without changing the statement or its identifiers.
- **I-DC-title-D.1.6** (fam:src:D.1.6): Add a short mathematical title without changing the statement or its identifiers.
- **I-DC-title-D.1.7** (fam:src:D.1.7): Add a short mathematical title without changing the statement or its identifiers.
- **I-DC-title-D.2.1** (fam:src:D.2.1): Add a short mathematical title without changing the statement or its identifiers.
- **I-DC-title-D.2.2** (fam:src:D.2.2): Add a short mathematical title without changing the statement or its identifiers.
- **I-DC-title-D.2.3** (fam:src:D.2.3): Add a short mathematical title without changing the statement or its identifiers.
- **I-DC-title-C.3.1** (fam:src:C.3.1): Add a short mathematical title without changing the statement or its identifiers.
- **I-DC-title-C.3.2** (fam:src:C.3.2): Add a short mathematical title without changing the statement or its identifiers.
- **I-DC-title-C.3.4** (fam:src:C.3.4): Add a short mathematical title without changing the statement or its identifiers.
- **I-DC-title-C.4.1** (fam:src:C.4.1): Add a short mathematical title without changing the statement or its identifiers.
- **I-D11-addition-description** (fam:src:D.1.1): Keep the exact rational function needed at the special fibres, and remove check-history narration.
- **I-D11-program-reference** (fam:src:D.1.1): Replace program/run narration by one operative program-table citation. The exact roots and complete x(6P) formula remain.
- **I-D12-height-locator** (fam:src:D.1.2): Cite the exact primary location and remove source-reading narration.
- **I-D12-height-conclusion** (fam:src:D.1.2): Preserve the height application and all special-fibre exclusions; archive the independent degree/correction-matrix diagnostic in the program record.
- **I-D12-appendix-pointer** (fam:src:D.1.2): Remove an obsolete appendix pointer: the complete application already appears in the immediately preceding proof, with its old label preserved.
- **I-D13-positive-title** (fam:src:D.1.3): Title the constructed quotient.
- **I-D13-positive-statement** (fam:src:D.1.3): State the precise quotient map and torsion order supplied by the unchanged construction.
- **I-D13-remove-numeric-check** (fam:src:D.1.3): Keep the analytic bound and remove an unnecessary numerical/check comparison.
- **I-D13-program-reference** (fam:src:D.1.3): Keep the four explicit lattice images and their gcd proof; cite the operative polynomial calculation once.
- **I-D14-orientation-citation** (fam:src:D.1.4): Give the verified primary coefficient identity and retain the explicit orientation comparison instead of process language.
- **I-D14-Hermitian-reference** (fam:src:D.1.4): Remove the forward construction dependence by referring to the relocated exact definition.
- **I-D15-known-independence** (fam:src:D.1.5): Replace the repeated AC9.3 proof by the opened primary result and exact invertible coefficient map for beta_part+c; retain the discrete-zero/countability application. The old proof is retained in the comparison record.
- **I-D16-positive-statement** (fam:src:D.1.6): State the exact classification and quotient construction positively.
- **I-D16-Hermitian-use** (fam:src:D.1.6): Use the relocated exact definition and preserve the integral-sign comparison and both directions of the polarization criterion.
- **I-D16-end-prose** (fam:src:D.1.6): Give the base of the descended loci without editorial reassurance.
- **I-D16-appendix-pointer** (fam:src:D.1.6): Remove the obsolete appendix pointer to the proof already printed here; retain its label.
- **I-D17-end-prose** (fam:src:D.1.7): Keep the explicit locus and torsion exclusion, removing process emphasis.
- **I-D21-normalization-prose** (fam:src:D.2.1): The full normalization/composition and Cartier-divisor arguments already specify the maps; remove defensive comparison.
- **I-D23-quotient-prose** (fam:src:D.2.3): Remove process emphasis.
- **I-D23-Hermitian-reference** (fam:src:D.2.3): Use the exact relocated sign convention.
- **I-D23-effective-source** (fam:src:D.2.3): Supply the opened primary effective-section/nullspace-quotient criterion at the operative application.
- **I-D23-finite-map-conclusion** (fam:src:D.2.3): Retain the exact finite/closed morphism argument and remove defensive commentary.
- **I-D23-appendix-pointer** (fam:src:D.2.3): Remove the obsolete appendix pointer to the complete printed proof; retain its label.
- **I-C32-boundary-prose** (fam:src:C.3.2): Remove process emphasis.
- **I-C32-end-prose** (fam:src:C.3.2): The exact coordinate change and degree-four morphism already give the result.
- **I-C33-numbered-obstruction** (fam:src:C.3.3): Number the existing local-obstruction discussion, preserve both labels and the tag, and state each proved scope and its exact source positively.
- **I-C34-end-scope** (fam:src:C.3.4): State the exact scope of the rational-invariant argument positively.
- **I-C41-program-reference** (fam:src:C.4.1): Keep the complete finite enumeration rule and character-sign transport, with one operative program-table citation.

## Count semantics

Thirteen scoped used-and-rechecked associations are recorded in one evidence group, covering the changed proof/discussion subjects. They record exposed-text editorial rereading only. No independent, targeted, or new-computation credit is claimed. Primary page opening and source/label/guard scans add no mathematical events. Application to the root source and final rendered pages remain separate gates.
