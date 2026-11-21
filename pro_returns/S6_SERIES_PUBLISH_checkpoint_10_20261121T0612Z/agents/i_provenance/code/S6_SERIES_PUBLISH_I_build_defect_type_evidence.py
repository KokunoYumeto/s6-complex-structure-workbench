#!/usr/bin/env python3
"""Read-only closure evidence inventory. It does not certify a rendered candidate."""
import csv
import hashlib
import io
import json
import pathlib
import re
import sys
from collections import Counter
from datetime import datetime, timezone

import fitz

BASE = pathlib.Path('/workspace/scratch/653608133b22')
OUT = BASE / 'work/agents/i_provenance'
PREFIX = 'S6_SERIES_PUBLISH_I_defect_type_closure'
csv.field_size_limit(sys.maxsize)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def evidence(path, scope):
    p = BASE / path
    assert p.is_file(), path
    return {'path': str(p), 'sha256': sha(p.read_bytes()), 'scope': scope}

def write_json(name, obj):
    p = OUT / name
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
    return p

register_path = BASE / 'work/S6_DEFECT_REGISTER.csv'
log_path = BASE / 'work/S6_SERIES_PUBLISH_defects_I.tsv'
source_path = BASE / 'work/S6_SERIES_PUBLISH_I.tex'
register_bytes, log_bytes, source_bytes = (p.read_bytes() for p in (register_path, log_path, source_path))
register = list(csv.DictReader(io.StringIO(register_bytes.decode())))
rows = list(csv.DictReader(io.StringIO(log_bytes.decode()), delimiter='\t'))
source = source_bytes.decode()
assert [r['type_id'] for r in register] == [f'D{i:02}' for i in range(1, 26)]
assert len({r['change_id'] for r in rows}) == len(rows)
by_id = {r['change_id']: r for r in rows}
for row in rows:
    assert row['review_status'].startswith('applied'), row['change_id']
    assert all(c in {r['type_id'] for r in register} for c in row['type'].split('/'))

snapshot_log = OUT / (PREFIX + '_ledger_snapshot.tsv')
snapshot_reg = OUT / (PREFIX + '_register_snapshot.csv')
snapshot_log.write_bytes(log_bytes)
snapshot_reg.write_bytes(register_bytes)

readers = [
    'work/records/S6_SERIES_PUBLISH_I_final_candidate12_reading_root.json',
    'work/agents/i_analytic/S6_SERIES_PUBLISH_I_final_candidate12_reading_analytic.json',
    'work/agents/i_topology/S6_SERIES_PUBLISH_I_final_candidate12_reading_topology.json',
    'work/agents/i_provenance/S6_SERIES_PUBLISH_I_final_candidate12_reading_provenance.json',
]
coverage_path = 'work/records/S6_SERIES_PUBLISH_I_candidate12_complete_coverage_snapshot.json'
coverage = json.loads((BASE / coverage_path).read_text())
assert coverage['covered_pages'] == coverage['page_count'] == 344
assert coverage['all_pages_read'] and not coverage['certified'] and not coverage['missing_pages']
actual_records = []
for path in readers:
    data = json.loads((BASE / path).read_text())
    assert data['pdf_sha256'] == coverage['pdf_sha256']
    for page in data['pages']:
        actual_records.append((page['page'], path, page))
assert len(actual_records) == 335
assert len({p for p, _, _ in actual_records}) == 335
inherited = json.loads((BASE / readers[0]).read_text())['inherited_pages']
assert sorted(inherited) == [1, 6, 7, 8, 9, 10, 11, 12, 13]

