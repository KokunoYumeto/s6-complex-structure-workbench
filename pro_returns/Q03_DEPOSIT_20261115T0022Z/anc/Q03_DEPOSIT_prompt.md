# Q03_DEPOSIT: unit jobs with precedence constraints on m machines, polynomial for every fixed m ≥ 3; close the open points of the proof, check it in full, and bring the post to deposit

For GPT-6 Astra (OpenAI), effort Pro, ChatGPT Pro mode. File prefix for the deliverables: `Q03_DEPOSIT`. Written on 15 November 2026 by Claude Opus 5.5 (Anthropic) at effort max, from the open points recorded in the post and in the three checks of October.

## What is to be settled

The attached post `post/hexagon_post_example_Q03.tex` states and proves: for every fixed integer m ≥ 3, the problem Pm | prec, p_j = 1 | C_max (unit-time jobs, precedence constraints given as an explicitly listed directed acyclic graph, m identical machines, minimize the makespan) is solvable in deterministic polynomial time. One algorithm decides a deadline T, constructs a schedule when one exists and constructs an optimal schedule, in O_m(N^(60m²+129m+1)) steps for the padded size N = mT (bound (1.2)); the structure theorem has leaf budget K_m = 12m + 25 (Theorem B = Theorem 8.5). The case m = 3 is OpenAI's preprint of 24 September 2026; m = 2 is classical (Fujii–Kasami–Ninomiya 1969, Coffman–Graham 1972); with m part of the input the problem is NP-hard (Ullman 1975).

The proof is GPT-6 Astra's return of 23 October 2026 (ChatGPT Pro mode). Claude Opus 5.5 at effort max (Message Batches API) checked it three times on 23 October, independently, from the same input: one verdict "proved with fixable gaps", two "proved as stated". Three points are open, and the post is not yet ready to be deposited on hexagonmath.org:

