"""Seal the bounded eight-owner editorial proposal without canonical writes."""
from pathlib import Path
import collections
import csv
import datetime
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch04_working'
FINAL = ROOT / 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch04_final_v1'
P = 'S6_SERIES_PUBLISH_II_A2_D09_D04_batch04'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
sha = lambda b: hashlib.sha256(b).hexdigest()


def dump(name, value):
    (WORK / (P + '_' + name + '.json')).write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def canonical_hashes():
    return {n: sha((ROOT / n).read_bytes()) for n in [
        'S6_SERIES_PUBLISH_II.tex', 'CHECK_EVENTS.tsv',
        'S6_SERIES_PUBLISH_inventory.csv', 'S6_SERIES_PUBLISH_tags.tsv']}


assert not FINAL.exists(), 'The final packet is immutable; choose a new version.'
start_hashes = canonical_hashes()
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
guards = json.loads((WORK / (P + '_guards.json')).read_text())
inverse = json.loads((WORK / (P + '_inverse_guards.json')).read_text())
preservation = json.loads((WORK / (P + '_preservation.json')).read_text())
verification = json.loads((WORK / (P + '_verification.json')).read_text())
candidate = source
for g in guards:
    assert candidate.count(g['old']) == 1, g['id']
    candidate = candidate.replace(g['old'], g['new'])
for g in inverse:
    assert candidate.count(g['old']) == 1, g['id']
    candidate = candidate.replace(g['old'], g['new'])
assert candidate == source
for row in preservation:
    before = WORK / f"S6_SERIES_PUBLISH_II_A2_{row['tag']}_before.tex"
    after = WORK / f"S6_SERIES_PUBLISH_II_A2_{row['tag']}_after.tex"
    assert sha(before.read_bytes()) == row['before_sha256']
    assert sha(after.read_bytes()) == row['after_sha256']
    assert source.count(before.read_text()) == 1

retrieval_path = WORK / 'S6_SERIES_PUBLISH_II_A2_batch04_program_retrieval.json'
retrieval = json.loads(retrieval_path.read_text())
for row in retrieval['files']:
    path = Path(row['temporary_path'])
    assert sha(path.read_bytes()) == row['sha256']
    row['read_scope'] = 'Complete file text actually read; historical contents, not a new execution.'
    row['lines'] = len(path.read_text().splitlines())
    row['executed'] = False
retrieval['complete_reading_recorded_utc'] = now
retrieval['read_totals'] = {'program_sources': 8, 'saved_stdout_files': 8,
                          'saved_json_outputs': 8, 'historical_failure_stdout': 1}
retrieval['historical_program_executions_this_batch'] = 0
retrieval['download_disposition'] = 'Temporary source copies remain outside current and are excluded from the deliverable.'
retrieval_path.write_text(json.dumps(retrieval, indent=2, ensure_ascii=False) + '\n')

scope_source = ROOT.parent / 'S6_GRIND_3_night_run_cp36/S6_06_BLIND_results.csv'
with scope_source.open() as f:
    scope_rows = [r for r in csv.DictReader(f) if r['id'] in ['P4.26', 'P4.46']]
assert len(scope_rows) == 2
k = source.index('\\label{def:II:standing-torus-fibration}')
a = source.rfind('\\begin{definition}', 0, k)
b = source.index('\\end{definition}', k) + len('\\end{definition}')
definition = source[a:b]
definition_path = WORK / 'S6_SERIES_PUBLISH_II_A2_batch04_scope_P204.tex'
definition_path.write_text(definition)
dump('scope_receipt', {
    'created_utc': now, 'source_snapshot_sha256': sha(source.encode()),
    'historical_metadata_path': str(scope_source),
    'historical_metadata_sha256': sha(scope_source.read_bytes()),
    'selected_exact_rows': scope_rows,
    'standing_definition_path': str(definition_path.relative_to(ROOT)),
    'standing_definition_sha256': sha(definition.encode()),
    'domain_map': {
        '02XF': 'Historical Part 4.2 ambient support setting is the exact P204 setting; all local hypotheses are retained.',
        '02XK': 'P4.46 row identifies prompt 4.2 and the requested irreducible/NC support classes. P4.26 row spells out every reduced support irreducible or normal crossing. The proposed statement makes this exact whole-fibration condition explicit in P204.'},
    'new_hypothesis_or_new_restriction': False,
    'no_source_or_proof_of_closed_paper_read': True})

