"""Bind the complete GI proof comparison, primary locator and exact maps."""
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
gp = base + 'S6_SERIES_PUBLISH_II_01GI_guards_final.json'
cp = base + 'S6_SERIES_PUBLISH_II_01GI_comparison.json'
ep = base + 'S6_SERIES_PUBLISH_II_01GI_event_proposals.json'
assert bound(gp)['sha256'] == 'a8caeae7dfbb67644330e9baa10e4ae647c9d510d97362f720a6078eb4d87195'
assert bound(cp)['sha256'] == 'df3b4052dbbed4fcfff7346ea00514d2e1a205fb437671d1ab4203ccb9baa67d'
assert bound(ep)['sha256'] == 'eb98cc399f4639bc80155646caca6a2542d08a27e7ec8d912927948db885fc23'
source = bound('S6_SERIES_PUBLISH_II.tex')
assert source['sha256'] == '7da6ccc1170e25175a8feec240949bf6740eda6c94e7361f59b5a44c5c0e5107'
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
owner, bib = d['guards']
assert owner['statement_id'] == 'cdp:st:E11'
current = owner['before']
assert s.count(current) == 1
guards = []
for number, edit in enumerate(owner['literal_edits'], 1):
    assert current.count(edit['before']) == 1
    assert current.index(edit['before']) == edit['sequential_before_offset']
    current = current.replace(edit['before'], edit['after'], 1)
    guards.append(dict(change_id=f'II-GI-{number:03d}', old=edit['before'], new=edit['after'],
                       defect_type=edit['type'], reason=edit['reason']))
assert current == owner['after'] and len(guards) == 10
for key in ('original_full_block', 'proposed_full_block'):
    assert bound(owner[key])['sha256'] == owner[key + '_sha256']
assert (R / owner['original_full_block']).read_text() == owner['before']
assert (R / owner['proposed_full_block']).read_text() == owner['after']
assert bib['statement_id'] == 'bib:Viaclovsky2026Log'
for key, field in [('original_entry', 'before'), ('proposed_entry', 'after')]:
    assert bound(bib[key])['sha256'] == bib[key + '_sha256']
    assert (R / bib[key]).read_text() == bib[field]
assert s.count(bib['before']) == 1
bibguard = dict(change_id='II-GI-BIB-Viaclovsky2026Log', statement_owner=bib['statement_id'],
                old=bib['before'], new=bib['after'], defect_type=bib['type'], reason=bib['reason'])
programs_path = 'records/S6_SERIES_PUBLISH_II_GI_code_and_programs_binding.json'
programs = read(programs_path)
verify(programs)
for pair in programs['copies']:
    assert bound(pair['source'])['sha256'] == pair['sha256']
    assert bound(pair['destination'])['sha256'] == pair['sha256']
old_table = (R / programs['program_table_before']['path']).read_text()
new_table = (R / programs['program_table_after']['path']).read_text()
assert s.count(old_table) == 1
assert old_table.count('\\href{') == 15 and new_table.count('\\href{') == 17
extra = [dict(change_id='II-GI-PROGRAMS-01', statement_owner='tab:II:programs',
    old=old_table, new=new_table, defect_type='D09',
    reason='Cite the two exact certificates once in the sole end Programs table through the common commit macro and exact code paths; preserve all fifteen existing rows.')]
