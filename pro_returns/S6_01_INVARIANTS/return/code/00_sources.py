"""Inventory the supplied archive, verify its hashes, and extract PDF text.

Run from the project directory, with the extracted archive in ../background.
This performs read-only source inspection; it does not alter source documents.
"""
from pathlib import Path
import csv
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BG = ROOT.parent / 'background'
OUT = ROOT / 'outputs'
TEXT = BG / 'text'
TEXT.mkdir(exist_ok=True)
records = []
with (BG / 'MANIFEST.tsv').open() as stream:
    for row in csv.DictReader(stream, delimiter='\t'):
        path = BG / row['path_in_zip']
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        records.append({'path': row['path_in_zip'], 'bytes': path.stat().st_size,
                        'sha256': digest, 'matches_manifest': digest == row['sha256']})
for path in sorted(BG.rglob('*.pdf')):
    target = TEXT / (path.stem + '.txt')
    subprocess.run(['pdftotext', '-layout', str(path), str(target)], check=True)
    print('EXTRACTED', path.relative_to(BG), '->', target.relative_to(BG))
(OUT / 'source_hashes.json').write_text(json.dumps(records, indent=2) + '\n')
print('Verified source hashes:', sum(r['matches_manifest'] for r in records), '/', len(records))
assert all(r['matches_manifest'] for r in records)
