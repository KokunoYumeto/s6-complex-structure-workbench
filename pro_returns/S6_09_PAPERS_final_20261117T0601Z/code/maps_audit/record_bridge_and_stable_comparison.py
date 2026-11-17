"""Append exact review and semantic-output evidence; preserve all prior events."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / 'deliverables/work/maps_audit'
META = dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17')

bridge = ROOT / 'deliverables/work/root/F_spin_bridge_repair.tex'
event = dict(
    event_id='maps-independent-F-spin-bridge-20261117',
    results=['MAPS:F.2.10'],
    source=str(bridge.relative_to(ROOT)),
    source_sha256=hashlib.sha256(bridge.read_bytes()).hexdigest(),
    source_line_count=len(bridge.read_text().splitlines()),
    checking_agent='/root/maps_audit',
    review_kind='Independent complete mathematical reading and rederivation by a separate AI agent; not a human review',
    scope='Only the complete newly printed primitive exterior-square bridge, not a claim of an independent read of the entire receiving F.2.10 proof.',
    outcome='Passed after two explicit elementary precisions, now present in the hashed final text.',
    checks=[
        'Preservation of omega squared gives determinant one on E; determinant of the exterior square is (det g)^3, so the primitive five-dimensional action lands in SO.',
        'The exterior-square infinitesimal equations annihilate every off-diagonal coefficient and then every diagonal coefficient; both Lie algebras have dimension ten.',
        'Orthogonal elimination by reflections and paths through nonisotropic vectors prove connectedness of complex SO(5); an open subgroup of a connected group is the whole group.',
        'Identity on all decomposable bivectors fixes every two-plane and hence every line; the kernel is precisely the two scalars plus and minus identity.',
        'A lift of an order-m element has mth power in the kernel, hence finite order dividing 2m and is semisimple over C.',
        'The displayed symplectic transvection sends primitive basis vector 3 to minus vector 1 and vector 4 to vector 2, and annihilates the other three under T-I.',
        'For orthogonal type (2,2,1), N squared is zero, N adjoint is minus N, image N is an isotropic plane, and kernel N is its orthogonal complement.',
        'A Witt decomposition reduces N to a nonzero alternating form in dimension two; the residual line sign makes the initial identification determinant one, and the GL(2)/inverse-transpose change has determinant one.',
        'Surjectivity lifts the unique SO conjugacy class; its two symplectic lifts are a transvection and its negative. A sign change of a finite lift preserves its finiteness.',
        'The primitive exterior-square eigenvalues are 1, xy, x/y, y/x, and (xy)^(-1).',
    ],
    excluded_scope='No rational or integral conjugacy conclusion, classification citation, or remaining F-row proof is inferred from this review.',
    **META,
)
(WORK / 'F_spin_bridge_independent_review.json').write_text(json.dumps(event, ensure_ascii=False, indent=2) + '\n')
events_path = WORK / 'check_events.json'
events = json.loads(events_path.read_text())
if not any(e.get('event_id') == event['event_id'] for e in events):
    events.append(event)
    events_path.write_text(json.dumps(events, ensure_ascii=False, indent=2) + '\n')

record_path = WORK / 'stable_algebra_rerun_record.json'
record = json.loads(record_path.read_text())
original_dir = ROOT / 'sources/codex_workspace/courses/CG-S6/checks'
metadata_keys = {'reader', 'effort', 'date', 'source_hash_recomputed'}
for output in record['outputs']:
    current = ROOT / output['output']
    original = original_dir / current.name
    if not original.is_file():
        continue
    new_data = json.loads(current.read_text())
    old_data = json.loads(original.read_text())
    if current.name == 'ORIGINAL_COEFFICIENT_H28_CERTIFICATE.json':
        assert new_data == old_data
        output['parsed_json_identical_to_original'] = True
        output['byte_difference_explanation'] = 'The complete parsed certificate is identical; the original uses CRLF and the rerun uses LF.'
    else:
        differences = sorted(k for k in new_data.keys() | old_data.keys() if new_data.get(k) != old_data.get(k))
        assert set(differences) <= metadata_keys, differences
        output['mathematical_json_fields_identical_to_original'] = True
        output['differing_json_keys'] = differences
        output['difference_explanation'] = 'Only exact current-reader metadata and the optional-source hash-recomputation flag differ; all mathematical results and recorded checks agree.'
record['semantic_comparison_reader'] = META
record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')

ownership = WORK / 'remaining_maps_ownership_proposal.json'
data = json.loads(ownership.read_text())
if isinstance(data, dict):
    data['subsequent_parent_acceptance'] = dict(
        date='2026-11-17',
        provenance='Parent collaboration message: Accepted: root 39 F and cdp 22 E after II credit ready, you 21 B plus stable/WB dependency closure.',
        assignments={'/root': '39 F rows', '/root/cdp_audit': '22 E rows', '/root/maps_audit': '21 B rows and stable/WB dependencies'},
        original_proposal_retained=True,
    )
    ownership.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'bridge_sha256': event['source_sha256'], 'bridge_lines': event['source_line_count'], 'semantic_comparisons_added': True}, indent=2))
