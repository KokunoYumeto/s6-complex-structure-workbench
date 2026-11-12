# Consolidation and deduplication map

Date: 26 August 2026

## Current authority

- Public reading and Overleaf main document: project-root `main.tex`
  (123-page annotated edition).
- Clean source: project-root `original_clean_transcription.tex`
  (108-page reconstruction).
- Current validate/repair/disprove mathematics: `workbench.tex` and
  `supporting_materials/workbench/research/` (60-page paper at this consolidation checkpoint).

Files below `workbench_history/` are provenance checkpoints, not competing
current editions.

## Earlier trees and their destinations

| Earlier tree | Current destination | Treatment |
|---|---|---|
| Live 123-page public project baseline | project root and ordinary `supporting_materials/` folders | Retained as the presentation baseline; the current results block and navigation were updated in place. |
| Former 56-page standalone workbench | `workbench/`; checkpoint in `former_workbench_checkpoint_56_pages/` | Its complete proof development became the canonical workbench. The former project itself was not deleted and carries a migration notice. |
| Short conservative workbench branch | integrated propositions in `supporting_materials/workbench/research/`; snapshot in `18_page_branch_2026-08-26/` | Its independent `Pic^0`/duality route was integrated. Regressed topology labels were not allowed to overwrite the fuller proofs. |
| First repair notebook | `early_workbench_2026-08-25/` | Unique source and ledger drafts retained. |
| Earlier 121-page public release | `public_121_page_checkpoint_2026-08-24/` | Unique reader-guide/build records retained as a dated checkpoint. |
| Earlier workflow records | `workflow_record_2026-08-24/` | Unique control, goal, and logbook records retained with portable paths. |
| Human-organized audit/review tree | ordinary review/source folders; portable byte-conflicting predecessors in `preconsolidation_conflicts/` | Missing Reviewer A/B material was merged into the human-facing tree. Safe mathematical/source variants were retained; machine-local records were represented by sanitized successors. |

## Reviewer B integrated-evidence container

The locally supplied container
`reviewer_b_integrated_proof_repair_evidence_2026-08-25.zip` has:

- size: 87,012,011 bytes;
- SHA-256: `155cf2aa4d243a92cb6a19d28a7ee3412c10de871b5283a4d7a96564fa735821`;
- 302 ZIP entries (260 files and 42 directories);
- 98,131,722 uncompressed bytes;
- no unsafe or case-colliding paths.

The 87 MB container itself is not duplicated inside the Overleaf project.
Its substantive reports, checks, ledgers, source extracts, manifests, and
portable text records are under
`../peer_reviews/reviewer_B_corrective_2026-08-25/`. Generated page renders,
build logs, derivative PDFs, and redundant full-release snapshots remain in
the hash-identified container held locally by the depositor; that container
is not itself included or publicly located by this project. Three substantive
historical evidence PDFs are retained in the Reviewer B folder. The
path-level decision for all 260 archive files is recorded in
`../peer_reviews/reviewer_B_corrective_2026-08-25/source_record/REVIEWER_B_ARCHIVE_COVERAGE.json`.
This prevents render caches from
obscuring the mathematical sources or exhausting the editor's project budget.

## Deduplication rule

Byte-identical copies were omitted from the ordinary working tree. A small
number remain inside complete dated checkpoints or evidence-package layouts
where removing them would make the preserved snapshot misleading; those
folders are explicitly non-authoritative. When the same path had different
bytes, the current file stayed at its ordinary human-facing location.
Portable mathematical/source predecessors were retained under an explicitly
dated history or conflict folder; variants whose only distinct content was
machine-local paths were replaced by the sanitized semantic successor and
were not republished byte-for-byte. Superseded navigation/QA prose was
replaced by the current runnable version, not accumulated as another public
entry point. Generated TeX auxiliaries, bulk raster page renders, and
machine-specific build logs were excluded; compiled PDFs were kept only when
they serve as a stable reading or historical reference.

The deliberately unrepublished machine-local predecessor hashes are
`419a6228020ff04ba311003ca66f33b9e7d9298793d5235a88c6e543b9ca5f5d`,
`0f9809af921646bd7f6735923e0fafcdceecae284a58c3e788b26a91f6878de3`,
`a421e8ce3c0005f19924163a12af224efc35c3e21b2a78bea64b9ecac108e714`,
`28b400bfd7405a72e83a62df570a0cf3f36c3069b45f3d5b82ffd69ddaf1a775`,
`5e7ac02bb331cada15256750d1e1834819caa9d63739e8b83ede4fbf5e46c964`,
and
`3e1a4923e413260b66754e878b20c23526181013383fd53bc221629e561c5429`.
