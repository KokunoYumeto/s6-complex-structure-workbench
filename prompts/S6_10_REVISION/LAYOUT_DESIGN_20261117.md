# The S6 papers as a usable reference: design, version 3 (17 Nov 2026)

Main session (Claude Opus 5.5 at effort max), 17 Nov 2026 ~11:4x UTC. History:
- Version 1 (`LAYOUT_DESIGN_v1_REJECTED_20261117.md`) restated the user's remarks as a specification and was rejected.
- Version 2 (`LAYOUT_DESIGN_v2_20261117.md`) was my own design. The user found two faults in it:
  - an opening list of results with no reasons repels a mathematician, whose mind looks for why each claim holds;
  - a list of the results is a table of contents, not a way in.
- The user's goal: a reader with little attention to spare (the normal reader now, given how much mathematics AI
  produces) gets, wherever they stop, the results at the depth they have reached, with the reasons at that depth.

This version is built on that goal. The binding rule stays: every finding with its complete proof, every proof
checked, checked and unchecked apart.

## 1. The problem

The writing run (S6_09_PAPERS) produced 2,193 pages (I 530, II 659, III 1,004; 1,184 inventory rows).
- After a two-page front, statements and proofs run interleaved.
- Six kinds of material are mixed in one stream:
  - our new results;
  - known results re-derived;
  - classical background re-proved in full (Paper III, pp. 495-891);
  - second proofs;
  - history;
  - apparatus.
- The order follows how the material was produced more than the mathematics.

There is no way in short of reading. Nor would a summary fix that: a summary gives claims without reasons, and a list
of claims is a table of contents.

## 2. The principle: proofs as a ladder, complete at every rung

A proof can be written at several resolutions, each one a complete argument at its own grain. This is Leslie
Lamport's hierarchically structured proof ("How to Write a Proof", 1995; "How to Write a 21st Century Proof", 2012):
- the proof of a theorem is a short sequence of steps, each a precise claim with the reasons it follows;
- each step has its own proof, again a short sequence of steps, down to the details;
- a reader may stop at any level and holds a complete argument at that level;
- going one level down never contradicts the level above. It only fills a step in.

This is what the goal asks for:
- **every unit carries its own reason**: no claim appears without the why at the current depth;
- **each rung is a small, digestible load**: a theorem with three to seven steps, each a line or two;
- **stopping anywhere leaves a whole result**: the results and why they hold, at that depth;
- **depth is on demand**: the reader descends only into the steps they care about.

The ladder has rungs, and each has a fixed job:

| Rung | What the reader has after it | Size |
|---|---|---|
| 0 | the main result and the one mechanism that makes it true, in a sentence or two | a few lines per result |
| 1 | the proof as three to seven steps, each a precise claim with its reason in a line | under a page per result |
| 2 | each step's own proof as steps, with every external result named | a few pages per result |
| 3+ | the full proof, with every computation and citation (the existing 2,193 pages are mostly here) | as long as it is |

