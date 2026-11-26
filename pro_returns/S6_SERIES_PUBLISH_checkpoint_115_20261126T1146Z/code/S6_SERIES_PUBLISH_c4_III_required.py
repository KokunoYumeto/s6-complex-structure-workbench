"""Maintain the existing III required identities and admit root-reviewed checks.

This live table records required-row states and exposure chronology. It does
not refresh inventories, aggregate check counts, completion manifests or PDFs.
The explicit admit operation follows root's mathematical reading/comparison.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv
import hashlib
import io
import json

ROOT = Path(__file__).resolve().parents[1]
LIVE = ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv'
PROPOSED = ROOT / 'agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_required_progress_proposed.tsv'
csv.field_size_limit(100000000)

def read(path, delimiter='\t'):
    with path.open(newline='') as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        return reader.fieldnames, list(reader)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def moment(value):
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    assert result.tzinfo is not None
    return result

def init():
    assert not LIVE.exists(), 'Live progress already exists; never reset it.'
    fields, rows = read(PROPOSED)
    _, candidates = read(ROOT / 'records/S6_SERIES_PUBLISH_required_check_candidates.csv', ',')
    expected = {(r['tag'], r['paper'], r['label']) for r in candidates if r['paper'] == 'III'}
    assert len(rows) == len(expected) == 128
    assert {(r['tag'], r['paper'], r['label']) for r in rows} == expected
    assert all(r['status'] == 'open' for r in rows)
    assert b'\r' not in PROPOSED.read_bytes()
    for row in rows:
        assert (ROOT / row['statement_packet']).is_file()
        if row['derivation_path']:
            path = ROOT / row['derivation_path']
            assert '_' + row['tag'] + '_' in path.name, ('Wrong target derivation', row['tag'])
            assert sha(path) == row['derivation_sha256']
        if row['proof_released_utc']:
            assert moment(row['derivation_completed_utc']) < moment(row['proof_released_utc'])
    LIVE.write_bytes(PROPOSED.read_bytes())
    PROPOSED.unlink()  # Retain one live table, not a seed snapshot beside it.
    print('Installed one live table for all 128 existing III required identities; all initially open.')

def admit(args):
    before = LIVE.read_bytes()
    fields, progress = read(LIVE)
    selected = [r for r in progress if r['tag'] == args.tag]
    assert len(selected) == 1
    row = selected[0]
    assert row['status'] == 'open'
    assert row['source_ownership_status'] == 'verified'
    assert row['alias_clause_map_required'] == 'no' or row['alias_clause_map'].strip()
    assert row['derivation_path'] and row['derivation_completed_utc']
    assert sha(ROOT / row['derivation_path']) == row['derivation_sha256']
    if args.release_utc:
        row.update(proof_released_utc=args.release_utc,
                   proof_status='released_after_derivation',
                   root_release_authorization='Explicit root authorization after review of the fixed fresh derivation; complete target proof then read by the assigned checker.')
    assert row['proof_status'] == 'released_after_derivation'
    assert moment(row['derivation_completed_utc']) < moment(row['proof_released_utc'])
    comparison = ROOT / args.comparison
    assert comparison.is_file() and args.tag in comparison.read_text()
    assert len(comparison.read_text().split()) >= 100
    index = json.loads((ROOT / 'agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_packet_structure.json').read_text())
    source_hash = sha(ROOT / 'S6_SERIES_PUBLISH_III.tex')
    assert source_hash == index['source_sha256']['III'] and source_hash in comparison.read_text()
    group = next(g for g in index['metadata_groups'] if args.tag in g['candidate_tags'])
    assert group['source_ownership_verified'] and group['source_owner'] == row['source_owner']
    row.update(released_source_sha256=source_hash, released_proof_sha256=group['proof_sha256'])
    event_fields, existing = read(ROOT / 'CHECK_EVENTS.tsv')
    proposal_fields, proposed = read(ROOT / args.events)
    assert proposal_fields == event_fields
    events = [e for e in proposed if e['event_id'] == args.event_id]
    assert len(events) == 1
    event = events[0]
    assert event['statement_id'] == row['label']
    assert event['type'] == 'targeted proof check'
    assert event['event_id'] not in {e['event_id'] for e in existing}
    assert args.comparison in event['where'] and row['derivation_path'] in event['where']
    assert moment(event['date_utc']) >= moment(row['proof_released_utc'])
    assert moment(event['date_utc']) <= datetime.now(timezone.utc)
    old_other = [dict(r) for r in progress if r['tag'] != args.tag]
    row.update(status='done', packet_status='required_check_complete',
               checker_exposure_note='Fresh derivation was written before the authorized target-proof opening; the complete printed proof was then compared. Exact chronology and source scope remain in the cited evidence.',
               check_event_id=event['event_id'], proof_comparison_evidence=args.comparison,
               completion_evidence=row['derivation_path'] + '; ' + args.comparison + '; CHECK_EVENTS.tsv event ' + event['event_id'],
               notes='Required targeted check complete. Publication rewriting, provenance, typesetting and final page reading remain at their own open rows.')
    output = io.StringIO(newline='')
    writer = csv.DictWriter(output, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader(); writer.writerows(progress)
    product = output.getvalue().encode()
    check = list(csv.DictReader(io.StringIO(product.decode()), delimiter='\t'))
    assert [r for r in check if r['tag'] != args.tag] == old_other
    append = io.StringIO(newline='')
    csv.DictWriter(append, event_fields, delimiter='\t', lineterminator='\n').writerow(event)
    ledger = ROOT / 'CHECK_EVENTS.tsv'
    original_ledger = ledger.read_bytes()
    assert original_ledger.endswith(b'\n')
    assert LIVE.read_bytes() == before
    ledger.write_bytes(original_ledger + append.getvalue().encode())
    LIVE.write_bytes(product)
    assert ledger.read_bytes().startswith(original_ledger)
    assert LIVE.read_bytes() == product
    print('Admitted', event['event_id'], 'and closed existing required III row', args.tag)
    print('All previous event bytes and every other required progress row preserved; no derived record refreshed.')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='mode', required=True)
    sub.add_parser('init')
    p = sub.add_parser('admit')
    p.add_argument('--tag', required=True)
    p.add_argument('--events', required=True)
    p.add_argument('--event-id', required=True)
    p.add_argument('--comparison', required=True)
    p.add_argument('--release-utc')
    args = parser.parse_args()
    init() if args.mode == 'init' else admit(args)

if __name__ == '__main__':
    main()
