"""Build the live complete discrepancy report from retained audit records.

This is a reporting program, not a proof verifier. Completion is read only
from separately written paper-validation records and the final package gate.
"""
from pathlib import Path
import csv,json,re,collections

OUT=Path(__file__).resolve().parents[2]
report_path=OUT/'S6_09_PAPERS_report.md'
initial=OUT/'records/report_initial.md'
if not initial.exists():initial.write_text(report_path.read_text())
rows=list(csv.DictReader((OUT/'S6_09_PAPERS_inventory.csv').open()))
def load(rel,default=None):
    p=OUT/rel
    return json.loads(p.read_text()) if p.exists() else default
def meta(s):
    s=s.replace('GPT-6 Astra (OpenAI, ChatGPT Pro mode),',
                'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro),')
    s=s.replace('GPT-6 Astra (OpenAI, ChatGPT Pro mode)\n',
                'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026\n')
    return s
valid={x:load('records/'+x+'_final_validation.json',{}) for x in ['I','II','III']}
complete=bool(load('records/final_package_gate.json',{}).get('passed'))
text=('COMPLETE' if complete else 'INCOMPLETE')+'''\n
# S6_09_PAPERS — writing, proof comparisons and discrepancy record

The writing began on 16 November 2026 at 23:47 UTC. The principal task is the three complete papers. The required sequence is inventory, Paper I with all checks and PDF inspection, Paper II, Paper III, and a final common-reference check. Parallel readers may check later material while the preceding paper is being completed; this does not constitute assembly of a later paper.

## Completeness and current state

The inventory preserves all 745 run rows and the original 183 additional working-edition/course rows. Additional classical prerequisite results and worked examples have been added as explicitly identified provider rows: INVENTORY_TOTAL rows in total, in the required 17 columns. The added provider rows preserve full statements, proofs, source provenance and distinct audit scopes. No original row was removed or replaced. The run counts are INV 47, FAM 55, PUSH 154, CDP 239, MAPS 198, and ARI Part C 52. Producing-run badges are provenance, not independent verification. A historical recorded check counts at its stated scope; a title comparison, a statement reading, a full proof reading, an original-source hypothesis match and a computational rerun remain different events.

| Paper | Assigned rows | Validation state |
|---|---:|---|
'''
text=text.replace('INVENTORY_TOTAL',str(len(rows)))
class ReportText:
    """Append without repeatedly copying the multi-megabyte audit history."""
    def __init__(self, initial): self.parts=[initial]
    def __iadd__(self, addition): self.parts.append(addition); return self
    def __str__(self): return ''.join(self.parts)
    def __len__(self): return sum(map(len,self.parts))
text=ReportText(text)
for paper in ['I','II','III']:
    state=valid[paper].get('status','Writing/checking in progress' if (OUT/f'S6_09_PAPERS_{paper}.tex').exists() else 'Not assembled; the required sequence is being observed')
    text+=f"| {paper} | {sum(r['paper']==paper for r in rows)} | {state} |\n"
