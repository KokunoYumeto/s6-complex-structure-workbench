# How the S6 papers are laid out: a reference that a reader with little time can use (design, 17 Nov 2026)

Draft by the main session (Claude Opus 5.5 at effort max), 17 Nov 2026 ~11:3x UTC, from the user's words of the same
morning (quoted in section 1). It is the layout part of the next S6 revision run (S6_10), which also folds in the
results of S6_06_BLIND once its final is in. It is a long-paper variant of the Hexagon post format
(`recent_results_20261114/HEXAGON_POST_FORMAT_20261114.md`), whose binding rule (every finding with its full proof,
every proof checked, checked and unchecked apart) stays as it is.

## 1. What the user asked for

- "there shouldn't be any proofs that aren't in the papers. But that doesn't mean the paper has to be just a ream of
  like consecutive dense proofs."
- "It should be organized in a way where somebody looking for a particular result can just like very easily find
  that. Somebody needs to be very much aware of what the paper in total shows. It should just be very clearly
  internally linked."
- "It should read as sort of like a reference where the paper part is probably the first few dozen ... pages ... And
  then that sort of links forward to like all the dense proofs ... almost like a gazette to the paper before the paper.
  But like thinking about humans who have limited time trying to get the results they care about or the gist of the
  global shape of the results."
- "maybe there's a way to visualize things that is actually helpful. If there is, that's worth considering."

## 2. How the three papers are laid out now (S6_09_PAPERS final, 17 Nov 06:01 UTC)

| Paper | Pages | Results | Front matter | Then |
|---|---|---|---|---|
| I | 530 | 348 | 2 pages: one paragraph of statements with cross-references, the status table, the known-and-new table | sections 2-23 (pp. 3-300) with statements and proofs interleaved; appendices A-S (more proofs, the 46-page concordance R, programs S); open points T-U |
| II | 659 | 313 | 2 pages, the same three parts | sections 1-17 (pp. 3-545), appendices A-D (re-derivations, more proofs, the 38-page concordance, programs) |
| III | 1,004 | 523 | 2 pages, the same three parts | sections 1-9 (pp. 3-458), appendices A-AL (pp. 459-990: the classical topology re-derived, the 59-page concordance, programs) |

There is no index of results or notation, and no figures. The cross-references are dense (2,214, 3,336 and 3,898
`\cref`-type references), so the linking material exists; what is missing is a way in.

## 3. The layout of each paper

In this order, under fixed headings (the same in all three papers, so a reader who has used one finds everything in
the next):

**0. The gazette (2-4 pages).**
- *What this paper shows*: one paragraph on the global shape, in the terms of the field.
- *Results at a glance*: a table, one row per main result: number, the result in one line, its status (proved here;
  known and re-derived, with the source; refuted; computed with certificate; open), and a link to the full statement
  in part 1 and to the complete proof in part 2.
- *The series*: the three papers in five lines each, with links to their gazettes, so that any one paper places the
  other two.
- *The result map* (figure 1, section 5).
- *How to read this paper*: three routes in three lines: the results only (part 0); the paper (part 1); the full
  check (the order of part 2).

**1. The paper (about 20-40 pages).** The main theorems, each stated completely (it stands alone: all hypotheses
inside, every symbol defined or cited by number), with its context: what it answers, what it rests on, what it is
used for. After each theorem: the idea of its proof in a few sentences, the hard step named, and the forward link to
the complete proof. The credit for each result (the known-and-new table) and its literature status go here, beside the
result, not in a separate list. The figures that explain the objects (section 5) go here. A reader who stops after
part 1 knows every main result, its status, where its proof is and why it holds.

**2. The reference: every result with its complete proof.** Grouped by topic in the order of part 1, with no proof
left out and none shortened. Each result is one uniform block:
- the statement (the same text as in part 1 for the main results);
- *Status*: the check record in one line (who checked, how, model with effort, date), as in the inventory;
- *Uses*: the results and external sources its proof uses, as links;
- *Used by*: the results whose proofs use it, as links (generated from the references, not written by hand);
- *Back to*: a link to its row in the gazette or its place in part 1;
- the complete proof, in numbered steps where it is longer than about eight lines.

**3. Machine material.** Programs, certificates and commands, each with the statement it serves, attached and pinned.

**4. Open questions.** As now, with the precise missing steps.

**5. Records.** The verification record, the result concordance (source id to printed number), provenance,
declarations, references.

**6. Indexes.** An index of results by topic and by number, and an index of notation (symbol, meaning, where
defined). Every entry is a link.

