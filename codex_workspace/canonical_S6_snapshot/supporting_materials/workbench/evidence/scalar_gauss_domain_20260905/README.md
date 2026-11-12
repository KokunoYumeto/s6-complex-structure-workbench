# Scalar–Gauss domain: source and independent-review evidence

This packet records the complete scalar–Gauss parameterization, its literal-domain extension, and the independent review. It concerns the two scalar equations and Gauss with the original constants retained. The spatial equations are not imposed, so the result is not a full rotating-ansatz solution.

## The five source and replay files

| File | Role |
|---|---|
| scalar_gauss_domain.tex | Original candidate source: the classified-frame parameterization, phase inverse, and construction at every original positive coupling. |
| literal_domain_quotient_addendum.tex | Proof fragment supplying the temporal classification and complete literal-domain map, including its exact two-element fibres and quotient bijection. |
| check_scalar_gauss_domain.py | Exact symbolic checker of the retained residual entries and algebraic identities. |
| scalar_gauss_domain_shared.tex | Initial shared-source integration snapshot, combining the candidate proof and literal-domain addendum. |
| SOURCE_AND_REPLAY_RECEIPT.json | Input hashes, integration transformations, initial shared-source hash, and the recorded 25-group exact replay. |

The initial shared snapshot has SHA-256

C8025752A07D104F3736B2F9B27D2E0EDDB5F918CA99B4812A532720344381F1.

This identifies the preserved initial integration, not the later typesetting revision. The separate final snapshot is scalar_gauss_domain_shared_final_typesetting.tex; FINAL_SOURCE_RECEIPT.json and MANIFEST.json record its identity. Two long displays were split into rows without changing their mathematical contents. The initial snapshot and its original receipt remain unchanged.

## Independent review and provenance

INDEPENDENT_REVIEW.md is the full independent proof-bearing review. It verifies the classified bijection and reproduces the temporal classification needed for the literal domain. It proves that the raw literal parameter map is exactly two-to-one, with the sole identification

\[
(\zeta,p_+,p_-)\sim(-\zeta,-p_+,-p_-),
\]

and that the quotient is in bijection with the entire stated literal scalar–Gauss domain.

REPLAY_RECEIPT.json records the independent review's original successful serial replay. ADDENDUM_RECEIPT.json records the original literal-domain addendum, its hash, and its structural checks. These are historical receipts, with only absolute machine paths sanitized; no new replay was performed for this packet. The replay receipt's original reference to REVIEW.md denotes the source copied here as INDEPENDENT_REVIEW.md.

REVIEW_PROVENANCE.json records original file hashes, public-copy hashes, and the exact four path redactions. Redactions are located by original character offsets, line or JSON-field locators, and hashes of the removed substrings. The removed machine paths are not repeated in the public record. The originals remain local and unchanged; all mathematical text and recorded test results are retained.

Paths in the review and copied receipts use an explicit repository-relative convention. Historical commands and integration targets are relative to the original repository root, not this evidence directory; the interpreter is written as python. The original candidate and addendum named in those historical paths are preserved by the source snapshots listed above.

## Scope of verification

The checker reports 25 finite exact check groups, using symbolic identities with no floating-point acceptance. These checks verify residual entries, trace and determinant identities, rank-one factorizations, retained phases, frame maps, and the displayed inverse-coupling identity.

Analytical completeness comes from the proofs: temporal classification, exclusion of singular and zero-denominator cases, positivity, necessity and sufficiency, the full phase inverse, the literal quotient fibres, and existence at every prescribed positive coupling. A finite list of checker successes alone does not establish these statements.

No smooth follow-up is included in this batch. This evidence addition made no mathematical source changes, PDF builds, publication actions, or new checker runs. The release finalizer writes the final manifest.