# A bounded textual supplement to the complete actual-page reading, not a new check.
pdf12_path = BASE / 'work/build/I_candidate12/S6_SERIES_PUBLISH_I.pdf'
assert sha(pdf12_path.read_bytes()) == coverage['pdf_sha256']
pattern = re.compile(r'\b(?:agents?|workers?|Codex|ChatGPT|GPT[-\u2010\u2011\u2013\u2212 ]?\d(?:\.\d)?|Claude|OpenAI|Anthropic|Fable|Opus)\b', re.I)
name_hits = []
with fitz.open(pdf12_path) as pdf:
    for n, page in enumerate(pdf, 1):
        text = page.get_text()
        for m in pattern.finditer(text):
            context = text[max(0, m.start()-90):m.end()+140].replace('\n', ' ')
            if n == 16:
                disposition = 'Methodology model credit, or AC author citation in the adjacent known/new table; each is explicitly attributed.'
            else:
                assert m.group().lower() == 'claude', (n, m.group(), context)
                disposition = 'Name of the cited AC2026 author, linked by the citation or the bibliography entry; no workflow agent is invoked in the argument.'
            name_hits.append({'page': n, 'token': m.group(), 'context': context, 'disposition': disposition})
scan = {
    'paper': 'I', 'created_utc': datetime.now(timezone.utc).isoformat(),
    'source_sha256': sha(source_bytes), 'candidate12_pdf_sha256': coverage['pdf_sha256'],
    'method': 'Supplementary full-PDF text occurrence inventory, inspected in conjunction with the hashed complete actual-page reading. No page-image or mathematical-check credit is supplied by this scan.',
    'D07_pattern': pattern.pattern, 'D07_hits': name_hits,
    'D07_workflow_agent_or_worker_hits_in_mathematical_body': 0,
    'D07_disposition': 'All model/platform names occur in the methodology on page16. Other Claude occurrences identify the AC2026 author in explicit citations or the bibliography. No agents/workers are named as mathematical proof inputs.',
    'manual_equation_tag_commands': len(re.findall(r'\\tag\*?\{', source)),
    'automatic_equation_numbering': r'\numberwithin{equation}{section}' in source,
    'bibliography_entries': len(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{', source)),
    'statement_record_prints_only_tag': r'\newcommand{\StatementRecord}[4]{{\upshape\footnotesize[tag~\texttt{#3}]}\enspace\ignorespaces}' in source,
    'new_math_events': 0,
}
assert scan['manual_equation_tag_commands'] == 0
assert scan['automatic_equation_numbering'] and scan['statement_record_prints_only_tag']
scan_path = write_json(PREFIX + '_source_scan.json', scan)

# All IDs are included below; these are representative applied changes, not counts of distinct mathematical errors.
representatives = {
    'D01': ['I-00069', 'I-01272', 'I-01943'],
    'D02': ['I-00413', 'I-01933', 'I-01934'],
    'D03': ['I-00442', 'I-01949'],
    'D04': ['I-00664', 'I-01712'],
    'D05': ['I-00031', 'I-00463'],
    'D06': ['I-00025', 'I-01945', 'I-01946', 'I-01952', 'I-01953'],
    'D07': [],
    'D08': ['I-00253', 'I-01941'],
    'D09': ['I-00088', 'I-01732'],
    'D10': ['I-00009', 'I-00010'],
    'D11': ['I-00400', 'I-01262'],
    'D12': ['I-00042', 'I-01932'],
    'D13': ['I-00046', 'I-00067', 'I-00246'],
    'D14': ['I-00043', 'I-01680', 'I-01686', 'I-01688', 'I-01783'],
    'D15': ['I-00021', 'I-01045'],
    'D16': ['I-00070', 'I-01898'],
    'D17': ['I-00418', 'I-00654', 'I-00655', 'I-01939'],
    'D18': ['I-00033', 'I-00035', 'I-01940'],
    'D19': ['I-01342', 'I-01672'],
    'D20': ['I-00128', 'I-00646', 'I-01901'],
    'D21': ['I-00091'],
    'D22': ['I-00407', 'I-00534', 'I-01253'],
    'D23': ['I-01944', 'I-01947', 'I-01948', 'I-01950', 'I-01951'],
    'D24': ['I-00862', 'I-00865'],
    'D25': ['I-00029', 'I-00056', 'I-00059', 'I-00660', 'I-00866', 'I-01689', 'I-01936'],
}
descriptions = {
    'D01': 'Draft/history narration was removed from mathematical titles and proofs. The expressly required credited re-derivation/chronology passages and the qualified model history remain, with their exact source scope.',
    'D02': 'Defensive clauses were replaced by the precise maps, positive hypotheses or proved conclusions. Full affected proof comparisons preserve every mathematical clause.',
    'D03': 'Workflow-targeted refutations were removed or converted to self-contained positive mathematical examples. The last candidate12 example has its exact two points and line/period comparison preserved by I-01949.',
    'D04': 'Internal run/equation keys and detached compendium pointers were replaced by local numbered statements/equations or exact primary citations; the collar and branch maps remain explicit.',
    'D05': 'References to prompts and requested steps were replaced by mathematical family/coordinate hypotheses; numbered definitions carry the actual input.',
    'D06': 'Introductory letters and external/deferred numbering were resolved through retained stable labels. Candidate12 duplicate alias references and two aliases inheriting subsection numbers have exact applied repairs.',
    'D07': 'Zero edit rows bear this code. The complete candidate12 page-review chain and the separate occurrence inventory positively inspect model, author and worker names: model/platform names are confined to methodology; other Claude occurrences are the explicitly cited AC2026 author.',
    'D08': 'Workflow vocabulary was replaced by mathematical method/input/result descriptions. Ordinary mathematical uses such as a correction term or original equation were retained with context.',
    'D09': 'Body filenames and diagnostic-report narration were moved to records. The end table gives78 authenticated source links at the exact historical pin, with explicit receiving statements; new unpublished verification files are not attributed to that pin.',
    'D10': 'The common StatementRecord macro prints only the permanent small tag. Machine uses/used-by/check metadata and return-navigation text are hidden or removed; source labels and hypertargets are preserved.',
    'D11': 'Repeated scope disclaimers were removed after their hypotheses/conclusions were retained once in the actual statement. Genuine unresolved arithmetic questions are in the final part.',
    'D12': 'Repeated proofs were consolidated with exact alias preservation and complete old/new comparisons, including common marking/normalization, family construction, tangent calculation and automorphism argument.',
    'D13': 'Standalone coordinate, covariance, tangent-sheaf and other inputs were made numbered definitions/remarks/lemmas or moved into their owning proofs; no alias or unique formula was discarded.',
    'D14': 'Dependencies were reordered: common conventions first; full proper coherent-family construction before uses; classification proof beside its theorem; common residue/kernel and normal-crossing contraction before receiving results. Required credited appendices remain.',
    'D15': 'The abstract, seven main statements/outlines, known/new rows and methodology were revised as mathematical front matter. Model/effort/date and count qualifications are bound to the supplied evidence, with no invented historical attribution.',
    'D16': 'Main-chain statements and subsidiary inputs received short mathematical titles. Long or process-oriented titles were shortened without changing theorem scope.',
    'D17': 'Known textbook/analytic reproofs were replaced by opened exact sources plus the receiving matrix, characteristic-zero, parameter-pair, measure and convergence maps. The specifically required credited re-derived appendices were retained.',
    'D18': 'Primary statements and page/version locators were opened and scoped in receipts; bibliography aliases and editions were reconciled, sorted and pruned. Current source has117 entries; BM preprint/publication correspondence and Neretin/Gross/Drinfeld editions are explicit.',
    'D19': '331 logged rows convert displays and references to automatic section equation numbering while retaining every formula and anchor. Current source has zero manual tag commands and contains numberwithin equation/section.',
    'D20': 'Parallel normalizations were joined by explicit maps: differential/lattice homothety, coarse/root invariant pushforward, frame transport and exact subtraction sign. The chosen notation refers back to the common definitions.',
    'D21': 'The numerical-agreement proposition was replaced by the exact small-order torsion count from squarefree division polynomials and their degrees. Agreement/precision observations were relegated to records.',
    'D22': 'Previously unexplained choices now carry their maps/calculations: toric fixed and character-extension loci, the2pi-i chain isomorphism, and the twelve scalar fractions giving the exact integral period.',
    'D23': 'Font, spacing, punctuation, table and page-flow defects have logged source repairs. Candidate12 still showed orphan headings, diagram-edge overlap, a detached proof-stage heading and a QED-only page; the exact source repairs are applied and await candidate13 visual verification.',
    'D24': 'The introduction, supplying/receiving dependency table, proof outlines and further-results list were aligned with the current body and current seven theorem scopes. The common series paragraph no longer uses an incorrect paper ordinal.',
    'D25': 'The ledger records17 tagged edit associations, not17 distinct false theorems. Exact intermediate errors and completion steps are accompanied by scoped proof comparisons: boundary lattice point, logarithm transport, radial ratio, selected cusp diagonal, component resolution and Gross auxiliary-field hypotheses. The one refuted logarithm clause retains its original ID and a refined replacement. No unresolved substantive defect is reported in the completed candidate12 review.',
}

R = 'work/records/'
P = 'work/agents/i_provenance/'
A = 'work/agents/i_analytic/'
T = 'work/agents/i_topology/'
specific = {
    'D01': [(P+'S6_SERIES_PUBLISH_I_residual_prebuild_comparison.json','Exact old/current/proposed prose and applied scope.'),(P+'S6_SERIES_PUBLISH_I_final_source_count_binding.json','Qualified model/date/effort and methodology binding.')],
    'D02': [(P+'S6_SERIES_PUBLISH_I_editorial_mapsI_applied_comparison.json','Positive mapsI prose with full affected proof comparison.'),(A+'S6_SERIES_PUBLISH_I_final_residual_comparison.json','Complete analytic residual proof comparisons.')],
    'D03': [(A+'S6_SERIES_PUBLISH_I_final_candidate12_reading_analytic_guards.json','Exact positive two-point example guard.'),(A+'S6_SERIES_PUBLISH_I_final_candidate12_visual_archive.json','Full statement/proof archive; proof unchanged.')],
    'D04': [(P+'literature/S6_SERIES_PUBLISH_I_AC_DGKX_canonical_root_locator_receipt.json','Actual primary locators for canonical/root and collar uses.'),(R+'S6_SERIES_PUBLISH_I_bare_equation_reference_audit.json','Internal equation reference resolution audit.')],
    'D05': [(P+'S6_SERIES_PUBLISH_I_C12_check.md','Exact finite-period proof and branch scope.'),(R+'S6_SERIES_PUBLISH_I_hodge_editorial_comparison.json','Full family/Hodge scope replacement.')],
    'D06': [(R+'S6_SERIES_PUBLISH_I_candidate12_complete_coverage_snapshot.json','Observed duplicate/local reference findings in complete page coverage.'),(R+'S6_SERIES_PUBLISH_I_candidate12_integration_comparison.json','Proper/coherent/classification proof ownership and labels.')],
    'D07': [(str(scan_path.relative_to(BASE)),'All model/agent/worker name occurrences and contextual dispositions; complete-page reading supplies visual evidence.')],
    'D08': [(P+'S6_SERIES_PUBLISH_I_boundary_program_comparison.json','Mathematical method/input/result remains after bookkeeping removal.'),(A+'S6_SERIES_PUBLISH_I_editorial_CD_comparison.json','Complete arithmetic/body old-new comparisons.')],
    'D09': [(R+'S6_SERIES_PUBLISH_I_program_table_receipt.json','78 source links and exact pinned-path authentication scope.'),(P+'S6_SERIES_PUBLISH_I_boundary_program_comparison.json','Operative computation versus diagnostic disposition.')],
    'D10': [(str(scan_path.relative_to(BASE)),'Current common macro prints only the permanent tag.'),(R+'S6_SERIES_PUBLISH_I_defect_taxonomy_receipt.json','Classification of apparatus edits; no mathematical credit.')],
    'D11': [(P+'S6_SERIES_PUBLISH_I_editorial_mapsI_applied_comparison.json','Scopes retained in statements after repeated prose removal.'),(T+'editorial/S6_SERIES_PUBLISH_I_boundary_batch7_comparison.md','Full local boundary proof scopes retained.')],
    'D12': [(R+'S6_SERIES_PUBLISH_I_canonical_ring_comparison.json','Unified canonical construction and ring maps.'),(P+'S6_SERIES_PUBLISH_I_candidate11_tail_comparison.json','Full automorphism proof comparison and alias preservation.'),(R+'S6_SERIES_PUBLISH_I_candidate12_integration_comparison.json','Unified coherent construction and supplying scalar/residue proof.')],
    'D13': [(P+'S6_SERIES_PUBLISH_I_common_family_applied_comparison.json','Numbered common definitions and remarks with exact hypotheses.'),(P+'S6_SERIES_PUBLISH_I_editorial_mapsI_applied_comparison.json','Numbered circle/real-form inputs and preserved anchors.')],
    'D14': [(R+'S6_SERIES_PUBLISH_I_candidate12_integration_comparison.json','Full construction/classification relocation comparison.'),(A+'S6_SERIES_PUBLISH_I_residue_order_comparison.md','Common residue lemma before scalar/direct-image uses.'),(T+'editorial/S6_SERIES_PUBLISH_I_candidate11_cusp_comparison.md','Early local contraction with exact reparametrization.')],
    'D15': [(R+'S6_SERIES_PUBLISH_I_front_status_receipt.json','Exact seven front-matter literature/status rows.'),(P+'S6_SERIES_PUBLISH_I_final_source_count_binding.json','Source/count/model qualification receipt.'),(P+'S6_SERIES_PUBLISH_I_three_way_claim_table_final.json','42 source/report/deposit dispositions; final rendered gate remains pending.')],
    'D16': [(P+'S6_SERIES_PUBLISH_I_editorial_famF_applied_comparison.json','Mathematical period-domain and monodromy titles.'),(T+'editorial/S6_SERIES_PUBLISH_I_candidate11_prose_comparison.md','Full proof preservation while shortening titles.')],
    'D17': [(P+'literature/S6_SERIES_PUBLISH_I_AC_Engel_Conrad_locator_receipt.json','Opened group-presentation source and exact matrix identification.'),(P+'literature/S6_SERIES_PUBLISH_I_Neretin2024_beta_locator_receipt.json','Actual published beta pages38–39 and full convergence conditions.'),(P+'S6_SERIES_PUBLISH_I_candidate11_beta_comparison.json','Full old/proposed/applied beta proof comparison.')],
    'D18': [(P+'literature/S6_SERIES_PUBLISH_I_final_primary_locator_receipt.json','Bounded exact primary-source/version/page receipts.'),(T+'literature/S6_SERIES_PUBLISH_I_candidate11_primary_locator_closure.json','Nine-source actual-page closure and receiving scopes.'),(R+'S6_SERIES_PUBLISH_I_bibliography_disposition.json','Pruned uncited entries and retained editions.'),(P+'literature/S6_SERIES_PUBLISH_I_candidate11_bibliography_metadata_receipt.json','Edition metadata and BM correspondence.')],
    'D19': [(R+'S6_SERIES_PUBLISH_I_equation_map.json','Complete original/current equation-anchor map.'),(R+'S6_SERIES_PUBLISH_I_bare_equation_reference_audit.json','Literal equation reference audit.'),(str(scan_path.relative_to(BASE)),'Current zero-manual-tag count and section numbering declaration.')],
    'D20': [(R+'S6_SERIES_PUBLISH_I_coarse_root_comparison.json','Exact invariant-pushforward/normalization maps.'),(A+'S6_SERIES_PUBLISH_I_analytic_setup_comparison.json','Differential, discriminant and period-lattice transport.'),(T+'editorial/S6_SERIES_PUBLISH_I_candidate11_prose_comparison.md','Receiving coordinate z_q=z_r+F and trace sign.')],
    'D21': [(A+'S6_SERIES_PUBLISH_I_editorial_AB_comparison.json','Full numerical-proposition to exact degree-count corollary comparison.')],
    'D22': [(P+'S6_SERIES_PUBLISH_I_editorial_mapsI_applied_comparison.json','Same-chart toric action and character-limit comparison.'),(R+'S6_SERIES_PUBLISH_I_twists_editorial_comparison.json','Exact chain normalization maps.'),(T+'editorial/S6_SERIES_PUBLISH_I_residual_batch9_comparison.md','Twelve-term scalar sum and resulting period.')],
    'D23': [(P+'S6_SERIES_PUBLISH_I_candidate12_proof_placement_guards.json','Exact proof-stage reserve and qedhere guards.'),(T+'S6_SERIES_PUBLISH_I_candidate12_visual_guards.json','Actual-page orphan-heading findings.'),(R+'S6_SERIES_PUBLISH_I_program_table_layout_receipt.json','Program-table layout repair, followed by actual candidate12 pages330–332.')],
    'D24': [(R+'S6_SERIES_PUBLISH_I_front_status_receipt.json','Current main theorem mechanisms/status and table.'),(R+'S6_SERIES_PUBLISH_I_global_DE_comparison.json','Exact global D/E supplying-body comparison.'),(A+'S6_SERIES_PUBLISH_I_global_ABC_comparison.json','Exact main A–C body/outline comparison.'),(T+'S6_SERIES_PUBLISH_I_final_FG_comparison.json','Exact main F/G body/outline comparison.')],
    'D25': [(P+'S6_SERIES_PUBLISH_I_C12_check.md','Independent branch derivation and lattice-point correction.'),(A+'S6_SERIES_PUBLISH_I_nine_comparison.md','Exact logarithm-clause refutation and radial-ratio repair.'),(P+'S6_SERIES_PUBLISH_I_push_A12_selected_diagonal_ERROR_EVENT.json','Selected diagonal error and exact correcting charts.'),(T+'S6_SERIES_PUBLISH_I_P210_resolution_comparison.md','Receiving marked node map and both resolution charts.'),(T+'editorial/S6_SERIES_PUBLISH_I_P26_component_resolution_comparison.json','Resolve central component before Stein factorization.'),(A+'S6_SERIES_PUBLISH_I_Gross_auxiliary_comparison.md','Nonvanishing auxiliary-field hypotheses and all exact source maps.')],
}

heading_pages = [21,25,41,63,65,75,164,189,190,234,248,261,278,280,292,308]
pending = {
    'D03': [{'candidate12_pages':[138], 'observation':'Proposition19.6 began by refuting an unnamed assertion.', 'applied_edit_ids':['I-01949'], 'repair':'Retain the exact two central points and prove their difference lies outside the specified line plus period group; remove only refutation framing.', 'state':'Source repair applied; candidate13 page verification pending.'}],
    'D06': [
        {'candidate12_pages':[14], 'observation':'OutlineE6 repeated B.2 and outlineF1 repeated18.2 through aliases.', 'applied_edit_ids':['I-01945','I-01946'], 'repair':'Keep one printed supplying reference while preserving every original alias.', 'state':'Source repair applied; candidate13 reference verification pending.'},
        {'candidate12_pages':[44,51], 'observation':'Two retained proof markers inherited the surrounding subsection number.', 'applied_edit_ids':['I-01952','I-01953'], 'repair':'Move coherent-descent and classification proof aliases into their owning proposition/theorem headers; retain all labels/tags.', 'state':'Source repair applied; candidate13 labels and links must resolve to7.5 and7.8.'},
    ],
    'D23': [
        {'candidate12_pages':heading_pages, 'observation':'Section/subsection headings were separated from the following protected statements.', 'applied_edit_ids':['I-01944'], 'repair':'Shared Needspace reserves of14 baselines before sections and9 before subsections.', 'state':'Source repair applied; all reflowed candidate13 pages require actual reading.'},
        {'candidate12_pages':[17], 'observation':'Dependency arrow G→A crossed the D box; the adjacent B→G route was also adjusted.', 'applied_edit_ids':['I-01947','I-01948'], 'repair':'Route arrows outside the theorem boxes without changing endpoints.', 'state':'Source repair applied; candidate13 figure verification pending.'},
        {'candidate12_pages':[312,313,314], 'observation':'Proof-stage5 heading separated from text; final QED alone on otherwise blank314.', 'applied_edit_ids':['I-01950','I-01951'], 'repair':'Reserve6 baselines before stage5; place qedhere with the final sentence.', 'state':'Source repair applied; candidate13 placement and absence of QED-only page pending.'},
    ],
}
for records in pending.values():
    for item in records:
        for edit_id in item['applied_edit_ids']:
            assert source.count(by_id[edit_id]['new_text']) == 1, edit_id

common_evidence = [
    evidence(str(snapshot_log.relative_to(BASE)), 'Immutable full current defect ledger snapshot; every old/new text and applied edit identifier retained.'),
    evidence(str(snapshot_reg.relative_to(BASE)), 'Immutable25-type register including the D25 extension.'),
    evidence(coverage_path, 'Candidate12 complete344-page coverage;335 new page-image readings and9 earlier readings carried only by complete rendered-image equality. This candidate is explicitly uncertified.'),
] + [evidence(p, 'Complete assigned candidate12 actual-image reading record; exact observed findings remain historical evidence.') for p in readers]

types = []
for reg in register:
    code = reg['type_id']
    associated = [r for r in rows if code in r['type'].split('/')]
    reps = []
    for edit_id in representatives[code]:
        r = by_id[edit_id]
        assert code in r['type'].split('/'), (code, edit_id)
        reps.append({k:r[k] for k in ['change_id','type','statement_id','old_location','old_page','new_location','new_page','reason','old_text','new_text','review_status']})
    types.append({
        'type_id':code, 'class':reg['class'], 'defect':reg['defect'], 'required_fix':reg['required_fix'],
        'status':'pending_final_verification', 'edit_ids':[r['change_id'] for r in associated],
        'edit_associations':len(associated), 'single_code_edits':sum(r['type']==code for r in associated),
        'composite_code_edits':sum(r['type']!=code for r in associated),
        'distinct_nonempty_statement_fields':len({r['statement_id'] for r in associated if r['statement_id']}),
        'inspected_scope':descriptions[code], 'representative_applied_changes':reps,
        'evidence':common_evidence + [evidence(path, scope) for path, scope in specific[code]],
        'candidate12_findings':pending.get(code, []),
        'remaining':([item['state']+' '+item['repair'] for item in pending.get(code, [])] + ['Candidate13 certified complete rendered-page coverage and final exact source/PDF/ledger/register binding.']),
        'unresolved_substantive_defects':[],
    })

manifest_path = BASE / 'work/render/I_candidate13/manifest.json'
manifest = json.loads(manifest_path.read_text())
pdf13_path = BASE / 'work/build/I_candidate13/S6_SERIES_PUBLISH_I.pdf'
target_pdf_sha = sha(pdf13_path.read_bytes())
assert sha(source_bytes) == '26a6f5f8b1e911de363bed7346e970bc8fb77b21cf04fe9a2ce4d1f90d95b49e'
assert target_pdf_sha == '519355e39d7d821a10d728d5c8dbf69a50826ee215ab98619803d44e1cae2a2b'
obj = {
    'schema':1, 'paper':'I', 'created_utc':datetime.now(timezone.utc).isoformat(),
    'source':str(source_path), 'source_sha256':sha(source_bytes),
    'pdf':str(pdf13_path), 'pdf_sha256':target_pdf_sha,
    'candidate_scope':{'target':'I_candidate13','target_reading_status':'Pending final complete actual-page reading/certification at inventory creation.','render_manifest':str(manifest_path),'render_manifest_sha256':sha(manifest_path.read_bytes()),'prior_reading_candidate':'I_candidate12','prior_pdf_sha256':coverage['pdf_sha256'],'prior_source_sha256':coverage['source_sha256'],'prior_complete_coverage':344,'prior_new_page_image_readings':335,'prior_equal_image_inherited_readings':9,'prior_certified':False},
    'defect_log':{'path':str(log_path),'sha256':sha(log_bytes),'rows':len(rows),'snapshot':str(snapshot_log)},
    'register':{'path':str(register_path),'sha256':sha(register_bytes),'rows':len(register),'snapshot':str(snapshot_reg)},
    'final_certified':False,
    'count_semantics':'Each edit ID occurs once in the full ledger. A composite Dxx/Dyy row contributes once to each listed type, so per-type counts are edit-type associations and must not be added as distinct defects. These are recorded repair operations, not mathematical checks, unique errors, or claims that each residual occurrence was enumerated. D07 has zero coded edits and is supported by positive inspected-scope evidence. Historical classifications are preserved, without a new taxonomy mutation.',
    'unique_edit_rows':len(rows), 'edit_type_associations':sum(t['edit_associations'] for t in types),
    'ledger_review_status_counts':dict(Counter(r['review_status'] for r in rows)),
    'unresolved_substantive_defects':[],
    'substantive_scope':'No unresolved substantive defect is reported by the completed candidate12 actual-page reviews or the linked applied proof-comparison receipts. This inventory adds no mathematical certification. All25 types remain pending final certification of candidate13.',
    'mathematical_events_added':0, 'shared_files_modified':False, 'types':types,
}
dest = write_json(PREFIX+'_evidence.json',obj)

md = ['# Paper I: D01–D25 closure evidence draft','',
      '**Final closure is pending.** The current source repairs are applied; candidate13 must still receive certified complete rendered-page review. This artifact does not add check events.','',
      f"Source SHA256: `{obj['source_sha256']}`  ",f"Candidate13 PDF SHA256: `{target_pdf_sha}`  ",f"Defect ledger: {len(rows)} unique applied rows; {obj['edit_type_associations']} edit-type associations.  ",f"Register:25 types, SHA256 `{sha(register_bytes)}`.",'',obj['count_semantics'],'',
      'Candidate12 coverage comprises335 new complete page-image readings and9 earlier complete readings inherited only through identical rendered images, covering all344 pages. Candidate12 remains uncertified because its observed residuals required the current repairs.','',
      '| Type | Applied edit associations | Representative IDs | Inspected repair scope | Remaining gate |','|---|---:|---|---|---|']
for t in types:
    md.append('| '+t['type_id']+' | '+str(t['edit_associations'])+' | '+', '.join(r['change_id'] for r in t['representative_applied_changes'])+' | '+t['inspected_scope'].replace('|','\\|')+' | '+('Exact residual repairs plus candidate13 verification' if t['candidate12_findings'] else 'Candidate13 final verification and binding')+' |')
md += ['', '## Exact observed residuals and their applied repairs','']
for code, items in pending.items():
    for item in items:
        md += [f"- **{code}; candidate12 pages {', '.join(map(str,item['candidate12_pages']))}:** {item['observation']} Applied `{', '.join(item['applied_edit_ids'])}`: {item['repair']} {item['state']}"]
md += ['', '## Evidence by type','']
for t in types:
    md += ['### '+t['type_id']+' — '+t['defect'],'',t['inspected_scope'],'',f"All {len(t['edit_ids'])} associated edit IDs: "+(', '.join(t['edit_ids']) if t['edit_ids'] else 'none; positive scan and complete-page evidence below.')+'.','']
    for ev in t['evidence'][len(common_evidence):]:
        md.append(f"- `{ev['path']}` — {ev['scope']} SHA256 `{ev['sha256']}`.")
    md += ['', 'Remaining: '+' '.join(t['remaining']),'']
md += ['## Shared full-ledger and reading evidence','']
for ev in common_evidence:
    md.append(f"- `{ev['path']}` — {ev['scope']} SHA256 `{ev['sha256']}`.")
md += ['', 'No unresolved substantive defect is asserted by this inventory. The original logarithm-clause refutation and all corrected intermediate-proof claims remain preserved in the ledger and their scoped comparison records; the final page gate remains open.','']
(OUT/(PREFIX+'_evidence.md')).write_text('\n'.join(md))
with (OUT/(PREFIX+'_evidence.tsv')).open('w',newline='') as f:
    writer=csv.DictWriter(f,delimiter='\t',fieldnames=['type_id','status','edit_associations','single_code_edits','composite_code_edits','edit_ids','inspected_scope','evidence_paths','remaining'])
    writer.writeheader()
    for t in types:
        writer.writerow({k: ('; '.join(t['edit_ids']) if k=='edit_ids' else '; '.join(e['path'] for e in t['evidence']) if k=='evidence_paths' else '; '.join(t['remaining']) if k=='remaining' else t[k]) for k in writer.fieldnames})
print(json.dumps({'output':str(dest),'sha256':sha(dest.read_bytes()),'types':len(types),'unique_edit_rows':len(rows),'edit_type_associations':obj['edit_type_associations'],'final_certified':False,'missing_evidence':[]},indent=2))