text+='''
Each printed result has its complete proof in the main text or a linked appendix. Shared statements retain every distinct proof. The result index is a concordance; neither it nor a repository pointer replaces a proof. Programs are named, their commands and outputs are retained, and the mathematical argument specifies what their results establish. A failed argument remains visible with its correction or with its precise gap.

## Models, dates and methodology

The working edition was AI-produced by GPT-5.6 Sol (OpenAI), Codex reasoning effort ultra, 24 August–9 September 2026, with a few inputs by GPT-5.6 Sol (OpenAI), ChatGPT Pro mode, 24 August–9 September 2026. The six research runs were AI-produced by GPT-6 Astra (OpenAI), ChatGPT Pro mode, 12–16 November 2026. The current writing and independent readings are by GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, 17 November 2026. The historical readings were by Claude Fable 5.2 (Anthropic), effort high and effort max, and Claude Opus 5.5 (Anthropic), effort max, 12–16 November 2026, at the dates and scopes retained per event. Where a report header differs from the registry, the report header controls.

The attached course is an additional provenance stratum: its course.json and provenance.json name GPT-6 Astra (OpenAI), Codex reasoning effort ultra, 9 October 2026; individual companion chapters carry exact dates from 8 through 11 October 2026. GPT-6.1 Sol (OpenAI), effort ultra, October 2026 providers retain their header-level date distinctions, including headers without an exact day. Retained prerequisite providers have their own source provenance. These are not silently attributed to the August–September working edition. The final chapter-specific record controls the provenance of each retained course argument.

No human has checked the mathematics. No person is named as an author of or contributor to this work. The work is AI-produced, and the text is dedicated under CC0 1.0. Other authors receive credit only for their own results and sources.

The requested wording identifying ChatGPT Pro mode with one universal highest effort setting is not supported by the official documentation opened in this writing. That documentation distinguishes reasoning mode from reasoning effort. The papers therefore retain the recorded Pro-mode designation, explain the distinction, and do not assert the unsupported equivalence. Anthropic's opened official effort documentation identifies max as its maximum capability setting. The exact sources and opened scopes are retained below and in the bibliography.

## Credit and allowed date statements

The original AC26 PDF controls every difference with the searchable transcription. The standard mod-2Z classification is attributed to DGKX version 1, Theorem 1.4; that version is dated 23 September 2026, version 2 omits the result, and the complete public working-edition proof was present by 8 September 2026. These are the only comparative date statements about results. The standard tangent dimensions, Kuranishi germ and full automorphism group are expressly re-derived after reading DGKX version 1. AC26 receives credit for the contradiction to CDP20, Corollary 2.3. Source searches record found loci or the actual searched scope; a failure to find a matching statement is not an exhaustive literature-absence claim.

## Principal corrections and distinctions

1. The invariant source's reversed-meridian matrix is Q=P_mark S. It is not interchangeable with the required FAMILY matrix. Positive base loops, clockwise analytic root decks, affine twist vectors and collar integration orientations are transported explicitly.
2. The order-four Albanese lattice contains the factor 1/2. Its nome is iw/216; the order-three nome is −w²/48³, and their relation is q1=(27/64)q2². The Engel reference lift is fixed at c=0, so its parameter is w² with that specific linearization.
3. The degree-one cusp-torsion assertion is false in AC26's original PDF, Remark 9.21 on page 81. It is not merely a transcription error. The full local module calculation proves that degree-one torsion is supported on the two multiple fibres, while degree-two cusp torsion remains. Remark 1.3 must be qualified by degree.
4. The historical FAMILY questions C.3.3 and E.1.5 retain their entire local arguments, but their printed headings and inventory kinds identify the subsequent complete boundary and virtual-Euler exclusions. They are not counted among the outstanding questions.
5. The strongest filling obstruction uses the actual affine origins. The former reading's unverified origin-comparison step has been derived from the marked cusp gluing, with the radial gamma defect and all finite twists retained. A linear lattice comparison alone is not treated as that proof.
6. The obsolete global-meridians program failed. Its corrected successor and the independent quotient fixed-space computation passed. Both outputs remain. The all-fan homology program required a dependency-ordered rerun; its initial failure and successful rerun remain.
7. The normalized norm and the Betti measure require the stated orientation and factor 12. The Cayley coordinate is chi=(tau−i)/(tau+i), with k=pi²E4(i) and z=k chi². Source-local symbols and scalings are transported by the shared notation dictionary; the earlier report's k_chi shorthand was ambiguous and is superseded by this explicit formula.
8. The two source entries named Brunella1999 are different works. The forms paper has been given the separate key Brunella1999Forms; the original forms PDF identifies Marco Brunella, overriding an erroneous author field on the publisher HTML. Metadata checking does not by itself verify its use in a proof.
9. The analytic base-change checks retain their precise domains. Reduced-base Bănică–Stănăşilă statements are not silently used for nonreduced Kuranishi bases. The local one-variable Kuranishi algebra and the nonzero actual-family map provide the required argument.
10. The provisional MAPS fourfold torsion differential has a complete Fox/Wang calculation in the audit supplement. The finite Smith computations alone would not identify the geometric differential. The earlier factor-four shortcut is not retained as a proof.
11. The general-cusp deck quotient uses the actual triangle-monodromy deck group. The fundamental group of the punctured base is not substituted for that deck group. Compact chart subsets, rather than a false assertion of properness on an entire open chart, supply the quotient separation argument.
12. The two marked modular collisions 50/II and 56/II now have a complete geometric realization proof, primitive junction and gauge calculations, and an independently rerun exact certificate. Matching numerical invariants alone is not used to identify a geometric filling.
13. The fourfold chain comparison includes the explicit cyclic bar inclusion and the logarithmic cylinder hypotheses. The rank-six adapter distinguishes homology matrices A-transpose and B-transpose from the inverse matrices defining the left cohomology action. Exact finite computations do not replace the geometric argument.
14. The initial fourfold program run had six invocation, layout or timeout failures. Every operative program subsequently completed with valid input and the documented layout. The two independent fresh homology runs, the marked gluing enumeration and the actual Hecke tuple tests are retained alongside all earlier failures. No infinite enumeration is claimed to have been executed.
15. The coefficient and stable-homotopy providers retain all weights, polynomial coefficients before inversion, the full cobar matrices, minor witnesses and the separate geometric correspondence. The course conversion restores twenty substantive mathematical tails and preserves all available diagram captions. Thirty-seven referenced image assets were not supplied; the paper says so and gives their complete source descriptions without claiming to have inspected the missing images.
16. The almost-complex obstruction for the twelve-sphere is credited to Borel–Serre with all three source re-derivations retained in the known-results appendix. The fixed-orientation homotopy class of the almost-complex structure is credited to AC26, Section 1.4, with the full section-bundle argument printed.
17. The fixed-metric carrier and retained-angle arguments are printed in full. Their topology distinguishes intrinsic rescaled flat limits from ambient tangent geometry. The retained-angle class detects the specified quotient through a framed torus of Arf invariant one; no order or splitting beyond the proved detection statement is asserted.
18. The invariant-circle geometry in PUSH C.3.1 is credited to AC26, Proposition 9.24 and Remark 9.25, and to the exact DGKX version-1 shift formulas. The retraction used in PUSH C.3.8 is credited to AC26, Proposition 7.2; its additional primitive quotient calculation remains separately identified.
19. Original bibliography metadata have been reconciled, including the actual Poénaru title, the Reiser volume-year, the issue-only Zhubr citation and the author-manuscript status of Peters–Sterk. Thirteen title collisions are resolved explicitly. Version-specific course references distinguish the original author versions from later publication-year labels; Newlander–Nirenberg is cited through the actually opened Russian translation and the full receiving proof.
20. The final credit pass closes fifty stale Paper II comparison fields: five invariant results, thirty working-edition CDP results and fifteen correction-note results. The known standard-pencil stability statement is explicitly credited to DGKX version 1 and AC26; its complete original proof is moved byte for byte to the existing known-results appendix. The three distinct all-Picard proofs remain printed with their common known conclusion credited. No existing theorem or equation number changes.
21. The finite free-complex theorem in Bănică–Stănăşilă is Chapter III, Section 4, Theorem 4.1, page 124. Two inherited citations to Chapter III, Section 3, Theorem 3.4 were corrected after opening the original. The latter theorem is a different base-change criterion. The receiving hypotheses and complete argument are retained.
22. Eleven previously checked standalone wording corrections in the PUSH appendix were lost in a fresh assembly because the assembler incorrectly filtered on an audit status that had changed from proposed to applied. A complete current-source comparison detected the regression. The eleven exact passages were restored and the assembler filter corrected; all thirty-four complete PUSH blocks and all 189 displayed expressions were independently compared again. The observed failure record is retained.
23. Source-inherited raw LaTeX fences, theorem/proof boundaries and misplaced course anchors were checked against the full source chapters. Exact corrections preserve all mathematical arguments; the final comparison covers all thirty-three complete chapters and all 249 registered units. The complex-linearity comma and the proof-end glyph were corrected separately, with their original text and mathematical checks retained.
24. Current inventory wording is distinguished from historical evidence. Obsolete not-yet-printed prefixes are replaced only where the actual final statement and its independent check are present; their full old fields remain in the edit ledger. A missing earlier-reader record is stated as an absence of a located prior check, not invented or confused with the current independent reading. The final notation record supersedes its early partial snapshot, which is retained explicitly as history.
25. Identical works cited under inherited source keys are retained as bibliography aliases for exact source traceability. In particular, Paper II's CDP2020 entries labelled 2020a/2020b identify the same published work, and its AC26 entries labelled 2026a/2026b/2026c identify the same original PDF. These suffixes distinguish retained keys, not distinct works or independent sources. The full collision ledger identifies the aliases and the authoritative metadata; no mathematical inference counts them as separate evidence.
26. The final printed companion-reference check covers 294 occurrences and 92 distinct destinations, with no wrong theorem type, broken destination or range interior. It records one harmless duplicated “Paper I” prefix before the correctly identified Theorem 21.58 in Paper III. The exact wording observation remains disclosed; it changes no statement, implication or reference target.

## Exact boundaries retained in the separate final parts

Paper I retains the unevaluated literal global coefficient atlas for chosen smooth representatives and the unconditional transcendence question for the normalized norm at a nontorsion point. The cohomology classes, products, metric-type assertions and conditional arithmetic statements proved in the body are not declared open by those boundaries.

Paper II retains the splitting of the specified rank-three comb kernel bundle. Its proved degree bounds and examples show why rank and degree alone do not determine the splitting. The Kuranishi germ, vanishing obstruction map and tangent dimensions are established independently by the complete period-section argument.

Paper III retains the precise unclassified star-log and torsion-marked fillings of MAPS D.2.4. For the specified OS45/default weighted example, the remaining refined class is 0 versus 4 in Z/8; the primitive cubic, fundamental-class invariant, absolute characteristic classes and all explicitly stated preceding subcases are established. These are mathematical boundaries of the printed arguments, not unread proof batches.

## Format decisions

The full binding post format, its template and its worked example were opened. LuaLaTeX replaces the format template's pdfLaTeX because the task explicitly requires LuaLaTeX. Every paper is one self-contained TeX source with an inline bibliography. Long result, notation, verification and program tables belong in appendices. Proofs keep their checked local subdivision when forcibly rewriting every paragraph into a new step numbering would obscure the exact source comparison; the complete reasoning is retained. Source numbers are mapped to actual printed numbers in the full concordance. Typed status is carried by the statement, its caption or explicit credit, and the separate final part. The front matter is kept near the requested three-page scale and is visually checked. No mathematical argument is shortened to meet a page target.

## Typesetting: before and after

The per-build table below records every saved paper build. Failed or intermediate runs are not delivery passes. One distinct long inline exterior-power basis caused the 6.88432pt overflow; it was repaired with explicit mathematical break opportunities. The final validation file records the current pages corresponding to that location and every page inspected as an image.

| Build | Completed PDF in log | Overfull boxes | Boxes exceeding 2pt | Maximum excess (pt) |
|---|---|---:|---:|---:|
'''
stats=[]
for p in sorted((OUT/'editorial').glob('S6_09_PAPERS_*_build_*.stdout.txt')):
    s=p.read_text(errors='replace'); boxes=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([\d.]+)pt',s)]
    if s.startswith('INCOMPLETE\n'):
        stats.append({'build':p.name,'log_kind':'Misdirected report, not a build log','completed_pages':None,'overfull':None,'over_2pt':None,'max_pt':None})
        text+=f"| {p.stem} | Preserved report miswrite; excluded from build evidence | n/a | n/a | n/a |\n"
        continue
    pdf=re.search(r'Output written on .*?\((\d+) pages',s)
    item={'build':p.name,'completed_pages':int(pdf[1]) if pdf else None,'overfull':len(boxes),'over_2pt':sum(x>2 for x in boxes),'max_pt':max(boxes,default=0)}
    stats.append(item)
    text+=f"| {p.stem} | {pdf[1]+' pages' if pdf else 'No completed PDF recorded'} | {len(boxes)} | {item['over_2pt']} | {item['max_pt']:.5f} |\n"
