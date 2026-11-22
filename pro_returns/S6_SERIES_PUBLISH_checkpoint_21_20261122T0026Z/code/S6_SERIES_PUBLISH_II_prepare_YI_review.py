"""Bind the fully read YI comparison, record precision, and exact current Programs pair."""
from pathlib import Path
import datetime
import hashlib
import json
import sys

R = Path(__file__).resolve().parents[1]


def sha(value):
    return hashlib.sha256(value.encode() if isinstance(value, str) else value).hexdigest()


def bound(path):
    return dict(path=path, sha256=sha((R / path).read_bytes()))


def read(path):
    return json.loads((R / path).read_text())


def write(path, value):
    p = R / path
    assert not p.exists(), p
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


base = 'agents/ii_checks_A/recovery_20261121T195642Z/'
index = base + 'S6_SERIES_PUBLISH_II_A_recovery_group14_YI_final_index_v2.json'
assert bound(index)['sha256'] == 'd249defc912cd6dc66a21194bf834350430df8c682ef7580e9bb8c83a43c6b69'
ix = read(index)
inputs = [bound(index)]
for item in ix.values():
    if isinstance(item, dict) and 'path' in item:
        assert bound(item['path'])['sha256'] == item['sha256']
        assert (R / item['path']).stat().st_size == item['bytes']
        inputs.append(bound(item['path']))
precision = sys.argv[1]
assert 'YI' in precision and (R / precision).is_file()
inputs.append(bound(precision))
fp, rp = ix['freeze_receipt']['path'], ix['release_receipt']['path']
freeze, release = read(fp), read(rp)
assert release['freeze_receipt_sha256'] == bound(fp)['sha256']
assert freeze['created_utc'] < release['created_utc']
assert bound(freeze['frozen_derivation_path'])['sha256'] == ix['derivation']['sha256']
inputs.append(bound(freeze['frozen_derivation_path']))
source_path = 'S6_SERIES_PUBLISH_II.tex'
source_binding = bound(source_path)
assert source_binding['sha256'] == '2b41af5e10c76a8f7f236b16b0b647cc22eb7d293a1504f50c6fecc090957588'
source = (R / source_path).read_text()
d = read(ix['editorial_proposals']['path'])
block, = d['blocks']
assert block['tag'] == '02YI' and block['statement_unchanged'] is True
original, proposed = bound(block['original_path']), bound(block['proposed_path'])
assert original['sha256'] == block['original_sha256']
assert proposed['sha256'] == block['proposed_sha256']
cur = (R / original['path']).read_text()
assert source.count(cur) == 1
guards = []
for g in d['guards']:
    assert sha(cur) == g['intermediate_before_sha256']
    assert cur.count(g['literal_old']) == 1
    assert cur.index(g['literal_old']) == g['offset_before']
    cur = cur.replace(g['literal_old'], g['literal_new'], 1)
    assert sha(cur) == g['intermediate_after_sha256']
    guards.append(dict(change_id=g['guard_id'], old=g['literal_old'], new=g['literal_new'],
        defect_type='/'.join(g['defect_types']), reason=g['reason'] + ' ' + g['mathematical_transport']))
assert len(guards) == 7 and cur == (R / proposed['path']).read_text()

bibliography = []
for g in d['bibliography_guards']:
    old = (R / g['original_path']).read_text()
    new = (R / g['proposed_path']).read_text()
    assert old == g['literal_old'] and new == g['literal_new']
    assert sha(old) == g['old_sha256'] and sha(new) == g['new_sha256']
    assert source.count(old) == 1
    inputs.extend([bound(g['original_path']), bound(g['proposed_path'])])
    bibliography.append(dict(change_id='II-YI-BIB-' + g['key'],
        statement_owner='bib:' + g['key'], old=old, new=new,
        defect_type='/'.join(g['defect_types']), reason=g['reason'] + ' ' + g['mathematical_transport']))
