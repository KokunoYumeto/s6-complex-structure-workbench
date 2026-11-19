# Q03 source audit

**Audit date:** 15 November 2026, Europe/Berlin. **Checker:** GPT-6 Astra (OpenAI), effort ChatGPT Pro mode. This file records S checks: an identified source was opened and the attributed statement was compared. An S check establishes what the source says. Independent mathematical checking of Q03 belongs to the F/D report; independent Lean replay was not performed.

## Findings that change the post

1. The thirteen attached OpenAI preprint source files are byte-identical to the public files at OpenAI repository commit `4eaee87548250b2682affda7d05d947c05554bae`. Theorem numbers, labels and numeric constants can therefore be checked against the exact source supplied to the producing model.
2. The drbh commit `bbd30137258b15d8c5caedd035d72e8e8a875dbd` contains a four-machine adaptation through the complete release theorem, including exact optimization, deadline decision and a fixed multitape polynomial bound. Calling its scope merely a partial four-machine adaptation understates the source. The same commit's README still describes the baseline: the code, commit diff and theorem declaration resolve this discrepancy.
3. The published OpenAI scope file describes complete three-machine optimization and deadline decision, on one fixed finite machine with polynomial binary-input running time. The scope comparison does not amount to a fresh Lean build.
4. An existing all-fixed-machine paper was found: Klaus Jansen, arXiv:2611.09392v1, 6 November 2026. Its theorem and linear description budgets are recorded under S-J. An existing three-machine exponent refinement by David Niedbala Giraudin was also found on Hexagon. The revised post must remove unqualified novelty assertions and make no priority claim.
5. The original FKN article's metadata and abstract were accessible; its original full proof was not. Its 1971 erratum was opened and must accompany the citation. All other cited source statements were opened, including the original Coffman–Graham and Ullman papers and Garey–Johnson's actual OPEN8 entry.
6. The original dependency column uses several valid source labels for statements that actually occur in adjacent unnumbered prose. The exact 44-row concordance is supplied as machine-readable JSON and appended below.

## Verification record for source claims

| Check | Source opened and scope compared | Verdict and limit |
|---|---|---|
| S-P | OpenAI preprint, all thirteen attached files compared with pinned public files; Theorems 1.1 and 3.4, all dependency-column counterparts, constants and §9 accounting | Source correspondence checked; all bytes identical. Capacity-three counterparts do not themselves establish Q03's capacity-m replacements. |
| S-F | Pinned OpenAI scope, comparator target and actual `Scheduling/Model.lean` and `Main.lean`; all 53 scheduling files opened | Complete three-machine algorithm is the stated scope; actual proof body identified separately from comparator `sorry`. No independent Lean build/axiom audit. |
| S-D | drbh exact commit, `Model.lean`, `Main.lean`, list/certificate/formula files and commit diff | Complete four-machine release theorem is present in the source; general fixed-m extension is not a theorem in this commit. No independent Lean build. |
| S-N | Official arXiv v1 and published SODA 2025 paper, Theorem 1.1 | Attributed exact upper bound and bibliography checked. An upper bound does not prove a lower bound on the algorithm's actual running time. |
| S-A | Official arXiv v1 and ESA 2022 proceedings full text | Approximation guarantee, stated bound and bibliography checked; relation to exactness explained below. |
| S-FKN | SIAM publisher metadata/abstract for 1969 article | Two-processor unit-job scope and bibliographic data checked; original full article unavailable. |
| S-FKN-e | SIAM 1971 erratum, complete p.141 | Correction and complexity statement checked at source-statement level. |
| S-CG | Author-hosted original scan and Springer metadata | Two-processor optimality Theorem 1, p.203, and quadratic assertion, p.202, checked. |
| S-U | Original ten-page article scan and publisher metadata | Unit-job NP-completeness with processor number in the input, Theorem 1, p.389, checked. |
| S-GJ | Complete book scan, relevant pages visually inspected; bibliographic catalogue | OPEN8 in Appendix A13, p.287, and SS9, p.239, checked. |
| S-L | Course metadata and all eleven chapter sources | First eight byte-identical to attachments; last three explicitly derived from Q03. Advertised `provenance.json` URL unavailable (404). |
| S-J | Official arXiv v1 PDF, theorem and structural budget statements | Existing all-fixed-m statement and linear budgets checked for scope; full proof not independently audited. |
| S-G | Hexagon 2611.00060v1, full three-page PDF | Existing three-machine exponent claim checked for scope; full proof not independently audited. |

