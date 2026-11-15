# Second pass over a pile of candidate results: which are new, which are known, which are wrong

You are going over a pile of mathematical results that a first pass collected from our work, to say for each one what
it really is. The first pass was quick and partly mechanical; yours is the second pass: more careful, item by item.

**What the pile is.** Over the past months AI models wrote open mathematics courses (lessons in LaTeX/HTML, public at
https://kokunoyumeto.github.io/open-math-courses-public/) and ran research workbenches on GitHub
(github.com/KokunoYumeto). The lesson writers were told to fix, generalize and prove whatever their sources left open,
so the lessons contain results beyond their sources: corrections of printed books and papers, counterexamples,
sharper constants, generalizations, gaps filled, new proofs. A first pass (Claude Opus 5.5 at effort medium, 14 Nov
2026) read the lessons partly by eye and partly through keyword sentences, and collected:
- `LESSON_FINDINGS.csv`: 1,509 rows, of which the rows whose `verdict` begins with "candidate" are the candidates; the
  others carry a one-line reason why they are not findings;
- `REPO_RESULTS.csv`: 13,274 rows from the repositories (claims ledgers, results registers, research notes);
- `RESULTS_SCHEMA_v1.md`: the format your output takes;
- `lessons/`: the source files of every lesson that has a candidate row, and `repo_items/`: the files behind the
  repository rows named below.

**The task.**
1. Every candidate row of `LESSON_FINDINGS.csv`. Open the lesson at its locator and read the passage and what it
   rests on. State the result exactly (hypotheses, conclusion, constants). Find what it goes beyond: the printed or
   preprint source and the exact place. Search the literature (the web, arXiv, MathSciNet-style references you can
   reach) for whether the result, the correction or the counterexample is already known, and give what you find with
   its reference. Check the mathematics far enough to say whether it holds: follow the argument; recompute a
   counterexample or a constant where that is short. Then give the verdict: no earlier source found (say where you searched) / known (with
   the reference) / wrong (with the error) / not a result (a restatement).
2. In `REPO_RESULTS.csv`, every row of these sources: the zeta reader's row SZ-20260923-942 (a single test said to detect every off-critical
   zero); the printed errors recorded in the Enriques commentary; the counterexamples in the Montpellier research
   notes (MPL_142 N008.3, MPL_146 R005 and R104, MPL_147 N007, and the others of that kind). The same steps as in 1.
3. For each item, whether it is worth a short note of its own (a result a reader in the field would want to know), and
   why.

**What not to do.** Do not rewrite the lessons or the notes. Do not count anything as new because you could not find
it in one search: say what you searched. Do not call a result proved because the lesson says so: say what you checked.

**Output.**
- `SECOND_PASS.jsonl` and `SECOND_PASS.csv` in the schema of `RESULTS_SCHEMA_v1.md`: one record per item, the source's
  claim in `status_claimed` and `claimed_by`, your own check as one entry in `checks` (checker "GPT-6 Astra (ChatGPT Pro
  mode)", scope `proof_followed`, `computation_reproduced` or `literature_checked` as the case is, your verdict and the
  references), `novelty` as `potentially_new` or `known`, never "new".
- `SECOND_PASS_SUMMARY.md`: the items worth a note first, each in five lines (what it says, what it goes beyond, why it
  matters, what you checked, what is left), then the known ones with their references, then the wrong ones with the
  error, then the counts.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution environment, once every hour of work, each under a new name, `SECOND_PASS_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held. Save checkpoints once an hour and at no other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost.

**The whole task is every candidate row and every named repository item, each given the steps above.** Work through
them in order and deliver when all are done.