assert len(bibliography) == 2
pg = d['program_table_guard']
oldtable, newtable = (R / pg['original_path']).read_text(), (R / pg['proposed_path']).read_text()
assert oldtable == pg['literal_old'] and newtable == pg['literal_new']
assert sha(oldtable) == pg['old_sha256'] and sha(newtable) == pg['new_sha256']
assert source.count(oldtable) == 1
assert oldtable.count('\\href{') == 23 and newtable.count('\\href{') == 25
assert newtable == oldtable.replace('\\end{longtable}', pg['added_rows'] + '\\end{longtable}')
program_pair = dict(original=bound(pg['original_path']), proposed=bound(pg['proposed_path']))
extra = dict(change_id='II-YI-PROGRAMS', statement_owner='tab:II:programs',
    old=oldtable, new=newtable, defect_type='/'.join(pg['defect_types']),
    reason=pg['reason'] + ' ' + pg['mathematical_transport'])

old_scope = read(ix['bounded_prior_scope']['path'])
assert old_scope['current_complete_owner']['text'] == (R / original['path']).read_text()
prior_table = 'records/S6_SERIES_PUBLISH_II_GN_context_pairs/programs_before.tex'
assert old_scope['end_program_table']['text'] == (R / prior_table).read_text()
assert bound(prior_table)['sha256'] == 'd62290ebeb3c092e3690b944c268fa49327e6454f0b004dc80ec44f28e07214e'
inputs.append(bound(prior_table))
standing = read('records/S6_SERIES_PUBLISH_II_WW_WX_safe_named_inputs.json')['standing_domain']
assert sha(standing['text']) == standing['sha256'] == 'e0c83437d70bfb93061f7a12854252269d7219914c152d17a269cbfc08871dab'
inputs.append(bound('records/S6_SERIES_PUBLISH_II_WW_WX_safe_named_inputs.json'))

copies = []
for key in ['prerelease_run', 'related_prior_run', 'postrelease_run']:
    origin = ix[key]['path']
    dest = 'code/' + Path(origin).name
    assert not (R / dest).exists(), dest
    (R / dest).write_bytes((R / origin).read_bytes())
    assert bound(dest)['sha256'] == ix[key]['sha256']
    copies.append(dict(source=bound(origin), destination=bound(dest), exact_byte_copy=True))
    inputs.append(bound(dest))
code_binding_path = 'records/S6_SERIES_PUBLISH_II_YI_code_and_programs_binding.json'
write(code_binding_path, dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    copies=copies, complete_math_sources=[ix[k] for k in ['prerelease_program','related_prior_excerpt','postrelease_program']],
    complete_math_outputs=[ix[k] for k in ['prerelease_output','related_prior_output','postrelease_output']],
    program_table_full_pair=program_pair, program_rows_before=23, program_rows_after=25,
    root_program_executions=0, additional_computation_events=0))
inputs.append(bound(code_binding_path))
root_images = []
for path, page in [
    (base + 'S6_SERIES_PUBLISH_Mumford_1961_p6-03.png', 'Mumford printed p.6'),
    (base + 'Milnor1968/S6_SERIES_PUBLISH_Milnor1968_viewer_001.webp', 'Milnor 1968 title page'),
    (base + 'S6_SERIES_PUBLISH_Lojasiewicz_1964_page-17.png', 'Lojasiewicz printed p.464')]:
    root_images.append(dict(image=bound(path), scope=page, actual_complete_image_read_by_root=True))
