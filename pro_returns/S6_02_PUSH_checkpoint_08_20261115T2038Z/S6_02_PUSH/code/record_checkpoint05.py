#!/usr/bin/env python3
"""Verify the immutable fifth checkpoint and record its successful save."""
from pathlib import Path
import csv, datetime, hashlib, io, json, zipfile
import fitz

root = Path(__file__).resolve().parents[1]
archive = root.parent / 'S6_02_PUSH_checkpoint_05.zip'
expected = 'e31c68da4616218885bbda856a9877a7d563d4dff5b473502edc856cfabb47c2'
actual = hashlib.sha256(archive.read_bytes()).hexdigest()
assert actual == expected
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    prefix = root.name + '/'
    manifest = json.loads(z.read(prefix + 'code/checkpoint_manifest_05.json'))
    for row in manifest['files']:
        data = z.read(prefix + row['path'])
        assert len(data) == row['bytes']
        assert hashlib.sha256(data).hexdigest() == row['sha256']
    rows = list(csv.DictReader(io.StringIO(z.read(prefix + 'S6_02_PUSH_results.csv').decode())))
    pdf = fitz.open(stream=z.read(prefix + 'S6_02_PUSH_paper.pdf'), filetype='pdf')
    assert len(rows) == 112 and len(pdf) == 140
    assert json.loads(z.read(prefix + 'code/deliverable_audit_draft19.json'))['passed']
    count = len(z.infolist())
identifier = 'libfile_fde3_f-ef881c41086c81919370c5e7677c9261_c6789dc4b4d481919ad633aabe6d84d0'
record = {'checkpoint': 5, 'archive': archive.name, 'sha256': actual,
          'bytes': archive.stat().st_size, 'files': count,
          'library_file_id': identifier, 'status': 'saved_and_integrity_verified',
          'created_utc': manifest['created_utc'],
          'verified_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'pdf_pages': 140, 'statement_rows': 112, 'bibliography_entries': 88,
          'retained_changed_versions': 142, 'next_checkpoint_due_utc': '2026-11-15 18:38:56 UTC'}
(root / 'code' / 'checkpoint05_saved.json').write_text(json.dumps(record, indent=2) + '\n')
log = root.parent / 'checkpoint05_package.out'
(root / 'code' / 'checkpoint05_package.out').write_bytes(log.read_bytes())
p = root / 'checkpoints.md'
s = p.read_text()
assert '| 05 |' not in s
row = f'| 05 | {archive.name} | {identifier} | Saved after the fifth hour; {count} files; 34,762,940 bytes; archive SHA-256 {actual}. |\n'
at = s.index('\n\nThe first archive')
s = s[:at] + '\n' + row.rstrip('\n') + s[at:]
s += ('\n\nThe fifth checkpoint was assembled at approximately17:39 UTC, immediately after the17:38:56 deadline, and saved at approximately17:39 UTC. It contains the clean140-page draft19 PDF,112 numbered statements,88 bibliography entries, a passing integration audit,17-page visual QA and142 retained changed versions. The separate E.2.7 and parabolic-Kato working drafts are retained without being counted as integrated draft19 statements. Every archived file was checked against its SHA-256 manifest after saving.\n\n'
      'The fifth-hour assessment is in code/progress_assessment_05.json and continues work on the actual analytic filling and smooth deformation-limit questions. The next hourly checkpoint and assessment are due at18:38:56 UTC. Earlier archives remain unchanged.\n')
p.write_text(s)
p = root / 'code' / 'refresh_report.py'
s = p.read_text().replace('The fifth hourly checkpoint is scheduled for17:38:56 UTC.',
                         'The fifth checkpoint was saved at approximately17:39 UTC with the clean140-page draft19 paper,112 statements,88 source entries,17-page visual QA and142 retained changed versions. Its complete archive passed manifest and ZIP-integrity verification. The next checkpoint and assessment are due at18:38:56 UTC.')
p.write_text(s)
print(json.dumps(record, indent=2))
