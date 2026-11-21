**The attached files.** Besides this file there is one ZIP, `S6_SERIES_PUBLISH_continue_cp10.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `S6_GRIND_6_literature.zip` is the folder `S6_GRIND_6_literature/`, and the first run's `S6_SERIES_PUBLISH_checkpoint_10.zip` is the folder `S6_SERIES_PUBLISH_checkpoint_10/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# S6_SERIES_PUBLISH: the five S6 papers made publication-ready

Writing and checking prompt, 20 November 2026, for GPT-6 Astra (OpenAI), ChatGPT Pro mode, sent again on 21
November 2026 as the continuation of its first run (section 0). File prefix of every deliverable:
`S6_SERIES_PUBLISH`. Written by Claude Opus 5.5 (Anthropic) at effort max, which added section 0 and the passages
that refer to it on 21 November. It continues the prompt `S6_SERIES_GRIND_PROMPT.md` (attached), whose run
produced the five papers the first run started from.

## This prompt may be sent more than once, from any account

Everything you need is in the attached ZIP. Do not search any Library, Space, project or earlier conversation, and do
not rely on any file that is not attached.

This is a continuation of the first run of this prompt (section 0). The **base files** are every file and folder in
the ZIP except the folder `S6_SERIES_PUBLISH_checkpoint_10/`: byte for byte the files of the first run's base ZIP
`S6_SERIES_PUBLISH.zip` (SHA-256 `1cfbca4f84d07edfc765c639c42eb7aa4833cf4542776da1dcde267a03a24510`), and three files
added for this continuation (section 0.4). `BASE_FILELIST.tsv` gives the size, SHA-256 and origin of each.
- **Restore your workspace** from the newest checkpoint and from the base files. The newest checkpoint is the first
  run's checkpoint 10 (the folder `S6_SERIES_PUBLISH_checkpoint_10/`), unless a ZIP named
  `S6_SERIES_PUBLISH_checkpoint_NN.zip` with NN above 10 (or several parts of one) is attached as well; then it is
  that one. Verify every file against the checkpoint's file list (size and SHA-256), and the base files against
  `BASE_FILELIST.tsv`.
- Read the checkpoint's `PROGRESS_LEDGER.md` and `S6_SERIES_PUBLISH_report.md`, then continue the work from the
  state they record.
- Number your next checkpoint NN+1 (after the first run's checkpoint 10: `S6_SERIES_PUBLISH_checkpoint_11.zip`).
- Record the continuation, with its start time, in the ledger and the report.

## 0. This continuation: the first run, and what has happened since

**Two checkpoints named 10.** In sections 1 to 5, "checkpoint 10" is the checkpoint 10 of S6_SERIES_GRIND
(20 November 2026, 02:11 UTC), the state the first run of this prompt started from. "The first run's checkpoint 10" and
the folder `S6_SERIES_PUBLISH_checkpoint_10/` are this prompt's own, from which you continue.

### 0.1 The first run of this prompt

GPT-6 Astra (OpenAI), ChatGPT Pro mode, ran this prompt from 20 November 2026, 22:42 UTC, saving a checkpoint every 45
minutes. Its checkpoint 10 was saved at 06:12 UTC on 21 November. Nothing after it reached us: no later checkpoint and
no final ZIP. Checkpoints 07 to 09 did not reach us either, which loses nothing, since checkpoint 10 holds the whole
state: all 2,049 files of its file list match in size and SHA-256. It is attached as the folder
`S6_SERIES_PUBLISH_checkpoint_10/`, and it is public in the repository at commit
`1fb9194767aef92abcc06071e3820c2f226b9512`, folder `pro_returns/S6_SERIES_PUBLISH_checkpoint_10_20261121T0612Z/`.
Any work the first run did after its checkpoint 10 is lost: redo it from the records of that checkpoint.

What its records show (its report and `PROGRESS_LEDGER.md` give the detail):
- **Paper V** is complete since the first run's checkpoint 04: 177 pages, source SHA-256 `f89b9ece...`, PDF
  `ac8468a9...`, gate record `records/S6_SERIES_PUBLISH_V_complete_gate.json`.
- **Paper I** is at candidate 13: 346 pages (source `26a6f5f8...`, PDF `519355e3...`), every rendered page read. Eleven
  exact edits found in that reading are archived but not applied (six D02, four D23, one D18). Still to do: those
  edits, the integrated rebuild, the reading of every changed page, and the bindings of source, PDF and ledger for the
  metadata, the defect loci, the main theorems A-G and the 42 provenance claims. Its 25 defect rows and its final-page
  row are open. Our own check of candidate 13 on 21 November (a clean pdfLaTeX build, the register's search words in
  the rendered text, the first pages read, all 80 repository links opened) found three further D23 instances:
  "Poincare" without its accent at lines 17178, 26588 and 26656 of the checkpoint's `S6_SERIES_PUBLISH_I.tex`. Our
  recount of `CHECK_EVENTS.tsv` for Paper I's 333 printed environments gave exactly the counts its §1.5 prints (767,
  10, 143, 731, 194 and 1); recompute them if the ledger changes.