scope = (
    'Root actually read the entire frozen YI derivation, the complete original, proposed v1 '
    'and final v2 four-item proofs, the whole comparison and its additive Div(T) and '
    'total-quotient-ring corrections, '
    'all seven literal owner guards, both full bibliography pairs, all three events, '
    'the complete old pinned compactification source and its exact n=1 executable prefix, '
    'both complete fresh programs and every output field, and all input/freeze/release/run/'
    'failure/primary-reading/whole-pair/validation receipts. Root read all four exact historical '
    'rows, both adjacent gaps and the exact standing-domain and A.5.3 inputs. The bounded '
    'historical owner is the fully read original; its twenty-one-row Programs text is '
    'byte-identical to the complete table previously read by root and bound here. Root also '
    'read both complete current twenty-three/twenty-five-row Programs tables. Root actually '
    'viewed and read all of Mumford p.6, the Milnor title page and Lojasiewicz p.464; the '
    'checker primary receipts retain their separate broader reading scope. The first '
    'oversized root output was truncated; the full final index, both proof blocks and '
    'comparison were then separately reopened in full. A truncated Programs output was '
    'likewise replaced by separate complete table reads before this attestation. The '
    'finite-duality/conductor maps, principal divisor and diagonal weighted identities, '
    'minimal-resolution adjunction, analytic f=h^m map, boundary transport and oriented '
    'normal bundle establish the retained conclusions. The exact Q(i) coordinate inverse '
    'and north/south intersections identify the sphere with E_minus-E_plus in the n=1 '
    'compactification. The initial postrelease n=2 association remains recorded and corrected; '
    'the frozen bytes remain unchanged. D_h maps to D_str by the identity on Div(T), not by '
    'identifying either divisor with zero. In the final v2, localization gives '
    'B tensor_A Q(A)=Q(A); evaluation at1 and multiplication are inverse conductor maps '
    'for all analytic branches. This corrects newly proposed v1 wording before any '
    'canonical application and preserves the original printed finite-duality claim. '
    'Root read the full v2 changed guard, all remaining guard metadata and all three v2 '
    'events; the other six literal guards and both bibliography/Programs pairs are '
    'exactly the already-read v1 bytes. Root makes no extra independent-check or '
    'computation claim and no PaperII rendered-page reading claim.'
)
reading_path = 'records/S6_SERIES_PUBLISH_II_YI_root_reading_01.json'
write(reading_path, dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    source=source_binding, scope=scope, bound_inputs=inputs, actual_root_primary_images=root_images,
    program_table_full_pair=program_pair, mathematical_events_added=0,
    canonical_mutations=0, paper_II_rendered_page_credit=0))
target = dict(tag='02YI', statement_owner='night:P4R.6', checker='ii_check_a',
    freeze_receipt=bound(fp), release_receipt=bound(rp), frozen_derivation=bound(freeze['frozen_derivation_path']),
    original_full_block=original, proposed_full_block=proposed,
    actual_complete_original_proof_read=True, actual_complete_proposed_proof_read=True,
    comparison='All four complete proof items and their exact divisor, fibre, intersection and coordinate maps compared with the frozen derivation; the additive record correction is bound.',
    full_comparison=ix['comparison'], comparison_precision=bound(precision), guards=guards,
    mathematical_statement_unchanged=True, statement_precision=block['statement_precision'],
    scope_repairs=[], proof_repairs=[])
proposal = 'records/S6_SERIES_PUBLISH_II_YI_reviewed_proposals.json'
write(proposal, dict(paper='II', targets=[target], bibliography_guards=bibliography,
    root_reading=bound(reading_path), root_reading_scope=scope, bound_inputs=inputs,
    program_table_binding=bound(code_binding_path)))
ev = read(ix['event_proposals']['path'])
assert len(ev['events']) == 3
ev['root_binding'] = dict(original_events=ix['event_proposals'], root_reading=bound(reading_path),
    comparison_precision=bound(precision), code_and_programs=bound(code_binding_path),
    events_unchanged=True, additional_independent_or_computation_events=0)
events = 'records/S6_SERIES_PUBLISH_II_YI_reviewed_event_proposals.json'
write(events, ev)
config = 'records/S6_SERIES_PUBLISH_II_YI_prepare_config.json'
write(config, dict(proposal=bound(proposal), source_before_sha256=source_binding['sha256'],
    root_actual_complete_pairs_read=True, root_review_scope=scope,
    output='records/S6_SERIES_PUBLISH_II_YI_editorial_guard.json', extra_guards=[extra],
    expected_patch_count=10, mathematical_statement_and_values_unchanged=True))
print(json.dumps(dict(proposal=bound(proposal), events=bound(events), prepare_config=bound(config),
    root_reading=bound(reading_path), code_and_programs=bound(code_binding_path),
    owner_edits=7, bibliography_edits=2, program_edits=1), indent=2))
