"""Bind the read E13 proof, exact frame maps and computation certificates."""
from pathlib import Path
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


base = 'agents/ii_infra/recovery_20261121/'
gp = base + 'S6_SERIES_PUBLISH_II_01GK_guards_v2.json'
cp = base + 'S6_SERIES_PUBLISH_II_01GK_comparison_v2.json'
ep = base + 'S6_SERIES_PUBLISH_II_01GK_event_proposals_v2.json'
assert bound(gp)['sha256'] == 'c044687f356cae3e76acd3a0e00598b04efc2a44c2b47038be81ad7cb80e31ba'
assert bound(cp)['sha256'] == 'b30505759c961369aa501778727d35b445771599bd38d791e60af8adcb6d8b9d'
assert bound(ep)['sha256'] == '412f87aa36de564fd184c3cca2e661f5fa459ca87139cd3bb501b213c5b1d41c'
source = bound('S6_SERIES_PUBLISH_II.tex')
assert source['sha256'] == '5f6cc99dc76bae40cf8f982ce1fb9fd7c39d0887e6849cd6622a498eb234fd37'
s = (R / source['path']).read_text()
d, c, original_events = read(gp), read(cp), read(ep)
checked = {}


def verify(value):
    if isinstance(value, dict):
        if 'path' in value and 'sha256' in value:
            actual = bound(value['path'])
            assert actual['sha256'] == value['sha256'], (value, actual)
            checked[value['path']] = actual
        for child in value.values():
            verify(child)
    elif isinstance(value, list):
        for child in value:
            verify(child)


verify(c)
verify(original_events)
owner = d['guards'][0]
assert len(d['guards']) == 1
current = owner['before']
assert s.count(current) == 1
guards = []
for number, edit in enumerate(owner['literal_edits'], 1):
    assert current.count(edit['before']) == 1
    assert current.index(edit['before']) == edit['sequential_before_offset']
    current = current.replace(edit['before'], edit['after'], 1)
    guards.append(dict(change_id=f'II-GK-{number:03d}', old=edit['before'], new=edit['after'],
                       defect_type=edit['type'], reason=edit['reason']))
assert current == owner['after'] and len(guards) == 14
for key in ('original_full_block', 'proposed_full_block'):
    assert bound(owner[key])['sha256'] == owner[key + '_sha256']
assert (R / owner['original_full_block']).read_text() == owner['before']
assert (R / owner['proposed_full_block']).read_text() == owner['after']
programs_path = 'records/S6_SERIES_PUBLISH_II_GK_code_and_programs_binding.json'
programs = read(programs_path)
verify(programs)
for pair in programs['copies']:
    assert bound(pair['source'])['sha256'] == pair['sha256']
    assert bound(pair['destination'])['sha256'] == pair['sha256']
old_table = (R / programs['program_table_before']['path']).read_text()
new_table = (R / programs['program_table_after']['path']).read_text()
assert s.count(old_table) == 1
extra = [dict(change_id='II-GK-PROGRAMS-01', statement_owner='tab:II:programs',
    old=old_table, new=new_table, defect_type='D09',
    reason='Cite the two fresh certificates once in the sole end Programs table through the common commit macro and exact code paths; preserve all existing rows.')]
