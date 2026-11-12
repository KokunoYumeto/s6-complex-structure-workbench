# Common brief for the S6 workbench survey (12 Nov 2026)

You are one of several readers working in parallel on a survey. Model: Claude Fable 5.2, effort high (the
user's choice for this survey). Read this whole file, then your own assignment.

## What the survey is for

The user wants a list of what is worth checking in the S6 work: the complex-structure construction on S^6 and
everything that grew from it. Most of the later work was done by GPT-5.6 Sol in Codex over about two weeks
(late Aug - early Oct 2026), following up the original manuscript produced by Claude (Fable 5) under Levent
Alpöge and rechecking its mathematics. The user expects that it contains findings nobody has picked out yet.

Count everything that adds mathematics, even a little:
- new results (theorems, classifications, computations, counterexamples);
- corrections of the original manuscript or of the literature;
- refinements, sharpenings or generalizations of statements or proofs of the original manuscript;
- new ways of stating or proving known results;
- well-posed open questions that the work isolates.

This is a survey to find candidates, not a verification. Read each part carefully enough to decide whether it
is worth a full check: neither skim nor verify everything in depth. A short sanity check (a small hand or
script calculation, a dimension count, a comparison of two formulas) is welcome when it is cheap. Be plain
about uncertainty. Do not call a result new unless you looked for it in the literature; do not call it proved
unless you read the proof and saw no gap. Say "the workbench says VERIFIED" when that is all you know.

## Facts after your training cutoff (June 2026) that you must take as given

- July-Aug 2026: Levent Alpöge circulated a 108-page manuscript produced by Claude, "The (3,4,infinity) modular
  family of 2-tori, completed at its three special points, is a complex structure on S6" (https://alpo.ge/s6.pdf),
  cited as [AC26]. It constructs a compact complex threefold X with a holomorphic map f: X -> P^1, fibres complex
  2-tori over P^1 minus {0,1,infinity}, multiple fibres of multiplicity 3 and 4 over 0 and 1 (reductions
  bielliptic surfaces S_1, S_2), and over infinity a non-normal normal-crossings fibre W (a degree-6 del Pezzo
  surface with opposite sides of its hexagon glued). Main Theorem of [AC26]: (1) the fibre description;
  (2) pi_1(X) = Z/|12 l_0 - 4 l_1 - 3 l_2| = 1 and H_*(X;Z) = H_*(S^6;Z), so X is diffeomorphic to S^6;
  (3) a(X) = 1, M(X) = f^*C(t); (4) K_X = f^*O(-1) (x) O(2 S_2), not torsion; c_3 = 2; Aut^0(X) = C^* with fixed
  locus one double curve of W. Further in [AC26]: Pic(X) = C; h^{0,q} = (1,1,0,0), h^{p,0} = 0 (p>0), the
  Frölicher spectral sequence does not degenerate at E_1 (Prop. 9.13, 9.20, Cor. 9.22; Remark 9.21 lists
  "expected values" for the rest); R^2 f_*(T_X (x) L) != 0 for every line bundle L (Thm 10.5); Prop. 10.8
  (a line bundle non-torsion on every fibre); section 10 locates where Campana-Demailly-Peternell fails.
- 13/29 Sep 2026: Philip Engel, "Complex structures on S6", arXiv:2609.38442, cited as [E26]: an independent
  self-contained proof by a geometric route (rational elliptic surface with fibres IV*, III, I_1; principal
  C^*-bundle of O(P-O); quotient by a lift of translation by 6P; Mumford filling at infinity; logarithmic
  transforms of multiplicity 3, 4). One-parameter family X(u, a_0, a_1), u in a small punctured disc. Engel
  omits the CDP discussion and the Dolbeault computations. His section 8 lists remarks and open directions:
  8.1 the family really deforms (sketch only) and Conjecture 8.2 on a flat proper filling at u = 0;
  8.3 a quotient map S^6 -> S^3 by the invariant rank-3 subtorus (Seifert picture); 8.4 the invariant class of
  type (1,6), Hodge form of signature (1,1), Klingler's question whether the monodromy group acts properly
  discontinuously on the period domain; 8.5 generalizations (other elliptic surfaces; a conifold transition).
  Full text: C:\Users\user\Documents\workbench_review_20261112\literature\engel_S6.txt (read it; 25 pages).
- So: S^6 has complex structures, and the theorem of Campana-Demailly-Peternell that such a structure has
  algebraic dimension 0 (CDP98 Cor. 4.2; CDP20 Thm 2.2, Cor. 2.3) is false. Do not treat these as doubtful.
  Older workbench files (before about 5 Oct 2026) are worded cautiously ("claimed", "candidate", "does not
  certify the global S6 construction"); that caution was about the state of checking then, not about the result.
- Many other problems were resolved in 2026. Before judging novelty of anything outside S6 geometry, look at
  C:\Users\user\Documents\recent_results_20261110\SCOREBOARD.md (never open proof_packs\ or .lean files there).

## The baseline to compare against

- The original manuscript, transcribed: C:\Users\user\Documents\math\research\s6_recent_results_main\canonical_S6_snapshot\original_clean_transcription.tex
  (5,700 long lines; grep for "Theorem 9.1", "Proposition 9.13", "Theorem 10.5" and so on; line 60-330 holds the
  two summary pages with the Setup and the Main Theorem). main.tex in the same folder is the annotated edition.
- Engel's paper (above).
- For each candidate, say what it adds over [AC26] (is the statement there? weaker? proved differently?), over
  [E26], and over the general literature. For your best candidates (interest 4-5) do a literature check with
  WebSearch / WebFetch (load them with ToolSearch "select:WebSearch,WebFetch"); use primary sources (arXiv and
  other freely accessible copies). Never put the user's name, the repository name or project names in a query
  or URL. Say what you searched and what you found; "not searched" is an acceptable entry for minor items.

## Where things are (read only; change nothing there)

- Local Codex workspace (primary, most up to date on S6): C:\Users\user\Documents\math\research\s6_recent_results_main\
  - canonical_S6_snapshot\ : the S6 project as of early Sep 2026. workbench.tex is the root of the cumulative
    workbench (782 pages); its inputs are in supporting_materials\workbench\research\*.tex; ledgers in
    supporting_materials\workbench\research\ledgers\ (claim_ledger.txt, morphism_ledger.txt, uncertainties.txt,
    next_lemmas.tex, research_log.tex); result map in research\mathematical_summary.tex and research\status.tex.
    An index of the claim ledger (id | status | kind | statement) is at
    C:\Users\user\Documents\workbench_review_20261112\work\claim_ledger_index.txt.
  - courses\CG-S6\ : a later course (to 8 Oct 2026) that reproves the construction lesson by lesson; src\*.md.
  - mathematical_consolidation\, related_sources\, ledgers\, source_dialogues\, source_text_blobs\.
- The public repository, cloned (secondary, later, recontextualized): C:\Users\user\Documents\workbench_review_20261112\repo\
  (s6\ and yang-mills\continuations\20260930-s6-ns-moment-map-bridge\ are the S6-related parts).

Depth (the user's instruction): a medium-deep reading of the local workspace, and only a light reading of the
repository (enough to see what it adds or changes on S6). Medium-deep means: read every statement and its
status; read the proofs of the statements that could be candidates closely enough to see their structure, their
inputs and their weak points; pass quickly over routine verification, conventions, build records and provenance.

Rules: read only in both places. No git commands in either place. Write only inside
C:\Users\user\Documents\workbench_review_20261112\work\ (your notes file, and scratch scripts under
work\scratch\<your id>\ if you need them). Do not start other agents. Do not open large .gz/.sqlite dumps unless
your assignment says so. If a file is very long, read it in parts, but read all of it unless told otherwise.
On Windows; use the Read/Grep/Glob tools or Git Bash; python is available (run it with -I).

## What to write

Write one file: C:\Users\user\Documents\workbench_review_20261112\work\<YOUR_ID>_notes.md (UTF-8), with:

### 1. Reading notes
For each file you read: path, size, date if visible, what it contains (sections, the main labelled statements
with their labels, the status marks the workbench gives them), and how it relates to other files (duplicates,
"preprint" views of the same source, superseded versions). A later checker must be able to find things from this.

### 2. Candidates
One entry per candidate, numbered <YOUR_ID>-1, <YOUR_ID>-2, ... Each entry has exactly these fields:
- **Title** (one line) and **Type**: new result / correction of [AC26] / correction of the literature /
  refinement of [AC26] / new proof or restatement of a known result / computation / open question isolated /
  expository only.
- **Where**: file, label or section, line range; date.
- **Statement**: the precise statement, with its formulas and hypotheses (copy the mathematics, do not paraphrase
  it into vagueness).
- **Support**: what supports it (a written proof: how long, what it uses; a script or exact check; a ledger
  entry), and what the workbench itself says about its status.
- **What it adds**: over [AC26] (give the place in the original if there is one), over [E26], over the
  literature (what you searched, what you found, or "not searched").
- **First assessment**: how solid it looks, the gaps or risks you see, any sanity check you did and its result.
- **A full check must establish**: the list of things a checker at effort max would have to verify.
- **Deserves a full check**: yes / maybe / no, with one sentence of reason; and **Interest**: 1-5
  (5 = would matter to specialists if correct; 1 = bookkeeping).
Include small items; give them short entries. Where many items are of one kind (for example ten convention
checks), one grouped entry is fine if it lists them.

### 3. Doubts and errors
Anything in the files that looks wrong, circular, overclaimed, or contradicted elsewhere, with locators.

### 4. Not read
Anything in your assignment you did not read, and why.

Your final message (it is read by the coordinator, not the user): at most 40 lines; the path of your notes file,
then your candidates in order of interest, one line each (id, statement in a few words, location, assessment,
full check yes/maybe/no).
