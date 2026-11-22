"""Bind actually read group11 pairs and expand each repeated literal exactly."""
from pathlib import Path
import copy
import datetime
import hashlib
import json

R = Path(__file__).resolve().parents[1]


def sha(value):
    return hashlib.sha256(value.encode() if isinstance(value, str) else value).hexdigest()


def bound(path):
    return dict(path=path, sha256=sha((R / path).read_bytes()))


def read(path):
    return json.loads((R / path).read_text())


def write(path, data):
    p = R / path
    assert not p.exists(), p
    p.write_text(json.dumps(data, indent=2) + '\n')


base = 'agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group11/'
proposal_path = base + 'S6_SERIES_PUBLISH_II_clean_group11_final_proposals.json'
events_path = base + 'S6_SERIES_PUBLISH_II_clean_group11_event_proposals.json'
assert bound(proposal_path)['sha256'] == 'b443521afe4d3d1d8206407a95d7b176dabef832d300f2d85c577883e88475b8'
assert bound(events_path)['sha256'] == '3f7013c374068362ba9871c410d9b825fe381a6e5256f20180590a2e423ee3ba'
source = bound('S6_SERIES_PUBLISH_II.tex')
assert source['sha256'] == '464cf7949b3033f58d9e01daca319d5c2ce883e2bf498fb968bd3dfa2800caef'
source_text = (R / source['path']).read_text()
d, events = read(proposal_path), read(events_path)
checked = {}


def verify_bindings(value):
    if isinstance(value, dict):
        if 'path' in value and 'sha256' in value:
            actual = bound(value['path'])
            assert actual['sha256'] == value['sha256'], (value, actual)
            checked[value['path']] = actual
        for child in value.values():
            verify_bindings(child)
    elif isinstance(value, list):
        for child in value:
            verify_bindings(child)


verify_bindings(d)
verify_bindings(events)
expected = {
    '01FD': 'e0c3f98db8525062be1415b8b6f16273f8ad8bcaca4ea639b0d3b85fa79f7ba7',
    '01FE': 'b035543fb4dfb45cbad3b3adbf90117ed55ead4cdee8b0087e811c932d2e6bfc',
    '01FF': '1d5fe6895514b7c29ca1f1c191b32f869d2c2814a0b407a18425d8c06c1c7b34',
}
assert len(d['targets']) == 3 and len(events['events']) == 6
expanded = []
for t in d['targets']:
    tag = t['tag']
    assert t['proposed_full_block']['sha256'] == expected[tag]
    original = (R / t['original_full_block']['path']).read_text()
    final = (R / t['proposed_full_block']['path']).read_text()
    assert source_text.count(original) == 1
    es = [e for e in events['events'] if e['tag'] == tag]
    assert {e['event_type'] for e in es} == {'targeted proof check', 'used and rechecked in this run'}
    for e in es:
        for key in ('statement_owner', 'checker', 'freeze_receipt', 'frozen_derivation',
                    'release_receipt', 'release_envelope', 'original_full_block', 'proposed_full_block'):
            assert e[key] == t[key], (tag, key)
        assert e['event_count'] == 1 and e['no_extra_computation_event'] is True
    t['comparison'] = next(e['scope'] for e in es if e['event_type'] == 'targeted proof check')
    t['actual_rereading_scope'] = next(e['scope'] for e in es if e['event_type'] == 'used and rechecked in this run')
    t['full_comparison'] = d['comparison']
    t['actual_complete_original_proof_read'] = True
    t['actual_complete_proposed_proof_read'] = True
    current, guards = original, []
    for g in t['guards']:
        count = g['expected_occurrences_in_owning_block']
        assert current.count(g['old']) == count, (tag, g['change_id'])
        positions, cursor = [], 0
        for i in range(count):
            pos = current.index(g['old'], cursor)
            positions.append((i, pos))
            cursor = pos + len(g['old'])
        for i, pos in reversed(positions):
            start, end = pos, pos + len(g['old'])
            assert current[start:end] == g['old']
            while current.count(current[start:end]) != 1:
                previous = start, end
                start, end = max(0, start - 80), min(len(current), end + 80)
                assert previous != (start, end)
            replacement = copy.deepcopy(g)
            replacement['old'] = current[start:end]
            replacement['new'] = current[start:pos] + g['new'] + current[pos + len(g['old']):end]
            replacement['expected_occurrences_in_owning_block'] = 1
            if count > 1:
                replacement['change_id'] += f'-occurrence-{i + 1}'
                replacement['logical_literal_before'] = g['old']
                replacement['logical_literal_after'] = g['new']
                expanded.append(dict(tag=tag, guard=replacement))
            current = current[:start] + replacement['new'] + current[end:]
            guards.append(replacement)
    assert current == final, tag
    t['guards'] = guards
