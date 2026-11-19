# Source audit working notes and handoff

Date: 15 November 2026, Europe/Berlin. Checker: GPT-6 Astra, effort ChatGPT Pro mode.

## Delivered source work

- `Q03_DEPOSIT_sources.md` contains the S checks, exact source locators, availability limits, numeric constants and full 44-row dependency source concordance.
- `Q03_DEPOSIT_literature.md` contains the dated search, every recorded query and returned-source headings. The closing pass repeats the exact-title/fixed-m search on the same date.
- `work/C_bibliography.tex` is an integration-ready bibliography, with the FKN erratum and discovered Jansen/Giraudin literature.
- `work/C_dependency_source_map.md` and `code/C_dependency_source_map.json` give exact corrections for dependency column 2; they do not replace Part B's internal dependency audit.
- `code/C_*` programs retain retrieval/comparison/locator metadata, outputs and the reproducible search-log renderer.

## Corrections made during this audit

The README at drbh bbd3013 still describes the baseline. An initial interpretation based on that README was withdrawn after opening the exact commit diff and source files. Model.lean has capacity 4, Main.lean proves the complete release statement and the adaptation's retained names do not determine its semantics. The final source report contains the corrected scope only.

The OpenAI comparator target contains `sorry`. This is recorded explicitly; it must not be mistaken for the completed proof. The actual `lean/OAI/Computability/Scheduling/` source directory was separately inspected: all 53 Lean files, including Model.lean and Main.lean. Removing the comparator's target theorem declaration yields byte-identical Model.lean. The actual Main.lean contains the proof body. No independent Lean build is claimed for either repository.

The search's important new result is the already public Jansen fixed-machine theorem and linear leaf budgets. Its entire external proof was not independently checked. The Q03 result therefore carries no claim of novelty or priority from this audit. Giraudin's three-machine refinement is also existing literature.

Garey–Johnson access succeeded after an initial size-limit rejection and a truncated transfer: complete validated range download, visual OPEN8 p.287 and SS9 p.239 check. Coffman–Graham pp.202–203 were also visually checked after OCR digit errors. Original FKN 1969 full proof remains unavailable; publisher metadata/abstract and the 1971 erratum were opened.

## Research-cache exclusions from the final deliverable

These early work files were moved outside the deliverable directory to `retrieved_sources/audit_aux/`. They contain retrieved source material, not new proof-audit conclusions. Their factual conclusions and identifiers are superseded by the source report and metadata outputs:

| Former deliverable-tree path | Reason retained externally instead |
|---|---|
| `work/openai_paper_live.txt` | Full retrieved preprint text; the thirteen-file byte comparison and exact locator map replace this duplicate. |
| `work/drbh_README_bbd3013.md` | Full pinned README; corrected README/code discrepancy is recorded in S-D. |
| `work/drbh_commit_bbd3013.json` | Full GitHub commit diff, including retrieved source code; exact commit hash and scope checks are sufficient for the deposit. |
| `work/drbh_commits.json` | Raw repository history API response; the relevant commit/date sequence is recorded in S-D. |
| `work/drbh_model_bbd3013.txt` | Full retrieved model source; exact declarations and line locators are recorded in S-D. |

All fetched PDFs, scans, course text and complete repository files were written directly under the external `retrieved_sources/` cache. They are not included in the final ZIP. Source URLs, versions, hashes, failed attempts and factual source comparisons remain in the deliverables. The original user attachments remain the separately supplied inputs and are not duplicated.

## Residual source-verification limits

1. Original FKN 1969 full proof unavailable after publisher PDF/access attempts; abstract and 1971 erratum checked.
2. Course-advertised `provenance.json` returned HTTP404; all 11 chapters and other metadata accessible.
3. Neither OpenAI nor drbh Lean builds were replayed; text inspection is not formal proof verification.
4. Jansen/Giraudin complete external proofs were not independently audited; their statement scope was checked.
5. A finite web search does not establish a complete forward-citation census; all found relevant citing/derived items and the query limits are recorded.

## Execution detail

The first multi-process Coffman–Graham OCR run was stopped after hanging under unrestricted OCR threading. The final reproduction script sets `OMP_THREAD_LIMIT=1`, and its complete metadata output was regenerated. The OCR text and rendered scan pages remain outside the deliverable tree. Key printed pages were visually checked, so OCR digit mistakes are not used as bibliographic evidence.
