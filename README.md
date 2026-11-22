# S6 complex-structure workbench

AI-produced mathematics on the complex structures on the six-sphere that began with the manuscript of Claude and
Levent Alpöge ([AC26], <https://alpo.ge/s6.pdf>). The main result of the work is a series of five papers on the
(3,4,∞) family. The repository also holds the research runs behind them, their programs and check records, and the
earlier workbench, course and survey.

State of this page: 22 November 2026.

## The five papers: *The (3,4,∞) family of complex six-spheres*

| Paper | State | Newest source here |
|---|---|---|
| I. Periods, moduli and the two ends | Revision and checks finished on 21 November; submitted to Hexagon on 22 November and not yet published | [TeX](pro_returns/S6_SERIES_PUBLISH_checkpoint_34_20261122T1301Z/S6_SERIES_PUBLISH_I.tex), [PDF](pro_returns/S6_SERIES_PUBLISH_checkpoint_21_20261122T0026Z/S6_SERIES_PUBLISH_I.pdf) |
| II. Torus-fibred threefolds and the sign theorem | All 198 required further checks done; editing and the page-by-page reading are under way | [TeX](pro_returns/S6_SERIES_PUBLISH_checkpoint_34_20261122T1301Z/S6_SERIES_PUBLISH_II.tex) (the [PDF of 20 November](pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/S6_SERIES_GRIND_II.pdf) is older) |
| III. Maps and the resulting manifolds | Consolidated draft of 20 November; publication revision not begun | [TeX](pro_returns/S6_SERIES_PUBLISH_checkpoint_34_20261122T1301Z/S6_SERIES_PUBLISH_III.tex), [PDF](pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/S6_SERIES_GRIND_III.pdf) |
| IV. Smooth monodromy in the group of homotopy seven-spheres | Consolidated draft of 20 November; publication revision not begun | [TeX](pro_returns/S6_SERIES_PUBLISH_checkpoint_34_20261122T1301Z/S6_SERIES_PUBLISH_IV.tex), [PDF](pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/S6_SERIES_GRIND_IV.pdf) |
| V. Complex fourfolds from the family | Published: [hexagon:2611.00742](https://hexagonmath.org/2611.00742); version 3 submitted | [TeX](pro_returns/S6_SERIES_PUBLISH_checkpoint_34_20261122T1301Z/S6_SERIES_PUBLISH_V.tex), [PDF](pro_returns/S6_SERIES_PUBLISH_checkpoint_21_20261122T0026Z/S6_SERIES_PUBLISH_V.pdf) |

[`RECORDS.md`](RECORDS.md) gives, for each paper and version, the commit, the records, the programs and their
checksums. It is the address the papers cite.

[`pro_returns/LATEST.md`](pro_returns/LATEST.md) marks the newest return of every run. Use it: older folders keep older
versions of the statements.

## Status of the mathematics

**Every proof here was produced by AI and has been checked only by AI. No human mathematician has checked the
mathematics.**

- Each paper has a check record (`S6_SERIES_PUBLISH_checks_<paper>.md`), and
  [`CHECK_EVENTS.tsv`](pro_returns/S6_SERIES_PUBLISH_checkpoint_34_20261122T1301Z/CHECK_EVENTS.tsv) lists every check
  by statement, with the model, the kind of check and its outcome. A targeted proof check, an independent
  re-derivation and a computation are different events and are recorded as such.
- Refuted statements are recorded with their corrections. In Paper II, the revision of 22 November refuted two
  earlier statements by one explicit compact fibration (tag P205) and corrected both: an elliptic conductor has one
  or two image curves, where the draft said one (tag 02Y6), and the exclusion of ordinary double curves needs
  positive Euler number (tag 02XE).
- In the material of August to October, "verified", "proved" and "closed" are that workbench's own labels. It
  corrected its own "verified" proofs at least six times.
  [`survey_20261112/FINDINGS.md`](survey_20261112/FINDINGS.md) gives the status of those results as of 12 November.

## The work this builds on

The construction is not ours. These works are credited in the papers statement by statement.

- **[AC26]** Claude and Levent Alpöge, *The (3,4,∞) modular family of 2-tori, completed at its three special points, is
  a complex structure on S^6*: <https://alpo.ge/s6.pdf>. The manuscript is AI-written; copies that the runs used are
  in their return folders.
- **[E26]** Philip Engel, *Complex structures on S^6*: [arXiv:2609.38442](https://arxiv.org/abs/2609.38442), and his
  [Threefold Explorer](https://philip-engel.github.io/threefold-explorer/).
- Yun-Heng Du, Bin Guo, Yuta Kusakabe and Song-Yan Xie: [arXiv:2610.00250](https://arxiv.org/abs/2610.00250)
  (version 1 has the standard classification and deformation results).
- Jeff Viaclovsky: *A two-parameter family of complex structures on S^6*
  ([arXiv:2609.33785](https://arxiv.org/abs/2609.33785)), *Combs and complex structures on the six-sphere*
  ([arXiv:2610.10451](https://arxiv.org/abs/2610.10451)) and *Logarithmic transformations on the six-sphere*
  ([arXiv:2610.39102](https://arxiv.org/abs/2610.39102)).
- Wang, *A complex structure on a rational homology six-sphere*:
  [arXiv:2609.11541](https://arxiv.org/abs/2609.11541).
- Xiufan Yang, *Compact complex threefolds fibred by two-dimensional complex tori*:
  [arXiv:2609.29666](https://arxiv.org/abs/2609.29666).
- Liu and Rollenske, *Yet another family of complex structures on S^6*:
  [arXiv:2609.33826](https://arxiv.org/abs/2609.33826).
- Mandal: [arXiv:2609.27929](https://arxiv.org/abs/2609.27929).

The complete bibliography is
[`S6_SERIES_PUBLISH_references.bib`](pro_returns/S6_SERIES_PUBLISH_checkpoint_34_20261122T1301Z/S6_SERIES_PUBLISH_references.bib).

## The runs, 12 to 22 November 2026

All are by GPT-6 Astra (OpenAI, ChatGPT Pro mode). Each folder has the prompt as sent.

| Run | What it did | Newest here |
|---|---|---|
| S6_01_INVARIANTS | Hodge, Bott–Chern and Aeppli numbers, tangent cohomology, Picard twists | [return](pro_returns/S6_01_INVARIANTS/) |
| S6_02_FAMILY | The period family, its identifications and degenerations | [return](pro_returns/S6_02_FAMILY/) |
| S6_02_PUSH | Degenerations, smooth monodromy, the parameter boundary | [final](pro_returns/S6_02_PUSH_final_20261115T2217Z/) |
| S6_03_CDP | Cotangent kernels, torus fibrations, the Campana–Demailly–Peternell argument | [checkpoint 13](pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/) |
| S6_04_MAPS_MANIFOLDS | Maps and manifolds from the torus fibrations | [checkpoint 12](pro_returns/S6_04_MAPS_MANIFOLDS_checkpoint_12_20261116T0243Z/) |
| S6_05_ARITHMETIC | Arithmetic counts, lattice neighbours, elliptic period norms | [final](pro_returns/S6_05_ARITHMETIC_final_20261115T1846Z/) |
| S6_06_BLIND | Second derivations of the central claims from the data alone | [checkpoint 35](pro_returns/S6_06_BLIND_checkpoint_35_20261118T1208Z/) |
| S6_07_PAPER | A first paper assembled from the runs | [final](pro_returns/S6_07_PAPER_final_20261116T1537Z/) |
| S6_09_PAPERS | Three papers with the proofs in them | [final](pro_returns/S6_09_PAPERS_final_20261117T0601Z/) |
| S6_10_PAPERS | The papers rewritten for their readers | [checkpoint 15](pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/) |
| S6_SERIES_GRIND | Everything consolidated into the series of five | [checkpoint 10](pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/) |
| S6_SERIES_PUBLISH | Publication revision and further checks, still running | [checkpoint 34](pro_returns/S6_SERIES_PUBLISH_checkpoint_34_20261122T1301Z/) |

[`pro_returns/Q03_DEPOSIT_20261115T0022Z/`](pro_returns/Q03_DEPOSIT_20261115T0022Z/) is a separate result on
scheduling, unrelated to S^6. It was not submitted, because Jansen
([arXiv:2611.09392](https://arxiv.org/abs/2611.09392)) proves the same theorem with better bounds.

The notes written when the first two runs returned, with their results and reviews:
[`RETURNS_20261112-13.md`](RETURNS_20261112-13.md).

## The earlier material

- **The survey of 12 November:** [`survey_20261112/FINDINGS.md`](survey_20261112/FINDINGS.md) ranks 32 findings of the
  earlier work and says where each statement and proof is; the readers' combined notes are
  [`READING_NOTES.md`](survey_20261112/READING_NOTES.md).
- **The course CG-S6:** [`codex_workspace/courses/CG-S6/README.md`](codex_workspace/courses/CG-S6/README.md), eleven
  lessons with companion chapters and check scripts, to 11 October.
- **The workbench of 24 August to 9 September:**
  [`codex_workspace/canonical_S6_snapshot/`](codex_workspace/canonical_S6_snapshot/); start with `workbench.pdf` and
  `workbench_and_manuscript_overview.pdf`.

## Folders

| Folder | Contents |
|---|---|
| [`RECORDS.md`](RECORDS.md) | The standing records page of the five papers |
| [`pro_returns/`](pro_returns/) | The returns, one folder per prompt or checkpoint. From 22 November a new folder holds the deliverables: papers, reports, registers and programs |
| [`reviews/`](reviews/) | Claude's intakes, reviews and recomputations, with the series design and the route notes |
| [`prompts/`](prompts/), [`raw/`](raw/) | Research prompts with their history; further intakes and prompts |
| [`tools/`](tools/) | Scripts that built and audited the prompts |
| [`claude_math_notes/`](claude_math_notes/) | Claude's working notes on S^6 and on the Grothendieck programme, with consults and check scripts; [`PROGRAMS.md`](claude_math_notes/PROGRAMS.md) says which sections are on S^6 |
| [`survey_20261112/`](survey_20261112/) | The survey of 12 November and its readers' notes |
| [`codex_workspace/`](codex_workspace/) | The workbench, course, consolidation of 30 September, ledgers, correction note and custody records |
| [`yang_mills_repository_s6/`](yang_mills_repository_s6/) | The `s6/` folder of [yang-mills-interacting-workbench](https://github.com/KokunoYumeto/yang-mills-interacting-workbench) at `dff1de9b`, from which this repository was split |
| [`records/`](records/) | SHA-256 lists of the files the papers cite and of the large certificates |
| [`LEFT_OUT.tsv`](LEFT_OUT.tsv) | What the first publication of 12 November left out, file by file, with the reason |

Links inside copied folders keep their original form. A `../` link that points above `yang_mills_repository_s6/`
refers to the Yang-Mills repository; absolute local paths refer to the machine where the work was done.
Working records keep the commit identifiers they were written with; for the papers, use those in
[`RECORDS.md`](RECORDS.md). Certificates over 45 MB are stored as `.json.gz`, with the checksums of the unpacked
files in [`records/large_certificates.sha256`](records/large_certificates.sha256).

## Who produced what

All dates are 2026. Models and efforts are those of the records named.

- **[AC26]:** Claude, under Levent Alpöge's direction (credit as in
  `codex_workspace/courses/CG-S6/provenance.json`).
- **Transcription of the manuscript and reviews A and B (24–26 August):** ChatGPT in Pro mode at reasoning effort
  ultra; review B's build script names OpenAI GPT-5.6 Pro, and the files of review A name no model.
- **Review C and the workbench (24 August to 9 September):** OpenAI Codex, GPT-5.6 Sol at reasoning effort ultra
  until 4 September (with a few GPT-5.6 Luna and GPT-5.6 Terra sessions, at reasoning effort ultra) and GPT-6 Astra
  at reasoning effort ultra from 5 September (`survey_20261112/READING_NOTES.md`, reader I). The correction note [N]
  of 1 September records "OpenAI Codex gpt-5.6-sol, Ultra".
- **Consolidation of 30 September and custody records:** OpenAI Codex, gpt-6-sol at reasoning effort ultra
  (`codex_workspace/custody/FINAL_CUSTODY_AUDIT.json`).
- **Course CG-S6 (to 11 October):** OpenAI Codex, GPT-6 Astra at reasoning effort ultra; prerequisite chapters keep
  GPT-6.1 Sol (reasoning effort ultra) authorship where their arguments are retained.
- **Paper [R], "The S6 record and the integral monodromy of its (3,4,∞) period system" (28 September):** Claude Opus
  5.5 at effort max. Not in this repository.
- **Survey of 12 November:** Claude Fable 5.2 at effort high, from its own reading and the notes of fifteen readers,
  also Claude Fable 5.2 at effort high. The survey is not a verification.
- **Research, papers and revisions in `pro_returns/` (from 12 November):** GPT-6 Astra (OpenAI, ChatGPT Pro mode).
- **Prompts, intakes, reviews and recomputations:** Claude Fable 5.2 at effort high and at effort max, and Claude
  Opus 5.5 at effort max, as each file records; the publication of prompts on 15 November: Claude Opus 5.5 at effort
  high.
- **The repository:** first selection, privacy pass, filing and README of 12 November, Claude Opus 5.5 at effort
  high; the filing since then and this README, Claude Opus 5.5 at effort max.

## What is not here

- Other authors' papers. They are cited and linked; records quote short passages where a check needs exact wording.
- Raw Codex thread records and private working records. A curated chronology of the mathematics is included
  ([`public_mathematical_provenance_v1.md`](codex_workspace/canonical_S6_snapshot/supporting_materials/publication/public_mathematical_provenance_v1.md)).
  Manifests and notes inside copied folders are kept as written, so some of them list files that are not here.
- The source archives' blob stores, private catalogues and private working copies, and the five related source tasks
  on other topics (Yang–Mills, Navier–Stokes, Riemann hypothesis, Geometric Unity).
- The background archives attached to the prompts, and the working files of returns filed from 22 November.

## Changes made for publication

The user's first name was replaced by "user", including in local paths and in compressed files. In a few files,
passages that quote or describe private records were left out. Files changed in these ways no longer match the
SHA-256 values recorded for them in the copied folders' manifests and receipts. No other content of the copied
files was changed.

## Rights and credits

To the extent we hold rights in the AI-produced material of this repository, they are dedicated to the public domain
under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). [AC26] keeps its credit to Claude and Levent
Alpöge. The rights in [E26] and the other cited works are their authors'. Bundled software and data keep their own
credits and notices: Philip Engel's Threefold Explorer (code MIT, documentation CC BY 4.0), MathJax, TeX packages,
python-flint with its libraries, and the lattice data drawn from Gabriele Nebe and Neil Sloane's Catalogue of Lattices.
