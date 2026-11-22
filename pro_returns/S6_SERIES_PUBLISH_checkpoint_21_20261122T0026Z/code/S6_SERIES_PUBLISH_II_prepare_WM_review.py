"""Bind the completely read WM proof pair, scope witnesses and exact edits."""
from pathlib import Path
import datetime
import hashlib
import json

R = Path(__file__).resolve().parents[1]


def sha(x):
    return hashlib.sha256(x.encode() if isinstance(x, str) else x).hexdigest()


def bound(p):
    return dict(path=p, sha256=sha((R / p).read_bytes()))


def read(p):
    return json.loads((R / p).read_text())


def write(p, d):
    p = R / p
    assert not p.exists()
    p.write_text(json.dumps(d, indent=2) + '\n')


base = 'agents/ii_checks_A/recovery_20261121T195642Z/'
index = base + 'S6_SERIES_PUBLISH_II_A_recovery_group09_WM_final_index.json'
assert bound(index)['sha256'] == '3c983a256d74ca974d98a4adfee97f99023369e6334fd648f100aa78e8bd9720'
ix = read(index)
for binding in ix['files']:
    assert bound(binding['path']) == binding
proposal = base + 'group09_WM/S6_SERIES_PUBLISH_II_A_WM_editorial_proposals.json'
events = base + 'group09_WM/S6_SERIES_PUBLISH_II_A_WM_event_proposals.json'
comparison = base + 'S6_SERIES_PUBLISH_II_A_WM_comparison.md'
d = read(proposal)
assert bound('S6_SERIES_PUBLISH_II.tex')['sha256'] == 'deed2de0d348b9644cf56307296423d59a62a5947ac7ac0ba9ba41a9ec3e42fc'
source = (R / 'S6_SERIES_PUBLISH_II.tex').read_text()
block, = d['blocks']
assert block['tag'] == '02WM' and block['statement_unchanged'] is False
original, proposed = bound(block['original_path']), bound(block['proposed_path'])
assert original['sha256'] == block['original_sha256']
assert proposed['sha256'] == block['proposed_sha256']
cur = (R / original['path']).read_text()
assert source.count(cur) == 1
guards = []
for g in d['guards']:
    assert g['tag'] == '02WM' and sha(cur) == g['intermediate_before_sha256']
    assert cur.count(g['literal_old']) == 1
    assert cur.index(g['literal_old']) == g['offset_before']
    cur = cur.replace(g['literal_old'], g['literal_new'], 1)
    assert sha(cur) == g['intermediate_after_sha256']
    guards.append(dict(change_id=g['guard_id'], old=g['literal_old'], new=g['literal_new'],
                       defect_type='/'.join(g['defect_types']),
                       reason=g['reason'] + ' ' + g['mathematical_transport']))
assert len(guards) == 10 and cur == (R / proposed['path']).read_text()
bibguards, bibpairs = [], []
for g in d['bibliography_guards']:
    old, new = bound(g['full_original_path']), bound(g['full_proposed_path'])
    assert old['sha256'] == g['original_sha256'] and new['sha256'] == g['proposed_sha256']
    assert (R / old['path']).read_text() == g['literal_old']
    assert (R / new['path']).read_text() == g['literal_new']
    assert source.count(g['literal_old']) == 1
    bibguards.append(dict(change_id='II-WM-BIB-' + g['key'], statement_owner='bib:' + g['key'],
                          old=g['literal_old'], new=g['literal_new'],
                          defect_type='/'.join(g['defect_types']),
                          reason=g['reason'] + ' ' + g['mathematical_transport']))
    bibpairs.append(dict(key=g['key'], original=old, proposed=new))
assert len(bibguards) == 3
fp = next(x['path'] for x in ix['files'] if 'derivation_freezes/02WM/' in x['path'])
rp = next(x['path'] for x in ix['files'] if 'released_proofs/02WM/' in x['path'])
freeze = read(fp)
scope = (
    'Root actually read the complete original and proposed statement and all five proof items, '
    'the entire frozen derivation, both complete preproof counterexamples, the complete final '
    'comparison and postrelease precision correction, all ten target guards and three complete '
    'bibliography pairs, and every proposed event outcome. Root read both complete new program '
    'sources and every output row: all prerelease character/cell/minor/finite-cover data, all '
    'thirty-six postrelease ruled rows, four conductor rows and the final Euler row. Root read '
    'the whole primary-scope and run receipts and the bounded receiving and historical-program '
    'association records. Primary-source page-image reading is credited to the checker. '
    'The two statement repairs require singular reduced S and confine the elliptic conductor '
    'conclusion to the last two alternatives; each has an actual preproof counterexample. '
    'The frozen summary wording is corrected by the exact finite map eta_R: six disjoint P1 '
    'curves of Euler number twelve onto the nodal hexagon R of Euler number six. Its frozen '
    'bytes and the already correct detailed witness are preserved, with no extra independent '
    'credit. No Paper II page-image reading or global defect closure is claimed.'
)
target = dict(tag='02WM', statement_owner='night:P4.15', checker='ii_check_a',
              freeze_receipt=bound(fp), release_receipt=bound(rp),
              frozen_derivation=bound(freeze['frozen_derivation_path']),
              original_full_block=original, proposed_full_block=proposed,
              actual_complete_original_proof_read=True, actual_complete_proposed_proof_read=True,
              comparison='All five original and proposed proof items, all exact maps, both refuted scopes, numerical bounds and receiving uses read and compared.',
              full_comparison=bound(comparison), guards=guards,
              mathematical_statement_unchanged=False, scope_repairs=block['scope_repairs'])
out = 'records/S6_SERIES_PUBLISH_II_WM_reviewed_proposals.json'
write(out, dict(paper='II', targets=[target], bibliography_guards=bibguards,
                bibliography_full_pairs=bibpairs, bound_inputs=[bound(index)] + ix['files'],
                root_reading_scope=scope,
                root_reading_completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
cfg = 'records/S6_SERIES_PUBLISH_II_WM_prepare_config.json'
write(cfg, dict(proposal=bound(out), source_before_sha256=bound('S6_SERIES_PUBLISH_II.tex')['sha256'],
                root_actual_complete_pairs_read=True, root_review_scope=scope,
                output='records/S6_SERIES_PUBLISH_II_WM_editorial_guard.json',
                expected_patch_count=13, mathematical_statement_and_values_unchanged=False))
print(json.dumps(dict(proposal=bound(out), events=bound(events), prepare_config=bound(cfg)), indent=2))
