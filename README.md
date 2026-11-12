# S6 complex-structure workbench

This repository holds the AI-produced work on the complex structure on the six-sphere S^6 and the material around it:
the first check of the original manuscript, the workbench that grew from it (24 August to 9 September 2026), the
course CG-S6 (to 11 October 2026), the consolidation of 30 September 2026, and a survey of all of it written on
12 November 2026. It was split out of
[yang-mills-interacting-workbench](https://github.com/KokunoYumeto/yang-mills-interacting-workbench), whose `s6/`
folder is copied here.

The construction itself is not ours. It is the 108-page manuscript produced with Claude under Levent Alpöge's
direction ([AC26], <https://alpo.ge/s6.pdf>), and Philip Engel gave an independent treatment ([E26],
[arXiv:2609.38442](https://arxiv.org/abs/2609.38442)). Neither document is reproduced here; see "What was left out".

## Status of the mathematics

Every proof in this repository was produced by AI models and has been reviewed only by other AI sessions, unless a
file says otherwise. No proof here has been checked by a human mathematician. The labels "verified", "proved" or
"closed" inside the files are the workbench's own; the workbench corrected its own "verified" proofs at least six
times. The survey of 12 November (`survey_20261112/FINDINGS.md`) gives the status of each result, what it adds over
[AC26], [E26] and later papers, and what a full check would have to establish.

## Where to start

1. **The survey of 12 November 2026:** [`survey_20261112/FINDINGS.md`](survey_20261112/FINDINGS.md). It ranks 32
   findings, marks each as settled in the literature, proved in the workbench, sketch or open, and says where each
   statement and proof is. The readers' notes behind it are in `survey_20261112/work/*_notes.md`; their combined text
   is `survey_20261112/READING_NOTES.md`.
2. **The course CG-S6:** [`codex_workspace/courses/CG-S6/README.md`](codex_workspace/courses/CG-S6/README.md). Eleven
   lessons with companion chapters (HTML, with editable Markdown sources in `src/` and check scripts in `checks/`).
   It is the latest treatment of the construction, its topology, canonical ring, deformation and the
   Campana-Demailly-Peternell step.
3. **The canonical snapshot of early September 2026:** `codex_workspace/canonical_S6_snapshot/`. Start with
   `workbench.pdf` (source `workbench.tex`) and `workbench_and_manuscript_overview.pdf`; the research files are in
   `supporting_materials/workbench/research/`, and the AI reviews of the manuscript in
   `supporting_materials/peer_reviews/` (map: `peer_reviews/README.md`).

## How the repository is organized

| Folder | Contents | Source |
|---|---|---|
| `codex_workspace/canonical_S6_snapshot/` | The workbench (`workbench.tex`/`.pdf`), the preprints and drafts derived from it, the reviews A, B and C of the manuscript, evidence folders with checker scripts and their outputs, earlier workbench checkpoints, and the publication records | Local Codex workspace, frozen early September 2026 |
| `codex_workspace/courses/CG-S6/` | The course: lessons 1-11, companion chapters, sources, checks, figures, `provenance.json` | Local Codex workspace, to 11 October 2026 |
| `codex_workspace/mathematical_consolidation/` | The consolidation of 30 September 2026: `CONSOLIDATION.tex`, `CLAIM_LEDGER.md`, `MASTER_MAP.md`, mathematical checks, the catalogue build scripts and receipts | Local Codex workspace |
| `codex_workspace/ledgers/` | Source-reading ledgers and the index of source files | Local Codex workspace |
| `codex_workspace/correction_note_20260901/` | The correction note [N] of 1 September 2026 on the Campana-Demailly-Peternell step (TeX, assessment, bibliography, checksums) | Taken from the workspace's hash-named text store under readable names |
| `codex_workspace/custody/`, `CUSTODY_INDEX.md`, `RELATED_SOURCE_DISPOSITIONS.md` | Records of how the source archives were verified and routed into the workspace | Local Codex workspace |
| `yang_mills_repository_s6/` | The `s6/` folder of yang-mills-interacting-workbench at commit `dff1de9b`, including the status note of 5 October 2026 (`STATUS_2026-10-05.md`) and the public form of the 30 September consolidation | GitHub |
| `survey_20261112/` | The survey: `FINDINGS.md`, `READING_NOTES.md`, the fifteen readers' notes and their scratch scripts | Survey of 12 November 2026 |
| `pro_returns/` | The prompts sent to GPT-6 Astra in ChatGPT Pro mode and what came back, one folder per prompt: `PROMPT.md`, `RETURN_NOTES.md` and the unchanged return in `return/` | Returns of 12 November 2026 onwards |
| `LEFT_OUT.tsv` | Every file of the sources that is not in this repository, with its size, SHA-256 and the reason | This publication |

Links inside the copied folders keep their original form. Links in `yang_mills_repository_s6/` that point above the
folder (`../`) refer to the Yang-Mills repository; absolute local paths refer to the machine where the work was done.

## Who produced what

All dates are 2026. Model names and effort settings are those given in the records named.

- **Original manuscript [AC26]:** produced with Claude under Levent Alpöge's direction (credit as given in
  `codex_workspace/courses/CG-S6/provenance.json`). Not included.
- **Transcription of the manuscript and reviews A and B (24-26 August):** ChatGPT in Pro mode (ten transcription
  strips, two full reviews and their corrective rounds). The build script of review B names the model as "OpenAI
  GPT-5.6 Pro" (`peer_reviews/reviewer_B_corrective_2026-08-25/source_record/scripts/build_reports.sh`); the files
  of review A do not name a model.
- **Review C and the workbench (24 August to 9 September):** OpenAI Codex. According to the session records summarized
  in `survey_20261112/READING_NOTES.md` (reader I), the sub-agents were GPT-5.6 Sol at effort ultra until 4 September
  (with a few GPT-5.6 Luna and GPT-5.6 Terra sessions) and GPT-6 Astra at effort ultra from 5 September; the root
  session was recorded as GPT-6 Astra at effort ultra at the time of capture. The correction note [N] records "OpenAI
  Codex gpt-5.6-sol, Ultra".
- **Consolidation of 30 September and the custody records:** OpenAI Codex; the consolidation main session is recorded
  as gpt-6-sol at effort ultra (`codex_workspace/custody/FINAL_CUSTODY_AUDIT.json`).
- **Course CG-S6 (to 11 October):** OpenAI Codex, GPT-6 Astra at effort ultra (course README); prerequisite chapters
  keep GPT-6.1 Sol authorship where their arguments are retained.
- **Paper [R], "The S6 record and the integral monodromy of its (3,4,∞) period system"** (28 September), cited by the
  status note of 5 October: Claude Opus 5.5. Not in this repository; it is in Zenodo record
  [10.5281/zenodo.23003415](https://doi.org/10.5281/zenodo.23003415).
- **Survey of 12 November (`survey_20261112/`):** Claude Fable 5.2 at effort high, from its own reading and the notes
  of fifteen readers, also Claude Fable 5.2 at effort high. The survey is not a verification.
- **Returns of the Pro prompts (`pro_returns/`):** GPT-6 Astra (OpenAI, ChatGPT Pro mode), from 12 November; not
  reviewed by a person. The return notes and their filing: Claude Opus 5.5.
- **This repository's selection, privacy pass and README:** Claude Opus 5.5.

## What was left out

`LEFT_OUT.tsv` lists every omitted file with the reason. In short:

- copies of the original manuscript [AC26] (transcriptions, annotated copies, page extracts) and of third-party
  papers; the review reports themselves are included;
- raw conversation material: Codex thread records, dialogue files and their extracts, including the 385 MB thread
  item ledger. The sanitized public records prepared for publication are included
  (`canonical_S6_snapshot/supporting_materials/publication/complete_sanitized_conversation_v1.jsonl` and
  `full_record_public_annex_v2/`);
- the hash-named blob stores of the source archives (older versions of the files included here, mixed with
  conversation records and third-party papers), the private catalogue databases (270 MB) and private working copies;
- the five related source tasks on other topics (Yang-Mills, Navier-Stokes, Riemann hypothesis, Geometric Unity);
- TeX build by-products, Python caches, compiled binaries, rendered page images, the 77 MB Koide census (reproducible
  with the checker beside it) and duplicates.

The prompts for GPT-6 Astra in ChatGPT Pro mode that the survey prepared (six in `FINDINGS.md`, since merged into five:
`S6_01_INVARIANTS`, `S6_02_FAMILY`, `S6_03_CDP`, `S6_04_MAPS_MANIFOLDS`, `S6_05_ARITHMETIC`) are published with their
returns in `pro_returns/` as each comes back (see "Returns of the Pro prompts" below); the prompts' background archives (the attached
sources) are not published.

## Returns of the Pro prompts

### S6_01_INVARIANTS (returned 12 November 2026)

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); not reviewed by a person. Folder:
[`pro_returns/S6_01_INVARIANTS/`](pro_returns/S6_01_INVARIANTS/) (prompt `PROMPT.md`, notes `RETURN_NOTES.md`, the
return unchanged in `return/`; check it there with `sha256sum -c MANIFEST_SHA256.txt`). The programs were returned by
the model and have not been run by us. The model rendered pages 5, 62, 63 and 81 of [AC26] and extracted the text of
pages 62-63 to check the passages it corrects; these four pages are kept in `return/outputs/` and `return/logs/` as
part of its record.

**What was asked.** An independent derivation of the Hodge diamond of the complex threefold X of [AC26] with the
decisive scalar evaluated (Part A); the same invariants for the other members of the family (B); Frölicher,
Bott-Chern and Aeppli cohomology and special metrics (C); the tangent cohomology, the Kuranishi space and every Picard
twist (D); and the deformations and comb members (E).

**What came back.** A 48-page paper (`return/S6_01_INVARIANTS_paper.pdf`) with 47 numbered statements (41 Proved,
2 Known, 2 Refuted, 2 Open; `return/S6_01_INVARIANTS_results.csv`), the report `return/S6_01_INVARIANTS_report.md`,
code, outputs and logs. Fourteen of the sixteen items are finished at outcome (a), C.3 and E.2 are unfinished:

- A.1-A.4: the cotangent direct images; the scalar μ_s(0) = i·4√π/(3^{3/4}Γ(1/4)²), nonzero, computed to 100 digits
  by two methods; h^{1,2} = h^{2,1} = 1, h^{1,1} = h^{2,2} = 2, independent of c; the cusp-torsion assertions of [AC26]
  Remarks 1.3 and 9.21 corrected (statement A4.2, Refuted), the workbench's degree-one correction confirmed.
- B.1-B.3: the same Hodge numbers for all admissible (3,4) twists and all coprime (3k,4l); K_X and the anticanonical
  ring for each (3k,4l); the universal covers of the members with finite fundamental group have h^{1,1} = h^{2,2} = n+1.
- C.1-C.2: E₁ ≠ E₂ = E_∞ with the differentials on a named basis; Bott-Chern numbers (1,0,2,2,2,2,1) and Aeppli
  numbers (1,2,2,2,2,0,1) computed directly.
- C.3, unfinished: the Bott-Chern algebra, the Picard map, the +12 sign, the non-Kähler degrees and the metric types
  (no balanced, SKT, astheno-Kähler or Chern-Ricci-flat metric; Gauduchon metrics exist) are proved; evaluated
  coefficients of the global representatives G, Q are missing.
- D.1-D.4: h(T_X) = (1,1,1,0); the Kodaira-Spencer map of the family is an isomorphism; the Kuranishi space is a
  smooth line; the tangent cohomology of every twist T_X ⊗ M, with r = 1 for every nonintegral twist.
- E.1: small deformations keep the elliptic fibration and algebraic dimension one.
- E.2, unfinished: for the comb members h(T_{X_m}) = (2m+1, 8m+1, 6m+1, 0) is proved, which refutes the universal
  bound h⁰(T) ≤ 2 of [AC26] Remarks 1.2/9.26 and of HKP Corollary 1.3 (statement E2.4, Refuted); the Hodge-kernel
  splitting, the torsion support and the obstruction maps remain open.

## Changes made for publication

The user's first name was replaced by "user" in every file, including local paths and the contents of compressed
files. Files changed this way no longer match the SHA-256 values recorded for them in the manifests and receipts
inside the copied folders. No other content was changed.

## Rights

The rights in the original manuscript [AC26] and in [E26] belong to their authors; neither is reproduced here. To the
extent we hold rights in the AI-produced material of this repository, they are dedicated to the public domain under
[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Bundled third-party software and fonts (for example
MathJax in `codex_workspace/courses/CG-S6/assets/`) keep their own notices.
