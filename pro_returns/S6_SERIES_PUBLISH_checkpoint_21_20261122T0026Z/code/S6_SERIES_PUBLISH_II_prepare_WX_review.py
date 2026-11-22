"""Bind the actually read WX proof, exact guards and primary page images."""
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
index = base + 'S6_SERIES_PUBLISH_II_A_recovery_group10_WX_final_index.json'
assert bound(index)['sha256'] == '8807d766d28e312c33b59e436191d79f2c709ece2ec02ad9bd2a7d057ae808b3'
ix = read(index)
inputs = [bound(index)]
for item in ix['artifacts']:
    assert bound(item['path'])['sha256'] == item['sha256']
    assert (R / item['path']).stat().st_size == item['bytes']
    inputs.append(bound(item['path']))
fp, rp = ix['freeze_receipt'], ix['release_receipt']
assert bound(fp)['sha256'] == ix['freeze_receipt_sha256']
assert bound(rp)['sha256'] == ix['release_receipt_sha256']
freeze, release = read(fp), read(rp)
assert release['freeze_receipt_sha256'] == bound(fp)['sha256']
assert freeze['created_utc'] < release['created_utc']
inputs += [bound(fp), bound(rp), bound(freeze['frozen_derivation_path'])]
proposal = base + 'group10_WX/S6_SERIES_PUBLISH_II_A_WX_editorial_proposals.json'
events = base + 'group10_WX/S6_SERIES_PUBLISH_II_A_WX_event_proposals.json'
comparison = base + 'S6_SERIES_PUBLISH_II_A_WX_comparison.md'
d = read(proposal)
source_path = 'S6_SERIES_PUBLISH_II.tex'
assert bound(source_path)['sha256'] == '54c1fb8f58ced2d3eeb5eec31d8dbfa6d2206753cf8361b953605032f90fb8ca'
source = (R / source_path).read_text()
block, = d['blocks']
assert block['tag'] == '02WX' and block['statement_unchanged'] is False
original, proposed = bound(block['original_path']), bound(block['proposed_path'])
assert original['sha256'] == block['original_sha256']
assert proposed['sha256'] == block['proposed_sha256']
cur = (R / original['path']).read_text()
assert source.count(cur) == 1
guards = []
for g in d['guards']:
    assert g['tag'] == '02WX'
    assert sha(cur) == g['intermediate_before_sha256']
    assert cur.count(g['literal_old']) == 1
    assert cur.index(g['literal_old']) == g['offset_before']
    cur = cur.replace(g['literal_old'], g['literal_new'], 1)
    assert sha(cur) == g['intermediate_after_sha256']
    guards.append({'change_id': g['guard_id'], 'old': g['literal_old'],
                   'new': g['literal_new'], 'defect_type': '/'.join(g['defect_types']),
                   'reason': g['reason'] + ' ' + g['mathematical_transport']})
assert len(guards) == 20 and cur == (R / proposed['path']).read_text()

pair_dir = 'records/S6_SERIES_PUBLISH_II_WX_context_pairs/'
bibguards, bibpairs = [], []
for g in d['bibliography_guards']:
    key = g['key']
    old = bound(pair_dir + f'S6_SERIES_PUBLISH_II_WX_{key}_original.tex')
    new = bound(pair_dir + f'S6_SERIES_PUBLISH_II_WX_{key}_proposed.tex')
    oldtext, newtext = (R / old['path']).read_text(), (R / new['path']).read_text()
    assert oldtext.count(g['literal_old']) == 1
    assert oldtext.replace(g['literal_old'], g['literal_new'], 1) == newtext
    assert source.count(oldtext) == 1
    bibguards.append({'change_id': 'II-WX-BIB-' + key, 'statement_owner': 'bib:' + key,
                      'old': oldtext, 'new': newtext,
                      'defect_type': '/'.join(g['defect_types']),
                      'reason': g['reason'] + ' ' + g['mathematical_transport']})
    bibpairs.append({'key': key, 'original': old, 'proposed': new})
assert len(bibguards) == 2
pg = d['program_table_guard']
program_pair = {part: bound(pair_dir + f'S6_SERIES_PUBLISH_II_WX_Programs_{part}.tex')
                for part in ('original', 'proposed')}
for part, literal in [('original', 'literal_old'), ('proposed', 'literal_new')]:
    assert (R / program_pair[part]['path']).read_text() == pg[literal]
assert source.count(pg['literal_old']) == 1
extra = {'change_id': 'II-WX-PROGRAMS', 'statement_owner': 'series:II:programs',
         'old': pg['literal_old'], 'new': pg['literal_new'],
         'defect_type': '/'.join(pg['defect_types']),
         'reason': pg['reason'] + ' ' + pg['mathematical_transport']}

for path in ['records/S6_SERIES_PUBLISH_II_WX_root_reading_01.json',
             'records/S6_SERIES_PUBLISH_II_WX_prior_program_scope.json',
             'records/S6_SERIES_PUBLISH_II_WX_root_receiver_scope_01.json',
             base + 'S6_SERIES_PUBLISH_Liu_Rollenske_2012_retrieval.json',
             base + 'S6_SERIES_PUBLISH_Liu_Rollenske_2012_published.pdf']:
    inputs.append(bound(path))
