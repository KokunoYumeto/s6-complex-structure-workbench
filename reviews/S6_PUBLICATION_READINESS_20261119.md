# S6 papers: what must still be there before publication (19 Nov 2026)

Written by Claude Opus 5.5 at effort max (agent a1704602, started by the main session), 19 Nov 2026, finished at
about 16:45 UTC. The brief is `reviews/S6_PUBLICATION_READINESS_BRIEF_20261119.md`. I wrote no other file, so the
scripts I used are in my scratchpad only.

**What I read:**
- the brief, and the rules it names: AGENTS.md (paper and PDF rules) and the memory files paper-reports-all-findings,
  hexagon-outlet, publish-checked-new-results, check-rubric, checks-built-into-use and cite-results-by-statement;
- the S6_10_PAPERS prompt as sent (`sent_20261115/S6_10_PAPERS/PROMPT_FINISH_as_sent_20261119.md`);
- from the newest S6_10_PAPERS checkpoint (cp15, `returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z_unzipped/`):
  - the report's continuation sections;
  - the inventory, CHECK_EVENTS.tsv and the frozen gate tables of formal review 05, by script;
  - all 88 rung-0 blocks of the six openings, extracted by script;
  - the bibliography's verification marks;
- the intakes `INTAKE_S6_06_BLIND_cp36_20261119.md` (sections 1-7) and `S6_09_INTAKE_20261117/INTAKE_S6_09.md`
  (sections 1, 2 and 5);
- the S6_10 cp06 intake and its CHECK_EVENTS (`raw/intake/` in the GitHub clone);
- the public clone `github_backup_20261113/s6-complex-structure-workbench` (HEAD 2838f66b, the same as origin/main);
- the newest RUNBOOK lines.

**Pages:** I located every main label in the cp15 PDFs with PyMuPDF. The labels are printed in the PDFs, so "label,
p. N" is a locator a reader can search. Pages will move with later checkpoints.

**What I did not do:** read any proof, open any literature, or run the PDF check.

**Model names.** GPT-6 Astra (ChatGPT Pro mode) is the model of every S6 run, the S6_10 writing included. Claude
checks are named with their model and effort.

**Corrected the same day, about 18:30 UTC.** The corrections are in `S6_PAPER_V_DEPOSIT_PREP_20261119.md`, section 1,
beside this file. That file also holds the series-consistency verdict and the plan in the user's format.
- **Checks: the goal is confidence, not a count.** Revised again at about 19:30 UTC, on the user's word. Humans will
  have less time to referee AI-produced mathematics, so the checking falls to us. Every printed result is checked until
  we are confident it is right.
  - The number of renewed same-family checks is not the measure.
  - The confidence programme is in `S6_SERIES_DESIGN_20261119.md`, section 4: a global check by another model family,
    independent computation, literature status, and targeted checks of the error-prone points, before each deposit.
  - The 39 rows checked only by the writing run are among those error-prone points.
- **One proof per statement was not a problem:** Paper V prints one proof per statement.
- **No separate Hexagon note:** the deposit is the paper.
- **The run ended at cp15.**

Section 5 is corrected accordingly. The other sections keep their record of 16:45 UTC.

**Independent check,** in this file, means a recorded proof check, re-proof or new computation made by a session other
than the one that produced the proof. Which model family made it is not the test (check-rubric).

## 0. In short

The six papers are close to the publication rules already:
- every new result is printed with its proof;
- known results are cited;
- the open items are in separate parts;
- the statuses use the four allowed words;
- every printed proof has at least one recorded check.

