#!/usr/bin/env python3
"""Verify every archived manifest entry and record the seventh immutable save."""
from pathlib import Path
import csv,datetime,hashlib,io,json,re,sys,zipfile
import fitz

root=Path(__file__).resolve().parents[1]
identifier=sys.argv[1]
assert re.fullmatch(r'[A-Za-z0-9_-]+',identifier)
archive=root.parent/'S6_02_PUSH_checkpoint_07.zip'
log=root.parent/'checkpoint07_package.out'
expected=re.search(r'sha256 ([0-9a-f]{64})',log.read_text()).group(1)
actual=hashlib.sha256(archive.read_bytes()).hexdigest()
assert actual==expected
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    prefix=root.name+'/'
    manifest=json.loads(z.read(prefix+'code/checkpoint_manifest_07.json'))
    for row in manifest['files']:
        data=z.read(prefix+row['path'])
        assert len(data)==row['bytes']
        assert hashlib.sha256(data).hexdigest()==row['sha256']
    rows=list(csv.DictReader(io.StringIO(z.read(prefix+'S6_02_PUSH_results.csv').decode())))
    pdf=fitz.open(stream=z.read(prefix+'S6_02_PUSH_paper.pdf'),filetype='pdf')
    assert len(rows)==134 and len(pdf)==182
    audit=json.loads(z.read(prefix+'code/deliverable_audit_draft27.json'))
    assert audit['passed'] and audit['bibliography_entries']==102
    qa=json.loads(z.read(prefix+'qa/draft27/visual_inspection.json'))
    assert not qa['observed_issues'] and len(qa['visually_inspected_pages'])==29
    retained=len(json.loads(z.read(prefix+'code/retention_record.json')))
    count=len(z.infolist())
record={'checkpoint':7,'archive':archive.name,'sha256':actual,
        'bytes':archive.stat().st_size,'files':count,
        'library_file_id':identifier,'status':'saved_and_integrity_verified',
        'created_utc':manifest['created_utc'],
        'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'pdf_pages':182,'statement_rows':134,'bibliography_entries':102,
        'retained_changed_versions':retained,
        'next_checkpoint_due_utc':'2026-11-15 20:38:56 UTC'}
(root/'code'/'checkpoint07_saved.json').write_text(json.dumps(record,indent=2)+'\n')
(root/'code'/'checkpoint07_package.out').write_bytes(log.read_bytes())
p=root/'checkpoints.md';s=p.read_text()
assert '| 07 |' not in s
row=(f'| 07 | {archive.name} | {identifier} | Saved after the seventh hour; '
     f'{count} files; {archive.stat().st_size:,} bytes; archive SHA-256 {actual}. |\n')
at=s.index('\n\nThe first archive')
s=s[:at]+'\n'+row.rstrip('\n')+s[at:]
s+=('\n\nThe seventh checkpoint was assembled and saved at approximately19:39UTC, '
    'after the19:38:56 deadline. It contains the clean182-page draft27 PDF,134 numbered statements, '
    '102 bibliography entries, a passing integration audit and a29-page visual sample. '
    'The E.2.20 cusp reconstruction working proof and independent reviews are retained separately '
    'without being counted as an integrated proved statement. Every archived file was checked '
    'against its SHA-256 manifest after saving. The seventh-hour assessment is CONTINUE. '
    'The next checkpoint and assessment are due at20:38:56UTC. Earlier archives remain unchanged.\n')
p.write_text(s)
p=root/'code'/'refresh_report.py';s=p.read_text()
s=s.replace('The next checkpoint and assessment are due at 19:38:56 UTC.',
'''The seventh checkpoint was saved at approximately19:39UTC with the clean182-page draft27 paper,134 statements,102 bibliography entries and29-page visual QA. Its complete archive passed manifest and ZIP-integrity verification. The next checkpoint and assessment are due at20:38:56UTC.''')
s=s.replace('Checkpoint07 is scheduled for 19:38:56 UTC; it is not created earlier.',
'''Checkpoint07 was saved at approximately19:39UTC after its hourly deadline. The next checkpoint is due at20:38:56UTC.''')
p.write_text(s)
print(json.dumps(record,indent=2))
