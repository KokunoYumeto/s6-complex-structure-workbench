# Draft check of the S6 paper (S6_07_PAPER, final of 16 Nov 2026, 15:37 UTC)

By Claude (Fable 5.2 at effort high), agent a3da11221b89f2996, 16 November 2026, 17:35 UTC. No sub-agents.
The paper: `returns/S6_07_PAPER_final_20261116T1537Z_unzipped/S6_07_PAPER_paper.tex` (8,079 lines, 144 pages),
AI-produced by GPT-6 Astra (ChatGPT Pro mode). Checked against the six returns, the workbench file, arXiv:2610.00250
version 1, the writing prompt (`ALREADY_RAN/S6_07_PAPER/PROMPT.md`) and `DECISION.md`.

**Verdict: postable after the listed fixes.** No statement was found strengthened, weakened or changed in its
constants, hypotheses or status against its source. The fixes are five wording points, one reproduced proof of
another paper, one stale limit, and one check outside the text (the repository the announcements point to).

## 1. What was done, and what was not

- Scripts (in `scripts/`, outputs in `out/`): `s3_diff.py` (every source-table row: printed statement taken from the
  TeX by label, source statement taken from the source file by id, token diff after removing labels, references and
  font macros); `s5_text_rows.py` (rows without a source id: containment of the printed block in the source file by
  4-token shingles; direct diff where the source is addressed by a TeX label); `s7_proofs.py` and
  `s8_proof_new_text.py` (all 80 proofs against the source proofs; print-only text searched in all 321 section files
  of the six returns); `s9_appA.py` (Appendix A against the workbench file); `s6_status_words.py` (status by
  environment; the words of condition 11).
- Read in full: the metadata header and abstract, the Result section (Statement, Status, Known and new with the
  Campana-Demailly-Peternell paragraph, Proof map), section 2a, Open questions, Limits, Verification record (the
  short one), Provenance, Declarations, the head of Appendix A, the credit table rows 1-10 and 12.
- Appendix A was not read line by line. It was compared token by token with
  `workbench/period_shift_classification.tex`: 5,567 against 5,701 tokens, ratio 0.983, 49 differences, all of them
  the paper's renamed symbols (`u` to `s_new`, `w` to `ell^log`, `u` to `h_loc`, subscripts `per`, `Lambda`,
  `mathscr` dropped), the environment names, and the introductory paragraph.
- Not done: sections 1-11 and Appendices B and C were not read beyond the flagged places; no page of the PDF was
  rendered by me (the final build log `records/build/master_pass20.log` has 0 overfull boxes); the repository URL was
  not opened; the bibliography entries and the notation sheet were not checked; Engel's quotation was compared with
  the text copy of his paper, not with his TeX source (not on disk here).

## 2. Counts

| Item | Count |
|---|---|
| Source-table rows | 145: T 73, A 32, K 10, text 29, "false as worded" 1 |
| Printing environments | theorem 22, proposition 40, lemma 6, corollary 1, certified computation 3, remark 1 (INV A4.2, status T): 73 T; known result 10; announcement 32; refuted statement 1; definition 20; proof 80 |
| Status of each row against its environment | 145 of 145 agree |
| Status of each row against the prompt's binding table | all agree (list in 4) |
| `statement_as_printed` (CSV) against the TeX body | 137 rows compared, 0 differences; 8 rows name a label that is not in the TeX (D5) |
| Statements located in the source by id and diffed | 118: 79 identical after the paper's notation; 39 with residual differences, all judged below |
| Rows not located by id | 27: 2 workbench statements identical (ratio 1.000); the DGKX factorization theorem (their parameter renamed); Engel's conjecture (quotation agrees with the text copy); 23 text or definition rows checked by containment |
| Residual differences judged | 31 references, locators or notation; 2 splits of one source statement into a T part and an A part (INV B2.1; PUSH A.3.2), as the prompt's table prescribes; 1 dropped closing clause (PUSH E.2.23); 1 word (INV C3.3); 1 added parenthesis (PUSH E.2.1); 3 index renamings (CDP C5b: r_1, r_2 printed r_3, r_4) |
| Changes of content in a T, K or A statement | 0 found |
| Proofs matched to a source proof | 79 of 80 (75 by id; the four K-proofs moved to Appendix B rematched: FAM A.1.1 ratio 0.986, A.5.1 1.000, A.5.2 0.961, B.4.1 0.985). Token ratio at least 0.98: 58; 0.90 to 0.98: 14 |
| Proofs with text found in no return | 2 (D2, D8); 3 more assemble passages from several source places (D9) |

## 3. Discrepancies

Severity: **fix** = change before posting; **check** = something to confirm outside the text; **minor** = wording,
worth doing in the same pass; **note** = no change needed.

