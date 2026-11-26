"""Seal bounded editorial evidence; never write the canonical paper or ledger."""
from pathlib import Path
import collections
import csv
import datetime
import hashlib
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
BASE = 'S6_SERIES_PUBLISH_II_A2_D09_D04_batch06'
WORK = ROOT / 'agents/continuation2_A' / (BASE + '_working')
FINAL = ROOT / 'agents/continuation2_A' / (BASE + '_final_v1')
assert not FINAL.exists(), 'A sealed packet must never be overwritten.'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
sha = lambda b: hashlib.sha256(b).hexdigest()

def read_json(path):
    return json.loads(path.read_text())

def bind(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(data), 'sha256': sha(data)}

def write(name, data):
    (FINAL / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')

source_path = ROOT / 'S6_SERIES_PUBLISH_II.tex'
source_bytes = source_path.read_bytes()
source = source_bytes.decode()
source_sha = sha(source_bytes)
guards = read_json(WORK / (BASE + '_guards.json'))
inverse = read_json(WORK / (BASE + '_inverse_guards.json'))
preservation = read_json(WORK / (BASE + '_preservation.json'))
spans = []
for g in guards:
    assert source.count(g['old']) == 1, (g['id'], source.count(g['old']))
    assert sha(g['old'].encode()) == g['old_sha256']
    assert sha(g['new'].encode()) == g['new_sha256']
    start = source.index(g['old'])
    spans.append((start, start + len(g['old']), g['id']))
for left, right in zip(sorted(spans), sorted(spans)[1:]):
    assert left[1] <= right[0], (left, right)
candidate = source
for g in guards:
    assert candidate.count(g['old']) == 1, g['id']
    candidate = candidate.replace(g['old'], g['new'], 1)
for row in preservation:
    tag = row['tag']
    before = (WORK / f'S6_SERIES_PUBLISH_II_A2_{tag}_before.tex').read_text()
    after = (WORK / f'S6_SERIES_PUBLISH_II_A2_{tag}_after.tex').read_text()
    old_follow = (WORK / f'S6_SERIES_PUBLISH_II_A2_{tag}_following_before.tex').read_text()
    new_follow = (WORK / f'S6_SERIES_PUBLISH_II_A2_{tag}_following_after.tex').read_text()
    assert source.count(before + old_follow) == 1, tag
    assert candidate.count(after + new_follow) == 1, tag
    assert sha(before.encode()) == row['before_sha256']
    assert sha(after.encode()) == row['after_sha256']
restored = candidate
for g in inverse:
    assert restored.count(g['old']) == 1, g['id']
    restored = restored.replace(g['old'], g['new'], 1)
assert restored == source

FINAL.mkdir()
for path in sorted(WORK.iterdir()):
    if path.is_file():
        shutil.copyfile(path, FINAL / path.name)

support = read_json(WORK / 'S6_SERIES_PUBLISH_II_A2_batch06_support_index.json')
for r in support:
    f = FINAL / Path(r['path']).name
    r.update(bind(f))
    r.update(complete_contents_read=True, changed_by_this_packet=False, new_events=0)
write('S6_SERIES_PUBLISH_II_A2_batch06_support_index.json', support)

retrieval = read_json(WORK / 'S6_SERIES_PUBLISH_II_A2_batch06_retrieval_attempts_01.json')
opened = [r for r in retrieval['attempts'] if r.get('status') == 200]
failed = [r for r in retrieval['attempts'] if r.get('status') != 200]
assert len(opened) == 22 and len(failed) == 1
assert sum(r['name'].endswith('.py') for r in opened) == 10

methods = {
 'E_triple_images.py': ('01B9', 'Groebner saturation of three symbolic cubes; generic cubic residues; discriminant-degree and exact nodal-product identity.', 'Pole totals 3, 2+1, 1+1+1; residue valuation 18; discriminant degree -12.', 'Analytic classification and compact geometry remain in the proof.'),
 'A_low_delta_cusp.py': ('01B9', 'Symbolic-square and conormal-lattice calculations followed by three symbolic-cube saturations.', 'Exact generators and branchwise residue/pole data used in B9.', 'Other source investigations were read without additional owner credit.'),
 'E_binary_products.py': ('01BC', 'Weighted products in degrees 2–8 and variable-coefficient examples in degrees 2–5; endpoint addition.', 'Exact weighted identities and (-1)+(-1)=-2.', 'Every-degree and topological sign arguments remain in the proof.'),
 'E_cubic_double.py': ('01BC', 'Exact coordinate substitutions and inverses; factorization of finite-cover maps.', 'The vZ+y^4 chart and the scalar-zero finite-cover identities.', 'Other cubic/contact calculations receive no new event.'),
 'example_mayer_vietoris.py': ('02XD', 'Ordered local bases, inverse quotient projections, sparse cellular maps and signed global matrices.', 'Eighteen arrays; F1 determinant -1; unit Smith factors; reduced relation determinants -1,+1.', 'Historical producer read only; the new editorial comparison code was executed.'),
 'D_trivial_monodromy.py': ('01GE', 'First-unit-pivot quotient coordinates for three lattice cycles and exterior-square classes.', '15x15 determinant +1, 29x30 unit Smith factors and six primitive reduced relations.', 'The extra D.2.8 output was read without new D.2.8 credit.'),
 'A_return_germs.py': ('01D7', 'Formal coefficient extraction for d=1,...,8, with the source explanation 3d>2d.', "a'psi=a psi' and H'psi=-a lambda'; psi=ka and lambda=d0-kH.", 'The every-order analytic return argument remains in the owner.'),
 'root_cyclic_elliptic_types.py': ('01DC', 'All cyclic characters of orders 2,3,4,6, reflection-kernel gcds and elliptic branch indices.', 'Seven chi=1 and four chi=2 configurations, including zero-character disposition.', 'The local analytic quotient proof remains in the owner.'),
 'independent_sign_checks.py': ('01DF', 'Four square-zero nilpotents; exterior-square invariant kernels and restricted Gram forms.', 'Inertias (3,3,0),(1,1,2),(1,2,1),(2,1,1) and the exact alternative bases.', 'Other shared-source calculations were read without I/V proof/source/PDF exposure or extra credit; this exposed reading is not independent.'),
 'UN24_UN39_exact_certificate_08.py': ('01DI', 'Exact degree-at-most-four cyclotomics, nineteen oriented characteristic polynomials, companion determinants, averaging and Mobius inversion.', 'All nineteen table rows; j in {0,4,6,8}; zero-Euler indices 0,2,3,4.', 'UN24 extras and historical 607-check count remain historical, with no new event.')
}
program_scope = []
for r in opened:
    if not r['name'].endswith('.py'):
        continue
    owner, method, result, limit = methods[r['name']]
    program_scope.append({**r, 'receiving_tag': owner, 'source_read_in_full': True,
                          'historical_execution_this_batch': False,
                          'method_and_input': method, 'receiving_output': result,
                          'scope_limit': limit})
write(BASE + '_program_scope.json', {
    'created_utc': now, 'historical_sources': program_scope,
    'successful_output_files_read_in_full': [
        {**r, 'contents_read_in_full': True, 'reading_method': 'Complete text or exact compact JSON serialization preserving every key/value.'}
        for r in opened if not r['name'].endswith('.py')],
    'failed_retrievals': failed,
    'failed_retrieval_disposition': 'The unavailable independent_sign_checks stdout path returned HTTP404. Its complete JSON exists and was read; no historical computation was executed or failed here.',
    'downloads_excluded_from_deliverables': True,
    'current_Programs_source_macro': r'\SsixRepositoryCommit',
    'verified_historical_commit': '83d76022bcd442278b760db9ff438afceed6c6ea',
    'new_code_remote_existence_claim': False,
    'publication_gate': 'Root retains the final five-together regeneration and repository commit/link validation gate.'})

owner_reads = []
for r in preservation:
    tag = r['tag']
    owner_reads.append({**r,
        'complete_original_and_final_read': True,
        'complete_following_material_read': True,
        'before_file': bind(FINAL / f'S6_SERIES_PUBLISH_II_A2_{tag}_before.tex'),
        'after_file': bind(FINAL / f'S6_SERIES_PUBLISH_II_A2_{tag}_after.tex'),
        'following_before_file': bind(FINAL / f'S6_SERIES_PUBLISH_II_A2_{tag}_following_before.tex'),
        'following_after_file': bind(FINAL / f'S6_SERIES_PUBLISH_II_A2_{tag}_following_after.tex')})
write(BASE + '_reading_receipt.json', {
    'created_utc': now, 'reading_completed_by_utc': now,
    'scope': 'Complete exposed original/final editorial comparison; no independent derivation.',
    'owners': owner_reads, 'supporting_complete_reads': support,
    'final_reading_disposition': 'B9/BC, D7/DC and DF/DI full final pairs were read untruncated. Complete final XD/GE were reread after the last aligned-display and exact source/target-basis wording polish. All nine final Programs rows and all comparison text were read.',
    'historical_sources_read_in_full': 10,
    'historical_outputs_read_in_full': 12,
    'historical_executions_this_batch': 0,
    'new_postreading_preservation_program_executions': 1,
    'new_independent_check_credit': 0,
    'all_statement_mathematical_hypotheses_and_conclusions_unchanged': True,
    'GE_statement_editorial_reference_change': 'The internal D.2 phrase becomes the exact already stated identity-integral-monodromy class.',
    'all_original_proof_steps_retained': True,
    'all_equation_references_retained': True,
    'I_or_V_source_proof_PDF_reads': 0,
    'new_literature_status_searches': 0,
    'new_primary_source_credit': 0,
    'canonical_mutations': 0})

code_paths = [ROOT / 'code' / name for name in [
    'S6_SERIES_PUBLISH_II_A2_D09_D04_batch06_extract.py',
    'S6_SERIES_PUBLISH_II_A2_D09_D04_batch06_retrieve.py',
    'S6_SERIES_PUBLISH_II_A2_D09_batch06_matrix_maps.py',
    'S6_SERIES_PUBLISH_II_A2_D09_D04_batch06_prepare.py',
    'S6_SERIES_PUBLISH_II_A2_D09_D04_batch06_seal.py']]
write(BASE + '_execution_receipt.json', {
    'created_utc': now,
    'new_program': bind(code_paths[2]),
    'output': bind(FINAL / 'S6_SERIES_PUBLISH_II_A2_D09_batch06_matrix_maps.out'),
    'actual_executions': 1, 'first_mathematical_execution_succeeded': True,
    'historical_producer_imported_or_executed': False,
    'checks': ['Eighteen original TeX arrays equal exact generating formulas and historical JSON.',
               'XD determinants and both unit Smith-factor lists.',
               'All six local GE/XD integral quotient maps, two-sided inverses and both exact global block identities.',
               'DF exact invariant-basis map and Gram congruence for both epsilon values.'],
    'classification': 'Post-reading editorial preservation calculation; no independent or extra whole-proof event.'})
write(BASE + '_preparation_attempt_receipt.json', {
    'created_utc': now,
    'initial_preparation_failure': 'The short literal UN.19--20 reference guard matched two owner contexts. The uniqueness assertion stopped preparation.',
    'resolution': 'Each reference replacement was anchored to its exact owning sentence; inverse guards were anchored before the successful preparation.',
    'later_preparation': 'Successful exact guard/preservation generation, followed by aligned XD display formatting and precise GE source/target-basis wording; no change to mathematical values or routes.',
    'mathematical_failed_runs': 0, 'canonical_mutations': 0,
    'optional_replay_or_historical_execution_claim': False})

references = []
for g in guards:
    if 'D04' in g['defect_ids']:
        references.append({k: g[k] for k in ['id','owner','tag','old','new','old_sha256','new_sha256','reason']})
held = []
for r in preservation:
    tag = r['tag']
    old = (WORK / f'S6_SERIES_PUBLISH_II_A2_{tag}_before.tex').read_text() + (WORK / f'S6_SERIES_PUBLISH_II_A2_{tag}_following_before.tex').read_text()
    new = (WORK / f'S6_SERIES_PUBLISH_II_A2_{tag}_after.tex').read_text() + (WORK / f'S6_SERIES_PUBLISH_II_A2_{tag}_following_after.tex').read_text()
    for m in re.finditer(r'\((?:[A-Z]+\.)[A-Za-z0-9.]+\)', old):
        assert new.count(m.group()) >= old.count(m.group())
        held.append({'owner': r['owner'], 'tag': tag, 'text': m.group(),
                     'original_extract_line': old.count('\n',0,m.start())+1,
                     'disposition': 'Retained verbatim for root D19; no change in this packet.'})
assert len(held) == 8
write(BASE + '_encountered_reference_inventory.json', {
    'created_utc': now, 'scope': 'The eight completely read owner/following contexts only; no source-wide closure claim.',
    'D04_fixed_instances': references,
    'new_D05_D06_D07_fixed_instances': [],
    'D19_raw_equation_mentions_held': held,
    'classification_exclusions': ['Inert StatementRecord fourth arguments','permanent label tokens','macro definitions','Programs source links'],
    'earlier_fixed_D09_census_residual_before_this_packet': {'paragraphs':39,'contexts':37},
    'this_packet_fixed_census_contexts':8, 'this_packet_fixed_census_paragraphs':9,
    'residual_after_root_admission_pending_fresh_census': {'paragraphs':30,'contexts':29},
    'remaining_unresolved_Picard_historical_I_uses': 'The separately recorded five uses remain outside this packet; no identity is guessed.'})

write(BASE + '_removed_program_descriptions.json', {
    'created_utc': now,
    'guards_with_removed_or_relocated_narration': [
        {'guard_id': g['id'], 'owner':g['owner'], 'original':g['old'], 'receiving':g['new'], 'disposition':g['reason']}
        for g in guards if g['owner'] != 'Programs' and any(t in g['defect_ids'] for t in ['D09','D13'])],
    'historical_literature_comparison_original': (WORK/'S6_SERIES_PUBLISH_II_A2_01GE_following_before.tex').read_text(),
    'fresh_literature_status_claim': False})

group = 'S6_SERIES_PUBLISH_II_A2_D09_D04_batch06_20261122'
events = []
for r in preservation:
    events.append({
        'statement_id':r['owner'], 'date':'2026-11-22', 'date_utc':now,
        'who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort not separately exposed; S6_SERIES_PUBLISH continuation2, checker ii_checks_a2',
        'type':'used and rechecked in this run',
        'event_id':f"ce:S6_SERIES_PUBLISH_II_A2_ED06_{r['tag']}_reread_20261122",
        'evidence_group':group,
        'source_file':str((FINAL/(BASE+'_comparison.md')).relative_to(ROOT)),
        'where':f"{r['tag']} / {r['owner']}", 'event_count':1,
        'outcome':f"Read every original/final statement and proof item ({r['item_tokens']} original item tokens) and all following material. All original mathematical routes, displays, labels, tags, list formats and equation references remain. Program input/output maps and the exact relocated mathematical examples are recorded. Eighteen XD arrays and GE/DF basis maps have a post-reading preservation calculation. Eight exposed rereads share one evidence group; no independent derivation, mathematical repair, primary-page event or required-row closure."})
write(BASE+'_event_proposals.json', {'created_utc':now,'canonical_events_added':0,'events':events})
write(BASE+'_final_replay.json', {
    'created_utc':now, 'current_source_sha256':source_sha,
    'source_bytes':len(source_bytes), 'guards_unique_and_disjoint':True,
    'forward_guards':len(guards), 'inverse_guards':len(inverse),
    'all_eight_current_owner_plus_following_blocks_match':True,
    'all_eight_receiving_owner_plus_following_blocks_match':True,
    'exact_forward_inverse_identity':True,
    'in_memory_candidate_sha256':sha(candidate.encode()),
    'candidate_file_written':False,
    'canonical_source_unchanged_at_verification_end':sha(source_path.read_bytes()) == source_sha,
    'canonical_mutations':0})
assert sha(source_path.read_bytes()) == source_sha

rows = list(csv.DictReader((FINAL/(BASE+'_defects.tsv')).open(), delimiter='\t'))
files = [bind(f) for f in sorted(FINAL.iterdir()) if f.is_file()]
files += [bind(f) for f in code_paths]
index = {
    'created_utc':now, 'status':'Immutable bounded proposal for root admission; no canonical writes.',
    'source_extraction_sha256':read_json(WORK/'S6_SERIES_PUBLISH_II_A2_batch06_extraction.json')['source_sha256'],
    'source_guard_snapshot_sha256':guards[0]['source_snapshot_sha256'],
    'current_source_verified_sha256':source_sha,
    'owners':preservation, 'files':files,
    'guard_count':17, 'owner_guard_count':15, 'Programs_guard_count':2,
    'new_program_rows':8, 'amended_program_rows':1, 'new_historical_program_links':10,
    'defect_rows':len(rows), 'defect_rows_by_class':dict(collections.Counter(r['type'] for r in rows)),
    'original_item_tokens':82, 'original_proof_displays':96,
    'moved_following_displays':7, 'new_generating_displays':4,
    'former_unlabelled_output_arrays_exactly_represented':18,
    'events_proposed':8, 'evidence_groups_proposed':1,
    'new_independent_check_credit':0, 'required_row_movement':0, 'canonical_mutations':0,
    'pending_scope':'Residual fixed-census accounting after root admission:30 D09 paragraphs in29contexts. No fresh whole-source closure. Root owns D10/D16/D19/builds; B structural reservations remain untouched.'}
write(BASE+'_index.json', index)
print(json.dumps(bind(FINAL/(BASE+'_index.json')),indent=2))
print(json.dumps({k:index[k] for k in ['guard_count','defect_rows','defect_rows_by_class','events_proposed','original_item_tokens','current_source_verified_sha256']},indent=2))
