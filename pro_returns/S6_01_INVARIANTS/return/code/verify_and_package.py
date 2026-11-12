#!/usr/bin/env python3
"""Verify the delivered ledger and records; make and check the one-file ZIP.

The manifest lists the SHA-256 digest of every member except the manifest
itself. Mathematical calculations are run by run_all.py, not by this script.
This program's retained output is outputs/package_verification.json.
"""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import re
import zipfile

import fitz

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'S6_01_INVARIANTS'
parser = argparse.ArgumentParser()
parser.add_argument('--zip', type=Path, default=ROOT.parent / (PREFIX + '.zip'))
args = parser.parse_args()
target = args.zip.resolve()
assert ROOT not in target.parents, 'The archive must be outside its input directory.'

required = [PREFIX + suffix for suffix in (
    '_paper.tex', '_paper.pdf', '_results.csv', '_references.bib', '_report.md'
)]
for name in required:
    assert (ROOT / name).is_file(), name

fields = ['id', 'statement', 'status', 'where_proved', 'depends_on',
          'item_of_the_prompt', 'findings_of_the_survey_settled (F-numbers)', 'notes']
with (ROOT / (PREFIX + '_results.csv')).open(newline='', encoding='utf-8') as stream:
    reader = csv.DictReader(stream)
    assert reader.fieldnames == fields
    rows = list(reader)
assert len(rows) == 47
assert len({row['id'] for row in rows}) == len(rows)
tex = '\n'.join(p.read_text() for p in sorted((ROOT / 'fragments').glob('part_*.tex')))
claims = re.findall(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}', tex)
assert [(row['id'], row['status']) for row in rows] == claims
statuses = Counter(row['status'] for row in rows)
assert statuses == {'Proved': 41, 'Refuted': 2, 'Known': 2, 'Open': 2}
assert {row['id'] for row in rows if row['status'] == 'Open'} == {'C3.8', 'E2.3'}

items = [f'{part}.{i}' for part, n in [('A', 4), ('B', 3), ('C', 3), ('D', 4), ('E', 2)]
         for i in range(1, n + 1)]
report = (ROOT / (PREFIX + '_report.md')).read_text(encoding='utf-8')
assert report.startswith('| Item |')
report_rows = [line.split('|')[1:-1] for line in report.splitlines()
               if re.match(r'^\| [A-E]\.\d+ \|', line)]
assert [cols[0].strip() for cols in report_rows] == items
classifications = {cols[0].strip(): cols[2].strip() for cols in report_rows}
assert Counter(classifications.values()) == {'(a)': 14, '(c)': 2}
assert {item for item, value in classifications.items() if value == '(c)'} == {'C.3', 'E.2'}
for cols in report_rows:
    if cols[2].strip() == '(c)':
        assert 'unfinished' in cols[3].lower()
coverage = {item: [row['id'] for row in rows
                  if item in row['item_of_the_prompt'].split(';')] for item in items}
assert all(coverage.values())
assert coverage == json.loads((ROOT / 'outputs/prompt_coverage.json').read_text())

bib = (ROOT / (PREFIX + '_references.bib')).read_text(encoding='utf-8')
entries = re.split(r'(?m)(?=^@\w+\{)', bib)
entries = [entry for entry in entries if entry.strip()]
keys = [re.match(r'@\w+\{([^,]+),', entry).group(1) for entry in entries]
assert len(keys) == 19 and len(set(keys)) == 19
assert all(re.search(r'note\s*=\s*\{verified:', entry, flags=re.I) for entry in entries)

reproduction = json.loads((ROOT / 'outputs/reproduction.json').read_text())
assert len(reproduction) == 15
for job in reproduction:
    assert job['returncode'] == 0, job
    assert (ROOT / job['program']).is_file(), job
    assert (ROOT / job['output']).is_file(), job
build = json.loads((ROOT / 'outputs/build_pdf.json').read_text())
assert not build['document_errors'] and not build['warnings']
assert len(build['passes']) == 4 and all(p['returncode'] == 0 for p in build['passes'])
pdf = ROOT / (PREFIX + '_paper.pdf')
with fitz.open(pdf) as document:
    assert len(document) == build['pages'] == 48
assert pdf.stat().st_size == build['pdf_bytes']
qa = json.loads((ROOT / 'outputs/pdf_qa.json').read_text())
assert qa['pages'] == 48 and not qa['extreme_boundary_blocks']
assert set(qa['claim_pages']) == {row['id'] for row in rows}
assert qa['visual_inspection'].startswith('Completed')
assert (ROOT / 'outputs/visual_review.md').is_file()
for sheet in qa['contact_sheets']:
    assert (ROOT / sheet).is_file()

main_tex = (ROOT / (PREFIX + '_paper.tex')).read_text()
for input_name in re.findall(r'\\input\{([^}]+)\}', main_tex):
    path = ROOT / input_name
    if path.suffix != '.tex':
        path = path.with_suffix('.tex')
    assert path.is_file(), input_name

record = {
    'status': 'passed', 'paper_pages': 48, 'numbered_statements': len(rows),
    'statement_statuses': dict(statuses), 'prompt_items': len(items),
    'prompt_outcomes': classifications, 'unfinished_items': ['C.3', 'E.2'],
    'verified_bibliography_entries': len(keys),
    'successful_reproduction_programs': len(reproduction),
    'clean_build': True, 'all_pages_visually_inspected': True,
    'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'scope': 'Artifact consistency and recorded execution; not independent human peer review.'
}
(ROOT / 'outputs/package_verification.json').write_text(json.dumps(record, indent=2) + '\n')

members = [ROOT / name for name in required]
members += [ROOT / 'README.md', ROOT / (PREFIX + '_paper.bbl'),
            ROOT / (PREFIX + '_paper.log')]
for folder in ['code', 'fragments', 'outputs', 'logs']:
    members += [p for p in (ROOT / folder).rglob('*') if p.is_file()
                and '__pycache__' not in p.parts and p.suffix not in {'.pyc', '.tmp'}]
members = sorted(set(members), key=lambda p: p.relative_to(ROOT).as_posix())
assert all(p.is_file() and not p.is_symlink() for p in members)
hashes = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
          for p in members}
manifest = ROOT / 'MANIFEST_SHA256.txt'
manifest.write_text(''.join(f'{digest}  {name}\n' for name, digest in hashes.items()), encoding='utf-8')
members.append(manifest)
temporary = target.with_suffix(target.suffix + '.tmp')
with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in members:
        archive.write(path, PREFIX + '/' + path.relative_to(ROOT).as_posix())
with zipfile.ZipFile(temporary) as archive:
    assert archive.testzip() is None
    assert len(archive.namelist()) == len(members)
    assert len(set(archive.namelist())) == len(members)
    for name, digest in hashes.items():
        assert hashlib.sha256(archive.read(PREFIX + '/' + name)).hexdigest() == digest, name
    assert all(name.startswith(PREFIX + '/') and '..' not in Path(name).parts
               for name in archive.namelist())
temporary.replace(target)
delivery = {
    'zip_path': str(target), 'zip_bytes': target.stat().st_size,
    'zip_sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
    'archive_members': len(members), 'archive_crc_check': 'passed',
    'all_manifest_hashes': 'passed'
}
(target.parent / (PREFIX + '_delivery.json')).write_text(json.dumps(delivery, indent=2) + '\n')
print(json.dumps(delivery, indent=2))