(OUT/'records/typesetting_build_history.json').write_text(json.dumps(stats,indent=2)+'\n')
text+='\n## Full root proof and source-comparison record\n\nThe retained reading records preserve the actual chronology, including reservations and failed attempts later resolved. Earlier progress wording is historical evidence; the final per-result outcome, explicit closure events and current validation records govern the delivered state. Nothing in a historical partial reading is silently promoted to a complete proof check.\n\n'
root_audit=meta((OUT/'work/root/proof_audit.md').read_text())
text+=root_audit+'\n'
for title,rel in [('Invariant and arithmetic corrections','work/invariants_arithmetic/corrections.json'),
                  ('CDP technical corrections','work/cdp_audit/TECHNICAL_CORRECTIONS.md'),
                  ('MAPS proof and dependency record','work/maps_audit/audit_notes.md'),
                  ('Bibliography collision resolutions','records/bibliography_collision_resolutions.json'),
                  ('Statement-kind corrections','records/inventory_kind_corrections.json'),
                  ('Paper II mathematical and editorial changes','records/II_editorial_mathematical_changes.json'),
                  ('Paper I final validation','records/I_final_validation.json'),
                  ('Paper II working citation normalization','records/II_working_citation_normalizations.json'),
                  ('Paper II standalone reference corrections','records/II_standalone_reference_corrections.json'),
                  ('Paper II exact known-result credits and moves','records/II_positive_credit_changes.json'),
                  ('Paper II Kodaira citation closure','work/cdp_audit/kodaira_citation_closure.json'),
                  ('Paper II complete two-parameter proof checks','work/root/II_push_E5_full_checks.json'),
                  ('Writing-stage carrier and relative-bordism repairs','work/maps_audit/independent_repair_reviews.json'),
                  ('Paper II final validation','records/II_final_validation.json'),
                  ('Complete root fourfold receiving-proof readings','work/root/maps_F_proof_audit.md'),
                  ('Published integral-isomorphism algorithm: exact hypotheses','work/root/BHJ22_source_check.json'),
                  ('MAPS D complete proof and computation audit','work/invariants_arithmetic/maps_D_completion_summary.json'),
                  ('MAPS D precise remaining questions','work/invariants_arithmetic/maps_D_remaining_questions.json'),
                  ('Independent modular collision realization proof review','work/cdp_audit/modular_collision_review/independent_review.json'),
                  ('Rank-six algebraic Hecke tests','code/root_maps_F/hecke_algebraic_execution_record.json'),
                  ('Rank-six original program reruns and superseded invocation failures','code/root_maps_F/execution_manifest.json'),
                  ('Rank-six documented CLI and fresh chain reruns','code/root_maps_F/cli_execution_manifest.json'),
                  ('Complete course proof conversion and exact ranges','work/maps_audit/III_course_conversion_manifest.json'),
                  ('Course provenance and illustrative-content moves','work/maps_audit/III_course_conversion_moves.json'),
                  ('Bibliography title collisions and publication metadata','records/bibliography_collision_review.json'),
                  ('Paper III final receiving and dependency closure','work/maps_audit/III_final_closure_overlay.json'),
                  ('Paper III MAPS source-to-print comparison','work/maps_audit/III_MAPS190_source_to_print_check.json'),
                  ('Paper III independent D69 source-to-print comparison','work/invariants_arithmetic/maps_D_source_to_print_check.json'),
                  ('Paper III PUSH source-to-print comparison','work/cdp_audit/push_C_retention/full_retention_review.json'),
                  ('Paper III integrated PUSH comparison after exact editorial repairs','work/cdp_audit/push_C_retention/final_integrated_retention.json'),
                  ('Paper III complete chapter-reference corrections','work/maps_audit/III_course_common_reference_repairs.json'),
                  ('Paper III final chapter-reference gate','work/maps_audit/III_course_common_reference_final_gate.json'),
                  ('Paper III observed course label and proof-boundary repairs','records/III_course_structure_repairs.json'),
                  ('Independent complete course statement/proof boundary review','work/invariants_arithmetic/course_statement_proof_boundary_review.json'),
                  ('Independent complex-linearity punctuation verification','work/invariants_arithmetic/almost_complex_complex_linearity_typography.json'),
                  ('Final omitted-glyph and undated-source corrections','records/final_glyph_and_undated_entry_repairs.json'),
                  ('Paper I nonoperative comparisons removed from three Uses lines','work/invariants_arithmetic/paper_I_nonoperative_Uses_corrections.json'),
                  ('Paper III source inherited superscripts and exact reference corrections','records/III_push_typography_and_reference_corrections.json'),
                  ('Paper III standalone PUSH locators','records/III_push_standalone_edits.json'),
                  ('Final standalone exact source and program locators','records/I_final_standalone_fixes.json'),
                  ('Final standalone MAPS companion locators','records/III_final_standalone_fixes.json'),
                  ('Final numbered companion overview','records/common_numbered_companion_overview.json'),
                  ('Exact final printed inventory statements','records/common_printed_statement_refresh.json'),
                  ('Paper III course argument and equation retention','work/maps_audit/III_course_retention_review.json'),
                  ('Paper III exact final complete course chapter and249-unit retention','work/maps_audit/III_course249_final_source_to_print_check.json'),
                  ('Paper III complete course provenance','records/III_producer_concordance.json'),
                  ('Paper III explicit source-alias corrections','work/root/III_prompt_alias_corrections.json'),
                  ('Paper III final program catalogue','records/III_program_index.json'),
                  ('Paper III geometric verifier reruns','work/cdp_audit/course_geometric_execution_manifest.json'),
                  ('Paper III full late carrier readings','work/root/late_carrier_full_reading.json'),
                  ('Paper III native-period prerequisites','work/root/carrier_prerequisite_independent_review.json'),
                  ('Paper III exact layout repairs','records/III_layout_repairs_build10.json'),
                  ('Paper III retained known twelve-sphere obstruction proofs','work/cdp_audit/carrier_S12_route_validation.json'),
                  ('Fourfold execution failure reconciliation','code/root_maps_F/final_execution_reconciliation.json'),
                  ('Paper III final metadata and external-reference review','work/maps_audit/III_final_historical_metadata_review.json'),
                  ('Paper III exact external-reference wording','records/III_external_reference_wording_repairs.json'),
                  ('Paper II final credit and locator repairs','records/II_final_attribution_and_locator_repairs.json'),
                  ('Paper II final exact full-source retention chain','records/II_final_exact_retention_chain.json'),
                  ('Paper II final six credit insertions and result concordance','records/II_final_credit_index_refresh.json'),
                  ('Paper II final inline bibliography refresh','records/II_final_inline_bibliography_refresh.json'),
                  ('Paper II final number and reference-kind identity','records/II_final_label_identity_check.json'),
                  ('Paper II premature AUX diagnostic during an active build','records/II_label_check_during_active_build.json'),
                  ('Paper III observed PUSH assembly regression','work/cdp_audit/push_C_retention/current_editorial_regressions.json'),
                  ('Paper III exact final restoration of eleven checked passages','records/III_final_push_prose_restoration.json'),
                  ('Paper III final complete PUSH block comparison','work/cdp_audit/push_C_retention/current_final_retention.json'),
                  ('Final per-row credit and status closure','records/final_credit_closure_merge.json'),
                  ('Final exact inventory current-status corrections','work/invariants_arithmetic/final_inventory_current_status_applied.json'),
                  ('Final all-seventeen-column inventory and credit gate','work/invariants_arithmetic/final_inventory_completeness_credit_gate.json'),
                  ('Exact canonical and retained alias-number agreement','records/final_credit_alias_validation.json'),
                  ('Final five INV credit comparisons','work/invariants_arithmetic/inv_E_credit_comparison_5.json'),
                  ('Final correction-note fifteen-result comparisons','work/maps_audit/correction_note15_credit_overlay.json'),
                  ('Final thirty working-edition CDP credit comparisons','work/cdp_audit/II_working_credit/working_credit_comparison_30.json'),
                  ('Final working-edition credit overlay validation','work/cdp_audit/II_working_credit/overlay_validation.json'),
                  ('Final program-manifest fingerprint reconciliation','work/cdp_audit/III_program_manifest_fingerprint_refresh.json'),
                  ('Final program-manifest exact operative-event comparison','work/cdp_audit/III_program_manifest_fingerprint_refresh_2.json'),
                  ('Final notation concordance','records/notation_concordance.json'),
                  ('Final public notation-record reconciliation','records/notation_concordance_final_refresh.json'),
                  ('Final actual course anchor and theorem-label attachment check','work/invariants_arithmetic/final_course_anchor_AUX_check.json'),
                  ('Final all-paper package gate','records/final_package_gate.json'),
                  ('Independent final original-CSV and all-paper gate','work/maps_audit/final_package_independent_gate.json'),
                  ('Final exact printed companion-number and kind check','work/invariants_arithmetic/final_companion_reference_gate.json'),
                  ('Checkpoint-history self-reference correction','records/checkpoint_retention_self_reference_fix.json'),
                  ('Observed checkpoint save size-limit failure','records/checkpoint_06_library_retry.json'),
                  ('Lossless representation of the same sixth hourly checkpoint','records/checkpoint_06_lossless_repack.json'),
                  ('Exact byte-identical visual asset aliases and retained paths','records/visual_asset_deduplication.json'),
                  ('Independent exact ZIP size and duplicate-byte assessment','work/cdp_audit/delivery_compression_audit/standard_zip_exact_size_dry_run.json'),
                  ('Alternative compression attempt and explicit interruption','work/maps_audit/checkpoint06_lossless_encoding.json'),
                  ('Final archive restoration validation','work/invariants_arithmetic/archive_restoration_validation/validation_report.json'),
                  ('Exact final delivery scope and mathematical boundaries','records/final_delivery_scope.json'),
                  ('Paper III final validation','records/III_final_validation.json')]:
    file=OUT/rel
    if not file.exists():continue
    text+='\n## '+title+'\n\nSource record: `'+rel+'`.\n\n'
    content=meta(file.read_text())
    text+=('```json\n'+content+'```\n') if file.suffix=='.json' else content+'\n'
