# The S6 papers as a usable reference: design, version 2 (17 Nov 2026)

My own design (main session, Claude Opus 5.5 at effort max), 17 Nov 2026 ~11:3x UTC. Version 1
(`LAYOUT_DESIGN_v1_REJECTED_20261117.md`) restated the user's remarks as a specification; the user rejected it in
full and asked me to think the question through myself. The one binding constraint I keep from our rules is that
every finding of ours appears with its complete proof, every proof is checked, and checked and unchecked findings are
kept apart.

## 1. What the three papers are now, and where the trouble lies

The writing run (S6_09_PAPERS) produced 2,193 pages: I 530, II 659, III 1,004, with 1,184 inventory rows. Each paper
has a two-page front and then statements and proofs interleaved. There is no index, no stable identifier scheme and
no dependency picture. The volume is not the real problem. The real problem is that six kinds of material are mixed in
one stream, and a reader cannot tell which kind a page is:

1. **Our new results**, the reason the papers exist.
2. **Known results re-derived**, credited: DGKX's classification, tangent cohomology and Aut = C*, and [AC26]'s
   construction data. They are valuable as independent confirmation, but they are not our claims.
3. **Classical background re-proved in full.**
   - Paper III's appendices G-AI rebuild Morse cancellation, Whitney moves, handle slides, the Adams spectral sequence
     and the integral stable group (pp. 495-891).
   - The inventory lists 155 rows of kind "classical proved construction" and 48 "classical worked example", plus
     238 rows the run added from our course and working edition.
4. **Second and third proofs** of one statement ("every distinct proof retained").
5. **History:** partial arguments of earlier runs, kept beside the later complete answers.
6. **Apparatus:** concordance tables (46, 38 and 59 pages), programs, verification records.

The sections are also ordered by how the material was produced more than by the mathematics, as their titles show:
"The alternate collapse and Mayer-Vietoris route", "Integral topology without the cusp-collapse argument".

## 2. Who reads it, and what each needs

- **A mathematician with ten minutes** (the most common reader of anything on S^6): what was found, how sure it is,
  and what is new against [AC26], Engel and DGKX.
- **A specialist who needs one fact,** such as the Hodge numbers, the Kuranishi germ, a Θ₇ class or the CDP repair:
  the exact statement with its hypotheses, its status, and a proof they can follow without reading everything before
  it.
- **A checker or referee:** every proof, in an order where each step's dependencies come first, and the record of who
  checked what.
- **An AI reader.** Hexagon expects to be read for training. It needs statements that stand alone, machine-readable
  status, and stable identifiers.

No single linear text serves all four. What serves them is one source with several views, which large proof projects
already use.

## 3. The design

### 3.1 Every piece of content gets one kind, and each kind one place

| Kind | Where it goes |
|---|---|
| New results | the papers: stated in Part A, proved in Part B |
| Known results re-derived | Part B, in a section "Known results, re-derived"; Part A cites them by source and tag |
| Classical background | one shared volume for the series, "Background, re-derived", which the papers cite by tag; where a textbook has the statement in the form we use, cite the textbook as well |
| Second proofs | Part B, right after the primary proof, headed "Independent second proof" (they are part of the check record) |
| History, partial arguments | provenance records, not the papers; a partial argument stays only where it is the only record of a partial result |
| Apparatus | Part C of each paper, and the machine-readable record |

This alone should bring each paper's own text down to its findings. My guess is a few hundred pages for III rather
than 1,004, but that is a guess until the split is counted.

### 3.2 Stable tags, as in the Stacks Project

Every statement gets a permanent tag (four characters, as in the Stacks Project and Kerodon) that never changes
across revisions, independent of its printed number. Cross-references, the inventory, check records, Hexagon posts
and later papers cite the tag. The revision that folds in S6_06_BLIND will renumber everything; with tags no reference
breaks. The concordance from run ids (B.4.33, F.2.39, ...) to tags is generated once and published.

This is the most important single decision. A reference work is citable and navigable because its identifiers are
stable.

### 3.3 The series: an overview paper and three papers

