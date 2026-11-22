"""Bind the actually read final pairs and prepare their literal source edits."""
from pathlib import Path
import datetime
import hashlib
import json

R = Path(__file__).resolve().parents[1]
B = Path('agents/ii_infra/recovery_20261121')
def bound(p):
    p = Path(p)
    return {'path': str(p), 'sha256': hashlib.sha256((R/p).read_bytes()).hexdigest()}
def read(p):
    return json.loads((R/p).read_text())
def write(p, data):
    p = R/p
    assert not p.exists()
    p.write_text(json.dumps(data, indent=2)+'\n')

gp = B/'S6_SERIES_PUBLISH_II_SX_033C_033O_guards_v3.json'
cp = B/'S6_SERIES_PUBLISH_II_SX_033C_033O_comparison_v4.json'
ep = B/'S6_SERIES_PUBLISH_II_SX_033C_033O_event_proposals_v4.json'
g, c, e = read(gp), read(cp), read(ep)
assert bound(gp)['sha256'] == 'c6f82bfe5e1e121a8e8334ab4110e49ca41e9a85bf2606fa114d083de5239dcc'
assert bound(cp)['sha256'] == 'd861e5f25d684a1a49885a0b66f4bf262be56ebf4ffd41908119021262c4b5a7'
assert bound(ep)['sha256'] == 'a05345614078e3f99bee66b0159db9a8fb1aed2a73b6fa12d666691950985b2a'
assert bound('S6_SERIES_PUBLISH_II.tex')['sha256'] == 'd3bed8fddbb76b436c5d66e0bcc79eb07b9351b768c182187500267b86f5292d'
scope = ('Root actually read all three complete original/proposed pairs and frozen derivations, '
         'the final complete 033C v3 pair, every final literal guard, the complete comparisons, '
         'the complete Programs-table and HKP bibliography pairs, and the fresh, postrelease, '
         'pinned old-slice and Gram/Newton programs with their outputs. Primary page-image '
         'reading is credited only to the checker at its documented scope. No Paper II '
         'page-image reading is claimed.')
targets = []
for x, y in zip(g['guards'][:3], c['records']):
    assert x['tag'] == y['tag']
    f = read(y['freeze_receipt']['path'])
    targets.append(dict(tag=x['tag'], statement_owner=x['statement_id'], checker='restore_build',
        freeze_receipt=y['freeze_receipt'], release_receipt=y['release_receipt'],
        frozen_derivation={'path':f['frozen_derivation_path'], 'sha256':f['derivation_sha256']},
        original_full_block=bound(x['original_full_block']),
        proposed_full_block=bound(x['proposed_full_block']),
        guards=[dict(change_id=f"II-{x['tag']}-{i:02d}", old=z['before'], new=z['after'],
                     defect_type=z['type'], reason=z['reason'])
                for i,z in enumerate(x['literal_edits'],1)],
        comparison=y['checks'], full_comparison=bound(cp),
        actual_complete_original_proof_read=True, actual_complete_proposed_proof_read=True,
        root_actual_reading_scope=scope,
        unresolved_structural_findings=y['unresolved_findings']))
pp = Path('records/S6_SERIES_PUBLISH_II_SX_033C_033O_reviewed_proposals.json')
write(pp, dict(paper='II', targets=targets, original_guard=bound(gp),
               original_comparison=bound(cp), original_events=bound(ep),
               root_rereading_completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
               source_at_preparation=bound('S6_SERIES_PUBLISH_II.tex')))
summaries = {
 '01SX':'Independent prerelease derivation uses the permitted tangent-cohomology statement at m=12, the explicit diffeomorphism composition and the injective pullback C(t) to M(X_m). The full source comparison verifies the published HKP proof diagnosis at the cited edition; no independent credit for the upstream E15 computation is claimed.',
 '033C':'Independent prerelease derivation proves the corollary from the permitted E.2.23/E.2.24 statements by base reduction, the fibre-product map, induction along finite chains and inverse images of clopen loci. Its final proof has been fully compared. The D12 structural/owner disposition remains open and no check of the two input owners or exposed 0339 is credited.',
 '033O':'Independent prerelease derivation computes dual matrices, both rational centralizers and the integral fixed, norm and vanishing lattices with explicit coordinate maps. Complete comparison and postrelease polynomial, pinned old-slice and Gram/Newton calculations agree. The proof repair replaces inverse transpose on singular centralizer elements by the bijection C to C^t; all statement matrices and lattice values are unchanged.'}
events = []
for x in e['events']:
    z = dict(x)
    z['outcome'] = summaries[x['tag']]
    z['root_review_completed'] = True
    z['proposal_only'] = False
    events.append(z)
for x in targets:
    events.append(dict(paper='II', tag=x['tag'], statement_owner=x['statement_owner'],
        event_type='used and rechecked in this run', event_count=1,
        scope='Checker and root actually reread the complete original and final proposed statement/proof blocks, and reviewed the exact edits against the complete step comparison. '+summaries[x['tag']],
        original_full_block=x['original_full_block'], proposed_full_block=x['proposed_full_block'],
        full_comparison=bound(cp)))
evp = Path('records/S6_SERIES_PUBLISH_II_SX_033C_033O_reviewed_event_proposals.json')
write(evp, dict(events=events, original_event_proposal=bound(ep), actual_event_types=True))
extras = []
for x in g['guards'][3:]:
    extras.append(dict(change_id=x['id'], statement_owner=x['statement_id'],
        old=x['before'], new=x['after'], defect_type=x['type'], reason=x['reason']))
cfg = Path('records/S6_SERIES_PUBLISH_II_SX_033C_033O_prepare_config.json')
write(cfg, dict(proposal=bound(pp), source_before_sha256=bound('S6_SERIES_PUBLISH_II.tex')['sha256'],
    root_actual_complete_pairs_read=True, root_review_scope=scope,
    output='records/S6_SERIES_PUBLISH_II_SX_033C_033O_editorial_guard.json',
    expected_patch_count=17, mathematical_statement_and_values_unchanged=True,
    extra_guards=extras))
print(json.dumps({'proposal':bound(pp), 'events':bound(evp), 'prepare_config':bound(cfg)}))
