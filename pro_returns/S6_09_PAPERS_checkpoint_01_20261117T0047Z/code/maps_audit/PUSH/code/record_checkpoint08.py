#!/usr/bin/env python3
"""Verify every archived byte and record the eighth immutable checkpoint save."""
from pathlib import Path
import csv, datetime, hashlib, io, json, re, sys, zipfile
import fitz

root = Path(__file__).resolve().parents[1]
identifier, tag = sys.argv[1:3]
assert re.fullmatch(r'[A-Za-z0-9_-]+', identifier)
archive = root.parent/'S6_02_PUSH_checkpoint_08.zip'
log = root.parent/'checkpoint08_package.out'
expected = re.search(r'sha256 ([0-9a-f]{64})',log.read_text()).group(1)
actual = hashlib.sha256(archive.read_bytes()).hexdigest()
assert actual == expected
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    prefix = root.name+'/'
    manifest = json.loads(z.read(prefix+'code/checkpoint_manifest_08.json'))
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
    assessment = json.loads(z.read(prefix+'code/progress_assessment_08.json'))
    assert assessment['decision'] == 'CONTINUE'
    retained = len(json.loads(z.read(prefix+'code/retention_record.json')))
    count = len(z.infolist())
    pages = len(pdf)
record = {
    'checkpoint':8, 'archive':archive.name, 'sha256':actual,
    'bytes':archive.stat().st_size, 'files':count,
    'library_file_id':identifier, 'status':'saved_and_integrity_verified',
    'created_utc':manifest['created_utc'],
    'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'build':tag, 'pdf_pages':pages, 'statement_rows':len(rows),
    'bibliography_entries':audit['bibliography_entries'],
    'visually_inspected_pages':len(qa['visually_inspected_pages']),
    'retained_changed_versions':retained,
    'next_checkpoint_due_utc':'2026-11-15 21:38:56 UTC'
}
(root/'code'/'checkpoint08_saved.json').write_text(json.dumps(record,indent=2)+'\n')
(root/'code'/'checkpoint08_package.out').write_bytes(log.read_bytes())
p = root/'checkpoints.md'
s = p.read_text()
assert '| 08 |' not in s
row = (f'| 08 | {archive.name} | {identifier} | Saved after the eighth hour; '
       f'{count} files; {archive.stat().st_size:,} bytes; archive SHA-256 {actual}. |')
at = s.index('\n\nThe first archive')
s = s[:at]+'\n'+row+s[at:]
created = datetime.datetime.fromisoformat(manifest['created_utc']).strftime('%H:%M:%S UTC')
summary = (f'The eighth checkpoint was assembled at{created}, after the20:38:56UTC deadline, and saved with full integrity verification. '
           f'It contains the clean{pages}-page {tag} PDF,{len(rows)} statements,{audit["bibliography_entries"]} bibliography entries, '
           f'a passing integration audit and{len(qa["visually_inspected_pages"])}-page visual sample. '
           f'All{retained} changed historical versions are retained. Every archived manifest byte count and SHA-256 digest and the ZIP CRCs were verified. '
           'The eighth-hour assessment is CONTINUE. The next checkpoint and assessment are due at21:38:56UTC. Earlier archives remain unchanged.')
s += '\n\n'+summary+'\n'
p.write_text(s)
p = root/'code'/'refresh_report.py'
s = p.read_text()
s = s.replace('Checkpoint08 is scheduled for20:38:56UTC and is not created earlier.', summary)
p.write_text(s)
print(json.dumps(record,indent=2))
