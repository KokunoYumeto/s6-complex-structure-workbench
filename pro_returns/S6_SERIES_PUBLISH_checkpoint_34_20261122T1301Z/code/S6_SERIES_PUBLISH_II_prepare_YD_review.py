"""Bind the whole YD proof comparison and the preserved v2 precision."""
from pathlib import Path
import datetime
import hashlib
import json
import re

R = Path(__file__).resolve().parents[1]


def sha(data):
    return hashlib.sha256(data.encode() if isinstance(data, str) else data).hexdigest()


def bound(path):
    return {'path': path, 'sha256': sha((R / path).read_bytes())}


def read(path):
    return json.loads((R / path).read_text())


def write(path, value):
    p = R / path
    assert not p.exists()
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


base = 'agents/ii_checks_A/recovery_20261121T195642Z/'
index = base + 'S6_SERIES_PUBLISH_II_A_recovery_group12_YD_final_index.json'
index2 = base + 'S6_SERIES_PUBLISH_II_A_recovery_group12_YD_final_index_v2.json'
assert bound(index)['sha256'] == 'ea17fbd2312efcdbcc1c30b8555aba06c0741d9d5e8564a533e8f7e5c244a255'
assert bound(index2)['sha256'] == '060dce7e060fe36cb11478ebfbdf6972f440bad0a0654a976bd58a6b93b4da31'
inputs = [bound(index), bound(index2)]
for item in read(index)['files']:
    assert bound(item['path'])['sha256'] == item['sha256']
    assert (R / item['path']).stat().st_size == item['bytes']
    inputs.append(bound(item['path']))
ix2 = read(index2)
for item in ix2.values():
    if isinstance(item, dict) and 'path' in item:
        assert bound(item['path'])['sha256'] == item['sha256']
        inputs.append(bound(item['path']))
precision = base + 'group12_YD_v2/S6_SERIES_PUBLISH_II_A_YD_v2_record_precision.json'
assert bound(precision)['sha256'] == '880b75f581b1290fa25a54258c78e90ef7c11f2283d682a80c6fa9b9563974ec'
inputs.append(bound(precision))
fp = 'agents/ii_infra/derivation_freezes/02YD/20261121T231704523741Z/S6_SERIES_PUBLISH_derivation_freeze_receipt.json'
rp = 'agents/ii_infra/released_proofs/02YD/ebc0b2dadfc25c76/S6_SERIES_PUBLISH_release_receipt.json'
freeze, release = read(fp), read(rp)
assert release['freeze_receipt_sha256'] == bound(fp)['sha256']
assert freeze['created_utc'] < release['created_utc']
assert bound(freeze['frozen_derivation_path'])['sha256'] == freeze['derivation_sha256']
inputs.append(bound(freeze['frozen_derivation_path']))
proposal = ix2['editorial_proposals_v2']['path']
agent_events = base + 'group12_YD/S6_SERIES_PUBLISH_II_A_YD_event_proposals.json'
comparison = base + 'S6_SERIES_PUBLISH_II_A_YD_comparison.md'
d = read(proposal)
source_path = 'S6_SERIES_PUBLISH_II.tex'
assert bound(source_path)['sha256'] == '1a64a300d711332dee3ee9779d7ad902ee58efb92ca558d912ccd86832aa440b'
source = (R / source_path).read_text()
block, = d['blocks']
assert block['tag'] == '02YD' and block['statement_unchanged'] is True
original, proposed = bound(block['original_path']), bound(block['proposed_path'])
assert original['sha256'] == block['original_sha256']
assert proposed['sha256'] == block['proposed_sha256']
cur = (R / original['path']).read_text()
assert source.count(cur) == 1
guards = []
for g in d['guards']:
    assert sha(cur) == g['intermediate_before_sha256']
    assert cur.count(g['literal_old']) == 1 and cur.index(g['literal_old']) == g['offset_before']
    cur = cur.replace(g['literal_old'], g['literal_new'], 1)
    assert sha(cur) == g['intermediate_after_sha256']
    guards.append({'change_id': g['guard_id'], 'old': g['literal_old'],
                   'new': g['literal_new'], 'defect_type': '/'.join(g['defect_types']),
                   'reason': g['reason'] + ' ' + g['mathematical_transport']})
assert len(guards) == 9 and cur == (R / proposed['path']).read_text()
assert not d['bibliography_guards']

pair_dir = 'records/S6_SERIES_PUBLISH_II_YD_context_pairs/'
pg = d['program_table_guard']
program_pair = {part: bound(pair_dir + f'programs_{part}.tex') for part in ('original', 'proposed')}
oldtable, newtable = ((R / program_pair[p]['path']).read_text() for p in ('original', 'proposed'))
end = '\\end{longtable}'
assert pg['literal_old'].endswith(end) and pg['literal_new'].endswith(end)
assert pg['literal_new'].startswith(pg['literal_old'][:-len(end)])
addition = pg['literal_new'][len(pg['literal_old']) - len(end):-len(end)]
assert newtable == oldtable[:-len(end)] + addition + end
assert source.count(oldtable) == 1
assert oldtable.count('\\href{') == 17 and newtable.count('\\href{') == 18
inputs.append(bound(pair_dir + 'rebase_receipt.json'))
extra = {'change_id': 'II-YD-PROGRAMS', 'statement_owner': 'series:II:programs',
         'old': oldtable, 'new': newtable, 'defect_type': '/'.join(pg['defect_types']),
         'reason': pg['reason'] + ' ' + pg['mathematical_transport'] + ' Exact rebase retains all seventeen current rows.'}
