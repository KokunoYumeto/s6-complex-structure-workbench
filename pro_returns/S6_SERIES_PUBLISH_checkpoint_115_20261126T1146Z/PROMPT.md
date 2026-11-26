**The attached files.** Besides this file there is one ZIP, `S6_SERIES_PUBLISH_continue_cp100.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `S6_GRIND_6_literature.zip` is the folder `S6_GRIND_6_literature/`, and checkpoint 100 is the folder `S6_SERIES_PUBLISH_checkpoint_100/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# S6_SERIES_PUBLISH: the five S6 papers made publication-ready

Writing and checking prompt, 20 November 2026, for GPT-6 Astra (OpenAI), ChatGPT Pro mode, sent again on 26 November
2026 as its ninth continuation, from checkpoint 100 (section 0). File prefix of every deliverable: `S6_SERIES_PUBLISH`.
Written by Claude Opus 5.5 (Anthropic) at effort max, which rewrote section 0 and the passages that refer to it on 22,
23, 24, 25 and 26 November. It continues the prompt `S6_SERIES_GRIND_PROMPT.md` (attached), whose run produced the five
papers the first run started from.

**Start with Paper III, where checkpoint 100 left it.** Paper II is final. Then Paper IV. Papers I, II and V wait for
the last step, the five together.

## This prompt may be sent more than once, from any account

Everything you need is in the attached ZIP. Do not search any Library, Space, project or earlier conversation, and do
not rely on any file that is not attached.

The **base files** are every file in the ZIP, checkpoint 100's folder included. `BASE_FILELIST.tsv` gives the size,
SHA-256 and origin of each.
- **Restore your workspace:** the folder `S6_SERIES_PUBLISH_checkpoint_100/` is the working directory, already merged (checkpoint 21, then
  checkpoints 35, 44, 52, 62, 70, 91 and 100, each over the ones before). The restore instructions in the checkpoints'
  own READMEs and in the earlier prompts are superseded by this paragraph.
- **A newer return:** if a ZIP named `S6_SERIES_PUBLISH_checkpoint_NN.zip` with NN above 100 (or several parts of one),
  or `S6_SERIES_PUBLISH_final.zip`, is attached as well, its files take the place of the files of the same paths in
  that folder. Continue from the state it records.
- **Verify** with `python restore_cp100.py`, run in the unpacked folder: it checks every base file against
  `BASE_FILELIST.tsv`.
- Read the checkpoint's `S6_SERIES_PUBLISH_report.md` (its last sections first) and `PROGRESS_LEDGER.md`, then continue
  the work from the state they record.
- Number your next checkpoint NN+1 (after checkpoint 100: `S6_SERIES_PUBLISH_checkpoint_101.zip`).
- Record the continuation, with its start time, in the ledger and the report.

## 0. This continuation: the nine runs so far, and what has changed

**Two checkpoints named 10.** In sections 1 to 5, "checkpoint 10" is the checkpoint 10 of S6_SERIES_GRIND
(20 November 2026, 02:11 UTC), the state the first run of this prompt started from. This prompt's own checkpoints are
numbered 01 to 100; you continue from its checkpoint 100.

### 0.1 The runs of this prompt, and the state at checkpoint 100

GPT-6 Astra (OpenAI), ChatGPT Pro mode, ran this prompt nine times:
- **the first run,** from 20 November 2026, 22:42 UTC, to its checkpoint 10 (21 November, 06:12 UTC);
- **the first continuation,** from 21 November, 16:11 UTC, to checkpoint 21 (22 November, 00:26 UTC);
- **the second continuation,** from 22 November, 03:15 UTC, to checkpoint 35 (22 November, 13:45 UTC);
- **the third continuation,** from 22 November, 16:56 UTC, to checkpoint 44 (22 November, 23:41 UTC);
- **the fourth continuation,** from 23 November, 10:47 UTC, to checkpoint 52 (23 November, 16:47 UTC);
- **the fifth continuation,** from 23 November, 18:26 UTC, to checkpoint 62 (24 November, 01:56 UTC);
- **the sixth continuation,** from 24 November, 11:15 UTC, to checkpoint 70 (24 November, 17:16 UTC);
- **the seventh continuation,** from 24 November, 19:34 UTC, to checkpoint 91 (25 November, 11:19 UTC);
- **the eighth continuation,** from 25 November, 15:23 UTC, to checkpoint 100 (25 November, 22:08 UTC). Its
  checkpoint 93 never reached us; checkpoint 100 holds all of its work since checkpoint 91, so nothing of it is lost.
  Nothing after checkpoint 100 reached us: neither review 70, due at 22:23:14 UTC, nor checkpoint 101, due at
  22:53:14 UTC. Checkpoint 100's files match its file list in size and SHA-256.

Work done after checkpoint 100 that did not reach us is lost: redo it from the records of that checkpoint.

The state (the report and `PROGRESS_LEDGER.md` give the detail):

| Paper | State at checkpoint 100 | Source SHA-256 |
|---|---|---|
| I | complete: gate closed 21 November, 18:27 UTC; published (section 0.2) | `179fcc4e...` |
| II | **final:** gate closed 23 November, 13:13 UTC, with all 5,876 unit criteria done; its 787-page PDF (`b31d78f9...`, attached) read page by page by you, and read again by us (section 0.7) | `106fcde4...` |
| III | **in progress:** all 128 required checks done; the text rewritten in its source and regrouped into 28 sections after its first clean build; 3,158 of its 3,248 unit criteria done, 90 open | `1d9ee185...` |
| IV | not begun: 66 required checks; its 756 unit criteria open | `75e93bc2...` |
| V | complete since checkpoint 04; version 3 published (section 0.2) | `f89b9ece...` |

**Settled in the seventh continuation,** each with its events in `CHECK_EVENTS.tsv` and its defect rows and receiving
proof in its checker folder (statement numbers are those of checkpoint 10):
- **02S8 and 02S9** (`night:P3F.31` and `night:P3F.32`, Theorems 6.5 and 6.6): their conclusions stand, with corrected
  proofs. The capped square gives return index zero, oriented homotopy-sphere class zero and the product mapping
  torus; the refuted substitutions of the original proofs stay recorded.