| # | Paper label | Location | Kind | Severity | Proposed fix |
|---|---|---|---|---|---|
| D1 | abstract | l. 210 | "The construction is credited to Claude (effort not recorded) and Alpöge and to Engel". Our rule forbids "effort not recorded"; [AC26] dates from July-August 2026, so the run counts as effort max. | fix | "credited to Claude (Fable 5 at effort max) and Alpöge, and to Engel". |
| D2 | `dgkx:all-maps-factor` | App. B, l. 7039-7044, "The universal map statement" | The proof printed is that of Theorem 7.2 of arXiv:2610.00250v1, "reproduced with that credit": 65 % of its 4-token shingles are in their text. A K-item was to carry our re-derivation; and their proof text is not ours to print in a CC0 paper. | fix | Print the statement with its citation and either no proof ("proof: [DGKXv1, Theorem 7.2]") or our own: the first paragraph of the proof of FAM B.3.1 is the same argument (H^2(S^6) = 0, the pulled-back Fubini-Study form, Stokes on a torus fibre). |
| D3 | `inv:B3.2` | l. 3170; Limits, item 4 | A theorem with printed proof whose proof invokes INV B1.2, which is an announcement. The paper says so in Limits only. | fix | Head the statement "T, conditional on INV B1.2 (A)" and say it in the results table; or make B3.2 an announcement. (The binding table produced this; it is not the writer's change.) |
| D4 | Limits, item 4 | l. 6213 | "The unread local direct-image inputs INV A1.1-A1.2" is out of date: `READING_S6_01_A1.md` (Claude Fable 5.2 at effort max, 16 Nov 14:25 UTC) read both and found them correct. | fix | Replace by "INV A1.1-A1.2 were read once (Claude Fable 5.2 at effort max, 16 Nov 2026) and found correct"; add the row to the verification record. The remark on ARI C.8.1-C.8.3 stays. |
| D5 | 8 source rows `periods:*` (theta-definitions, special-computation-availability, norm-definition, division-model, measure-conventions, certificate-record, local-expansion-constants, ladder-modular-conventions) | source table; App. C l. 7459, 7626 | The table gives labels that are not `\label`s of the TeX; the passages are unlabelled text of sections 3-4. | minor | Add the eight labels at the passages, or mark the rows "unlabelled text, section and line". |
| D6 | credit table, row 10 | l. 7561 ff. | "the smooth sphere fibre has Euler number two": the count of PUSH A.3.2 uses the fibre of Engel's untwisted family X(u), not the sphere family. | fix | "whereas the fibres of the untwisted family have Euler number two". |
| D7 | repository pointers | Provenance l. 6223; Limits items 1 and 8; every A-item | The 32 announcements and the proof of record for the radius 216 point to the repository. The writer could not retrieve the URL, and the certificate data and verifiers were not in its bundle. | check | Before posting: the repository is public, and holds the six returns under the run names and statement numbers the paper uses, with `f_interval_parallel_certificate.json`, the verifiers and the Arb certification. |
| D8 | `fam:A.5.2-corollary` | l. 3967-3975 | The two-line proof is the writer's own (by A.5.2 every small deformation is a member; each member has a = 1 by [AC26]). Its statement comes from the review's finding F4, not from a return. | note | None; it is the corollary the binding table asks for (row 6d). |
| D9 | `inv:B3.3`, `cdp:C5b`, `inv:B3.1` proofs | l. 3241, 3668, 3061 | Proofs with long print-only passages: B3.3 has a 619-token passage "For the invoked source argument take m_1 = 3, m_2 = 4, k = l = 1, d = 6 ..." (83 % found elsewhere in the returns: an invoked argument written out for the case at hand); C5b has 468 print-only tokens in six passages, all found elsewhere in the returns; B3.1 has two bridging sentences. | check | These three proofs deserve one line-by-line reading against the passages they invoke; the mechanical test finds no new argument. |
| D10 | `e26:Conjecture8.2` | l. 5560; preamble l. 130 ff. | The environment is named "Refuted statement (false)". DECISION files it as a counterexample to a conjecture. | minor | Name the environment "Conjecture (false as worded)" and keep "counterexample" for PUSH A.3.2, as the results table already does. |
| D11 | Result table | l. 224 | Last row: the announcements have kind "theorem". | minor | Kind "announcement". |
| D12 | App. B, proof of FAM A.5.2 | l. 7068 ff. | "These replace the producing run's incorrect DGKX lemma citations." Limits says "unsuitable". | minor | "These replace the producing run's citations of two lemmas of version 1." |
| D13 | `push:E.2.5.scope` | l. 6102 | A = 12kl and D = kl - 3k - 4l are in the source. The explicit formula w_{k,l} = exp(-pi i c/(kl)) is the writer's rendering of "the isomorphism parameter of PUSH E.2.7"; it agrees with the 2klZ identification, and I did not find it verbatim. | check | Compare with PUSH E.2.7. |
| D14 | `push:E.2.1` | l. 3767 | Added "(in particular gcd(3k,4l) = 1)" after "the admissible logarithmic data of PUSH E.1". That scope is coprime. | note | None. |
| D15 | `inv:C3.3` | l. 2892 | "independent of the disputed value of h" printed "evaluated value". | note | None. |
| D16 | `push:E.2.23` | l. 6152 | The closing clause "and E.2.4 is resolved by this theorem" is dropped. | note | None. |
| D17 | six definitions written by the writer (`push:A.1.fan`, `A.2.rays`, `A.2.periods`, `C.4.1.scope`, `E.1.1.scope`, `E.2.5.scope`) | l. 5717-6102 | Summaries of source set-up text in the paper's notation, status "text"; shingle cover in their source files 0.23 to 1.00. No number in them is absent from the source. | note | None beyond D13. |

## 4. Status labels against DECISION.md and the binding table

- PUSH B.4.33 (no filling at the puncture): announcement. Agrees.
- Theta_7: PUSH C.3.24, C.3.27 and MAPS B.6.21, B.6.24: announcements, "two runs" stated (l. 5993). Agrees.
- PUSH E.2.21-E.2.24 (the families as components): announcements. Agrees.
- Section 5 from the S6_01 intake: direct images, the scalar, the Hodge table (INV A1.0-A1.3, A2.1, A2.2, A2.4, A3.1),
  Frölicher (C1.1), Bott-Chern and Aeppli numbers (C2.1): theorems. N^2 = 0 (C3.3), the Hodge numbers of the (3k,4l)
  members (B2.1 second half, B1.2), the metric statements (C3.5, C3.7): announcements. The correction of [AC26]
  Remarks 1.3 and 9.21 (A4.2): T, printed as a remark, paraphrased and not quoted. Agrees, with D3.
- Engel's Conjecture 8.2: quoted as worded, "false as worded"; PUSH A.3.1 and A.3.2 theorems with proofs (virtual
  Euler number 0 against 2); the corrected fillings an announcement (PUSH A.3.2, final sentence, and A.1, A.2). This
  is row 10 of the prompt's table. DECISION section 1 lists "with the corrected form" among the theorems; the prompt
  made the corrected form an announcement, and the paper follows the prompt.
