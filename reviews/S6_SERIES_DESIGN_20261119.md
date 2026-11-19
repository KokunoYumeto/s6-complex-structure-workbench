# The S6 series: a design built from what works (19 Nov 2026)

Written by Claude Opus 5.5 at effort max (agent a1704602), 19 Nov 2026, about 19:30 UTC, at the main session's request.
It follows `S6_PUBLICATION_READINESS_20261119.md` and `S6_PAPER_V_DEPOSIT_PREP_20261119.md` (beside this file).

## 0. The goal, as given

- **Get the point at once.** A busy expert gets the point at once and goes deeper only where they want, with as little
  effort as possible.
- **Not wrong.** The results must not be wrong. Humans will have less time to referee AI-produced mathematics, so the
  checking falls to us.
- **One work.** The series is one coherent work on one topic.

The user's own picture is a hypothesis, not a specification:
- layers in depth, "in waves";
- a methodology note;
- PDF links from the outline of an argument to its full proof;
- one paper per topic;
- a count of three checks, since withdrawn: checked to confidence.

The method below is designed from the evidence (section 1). Section 2 says where it agrees with the user's picture and
where it does not.

## 1. What the evidence says

### 1.1 How experts read

- **Reading for ideas.** Mathematicians read published proofs mainly for insight and methods, less to verify them.
  - Besides line-by-line reading, they read modularly. They "zoom out" to the high-level structure and the methods,
    then zoom in on the parts they doubt or need.
  - One interviewee describes understanding a proof as seeing how its lemmas fit together.
  - Source: Weber and Mejía-Ramos 2011, manuscript pp. 18, 24-25. A survey of 118 mathematicians (Mejía-Ramos and Weber
    2014) supports the reading for insight; I read only its abstract.
- **Scanning for theorems.** Readers scan papers for the statements of theorems. They decide from those whether to read
  on, so the results belong up front, stated prominently.
  - Source: Herbert Wilf's guest lecture in Knuth, Larrabee and Roberts 1989 (class of 28 Oct, PDF pp. 61-62); same
    source, §1 rule 13 (prose should survive a reader who skims the formulas).
- **Milestones first.** Major steps should be stated early as self-contained propositions, so that the reader holds the
  plan before the details.
  - Peripheral material and heavy computation go to the back.
  - Never order a paper by the chronology of the work.
  - Source: Tao, "Organise the paper".
- **The audience.** It sets how much motivation, detail and repetition a text needs (Halmos 1970, read in Ewing's
  excerpt, 2007).

### 1.2 Proofs readable at the top level and at any depth

- **Hierarchical proofs.** Lamport's structured proofs number every step by level (⟨1⟩1, ⟨2⟩3, ...). Each step is a
  claim with its justification.
  - He recommends reading level by level: the high-level steps first, then their proofs.
  - On paper, the complete higher-level proof can be given first, followed by the lower levels.
  - In hypertext, the reader sees the statement, opens the top steps, and opens or hides any step's proof.
  - A short proof sketch may precede the proof at any level, so a reader can stop at the sketch.
  - For a journal, he would now publish the sketch and link to the full proof.
  - Sources: Lamport 1995, §4.3, pp. 10-11; 2012, §2, pp. 4-5; §4.4, pp. 14-15; p. 17.
- **The measured cost.** Leron (1983) proposed proofs by levels, main ideas at the top. The one controlled comparison I
  found (Fuller et al. 2011, students) reports a trade-off:
  - readers of structured proofs could better state the key ideas;
  - but they did slightly worse on other comprehension measures;
  - the format separates claims from their supporting evidence.

  I read this in a secondary account (van Bommel 2018, pp. 12-13), not the original. The lesson for us: every claim,
  at every level, keeps its reason beside it, and the levels are not scattered.
- **Experts and length.** Eye-tracking (Inglis and Alcock 2012) found that mathematicians, unlike students, check
  whether each line follows. Its proofs were too short to test how experts skim long works (abstract and secondary
  reports only).

