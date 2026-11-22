#!/usr/bin/env python3
"""Verify the bounded continuation rereading append without assigning new credit.

The preserved 7,866-row ledger is an exact byte prefix of the later ledger.
Only the root-reviewed, one-owner-per-row used-and-rechecked bundle may follow.
The prior check methods and evidence groups are retained byte for byte.
"""
from pathlib import Path
import csv
import hashlib
import io
import json

ROOT = Path(__file__).resolve().parents[1]
BASELINE_SHA = 'e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'
BASELINE_ROWS = 7866
REREAD_TYPE = 'used and rechecked in this run'
csv.field_size_limit(100_000_000)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def bound_read(item):
    path = (ROOT / item['path']).resolve()
    assert path.is_relative_to(ROOT), ('outside active tree', str(path))
    raw = path.read_bytes()
    assert sha(raw) == item['sha256'], ('bound file changed', item['path'])
    return raw


def table(raw):
    reader = csv.DictReader(io.StringIO(raw.decode(), newline=''), delimiter='\t')
    rows = list(reader)
    assert reader.fieldnames and len(reader.fieldnames) == len(set(reader.fieldnames))
    assert all(None not in row and None not in row.values() for row in rows)
    return reader.fieldnames, rows


def verify_append(receipt_path, ledger_path=None):
    receipt_path = Path(receipt_path).resolve()
    assert receipt_path.is_relative_to(ROOT)
    raw_receipt = receipt_path.read_bytes()
    receipt = json.loads(raw_receipt)
    assert receipt['schema_version'] == 1 and receipt['paper'] == 'I'
    assert receipt['applied'] is True and receipt['old_ledger_prefix_preserved'] is True
    before = bound_read(receipt['before_ledger'])
    assert sha(before) == BASELINE_SHA and receipt['before_rows'] == BASELINE_ROWS
    current_path = Path(ledger_path) if ledger_path else ROOT / 'CHECK_EVENTS.tsv'
    current = current_path.read_bytes()
    assert sha(current) == receipt['after_ledger_sha256']
    assert current.startswith(before) and len(current) > len(before)
    fields0, old_rows = table(before)
    fields1, current_rows = table(current)
    fields2, additions = table(bound_read(receipt['event_bundle']))
    assert fields0 == fields1 == fields2
    assert len(old_rows) == BASELINE_ROWS
    assert len(current_rows) == receipt['after_rows'] == BASELINE_ROWS + len(additions)
    assert current_rows[:BASELINE_ROWS] == old_rows
    assert current_rows[BASELINE_ROWS:] == additions and additions
    assert all(row['type'] == REREAD_TYPE for row in additions)
    owners = [row['statement_id'] for row in additions]
    assert len(owners) == len(set(owners)) and all(owners)
    ids = [row['event_id'] for row in additions]
    assert ids == receipt['appended_event_ids']
    assert len(ids) == len(set(ids)) and all(ids)
    old_ids = {row['event_id'] for row in old_rows}
    assert not old_ids.intersection(ids)
    all_ids = [row['event_id'] for row in current_rows]
    assert len(all_ids) == len(set(all_ids))
    manifest_raw = bound_read(receipt['manifest'])
    assert sha(manifest_raw) == receipt['approved_manifest_sha256']
    # The root's approval names the exact manifest and the ledger event scope.
    approval = json.loads(bound_read(receipt['approval']))
    assert approval['approved'] is True
    assert approval['manifest_sha256'] == sha(manifest_raw)
    assert approval['event_type'] == REREAD_TYPE
    assert approval['approved_event_count'] == len(additions)
    assert approval['new_independent_targeted_computation_credit'] == 0
    return {
        'receipt': {'path': str(receipt_path.relative_to(ROOT)), 'sha256': sha(raw_receipt)},
        'before_ledger_sha256': BASELINE_SHA,
        'before_rows': BASELINE_ROWS,
        'after_ledger_sha256': sha(current),
        'after_rows': len(current_rows),
        'appended_events': len(additions),
        'appended_event_type': REREAD_TYPE,
        'appended_statement_ids': owners,
        'appended_event_ids': ids,
        'old_ledger_bytes_and_rows_preserved': True,
        'new_independent_targeted_computation_credit': 0,
    }
