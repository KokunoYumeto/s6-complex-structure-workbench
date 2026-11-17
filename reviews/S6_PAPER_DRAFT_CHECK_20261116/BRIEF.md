# Brief: draft check of the S6 paper. Claude (Fable 5.2 at effort high), agent a3da11221b89f2996, 16 Nov 2026

From the main session, Claude (Opus 5.5 at effort max). The user approved this check at 17:5x UTC. You are a copy of
the S6 intake agent, rolled back to the state after the 15 Nov checkpoint intakes. Since that state, all four S6
finals came in. Their intake is in `reviews/S6_FINAL_INTAKE_20261116/INTAKE_FINAL.md`, the S6_01 intake in
`INTAKE_S6_01.md`, and the decision in `DECISION.md`, all in that folder. Read DECISION.md first. It holds the
conditions the paper had to meet.

**The paper.** `returns/S6_07_PAPER_final_20261116T1537Z_unzipped/`:
- `S6_07_PAPER_paper.tex`, 144 pages and 592 KB. Do not read it whole; see the method below.
- `S6_07_PAPER_source_table.csv`, 145 rows, with the columns paper_label, statement_as_printed, status, source_run,
  source_id, source_file, wording_vs_source, found_in_AC26, found_in_E26, found_in_DGKX_v1, credited_to, checks.
- `S6_07_PAPER_report.md` and `records/`.

It was written by GPT-6 Astra (ChatGPT Pro mode) from the six S6 returns in `returns/`, under the binding conditions of
`s6_pro_prompts_20261112/ALREADY_RAN/S6_07_PAPER/PROMPT.md`.

**The task.** Find every place where the paper departs from its sources or from the conditions. Work in this order.
1. **Mechanical first.** With a Python script (run it with `python -I -B`, from your own folder), take each row of
   the source table, open its source_file, find source_id, and diff the printed statement against the source
   statement, normalising whitespace and macros. List every row whose hypotheses, conclusion or constants differ. Do
   not read the CSV or the TeX whole.
2. **Judge only what was flagged.** For each flagged row, decide: harmless rewording, notation (the paper uses the
   first run's conventions), or a change of content (strengthened, weakened, dropped hypothesis, wrong constant).
3. **Read these in full:**
   - the front matter and §0 (status, credit, the prescribed Campana-Demailly-Peternell paragraph);
   - §2a (the 2Z theorem as K, with the workbench-independence wording);
   - Appendix A;
   - the Limits part.
4. **Check the status labels against DECISION.md:** B.4.33 an announcement; Theta_7; E.2.24; section 5 from
   INTAKE_S6_01; Engel's Conjecture 8.2 as a counterexample.
5. **Credit.** DGKX v1 credited for 2Z, h^q(T) and Aut; Engel [E26]; Alpöge [AC26]; CDP; no claim of priority. Flag,
   but do not change, anything that bears on precedence: the user is still to supply the date the 2Z file entered the
   public Overleaf edition.
6. **Proofs.** Sample the 80 proof environments. Check that each sampled proof is the source's proof, with no new
   argument, and report any gap you see.

**Deliverable.** `DRAFT_CHECK.md` in this folder:
- counts;
- a table of discrepancies (paper label, location, kind, severity, proposed fix);
- the credit findings;
- a verdict: postable as is, postable after the listed fixes, or not postable.

Keep your scripts in `scripts/` here.

**Bounds.** Your context is about 686k. Stop and write by about 880k, and in any case before 920k. Use no other
agents. Read no files of the user's outside the S6 folders. Report in three or four lines when done.
