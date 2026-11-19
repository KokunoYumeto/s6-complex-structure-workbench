# S6 series consistency, Paper V deposit preparation, and the plan in the new format (19 Nov 2026)

Written by Claude Opus 5.5 at effort max (agent a1704602), 19 Nov 2026, about 18:30 UTC. It follows
`S6_PUBLICATION_READINESS_20261119.md` (beside this file).
- **Corrections of that file** (section 1) come from two coordinator messages and the user's six remarks of about
  17:1x UTC, which the main session relayed.
- **Working folder:** `s6_pro_prompts_20261112_work/S6_PAPER_V_DEPOSIT_20261119/`. It holds the scripts and outputs
  named below, and the Paper V copy with its build.
- **Nothing was deposited.**

## 0. In short

- **The series is consistent at checkpoint 15.** All 436 cross-paper citations resolve to the statement intended, in
  the cited paper's current numbering (about 121 distinct statements).
  - Every imported statement is proved, except one: Paper IV cites Paper II's printed refutation of P3K.36, as a
    refutation.
  - No later result refutes an imported statement: not S6_06_BLIND cp36, not the 16 corrections of sweep 1, and none
    of the intakes.
  - The scope that later corrections require is printed in every class-0 theorem of Paper IV. The exception is the
    wording of night:P3K.7 and P3K.8, where the scope comes only from their section.
- **The papers cite each other in cycles** (II↔IV, II↔VI, III↔IV, IV↔V), so no posting order avoids citing an
  unposted paper.
  - **What protects a posted paper** is citing the others at one frozen, public version: cp15, pinned to a commit.
  - **Paper I imports nothing** and can be posted without this risk. **Paper V** imports only III Thm 6.2-6.3 and
    I Thm 17.4, all proved and untouched by later results, so it can be posted with pinned links.
- **What a series-wide consistency reading would take:** one Pro prompt (GPT-6 Astra, ChatGPT Pro mode), about 3-6
  hours on one slot at flat cost. It checks that each of the about 121 imports is used within its hypotheses and
  conventions. A Claude Opus 5.5 at effort max scripted pass, about 100k tokens, then freezes the version.
- **The plan is changed to the user's format.**
  - The deposit is the paper itself: an abstract with the main results, a short methodology section with links to the
    run and the check records on GitHub, then the results with their proofs and literature status.
  - There is no separate note.
  - Check lines and workflow text leave the body.
  - There is no renewed-checks bar.
- **What remains of S6_10** (ended at cp15) for publication:
  - the literature status of about 30 night-run main results;
  - the wording of IV P3K.7-P3K.8;
  - a second reading of the Liu-Rollenske correction before Paper II is posted.

  The rest is further results.

## 1. Corrections of the readiness file

- **No renewed-checks bar** (the coordinator, ~16:5x UTC, and the user, ~17:1x UTC). The three checks per proof were
  item 10 of the S6_10 prompt, built from a suggestion the user made about how to check. They are not a publication
  rule. What holds is AGENTS.md: every printed proof checked by a qualifying check and recorded (the writing run
  counts), and checked and unchecked parts kept apart.
  - So the renewed-check counts and their 90-250 hours are withdrawn as blockers.
  - So are the 39 rows "with no independent check": the writing run's check qualifies.
  - The list stays as information. For the Liu-Rollenske correction (II) a second reading is still advised, because it
    corrects a published paper.
- **One proof per statement was not a problem.** I checked by script: Paper V has 79 statement blocks, each with one
  proof; across the six papers, 11 blocks contain more than one proof environment.
  - The former routes the run says it preserves are not printed as second proofs. My readiness file's claim to the
    contrary is withdrawn.
- **No separate Hexagon note per paper.** The deposit is the paper; the Hexagon form fields are filled per paper.
- **"No human has checked the mathematics"** need not be repeated: Hexagon's AI-author label carries it. One line in
  the methodology section is enough.
- **S6_10 ended at cp15** (10:45 UTC), the newest checkpoint on disk.

## 2. Step 2: the check files on GitHub

- **Already public** (housekeeper map `github_housekeeping_20261114/NOTES_ON_GITHUB_20261119.md`):
  - sweep 1, all seven files, in grothendieck-montpellier-archive `raw/results_register/sweep1_s6/`;
  - the cp36 intake and its CHECK_EVENTS, in s6-complex-structure-workbench `reviews/`.