text+='''
## Results moved between papers

| Source | Result | Paper | Printed label |
|---|---|---|---|
'''
defaults={'S6_02_FAMILY':'I','S6_02_PUSH':'I','S6_01_INVARIANTS':'I','S6_03_CDP':'II','S6_04_MAPS_MANIFOLDS':'III','S6_05_ARITHMETIC':'I'}
for r in rows:
    expected=defaults.get(r['source_run'])
    if r['source_run']=='S6_01_INVARIANTS' and r['source_id'].startswith('E'):expected='II'
    if expected and r['paper']!=expected:
        text+=f"| {r['source_run']} | {r['source_id']} | {r['paper']} | `{r['printed_label']}` |\n"
text+='\n## Per-result wording, corrections and final outcomes\n\nThe exact seventeen-column inventory is the controlling result concordance. The following decision ledger includes each assigned row, its content-sensitive wording record, outcome and remaining qualifications. Historical events in the row remain historical; the final receiving event governs the printed status.\n'
for r in rows:
    text+='\n### '+r['source_run']+' / '+r['source_id']+'\n\n'
    text+='Paper '+r['paper']+'; label `'+r['printed_label']+'`; kind: '+r['kind']+'.\n\n'
    for heading,field in [('Wording against the source','wording_vs_source'),('Final outcome','check_outcome'),('Discrepancies and decisions','notes')]:
        if r[field].strip():text+='**'+heading+'.** '+r[field]+'\n\n'
