# S6_SERIES_GRIND: the S6 papers finished as one standardized series, every result integrated and checked to confidence

Writing and checking prompt, 19 November 2026, for GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix of every
deliverable: `S6_SERIES_GRIND`. Written by Claude Opus 5.5 (Anthropic) at effort max.

## This prompt may be sent more than once, from any account

Everything you need is in the attached ZIP. Do not search any Library, Space, project or earlier conversation, and do
not rely on any file that is not attached.

- **A fresh start.** If no checkpoint is attached, start from the attached state (section 2). Your first checkpoint is
  `S6_SERIES_GRIND_checkpoint_01.zip`.
- **A continuation.** If a ZIP named `S6_SERIES_GRIND_checkpoint_NN.zip` (or several parts of one) is attached besides
  the base ZIP, this is a continuation of an earlier run of this same prompt.
  - Restore your workspace from that checkpoint and from the base ZIP. Verify every file against the checkpoint's file
    list (size and SHA-256).
  - Read its `PROGRESS_LEDGER.md` and `S6_SERIES_GRIND_report.md`, then continue the work from the state they record.
  - Number your next checkpoint NN+1.
  - Record the continuation, with its start time, in the ledger and the report.

## 1. The goal

The S6 work is a series of papers on one object: the holomorphic families of complex structures on S⁶ built from the
(3,4,∞) family of torus-fibred complex six-spheres, and what follows from them. The papers will be published one by
one: on GitHub at once, and on a public repository for AI-produced mathematics after a human reads each one.

The series must do three things:
1. **The point at once.** A mathematician with little attention to spare gets the point of each paper in its first
   pages, and can go deeper exactly where they want, with as little effort as possible.
2. **Not wrong.** Humans will have less time to referee AI-produced mathematics, so the checking falls to us. Every
   result is checked until we are confident it is right (section 5).
3. **One coherent work** on one topic, clearly marked as a series whose papers relate to each other.

**Done** means:
- the five papers of section 3 exist in the standardized form of section 4;
- every result of the attached state is integrated: printed with its complete proof in its paper, in its paper's final
  part with what is proved and the gap stated exactly, or left out for a reason recorded in the inventory;
- every result is checked to confidence, and the record shows how;
- every PDF passes the typesetting check.

## 2. The state you start from

The attached ZIP holds everything below. Its folders are described at the end of this prompt.

**The six papers of S6_10_PAPERS at its checkpoint 15** (19 Nov 2026, 10:45 UTC; the run has ended there). One
standalone LuaLaTeX file each:

| Paper | Topic | Pages |
|---|---|---:|
| I | the (3,4,∞) family: periods, moduli, the two ends | 475 |
| II | torus-fibred threefolds with b₁ = b₂ = 0; the Campana-Demailly-Peternell argument; the sign theorem for irreducible and normal-crossings fibres | 471 |
| III | maps from the six-spheres and the manifolds the construction gives | 409 |
| IV | smooth monodromy in Θ₇ = Z/28 | 1,507 |
| V | complex fourfolds on 3HP²#(−HP²) and the family in c | 173 |
| VI | the sign theorem for every degeneration | 415 |

Each opens with its main results at rung 0 (the result and its mechanism) and rung 1 (its proof in 3-7 steps): 77
rung-0 blocks in all.

**The inventory** (`S6_10_PAPERS_inventory.csv`):
- 1,524 rows: 1,160 printed (1,134 labels) and 364 compendium-only, each with its reason;
- statuses: 1,473 proved, 33 false as stated, 17 open, 1 proved under hypotheses H;
- 167 main rows.

The check record is `CHECK_EVENTS.tsv`: 6,492 typed events. The run's report and ledger are attached.

**The open rows:**
- inv:C3.8 and its two remarks, in Paper I;
- ari:C.7.4, proved under a period hypothesis H that is open, in Paper I;
- inv:E2.3, in Paper II;
- maps:src:D.2.4, in Paper III;
- night:P3K.75 and night:P3K.109-P3K.119, printed "open, under continuation review" in Paper IV's final part.

**What our checks since then found** (all attached, folder `S6_GRIND_2_checks_and_plan`):