### 1.3 Organizers, signalling, progressive disclosure

- **Advance organizers** help learning and retention modestly, across 135 studies (Luiten, Ames and Ackerson 1980;
  abstract only).
- **Signalling** (headings, previews, highlighting) improves comprehension and transfer with small-to-medium effects:
  d = 0.38 in one meta-analysis, r = 0.17 in another (as reported; I did not open them).
- **Progressive disclosure** shows the few most important items first and the rest on request (Nielsen 2006). It works
  under two conditions:
  - the split between first and second layer must be right;
  - the way to the second layer must be obvious.

What these support is a first layer that is the real structure of the work, with a clear and consistent path down. A
generic summary does not do that job.

### 1.4 Navigating very long works and series

- **Stable tags.** The Stacks project gives every result a permanent four-character tag. A tag never changes when the
  text is renumbered or moved, and a removed result keeps its tag with the reason. Citations link to the tag's page.
- **Blueprints.** A Lean blueprint (Massot) records, in each statement, which other results its proof uses (`\uses`),
  its formal status (`\lean`, `\leanok`), and builds the dependency graph from that. The graph's colours show what is
  stated, proved or formalized.
- **Both serve the reader who needs one fact,** and the checker. They are a navigation layer, not the reading path.

### 1.5 What catches errors

- **Writing every step out.** Writing a proof hierarchically, justifying every step, catches errors that prose hides.
  - Rewriting conventional proofs in this form, Lamport and Abadi found serious mistakes in almost every one, though
    the theorems were true.
  - Most errors come from not carrying a proof down to enough levels (Lamport 1995, §4.1-4.2, pp. 8-10; 2012, §3,
    p. 6).
- **Errors are common.** Published estimates put logical errors in about half of published proofs, though most
  theorems are true (Davis 1972 and Hanna 1991, cited in Weber and Mejía-Ramos 2011, p. 24).
- **Global errors.** Tao separates them from local ones. A global error is one where the argument proves too much or
  contradicts a known example. It can be found by looking at the large-scale structure, and it is often the most
  serious kind. Local errors need line-by-line reading.
- **Repetition is not independence.** Twenty-seven independently written programs from one specification failed
  together far more often than independence predicts (Knight and Leveson 1986; abstract and secondary reports). Checks
  by the same method, or by the same kind of checker, miss the same things.
- **Our own record (S6):**
  - The substantive errors were caught by:
    - computation against a formula (the all-fan polynomial failed on two fans);
    - tracking a convention (the sign of the physical line);
    - comparing statements with their summaries and sources (the lost gcd hypothesis, the missing reference-fan
      scope, misplaced credit).
  - The second-family checks of 19 Nov confirmed the sign convention, and the cause of the old ×(−5).
  - The renewed re-derivations of already-checked rows by the same model family, 75 rows on 19 Nov, found no new
    mathematical fault.

## 2. The user's picture against the evidence

