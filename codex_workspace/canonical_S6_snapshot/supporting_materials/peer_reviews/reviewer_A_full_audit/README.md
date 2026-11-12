# Full mathematical peer-review bundle

This package reviews the complete 108-page S6 manuscript in `s6_canonical_108_pages_audited.zip`.

## Primary conclusion

Recommendation: **major revision and independent specialist replication**. No fatal mathematical contradiction was identified in the complete manuscript. The complete Section 10 materially supersedes the earlier packet-only assessment by giving a technically substantive proposed failure mechanism for the printed CDP98/CDP20 arguments at the nonnormal fibre.

The report does not certify the main theorem. The principal unresolved verification risks are the global collapse, integral nearby-cycle specialization, analytic base change and duality at special fibres, and external adjudication of the proposed CDP counterexample.

## Contents

- `report/full_mathematical_peer_review.pdf` - primary 17-page referee report.
- `report/full_mathematical_peer_review.md` and `.tex` - editable sources.
- `audit/issue_ledger.csv` and `.json` - confirmed errors, revision requests, and verified components.
- `audit/theorem_dependency_matrix.csv` - central claims and dependencies.
- `audit/exact_checks.py` - exact arithmetic and symbolic audit.
- `audit/exact_checks_results.json` and logs - 28 of 28 checks passed.
- `audit/literature_comparison_CDP98_CDP20.md` - focused analysis of the formal conflict.
- `evidence/` - reconstruction verification extracts and source-page line map.
- `review_receipt.json` and `MANIFEST.sha256` - reproducibility metadata.

## Confirmed local errors

1. Remark 7.28 has a quantifier defect. Its residue biconditional is false for a fixed triple; it is correct as an existential statement in `ell_0`.
2. Proposition 4.7(iv) uses an incorrect reason for closedness of the section image; the conclusion is repairable by a closed-graph/section argument.

## Reproduction

Run:

```bash
python audit/exact_checks.py
```

The PDF report was rendered at 200 dpi and preflighted. No clipping, overlap, or broken glyphs was found in the rendered pages.
