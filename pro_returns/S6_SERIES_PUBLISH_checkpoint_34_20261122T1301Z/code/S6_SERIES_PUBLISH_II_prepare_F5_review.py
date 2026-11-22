"""Bind the complete F5 proof comparison, its smooth scope and exact literal edits."""
from pathlib import Path
import datetime
import hashlib
import json
import re

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


base = 'agents/ii_infra/recovery_20261121/'
gp = base + 'S6_SERIES_PUBLISH_II_01F5_guards_v2.json'
cp = base + 'S6_SERIES_PUBLISH_II_01F5_comparison.json'
ep = base + 'S6_SERIES_PUBLISH_II_01F5_event_proposals.json'
assert bound(gp)['sha256'] == 'e3fec694985a4c6344abe4ac9fd57c75da2ab75fb8e04147848cf5c03ce8df23'
assert bound(cp)['sha256'] == 'fa86f9d9e228e9182e36a60559341b74f20fbdec6832724addf4aac7bc758073'
assert bound(ep)['sha256'] == '9a8ca4fc0e00f2cbeb4f6a1d0421a631cf39d529e17514ce5afa49897fa2eea6'
source = bound('S6_SERIES_PUBLISH_II.tex')
assert source['sha256'] == '1b18f6a907f3d75d9207f4901a08915fc173da88213d1e6a60de0d66fbd20200'
s = (R / source['path']).read_text()
d, c = read(gp), read(cp)
owner = d['guards'][0]
current = owner['before']
assert s.count(current) == 1
guards = []
for number, edit in enumerate(owner['literal_edits'], 1):
    assert current.count(edit['before']) == 1
    assert current.index(edit['before']) == edit['sequential_before_offset']
    current = current.replace(edit['before'], edit['after'], 1)
    guards.append(dict(change_id=f'II-F5-{number:03d}', old=edit['before'], new=edit['after'],
                       defect_type=edit['type'], reason=edit['reason'] + ' ' + edit.get('exact_mathematical_witness', '')))
assert current == owner['after'] and len(guards) == 25
for key in ('original_full_block', 'proposed_full_block'):
    assert bound(owner[key])['sha256'] == owner[key + '_sha256']
assert (R / owner['original_full_block']).read_text() == owner['before']
assert (R / owner['proposed_full_block']).read_text() == owner['after']
bibliography_guards, bibliography_pairs = [], []
for entry in d['guards'][1:]:
    current = entry['before']
    assert s.count(current) == 1
    for number, edit in enumerate(entry['literal_edits'], 1):
        assert current.count(edit['before']) == 1
        after = current.replace(edit['before'], edit['after'], 1)
        bibliography_guards.append(dict(change_id=f'II-F5-BIB-{entry["key"]}-{number:02d}',
                                         statement_owner=entry['statement_id'], old=current, new=after,
                                         defect_type=edit['type'], reason=edit['reason'],
                                         logical_literal_before=edit['before'], logical_literal_after=edit['after']))
        current = after
    assert current == entry['after']
    for key in ('original_entry', 'proposed_entry'):
        assert bound(entry[key])['sha256'] == entry[key + '_sha256']
    bibliography_pairs.append(dict(original=bound(entry['original_entry']), proposed=bound(entry['proposed_entry']),
                                    publication_evidence=entry['publication_evidence']))
assert len(bibliography_guards) == 3
start = s.index(owner['before'])
end = start + len(owner['before'])
hits = []
for match in re.finditer(r'(?<![A-Za-z0-9.])C\.PK\.[1-8](?![A-Za-z0-9.])', s):
    inside = start <= match.start() < end
    identifier = s[max(0, match.start() - 7):match.start()] == 'cdp:eq:'
    assert inside or identifier
    hits.append(dict(token=match.group(), character_offset=match.start(), line=s.count('\n', 0, match.start()) + 1,
                     inside_owner=inside, label_identifier=identifier))
assert len(hits) == 43
number_map = 'records/S6_SERIES_PUBLISH_II_F5_incoming_equation_map.json'
write(number_map, dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), source=source,
                       scope='All exact C.PK.1 through C.PK.8 tokens in the current source; longer tokens excluded.',
                       hits=hits, outside_owner_bare_receivers=0,
                       equation_map=[dict(old_number=f'C.PK.{n}', retained_label=f'cdp:eq:C.PK.{n}',
                                          retained_tag='tag-' + tag, new_number='ordinary paper equation counter')
                                     for n, tag in enumerate(['00V8', '00V9', '00VA', '00VB', '00VC', '00VD', '00VE', '00VF'], 1)],
                       exact_quotient_reference_transport=owner['preservation']['reference_exception'],
                       events_added=0))
