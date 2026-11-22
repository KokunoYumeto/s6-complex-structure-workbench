"""Bind the completed YG proof reading and exact current Programs pair."""
from pathlib import Path
import datetime
import hashlib
import json

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
index = base + 'S6_SERIES_PUBLISH_II_A_recovery_group13_YG_final_index.json'
assert bound(index)['sha256'] == '68e60e7c56b643c1c30275dd78943704b1168ad848e8375a64ea78cab7ad5d00'
ix = read(index)
inputs = [bound(index)]
for item in ix.values():
    if isinstance(item, dict) and 'path' in item:
        assert bound(item['path'])['sha256'] == item['sha256']
        assert (R / item['path']).stat().st_size == item['bytes']
        inputs.append(bound(item['path']))
precision = base + 'group13_YG/S6_SERIES_PUBLISH_II_A_YG_program_table_precision.json'
inputs.append(bound(precision))
fp, rp = ix['freeze_receipt']['path'], ix['release_receipt']['path']
freeze, release = read(fp), read(rp)
assert release['freeze_receipt_sha256'] == bound(fp)['sha256']
assert freeze['created_utc'] < release['created_utc']
assert bound(freeze['frozen_derivation_path'])['sha256'] == freeze['derivation_sha256']
inputs.append(bound(freeze['frozen_derivation_path']))
d = read(ix['editorial_proposals']['path'])
source_path = 'S6_SERIES_PUBLISH_II.tex'
assert bound(source_path)['sha256'] == '77623b74d9997130f38153dece81fa836b3775cfc2d11ac77760a5ca99239b5b'
source = (R / source_path).read_text()
block, = d['blocks']
assert block['tag'] == '02YG' and block['statement_unchanged'] is True
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
assert len(guards) == 12 and cur == (R / proposed['path']).read_text()
assert not d['bibliography_guards']
pair_dir = 'records/S6_SERIES_PUBLISH_II_YG_context_pairs/'
pg = d['program_table_guard']
program_pair = {part: bound(pair_dir + f'programs_{part}.tex') for part in ('original', 'proposed')}
oldtable, newtable = ((R / program_pair[p]['path']).read_text() for p in ('original', 'proposed'))
assert oldtable == pg['literal_old'] and newtable == pg['literal_new']
end = '\\end{longtable}'
assert oldtable.endswith(end) and newtable.endswith(end)
assert newtable.startswith(oldtable[:-len(end)])
assert source.count(oldtable) == 1
assert oldtable.count('\\href{') == 18 and newtable.count('\\href{') == 19
inputs.append(bound(pair_dir + 'rebase_receipt.json'))
extra = {'change_id': 'II-YG-PROGRAMS', 'statement_owner': 'series:II:programs',
         'old': oldtable, 'new': newtable, 'defect_type': '/'.join(pg['defect_types']),
         'reason': pg['reason'] + ' ' + pg['mathematical_transport'] + ' The complete current eighteen rows are retained and exactly one row is appended.'}
run_source = ix['program_run']['path']
run_copy = 'code/S6_SERIES_PUBLISH_II_A_02YG_relation_run.json'
assert not (R / run_copy).exists()
(R / run_copy).write_bytes((R / run_source).read_bytes())
assert bound(run_copy)['sha256'] == ix['program_run']['sha256']
inputs.append(bound(run_copy))
events = 'records/S6_SERIES_PUBLISH_II_YG_reviewed_event_proposals.json'
ev = read(ix['event_proposals']['path'])
assert len(ev['events']) == 3
ev['root_binding'] = {'original_events': ix['event_proposals'], 'table_precision': bound(precision),
    'complete_current_table_pair': program_pair, 'events_unchanged': True, 'extra_event_credit': 0}
write(events, ev)
scope = (
    'Root actually read the complete frozen YG derivation, entire original and final four-item '
    'proofs, whole comparison, all twelve literal guards, all three events, the complete fresh '
    'Laurent-polynomial program and output/run, input/freeze/release and whole-pair receipts, '
    'the full bounded owner/gap/three historical rows/fifteen-row historical Programs scope, '
    'its actual-reading receipt, and both complete current eighteen/nineteen-row Programs tables. '
    'The index table-count prose is corrected by a preserved additive precision receipt; the actual '
    'agent guard already matches the current table exactly. The earlier held gap was read only '
    'by root and remains unchanged for its adjacent-owner audit. The positive parallel transport '
    'conjugation, nested inclusion/retraction maps, meridian normal-closure quotient, rational '
    'relation-space map and inverse, and normalization-star/graph maps give all claimed transports. '
    'Coefficient convolution checks the universal matrix identities; the determinant expansions '
    'and formal incidence cell count agree with the separate topological proof. Root makes no '
    'additional independent-check claim and no Paper II rendered-page reading claim.'
)
target = dict(tag='02YG', statement_owner='night:P4R.4', checker='ii_check_a',
    freeze_receipt=bound(fp), release_receipt=bound(rp), frozen_derivation=bound(freeze['frozen_derivation_path']),
    original_full_block=original, proposed_full_block=proposed,
    actual_complete_original_proof_read=True, actual_complete_proposed_proof_read=True,
    comparison='All four complete original/final proof items and every induced map checked against the frozen derivation.',
    full_comparison=ix['comparison'], guards=guards, mathematical_statement_unchanged=True,
    statement_precision=block['statement_precision'], scope_repairs=[], proof_repairs=[])
out = 'records/S6_SERIES_PUBLISH_II_YG_reviewed_proposals.json'
write(out, dict(paper='II', targets=[target], bibliography_guards=[],
    program_table_full_pair=program_pair, bound_inputs=inputs, root_reading_scope=scope,
    root_reading_completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
root_reading = 'records/S6_SERIES_PUBLISH_II_YG_root_reading_01.json'
write(root_reading, dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    scope=scope, proposal=bound(out), event_proposals=bound(events), bound_inputs=inputs,
    program_table_full_pair=program_pair, mathematical_events_added=0,
    paper_II_rendered_page_reading_credit=0))
cfg = 'records/S6_SERIES_PUBLISH_II_YG_prepare_config.json'
write(cfg, dict(proposal=bound(out), source_before_sha256=bound(source_path)['sha256'],
    root_actual_complete_pairs_read=True, root_review_scope=scope,
    output='records/S6_SERIES_PUBLISH_II_YG_editorial_guard.json', extra_guards=[extra],
    expected_patch_count=13, mathematical_statement_and_values_unchanged=True))
print(json.dumps(dict(proposal=bound(out), events=bound(events), prepare_config=bound(cfg),
    root_reading=bound(root_reading), owner_edits=12, program_edits=1), indent=2))
