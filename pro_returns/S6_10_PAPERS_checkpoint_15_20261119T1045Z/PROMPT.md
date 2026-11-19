**The attached files.** Besides this file there is one ZIP, `S6_10_PAPERS_FINISH_account2.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `S6_08_PAPERS_1_returns_tex.zip` is the folder `S6_08_PAPERS_1_returns_tex/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# S6_10_PAPERS: the S6 papers rewritten for their readers: our new results, each proved in full and laid out as a ladder, known results cited, and the S6_09 text published beside them as the proof compendium

Writing and checking prompt, 17 November 2026. For GPT-6 Astra (OpenAI), effort Pro, ChatGPT Pro mode. File prefix for your deliverables: `S6_10_PAPERS`. Written by Claude Opus 5.5 (Anthropic) at effort max, the main session, from the plan of 17 November 2026, which is attached.

## This run continues an earlier one

An earlier run of this prompt (GPT-6 Astra, ChatGPT Pro mode, 17-18 November 2026, on this account) stopped after its
checkpoint 06, saved on 18 November 2026 at 07:32 UTC, while it was closing its final delivery gates.

**Restore its workspace first.** Its state is attached as `S6_10_PAPERS_checkpoint_06_restore.tar.xz`: the 3,847
files that checkpoint 06 holds, with its file list `S6_10_PAPERS/CHECKPOINT_FILES.tsv` (path, size, SHA-256, whether
the file is in checkpoint 06, and which checkpoint holds it), and in `_from_earlier_checkpoints/` the files of
checkpoint 01. The list names 1,187 more files, about 80 MB, that checkpoints 02 to 05 hold. Those checkpoints are in
this account's Library as `S6_10_PAPERS_checkpoint_02.zip` to `S6_10_PAPERS_checkpoint_05.zip`: search the Library for
them by name. Unpack the archive, take each file the list assigns to checkpoints 01 to 05 from that checkpoint, and
verify every file's size and SHA-256 against the list before you work.

**The state at checkpoint 06,** from the earlier run's `PROGRESS_LEDGER.md` (its review of 07:32 UTC):
- the six papers I to VI are written, with standalone builds and draft PDFs;
- the inventory has 1,480 rows; all 288 registered rows of the night run S6_06_BLIND have explicit dispositions (249
  source-Proved, 35 source-Refuted, three Known, one Open);
- seven source rows are open, each with its strongest proved reduction: in Paper I, inv:C3.8 (with the two remarks
  WORKING_INV:rem:bcpr-literal-gauge and rem:bcpr-global-gauge-boundary) and ari:C.7.4; in Paper II, inv:E2.3; in
  Paper III, maps:src:D.2.4; in Paper IV, night:P3K.75;
- the run described itself as "INCOMPLETE solely at the stated final delivery/administrative gates": reconciling the
  inventory wording, the final cross-reference, hash and log audit of all six papers, the final visual receipts (its
  final visual inspection had found two TikZ faults in Paper I), and the completion report and archive.

**What an intake of checkpoint 06 found** (Claude Opus 5.5 at effort max, 18 November 2026; its proof checks of Paper
I's torsion table, Paper II's conormal criterion and nodal counterexample, and Paper VI's parity theorem all held).
These are part of the task:
1. `CHECK_EVENTS.tsv` holds 994 events on 850 statements; the inventory's check records hold 1,488 current events on
   all 1,116 printed rows. 246 printed rows have no line in it (Paper II 104, Paper IV 120, Paper VI 22); their events
   are in `records/*.tsv` and `analysis/*/current_check_events.tsv`. Merge every event into it.
2. The events use the run's own codes ("D", "C", "E", "editorial_reconciliation", "A-identity", "F-partial",
   "scope-record") and three spellings of the checker, one without its effort. Give each event one of the six types of
   this prompt and one checker name with its effort.
3. Printed historical records name "Claude Fable 5.2 (Anthropic), effort high, 16 November 2026" as a check without
   saying what it was. On many rows it is the register intake (`reviews/S6_FINAL_INTAKE_20261116/INTAKE_FINAL.md`), which
   is not a check of the whole proof; on others it is a source-to-print comparison. Print each historical event with its
   type.