- **Papers II, III and IV** are not begun: 197, 128 and 66 required-check candidates at review 05.
- **The last progress review**, review 05 at 05:42 UTC, found no row changed since review 04 (04:43 UTC), and so
  counted one review without movement. In that hour the run had read the rest of candidate 11 and built candidate 12,
  and by checkpoint 10 it had read all of candidate 13. But once all of Paper I's required checks were closed (review
  04), its reading and editing could change no row, because a paper's defect rows and its final-page row closed only
  at its final gate. A second such review at 06:42 would have stopped the run in the middle of Paper I. Section 0.3
  refines the rows so that this cannot recur.

### 0.2 What has happened since this prompt was first written (20 November 2026, 23:39 UTC)

1. **Paper V is published** on Hexagon (hexagonmath.org), the public repository of section 1, as hexagon:2611.00742:
   - **version 1** (20 November, 23:59 UTC): `S6_series_V_corrected_20261120.tex`, the source of section 2, item 7
     (192 pages);
   - **version 2** (21 November, 03:20 UTC), the current version: the first run's final Paper V of its checkpoint 04,
     with two changes of ours in §1.5, quoted in item 2. Attached: `S6_series_V_public_v2.tex`, the source as
     published, and `HEXAGON_METADATA_V_public_v2.json`, its deposit fields, which replace `HEXAGON_METADATA_V.json`
     as the deposit form of Paper V wherever this prompt names that form. Its comments field opens with the note on
     what changed from version 1: such a note goes in the deposit fields, never in a paper.
2. **The two changes in version 2**, both in §1.5:
   - after the sentence that ends "16--20 November 2026.": "Claude Opus 5.5 (Anthropic), at effort max, revised the
     presentation on 20 November 2026, rewriting the abstract and Section~1; parts of both are in its wording." This
     is the rewriting of section 2, item 7;
   - the sentence "The additional records and programs of this publication revision accompany its source
     distribution." replaced by a link to the first run's records at a pinned commit (its checkpoint 04, commit
     `af034f2`).
3. **Hexagon takes the TeX source alone.** No record or program accompanies a deposited paper, so a sentence saying
   that records or programs accompany a paper's source is false, in a paper and in its deposit fields. Paper I's §1.5
   and its deposit fields have it at the first run's checkpoint 10: remove it there, and write it nowhere. Each paper
   links the records of this revision once, from §1.5, through one macro set in its preamble beside the commit macro
   (for example `\SsixPublishRecords`). Set it to the folder of the first run's checkpoint 10,
   https://github.com/KokunoYumeto/s6-complex-structure-workbench/tree/1fb9194767aef92abcc06071e3820c2f226b9512/pro_returns/S6_SERIES_PUBLISH_checkpoint_10_20261121T0612Z/; at deposit we set it to the folder that holds the
   paper's final records. The deposit fields give the same address, written out.
4. **Paper V from now on.** Its text of record is `S6_series_V_public_v2.tex`. Papers I-IV cite it by the numbering
   and tags of that version. In the five-together step (section 5, step 4), change V only where the series requires
   it (references to I-IV, the series table of §1.1, the notation), starting from that file; log every change in
   `S6_SERIES_PUBLISH_defects_V.tsv`; and write the note for its version 3 in the deposit fields: plain text, at most
   2,000 characters, saying what changed and why. A mathematical error found in V is corrected and recorded like any
   other (section 4.2). If V needs no change, it stays as published, and the report says so.