copypath = 'records/S6_SERIES_PUBLISH_II_YD_related_code_binding.json'
for pair in read(copypath)['copies']:
    assert bound(pair['source'])['sha256'] == pair['sha256']
    assert bound(pair['destination'])['sha256'] == pair['sha256']
inputs.append(bound(copypath))
for path in [base + 'S6_SERIES_PUBLISH_II_A_02WM_primary_scope.json',
             base + 'S6_SERIES_PUBLISH_Beauville_1978_opened_scope_01.json',
             base + 'group07_WT/S6_SERIES_PUBLISH_II_A_02WT_reading_precision.json']:
    inputs.append(bound(path))
bib_reading = []
for key in ['Kodaira1954', 'Beauville1978', 'OVV2020', 'BBK2019', 'Inoue1974']:
    match = re.search(r'\\bibitem(?:\[[^\n]*\])?\{' + re.escape(key) + r'\}', source)
    assert match
    stop = source.find('\\bibitem', match.end())
    if stop < 0:
        stop = source.index('\\end{thebibliography}', match.end())
    bib_reading.append(dict(key=key, complete_entry_sha256=sha(source[match.start():stop]),
                            actual_complete_entry_read=True, changed=False))

ev = read(agent_events)
assert len(ev['events']) == 3
old = ev['events'][1]['outcome']
assert 'and49397bb1…' in old and 'Eight literal guards' in old
ev['events'][1]['outcome'] = old.replace('and49397bb1…', 'anda3071c23…').replace('Eight literal guards', 'Nine literal guards') + (
    ' The complete v2 final has also been reread; its sole additional edit removes the iteration prefix '
    'while retaining all three items. The preserved v2 record-precision addendum supplies the actual '
    'observed rereading interval and supersedes the copied wrapper note.')
ev['events'][1]['date_utc'] = read(precision)['created_utc']
ev['v2_binding'] = {'index': bound(index2), 'rereading': ix2['whole_pair_rereading_v2'],
                    'precision': bound(precision), 'original_events_preserved': bound(agent_events),
                    'extra_event_credit': 0}
events = 'records/S6_SERIES_PUBLISH_II_YD_reviewed_event_proposals.json'
write(events, ev)
scope = (
    'Root actually read the whole frozen YD derivation, complete original and both final v1/v2 three-item '
    'proofs, whole comparison, all nine v2 guards, all events, the complete new Euler program/output, '
    'the exact related old Hopf code and full output/run, and the bounded seven-owner-row historical '
    'scope. Root read the input, freeze/release, source-scope and record-precision receipts, all five '
    'current complete bibliography entries, and both complete rebased Programs tables. Root also '
    'read the full primary OVV Proposition4.5 proof and orbifold description at source lines1734--1835; '
    'other primary proof/page reading is attributed precisely to the checker receipts. The actual '
    'normalization homeomorphism, blowdown and ruling group maps, Kodaira embedding, elliptic quotient '
    'and differential, and composed universal cover establish all stated comparisons. Symbolic cell '
    'convolution proves the Euler identities, and the degree120 related Hopf example is limited to '
    'its stated b1 overlap. The root numbering finding is corrected by the sole v2 addition; prior '
    'versions and timing precision are preserved. No mathematical assertion is refuted, no statement '
    'scope is changed, no broader absence or independent root credit is claimed, and PaperII '
    'rendered-page reading credit remains zero.'
)
target = dict(tag='02YD', statement_owner='night:P4R.2', checker='ii_check_a',
    freeze_receipt=bound(fp), release_receipt=bound(rp), frozen_derivation=bound(freeze['frozen_derivation_path']),
    original_full_block=original, proposed_full_block=proposed,
    actual_complete_original_proof_read=True, actual_complete_proposed_proof_read=True,
    comparison='All three complete original/final proof items and actual comparison maps checked against the frozen derivation.',
    full_comparison=bound(comparison), guards=guards, mathematical_statement_unchanged=True,
    scope_repairs=[], proof_repairs=[])
out = 'records/S6_SERIES_PUBLISH_II_YD_reviewed_proposals.json'
write(out, dict(paper='II', targets=[target], bibliography_guards=[],
    bibliography_reading=bib_reading, program_table_full_pair=program_pair,
    bound_inputs=inputs, root_reading_scope=scope,
    root_reading_completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
root_reading = 'records/S6_SERIES_PUBLISH_II_YD_root_reading_01.json'
write(root_reading, dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    scope=scope, proposal=bound(out), event_proposals=bound(events), bound_inputs=inputs,
    bibliography_reading=bib_reading, program_table_full_pair=program_pair,
    mathematical_events_added=0, paper_II_rendered_page_reading_credit=0))
cfg = 'records/S6_SERIES_PUBLISH_II_YD_prepare_config.json'
write(cfg, dict(proposal=bound(out), source_before_sha256=bound(source_path)['sha256'],
    root_actual_complete_pairs_read=True, root_review_scope=scope,
    output='records/S6_SERIES_PUBLISH_II_YD_editorial_guard.json', extra_guards=[extra],
    expected_patch_count=10, mathematical_statement_and_values_unchanged=True))
print(json.dumps(dict(proposal=bound(out), events=bound(events), prepare_config=bound(cfg),
    root_reading=bound(root_reading), owner_edits=9, program_edits=1), indent=2))