These S identifiers are intended for the post's verification record. They should not be relabelled L (formalization verified) or used as evidence that the entire external proof was independently reproduced.

## [P] OpenAI preprint — S-P

**URL:** [official preprint directory](https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026). **Pinned version:** repository commit `4eaee87548250b2682affda7d05d947c05554bae`, observed during this audit. **Title/byline/date:** *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling*, OpenAI, 24 September 2026. The title, author and date are in `build/paper.tex:63–67`.

The source directory initially returned a search-opening error. The pinned raw files were then retrieved successfully. `code/C_retrieve_compare.py` queried the repository commit and retrieved each of the thirteen paths supplied in the attachment. The complete per-file byte counts and SHA-256 comparisons are in `code/C_retrieve_compare_output.json`; every `equal` field is true. `code/C_preprint_byte_comparison.json` is a separately saved comparison from the same audit. No attached/published textual discrepancy was found at this pinned version. This compares these thirteen files, not all files or every historical repository revision.

### Exact claims and constants

| Item | Exact source locator | Statement compared and verdict |
|---|---|---|
| Theorem 1.1 | `paper.tex:120–130`, label `thm:main` | Explicitly listed unit jobs, arbitrary acyclic precedence, three identical machines, exact optimum and valid-deadline decision. Fixed deterministic multitape bound `O((L+2)^150020)`. Matches the base-case citation. |
| Real-time/integer-slot passage | `paper.tex:109–114` | The rounding argument appears in introduction prose; Q03 2.2 is separately numbered. |
| Fixed primitive budget | `paper.tex:313` | The finite family uses `K=10000`. |
| Family enumeration | Lemma 2.3, `paper.tex:328–338`, `lem:family` | Triple primitives yield `O(N^(3K))` formula bound. The coefficient 3 comes from slot size. |
| Hierarchy definition and implication | Definition 3.2, `paper.tex:423`; Lemma 3.3, line 438 | `def:hierarchy` and `lem:hierarchy-dp` are the exact counterparts. |
| Source structure theorem | Theorem 3.4, `paper.tex:456–460`, `thm:structure` | A hierarchy with fewer than 500 leaves in its required descriptions. The source does not state the Q03 symbolic budget `12m+25`. |
| List capacity | Lemma 6.4, `lists.tex:126–150`, `lem:list-length` | At most three injections and five entries. |
| Earlier-low extension | Lemma 6.6, `lists.tex:218–248`, `lem:old-low` | At most 21 leaves. |
| Entry bound | Lemma 6.8, `lists.tex:341–352`, `lem:entry-size` | A newly switched first entry is bounded by 25; the uniform stated entry bound is fewer than 40. |
| Construction validity | Proposition 7.3, `boundary.tex:140` onward, `prop:construction-valid` | Reuses the fewer-than-40 entry bound and the three boundary invariants. |
| Final numeric accounting | Lemma 8.3, `descriptions.tex:165–188`, `lem:final-count` | Qualifier union at most 195; same-cutoff 196; common allowance 205; high 197; low 209; node 406; relative bound 210 plus one removed-slot predicate. |
| Multitape accounting | §9, `paper.tex:488–524` | With `B=O_K(N^(3K))`, states `S=BN^3`, the dominant displayed bound is `B^5 N^13 = O_K(N^(15K+13))`. The proof finishes with explicit input exponent 150020. |
| Compact isolated jobs | Remark 9.1, `paper.tex:526`, `rem:compact` | Polynomial decision with compactly supplied isolates; no promise to list an exponentially large output schedule. |

