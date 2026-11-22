"""Bind the actually read group10 pairs and expand repeated literal edits exactly."""
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
    destination = R / path
    assert not destination.exists(), destination
    destination.write_text(json.dumps(data, indent=2) + '\n')


base = 'agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group10/'
agent_proposal = base + 'S6_SERIES_PUBLISH_II_clean_group10_final_proposals.json'
event_proposal = base + 'S6_SERIES_PUBLISH_II_clean_group10_event_proposals.json'
assert bound(agent_proposal)['sha256'] == '855e6b4bc4e616a9044ecdcdf7ed94b0126d710747909ff84eb152afc9672d07'
assert bound(event_proposal)['sha256'] == 'b49060b8a8308dfecdcbca91ba667ec0a9dca23ee8bc9c291391f12f7f812375'
source = bound('S6_SERIES_PUBLISH_II.tex')
assert source['sha256'] == '40d3207b67e1af91ee1907fae0be6bddae66725b6459f6e3d34a13c135c56a2b'
text = (R / source['path']).read_text()
d = read(agent_proposal)
ev = read(event_proposal)
checked_bindings = {}


def verify_bindings(value):
    if isinstance(value, dict):
        if 'path' in value and 'sha256' in value:
            actual = bound(value['path'])
            assert actual['sha256'] == value['sha256'], (value, actual)
            checked_bindings[value['path']] = actual
        for child in value.values():
            verify_bindings(child)
    elif isinstance(value, list):
        for child in value:
            verify_bindings(child)


verify_bindings(d)
verify_bindings(ev)
expected_proposed = {
    '03IC': '3c97fb76f42717bc4f7b8ee773e90d57c5b3115644fd0ea81f582bf333980ebd',
    '03IE': 'bf0456dd36d595be41a031c61b1eed7f8b002490e4c0034359a5b8925d94bc41',
    '03ID': 'baf0d047122bcf436d4a0087e002ef2314b322d9c4c29a6279d3b3d747dbb00b',
    '03IL': '2a34e7f51a77e61380e8fa79dcecbf74fb2ada0b591de3a98a7a8ab4d16fa001',
    '03IM': '465d1f0223516b1260d0980cb49f519a899eef501c837ef5c9863aaea40c4a57',
    '03DR': 'f6b7e21078c5dbefab367eaf32639d52089d61c24aeb3fd13d59c5fa9c73076c',
    '03IW': 'aa992062c7c73053f99efc6cb98f15c3d36c07d8c950cd13db07ad6848f56dc0',
    '03IN': '4006fe64fe5b2b88f578e5cd8b2aa4d3dc1ac457d6a168b862ab6fc0a2a15a52',
    '03IH': '815115ab33ef3864b80aad2e8e11d9b5e186b2ec1a74cf7e00f0cf969d7a9646',
    '03I6': '32acfd89837782cbca8b2cc55abda954e7b7ebf64ea88c310160ae5ffbc7e889',
}
expanded = []
event_comparisons = []
assert len(d['targets']) == 10 and len(ev['events']) == 20
for target in d['targets']:
    tag = target['tag']
    assert target['proposed_full_block']['sha256'] == expected_proposed[tag]
    original = (R / target['original_full_block']['path']).read_text()
    proposed = (R / target['proposed_full_block']['path']).read_text()
    assert text.count(original) == 1
    target_events = [event for event in ev['events'] if event['tag'] == tag]
    assert {event['event_type'] for event in target_events} == {'targeted proof check', 'used and rechecked in this run'}
    for event in target_events:
        for key in ('statement_owner', 'checker', 'prior_exposure', 'mathematical_statement_and_values_unchanged',
                    'displayed_final_conclusions_preserved', 'freeze_receipt', 'frozen_derivation',
                    'release_envelope', 'release_receipt', 'original_full_block', 'proposed_full_block',
                    'named_statement_scope'):
            assert event[key] == target[key], (tag, key)
        expected_scope = target['comparison'] if event['event_type'] == 'targeted proof check' else target['actual_rereading_scope']
        assert event['scope'] == expected_scope
        assert event['event_count'] == 1 and event['no_extra_computation_event'] is True
        event_comparisons.append(dict(tag=tag, event_type=event['event_type'], scope_exactly_matches_read_comparison=True))
    current = original
    new_guards = []
    for guard in target['guards']:
        count = guard['expected_occurrences_in_owning_block']
        assert current.count(guard['old']) == count, (tag, guard['change_id'])
        positions = []
        cursor = 0
        for index in range(count):
            position = current.index(guard['old'], cursor)
            positions.append((index, position))
            cursor = position + len(guard['old'])
        # Right-to-left occurrence edits preserve the offsets of pending matches,
        # including replacements that themselves contain the original literal.
        for index, position in reversed(positions):
            assert current[position:position + len(guard['old'])] == guard['old']
            start, end = position, position + len(guard['old'])
            while current.count(current[start:end]) != 1:
                previous = (start, end)
                start, end = max(0, start - 80), min(len(current), end + 80)
                assert previous != (start, end)
            replacement = copy.deepcopy(guard)
            replacement['old'] = current[start:end]
            replacement['new'] = current[start:position] + guard['new'] + current[position + len(guard['old']):end]
            replacement['expected_occurrences_in_owning_block'] = 1
            if count > 1:
                replacement['change_id'] += f'-occurrence-{index + 1}'
                replacement['logical_literal_before'] = guard['old']
                replacement['logical_literal_after'] = guard['new']
                expanded.append(dict(tag=tag, guard=replacement))
            assert current.count(replacement['old']) == 1
            current = current.replace(replacement['old'], replacement['new'], 1)
            new_guards.append(replacement)
    assert current == proposed, tag
    target['guards'] = new_guards