1. **The sign convention of Paper IV.** The physical line is M, not U = M⁻¹. A second model family checked this in its
   geometry on 19 Nov 2026 (intake of the night run S6_06_BLIND at checkpoint 36, section 6). It also re-proved the
   normalization of P3F.22, μ(λ(b)) = +1/28 (section 7), relative to Jin's coordinates (k,ℓ)(a) = (1,4) and
   (k,ℓ)(b) = (8,8) (arXiv:2608.26698v2, Lemma 6.2). Record both as check events of those rows.
2. **The night run at its checkpoint 36** (`S6_06_BLIND_results.csv`, 299 rows; its report). The papers carry 296 of
   its 299 rows. Not yet integrated:
   - P1.6 and P1.14: the night run's own derivation of the fourfold's oriented diffeomorphism type, by Wall's
     extended-form classification and Kramer-Stolz, Theorem A. Record them as an independent re-proof of the
     conclusion of maps:src:F.4.1.
   - P5.7: the comparison with both versions of Du-Guo-Kusakabe-Xie. It belongs to Paper I's credited appendix.
   - P3K.109-P3K.119 and P3K.75: open (above).
3. **The intake of S6_10_PAPERS checkpoint 06** (Claude Opus 5.5 at effort max, 18 Nov 2026): 12 check events that the
   papers' records omit, among them re-proofs of cdp:st:B1 and of the parity theorem cdp:st:C.2.UN.1. Merge them.
4. **The register sweep** (Claude Opus 5.5 at effort max, 18 Nov 2026; folder `sweep1_s6`): 16 corrections, 177 merge
   links, 95 flag verdicts.
   - Carried, as far as our checks reached:
     - the reference-fan scope of the class-0 theorems (correction 2), except the wording of night:P3K.7 and
       night:P3K.8, whose scope comes only from their section;
     - the gcd(n,3k) hypothesis of S6_04 D.2.11 (correction 1);
     - the corner coefficient −pn (correction 9);
     - the resolved fibre-product fourfold (correction 11).
   - Check every one of the 16 against the papers, carry what is not carried, and record each as a check event.
5. **The series consistency** (`S6_PAPER_V_DEPOSIT_PREP_20261119.md`, section 3; `series_consistency.json`).
   - At checkpoint 15, all 436 cross-paper citations (about 121 distinct statements) resolve to the intended statement
     in the current numbering. Every imported statement is proved, or is cited as the refutation it is. No later result
     refutes one.
   - Restructuring renumbers the papers, so regenerate every cross-reference from labels and tags, and repeat the check
     on your final state.
6. **What the papers lack for their readers** (`S6_PUBLICATION_READINESS_20261119.md`, `S6_SERIES_DESIGN_20261119.md`):
   - no paper has a table of contents, and Papers I and III have no abstract;
   - every statement carries a long check record full of workflow text;
   - no statement links back to the step it proves;
   - only Paper I describes the series;
   - Paper IV's final part of results not yet established is about a third of the paper;
   - the bibliography file carries 32 unverified or pending entries that no paper cites.
7. **Rows checked only by the session that wrote them** (39):
   - I:weierstrass-comparison and I:monodromy-fundamental-set (I);
   - night:P3K.36 and ii:LR:covering (II);
   - in Paper IV, iv:i3_all_reduced_caps and the 34 rows iv:correction:* together with iv:rank_two_specialization.
8. **Literature status still pending** on the night run's main results:
   - I: night:P2.2, P2.7, P2.9;
   - II: night:P4.58 and P3K.36;
   - III: night:P3F.34;
   - IV: night:P3F.21, P3F.35, P3K.99-P3K.108, and the seven refuted historical rows P3K.10, 22, 23, 30, 31, 33 and
     P3F.53.

## 3. The papers of the series

**THE SPLIT.** This is the paragraph to edit if the split changes before this prompt is sent. The series has five
papers, each on one topic, so that each topic has one place:

- **I.** The (3,4,∞) family: periods, moduli and the two ends. This is S6_10 Paper I.
- **II.** Torus-fibred threefolds with b₁ = b₂ = 0, the Campana-Demailly-Peternell argument, and the sign theorem.
  - This is S6_10 Paper II, with S6_10 Paper VI as its second part.
  - The sign theorem appears once: for irreducible and normal-crossings fibres first, then for every degeneration.