support = []
for path in sorted(WORK.glob('S6_SERIES_PUBLISH_II_A2_batch04_support_*.tex')):
    support.append({'path': str(path.relative_to(ROOT)), 'bytes': path.stat().st_size,
                    'sha256': sha(path.read_bytes()), 'complete_statement_proof_read': True,
                    'changed': False, 'new_check_events': 0})
with (WORK / (P + '_defects.tsv')).open() as f:
    defects = list(csv.DictReader(f, delimiter='\t'))
assert len(defects) == 47
assert sum(r['items_preserved'] for r in preservation) == 42
assert sum(r['bracket_displays_preserved'] for r in preservation) == 85
boundary_source = ROOT / 'code/S6_SERIES_PUBLISH_II_A2_D09_batch04_boundary_nodes.py'
boundary_output = WORK / 'S6_SERIES_PUBLISH_II_A2_D09_batch04_boundary_nodes_output.json'
dump('reading_receipt', {
    'created_utc': now,
    'scope': 'Exposed complete editorial comparison. No independent derivation, new computational event, required-row movement or page-reading credit.',
    'owners': [dict(owner=r['owner'], tag=r['tag'], before_sha256=r['before_sha256'],
                    after_sha256=r['after_sha256'], complete_original_and_final_read=True,
                    following_paragraph_read=True,
                    byte_identical_mathematical_block=r['before_sha256'] == r['after_sha256'])
               for r in preservation],
    'supporting_proof_reads': support,
    'actual_reading_note': 'Final XL fully reread after the last polish; final XN fully reread after combining the reference range. Every other changed final owner block fully read. XE/YB final mathematical bytes equal the fully read originals.',
    'historical_program_reading': retrieval['read_totals'],
    'historical_program_executions_this_batch': 0,
    'new_boundary_program': {'source_sha256': sha(boundary_source.read_bytes()),
                             'output_sha256': sha(boundary_output.read_bytes()),
                             'source_and_output_fully_read': True,
                             'successful_executions': 3, 'failed_assertions': 0,
                             'last_adjustment': 'Removed unnecessary nonzero assumptions on y,z; output unchanged.',
                             'additional_check_events': 0},
    'current_existing_verifier_sources_read': [
        {'path': n, 'sha256': sha((ROOT / n).read_bytes()),
         'complete_source_read': True, 'executed_this_batch': False}
        for n in ['code/S6_SERIES_PUBLISH_II_A2_YB_original_graph.py',
                  'code/S6_SERIES_PUBLISH_II_A2_P206_curve_algebra.py']],
    'all_final_guards_and_inverses_replayed': True,
    'canonical_hashes_at_final_replay': start_hashes,
    'canonical_mutations_by_agent': 0,
    'event_count': 8, 'evidence_group_count': 1})