for guard in d['bibliography_guards']:
    guard['statement_owner'] = 'bib:' + guard['key']
    assert text.count(guard['old']) == 1
    assert (R / guard['original']['path']).read_text() == guard['old']
    assert (R / guard['proposed']['path']).read_text() == guard['new']
patch_count = sum(len(target['guards']) for target in d['targets']) + len(d['bibliography_guards'])
assert patch_count == 130
scope = (
    'Root actually read all ten complete original and final proposed owning proofs, all ten complete frozen '
    'derivations, the complete fresh Fraction/interpolation program and all its output, all 123 logical '
    'owner guard pairs and three complete bibliography pairs, and the full primary, method, exact-transport, '
    'deck-correction and dated CLS-name receipts. The final immutable IH was read again in full after its '
    'selected-root wording changed. All ten final comparison scopes and the full pair-reading and guard '
    'receipts were read. Each event scope and its bindings are verified byte-for-byte against those read '
    'comparison fields. Nine proposed-proof hashes match the earlier complete readings; final IH is bound '
    'to the current complete rereading. Primary-source image and historical related-program readings are '
    'credited to i_provenance, not root. IC retains only the proved forward implication; IH selects the '
    'fixed-whisker lift and records b=-b_plus; IM transports the primitive generator by omega=epsilon*p*omega_AC. '
    'The exact chart identities transport the primary construction and nearby-cycle units. Frozen bytes '
    'are preserved and postrelease corrections add no independent credit. No Paper II rendered-page '
    'reading, extra computation event, or global defect closure is claimed.'
)
reading = 'records/S6_SERIES_PUBLISH_II_group10_root_reading_02.json'
write(reading, dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    source=source, agent_proposal=bound(agent_proposal), event_proposal=bound(event_proposal),
                    scope=scope, checked_file_bindings=list(checked_bindings.values()),
                    complete_pairs=[dict(tag=t['tag'], original=t['original_full_block'], proposed=t['proposed_full_block']) for t in d['targets']],
                    event_field_comparisons=event_comparisons, duplicate_literal_expansion=expanded,
                    mathematical_statement_and_values_unchanged=False,
                    literal_patch_count=patch_count, events_added=0, canonical_mutations=0))
d['original_agent_proposal'] = bound(agent_proposal)
d['root_actual_reading'] = bound(reading)
d['root_review_scope'] = scope
proposal = 'records/S6_SERIES_PUBLISH_II_group10_reviewed_proposals.json'
write(proposal, d)
config = 'records/S6_SERIES_PUBLISH_II_group10_prepare_config.json'
write(config, dict(proposal=bound(proposal), source_before_sha256=source['sha256'],
                   root_actual_complete_pairs_read=True, root_review_scope=scope,
                   output='records/S6_SERIES_PUBLISH_II_group10_editorial_guard.json',
                   expected_patch_count=patch_count, mathematical_statement_and_values_unchanged=False))
print(json.dumps(dict(proposal=bound(proposal), prepare_config=bound(config), root_reading=bound(reading),
                      literal_patch_count=patch_count, verified_bindings=len(checked_bindings), expanded_duplicate_guards=expanded), indent=2))