5. **Who did what** (section 4.1): Claude Opus 5.5 (Anthropic) at effort max rewrote Paper V's abstract and §1 on 20
   November 2026 (published in version 1; parts remain in version 2).

### 0.3 The ledger rows from now on

The rule of the progress check is unchanged. Its open rows (the paragraph after it) are finer from now on: a defect
type is done for a paper as soon as no instance of it is left in the paper's current source and every instance is
logged, and the reading of a paper is one row per page of its current candidate PDF. So the edits and the reading that
make a paper publishable count as they are done. Under these rows the first run moved in every interval up to its
checkpoint 10, so this continuation starts with no review without movement. The work has passed three hours, so its
reviews fall every hour from its start.

### 0.4 Your checkpoints, and the files added

Your checkpoints hold, like the first run's, every file of the work in its current version, every file restored from
the first run's checkpoint 10 included (the first run's work is your own work), so that the base files and your newest
checkpoint alone restore the workspace. Only the base files are left out.

Three files were added to the base for this continuation: `S6_series_V_public_v2.tex` and
`HEXAGON_METADATA_V_public_v2.json` (section 0.2), and `S6_SERIES_PUBLISH_PROMPT_as_first_sent.md`, this prompt as
first sent (section 0 and the passages that refer to it are what changed). Sections 1 to 5 describe the state the first
run started from; where the first run's checkpoint 10 records a later state (Paper V's remaining items in section 2,
item 7, for example), that checkpoint holds.

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

*The state the first run started from. This continuation starts from the first run's checkpoint 10 (section 0).*

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
83d76022bc, folder `pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/`.

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

`S6_DEFECT_REGISTER.csv` has 24 defect types, each with what it looks like, where it occurred in Paper V, quoted
examples with pages, search words and the required fix. In every paper:
- find every instance of every type. The search words are where to start; read every page you rewrite, because the
  register's types also occur in words no search finds;
- fix each instance as the register's "required fix" says;
- log it in `S6_SERIES_PUBLISH_defects_<P>.tsv`: type, location (statement number or section and page in the old and
  the new PDF), the old text, the new text;
- record every further kind of defect you meet as a new row of the register (D25 onward), with the same columns, and
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
  which result, so that a reader can redo it. Its program is cited once, in one form: the repository, the pinned
  commit, the file. Define the commit once per paper in a macro, so that it is set in one place at publication; cite
  your own new programs through the same macro as `code/<file>`. Each paper ends with a short table of its programs.
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
   or online); each link opened at its pinned commit.

Record each claim with the three outcomes in `S6_SERIES_PUBLISH_provenance_checks.tsv`. A claim that fails any of the
three is corrected in every place it occurs.

The facts of the work to state (condition 9 of the earlier prompt, extended):
- GPT-5.6 Sol (OpenAI) in Codex at reasoning effort ultra: the working edition, 24 August - 9 September 2026;
- GPT-6 Astra (OpenAI), ChatGPT Pro mode: the research runs of 12-16 November 2026, an independent re-derivation run
  of 16-18 November, the writing runs of 16-20 November, and this run (its first run from 20 November, and this
  continuation);
- Claude Fable 5.2 (Anthropic) at effort high and at effort max, and Claude Opus 5.5 (Anthropic) at effort max: the
  readings, intakes, sweeps, checks and recomputations of 12-20 November 2026;
- Claude Opus 5.5 (Anthropic) at effort max: the rewriting of Paper V's abstract and §1 on 20 November 2026
  (section 0.2, item 5).

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
run"; a step you re-derived before reading it is a targeted proof check. Merge the attached events recorded since
checkpoint 10. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

## 5. The order of the work

1. **Restore and verify** the base files and the newest checkpoint (top of this prompt).
2. **Paper I, complete,** from the state of the first run's checkpoint 10 (section 0.1): rewritten to section 3; the
   checks of section 4 for its results and its provenance; built; the typesetting check; then every page of its
   rendered PDF read against the register, as a reader would, and that reading logged in
   `S6_SERIES_PUBLISH_reading_I.md` (page, what was found, how it was fixed). Paper I comes first because it is to be
   deposited as soon as it is ready.