- K-items: FAM A.1.1, A.2.1, A.3.1, A.4.2, A.5.1, A.5.2, B.4.1, the DGKX factorization theorem, and the two workbench
  statements. Agrees with conditions 9 and 11.
- PUSH E.2.1 ((1,1,1,0) for coprime (3k,4l)): T, marked "two runs, no second reader" (l. 3761, 3789). Agrees.

## 5. Credit

- **arXiv:2610.00250 version 1 (Du, Guo, Kusakabe, Xie)** is credited for the 2Z statement (section 2a, abstract,
  credit row 2), the tangent cohomology, Kuranishi line and miniversality (credit row 6, section 6a), Aut = C^*
  (credit row 7), the intrinsic pencil and the factorization of maps to P^1 (credit row 1), and the punctured disc
  without its radius (credit row 4). Section 2a has exactly the prescribed wording: Theorem 1.4 of version 1;
  "Version 2 does not contain it"; "The same statement was obtained independently in the workbench from which this
  paper grew, and Appendix A prints that proof in the present notation."
- **Engel [E26]**: the geometric construction, Lemma 2.1 and Corollary 2.2, Remark 8.4 (Klingler's question),
  Proposition 2.4; Remark 8.1 corrected neutrally; Conjecture 8.2 quoted.
- **[AC26]**: the construction, K_X, Aut^0, the structure-sheaf direct images, h^{0,q}, h^{p,0}, h^{1,1} = h^{1,2} + 1,
  the Néron-Severi equation (Lemma 9.2) and the elliptic-logarithm reading (Remark 3.12), stated as known although
  their proofs are printed. With D1 for the model's effort.
- **Campana, Demailly and Peternell**: the prescribed paragraph, once (l. 247), and the bibliography entry; nothing
  else.
- **No claim of priority**: "priority" and "earlier than" do not occur; "first" and "before" occur only in
  mathematical senses in the front matter, the end matter and Appendix C; no date is compared with another. The
  paper says "AI-produced", never "AI-assisted"; CC0 is in the date line and the declarations; every model is named
  with its effort except in D1.
- **Bearing on precedence; flagged, not changed.** The user is still to supply the date on which
  `period_shift_classification.tex` entered the public Overleaf edition. If it is before 23 September 2026, these
  places change: section 2a (l. 473); the abstract's last sentence (l. 210); the header field `known_before`
  (l. 14); credit row 2. The same question for the Hodge numbers h^{1,1} = 2, h^{1,2} = 1 (the Reddit update of
  29 August): credit row 5, which already says that the numerical Hodge table is credited to the workbench
  (GPT-5.6 Sol, Codex reasoning effort ultra), and section 5.2.

## 6. Proofs

All 80 proof environments were compared mechanically; none was only sampled. 79 are the source's proof in the
paper's notation; the differences are run prefixes, reference locators, the renamed symbols, the prescribed
replacement of two citations in FAM A.5.2 by standard references, and the passages of D9. The one proof with no
source proof is D8. One proof is another paper's (D2). I saw no gap in the places read; I read no proof line by
line except the two short ones (D2, D8), so this section establishes that the proofs are the sources' proofs, not
that they are correct.

## 7. Order of work for the fixes

1. D2 (replace the reproduced proof), D1, D3, D4, D6: five edits in the TeX.
2. D7: confirm the repository.
3. The user's Overleaf date, then the wording of section 2a and the three other places.
4. D5, D10, D11, D12 in the same pass; D9 and D13 as one bounded reading.