Rung 0 is not a bare claim: it carries its mechanism (for example, "no filling at w = 0, because the corner's gamma
winding is nonzero while a filling would force it to vanish"). Rung 1 is already a proof, just a coarse one.

## 3. The papers, built on the ladder

**The opening of each paper is rungs 0 and 1 of its main results**, in an order that tells the story: the object,
what we determine about it, and what follows. Each result's rung-1 steps link down to rung 2.
- A reader who stops after the opening (roughly 10-25 pages for a paper of this size) has every main result with a
  coarse but complete proof.
- A reader who follows one step down gets that step's argument, and so on.

**The body is rungs 2 and below, arranged by the mathematics.** Chapters follow the objects: the family, its
periods, its moduli, its ends, its cohomology, its deformations. Each statement block holds, in this order:
- its tag;
- its typed status (proved here, known and re-derived, refuted, computed with certificate, conditional, open);
- its check record in one line: who, how, model and effort, date;
- what it uses and what uses it;
- the statement;
- the proof, written as numbered steps that link up to the step they prove and down to their own expansions.

**Where everything else goes:**

A paper is for our new results. What is known is cited, not proved again.

| Kind | Place |
|---|---|
| Our new results | proved in full: rungs 0-1 in the opening, rungs 2 and below in the body |
| Known results ([AC26], Engel, DGKX, CDP and the rest) | cited with exact locators (statement and page). Our own re-derivation is kept only where it confirms a recent unrefereed result that a main result rests on (DGKX v1's classification, [AC26]'s computations), as a short credited remark or appendix. |
| Classical background (Morse theory, handle moves, Whitney moves, the Adams spectral sequence, the course CG-S6) | cited from the literature with locators; not re-proved; no background volume. A short proof is given only where we use a classical result in a form its sources do not state. |
| Second proofs | the body, after the primary proof, as "independent second proof"; part of the check record |
| History | provenance records, not the papers |
| Apparatus | the records part of each paper, and the machine-readable JSON |

Measured on the S6_09 inventory by script (kind, source and credit columns; a first pass for the intake to refine):

| Kind | Rows | By paper (I / II / III) | Share of the statement text |
|---|---|---|---|
| Our results | 852 | 313 / 295 / 244 | 45 % |
| Known results | 67 | 23 / 18 / 26 | 2 % |
| Classical and course material | 265 | 12 / 0 / 253 | 53 % |

Paper III's appendices G-AI (pp. 495-891) are mostly this classical material. Cited instead of re-proved, Paper III
loses most of its length. The re-derivations are not lost. The full S6_09 text is published beside the papers as the
**proof compendium**, a supplementary file of the deposit, tag-linked to the papers. A reader who wants the classical
steps or every computation follows a citation or a tag into it. It is the verification asset, not the main text.

**The series.** The three papers share one object, and III and II rest on I. So Paper I's opening starts with a rung 0
for the whole series: the family, and the main result of each paper with its mechanism. It is not a separate overview
paper. Each paper's opening points to that rung for the others.

## 4. Stable tags and the lookup tools

These serve the specialist who needs one fact, and the checker. They are not the first reading.
- **Tags:** every statement gets a permanent four-character tag, as in the Stacks Project and Kerodon. It is
  independent of the printed number and never changes, so references, check records, Hexagon posts and later papers
  survive the S6_10 renumbering.
- **The web blueprint,** after Patrick Massot's leanblueprint (used by the PFR and FLT projects). The dependency graph
  of all statements, coloured by status and searchable. Each node shows the statement and its rung-1 proof and opens
  the full proof. The edges come from the proofs' own references, so the graph is exact.
- **The JSON record:** tags, statements, status, checks, dependencies, credits and source ids, for AI readers and for
  our later prompts.

## 5. Figures

A figure goes where the geometry carries the reason, as a rung in its own right:
- **the (3,4,∞) base orbifold** with the fibres over it: rung 0 of the construction;
- **the parameter disc** 0 < |w| < 216, with the puncture, the natural boundary, the special fibres and the real loci:
  rung 0 of the moduli and the ends;
- **the fundamental domain** of the index-twelve monodromy kernel.

The Θ₇ results go in a table (family, construction, class, the classes its covers reach), because the content is
tabular. The tools of the 16 Nov session (`math_viz_20261116/`) serve the web blueprint.

## 6. How it gets made, and how the ladder is kept honest

1. **By script, no model:** classify every statement by kind (first pass above; the S6 intake refines it); assign the
   tags; extract what each statement uses; build the graph, the web blueprint and the JSON. A retention check confirms
   that every one of our results and its proof appears in the new layout, identical up to labels. For every known or
   classical statement dropped, the check confirms that each place that used it now cites a source with a locator.
2. **By one GPT-6 Astra (ChatGPT Pro mode) run, after S6_06_BLIND's final:**
   - fold in the night run's results, each with its full checked proof;
   - write rungs 0-2 of every main result, and arrange the body by the mathematics on the script's skeleton.
3. **The danger of a ladder is an upper rung that says more than the rungs below prove.** Two rules prevent it:
   - each step of a rung is a precise claim, and the rung below proves exactly that claim (Lamport's discipline);
   - the check of a paper includes, for every main result, a reading that every rung-1 step is the statement proved by
     its rung-2 expansion.

   The S6 intake agent and our own script check both look for this.
