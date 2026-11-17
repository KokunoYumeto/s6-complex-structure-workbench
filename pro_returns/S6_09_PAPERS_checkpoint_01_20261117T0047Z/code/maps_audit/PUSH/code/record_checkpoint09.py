#!/usr/bin/env python3
"""Verify every archived byte and record the ninth immutable checkpoint save."""
from pathlib import Path
import csv, datetime, hashlib, io, json, re, sys, zipfile
import fitz

root = Path(__file__).resolve().parents[1]
identifier, tag = sys.argv[1:3]
assert re.fullmatch(r'[A-Za-z0-9_-]+', identifier)
archive = root.parent/'S6_02_PUSH_checkpoint_09.zip'
log = root.parent/'checkpoint09_package.out'
expected = re.search(r'sha256 ([0-9a-f]{64})', log.read_text()).group(1)
actual = hashlib.sha256(archive.read_bytes()).hexdigest()
assert actual == expected
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    prefix = root.name+'/'
    manifest = json.loads(z.read(prefix+'code/checkpoint_manifest_09.json'))
    created = datetime.datetime.fromisoformat(manifest['created_utc'])
    assert created >= datetime.datetime(2026,11,15,21,38,56,tzinfo=datetime.timezone.utc)
    for row in manifest['files']:
        data = z.read(prefix+row['path'])
        assert len(data) == row['bytes']
        assert hashlib.sha256(data).hexdigest() == row['sha256']
    rows = list(csv.DictReader(io.StringIO(z.read(prefix+'S6_02_PUSH_results.csv').decode())))
    pdf = fitz.open(stream=z.read(prefix+'S6_02_PUSH_paper.pdf'),filetype='pdf')
    audit = json.loads(z.read(prefix+f'code/deliverable_audit_{tag}.json'))
    assert audit['passed'] and len(rows) == audit['registry_rows']
    qa = json.loads(z.read(prefix+f'qa/{tag}/visual_inspection.json'))
    assert not qa['observed_issues'] and len(pdf) == qa['pdf_pages']
    assessment = json.loads(z.read(prefix+'code/progress_assessment_09.json'))
    assert assessment['decision'] == 'CONTINUE'
    retained = len(json.loads(z.read(prefix+'code/retention_record.json')))
    count, pages = len(z.infolist()), len(pdf)
record = {
    'checkpoint':9, 'archive':archive.name, 'sha256':actual,
    'bytes':archive.stat().st_size, 'files':count,
    'library_file_id':identifier, 'status':'saved_and_integrity_verified',
    'created_utc':manifest['created_utc'],
    'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'build':tag, 'pdf_pages':pages, 'statement_rows':len(rows),
    'bibliography_entries':audit['bibliography_entries'],
    'visually_inspected_pages':len(qa['visually_inspected_pages']),
    'retained_changed_versions':retained,
    'next_checkpoint_due_utc':'2026-11-15 22:38:56 UTC'
}
(root/'code'/'checkpoint09_saved.json').write_text(json.dumps(record,indent=2)+'\n')
(root/'code'/'checkpoint09_package.out').write_bytes(log.read_bytes())
p = root/'checkpoints.md'
s = p.read_text()
assert '| 09 |' not in s
row = (f'| 09 | {archive.name} | {identifier} | Saved after the ninth hour; '
       f'{count} files; {archive.stat().st_size:,} bytes; archive SHA-256 {actual}. |')
at = s.index('\n\nThe first archive')
s = s[:at]+'\n'+row+s[at:]
stamp = created.strftime('%H:%M:%S UTC')
summary = (f'The ninth checkpoint was assembled at {stamp}, after the 21:38:56 UTC deadline, and saved with full integrity verification. '
           f'It contains the clean {pages}-page {tag} PDF, {len(rows)} statements, {audit["bibliography_entries"]} bibliography entries, '
           f'a passing integration audit and a {len(qa["visually_inspected_pages"])}-page visual sample. '
           f'All {retained} changed historical versions are retained. Every archived manifest byte count and SHA-256 digest and the ZIP CRCs were verified. '
           'The ninth-hour assessment is CONTINUE. The next checkpoint and assessment are due at 22:38:56 UTC. Earlier archives remain unchanged.')
s += '\n\n'+summary+'\n'
p.write_text(s)
p = root/'code'/'refresh_report.py'
s = p.read_text().replace('Checkpoint09 is scheduled for 21:38:56 UTC and is not created earlier.', summary)
p.write_text(s)
print(json.dumps(record,indent=2))