freeze = read(c['freeze_receipt']['path'])
release = read(c['release_receipt']['path'])
assert freeze['created_utc'] < release['created_utc']
assert release['freeze_receipt_sha256'] == c['freeze_receipt']['sha256']
assert bound(freeze['frozen_derivation_path'])['sha256'] == c['frozen_derivation']['sha256']
scope = (
    'Root actually read the whole frozen GI derivation, complete original and final v2 four-item proof, '
    'all ten owner edits and the complete bibliography pair, both full comparisons, every fresh and '
    'postrelease program/output field, the old E11-only code and full run/scope receipts, the input '
    'and freeze/release records, and the original/final Programs tables. Root actually viewed and '
    'read the complete public primary p1, including full Theorem1.1, and read exact primary source '
    'lines262--350 and386--492, including the entire affine-filling proposition and proof. Root also '
    'read the complete current-I integral dictionary statement/proof. The global root morphism, '
    'fixed-cover affine derivative and translation-cohomology maps, integral basis conjugacies, '
    'period coordinate map, Euler-field factor, covector sign and u/c parameter map are explicit. '
    'The two intermediate weighted cohomology regimes are retained; universal congruence arguments '
    'prove all admissible cases and the finite runs check their implementation. The postrelease '
    'Hilbert recurrence checks all old E11 identities by a different method and expands HRR exactly. '
    'The four original proof items, all original displayed formulas and the whole stated p!=0 '
    'affine-twist scope remain. No independent root credit, extra computation event, PaperII '
    'rendered-page reading or remote code availability is claimed.'
)
reading = 'records/S6_SERIES_PUBLISH_II_GI_root_reading_01.json'
primary_image = base + 'GI_primary_pdf/S6_SERIES_PUBLISH_public_page-01.png'
write(reading, dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), source=source,
    scope=scope, guard_proposal=bound(gp), comparison=bound(cp), agent_events=bound(ep),
    frozen_derivation=bound(freeze['frozen_derivation_path']), complete_original=c['original_full_block'],
    complete_final=c['proposed_full_block'], checked_bindings=list(checked.values()),
    primary_images_actually_read_by_root=[dict(bound(primary_image), printed_page=1)],
    program_copies_and_table_pairs=bound(programs_path), events_added=0, canonical_mutations=0))
target = dict(tag='01GI', statement_owner='cdp:st:E11', checker='restore_build',
    freeze_receipt=bound(c['freeze_receipt']['path']), release_receipt=bound(c['release_receipt']['path']),
    frozen_derivation=bound(freeze['frozen_derivation_path']),
    original_full_block=bound(owner['original_full_block']), proposed_full_block=bound(owner['proposed_full_block']),
    actual_complete_original_proof_read=True, actual_complete_proposed_proof_read=True,
    comparison='Complete four-item logarithmic-normal proof compared with the prerelease critical-scheme derivation through exact root, affine, conductor, integral marking and scale-class maps.',
    full_comparison=bound(cp), guards=guards, mathematical_statement_and_values_unchanged=True)
proposal = 'records/S6_SERIES_PUBLISH_II_GI_reviewed_proposals.json'
write(proposal, dict(paper='II', targets=[target], bibliography_guards=[bibguard], checker_comparison=c,
    root_reading=bound(reading), root_reading_scope=scope, bound_inputs=[bound(gp), bound(cp), bound(ep), bound(programs_path)]))
events = 'records/S6_SERIES_PUBLISH_II_GI_reviewed_event_proposals.json'
write(events, dict(original_checker_proposal=bound(ep), comparison=bound(cp), root_reading=bound(reading), events=[
    dict(statement_owner='cdp:st:E11', event_type='targeted proof check', event_count=1,
         scope='A complete derivation frozen before target and old-routine release computes the tangent groups through the critical-scheme sequence and proves smooth reduced miniversality of the stated scale family. Exact higher-root and affine descent, period and integral marking maps, Euler-field/covector normalization and both intermediate weighted-cohomology regimes are supplied. Related GK exposure and the precise current-I inputs are disclosed. Universal congruences establish all stated cases. After release, the old E11-only slice was read and run; a new Hilbert-series recurrence checks every old identity by a different method and the HRR expansion by exact coefficients.'),
    dict(statement_owner='cdp:st:E11', event_type='used and rechecked in this run', event_count=1,
         scope='Actually read all four original and final proof items, every edit and both full bibliography entries. The exact root map, fixed-cover affine derivative, normalized scale class and analytic local-algebra argument are explicit. The complete original logarithmic-normal/RR argument, every displayed original formula and full affine-twist conclusion remain. Public Theorem1.1 p1 and exact version-one source bytes are bound. All fifteen current Programs rows are retained and two exact program rows added; copied programs/outputs remain byte-identical. No extra independent or computation event and no PaperII rendered-page credit.')], events_added=0))
config = 'records/S6_SERIES_PUBLISH_II_GI_prepare_config.json'
write(config, dict(proposal=bound(proposal), source_before_sha256=source['sha256'],
    root_actual_complete_pairs_read=True, root_review_scope=scope,
    output='records/S6_SERIES_PUBLISH_II_GI_editorial_guard.json', expected_patch_count=12,
    extra_guards=extra, mathematical_statement_and_values_unchanged=True))
print(json.dumps(dict(proposal=bound(proposal), events=bound(events), prepare_config=bound(config),
    root_reading=bound(reading), verified_bindings=len(checked)), indent=2))