- **III.** Maps from the six-spheres and the manifolds they give. This is S6_10 Paper III without its §6.
- **IV.** Smooth monodromy in Θ₇. This is S6_10 Paper IV.
- **V.** Complex fourfolds from the family. This is S6_10 Paper V, with S6_10 Paper III §6 (the fibre-product fourfold:
  maps:src:E.1.x, E.2.x) as one of its parts.

The series title is *The (3,4,∞) family of complex six-spheres*. Each paper's title names its topic after the series
title and its number.

## 4. The standardized form

Every paper has the same form. It is built from what is known to work for the reader of section 1: the plan stated
first, the reasons kept beside the claims, and a clear path to the detail. The reasons are in
`S6_SERIES_DESIGN_20261119.md`.

**4.1 The first pages,** about 8-20 per paper, in this order:
1. **The title block and the abstract.** The abstract states the main theorems in words, in at most 250 words.
2. **A table of contents,** standard and hyperlinked.
3. **§1 Results and their proofs in outline:**
   - **1.1 The series and this paper.** One paragraph and one table, written once and used in every paper: the five
     papers, the main result of each in one line, and which papers each one uses. Paper I's §1.1 also carries the
     whole series at rung 0.
   - **1.2 The main theorems,** lettered A, B, C, ..., at most about seven per paper.
     - Each is stated in full, with its hypotheses and scope.
     - Each has its one mechanism in a sentence (rung 0).
     - Each has its literature status: new; or corrects [X, statement, page]; or known and cited, re-derived only under
       the exceptions of condition 2.
     - Group the 77 rung-0 blocks into these theorems. The other results of each paper go in one table of further
       results: one line each, with its number and link.
   - **1.3 The proofs in outline.** For each main theorem, 3-7 numbered steps (rung 1). Each step is a precise claim,
     its reason in a line, and a link to the body statement that proves it.
     - Each step is exactly the claim that its expansion proves, and no step says more than the body proves.
   - **1.4 Known and new.** One table citing prior results with exact locators.
   - **1.5 Methodology,** about one page:
     - **Who did what**, each model with its effort and dates (condition 9), and in three sentences how the models
       worked together: prompts, returns, readings and checks, corrections back into the next prompt.
     - **How the results were checked to confidence** (section 5): the kinds of check, with their counts.
     - **One sentence** that no human has checked the mathematics.
     - **The CC0 dedication.**
     - **The provenance links:** the runs, the checkpoints and the check records on GitHub.
   - **1.6 How the paper is organized:** one paragraph and a figure of how the main theorems depend on each other.
4. **The body, ordered by the mathematics** (rung 2 and below; never by the chronology of the work).
5. **A final part, "Results not yet established".** Each such result with everything proved about it and its gap
   stated exactly.
6. **References.** Only entries the paper cites, each opened and marked verified.

**4.2 A statement block in the body** holds, in this order:
- its number, its tag and its status in one word;
- a link "checks" to its entry in the paper's check file;
- a line "uses: ..." (the labels its proof uses);
- a back-link "proves step k of Theorem B" where it does;
- the statement;
- the proof, in numbered steps.

**Proofs:**
- A long proof uses numbered levels in Lamport's manner (⟨1⟩1, ⟨1⟩2 with ⟨2⟩1, ...), and may open with a
  one-paragraph sketch.
- Every step at every level is a claim with its reason beside it.
- A computational step states its method, inputs and results in the text. Its program and output are in `code/`, and
  the paper names the file.

No workflow text in the papers: statuses are one word, and the check records are in the check files. Every proof is in
the paper. The check records and the runs that produced the results are the provenance, kept on GitHub and linked.

**4.3 Numbers, tags and links:**
- **Numbers.** Statements are numbered by section inside a paper (Theorem 7.4) and cited across the series as II.7.4.
  Main theorems are cited as II.A.
- **Tags.** Every statement receives a permanent four-character tag, unique across the series, printed in its header
  and recorded in `S6_SERIES_GRIND_tags.tsv` (tag, paper, number, page, label, status). A tag never changes and is
  never reused. Every statement carries `\hypertarget{tag-XXXX}{}`.
