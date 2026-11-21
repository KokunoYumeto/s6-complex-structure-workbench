#!/usr/bin/env python3
"""Bind candidate15 source and counts; leave final claims/guard to certified coverage."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
from S6_SERIES_PUBLISH_I_cont_recount import recount, KINDS

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
OLD_SHA = '1f2d0d376f71e7843265976aeeb72cf8e1ff77aea176ff5dbb4e67446c25b36f'
NEW_SHA = '45bf46fc14a50f7a148cdd34bf2be68b04cd89e1cb7d620191c6e8518f7249f8'
LEDGER_SHA = 'e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bind(path):
    return {'path': str(path.relative_to(ROOT)), 'sha256': sha(path), 'bytes': path.stat().st_size}


def put(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


source = ROOT / 'S6_SERIES_PUBLISH_I.tex'
ledger = ROOT / 'CHECK_EVENTS.tsv'
before_path = OUT / 'candidate14/inputs/S6_SERIES_PUBLISH_I.tex'
receipt_path = ROOT / 'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate14_residue_receipt.json'
receipt = json.loads(receipt_path.read_text())
assert sha(before_path) == OLD_SHA == receipt['before_source_sha256']
assert sha(source) == NEW_SHA == receipt['after_source_sha256']
assert sha(ledger) == LEDGER_SHA
before = before_path.read_text()
after = source.read_text()
reconstructed = before
changes = []
for change in receipt['changes']:
    old, new = change['old'], change['new']
    assert reconstructed.count(old) == 1, change['guard_id']
    location = reconstructed.index(old)
    changes.append({
        'guard_id': change['guard_id'],
        'change_id': change['change_id'],
        'type': change['type'],
        'statement_id': change['statement_id'],
        'old': old,
        'new': new,
        'old_context': reconstructed[max(0, location-240):location+len(old)+240],
        'exact_single_occurrence_replacement_verified': True,
    })
    reconstructed = reconstructed.replace(old, new, 1)
assert reconstructed == after
assert len(changes) == 3

old_recount_path = OUT / 'candidate14/S6_SERIES_PUBLISH_I_cont_recount.json'
old_recount = json.loads(old_recount_path.read_text())
fresh = recount(ROOT, ROOT.parent / 'S6_SERIES_PUBLISH_work')
assert fresh['source_sha256'] == NEW_SHA and fresh['ledger_sha256'] == LEDGER_SHA
assert fresh['counts'] == old_recount['counts']
for key in ['selected_ledger_rows', 'selected_event_ids', 'declared_evidence_groups']:
    assert fresh[key] == old_recount[key], key
statement_keys = ['id', 'kind', 'identities']
assert [{k: s[k] for k in statement_keys} for s in fresh['statements']] == [
    {k: s[k] for k in statement_keys} for s in old_recount['statements']]
assert fresh['counts']['statements'] == 333
assert [fresh['counts'][kind] for kind in KINDS] == [767, 10, 143, 731, 194, 1]
fresh_path = OUT / 'S6_SERIES_PUBLISH_I_candidate15_recount.json'
put(fresh_path, fresh)

method_pattern = r'\\subsection\{Methodology\}\s*(.*?)\s*\\subsection\{How the paper is organized\}'
method_before = re.search(method_pattern, before, re.S)[1]
method_after = re.search(method_pattern, after, re.S)[1]
assert method_before == method_after
old_claim_path = OUT / 'candidate14/S6_SERIES_PUBLISH_I_cont_three_way_claims.json'
old_claims = json.loads(old_claim_path.read_text())
status_rows = []
for section, entries in old_claims['exact_main_status_binding'].items():
    for kind, row in entries.items():
        assert after.count(row['text']) == 1
        status_rows.append({'section': section, 'kind': kind, 'text': row['text'], 'occurrences': 1})
assert len(status_rows) == 21

result = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'paper': 'I',
    'candidate': 15,
    'source': bind(source),
    'ledger': bind(ledger),
    'candidate14_source_snapshot': bind(before_path),
    'source_edit_receipt': bind(receipt_path),
    'exact_whole_source_reconstruction_from_three_edits': True,
    'edits': changes,
    'candidate14_recount': bind(old_recount_path),
    'candidate15_recount': bind(fresh_path),
    'counts': fresh['counts'],
    'printed_statement_identity_sequence_unchanged': True,
    'selected_ledger_row_sequence_unchanged': True,
    'selected_event_id_sequence_unchanged': True,
    'declared_evidence_group_sequence_unchanged': True,
    'methodology_bytes_unchanged': True,
    'main_status_string_bindings': status_rows,
    'source_status_strings_verified': len(status_rows),
    'source_difference_review': 'Read the three exact clause deletions and their attached edit receipt. Independently reconstructed the entire candidate15 source from the archived candidate14 source using exactly those replacements, then recomputed statement identities and ledger selection from current source.',
    'final_42_claim_guard_generated': False,
    'final_42_claims_closed': False,
    'remaining_gate': 'Candidate15 PDF occurrence correspondence and certified source/PDF-bound exhaustive rendered-page coverage; then final 42-claim/deposit guard regeneration.',
    'mathematical_events_added': 0,
    'page_reading_credit_added': 0,
    'shared_files_modified': False,
}
dest = OUT / 'S6_SERIES_PUBLISH_I_candidate15_source_count_rebinding.json'
put(dest, result)
assert sha(source) == NEW_SHA and sha(ledger) == LEDGER_SHA
print(json.dumps({
    'receipt': str(dest.relative_to(ROOT)),
    'receipt_sha256': sha(dest),
    'source_sha256': NEW_SHA,
    'ledger_sha256': LEDGER_SHA,
    'exact_whole_source_reconstruction_from_three_edits': True,
    'counts': fresh['counts'],
    'source_status_strings_verified': 21,
    'final_42_claim_guard_generated': False,
    'mathematical_events_added': 0,
    'page_reading_credit_added': 0,
}, indent=2))