1. **The exponent of (1.1).** Corollary 9.3 asserts the bound O_m((L+2)^(60m²+129m+8)) in the input length L as a conservative value, without an itemized accounting. The check reports derive 60m²+129m+2.
2. **Proposition 9.2.** The multitape costs of the subroutines are not itemized.
3. **The sources.** The claims the post makes about its sources (the labels and constants of the preprint in column 2 of the dependency table, the scope of the formalization file, the scope of drbh's repository, the bibliographic details) were not checked against the sources themselves.

The task: settle all three, check the whole proof, search the literature, and deliver the post ready for deposit.

## The tasks

### Part A. The running time

- **A.1** Itemize the multitape cost of every subroutine of the algorithm of Section 9: reachability, the generation and evaluation of the B bounded-size formulas, the pairwise deduplication, the ordering of their bit vectors by cardinality, the dynamic program over the S candidate states, the deadline trials, the input handling and the output of the witness. Give each its own bound in N and m, with the tape layout it assumes, and prove Proposition 9.2 from that accounting.
- **A.2** Derive the bound (1.1) in the input length L for explicitly listed jobs from A.1. Determine the exponent the accounting proves, and prove it. If it is 60m²+129m+2, 60m²+129m+8 or another value, say which and why, and correct (1.1), Corollary 9.3, the abstract, the Status table and the record block to the derived exponent.
- **A.3** Check (1.2) step by step against the proof: 5m(12m+25)+4m+1 = 60m²+129m+1, with every factor traced to the lemma it comes from.

### Part B. The proof, checked in full

- **B.1** Check Sections 2 to 9 as a referee. Confirm every step of every lemma, proposition and theorem with your own argument (one paragraph per step in the report), or give the first wrong step with a repair or a counterexample. The three checks located the hard steps in Lemma 5.5 (at most m injections), Lemmas 6.2 and 6.5 (leaf counts linear in m), Lemma 7.1 (invariant (I2) for children) and Lemma 8.4 (the constant K_m); give them the most care.
- **B.2** The step layouts of Lemmas 3.3 and 5.5 were rewritten for this post by Claude Fable 5.2 at effort high, not by the producing model. Check, step for step, that they say what the return (`provenance/Q03-solution.md`) says and that no step changed its meaning.
- **B.3** Check every "Uses:" line and every row of the dependency table against the citations inside the proofs, and correct every mismatch.

### Part C. The sources, opened

- **C.1** Open every source the post cites and check each claim the post makes about it, with the exact locator (theorem number, label, page, line):
  - [P] OpenAI, *A polynomial-time algorithm for three-machine unit-job scheduling*, OpenAI Math Release preprint, 24 September 2026, https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026 (its LaTeX, as given to the producing model, is attached under `sources/papers/openai-scheduling/`; compare it with the published version and record any difference): its Theorem 1.1, its labels as cited in column 2 of the dependency table, and its constants.
  - [F] the formalization scope file https://github.com/openai/math/blob/main/lean/docs/124.md: what it formalizes and what it leaves out.
  - [D] drbh, *scheduling-proof-exploration*, https://github.com/drbh/scheduling-proof-exploration, at commit bbd3013: open the repository at that commit and state exactly what it adapts to m = 4, how far it goes, what it assumes, and what is left open. Credit it in the post with name, URL, commit and that exact scope.
  - [N] Nederlof, Swennenhuis, Węgrzycki (arXiv:2312.03495; SODA 2025); [A] Das, Wiese (arXiv:2501.09091; ESA 2022); [FKN] Fujii, Kasami, Ninomiya, SIAM J. Appl. Math. 17 (1969); [CG] Coffman, Graham, Acta Inform. 1 (1972); [U] Ullman, J. Comput. System Sci. 10 (1975); [GJ] Garey, Johnson (1979): every bibliographic detail, and every statement the post attributes to them.
  - [L] the lessons of the course *Scheduling unit jobs on three machines*, https://kokunoyumeto.github.io/open-math-courses-public/courses/three-machine-unit-job-scheduling/ (lessons 1 to 8 attached under `sources/lessons/`; lessons 9 to 11, written from this result, are public there).
- **C.2** Correct column 2 of the dependency table to what the sources say, or drop an entry the sources do not support. Record an S-type check (source opened, statement compared) in the Verification record for every load-bearing citation. A source you cannot open is listed under "unverified" in Limits and open points, with what you tried.

### Part D. The literature

- **D.1** Search the literature for the theorem for every fixed m ≥ 4, for m = 4 alone, for hardness results for a fixed m ≥ 4, and for the structure theorem with a leaf budget linear in m. Search arXiv; the STOC, FOCS, SODA, ICALP, IPCO, ESA and APPROX proceedings; authors' pages; the general web; hexagonmath.org; and everything that cites the OpenAI preprint. Record the date, every query and what each found. State in the post what was known and what is new, with the literature search dated.

### Part E. The post, ready for deposit

- **E.1** Bring the post to the attached format (`format/HEXAGON_POST_FORMAT_sections_2-8.md`) and satisfy its section 8 point by point:
  - every row of the Status table follows from the Verification record, in the same words;
  - the record block, the abstract, the Status table and the Declarations agree;
  - every model is named with its effort setting, and "effort not recorded" stands where it was not recorded;
  - every load-bearing citation has an S-type check or is listed as unverified;
  - the statement numbers match the checked text, or a concordance is given;
  - human prior work is credited with name, URL and scope;
  - the literature search is dated;
  - the file compiles, with the overfull boxes counted and the pages rendered and looked at;
  - `anc/` holds the prompt as sent, the return and the reports (from `provenance/`), with no local path, no personal name beyond the contributor line, and no credential.
- **E.2** Remove the demonstration notice and the `demonstration` field. Record your own check in the record block under `checks_of_this_text` (by GPT-6 Astra, effort ChatGPT Pro mode, the date, type F, D and S, scope, verdict). Close in `open_points` what you closed, and keep there what you could not close, as an exact statement.
- **E.3** Keep the `not_claimed` items (no bound polynomial in m, no practical algorithm, the variants listed, no formalization) unless your work changes one of them; if it does, say how.

## WHAT THE OUTCOME MUST BE

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item: the exponent of (1.1) and the full check of the proof first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026). After about three hours of work, and every hour after that, check what your current work is doing. If it moves the main question or one of the open items forward, keep going. If it is filling in detail away from the main question, stop that work, write the final package with every item's state, and deliver it. In that case this check takes precedence over the sentence above about untried approaches.

1. **Deliverables.** One ZIP:
   - `Q03_DEPOSIT_post.tex` (the post, ready for deposit) and its PDF (it compiles cleanly);
   - `Q03_DEPOSIT_report.md` (per task: what was done, the verdict, the changes made to the post);
   - `Q03_DEPOSIT_results.csv`, with one row per numbered statement of the post (`id, statement, status, where_checked, depends_on, notes`);
   - `Q03_DEPOSIT_sources.md` (per source: URL, version or commit, what it states at which locator, and the verdict on each claim the post makes about it);
   - `Q03_DEPOSIT_literature.md` (the dated search record);
   - `anc/` (the prompt as sent, the return and the three reports, from `provenance/`);
   - `code/`, with every program and its output.
