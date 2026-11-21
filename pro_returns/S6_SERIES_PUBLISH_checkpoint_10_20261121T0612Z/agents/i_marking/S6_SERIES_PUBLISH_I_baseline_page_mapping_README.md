# Original Paper I PDF: read-only old-side page mapper

Run from `work/`:

```bash
python agents/i_marking/S6_SERIES_PUBLISH_I_baseline_page_mapper.py
```

The helper reads the pinned 419-page original PDF, original TeX, attached tag index, and the latest defect TSV. It writes only its own JSON receipt, audit JSON, and summary TSV. It never modifies the defect log, source, PDF, or root mapper. All filenames and destinations are hash-bound.

## Reuse in the current SyncTeX mapper

Import this separate module with `importlib.util.spec_from_file_location`, then call:

```python
old_by_id = baseline_module.load_old_side(
    baseline_receipt_path, baseline_pdf_path, original_source_path, defect_rows)
assert len(old_by_id) == len(defect_rows)
```

The helper validates the baseline PDF and source hashes, then checks each change ID, statement ID, exact old-text hash, and original old-location string. An altered old row is omitted; the caller must regenerate the baseline receipt for missing entries. New-text changes do not alter an unchanged old-side locator.

Use `old_by_id[row['change_id']]` directly for the old plan. It already contains `pages`, `method`, `location`, `exact=False`, and `reused_from_unchanged_baseline_receipt=True`. Do not construct the old `Document`, read an old AUX, run old SyncTeX, or call old `prepare`. The existing current-side `Document` and current SyncTeX flow can remain. The baseline metadata for the combined receipt comes from this JSON.

## Page semantics

All 419 printed footer numbers were checked against the one-based PDF pages. All 520 original-source tag destinations agree with the attached tag index; 128 plain source headings also match unique bookmarks and their actual named destinations.

A unique phrase match certifies only the selected literal prose fragment's page. The exact character/whitespace comparison map is declared in the receipt; it does not convert mathematical macros or remove line-end hyphens. A destination certifies the statement, section, entry start, or explicitly labelled preceding context locus. Neither supplies complete long-proof page bounds. Intermediate wording absent from the original remains source-only unless an unchanged unique phrase is directly found.

Latest run: 1,676 defect rows; 774 with exact selected-phrase loci; 719 with destination/context loci; 183 with no page claim (14 preamble, 169 intermediate). No source/index destination discrepancies. This is location metadata and adds no mathematical check or rendered-page review credit.

Validation: all 1,676 old rows import successfully; a changed old-text row is rejected. Three selected phrases were independently located by Poppler, including pages 19 and 20 for edits whose related section starts on page 6. A separate five-destination Poppler audit is supplied by the provenance agent.
