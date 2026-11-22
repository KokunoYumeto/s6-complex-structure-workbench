"""Bind the actually read Y2 proof and rebase its Programs row exactly."""
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
index = base + 'S6_SERIES_PUBLISH_II_A_recovery_group11_Y2_final_index.json'
assert bound(index)['sha256'] == 'a6a0a2d11c26db2126d9608fc531c6e10dc79ec9cba36a68bf8c239fd1b94736'
ix = read(index)
inputs = [bound(index)]
for item in ix['files']:
    assert bound(item['path'])['sha256'] == item['sha256']
    assert (R / item['path']).stat().st_size == item['bytes']
    inputs.append(bound(item['path']))
fp = 'agents/ii_infra/derivation_freezes/02Y2/20261121T230417020856Z/S6_SERIES_PUBLISH_derivation_freeze_receipt.json'
rp = 'agents/ii_infra/released_proofs/02Y2/7cbacc27defe4a41/S6_SERIES_PUBLISH_release_receipt.json'
freeze, release = read(fp), read(rp)
assert release['freeze_receipt_sha256'] == bound(fp)['sha256']
assert freeze['created_utc'] < release['created_utc']
assert bound(freeze['frozen_derivation_path'])['sha256'] == freeze['derivation_sha256']
inputs.append(bound(freeze['frozen_derivation_path']))
proposal = base + 'group11_Y2/S6_SERIES_PUBLISH_II_A_Y2_editorial_proposals.json'
agent_events = base + 'group11_Y2/S6_SERIES_PUBLISH_II_A_Y2_event_proposals.json'
comparison = base + 'S6_SERIES_PUBLISH_II_A_Y2_comparison.md'
d = read(proposal)
source_path = 'S6_SERIES_PUBLISH_II.tex'
assert bound(source_path)['sha256'] == '7a6483615fdb871920de3ae9f2a78da1d14f10944714149f538557425bffa6a6'
source = (R / source_path).read_text()
block, = d['blocks']
assert block['tag'] == '02Y2' and block['statement_unchanged'] is True
original, proposed = bound(block['original_path']), bound(block['proposed_path'])
assert original['sha256'] == block['original_sha256']
assert proposed['sha256'] == block['proposed_sha256']
cur = (R / original['path']).read_text()
assert source.count(cur) == 1
guards = []
for g in d['guards']:
    assert g['tag'] == '02Y2'
    assert sha(cur) == g['intermediate_before_sha256']
    assert cur.count(g['literal_old']) == 1
    assert cur.index(g['literal_old']) == g['offset_before']
    cur = cur.replace(g['literal_old'], g['literal_new'], 1)
    assert sha(cur) == g['intermediate_after_sha256']
    guards.append({'change_id': g['guard_id'], 'old': g['literal_old'],
                   'new': g['literal_new'], 'defect_type': '/'.join(g['defect_types']),
                   'reason': g['reason'] + ' ' + g['mathematical_transport']})
assert len(guards) == 10 and cur == (R / proposed['path']).read_text()

pair_dir = 'records/S6_SERIES_PUBLISH_II_Y2_context_pairs/'
bibguards, bibpairs = [], []
for g in d['bibliography_guards']:
    key = g['key']
    old = bound(pair_dir + key + '_original.tex')
    new = bound(pair_dir + key + '_proposed.tex')
    oldtext, newtext = (R / old['path']).read_text(), (R / new['path']).read_text()
    assert oldtext == g['literal_old'] and newtext == g['literal_new']
    assert source.count(oldtext) == 1
    bibguards.append({'change_id': 'II-Y2-BIB-' + key, 'statement_owner': 'bib:' + key,
                      'old': oldtext, 'new': newtext,
                      'defect_type': '/'.join(g['defect_types']),
                      'reason': g['reason'] + ' ' + g['mathematical_transport']})
    bibpairs.append({'key': key, 'original': old, 'proposed': new})
assert len(bibguards) == 2
pg = d['program_table_guard']
program_pair = {part: bound(pair_dir + f'programs_{part}.tex')
                for part in ('original', 'proposed')}
oldtable, newtable = ((R / program_pair[p]['path']).read_text()
                      for p in ('original', 'proposed'))
end = '\\end{longtable}'
assert pg['literal_old'].endswith(end) and pg['literal_new'].endswith(end)
assert pg['literal_new'].startswith(pg['literal_old'][:-len(end)])
addition = pg['literal_new'][len(pg['literal_old']) - len(end):-len(end)]
assert newtable == oldtable[:-len(end)] + addition + end
assert source.count(oldtable) == 1
assert oldtable.count('\\href{') == 14 and newtable.count('\\href{') == 15
inputs.append(bound(pair_dir + 'rebase_receipt.json'))
extra = {'change_id': 'II-Y2-PROGRAMS', 'statement_owner': 'series:II:programs',
         'old': oldtable, 'new': newtable, 'defect_type': '/'.join(pg['defect_types']),
         'reason': pg['reason'] + ' ' + pg['mathematical_transport'] +
                   ' Exact rebase preserves all fourteen current rows and adds the proposed row.'}