PDF bookmarks follow parts 0-6, so the side panel of any PDF viewer is a working table of contents.

## 4. What does not change

- Every proof stays in the papers; nothing goes to a repository.
- Every proof is checked, with the record (the binding rule of the format; AGENTS.md).
- Checked and unchecked findings stay in separate parts.
- The statement numbers of the checked text stay, or the concordance maps old to new.
- Credit stays as decided: the construction is [AC26]'s (Claude and Alpöge) and Engel's. The 2Z classification is
  credited to DGKX v1, with the line "our public working edition had the full proof by 8 Sep 2026".

## 5. Figures that help (and only those)

A figure goes in if it lets a reader find a result faster, or see an object that the text otherwise makes them
reconstruct. Each is drawn from data the papers already contain, so it can be checked. Candidates, in order of
expected use:

1. **The result map** (every paper; figure 1 of the gazette). The main results as nodes, an arrow where a proof uses
   another result, across all three papers. Colour by paper; marked by status (proved, known and re-derived,
   refuted, open). Each node is a link. Built from the papers' own references, so it is exact. The full graph of about
   900 statements is unreadable: the map shows the main results and the statements they rest on, two levels deep, and
   the reference part keeps the full Uses and Used-by lists.
2. **The parameter disc** (Paper I). The disc 0 < |w| < 216, with:
   - the puncture w = 0, where no filling exists, and the natural boundary |w| = 216;
   - the order-three and order-four base points, and the maximum of the norm;
   - the eleven rational CM fibres and the other special fibres;
   - the real structures' fixed loci;
   - the identification c ~ c + 2.

   It is the picture behind Paper I's title.
3. **The Θ₇ classes** (Paper III). Z/28 as a circle with each sphere family's class marked. The (3,4) family and every
   X₃ₖ,₄ₗ family sit at 0. Once S6_06_BLIND is folded in, the circle also shows OS47 at 24, OS45 at 25 (a generator,
   with its covers reaching every class) and the flop families at 15, 2, 17, 14 and 20. The table beside it gives each
   family's construction and its proof.
4. **The construction** (Paper I, part 1). The torus-fibred picture of X_c: the base with its multiple fibres of
   multiplicity 3 and 4 and the cusp, the vanishing circles, and the page surface with its section.
5. **The fundamental domain of the monodromy group** (Paper I): the index-twelve kernel, with its cusps, in the upper
   half-plane.
6. **The CDP endpoint** (Paper II): the exact sequence with the torsion term the published endpoint argument omits,
   as a commutative diagram (TikZ), in part 1.

Figures 1-3 are navigation and global shape; 4-6 are understanding. All are TikZ in the TeX source, or a PDF with the
script and data that drew it in the machine material, pinned.

**The same toolkit as the Longue Marche Plates of 16 Nov** (`math_viz_20261116/`; artifact "Longue Marche Plates",
https://claude.ai/artifact/8C6EBhQf2dyQ8NUoMF9Qm5). One colour language across all figures (`tools/palette.json`:
here one colour per paper and one mark per status). Graphviz, three.js and Blender are set up and tested there. Beside
the static figures in the PDFs, an interactive companion page, "S6 Plates", would serve the user's main point,
finding a result quickly:
- the result map with a search box. Each node shows its statement and status and opens the PDF at the page of its
  proof; the page numbers come from the papers' .aux files, so the links stay exact;
- the parameter disc, where a click on a special fibre shows its data and its proof;
- the Θ₇ circle, where a click on a family shows its construction, its class and its proof.

The page is built from the inventory and the .aux files by script and rebuilt after every revision, so it never drifts
from the papers.

## 6. How it gets made

- **One revision run** of GPT-6 Astra (ChatGPT Pro mode), after S6_06_BLIND's final is in, doing two jobs:
  1. fold the night run's results into the papers, each with its full checked proof;
  2. lay the papers out as above.
  - It is one cluster, so one prompt ([[parsimonious-pro-slots]]). It is dense, so it counts as two slots on account 1
    or 3.
- **What we prepare first, by script, as inputs to that run:**
  - the Uses and Used-by lists of every result, from the TeX references;
  - the data of the result map, and a first drawing of it to test whether it is readable;
  - the results index from the inventory.
- **Our checks after the run:**
  - the two linters on the prompt before it goes;
  - after the return: the PDF check (overfull boxes, rendered pages looked at);
  - a script check that every result of the old inventory is still there with its proof;
  - the S6 intake.