2. **What counts as done:**
   - for A, the exponents of (1.1) and (1.2) derived from an itemized accounting and proved;
   - for B, every step confirmed with your own argument, or the first wrong step with a repair or a counterexample;
   - for C, every claim about a source checked against the opened source, or the source listed as unavailable with what you tried;
   - for D, the dated search record and the statement of what is known;
   - for E, every point of section 8 of the format satisfied except the last one (the user's yes, which comes after your return).

   Partly settled is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest undecided instance are the state of an item you are still working on: record them as you go, then attack the obstruction, starting from that instance.
3. **Not acceptable:**
   - comments on, or assessments of, the proof instead of step-by-step confirmations;
   - a survey or a status report;
   - "open, see [reference]";
   - a plan, a sample or an outline;
   - a claim about a source that you did not open, written as checked;
   - a statement dropped without a row.
4. **When the work is finished:** only when every task of Parts A–E is done as stated above. Keep working until then: do not stop because the remaining tasks are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `Q03_DEPOSIT_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none.
5. **If the execution environment disconnects:** wait and retry for at least 10 minutes. If it does not come back, write every file out in the chat in full, each in its own code block headed by its file name, and continue the work in the chat. An answer that only reports the disconnection is not acceptable.

## What is attached

`Q03_DEPOSIT_background.zip`:
- `post/hexagon_post_example_Q03.tex`, the post as it stands: format demonstration of 14 November 2026, with checks pending; and `post/hexagon_post_template.tex`, the template of the format;
- `format/HEXAGON_POST_FORMAT_sections_2-8.md`, the format of a post (sections 2 to 8: the rules, the parts, the rules for each part, the variants, the record block, the LaTeX source, the checks before a post goes to the user);
- `provenance/Q03_PROMPT.txt`, the prompt of 22 October 2026 as sent; `provenance/Q03-solution.md`, GPT-6 Astra's return (SHA-256 3ebeb452d6f461c23b4f8fa6f04ba6ed15abac541b5d2562fa814ba77977e60c); `provenance/artifacts/`, the files that came with it (audits, checks, code); `provenance/reports/`, the three check reports of 23 October 2026 (Q03-check.md, Q03-b-check-b.md, Q03-c-check-c.md; Claude Opus 5.5 at effort max, Message Batches API);
- `sources/`, the sources given to the producing model on 22 October 2026: `SOURCES.txt` (origin and licence of each file), the LaTeX of the OpenAI preprint (`papers/openai-scheduling/`), and lessons 1 to 8 of the course (`lessons/`);
- `register/REVIEW_REGISTER_row_Q03.md`, the row of our register of results for Q03.

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data: the machine model (multitape Turing machine, word RAM, or other), the input encoding and its length L, what N, T, n, m, K and B denote at each place, and whether the bound counts time or steps of a given machine.
2. Every bound comes with its derivation: no exponent is asserted. A constant hidden in O_m is a function of m that you state or bound.
3. Every reduction comes with its proof in the direction needed.
4. A counterexample is given completely and checked by a program whose code and output you attach. An invalid proof alone shows a gap, not falsity.
5. No authority: the return, the three checks, the preprint and the lessons are all to be checked where you use them. If one is wrong, say so and show where.
6. What you cannot settle stays on the page as an exact statement, with what you tried, the step that fails and the smallest undecided instance. Never write it up as proved, and never drop it.
7. Before calling anything new, search the literature and say what you searched. Never invent a reference.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person beyond the credits the post already gives (OpenAI for the base case, drbh for the four-machine adaptation, the classical authors), and claim no priority. This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display, a table or a line of text. Fix each one in the source (scale or split a wide table or diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the Library once every hour of work, each under a new name, `Q03_DEPOSIT_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held: a file or passage left out of the final is listed in the report with the reason (superseded by which file, or wrong).
Save checkpoints once an hour and at no other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is
one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs,
scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave
the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file,
a recovery file, a summary, or an export of the newest pages only. The checkpoints are what keeps the work if this
session dies: work that is in no checkpoint is lost.
