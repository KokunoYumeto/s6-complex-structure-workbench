#!/usr/bin/env python3
"""Recompute publication records from the verified attachment tree.

Default operation writes a dated preview under agents/continuation_infra.
Pass --apply only when the canonical record refresh is intended. Existing
programs remain unchanged, and the preview and before-copy hashes persist.
No check event is created by this administrative recomputation.
"""
from pathlib import Path
import argparse
import csv
import datetime as dt
import hashlib
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source', type=Path, default=ROOT.parent / 'S6_SERIES_PUBLISH_work')
    p.add_argument('--apply', action='store_true')
    p.add_argument('--require-identical-events', action='store_true')
    a = p.parse_args()
    stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    run = ROOT / 'agents/continuation_infra' / ('refresh_' + stamp)
    out = run / 'recomputed'
    out.mkdir(parents=True)
    inputs = sorted((ROOT / 'agents').rglob('S6_SERIES_PUBLISH*CHECK_EVENTS.tsv'))
    archived = [x for x in inputs if 'S6_SERIES_PUBLISH_I_candidate11_tail_before_locator_refresh' in x.parts]
    excluded = []
    for path in archived:
        current = path.parent.parent / path.name
        with path.open() as f:
            older = list(csv.DictReader(f, delimiter='\t'))
        with current.open() as f:
            newer = {x['event_id']: x for x in csv.DictReader(f, delimiter='\t')}
        assert {x['event_id'] for x in older} == set(newer)
        for row in older:
            for field in ['statement_id', 'date', 'who', 'type', 'evidence_group']:
                assert row[field] == newer[row['event_id']][field], (path, field)
        excluded.append(dict(path=str(path.relative_to(ROOT)), sha256=digest(path),
                             operative_bundle=str(current.relative_to(ROOT)),
                             reason='Exact event identity/type/checker/evidence-group correspondence with the operative after-binding version; retained as archive, counted once.'))
    inputs = [x for x in inputs if x not in archived]
    inputs += sorted((ROOT / 'records').glob('S6_SERIES_PUBLISH_*CHECK_EVENTS.tsv'))
    assert len(inputs) == len(set(inputs))
    source_hashes = {paper: digest(ROOT / f'S6_SERIES_PUBLISH_{paper}.tex') for paper in ['I','II','III','IV','V']}
    ledger_before = digest(ROOT / 'CHECK_EVENTS.tsv')
    cmd = [sys.executable, str(ROOT / 'agents/provenance/code/S6_SERIES_PUBLISH_recompute_records.py'),
           '--source', str(a.source.resolve()), '--output', str(out), '--tex-dir', str(ROOT)]
    for path in inputs:
        cmd += ['--extra-events', str(path)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    (run / 'recompute.out').write_text(result.stdout)
    (run / 'recompute.err').write_text(result.stderr)
    assert result.returncode == 0, result.stderr[-3000:]
    assert source_hashes == {paper: digest(ROOT / f'S6_SERIES_PUBLISH_{paper}.tex') for paper in source_hashes}, 'A source changed during recomputation.'
    assert ledger_before == digest(ROOT / 'CHECK_EVENTS.tsv'), 'The canonical event ledger changed during recomputation.'
    if a.require_identical_events:
        assert ledger_before == digest(out / 'CHECK_EVENTS.tsv'), 'Event ledger equality is required before canonical application.'
    with (out / 'S6_SERIES_PUBLISH_check_counts.tsv').open() as f:
        counts = list(csv.DictReader(f, delimiter='\t'))
    current_counts = [x for x in counts if x['scope'] == 'current_printed_statements_and_definitions']
    before = {}
    if a.apply:
        for source in sorted(out.iterdir()):
            target = ROOT / 'records' / source.name
            before[str(target.relative_to(ROOT))] = digest(target) if target.exists() else None
            shutil.copyfile(source, target)
        before['CHECK_EVENTS.tsv'] = ledger_before
        shutil.copyfile(out / 'CHECK_EVENTS.tsv', ROOT / 'CHECK_EVENTS.tsv')
    receipt = dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                   applied=a.apply, mathematical_events_added=0,
                   source_root=str(a.source.resolve()), source_sha256=source_hashes,
                   original_event_ledger_sha256=ledger_before,
                   recomputed_event_ledger_sha256=digest(out / 'CHECK_EVENTS.tsv'),
                   event_ledger_bytes_unchanged=ledger_before == digest(out / 'CHECK_EVENTS.tsv'),
                   event_bundles=[dict(path=str(x.relative_to(ROOT)), sha256=digest(x)) for x in inputs],
                   excluded_archived_event_versions=excluded, command=cmd,
                   exit_code=result.returncode, before_canonical_copy_sha256=before,
                   current_counts=current_counts,
                   summary=json.loads((out / 'S6_SERIES_PUBLISH_records_summary.json').read_text()))
    (run / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(dict(receipt=str(run / 'receipt.json'), applied=a.apply,
                          event_ledger_bytes_unchanged=receipt['event_ledger_bytes_unchanged'],
                          merged_rows=receipt['summary']['merged_rows'], current_counts=current_counts), indent=2))


if __name__ == '__main__':
    main()