4. The credit and literature comparison of condition 12 is pending on 286 rows: 283 night rows and 3 S6_09 supplement
   rows. 31 of them are main rows, among them night:P3K.69, night:P4.58 and night:P1A.1-6.
5. Status vocabulary: rows read "current scoped check recorded; see exact proof scope ..." where condition 5 allows
   four statuses only.
6. cdp:st:E18 is printed as a proved counterexample while its only current event is "F-partial" (the source match was
   pending).
7. ari:C.7.4: condition 5 names it as proved under hypotheses H. The paper prints it as open and moves the conditional
   argument to the compendium without a reason or a recorded fault. Unless that argument fails, print the conditional
   statement with H stated and the remark that H is open.
8. The run's corrections of our plan stand: the plan's fan formula KL(S−1)(S−3)/8 is false (Paper IV §1.8), the flop
   rule is 7A, not −5A (§1.9), and OS45 has physical reference class 3. Our plan file carries an erratum; do not take the
   old formula from it.
9. The night run S6_06_BLIND has gone on: its checkpoints after 30 (36 of 18 November 15:47 UTC is the newest we hold)
   are in this account's Library. Take them in under condition 9.
10. **Three checks of every paper, papers V and VI first, then I, II, III and IV.** They are part of finishing: a paper
    is done only when its three checks are done and its statuses and check records show them.
    - **Every new proof step re-derived.** For every new result, re-derive each step of its proof from its statement
      and the results it cites, writing your derivation before you read the printed step; then compare. A step that
      re-derives is checked: record "independent re-proof" when you re-derived the whole proof, "targeted proof check"
      for a step. A step that does not re-derive is a gap: repair it under the push rule; a result whose gap remains
      goes to the part of condition 8.
    - **Every computation rerun with new code.** For every computational step (certificates, interval and Arb
      arithmetic, grids, tables, enumerations, symbolic identities), write a new program that does not reuse the one
      that produced the result, with a different method or library wherever one exists; run it and compare the outputs
      exactly. Put the program and its output in `code/` and record "computation or formal certificate".
    - **New, and quoted correctly.** For every main result, do the credit check of condition 12 again with your
      searches written down. Quote every step taken from the literature exactly from the source, opened: the
      Campana-Demailly-Peternell step first ([CDP20] p. 692, the step as printed, then our reading, in neutral
      wording).

    Each check is a check event in `CHECK_EVENTS.tsv` with its type and outcome; what a check changes is corrected in
    the paper and listed in the report.

**The sweep of 18 November** (Claude Opus 5.5 at effort max) went over all 1,124 rows of our S6 register: the runs' one-line statements, the night run's report tables at its checkpoint 35, and the printed statements where a summary was in doubt. Its files are in `S6_10_PAPERS_4_sweep1.zip`: `SUMMARY.md`, `CORRECTIONS.md` (16 items), `MERGES.tsv` (177 links: same, weaker, refines, stronger, refuted by, settled by, corrects), `FLAG_VERDICTS.tsv` (95 flags), `PLACEMENT.tsv`, `CHECK_EVENTS.tsv` and `CHECK_COUNTS.tsv`. They are part of the task:
- Carry each of the 16 corrections into the papers where it bears, as a statement's scope, hypothesis or convention, or as a split of a corrected row into its own item. Where your check shows a correction is wrong, say so in the paper with the proof. Among them: S6_04 D.2.11 as printed assumes gcd(n,3k)=1, and the night run's P3F.33-34 extend it with a Z/3 that can appear; Θ₇ = 0 holds for the [AC26] reference fan only; the pairs (k,l) of S6_04 B.6.17 and B.6.20 and of P3K.9 and P3K.11 are given for the meridian-one line, and the physical pair is the negative; S6_05 C.5.1 is about CM and torsion together; S6_03 C.2.INT.3 needs H²(Y;Q)=0; S6_04 D.2.24, D.2.27 and D.2.28 hold in the natural sector only; the 33 refuted rows of S6_06_BLIND that carry corrected statements become new items citing K68 and K69.
- Use the merge links and the flag verdicts in the inventory's dependencies and in the credit of each result.
- Q03_DEPOSIT is not S6 and stays out of the papers.
- Record each correction you carry, or refute, as a check event.