- **Links:**
  - main theorem → its outline proof and its full statement;
  - outline step → the body statement that proves it;
  - body statement → the step it proves, and its uses and used-by lists, generated from the "uses" lines;
  - end of each proof → §1;
  - another paper's statement → that paper's PDF at `#nameddest=tag-XXXX`, with the page.
  - The PDF outline (bookmarks) mirrors §1 and the body.
- **Check files.** For each paper, `S6_SERIES_GRIND_checks_<P>.md`: one entry per statement, anchored by its tag.
  - Each entry gives every check event (who, with model and effort, the date, the type, what was done) and the
    independent routes that agree.
  - Each main theorem's entry adds a line saying how we know it and what risk remains.

**4.4 The binding conditions:**
1. **New results with complete proofs.** Every new result (one not found in the literature) is stated and proved in
   full in its paper, with the lemmas its proof uses, unless they are known. A refuted statement goes in as a
   counterexample or correction, with its proof.
2. **Known results are cited, not re-proved.** Known results (published work, classical results, textbooks, the course
   CG-S6) are cited with exact locators (statement and page), opened in the source before you cite them. There are
   three exceptions:
   - the credited appendix of Paper I with our proof that X_c ≅ X_c' if and only if c' − c ∈ 2Z, for the standard data.
     Our proof was in our public working edition by 8 September 2026. It is Theorem 1.4 of [DGKX] version 1
     (23 September 2026), and version 2 does not contain it. State both facts plainly.
   - the credited appendix of Paper I with the tangent cohomology (1,1,1,0), the Kuranishi germ and Aut(X_c) = C*.
     These are theorems of [DGKX] version 1, re-derived after reading it: say "re-derived".
   - a short proof where we use a known result in a form its sources do not state.

   Compare no other dates, and use no word such as "first" or "priority".
3. **Statuses.** Each result is one of:
   - proved;
   - proved under hypotheses H (state H, and say whether H holds in the cases used);
   - open, with everything proved about it;
   - false as stated, with the counterexample and the corrected statement.
4. **Scope.** Every statement names its hypotheses and choices: the cusp fan, the line convention (M or U), the
   parameter normalization.
5. **Credit, exactly.** Before a result is called new, check it against [AC26] (Claude and L. Alpöge: the original PDF
   wins where it and our transcription differ), [E26], [DGKX] versions 1 and 2, and the other attached literature.
   Search further online, and record each search in the inventory. A result found there is credited to its source even
   where our proof differs. A correction of a printed statement gives the locator, the statement as printed, the
   corrected statement and the reason, in neutral words.
6. **Literature is opened before it is cited.** Every bibliography entry is marked verified (opened and matched) or
   unverified. An unverified entry supports nothing the papers rely on.
7. **One notation for the series.** It is in `S6_10_PAPERS_notation_sheet.md`, kept current, with every transport
   between conventions stated where it is used.
8. **Figures** where the geometry carries the reason, in TikZ:
   - the (3,4,∞) base orbifold with its fibres;
   - the parameter disc 0 < |w| < 216 with its puncture, natural boundary, special fibres and real loci;
   - the fundamental domain of the index-twelve monodromy kernel.

   The Θ₇ results are in a table: family, construction, class, and the classes its covers reach.
9. **Authorship and models.** The papers are AI-produced and say so; never "AI-assisted". Every model is named with its
   effort setting and the dates of its work:
   - GPT-5.6 Sol (OpenAI) in Codex at reasoning effort ultra: the working edition, 24 Aug - 9 Sep 2026;
   - GPT-6 Astra (OpenAI), ChatGPT Pro mode: the research runs of 12-16 Nov 2026, the night run S6_06_BLIND of
     16-18 Nov, the writing runs S6_09_PAPERS and S6_10_PAPERS of 16-19 Nov, and this run;
   - Claude Fable 5.2 (Anthropic) at effort high and at effort max, and Claude Opus 5.5 (Anthropic) at effort max: the
     readings, intakes, sweeps and checks of 12-19 Nov 2026.

   The papers name no person as an author or contributor. Our text is dedicated to the public domain under CC0 1.0.