| The user's guess | What the evidence says | Design |
|---|---|---|
| Layers in depth, sequential as one scrolls; the first layer primes the mind | Supported: Lamport (level by level; layered presentation on paper), Tao (milestones first), organizers, signalling, disclosure | Kept |
| A reader of one result reads its shape, clicks through to its proof, and leaves | Supported (Lamport's hypertext reading; modular reading). The cost found by Fuller et al. comes from separating claims from their reasons. | Kept, with the condition that every claim at every level carries its reason in a line, so the reader never has to jump to learn why a step holds |
| The first layer as the shape of the argument | Supported if it is the actual proof at a coarse grain, not a summary: a summary gives claims without reasons. The organizer literature points the same way. | Layer 1 is a proof (3-7 steps per main result); layer 0 states each result with its one mechanism |
| One clear paper per topic; the series is one thing | Supported: each topic has one place to look, and the series is marked as one work (Stacks- and blueprint-style tags and graph across it) | Five papers instead of six (section 3.6) |
| A brief methodology note in the introduction | No reading research on this. It is what the AI-authorship labels and the user's goal need. | One page, linking the records |
| Three checks per result | Confidence comes from agreement of different methods aimed where errors occur. Repeating one method adds little (Knight and Leveson; our 75 rows). | No count: a confidence programme (section 4) |

## 3. The design

### 3.1 The series marking

- **Series title:** *The (3,4,∞) family of complex six-spheres*. Each paper is "*... I: periods, moduli and the two
  ends*", "*... II: ...*", with the same title block and a running header "S6 · II".
- **Numbering:**
  - Inside a paper, statements are numbered by section (Theorem 7.4).
  - Across the series, a statement is cited as II.7.4. Main theorems are lettered (Theorem A, B, ...) and cited across
    the series as II.A.
- **Tags:** every statement has a permanent four-character tag, unique across the series and printed in its header. A
  tags file on GitHub maps each tag to its paper, number, page, label, status and checks. Renumbering never breaks a
  citation.
- **The series in each paper:** one paragraph and one table at the start of §1, written once and used in every paper.
  - The table gives the five papers, the main result of each in one line, and which papers each one uses.
  - Paper I's §1 carries the whole series at layer 0. It already has this as its first rung (I.1).
  - There is no separate overview document.

### 3.2 What each paper's first ~20 pages hold, in order

1. **The title block, then the abstract.** The abstract states the main theorems in words, under 250 words.
2. **The table of contents.** It is standard and hyperlinked. None of the cp15 papers has one, and papers I and III have
   no abstract.
3. **§1 Results and their proofs in outline.** This is the first layer, about 8-20 pages.
   - **1.1 The series and this paper:** the paragraph and table of 3.1.
   - **1.2 Main theorems,** at most about seven per paper.
     - Each is stated in full, its hypotheses included, with its one mechanism in a sentence (layer 0).
     - Each carries its literature status: new; corrects [X, Thm n, p.]; or known, credited, re-derived.
     - The cp15 openings have 77 rung-0 blocks (I 25, II 15, III 10, IV 19, V 5, VI 3). They are grouped into main
       theorems. The rest become "further results" in one table: the result in a line, its number and a link.
   - **1.3 The proofs in outline** (layer 1). For each main theorem, 3-7 numbered steps, each a precise claim with its
     reason in a line and a link to where the step is proved.
     - Each step says exactly what its expansion proves and nothing more (Lamport's discipline). The cp15 rung-1 blocks
       are the material.
   - **1.4 Known and new:** one table that cites prior results with exact locators.
   - **1.5 Methodology,** about one page (3.5).
   - **1.6 How the paper is organized:** one paragraph and the dependency figure of the main theorems.
4. **The body, by the mathematics,** layers 2 and below. Each statement block holds:
   - its header (number, tag, status in one word, and a "checks" link);
   - a "uses" line and a "proves step k of Theorem B" back-link;
   - the statement;
   - the proof in numbered steps (Lamport's numbering wherever a proof is long), each step a claim with its reason.

   The verbose check records of cp15 leave the body.
5. **Results not yet established,** in their own final part: the open rows, each with what is proved and the gap.
6. **References.** Every entry verified, only cited entries.

### 3.3 The proof format

- **Main theorems:** layer 0 (statement and mechanism) and layer 1 (3-7 steps with reasons) in §1. Layer 2 (each
  step's own proof as steps) and the full detail are in the body.
- **Every step of every layer is a claim with its reason.** No bare claims. This keeps the advantage of structure and
  avoids the cost that the structured-proof study found.
- **Long proofs** use numbered levels (⟨1⟩1 ... with ⟨2⟩ sub-steps), and an optional one-paragraph sketch before the
  steps (Lamport 2012, §4.4).
- **Every proof is in the paper;** that is what the paper is. GitHub holds the provenance: the runs, their checkpoints,
  and the check records, linked from the methodology section and from each statement.
- **Computations:** a computational step is part of its proof. The paper states the method, the inputs and the results.
  The program and its certificate are attached to the deposit as machine material, pinned to the same commit.

### 3.4 The link layer

| From | To | Mechanism |
|---|---|---|
| Table of contents, PDF outline | sections, main theorems, the final part | hyperref and bookmarks |
| A main theorem in §1.2 | its outline proof in §1.3 and its full statement in the body | internal link |
| A layer-1 step | the body statement that proves it, "(proved in Prop. 7.4, p. 213)" | internal link to the tag's destination |
| A body statement | back to the step it proves, "proves step 3 of Theorem B (p. 6)"; and its uses and used-by lists | generated from the `\uses` lines |
| The end of each proof | back to §1 | internal link |
| A citation of another paper, "Theorem II.7.4" | that statement in the other paper's PDF | `#nameddest=tag-XXXX` on the pinned GitHub PDF, with `#page=N` as fallback; relative links for a downloaded set |
| A statement's "checks" link | its entry in the paper's check file on GitHub | anchor by tag |
| The methodology section | the run, CHECK_EVENTS, the intakes, the tags file, the S6_09 text | pinned URLs |

Every statement carries `\hypertarget{tag-XXXX}`, so links survive repagination. A web blueprint (dependency graph,
coloured by status) is generated from the same `\uses` lines and published beside the PDFs.

### 3.5 The methodology section (one page)

- **Who did what,** each model with its effort and dates:
  - GPT-5.6 Sol in Codex at reasoning effort ultra: the working edition of 24 Aug - 9 Sep 2026;
  - GPT-6 Astra (ChatGPT Pro mode): the research runs of 12-16 Nov, the independent night run of 16-18 Nov, and the
    writing runs of 16-19 Nov;
  - Claude Fable 5.2 at effort high and at effort max, and Claude Opus 5.5 at effort max: the reviews, intakes, sweeps
    and second-family checks of 12-19 Nov.
- **How they worked together,** in three sentences: prompts, returns, intakes, corrections back into the next prompt.
- **How the results were checked to confidence.** The kinds of check, with counts, and the rule of section 4.
- **One line** that no human has checked the mathematics.
- **CC0.**
- **The links.** Nothing else about process is in the paper.

### 3.6 Is the six-paper split right? Not quite.

- **The sign theorem is in two papers.** Paper II proves it for irreducible and normal-crossings fibres. Paper VI proves
  it for every degeneration, citing II 145 times. That is one topic in two places. **Merge VI into II** as its second
  part. The reader of "the sign theorem" then has one paper, with the general case after the special one.
- **Two complex fourfolds sit in two papers.** III §6 has the fibre-product fourfold; V has the one on
  3HP²#(−HP²), and V imports III Thm 6.2-6.3. **Move III §6 into V**, which becomes "complex fourfolds from the
  family". III keeps maps and manifolds, V loses its main import, and each topic has one place.
- **I (the family), III (maps and manifolds) and IV (smooth monodromy in Θ₇)** are distinct topics on one object, and
  stay separate. IV is long (1,507 pp.) because of its source families. A third of it is the final part of results not
  yet established. Its §1 carries the reader regardless.
- **Result: five papers.**

  | Paper | Topic | Pages at cp15 |
  |---|---|---|
  | I | the family: periods, moduli, the two ends | 475 |
  | II | torus-fibred threefolds, the argument of Campana-Demailly-Peternell, and the sign theorem | 471 + 415 from VI |
  | III | maps from the six-spheres and the manifolds they give | 409 less §6 |
  | IV | smooth monodromy in Θ₇ | 1,507 |
  | V | complex fourfolds | 173 + III §6 |

## 4. Checked to confidence

**The goal.** Every printed result is checked until we are confident it is right. How confidence is reached, and how
it is shown, follows from section 1.5:
- **Different methods,** aimed where errors occur. Re-running one method is not the route.
- **A different family for the global check.** The main results, and the results they rest on, get a global check by a
  checker of another model family. It reads the layer-1 proof against the body: does each step follow, does the
  argument prove too much, does it respect the scopes and conventions, does it agree with known special cases.
- **Computations by independent code.**
- **The literature status of every result, checked and cited.**
- **Targeted checks of the error-prone points:**
  - conventions and signs;
  - scopes and hypotheses;
  - constants;
  - long chains;
  - corrections of published work;
  - results that one run alone produced.
- **Formal proof** where a central statement is small enough to make it cheap.
- **Shown** in each paper's check file on GitHub. Each main result gets a line listing the independent routes that
  agree, and any risk that remains, with links. The methodology section gives the totals.

**What remains at cp15:**

| Work | Scope |
|---|---|
| A global check by another model family | about 125 of the 167 main rows have been read only by GPT-6 Astra sessions (II, III, IV, VI almost entirely) |
| Independent computation | the main computational claims not yet recomputed with new code (fresh code exists for 96 rows); mostly IV and I's arithmetic |
| Literature status | about 30 night-run main results (I, II, III, IV) |
| Error-prone points | IV's 35 correction rows; VI's chain C.2.UN.1-86; the Liu-Rollenske correction; D.2.5's scope; IV P3K.7-8 wording |
| Cross-paper imports | about 121 sites (`S6_PAPER_V_DEPOSIT_PREP_20261119.md`, §3) |
| The run's renewed same-family re-derivations (1,014 rows) | not a route to confidence in themselves; used where a row's only check is its producer |

**Route.**
- **Claude Opus 5.5 at effort max:** the global checks, one agent per topic, five agents of about 100-150k tokens each.
  Claude Fable 5.2 at effort max could do some of them with the user's OK.
- **GPT-6 Astra (ChatGPT Pro mode), in parallel as the user suggested on 18 Nov:** four prompts on two accounts, each
  about 6-10 hours:
  - IV: corrections, computations, literature;
  - II with VI: the chain, Liu-Rollenske, D.2.5, literature;
  - I with III: computations, literature;
  - the cross-paper imports.
- **No money.**
- **Placement:** before each paper's deposit (deposits are permanent). A paper is deposited when its main results and
  the points its readers rely on are at confidence. The checks of its supporting rows continue on GitHub.

## 5. The route to the reshaped series

| Step | How | Who | Cost |
|---|---|---|---|
| Tags, tags file, uses and used-by, back-links, cross-paper references with named destinations, stripped status headers, PDF outline, dependency figure, check files from CHECK_EVENTS and the intakes, consistency rerun, PDF check | scripts | Claude Opus 5.5 at effort max | about 200k tokens for the series; the V scripts (`S6_PAPER_V_DEPOSIT_20261119/`) carry over |
| The merges (VI into II; III §6 into V) and the reordering of each body by the mathematics | scripts for the moves, a model for the joins | GPT-6 Astra (ChatGPT Pro mode): one prompt each for II and V | 2 slots, about 4-6 h each |
| The fronts (abstract, §1.1-1.6) of the five papers, from the 77 rung-0 and their rung-1 blocks | a model writes | GPT-6 Astra (ChatGPT Pro mode): one prompt for all five, so the series reads as one | 1 slot, about 6-10 h |
| The check that every front says exactly what its body proves | a reading | Claude Opus 5.5 at effort max, within the global checks of section 4 | included |
| The confidence programme | section 4 | Claude and Pro | section 4 |

Order of work:
1. Freeze cp15 and run the scripts.
2. In parallel: the confidence programme, and the Pro prompts for the merges and the fronts.
3. Claude's front-against-body reading.
4. The PDF check.
5. Per paper, the user's yes and the deposit.

**Order of deposits.**
- **Paper V first.** It is the smallest and the nearest to confidence: its credit is done, and 5 of its main results have
  been read by another family. After the merge it imports only I Thm 17.4 (P2.4), which must be at confidence first.
- **Then I** (cited by every paper), II, III, and IV last.
- One deposit per UTC day.
- Each cites the others at the frozen, commit-pinned version.

**The decision for the user:**
- whether to merge (VI into II; III §6 into V);
- and V or I first. My recommendation is V, once I Thm 17.4 is at confidence.

## Sources

**Read for this design** (locators as above; quotations kept to a phrase, the rest in my words):
- L. Lamport, "How to Write a Proof", *Amer. Math. Monthly* 102 (1995). Version read: lamport.azurewebsites.net/pubs/lamport-how-to-write.pdf, §§1, 4.1-4.3.
- L. Lamport, "How to Write a 21st Century Proof", *J. Fixed Point Theory Appl.* 11 (2012). Version read: lamport.azurewebsites.net/pubs/proof.pdf, §§2, 3, 4.4 and the reply to the referee.
- K. Weber, J. P. Mejía-Ramos, "Why and how mathematicians read proofs: an exploratory study", *Educ. Stud. Math.* 76 (2011) 329-344. Author's manuscript: sites.math.rutgers.edu/~jpmejia/files/Weber_Mejia_(2011ESM).pdf, pp. 18, 24-25.
- D. E. Knuth, T. Larrabee, P. M. Roberts, *Mathematical Writing*, MAA Notes 14 (1989); jmlr.csail.mit.edu/reviewing-papers/knuth_mathematical_writing.pdf, §1 (rule 13), and H. Wilf's lecture (class of 28 Oct, PDF pp. 61-62).
- P. Halmos, "How to write mathematics", *Enseign. Math.* 16 (1970) 123-152. Read in J. Ewing, "Paul Halmos: In His Own Words", *Notices AMS* 54(9) (2007), p. 1136 ff.; the original's e-periodica copy is behind a verification page.
- T. Tao, "Organise the paper" and the index "Advice on writing papers" (terrytao.wordpress.com/advice-on-writing-papers/). Also "On 'local' and 'global' errors in mathematical papers, and how to detect them", read through a mirror.
- P. Massot, leanblueprint, README (github.com/PatrickMassot/leanblueprint).
- The Stacks project, "Tags" (stacks.math.columbia.edu/tags).
- J. Nielsen, "Progressive Disclosure", Nielsen Norman Group, 3 Dec 2006.
- C. M. van Bommel, "Mathematical Proofs 101" (arXiv:1806.06892), pp. 12-13: the account of Fuller et al. 2011.

**Abstract or secondary report only** (not opened in full; claims marked as such above):
- E. Fuller et al., "Comprehending Leron's structured proofs", RUME Proceedings 14 (2011) 84-102; and Fuller et al., "Comprehending structured proofs" (2014). The journal copy refused connection.
- U. Leron, "Structuring mathematical proofs", *Amer. Math. Monthly* 90 (1983) 174-185.
- M. Inglis, L. Alcock, "Expert and novice approaches to reading mathematical proofs", *JRME* 43 (2012) 358-390.
- J. P. Mejía-Ramos, K. Weber, survey of 118 mathematicians, *Educ. Stud. Math.* 85 (2014) 161-173.
- J. Luiten, W. Ames, G. Ackerson, *Amer. Educ. Res. J.* 17 (1980) 211-218.
- The signalling meta-analyses (Alpizar, Adesope and Wong 2020; Richter, Scheiter and Eitel 2016; Schneider et al. 2018).
- J. C. Knight, N. G. Leveson, *IEEE Trans. Softw. Eng.* SE-12 (1986) 96-109.

**Not consulted:** J.-P. Serre's talk "How to write mathematics badly". I found no text copy within the bound; the
design rests on the sources above.

**Our records:**
- the S6_10_PAPERS cp15 return (openings, CHECK_EVENTS, gate tables);
- sweep 1's CORRECTIONS.md;
- the cp36 intake;
- `S6_PAPER_V_DEPOSIT_PREP_20261119.md`.
