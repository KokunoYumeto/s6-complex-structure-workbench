# Continuation infrastructure

All paths below are relative to the active `S6_SERIES_PUBLISH` tree. Historical helpers remain unchanged. The continuation wrappers derive the active tree from their own location and use the verified sibling `S6_SERIES_PUBLISH_work` as the immutable base.

## Build and page evidence

The environment has pdfLaTeX (TeX Live 2025/dev), Poppler, SyncTeX, and PyMuPDF 1.26.6 with MuPDF 1.26.11. The unchanged build helper performs three passes and records the source and PDF hashes and log diagnostics. The unchanged renderer uses scale 1.6.

Run these commands from the active tree, after a new source has been frozen. Replace `N` with the candidate number and `P` with the preceding candidate number.

```sh
python code/S6_SERIES_PUBLISH_build.py S6_SERIES_PUBLISH_I.tex --output-dir build/I_candidateN
python code/S6_SERIES_PUBLISH_render.py build/I_candidateN/S6_SERIES_PUBLISH_I.pdf --output-dir render/I_candidateN --scale 1.6
python code/S6_SERIES_PUBLISH_compare_page_images.py records/S6_SERIES_PUBLISH_I_candidateP_complete_coverage_snapshot.json render/I_candidateN/manifest.json --output agents/continuation_infra/S6_SERIES_PUBLISH_I_candidateN_image_comparison.json
python code/S6_SERIES_PUBLISH_reading_coverage.py I --render render/I_candidateN
python code/S6_SERIES_PUBLISH_continuation_tools.py snapshot --render I=render/I_candidateN --output records/S6_SERIES_PUBLISH_continuation_I_candidateN_progress.json
```

Rendering and page comparison supply no reading credit. Only equality of the complete PNG carries an actual prior page-reading record forward. Every changed image requires an actual full-page reading. Coverage remains uncertified until the root agent completes the requested gates.

The reconstructed immutable candidate13 has 346 pages, all with exactly the same complete PNG hashes as the archived actual-reading coverage. The reconstruction receipt is `S6_SERIES_PUBLISH_I_candidate13_restore_comparison.json` in this directory. Candidate14 had 346 pages. Candidate15 has 345 pages; its coverage snapshot records 345 actual page readings and `certified: false`.

## Metadata and mathematical-event preservation

`code/S6_SERIES_PUBLISH_continuation_metadata.py` runs the historical extractor in an isolated copy. Its preview contains exact input/output hashes and generated files. `--apply` copies back only after the canonical inputs are checked for concurrent changes. It accepts `--certified` only with a matching final PDF receipt.

```sh
python code/S6_SERIES_PUBLISH_continuation_metadata.py I --build build/I_candidateN
python code/S6_SERIES_PUBLISH_continuation_metadata.py I --build build/I_candidateN --apply
```

`code/S6_SERIES_PUBLISH_continuation_refresh.py` adapts the historical refresh program to the verified base path. Its default is an isolated preview. The guarded application command requires the recomputed `CHECK_EVENTS.tsv` to remain byte-identical.

```sh
python code/S6_SERIES_PUBLISH_continuation_refresh.py --apply --require-identical-events
```

Applied candidate14 and candidate15 metadata remain uncertified. The candidate15 receipt is `metadata_I_20261121T163453620430Z/receipt.json`. It binds source `45bf46fc14a50f7a148cdd34bf2be68b04cd89e1cb7d620191c6e8518f7249f8` to PDF `b72c6da6acddfd797c82837fbd086e222eeef8e4526ed736328affde474df780`. The event ledger remains `e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714`.

## Defect locations

`code/S6_SERIES_PUBLISH_continuation_defect_pages.py` writes an isolated preview by default. It preserves every inherited historical before-item field after validating the exact old text, identifier, and old-location binding. Later rows declare their own `candidateN` before scope. The mapper loads `S6_SERIES_PUBLISH_I_candidateN_source_for_mapping.tex` from this directory, checks its source hash against that candidate's build summary, and uses that candidate's exact PDF. Candidate13 is additionally tied to the archived PDF through the verified full-image equality receipt.

Current replacement strings with multiple occurrences receive explicitly scoped retained contexts. The mapper does not label a repeated short string as a uniquely located edit. Nonprinting metadata and removed bibliography entries retain their explicit nonprinted status.

```sh
python code/S6_SERIES_PUBLISH_continuation_defect_pages.py --current-build build/I_candidateN
```

The optional `--source-snapshot` and `--defects-snapshot` arguments allow a preserved candidate preview after the canonical source has advanced. `--apply` is reserved for the root agent's requested canonical mapping operation and refuses a stale canonical source/log or unresolved current contexts.

The shared-parser helper `code/S6_SERIES_PUBLISH_synctex_batch.py` uses the same installed `libsynctex` as `/usr/bin/synctex`. Forty CLI-derived queries matched exactly; the validation receipt is `S6_SERIES_PUBLISH_synctex_batch_validation.json`. The mapper's `--cli-synctex` option retains the historical per-query CLI path. PDF-hash-keyed caches remain in the isolated preview directories.

The exact candidate15 preview is `defect_mapping_20261121T163944299450Z/`. It has 1,977 rows, 0 unresolved current contexts, and 1,952 printed current contexts within pages 1–345. All 1,953 inherited old-item records are unchanged, including 226 intermediate-wording rows without an established exact original-PDF phrase locus. The 21 next rows use candidate13 and the last 3 use candidate14. This preview has not been applied to canonical files.

## Scheduled progress and checkpoints

The authoritative start and schedule are in `records/S6_SERIES_PUBLISH_continuation_restore.json`. Checkpoint11 is due at 2026-11-21 16:56:17 UTC; review06 is due at 17:11:17 UTC. The wrapper refuses an early scheduled operation and an existing immutable output.

```sh
python code/S6_SERIES_PUBLISH_continuation_tools.py checkpoint 11
python code/S6_SERIES_PUBLISH_continuation_tools.py review 6 --render I=render/I_candidateN
```

The snapshot and review commands track page-image identities and individual recorded defect/provenance/check rows. The continuation stall counter starts at zero and advances only at the scheduled hourly reviews. Review output is accompanied by a Markdown insert for the root agent to place in the canonical ledger and report.

Checkpoint packaging preserves every restored checkpoint10 manifest path, includes new textual records and render manifests, validates every packaged byte against a new manifest, and uses a new immutable archive name. New page bitmaps and runtime caches are excluded. A new publication PDF is packaged only when its current final receipt is present and matches. No continuation checkpoint has yet been created by this agent.