**What blocks publication is not mathematics. It is these five things:**
1. **The run has not finished.** S6_10 is INCOMPLETE, and no checkpoint after cp15 (10:45 UTC) has been filed. cp16
   was due at 11:07 UTC.
   - The renewed "three checks" (item 10 of its prompt, the user's suggestion of 18 Nov) are done
     on 75 of 1,101 printed proofs.
   - At the observed pace of 4 to 11 rows an hour, the rest takes 90 to 250 hours.
2. **The check records are not yet fit to print or cite.**
   - They carry internal workflow text.
   - They link to no public record.
   - They omit the 22 Claude check events of the cp06 and cp36 intakes.
   - Four of the check files they rest on are not on GitHub.
3. **39 printed rows have no independent check.** 35 are in Paper IV: its corrected physical-line items, written and
   checked only by S6_10.
4. **The credit and literature check is pending on about 30 main rows,** all from the night run. Hexagon needs every
   posted result with its literature status, and a superseded result is not posted.
5. **No post exists.** The Hexagon note per paper (abstract, labels, known-and-new table, provenance), the user's yes
   and the one-deposit-a-day allowance are all still ahead.

**The shortest path:** Paper V on Hexagon (section 4).
- 16 of its 18 main results have all three renewed checks.
- All 18 have their credit check.
- None lacks an independent check.

## 1. The standard, and what counts as "must"

**Must (the rules):**
- every new result with its full proof in the paper;
- known results cited with exact locators, not re-proved;
- checked and unchecked results in separate parts, and a failed proof printed with its gap;
- every proof checked by a qualifying check, recorded with who, how, model, effort and date. The writing run's own
  check qualifies.
- every check a paper cites must be public on GitHub, with the statement and page;
- the PDF check: overfull boxes from the log (none beyond about 2pt) and rendered pages;
- for Hexagon:
  - our results only, under CC0;
  - honest labels and literature status, and no superseded result;
  - the user's yes for each deposit.

**Asked for on 18 Nov and owed:** the renewed three checks of every row (re-derive before reading, new code for every
computation, a fresh credit check).
- By the rules, one qualifying check per proof is enough, and every row has one except the 39 of section 2.3.
- My recommendation is to gate each deposit on two things:
  - the three checks of its main results and of the foundations they use (check-rubric: spend checks where most
    depends on them);
  - an independent check of its rows in section 2.3.

  The rest of the renewed checks then go on after the deposit, recorded on GitHub. This is a decision for the user
  (section 5).

**More results (not needed for publication):**
- closing the open rows: inv:C3.8, ari:C.7.4's hypothesis H, inv:E2.3, maps:src:D.2.4, night:P3K.75;
- accepting P3K.109-P3K.119;
- the odd-class observation of the cp36 intake;
- any further fans or families.

## 2. The state common to all six (cp15)

### 2.1 The run

- **Inventory:** 1,524 rows. Of these, 1,160 are printed (1,134 labels) and 364 are compendium-only, each with a
  reason.
- **Statuses:** 1,473 proved, 33 false as stated, 17 open, and one proved under hypotheses H (ari:C.7.4, as the cp06
  intake asked).
- **The renewed queue:** 1,101 printed proofs need it.
  - Done: 87 proof receipts, and 75 rows with all three gates.
  - Remaining: 1,014 (81 partial, 933 untouched).
  - Per paper at cp14: I 251, II 256, III 161, IV 225, V 33, VI 92.
- **Pages:** I 475, II 471, III 409, IV 1,507, V 173 and VI 415, which is 3,450 in all. The plan estimated 1,790.
- **The run's own build check:** the logs show zero overflows beyond 2pt in all six, and the report lists its visual
  inspections.
- **The renewed checks enlarge the papers.** The run prints each new derivation beside "the full former proof", which
  it keeps (report, checkpoints 14-15: "P1.18 now prints the full union of independently written ... derivations").
  Paper V grew from 131 pages (cp06) to 173 (cp15).
  - A paper for readers prints one checked proof per statement.
  - The former routes belong in the compendium.

### 2.2 The four gaps of the cp36 intake, against cp15

| Gap | At cp15 |
|---|---|
| 1. P3K.109-P3K.119 not accepted | **Stands.** All eleven are main rows printed "open" in IV §"Results not yet established" (pp. 1189-1461). Their renewed credit check is done; the proof and computation checks are partial or not started. Not needed for publication: they are already in the separate part. |
| 2. P1.6, P1.14, P5.7 not printed | **Stands.** All three are compendium-only, with reasons: P1.6 and P5.7 "known: cited background", and P1.14 "second proof ... shared with maps:src:F.4.1". This is a gap in the verification record of F.4.1, not in the mathematics. Add them as check events on maps:src:F.4.1. |
| 3. P3K.75 open | **Stands.** Printed open in IV, p. 1184, in the separate part. Closing it would be a further result. |
| 4. The physical line (P3K.68) | **Closed by a check** (Claude Opus 5.5 at effort max, 19 Nov, sections 6-7 of the intake): M is the right line, and P3F.22's normalization μ(λ(b)) = +1/28 is re-proved. That rests on Jin's coordinates. S6_10 opened and verified arXiv:2608.26698v2, Lemma 6.2 p. 35 (bib entry Jin2026). **Neither check is in the papers' records, and neither is public** (2.5). |

### 2.3 The printed rows with no independent check (39)

These rows' only recorded proof checks are by the session that wrote them, found by script over CHECK_EVENTS.tsv.

- **Paper I (2, both supporting):**
  - I:weierstrass-comparison and I:monodromy-fundamental-set, the receiving items S6_10 wrote.
- **Paper II (2):**
  - night:P3K.36 (main, false as stated: only the night run's own refutation);
  - ii:LR:covering (supporting, p. 441): the covering correction to Liu-Rollenske that II.14 prints.

  The S6_09 intake (section 5, item 5) asked for a second reader before a correction of Liu and Rollenske is printed.
- **Paper IV (35):**
  - 9 main rows: iv:correction:P3K.10, P3K.22, P3K.23, P3K.30, P3K.31, P3K.33, P3K.36 and P3F.53 (pp. 985-995), and
    iv:i3_all_reduced_caps (S6_10's receiving proof of night:P3K.108, p. 909).
  - 26 supporting rows: iv:rank_two_specialization and 25 further iv:correction rows (P3F.25; P3K.6, 17, 24, 25, 27,
    29, 32, 34, 35, 37, 40, 41, 43-46, 50, 52, 54 and 56-60).
  - What the cp36 intake covers: its arithmetic confirms the numbers in the P3K.10, 22, 23, 33 and 36 corrections
    (3; 3, 6, 9, 14; ×7; 26), but not their derivations.
  - Not covered at all: P3K.30, P3K.31, P3F.53 and the 26 supporting rows.
- **Papers III, V and VI:** none.

### 2.4 Check records as printed

- **They are verbose and unlinked.** Each `\StatementRecord` reads, for example: "Pre-continuation writing events: ...
  Continuation metadata events: ... status-vocabulary reconciliation; metadata reconciliation only; no new mathematical
  check ... The full former proof is preserved without retrospective prereading credit."
- **What a publication record needs:** one line per check, giving who, the check type, model and effort, the date, what
  the check did and a link to its public record and section (the user, 19 Nov ~15:5x UTC).
- **Claude events missing from them (22):**
  - **12 from the S6_10 cp06 intake** (Claude Opus 5.5 at effort max, 18 Nov). Re-proofs or proof checks of ari:C.4.2,
    ari:C.4.4, cdp:st:A.1.1, cdp:st:B1 and cdp:st:C.2.UN.1 (the parity theorem). Computations or consistency checks on
    fam:src:B.1.1, fam:src:C.2.3, inv:A2.2, night:P1A.2 and night:P1A.3. A rung-1 arithmetic check of night:P3K.69.
  - **10 from the cp36 intake** (Claude Opus 5.5 at effort max, 19 Nov): P3K.68, P3F.22, P3K.71, P3K.73-74, P3K.56,
    P3K.59, P3K.93 and P3R.2, the sign-flip arithmetic, and the record comparison.

### 2.5 Citable checks: public, and to publish

**Public** in the GitHub clone at 2838f66b (the same as origin/main):
- reviews/S6_02_REVIEW_FABLE/REVIEW.md (Claude Fable 5.2 at effort high, 12 Nov);
- in reviews/S6_FINAL_INTAKE_20261116/: INTAKE_FINAL.md, RESPONSE_EXPERT.md, INTAKE_S6_01.md and READING_S6_01_A1.md
  (Claude Fable 5.2 at effort high and at effort max, 16 Nov);
- reviews/S6_ROUTES_FABLE_MAX/NOTES.md;
- reviews/S6_INTAKE_CHECKPOINTS_20261115/INTAKE_S6_05_FINAL.md;
- reviews/S6_09_INTAKE_20261117/INTAKE_S6_09.md;
- raw/intake/S6_10_INTAKE_20261118.md, with its CHECK_EVENTS and code;
- the research runs' returns (S6_01 and S6_02_FAMILY by the README; S6_02_PUSH final, S6_03 cp13, S6_04 cp12, S6_05
  final, S6_09 final);
- S6_06_BLIND up to cp35;
- S6_10_PAPERS cp15 (with -data 37766ef).

**To publish** (on disk only, cited by the papers' check records or needed for them):

| What | Path (Documents\) | Cited for |
|---|---|---|
| cp36 intake, with gap 4 and P3F.22 | `s6_pro_prompts_20261112_work\reviews\INTAKE_S6_06_BLIND_cp36_20261119.md`, `..._CHECK_EVENTS.tsv`, `INTAKE_S6_06_BLIND_cp36_scripts\` | the sign of every class off the reference fan (IV) |
| S6_06_BLIND final state (cp36, 533.9 MB) | `s6_pro_prompts_20261112_work\returns\S6_06_BLIND_checkpoint_36_20261118T1547Z_unzipped\` | the source of P3K.117-P3K.119; goes to -data |
| Sweep 1 of the S6 register (Claude Opus 5.5 at effort max, 18 Nov) | `results_register\sweep1_s6\` | printed events "sweep 1, scope s6"; the 16 corrections |
| The check ledger and plan given to S6_10 | `s6_pro_prompts_20261112_work\S6_10_REVISION\S6_CHECK_LEDGER.tsv`, `S6_CHECK_LEDGER_SUMMARY.md`, `KEEP_SKETCH_20261117.md` | every "Historical events" line |
| This file | `s6_pro_prompts_20261112_work\reviews\S6_PUBLICATION_READINESS_20261119.md` | the readiness record |

The housekeeper a8ce28c3 (Claude Opus 5.5 at effort high) was resumed at 16:04 UTC to publish every Claude and Fable
note with a citation map, and push_sweeps ran. Check that each row above has a public link before a post cites it.

### 2.6 Cross-paper dependencies

These are counted from `\ExternalPaperRef` in the TeX:

| Paper | Cites |
|---|---|
| I | no other paper (it is cited by all five) |
| II | I 43, IV 13, VI 8 |
| III | I 47, II 7, IV 4 |
| IV | I 94, III 51, II 7, V 1 |
| V | III 13 (Thm 6.2, 6.3, ...), I 1 (Thm 17.4), VI 2 |
| VI | II 145 |

A posted paper cites an unposted one by its GitHub PDF, with the statement and page.

## 3. Paper by paper

Every paper's page 1 already says that it is AI-produced, that no human has checked its mathematics, and that it is
under CC0 1.0.

### Paper I. The (3,4,∞) family: periods, moduli, the two ends (475 pp.)

**1. New main results** (52 main rows: 51 proved, 1 open; locators checked in the cp15 PDF):

| Result (rung 0) | Labels and pages |
|---|---|
| The period β^part in closed form | fam:src:C.1.1 p. 22 |
| The exact domain 0<\|w\|<216 (theta norm maximum √2 at t=1) | fam:src:C.2.3 p. 28; ari:C.8.1-C.8.4 pp. 38-43; Arb re-certification push:src:E.4.1 p. 387 |
| All discrete data | fam:src:A.2.1 p. 47, A.3.1 p. 48, B.2.1 p. 56 |
| Two classes at fixed u; the correction of Engel's Remark 8.1 | fam:src:B.2.2 p. 58, B.2.3 p. 59 |
| (3k,4l): 2kl classes | fam:src:B.3.1 p. 60; push:src:E.1.2 p. 66 |
| Torsion values of the norm | ari:C.4.2 p. 34, ari:C.4.4 p. 36 |
| Albanese nomes | ari:C.2.1 p. 340 |
| Real structures | fam:src:B.4.2 p. 63; mapsI:src:A.3.2 p. 96 |
| Monodromy group of index 12 | fam:src:F.1.1 p. 70 |
| Stabilizers and the period map | fam:src:F.2.2 p. 74, F.3.1 p. 76 |
| Néron-Severi | fam:src:D.1.4 p. 82, D.1.6 p. 84 |
| Hodge table | inv:A2.2 p. 290, A3.1 p. 296 |
| Frölicher and Bott-Chern | inv:C1.1 p. 300, C2.1 p. 301, C3.3 p. 307 |
| Correction of [AC26] Remarks 1.3 and 9.21 | inv:A4.2 p. 299 |
| Twisted tangent cohomology | inv:D4.1 p. 311, D4.5 p. 318 |
| (1,1,1,0) for every coprime (3k,4l) | push:src:E.2.1 p. 319 |
| The untwisted pinching, and Engel's Conjecture 8.2 excluded by the virtual Euler number | push:src:A.1.2 p. 114, A.2.2 p. 117, A.3.2 p. 126 (with night:P2.10 p. 281, P2.11 p. 283) |
| The filling after w=r^6 | push:src:B.4.19 p. 204 |
| **No filling at w=0** | push:src:B.4.33 p. 247; night:P2.2 p. 273, P2.7 p. 277, P2.9 p. 280 |
| **The natural boundary \|w\|=216** | push:src:D.1.3 p. 255 |
| The boundary quotient | push:src:D.2.3 p. 257, D.3.1 p. 260 |
| Eleven CM parameters | ari:C.6.3 p. 348 |
| One critical point, star-shaped level curves | ari:C.8.15 p. 385; push:src:D.4.8 p. 270 |

- **Credited, not new:** fam:src:A.5.1 (p. 54; DGKX v1 Thm 1.4, with our own earlier proof, as the prompt requires),
  and fam:src:A.5.2 (p. 55) and B.4.1 (p. 62), which are DGKX v1 results re-derived.
- **Open:** inv:C3.8 (p. 449), and ari:C.7.4 (p. 427), proved under hypothesis H, with H open.

**2. Check state.**
- Every main row has a check by S6_09 and a re-derivation by S6_10 (18 Nov).
- 27 main rows have a Claude reading or computation:
  - Claude Fable 5.2 at effort high, 12 Nov (the S6_02 review): A.x, B.x, C.x, D.x and F.x of the family;
  - Claude Fable 5.2 at effort high and at effort max, 16 Nov: the A, C and D rows of S6_01; push A.3.2, B.4.19 and
    B.4.33.
- The cp06 intake adds ari:C.4.2 and C.4.4 (re-proof) and checks of C.2.3 and A2.2.
- **Renewed three checks:** 1 of 52 main rows (ari:C.2.1).
- **Read only by GPT-6 Astra sessions:**
  - S6_01: inv:A4.2, D4.1, D4.5;
  - S6_02_PUSH: A.1.2, A.2.2, D.1.3, D.2.3, D.3.1, D.4.8, E.1.2, E.2.1, E.4.1;
  - S6_05: ari:C.6.3, C.8.1-C.8.4, C.8.15;
  - S6_04: mapsI:src:A.3.2;
  - the night run: P2.2, P2.7, P2.9.
- **No independent check:** the two supporting rows of 2.3.

**3. Before publication.**
- **Must:**
  - credit and literature check of night:P2.2, P2.7 and P2.9 (main, "pending");
  - an independent check of I:weierstrass-comparison and I:monodromy-fundamental-set;
  - check records rebuilt and linked (2.4);
  - one proof per statement;
  - the renewed checks of the 51 remaining main rows (the user's ask);
  - the PDF check;
  - the Hexagon note.
- **Not needed (more results):** inv:C3.8 and the hypothesis H of C.7.4.

**4. Order and cost.**
1. Credit of P2.2, P2.7 and P2.9. Route: Claude Opus 5.5 at effort max, about 60k tokens, or the Pro check prompt of
   step 2.
2. The renewed checks of 51 main rows. Route: S6_10, if alive, or one Pro prompt for Papers I and III (GPT-6 Astra,
   ChatGPT Pro mode). That takes one slot for about 10 hours, at flat cost.
3. Records, one proof per statement, the PDF check and the note. Route: a Claude Opus 5.5 at effort max agent with
   scripts, about 150k tokens.

None of these steps costs money.

**5. Where it goes.**
- Hexagon, as the second deposit: it is the foundation, and every other paper cites it.
- GitHub as now.
- The Engel mail (Conj. 8.2) can cite push:src:A.3.2 p. 126 and night:P2.11 p. 283 on GitHub once the Claude
  re-derivation it still needs is done (RUNBOOK 19 Nov 16:06 UTC).

### Paper II. Torus-fibred threefolds with b₁=b₂=0; the CDP argument (471 pp.)

**1. New main results** (25 main rows: 23 proved, 1 open, 1 false as stated):

| Result (rung 0) | Labels and pages |
|---|---|
| **Cotangent torsion: the two endpoint vanishings on [CDP20] p. 692 need the injectivity of the connecting map** | cdp:st:A.1.1 p. 47 |
| **Nodal cubic × P¹ counterexample** | cdp:st:B1 p. 55 |
| [CDP20] Prop. 7.3 through unitary local systems | cdp:st:A.4.9 p. 75 |
| Integral component count (the rational formula is credited to [AC26] §10.5) | cdp:st:D.1.2 p. 13 |
| The very general fibre is a torus or a Hopf surface | cdp:st:C.3.1 p. 41 |
| **c₃ ∈ {0,2} for irreducible and normal-crossings supports** | night:P4.58 p. 238 |
| **The criterion for generic vanishing (replacement of [CDP20] Thm 2.2)** | cdp:st:C4f p. 288 (C4a p. 280, C4b p. 281) |
| Twisted tangent cohomology of X | cdp:st:C5b p. 292 |
| Trivial monodromy: c₃ ≤ 0, and equality realized | cdp:st:D.2.5 p. 302, D.2.7 p. 306 |
| Stability of the fibration | cdp:st:E6 p. 312, E7 p. 315 |
| Kuranishi germs of the two-parameter family, Liu-Rollenske and combs | cdp:st:E13 p. 322, E14 p. 324, E15 p. 328 |
| (3k,4l) is constant in families | push:src:E.2.23 p. 376, E.2.24 p. 378 |
| Four counterexamples and corrections | cdp:st:E12 p. 321, E17 p. 333, E18 p. 335; inv:E2.4 p. 388 |
| The Liu-Rollenske covering over u=w² | ii:LR:covering p. 441; night:P3K.36 (false as stated) p. 446 |

- **Open:** inv:E2.3 (p. 446).

**2. Check state.**
- Every main row has checks by S6_09 and S6_10 (18 Nov), except night:P3K.36.
- **Claude readings:**
  - Claude Fable 5.2 at effort high or max, 16 Nov: A.4.9, C4f, D.2.7, E.2.24;
  - cp06 intake (Claude Opus 5.5 at effort max): A.1.1 (proof check) and B1 (re-proof).
- **Renewed three checks:** A.1.1 only.
- **Read only by GPT-6 Astra sessions:**
  - B1's companions C.3.1, C4a, C4b, C5b, D.1.2, D.2.5, E6, E7, E12-E18 and E.2.23;
  - night:P4.58: the night run and S6_10.
- **No independent check:** night:P3K.36 and ii:LR:covering (2.3).
- The S6_09 intake noted that D.2.5 in its unrestricted wording was not confirmed by the night run. It carries II.9.

**3. Before publication.**
- **Must:**
  - an independent check of ii:LR:covering and of the P3K.36 refutation and correction. This is a correction of a
    published paper's claim, worded neutrally;
  - credit check of night:P4.58 and P3K.36 (pending);
  - a check of D.2.5's unrestricted scope;
  - records, one proof per statement, the PDF check and the note;
  - the renewed checks of 24 main rows (the user's ask).
- **Not needed:** inv:E2.3.

**4. Order and cost.**
1. The LR covering and P3K.36. Route: Claude Opus 5.5 at effort max, about 100k tokens.
2. The renewed checks with D.2.5 and P4.58. Route: one Pro prompt for Papers II and VI (the sign cluster), about 10
   hours, one slot.
3. Records and the note. Route: an agent, about 100k tokens.

**5. Where it goes.** Hexagon, after I.
- Its first two results (A.1.1, B1) are the series' most checked and most consequential. They are the best candidate
  for a short paper with a human author, should the user ever want arXiv or a journal (5).

### Paper III. Maps from the six-spheres, and the manifolds they give (409 pp.)

**1. New main results** (29 main rows: 28 proved, 1 open):

| Result (rung 0) | Labels and pages |
|---|---|
| The extension across the cusp; all of π₆(S³) occurs | maps:src:A.2.2 p. 7 |
| [e] = 6ν′ | maps:src:B.1.2 p. 9 |
| **f is null-homotopic** | maps:src:B.2.1 p. 10 |
| The cusp collapse represents η₄η₅ | maps:src:B.3.1 p. 11 |
| CW model (5,20,45,56,42,17,3) | maps:src:B.5.1 p. 17 |
| The Kummer cover has no smooth extension | maps:src:C.1.3 p. 26 |
| **Universal covers M_d** | maps:src:D.1.1-D.1.10 pp. 29-40, D.1.11 p. 218 |
| Rank-one Mordell-Weil profiles: 59 patterns on 50 rows | maps:src:D.2.28 p. 110, D.2.44-D.2.48 pp. 164-183; night:P3F.34 p. 240 |
| Conifold transition from S⁶ to S³×S³ | maps:src:D.3.1 p. 215, D.3.3 p. 217, D.3.2 p. 392 |
| A fourfold from the fibre product, not in Fujiki's class C | maps:src:E.2.1 p. 252 |

- **Open:** maps:src:D.2.4 (p. 394, Viaclovsky's Question 4).

**2. Check state.**
- Every main row has checks by S6_09 and S6_10 (18 Nov).
- **No Claude proof reading of any main row.** There are three computations from sweep 1 (B.5.1, D.1.4, P3F.34).
- **Renewed three checks:** none.
- **No independent check:** none.

**3. Before publication.**
- **Must:**
  - credit check of night:P3F.34 (pending);
  - the renewed checks of 29 main rows (the user's ask);
  - records, one proof per statement, the PDF check and the note.
- **Should:** one reading outside GPT-6 Astra of a headline (B.2.1 or D.1.x), because none exists.
- **Not needed:** D.2.4.

**4. Order and cost.**
- The renewed checks: in the I+III Pro prompt, about 10 hours.
- The Claude reading: Claude Opus 5.5 at effort max, about 100k tokens.
- Records and the note: about 100k tokens.

**5. Where it goes.** Hexagon, after II and VI.

### Paper IV. Smooth monodromy in Θ₇ = Z/28 (1,507 pp.)

**1. New main results** (42 main rows: 24 proved, 7 false as stated, 11 open):

| Result (rung 0) | Labels and pages |
|---|---|
| **Reference fan: class 0 for every coprime pair** | push:src:C.3.24 p. 59, C.3.27 p. 66; maps:src:B.6.24 p. 113 |
| The physical line M (supporting, carries every sign) | night:P3K.68 p. 401, P3K.69 p. 408 |
| **The all-fan algorithm; KL(S−1)(S−3)/8 is false** | night:P3K.71 p. 417, P3K.73 p. 428, P3K.74 p. 434 |
| OS45: class 3, and its covers give all of Z/28 | iv:correction:P3K.10 p. 985 |
| Primitive source profiles 3, 6, 9, 14 | iv:correction:P3K.22 p. 987 |
| **The flop multiplies by 7** | iv:correction:P3K.23 p. 987 |
| The whole-zero physical pair (3H, 24χ) | iv:correction:P3K.30 p. 990 |
| The old S-formula is false | iv:correction:P3K.31 p. 991 |
| **The original family: T₂ class 26; its fans give all of Z/28** | iv:correction:P3K.33 p. 992 |
| Source catalogue | iv:correction:P3F.53 p. 993 |
| Liu-Rollenske: T₂ class 26 | iv:correction:P3K.36 p. 995 |
| E6 collision: class 24 and its formula | night:P3K.99 p. 624, P3K.100 p. 702, P3K.103 p. 811 |
| M₆: class 27, the odd residues | night:P3K.101 p. 709, P3K.102 p. 801 |
| The progressions | night:P3K.104 p. 817, P3K.105 p. 829 |
| Selected I₃: class 8 | night:P3K.106 p. 843 |
| Every M₆ reduced cap realizes all 28 classes | night:P3K.108 p. 909 (iv:i3_all_reduced_caps) |
| M₂: the pair (−3,−12) | night:P3K.107 p. 914 |
| Main rows of Part 3F | night:P3F.21 p. 148, P3F.35 p. 164 |

- **False as stated, printed as corrections:** night:P3K.10 p. 1010, P3K.22 p. 1023, P3K.23 p. 1029, P3K.30 p. 1051,
  P3K.31 p. 1057, P3K.33 p. 1070 and P3F.53 p. 1081.
- **Not yet established** (separate part): P3K.75 p. 1184, and P3K.109-P3K.119 pp. 1189-1461.

**2. Check state.**
- Every night row has the night run's own check and an S6_10 re-derivation (18 Nov), except the 9 main rows of 2.3.
- **Claude:**
  - Claude Fable 5.2, 16 Nov: C.3.24 and C.3.27;
  - cp06 intake: P3K.69, rung-1 arithmetic only;
  - cp36 intake: P3K.68's choice of line (geometry), P3F.22 (re-proof), the algorithms P3K.71, 73 and 74 (new
    code), and the sign-flip arithmetic.
- **Renewed three checks:** none.
- **No independent check:** 35 rows (2.3), 9 of them main.
- **Size:** IV is 1,507 pages. Its two last sections are the corrections (659k characters of TeX) and the results not
  yet established (1,218k), about 35 % of the paper.

**3. Before publication.**
- **Must:**
  - an independent check of the 35 correction rows: at least the derivations behind P3K.30, P3K.31 and P3F.53, and
    behind the numbers the cp36 intake confirmed;
  - publish the cp36 intake and the night run's cp36 (2.5), so that the sign chain is citable;
  - credit checks of the night main rows (P3F.21, P3F.35, P3K.99-P3K.108, and the refuted historicals);
  - the renewed checks of 31 established main rows (the user's ask);
  - records, one proof per statement, the PDF check and the note. The note must say which classes rest on the
    reference fan and which on the all-fan algorithm.
- **Not needed:** P3K.75; P3K.109-P3K.119 (already in the separate part).

**4. Order and cost.**
1. Publish the files. Route: the housekeeper, about 20k tokens.
2. The corrections. Route: Claude Opus 5.5 at effort max, about 150k tokens, or the IV Pro prompt.
3. The renewed checks with credit. Route: one Pro prompt for Paper IV, about 12 hours.
4. Records and the note. Route: an agent, about 150k tokens.

**5. Where it goes.** Hexagon, last. A 1,507-page deposit needs its note to carry the reader: the opening's rungs 0-1
and the Θ₇ table.

### Paper V. The fourfold: a complex structure on 3HP² # (−HP²) and the family in c (173 pp.)

**1. New main results** (18 main rows, all proved):

| Result (rung 0) | Labels and pages |
|---|---|
| A three-connected eight-manifold with middle form 3⟨1⟩⊕⟨−1⟩ | maps:src:F.2.5 p. 13, F.2.6 p. 19; night:P1.13 p. 51 |
| Period planes from the genus-two pencil y² = x⁵ + λ³x + λ⁴ | maps:src:F.3.5 p. 38, F.3.6 p. 44 |
| **A compact complex fourfold diffeomorphic to 3HP²#(−HP²)** | maps:src:F.3.7 p. 49, F.4.1 p. 52 |
| **The family over 𝒰: pairwise nonisomorphic, algebraic dimension 1, Aut = C×Z/2, no antiholomorphic isomorphism** | night:P1.18 p. 58, P1A.1-P1A.6 pp. 67-80, P1.17 p. 76 |
| Input classification and the period-domain construction | maps:src:F.2.39 p. 154, F.3.4 p. 158, F.3.11 p. 163 |

**2. Check state.**
- **Renewed three checks:** 16 of 18 main rows.
- **F.2.39 and F.3.11:** their credit check is done and their proof check is partial. Both are "staged" in formal
  review 05.
- **Credit:** done on all 18.
- **Claude:**
  - Claude Fable 5.2, 16 Nov: F.2.5, F.3.4, F.3.5, F.3.6, F.4.1;
  - cp06 intake: P1A.2 and P1A.3, necessary conditions only.
- **No independent check:** none.
- **Renewed queue:** about 30 rows of the paper left.
- **F.4.1's last step** (homotopy-sphere absorption) now cites three inputs: Kramer-Stolz 2007, Theorem A, p. 178;
  the Wall-form classification (bib key IVVWallForm, Def. 3.6 and Thm 3.7(1)); and Mandal.
  - S6_10 marked each one verified, opened at those loci, on 18 Nov.
  - The S6_09 intake's doubt was about a 2026 reference for this step. A reading outside GPT-6 Astra of how Kramer-Stolz
    Theorem A is applied would settle it.
  - The night run reached the same conclusion independently (P1.6, P1.14), and that belongs in F.4.1's record.

**3. Before publication.**
- **Must:**
  - F.2.39 and F.3.11 through their renewed checks (or posted with their S6_09 and S6_10 checks, and the record saying
    so);
  - P1.6, P1.14 and P5.7 added as check events on F.4.1;
  - a check of whether V's citations of III (Thm 6.2 and 6.3) and I (Thm 17.4) are uses. If they are, the post cites
    III and I on GitHub by statement and page;
  - records with links, and one proof per statement. The former proofs of P1.12, P1.18 and F.2.16 are printed beside
    the renewed ones;
  - the PDF check and the note.
- **Should:** one reading outside GPT-6 Astra of F.4.1's use of Kramer-Stolz Theorem A. Route: Claude Opus 5.5 at
  effort max, about 60k tokens.
- **Not needed:** anything further.

**4. Order and cost.** See section 4: about one day, about 250k tokens of Claude Opus 5.5 at effort max, and no money.

**5. Where it goes.** Hexagon, as the first deposit.

### Paper VI. The sign theorem for every degeneration (415 pp.)

**1. New main results** (1 main row; three rung-0 results):

| Result (rung 0) | Labels and pages |
|---|---|
| **Every reduced fibre support has e ≥ 0; B = P¹, c₃ ∈ {0,2}, b₃ = 2 − c₃** | cdp:st:C.2.G.1 p. 400 |
| The equality case c₃ = 0, characterized | the opening's second rung 0 has no label |
| The parity e(S) ≡ dim ker(Λ²T − I) mod 2 is even, and every even value occurs | cdp:st:C.2.UN.1, C.2.UN.2 |

For C.2.UN.1 and C.2.UN.2 my label search found only the opening (pp. 4 and 6); locate them in the body before a post
cites them.

**2. Check state.**
- **C.2.G.1:**
  - S6_09 followed the complete proof (17 Nov);
  - S6_10 re-derived the revised assembly (18 Nov);
  - the continuation's proof check is partial;
  - the credit check is done.
- **Its chain** (C.2.UN.1-86, about 119 printed rows): every row has S6_09 and S6_10 checks, all GPT-6 Astra sessions.
  The only reading outside them is the cp06 intake's re-proof of the parity theorem.
- **No independent check:** none.
- **Renewed queue:** 92 rows.
- **Dependency:** VI cites Paper II 145 times.

**3. Before publication.**
- **Must:**
  - the renewed check of C.2.G.1 and of the chain rows it uses (the user's ask);
  - records (the parity re-proof added), one proof per statement, the PDF check and the note.
- **Should:** one reading outside GPT-6 Astra of the assembly of C.2.G.1. In S6_09's intake the theorem was the one
  result "I would not yet call established".

**4. Order and cost.**
- The renewed checks: in the II+VI Pro prompt.
- The Claude reading: Claude Opus 5.5 at effort max, about 150k tokens.

**5. Where it goes.** Hexagon, right after II: it rests on II.

## 4. The shortest path to a first publication: Paper V on Hexagon

1. **Is S6_10 alive?** Look in account 2's Library for a checkpoint after cp15 (minutes). If one exists, file it and
   use it: V and VI come first in the run's order, so V's queue should be near zero.
2. **Publish the missing check files** of 2.5. The housekeeper is already on it.
3. **On a copy of V** (the run's files stay unchanged):
   - fold in the Claude events (P1A.2, P1A.3) and P1.6, P1.14 and P5.7 as events on F.4.1;
   - rebuild every `\StatementRecord` as one linked line per check;
   - print one proof per statement, with former routes to the compendium;
   - settle F.2.39 and F.3.11 from the newest checkpoint.

   Route: Claude Opus 5.5 at effort max, scripts, about 150k tokens.
4. **Check V's citations** of III Thm 6.2-6.3, I Thm 17.4 and VI. Point them to the GitHub PDFs by statement and page,
   and confirm the links resolve. Route: the same agent.
5. **PDF check:** the overfull count from the log, and rendered pages (AGENTS.md). Minutes.
6. **The note in the post format** (`recent_results_20261114/HEXAGON_POST_FORMAT_20261114.md`):
   - the abstract travels alone;
   - Theorem A for the fourfold and Theorem B for the family;
   - the known-and-new table from V's credit receipts;
   - the proof map from the opening's rungs 0-1;
   - provenance;
   - the labels "primarily AI-generated", "no human author claimed" and human understanding "none";
   - the full paper as the compendium in the same deposit.

   Route: about 80k tokens.
7. **The user's yes,** with the files and the form answers shown. Then the deposit, one per UTC day.
8. **The next deposits,** a day apart as the allowance permits: I, II, VI, III, IV, each after its section 3 musts.

**Cost to the first deposit:**
- about 250k tokens of Claude Opus 5.5 at effort max, and the housekeeper's push;
- no Pro slot, unless S6_10 has died with F.2.39 and F.3.11 unchecked and the user wants their renewed checks first;
- no money.

**Where it does not go now.**
- **arXiv:** as I know its policy (to be confirmed on arxiv.org before any decision), an AI cannot be an author, and a
  human author must take responsibility for the content. Our papers name no person and say that no human has checked
  them. An arXiv route needs a human author who has checked a paper.
- **A journal:** the same, and these are 173-1,507-page papers.
- **The fitting outlets** are Hexagon, built for AI-produced mathematics with a named depositor, and GitHub, where
  cp15 is already public.

## 5. The blockers, one line each

This section was corrected at about 18:30 UTC.

**All papers**
- Each deposit waits for its paper's confidence pass (`S6_SERIES_DESIGN_20261119.md`, section 4). About 125 of the 167
  main rows still need a global check by another model family; the other parts of the pass are listed there.
- S6_10 ended at cp15. The count of its renewed same-family checks is not the measure.
- The printed check records carry workflow text and link no public record. In the user's format they leave the body;
  the methodology section links the check records on GitHub instead.
- Every check file the records rest on is now public (commit 4e8b5478 and the housekeeper's map), except S6_06_BLIND
  cp36 itself. That goes to the -data repository through the filer.
- No deposit version yet exists for any paper: the paper with its methodology section and records out of the body.
  Nor do the form answers or the user's yes. The allowance is one deposit per UTC day.
- The papers cite each other in cycles. Posted papers cite the others at one frozen, commit-pinned version
  (`S6_PAPER_V_DEPOSIT_PREP_20261119.md`, section 3).

**Paper I**
- The literature status is pending on night:P2.2, P2.7 and P2.9 (no filling at w=0).

**Paper II**
- A second reading of the Liu-Rollenske covering correction (ii:LR:covering) and of the P3K.36 refutation is advised
  before posting, because it corrects a published paper.
- The literature status is pending on night:P4.58.
- D.2.5's unrestricted scope is unconfirmed.

**Paper III**
- The literature status is pending on night:P3F.34.

**Paper IV**
- The literature status is pending on the night main rows.
- The wording of night:P3K.7 and P3K.8 lacks the reference-fan scope; their section supplies it.

**Paper V**
- Its citations of III, I and VI are linked by page at a pinned commit in the deposit copy. Its imports are consistent
  (`S6_PAPER_V_DEPOSIT_PREP_20261119.md`, section 3).

**Paper VI**
- It rests on Paper II, which is not posted; it cites II at the frozen version.