- **Paper 0, the overview** (about 20-30 pages; mine to propose, not yet asked for):
  - the family and its construction, with credit;
  - every main result of the series, stated exactly, with its status and tag;
  - for each result, the idea of its proof in a paragraph;
  - how the three papers depend on one another;
  - what is open.

  It is the series' front door, and the natural first Hexagon post.
- **Papers I, II and III,** each in three parts:
  - **A, the paper** (tens of pages): the new results of that paper with their context and proof ideas, written to
    be read;
  - **B, the reference:** every statement with its complete proof, ordered by the mathematics (object by object),
    in dependency order inside each chapter;
  - **C, the records:** verification, concordance, programs and provenance.

  One PDF per paper keeps findings and proofs together. Nothing points to a repository.
- **Background, re-derived:** one shared volume for the classical material, cited by tag.

### 3.4 Each statement is one uniform block, generated from one source

Each block holds:
- the tag and the printed number;
- the status, typed: proved here, known and re-derived, refuted, computed with certificate, conditional, open;
- the check record in one line: who, how, model and effort, date;
- *Uses* and *Used by*;
- the statement, standing alone;
- the proof, or the link to it.

The same block feeds the PDF, the web page and the published JSON, so the three cannot drift apart.

### 3.5 The one visualization I am sure helps: a blueprint dependency graph

Large collaborative proofs already solved this problem. The Lean blueprint (Patrick Massot's leanblueprint, used by
the PFR and FLT projects) shows the whole proof as a graph:
- nodes are statements, coloured by status;
- edges come from explicit "uses" annotations;
- a click shows the statement and opens its proof;
- the web version is searchable.

It works without Lean. Here the edges come from the proofs' own references, which the papers already have in the
thousands, so the graph is exact. It answers both "where is X proved and what does it rest on" and "what is the shape
of the whole". It belongs on the web, with a static overview figure in Paper 0. A full 1,000-node hairball would not
help, so the static figure shows the main results and two levels of dependencies.

### 3.6 Figures in the text: only where the geometry carries information

- **The base of the fibration:** the (3,4,∞) orbifold, with the multiple fibres of multiplicity 3 and 4, the cusp,
  and the singular fibres over it. This is what a reader needs to picture X_c.
- **The parameter disc** 0 < |w| < 216: the puncture with no filling, the natural boundary, the order-3 and order-4
  points, the norm's maximum, the CM fibres and the real loci.
- **The fundamental domain** of the index-twelve monodromy kernel.
- **The Θ₇ classes as a table, not a picture:** family, construction, class in Z/28, and the classes reached by its
  covers.

I would leave out decorative renderings, hairballs and anything that restates a table. The tools of the 16 Nov
visualization session (`math_viz_20261116/`: one colour language, Graphviz, three.js) fit the web blueprint.

### 3.7 Machine-readable record

Publish the inventory as JSON beside the PDFs: tags, statements, status, checks, dependencies, credits and source
ids. It is what an AI reader, or our own later prompts, should consume instead of scraping PDFs.

## 4. How it gets made

1. **By script, deterministic, no model.**
   - Classify every statement by kind (section 3.1) from the inventory's kind and source columns. The rows the script
     cannot decide go to a list for the writer.
   - Assign tags, and extract Uses and Used by from the references inside each proof.
   - Build the dependency graph, the web blueprint and the JSON record.
   - Split out the background volume.
   - **Check retention:** every statement and proof of S6_09 appears in the new layout, identical up to labels. A
     reorganization of 2,193 pages must not lose a line without a script noticing.
2. **By one GPT-6 Astra (ChatGPT Pro mode) run, after S6_06_BLIND's final.**
   - Fold in the night run's results (the Θ₇ classes of OS45, OS47 and the flop families; the noncoprime correction;
     the corner coefficient -pn; the CDP checks), each with its full checked proof.
   - Write Paper 0 and the three Part A's.
   - Order each Part B by the mathematics on the skeleton from step 1.
3. **Then our checks:** the retention script again, the PDF check, and the S6 intake agent's reading of Paper 0 and
   the Part A's against Part B.

## 5. What I would ask the user

1. **The shared background volume.** It keeps the run's checked re-derivations of classical topology, but separates
   them from our findings. The alternative is to drop them and cite textbooks.
   - My default: keep them as the volume.
2. **Paper 0.**
   - My default: write it, and post it on Hexagon first.