**Your task is the whole task of this prompt, from that state.** The earlier run's work is the draft you build on.
Check each part of it as you use it, correct what you find wrong, and record each correction as a correction of the
earlier run, with its check event. Your checkpoints continue the earlier run's numbering, from 07.

## Why this run

The run S6_09_PAPERS (GPT-6 Astra, ChatGPT Pro mode, 16-17 November 2026) wrote three papers on the complex structures on S^6 of the (3,4,∞) family: 1,184 statements on 2,193 pages. Its record is very good:
- every row of the six research runs is there;
- every proof was re-derived;
- the open items are stated exactly;
- credit and dates are careful;
- the typesetting is clean.

For a reader, though, the papers do not work. About a tenth of the pages are new mathematics. The rest re-proves known results and classical background (Paper III, pp. 495-891, re-proves Morse theory, handle and Whitney moves and the Adams spectral sequence), keeps routes that failed, and runs in the order the work was produced. The cause was our prompt: it asked for every result with its proof and allowed no selection.

This run rewrites the papers for their readers. Nothing proved is lost: the S6_09 text is published beside the new papers, unchanged, as the proof compendium, and the new papers cite it by its labels wherever a reader may want more.

## The readers

The papers are for mathematicians with little attention to spare, which is now the normal reader, given how much mathematics AI produces. Such a reader, wherever they stop, must hold the results at the depth they have reached, each with its reason at that depth. A list of claims without reasons repels a mathematician, and a list of results is only a table of contents. Hence the ladder of condition 3.

## The series

Six papers, in one notation (the S6_09 notation sheet), citing each other by theorem number:

| Paper | Subject | Estimate |
|---|---|---|
| I | the (3,4,∞) family: periods, moduli, the two ends of the disc | about 285 pp. |
| II | torus-fibred compact complex threefolds with b₁ = b₂ = 0 and the argument of Campana, Demailly and Peternell: where it fails, the exact criterion that replaces it, c₃ ∈ {0, 2}; the sign theorem for irreducible and normal-crossings fibres | about 345 pp. |
| III | maps from the complex six-spheres of the family, and the manifolds the construction gives | about 310 pp. |
| IV | smooth monodromy in Θ₇: the class of each family on every cusp fan, the flop rule, a generator, the families realizing every class | about 380 pp. |
| V | the fourfold: a complex structure on 3HP² # (−HP²) and the family in c | about 110 pp. |
| VI | the sign theorem for every degeneration of a torus fibration with b₁ = b₂ = 0 | about 360 pp. |

The estimates come from the plan, `plan/KEEP_SKETCH_20261117.md`. They are not targets: what a paper needs decides its length.