text+='\n## Original-source opening records\n\nEach entry gives the actual scope checked. A downloaded or identified source is not thereby verified. The shared bibliography contains the operative verification state, including explicit unverified nonoperative comparisons.\n'
source_records=['work/root/references_verified.json','work/invariants_arithmetic/references_verified.json',
            'work/invariants_arithmetic/working_references_verified.json','work/cdp_audit/references_verified.json',
            'work/maps_audit/references_verified.json','work/maps_audit/wb_foundation_source_checks.json',
            'work/maps_audit/topology_source_checks.json','work/cdp_audit/maps_E/references_verified.json',
            'work/cdp_audit/modular_collision_review/references_verified.json',
            'work/invariants_arithmetic/maps_D_references_verified.json',
            'work/invariants_arithmetic/maps_F_references_verified.json',
            'work/maps_audit/stable_primary_source_checks.json',
            'work/maps_audit/fourfold_priority_source_checks.json',
            'work/maps_audit/duality_euler_source_check.json']
source_records+=sorted(str(p.relative_to(OUT)) for p in (OUT/'work').rglob('*references_verified.json'))
source_records+=['work/maps_audit/final_course_primary_source_checks.json']
for rel in dict.fromkeys(source_records):
    file=OUT/rel
    if file.exists():
        text+='\n### '+rel+'\n\n```json\n'+meta(file.read_text())+'```\n'
text+='''
## Hourly checkpoints and retained history

The checkpoint schedule begins at 23:47 UTC on 16 November 2026. Checkpoint 01 was saved at the first hourly boundary, 00:47 UTC on 17 November. Later checkpoints use new consecutive numbers and are never overwritten. Every checkpoint is a complete ZIP of the deliverables and work records written by that boundary; supplied source archives and their extracted copies are excluded. The final package retains the checkpoint files or an exact older version of every superseded passage, with a path-and-hash retention manifest. The source-extraction duplicate removed from the authored work directory is listed as supplied material, not an omitted proof.

The three-hour progress check falls at 02:47 UTC on 17 November, with hourly checks thereafter. Writing or checking the three papers moves the principal task; optional extensions or polishing after a paper is finished do not.
'''
for rel in ['records/progress_checks.json','records/checkpoint_retention.json']:
    file=OUT/rel
    if file.exists():text+='\n```json\n'+file.read_text()+'```\n'
report_path.write_text(str(text))
print('Report written:',len(text),'characters; complete=',complete)
