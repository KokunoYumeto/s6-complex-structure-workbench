# Q03_DEPOSIT: proof audit, corrected running time, and deposit revision

**Main result of this audit:** the full stepwise check found no false mathematical step in the stated m≥3 proof. The running-time calculation now proves the common explicit-input exponent **60m²+129m+2**, with an itemized deterministic multitape implementation and explicit effective coefficients. The padded exponent remains **60m²+129m+1**. The description hierarchy has global leaf budget **12m+25** and relative-prefix budget **6m+16**.

**Audit date:** 15 November 2026, Europe/Berlin. **Produced and checked by:** GPT-6 Astra (OpenAI), effort ChatGPT Pro mode. Parallel mathematical, accounting and source subreviews used the same model and mode. The attached earlier verdicts were preserved and examined; none was used as a premise of the new proofs. **Human understanding:** none recorded. **Formalization:** none of the present general-m proof. **Priority:** none claimed.

**Package state:** Complete; final user approval remains after delivery.

The original +8 input exponent was a larger upper bound supported only by a sketch. The repaired accounting gives +2 directly. The proof review also makes the choice domain in Lemma 5.5 explicit, completes the Uses/dependency records, and verifies the two rewritten proof layouts against the producing return. No counterexample to the scheduling theorem or its structural statement was found or is claimed.

The source work materially changes the historical framing. The opened Jansen paper states the all-fixed-machine result and linear leaf budgets; drbh's exact cited commit contains the complete four-machine release-theorem code. OpenAI's comparator target uses a placeholder, while the separately opened scheduling source contains its actual proof body. The revised post credits those exact scopes and makes no novelty claim. The original FKN full article and the course archive endpoint have stated access limits. The supplied prompt is preserved unchanged, with an exact discrepancy against an absent prompt variant in the old artifact manifest disclosed.

## Deliverables and how this report is organized

The principal files are `Q03_DEPOSIT_post.tex`, `Q03_DEPOSIT_post.pdf`, this report, `Q03_DEPOSIT_results.csv`, `Q03_DEPOSIT_sources.md`, and `Q03_DEPOSIT_literature.md`. The post's record block and the separate form answers accompany the package. `anc/` preserves the supplied task, return and reports; `code/` contains the programs and their recorded outputs. The full proofs are in the post. This report includes the independent derivations of every step, rather than only referring the reader back to those proofs.

The first sections below give the task ledger, changes, source/literature findings, computational scope, format checks and build history. After that, the complete A, B and E audit files are embedded verbatim. Their earlier work-note wording, recommended edits and inspected-snapshot hashes are preserved for traceability; the disposition ledger identifies what was implemented. The historical numeric state-bound symbol S used in the A audit corresponds exactly to calligraphic S in the delivered Section 9, through the explicit rename S↦𝒮 with value BN^m. No mathematical set, bound or proof operation changes under that rename. Final layout counts are given in the build table below; an embedded audit's earlier inspected-snapshot count is identified by that audit's recorded source hash.

The companion source ledger supplies every source URL, version, locator and availability attempt; the literature ledger supplies the complete dated query record. Their principal conclusions and limits are also stated here, so this report is self-contained on the outcome and reasons for the revisions.

## Per-task completion matrix

| Task | State | What was settled | Evidence and post changes |
|---|---|---|---|
| A.1 | Done | All eight padded-call subroutines have tape layouts and explicit bounds. Formula, set, state and witness files are separate; all index bits and scans are charged. | Full Part A below, §§1–4; Proposition 9.2. |
| A.2 | Done | The input encoding gives n≤L; N≤mL on padded branches; at most L deadline trials add one exponent. The resulting exponent is 60m²+129m+2 with explicit G(m). | Full Part A §5; Corollary 9.3; corrected (1.1), abstract, Status and record. |
| A.3 | Done | B·𝒮·𝒮²·𝒮N=B⁵N^(4m+1), B=K512^K N^(mK), 𝒮=BN^m. With K=12m+25 this gives 60m²+129m+1. | Full Part A §§3–4; A_check_accounting.py/output. |
| B.1 | Done | Every numbered statement of Sections 2–9 is covered by independent stepwise arguments. No false mathematical step found. Choice-domain wording in 5.5 is made explicit. | All A/B audits embedded below; 44 numbered proof rows in CSV. |
| B.2 | Done | The three rewritten steps of 3.3 and four rewritten steps of 5.5 were compared with the return. The order-statistic and injection arguments retain their meaning. | B_foundations, Lemma 3.3; B_hard, Lemma 5.5 concordance. |
| B.3 | Done | All 44 Uses lines match the dependency table and CSV. Named references exist and precede the using statement; definitions and standing properties are identified explicitly. | E_proof_integration audit and checker; revised proof Uses lines. |
| C.1 | Done under the requested unavailable-source rule | All cited source claims were compared at exact locators or marked unavailable with attempts. Original FKN full text remains unavailable; its metadata/abstract and full erratum were opened. | Q03_DEPOSIT_sources.md; S-P through S-G records; source summary below. |
| C.2 | Done | All 44 source-counterpart rows corrected/verified, including unnumbered prose counterparts. S records name their scope and limits; unavailable text is listed in Limits. | C_dependency_source_map.json; source ledger appendix; post verification record. |
| D.1 | Done with stated search-index limits | All requested venues/directions searched; dated exact queries and outcomes retained. Jansen, drbh and Giraudin found; no matching fixed-m≥4 hardness claim located. No universal absence or exhaustive citation census asserted. | Q03_DEPOSIT_literature.md; source S-J/S-D/S-G; query metadata. |
| E.1 | Done | Status/record/declarations aligned; names/efforts and statement numbers checked; ancillary bytes preserved. Build and rendering record below. | Format checklist; E audits; final validation and visual record. |
| E.2 | Done | Demonstration notice/field removed; current GPT-6 Astra F,D,C,S audit recorded, dated 15 November 2026. Cost/proof items closed; exact source/provenance limits retained. | Post record, Verification record, Limits and open points. |
| E.3 | Done | Original not-claimed limits retained; no practical implementation, polynomial-in-m bound, unsupported variants or formalization claimed. No priority or optimal-exponent claim added. | Theorem A scope; Not claimed; Declarations; record block. |

## Exact mathematical outcome and principal edits

The original explicit-job input lists a finite DAG and canonical binary integers m≥3 and T. Vertex labels are 1,…,n, with an explicit vertex list and distinct arcs; all delimiters and length fields count in L. Renaming a different finite binary identifier encoding is charged to input handling. A deadline T<1 fails for nonempty jobs; T≥n is handled by a topological schedule without expanding mT; the nontrivial branch is 1≤T<n and n≤mT. That branch pads to N=mT isolated-extended jobs.

For K≥1 define C=K512^K, B=CN^(mK), 𝒮=BN^m, q=64(m+1)(K+1) and D=2²⁰q². The entire padded computation has coefficient bounded by

\[
A(m,K)=2^{40}(m+1)^4(K+1)^4(K512^K)^5
\]

at exponent 5mK+4m+1. With K_m=12m+25,

\[
e_m=5m(12m+25)+4m+1=60m^2+129m+1.
\]

At most n≤L deadline trials, each with N≤mn≤mL, yield the common bound

\[
G(m)(L+2)^{60m^2+129m+2},
\quad
G(m)=A(m,12m+25)m^{60m^2+129m+1}+2^{31}(m+1)^4.
\]

Input processing and the final witness are included. The N-only statement starts after parsing; there is no assumption that a raw binary deadline or an arbitrary input name has length bounded by N. These are explicit upper bounds for this implementation. The report does not assert they are tight.

| m | List/carry leaves | Global leaves K_m | Relative-prefix leaves | Padded exponent | Common input exponent |
|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 61 | 34 | 928 | 929 |
| 4 | 33 | 73 | 40 | 1477 | 1478 |
| 5 | 39 | 85 | 46 | 2146 | 2147 |
| 6 | 45 | 97 | 52 | 2935 | 2936 |

### Edit and disposition ledger

| Original item or intermediate defect | Disposition in the delivered post |
|---|---|
| +8 input exponent asserted as conservative | Replaced throughout current text/record by the derived +2; original return remains unchanged in anc. |
| “Other work is lower-degree” runtime paragraph | Replaced by eight explicit subroutine rows, tape lengths, scan costs, witness extraction and domination inequalities. |
| Raw-input/padded cost boundary implicit | Canonical encoding and parsed padded starting point stated explicitly; original input reading charged in L. |
| Lemma 5.5 “its job of least rank” | Replaced by least-rank job of K∩W′, making the producing return's choice domain explicit. |
| Long proofs lacked numbered step layout | Numbered steps and bracketed dependencies added; the checked arguments are retained. |
| Literal-citation Uses entries omitted real dependencies | Replaced by direct mathematical dependencies and standing definitions/invariants; all table/CSV rows matched. |
| Source counterpart labels attached to nearby prose | Corrected to the exact source prose/definition/equation and its locator. |
| Intermediate numeric-state rename missed juxtaposed S products | Corrected in every Section 9 math segment; the declared map is S↦𝒮, value BN^m. |
| Intermediate table row 8.1 still said unchanged/--- | Replaced by the actual restriction identities using the capacity-dependent carry bound A_m=6m+9. |
| Standalone ranges in 8.5, 9.1 and 9.4 relied on context | m≥3 written explicitly in each statement and its CSV row. |
| Cited OpenAI deadline range omitted | Cited result 1 now states the source range 1≤T≤n. Q03's arbitrary-integer cases are proved in 9.1. |
| “New here” for every fixed m and linear leaf budgets | Removed after the Jansen source was opened; no novelty or priority claim is made. |
| drbh described only as partial four-machine work | Corrected to complete capacity-four release-theorem code at the exact commit; no fresh Lean replay claimed. |
| Comparator placeholder alone could misdescribe OpenAI proof | Actual Model/Main proof source opened and compared; exact definition correspondence recorded separately from the comparator target. |
| FKN bibliography omitted erratum and access limitation | Full erratum credited; original article's metadata/abstract versus unavailable full text stated explicitly. |
| Course date used as first-publication evidence | Replaced by dated source bylines and observed accessibility; failed archive endpoint disclosed. |
| 47,788-token historical run claim | Omitted from current concise record; supplied historical metadata and absent logs are identified. |
| Prompt-as-sent byte identity to old manifest implicit | Supplied prompt preserved verbatim; different absent manifest variant and tested byte maps disclosed. |
| Demonstration status and no-current-check statements | Removed; Version 1, current F,D,C,S check, limitations and declarations align. |
| Initial revised table overflows and orphaned layout elements | Column widths and final page layout repaired; exact counts and visual inspection below. |

No numbered statement was dropped. The CSV contains every numbered statement and the three front-matter result rows. No mathematical counterexample was needed or produced.

## Part C — source findings, exact scope, and residual limits

The source checks compare statements and versions. They certify the attributed source content within the scope stated; they do not claim a new proof audit of every external paper or a new Lean execution. Every mathematical premise used to prove Q03 is proved in its own Sections 2–9.

