#!/usr/bin/env python3
"""Verify the immutable sixth checkpoint and record its successful save."""
from pathlib import Path
import csv, datetime, hashlib, io, json, re, sys, zipfile
import fitz

root = Path(__file__).resolve().parents[1]
identifier = sys.argv[1]
assert re.fullmatch(r'[A-Za-z0-9_-]+', identifier)
archive = root.parent / 'S6_02_PUSH_checkpoint_06.zip'
log = root.parent / 'checkpoint06_package.out'
expected = re.search(r'sha256 ([0-9a-f]{64})', log.read_text()).group(1)
actual = hashlib.sha256(archive.read_bytes()).hexdigest()
assert actual == expected
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    prefix = root.name + '/'
    manifest = json.loads(z.read(prefix + 'code/checkpoint_manifest_06.json'))
    for row in manifest['files']:
        data = z.read(prefix + row['path'])
        assert len(data) == row['bytes']
        assert hashlib.sha256(data).hexdigest() == row['sha256']
    rows = list(csv.DictReader(io.StringIO(z.read(prefix + 'S6_02_PUSH_results.csv').decode())))
    pdf = fitz.open(stream=z.read(prefix + 'S6_02_PUSH_paper.pdf'), filetype='pdf')
    assert len(rows) == 121 and len(pdf) == 159
    assert json.loads(z.read(prefix + 'code/deliverable_audit_draft23.json'))['passed']
    qa = json.loads(z.read(prefix + 'qa/draft23/visual_inspection.json'))
    assert not qa['observed_issues'] and len(qa['visually_inspected_pages']) == 22
    retained = len(json.loads(z.read(prefix + 'code/retention_record.json')))
    count = len(z.infolist())
record = {'checkpoint': 6, 'archive': archive.name, 'sha256': actual,
          'bytes': archive.stat().st_size, 'files': count,
          'library_file_id': identifier, 'status': 'saved_and_integrity_verified',
          'created_utc': manifest['created_utc'],
          'verified_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'pdf_pages': 159, 'statement_rows': 121, 'bibliography_entries': 96,
          'retained_changed_versions': retained,
          'next_checkpoint_due_utc': '2026-11-15 19:38:56 UTC'}
(root / 'code' / 'checkpoint06_saved.json').write_text(json.dumps(record, indent=2) + '\n')
(root / 'code' / 'checkpoint06_package.out').write_bytes(log.read_bytes())
p = root / 'checkpoints.md'
s = p.read_text()
assert '| 06 |' not in s
row = f'| 06 | {archive.name} | {identifier} | Saved after the sixth hour; {count} files; {archive.stat().st_size:,} bytes; archive SHA-256 {actual}. |\n'
at = s.index('\n\nThe first archive')
s = s[:at] + '\n' + row.rstrip('\n') + s[at:]
s += ('\n\nThe sixth checkpoint was assembled at approximately 18:39 UTC, after the 18:38:56 deadline, and saved at approximately 18:39 UTC. It contains the clean 159-page draft23 PDF, 121 numbered statements, 96 bibliography entries, a passing integration audit and a 22-page visual sample. The actual regular-place Hopf insertion working proof and independent referee report are retained without being counted as integrated draft23 statements. Every archived file was checked against its SHA-256 manifest after saving.\n\n'
      'The sixth-hour assessment is in code/progress_assessment_06.json and continues work because E.2 smooth-limit persistence now covers both signs and the prescribed local torus-germ construction has advanced. The next hourly checkpoint and assessment are due at 19:38:56 UTC. Earlier archives remain unchanged.\n')
p.write_text(s)
p = root / 'code' / 'refresh_report.py'
s = p.read_text().replace('The next checkpoint and assessment are due at18:38:56 UTC.',
                         'The sixth checkpoint was saved at approximately 18:39 UTC with the clean 159-page draft23 paper, 121 statements, 96 source entries and 22-page visual QA. Its complete archive passed manifest and ZIP-integrity verification. The next checkpoint and assessment are due at 19:38:56 UTC.')
s = s.replace('Checkpoint06 is scheduled for18:38:56 UTC.',
              'Checkpoint06 was saved at approximately 18:39 UTC; the next hourly checkpoint is due at 19:38:56 UTC.')
p.write_text(s)
print(json.dumps(record, indent=2))
