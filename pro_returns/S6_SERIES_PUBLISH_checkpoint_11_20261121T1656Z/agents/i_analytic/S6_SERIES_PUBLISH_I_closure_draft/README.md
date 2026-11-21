# Paper I closure validator draft

The validator is `../S6_SERIES_PUBLISH_close_I.py`. It reads shared inputs and writes only inside the analytic agent directory. It has no shared-mutation or event-creation mode.

## Run

```bash
python work/agents/i_analytic/S6_SERIES_PUBLISH_close_I.py --manifest render/I_candidate13/manifest.json
```

Exit status 0 means all required receipt bindings pass; exit status 2 means at least one gate remains open. The JSON report records every input hash and every failure. Counts are derived from the current printed identities and the merged ledger. No environment, page, edit or event total is copied from Paper V.

`--stage-updates` produces a proposed complete-gate receipt and guarded append-only updates for the progress ledger and report, only after all validation gates pass. The program never applies those updates. Existing historical report content stays intact. Root should review the full proposed documents and update any superseded present-tense status separately.

## Evidence still needed at draft creation

1. Final certified full-page coverage and final-PDF receipt, matching the current source, build, manifest and delivery PDF. Candidate13 currently has partial coverage; candidate12 coverage does not certify changed images.
2. Certified current metadata and current statement extraction, with a methodology-count receipt bound to the final source. Dynamic values currently agree at 333 environments, 353 identities, 1,846 associations and 1,614 groups.
3. Refreshed certified defect-page mapping for every current edit row. The retained candidate11 map has 1,676 rows; the current log has 1,953 rows. Its 85 current source-only loci require actual final locations or explicit honest nonprinting/deletion dispositions. An intermediate old wording need not be assigned a fictional original page.
4. Final D01–D25 closure evidence. Provenance has supplied `S6_SERIES_PUBLISH_I_defect_type_closure_evidence.json`, explicitly pending final verification. D07 has no edit rows and still has positive inspected-scope evidence.
5. A current-source/ledger dependency-closure binding for the zero-current-candidate result. All19 original completion receipts currently pass exact hash checks. A pending template specifies the required hashes and scope; it is not a completion receipt.
6. Final A–G binding or exact byte/guard transport of the existing exposed global comparisons. The ABC, DE and FG receipt hashes must be current. The aggregate template retains those existing groups and introduces no new check credit.
7. Final provenance/deposit binder and all42 claim dispositions, bound to the final source, frozen ledger and certified PDF/coverage. Apply its exact proposed shared provenance/deposit updates. Root's42-claim review must identify the final table hash and close its explicit rebinding items.

## Validation scope

The validator checks the evidence structure, file hashes and scope declarations. It does not manufacture an actual page reading or mathematical comparison. Each page requires a hashed reading record with the exact page/image/PDF tuple and a nonempty finding. Earlier readings transfer only by whole-image equality. A rendered PNG alone supplies no reading credit.

The two `TEMPLATE.json` files are deliberately uncertified, with null final hashes and pending fields. Root must replace those fields from actual final evidence. They must not be copied to shared completion paths unchanged.

## Implementation checks

The script compiles. A read-only run against candidate13 returned `closed: false`, correctly detecting missing final certification and stale mappings/bindings. All676 original labels and520 permanent tag targets were found in the current source. No shared file or CHECK_EVENTS row was changed by this run.