All source labels appearing in the original Q03 dependency column exist. Label existence alone was insufficient: rows 4.3, 5.4, 6.3 and 8.1 point most precisely to unnumbered source definitions or equations before the cited lemma; rows 9.2 and 9.3 point to §9's actual accounting. The appendix makes those corrections. Source numbering was reproduced by `code/C_source_map.py` from the common theorem counter and expanded input order; `code/C_preprint_statement_map.json` has 29 numbered statements.

## [F] OpenAI formalization scope — S-F

**URL/version:** [`lean/docs/124.md` at the pinned OpenAI commit](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/124.md). **SHA-256:** `2d5e4213616aa59a02822ec073df5df1d057c1ee18d7a2ece021d3d660e26ff5` (977 bytes).

Line 9 describes nonempty unit jobs, arbitrary acyclic precedence, three machines, exact optimum/deadline output, one fixed finite machine and polynomial binary-input time. Its line 15 links the comparator target. In [`ComparatorChallenges/ThreeMachine.lean`](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ThreeMachine.lean), `ReleaseTheorem:86–93` has exponent 150020, but the target theorem ends in `sorry` at line 96.

The actual proof source was identified through the pinned directory API: [`Scheduling/Main.lean:59–84`](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/Scheduling/Main.lean) supplies the proof body; `Scheduling/Model.lean:86–93` supplies its release statement. Deleting the comparator's target theorem declaration (including its placeholder proof) yields byte-for-byte the actual Model.lean file, establishing the exact correspondence of definitions. All 53 scheduling files were opened; a text scan found no `sorry`, `admit` or top-level `axiom`. This neither replays Lean nor audits imported axioms. The source scope remains three-machine; no Q03 formalization is claimed. Metadata and exact hashes are in `C_followup_source_checks_output.json` and `C_openai_formal_sources_output.json`.

## [D] drbh exact commit — S-D