## 5. Checked to confidence

**The goal** is that every printed result is right, and that a reader can see why we are confident of it. Confidence
comes from independent methods that agree, aimed at the places where errors occur.
- **What catches errors.** Writing out every step with its reason, down to enough levels, catches errors that prose
  hides. A global check finds the most serious errors: does the argument prove too much, does it contradict a known
  special case, does it respect its scopes and conventions? Computing a claimed number or formula by a second,
  independent method catches what reading does not.
- **What does not.** Repeating one method by the same kind of checker misses the same things.
- **Our own record agrees.** The substantive errors of S6 were found by computation contradicting a formula, by
  tracking a sign convention, and by comparing statements with their sources. Renewed re-derivations of already-checked
  rows by the same model family found nothing new.

So, for every result:
1. **Every step re-derived.** For every new result, re-derive each step of its proof from its statement and the results
   it cites, writing your derivation before you read the printed step; then compare.
   - A step that re-derives is checked. A step that does not is a gap: repair it.
   - A result whose gap remains goes to its paper's final part with the gap stated exactly.
2. **The global check.** For every main theorem and every result a main theorem rests on: check its outline proof
   against the body, its scope and conventions, and its agreement with every known special case, in its own paper and
   across the series.
3. **Independent computation.** Every computational step (certificates, interval arithmetic, enumerations, symbolic
   identities, the Θ₇ classes): a new program that reuses none of the earlier code, by a different method or library
   wherever one exists, its output compared exactly. The program and its output go in `code/`.
4. **The error-prone points first:**
   - the line conventions and signs of Paper IV;
   - the 39 rows of section 2 item 7;
   - the chain cdp:st:C.2.UN.1-86 behind the sign theorem;
   - the correction of Liu-Rollenske (ii:LR:covering and the refutation of P3K.36);
   - the unrestricted scope of cdp:st:D.2.5;
   - the night run's results that only it and S6_10 have read;
   - every statement that corrects a published one.
5. **Literature status** for every main result (condition 5). Do it first for the rows of section 2 item 8.
6. **The checks already recorded count.** A result already checked by an independent method keeps that check; build on
   it and add what confidence still needs.

**What confidence looks like in the record.** Each main theorem's entry in its check file lists:
- the independent routes that agree (for example: the proof re-derived; a re-proof by another run; the constants
  recomputed by independent code; agreement with a known special case; the literature status);
- what risk remains.

A result whose routes disagree is not done: settle the disagreement.

