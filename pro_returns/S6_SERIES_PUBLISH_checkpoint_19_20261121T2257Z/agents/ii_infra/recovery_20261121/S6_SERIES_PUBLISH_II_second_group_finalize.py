#!/usr/bin/env python3
"""Bind new recovery comparisons to the exact durable prereading evidence.

This writes only the agent's new recovery records. It never appends events,
changes the source, or attributes a historical hash to reconstructed bytes.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'agents/ii_infra/recovery_20261121'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def bind(path):
    path = ROOT / path if not isinstance(path, Path) else path
    return {'path': str(path.relative_to(ROOT)), 'sha256': digest(path),
            'bytes': path.stat().st_size}

def save(name, data):
    path = OUT / name
    with path.open('x') as stream:
        json.dump(data, stream, indent=2, ensure_ascii=False)
        stream.write('\n')
    return bind(path)

now = datetime.now(timezone.utc).isoformat()
source = ROOT / 'S6_SERIES_PUBLISH_II.tex'
source_bytes = source.read_bytes()
guard_path = OUT / 'S6_SERIES_PUBLISH_II_second_group_guards.json'
guards = json.loads(guard_path.read_text())
assert digest(guard_path) == '3287306661b04e49c006a085b0e8e3019d9d8c47166697d29c879bc3b1e5fbd2'
assert len(guards['guards']) == 21
expected = {
    '01F4': 'd346bc76eb7e8f1ab800c77cb2ba5c3a31210540d3c57e1aee5e9306efa462ed',
    '01FB': 'c83a42f27eee5f7cc395d6c99643b0e82f6c7430551b06fdb5fd649621a01e6f',
    '01F6': 'a941734caf07fcf9d776cc9ec0b37566320ead28b1abbbbc22c3e83ad9fb1206',
    '01GB': '2fb25f3687c962edfdfff78db0c5e9ef8aab292d1c83d805a3c3d6ac676e7672',
}
checks = []
for tag, expected_hash in expected.items():
    paths = list((ROOT / 'agents/ii_infra/derivation_freezes' / tag).glob('*/S6_SERIES_PUBLISH_derivation_freeze_receipt.json'))
    paths = [path for path in paths if digest(path) == expected_hash]
    assert len(paths) == 1, tag
    freeze_path = paths[0]
    freeze = json.loads(freeze_path.read_text())
    frozen_path = ROOT / freeze['frozen_derivation_path']
    assert digest(frozen_path) == freeze['derivation_sha256']
    release_path = ROOT / 'agents/ii_infra/released_proofs' / tag / expected_hash[:16] / 'S6_SERIES_PUBLISH_release_receipt.json'
    release = json.loads(release_path.read_text())
    assert release['freeze_receipt_sha256'] == expected_hash
    assert release['derivation_sha256'] == digest(frozen_path)
    assert datetime.fromisoformat(freeze['created_utc']) < datetime.fromisoformat(release['created_utc'])
    original_released = ROOT / release['full_owning_block_path']
    assert digest(original_released) == release['full_owning_block_sha256']
    block = next(row for row in guards['blocks'] if row['tag'] == tag)
    before = ROOT / block['original_full_block']
    after = ROOT / block['proposed_full_block']
    assert digest(before) == block['original_full_block_sha256']
    assert digest(after) == block['proposed_full_block_sha256']
    assert source_bytes.count(before.read_bytes()) == 1
    checks.append({
        'tag': tag, 'statement_id': block['statement_id'],
        'freeze_receipt': bind(freeze_path), 'frozen_derivation': bind(frozen_path),
        'release_receipt': bind(release_path), 'original_released_owning_block': bind(original_released),
        'current_original_full_block': bind(before), 'proposed_full_block': bind(after),
        'current_original_unique': True,
        'actual_complete_frozen_derivation_reread_after_restore': True,
        'actual_complete_original_and_proposed_statement_proof_read_after_restore': True,
        'actual_each_printed_step_comparison': True,
        'prereading_evidence_exactly_restored': True,
        'new_comparison_has_current_recovery_date': True,
        'preservation': {key: value for key, value in block.items() if key.startswith('all_') or key.startswith('named_')},
        'guard_ids': block['guard_ids'],
        'scope': ('Explicit smooth-ambient correction; broader singular interpretation is not established. Receiving statements and root front-context testimony bound below.' if tag == '01F4' else
                  'Exact named hypotheses and cited-input scope in the frozen derivation; all additional printed steps compared in the new recovery narrative.'),
    })

f9 = next(row for row in guards['blocks'] if row['tag'] == '01F9')
for key in ['original_full_block', 'proposed_full_block']:
    assert digest(ROOT / f9[key]) == f9[key + '_sha256']
assert source_bytes.count((ROOT / f9['original_full_block']).read_bytes()) == 1

evidence = [
    bind(OUT / 'S6_SERIES_PUBLISH_II_second_group_comparison.md'),
    bind(OUT / 'S6_SERIES_PUBLISH_II_second_group_exact.py'),
    bind(OUT / 'S6_SERIES_PUBLISH_II_second_group_exact_output.json'),
    bind(OUT / 'S6_SERIES_PUBLISH_II_C31_incoming_uses.json'),
    bind(OUT / 'S6_SERIES_PUBLISH_II_C31_scope_definitions.json'),
    bind(OUT / 'S6_SERIES_PUBLISH_II_C31_scope_definitions.tex'),
    bind('agents/ii_infra/primary_inputs/S6_SERIES_PUBLISH_C31_classification_primary_receipt.json'),
    bind('agents/ii_infra/S6_SERIES_PUBLISH_II_first_four_method_addendum_v2.json'),
    bind('agents/ii_infra/S6_SERIES_PUBLISH_II_first_four_method_addendum.md'),
]
receiver_files = [bind(path) for path in sorted(OUT.glob('S6_SERIES_PUBLISH_II_C31_incoming_uses_receiver_*_statement.tex'))]
comparison = {
    'created_utc': now,
    'checker': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode | restore_build',
    'recovery': {
        'restored_checkpoint': 14,
        'durable_prereading_freezes_and_releases': 'Exact bytes verified for all four original checks.',
        'missing_post_checkpoint_records': 'Historical final guards/comparison/computation are absent; this is a new actual comparison and new execution.',
        'historical_missing_final_guard_hash_for_identification_only': guards['historical_final_guard_sha256_missing'],
        'no_historical_timestamp_or_bytes_reconstructed_as_original': True,
        'hopf_and_fourth_group_independent_credit': 'Held; not included here.',
        'preflight_path_correction': 'The first run stopped before any output at an incorrect _v2.md name; the restored v2 JSON binds the existing unversioned Markdown file, whose hash was verified before retry.',
    },
    'current_source': bind(source),
    'guards': bind(guard_path), 'guard_count': 21,
    'status': 'UNAPPLIED proposals; root review and final applied-block binding required',
    'checks': checks,
    'editorial_only_additional_owner': {
        'tag': '01F9', 'statement_id': 'cdp:st:C.3.3',
        'original_full_block': bind(ROOT / f9['original_full_block']),
        'proposed_full_block': bind(ROOT / f9['proposed_full_block']),
        'complete_original_and_proposed_block_actually_read': True,
        'strong_every_element_single_commutator_claim_preserved': True,
        'source_of_mathematical_evidence': evidence[-2],
        'program_identity_method_and_execution_count_relocated_to_single_end_table': True,
        'additional_independent_event_proposed': False,
    },
    'program_table_full_comparison': {key: bind(ROOT / guards['program_table'][key]) for key in ['original_full_block', 'proposed_full_block']},
    'program_table_complete_before_and_after_actually_read': True,
    'evidence': evidence,
    'receiver_statement_archives': receiver_files,
    'front_context_review': {
        'root_actual_review_reported_in_parent_messages': True,
        'scope': 'Main B outline and B-to-A uses retain the same smooth main-B hypotheses.',
        'lost_historical_root_audit_hash_identification_only': '972ab36e08aee30def9162485cb6d6ab93df28be66b172a48ce2857487e7f185',
        'fresh_receiver_proof_reading_claimed': False,
    },
    'fresh_computation': {
        'method': 'Fraction-valued Chern-root polynomial dictionaries, exact root restriction, Poincare Euler coefficients, Leray cohomology and finite-length arithmetic.',
        'old_check_program_imported': False, 'sympy_used': False,
        'historical_run_recreated': False, 'new_execution_receipt': evidence[2],
    },
    'mathematical_events_added': 0, 'canonical_files_modified': False,
    'distinct_owner_proposals': 4,
    'deduplication': 'Same four owner/evidence-group identities as the historical second group; never count a recovery copy in addition to an accepted copy.',
}
comparison_bind = save('S6_SERIES_PUBLISH_II_second_group_comparison.json', comparison)
events = []
for item in checks:
    events.append({
        'paper': 'II', 'statement_id': item['statement_id'], 'tag': item['tag'],
        'date': now[:10], 'who': comparison['checker'] + ' | S6_SERIES_PUBLISH continuation',
        'type': 'targeted proof check',
        'evidence_group': 'S6_SERIES_PUBLISH_II_INFRA_' + item['tag'],
        'outcome': 'Durable before-release derivation hash verified; complete original/proposed proof actually reread and every step compared after restoration; new exact computational checks completed. Proposed publication/scope guards await root approval and application.',
        'scope': item['scope'],
        'freeze_receipt': item['freeze_receipt'],
        'release_receipt': item['release_receipt'],
        'frozen_derivation': item['frozen_derivation'],
        'comparison_receipt': comparison_bind,
        'current_original_full_block': item['current_original_full_block'],
        'proposed_full_block': item['proposed_full_block'],
        'different_method_computations': [evidence[1], evidence[2]],
        'proposal_only': True, 'required_final_applied_block_binding': True,
        'do_not_duplicate_historical_same_owner_credit': True,
        'recovery_timestamp': now,
    })
event_bind = save('S6_SERIES_PUBLISH_II_second_group_event_proposals.json', {
    'created_utc': now, 'status': 'Root review only; no ledger append',
    'events': events, 'one_proposal_per_distinct_owner': True,
    'mathematical_events_added_by_this_file': 0, 'canonical_ledger_modified': False,
    'source_sha256_at_binding': digest(source),
    'recovery_does_not_create_duplicate_credit': True,
})
print(json.dumps({'comparison': comparison_bind, 'event_proposals': event_bind,
                  'guards': bind(guard_path), 'count': len(events)}, indent=2))
