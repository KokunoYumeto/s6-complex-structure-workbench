#!/usr/bin/env python3
"""Record a dated publication-editing milestone without adding checking credit."""
from pathlib import Path
import argparse
import csv
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
parser = argparse.ArgumentParser()
parser.add_argument('--candidate', type=int, required=True)
parser.add_argument('--checkpoint', type=int, required=True)
parser.add_argument('--status-file', type=Path,
                    help='Exact current-state prose with status and pending keys.')
args = parser.parse_args()
status_input = json.loads(args.status_file.read_text()) if args.status_file else None
if status_input is not None:
    assert set(status_input) == {'status', 'pending'}
    assert all(isinstance(value, str) and value.strip() for value in status_input.values())
source = ROOT / 'S6_SERIES_PUBLISH_I.tex'
build_path = ROOT / f'build/I_candidate{args.candidate}/build_summary.json'
build = json.loads(build_path.read_text())
coverage_path = ROOT / 'records/S6_SERIES_PUBLISH_I_page_coverage.json'
coverage = json.loads(coverage_path.read_text())
assert build['source_sha256'] == coverage['source_sha256'] == sha(source)
assert build['pdf_sha256'] == coverage['pdf_sha256']
csv.field_size_limit(100_000_000)
with (ROOT / 'S6_SERIES_PUBLISH_defects_I.tsv').open() as stream:
    defects = list(csv.DictReader(stream, delimiter='\t'))
ledger = ROOT / 'PROGRESS_LEDGER.md'
progress = ledger.read_text()
types = re.findall(r'^\| I \| (D\d+): .*? \| (.*?) \|$', progress, re.M)
assert len(types) == 25
closed = [code for code, status in types if status.startswith('done')]
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
record = {
    'recorded_utc': now, 'checkpoint': args.checkpoint, 'paper': 'I',
    'candidate': args.candidate, 'source_sha256': sha(source),
    'pdf_sha256': build['pdf_sha256'], 'pages': coverage['page_count'],
    'pages_read': coverage['covered_pages'], 'missing_pages': coverage['missing_pages'],
    'coverage_record': str(coverage_path.relative_to(ROOT)),
    'coverage_record_sha256': sha(coverage_path),
    'build_summary': str(build_path.relative_to(ROOT)), 'build_summary_sha256': sha(build_path),
    'defect_log_sha256': sha(ROOT / 'S6_SERIES_PUBLISH_defects_I.tsv'),
    'logged_edits': len(defects), 'recorded_closed_types': closed,
    'recorded_open_types': [code for code, _ in types if code not in closed],
    'mathematical_ledger_sha256': sha(ROOT / 'CHECK_EVENTS.tsv'),
    'pending': status_input['pending'] if status_input else 'Complete the current contextual review, apply exact approved D08/D18 residue guards, rebuild and read every changed whole page, then bind all final evidence for the individual Paper I gate. Later papers remain queued in the prescribed order.',
    'mathematical_events_added_by_this_record': 0,
}
if args.status_file:
    record['status_input'] = {'path': str(args.status_file.resolve().relative_to(ROOT)),
                              'sha256': sha(args.status_file)}
path = ROOT / f'records/S6_SERIES_PUBLISH_continuation_checkpoint_{args.checkpoint:02}_preparation.json'
assert not path.exists()
path.write_text(json.dumps(record, indent=2) + '\n')
status = status_input['status'] if status_input else (f'Paper I candidate {args.candidate} has a clean {coverage["page_count"]}-page PDF; '
          f'{coverage["covered_pages"]} current page images have actual whole-page reading evidence. '
          f'The source has {len(defects)} logged edits. Remaining D08 prose announcements and D18 '
          'preprint-version entries are being resolved through exact source guards; the final source/PDF/ledger '
          'bindings and 42 provenance claims await the settled candidate. Paper V retains its earlier '
          'completed individual gate, and its published v2 source governs the final series review. '
          'Papers II, III and IV remain queued in that order. The full five-paper task remains incomplete.')
report_path = ROOT / 'S6_SERIES_PUBLISH_report.md'
report = report_path.read_text()
report, count = re.subn(r'(## Current gate\n\n).*?(?=\n## )', lambda m: m[1] + status + '\n', report, count=1, flags=re.S)
assert count == 1 and report.startswith('INCOMPLETE\n')
entry = (f'\n## Continuation checkpoint {args.checkpoint:02} preparation — {now}\n\n{status}\n\n'
         f'Current source: `{sha(source)}`. Current PDF: `{build["pdf_sha256"]}`. '
         f'Coverage: `{coverage["covered_pages"]}/{coverage["page_count"]}`. '
         f'The current mathematical ledger remains `{record["mathematical_ledger_sha256"]}`. '
         'The exact editorial maps and full affected-block comparisons preserve the displayed mathematical '
         'segments, labels and target sequences at their recorded scopes. The seven main theorems and forty '
         'outline claims remain byte-identical to the checked inherited candidate13 text. '
         'The completed candidate14 and candidate15 reading records are preserved; current page credit '
         'transfers only by exact complete-PNG equality. Newly found source issues remain explicit even '
         'after their pages have been read. No mathematical event is inferred from these editorial, '
         'visual or packaging operations.\n\n'
         f'The current ledger records {len(closed)} closed and {25-len(closed)} open defect types for I; '
         f'the exact status and evidence snapshot is `{path.relative_to(ROOT)}`. '
         'The checkpoint contains every restored checkpoint10 file in its current version, with new '
         'records and programs. No source or publication PDF is certified by checkpoint packaging.\n')
report_path.write_text(report + entry)
ledger.write_text(progress + entry)
print(json.dumps({'record': str(path.relative_to(ROOT)), 'sha256': sha(path), 'pages_read': coverage['covered_pages'], 'pages': coverage['page_count'], 'logged_edits': len(defects), 'open_types': 25-len(closed)}))
