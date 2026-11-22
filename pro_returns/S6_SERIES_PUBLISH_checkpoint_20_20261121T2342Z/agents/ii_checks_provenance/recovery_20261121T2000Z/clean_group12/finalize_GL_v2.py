from pathlib import Path
import hashlib,json,re,datetime,collections

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
BASE=HERE.parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def bind(path):
    path=Path(path)
    if not path.is_absolute(): path=ROOT/path
    return {'path':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
def save(name,obj):
    p=HERE/name
    assert not p.exists(),p
    p.write_text(json.dumps(obj,indent=2)+'\n')
    return bind(p)
def artifact(name):
    return bind(HERE/name)

prep_path=HERE/'S6_SERIES_PUBLISH_II_clean_group12_preparation_v2.json'
prep=json.loads(prep_path.read_text())
old=(ROOT/prep['original_full_block']['path']).read_text()
new=(ROOT/prep['proposed_full_block']['path']).read_text()
source=ROOT/'S6_SERIES_PUBLISH_II.tex'
source_text=source.read_text()
k=source_text.index(r'\label{cdp:st:E14}')
a=source_text.rfind(r'\begin{proposition}',0,k)
z=source_text.index(r'\end{proof}',k)+len(r'\end{proof}')
assert source_text[a:z]+'\n'==old

state=old
operations=[]
for g in prep['guards']:
    matches=[m.start() for m in re.finditer(re.escape(g['old']),state)]
    assert len(matches)==g['expected_occurrences_in_owning_block'],g['change_id']
    for at in reversed(matches):
        state=state[:at]+g['new']+state[at+len(g['old']):]
        operations.append((at,g['old'],g['new'],g['change_id']))
assert state==new
for at,previous,replacement,cid in reversed(operations):
    assert state[at:at+len(replacement)]==replacement,cid
    state=state[:at]+previous+state[at+len(replacement):]
assert state==old
old_statement=old[old.index('Every member'):old.index(r'\end{proposition}')]
new_statement=new[new.index('Every member'):new.index(r'\end{proposition}')]
assert old_statement==new_statement
display=re.compile(r'\\\[(.*?)\\\]',re.S)
old_displays=display.findall(old)
assert all(x in display.findall(new) for x in old_displays)
equations=re.compile(r'\\begin\{equation\}.*?\\end\{equation\}',re.S)
assert equations.findall(old)==equations.findall(new)
labels=re.compile(r'\\(?:label|hypertarget)\{([^}]+)\}')
assert labels.findall(old)==labels.findall(new)
refs=lambda s:collections.Counter(re.findall(r'\\(?:eqref|ref|SeriesRef)\{([^}]+)\}',s))
diff={'added':dict(refs(new)-refs(old)),'removed':dict(refs(old)-refs(new))}
release=BASE/'clean_derivations/S6_SERIES_PUBLISH_II_01GL_release_pointer.json'
fr=BASE/'clean_derivations/S6_SERIES_PUBLISH_II_01GL_freeze_pointer.json'
freeze=json.loads(fr.read_text())
release_data=json.loads(release.read_text())

original_read=save('S6_SERIES_PUBLISH_II_clean_group12_original_reading.json',{
    'created_utc':now,'checker':'i_provenance_recovery','tag':'01GL',
    'statement_owner':'cdp:st:E14','release_receipt':bind(release_data['receipt']),
    'released_original':artifact('S6_SERIES_PUBLISH_II_01GL_original.tex'),
    'current_original':prep['original_full_block'],'current_source':bind(source),
    'complete_released_statement_and_all_proof_items_actually_read':True,
    'complete_current_statement_and_all_proof_items_actually_read':True,
    'original_item_count':old.count(r'\item'),
    'current_delta':'Previously applied E4 primary-reference transport; mathematical target proof unchanged.',
    'postfreeze_E13_input_full_proof_actually_read':bind('agents/ii_infra/recovery_20261121/GK_guard_blocks/S6_SERIES_PUBLISH_II_01GK_proposed_full_block_v2.tex'),
    'postfreeze_E13_comparison_actually_read':bind('agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_01GK_comparison_v2.md'),
    'rendered_manuscript_page_credit':0,'canonical_mutations':0,'events_added':0})

methods=save('S6_SERIES_PUBLISH_II_clean_group12_computation_methods.json',{
    'created_utc':now,'tag':'01GL','freeze_receipt':bind(freeze['receipt']),
    'prereading_program':artifact('S6_SERIES_PUBLISH_II_01GL_prereading_exact.py'),
    'prereading_output':artifact('S6_SERIES_PUBLISH_II_01GL_prereading_exact_output.json'),
    'prereading_receipt':artifact('S6_SERIES_PUBLISH_II_01GL_prereading_computation_receipt.json'),
    'old_slice':bind('records/S6_SERIES_PUBLISH_II_GL_prior_program_scope/S6_SERIES_PUBLISH_II_GL_old_E14_slice.py'),
    'old_slice_receipt':bind('records/S6_SERIES_PUBLISH_II_GL_prior_program_scope/S6_SERIES_PUBLISH_II_GL_old_E14_slice_receipt.json'),
    'old_output':artifact('S6_SERIES_PUBLISH_II_01GL_old_program_output.txt'),
    'postrelease_program':artifact('S6_SERIES_PUBLISH_II_01GL_postrelease_critical_norm.py'),
    'postrelease_output':artifact('S6_SERIES_PUBLISH_II_01GL_postrelease_critical_norm_output.json'),
    'all_four_program_or_output_scopes_actually_read':True,
    'old_slice_executed_after_target_release':True,
    'methods':[
        {'old':'SymPy discriminant and central substitution',
         'new':'Exact critical-value polynomial identity followed by the Vieta norm of D at the two roots of D prime; sparse rational multiplication.',
         'timing':'postrelease','qualification':'The prerelease universal cubic formula is not counted as a sufficient method distinction.'},
        {'old':'Taylor series of -i/(1+x)',
         'new':'Normalization connecting cocycle from w -> w/(1-2iw) in Q(i)[w]/(w^3).',
         'timing':'prerelease','qualification':'The exact basis transport to the printed jet model is proved in the comparison and checked postrelease.'},
        {'old':'Determinant of the displayed two by two jet matrix',
         'new':'Actual normalization restriction plus explicit inverse basis change and a two-sided four-dimensional interpolation inverse.',
         'timing':'geometric derivation and interpolation prerelease; jet basis-map certificate postrelease'}],
    'shared_E_checks_file_opened':False,'no_extra_computation_event':True,
    'canonical_mutations':0,'events_added':0})

primary_root=BASE/'primary_builds_GW/LiuRollenske2026_retry2'
primary=save('S6_SERIES_PUBLISH_II_clean_group12_primary_receipt.json',{
    'created_utc':now,'prereading_inputs':artifact('S6_SERIES_PUBLISH_II_01GL_prereading_inputs.json'),
    'LR_source':bind(primary_root/'S6_arxiv.tex'),'LR_aux':bind(primary_root/'S6_arxiv.aux'),
    'LR_compiled_pdf':bind(primary_root/'S6_arxiv.pdf'),
    'LR_edition':'arXiv:2609.33826v2; current bibliography unchanged',
    'locators':[
        {'label':'prop: surface facts','number':'Proposition 2.1','source_lines':[246,269],
         'actual_scope_read':'Complete statement with exact Weierstrass equation, section and line-homomorphism isomorphism.'},
        {'label':'thm: main','number':'Theorem 5.1','source_lines':[1702,1706],
         'actual_scope_read':'Complete statement; only its six-sphere topology conclusion is used.'}],
    'printed_page_numbers_from_private_build_used':False,
    'root_construction_inputs':bind('agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_01GL_construction_inputs_v2.tex'),
    'root_construction_receipt':bind('agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_01GL_construction_inputs_v2.json'),
    'current_E7_statement':artifact('S6_SERIES_PUBLISH_II_01GL_current_E7_statement.tex'),
    'postfreeze_E13_full_block':bind('agents/ii_infra/recovery_20261121/GK_guard_blocks/S6_SERIES_PUBLISH_II_01GK_proposed_full_block_v2.tex'),
    'postfreeze_E13_comparison':bind('agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_01GK_comparison_v2.json'),
    'scope':'All stated local maps were actually read; the E13 small-mu theorem is not extended to the cusp family. No new primary-page or mathematical event.'})

validation=save('S6_SERIES_PUBLISH_II_clean_group12_guard_validation.json',{
    'created_utc':now,'source':bind(source),'preparation':bind(prep_path),
    'current_owning_block_exact':True,'forward_exact':True,'inverse_exact':True,
    'original_statement_text_exact':True,'all_original_display_math_preserved':True,
    'all_four_labeled_equations_exact':True,'labels_and_tags_exact':True,
    'guard_count':len(prep['guards']),'literal_occurrences':len(operations),
    'reference_delta':diff,
    'math_scope':'Added explicit coordinate, relative line-bundle, root, canonical, connection, normalization and analytic-ideal maps; the old root convention has explicit domain subscripts. The iteration-only inline marker is removed. No original mathematical conclusion or domain is changed.',
    'canonical_mutations':0,'events_added':0})

comparison=artifact('S6_SERIES_PUBLISH_II_clean_group12_comparison.md')
reading=save('S6_SERIES_PUBLISH_II_clean_group12_final_pair_reading.json',{
    'created_utc':now,'checker':'i_provenance_recovery','source':bind(source),
    'rows':[{'tag':'01GL','statement_owner':'cdp:st:E14',
             'released_original':artifact('S6_SERIES_PUBLISH_II_01GL_original.tex'),
             'current_original':prep['original_full_block'],'final_proposed':prep['proposed_full_block'],
             'complete_original_statement_and_proof_actually_read':True,
             'complete_current_original_statement_and_proof_actually_read':True,
             'complete_final_proposed_statement_and_proof_actually_read':True,
             'manual_exact_guard_comparison':True,
             'scope':'Read the entire v1, corrected its two newly introduced scope ambiguities, then read every line of the complete v2 statement and all twelve proof items. Actual source reading, not inferred from validation.'}],
    'comparison':comparison,'primary_receipt':primary,'methods':methods,
    'rendered_manuscript_page_credit':0,'canonical_mutations':0,'events_added':0})

target=dict(tag='01GL',statement_owner='cdp:st:E14',checker='i_provenance_recovery',
    freeze_pointer=bind(fr),freeze_receipt=bind(freeze['receipt']),
    derivation=bind(BASE/'clean_derivations/S6_SERIES_PUBLISH_II_01GL_fresh_derivation.md'),
    release_receipt=bind(release_data['receipt']),
    released_original_full_block=artifact('S6_SERIES_PUBLISH_II_01GL_original.tex'),
    original_full_block=prep['original_full_block'],proposed_full_block=prep['proposed_full_block'],
    guards=prep['guards'])
final=save('S6_SERIES_PUBLISH_II_clean_group12_final_proposals.json',{
    'schema_version':1,'paper':'II','checker':'i_provenance_recovery','created_utc':now,
    'source_at_final_review':bind(source),'targets':[target],'bibliography_guards':[],
    'original_reading':original_read,'prereading_inputs':artifact('S6_SERIES_PUBLISH_II_01GL_prereading_inputs.json'),
    'preparation':bind(prep_path),'comparison':comparison,'primary_receipt':primary,
    'computation_methods':methods,'final_pair_reading':reading,'guard_validation':validation,
    'mathematical_statement_and_values_unchanged':True,
    'displayed_final_conclusions_preserved':True,
    'scope_exceptions':['Explicit map and dependency expansions listed in the validation; no enlargement of the E13 parameter domain.','Temporary local cusp coordinate renaming is transported back by its actual quotient-ring map.'],
    'prior_exposure':'Declared cited construction and E1/E4/E5/E6/E13 statements; prior completed E7/D1.9 and Paper I inputs; related E13 method/status messages and primary Two coherent calculation. E14 proof and old E14 routine remained closed until freeze. Complete E13 proof was read only afterward for local-input comparison.',
    'prospective_counts':{'targeted_proof_check':1,'used_and_rechecked':1,'additional_computation_event':0},
    'status':'Complete actual comparison and final full-pair reading; root review and canonical application pending.',
    'canonical_mutations':0,'events_added':0})

events=[]
for typ,scope in [
 ('targeted proof check','Frozen full prereading construction, cusp normalization-cocycle and critical-scheme derivation; exact original/full revised logarithmic proof comparison. Includes fresh prerelease programs and disclosed postrelease critical-root norm certificate; no additional independent event.'),
 ('used and rechecked in this run','Actual complete current original and final v2 statement/proof rereading after the exact publication guards; no second independent derivation is claimed.')]:
    events.append({'paper':'II','tag':'01GL','statement_owner':'cdp:st:E14',
        'checker':'i_provenance_recovery','event_type':typ,'event_count':1,'scope':scope,
        'freeze_receipt':target['freeze_receipt'],'frozen_derivation':target['derivation'],
        'release_receipt':target['release_receipt'],'original_full_block':target['original_full_block'],
        'proposed_full_block':target['proposed_full_block'],'proposal_bundle':final,
        'comparison':comparison,'computation_methods':methods,'final_pair_reading':reading,
        'source_application_pending':True,'proposal_only':True,'no_extra_computation_event':True,
        'mathematical_statement_and_values_unchanged':True,
        'prior_exposure':'Exactly as disclosed in the final proposal and frozen prereading input receipt.'})
ep=save('S6_SERIES_PUBLISH_II_clean_group12_event_proposals.json',{
    'schema_version':1,'paper':'II','created_utc':now,'proposal_only':True,'events':events,
    'prospective_counts':{'targeted_proof_check':1,'used_and_rechecked':1},
    'canonical_mutations':0,'events_added':0})
print(json.dumps({'final':final,'events':ep,'reading':reading,'methods':methods,
                  'guard_count':len(prep['guards']),'literal_occurrences':len(operations),
                  'source':bind(source)},indent=2))
