#!/usr/bin/env python3
"""Consolidate completed MAPS D readings without promoting scoped or archival evidence.

This is an evidence assembler, not a mathematical test. It preserves the preceding
checkpoint and checks every executable/output and extracted-proof hash it cites.
"""
from pathlib import Path
from collections import Counter, defaultdict
import copy
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / 'deliverables/work/invariants_arithmetic'
SRC = ROOT / 'sources/returns/S6_04_MAPS_MANIFOLDS'
META = dict(checker='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17 UTC')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load(path):
    return json.loads(path.read_text())

def save(name, value):
    (WORK / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

rows = load(WORK / 'maps_D_independent_audit.json')
previous = WORK / 'maps_D_before_final_consolidation.json'
if not previous.exists():
    previous.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
credits = {x['source_id']: x for x in load(WORK / 'maps_D_credit_comparison.json')}
refs = {x['citation_key']: x for x in load(WORK / 'maps_D_references_verified.json')}
base_refs = {x['citation_key']: x for x in load(WORK / 'source_credit_map.json')}
closure = load(WORK / 'maps_modular_collision_closure.json')

run_files = [
    WORK / 'maps_D_program_runs.json',
    WORK / 'maps_D_explorer_cache_runs.json',
    ROOT / 'deliverables/code/invariants_arithmetic/maps_D_review/modular_collision_realizations_run.json',
]
runs = []
for path in run_files:
    data = load(path)
    for run in data if isinstance(data, list) else [data]:
        run = copy.deepcopy(run)
        run['execution_ledger'] = str(path.relative_to(ROOT / 'deliverables'))
        run['archive_relative_command'] = run['command'].replace('deliverables/', '')
        run['archive_relative_program'] = run['program'].removeprefix('deliverables/')
        run['archive_relative_output'] = run['output'].removeprefix('deliverables/')
        run['run_id'] = 'mapsD-run-' + hashlib.sha256(run['command'].encode()).hexdigest()[:12]
        for field in ['program', 'output']:
            actual = digest(ROOT / run[field])
            assert actual == run[field + '_sha256'], (field, run[field], actual, run[field + '_sha256'])
        run['artifact_hashes_rechecked'] = True
        run['associated_source_ids'] = []
        stem = Path(run['program']).stem
        if stem in ['root_remaining_smooth_profiles', 'root_all_weighted_coordinate_audit']:
            run['retained_comparison_note'] = 'No corresponding retained stdout file existed. Fresh execution passed; false in the original runner comparison means absent baseline, not a mathematical mismatch.'
        elif stem == 'manifolds_weighted_profiles':
            run['retained_comparison_note'] = 'Fresh output adds the diagnostic actual rank-one factors:436, non-narrow vertical contents:[1]. The remaining retained output agrees; all assertions passed.'
        elif stem == 'independent_cover_markings_attempt1':
            run['status'] = 'superseded_failed_auxiliary_assertion'
            run['failure_diagnosis'] = 'An overstrong demand for a literal second unit column failed. The correct integral image uses column0 minus d*column4; the succeeding independent_cover_markings program proves this. This is not a failure of a source theorem.'
        elif stem == 'root_OS45_bridge':
            run['mathematical_scope'] = 'Certifies the actual order-two boundary class and an odd Mayer-Vietoris bridge class. Does not supply its embedded representative, reference framing, or critical-specialization linking; refined P remains0 or4.'
        runs.append(run)

by_stem = defaultdict(list)
for run in runs:
    by_stem[Path(run['program']).stem].append(run)

programs = {
 1:['manifolds_os_configurations','certify_modular_collision_realizations'],
 2:['check_maps_explorer_cache','manifolds_explorer_21'],
 3:['check_maps_explorer_cache','manifolds_semistable'],
 5:['manifolds_unbounded_logs'],6:['manifolds_iii_star'],7:['manifolds_wang'],
 9:['manifolds_liu_rollenske'],10:['manifolds_yang'],11:['manifolds_type_c_ii'],
 12:['manifolds_rankone_families'],13:['manifolds_semistable'],15:['manifolds_i2_cusp'],
 16:['manifolds_star_smooth'],17:['manifolds_star_additive'],18:['manifolds_star_i3_cusp'],
 19:['manifolds_degree_one'],20:['manifolds_original_additive'],21:['manifolds_mixed_additive'],
 22:['manifolds_sphere_initial'],23:['manifolds_sphere_gluing'],24:['manifolds_sphere_gluing'],
 25:['manifolds_semistable_catalogue'],26:['manifolds_nonstar_catalogue','manifolds_sphere_normal_lattices'],
 27:['manifolds_i1star_obstruction'],28:['manifolds_i1star_obstruction','manifolds_nonstar_catalogue'],
 29:['manifolds_unrestricted_finite_logs'],30:['manifolds_all_finite_logs'],
 31:['manifolds_original_zero_degree'],32:['manifolds_original_chern'],33:['manifolds_original_multiplicative'],
 34:['manifolds_weighted_engel'],
 35:['fourfolds_D2_c2_AH','manifolds_tate_markings','root_remaining_smooth_profiles'],
 36:['manifolds_odd_prime_AH','manifolds_tate_markings','root_remaining_smooth_profiles'],
 37:['manifolds_weighted_profiles'],38:['manifolds_mixed_prime_AH','manifolds_tate_markings'],
 39:['fourfolds_D2_c3_AH','manifolds_tate_markings'],40:['manifolds_odd_weighted_profiles'],
 41:['manifolds_all_weighted_profiles','fourfolds_bar_koszul','root_all_weighted_coordinate_audit'],
 42:['manifolds_three_mixed_AH','manifolds_tate_markings'],43:['manifolds_general_cusp'],
 44:['fourfolds_D2_2power_AH','fourfolds_D2_frame_certificate','manifolds_even_critical_cycles','maps_D2_frame_checks','manifolds_tate_markings'],
 45:['fourfolds_D2_remaining_AH','manifolds_extended_critical_cycles','maps_D2_II_frame_checks','manifolds_tate_markings'],
 46:['manifolds_general_initial_audit'],47:['fourfolds_D2_component_ring'],
 48:['maps_weighted_engel_invariants','fourfolds_D48_thomas'],49:['manifolds_star_log_caps'],
 50:['root_vertical_corrections','fourfolds_corrected_Mumford_examples'],
 51:['manifolds_invariant_chern_caps'],52:['manifolds_corrected_initial_audit'],
 53:['maps_weighted_os45','fourfolds_OS45_component_ring','fourfolds_OS45_primitive_cubic',
     'fourfolds_OS45_localization','maps_weighted_os45_mu','root_OS45_bridge'],
}

# Earlier records were opened in full for the D portions; production itself is
# not represented as independent review. Exact JSON pointers retain the scope.
prior = defaultdict(list)
review_files = [
 *['root_audit_checkpoint%02d_progress.json'%n for n in range(3,10)],
 'root_completion_audit10.json','root_completion_audit11.json',
 *['root_d%d_completion_audit.json'%n for n in [36,37,38,39,40,42]],
 'root_D47_completion_audit.json','root_D48_completion_audit.json',
 'root_D49_D50_completion_audits.json','root_D51_D53_completion_audits.json',
]

def matched_ids(key):
    m = re.fullmatch(r'D\.2\.(\d+)(?:--?(?:D\.2\.)?(\d+))?', key)
    if m:
        return ['D.2.%d'%n for n in range(int(m[1]), int(m[2] or m[1])+1)]
    if key in ['D51','D52','D53']:
        return ['D.2.' + key[1:]]
    return []

def prior_entry(path, date, pointer, record, role='source-run root'):
    return dict(reviewer='GPT-6 Astra (OpenAI, ChatGPT Pro mode), '+role,
                effort='Pro mode; no finer effort parameter recorded', date=date,
                source_file=str(path.relative_to(ROOT)), source_sha256=digest(path),
                locator=pointer, scope=record,
                provenance='Within-run independent reading; not an external human or cross-model review.',
                model_identity_source='sources/reviews/WHO_WROTE_WHAT.md, producing-runs paragraph; source work_log.md lines9–12')

for name in review_files:
    path = SRC/'records'/name
    data = load(path)
    date = next((data[k] for k in ['reviewed_utc','audited_utc','updated_utc'] if k in data),
                'Exact timestamp not recorded in this file; producing run15–16 November2026 UTC')
    collected = []
    def walk(obj, pointer=''):
        if not isinstance(obj,dict):
            return
        for key,value in obj.items():
            ids = matched_ids(key)
            ptr = pointer+'/'+key.replace('~','~0').replace('/','~1')
            if ids:
                for sid in ids:
                    collected.append((sid,ptr,value))
            elif isinstance(value,dict):
                walk(value,ptr)
    walk(data)
    if not collected:
        m = re.search(r'root_[dD](\d+)_completion_audit',name)
        assert m, name
        collected=[('D.2.'+m[1],'/',data)]
    for sid,ptr,record in collected:
        d = record.get('reviewed_utc',date) if isinstance(record,dict) else date
        prior[sid].append(prior_entry(path,d,ptr,record))

md_records = [
 ('maps_D44_peer_audit.md',[44],'maps agent','16 November2026 (file header)'),
 ('maps_D45_relative_audit.md',[45],'maps agent','16 November2026 (producing-run context; exact time unrecorded)'),
 ('fourfolds_D48_peer_audit.md',[48],'fourfolds agent','16 November2026 (file header)'),
 ('maps_D48_source_audit.md',[48],'maps/root source audit','16 November2026 (file text)'),
 ('fourfolds_D49_parity_audit.md',[49],'fourfolds agent','15–16 November2026 producing run; exact timestamp unrecorded'),
 ('fourfolds_OS45_mu_peer_audit.md',[53],'fourfolds agent','15–16 November2026 producing run; exact timestamp unrecorded'),
 ('maps_D2_frame_source_audit.md',[44,45,48],'maps agent','15–16 November2026 producing run; exact timestamp unrecorded'),
 ('fourfolds_D50_peer_audit.md',[50],'fourfolds agent','15–16 November2026 producing run; exact timestamp unrecorded'),
]
for name, nums, role, date in md_records:
    path=SRC/'records'/name
    content=path.read_text()
    for n in nums:
        prior['D.2.%d'%n].append(prior_entry(path,date,'entire file, lines1–%d'%len(content.splitlines()),content,role))
worklog=SRC/'records/work_log.md'
for n in [5,6]:
    prior['D.2.%d'%n].append(prior_entry(worklog,'2026-11-15 15:57–16:24 UTC',
        'lines26–35','Root audited the arbitrary-determinant Mayer–Vietoris step and three invariant normal tori; this is the expressly recorded bounded scope.'))

scope_limits = {
 'D.2.49':['Nonprimitive long-circle root powers and other integral star blocks are not covered; complete smooth invariants of the new star-log outputs remain uncomputed.'],
 'D.2.50':['The corrected original-cap marked boundary maps and the smooth invariants of the16 new examples are not inferred from their homology.'],
 'D.2.51':['For h>1 the mixed elliptic–gamma and second fixed-normal torsion columns are not determined. Full local homology is proved for all h, but the full marked kernel is only supplied for h=1.'],
 'D.2.52':['Corrected original multiplicative caps, unresolved h>1 original additive torsion columns, and unspecified whole-fibre meridian changes are excluded from the proved algorithm.'],
 'D.2.53':['Refined characteristic class P remains0 or4 in Z/8 for the exact OS45/default example. The full primitive cubic, full fundamental class mu and integral c1=c2=lambda=0 are proved; the complete smooth classification is not asserted. The verified odd Mayer–Vietoris class does not yet supply an embedded representative with evaluated reference framing and critical-specialization linking.'],
}
all_open = [
 dict(id='mapsD:open:star-markings',source_ids=['D.2.4','D.2.49'],claim=scope_limits['D.2.49'][0]),
 dict(id='mapsD:open:corrected-original-multiplicative',source_ids=['D.2.4','D.2.50','D.2.52'],claim='Full marked boundary maps of corrected original multiplicative caps.'),
 dict(id='mapsD:open:additive-torsion-columns',source_ids=['D.2.4','D.2.51','D.2.52'],claim=scope_limits['D.2.51'][0]),
 dict(id='mapsD:open:remaining-smooth-invariants',source_ids=['D.2.4','D.2.49','D.2.50','D.2.52'],claim='Complete smooth invariants of the remaining weighted, additional-regular-log and new star-log outputs; homology computations do not identify their smooth types.'),
 dict(id='mapsD:open:OS45-refined',source_ids=['D.2.4','D.2.53'],claim=scope_limits['D.2.53'][0]),
]

for row in rows:
    sid=row['source_id']
    # Source and proof comparisons are content hashes, not filename inference.
    for block in row['source_blocks']+row.get('supplemental_source_blocks',[]):
        text=''.join((ROOT/block['file']).read_text().splitlines(keepends=True)[block['start_line']-1:block['end_line']])
        assert hashlib.sha256(text.encode()).hexdigest()==block['sha256'], (sid,block)
    for f,h in [('extracted_file','extracted_sha256'),('complete_proof_file','complete_proof_sha256')]:
        if f in row:
            assert digest(ROOT/'deliverables'/row[f])==row[h],(sid,f)
    row['proof_comparison']={
        'status':'every recorded source slice and whole extracted candidate hash rechecked',
        'additional_mathematical_provider':closure['printed_label'] if sid=='D.2.1' else None,
        'source_paragraphs_preserved':True,
        'scope':'Complete original proof retained, including separately extracted nested proof inputs. Editorial labels may be transformed by the assembly owner; this ledger fixes the mathematical source text.'}
    old_runs=row.get('program_runs',[])
    stems=[Path(x['program']).stem for x in old_runs]
    if sid.startswith('D.2.'):
        stems+=programs.get(int(sid.split('.')[-1]),[])
    if sid=='D.1.1':
        stems+=['manifolds_cover']
    selected={}
    for stem in stems:
        for run in by_stem[stem]:
            if run['exit_code']==0:
                selected[run['run_id']]=run
                if sid not in run['associated_source_ids']:
                    run['associated_source_ids'].append(sid)
    row['program_runs']=list(selected.values())
    row['numerical_check_scope']='All cited exact programs have actual successful executions attached. Finite supplementary cases are not substituted for the separately read all-parameter geometric proof.' if selected else 'No separate numerical program is operative in this row; inherited prerequisites retain their own run evidence.'
    existing=[p for p in row.get('recorded_checks',[]) if not p.get('consolidated_D_review')]
    seen={(p.get('source_file'),p.get('locator')) for p in existing}
    for p in prior[sid]:
        if (p.get('source_file'),p.get('locator')) not in seen:
            p['consolidated_D_review']=True
            existing.append(p)
    row['recorded_checks']=existing
    if existing:
        row.pop('recorded_check_absence',None)
    else:
        row['recorded_check_absence']='No separately identified prior full-proof check for this exact row was located in the declared D review pass. The final intake reports section status but is not promoted to a full-proof correctness check.'
    row['review_provenance_scope']={
        'author_registry':'sources/reviews/WHO_WROTE_WHAT.md',
        'source_production':'GPT-6 Astra (OpenAI, ChatGPT Pro mode),15–16 November2026',
        'prior_intake':'Claude Fable5.2, effort high,16 November2026: INTAKE_FINAL.md §3 lines165–195; overview/status, not a full proof audit for these69 rows',
        'current_independent_reader':META,
    }
    row['credit_checks']={key:credits[sid][key] for key in ['found_in_AC26','found_in_E26','found_in_DGKX_v1','found_elsewhere']}
    for key in row['credit_checks']:
        row[key]=row['credit_checks'][key]
    row['credit_comparison_file']='work/invariants_arithmetic/maps_D_credit_comparison.json'
    row['scoped_reference_checks']=[]
    for key in row.get('reference_dependencies',[]):
        ref=base_refs['AC2026'] if key=='AC26' else refs[key]
        row['scoped_reference_checks'].append({
            'citation_key':key,'ledger':'work/invariants_arithmetic/source_credit_map.json' if key=='AC26' else 'work/invariants_arithmetic/maps_D_references_verified.json',
            'opened_locator':ref['opened_locator'],'local_source':ref['local_source'],
            'source_sha256':ref['source_sha256'],'actual_use':ref.get('actual_use',ref.get('relation','Original construction and stated antecedent only.')),
            'status':'verified at the exact recorded scope',
        })
    row['verification_status']='verified_stated_scope'
    row['check_outcome']='verified complete proof under the stated hypotheses, with operative source and exact-computation closures completed'
    row['own_check']['outcome']=row['check_outcome']
    row['own_check']['completion_evidence']={
        'date':'2026-11-17 UTC','program_run_ids':list(selected),
        'source_checks':'scoped_reference_checks in this row; exact statements and hypotheses, not a whole-paper verification claim',
        'credit_matrix':'four original-baseline fields completed; scoped negative searches do not assert worldwide novelty',
        'earlier_pending_language':'Any pending numerical/source wording in the original reading notes below is historical and is superseded by this completion record.'}
    row['explicit_scope_limitations']=scope_limits.get(sid, row.get('explicit_scope_limitations',[]))
    row['unresolved_claims']=[{**x,'is_gap_in_stated_proved_theorem':False} for x in all_open if sid in x['source_ids']]
    if sid=='D.2.1':
        row['verification_status']='verified_with_authored_dependency_provider'
        row['check_outcome']='complete original proof checked; absent50/II and56/II geometric realization certificate replaced by a complete authored marked construction'
        row['own_check']['outcome']=row['check_outcome']
        row['dependency_repair']=closure
        row['editorial_changes']=list(dict.fromkeys(row['editorial_changes']+[
            'Replace reliance on the absent geometric-monodromy-proof.md by the complete mapsD:repair:collision-realization provider. Keep the exact known-configuration/Mordell–Weil credit to Miranda and Fukae.',
            'The provider was authored and checked by this reader and sent to the assembly owner for an independent receiving read; that receiving read is not asserted here.']))
    if sid=='D.2.2':
        row['verification_status']='verified_archival_computation_only'
        row['check_outcome']='bounded50-case archival computation independently verified; fresh endpoint attempt timed out; no unpublished geometric database proof inferred'
        row['own_check']['outcome']=row['check_outcome']
        row['own_check']['proof_read']='whole computation statement, all limitations, full request-generating and cache-verifying programs, and all50 request/response records'
        row['own_check']['details']='Regenerated all50 inputs and checked exact payload identity, saved responses, API version, echoed parameters, all homology groups, duality/free ranks, Euler and fundamental-group abelianization consistency. Independently recovered24 simply connected cases and exactly3 sphere outputs. Original50-case cached script replayed successfully. This verifies the published bounded archive, not a fresh remote topology-engine execution or an unpublished database realization theorem.'
        row['execution_limitations']=['Fresh original-endpoint POST timed out after42.462 seconds; saved at work/invariants_arithmetic/maps_D_explorer_fresh_probe.json.','Public database mathematical-scope document expressly excludes private geometric construction certificates. Those are not silently assumed.']
    if sid=='D.2.3':
        row['own_check']['details']='Re-derived the cusp Euler count3F=2E and V−E+F=0, hence F=2V; every other local piece and the torus-family exterior has Euler zero. Read the entire affine-meridian versus linear-monodromy distinction. Independently checked all8 archived clutch inputs for OS45/47/55/56: clutch0 gives Z and clutch1 the trivial group. These are archived outputs; the explicit semistable geometric group calculation is separately checked.'
    if sid=='D.2.4':
        row['verification_status']='open_problem_reconciled_with_later_results'
        row['check_outcome']='complete historical/open-task block read; each claimed later closure checked; exact remaining claims preserved in maps_D_remaining_questions.json'
        row['own_check']['outcome']=row['check_outcome']
        row['own_check']['proof_read']='whole open-problem statement and all its retrospective status paragraphs; this row is not a proved theorem'
        row['own_check']['details']='Compared every later-status clause against the complete independently read D2.22–53 proofs. The162 minimal simply connected patterns, weighted Engel family, nonsaturated general cusp, component-corrected initial data and scoped invariant-Chern caps have their separate proofs. The unrestricted filling/smooth-classification request remains open in the five precisely listed extension directions. No already resolved historical question is kept open merely because an earlier row posed it.'
        row['unresolved_claims']=all_open
    if sid=='D.2.53':
        row['own_check']['completion_evidence']['odd_bridge']='root_OS45_bridge successful rerun matches retained stdout exactly. H2 exterior=Z²+Z/2 and independent free kernel images leave precisely the order-two angular class; H3(X)=Z/8 surjects onto it. This proves an odd homology class only. The reference framing and critical-specialization intersection remain uncomputed.'

# Give each exact run a statement role and a portable archive entry.
for run in runs:
    run['associated_source_ids'].sort(key=lambda x:tuple(map(int,x.split('.')[1:])))
    if run['exit_code']!=0:
        run['associated_source_ids']=['D.1.4','D.1.12']
    run['statement_role']=run.get('role',run.get('mathematical_scope',
        'Exact algebra/chain/marking certificate for the attached result IDs; supports, and does not replace, their complete geometric proofs.'))
    if run.get('execution_type'):
        run['statement_role']=run['execution_type']+'; exact payload and bounded output checks only.'

assert len(rows)==69 and len(credits)==69 and len(runs)==73
assert all(run['associated_source_ids'] for run in runs),[r['program'] for r in runs if not r['associated_source_ids']]
save('maps_D_independent_audit.json',rows)
save('maps_D_program_manifest.json',runs)
save('maps_D_remaining_questions.json',dict(**META,questions=all_open,
    distinction='These are explicit unproved extensions/open tasks. No extra theorem gap was found in the scoped proved statements; the bounded Explorer entry remains archival only.'))

columns=['source_id','source_title','printed_label','verification_status','check_outcome','recorded_checks','own_check','program_runs','scoped_reference_checks','found_in_AC26','found_in_E26','found_in_DGKX_v1','found_elsewhere','unresolved_claims','source_blocks','supplemental_source_blocks','complete_proof_file','extracted_file']
with (WORK/'maps_D_independent_audit.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=columns)
    writer.writeheader()
    for row in rows:
        writer.writerow({k:json.dumps(row.get(k),ensure_ascii=False) if isinstance(row.get(k),(list,dict)) else row.get(k,'') for k in columns})

summary=dict(**META, result_count=len(rows), verification_status_counts=dict(Counter(r['verification_status'] for r in rows)),
    source_reference_count=len(refs),baseline_credit_rows=len(credits),baseline_search_records=len(load(WORK/'maps_D_credit_search_log.json')),
    execution_records=len(runs),successful_execution_records=sum(r['exit_code']==0 for r in runs),
    preserved_superseded_failures=sum(r['exit_code']!=0 for r in runs),
    primary_geometric_repair='work/invariants_arithmetic/maps_modular_collision_realizations.tex',
    repair_label=closure['printed_label'],
    full_audit='work/invariants_arithmetic/maps_D_independent_audit.json',
    programs='work/invariants_arithmetic/maps_D_program_manifest.json',
    remaining_questions='work/invariants_arithmetic/maps_D_remaining_questions.json',
    note='Source originals and top-level inventory were not changed. Final label/placement transforms remain with the assembly owner.')
save('maps_D_completion_summary.json',summary)
print(json.dumps(summary,ensure_ascii=False,indent=2))