3. **Then Papers II, III and IV, in that order,** each completed in the same way before the next.
4. **The five together:** cross-references regenerated, the series table and notation sheet, tags, check files, the
   consistency check, the deposit fields, a last reading of every first part (abstract to §1.6) of the five. Paper
   V, complete since the first run's checkpoint 04 and published, changes here only as section 0.2, item 4 says.

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

**The main question** of this prompt is the five publication-ready papers. **The open rows** of the ledger are: for
each paper, each defect type of the register not yet removed from it (done when no instance of it is left in the
paper's current source and every instance is logged); each page of the paper's current candidate PDF not yet read
(a page whose image changes in a rebuild is open again); each result of section 4.2 not yet checked; each provenance
claim not yet checked three ways. A row that reaches its done state has changed status (section 0.3).

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
   - The same PROMPT.md with your newest checkpoint attached will continue the work (top of this prompt).
   - Never present such a return as complete.

## What to deliver

One ZIP, `S6_SERIES_PUBLISH_final.zip`, holding:
- `S6_SERIES_PUBLISH_I.tex` to `S6_SERIES_PUBLISH_V.tex` and their PDFs (Paper V: its published source
  `S6_series_V_public_v2.tex`, with any change made under section 0.2, item 4);
- `S6_SERIES_PUBLISH_defects_I.tsv` to `_V.tsv` (section 3.1) and the extended `S6_DEFECT_REGISTER.csv`;
- `S6_SERIES_PUBLISH_reading_I.md` to `_V.md`: the page-by-page reading of each final PDF;
- `S6_SERIES_PUBLISH_provenance_checks.tsv` and the programs that recomputed the counts;
- `S6_SERIES_PUBLISH_inventory.csv`, `S6_SERIES_PUBLISH_tags.tsv` (the same tags), and `S6_SERIES_PUBLISH_checks_I.md`
  to `_V.md`, each statement's entry holding its check events, its uses and used-by lists and its back-links;
- `S6_SERIES_PUBLISH_notation_sheet.md` and `S6_SERIES_PUBLISH_references.bib`, every entry marked verified or
  unverified;
- `CHECK_EVENTS.tsv` and `PROGRESS_LEDGER.md`;
- `S6_SERIES_PUBLISH_deposit_fields.md`: for each paper, in the form of `HEXAGON_METADATA_V_public_v2.json`: its
  title; its
  abstract; its comments (the series, the paper's main result in one sentence, the related work, the link to the
  records); its provenance statement, which opens with the sentence "Text: AI-authored; none of it was written by a
  human. The submitter takes responsibility for the veracity of the text." and then says how the paper was produced and
  how it was checked, with counts recomputed from the final `CHECK_EVENTS.tsv`; the subject, cross-lists, MSC codes and
  tags; licence CC0 1.0; for Paper V, if it changed, the note for its version 3 (section 0.2, item 4);
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
    version, every other file of your own work that the next step needs (those restored from the first run's
    checkpoint 10 included, section 0.4), and a file list with size and SHA-256 of each file. The base files and
    the newest checkpoint alone restore your workspace.
  - **Left out:** the base files themselves, earlier checkpoints, archives of earlier versions, and rendered page
    images (keep only an image that shows a problem the report discusses).
  - It is never a JSON file, a recovery file, a summary, or an export of the newest pages only.
  - Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it.
- **Size.** Keep every checkpoint ZIP, and the final ZIP, under 500 MB. If one would be larger, save it as several ZIPs
  of under 500 MB each, `S6_SERIES_PUBLISH_checkpoint_NN_part<k>.zip`, the file list in the first part.
- **The final ZIP** holds every deliverable in its current version. A file or passage dropped from the work is listed
  in the report with the reason.

Work through all five papers; do not ask whether to continue.

---

THE MATERIAL YOU ARE GIVEN

One ZIP. LaTeX sources wherever they exist; PDFs only where no source exists.

- **The first run's checkpoint 10:** the folder `S6_SERIES_PUBLISH_checkpoint_10/`, with its file list (section
  0.1).
- **Added for this continuation:** `S6_series_V_public_v2.tex`, `HEXAGON_METADATA_V_public_v2.json` and
  `S6_SERIES_PUBLISH_PROMPT_as_first_sent.md` (section 0.4), and `BASE_FILELIST.tsv` (top of this prompt).
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