- **Published now,** in one commit, s6-complex-structure-workbench `4e8b5478` (committer KokunoYumeto noreply; scrubbed
  like the housekeeper's notes):
  - `reviews/INTAKE_S6_06_BLIND_cp36_scripts/` (the 5 scripts and their outputs);
  - `reviews/S6_10_REVISION/S6_CHECK_LEDGER.tsv`, `S6_CHECK_LEDGER_SUMMARY.md` and `KEEP_SKETCH_20261117.md` (one
    quotation of the user's words omitted).

  Each path was checked on `main`.
- **Not done:** S6_06_BLIND cp36 itself (533.9 MB). It goes to the -data repository through the filer
  (`file_and_push_auto.py`), not through the contents API.

## 3. The series-consistency check

### 3.1 Method

Three scripts in the working folder: `series_consistency.py` (with `.out` and `.json`), `scope_check.py` and
`old_values.py`.

**What a paper takes from the others:**
- every printed `\ExternalPaperRef{kind}{number}{paper}` of the six cp15 papers;
- each paper's own source files, for the label each citation was made from.

**Whether the cited paper still states it:**
- **For II and V,** which were rebuilt at cp15 after the papers citing them were assembled: the printed numbers
  against the current `.aux`.
- **For I, III, IV and VI:** against the statement headers ("Theorem 6.2 ... Label: maps:src:E.1.2") in the cp15 PDFs.
  The six cases the parser could not settle I resolved by hand.

**Later results:**
- every imported statement against sweep 1's CORRECTIONS.md (16 items), MERGES.tsv (refuted by, settled by, refines,
  stronger) and FLAG_VERDICTS.tsv;
- S6_06_BLIND cp36 through the cp36 intake;
- the class-0 statements against sweep 1's correction 2 (the reference-fan scope).

**Notation:**
- the series notation sheet;
- where the superseded values (the polynomial KL(S−1)(S−3)/8, OS45 = 25) and the dual "meridian-one" line still occur,
  by section and by the status of the statement around them.

### 3.2 What each paper takes from the others

| From → to | Printed citations | Distinct statements | Status in the source paper | Number matches |
|---|---:|---:|---|---|
| II → I | 43 | 15 | all proved | yes (B.4.4 = I Prop 15.17, by hand) |
| II → IV | 13 | 6 | proved (corrected items P3K.35, P3K.36; P3F.41, P3F.47; P3K.73, P3K.74) | yes |
| II → VI | 8 | 2 | proved (C.2.G.1, C2a) | yes |
| III → I | 47 | 16 | proved | yes (mapsI:src:A.1.2 = I Prop 22.2) |
| III → II | 7 | 3 | proved (push:src:E.5.1-E.5.3 = II 12.22-12.24) | yes (aux) |
| III → IV | 4 | 2 | proved (iv:correction:P3K.6; maps:src:B.6.24) | yes |
| IV → I | 94 | 29 | proved | yes (push:src:A.1.1 = I Prop 14.1) |
| IV → II | 7 | 1 | night:P3K.36, false as stated, cited as its refutation (II Correction 16.2) | yes (aux) |
| IV → III | 51 | 10 | proved | yes (night:P3F.26 = III Thm 5.1) |
| IV → V | 1 | 1 | proved (night:P1.11 = V 4.7) | yes (aux) |
| V → I | 1 | 1 | proved (night:P2.4 = I Thm 17.4, p. 275) | yes |
| V → III | 13 | 2 + 3 equations | proved (maps:src:E.1.2 = III Thm 6.2, p. 244; E.1.3 = III Thm 6.3, p. 246; equations E.4, E.5, E.9) | yes |
| V → VI | 2 | 2 | proved (cdp:st:C2a, C2c = VI Prop 4.1, 4.3, pp. 143, 145); a comparison, not a use | yes |
| VI → II | 145 | 28 | proved (the C.3, A.5, D.1 and P4 rows) | yes (aux: every printed number is the current number of an intended label) |

- **Paper I cites no other paper.**
- **No numbering drift:** II and V were rebuilt after the papers that cite them, but their numbering did not move.

### 3.3 Later results against the imports

**S6_06_BLIND cp36 (the physical-line corrigendum).**
- It changes only the classes off the reference fan in Θ₇. Those live in Paper IV.
- The imports of IV statements (II → IV, III → IV) are the corrected items, with the corrected values (T₂ class 26 for
  Liu-Rollenske).
- The cp36 intake found no conflict, and the second-model check confirmed the sign convention (M, normalized by
  P3F.22).

**Sweep 1 corrections touching imported statements:**
- **2, the reference-fan scope.** It is printed in IV's class-0 statements: C.3.24, C.3.27, C.4.1, B.6.2, B.6.21, B.6.24
  and B.6.25 each begin "Retain the reference cusp fan ...".
  - night:P3K.7 and P3K.8 ("The original return also has index zero ...") lack the words. Their section, "The page and
    the reference return", supplies the scope. One line each fixes it.
  - push:src:E.1.3 (I) claims no zero class, only invariance under the twist identification, so it needs no scope.
- **9, the corner coefficient −pn.** It is carried: I's rung 0 for the no-filling theorem states −pn, and IV cites
  P2.1, P2.2, P2.7 and B.4.33 from I.
- **11, the fibre-product fourfold is the small resolution.** III names the crepant small resolution (its rung 0, III.10),
  and V imports exactly E.1.2 and E.1.3 (the index-one Kuhn cusp, Euler number 6). Sweep 1 also checked by computation
  that the cusp carries χ = 6 (P1.11 against S6_04 E.1.3: agrees).
- **1, the gcd(n,3k) hypothesis of D.2.11.** III prints P3F.33-34 as its extension (rung 0, III.8). IV cites those rows.
- **The merges** among imported statements are refinements and strengthenings, for example PUSH E.1.2 refines FAMILY
  B.3.1, and P2.9 is stronger than PUSH B.4.33. A paper that cites the weaker true statement stays correct.

**The intakes.**
- The S6_09 intake recommended a second reading of P2.4-P2.9 against I Thm 21.58. That covers V's import of I Thm 17.4
  (P2.4). It is a recommendation, not a recorded doubt.

**V's imports, as checked:**
- III E.1.2: S6_09 and S6_10;
- III E.1.3: S6_09, S6_10, and a sweep-1 computation by Claude Opus 5.5 at effort max;
- I P2.4: the night run and S6_10.

None is touched by a later result.

### 3.4 Notation and conventions

- **The series notation sheet** (`S6_10_PAPERS_notation_sheet.md`) opens with the series-wide transports:
  - the two Weierstrass models and their lattice map;
  - the physical line M against the meridian line M⁻¹ (circle weight −1);
  - the corrected physical index A_M = H/2 − χ;
  - ℍ for the upper half-plane;
  - w = exp(−πic), u = w² and q₂ = iw/216.
- **The superseded values** occur only in IV and II:
  - in the statements printed false as stated;
  - in the corrections;
  - in IV's opening, which names the old polynomial as false;
  - in explanatory text of proved statements.

  No paper uses them as current.
- **The dual line** ("meridian-one") is named 3 times in III's OS49 section and 90 times in IV, always as a named
  convention. Sweep 1's correction 3 asks each row to state its line. I did not check each statement's own convention
  line; the consistency reading of 3.5 would.
- **Paper V uses its own notation** for its family (the rank-six torus family, the half-plane in ξ). Its contact with the
  series is the fibre-product fourfold and the Kuhn cusp of III §6, cited by number.

### 3.5 Verdict

- **Can be posted now without the cross-paper risk:**
  - **Paper I.** It imports nothing.
  - **Paper V,** provided it cites III and I at the pinned cp15 version. Its imports are proved, consistent, and
    untouched by later results.
- **The others import from papers not yet posted, and the citations form cycles.** Posting order cannot remove the
  risk. Freezing the series at one version and citing that version can.
- **The series-wide consistency pass before the first deposit:**
  1. **A reading of the about 121 import sites.** For each: the citing passage, the cited statement with its hypotheses
     and convention, and a verdict on whether the use is within them. Route: one Pro prompt (GPT-6 Astra, ChatGPT Pro
     mode) with the six cp15 TeX files and a site list built by `series_consistency.py`; about 3-6 hours, one slot,
     flat cost.
     - Alternative: Claude Opus 5.5 at effort max in two bounded agents, about 300-400k tokens.
  2. **The scripted pass.** Fix the wording of IV P3K.7-P3K.8, freeze the version (one commit), and rerun the three
     scripts on it. Route: Claude Opus 5.5 at effort max, about 100k tokens.
- **With Paper I or V first,** the deposit can go before the reading finishes. The reading then covers the next papers.

## 4. The Paper V copy (kept; to be reshaped to the new format)

`S6_PAPER_V_DEPOSIT_20261119/S6_10_PAPERS_V_deposit.tex`, built by `build_deposit_copy.py`. Its PDF and log are in
`build/`.
- **The check records are rebuilt.** Each of the 79 statements carries one line per check: who (model and effort), the
  date, what was done, and a commit-pinned link to its public record.
  - 414 lines in all; the run's bookkeeping entries are left out.
  - The two Claude computations of the cp06 intake are added (P1A.2, P1A.3).
  - The night run's own derivation of the fourfold's diffeomorphism type is added to F.4.1 (P1.6, P1.14). P5.7 belongs
    to Paper I and is not added.
  - **In the new format these lines leave the body.** They become a public check file for Paper V, which the
    methodology section links (`records.tsv` holds the per-statement summary).
- **Cross-references are linked.** Paper III Thm 6.2 (p. 244) and 6.3 (p. 246), Paper I Thm 17.4 (p. 275), Paper VI
  Prop 4.1 (p. 143) and 4.3 (p. 145), and S6_09 Paper III A.9 (p. 466) link to the public PDFs at a pinned commit, with
  the page. Each Paper I, III and VI target page was opened by script, and its statement matches; the S6_09 page comes
  from S6_09's public `.aux`.
- **One proof per statement:** already true in V.
- **The PDF check** (LuaLaTeX, 3 passes, 183 pages):
  - 0 errors, 0 undefined references, 0 missing characters, 0 font warnings and 0 overfull boxes;
  - measured on the PDF, nothing extends past the right margin by more than 2.9pt (the bibliography); elsewhere 2.1pt
    is character protrusion;
  - no page has an overflow over 10pt.
  - Pages 1, 54, 57, 63, 92 and 182 are rendered in `build/`. Page 57 (Thm 6.2 = F.4.1 with its new record) was looked
    at: it is clean, apart from two doubled punctuation marks that come from the run's event texts.
  - The local MiKTeX lacks `aliascnt`, and its package manager does not run. The build used a local stand-in
    (`build/aliascnt.sty`, two commands). The deposit uses the standard package.

## 5. The plan in the new format

**The deposit is the paper.** For each paper:
- **Title and abstract.** The abstract states the main results.
- **A short methodology section:**
  - how the results were produced (models with effort and dates);
  - how they were checked: the kinds of check and how many of each, with links to the run's CHECK_EVENTS, the intakes
    and the paper's check file on GitHub;
  - one line that no human has checked the mathematics.
- **The results, as a mathematician reads them:** statement, proof, and literature status (known: cited with its
  locator; or new).
  - The opening's rungs 0-1 stay.
  - Check records leave the body: the statement block keeps label and status.
  - Unchecked and open results stay in their separate final part.
- **Hexagon form fields,** filled per paper for the user's yes: title, abstract, the AI-author label, CC0, the tools
  (models with effort), and human understanding.

**What remains of S6_10 (ended at cp15), for publication:**
1. **The literature status of the night-run main results** still "pending":
   - I: P2.2, P2.7, P2.9;
   - II: P4.58;
   - III: P3F.34;
   - IV: P3F.21, P3F.35, P3K.99-P3K.108 and the refuted historicals.

   Route: one Claude Opus 5.5 at effort max agent with web search, about 150k tokens, or the Pro reading of 3.5.
   Paper V needs none: its credit checks are done.
2. **The wording of IV P3K.7-P3K.8** (the reference fan). Route: the scripted pass.
3. **A second reading of the Liu-Rollenske correction** (II ii:LR:covering and the P3K.36 correction) before Paper II is
   posted. Route: Claude Opus 5.5 at effort max, about 100k tokens.
4. **The bibliography as shipped:** the cited entries only. The .bib carries 32 entries marked unverified or pending;
   none of them is cited in any of the six papers (checked by script).
5. **Not needed** (further results): P3K.75, P3K.109-P3K.119, inv:C3.8, inv:E2.3, maps:src:D.2.4, and the hypothesis H
   of C.7.4. Also not needed: the run's renewed three checks.

**Order of work** (no money, no API):
1. Freeze the series at cp15 plus the scripted fixes, pinned to one commit (Claude, about 100k tokens).
2. Reshape Paper V or Paper I into the format above. The scripts carry over: move records out, write the methodology
   section and the literature-status line per statement, and build the check file (Claude, about 150k tokens per
   paper).
3. The Pro consistency reading of the import sites (3.5), in parallel.
4. Then the user's yes, and one deposit per UTC day.
5. The remaining papers follow in the order their items above close: II after the Liu-Rollenske reading, then VI, III
   and IV.

**What the first deposit needs from the user:**
- the choice of Paper V or Paper I first;
- a look at the reshaped PDF and the form answers;
- a yes for the deposit (Hexagon, under the user's account; deposits are permanent).