for g in d['bibliography_guards']:
    g['statement_owner'] = 'bib:' + g['key']
    assert source_text.count(g['old']) == 1
    assert (R / g['original_entry']['path']).read_text() == g['old']
    assert (R / g['proposed_entry']['path']).read_text() == g['new']
patch_count = sum(len(t['guards']) for t in d['targets']) + len(d['bibliography_guards'])
assert patch_count == 38
scope = (
    'Root actually read all three complete frozen derivations and released original proofs, as already '
    'bound in root reading01; all three complete final proofs, including FD v3 and FE v2, and the '
    'complete current FF original were then read. All33 logical owner guards, both complete bibliography '
    'pairs, the full comparison, primary/input and exact-transport receipts, full final pair-reading and '
    'guard-validation receipts, all17 bounded historical owner rows and all6 event proposals were read. '
    'The incoming coded-reference rows were inspected; current C3.1 and integral-CDP smooth domains '
    'were actually read. Root separately read the F0 Hopf contraction/finite-quotient receiving paragraph '
    'at current lines45935--45943; it uses the preserved surface construction. That exposure supplies '
    'no independent F0 check and was not transmitted to the checker. FD retains its complete positive '
    'pairing argument and proves the exact reduced-image normalization lift; FE explicitly treats the '
    'primary divisor before finite-cover descent; FF retains every Picard and norm map and all factors '
    'in its six displayed identities. Smooth connected total spaces are explicit in FD/FF; no singular '
    'counterexample is claimed. Postrelease clarifications have no extra independence. Primary PDF '
    'reading is credited to i_provenance; no root primary-image or PaperII page-image credit is added. '
    'No computer routine is identified in the17 inspected historical rows and no new computation '
    'event or global defect closure is claimed.'
)
reading = 'records/S6_SERIES_PUBLISH_II_group11_root_reading_02.json'
write(reading, dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), source=source,
    prior_reading=bound('records/S6_SERIES_PUBLISH_II_group11_root_reading_01.json'),
    proposal=bound(proposal_path), event_proposal=bound(events_path), scope=scope,
    checked_bindings=list(checked.values()), duplicate_literal_expansion=expanded,
    complete_pairs=[dict(tag=t['tag'], original=t['original_full_block'], final=t['proposed_full_block']) for t in d['targets']],
    literal_patch_count=patch_count, mathematical_events_added=0, canonical_mutations=0))
d['original_agent_proposal'] = bound(proposal_path)
d['root_actual_reading'] = bound(reading)
d['root_review_scope'] = scope
reviewed = 'records/S6_SERIES_PUBLISH_II_group11_reviewed_proposals.json'
write(reviewed, d)
config = 'records/S6_SERIES_PUBLISH_II_group11_prepare_config.json'
write(config, dict(proposal=bound(reviewed), source_before_sha256=source['sha256'],
    root_actual_complete_pairs_read=True, root_review_scope=scope,
    output='records/S6_SERIES_PUBLISH_II_group11_editorial_guard.json',
    expected_patch_count=patch_count, mathematical_statement_and_values_unchanged=False))
print(json.dumps(dict(proposal=bound(reviewed), prepare_config=bound(config), root_reading=bound(reading),
    literal_patch_count=patch_count, verified_bindings=len(checked)), indent=2))
