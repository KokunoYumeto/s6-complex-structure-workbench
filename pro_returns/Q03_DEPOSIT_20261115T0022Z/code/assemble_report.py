#!/usr/bin/env python3
"""Assemble the complete Q03 audit report, retaining every embedded audit byte.

Run after final post assembly and PDF/visual checks. The report includes all
six mathematical/provenance/integration work audits verbatim; its front summary,
per-task ledger, format checklist, and build tables describe the delivered state.
"""
from pathlib import Path
import csv,hashlib,json,re

BASE=Path(__file__).resolve().parents[1]
WORK=BASE/'work'
AUDITS=[
 ('Part A — full itemized accounting and Section 9 proof audit','A_accounting.md'),
 ('Part B — full independent audit of Sections 2–5.4','B_foundations.md'),
 ('Part B — full independent audit of Sections 5.5–8.5','B_hard.md'),
 ('Part E — full provenance and ancillary-file audit','E_provenance.md'),
 ('Part E — full mathematical integration audit','E_proof_integration.md'),
 ('Part E — full final consistency audit','E_final_consistency.md'),
]

def read_json(name,default=None):
    p=BASE/name
    return json.loads(p.read_text()) if p.exists() else default

def main():
    embedded=[(title,name,(WORK/name).read_text()) for title,name in AUDITS]
    visual_path=WORK/'visual_qa_report.md'
    visual=visual_path.read_text() if visual_path.exists() else None
    builds={k:read_json(f'work/{k}/build_check.json',{}) for k in ['build_before','build_revision_1','build_final']}
    final=builds['build_final']
    histories=read_json('code/C_search_history_complete.json',[])
    nqueries=sum(len(b.get('queries',[])) for b in histories)
    rows=list(csv.DictReader((BASE/'Q03_DEPOSIT_results.csv').open()))
    post=(BASE/'Q03_DEPOSIT_post.tex').read_bytes()
    gates='Complete; final user approval remains after delivery.' if visual else 'Mathematical and source work complete; final visual-QA insertion is pending in this working report.'
    parts=[]
    def add(s):parts.append(s.rstrip()+'\n\n')
    add(r'''# Q03_DEPOSIT: proof audit, corrected running time, and deposit revision

**Main result of this audit:** the full stepwise check found no false mathematical step in the stated m≥3 proof. The running-time calculation now proves the common explicit-input exponent **60m²+129m+2**, with an itemized deterministic multitape implementation and explicit effective coefficients. The padded exponent remains **60m²+129m+1**. The description hierarchy has global leaf budget **12m+25** and relative-prefix budget **6m+16**.

**Audit date:** 15 November 2026, Europe/Berlin. **Produced and checked by:** GPT-6 Astra (OpenAI), effort ChatGPT Pro mode. Parallel mathematical, accounting and source subreviews used the same model and mode. The attached earlier verdicts were preserved and examined; none was used as a premise of the new proofs. **Human understanding:** none recorded. **Formalization:** none of the present general-m proof. **Priority:** none claimed.''')
    add('**Package state:** '+gates)
    add(r'''The original +8 input exponent was a larger upper bound supported only by a sketch. The repaired accounting gives +2 directly. The proof review also makes the choice domain in Lemma 5.5 explicit, completes the Uses/dependency records, and verifies the two rewritten proof layouts against the producing return. No counterexample to the scheduling theorem or its structural statement was found or is claimed.

The source work materially changes the historical framing. The opened Jansen paper states the all-fixed-machine result and linear leaf budgets; drbh's exact cited commit contains the complete four-machine release-theorem code. OpenAI's comparator target uses a placeholder, while the separately opened scheduling source contains its actual proof body. The revised post credits those exact scopes and makes no novelty claim. The original FKN full article and the course archive endpoint have stated access limits. The supplied prompt is preserved unchanged, with an exact discrepancy against an absent prompt variant in the old artifact manifest disclosed.

## Deliverables and how this report is organized

The principal files are `Q03_DEPOSIT_post.tex`, `Q03_DEPOSIT_post.pdf`, this report, `Q03_DEPOSIT_results.csv`, `Q03_DEPOSIT_sources.md`, and `Q03_DEPOSIT_literature.md`. The post's record block and the separate form answers accompany the package. `anc/` preserves the supplied task, return and reports; `code/` contains the programs and their recorded outputs. The full proofs are in the post. This report includes the independent derivations of every step, rather than only referring the reader back to those proofs.

The first sections below give the task ledger, changes, source/literature findings, computational scope, format checks and build history. After that, the complete A, B and E audit files are embedded verbatim. Their earlier work-note wording, recommended edits and inspected-snapshot hashes are preserved for traceability; the disposition ledger identifies what was implemented. The historical numeric state-bound symbol S used in the A audit corresponds exactly to calligraphic S in the delivered Section 9, through the explicit rename S↦𝒮 with value BN^m. No mathematical set, bound or proof operation changes under that rename. Final layout counts are given in the build table below; an embedded audit's earlier inspected-snapshot count is identified by that audit's recorded source hash.

The companion source ledger supplies every source URL, version, locator and availability attempt; the literature ledger supplies the complete dated query record. Their principal conclusions and limits are also stated here, so this report is self-contained on the outcome and reasons for the revisions.''')
    add('## Per-task completion matrix')
    task_rows=[
('A.1','Done','All eight padded-call subroutines have tape layouts and explicit bounds. Formula, set, state and witness files are separate; all index bits and scans are charged.','Full Part A below, §§1–4; Proposition 9.2.'),
('A.2','Done','The input encoding gives n≤L; N≤mL on padded branches; at most L deadline trials add one exponent. The resulting exponent is 60m²+129m+2 with explicit G(m).','Full Part A §5; Corollary 9.3; corrected (1.1), abstract, Status and record.'),
('A.3','Done','B·𝒮·𝒮²·𝒮N=B⁵N^(4m+1), B=K512^K N^(mK), 𝒮=BN^m. With K=12m+25 this gives 60m²+129m+1.','Full Part A §§3–4; A_check_accounting.py/output.'),
('B.1','Done','Every numbered statement of Sections 2–9 is covered by independent stepwise arguments. No false mathematical step found. Choice-domain wording in 5.5 is made explicit.','All A/B audits embedded below; 44 numbered proof rows in CSV.'),
('B.2','Done','The three rewritten steps of 3.3 and four rewritten steps of 5.5 were compared with the return. The order-statistic and injection arguments retain their meaning.','B_foundations, Lemma 3.3; B_hard, Lemma 5.5 concordance.'),
('B.3','Done','All 44 Uses lines match the dependency table and CSV. Named references exist and precede the using statement; definitions and standing properties are identified explicitly.','E_proof_integration audit and checker; revised proof Uses lines.'),
('C.1','Done under the requested unavailable-source rule','All cited source claims were compared at exact locators or marked unavailable with attempts. Original FKN full text remains unavailable; its metadata/abstract and full erratum were opened.','Q03_DEPOSIT_sources.md; S-P through S-G records; source summary below.'),
('C.2','Done','All 44 source-counterpart rows corrected/verified, including unnumbered prose counterparts. S records name their scope and limits; unavailable text is listed in Limits.','C_dependency_source_map.json; source ledger appendix; post verification record.'),
('D.1','Done with stated search-index limits','All requested venues/directions searched; dated exact queries and outcomes retained. Jansen, drbh and Giraudin found; no matching fixed-m≥4 hardness claim located. No universal absence or exhaustive citation census asserted.','Q03_DEPOSIT_literature.md; source S-J/S-D/S-G; query metadata.'),
('E.1','Done' if visual else 'Text/file checks done; final visual-QA insertion pending','Status/record/declarations aligned; names/efforts and statement numbers checked; ancillary bytes preserved. Build and rendering record below.','Format checklist; E audits; final validation and visual record.'),
('E.2','Done','Demonstration notice/field removed; current GPT-6 Astra F,D,C,S audit recorded, dated 15 November 2026. Cost/proof items closed; exact source/provenance limits retained.','Post record, Verification record, Limits and open points.'),
('E.3','Done','Original not-claimed limits retained; no practical implementation, polynomial-in-m bound, unsupported variants or formalization claimed. No priority or optimal-exponent claim added.','Theorem A scope; Not claimed; Declarations; record block.'),
]
    add('| Task | State | What was settled | Evidence and post changes |\n|---|---|---|---|\n'+'\n'.join('| '+' | '.join(r)+' |' for r in task_rows))
    add(r'''## Exact mathematical outcome and principal edits

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

No numbered statement was dropped. The CSV contains every numbered statement and the three front-matter result rows. No mathematical counterexample was needed or produced.''')
    add(r'''## Part C — source findings, exact scope, and residual limits

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

## Part D — literature outcome and dated search record''')
    add(f'The search was conducted on **15 November 2026 (Europe/Berlin)**. The saved ledger currently contains **{len(histories)} batches and {nqueries} exact queries**, including a closing repeated search. The complete spellings, engine choices, returned headings/URLs and access limits are in `Q03_DEPOSIT_literature.md` and `code/C_search_history_complete.json`.')
    add(r'''The search covered the theorem for all fixed m≥4, the single case m=4, fixed-m hardness, linear description budgets, arXiv, STOC, FOCS, SODA, ICALP, IPCO, ESA, APPROX, authors' pages, GitHub, the general web and Hexagon. Exact-title and source-name searches also sought work citing or derived from the OpenAI preprint. The identified chain includes drbh, the course, Jansen, Giraudin, mathcommunity revision activity, the AI Proved What episode and Plectis Atlas indexing. Each has its role and evidence in the literature ledger.

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

## Part E — format checklist and delivery state''')
    checkrows=[
('1','Done','Every Status row is supported by the Verification record; claim, current-check types/verdict, human understanding, formalization and declared limits agree.'),
('2','Done','POST-RECORD, abstract, Status and Declarations agree on kind, bounds, claim, model/effort/date and check scopes.'),
('3','Done','All producing/checking models have an effort setting; original question/course use effort not recorded. Current-task author Opus max is included.'),
('4','Done with declared source-access limits','No external theorem is a proof premise. Every attributed source has an S row or precise unavailable scope in Limits, including original FKN full text.'),
('5','Done','Original numbering retained;44 proof statements + 3 front rows; full text/dependency/source correspondence checked. Symbol rename and explicit ranges documented.'),
('6','Done','OpenAI, drbh at exact commit, classical authors and discovered prior literature credited by name, URL and exact scope; no human authorship of Q03 added.'),
('7','Done','Literature search dated 15 November 2026, with closing repeated queries and exact query/result ledger; no priority claim.'),
('8','Done' if visual else 'Final build passed; visual-QA insertion pending','Final compilation counts are read dynamically below. All final pages rendered; visual inspection is documented in the inserted QA record before delivery.'),
('9','Done','Prompt, return and three reports preserved byte for byte in anc; current task also retained. No actual local paths/private identities/credentials found; prompt-manifest discrepancy disclosed.'),
('10','User approval remains after delivery','The package supplies the PDF, record block and form answers for review. No external publication or deposit was performed by this audit.'),
]
    add('| Format §8 item | State | Evidence |\n|---|---|---|\n'+'\n'.join('| '+' | '.join(r)+' |' for r in checkrows))
    add('### Compilation and visual verification')
    buildrows=[]
    for key,label in [('build_before','Supplied baseline'),('build_revision_1','Initial revised assembly'),('build_final','Final revised build')]:
        b=builds[key]
        buildrows.append((label,str(b.get('pages','pending')),str(b.get('overfull_count','pending')),str(b.get('overfull_over_2pt','pending')),str(b.get('max_overfull_pt','pending'))))
    add('| Build | Pages | Overfull boxes | More than 2pt | Maximum overflow(pt) |\n|---|---:|---:|---:|---:|\n'+'\n'.join('| '+' | '.join(r)+' |' for r in buildrows))
    add('The initial revised assembly had four 4.70132pt dependency-table alignment overflows and two 1.4092pt verification-header overflows. Column widths were corrected. The final build data above are read from `work/build_final/build_check.json`; its complete log and console outputs are retained. The current final log has no undefined-reference/citation or fatal-error message. Final layout adjustments also address the isolated Theorem A Uses line and the separated 8.1 heading observed during visual review; the exact final inspection record follows.')
    if visual:add(visual)
    else:add('<!-- VISUAL_QA_PENDING -->\n**Final visual-QA insertion pending in this working report.** The assembling agent is reviewing the rendered final pages and will write `work/visual_qa_report.md`; rerunning `code/assemble_report.py` inserts that exact record and completes checklist item 8. This marker must be absent from the delivered report.')
    add(r'''### Preservation, supersession and exclusions

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

The following six files are included in full, with their original text. Every embedded record is identified by filename; the generator checks exact inclusion and records its SHA-256 in `code/assemble_report_output.json`.''')
    for title,name,content in embedded:
        add('---\n\n## '+title+'\n\nSource record: `work/'+name+'`. Full text follows.\n\n<!-- BEGIN '+name+' -->')
        parts.append(content)
        if not content.endswith('\n'):parts.append('\n')
        add('\n<!-- END '+name+' -->')
    report=''.join(parts)
    for _,name,content in embedded:assert content in report,name
    out=BASE/'Q03_DEPOSIT_report.md';out.write_text(report)
    info={'report':out.name,'bytes':len(report.encode()),'words':len(report.split()),
      'sha256':hashlib.sha256(report.encode()).hexdigest(),'embedded_audits':[
        {'file':'work/'+name,'bytes':len(c.encode()),'sha256':hashlib.sha256(c.encode()).hexdigest(),'included_verbatim':True} for _,name,c in embedded],
      'visual_QA_included':visual is not None,'visual_QA_marker_remaining':'VISUAL_QA_PENDING' in report,
      'build_counts':builds,'CSV_rows':len(rows),'search_batches':len(histories),'search_queries':nqueries,
      'post_sha256_at_assembly':hashlib.sha256(post).hexdigest()}
    (BASE/'code/assemble_report_output.json').write_text(json.dumps(info,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(info,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