- **02KS** (`maps:src:D.2.18`, Theorem 5.27): (D.V1) and (D.V2) stand; (D.V3) is refuted by the integral divisor cube
  6, and the refined classification (for n = ±1, X is diffeomorphic to Fl(C³) # (S² × S⁴) # (S³ × S³) # Σ₀(N_m)) is
  proved.
- **Six more statements whose smooth identification failed in part,** each refuted where it fails and refined with a
  complete proof, its homology and its other invariants kept: 02LB (`maps:src:D.2.35`, 5.44: the stipulated fan gives
  cubic 1 + κ, so 7 of its 15 patterns are not the cubic-one conic), 02LC (`maps:src:D.2.36`, 5.45: ten assignments),
  02LE (`maps:src:D.2.38`, 5.47: the uniform conic factor, three odd assignments and the type counts), 02LJ
  (`maps:src:D.2.42`, 5.51: rows 1, 2, 5 and 14 have cube zero, rows 6, 7 and 10 an invariant P of order 5), 02LL
  (`maps:src:D.2.44`, 5.53: four identifications) and 02LM (`maps:src:D.2.45`, 5.54: eight assignments).
- In all, the seventh continuation recorded 24 refuted events. The others refute the scope of a count (02LI, D26) or
  intermediate steps and auxiliary formulas of proofs whose conclusions are proved another way (D25), among them the
  physical-circle and fan assertions of 02L0, 02L1, 02L7 and 02LF, the auxiliary order formula (D.ST12) of 02L2, the
  period-index inference of 02LN, the orientation sign of 02LQ, and the reading of Zhubr's page 793 in 02K9
  (`maps:src:D.1.11`: it prints H₂, not rank H₃ = 0).

**Settled in the eighth continuation,** in the same way:
- **02LG** (`maps:src:D.2.4`), the last required check, is the eighth instance of D27: its uniform residual models
  (P = 2, 0, 14) fail in 12 of its 18 assignments. The refined statement has P = 2ε, 4ε and 4 + 10ε, with models
  Z_(4,ε), Z_(8,ε) and Z_(4,ε) # Z_(5,1); its counts 495, 59/50, 162 and 18 stand.
- **02LT** (`maps:src:D.2.51`) and **02LV** (`maps:src:D.2.53`), the two comparisons outside the 128, are admitted: each
  refutes intermediate steps (D25) of a proof whose conclusions stand.
- These are the three refuted events of the eighth continuation. The three events of nonstandard type that checkpoint
  91 carried (02LF, 02LI, 02LN) now have their standard type, and our 11 intake rows of checkpoints 71 to 91 are merged.
- **The text.** Paper III's source carries the repairs and the refined statements, for the first time since checkpoint
  44 (`9105ab47...` then, `1d9ee185...` now), with every label, tag target and proof kept: 1,222 labels, 1,161 tag targets,
  137 proofs. In its front matter the outline of main theorems A and B asserted an exact factorization and an equality
  f = H P e that the body does not prove; it now states the homotopies the body proves (three D25 rows).
- **The first clean build** (pass 08, of the source before the regrouping below): 694 pages, two overfull boxes of
  0.83pt and 1.34pt, no undefined reference or citation and no missing font.

**No other paper cites these statements in its text.** In the sources of checkpoint 70, which checkpoints 91 and 100
leave unchanged, Papers I, II and IV carry the labels, tags and printed numbers of the statements refined in the
seventh and eighth continuations only in their shared block of cross-reference definitions, and Paper V not at all.
Check this again on the final sources, and recheck every use recorded under another name (Paper IV's statement records)
in the IV phase.

Open in Paper III, as checkpoint 100 records it (`S6_SERIES_PUBLISH_unit_progress.tsv`, the report and the README):
- **The structural pass after the regrouping.** The reading of 80 pages of pass 08 found sections of 72, 100 and 299
  pages (D14); fourteen heading replacements regrouped 58 units into 28 sections. Open: the 58 D14 rows and the
  clean-build gate, with 23 D23 rows, 6 D18, 2 D04 and 1 D24 (90 in all); the visual repairs and hyperlink bindings that
  reading found, in preparation; the generator of the derived records, reviewed and held until the layout is final.
- **Provenance:** 61 claims of Paper III, 56 complete; four joint-series claims and the visibility of the printed
  programs table open.
- **The build, the typesetting check and the reading of every page** of the final PDF. The deposit fields of Paper III
  are drafted.
- **T1, from our reading** (section 0.8): the source does not build under a current LaTeX kernel. Fix it before the
  next build.
- **The typing of `S6_SERIES_PUBLISH_defects_III.tsv`:**
  - two rows are typed `D45` (III-C8-APPLY-127-02LM-1 and III-C8-APPLY-128-02LM-1), a type the register does not have;
    the matching rows of the other D27 statements are typed D27;
  - ten rows carry D27 on six statements that have no D27 finding: III-C8-APPLY-087-02L1-1 and -088 (02L1),
    III-C8-APPLY-091-02L3-1 and -092 (02L3), III-C8-APPLY-103-02LA-1 and -104 (02LA), III-C8-THREE-PUB-047-D27 and
    III-C8-THREE-READBACK-019-D27 (02LF), III-C8-LV-PUB-038-D27 (02LV) and c8-III-regular-025
    (`wb:cusp-spec-globalization-obstruction`). The reasons of the last four say that no classification changes. Give
    each row the types of what it fixes; where a row does record a D27 instance, log that instance as a D27 finding,
    with its check event;
  - the type column separates several types by `;`, `,` or `/`: use one separator.

Work that was prepared and not yet admitted at checkpoint 100 is in the folders `agents/continuation4_*` to
`agents/continuation8_*`: use it.

**Defect types D26 and D27, all their instances so far in Paper III.** Both block publication.
- **D26,** "missing or ambiguous parameter scope in a statement", added by the fourth continuation: eleven instances by
  checkpoint 70 (02K2, 02KE, 036W, 0374, 02KN, 02KY, 038T, two in 038W and two in 038X) and six in the seventh
  continuation (02L4, 02LA, 02LD, 02LH, 02LI, 02LU); the eighth continuation's text pass logged its D26 rows in
  `S6_SERIES_PUBLISH_defects_III.tsv`. In each instance, a sentence true for the general value of a parameter fails at
  a value that the statement allows, or leaves its scope unstated.
- **D27,** "a claimed smooth identification contradicted by a preserved integral invariant", added by the seventh
  continuation: eight instances, 02KS, 02LB, 02LC, 02LE, 02LJ, 02LL and 02LM (seventh continuation) and 02LG (eighth).

`S6_SERIES_PUBLISH_new_defect_applications.tsv` records where each is applied: Paper III now, Paper IV after it, and
Papers I, II and V in the five-together step.

### 0.2 What has been published

1. **Paper I is published** on Hexagon (hexagonmath.org), the public repository of section 1, as hexagon:2611.00851,
   version 1, public since 23 November 2026, 20:40 UTC. It was committed in its corrected form on 22 November at
   15:00 UTC, and committed again at 19:31 UTC with its links changed to the records page: the version published.
   - Attached: `S6_series_I_public_v1.tex`, the source as committed at 19:31 UTC (SHA-256 `e9674156...`), and
     `HEXAGON_METADATA_I_public_v1.json`, its deposit fields. They replace the files of those names in the earlier
     continuations: only links and the printed commit differ.
   - It is your final Paper I (`179fcc4e...`) with these changes of ours: the accent of "Bézout" restored in two
     places (the proof that uses Bézout's identity and the programs table); in step 8 of Theorem 21.16 the second
     family renamed from D_m to D_{Σ_m}, "for the member Σ_m with these m added rays", because Proposition 21.15
     already uses D_m; its program links, now each a link to the records page (section 0.3), with the sentence on the
     links changed to say so; and the printed commit of section 0.3.
   - Claude Opus 5.5 (Anthropic) at effort max read all 343 pages on 21-22 November before the first deposit and
     found no mathematical error. Its log is attached, `CLAUDE_READING_LOG_PAPER_I.md`, and lists what it recomputed.
     It is a reading of the whole text and not a re-derivation of each proof.
   - **Its text of record is `S6_series_I_public_v1.tex`.** Its gate stands. Do not reopen, rebuild or reread it
     before the five-together step. There, start from that file and write its version 2: what the series requires,
     the links of section 0.3, and one point of notation found in that reading (Cited result 23.10 writes the
     arithmetic equation's coordinates in lower case, where Definition 2.6 and section 24 use capitals). Write the
     note for version 2 in the deposit fields: plain text, at most 2,000 characters, saying what changed and why.
2. **Paper V is published** on Hexagon as hexagon:2611.00742, now in version 3: version 2 of 21 November, 03:20 UTC,
   and version 3, submitted on 22 November at 19:32 UTC and public by 24 November. Version 3 changes only
   the references to the repository: they go to the records page, through the macro `\SsixRecordsPage`, and the
   commit it prints is that of section 0.3. Its text of record is now `S6_series_V_public_v3.tex` (SHA-256
   `f3df9432...`), the source of version 3 as published, and `HEXAGON_METADATA_V_public_v3.json` is its deposit form,
   in place of `HEXAGON_METADATA_V.json` wherever this prompt names that form. `S6_series_V_public_v2.tex` remains
   the source of version 2. In the five-together step change V where the series requires it
   (references to I-IV, the series table of §1.1, the notation), starting from `S6_series_V_public_v3.tex`; log every
   change in `S6_SERIES_PUBLISH_defects_V.tsv`; write the note for its version 4 in the deposit fields. A
   mathematical error found in V is corrected and recorded like any other (section 4.2). If V needs no change, it
   stays as published, and the report says so.
3. **What V takes from Paper II.** V uses IV 2.54, whose proof goes through IV 2.52 and III 5.23, 5.21 and 5.15 to
   II 13.23 and II 13.24 (`push:src:E.5.2` and `push:src:E.5.3`, in cp10's numbering). Both stand unchanged in
   Paper II's final text. If the statement of either changes, recheck that chain through V and report it at the top
   of the report.
4. **Two statements of Paper II were refuted and refined by the second continuation:** `night:P4R.13` (tag 02Y6) and
   `night:P4.40` (tag 02XE). Papers I and V use neither. Their uses in Paper II were rechecked against the refined
   statements by checkpoint 44. In Papers III and IV, recheck every use of them against the refined statements.
5. **What is deposited next, together:** Papers II, III and IV, Paper I's version 2 and Paper V's version 4 if it
   changed. Papers II-IV cite I and V by the numbering and tags of their posted versions, regenerated in the
   five-together step if these change.
6. **Hexagon takes the TeX source alone.** No record or program accompanies a deposited paper, so no paper and no
   deposit field says that records or programs accompany its source.

### 0.3 One records page: the rule for every link

The series has one standing records page, which we update:
`https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md`, with one section for each paper, `#paper-i` to `#paper-v`
(a copy as of 23 November is attached: `RECORDS_page_20261123.md`). For every version still to be deposited (II, III,
IV, Paper I's version 2, and Paper V's version 4 if it is written):
- **The one repository address** in the paper's source, in its PDF and in each deposit field is that page at the
  paper's own section, for Paper II `https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md#paper-ii`. Set
  `\SsixPublishRecords` to it. No link to a commit, snapshot, folder or file of the repository remains, also not in a
  source comment and not through `\CompendiumRef` or any other macro.
- **The commit** is printed once, in §1.5, through `\SsixRepositoryCommit`, set to
  `a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7`, the commit that Papers I and V print; we reset it at deposit. Paper II's
  final source already sets both macros as this section requires. No other commit identifier stands in the source,
  its comments or the deposit fields.
- **Programs** are named in the paper's programs table as plain text, by file path, without a link. The page links
  them.
- **For the page,** deliver `S6_SERIES_PUBLISH_records_<P>.tsv` for each such paper: one row for each file the paper
  names, with the path as printed, the full path in the repository or `code/<file>` for a program of these runs, and
  its SHA-256. Every repository path is found in the attached `REPOSITORY_PROGRAM_PATHS.txt` (the programs at that
  commit), and every `code/` path in the checkpoint's `code/`. A printed path found in neither is wrong: repair it.

This rule replaces every other instruction on links and pins in the attached prompts, reports and records. Their
addresses are history and are not copied into a paper or a deposit field.

### 0.4 The ledger rows

The rule of the progress check is unchanged. Its rows follow the work on the text, unit by unit, where a unit is a
subsection, or a section that has no subsections:
- each defect type in each unit: done when no instance of it is left in that unit's current source and every instance
  there is logged. Since checkpoint 51 each unit of Papers III and IV has a D26 row as well, and since the seventh
  continuation a D27 row;
- each unit's restructuring under section 3.4: done when its material stands in its final place, with one statement
  and one proof for each result;
- each required check; each provenance claim; each paper's clean build; each page of the current candidate PDF;
- each finding of our reading of Paper III (section 0.8): done when its change is made and logged, or when the finding
  is shown wrong and that is logged.

A row opens again only when an edit or a reading finds an instance in it. Review 69 (25 November, 21:27 UTC) found
movement, and review 70, due at 22:23:14 UTC, did not reach us, so this continuation starts with no review without
movement. The work has passed three hours, so its reviews fall every hour from its start.

### 0.5 The time goes into the papers

The second continuation saved seven diffs of the inventory of about 48 MB each, which differed almost only in line
endings, and a manifest, seal or rebinding for nearly every batch of edits. From now on:
- **An edit's record is its row in the defects table, and a check's record is its row in `CHECK_EVENTS.tsv`.** Make no
  manifest, seal, receipt, rebinding, transport record or census refresh for an edit or a batch.
- **Derived files** (inventory, check files, tags, counts, hashes, deposit fields) are recomputed when a paper's text
  is final and again in the five-together step. Save no diff and no copy of them.
- **Text files are written with LF line endings,** by every program.
- **At a checkpoint** add one short dated section to the report: what changed and which rows closed.

The checks themselves are unchanged: every rewritten proof is read against the proof it replaces (section 4.2), and
the event is recorded.

### 0.6 How checkpoint 100 is packed, and your checkpoints

`CP100_INDEX.tsv` has one row for each path of the merged working directory:
- **packed:** in the folder `S6_SERIES_PUBLISH_checkpoint_100/`, byte for byte;
- **copy:** the same bytes as a packed file. Where a program needs such a path,
  `python restore_cp100.py --copy <path or folder> ...` recreates it;
- **normalized:** one of the seven large diffs, replaced by the same diff without the change of line endings;
- **left out:** earlier versions, large working files of earlier steps, working files of the finished Papers I and V,
  PDFs other than Paper II's final PDF, images and downloaded copies used in finished steps. The row gives the reason. Open a published work again
  online where the work needs it, at the version and locus the retrieval records give.

A path that an earlier record cites and that is not packed is no lost record: it reopens no row, no check and no gate.

**Your checkpoints and your final ZIP are lean:**
- A checkpoint holds every deliverable in its current version, `code/`, and every other file of yours created or
  changed since checkpoint 100 that the next step needs. Unchanged base files are not copied into it.
- Neither holds a copy of a published work, whole or in part: no PDF, extracted or OCR text, page image, saved web
  page, or log that reproduces its passages. Record its address, version, SHA-256 and the locus read, and say in your
  own words what it states.

**No copies of sources in any ZIP you return.** No ZIP you return holds an unchanged copy of an attached file, or a
copy or plain text extraction of another author's paper, book or scan. We have the attached files; for a source you
fetched yourself, record the citation, the address, the SHA-256 and the pages used. Whatever this task asks you to
deliver (transcriptions, translations, editions, notes, programs, figures) always goes in.

The base files and your newest checkpoint alone restore your workspace.

### 0.7 Our reading of all of Paper II, for the five-together step

Claude Opus 5.5 (Anthropic) at effort max read all 787 pages of Paper II's final PDF (`b31d78f9...`) on 24 November
2026, page by page, against its source, and recomputed by hand most of the steps on which each proof turns (with
sympy where a computation is long). It found no mathematical error. It found 23 points of presentation (P1-P23) and 4
of typesetting (T1-T4):
- `CLAUDE_READING_FINDINGS_PAPER_II.tsv`: one row for each, with its place (page of the final PDF, statement, line of the final source), the
  finding, the proposed change and its state after the reading;
- `CLAUDE_READING_LOG_PAPER_II.md`: the log, part by part: what was recomputed, and each finding in context.

These two files are unchanged since the eighth continuation.

In the five-together step, where Paper II changes (section 0.2), settle every row: make the change, or another that
removes the defect, and log it in `S6_SERIES_PUBLISH_defects_II.tsv` under the finding's id; where you find a finding
wrong, log under its id why, and leave the text. Several rows concern the series as a whole: P4 and P11 (the series
table must say which results of each paper use which results of another; the reading checked that no proof is
circular between Papers II, III and IV), P9 and T2 (the printed references to the other papers, regenerated from the
posted Papers I and V and the final III and IV), and P23 and T1 (the programs table, under section 0.3). P19 and P21
correct published work, and both are checked at the source: P19 against AC26 (Remarks 1.2 and 9.26), and P21 against
Fujimoto's paper (J. Math. Kyoto Univ. 28 (1988), 91-110), opened on 24 November at pp. 91-92, 94-97 and 99. His
definition of an elliptic threefold admits the compact non-Kähler H_m of Proposition 47.4, his Theorem 2.8 and
Corollary 2.10 are quoted exactly, and the gap is in the covering on p. 96, as Paper II says. Neither needs a change to
Paper II; keep their exact locators when the bibliography is regenerated.

### 0.8 Our reading of Paper III, so far

Claude Opus 5.5 (Anthropic) at effort max is reading all of Paper III, as it read Paper II: the source of checkpoint 100
(`1d9ee185...`) with a PDF built from it, part by part, recomputing the steps on which each proof turns (with sympy and
numpy where a computation is long). By 26 November it had read pages 1 to 162 of that PDF, from the title to the middle
of the proof of Theorem 8.2 (tag 02KM). So far it has found no mathematical error, one point of typesetting (T1) and
seventeen of presentation (P1-P17):
- `CLAUDE_READING_FINDINGS_PAPER_III.tsv`: one row for each, with its place (the statement number and page of a build of `1d9ee185...`, the tag, and the
  line of that source, so that each row can be found after your re-layout), the finding, the proposed change and its
  state;
- `CLAUDE_READING_LOG_PAPER_III.md`: the log, part by part: what was recomputed, what was taken from the cited literature, and each finding in
  context;
- `CLAUDE_READING_PAPER_III_checks/`: the programs that recomputed the longer computations (Proposition 5.5 and Remark 5.7, Theorems 6.4, 6.7,
  7.12, 7.14 and 8.2), each with its output.

Settle every row in Paper III's text pass, before its next build: make the change, or another that removes the defect,
and log it in `S6_SERIES_PUBLISH_defects_III.tsv` under the finding's id (for example `CLAUDE-III-P15`); where you find
a finding wrong, log under its id why, and leave the text. T1 comes first: the paper must build on a current TeX Live
(section 3.5), and under the LaTeX kernel of 1 November 2025 it stops at its first labelled display. P4 concerns the series
table and is settled in the five-together step. Four rows reach beyond the places they name: P2 (capitalized
references), P11 (inverse maps stated for renamings and identities), P14 (program-output wording in a computation) and
P15 (one letter for one object within a proof); apply them to the whole paper.

The rest of the reading follows, and its findings will come in the same form; do not wait for them.

## 1. Why this run, and the goal

The run of `S6_SERIES_GRIND_PROMPT.md` wrote the series *The (3,4,∞) family of complex six-spheres* as five papers.
Its last checkpoint (checkpoint 10, 20 November 2026, 02:11 UTC) is the state you start from; the run ended there.
The mathematics of the papers has been checked many times, by several runs and two model families. Their text has not
been fit to publish.

On 20 November 2026 Paper V was deposited on a public repository for AI-produced mathematics and withdrawn by us for
correction within the hour. A reading of the deposited PDF, page by page (attached: `V_READING_NOTES_20261120.md`),
found that it reads as the record of how it was produced, not as mathematics: narration of our own earlier drafts
("a corrected compact construction", "The former open paragraph is retained in the research records"), labels of our
runs and prompts used as references ("P1.12", "every datum of F.2", "Lead 6", "the prompt"), program paths and check
counts inside proofs, machine headers on every statement, the same result proved three times, a definition the main
theorem depends on left as an unnumbered paragraph, and the headline construction starting on page 71. The reading
found no mathematical error. Every number it recomputed agreed; the notes list them.

The same defects are in Papers I-IV, at larger scale (section 2, the census).

**The goal: five papers that a research mathematician reads as mathematics, and that we can publish under our names
without embarrassment.** The three requirements of the series stand:
1. **The point at once.** A mathematician with little attention to spare gets the point of each paper in its first
   pages, and can go deeper exactly where they want.
2. **Not wrong.** Every result is checked to confidence, and the record shows how.
3. **One coherent work** on one topic, clearly a series.

and a fourth, which the earlier run did not meet:

4. **Nothing in the text records the production process.** The papers state mathematics as it stands. The history of
   the work, the runs, the prompts, the checks and the files are the provenance: they live in the check files and the
   records on GitHub, linked once from each paper's methodology section.

**Done** means: the five papers rewritten to the standard of section 3, every defect of the register removed and
logged, the checks of section 4 done and recorded, every PDF building cleanly and read page by page in its final form.

## 2. The state you start from

*The state the first run started from. This continuation starts from checkpoint 100 (section 0); where that checkpoint
records a later state, it holds.*

**The five papers of S6_SERIES_GRIND at its checkpoint 10** (standalone TeX, one file each, attached with every
deliverable of that checkpoint):

| Paper | Topic | Pages (cp10) | Printed statements |
|---|---|---:|---:|
| I | the (3,4,∞) family: periods, moduli, the two ends | 419 | 266 |
| II | torus-fibred threefolds with b₁ = b₂ = 0, the Campana-Demailly-Peternell argument, the sign theorem | 809 | 368 |
| III | maps from the six-spheres and the manifolds they give | 325 | 136 |
| IV | smooth monodromy in Θ₇ | 1,438 | 258 |
| V | complex fourfolds from the family | 225 | 104 |

With them: the inventory, the tags file (every statement's permanent tag), the check files, `CHECK_EVENTS.tsv`, the
notation sheet, the bibliography, the run's report and ledger, the deposit fields, and the file list of the run's
programs and outputs. The run's program sources are attached in `S6_PUBLISH_programs.zip`; the programs with their
outputs are public in the repository https://github.com/KokunoYumeto/s6-complex-structure-workbench at commit
a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7, folder `pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/`.

**What has been done since checkpoint 10** (all attached):
1. **The intake of checkpoint 10** (`INTAKE_S6_SERIES_GRIND_cp10_20261120.md`, with its check events): 22 exact
   consistency checks of Paper V's printed numbers; its section 5 lists what Papers II, III and IV still need.
2. **Rechecks of Paper V by a second model family** (20 Nov 2026):
   - Claude Opus 5.5 (Anthropic) at effort max: the chain of Theorems B, C and D and the Oka-theoretic part of
     Theorem F read and found sound as far as followed; the rational cohomology, the characteristic numbers, the
     reflection descent and K_C = L⁻⁹ recomputed independently (`REVIEW_V_aacf1302_20261120.md`,
     `RECHECK_V_aacf1302_20261120.py/.out`, `RECOMPUTE_B_aacf1302_20261120.py/.out`); Paper I's C.6.T2 rank proof
     rechecked (`RECHECK_I_C6T2_aacf1302_20261120.py/.out`).
   - Claude Fable 5.2 (Anthropic) at effort high: the structure of Theorems A and E against the body statements they
     cite, with recomputations (`REVIEW_V_A_E_ad85dcfa_20261120.md`, its check events and program). It notes that the
     decimal value of c_* rests on the interval certificates of the GPT-6 Astra runs and has not been recomputed
     outside them.
3. **Citation corrections** for Papers V and I (`citation_fixes.json`; the deposited copy of Paper V,
   `S6_series_V_deposit_20261120.tex`, carries them): duplicate entries merged (Grauert 1960, Yang 2026, Schröer-Siebert),
   the journal reference of Conway-Crowley-Powell-Sixt added with the version whose pages are cited, "attached-source
   edition" replaced by "arXiv v1" in the Yang locators, proper names restored in titles. Keep them, and do the same
   for II-IV.
4. **The page-by-page reading of Paper V as deposited** (`V_READING_NOTES_20261120.md`), the **defect register** built
   from it (`S6_DEFECT_REGISTER.csv`, 24 types) and the **census** (`S6_DEFECT_CENSUS.csv`). The census counts the
   register's strongest search patterns in each paper's PDF text. These are hits to be read in context, not
   confirmed defects:

| Paper | Pages | history (D01) | defensive (D02) | run labels (D04) | prompt items (D05) | "actual" (D08) | retain/supplied/fresh/survivor (D08) | files in text (D09) | machine headers (D10) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| I | 420 | 89 | 83 | 12 | 15 | 307 | 219 | 161 | 516 |
| II | 810 | 80 | 93 | 39 | 18 | 1,792 | 586 | 106 | 742 |
| III | 326 | 88 | 70 | 109 | 5 | 464 | 265 | 100 | 265 |
| IV | 1,439 | 393 | 248 | 1,722 | 15 | 6,709 | 2,799 | 364 | 488 |
| V | 225 | 36 | 41 | 54 | 42 | 306 | 179 | 127 | 209 |

5. **The deposit form of Paper V as submitted** (`HEXAGON_METADATA_V.json`): title, abstract, comments, provenance
   statement. It is the model for the deposit fields of all five papers (section 6), and its provenance statement is
   checked like the papers' (section 4.1).
6. **The results checked fewer than three times** (`UNDERCHECKED_RESULTS.csv`), computed from `CHECK_EVENTS.tsv` and
   the events recorded since, counting as substantive the targeted proof checks, independent re-proofs and computations
   or formal certificates:
   - 12 printed results have fewer than two substantive check events or only one checker (`below_bar = yes`): eight
     in Paper I (ari:C.4.1, ari:C.7.7, ari:C.7.8, inv:C3.6, push:src:B.4.3, push:src:C.3.5, push:src:D.4.6,
     push:src:E.3.1), two in Paper III (mapsIII:carrier-three-complex-wedge, mapsaudit:finite-degree-three), two in
     Paper IV (iv:source_transports; iv:open:K111:original_auxiliary_arrays, which is open and has no check);
   - 506 have exactly two (`below_bar = two_only`).

7. **Paper V, corrected by us** (Claude Opus 5.5 at effort max, 20 November 2026; `S6_series_V_corrected_20261120.tex`,
   192 pages, building with pdfLaTeX with no error, undefined reference or overfull box). Start Paper V from this source,
   not from checkpoint 10. Done in it:
   - the abstract, §1.1, the "known and new" table and the methodology rewritten;
   - the statement headers and the links back to §1 removed (tag only);
   - the narration of earlier drafts, the defensive clauses and the run and prompt labels removed;
   - a Definition of admissible data, and a numbered Definition of h_b;
   - Propositions 2.1, 4.5 and 4.8, the third homology proof, the repeats of 4.3 and 4.4, and the meta-statement 12.1
     deleted;
   - the shifted fivefolds moved to a Part III after the headline;
   - the bibliography sorted, with DOIs.

   Still to do in Paper V:
   - equation numbers by section in place of (E.x), (F.x) and (1.15.x);
   - the remaining overlaps: Theorems 6.1 and 6.3, Theorems 6.6 and 6.7, and Lemma 5.4 with step 5 of Theorem 5.5;
   - one parameter normalization instead of two;
   - the interval-arithmetic implementation details of §8 moved out of the proofs;
   - the textbook comparison in §11, which is to be cited rather than re-proved;
   - the residue list `S6_series_V_corrected_residue.txt` read in context.

## 3. What publication-ready means

### 3.1 The defect register

`S6_DEFECT_REGISTER.csv`, in checkpoint 100's version, has 27 defect types (the fourth continuation added D26, the seventh D27), each with what it looks like, where it occurred in Paper V, quoted
examples with pages, search words and the required fix. In every paper:
- find every instance of every type. The search words are where to start; read every page you rewrite, because the
  register's types also occur in words no search finds;
- fix each instance as the register's "required fix" says;
- log it in `S6_SERIES_PUBLISH_defects_<P>.tsv`: type, location (statement number or section and page in the old and
  the new PDF), the old text, the new text;
- record every further kind of defect you meet as a new row of the register (D28 onward), with the same columns, and
  apply it to all five papers.

### 3.2 The text

- **The mathematics as it stands.** No sentence refers to an earlier version of our own work, to a run, a prompt, a
  reading, a worker or a file history. A correction of published work stays, stated neutrally with its exact citation
  ("This corrects [CDP20, p. 692], where ..."); never call another author's argument "the reader's argument".
- **Every reference resolves** for a reader holding only the five papers and the cited literature: a statement of
  this paper by its number (Theorem 6.7), of another paper of the series by paper and number (II.7.4), published work
  by its exact locator (statement and page). No run label, prompt item or compendium number survives.
- **One statement, one proof.** A second independent proof that adds confidence goes into the check file, or into one
  remark citing it.
- **Every definition is a numbered Definition**; every result a numbered statement with a short mathematical title;
  no text between the end of a proof and the next statement except a numbered remark.
- **Computations.** A computational step says in the text what is computed, by which method, from which inputs, with
  which result, so that a reader can redo it. Its program is cited once, in one form: its file path, as plain
  text. The paper's one link is the records page, and its one commit is printed in §1.5 (section 0.3). Each paper ends with a short table of its programs.
  No file paths, JSON names, matrix rows, check counts, library versions or options in the text.
- **Statement blocks.** The block of `S6_SERIES_GRIND_PROMPT.md` section 4.2 is withdrawn: its header ("[02MQ] proved
  checks uses and used by uses: ... proves step 1 of Theorem A") and the link "Return to §1" after every proof made
  every page read as machine output. A statement now prints its number, its title and a small "tag 02MQ" after the
  number, nothing else. Keep `\hypertarget{tag-XXXX}{}` and every `\label` exactly, so that every existing link still
  resolves. The uses, used-by lists, back-links and check links go into the check files, linked once from §1.5. PDF
  bookmarks and hyperlinked statement numbers remain.
- **Status words.** Every statement in the body is proved; what is not proved is in the final part, said in words.
- **No defensive clauses.** A hypothesis that is not needed is stated once, positively, where it matters.
- **Register.** English, first person plural, the register of a careful research paper; no summaries of what is about
  to be done and no closing recapitulations.

### 3.3 The first pages

- **Title block and abstract.** The abstract states the main theorems in words a mathematician grasps at once, at most
  250 words, with no process words and no long decimals.
- **Table of contents.**
- **§1 Results and their proofs in outline:**
  - **1.1 The series and this paper.** One paragraph and one table, the same in every paper: the five papers, the main
    result of each in one line in mathematical words, which papers each uses.
  - **1.2 The main theorems,** lettered, each stated in full with hypotheses and scope, its mechanism in one sentence,
    its literature status in one line (new; or corrects [X, locator]; or known, cited).
  - **1.3 The proofs in outline:** for each main theorem 3-7 steps, each a precise claim, its reason in a line, and a
    hyperlinked statement number. No step says more than the body proves.
  - **1.4 Known and new:** one line per main theorem with its status and exact locators. No repeated paragraphs.
  - **1.5 Methodology,** about a page, in plain words: who did what (each model with its effort and dates), how the
    models worked together, how the results were checked (the kinds of check and their counts, computed from the final
    `CHECK_EVENTS.tsv`), the sentence that no human has checked the mathematics, the CC0 dedication, and one link to the
    records on GitHub. No run names, no internal event types, no file names.
  - **1.6 How the paper is organized,** describing the paper as it is, with the dependency figure.
- **Further results:** a list, one line each, with the statement number and what it says in words. No tag tables.

### 3.4 Structure and length

- **Order the body by the mathematics:** what the main theorems need, in the order they need it, the headline first.
  Sections of readable length with descriptive titles. No forward dependence of a construction on a later section.
- **Material off a paper's topic** moves to the paper whose topic it is, or to a clearly titled later part that says
  in one paragraph why it is there.
- **Known results are cited, not re-proved,** under the exceptions of `S6_SERIES_GRIND_PROMPT.md` section 4.4,
  condition 2.
- **Length follows from the content.** A paper is as long as its results and their proofs need: duplication, history,
  certificate dumps and re-proofs of known material go.
- **Paper V specifically** (the notes give the details):
  - the headline, compact complex fourfolds diffeomorphic to 3HP²#(−HP²), comes first;
  - the resolved fibre-product fourfold (Theorem A) and the shifted complex fivefolds (its current §2.7-2.25) are
    placed by the rule above; the fivefold material does not precede the headline;
  - the classification of its §11 is stated for a defined notion ("admissible datum", from the statement of Theorem
    F), never as "data of F.2";
  - one proof of the integral homology of M_c; one notation for the parameter (the real c, the complex ξ, c_* and the
    splitting), stated once in §1;
  - the definition of h_b is a numbered Definition with its proof of well-definedness.
- **Papers I-IV:** the same, using the intake's section 5 and the register.

### 3.5 The conditions that hold unchanged

Conditions 1-9 of `S6_SERIES_GRIND_PROMPT.md` section 4.4 hold unchanged: new results with complete proofs; known
results cited; statuses; scope; credit exactly; literature opened before it is cited; one notation for the series;
figures; authorship and models (every model named with its effort setting and dates; the papers name no person as an
author or contributor; CC0). Every tag stays the same and is never reused. Every cross-paper reference is regenerated
from labels and tags at the end, and the series consistency check of that prompt (section 2 item 5) is repeated on
the final state.

**The papers must compile on the deposit server:** each paper is one self-contained `.tex` file that builds with
pdfLaTeX on a current TeX Live, with no shell escape and no file other than standard packages. Check it with pdfLaTeX
as well as with the engine you use.

## 4. The checks

### 4.1 Provenance, checked three ways

Every provenance statement is checked three ways: in the papers (abstract, §1.1, §1.2's literature-status lines,
§1.4, §1.5), in the deposit fields, and in the attached deposit form of Paper V. That covers who did what, with which
model, effort and dates; the counts of checks; every "new", "corrects" or "known" claim; every credit; every link and
its commit; the sentence on human checking; the dedication.
1. **Against the records:** the attached reports, ledgers, intakes and reviews.
2. **By recomputation:** every count is recomputed by a program from `CHECK_EVENTS.tsv` in its final state, and the
   program is delivered.
3. **Against the primary source:** each cited work opened at the cited statement and page (the attached literature,
   or online); each link opened, and each file path found as section 0.3 requires.

Record each claim with the three outcomes in `S6_SERIES_PUBLISH_provenance_checks.tsv`. A claim that fails any of the
three is corrected in every place it occurs.

The facts of the work to state (condition 9 of the earlier prompt, extended):
- GPT-5.6 Sol (OpenAI) in Codex at reasoning effort ultra: the working edition, 24 August - 9 September 2026;
- GPT-6 Astra (OpenAI), ChatGPT Pro mode: the research runs of 12-16 November 2026, an independent re-derivation run
  of 16-18 November, the writing runs of 16-20 November, and this run (its first run of 20-21 November, its first
  continuation of 21-22 November, its second and third continuations of 22 November, its fourth and fifth continuations of 23-24 November, its sixth continuation of 24 November, its seventh continuation of
  24-25 November, its eighth continuation of 25 November, and this continuation);
- Claude Fable 5.2 (Anthropic) at effort high and at effort max, and Claude Opus 5.5 (Anthropic) at effort max: the
  readings, intakes, sweeps, checks and recomputations of 12-20 November 2026;
- Claude Opus 5.5 (Anthropic) at effort max: the rewriting of Paper V's abstract and §1 on 20 November 2026
  (section 0.2, item 2);
- Claude Opus 5.5 (Anthropic) at effort max: the reading of all of Paper I on 21-22 November 2026 and its three
  changes at deposit, and the correction of its links on 22 November (section 0.2, item 1);
- Claude Opus 5.5 (Anthropic) at effort max: the intake checks of checkpoints 47 to 52 on 23 November 2026
  (`CLAUDE_INTAKE_CHECK_EVENTS_20261123.tsv`), of checkpoints 53 to 62 on 24 November 2026
  (`CLAUDE_INTAKE_CHECK_EVENTS_20261124.tsv`), of checkpoints 63 to 70 on 24 November 2026
  (`CLAUDE_INTAKE_CHECK_EVENTS_cp63_70.tsv`), of checkpoints 71 to 91 on 24-25 November 2026
  (`CLAUDE_INTAKE_CHECK_EVENTS_cp71_91.tsv`) and of checkpoint 98 on 25 November 2026 (`CLAUDE_INTAKE_CHECK_EVENTS_cp92_100.tsv`,
  section 4.3);
- Claude Opus 5.5 (Anthropic) at effort max: the reading of all of Paper II on 24 November 2026, with the check of
  its finding P21 at the source the same day (section 0.7);
- Claude Opus 5.5 (Anthropic) at effort max: the reading of Paper III, from 25 November 2026, with its programs
  (section 0.8).

### 4.2 Results with few checks

- **The 12 results with `below_bar = yes`:** check each now by the method of `S6_SERIES_GRIND_PROMPT.md` section 5:
  derive each step from the statement and the results it cites, writing your derivation before you read the printed
  step, then compare; recompute every computational step with a new program by a different method; settle every
  disagreement. iv:open:K111:original_auxiliary_arrays is in Paper IV's final part: check what is proved about it.
- **The results with `below_bar = two_only`** on which a main theorem rests (its outline steps and the body statements
  those steps cite): a third, independent check of the same kind.
- **Every result whose proof you rewrite** is re-read against the proof it replaces. The rewrite changes wording,
  order and presentation; it changes a statement, hypothesis, number or step only to correct an error. Every error
  found is corrected, recorded with a check event of type "refuted, with the refined statement's id" where a statement
  was wrong, and listed in the report.
- **The global check** of every main theorem in its final form, as in that prompt's section 5 item 2.
- **Literature status** of every main theorem verified again (new; corrects; known), against the attached literature
  and an online search, each search recorded in the inventory.

### 4.3 Check events

For every statement, record its check events in CHECK_EVENTS.tsv: statement id, date, who (model, effort, run), type
(targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the
type of what actually happened, neither more nor less: a reworded proof that you re-read is "used and rechecked in this
run"; a step you re-derived before reading it is a targeted proof check. The attached events recorded since
checkpoint 10 are merged already. In the five-together step merge the readings of Paper I of 21-22 November
(`CLAUDE_READING_LOG_PAPER_I.md`), of Paper II of 24 November (`CLAUDE_READING_LOG_PAPER_II.md`) and of Paper III from 25 November (`CLAUDE_READING_LOG_PAPER_III.md`, as far as it has gone): one event per statement of type "carried as background without fault found",
its outcome quoting what the log says was recomputed there, and no higher type from that reading alone. The rows of `CLAUDE_INTAKE_CHECK_EVENTS_20261123.tsv`, `CLAUDE_INTAKE_CHECK_EVENTS_20261124.tsv`, `CLAUDE_INTAKE_CHECK_EVENTS_cp63_70.tsv` and `CLAUDE_INTAKE_CHECK_EVENTS_cp71_91.tsv`, our checks at checkpoints 47 to 91, are merged already. Merge now the attached `CLAUDE_INTAKE_CHECK_EVENTS_cp92_100.tsv`: our check of the refinement of 02LG at checkpoint 98 (the element orders and the Chinese-remainder map), and the computations of our reading of Paper III that our programs reproduce (02K5, Q018, 02OG, 02LK, 02KK, 02KL and 02KM; the programs and their outputs are in `CLAUDE_READING_PAPER_III_checks/`), each row as it stands: each covers only the steps its outcome names. An event withdrawn after it was recorded keeps its row; in the final table its outcome says that it was withdrawn, when and why, and no count includes it. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

## 5. The order of the work

1. **Restore and verify** checkpoint 100 and the base files (top of this prompt).
2. **Paper III, complete,** from where checkpoint 100 left it: T1 first (section 0.8), and the typing of section 0.1;
   then the regrouped sections finished (the 58 reopened D14 rows and the other open rows, with the visual repairs and
   hyperlink bindings that the reading of pass 08 found), each unit's restructuring and all its defect types (D26 and
   D27 included) in one pass, with the findings of our reading (section 0.8) settled in the same pass; its provenance
   and links; built, under a LaTeX kernel of November 2025 or later as well as under yours; the typesetting check; then
   every page of its rendered PDF read against the register, as a reader would, and that reading logged in
   `S6_SERIES_PUBLISH_reading_III.md` (page, what was found, how it was fixed).
3. **Then Paper IV,** completed the same way: its 66 required checks, with every use of 02S8 and 02S9 and of the other
   Paper III statements settled in the seventh and eighth continuations (section 0.1), and of the refined 02Y6 and 02XE
   of Paper II (section 0.2), rechecked against their settled form; then the same steps as for Paper III.
4. **The five together, last:** D26, D27 and every defect type added after them, applied to Papers I, II and V; the
   findings of our reading of Paper II settled (section 0.7), with P4 of our reading of Paper III (section 0.8);
   cross-references regenerated, the series table and notation sheet, tags, check files, the consistency check, the
   defects tables completed (each row's pages in the old and the new PDF and its final review status: many rows of
   `S6_SERIES_PUBLISH_defects_II.tsv` still say that a page concordance or a final page review is pending), the deposit
   fields and records tables, a last reading of every first part (abstract to §1.6) of the five. Papers I, II and V
   change in this step alone (section 0.2). A page of Paper II whose image changes is read again; its unchanged pages
   keep their reading.

Write the files from the start and extend them as you go, so that an interruption loses little.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most
of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the
smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach
stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter
search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then
push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided
step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three
hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every
checkpoint): every open row with its status, and for each main question its current gate (the strongest proved
reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller
gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two
consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it;
this check takes precedence over the sentence above about untried approaches.

**The main question** of this prompt is the five publication-ready papers. **The open rows** of the ledger are those of
section 0.4: for each unit of each paper, each defect type not yet removed from it and its restructuring if not yet
done; each result of section 4.2 not yet checked; each provenance claim not yet checked three ways; each paper's
build not yet clean; each page of the paper's current candidate PDF not yet read (a page whose image changes in a
rebuild is open again). A row that reaches its done state has changed status.

1. **Done** means:
   - the five papers are rewritten to the standard of section 3, from their first pages to their references;
   - every defect type of the register is removed from every paper, every instance logged;
   - the checks of section 4 are done and recorded, and every disagreement settled;
   - every PDF passes the typesetting check, compiles with pdfLaTeX, and has been read page by page in its final form;
   - the report lists every error found in the mathematics and how it was settled, and every change against the
     attached state with its reason.
2. **Not acceptable:**
   - any sentence that records the production process;
   - a reference that does not resolve for a reader of the five papers and the cited literature;
   - a program path, file name, check count or option inside a statement or proof;
   - a result stated or proved twice;
   - a new result without its complete proof in its paper;
   - a statement, hypothesis, number or proof step changed without the change being recorded and justified;
   - a model named without its effort;
   - a wording pass in place of the restructuring of section 3.4;
   - an outline, a sample, or some of the papers in place of all five.
3. **Finished** only when the five papers are done in the sense of point 1. Keep working until then: do not stop
   because the remaining work is large, because a paper looks presentable, or because much has already been written.
   - If the session itself ends first (the environment stops you, not your choice), the first line of
     `S6_SERIES_PUBLISH_report.md` reads INCOMPLETE, and the ledger shows the state reached for every open row.
   - The same PROMPT.md and ZIP with your newest checkpoint attached will continue the work (top of this prompt).
   - Never present such a return as complete.

## What to deliver

One ZIP, `S6_SERIES_PUBLISH_final.zip`, holding:
- `S6_SERIES_PUBLISH_I.tex` to `S6_SERIES_PUBLISH_V.tex` and their PDFs (Paper I: from its posted source
  `S6_series_I_public_v1.tex`; Paper V: from its published source `S6_series_V_public_v3.tex`; each with the
  changes made under section 0.2);
- `S6_SERIES_PUBLISH_defects_I.tsv` to `_V.tsv` (section 3.1) and the extended `S6_DEFECT_REGISTER.csv`;
- `S6_SERIES_PUBLISH_reading_I.md` to `_V.md`: the page-by-page reading of each final PDF;
- `S6_SERIES_PUBLISH_records_<P>.tsv` for each paper with a version still to be deposited (section 0.3);
- `S6_SERIES_PUBLISH_provenance_checks.tsv` and the programs that recomputed the counts;
- `S6_SERIES_PUBLISH_inventory.csv`, `S6_SERIES_PUBLISH_tags.tsv` (the same tags), and `S6_SERIES_PUBLISH_checks_I.md`
  to `_V.md`, each statement's entry holding its check events, its uses and used-by lists and its back-links;
- `S6_SERIES_PUBLISH_notation_sheet.md` and `S6_SERIES_PUBLISH_references.bib`, every entry marked verified or
  unverified;
- `CHECK_EVENTS.tsv` and `PROGRESS_LEDGER.md`;
- `S6_SERIES_PUBLISH_deposit_fields.md`: for each paper, in the form of `HEXAGON_METADATA_V_public_v3.json`: its
  title; its
  abstract; its comments (the series, the paper's main result in one sentence, the related work, the link to the
  records); its provenance statement, which opens with the sentence "Text: AI-authored; none of it was written by a
  human. The submitter takes responsibility for the veracity of the text." and then says how the paper was produced and
  how it was checked, with counts recomputed from the final `CHECK_EVENTS.tsv`; the subject, cross-lists, MSC codes and
  tags; licence CC0 1.0; the note for Paper I's version 2 and, if Paper V changed, for its version 4 (section 0.2);
- `S6_SERIES_PUBLISH_report.md`, giving every error found and how it was settled, every proof repaired, the checks
  per paper, every change against the attached state with its reason, the references opened, and the counts of the
  typesetting check before and after;
- `code/`: every program you wrote or ran, with its output.

## If the execution environment fails

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals
for as long as this session lasts, without writing recovery text into the conversation. When the environment is back,
restore your work from your newest checkpoint, redo what you had done after that checkpoint, and continue to the end.
Do not write files out as text instead: the work reaches us only through checkpoint ZIPs and the final ZIP.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log:
- no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text;
- no font may be missing; no reference or citation may be undefined.

Fix each problem in the source (scale or split a wide diagram, break a wide display, let a line break, load the font)
and compile again. Then render pages to images and look at them: every page that had an overflow, and the pages of
your page-by-page reading. Give the counts before and after in the report.

**Checkpoints.**
- **When.** Save a checkpoint ZIP once every 45 minutes of work, as a file of this conversation that can be downloaded.
  - Each has a new name, `S6_SERIES_PUBLISH_checkpoint_NN.zip`, with `NN` counting up from 01, or from one more than
    the attached checkpoint.
  - Never overwrite, rename or delete an earlier checkpoint.
  - Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, folder, chapter or
    paper.
- **What.**
  - **Self-contained apart from the base files.** A checkpoint is one ZIP holding every deliverable in its current
    version, every other file of your own work created or changed since checkpoint 100 that the next step needs
    (section 0.6), and a file list with size and SHA-256 of each file. The base files and the newest checkpoint alone
    restore your workspace.
  - **Left out:** the base files themselves, earlier checkpoints, archives, copies and diffs of derived files, copies
    and extracted text of published works, and rendered page images (keep only an image that shows a problem in our
    own papers that the report discusses).
  - It is never a JSON file, a recovery file, a summary, or an export of the newest pages only.
  - Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it.
- **Size.** Keep every checkpoint ZIP, and the final ZIP, under 500 MB. If one would be larger, save it as several ZIPs
  of under 500 MB each, `S6_SERIES_PUBLISH_checkpoint_NN_part<k>.zip`, the file list in the first part.
- **The final ZIP** holds every deliverable in its current version, and no copy of a published work (section 0.6). A file or passage dropped from the work is listed
  in the report with the reason.

Work through all five papers; do not ask whether to continue.

---

THE MATERIAL YOU ARE GIVEN

One ZIP. LaTeX sources wherever they exist; PDFs only where no source exists.

- **Checkpoint 100 of this prompt, merged and packed lean:** the folder `S6_SERIES_PUBLISH_checkpoint_100/`, with
  `CP100_INDEX.tsv` and `restore_cp100.py` (section 0.6).
- **Added for this continuation:** `CLAUDE_INTAKE_CHECK_EVENTS_cp92_100.tsv` (section 4.3); `CLAUDE_READING_FINDINGS_PAPER_III.tsv`, `CLAUDE_READING_LOG_PAPER_III.md` and the folder `CLAUDE_READING_PAPER_III_checks/`
  (section 0.8); and `BASE_FILELIST.tsv` (top of this prompt).
- **Added for the eighth continuation:** `CLAUDE_INTAKE_CHECK_EVENTS_cp71_91.tsv` (section 4.3; its rows are merged
  already), and `CLAUDE_READING_FINDINGS_PAPER_II.tsv` and `CLAUDE_READING_LOG_PAPER_II.md` (section 0.7).
- **Added for the seventh continuation:** `CLAUDE_INTAKE_CHECK_EVENTS_cp63_70.tsv` (section 4.3; its rows are merged
  already).
- **Added for the sixth and fifth continuations:** `CLAUDE_INTAKE_CHECK_EVENTS_20261124.tsv` and
  `CLAUDE_INTAKE_CHECK_EVENTS_20261123.tsv` (section 4.3; their rows are merged already).
- **Added or replaced for the fourth continuation:** `S6_series_I_public_v1.tex`, `HEXAGON_METADATA_I_public_v1.json`,
  `S6_series_V_public_v3.tex` and `HEXAGON_METADATA_V_public_v3.json` (section 0.2, items 1 and 2),
  `RECORDS_page_20261123.md` and `REPOSITORY_PROGRAM_PATHS.txt` (section 0.3).
- **Added for the second continuation:** `CLAUDE_READING_LOG_PAPER_I.md`.
- **Added for the first continuation:** `S6_series_V_public_v2.tex`, `HEXAGON_METADATA_V_public_v2.json` and
  `S6_SERIES_PUBLISH_PROMPT_as_first_sent.md`.
- **The five papers at S6_SERIES_GRIND's checkpoint 10:** `S6_SERIES_GRIND_I.tex` to `S6_SERIES_GRIND_V.tex` (standalone), and
  `S6_series_V_deposit_20261120.tex`, the deposited copy of Paper V with the citation corrections and pinned links.
- **Paper V as corrected on 20 November 2026:** `S6_series_V_corrected_20261120.tex` (section 2, item 7), with
  `S6_series_V_corrected_residue.txt`, the remaining pattern hits in its rendered text.
- **The rest of checkpoint 10:** `S6_SERIES_GRIND_inventory.csv`, `S6_SERIES_GRIND_tags.tsv`,
  `S6_SERIES_GRIND_checks_I.md` to `_V.md`, `CHECK_EVENTS.tsv`, `S6_SERIES_GRIND_notation_sheet.md`,
  `S6_SERIES_GRIND_references.bib`, `S6_SERIES_GRIND_report.md`, `PROGRESS_LEDGER.md`,
  `S6_SERIES_GRIND_deposit_fields.md`, `S6_SERIES_GRIND_filelist.tsv` (every program and output of the run, with
  size and hash), and `S6_SERIES_GRIND_PROMPT.md`, the prompt of that run.
- **`S6_PUBLISH_programs.zip`:** the source files (Python and notes) of the run's `code/` and `audit_*` folders, with
  their paths. Their outputs are in the public repository at the pinned commit (section 2).
- **The reading and the register:** `V_READING_NOTES_20261120.md`, `S6_DEFECT_REGISTER.csv`,
  `S6_DEFECT_CENSUS.csv`, `census.py`.
- **The checks since checkpoint 10:** `INTAKE_S6_SERIES_GRIND_cp10_20261120.md` with
  `INTAKE_S6_SERIES_GRIND_cp10_20261120_CHECK_EVENTS.tsv`; `REVIEW_V_aacf1302_20261120.md`,
  `RECHECK_V_aacf1302_20261120.py/.out`, `RECOMPUTE_B_aacf1302_20261120.py/.out`,
  `RECHECK_I_C6T2_aacf1302_20261120.py/.out`; `REVIEW_V_A_E_ad85dcfa_20261120.md` with its check events and
  `CHECK_A_E_ad85dcfa_20261120.py/.out`; `UNDERCHECKED_RESULTS.csv` and `build_underchecked.py`.
- **Citations:** `citation_fixes.json`.
- **The deposit form of Paper V:** `HEXAGON_METADATA_V.json`.
- **The design of the series:** `S6_SERIES_DESIGN_20261119.md` and `S6_PUBLICATION_READINESS_20261119.md`.
- **`S6_GRIND_6_literature.zip`:** the LaTeX sources of the literature ([E26], [DGKX] versions 1 and 2, [CDP98],
  [CDP20], Lehn-Rollenske-Schinko, Viaclovsky, Liu-Rollenske and the others), Duke-Imamoglu as a PDF, and [AC26] as
  published (PDF) with our transcription.
- **`S6_PUBLISH_literature_arxiv/`:** the LaTeX sources (arXiv e-prints, text files only; a PDF where arXiv has no
  source) of the other 56 arXiv works the series bibliography cites, one folder per identifier, with `FETCH_LOG.tsv`.
- **`S6_GRIND_4_s6_09_compendium.zip`:** the three S6_09 papers (TeX and .aux) with their inventory. A reference
  "[S6_09, label]" or a compendium number such as B.5.16 in the papers points here: find what it proves, then cite
  that statement in the series by its number, or prove the fact where it is used.
- **`S6_GRIND_5_research_runs_tex.zip`:** the TeX, results tables and reports of the research runs (S6_01_INVARIANTS,
  S6_02_FAMILY and S6_02_PUSH, S6_03_CDP, S6_04_MAPS_MANIFOLDS, S6_05_ARITHMETIC). The labels inv:, push:, ari:, cdp:
  and maps: printed in the papers come from these; the inventory maps each to its statement in the series.
- **`S6_GRIND_3_night_run_cp36.zip`:** the results register, report and literature log of the independent
  re-derivation run (labels P1.x, P1A.x, P3K.x, P3F.x).

Every other source you need you may open online; record its exact locator and mark it in the bibliography.