The plan lists, paper by paper:
- the main results (by the ids of `checks/gazette_candidates.tsv` and the night run's ids), each with a draft rung-0 sentence;
- the supporting results they use;
- the known results to cite;
- the classical material that moves out;
- the place of every row of the night run (its section 6);
- the decisions taken (its section 7).

Use it as the plan. Where your reading shows it wrong, follow the mathematics and record the change and its reason in the report. You may refine the titles so that they say what the papers prove.

## The binding conditions

Each of these binds every page of every paper.

1. **The papers carry our new results, each with its complete proof.** A new result is one of:
   - a row of the S6_09 inventory credited to our runs or our working edition and not found in the literature (its `found_in_*` and `credited_to` columns);
   - a result of the night run S6_06_BLIND.

   Each new result is stated and proved in full in its paper, and the lemmas its proof uses are proved there too unless they are known. A refuted statement goes in as a counterexample or a correction, with its proof. The paper is the reference for its results: no proof is replaced by a pointer to a repository or a working file.
2. **Known results are cited with exact locators, not proved again.** This covers:
   - the results of others: [AC26], [E26], [DGKX] versions 1 and 2, [CDP98], [CDP20], Lehn-Rollenske-Schinko, Viaclovsky, Liu-Rollenske, Huckleberry-Kebekus-Peternell and the rest;
   - classical results: Morse theory, handle and Whitney moves, the Adams spectral sequence, Kodaira's classification and the like, and the course CG-S6.

   Cite each by statement number and page, opened in the attached literature before you cite it. Our re-derivations of these stay in the compendium, and a paper may point to them as [S6_09, label]. There are three exceptions:
   - a credited appendix of Paper I with our proof that X_c ≅ X_c' if and only if c' − c ∈ 2Z, for the standard data. Our own proof of it was in our public working edition by 8 September 2026. It is Theorem 1.4 of [DGKX] version 1 (23 September 2026), and version 2 does not contain it. State both facts plainly;
   - a credited appendix of Paper I with the tangent cohomology (1,1,1,0), the Kuranishi germ and Aut(X_c) = C^*. These are theorems of [DGKX] version 1, re-derived by our first run after it had read that paper: say "re-derived";
   - a short proof where we use a known result in a form its sources do not state.

   Compare no other dates, and use no word such as "first" or "priority".
3. **The ladder.** Each paper opens with its main results at rungs 0 and 1:
   - **rung 0** is the result and the one mechanism that makes it true, in a sentence or two. An example of the register: "no filling at w = 0, because the corner's γ-winding is nonzero while a filling would force it to vanish";
   - **rung 1** is its proof in three to seven steps, each a precise claim with its reason in a line.

   A reader who stops after the opening holds every main result with a coarse but complete proof. The body holds rung 2 (each rung-1 step's own proof as steps, with every external result named) and the full detail below it. The body is ordered by the mathematics: the family, its periods, its moduli, its ends, its cohomology, its deformations, and so on, not the runs.

   Each step at one rung is exactly the claim that its expansion one rung down proves, and no rung says more than the rungs below it prove. Paper I's opening begins with a rung 0 for the whole series: the family, and the main result of each of the six papers with its mechanism. A main result is one the plan names, or a new main result of the night run.
4. **Every statement block has the same parts, in this order:**
   - its label: keep the S6_09 label where the statement existed, and give new statements labels in the same style;
   - its status (condition 5);
   - its check record (condition 7);
   - a "uses" line listing the labels its proof uses;
   - the statement;
   - the proof, as numbered steps.

   We build the stable tags, the dependency graph and the machine-readable record from these labels and "uses" lines by script after the return. You do not make tags.
5. **Statuses:**
   - proved;
   - proved under hypotheses H: state H, and say whether H holds in the cases the papers use. ARI C.7.4 (transcendence at the conductor-361 CM point under a period conjecture) is of this kind, with H open;
   - open, with everything proved about it;
   - false as stated, with the counterexample and the corrected statement.

   "Conditional" alone is not a status.
6. **Scope.** Every statement names its hypotheses and its choices. The class-0 statements of S6_09 hold for the reference cusp fan and say so; Paper IV gives the class for every fan.
7. **Check records name every checker.** The attached ledger `checks/S6_CHECK_LEDGER.tsv` lists, for each S6_09 row, every earlier check we hold:
   - our intakes, reviews and readings, by Claude Fable 5.2 (Anthropic) at effort high or at effort max and Claude Opus 5.5 (Anthropic) at effort max;
   - the inventory's recorded checks;
   - the night run's re-derivations. Record them as re-derivations by S6_06_BLIND, not as blind ones: its account's Space held the earlier S6 work and is searchable, so it may have seen it.

   Entries marked "discussed in" are discussions, not checks. Re-derive every proof you print, as S6_09 did: that is a check. In each block's check record, name every checker with model, effort and date:
   - write "also checked in this writing" where the ledger lists earlier checks;
   - write "checked only in this writing" where it lists none;
   - the night run's own results were checked only by the night run: say so, and your re-derivation adds a check.

   A recorded check counts, whoever made it. A checked result is never called unchecked.
8. **Checked results and results not yet established are in separate parts.** A proof that fails your check has a gap to close: repair it (the push rule below applies). A result whose proof still has a gap after that work goes into a plainly headed part at the end of its paper, with its proof as far as it goes and the gap stated exactly. It is never dropped and never printed as proved.
9. **The night run S6_06_BLIND goes in.** Its attached state is its newest checkpoint or its final. The run is still going while you write, on this same account, and this account's Space search is on. So the attached state (checkpoint 21) is not its last; checkpoint 36 is in this account's Library, and later ones may be:
   - **At the start, and at every hourly review,** search this account's Space for the newest S6_06_BLIND checkpoint (files named `S6_06_BLIND_checkpoint_NN.zip`) or its final.
   - Where it is newer than what you have, take its new and changed rows in, placed by the same rule.
   - Your own checkpoints may be seen by it in the same way. That is expected, and it needs nothing from you.

   Place it as the plan's section 6 places it:
   - **Paper IV:**
     - the class of every family on every fan, by the formula KL(S−1)(S−3)/8;
     - the flop rule;
     - the generator OS45 and the covers that realize every class of Θ₇;
     - the table of families;
   - **Paper V:** the family in c (its Hodge table, tangent cohomology, automorphisms and exact domain);
   - **five text changes:**
     - the reference-fan scope;
     - the non-coprime homology of OS49 after III Thm 4.20, whose printed form assumes gcd(n,3k) = 1;
     - the sign theorem restated for irreducible and normal-crossings fibres, with "Hopf" in place of "class VII";
     - a neutral correction: Liu-Rollenske's family with fixed data closes up over u = w², not over the u-disc, while their tangent-cohomology statement stands;
     - the no-filling theorem widened to every admissible twist and every coprime (3k,4l) family, with the corner coefficient −pn in its mechanism.

   Where the attached state is a checkpoint, the rows it still marks as running go to the part of condition 8 in Paper IV, with what is proved.
10. **The sign theorem.** Paper II proves it for irreducible and normal-crossings fibres, from the night run's Part 4 and S6_09's section 9. Paper VI proves it for every degeneration, from S6_09 Paper II sections 7-12, with its own opening at rungs 0 and 1. Paper II cites Paper VI for the general case.
11. **The fixes our checks of S6_09 left** (`checks/INTAKE_S6_09.md`, sections 1.3 and 4.3):
    - [AC26] is credited as its authors name themselves, Claude and L. Alpöge;
    - the phrases "effort not recorded" and "date not recorded" appear nowhere. Give the date where our records give it, and otherwise leave the date out;
    - every other item of those sections is done.
12. **Credit, exactly.** Before a result is called new, check it against [AC26] (Claude and L. Alpöge: the original PDF, with our transcription for searching; the PDF wins where they differ), [E26], [DGKX] versions 1 and 2 and the other attached literature. Record each check in the inventory: found, with the place; or not found, with what you searched for. A result found there is credited to its source even when our proof differs. Our corrections of printed statements are of kind "Correction" or "Counterexample", each with its locator, the statement as printed, the corrected statement and the reason, worded neutrally. That X_c contradicts [CDP20, Corollary 2.3] is due to [AC26]: Paper I says so in its introduction and refers to Paper II.
13. **Literature is opened before it is cited.** Every bibliography entry is marked verified (opened and matched with what is cited) or unverified, and an unverified entry supports nothing the papers rely on.
14. **Authorship and models.** The papers are AI-produced and say so; never "AI-assisted". Every model is named with its effort setting and the dates of its work:
    - GPT-5.6 Sol (OpenAI) in Codex at reasoning effort ultra, the working edition of 24 August to 9 September 2026, with a few inputs from GPT-5.6 Sol in ChatGPT Pro mode on the web;
    - GPT-6 Astra (OpenAI, ChatGPT Pro mode): the research runs of 12-16 November 2026, S6_09_PAPERS of 16-17 November, the night run S6_06_BLIND of 16-17 November, and this writing;
    - Claude Fable 5.2 (Anthropic) at effort high and at effort max, and Claude Opus 5.5 (Anthropic) at effort max: the readings, checks and plans of 12-17 November 2026.

    A short methodology paragraph in each paper explains the effort names, citing OpenAI's and Anthropic's own documentation, which you open. Each paper states that no human has checked its mathematics. The papers name no person as an author of, or contributor to, our work. Our text is dedicated to the public domain under CC0 1.0, and the declarations say so.
15. **Figures where the geometry carries the reason,** each a rung of its own, in TikZ in the TeX:
    - the (3,4,∞) base orbifold with the fibres over it;
    - the parameter disc 0 < |w| < 216, with the puncture, the natural boundary, the special fibres and the real loci;
    - the fundamental domain of the index-twelve monodromy kernel.

    The Θ₇ results go in a table: family, construction, class, and the classes its covers reach.
16. **The format.** The post format (`format/HEXAGON_POST_FORMAT_20261114.md`) holds with its binding rule. Its limit of about three pages of front matter does not apply: the openings of condition 3 replace that front matter.

## The order of the work

1. **The inventory first.** Write `S6_10_PAPERS_inventory.csv`:
   - one row per statement printed in the six papers;
   - one row per S6_09 row that is not printed, with its place in the compendium and the reason (known, classical, a failed route, a second proof, apparatus);
   - one row per row of the night run.

   The columns are `paper, label, s6_09_label, source_run, source_id, kind, status, main_or_supporting, uses, check_record, credited_to, in_compendium_only_because, notes`. Keep it current as you go. It is the measure of completeness.
2. **The openings of all six papers,** rungs 0 and 1 of every main result, one file per paper.
3. **The bodies,** paper by paper, in the order I, II, VI, III, V, IV. IV comes last because the night run feeds it. Each paper is complete before the next: written, every proof checked, typeset, the typesetting check passed.
4. **The six together:** cross-references, notation, the series rung 0 in Paper I, and the check records consistent across the papers.

Write the files from the start and extend them as you go, so that an interruption loses little.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

For this prompt the main question is the six complete papers. The following is work on the main question:
- writing our new results into them with their proofs and their rungs;
- checking those proofs;
- citing the known results with their locators.

Extending a result beyond what the papers report, or re-proving what the papers cite, is not.

In this prompt an open row is an inventory row that is not yet done in the sense of point 1 below, the three checks of
item 10 of the first section included: a row whose three checks are completed and recorded has changed status.

1. **Done** means:
   - every row of the inventory is in one of three places: printed with its checked proof in its paper; in the part of condition 8 with its gap stated; or in the compendium only, for a reason the inventory states;
   - the six papers are complete from their openings to their references;
   - every paper has had the three checks of item 10 of the first section, and its statuses and check records show
     them;
   - every condition above holds on every page;
   - each PDF passes the typesetting check;
   - the report lists every discrepancy you met and how it was settled, and every change against the plan with its reason.
2. **Not acceptable:**
   - a new result without its proof in its paper;
   - a known or classical result re-proved at length in a paper, outside the exceptions of condition 2;
   - a main result without its rungs 0 and 1;
   - a rung that says more than the rungs below it prove;
   - a result called unchecked when the ledger or your own re-derivation records a check;
   - "conditional" as a status;
   - a statement without its scope;
   - a model named without its effort;
   - a reference cited unopened for something the papers rely on;
   - a paper without the three checks of item 10 of the first section;
   - an outline, a sample, or some of the papers in place of all six.
3. **Finished** only when the six papers are done in the sense of point 1. Keep working until then: do not stop because the remaining work is large, because a paper looks presentable, or because much has already been written. If the session itself ends first (the environment stops you, not your choice), the first line of `S6_10_PAPERS_report.md` reads INCOMPLETE and the inventory shows the state reached for every row; a continuation run will resume from your newest checkpoint and this prompt. Never present such a return as complete.

---

THE MATERIAL YOU ARE GIVEN

Seven zips. Each has a `MANIFEST.tsv` with the origin of every file and the reason it is attached.
- `S6_10_PAPERS_1_s6_09.zip`: the S6_09_PAPERS return, which is the compendium:
  - the TeX of its three papers;
  - its inventory (1,184 rows) and notation sheet;
  - its bibliography and its report.
- `S6_10_PAPERS_2_night_run.zip`: the newest state of the night run S6_06_BLIND: its paper's TeX, its results table, its report, its literature log and its bibliography. Its README says whether it is a checkpoint or the final.
- `S6_10_PAPERS_3_plan_and_checks.zip`:
  - `plan/`:
    - `LAYOUT_DESIGN_20261117.md`, the layout and the reasons for it;
    - `KEEP_SKETCH_20261117.md`, what each paper keeps, with the night run's placement and the decisions;
    - `LESSONS_S6_09.md`, what S6_09 taught us;
  - `checks/`:
    - `S6_CHECK_LEDGER.tsv` and its summary;
    - `INTAKE_S6_09.md`, our intake of S6_09 by Claude Fable 5.2 at effort high, with the fixes it lists;
    - `gazette_candidates.tsv`, the 61 main results with their uses;
  - `reviews/`, every review, intake, reading, position and check made on the S6 runs, with `WHO_WROTE_WHAT.md`;
  - `format/`, the post format.
- `S6_10_PAPERS_4_sweep1.zip`: the sweep of 18 November over all 1,124 S6 rows (see the paragraph above the task): its summary, 16 corrections, merge links, flag verdicts, placement and check counts.
- `S6_08_PAPERS_5_literature.zip`, as given to S6_09:
  - `papers/`, the LaTeX sources of the literature ([E26], [DGKX] versions 1 and 2, [CDP98], [CDP20], Lehn-Rollenske-Schinko, Viaclovsky's papers, Liu-Rollenske and the others), with Duke-Imamoglu as a PDF (no source exists);
  - `original/`, [AC26] as published (PDF) and our transcription of it.
- `S6_08_PAPERS_1_returns_tex.zip`: the TeX of the six research runs with their results tables and reports. In our files, "FAM A.5.2" is Statement A.5.2 of S6_02_FAMILY; PUSH, INV, CDP, MAPS and ARI are S6_02_PUSH, S6_01_INVARIANTS, S6_03_CDP, S6_04_MAPS_MANIFOLDS and S6_05_ARITHMETIC.
- `S6_08_PAPERS_2_returns_code.zip`: the same runs' programs, certificates, records and computation logs, for re-running.

WHAT TO DELIVER

One ZIP containing:
- `S6_10_PAPERS_I.tex` to `S6_10_PAPERS_VI.tex` and their PDFs (LuaLaTeX, compiling cleanly), in English, first person plural, in the register of a careful research paper, with no summaries of what is about to be done and no closing recapitulations;
- `S6_10_PAPERS_inventory.csv` (point 1 of the order of the work);
- `S6_10_PAPERS_notation_sheet.md`;
- `S6_10_PAPERS_references.bib`, every entry marked verified or unverified;
- `S6_10_PAPERS_report.md`, giving:
  - every gap, disagreement or unmatched statement you met, with its places and how it was settled;
  - every proof you repaired;
  - the three checks of each paper: what was re-derived, what was rerun and with which program, what was quoted and
    from where, and what each check changed;
  - every change against the plan, with its reason;
  - the references opened;
  - the counts of the typesetting check before and after;
- `code/`: every program you wrote or re-ran, with its output.

Work through the whole inventory; do not ask whether to continue.

IF THE EXECUTION ENVIRONMENT FAILS

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals
for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore
your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after
that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only
through checkpoint ZIPs and the final ZIP.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log:
- no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text;
- no font may be missing (S6_09's rendering lacked `rsfs10`).

Fix each problem in the source (scale or split a wide diagram, break a wide display, let a line break, load the font) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here. Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

**Checkpoints.** Save a checkpoint ZIP to the Library once every 45 minutes of work, each under a new name, `<ID>_checkpoint_<NN>.zip`, with `NN` counting up from 07 (the earlier run saved 01 to 06). Never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from your checkpoints (the newest first, then the earlier ones its file list names) and from this conversation before you continue. The final ZIP holds every deliverable in its current version and every file of yours that is in no checkpoint whose save you saw succeed; its file list names the checkpoint that holds each other file. A file or passage dropped from the work is listed in the report with the reason (superseded by which file, or wrong).
Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every deliverable in its current version (paper, sections, results table, report, notes, scripts) and every other file of yours that is new or changed since your last checkpoint whose save you saw succeed, with a file list that names, for each file left out because it is unchanged, the checkpoint that holds it. Leave out the attached files themselves, the scans and sources you were given: we have them. Leave out earlier checkpoints, archives of earlier versions, and rendered page images (keep only an image that shows a problem the report discusses); we keep every checkpoint you save. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB. The Library refuses a file larger than 512 MiB (536,870,912 bytes), and a checkpoint it refuses is lost: one of our runs lost a checkpoint that way. If one would be larger, save it as several ZIPs of under 500 MB each, `<ID>_checkpoint_<NN>_part<k>.zip`, the file list in the first part.