ev = read(agent_events)
assert len(ev['events']) == 3
assert [e['type'] for e in ev['events']] == [
    'targeted proof check', 'used and rechecked in this run', 'computation or formal certificate']
old_claim = 'Formal affine exponent arithmetic for symbolicm proves d(z^m)/z^m=m z^-1 dz, matching the explicit positively oriented circle parametrization.'
new_claim = ('The Laurent calculation takes the derivative-rule coefficient m and exponent m−1 as inputs '
             'and checks exponent cancellation (m−1)+(−m)=−1; it does not implement differentiation. '
             'The explicit positively oriented circle parametrization proves the winding m in the derivation.')
assert ev['events'][2]['outcome'].count(old_claim) == 1
ev['events'][2]['outcome'] = ev['events'][2]['outcome'].replace(old_claim, new_claim)
ev['root_precision'] = {'original_agent_proposal': bound(agent_events),
                        'scope': 'One computation-outcome sentence precisely scoped after reading every code/output field; agent acknowledged. No extra event.'}
events = 'records/S6_SERIES_PUBLISH_II_Y2_reviewed_event_proposals.json'
write(events, ev)

actual_images = []
for name, printed in [('S6_SERIES_PUBLISH_Lojasiewicz_1964_page-17.png', 464),
                      ('S6_SERIES_PUBLISH_Bobadilla_Kollar_2012_p85.png', 85)]:
    actual_images.append(dict(bound(base + name), printed_page=printed,
                              actual_complete_image_read_by_root=True))
scope = (
    'Root actually read the entire frozen derivation, whole original and final proposed owner, '
    'whole comparison, all ten literal edits, both complete bibliography pairs, all proposed events, '
    'whole new program and every output field, all run/freeze/release and primary-reading receipts, '
    'the bounded four-row historical program-scope record, and both complete rebased Programs tables. '
    'Root actually viewed and read the complete primary images of Lojasiewicz printed464 and '
    'Bobadilla--Kollar printed85; further main-proof image reading belongs to ii_check_a. '
    'The retraction is exactly tau r_K tau^-1; n maps to t^n, and the unit coordinate is '
    'z prime = z exp(log(v)/m). The full complement-kernel and meridian-conjugacy arguments, '
    'normal abelian subgroup and successive cyclic quotient maps remain. The polynomial '
    'convolution checks the universal barycentric identities. The Laurent calculation checks '
    'exponent cancellation with the derivative rule supplied as input; the circle proof gives '
    'winding m. This precision changes only a reviewed event copy, with the original proposal '
    'retained. No mathematical error, statement change, independent root check, PaperII '
    'rendered-page credit or global defect closure is claimed.'
)
target = {
    'tag': '02Y2', 'statement_owner': 'night:P4R.1', 'checker': 'ii_check_a',
    'freeze_receipt': bound(fp), 'release_receipt': bound(rp),
    'frozen_derivation': bound(freeze['frozen_derivation_path']),
    'original_full_block': original, 'proposed_full_block': proposed,
    'actual_complete_original_proof_read': True,
    'actual_complete_proposed_proof_read': True,
    'comparison': 'Complete original/final proof and all geometric/group maps compared with the frozen derivation.',
    'full_comparison': bound(comparison), 'guards': guards,
    'mathematical_statement_unchanged': True,
    'scope_repairs': [], 'proof_repairs': [],
}
out = 'records/S6_SERIES_PUBLISH_II_Y2_reviewed_proposals.json'
write(out, {'paper': 'II', 'targets': [target], 'bibliography_guards': bibguards,
            'bibliography_full_pairs': bibpairs, 'program_table_full_pair': program_pair,
            'bound_inputs': inputs, 'root_reading_scope': scope,
            'root_reading_completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()})
root_reading = 'records/S6_SERIES_PUBLISH_II_Y2_root_reading_01.json'
write(root_reading, {'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    'scope': scope, 'proposal': bound(out), 'event_proposals': bound(events),
                    'bound_inputs': inputs, 'actual_primary_images': actual_images,
                    'bibliography_full_pairs': bibpairs, 'program_table_full_pair': program_pair,
                    'mathematical_events_added': 0, 'paper_II_rendered_page_reading_credit': 0})
cfg = 'records/S6_SERIES_PUBLISH_II_Y2_prepare_config.json'
write(cfg, {'proposal': bound(out), 'source_before_sha256': bound(source_path)['sha256'],
            'root_actual_complete_pairs_read': True, 'root_review_scope': scope,
            'output': 'records/S6_SERIES_PUBLISH_II_Y2_editorial_guard.json',
            'extra_guards': [extra], 'expected_patch_count': 13,
            'mathematical_statement_and_values_unchanged': True})
print(json.dumps({'proposal': bound(out), 'events': bound(events),
                  'prepare_config': bound(cfg), 'root_reading': bound(root_reading),
                  'literal_owner_edits': len(guards), 'bibliography_edits': 2,
                  'program_table_edits': 1, 'root_actual_primary_images': 2}, indent=2))