**Check events.** For every statement, record its check events in CHECK_EVENTS.tsv: statement id, date, who (model,
effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and
rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome.
This covers the statements of this run and every earlier statement you check, use or refute here. Give each event the
type of what actually happened, neither more nor less. Merge the events of the attached intakes and sweeps into it.
`CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

## 6. The order of the work

1. **Restore and verify** the attached state, or your checkpoint (top of this prompt).
2. **The inventory first.** Carry `S6_10_PAPERS_inventory.csv` forward as `S6_SERIES_GRIND_inventory.csv`, with the new
   columns paper, tag, check summary and confidence line. Place every row of the papers, of the compendium and of the
   night run, and keep it current: it is the measure of completeness.
3. **The corrections and findings of section 2,** each carried into the papers and recorded.
4. **The split of section 3:** move the material, regenerate cross-references from labels and tags, and repeat the
   consistency check of section 2 item 5.
5. **The first pages of all five papers** (section 4.1), so that the series reads as one.
6. **The bodies, paper by paper, in the order I, II, III, V, IV:** the form of 4.2, the confidence work of section 5,
   the open rows under the push rule below.
7. **The five together:** tags, links, check files, the series table, the notation, the consistency check repeated,
   the typesetting check.

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

**The main question** of this prompt is the five finished papers.
- **Work on the main question:**
  - writing the results into the standardized form with their proofs;
  - checking them to confidence;
  - citing the known results with their locators.
- **An open row** is an inventory row that is not yet done in the sense of point 1 below: placed, written in the form
  of section 4, and checked to confidence. A row that reaches that state has changed status. The open mathematical rows
  of section 2 are attacked under the push rule. Each of them that stays open is placed in its paper's final part, with
  everything proved about it.

1. **Done** means:
   - every row of the inventory is in one of three places: printed with its checked proof in its paper; in its paper's
     final part with what is proved and its gap stated exactly; or left out, for a reason the inventory states (known
     and cited, classical and cited, a failed route, a second proof, apparatus);
   - the five papers are complete from their first pages to their references, in the form of section 4;
   - every result is checked to confidence (section 5), and its check file shows how;
   - every condition of section 4.4 holds on every page;
   - each PDF passes the typesetting check;
   - the report lists every discrepancy you met and how it was settled, and every change against the attached state
     with its reason.
2. **Not acceptable:**
   - a new result without its complete proof in its paper;
   - a known or classical result re-proved at length, outside the exceptions of condition 2;
   - a main theorem without its mechanism and its outline proof;
   - an outline step that says more than the body proves;
   - workflow text in a paper;
   - a statement without its scope;
   - a model named without its effort;
   - a reference cited unopened for something the papers rely on;
   - an outline, a sample, or some of the papers in place of all five.
3. **Finished** only when the five papers are done in the sense of point 1. Keep working until then: do not stop
   because the remaining work is large, because a paper looks presentable, or because much has already been written.
   - If the session itself ends first (the environment stops you, not your choice), the first line of
     `S6_SERIES_GRIND_report.md` reads INCOMPLETE, and the inventory shows the state reached for every row.
   - The same PROMPT.md with your newest checkpoint attached will continue the work (top of this prompt).
   - Never present such a return as complete.

## What to deliver

One ZIP, `S6_SERIES_GRIND_final.zip`, holding:
- `S6_SERIES_GRIND_I.tex` to `S6_SERIES_GRIND_V.tex` and their PDFs (LuaLaTeX, compiling cleanly):
  - in English, first person plural, in the register of a careful research paper;
  - no summaries of what is about to be done and no closing recapitulations;
- `S6_SERIES_GRIND_inventory.csv`, `S6_SERIES_GRIND_tags.tsv`, and `S6_SERIES_GRIND_checks_I.md` to
  `S6_SERIES_GRIND_checks_V.md`;
- `S6_SERIES_GRIND_notation_sheet.md` and `S6_SERIES_GRIND_references.bib`, every entry marked verified or unverified;
- `CHECK_EVENTS.tsv` and `PROGRESS_LEDGER.md`;
- `S6_SERIES_GRIND_deposit_fields.md`: for each paper, its title, its abstract, and a one-paragraph statement of how it
  was produced and checked, ready for a deposit form;
- `S6_SERIES_GRIND_report.md`, giving:
  - every gap, disagreement or unmatched statement you met, with its places and how it was settled;
  - every proof you repaired;
  - the confidence work per paper (what was re-derived, recomputed with which program, quoted from where, and what each
    check changed);
  - every change against the attached state, with its reason;
  - the references opened;
  - the counts of the typesetting check before and after;
- `code/`: every program you wrote or ran, with its output.

## If the execution environment fails

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals
for as long as this session lasts, without writing recovery text into the conversation. When the environment is back,
restore your work from your newest checkpoint, redo what you had done after that checkpoint, and continue to the end.
Do not write files out as text instead: the work reaches us only through checkpoint ZIPs and the final ZIP.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log:
- no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text;
- no font may be missing.

Fix each problem in the source (scale or split a wide diagram, break a wide display, let a line break, load the font)
and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread
over the document. Give the counts before and after in the report.

**Checkpoints.**
- **When.** Save a checkpoint ZIP once every 45 minutes of work, as a file of this conversation that can be downloaded.
  - Each has a new name, `S6_SERIES_GRIND_checkpoint_NN.zip`, with `NN` counting up from 01, or from one more than the
    attached checkpoint.
  - Never overwrite, rename or delete an earlier checkpoint.
  - Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, folder, chapter or
    paper.
- **What.**
  - **Self-contained apart from the attached base ZIP.** A checkpoint is one ZIP holding:
    - every deliverable in its current version (papers, PDFs, inventory, tags, check files, notation sheet,
      bibliography, report, ledger, `CHECK_EVENTS.tsv`);
    - every other file of your own work that the next step needs;
    - a file list with size and SHA-256 of each file.

    The base ZIP and the newest checkpoint alone restore your workspace.
  - **Left out:** the attached files themselves (we have them), earlier checkpoints, archives of earlier versions, and
    rendered page images (keep only an image that shows a problem the report discusses).
  - It is never a JSON file, a recovery file, a summary, or an export of the newest pages only.
  - Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it.
- **Why.** The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost.
- **Size.** Keep every checkpoint ZIP, and the final ZIP, under 500 MB. If one would be larger, save it as several ZIPs
  of under 500 MB each, `S6_SERIES_GRIND_checkpoint_NN_part<k>.zip`, the file list in the first part.
- **The final ZIP** holds every deliverable in its current version. A file or passage dropped from the work is listed
  in the report with the reason (superseded by which file, or wrong).

Work through the whole inventory; do not ask whether to continue.

---

THE MATERIAL YOU ARE GIVEN

One ZIP, unpacked into these folders (LaTeX sources wherever they exist; PDFs only where no source exists):

- **`S6_GRIND_1_papers_cp15/`**, the state of S6_10_PAPERS at its checkpoint 15:
  - the six standalone papers `S6_10_PAPERS_I.tex` to `S6_10_PAPERS_VI.tex` with `preamble.tex`;
  - the inventory, `CHECK_EVENTS.tsv`, the notation sheet, the bibliography, the report and `PROGRESS_LEDGER.md`;
  - `gate_tables/`, the run's final row-state tables.
- **`S6_GRIND_2_checks_and_plan/`**, the checks and plans since then:
  - `S6_SERIES_DESIGN_20261119.md`: the reasons behind section 4 and section 5, with their sources;
  - `S6_PUBLICATION_READINESS_20261119.md` and `S6_PAPER_V_DEPOSIT_PREP_20261119.md`: the state per paper, and the
    series consistency;
  - `series_consistency.json` and `.out`: the cross-paper imports, and the scripts that built them;
  - `INTAKE_S6_06_BLIND_cp36_20261119.md` with its check events and scripts: the night run's last state, and the
    second-family checks of the sign convention and of P3F.22;
  - `S6_10_INTAKE_20261118.md` with its check events and code: the intake of S6_10 checkpoint 06;
  - `INTAKE_S6_09.md` and `gazette_candidates.tsv`: the intake of the S6_09 papers;
  - `sweep1_s6/`: the register sweep, with its 16 corrections, merges, flags and check events;
  - `S6_CHECK_LEDGER.tsv` and its summary: every earlier check per S6_09 row;
  - `KEEP_SKETCH_20261117.md` and `LAYOUT_DESIGN_20261117.md`: the earlier plan;
  - `paper_V_deposit/`: the rebuilt check records and the cross-reference links of a Paper V copy, as a worked example
    of the check files and links.
- **`S6_GRIND_3_night_run_cp36/`**: the night run's results register, report and literature log at its checkpoint 36.
  Its proofs of the rows the papers carry are printed in the papers.
- **`S6_GRIND_4_s6_09_compendium/`**: the three S6_09 papers (TeX and their .aux files) with their inventory. It is
  the earlier, exhaustive writing of the series. The papers cite it as [S6_09, label] where a reader may want a second
  proof or a classical derivation.
- **`S6_GRIND_5_research_runs_tex/`**: the TeX, results tables and reports of the research runs:
  - S6_01_INVARIANTS;
  - S6_02_FAMILY and S6_02_PUSH;
  - S6_03_CDP;
  - S6_04_MAPS_MANIFOLDS;
  - S6_05_ARITHMETIC.

  In our files, "FAM A.5.2" is Statement A.5.2 of S6_02_FAMILY, and PUSH, INV, CDP, MAPS and ARI name the others.
- **`S6_GRIND_6_literature/`**: the LaTeX sources of the literature ([E26], [DGKX] versions 1 and 2, [CDP98], [CDP20],
  Lehn-Rollenske-Schinko, Viaclovsky, Liu-Rollenske and the others), Duke-Imamoglu as a PDF, and [AC26] as published
  (PDF) with our transcription.

Every other source you need you may open online; record its exact locator and mark it in the bibliography.