freeze = read(c['freeze_receipt']['path'])
assert bound(freeze['frozen_derivation_path'])['sha256'] == c['prereading_derivation']['sha256']
scope = (
    'Root actually read the entire frozen E13 derivation, complete original nine-item proof and complete '
    'final v2 nine-item proof, all14 literal guards, the full Markdown and JSON comparisons, all old/new '
    'program sources and outputs, the exact old-E13-only run receipt, and the event proposal. The original '
    'and final Programs tables were both read in full. Root actually viewed and read the complete public '
    'primary images6,19,20; these identify equation3.1/Proposition3.1 and Proposition6.4 with its complete '
    'family proof. The connection is the same under omega_print=omega_fresh/2, V_print=2v_fresh and '
    'a_i=2h_i; the pairing map, coherent conductor restriction, interpolation inverse and root transition '
    'are explicit. The two old computational steps are checked by exact inverse/coefficient and Laurent '
    'arithmetic after release; the prerelease computation and geometric derivation have separate timing. '
    'Every displayed formula and stable label/tag is preserved. The two E11 dependency tokens are '
    'replaced by the complete local period/connecting-map and extension argument, with the exact primary '
    'locator. No scope change, extra independent event for postrelease work, new remote repository write '
    'or PaperII page-image credit is claimed.'
)
reading = 'records/S6_SERIES_PUBLISH_II_GK_root_reading_01.json'
write(reading, dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), source=source,
    scope=scope, guard_proposal=bound(gp), comparison=bound(cp), agent_events=bound(ep),
    frozen_derivation=bound(freeze['frozen_derivation_path']), complete_original=c['original_full_block'],
    complete_final=c['proposed_full_block'], checked_bindings=list(checked.values()),
    primary_images_actually_read_by_root=c['publication_evidence']['actual_full_images_read_by_restore_build'],
    program_copies_and_table_pairs=bound(programs_path), events_added=0, canonical_mutations=0))
target = dict(tag='01GK', statement_owner='cdp:st:E13', checker='restore_build',
    freeze_receipt=bound(c['freeze_receipt']['path']), release_receipt=bound(c['release_receipt']['path']),
    frozen_derivation=bound(freeze['frozen_derivation_path']),
    original_full_block=bound(owner['original_full_block']), proposed_full_block=bound(owner['proposed_full_block']),
    actual_complete_original_proof_read=True, actual_complete_proposed_proof_read=True,
    comparison='Complete nine-item logarithmic-normal proof compared with the prerelease critical-scheme derivation through exact period, connection, pairing and residue maps.',
    full_comparison=bound(cp), guards=guards, mathematical_statement_and_values_unchanged=True)
proposal = 'records/S6_SERIES_PUBLISH_II_GK_reviewed_proposals.json'
write(proposal, dict(paper='II', targets=[target], bibliography_guards=[], checker_comparison=c,
    root_reading=bound(reading), root_reading_scope=scope, bound_inputs=[bound(gp), bound(cp), bound(ep), bound(programs_path)]))
events = 'records/S6_SERIES_PUBLISH_II_GK_reviewed_event_proposals.json'
write(events, dict(original_checker_proposal=bound(ep), comparison=bound(cp), root_reading=bound(reading), events=[
    dict(statement_owner='cdp:st:E13', event_type='targeted proof check', event_count=1,
         scope='A complete independent derivation frozen before target release computes the tangent groups through the critical-scheme exact sequence and proves smooth reduced local miniversality using the cited primary two-invariant input. The printed logarithmic-normal route is completely compared through the exact differential factor2, alternating pairing, coherent conductor projection and restriction maps. The original E13 residue/root-transition routine was isolated and read only after freeze, then checked by a different explicit-inverse and Laurent-coefficient method. Its postrelease timing adds no independent group.'),
    dict(statement_owner='cdp:st:E13', event_type='used and rechecked in this run', event_count=1,
         scope='Actually read the complete original and final v2 nine-item owner, every literal edit and all mathematical/computational comparisons. The full local rank-two period derivative and extension argument supplies the former E11 dependency. All original displayed equations, labels and tags remain identical. Public primary pages6,19,20 verify the exact source locators. The sole Programs table retains all previous rows and adds the two exact fresh certificate paths; program copies are byte-identical. No additional computation event or PaperII rendered-page credit is claimed.')], events_added=0))
config = 'records/S6_SERIES_PUBLISH_II_GK_prepare_config.json'
write(config, dict(proposal=bound(proposal), source_before_sha256=source['sha256'],
    root_actual_complete_pairs_read=True, root_review_scope=scope,
    output='records/S6_SERIES_PUBLISH_II_GK_editorial_guard.json', expected_patch_count=15,
    extra_guards=extra, mathematical_statement_and_values_unchanged=True))
print(json.dumps(dict(proposal=bound(proposal), events=bound(events), prepare_config=bound(config),
    root_reading=bound(reading), verified_bindings=len(checked)), indent=2))