| Check | Opened source/version and exact locator | Finding and change |
|---|---|---|
| S-P | [OpenAI preprint](https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026), commit 4eaee87548250b2682affda7d05d947c05554bae; Theorem 1.1, Theorem 3.4, all source-column counterparts, §9 | Thirteen attached files are byte-identical. The source gives capacity-three results and its own numeric budgets. Column 2 now identifies exact numbered/prose counterparts. |
| S-F | [Scope file](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/124.md), line 9; comparator ReleaseTheorem:86–93; Scheduling/Main.lean:59–84 and Model.lean:86–93 | The comparator target ends in sorry, while actual Main.lean supplies the proof body. Deleting the comparator's target theorem declaration yields byte-identical Model.lean. All 53 scheduling files opened; no independent Lean replay/imported-axiom audit. |
| S-D | [drbh exact commit](https://github.com/drbh/scheduling-proof-exploration/tree/bbd30137258b15d8c5caedd035d72e8e8a875dbd), 8 October 2026; Model.lean:16–20 and 86–94; Main.lean:59–84 | Capacity four and full release-theorem code: exact optimization, bounded-deadline witness/NO output, fixed finite multitape bound C(L+2)^200022. Entry budget 29; list length 6. Arbitrary fixed m is not stated by this commit. No independent build. |
| S-N | [Nederlof–Swennenhuis–Węgrzycki](https://arxiv.org/abs/2312.03495v1), Theorem 1.1, printed p. 536; SODA 2025 pp. 535–552 | Exact upper bound (1+n/m)^(O(√(nm))) and bibliography checked. For fixed m this displayed bound is exp(O_m(√n log n)); it is not a lower bound on actual runtime. |
| S-A | [Das–Wiese](https://arxiv.org/abs/2501.09091v1), Theorem 1; [ESA 2022 article 40](https://doi.org/10.4230/LIPIcs.ESA.2022.40), 40:1–40:11 | Approximation guarantee and parameter-dependent time bound checked. With integer makespan and ε=1/(n+1), the guarantee yields exactness; dependence on this varying ε is retained and gives no stated polynomial bound. |
| S-FKN / S-FKN-e | [1969 article](https://doi.org/10.1137/0117070), metadata/abstract; [1971 erratum](https://doi.org/10.1137/0120018), complete p. 141 | Original 17(4), 784–789 bibliography and scope checked; erratum 20(1), 141 read. Original full article unavailable through attempted publisher routes and explicitly listed as unverified. |
| S-CG | [Coffman–Graham](https://doi.org/10.1007/BF00288685), original scan, Theorem 1 p. 203; p. 202 | Two-processor optimality and quadratic assertion checked in full source; Acta Informatica 1, 200–213 (1972). Relevant printed pages visually inspected. |
| S-U | [Ullman](https://doi.org/10.1016/S0022-0000(75)80008-0), Theorem 1 p. 389; discussion p. 392 | Unit-job NP-completeness with machine count in the input; JCSS 10(3), 384–393 (1975). The source discusses the fixed-count question on p. 392. |
| S-GJ | Garey–Johnson (1979), Appendix A13 OPEN8 p. 287; Appendix A5.2 SS9 p. 239 | Actual scan pages opened and visually checked. OPEN8 is the historical three-machine question, not a claim about present unresolved status. |
| S-L | [Course](https://kokunoyumeto.github.io/open-math-courses-public/courses/three-machine-unit-job-scheduling/), metadata and all 11 chapter sources | First 8 match attachments byte for byte. Lessons 9–11 date themselves 24 October and derive from Q03; their first publication is not established by an archive endpoint that returned 404. |
| S-J | [Jansen arXiv:2611.09392v1](https://arxiv.org/abs/2611.09392v1), 6 November 2026; Theorem 1.1 p. 1, Lemma 7.15 pp. 64–66 | Existing fixed-m exact algorithm and linear budgets 4m+5 and m+3. The statement includes fixed-multitape O(L)+m^{O(m²)}n^{12m²+26m+2}log³n optimization. Full external proof not independently audited. |
| S-G | [Giraudin Hexagon 2611.00060v1](https://hexagonmath.org/pdf/2611.00060v1), Theorem 1 p. 1; dated 3 November, platform listing 4 November | Three-machine exponent 276 statement opened. It does not quantify arbitrary fixed m. Full external proof not independently audited. |

The exact source-count details matter for the dependency audit. OpenAI's source sets the enumeration budget K=10000; Theorem 3.4 promises fewer than 500 leaves. Its final proof bounds qualifier unions 195, same-cutoffs 196, common allowance 205, high part 197, low part 209 and global nodes 406; it gives a relative bound 210 plus one removed-slot predicate. The entry lemma bounds a newly switched first entry by 25 and states a uniform fewer-than40 entry bound. The original Q03 comparison wording about source constants therefore required correction to these locators, not repetition from memory. These source constants are not used to derive Q03's 12m+25 bound.

Access failures and their recovery are recorded in full in `Q03_DEPOSIT_sources.md`: pinned raw retrieval recovered OpenAI files; exact-commit API/archive retrieval recovered drbh; official arXiv PDF retrieval succeeded after an opening error; validated byte-range download recovered the Garey–Johnson scan. The original FKN full proof and course provenance.json endpoint remain the stated unavailable items. No unavailable source is presented as having been read. The external Lean builds and the complete Jansen/Giraudin proofs were outside the stated S-check scope, and are not premises of Q03.

## Part D — literature outcome and dated search record

The search was conducted on **15 November 2026 (Europe/Berlin)**. The saved ledger currently contains **14 batches and 50 exact queries**, including a closing repeated search. The complete spellings, engine choices, returned headings/URLs and access limits are in `Q03_DEPOSIT_literature.md` and `code/C_search_history_complete.json`.

The search covered the theorem for all fixed m≥4, the single case m=4, fixed-m hardness, linear description budgets, arXiv, STOC, FOCS, SODA, ICALP, IPCO, ESA, APPROX, authors' pages, GitHub, the general web and Hexagon. Exact-title and source-name searches also sought work citing or derived from the OpenAI preprint. The identified chain includes drbh, the course, Jansen, Giraudin, mathcommunity revision activity, the AI Proved What episode and Plectis Atlas indexing. Each has its role and evidence in the literature ledger.

The controlling result for the post's framing is the opened Jansen theorem and linear budget statement. The post consequently presents its complete Q03 argument and accounting, with no claim that the all-fixed-m theorem or a linear budget first appears here. The drbh scope is credited fully. Giraudin supplies a separately stated three-machine exponent refinement. The search located no source proving hardness for a particular fixed m≥4 in the exact unit-job/arbitrary-DAG model. This is a finite search finding. No complete forward-citation index was obtained for the GitHub preprint, and the report does not infer that unindexed work does not exist.

## Computational evidence and exact coverage

| Program or check | Observed result | Scope and limit |
|---|---|---|
| Original `code/check_walk.py`, re-executed | 65,610 cases; 2,503,064 shared-cutoff premises; 133,963 exchange candidates; zero violations | All 65,536 edge choices in a fixed4+4 two-layer m=4 family, 72 specified three-layer m=4/m=5 cases, and 2 constructed cases. It is not enumeration of all scheduling instances. |
| New `code/B_hierarchy_check.py` | 255 feasible DAGs, 754 nodes, 132 switched children, 499 capacity/global-child checks, 7,069 cutoff identities, 978 relative formulas; zero violations | Fixed seed 20261115, specified sampled layered families, m=3,4,5. Complete actual hierarchies constructed; full replacement schedules checked for nonvacuous I3 pairs. |
| Nonvacuous I3 checks in the new hierarchy run | 11 pairs, 8 full replacements, 12 globally checked exchanges; 48 qualifiers at a left boundary and 5 strictly before it | These are finite measured cases, not a proof for every boundary history. |
| New hierarchy coverage limits | Maximum depth 5; maximum observed surviving injection count 1; maximum observed global-child leaf count 10; zero surviving-first initial-pair replacements | The arbitrary-history proofs of 5.5 and 6.1 establish the full bound and flattening case; those universal claims are not inferred from the finite run. |
| `A_check_accounting.py` | Exact exponent substitutions and every table-row domination inequality pass | Algebraic checker in m−3 coordinates for all m≥3, K≥1; the tape implementation itself is proved in Part A. |
| `E_verify_provenance.py` | Six exact ancillary copies; expected return hash; zero actual local paths/credentials | Two screened Windows-drive matches are inspected TeX function notation. Exact hashes and prompt byte-map tests recorded. |
| `E_check_proof_integration.py` | Zero missing/duplicate rows, proof/dependency/source-map mismatches, forward named Uses references or unconverted numeric-state symbols | Compares exact current post/CSV/source-map snapshots; all 44 proof statements and 3 front rows included. |
| `E_check_final_consistency.py` | Constants, exponents, ranges, models/efforts/dates, prompt qualification and 47 CSV rows agree | Records exact inspected-source hash; rerun after final assembly. |
| Source comparison/locator programs | Thirteen OpenAI attached/public files and first 8 course chapters match; exact commits, hashes, locators and query outputs saved | Text/source inspection is recorded separately from proof re-derivation and Lean execution. |

Every program and its output are retained under `code/`. There was no counterexample search result used as a disproof. No finite experiment is promoted to a universal theorem; the full independent stepwise proofs follow later in this report.

## Part E — format checklist and delivery state

| Format §8 item | State | Evidence |
|---|---|---|
| 1 | Done | Every Status row is supported by the Verification record; claim, current-check types/verdict, human understanding, formalization and declared limits agree. |
| 2 | Done | POST-RECORD, abstract, Status and Declarations agree on kind, bounds, claim, model/effort/date and check scopes. |
| 3 | Done | All producing/checking models have an effort setting; original question/course use effort not recorded. Current-task author Opus max is included. |
| 4 | Done with declared source-access limits | No external theorem is a proof premise. Every attributed source has an S row or precise unavailable scope in Limits, including original FKN full text. |
| 5 | Done | Original numbering retained;44 proof statements + 3 front rows; full text/dependency/source correspondence checked. Symbol rename and explicit ranges documented. |
| 6 | Done | OpenAI, drbh at exact commit, classical authors and discovered prior literature credited by name, URL and exact scope; no human authorship of Q03 added. |
| 7 | Done | Literature search dated 15 November 2026, with closing repeated queries and exact query/result ledger; no priority claim. |
| 8 | Done | Final compilation counts are read dynamically below. All final pages rendered; visual inspection is documented in the inserted QA record before delivery. |
| 9 | Done | Prompt, return and three reports preserved byte for byte in anc; current task also retained. No actual local paths/private identities/credentials found; prompt-manifest discrepancy disclosed. |
| 10 | User approval remains after delivery | The package supplies the PDF, record block and form answers for review. No external publication or deposit was performed by this audit. |

### Compilation and visual verification

| Build | Pages | Overfull boxes | More than 2pt | Maximum overflow(pt) |
|---|---:|---:|---:|---:|
| Supplied baseline | 32 | 0 | 0 | 0 |
| Initial revised assembly | 38 | 6 | 4 | 4.70132 |
| Final revised build | 38 | 0 | 0 | 0 |

The initial revised assembly had four 4.70132pt dependency-table alignment overflows and two 1.4092pt verification-header overflows. Column widths were corrected. The final build data above are read from `work/build_final/build_check.json`; its complete log and console outputs are retained. The current final log has no undefined-reference/citation or fatal-error message. Final layout adjustments also address the isolated Theorem A Uses line and the separated 8.1 heading observed during visual review; the exact final inspection record follows.

### Completed visual inspection of the final PDF

**Reviewer:** GPT-6 Astra (OpenAI), effort ChatGPT Pro mode, 15 November 2026.
The inspected final PDF has **38 pages** and SHA-256
`d8782e70ae9286badbf36c6ac98247698f7747fa00f1c9733d4a76b1d1c6265a`.
Its source hash is recorded in `code/visual_review.json` and the final build record.

All 38 pages were rendered at 85 dpi and inspected in seven numbered contact
sheets. Additional individual-page views by the assembling reviewer covered
pages **1, 3, 4, 5, 6, 7, 14, 20 and 27**, spanning the title/results, every
dependency-table continuation, foundations, walks, the capacity injection and
global child formulas. The cost/verification/reference pages receive the
additional review documented in `work/E_visual_tail.md`. Every page belonging
to a previously overflowing table was visually examined: pages 3–6 and 34–35.

The dependency and verification tables now fit their columns and margins;
no clipping, overlap or missing content was observed. The first-page Theorem A
Uses line is together with its statement, and Theorem B begins page 2. The
Lemma 8.1 heading and its displayed statement are together on page 27. The
remaining proof displays, source URLs, page numbers and reference continuations
were checked in the contact sheets. The final page ends with the completed
bibliography and has its normal remaining white space.

The baseline supplied post built to 32 pages with zero overfull messages. The
first revised 38-page assembly had six messages: four dependency-table
alignments of 4.70132 pt and two verification-header overflows of 1.4092 pt.
Column widths were repaired. Subsequent layout edits shortened the abstract's
repeated attribution wording while preserving its content, adjusted title
spacing, kept numbered headings with following text, and explicitly ended the
first page after Theorem A's Uses line. The delivered 38-page build has **zero
overfull boxes, zero boxes over 2 pt, and zero undefined-reference/citation
warnings**. There is no unresolved visual finding.

`code/render_review.py` reproduces the contact sheets; `code/record_visual_review.py`
serializes these completed observations and requires the exact inspected PDF
hash. Neither script treats rendering alone as a visual inspection. Final
page PNGs, contact sheets and the full build logs are retained in the archive.

### Preservation, supersession and exclusions

All original mandatory ancillary files remain unchanged. In particular, the original return retains its historical +8 exponent and source assertions; the revised post supersedes those claims for the current deposit, and this report explains the changes. The supplied original prompt's exact bytes remain authoritative for what was attached to this task; no missing manifest variant is fabricated. The original report verdicts remain intact.

All audit work files and their substantive findings are retained. The embedded A/B/E records are reproduced verbatim below. Earlier phrasing in a work record that recommends a change is preserved as the record of that recommendation; the edit ledger above and current post show its implementation. The records concerning incomplete intermediate S renaming, a table-row placeholder, and initial overflows are retained with their exact correction and validation. No failed mathematical statement or missing numbered statement was silently dropped.

The following exclusions are explicit. They concern supplied inputs, retrieved source reproductions, generated runtime files or duplicate intermediate render artifacts; the proof/audit conclusions, commands and relevant outputs remain in the package.

| Excluded file or category | Reason and retained replacement/evidence |
|---|---|
| Original attached background ZIP and its duplicated scans/sources | Already supplied inputs; not duplicated in checkpoints/final package. Required prompts, return and reports are separately preserved in anc. Their source identities and hashes remain recorded. |
| Newly retrieved full PDFs/scans/course chapters/repository snapshots in the external research cache | Source texts used for inspection are not republished in the deliverable. URLs, versions, hashes, locators, scope findings, failed/recovered access attempts and reproducing retrieval code are retained. |
| Former `work/openai_paper_live.txt` | Full retrieved preprint text; superseded for deposit by the thirteen-file byte comparison and exact source-locator map. |
| Former `work/drbh_README_bbd3013.md` | Full pinned README; its discrepancy with actual code and the corrected scope are recorded in S-D. |
| Former `work/drbh_commit_bbd3013.json` | Full external commit diff/source; exact commit/hash/scope and needed comparisons retained in source outputs. |
| Former `work/drbh_commits.json` | Raw external history API response; relevant commit/date sequence retained in S-D. |
| Former `work/drbh_model_bbd3013.txt` | Full external model source; exact capacity and release declaration locators retained in S-D. |
| `work/tex_runtime/pdflatex.fmt`, `pdftex.map`, `texsys.aux` and runtime-only generated state | Regenerable typesetting runtime data, not mathematical artifacts; build program, format-build diagnostics and final logs preserve the reproduction record. |
| Duplicate baseline/intermediate PDFs and duplicate final PDF beneath the build directory | The delivered root `Q03_DEPOSIT_post.pdf` is the publication artifact. Baseline/intermediate/final build JSON, logs and visual evidence preserve the before/after checks without presenting obsolete PDFs as deliverables. |
| Redundant intermediate page images/contact sheets, where omitted by packaging | Final-page rendering/visual-review evidence and the exact issue/fix ledger are retained; obsolete intermediate pixels add no distinct proof or audit conclusion. |
| Local transfer/runtime caches, Python bytecode caches, temporary shell files | Regenerable execution intermediates; no proof, source finding, authored program or recorded substantive output is removed through this exclusion. |

`work/C_source_notes.md` records the exact early source files moved to the external cache and their reasons. The final ZIP packaging ledger lists the files actually excluded by the packaging filters. No prior hourly checkpoint is overwritten, renamed or deleted. Checkpoints are created only at the requested hourly boundary; the first boundary for this run is00:27UTC. The package keeps the authored evidence available for continuation and review.

### Remaining qualifications, stated exactly

1. The original FKN 1969 full proof was unavailable through the attempted routes. Its metadata/abstract and the 1971 erratum were opened, and Coffman–Graham's full source supplies the separately checked two-machine background statement.
2. The course's advertised provenance.json returned HTTP 404. All 11 chapters were opened; the first 8 match the attachments. Their byline dates do not independently establish first-publication dates.
3. The old artifact manifest lists an absent 9,383-byte inputs/PROMPT.txt. The supplied 9,551-byte prompt is preserved; the tested exact newline/BOM maps do not produce the listed hash. No byte identity or missing text is invented.
4. Historical model-run dates, API mode and independence are supplied-record metadata. No underlying batch logs were provided; the current text does not claim their independent authentication.
5. The OpenAI and drbh Lean builds/imported-axiom reports were not replayed. Actual source statements and proof bodies were opened; no new L-type formalization check is claimed.
6. Jansen and Giraudin were checked for their declared results and relation to this subject. Their complete external proofs were not independently re-derived and are not used as Q03 premises.
7. Literature search indexes are incomplete. The exact 50-query record at this assembly establishes what was searched and found, without a universal theorem about absent publications or citations.

These are source, archival and scope qualifications. The mathematical A/B items have complete arguments below. Final user approval of the displayed post remains the user's step after receiving the package; this audit performed no public deposit.

---

# Full independent mathematical and provenance records

The following six files are included in full, with their original text. Every embedded record is identified by filename; the generator checks exact inclusion and records its SHA-256 in `code/assemble_report_output.json`.

---

## Part A — full itemized accounting and Section 9 proof audit

Source record: `work/A_accounting.md`. Full text follows.

<!-- BEGIN A_accounting.md -->

# Part A and Section 9: independent audit

Audit date: 15 November 2026 (Europe/Berlin). Auditor: GPT-6 Astra, effort ChatGPT Pro mode.

## Verdict and scope

The finite enumeration algorithm of Section 2 admits the padded running-time bound in Proposition 9.2. An itemized sequential-tape implementation is given below. The calculation proves the input-length exponent **60m²+129m+2** for the stated procedure that tests at most n deadlines. The previously printed +8 is a weaker bound; no extra six powers are required by this accounting. The bound in N starts from the parsed, canonically numbered padded instance. Reading an arbitrary original input is charged separately in L.

The accounting applies to the actual finite computation, including its witness on every accepted instance. Its running time does not require a conclusion about the completeness of the description family. The proof composition used in Theorem 9.1 is audited in §7 below; the independent audit of Theorem 8.5 supplies the structural part of that composition.

## 1. Machine, encoding, symbols, and constants

Use one deterministic multitape Turing machine with a fixed finite alphabet and a fixed finite number of tapes (32 suffice for the files, copied records, stacks, unary scan counters, binary loop counters, and output described below). The number of tapes is independent of m, K, n, and N. The program receives m and computes K; its formula stack is encoded on a tape, rather than being implemented by K separate tapes.

An explicit instance contains a canonical self-delimiting binary integer m, a canonical signed binary deadline T, n, an explicit list of the n vertices numbered 1,...,n, and a list of distinct arcs with endpoints in that list. All separators and length fields count towards the bit length L. Vertex identities are these canonical integers. There is at least one bit per explicit vertex, hence n≤L. The graph is promised acyclic; the preprocessing can also reject malformed encodings, repeated arcs, and cycles within the preprocessing bound below. Alternative finite binary vertex names are supported by a first renaming pass charged to L, using repeated scans and comparisons; they do not enter the N-only padded bound.

In a nontrivial padded call, m≥3, K≥1, 1≤T<n, n≤mT, J=[N], and N=mT≥m. The padded DAG is presented in canonical form; isolated padding vertices have consecutive new labels. Set

- C=K·512^K;
- B=C·N^(mK), an integer upper bound on the number of syntactic formulas with at most K leaves;
- S=B·N^m, an integer upper bound on the number of states for one described set;
- h=⌈log₂(N+1)⌉;
- q=64(m+1)(K+1).

The actual formula, set, and state counts may be smaller; all loops run over the actual counts. The displayed B and S are bounds, not instructions to materialize unused records.

For explicit hidden constants, the implementation below has all table-row costs bounded by D times the expression in its row, where D=2²⁰q². The coarse final envelope

A(m,K)=2⁴⁰(m+1)⁴(K+1)⁴(K·512^K)⁵

bounds the coefficient of N^(5mK+4m+1). The fixed numerical slack covers at most 32 tape heads, delimiters, returning to the beginning of scanned files, stack management, and the sum of the listed rows. A basic full scan/copy/compare operation uses a bounded number of moves per symbol; the loop and record descriptions below give at most 64 such elementary passes per row operation after counters and stack words have been included. Thus D, and consequently A, are effective bounds depending only on the displayed parameters. These constants have no claim to sharpness.

The useful length inequality is

⌈log₂(S+1)⌉ ≤ 2+10K+(mK+m)h ≤ qh/8 ≤ qN/8.

Here log₂K≤K for K≥1, so log₂C≤10K; and h≤N for N≥3. The same bound applies to a formula number or a described-set number. An individual formula code uses at most O(K(m+1)h) bits, also covered by qN. All index comparisons and binary increment operations are charged at their full bit cost.

## 2. Tape layout and scan costs

1. **Graph files.** Store adjacency and transitive-closure matrices in row-major order, as N² bits with row separators. Use a separate length-N active-vertex vector and rank map. A requested matrix location is reached with a unary distance scratch word. Constructing that word and scanning to the location cost at most a constant times N². The counter is moved in parallel with the matrix head, so an N² scan does not incur a binary counter increment at every bit.

2. **Formula file.** Each record has a formula code, its evaluated N-bit set, and an index. Its length is at most qN. Formula evaluation uses a delimited postorder stack on one tape. A stack access can scan its O(KN) bits; this cost is included in the formula-evaluation bound.

3. **Described-set file.** After duplicate removal, each record has an N-bit set, its cardinality, an ordinal, and an acceptance bit. Pad records to the same length, at most qN. A query set is kept on a separate tape. Comparing it against every record costs at most D·BN; the deliberately looser D·BN² bound accommodates seeking and copying a matching witness as well.

4. **Witness file.** Store a set ordinal and the full schedule of each accepted set. A schedule is an ordered list of at most N canonical job identifiers, each at most h bits, with slot separators. One record has at most qN² bits. The whole witness file has at most qBN² bits. The witness file is separate from the state file; its longer records do not increase state-access cost.

5. **Current-state file.** For the current W, each state record has L,Z,R as three N-bit vectors, its ordinal, a reached bit, an initial bit, and a predecessor ordinal or a null symbol. A final bit may be stored as well. Its length is at most qN. There are at most S records. Fetching or updating a record by its ordinal scans at most qSN bits. The scan compares the query ordinal with the ordinal field of each record, charging all bits; no constant-time indexed access is used. A bounded number of such scans costs at most D·SN.

6. **Work files.** A fixed collection of auxiliary tapes holds W, two states, a transition-gap vector, counters, and a predecessor path. Variable-length lists and the formula stack are ordinary delimited records. Nothing in this layout allocates a new tape when m or K increases.

## 3. Itemized padded-call cost table

Every expression in the following table counts deterministic multitape steps up to the common coefficient D. B and S have the meanings fixed above.

| Subroutine | Bound for the entire padded call | Construction giving the bound |
|---|---:|---|
| Canonical padded input to adjacency; reachability; deterministic rank | N⁵ | At most N² arc insertions with N² scans; N³ Floyd–Warshall iterations with O(N²) matrix accesses; repeated scans for deterministic topological order. |
| Generate and evaluate all formulas | B N³ | At most K leaves per formula; at most mN reachability queries per cone leaf; each query costs O(N²); fixed-parameter factors fit D. Postorder Boolean vector operations fit the same bound. |
| Pairwise deduplication | B³ N | At most B² record pairs; fetch/compare/mark by complete scans of a file of length at most qBN. Compact surviving records afterwards. |
| Cardinalities and cardinality ordering | B³ N² | Compute each cardinality by scanning its N bits. Repeated selection scans or pair comparisons with full record retrieval give this deliberately loose bound. Equal-cardinality records use their ordinal as a deterministic tie-breaker. |
| Enumerate and initialize all current-state files | B S (B N²+N⁴) | For each of at most B sets and S candidates, fetch W and F, form L,Z,R, test compatibility, and perform the initial/final acceptance queries. |
| Reachability dynamic program on state graphs | 3 B S⁴ N | At most S passes over at most S² ordered state pairs for each of B sets; each pair costs at most 3D SN. |
| Reconstruct and store all accepted witnesses | B S N²+B²N³ | Every predecessor path has at most N/m states; fetch its records and at most N/m+1 smaller accepted schedules, then concatenate the disjoint pieces. |
| Produce the selected padded witness | N³ | Scan the saved schedule and rank-to-label map; delimit slots; output at most N identifiers. The preceding row already includes storing the witness. |

Here are the details proving each row.

### 3.1 Reachability and rank

Initialize the N×N adjacency matrix. There are at most N² distinct arcs; writing each one by a complete matrix seek gives O(N⁴). Floyd–Warshall maintains the invariant that, after processing vertices 1,...,k, the matrix indicates paths whose internal vertices are in that set. The usual recurrence uses three matrix locations for each triple (i,j,k), and every matrix access, including a possible update, costs O(N²) using the unary scratch distance. N³ triples therefore cost O(N⁵). A nonzero diagonal detects a cycle. For the DAG case, select the smallest active vertex having no active predecessor, remove it, and append it to the rank map. Scanning candidate rows and the active vector with repeated complete seeks costs at most O(N⁵) over all removals. Lemma 2.1 proves that the resulting rank respects reachability. Reverse-frame ranks and cones use the same matrix and the map i↦N+1−i.

### 3.2 Formula count and generation

The exact overcount of leaf choices is 4+8(N+2)+20·binom(N,m). For N≥m≥3 this is at most 64N^m. The four terms for constants include complements, the threshold count includes the two frames and complements, and each of the five slot/cone atom types has two frames and two complement choices. A full ordered binary tree with ℓ leaves has at most 4^ℓ shapes and at most 2^(ℓ−1) assignments of union/intersection labels. Thus each ℓ contributes at most (512N^m)^ℓ; summing ℓ=1,...,K gives at most K512^K N^(mK)=B.

Enumerate only valid Dyck (balanced-parenthesis) words of length 2(ℓ−1), by depth-first extension through valid prefixes. The search visits O(K) prefix-tree edges per output and each update/scan costs O(K), giving O(K²) delay. These words encode the full ordered binary-tree shapes with ℓ leaves. Then enumerate their internal labels and leaf parameters. Enumeration is by finite counter loops; the total code and counter length for one formula is at most qN. A cone atom is evaluated by considering each job x and each of at most m members y of its slot subset and retrieving the appropriate reachability bit. At most mN queries, each costing O(N²), give O(mN³) per cone. The membership vector for a slot or rank threshold and its complement costs less. Evaluate the whole tree in postorder; each internal operation combines two N-bit vectors. Even scanning the O(KN)-bit stack at every node costs O(K²N). K cone evaluations and all stack scans fit D N³. Multiplying by the formula count gives D B N³.

### 3.3 Deduplication and sorting

Compare each pair of evaluated formula records. A complete fetch of each indexed record scans at most qBN bits; comparing N-bit vectors and marking the later equal record are charged to those scans. There are at most B² pairs. This gives D B³N, including the final compaction pass. Every distinct set retains a representative formula, so no set is lost. A cardinality pass scans each bit vector and stores its count in a field of at most h bits. A selection-sort implementation repeatedly scans the unselected records, compares cardinality/ordinal pairs, and copies the selected record into a second set file. Even the more wasteful implementation that obtains every compared record by a full seek uses at most D B³N². Thus no unproved bound on random-access sorting is used.

### 3.4 State enumeration and compatibility

Fix W. A representative described set F and an m-element subset Z determine L=W∩F and R=W\(L∪Z). There are at most B·binom(N,m)≤S choices. Reject Z outside W, intersections Z∩L, non-antichains, and the forbidden precedence pairs specified in Section 2. These checks are finite tests over the N-bit vectors and the N² reachability bits. The deliberately slow implementation considers every ordered job pair, fetches its relation with an O(N²) matrix scan, and checks the relevant membership bits; the complete check is O(N⁴). Fetching the set records and checking acceptance of L and R costs at most D BN². This gives D BS(BN²+N⁴) over all W. Accepted smaller-set schedules are not fetched during every state test; only their acceptance bits are needed.

### 3.5 State-graph propagation

Initialize reached flags on the initial states, with null predecessor. During each pass through ordered pairs (u,v), fetch both records, test reached(u), unreached(v), and L_u∪Z_u⊆L_v, then test acceptance of L_v\(L_u∪Z_u). On the first successful transition to v, set reached(v) and its predecessor to u. Do not replace the predecessor of an already reached state. This makes predecessor links point to states reached earlier and prevents a spurious predecessor cycle.

Fetching/updating state records takes at most D SN. A complete acceptance query takes at most D BN². Any compatibility recheck is at most D N⁴. Since m≥3,

BN²≤BN^(m+1)=SN, and N⁴≤BN^(m+1)=SN.

Thus a complete pair test is at most 3D SN. Every reachable vertex has a simple path of at most S−1 edges. Induction on path length shows that after S full pair passes every reachable vertex is marked, including for the asynchronous within-pass updates used here. The cost is therefore at most

B · S · S² · 3D SN = 3D B S⁴ N = 3D B⁵ N^(4m+1).

The strict inclusion |L_v|≥|L_u|+m also shows that this graph is acyclic. That fact provides the sharper witness-path bound used next, but is not needed for the deliberately generous S-pass time bound.

### 3.6 Witness reconstruction and output

Backtrack from a reached final state until an initial state is found. Each transition increases |L| by at least m; hence the path has at most |W|/m≤N/m states. Retrieve each record by scanning the state file, costing at most D SN² for W. Reverse the path records on a work tape. The first left part, each transition gap, and the final right part are accepted smaller sets. There are at most N/m+1 such pieces. Their saved schedules can each be retrieved by scanning at most qBN² symbols, costing at most D BN³ in total for W. Proposition 2.8's disjoint-partition identity proves that the concatenation contains exactly |W| jobs, each once. Append this schedule to the separate witness file, retaining the just-constructed schedule on its work tape. Over B sets this gives the stated D(BSN²+B²N³) row. This argument avoids recursively recomputing smaller witnesses.

For the selected J schedule, use the retained work-tape copy from its reconstruction (J is the unique described set of cardinality N), delete padded identifiers, translate any rank indices back to their original canonical labels, and assign the at most m jobs in a slot to machines in increasing-identifier order. Repeated map scans cost O(N³); output itself uses O(N log(N+1)+N log(m+1)) bits and costs no more. An optimum is written only after the first accepted deadline is found.

## 4. Domination and exact N exponent

Put P=B⁵N^(4m+1). Since m≥3, K≥1, N≥3, and B≥1, every non-DP row is bounded by a fixed small multiple of P. In particular,

- BS(BN²+N⁴)=B³N^(m+2)+B²N^(m+4);
- BSN²+B²N³=B²N^(m+2)+B²N³;
- N⁵, BN³, B³N, and B³N² all have B-exponent at most 5 and N-exponent at most 4m+1.

The largest elementary N exponent outside propagation is m+4, and m+4≤4m+1 for m≥1. This proves all the domination inequalities explicitly. Summing the row coefficients fits the envelope A(m,K) above, because q²=2¹²(m+1)²(K+1)² and the numerical slack in A exceeds 256D after removing the factor C⁵.

Finally,

P=(K512^K)⁵ N^(5mK+4m+1).

This proves Proposition 9.2 with an effective fixed-parameter coefficient and with its witness cost included. The factor accounting is: one B for all described W; one S for graph-propagation passes; S² for ordered pairs; one SN for sequential state-file access. Since S=BN^m, the product B·S·S²·SN is B⁵N^(4m+1). Lemma 2.7 gives B, the state definition in Section 2 and the counting step in Proposition 9.2 give S, and the file layout above gives the final N.

## 5. Input-length accounting and the corrected exponent

Parse the canonical input once. Repeated full scans suffice to validate identifiers, detect repeated arcs, construct the canonical graph, compare the signed binary deadline against 1 and n, and calculate mT for the nontrivial branch. This takes at most P_m(L+2)⁴ steps for P_m=2³⁰(m+1)⁴. For instance, at most L² pairs of tokens are compared, each by at most O(L) scans, and all unary/binary conversions and adjacency writes fit another factor L. This is deliberately coarser than necessary. Noncanonical large identifiers can be renamed within the same bound. The original input is never assumed to have length bounded by N.

For T<1, reject the nonempty instance. For T≥n, produce the topological schedule of n jobs one per slot directly from the original arc list. There are at most n removal stages and n candidate vertices per stage. For one candidate, scan the original arc list; endpoint comparison and lookup of a predecessor in the length-n active vector cost at most O(L²) over that scan. Thus this direct topological procedure takes O(n²L²)≤O(L⁴), without invoking the padded N⁵ preprocessing. Both elementary branches cost at most P_m(L+2)⁴, including their O(n(log n+log m)) output. For 1≤T<n reject n>mT; otherwise N=mT≤mn≤mL. This avoids expanding a large binary deadline.

Set K_m=12m+25 and

e_m=5mK_m+4m+1=60m²+129m+1.

The actual padded call takes at most A(m,K_m)N^e_m. The prescribed optimization procedure tries T=1,...,n, stopping at the first acceptance. Each trial has N≤mn and there are at most n≤L trials. Its padded work is at most

A(m,K_m)·n·(mn)^e_m ≤ A(m,K_m)m^e_m(L+2)^(e_m+1).

Input handling and the final witness cost have degree at most 4; e_m+1≥929 for m≥3. Thus all three tasks fit

G(m)(L+2)^(60m²+129m+2),

where G(m)=A(m,12m+25)m^(60m²+129m+1)+2³¹(m+1)⁴ is one effective coefficient bound. The +2 exponent comes from the +1 in e_m and one further factor L for the deadline trials. For a single already specified nontrivial deadline, the same accounting gives input exponent e_m; the common bound covering optimization is e_m+1. This is an upper bound established by the specified algorithm, not an assertion of optimality of that exponent.

The corrected table is:

| m | K_m | padded N exponent | common input L+2 exponent |
|---:|---:|---:|---:|
| 3 | 61 | 928 | 929 |
| 4 | 73 | 1477 | 1478 |
| 5 | 85 | 2146 | 2147 |
| 6 | 97 | 2935 | 2936 |

Equation (1.1), Corollary 9.3, the abstract, the Status table, the record block, and the small-m table must use +2 consistently. Equation (1.2) remains +1. The phrase “after padding” should explicitly say that its N-only accounting starts from the parsed canonical padded DAG; the complete input-reading cost belongs to the L bound.

## 6. Compact-isolated input (Proposition 9.4)

Use a compact encoding with n and T in binary and an explicit arc list whose endpoint labels are binary integers in [n]. Let d be the number of distinct endpoints. List and rename them by repeated input scans, in polynomial time in this encoding length. Every nonisolated vertex is among them, hence d≤2|E|. Reject n>mT or T<1 for the nonempty input.

For T≥d, topologically schedule the d incident vertices one per slot. There are mT−d unused machine-slot positions and n−d isolated jobs, and mT−d≥n−d. Assign the isolated jobs injectively to unused positions. This gives a complete existence proof; the decision machine need not enumerate those jobs.

For T<d, n≤mT<md≤2m|E|. Therefore explicitly enumerating all n vertices and padding to N=mT produces a graph polynomial in the compact input length for fixed m. The Section 9 decision computation then applies to that canonical expansion. The implication from the expanded decision answer back to the compact instance is exactly the deletion/insertion correspondence of Lemma 2.3. Each input-label comparison costs at most the compact input length, already charged in the input preprocessing. Outputting an explicit schedule may require Ω(n) identifiers; Proposition 9.4 claims decision time only.

## 7. Section 9: step-by-step logical audit and Uses corrections

### Theorem 9.1

**Step 1: acceptance and witness.** The state path stored by the finite computation gives the ordered disjoint partition (2.3). Proposition 2.8 concatenates the saved schedules of its accepted smaller gaps and the path's m-element slots. Its compatibility checks exclude every precedence directed from a later piece to an earlier one. This proves soundness and the returned witness claim.

**Step 2: completeness composition.** Theorem 8.5 produces a hierarchy with the same globally enumerated atomic language and the same budget K_m. Lemma 2.10 sends each marked slot to a state and sends its intervening child gaps to accepted smaller sets. At the root this is an accepting state path for J. The formulas and parameter K are identical on both sides of this composition; there is no extra promise on the actual finite search.

**Step 3: padding.** Lemma 2.3 inserts isolated jobs into all vacant machine-slot positions and deletes them in the reverse direction. The maps preserve each original precedence pair because they change none of the original slot indices. Thus acceptance of padded J has exactly the deadline meaning used in the theorem.

**Step 4: elementary deadlines.** A nonempty schedule needs a positive slot, so T<1 fails. Lemma 2.1 supplies a topological order, and its one-job-per-slot schedule finishes in n slots. Hence T≥n is answered without constructing mT padding jobs. The capacity inequality n≤mT is necessary for the remaining branch.

**Step 5: optimization.** Lemma 2.1 guarantees a feasible deadline n. The integer slot convention and Lemma 2.2 put the optimum among 1,...,n even when real starts were originally allowed. Testing all these deadlines in increasing order and returning the first accepted witness therefore returns an optimum. Assigning distinct machine indices within each slot changes no slot or precedence inequality.

**Uses line.** Explicitly list Lemmas 2.1, 2.3, 2.10, Proposition 2.8, and Theorem 8.5. Include Lemma 2.2 when the theorem is presented as covering the original real-start scheduling convention. The current line omits the elementary topological-order reference.

### Proposition 9.2

**Step 1: finite formula count.** The full binary-tree and leaf-alphabet count in §3.2 yields B=K512^K N^(mK). This is Lemma 2.7 with every multiplicative factor accounted for.

**Step 2: state count.** Choosing a represented left-set formula and an m-element subset Z uniquely specifies L and R for fixed W; the tests only discard candidates. Hence S=BN^m bounds all retained candidates, including duplicates. The computation never guesses any further boundary data.

**Step 3: storage and access.** The separate files in §2 have exact length envelopes qBN, qSN, and qBN². Full scan access, including ordinal comparison, has the costs used by the propagation calculation. The bit length of each ordinal is bounded before it is treated as part of a record.

**Step 4: graph propagation.** S complete passes suffice by induction on simple-path length. The pair test is charged to the actual sequential data access and acceptance-query routine. The product B·S·S²·SN is exactly B⁵N^(4m+1), as §3.5 proves.

**Step 5: all remaining operations.** The eight rows of §3 cover preprocessing, formula generation and evaluation, deduplication, ordering, state construction, propagation, backtracking, and output. §4 proves every domination inequality. No unspecified “lower-degree polynomial” remains.

**Uses line.** Lemmas 2.1, 2.7, and Proposition 2.8; definitions of the state/transition procedure in Section 2. Lemma 2.1 supplies rank preprocessing; Proposition 2.8 supplies the disjoint witness concatenation. The syntactic and table cost derivations themselves use no structural theorem.

### Corollary 9.3

**Step 1: parameter substitution.** K_m=12m+25 is the budget established in Lemma 8.4 and Theorem 8.5. Substitution gives 5mK_m+4m+1=60m²+129m+1 by distributivity, with terms 60m²,125m,4m,1.

**Step 2: encoding bound.** Explicitly listing every vertex gives n≤L. The only padded branch satisfies N=mT≤mn≤mL. Replacing N by mL introduces m^e_m into the coefficient, which is a function of fixed m.

**Step 3: all deadlines and input costs.** At most n≤L trials introduce one additional power of L. The parser and output costs have degree at most 4, below e_m+1. The coefficient G(m) and the resulting +2 exponent are displayed in §5.

**Uses line.** Proposition 9.2, Theorem 9.1 (deadline procedure), Lemma 2.3 (padding bound), and Lemma 8.4/Theorem 8.5 (value of K_m). The current “no numbered statement” line should be replaced.

### Proposition 9.4

**Step 1: early capacity test.** n≤mT is necessary because there are mT available machine-slot positions. T≥1 is necessary for a nonempty job set.

**Step 2: large deadline.** The incident-vertex count d and topological order give a schedule using one slot per incident vertex. Every remaining job is isolated, and the explicit inequality mT−d≥n−d proves that distinct vacant positions suffice.

**Step 3: short deadline.** T<d and d≤2|E| yield N=mT<2m|E|. The early capacity check also gives n≤N, so the compact job universe can be expanded completely in polynomial time before invoking the padded decision procedure.

**Step 4: output qualification.** A literal list of n scheduled vertices contains at least n symbols. Thus the polynomial compact-input claim here concerns the Boolean decision computation. Its proof does not promise the compact input can always be accompanied by a short explicit output list.

**Uses line.** Lemma 2.1, Lemma 2.3, Theorem 9.1, and Proposition 9.2 (or Corollary 9.3 after canonical expansion). The current “no numbered statement” line should be replaced.

## 8. Program record

`code/A_check_accounting.py` verifies the exponent expansion, the small-m table, and the algebraic dominance of every table row over all integer m≥3 and K≥1 by checking the resulting nonnegative coefficient expressions. Its output is `code/A_check_accounting.out`. The program checks arithmetic and the symbolic inequalities; the tape implementation and the logical proof are the arguments above.

<!-- END A_accounting.md -->

---

## Part B — full independent audit of Sections 2–5.4

Source record: `work/B_foundations.md`. Full text follows.

<!-- BEGIN B_foundations.md -->

# Independent proof audit: Sections 2–5.4

Checker: GPT-6 Astra (OpenAI), effort ChatGPT Pro mode. Date: 15 November 2026, Europe/Berlin. The checker had the post and original return; the three previous reports were available as provenance but were not used as premises. The arguments below were derived from the definitions. Section and equation numbers refer to the post, whose numbered statements retain the return's numbering.

## Lemma 2.1 — proved as stated

**Step 1, the strict order.** A positive directed closed walk contains a directed cycle: select a repeated vertex with a shortest positive segment between equal occurrences. Acyclicity therefore excludes x≺x. Concatenating the paths witnessing x≺y and y≺z gives a positive walk from x to z; deleting repeated segments gives a path. This proves transitivity on precisely the explicitly given vertex set.

**Step 2, preservation of inequalities.** For a path v₀,…,vₖ, the arc inequalities give τ(v₀)<…<τ(vₖ), hence the endpoint inequality. Conversely an arc is a path of length one. The identity map on schedules is therefore a bijection between schedules respecting all arcs and schedules respecting the transitive closure.

**Step 3, the rank map.** In every nonempty remaining induced order, following an alleged predecessor forever repeats a vertex, so a minimal vertex exists. Remove the least identifier among minimal vertices. A predecessor x of y cannot remain when y is removed, since otherwise y is not minimal in the transitive restriction. The removal-position map λ:V→[n] is a bijection with x≺y⇒λ(x)<λ(y). The tie rule makes the function deterministic. Padding adds isolated vertices, so the argument also produces the required λ:J→[N].

## Lemma 2.2 — proved as stated

**Step 1, augmented graph.** On a machine, unit processing and no overlap imply s(v)≥s(u)+1 for consecutive jobs in increasing real start time. Each precedence arc has the same inequality. Summing around a directed cycle would give s(u)≥s(u)+k for k>0, so the augmented graph is acyclic.

**Step 2, integer recurrence.** Process the augmented graph in topological order and define s′ by the maximum in the post. Every predecessor has already received an integer, so the recurrence is defined and integer valued. Induction gives s′(u)+1≤s(u)+1≤s(v) for every incoming arc; the zero term is ≤s(v) by nonnegative original starts. Hence s′(v)≤s(v).

**Step 3, explicit schedule transformation.** Preserve the original assignment μ and set τ(v)=s′(v)+1. Consecutive jobs on a machine are separated by at least one unit, and transitivity extends this to all pairs on that machine. Original precedence arcs are respected as well. Every new completion time is τ(v)≤s(v)+1. The transformation is explicit; it preserves feasibility and weakly decreases makespan. The reverse embedding of an integer-slot schedule uses start τ(v)−1 and any injective assignment of each slot's jobs to machine labels.

## Lemma 2.3 — proved as stated

**Step 1, capacity.** A map to T slots with at most m jobs per slot contains at most mT jobs. Thus n>mT is an exact rejection test.

**Step 2, extension.** Label the dummy vertices n+1,…,mT. Enumerate empty machine/time positions in lexicographic (time,machine) order and fill them with these dummy vertices in identifier order. The dummies have no order relations, so the resulting partition of J consists of T antichains of size m and respects every original relation.

**Step 3, restriction.** Restrict any full schedule of J to V. Every slot now contains at most m jobs, and each original arc still has increasing slot numbers. This gives both directions of the required feasibility equivalence. The bound N=mT≤mn follows from T≤n. An optimization implementation need only pad T<n, since a topological schedule handles T≥n.

## Lemma 2.4 — proved as stated

**Step 1, fixed interval length.** Every full schedule of W uses |W|/m slots, and W originally occupies exactly that many consecutive slots. Thus substitution has a well-defined position-preserving map outside the interval and a bijective assignment of W to the same interior slots.

**Step 2, every precedence case.** A relation with both endpoints inside W is respected by the substituted full schedule. A relation with both outside has unchanged times. With one endpoint outside, its time lies on one fixed side of the entire interval; every possible new time of the inside endpoint stays on the other side of that boundary. Feasibility of the original witness fixes the permitted direction. This checks all ordered pairs in the transitive relation, including those whose original graph paths leave W.

## Frames, cones, and the normalization selector

**Reversal map.** For a T-slot full schedule τ, define Rτ(x)=T+1−τ(x), reverse the strict relation, and replace λ by N+1−λ. The inequalities reverse exactly, slot sizes are preserved, and R² is the identity. Under this bijection P in one frame is D in the other, with the same equality for weak cones. No comparison of frames is used without these explicit transformations.

**Cone closure.** For x∈D_a and x≺y, a witness u∈a with u≺x also satisfies u≺y. The same proof includes x∈a for the weak cone. Reversing arrows proves closure of P_a and its weak version. Taking complements reverses the closure implication. A rank suffix is closed upwards because ranks increase on ≺. These arguments hold even for the m-subsets enumerated as atoms that are not antichains; Lemma 2.5 separately uses the antichain property for time.

**Exact selector used by the existence proof.** For each schedulable W and priority bijection π, the finite set of full schedules is nonempty. Map each schedule to the concatenation of its sorted priority tuples. Because π is injective, this encoding determines the ordered sequence of job sets uniquely. Select its lexicographically least element, then decode using π⁻¹. This defines the normalization map used in Section 3. It stays in the feasible set and changes the exterior only through the interval-replacement map of Lemma 2.4. The finite search of Section 2 does not evaluate this selector; the selector constructs its completeness certificate.

## Lemma 2.5 — proved as stated

**Step 1, strict cones.** Membership x∈P_a provides y∈a with x≺y, so τ(x)<τ(a); membership x∈D_a similarly gives τ(x)>τ(a). Equality of times would violate feasibility. Since the slot is an antichain, neither strict cone contains a member of a.

**Step 2, weak and virtual versions.** Adding the slot gives the corresponding weak temporal implications. For the virtual position 0, D=J and P=∅ satisfy them directly; for position T+1 the prescribed sets are reversed. These conventions are the ones used whenever a boundary in a subsequent formula is virtual.

## Lemma 2.6 — proved as stated

**Step 1, recursive map on formula trees.** Define c on leaves by toggling the permitted complement flag, and define c(F∩G)=c(F)∪c(G), c(F∪G)=c(F)∩c(G). Structural induction gives [c(F)]=J\[F]. Each leaf maps to one leaf, so the leaf-count function is preserved exactly. In particular, F\G is represented by F∩c(G) with the sum of the two leaf counts.

## Lemma 2.7 — proved as stated

**Step 1, alphabet.** Counting generously, the two constants, thresholds in both frames, five subset/cone types in both frames, and complement flags give at most 4+8(N+2)+20·binom(N,m) atoms. For N≥m≥3, this is ≤64N^m. Treating coincident evaluated atoms as different syntactic choices only increases the bound.

**Step 2, trees and labels.** An ordered full binary tree with ℓ leaves has ℓ−1 internal vertices; its count is the Catalan number C_(ℓ−1)≤4^(ℓ−1)≤4^ℓ. There are 2^(ℓ−1) operation assignments and at most (64N^m)^ℓ leaf assignments. Their product is ≤(512N^m)^ℓ. Summing for 1≤ℓ≤K gives B=K512^K N^(mK), exactly the constant used in the cost audit.

**Step 3, actual enumeration.** Enumerate the finite tree encodings and labels, evaluate each leaf from the reachability relation and rank, and combine bit vectors at internal vertices. Equality is bitwise equality on J; keeping the earliest representative for each vector preserves precisely the image of the evaluation function. The separate Part A analysis supplies tape costs for this construction and pairwise deduplication.

## Proposition 2.8 — proved as stated

**Step 1, well-founded acceptance.** Each state contains a nonempty m-slot Z. Its L and R omit Z. Each transition gap L′\(L∪Z) also omits Z, and therefore has size less than |W|. Processing cardinalities increasingly makes every lookup either an already computed value or the stipulated false value outside the family. The empty schedule starts the induction.

**Step 2, partition induced by a path.** The inclusion Lᵢ∪Zᵢ⊆Lᵢ₊₁ gives Lᵢ₊₁=(Lᵢ⊔Zᵢ)⊔Aᵢ by the definition of Aᵢ. Induction expands this into the prefix of (2.3). At the last state, W=L_k⊔Z_k⊔R_k closes the partition. These equalities prove that no job is repeated or omitted; successive left sets also have strictly increasing sizes, so a path cannot cycle.

**Step 3, precedence across the partition.** A later marked slot Zⱼ has every earlier piece inside Lⱼ, and state compatibility excludes Zⱼ≺Lⱼ. A later gap Aⱼ is contained in Rⱼ, whereas every earlier piece is contained in Lⱼ∪Zⱼ; the two compatibility conditions exclude all such backwards relations. Internal relations are respected by the inductively supplied schedules. Concatenation therefore gives a full schedule of W.

**Step 4, witness map.** Store a predecessor state only at its first successful discovery, together with the accepted smaller-set witnesses. Backtracking produces the finite state path; concatenate the stored gap schedules and the explicit Z slots in order. The established disjoint partition bounds its output by |W| job occurrences. This is an explicit decoding map from an accepting path to a schedule, requiring no selection from an unrecorded feasible set.

## Definition 2.9 — well-defined and used with its stated meaning

**Step 1, separate witnesses.** At each node the interval is a subset of the same global job universe J and inherits its full transitive relation. Children receive copies of the current full witness. Rescheduling a descendant in one copy does not change an ancestor's sets, labels, formulas, or another branch's witness. Every child omits a marked m-slot, reducing |W|/m by at least one. Finite branching and this integer depth bound give a finite tree.

## Lemma 2.10 — proved as stated

**Step 1, states from marks.** At mark zᵢ, use its actual original-time prefix Lᵢ and suffix Rᵢ. The hierarchy provides the required relative formula. Feasibility of the node witness excludes every backward relation in the state tests. Thus every such triple is among the candidates enumerated by the dynamic program.

**Step 2, acceptance by size induction.** The first prefix, final suffix, and gaps are exactly empty sets or child nodes. Their acceptance follows from the empty base value or the induction on smaller node sizes. Consecutive marks satisfy Lᵢ∪zᵢ⊆Lᵢ₊₁, with the accepted child as difference. These triples form an initial-to-final path. Induction therefore accepts the root J.

## Lemma 3.1 — proved as stated

**Step 1, prefix inclusion.** For a job before z, a high job is in P_z by separator clause (a); a low job is in H and outside the weak successor cone by its strict earlier time. Both cases enter B_z(H).

**Step 2, reverse inclusion.** A P_z job is strictly earlier by Lemma 2.5. A job in U∩H\widehat(D_z) is low and neither at z nor after z: the first is excluded by the weak cone and the second by separator clause (b). Therefore B_z(H)∩U equals the exact prefix. No membership information about H outside U is needed.

## Lemma 3.2 — proved as stated

**Step 1, explicit transformation.** Apply time reversal R, order reversal, and the cutoff map S↦U\S. Closure of S downwards makes its complement closed downwards in the reversed order. Original low-after/successor clause (b) becomes high-before/predecessor clause (a); original clause (a) becomes clause (b). Each transformation is an involution, proving the equivalence in both directions.

## Lemma 3.3 — proved as stated; rewritten layout preserves the argument

**Step 1, unchanged prefix.** Suffix replacement keeps all slots through r fixed. Swapping y at r with x in that suffix subsequently changes only r and the slot of x. Thus the encoded schedule agrees with the minimizing schedule in every coordinate preceding the r tuple.

**Step 2, sorted tuple comparison.** Let α=π(x)<β=π(y). Replacing β by α weakly increases the count of tuple entries ≤q for every q, since its change is 1_(α≤q)−1_(β≤q)≥0. For each order-statistic index k, the smallest threshold with at least k entries therefore weakly decreases. The sum decreases by β−α>0, so at least one coordinate decreases strictly. The first changed tuple coordinate consequently decreases. This proves the comparison for every m, with the concrete map on multisets and sorted coordinates given explicitly.

**Step 3, minimizing contradiction.** Feasibility of the hypothesized exchange would place the new encoded schedule inside the same finite comparison set, with the same earlier coordinates and a smaller first changed coordinate. That contradicts the selected minimum. Suffix reordering is already included in this comparison, so later uses retain precisely the lemma's quantifier.

**B.2 concordance.** The return's Lemma 3.3 has one paragraph: unchanged earlier slots; replace a larger priority by a smaller one; all order statistics weakly decrease and one strictly; contradict minimality. The post's Steps 1, 2, 3 are this same sequence. Its threshold-count and sum sentences supply a proof of the order-statistic assertion rather than changing its hypotheses or conclusion. The “where m enters” sentence only records that the tuple length is arbitrary. The report records this as a full semantic comparison, not a character-for-character identity.

## Lemma 3.4 — proved as stated

**Step 1, predecessors of the earliest exception.** For w≺x in U, precedence extension puts w in L, and feasibility puts w before t. A w at s would witness x∈D_s. A w between s and t would itself be an earlier L job; minimality of t forces w∈D_s, again giving x∈D_s by transitivity. Thus every such w is strictly before s. When s is the exterior boundary, the same alternatives exhaust the jobs of U before t.

**Step 2, first forced successor.** Take high y at r with s≤r<t. Absence of any successor of y through time t makes the swap x↦r,y↦t feasible: all predecessors of x are before s; all its original successors are after t; predecessors of y are before r; and its alleged successors are after t. These inequalities also exclude conflicts with companions in the destination slots. Exterior jobs remain on their original side of U. Because x∈M and y∉M, their priorities improve the earlier slot, contradicting Lemma 3.3. Thus y has a successor no later than t.

**Step 3, propagation to t.** A successor of a high job remains outside the prefix M. Repeat the preceding swap argument for that successor when it occurs before t. Its time increases strictly at each iteration, so the finite sequence reaches t. Transitivity gives a strict successor of the original y at t, proving conclusion (2).

**Step 4, all high jobs before t.** A high job at or after s uses conclusion (2). A high job before s has a successor w in the s slot by clause (a). Closure of the high set puts w outside M, and conclusion (2) moves its witness to t. Transitivity then puts the original job in P_t. An exterior s has no U jobs before it, so that alternative is vacuous. This proves clause (a) at t.

## Lemma 3.5 — proved as stated

**Step 1, invariant and termination.** Use Lemma 3.4 with M=L at each earliest-exception move. It preserves clause (a), and every target is strictly later. The number of positions is finite. At the last position absence of exceptions is exactly clause (b). An already separating position has no exception, so its image under the walk is itself.

## Lemma 3.6 — proved as stated

**Step 1, the first move.** Enlarging S to S∪{p} removes one high job, preserving clause (a). All old low jobs after s are already in D_s. Thus any first exception is exactly p; the first target is p's slot. Lemma 3.4 with M=L=S⁺ proves clause (a) for S⁺ there. Adding p back to the high set changes no before-target condition because p is at that target, proving clause (a) for S as well.

**Step 2, later moves and stopping.** Every later exception lies after p's slot, so it belongs to S. Lemma 3.4 applies with M=S,L=S⁺, and also with M=L=S⁺, preserving both versions of clause (a). At the terminal position clause (b) for S⁺ implies clause (b) for S by inclusion. The no-move case already satisfies both clauses. Restricting a priority prefix from W to U preserves its order-prefix property; promoting a vertex outside U changes no restricted set and therefore yields the identity walk.

## Corollary 3.7 — proved as stated

**Step 1, admissible priority.** Place S first and U\S second, ordering each by rank. A relation from the second block to the first contradicts the downset property of S. Within each block rank extends precedence. This is a legitimate total priority order.

**Step 2, separator construction.** Apply the explicitly defined normalization selector to a feasible schedule of U. Its first slot separates the empty cutoff because there are no earlier jobs and no low jobs. Promote S in priority order and apply Lemma 3.6 at each promotion. Positions stay genuine slots and never decrease, and the final one separates S. Nonemptiness of U guarantees a first slot.

## Lemma 4.1 — proved as stated

**Step 1, the order map.** Every entry containing x also contains y for x≺y. Hence the largest index M(y) is at least M(x). A strict index increase gives the lexicographic inequality, and equal indices give it from λ(x)<λ(y). The map x↦(M(x),λ(x)) is injective because λ is injective; this justifies every minimum-key choice.

## Lemma 4.2 — proved as stated

**Step 1, tag frame.** I1 partitions W into O⊆P_b and W\O⊆D_a. Thus W⊆D_a∪P_b. Removing D_a leaves X⊆P_b; removing P_b leaves Y⊆D_a. Both X=W∩(J\D_a) and W∩P_b are relative downsets by the cone closure argument above.

**Step 2, reversed frame.** Under reversal, the new a is old b and the new b is old a. New D_a=old P_b and new P_b=old D_a. Substitution in the displayed inclusions interchanges X and Y and leaves the cover unchanged. The same closure argument proves the new cutoffs. Thus the claim really holds in either working frame.

## Lemma 4.3 — proved as stated

**Step 1, same-side blocks.** Since O⊆P_b, the three sets S₀=(W\O)∩P_b, O, and Y=W\P_b are disjoint and cover W. A predecessor in W of x∈S₀ is in P_b, and qualification of that predecessor would force qualification of x; hence it lies in S₀. Also no Y vertex precedes a P_b vertex. These facts exclude relations backwards between blocks. Ranks order S₀,Y and Lemma 4.1 orders O.

**Step 2, same-side prefixes.** Adding O in increasing key order makes each Sᵢ an initial segment, ending at W∩P_b. Every Sᵢ is therefore contained in P_b. The initial S₀ lies in D_a by I1 because it contains no qualifier.

**Step 3, switched-side order.** X is a downset by Lemma 4.2, so placing it before W\X and sorting each by the working-frame rank respects precedence. Promotion by rank gives all and only the prefixes of X, ending at X⊆P_b. The initial cutoff ∅ is contained in D_a.

## Construction before Lemma 4.4

**Center and side maps.** Corollary 3.7 gives a separator for W∩P_b in the tag frame; Lemma 2.4 installs that schedule. Reversal sends its cutoff to W\D_a on the switched side by Lemma 3.2. Each open side E is then replaced by its normalization-selector output for the restricted priority order. Jobs on each side of the fixed center are unchanged as sets, and its separator clauses quantify exactly these sets, so its separator property survives. Root center selection at the last slot separates J directly and leaves no switched side.

## Lemma 4.4 — proved as stated

**Step 1, common endpoint labels.** The left boundary a separates S₀∩E because S₀⊆D_a. After promotion i, Lemma 3.6 makes sᵢ a separator for Sᵢ₋₁ and Sᵢ. Thus sᵢ and sᵢ₊₁ both separate Sᵢ. Repeated positions satisfy the same conclusions. The final center's separator clause (a) on W puts every high job of its earlier side E in P_v.

## Lemma 4.5 — proved as stated

**Step 1, exact gap enumeration.** A nondecreasing finite sequence has one transition between each pair of consecutive distinct values; take the last occurrence of the earlier value and the next index. These are precisely the strict steps sᵢ<sᵢ₊₁ used for children. Its right endpoint is always an actual side slot or the center, and its left endpoint is a side slot or a.

**Step 2, labels and shrinking.** A low child job lies after a′, so the separator clause (b) there puts it in D_a′. It also lies in Sᵢ⊆P_b by Lemma 4.3. A high child job lies before b′, so Lemma 4.4 puts it in P_b′, including the center endpoint. Every child omits the center's m jobs, proving strict decrease. At the root the center is last, so no switched child can occur.

## Lemma 5.1 — proved as stated

**Step 1, qualifier identity.** Let j be the greatest old entry containing a job. With j>d, that entry survives; with j=d, survival is exactly λ≥r; with j<d, all entries containing the job were deleted. These alternatives are equivalent to old key≥(d,r), including arbitrary exterior jobs.

**Step 2, order transfer.** For each surviving job the exact key map is (j,λ)↦(j−d+1,λ). Subtracting the same integer from the first coordinate preserves and reflects every lexicographic comparison. The trimmed entry stays upward closed because rank suffix and old entry are both upsets; the other entries are unchanged.

## Lemma 5.2 — proved as stated

**Step 1, effect of deletion.** Let M(z) and R(z) be respectively the largest old and retained old indices containing z. Because x∈W′, every entry containing x meets W′ and is retained, so R(x)=M(x). For exterior y only R(y)≤M(y) is guaranteed. The increasing relabeling of retained indices preserves the comparison of R values.

**Step 2, both key cases.** R(x)<R(y) yields M(x)<M(y). When R(x)=R(y) and λ(x)<λ(y), either M(y) exceeds that index or equals it; the first alternative decides by index and the second by rank. This proves exactly the one-way inequality needed in Lemma 7.2, with its required hypothesis x∈W′.

## Lemma 5.3 — proved as stated

**Step 1, same update.** By the cutoff promotion order and Lemma 5.1, the carry intersects W in O\S and preserves that group's keys. Lemma 4.2 gives W∩(D_a\P_b)=W\P_b=Y. Since Y∩O=∅, the appended injection contributes exactly the last priority block, with its last index overriding no carry job inside W. Hence the union is (O\S)⊔Y=W\S, with precisely the restricted side-priority order.

**Step 2, switched update.** On X, G contains every job, so G∩{λ≥h} selects exactly X\S. On W\X, the second entry D_a contains every job and its larger index determines their keys even when they also lie in G. Thus these two groups have the required order and union W\S. This uses exactly the G properties later constructed in Lemma 6.4; Proposition 7.3 establishes the induction order, so it is a proved update identity for that construction.

**Step 3, pruning and I1.** Deleting entries disjoint from W′ does not change qualification there. Therefore O′=W′\S. Lemma 4.5 puts that set in P_b′ and its complement in W′ in D_a′. These are precisely child I1. The original Uses line omitted Lemma 4.5, a genuine direct dependency.

## Lemma 5.4 — proved as stated

**Step 1, exact entry-history map.** Give each initial entry and each appended injection a persistent birth label. Same-side updates only delete such labels or intersect the surviving set with a rank suffix. For two suffixes the identity {λ≥r}∩{λ≥r′}={λ≥max(r,r′)} follows pointwise from the two integer inequalities. Hence a surviving birth set is intersected with at most one effective suffix. A switched update deletes all preceding birth labels and begins a new run, so all thresholds combined in this identity use one and the same rank map.

## Direct dependency corrections for Sections 2–5

The revised Uses lines name direct numbered results, plus definitions or invariants that are genuinely used. Lemma 2.2 uses Lemma 2.1 for the augmented topological order. Lemma 2.7 uses Lemma 2.1 and the Section 2.1 atom definitions. Proposition 2.8 uses only Section 2.2 definitions and size induction. Lemma 2.10 uses Definition 2.9 and Section 2.2. Lemma 3.5 uses Lemma 3.4. Lemma 3.6 uses Lemmas 3.4 and 3.5 for the specified finite walk. Lemma 4.4 uses Lemmas 3.6, 4.3 and the center construction. Lemma 4.5 uses Lemmas 4.3, 4.4 and Definition 2.9 for identification of gaps. Lemma 5.3 uses Lemmas 4.2, 4.3, 4.5 and 5.1, I1, and the expressly displayed property (5.3) of G. Its text need not cite the later Lemma 6.4 as a lemma available in the local proof order: Section 7.3 proves that property before applying the update. No forward logical dependency on a descendant is introduced.

## Present verdict

All numbered statements through 5.4 are proved with the stated definitions. No wrong mathematical step was found in this range. The missing Uses entries are documentation repairs. The explicit input model and running-time repairs are recorded separately in Part A. The independent review of 5.5–8.5 supplies the remaining structural checks.

<!-- END B_foundations.md -->

---

## Part B — full independent audit of Sections 5.5–8.5

Source record: `work/B_hard.md`. Full text follows.

<!-- BEGIN B_hard.md -->

# Independent step-by-step audit of Sections 5.5–8.5

Checker: GPT-6 Astra (OpenAI), effort ChatGPT Pro mode. Date: 15 November 2026. The arguments below were checked directly from the supplied post and its definitions, before reading the earlier checker verdicts. The supplied mathematical return was opened for the requested textual concordance of Lemma 5.5. No earlier checker verdict is used as a mathematical premise.

Each numbered paragraph below confirms the corresponding logical step with its hypotheses and set maps made explicit. The finite-program results at the end supplement these arguments. All assigned statements have been checked; no false mathematical step was found in Sections 5.5–8.5.

## Lemma 5.5 — at most m injection descendants

**Verdict: confirmed, with one wording clarification.** In Step 2 replace “let x_K be its job of least rank” by “let x_K be the least-rank job of K∩W′.” The latter states the chosen domain explicitly and is exactly the choice in the producing return.

1. Fix the child edge W→W′ and retain the injection entries with their creation-event identities, even when two evaluated subsets happen to be equal. Let K be older than K′ and let U→U′ be the edge that created K′. Survival of K to W′ implies that it was retained in the carry out of U. The carry is a list of subsets of the old qualifier union. On U that union is O_U⊆P_{b_U} by I1. The fresh K′ before later trimming is D_{a_U}∩(J\P_{b_U}); hence its intersection with K inside U is empty. Every later operation sends an entry E to itself, to E∩{λ≥r}, or deletes it. Thus the corresponding surviving sets K_final⊆K_then and K′_final⊆K′_then remain disjoint on W⊆U. This proves Step 1 without using a descendant invariant.

2. Pruning retains K precisely because K∩W′ is nonempty. The total rank gives a unique minimum x_K of this intersection. Lemma 5.3 puts this job in W′\S, and (4.6) puts it in P_{b′}. Consequently the set {y∈b′:x_K≺y} is nonempty. Its minimum-rank element f(K) exists and is unique. The entry is an upset of J, so x_K∈K and x_K≺f(K) imply f(K)∈K. This proves Step 2 using the global domain J of the upset; the witness f(K) is outside W′.

3. Lemma 4.5 gives b′⊆W and |b′|=m. For two distinct creation-event identities K,K′, equality f(K)=f(K′) would put this job in K∩K′∩W, contradicting paragraph 1. The specified function f therefore is an injection from the surviving injection identities into the m-element set b′.

4. Injection gives at most m surviving injection entries. A switched creation has only its two initial entries; the root has one. Lemma 5.4 assigns every other entry exactly one injection creation event and never duplicates an entry. Thus adding the possible initial descendants gives at most m+2 entries in every pruned list. A carry out of such a list deletes a prefix and may trim one entry, so it also has at most m injection descendants; the fresh appended injection is counted only after child pruning for the next invariant.

### Concordance with provenance/Q03-solution.md

The return's first proof paragraph (“A new run starts…”) is the post's setup. The return's paragraph beginning “First, any two such entries…” is exactly Step 1, including the containment W⊆U and monotonically shrinking entries. Its next paragraph choosing x_K∈K∩W′ and obtaining a boundary successor is Step 2. Its displayed map f, uniqueness argument, and |b′|=m are Steps 2–3 and the first sentence of Step 4. Its final paragraph adds at most two initial entries, emphasizes the global upset property, and excludes reliance on descendant formulas; these are the rest of Step 4 and the post's final explanatory paragraph. No hypothesis or inference has been removed. The post's antecedent “its job” should be made explicit as above to preserve the return's fully stated selection domain.

## Lemma 6.1 — local replacement of the initial pair

**Verdict: confirmed.**

1. Track the two creation-event identities of the initial pair. A carry retains a suffix of the current list; it trims only the first retained entry. The first initial identity remains earlier than the second at every stage at which both remain. Therefore a carry starting at the second or at an injection deletes the first permanently. Along the history ending at a carry that retains the first, the second has never been the trimmed first retained entry. It remains the original D_{a_0} until pruning deletes it. Pruning deletes it only after its intersection with a node is empty. All later nodes, including U, lie inside that node. A deleted second entry therefore has empty intersection with U.

2. The equality is verified by the inclusion map U→Q_0. On U∩D_{a_0}, the second identity is present whenever this intersection is nonempty, and selects the whole intersection. On U\D_{a_0}, containment Q_0\D_{a_0}⊆G_0 puts every job in G_0. Thus membership in the first surviving identity G_0∩{λ≥k} agrees there with λ≥k. Combining the two disjoint parts proves U∩(union of carried initial identities)=U∩(D_{a_0}∪{λ≥k}). Both displayed factors are upsets, so their union is an upset of J. No inference uses its value outside U.

## Lemma 6.2 — extension of an earlier low cutoff

**Verdict: confirmed.**

1. For a switched edge, H is exactly the initial rank segment of X_U=U\D_{a_U}. The maximum selected rank r (or r=0 for the empty segment) satisfies H=U∩(J\D_{a_U})∩{λ≤r}. The two global factors are downsets in that edge's frame, proving both downward closure and the two-leaf representation of H*.

2. For a same edge, the ordered partition of U is S_0, O_U, Y_U. The low cutoff consists of S_0 and the promoted prefix of O_U; the carry selects exactly the complementary suffix O_U\H. Since U∩P_{b_U}=S_0⊔O_U, subtracting the carry union Φ from U∩P_{b_U} gives H. This proves (6.4) from the actual qualifier identity, with no global assertion about H outside U.

3. Lemma 5.5 bounds the injection identities in the carry by m. Lemma 5.4 represents each by D_{a_V}∩(J\P_{b_V})∩{λ≥r_V}; the suffix may be absent. All three leaves are in the permitted alphabet, and all factors are upsets. Thus their union has a description with at most 3m leaves. A union of nonempty families adds leaf counts and creates no extra leaves at its internal binary union nodes.

4. The initial identities contribute at most two leaves after an equality-preserving replacement on U. In a root run the original J intersected with a rank suffix equals that suffix on all J. In a switched run retaining the first identity, Lemma 6.1 gives D_{a_0}∪{λ≥k} on U; this uses two leaves. When the first identity has disappeared, the second is D_{a_0} with at most one combined suffix, also two leaves. When both disappear there is no initial contribution. These four cases exhaust the ordered initial identities. The global expressions substituted in these cases are all upsets, so their union with the injection expressions is an upset Φ′ with U∩Φ′=U∩Φ and at most 3m+2 leaves. For an empty carry use the one-leaf empty set.

5. Put H*=P_{b_U}∩(J\Φ′). The complement map on formulas of Lemma 2.6 preserves the number of leaves. Thus H* uses at most 1+(3m+2)=3m+3 leaves. Both global factors are downsets, and their intersection with U is (U∩P_{b_U})\Φ=H. This proves all three assertions in the statement: global downward closure, exact restriction to U, and the bound independent of history depth.

## Lemma 6.3 — arrangement at a switch

**Verdict: confirmed.**

1. The root center is its last slot; its switched open side is empty, so a nonempty switched child has a parent W distinct from the root. Let U be W's parent. In the frame that created W, call U's boundaries A<B, its center V, and W's boundaries α<β. Lemma 4.5 and the side construction give A≤α<β≤V<B, with β a genuine slot. Under the explicit time reversal t↦T+1−t, the labels become a_-=rev(B), v_-=rev(V), a=rev(β), b=rev(α), b_-=rev(A). Applying this decreasing bijection to those inequalities gives a_-<v_-≤a<b≤b_- exactly. The image of a genuine slot is a genuine slot, proving the assertion about a.

## Lemma 6.4 — the switch upset

**Verdict: confirmed.**

1. In the current frame, D_{a_-} is an upset; the complements of the two weak predecessor cones are upsets; and H* is an upset because it was a downset in the opposite frame. The identity map on J with reversed order sends a downset in the old order to an upset in the current order. Hence the intersection G in (6.8) is an upset of J.

2. Fix x∈X=W\D_a. The preceding edge U→W was taken in the opposite frame. An old high x would belong by (4.6) to the old predecessor cone of its right boundary. That boundary is current a, and that cone is current D_a. This contradicts x∉D_a, so x is old low and belongs to H. Lemma 4.3 puts H in the old predecessor cone of U's old right boundary, which under reversal is current D_{a_-}. Since x lies strictly after a and a≥v_-, Lemma 2.5 excludes x from current weak predecessor cones at a and v_-. Finally x∈U and H*∩U=H give x∈H*. All four factors defining G have now been verified for x.

3. Let z∈G occur at or before a in the current schedule. The D_{a_-} factor puts it strictly after a_-. The arrangement a<b≤b_- puts z strictly before b_-. These strict inequalities prove z∈U. Therefore the equality H*∩U=H may be applied, yielding z∈H. This localization is essential because equality of H* and H is asserted only on U.

4. For z at or before v_- currently, time reversal puts z at or after U's old center. At the center the weak-cone exclusion directly fails. Strictly after the old center, z∈H⊆S_* and the center separator's low condition put z in the old successor cone of that center, hence in current P_{v_-}. This also contradicts the defining complement factor of G.

5. For v_-<time(z)≤a currently, time reversal puts z before the old center and at or after the old edge's right boundary a. At that boundary z belongs to the weak cone. Strictly after that boundary, z is old low for H, lies on the old side domain E, and Lemma 4.4 makes that boundary a separator for H; it therefore belongs to old D_a=current P_a. The final edge with right boundary at the center has no interval satisfying this strict subcase. In every possible subcase z lies in current widehat P_a, contrary to G's factor.

6. The witness of U supplied these center and separator facts. Between creating W and using its switched side, rescheduling is confined to the open interval W. Jobs at or before current a and all boundary/center slots involved in paragraphs 3–5 remain fixed. The sets H,H* and cones are functions of fixed job sets and precedence. Thus those arguments apply to the current witness. The first switch entry lies inside G, and the second inside D_a; consequently neither has a qualifier at or before a.

## Lemma 6.5 — leaf counts

**Verdict: confirmed.**

1. A surviving injection identity is (D∩(J\P)) intersected with zero or one rank suffix by Lemma 5.4; it therefore uses at most three leaves. A root initial identity is J with zero or one suffix and uses at most two. A switched second initial identity is D_a with zero or one suffix and uses at most two. Combining repeated suffixes is justified by their exact equality {λ≥r}∩{λ≥s}={λ≥max(r,s)} on all J.

2. Formula (6.8) contributes three cone leaves and an H* using at most 3m+3 leaves by Lemma 6.2. Hence G uses at most 3m+6 leaves. Intersecting G with the initial rank suffix adds one, for 3m+7. Later suffix intersections replace that same suffix by the maximum threshold, so the count remains 3m+7 throughout the run. A direction switch deletes these identities before introducing its own initial pair.

3. A pruned list has at most m injection identities and at most two initial identities by Lemma 5.5. Its union therefore has a formula using at most 3m+(3m+7)+2=6m+9 leaves in a switched run. In a root run the same bound covers 3m+2. Taking a carry only discards entries and combines one suffix as in paragraph 1. Empty unions are represented by the one-leaf empty-set atom. Thus A_m=6m+9 applies to every pruned-list union and every carry union, including carries attached to cutoffs whose gaps are empty.

## Lemma 7.1 — exterior qualifier invariant I2

**Verdict: confirmed.**

1. The parent's preparatory rescheduling preserves its three invariants: I1 concerns fixed subsets and fixed boundary slots; I2 concerns exterior jobs whose slots remain fixed; I3 already quantifies over every full schedule of the parent's interval. Pruning removes entries and thus qualifiers, so proving I2 for every qualifier of the pre-pruning list suffices. Fix such z at or before a′.

2. For time(z)>a, all possible positions up to a′ lie in the normalized side E, because a′ is a side position before the center. Lemma 5.3 says every such qualifier in W is high for S_i. A qualifier in slot a′ lies in widehat P_{a′} by membership; a qualifier strictly before a′ lies in P_{a′} by the high condition of the separator at s_i=a′. This proves the first case.

3. For time(z)≤a, an injection qualifier is impossible because its entry lies in D_a. A switch-pair qualifier is impossible by Lemma 6.4 and the successor-cone property for its second entry. Hence this is a same update and z qualifies through its carry. Lemma 5.1 makes z an old qualifier. Parent I2 supplies y∈a with z=y or z≺y. Since the carry union is an upset of J, y also belongs to it. This proves both the existence of a genuine boundary job and its survival through the carry. When a′=a the same witness immediately proves the desired conclusion.

4. Assume a′>a. Every actual advance from a through a′ uses a cutoff S_j⊆S_i, including intermediate unmarked steps. Lemma 5.1 gives carry∩W=O\S_i. Thus every carry qualifier in E is outside every such S_j. At the first advance a→t the chosen exception x∈S_j∩E satisfies x∉D_a. Every predecessor w of x occurs before t. Membership in slot a would directly put x in D_a. A predecessor with a<time(w)<t belongs to E and to the downset S_j. Earliest-exception minimality puts w in D_a, and transitivity then puts x in D_a. Both alternatives are impossible; all predecessors of x in J occur strictly before a.

5. Parent I1 puts x∈O because x∉D_a. Since S_0⊆D_a, x entered the low set by a promotion from O. The carry threshold (d,r) is the least old key in O\S_i; all promoted jobs in S_i∩O have smaller keys. Hence key_old(x)<(d,r). The qualifier y belongs to the carry, so Lemma 5.1 gives key_old(y)≥(d,r). Parent I3 applies to the currently chosen replacement schedule of W, x∈W\D_a, and y∈a, and prohibits their exchange.

6. If y had no successor at or before t, this exchange would preserve every precedence relation: x's predecessors are before a by paragraph 4, its successors are after its old time t, y's predecessors are before its old time a, and its successors would be after t. The sizes of both slots remain m. A companion at either destination slot cannot be comparable in the forbidden direction, because that would be one of the predecessor/successor relations just ruled out. Thus the exchange would be a full schedule, contradicting I3. Therefore y has a strict successor y_1 with a<time(y_1)≤t. The carry is an upset, so y_1 qualifies; it belongs to E and is high for S_j.

7. At time(y_1)=t, the desired successor at the first target is already present. For time(y_1)<t, apply Lemma 3.4(2) to the normalized E with M=L=S_j∩E and exterior position a. Restricting the total priority and prefix to E preserves their prefix relationship. Condition (a) at the exterior boundary has no E-job before it; x is still the earliest exception. The lemma gives a strict successor of y_1 in t, and the upset carry contains it. In either case there is a carry qualifier in t strictly above y. It cannot equal the low x.

8. At each subsequent genuine-slot advance s→t′, the carry qualifier already obtained at s is high for the currently used S_j. Lemma 3.4(2) with M=L=S_j∩E sends it to a strict successor at t′, again in the carry. The walk has finitely many advances and reaches a′. Transitivity gives a job of a′ strictly above y, hence also strictly above z when z=y or z≺y. Therefore z∈P_{a′}. This completes I2 for every pre-pruning qualifier and hence every pruned qualifier.

## Lemma 7.2 — exterior exchange invariant I3

**Verdict: confirmed.**

1. For x∈W′\D_{a′}, child I1 from Lemma 5.3 guarantees qualification. The hypothesis already gives qualification of y after pruning. Lemma 5.2 applies with x inside the pruning domain W′ and transfers key_child(x)<key_child(y) to the pre-pruning list, including the possibility that y belonged to deleted exterior entries.

2. For a′>a, the slot a′ lies in normalized E. Both x and y lie in W, so Lemma 5.3 transfers the pre-pruning comparison to the priority order of E. The arbitrary replacement of W′ lies entirely after a′ and is a full replacement by Lemma 2.4. It changes no job at or before a′ and preserves the set of E-jobs after a′. An exchange feasible in J would therefore produce a full E-schedule with an improved slot at a′, contradicting Lemma 3.3 with its allowed suffix rescheduling. This establishes I3 in this case.

3. For a′=a, a switched update has no boundary qualifier by Lemma 6.4, so it supplies no pair satisfying the statement's hypotheses. For a same update, neither x∉D_a nor the boundary job y can qualify through the injection D_a\P_b; for y this follows from Lemma 2.5. Both qualify through the carry. Lemma 5.1 therefore transfers their strict pre-pruning comparison to the old parent keys. The parent has x∈W\D_a and old qualifier y∈a. Its current preparatory schedule followed by the arbitrary child replacement is one full replacement of W. Parent I3 prohibits precisely the proposed exchange, proving this case too.

## Proposition 7.3 — construction and induction order

**Verdict: confirmed.**

1. At the root the entry J is an upset, both boundaries are virtual, I1 holds from P_b=J, and I2/I3 have no boundary job. The root count and leaf bounds hold directly. Assume the construction data and all three invariants are established through a node W. Lemma 2.4 and Corollary 3.7 allow the center preparation; normalization of each side is an existence choice over a finite nonempty family. Lemmas 4.3–4.5 then yield priority prefixes, terminating side walks, marks, and all nonempty gap children with their edge data.

2. A same update uses W's already constructed list. A switched update refers to the edge U→W, which exists strictly earlier in the induction. Lemma 6.2 computes its short extension from its rank prefix or its already recorded carry; the flattening equality of 6.1 refers only to initial entries of that earlier run. Lemma 6.4 then constructs G using the already fixed boundaries and center of U. Thus neither an unconstructed child's I2/I3 nor its leaf bound enters the switch construction.

3. New entries are global upsets. Lemma 5.3 proves the exact qualifier identity and child I1 before any further boundary invariant is invoked. Lemma 5.5 proves the pruned count from old I1, that identity, and known edge cones. Lemmas 6.1–6.5 prove leaf bounds using already existing earlier-run descriptions and the just proved count. Lemmas 7.1 and 7.2 then establish child I2 and I3 from parent I2/I3 and the current normalized sides. This order supplies all induction hypotheses for each child.

4. Each child omits its parent's center slot and consists of complete slots, so |W′|/m≤|W|/m−1. A branch has at most N/m nonempty nodes. Each side has only finitely many promoted jobs and marks, hence each node has finite degree. Induction on the remaining slot count gives a finite whole tree. Copies of witnesses at branching ensure that a modification below one child changes no witness used by another child.

## Lemma 8.1 — cutoff predicates

**Verdict: confirmed.**

1. On a same side, U=W is partitioned as S_0⊔O⊔Y, with W∩P_b=S_0⊔O. Lemma 5.1 makes Φ_i∩W exactly the unpromoted O\S_i. Thus W∩(P_b\Φ_i)=S_0∪(O∩S_i)=S_i. The carry union has A_m leaves by Lemma 6.5, complementation preserves them by Lemma 2.6, and the additional P_b factor adds one, giving A_m+1.

2. On a switched side, S_i is exactly the set of X=W\D_a jobs of rank at most the last promoted rank r_i, with r_i=0 for no promotions. Intersecting (J\D_a)∩{λ≤r_i} with W gives that set exactly. This expression has two leaves and is within A_m+1. Both cases include empty gaps because their cutoffs and carries are defined before selecting nonempty children.

## Lemma 8.2 — global descriptions

**Verdict: confirmed.**

1. For the high part, a job x∈W′\S qualifies by 5.3 and belongs to P_{b′} by 4.5. Its time lies strictly after a′, so 2.5 excludes it from widehat P_{a′}. Conversely, membership in the right side of (8.4) implies time(x)<b′. Were time(x)≤a′, child I2 (Lemma 7.1) would place this qualifier in widehat P_{a′}, contradicted by the last factor. Thus a′<time(x)<b′, giving x∈W′; 5.3 then puts it outside S. This proves equality as subsets of J without intersecting a parent formula.

2. Let z belong to the right side of (8.5). The D_{a′} and P_b factors give a′<time(z)<b, and a′≥a. Hence z∈W. The restriction equality of 8.1 is now applicable and yields z∈S_i. Since S_i⊆S_*, a low z at the center belongs to its weak successor cone; a low z after the center belongs to D_v by the center separator. The factor J\widehat D_v excludes both, so z lies in the side E before v.

3. Within E, z is low for S_i. At b′ it belongs to the weak successor cone. After b′, Lemma 4.4's common-cutoff separator puts it in D_{b′}; for the last edge b′=v this alternative was already excluded by paragraph 2. Thus the factor J\widehat D_{b′} forces time(z)<b′. Together with time(z)>a′ this yields z∈W′∩S_i.

4. Conversely, a low job z∈W′∩S_i lies in D_{a′}∩P_b by 4.5 and in the cutoff predicate by 8.1. It occurs before both b′ and v, so 2.5 excludes it from their weak successor cones. It satisfies all factors of (8.5). The two inclusions prove the exact global equality.

## Lemma 8.3 — relative descriptions at marks

**Verdict: confirmed.**

1. In the chosen working frame, H_*=P_b on a same side and H_*=J\D_a on a switched side satisfy H_*∩W=S_* by the center definitions. Lemma 3.1 at center v therefore gives W∩B_v(H_*) equal to the open side E before the center. This formula requires only a relative equality on W.

2. Every side mark has a representation z=s_i with i≥1. Lemma 4.4 (or directly 3.6 for the final promoted cutoff) makes z a separator for S_i on E. Lemma 8.1 gives E∩widetilde S_i=E∩S_i. Applying Lemma 3.1 on E yields its prefix before z. Intersecting with B_v(H_*) first restricts the formula to E within W, so W∩F_z is exactly all W-jobs before z in the working frame. Repeated positions cause no difficulty: a chosen occurrence i has the requisite separator property.

3. Under forward time this is the requested prefix. Under reversed time, the three disjoint sets (working prefix), slot z, (working suffix) partition W. The reversal map sends the working suffix to the original prefix. Hence W∩((J\F_z)\z) is exactly the original-time prefix. Lemma 2.6 gives a same-leaf complement formula, and intersecting with the complemented slot atom adds one leaf. The same argument covers the center's three-leaf formula.

## Lemma 8.4 — uniform leaf budget

**Verdict: confirmed.**

1. In (8.4), the qualifier union contributes at most A_m leaves by 6.5, and the two cone factors each contribute one. This high-part formula therefore uses A_m+2 leaves. In (8.5), 8.1 contributes A_m+1 leaves for the cutoff predicate and its four other cone factors contribute four; this low-part formula therefore uses A_m+5. Their union is exactly W′ by 8.2, and binary union adds their leaf counts. The result is 2A_m+7=2(6m+9)+7=12m+25.

2. The expression B_v(H_*)=P_v∪(H_*∩(J\widehat D_v)) has three leaves because H_* is a one-leaf cone or complemented cone. The second separator expression B_z(widetilde S_i) has 1+(A_m+1)+1=A_m+3. Equation (8.7) intersects the two expressions, giving A_m+6; reversal in (8.8) adds one for the complemented slot. Thus every original-time marked prefix uses at most A_m+7=6m+16 leaves.

3. Every genuine boundary slot has exactly m jobs, placing all cones and slot-membership tests in Section 2's atomic alphabet. At virtual boundaries the displayed definitions are J or the empty set and each uses one permitted constant atom. Reverse-frame ranks/cones are explicitly permitted in that alphabet. No uncounted node-membership atom or parent formula occurs in these expressions. Finally 6m+16≤12m+25 follows from 6m+9≥0, which holds for the stated m≥3.

## Theorem 8.5 — hierarchy

**Verdict: confirmed.** The earlier foundations are checked in the companion B_foundations audit; the derivation below identifies each use.

1. Proposition 7.3 supplies a finite construction starting from any full schedule of J. Every nonempty node retains a full-schedule witness of J by interval replacement and marks its center, so at least one slot is marked. Sorting the marks in original time gives exactly its gap children, because each side's nondecreasing walk positions create one gap per strict successive position; the center joins the two sides and the original external boundaries complete the list.

2. The root is J and has its one-leaf atom. Every nonroot node is one of these gaps; 8.2 and 8.4 give its global description with at most K_m=12m+25 leaves. Lemmas 8.3–8.4 give each marked original-time prefix a relative formula with at most 6m+16≤K_m leaves. Children inherit copies of their parent's current witness by the construction. These verify the four clauses of Definition 2.9 individually, proving the claimed hierarchy without any depth accumulation in descriptions.

## Direct dependency corrections for this portion

This list records genuine uses, including equation references that the existing literal-citation extractor omitted. A dependency on a set's definition is identified separately rather than replaced by an invented numbered lemma.

| Result | Direct numbered/invariant dependencies to record |
|---|---|
| 5.5 | 4.5, 5.1, 5.3, 5.4; I1; injection definition (5.2) |
| 6.1 | 5.1, 5.4; pruning/run definitions; switch-pair definition (5.4) |
| 6.2 | 2.6, 5.3, 5.4, 5.5, 6.1; cutoff construction |
| 6.3 | 4.5; frame reversal definition |
| 6.4 | 2.5, 4.3, 4.4, 4.5, 6.2, 6.3; equation (6.8) |
| 6.5 | 2.6, 5.4, 5.5, 6.2; equations (5.2), (5.4), (6.8) |
| 7.1 | 2.5, 3.4, 3.6, 4.3, 4.4, 5.1, 5.3, 6.4; I1, I2, I3 |
| 7.2 | 2.4, 2.5, 3.3, 5.1, 5.2, 5.3, 6.4; I1, I3 |
| 7.3 | 2.4, 3.7, 4.3–4.5, 5.3, 5.5, 6.1–6.5, 7.1, 7.2; root invariants |
| 8.1 | 2.6, 4.3, 5.1, 6.5; equations (8.1), (8.2) |
| 8.2 | 2.5, 4.3, 4.4, 4.5, 5.3, 7.1, 8.1; center separator |
| 8.3 | 2.6, 3.1, 4.4, 8.1; center cutoff definition |
| 8.4 | 2.6, 6.5, 8.1, 8.2, 8.3; atomic formula alphabet |
| 8.5 | Definition 2.9, 7.3, 8.2, 8.3, 8.4 |

The earlier “no numbered statement is cited” Uses line for 8.4 was a description of literal citation strings, not a sufficient dependency account: its proof uses the earlier proved meanings and size bounds of (8.4)–(8.8). The corrected line records these mathematical dependencies explicitly.

## Independent finite construction check

The program `code/B_hierarchy_check.py` and its complete output `code/B_hierarchy_check_output.json` are included. This newly written program constructs the whole hierarchy for 255 feasible DAGs using the seed 20261115 and the fully specified layered sampling families printed in the output. Machine counts 3, 4, and 5 and 3–6 original slots occur. Every normalization is obtained by exact recursion over minimal-job m-subsets in lexicographic priority order. It constructs and checks actual global entry sets, exact cutoff predicates, earlier-cutoff extensions, direction changes, capacity witnesses, and both parts of each global child formula. For each nonvacuous I3 pair it enumerates every feasible full replacement of that node interval and checks every prescribed exchange globally. All assertions passed.

| Measured item | Count |
|---|---:|
| Input DAGs | 255 |
| Constructed nodes / I1 and I2 checks | 754 |
| Actual switched children | 132 |
| Injection-to-boundary witness checks | 499 |
| Earlier-cutoff extensions | 499 |
| Cutoff restriction identities | 7069 |
| Global child formulas | 499 |
| Relative side-mark formulas | 978 |
| Nonvacuous I3 pairs | 11 |
| Full replacements enumerated for I3 | 8 |
| Globally checked exchanges | 12 |
| Qualifiers at their left boundary | 48 |
| Qualifiers strictly before their left boundary | 5 |
| Surviving-first initial-pair replacements encountered | 0 |

The run's maximum node depth is 5, maximum observed surviving injection count is 1, and maximum observed global-child formula leaf count is 10. It encountered zero surviving-first initial-pair replacements, so the audit of that exact history case is the arbitrary-history proof of Lemma 6.1 above. The finite family and these measured limits are stated precisely; the universal mathematical conclusions follow from the stepwise arguments, not an extrapolation of these measurements. Cases exercising a direction switch or a nonvacuous exterior exchange are printed completely with their arc lists in the output.

<!-- END B_hard.md -->

---

## Part E — full provenance and ancillary-file audit

Source record: `work/E_provenance.md`. Full text follows.

<!-- BEGIN E_provenance.md -->

# E: provenance, preservation, and ancillary-file audit

Audit date: 15 November 2026 (Europe/Berlin). Auditor: GPT-6 Astra, effort ChatGPT Pro mode.

## Findings

The supplied return is preserved byte for byte and has the requested SHA-256. The three supplied reports have the stated model/effort headings and the stated verdicts. Their mathematical scope is the original answer: its structural proof and finite-search argument, with comments on the earlier runtime sketch and on unverified source claims. They do not document an S-type source comparison or a C-type execution of the attached code. This audit of the supplied records does not turn those older reads into checks of the revised post.

The dates, Message Batches API mode, and description of the three reports as independent runs on the same input are expressly supplied in the present task and in the original post/register. The report files themselves contain no execution timestamps or API request logs. Preserve this information as supplied provenance metadata. The numerical assertion “47,788 input tokens each” and the assertion that no run saw another report occur only in the original post's Independence paragraph; no underlying logs are included. They add nothing needed to assess the theorem and should be omitted from the revised concise record, or explicitly identified as assertions of the supplied post.

One exact provenance discrepancy remains: the supplied `Q03_PROMPT.txt` has 9,551 bytes and SHA-256 `792b1a676ab01162d40d78ac73440d5a0dbe5e31b626cac398bcb882358fa54a`; the old artifact manifest instead records an `inputs/PROMPT.txt` of 9,383 bytes and SHA-256 `41db4774893d4ee075889202411db254e3884a111734b07d6959c5670faec13b`. That particular manifest-listed file is absent from the supplied background. The task identifies `Q03_PROMPT.txt` as its supplied prompt as sent; it is preserved unchanged under that description. Its byte identity to the different manifest entry has not been established. This is a version-history qualification, with no use in the proof.

No genuine machine-local absolute path, private contributor identity, email address, private key, or credential was found in the six mandatory ancillary files. Public bibliographic author names and the source URLs remain as required credits. The automated Windows-drive heuristic produced two matches on TeX function notation `f:\mathscr`; inspection establishes the exact mathematical context, so neither is a filesystem path. No ancillary bytes were altered.

## 1. Records opened, with exact locators

| Record | Locator | What it supports | Qualification |
|---|---|---|---|
| `provenance/Q03_PROMPT.txt` | Lines 1–2; task paragraphs 0–4, lines 7–61 | Original task Q03, internally dated 22 October 2026; explicit scheduling model, all-machine extension request, proof/source and deliverable requirements | The file does not name the question-writing model or its effort. Those fields come from the supplied post. |
| `provenance/Q03-solution.md` | Title and date, lines 1–4; mathematical sections 2–9; bibliography and Further consequences | Return internally dated 23 October 2026, with the original statement numbering and +8 input bound | Model/effort credit is supplied by the current task and original post, rather than a model-signature field in this return. |
| `provenance/artifacts/MANIFEST.json` | `files` entry `Q03-solution.md`, lines 5–8 | Return length 94,789 and SHA-256 `3ebeb452d6f461c23b4f8fa6f04ba6ed15abac541b5d2562fa814ba77977e60c` | Recomputed hash matches both attached copies and the ancillary copy. |
| Same manifest | `files` entry `inputs/PROMPT.txt`, lines 60–63 | A recorded 9,383-byte input prompt, hash `41db4774893d4ee075889202411db254e3884a111734b07d6959c5670faec13b` | That file is absent; the supplied 9,551-byte `Q03_PROMPT.txt` has a different hash. |
| `provenance/reports/Q03-check.md` | Header, line 1; Verdict, lines 3–4; Check of the argument, lines 21–85; External results used, lines 87–95 | Claude Opus 5.5, effort max; “PROVED WITH FIXABLE GAPS”; structural steps followed and re-derived, input exponent gap, source claims unverified | No report date or API invocation metadata inside the report; no source or code execution certification. |
| `provenance/reports/Q03-b-check-b.md` | Header, line 1; Verdict, lines 3–4; Minor issues M1–M3, lines 88–98; External results, lines 101–108 | Claude Opus 5.5, effort max; “PROVED AS STATED”; expressly says structural steps were re-derived; flags runtime itemization and source correspondence | No report date or API invocation metadata inside the report. Its bibliographic wording includes reliance on recall; retain no S-type classification. |
| `provenance/reports/Q03-c-check-c.md` | Header, line 1; Verdict, lines 3–4; §9, lines 78–81; §11, line 83; External results, lines 85–92 | Claude Opus 5.5, effort max; “PROVED AS STATED”; key proof steps followed; input exponent informal; code unavailable to inspect; sources not checked | The explicit “code was not available to inspect” excludes a C-type run for this report. |
| `register/REVIEW_REGISTER_row_Q03.md` | Dated heading, line 1; Q03 row, line 5 | Register snapshot of 14 November 2026; three Opus-max verdicts dated 23 October; separate lesson-chain activity dated 24 October | Cost estimates and later lesson checks are recorded assertions. Their underlying session files are not supplied. |
| Present task, `anc/Q03_DEPOSIT_prompt.md` | Lines 3, 9, 28, 57, 97, 111 | Current task written 15 November 2026 by Claude Opus 5.5, effort max; return by GPT-6 Astra in ChatGPT Pro mode; three report dates/API/independent-input description; Fable effort high for the two proof layouts; current audit attribution | These are the user's supplied provenance statements. No broader authentication claim is made. |
| Original post | POST-RECORD lines 25–34 | Question model effort not recorded; proof model ChatGPT Pro mode; Fable effort high; prior classifications F,D / D / F | Preserve the exact attribution, while updating the record for the present revision. |
| Original post | Independence paragraph, lines 1523–1525 | Separate runs, same input, claimed 47,788 input tokens per run, no cross-report exposure | No supporting raw batch log is supplied. Prefer concise attributed wording without the numerical token claim. |
| Original post | Checks of other texts, lines 1528–1531; Provenance, lines 1563–1564 | The post records additional lesson writing/checking sessions and public lessons 9–11 | Do not count these as checks of the revised post. Source verification of the public lessons is recorded separately in the source audit. |
| Original post | Provenance, lines 1548–1562; Declarations, lines 1571–1578 | Question, proof, original conversion and layout attribution; human-understanding/formalization declarations; prior-work credits | The present revision must name GPT-6 Astra, effort ChatGPT Pro mode, as its reviser/checker as well. |

## 2. Exact preservation checks

The six files below were compared to the supplied originals. All copies match. Public filenames in this table are relative to the final package.

| File | Bytes | SHA-256 |
|---|---:|---|
| `anc/Q03_DEPOSIT_prompt.md` | 17,129 | `aa9d96d9e3a4125df1dc9151f5cf69de6580ce79c99208a7bc48df0dad5bb706` |
| `anc/ai-provenance/Q03_PROMPT.txt` | 9,551 | `792b1a676ab01162d40d78ac73440d5a0dbe5e31b626cac398bcb882358fa54a` |
| `anc/ai-provenance/Q03-solution.md` | 94,789 | `3ebeb452d6f461c23b4f8fa6f04ba6ed15abac541b5d2562fa814ba77977e60c` |
| `anc/ai-provenance/Q03-check.md` | 8,900 | `0ce501f1241a87fcffe637657effbceb84b487bf20021b2dc95fa1a465f06079` |
| `anc/ai-provenance/Q03-b-check-b.md` | 10,676 | `15ea0b95e4b23f68bb0b50a2eda1d08cae99793cf3ce46a9e15b5a5c95071b2a` |
| `anc/ai-provenance/Q03-c-check-c.md` | 10,207 | `e1a821b14067ec136f80b6c6e0e2705dc04ffe84d28a4c7f15564de12bbdb30b` |

The original return copy in `provenance/artifacts/Q03-solution.md` is also 94,789 bytes with the same hash. Thus the map from either supplied return copy to the published ancillary copy is the identity on every byte. The dated original proof, including its superseded +8 input exponent and historical source claims, remains preserved as provenance; corrected assertions belong in the revised post and report.

### Prompt-manifest discrepancy: exact transformations tested

The supplied prompt is ASCII with 61 LF bytes and no CR or CRLF. The following exact byte maps were computed without changing the preserved file:

| Map | Output bytes | Matches old manifest? |
|---|---:|---|
| Identity | 9,551 | No |
| Replace every CRLF by LF | 9,551; identical to input | No |
| Replace each LF by CRLF after CRLF-to-LF replacement | 9,612 | No |
| Remove an initial UTF-8 BOM | 9,551; identical to input | No |
| Remove all terminal CR/LF bytes | 9,550 | No |

All output hashes are in `code/E_verify_provenance.out`. None equals the old manifest's hash, so no reconstruction of the absent file is asserted or created. The next evidence needed to resolve this version question is the original manifest-listed `inputs/PROMPT.txt` or its enclosing original artifact archive. That uncertainty changes no theorem premise or cost bound.

## 3. Check types and scopes to carry into the post

Use the three original report verdicts verbatim, alongside their stated findings:

1. **Claude Opus 5.5, effort max, Message Batches API; 23 October 2026; F,D.** Original answer: structural and dynamic-program proof checked; verdict **proved with fixable gaps**. Findings: input exponent not derived and source claims unverified.
2. **Claude Opus 5.5, effort max, Message Batches API; 23 October 2026; D.** Original answer: structural steps expressly re-derived; verdict **proved as stated**. Findings M1–M3: input exponent, subroutine itemization, and source correspondence needed further work.
3. **Claude Opus 5.5, effort max, Message Batches API; 23 October 2026; F.** Original answer: key proof steps checked one by one; verdict **proved as stated**. Findings: informal input exponent and unchecked bibliography; code not available to inspect.

For all three, dates and API mode are the supplied task/register metadata. The files' headings independently support model/effort and their Verdict sections support the exact verdict words. The numerical number of original runs is three because three distinct report files are supplied. The task describes them as independent runs on the same input; preserve that description with an attribution to the supplied provenance, without implying independently authenticated execution logs.

The current check must be a separate record for **GPT-6 Astra, effort ChatGPT Pro mode, 15 November 2026**, with the actual F,D,S scopes and verdict reached by the root audit. Its C-type computations, where listed, are the actual rerun/new programs and outputs. The current source-opening checks have their own precise source/version/locator rows. There is no formalization of the present general-m proof in this work, and no human check has been performed in this session.

## 4. Recommended concise provenance and record wording

### Provenance prose

> The original task is dated 22 October 2026. The supplied post attributes it to Claude Opus 5.5, effort not recorded. The 23 October return is attributed in the supplied task to GPT-6 Astra, effort ChatGPT Pro mode. Its preserved ancillary copy has SHA-256 `3ebeb452d6f461c23b4f8fa6f04ba6ed15abac541b5d2562fa814ba77977e60c`. The three supplied Claude Opus 5.5 reports, effort max, have verdicts “proved with fixable gaps”, “proved as stated”, and “proved as stated”; the task/register date them 23 October 2026 and describe independent Message Batches API runs on the same input. Claude Fable 5.2, effort high, assembled the 14 November post and the numbered layouts of Lemmas 3.3 and 5.5. GPT-6 Astra, effort ChatGPT Pro mode, audited and revised this text on 15 November 2026. The supplied prompt and all returns/reports are preserved unchanged in `anc/`; the prompt-file discrepancy described in Limits concerns the older artifact manifest.

### Metadata fields requiring precise wording

- `produced_by` includes original question / proof / 14 November assembly, plus current deposit-task author (Claude Opus 5.5, effort max) and current reviser/checker (GPT-6 Astra, effort ChatGPT Pro mode).
- `checks` retains the three original exact verdicts and marks their scope as the original answer.
- `checks_of_this_text` is a new current-date entry with the complete revised-text audit scope and its actual verdict.
- Independence wording: **“The supplied task describes the three prior reports as independent runs of the same model on the same input; raw execution logs were not supplied.”**
- Prompt provenance wording: **“Supplied original-task text preserved unchanged; byte identity to the different `inputs/PROMPT.txt` entry of the old artifact manifest is unverified.”**
- Historical lesson checks may be mentioned as supplied-register history; they must not enlarge the count of proof checks of this text.
- Human understanding remains **none** as the supplied declaration; no human checking is added by this audit. Formalization remains **none** for the present general-m theorem.

## 5. Ancillary privacy and reproducibility check

`code/E_verify_provenance.py` verifies all six byte hashes and screens the text for absolute Unix paths, home-relative paths, file URIs, possible Windows drives, credential patterns, private-key markers, and email addresses. Its complete output is `code/E_verify_provenance.out`. It reports six preserved copies, two manually resolved TeX false positives, zero actual local paths, and zero observed credentials. Manual reading found only public bibliographic names and source credits, with no private contributor identity added.

The scan is reported as a finite inspection of these exact files. It does not authenticate old API sessions and does not imply that a regex can decide every possible privacy question. No credentials or suspected credential strings are echoed by its output. The original files were neither normalized nor redacted.

## 6. Section 9 layout update

`work/A_replacement.tex` now contains 20 numbered `\step` headings across the proofs of 9.1–9.4. Each heading states its step's claim and names its dependencies in brackets. The mathematics and exponents of the previous accounting are preserved. Proposition 9.4's stronger explicit-output sentence now has a concrete family: fixed m, n=2^k independent jobs, T=n, and an empty arc list. Its compact input has O(k) bits; every literal schedule lists all 2^k jobs and has at least 2^k output symbols.

<!-- END E_provenance.md -->

---

## Part E — full mathematical integration audit

Source record: `work/E_proof_integration.md`. Full text follows.

<!-- BEGIN E_proof_integration.md -->

# Independent integration audit of the assembled mathematical post

Checker: GPT-6 Astra (OpenAI), effort ChatGPT Pro mode. Date: 15 November 2026.

**Verdict: all requested mathematical integration checks pass.** The assembled post retains the reviewed proof, the statement CSV covers every statement exactly once, the Uses lines agree with the dependency table and CSV, and every source counterpart agrees with the source audit's concordance. Two integration defects observed during the review were corrected by the assembling agent and checked again: incomplete renaming of the numeric state bound, and the empty capacity-transfer explanation for Lemma 8.1. No main-post edit was made by this checker.

The reproducible checks are in `code/E_check_proof_integration.py`; the exact checked artifact hashes and complete output are in `code/E_check_proof_integration_output.json`. The checker reads each artifact once, so its hashes identify the actual snapshot compared. It can be rerun after final typesetting or record updates.

## 1. Complete statement coverage

| Proof section | Numbered identifiers | Count |
|---|---|---:|
| 2 | 2.1–2.10, including Definition 2.9 | 10 |
| 3 | 3.1–3.7 | 7 |
| 4 | 4.1–4.5 | 5 |
| 5 | 5.1–5.5 | 5 |
| 6 | 6.1–6.5 | 5 |
| 7 | 7.1–7.3 | 3 |
| 8 | 8.1–8.5 | 5 |
| 9 | 9.1–9.4 | 4 |
| **Proof total** | | **44** |
| Front matter | Theorem A, Theorem B, Cited result 1 | 3 |
| **CSV total** | | **47** |

The program parses all 44 actual statement environments and reads the CSV with the standard CSV parser, which respects multiline quoted statement cells. It verifies that every expected identifier occurs once, that no additional identifier occurs, and that every proof statement's kind, title, and complete statement text equal its CSV statement. The status of Definition 2.9 is “definition checked”; the other 43 proof statements have “proved as stated.” The front rows separately cover both main theorems and the single cited result. There are zero missing, duplicate, or mismatched rows.

Theorem A's CSV dependencies are exactly 9.1, 9.2, and 9.3. Theorem B's dependencies are exactly Definition 2.9, Proposition 7.3, and Lemmas 8.2–8.4. These are the same direct dependencies displayed beneath their actual statements, with the range 8.2–8.4 expanded to individual identifiers.

## 2. Preservation of the reviewed Sections 2–8

The program extracts the entire assembled text from the start of Section 2 through the end of Section 8, including every unnumbered definition and explanatory paragraph. It compares that text with `work/B_proof_revised.tex` after precisely these recorded assembly transformations:

1. Remove the two obsolete descriptive proof headings above 3.3 and 5.5; their actual numbered steps remain present.
2. In Theorem 8.5 write the standing range explicitly: “For m≥3, every full schedule…” The earlier standing model and notation table already fix m≥3, and the newly written range states that same domain within the theorem itself.

The resulting texts are equal. Thus the full reviewed proof, its unnumbered construction data, and all equations are retained. The explicit selection in Lemma 5.5 is present verbatim as “let x_K be the least-rank job of K∩W′.” Its map f remains an explicitly selected function into the genuine slot b′, and the four-step injection proof remains unchanged apart from this reviewed clarification.

The corresponding scope clarifications in 9.1 and 9.4 also appear in their actual statements and their regenerated CSV rows: “For m≥3…” and “For each fixed m≥3…”.

## 3. Uses lines, dependency table, and construction order

Every proof statement and Definition 2.9 has a Uses line immediately following its environment. Independently parsing the 44 rows of the typeset dependency table gives the same statement identifiers, kinds, and Uses text. The CSV `depends_on` cell equals that text for every proof statement. There are zero discrepancies among these three representations.

For every named result invoked in a Uses line, the referenced statement exists and precedes the current result in the proof order. The program expands same-section ranges before checking them. Definitions and standing data are retained as such: in particular, the Uses line of Lemma 5.3 cites the stipulated switch-upset property (5.3), together with the earlier qualifier/cone results and I1. It introduces no invocation of the later Lemma 6.4. Proposition 7.3 establishes the ancestor-first construction order before invoking 5.3 with the constructed switch upset.

The dependency table's row 8.1 originally still had the inherited placeholder “Unchanged argument: ---”. The assembling agent replaced it with the concrete statement that the same restriction identities use the capacity-dependent carry bound A_m=6m+9, and marked the row changed. The current row agrees with Lemma 8.1's identity and leaf-count proof.

## 4. Source counterpart consistency

Every one of the 44 source-column entries was compared with `code/C_dependency_source_map.json`. The comparison checks the exact displayed source statement number or prose section and, where present, the source's LaTeX label, after removing typesetting-only `allowbreak` commands. All entries match. Each CSV notes cell also contains the corresponding source display, exact locator, and audit note from that concordance.

This includes the corrected prose counterparts for 4.3, 5.4, 6.3, and 8.1; the source's Theorem 3.4 for Q03 Theorem 8.5; Section 9 accounting for Q03 9.2–9.3; and source Remark 9.1 for Q03 9.4. Their primary-source comparison is documented in the S-P source audit. The present check verifies faithful integration of that already recorded comparison into the post and CSV.

## 5. Standing data and domains of the principal results

| Result | Identifiable standing data and exact scope |
|---|---|
| Cited result 1 | m=3, the explicitly listed DAG model immediately preceding it, polynomial deterministic multitape decision, feasible-schedule construction, and optimization; source [P], Theorem 1.1, S-P. |
| Theorem A | One algorithm receives the explicit DAG and binary m≥3,T; n≥1; a schedule is the stated capacity-m map into integer slots. Section 9 specifies the canonical self-delimiting encoding and L. The common bound covers decision, witness construction, and optimization. Its N-only bound starts from the parsed canonical padded graph with 1≤T<n and n≤mT. A(m,K) and G(m) are displayed explicitly in 9.2–9.3. |
| Theorem B | m≥3, padded universe J with |J|=mT, the full-schedule definition in 2.3, and the precise hierarchy definition 2.9. Its global and relative budgets are 12m+25 and 6m+16, with no dependence on depth. |
| Theorem 8.5 | m≥3 is now explicit. J, full schedules, permitted formulas and K_m, and hierarchy clauses have all been defined before this statement. The proof invokes 7.3 and 8.2–8.4 in that established order. |
| Theorem 9.1 | m≥3 is explicit; the actual finite procedure is Section 2's state graph with K=K_m. Acceptance is for the padded J, padding/removal uses 2.3, and the theorem's proof specifies the elementary deadline branches and increasing optimization trials. |
| Proposition 9.2 | m≥3, K≥1, parsed canonically numbered J=[N] with N=mT≥m; one deterministic machine with a fixed number of tapes. B, the numeric state bound, q, h and C are defined before their cost uses. The explicit coefficient A(m,K) bounds the complete padded computation, including its witness. |
| Corollary 9.3 | K_m=12m+25, e_m=60m²+129m+1, explicit input length L with n≤L, N≤mn≤mL, and at most n trials. The resulting exponent is e_m+1=60m²+129m+2, with the displayed coefficient G(m). |
| Proposition 9.4 | Each fixed m≥3; total vertex count n in binary and explicitly listed arc endpoints. The proof defines d, derives n≤N<2m|E| in its expansion branch, and states the decision-output scope. Its last paragraph specifies the zero-makespan convention for the empty instance. |

Proposition 2.8 explicitly states its own wider domain m≥1 and arbitrary description family for the soundness argument. The symbols L,Z,R are local set variables in state triples; L in the complexity formulas is explicitly identified as input length. The notation paragraph also distinguishes the leaf budget K from the indexed entry sets K_j by their definitions.

## 6. Numeric state-bound renaming

The assembly introduced calligraphic S for the numeric state bound and retained S for low cutoffs. The first assembly substituted only isolated occurrences, leaving ordinary S in juxtaposed expressions such as qSN, BS(BN²+N⁴), and 3BS⁴N. That was a genuine notation inconsistency because the new notation paragraph stated the renamed quantity explicitly.

The assembling agent replaced S throughout Section 9's mathematical segments, including juxtaposed products. The current check scans all inline and displayed mathematics in that section, removes the declared calligraphic-S token, and confirms that no plain uppercase S remains. The renaming preserves the explicitly declared value B N^m at every use. Thus its arithmetic products and all eight subroutine bounds continue to denote the same numeric quantities audited in Part A.

## 7. Conclusion of this integration check

The current JSON output reports zero missing/duplicate statement rows, zero statement or dependency mismatches, zero source-counterpart mismatches, zero forward named Uses references, and zero unconverted numeric-state symbols. All 47 CSV rows are present; the reviewed Sections 2–8 and the explicit choice domain in 5.5 pass their comparisons. No mathematical integration correction remains outstanding in this check. PDF compilation and visual review are being recorded separately by the assembling agent.

<!-- END E_proof_integration.md -->

---

## Part E — full final consistency audit

Source record: `work/E_final_consistency.md`. Full text follows.

<!-- BEGIN E_final_consistency.md -->

# Final assembled-text consistency audit

Audit date: 15 November 2026 (Europe/Berlin). Auditor: GPT-6 Astra, effort ChatGPT Pro mode.

Files examined: `Q03_DEPOSIT_post.tex`, `work/frontmatter.tex`, `work/endmatter.tex`, `Q03_DEPOSIT_results.csv`, the current assembly script, and the final-build log. The exact assembled-source hash inspected by the reproducible checker is recorded in `code/E_check_final_consistency.out`. Root's final rendering inspection is recorded separately; this audit checks the text, metadata, CSV correspondence, and reported build counts.

## Verdict

The inspected assembled post and CSV are consistent on the proved exponents, effective constants, input model, theorem ranges, source-statement range, historical/current check scopes, model/effort/date fields, original-prompt qualification, and numbered-statement coverage. Two concrete assembly/scope defects were identified and corrected during this review, and one source-range clarification was incorporated. No remaining mathematical or metadata inconsistency was found within this audit's scope.

## 1. Numeric state-bound rename: defect found and corrected

The first assembly renamed standalone `S` to `\mathcal{S}` but left adjacent products such as `qSN`, `BS^4N`, `DSN`, and the table entries unchanged. Its definition therefore used the new symbol while several costs still used the old one. The defect arose from a word-boundary text substitution.

The revised assembly performs the replacement inside every Section 9 mathematical segment. The exact map is: every occurrence of the old numeric-state-bound symbol `S` in those segments becomes `\mathcal{S}`; prose is unchanged. Section 9 contains no cutoff using that old symbol, and the earlier proof's cutoffs retain their original `S`. The notation table records the correspondence `\mathcal{S}=S_{\text{old Section 9}}=BN^m` in words. This is a rename of the same integer bound.

The checker finds 24 occurrences of `\mathcal{S}` in Section 9 and no unconverted `S` in its mathematical segments after removing those exact command strings. In particular, the corrected dominant expression is

\[
B\cdot\mathcal S\cdot\mathcal S^2\cdot3D\mathcal S N
=3DB\mathcal S^4N=3DB^5N^{4m+1}.
\]

All intermediate record and witness costs now use the same numeric parameter.

## 2. Input model, exponents, and coefficients

Theorem A and the abstract state the common input bound with exponent `60m^2+129m+2`. Equation (1.2) states the padded exponent `60m^2+129m+1` and explicitly begins from the parsed, canonically numbered padded DAG. Section 9's encoding contains explicit vertices, canonical binary integer fields and distinct arcs, so `n≤L`. Its nontrivial padded branch satisfies `1≤T<n`, `n≤mT` and `N=mT≤mn≤mL`. The elementary branches use the original arc list and fit the separately accounted degree-four input cost.

The coefficient formulas in the assembled Proposition 9.2 and Corollary 9.3 match the independently reviewed accounting exactly:

\[
q=64(m+1)(K+1),\qquad D=2^{20}q^2,
\]
\[
A(m,K)=2^{40}(m+1)^4(K+1)^4(K512^K)^5,
\]
\[
G(m)=A(m,12m+25)m^{60m^2+129m+1}+2^{31}(m+1)^4.
\]

The record block makes the same claims with these named coefficients. The common input exponent includes the at most `n≤L` deadline trials. The small-m table is 928/929, 1477/1478, 2146/2147 and 2935/2936 for the padded/input exponents at m=3,4,5,6. No obsolete `60m^2+129m+8` remains in the assembled post. Historical +8 claims remain only in the preserved original provenance, as intended.

The report of the theorem's scope includes decision, a witness on acceptance, and optimal-schedule construction. The description theorem uses global budget `12m+25`, relative-prefix budget `6m+16`, and a one-leaf root. The declarations retain the stated limits: no practical algorithm, no bound polynomial in m, no unsupported variants, and no formalization of this proof.

## 3. Standalone theorem and source ranges

The first assembled Proposition 9.4 said merely “For fixed m”, although its cited computation in Proposition 9.2 explicitly requires m≥3. The revision states “For each fixed m≥3”. The assembled Theorem 8.5 and Theorem 9.1 now also explicitly state m≥3, agreeing with Theorems A and B without requiring an unstated global convention.

The opened OpenAI Theorem 1.1 restricts its deadline input to `1≤T≤n`. The first front-matter cited-result statement omitted that range after an input description allowing an arbitrary integer deadline. The revision now names `1≤T≤n` explicitly for the source's deadline and witness statements; its optimization statement is retained. The main theorem's broader integer-deadline handling is proved by its own elementary branches in Section 9.

The compact-output qualification has its explicit example in Proposition 9.4: fixed m, n=2^k isolated jobs and T=n. The compact input has O(k) bits, while a literal schedule lists 2^k jobs. This supports the stated exponential-output possibility within the same input convention.

## 4. Metadata and verification language

The assembled record, abstract, Status, Verification record, Provenance and Declarations agree on:

- Version 1 and current audit date 15 November 2026.
- Kind: generalization; claim: proved; current mathematical verdict: proved as stated.
- Current checker/editor: GPT-6 Astra, effort ChatGPT Pro mode; current check types F,D,C,S.
- Original question: Claude Opus 5.5, effort not recorded, 22 October 2026.
- Original proof return: GPT-6 Astra, effort ChatGPT Pro mode, 23 October 2026.
- Original format text: Claude Fable 5.2, effort high, 14 November 2026.
- Present deposit-task author: Claude Opus 5.5, effort max, 15 November 2026.
- Three earlier reports: Claude Opus 5.5, effort max, Message Batches API, 23 October 2026 as supplied metadata; verdicts one “proved with fixable gaps” and two “proved as stated”.
- Human understanding: none; formalization: none for this proof; no novelty or priority claim.

The current and historical scopes are separated. The three earlier verdicts refer to the original return; the current FD1 entry refers to the revised text. Historical execution dates, API mode and independence descriptions are identified as supplied-record metadata, with absent raw logs disclosed. The three reports receive no fabricated source-opening or code-execution credit. The source checks identify their actual scope, including original FKN full-text unavailability, the course archival endpoint failure, and unreplayed Lean builds. The latest S-F wording names both the target declaration and actual proof source; the comparator placeholder is not used to describe the separate proof body as absent.

The 9,551-byte supplied original prompt, the historical manifest's absent 9,383-byte variant, and the unsuccessful exact newline/BOM maps are stated in Limits and in the metadata. The original return's SHA-256 is unchanged. The machine-readable record includes the present-task author and effort, matching the updated Provenance and Declarations. No `demonstration` field or obsolete demonstration notice remains.

## 5. Statement CSV and build-count check

The post contains 44 distinct numbered statements in Sections 2–9, including Definition 2.9. The CSV has exactly 47 rows: those 44, Theorems A and B, and Cited result 1. Every numbered statement's complete extracted body matches its CSV `statement` field exactly after the assembly's explicitly defined wrapper construction: kind, number, parenthesized title, newline, and the source body with outer whitespace removed. No mathematical text is rewritten by that comparison. All 44 comparisons pass.

The final-build log inspected during this audit reports zero overfull-box messages, zero undefined-reference/citation messages, and zero fatal error messages. Its `build_check.json` reports 38 pages, zero overfull boxes, and zero boxes over 2pt; the current E1 table row reports the same values. The page images and their visual inspection remain part of the root's rendering record, not a claim derived from these numerical checks.

`code/E_check_final_consistency.py` performs the exact correspondence and metadata tests and records their output in `code/E_check_final_consistency.out`. Re-run it after any later assembly change so its source hash and measured fields identify the delivered source.

<!-- END E_final_consistency.md -->