event_path = str((FINAL / (P + '_comparison.md')).relative_to(ROOT))
events = []
for r in preservation:
    events.append({
        'statement_id': r['owner'], 'date': '2026-11-22', 'date_utc': now,
        'who': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort not separately exposed; S6_SERIES_PUBLISH continuation2, checker ii_checks_a2',
        'type': 'used and rechecked in this run',
        'event_id': f"ce:S6_SERIES_PUBLISH_II_A2_ED04_{r['tag']}_reread_20261122",
        'evidence_group': P + '_20261122', 'source_file': event_path,
        'where': r['tag'] + ' / ' + r['owner'], 'event_count': 1,
        'outcome': f"Read the complete original/final owning statement and proof ({r['items_preserved']} original item tokens) and the full following paragraph. All original mathematical regions, displays, labels, tags and equation references retained. The comparison maps every original step and every historical program computation to its actual receiving owner. XL's existing shifted-square boundary example is retained with explicit analytic coordinate maps; the bounded new program agrees. Exact domain metadata resolves XF/XK's historical setting phrases. All guards and inverses replay; no independent derivation, mathematical repair, extra computation event, required-row closure or page-reading credit. Eight owner reviews share one evidence group."})
dump('event_proposals', {'created_utc': now, 'canonical_events_added': 0, 'events': events})

end_hashes = canonical_hashes()
dump('final_replay', {
    'created_utc': now, 'source_snapshot_sha256': verification['source_snapshot_sha256'],
    'current_source_verified_sha256': sha(source.encode()),
    'exact_guards': len(guards), 'exact_inverse_guards': len(inverse),
    'owner_blocks': len(preservation), 'all_guards_unique_and_replay_exact': True,
    'canonical_hashes_before': start_hashes, 'canonical_hashes_after': end_hashes,
    'same_canonical_hashes_during_seal_preparation': start_hashes == end_hashes,
    'canonical_mutations_by_agent': 0})
FINAL.mkdir()
for path in sorted(WORK.iterdir()):
    if path.is_file(): shutil.copyfile(path, FINAL / path.name)
bindings = []
for path in sorted(FINAL.iterdir()):
    bindings.append({'path': str(path.relative_to(ROOT)), 'bytes': path.stat().st_size,
                     'sha256': sha(path.read_bytes())})
for n in ['code/S6_SERIES_PUBLISH_II_A2_D09_D04_batch04_prepare.py',
          'code/S6_SERIES_PUBLISH_II_A2_D09_D04_batch04_seal.py',
          'code/S6_SERIES_PUBLISH_II_A2_D09_batch04_boundary_nodes.py',
          'code/S6_SERIES_PUBLISH_II_A2_YB_original_graph.py',
          'code/S6_SERIES_PUBLISH_II_A2_P206_curve_algebra.py']:
    path = ROOT / n
    bindings.append({'path': n, 'bytes': path.stat().st_size, 'sha256': sha(path.read_bytes())})
index = {
    'created_utc': now, 'status': 'Immutable bounded proposal for root admission; no canonical writes.',
    'source_snapshot_sha256': verification['source_snapshot_sha256'],
    'current_source_verified_sha256': sha(source.encode()),
    'owners': preservation, 'files': bindings,
    'owner_and_following_guard_count': 34, 'Programs_guard_count': 3,
    'guard_count': 37, 'new_program_rows': 7, 'amended_program_rows': 2,
    'new_program_links': 9, 'raw_statement_reference_instances': 27,
    'defect_rows': len(defects), 'defect_rows_by_class': dict(collections.Counter(r['type'] for r in defects)),
    'events_proposed': 8, 'evidence_groups_proposed': 1,
    'new_independent_check_credit': 0, 'required_row_movement': 0,
    'canonical_mutations': 0,
    'pending_scope': 'On the fixed printed census03 basis: 47 D09 paragraphs in 45 owner contexts remain after this eight-paragraph packet is admitted. This is not a fresh whole-source closure census. Root owns D10/D16/D19 and builds; unresolved historical Paper I identities retain their separate open disposition.'}
index_path = FINAL / (P + '_index.json')
index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'index': str(index_path.relative_to(ROOT)), 'bytes': index_path.stat().st_size,
                  'sha256': sha(index_path.read_bytes()), 'bound_files': len(bindings),
                  'source_sha256': sha(source.encode()), 'guards': len(guards),
                  'defects': len(defects), 'events': len(events)}, indent=2))
