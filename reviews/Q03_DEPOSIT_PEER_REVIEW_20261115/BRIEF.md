# Peer review of the Q03 Hexagon post — brief (15 Nov 2026, main session, Claude Opus 5.5 at effort max)

**Reviewer:** a new Claude Fable 5.2 agent at effort max. Independent by design: not the producer of the post (GPT-6 Astra,
ChatGPT Pro mode), not the October checkers (Claude Opus 5.5 at effort max), not the format designer (Claude Fable 5.2 at
effort high, which rewrote the step layouts of Lemmas 3.3 and 5.5 on 14 Nov).

**The user's word (P5265, 14 Nov 2026 23:20 UTC):** the Pro prompt for the Hexagon post folds in everything that was meant
for Fable; then "let Fable do a peer review, but not necessarily a full redo except for any particularly important parts
like that exponent or whatever. Maybe let it see if it independently derives that. But yeah, remember Fable is expensive."

## What is under review

The theorem: P_m | prec, p_j = 1 | C_max (unit-time jobs with an arbitrary precedence DAG on m identical machines, makespan)
is solvable in polynomial time for every fixed m >= 3, by a description-hierarchy dynamic program that generalizes the
OpenAI three-machine preprint (24 Sep 2026). The return of 15 Nov 2026 00:22 UTC (GPT-6 Astra, ChatGPT Pro mode; prompt
`anc/Q03_DEPOSIT_prompt.md`) is in

`C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns\Q03_DEPOSIT_20261115T0022Z_unzipped\`

- `Q03_DEPOSIT_post.tex` / `.pdf`: the post (the object of the review);
- `Q03_DEPOSIT_report.md` (148 KB): the run's audit; `Q03_DEPOSIT_results.csv` (47 rows: 45 proved as stated);
  `Q03_DEPOSIT_sources.md`, `Q03_DEPOSIT_literature.md`, `Q03_DEPOSIT_form_answers.md`; `code/`; `anc/`.

The run reports: no false step; global leaf budget 12m+25, relative-prefix budget 6m+16; padded exponent 60m^2+129m+1;
explicit-input exponent 60m^2+129m+2 (the earlier +8 was a sketch).

## Order of work (keep the derivation independent)

1. Read the post in full (TeX; the PDF where layout matters).
2. **Target A, the exponent.** From Section 9's algorithm and the bounds of Sections 2-8 as the post states them, derive
   yourself: the global leaf budget, the relative-prefix budget, the padded exponent and the explicit-input exponent, with
   the form of the coefficient. Write your derivation into the review file **before** you open Part A of
   `Q03_DEPOSIT_report.md`, `code/A_check_accounting.*` or `anc/ai-provenance/`. Then compare, and resolve every difference:
   which side is right, and where the other goes wrong.
3. **Target B, the rewritten layouts.** Lemma 3.3 and Lemma 5.5, step by step.
4. **Target C, the claims.** Abstract, Status table, verification record, declarations and the "not claimed" list claim only
   what the record holds; every model named with its effort; the source statements attributed to Jansen, drbh and the
   OpenAI preprint as the post gives them. Two facts the run did not have, for the framing:
   - our course's m-machine lessons (`every-fixed-number-of-machines`, `unit-jobs-on-m-machines`,
     `lists-and-boundaries-on-m-machines` in the course `three-machine-unit-job-scheduling`) were first public on
     **24 Oct 2026 at 10:14 UTC**: commit c08b1f74 of github.com/KokunoYumeto/open-math-courses-public (the return's row
     S-L says first publication was not established);
   - Jansen, arXiv:2611.09392v1, is dated **6 Nov 2026**; the return reports that it states the all-fixed-m exact algorithm
     with budgets 4m+5 and m+3 and a fixed-multitape bound O(L) + m^{O(m^2)} n^{12m^2+26m+2} log^3 n. Open its LaTeX source
     (https://arxiv.org/e-print/2611.09392) and check the statement the post attributes to it.
   Say how the post should state these dates: as facts with their evidence, no priority claim beyond the dated record.
5. **Not a full redo.** Sections 2-8 outside Lemmas 3.3 and 5.5 are read as far as Targets A-C need them, not re-proved line
   by line. A gap or an error found anywhere is a finding, with its location.

## Output

`PEER_REVIEW_Q03_20261115.md` in this folder:
- Target A: your budgets and exponents with the derivation; agree or differ, and the resolution;
- Target B and Target C: verdicts with locations;
- the required edits to the post (section or statement, the change);
- one paragraph: deposit-ready or not, and what must change first.

Do not edit the post. Sign as Claude Fable 5.2 at effort max.

**Sub-agents allowed: 0.** **Compute bound: 300k tokens.** No recursive search over big trees: name the folder; never Grep or
Glob from Documents. Do not stop for context; if your context starts with a summary you were compacted: reread this brief
and your review file, then go on.