freeze = read(c['freeze_receipt']['path'])
scope = (
    'Root actually read the complete original and final twelve-item F5 proof, both complete bibliography '
    'pairs, all twenty-eight literal edits, the whole frozen derivation, the full JSON and Markdown '
    'comparisons, the complete prereading program/output and postrelease shear program/output, the primary '
    'and edition receipts, both event scopes, and the exact equation-token audit. Root read the complete '
    'safe receiving statements and the integral-CDP definition, and the exact frontmatter scope was '
    'already bound. Root actually viewed Borcea printed379--380 and SS author2--3 in reading01, and now '
    'Steenbrink printed234,237,238,239 in full, including the whole printed proof of2.18 and2.20 and the '
    '2.21 formula. Further primary image reading and the source-version comparison are credited to '
    'restore_build. The Picard-family quotient and [v,z]->zv descent fix the actual positive-degree '
    'character; the four central-shear differences have explicit primitives and the displayed exact '
    'form change identifies the printed cohomology basis. The independent fibre-integral argument and '
    'the retained logarithmic argument construct the required global section through their specified '
    'maps. The sole domain repair adds smoothness, already present in each actual receiving domain. '
    'No singular counterexample or broader singular theorem is asserted. Eight stable labels and '
    'hypertargets are retained under ordinary equation numbering. No additional computation event, '
    'independent credit for postrelease work, or Paper II rendered-page credit is claimed.'
)
root_images = []
for page in (234, 237, 238, 239):
    path = base + f'GA_primary_inputs/S6_SERIES_PUBLISH_II_Steenbrink1976_p{page}.jpg'
    root_images.append(dict(**bound(path), printed_page=page, actual_root_reading='Entire page image viewed and read during this review.'))
reading = 'records/S6_SERIES_PUBLISH_II_F5_root_reading_02.json'
write(reading, dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), source=source,
                    scope=scope, prior_reading=bound('records/S6_SERIES_PUBLISH_II_F5_root_reading_01.json'),
                    final_complete_pairs=c['complete_pairs'], comparison=bound(cp), guard_proposal=bound(gp),
                    equation_map=bound(number_map), new_primary_images_actually_viewed=root_images,
                    postrelease_program=c['different_method_comparison']['postrelease_shear_program'],
                    postrelease_output=c['different_method_comparison']['postrelease_shear_output'],
                    events_added=0, canonical_mutations=0))
target = dict(tag='01F5', statement_owner='cdp:st:C.3.10', checker='restore_build',
              freeze_receipt=bound(c['freeze_receipt']['path']), release_receipt=bound(c['release_receipt']['path']),
              frozen_derivation=bound(freeze['frozen_derivation_path']),
              original_full_block=bound(owner['original_full_block']), proposed_full_block=bound(owner['proposed_full_block']),
              actual_complete_original_proof_read=True, actual_complete_proposed_proof_read=True,
              comparison='All twelve original and proposed steps compared with the pre-release fibre-integral derivation; exact family quotient, positive-degree character, full H2 action, logarithmic projection and coherent lift checked.',
              full_comparison=bound(cp), guards=guards, scope_repair=c['scope_correction'],
              mathematical_statement_and_values_unchanged=False)
proposal = 'records/S6_SERIES_PUBLISH_II_F5_reviewed_proposals.json'
write(proposal, dict(paper='II', targets=[target], bibliography_guards=bibliography_guards,
                     bibliography_full_pairs=bibliography_pairs, checker_comparison=c,
                     root_reading=bound(reading), root_reading_scope=scope,
                     bound_inputs=[bound(gp), bound(cp), bound(ep), bound(number_map), bound(c['complete_comparison_text']['path']),
                                   bound(c['prereading_input_receipt']['path'])]))
events = 'records/S6_SERIES_PUBLISH_II_F5_reviewed_event_proposals.json'
write(events, dict(original_checker_proposal=bound(ep), comparison=bound(cp), root_reading=bound(reading), events=[
    dict(statement_owner='cdp:st:C.3.10', event_type='targeted proof check', event_count=1,
         scope='A complete independent derivation was frozen before target release. It constructs the intrinsic rank-one Picard quotient and positive-degree character, proves constant period parameters and full H2 action, obtains the coherent section by the actual relative-canonical fibre integral with explicit coarea and component bounds, and uses the Serre-pairing scalar to construct an ambient positive-degree line bundle. Complete comparison verifies every step of the retained twelve-item logarithmic argument on the explicitly smooth domain. The frozen derivation and fresh prereading exterior-algebra program are bound; postrelease shear verification adds no independent event.'),
    dict(statement_owner='cdp:st:C.3.10', event_type='used and rechecked in this run', event_count=1,
         scope='Actually read the entire original and final twelve-item proof and both original/proposed bibliography pairs. Checked all twenty-eight edits, the exact relative quotient and descent map, full central-shear action with exact primitives, blowup pushforward, logarithmic de Rham projection, coherent lift and nonconstant fibrewise linear system. Smoothness is explicit and every actual receiving domain already supplies it. All eight stable equation labels and tags are retained; two C.SK.2 literals are transported to their exact label. Primary editions and actual page-image readings are recorded separately.')], events_added=0))
config = 'records/S6_SERIES_PUBLISH_II_F5_prepare_config.json'
write(config, dict(proposal=bound(proposal), source_before_sha256=source['sha256'],
                    root_actual_complete_pairs_read=True, root_review_scope=scope,
                    output='records/S6_SERIES_PUBLISH_II_F5_editorial_guard.json', expected_patch_count=28,
                    mathematical_statement_and_values_unchanged=False))
print(json.dumps(dict(proposal=bound(proposal), events=bound(events), prepare_config=bound(config),
                      root_reading=bound(reading), equation_map=bound(number_map)), indent=2))