milnor = read(base + 'S6_SERIES_PUBLISH_II_A_WX_Milnor_primary_reading.json')
for page in milnor['page_map']:
    assert bound(page['path'])['sha256'] == page['sha256']
actual_images = []
for viewer, printed in [(104, 111), (105, 112), (106, 113), (107, 114), (108, 115)]:
    path = base + f'Milnor1968/S6_SERIES_PUBLISH_Milnor1968_viewer_{viewer:03d}.webp'
    actual_images.append(dict(bound(path), primary='Milnor1968', printed_page=printed,
                              actual_complete_image_read_by_root=True))
actual_images.append(dict(bound(base + 'S6_SERIES_PUBLISH_Liu_Rollenske_2012_p187.png'),
                          primary='Liu--Rollenske2012', printed_page=187,
                          actual_complete_image_read_by_root=True))
assert len(read(events)['events']) == 3
assert [e['type'] for e in read(events)['events']] == [
    'targeted proof check', 'used and rechecked in this run', 'computation or formal certificate']

scope = (
    'Root actually read the complete original and final proposed seven-item owner, the entire '
    '395-line frozen derivation, the complete comparison, all twenty literal guards, both full '
    'bibliography pairs and both complete end-Programs tables, and every proposed event field. '
    'Root read both whole new programs and every output row, the complete run and primary-reading '
    'receipts, freeze/release receipts, and bounded historical-program and receiver scopes. '
    'Root actually viewed the complete published Liu--Rollenske Table1 image on printed187 and '
    'Milnor printed111--115, including complete B1--B3 proofs, B4 and the positivity proof. '
    'Milnor115 presents the free-module/colength equality as Problem3; the comparison supplies '
    'its finite-module, regular-sequence, Tor and Nakayama proof. The printed positivity theorem '
    'uses polynomial wording; the frozen derivation explicitly transports every step to the '
    'analytic gradient map. Further primary reading belongs to ii_check_a. The ambient-germ '
    'isomorphism, actual residue divisor, unit maps, full common powers and unequal component '
    'multiplicities are explicit. The final global invocation has its all-supports domain. '
    'The seven printed items and all deformation, Hessian, critical-remainder and normalization '
    'formulas are preserved. No independent credit is assigned to postrelease repairs or receiver '
    'reading, and no Paper II rendered-page credit or global defect closure is claimed.'
)
target = {
    'tag': '02WX', 'statement_owner': 'night:P4.25', 'checker': 'ii_check_a',
    'freeze_receipt': bound(fp), 'release_receipt': bound(rp),
    'frozen_derivation': bound(freeze['frozen_derivation_path']),
    'original_full_block': original, 'proposed_full_block': proposed,
    'actual_complete_original_proof_read': True,
    'actual_complete_proposed_proof_read': True,
    'comparison': 'All seven original/final proof items and their exact multiplicity, residue, coordinate and global-scope maps compared.',
    'full_comparison': bound(comparison), 'guards': guards,
    'mathematical_statement_unchanged': False,
    'scope_repairs': block['scope_repairs'], 'proof_repairs': block['proof_repairs'],
}
out = 'records/S6_SERIES_PUBLISH_II_WX_reviewed_proposals.json'
write(out, {'paper': 'II', 'targets': [target], 'bibliography_guards': bibguards,
            'bibliography_full_pairs': bibpairs, 'program_table_full_pair': program_pair,
            'bound_inputs': inputs, 'root_reading_scope': scope,
            'root_reading_completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()})
root_reading = 'records/S6_SERIES_PUBLISH_II_WX_root_reading_02.json'
write(root_reading, {'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    'scope': scope, 'proposal': bound(out), 'event_proposals': bound(events),
                    'bound_inputs': inputs, 'actual_primary_images': actual_images,
                    'bibliography_full_pairs': bibpairs, 'program_table_full_pair': program_pair,
                    'mathematical_events_added': 0, 'paper_II_rendered_page_reading_credit': 0})
cfg = 'records/S6_SERIES_PUBLISH_II_WX_prepare_config.json'
write(cfg, {'proposal': bound(out), 'source_before_sha256': bound(source_path)['sha256'],
            'root_actual_complete_pairs_read': True, 'root_review_scope': scope,
            'output': 'records/S6_SERIES_PUBLISH_II_WX_editorial_guard.json',
            'extra_guards': [extra], 'expected_patch_count': 23,
            'mathematical_statement_and_values_unchanged': False})
print(json.dumps({'proposal': bound(out), 'events': bound(events),
                  'prepare_config': bound(cfg), 'root_reading': bound(root_reading),
                  'literal_owner_edits': len(guards), 'bibliography_edits': 2,
                  'program_table_edits': 1, 'root_actual_primary_images': 6}, indent=2))
