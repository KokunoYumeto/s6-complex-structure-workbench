#!/usr/bin/env python3
"""Convert only CRLF row terminators; assert every decoded field unchanged."""
from pathlib import Path
import csv
import io

ROOT = Path(__file__).resolve().parents[1]
folder = ROOT / 'agents/continuation8_iii_later'
for path in sorted(folder.glob('S6_SERIES_PUBLISH_III_metrics*.tsv')):
    before = path.read_bytes()
    fields_before = list(csv.reader(io.StringIO(before.decode(), newline=''), delimiter='\t'))
    after = before.replace(b'\r\n', b'\n')
    fields_after = list(csv.reader(io.StringIO(after.decode(), newline=''), delimiter='\t'))
    assert fields_before == fields_after
    assert b'\r' not in after
    path.write_bytes(after)
    print(path.name, 'CRLF_removed', before.count(b'\r\n'), 'all_fields_unchanged', len(fields_after), 'CR_remaining', after.count(b'\r'))
print('No mathematical source changed; both metric table writers now explicitly use LF.')