**Name/URL:** drbh, [scheduling-proof-exploration](https://github.com/drbh/scheduling-proof-exploration/tree/bbd30137258b15d8c5caedd035d72e8e8a875dbd). **Commit:** `bbd30137258b15d8c5caedd035d72e8e8a875dbd`, 8 October 2026, 13:51:17 UTC. **Archive:** 219623 bytes; SHA-256 `9c520af86eaaf60c9de151bcf7a02b0055d46b1a7bc4741870d472f269031268`. Exact archive and commit diff opened.

Paths are relative to `OAI/Computability/Scheduling/`. `Model.lean:16–20` sets capacity four. Its encoding lists all jobs; `CorrectOutput` specifies optimum or deadline/witness/NO output; `ReleaseTheorem:86–94` quantifies a fixed finite multitape machine and `C(L+2)^200022`. `Main.lean:59–84` proves `main_theorem : ReleaseTheorem`, for `n≥1`, acyclic instances and optional deadlines satisfying `1≤T≤n`. `EffectiveFamily.lean:170–195` enumerates four-element slots. `RunCertificates.lean` bounds entries by 29 leaves and lists by six entries; `PriorityUpdates.lean:418–430` uses `6·29=174≤195`.

Names `ThreeMachine` and `Triple` remain, but the definitions use four jobs. This commit's README describes the baseline; the explanatory update is later commit `6faeb33e9bf29c6e769fdd9fd49aa0567078ea5c`. The complete four-machine theorem is present; arbitrary fixed-m coverage is not. A text scan found no `sorry`, `admit` or top-level `axiom` in 53 scheduling files. The scan and author's build report are not an independent Lean verification. Credit drbh with this exact scope; “partial four-machine work” understates it.

## [N] Nederlof, Swennenhuis, Węgrzycki — S-N

**Bibliography:** Jesper Nederlof, Céline M. F. Swennenhuis, Karol Węgrzycki, *A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints*, SODA 2025, pp.535–552, [DOI 10.1137/1.9781611978322.16](https://doi.org/10.1137/1.9781611978322.16). [arXiv:2312.03495v1](https://arxiv.org/abs/2312.03495v1), 6 December 2023. Official arXiv text, publisher entry and [published proceedings PDF](https://research-portal.uu.nl/ws/portalfiles/portal/254249631/1.9781611978322.16.pdf) opened.

**Locator/claim:** Theorem 1.1, printed p.536, gives exact bound `(1+n/m)^(O(sqrt(nm)))`; §6, pp.545–547, derives it. For fixed m, this displayed upper-bound expression is `exp(O_m(sqrt(n) log n))`. Replace “not polynomial for fixed m” with that expression or “this displayed bound does not establish polynomial time.” An upper bound alone cannot establish a matching runtime lower bound. Statement and bibliography checked; the entire external proof was not independently re-proved.

## [A] Das and Wiese — S-A

**Bibliography:** Syamantak Das and Andreas Wiese, *A Simpler QPTAS for Scheduling Jobs with Precedence Constraints*, ESA 2022, LIPIcs 244, article 40, pp.40:1–40:11, [DOI 10.4230/LIPIcs.ESA.2022.40](https://doi.org/10.4230/LIPIcs.ESA.2022.40). [arXiv:2501.09091v1](https://arxiv.org/abs/2501.09091v1), 15 January 2025. The later arXiv submission is not the conference publication date.

**Locator/claim:** Theorem 1 in arXiv and ESA §1.1, p.40:3, give a `(1+ε)` approximation with displayed time `n^(O_{m,ε}((log n)^(m/ε)))`. ESA full text opened. Replace “approximation, not exact feasibility” with the guarantee. A precise connection exists: choose `ε=1/(n+1)`; integral makespans and `OPT≤n` give a returned value `<OPT+1`, hence the exact optimum. Substituting this ε into the stated bound does not establish polynomial time. This supplies the relation rather than a categorical separation.

## [FKN] and erratum — S-FKN, S-FKN-e

**Bibliography:** M. Fujii, T. Kasami, K. Ninomiya, *Optimal Sequencing of Two Equivalent Processors*, SIAM Journal on Applied Mathematics 17(4), July 1969, pp.784–789, [DOI 10.1137/0117070](https://doi.org/10.1137/0117070). **Erratum:** same authors, 20(1), January 1971, p.141, [DOI 10.1137/0120018](https://doi.org/10.1137/0120018).

Publisher metadata and abstract identify arbitrary precedence, equal unit lengths and two processors. Direct original-PDF access redirected to the abstract/access page; the original proof was unavailable. The [complete erratum](https://epubs.siam.org/doi/epdf/10.1137/0120018) corrects the appendix's alternating-chain construction and gives order `max(n^3,f(n))`, f being the general-graph matching bound. Add it to the bibliography. The classical two-machine statement also has directly opened source [CG]; that does not erase the unavailable original-FKN-proof limitation.

## [CG] Coffman and Graham — S-CG

**Bibliography:** E. G. Coffman, Jr., R. L. Graham, *Optimal Scheduling for Two-Processor Systems*, Acta Informatica 1, September 1972, pp.200–213, [DOI 10.1007/BF00288685](https://doi.org/10.1007/BF00288685). Springer metadata and [author-hosted scan](https://fanchung.ucsd.edu/ron/papers/72_04_two_processors.pdf) opened.

**Locator/claim:** §I, p.202, specifies arbitrary acyclic precedence, equal lengths and two processors and asserts quadratic order. §II, p.203, defines Algorithm A, then Theorem 1 proves its list optimal. Scaling equal lengths to one preserves precedence and machine-conflict relations and multiplies all completion times by the same positive factor, giving the unit-job statement. Pages 202–203 were visually inspected after OCR; OCR had misread some digits. Metadata, model and theorem scope checked.

## [U] Ullman — S-U

**Bibliography:** Jeffrey D. Ullman, *NP-Complete Scheduling Problems*, Journal of Computer and System Sciences 10(3), June 1975, pp.384–393, [DOI 10.1016/S0022-0000(75)80008-0](https://doi.org/10.1016/S0022-0000(75)80008-0). [Original full article scan](https://www.cs.montana.edu/bhz/classes/fall-2021/csci460/paper4.pdf) and publisher metadata opened.

**Locator/claim:** Definitions on pp.384–385 include processor number in the input. Theorem 1, p.389, establishes NP-completeness with all execution times one. §IV, p.392, separately asks about fixed processor count. The exact attribution is therefore the variable-m unit-job problem: this reduction produces varying processor counts and supplies no fixed-m hardness theorem. Avoid turning NP-hardness into an unconditional nonexistence assertion for polynomial algorithms. Source statement and parameter scope checked; no new conditional theorem is asserted.

## [GJ] Garey and Johnson — S-GJ

**Bibliography:** Michael R. Garey, David S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness*, W. H. Freeman, San Francisco, 1979. Front matter and [bibliographic catalogue](https://books.google.com/books/about/Computers_and_Intractability.html?id=fjxGAQAAIAAJ) checked.

The [book scan](https://perso.limos.fr/~palafour/PAPERS/PDF/Garey-Johnson79.pdf) exceeded the web opener's size limit; a full transfer was truncated. `C_gj_range_download.py` recovered all 13756924 bytes using validated ranges; SHA-256 `469e6d193212ee070db8f6df1a24782b2d15397edd368f0b66f1e089794633c2`.

**Locator:** Appendix A13, OPEN8, printed p.287 (two-page-scan PDF page 149) states the three-processor unit-job precedence/deadline problem. Its comment cites two-processor polynomial solvability and variable-processor NP-completeness. Appendix A5.2, SS9, p.239, gives the variable-m formulation. Both pages and front matter visually inspected. Say historically listed open there, not presently unresolved.

## [L] Course lessons — S-L

**URL:** [Scheduling unit jobs on three machines](https://kokunoyumeto.github.io/open-math-courses-public/courses/three-machine-unit-job-scheduling/). Index, `course.json`, `providers.json`, and all eleven `src/*.md` files opened. `code/C_course_compare_output.json` has URLs, sizes, hashes and comparisons.

All eleven content hashes match metadata; lessons 1–8 are byte-identical to attachments. Lessons 9–11 are dated 24 October 2026 and identify Q03 and three checks as their basis: derivative exposition, not independent verification. The course byline names Claude Opus 5.5, effort not recorded; review metadata marks author self-checking and incomplete independent review. The advertised `provenance.json` returned HTTP404. Page dates do not establish archived first-publication time: use “dated 24 October 2026; publicly accessible 15 November 2026.” CC0 1.0 is declared.

## [J] Jansen — S-J

Klaus Jansen, *Precedence Constraint Scheduling on a Fixed Number of Machines*, [arXiv:2611.09392v1](https://arxiv.org/abs/2611.09392v1), submitted 6 November 2026, 12:32:09 UTC. Official 72-page PDF retrieved (772097 bytes; SHA-256 `2b357c758514288db55efde8046f1f4d35a52c02a1736e08738a2742b2779d56`).

Theorem 1.1, p.1, states exact optimization for fixed `m≥3`, explicit jobs, RAM bound `O(L)+m^{O(m²)}n^{6m²+13m+1}log n`, and fixed-multitape bound `O(L)+m^{O(m²)}n^{12m²+26m+2}log³ n`; single-deadline uses `log² n`. Lemma 7.15, pp.64–66, supplies node budget `4m+5`, relative-cut budget `m+3`, qualifier union `3m`. Its subject overlaps both the all-fixed-m theorem and linear-leaf structure sought in Part D. The complete proof was not independently audited. Existing-publication claims must acknowledge it without attributing Q03's production to its author.

## [G] Giraudin — S-G

David Niedbala Giraudin, *Three-machine unit-job scheduling in time O((L+2)^276)*, [Hexagon 2611.00060v1](https://hexagonmath.org/pdf/2611.00060v1). The three-page PDF is dated 3 November 2026; platform listing 4 November. Theorem 1, p.1, states this multitape bound for three machines by reusing OpenAI structure with a smaller primitive family. Its theorem does not quantify arbitrary fixed m. Scope was compared; the entire proof was not independently audited. A blanket “no subsequent refinement found” statement would be inaccurate.

## Availability and limitations

| Attempt | Outcome and recovery |
|---|---|
| OpenAI directory/raw URLs in search opener | Some opens returned disabled/opening errors; pinned raw retrieval succeeded for every attached path. |
| drbh exact commit in search opener | Direct opening failed; commit API and exact codeload archive succeeded. |
| Jansen official arXiv in search opener | Direct open failed; full mirror opened, then official PDF retrieved successfully. |
| Original FKN PDF | Redirected to abstract/access page. Metadata/abstract checked; original proof unavailable; erratum accessible. |
| Garey–Johnson scan | Size-limit rejection, then truncated transfer; validated range download succeeded and pages rendered. |
| Course `provenance.json` | HTTP404. Other metadata and all chapters accessible. |
| OpenAI/drbh Lean builds | Not executed. Author-reported builds/axioms are not fresh L checks. |
| Jansen/Giraudin full proofs | Not independently re-proved. S-J/S-G concern declared scope only. |

## Reproducibility and packaging

`code/C_retrieve_compare.py`, `C_course_compare.py`, `C_gj_range_download.py`, `C_pdf_inspect.py`, and `C_source_map.py` reproduce retrieval metadata, comparisons, OCR locators and concordance; saved outputs accompany them. `C_search_history.json` stores query metadata and returned-result URLs. Newly retrieved full texts/scans/repository snapshots remain outside the deliverable tree. Early work copies moved to that external research cache are listed in `work/C_source_notes.md` with the reason for exclusion.

## Exact dependency source concordance

The following appendix is generated from `code/C_dependency_source_map.json`. It corrects column 2 only; Q03's internal Uses dependencies are checked in Part B. Source counterparts do not certify the generalized statements.

| Q03 id | Correct source entry | Exact label/location | Comparison |
|---|---|---|---|
| 2.1 | [P] Section 2.2 | paper.tex:283-297, frames and fixed topological rank | Topological rank is fixed in the source preliminaries; Q03 gives a separate lemma. |
| 2.2 | [P] Section 1 | paper.tex:109-114, floor/start-time argument | The real-to-integer schedule argument appears in unnumbered prose. |
| 2.3 | [P] Lemma 2.1 | `lem:padding`; paper.tex:254 onward | Capacity 3 counterpart. |
| 2.4 | [P] Lemma 2.2 | `lem:reorder`; paper.tex:271 onward | Capacity 3 counterpart. |
| 2.5 | [P] Section 2.2 | paper.tex:283-310, frame and cone definitions | Definitions/prose; no separate source lemma. |
| 2.6 | [P] Section 2.3 | paper.tex:322-324, complement by De Morgan | Prose before Lemma 2.3. |
| 2.7 | [P] Lemma 2.3 | `lem:family`; paper.tex:328 onward | The source counts triple primitives, hence exponent 3K. |
| 2.8 | [P] Proposition 3.1 | `prop:algorithm`; paper.tex:374 onward | Statement plus Section 3 dynamic program. |
| 2.9 | [P] Definition 3.2 | `def:hierarchy`; paper.tex:423 onward | Source definition of a bounded hierarchy. |
| 2.10 | [P] Lemma 3.3 | `lem:hierarchy-dp`; paper.tex:438 onward | Hierarchy-to-DP acceptance. |
| 3.1 | [P] Lemma 4.2 | `lem:separator-description`; separators.tex:35 onward | Separator description formulas. |
| 3.2 | [P] Lemma 4.2 | `lem:separator-description`; separators.tex:35 onward | Reversal is explicitly included in the statement and proof. |
| 3.3 | [P] Lemma 4.3 | `lem:lex-prefix`; separators.tex:59 onward | Normalized-prefix exchange. |
| 3.4 | [P] Lemma 4.4 | `lem:shared`; separators.tex:75 onward | Constituent one-advance argument inside the source proof. |
| 3.5 | [P] Lemma 4.4 | `lem:shared`; separators.tex:75 onward | Constituent fixed-cutoff walk inside the source proof. |
| 3.6 | [P] Lemma 4.4 | `lem:shared`; separators.tex:75 onward | Shared-cutoff walk statement and proof. |
| 3.7 | [P] Corollary 4.5 | `cor:any-ideal`; separators.tex:146 onward | Creating a separator. |
| 4.1 | [P] Section 5.1 | construction.tex:19-28, ordered keys | Key monotonicity is unnumbered prose. |
| 4.2 | [P] Section 5.2 | construction.tex:81-115, cover and center formulas | Cover equation and same/switch center separator. |
| 4.3 | [P] Section 5.2 | construction.tex:116-136, priority orders and cutoffs | Replace the original edge-label lemma label with these definitions and justification. |
| 4.4 | [P] Lemma 5.1 | `lem:edge-labels`; construction.tex:139-173 and Lemma 5.1 | Shared walk construction immediately before the lemma supplies common cutoffs. |
| 4.5 | [P] Lemma 5.1 | `lem:edge-labels`; construction.tex:175 onward | Edge boundary/cone/shrinking assertions. |
| 5.1 | [P] Lemma 6.1 | `lem:carry`; lists.tex:13 onward | Suffix-carry formula. |
| 5.2 | [P] Lemma 6.2 | `lem:prune`; lists.tex:35 onward | Pruning comparison. |
| 5.3 | [P] Lemma 6.3 | `lem:update-labels`; lists.tex:85 onward | Qualifier partition and child first invariant. |
| 5.4 | [P] Section 6.3 | lists.tex:115-120, run and combined rank thresholds | Replace list-length lemma label: entry shape is the preceding prose. |
| 5.5 | [P] Lemma 6.4 | `lem:list-length`; lists.tex:126 onward | Source has at most 3 injections and 5 entries; Q03 replaces capacity and bound. |
| 6.1 | [P] Lemma 6.5 | `lem:flatten`; lists.tex:175 onward | Flattening the initial pair. |
| 6.2 | [P] Lemma 6.6 | `lem:old-low`; lists.tex:218 onward | Source earlier-low extension has at most 21 leaves. |
| 6.3 | [P] Section 6.5 | lists.tex:254-268, equation (ancestry) | Replace G lemma label: arrangement is the preceding prose/equation. |
| 6.4 | [P] Lemma 6.7 | `lem:G`; lists.tex:281 onward | Switch upset. |
| 6.5 | [P] Lemma 6.8 | `lem:entry-size`; lists.tex:341 onward | Individual entry counterpart; the aggregate 6m+9 accounting is Q03-specific. |
| 7.1 | [P] Lemma 7.1 | `lem:past`; boundary.tex:18 onward | Second boundary invariant for children. |
| 7.2 | [P] Lemma 7.2 | `lem:swap`; boundary.tex:99 onward | Third boundary invariant for children. |
| 7.3 | [P] Proposition 7.3 | `prop:construction-valid`; boundary.tex:140 onward | Construction validity. |
| 8.1 | [P] Section 8.1 | descriptions.tex:16-40, cutoff-agreement/direct-same/direct-switch equations | Replace global-child lemma label: predicates are defined immediately before that lemma. |
| 8.2 | [P] Lemma 8.1 | `lem:global-child`; descriptions.tex:47 onward | Global child formula. |
| 8.3 | [P] Lemma 8.2 | `lem:relative-splits`; descriptions.tex:121 onward | Relative descriptions at marked slots. |
| 8.4 | [P] Lemma 8.3 | `lem:final-count`; descriptions.tex:165 onward | Source uses fixed numeric budgets; Q03 uses aggregate linear budgets. |
| 8.5 | [P] Theorem 3.4 | `thm:structure`; paper.tex:456 onward | Source theorem has fewer than 500 leaves; Q03 asserts 12m+25. |
| 9.1 | [P] Theorem 1.1 | `thm:main`; paper.tex:120-130 and Proposition 3.1 | The m=3 main result; capacity-m correctness requires the Q03 proof. |
| 9.2 | [P] Section 9 | paper.tex:488-524, proof of Proposition 3.1 | This is the actual source accounting, rather than only its proposition statement. |
| 9.3 | [P] Section 9 | paper.tex:520-524, input length and deadline trials | Actual input-exponent derivation; source final exponent is 150020. |
| 9.4 | [P] Remark 9.1 | `rem:compact`; paper.tex:526 onward | Compact isolated-job decision remark; no explicit-output size promise. |
