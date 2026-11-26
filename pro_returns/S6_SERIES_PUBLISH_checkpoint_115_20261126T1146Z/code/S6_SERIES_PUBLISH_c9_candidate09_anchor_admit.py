"""Admit the reviewed one-line 02LI opening reservation and one defect record."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json

ROOT = Path(__file__).resolve().parents[1]
STEM = ROOT / 'agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_candidate09_anchor'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
DEFECTS = ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv'
old_source = SOURCE.read_bytes()
old_defects = DEFECTS.read_bytes()
assert hashlib.sha256(old_source).hexdigest() == '75000e4890bf8ff639d74dbfcfff77f06d1a48579c02667df04a4b1b7c29a254'
proposal, = json.loads(Path(str(STEM) + '_proposals.json').read_text())
with Path(str(STEM) + '_defects.tsv').open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields = reader.fieldnames
    row, = list(reader)
assert row['change_id'] == proposal['change_id'] == 'C9-III-CANDIDATE09-ANCHOR-001'
assert row['type'] == proposal['type'] == 'D23'
assert row['statement_id'] == proposal['statement_id'] == 'maps:src:D.2.41'
assert row['old_text'] == proposal['old'] and row['new_text'] == proposal['new']
assert row['reason'] == proposal['reason']
assert proposal['new'] == '\\Needspace{6\\baselineskip}\n' + proposal['old']
assert old_source.count(proposal['old'].encode()) == 1
new_source = old_source.replace(proposal['old'].encode(), proposal['new'].encode(), 1)
assert new_source.replace(proposal['new'].encode(), proposal['old'].encode(), 1) == old_source
assert hashlib.sha256(new_source).hexdigest() == '5a95d62059fcaf7859df33f5793d9cd97462024d50a1f7ee59f9fae0b2704187'
assert old_defects.splitlines()[0].decode().split('\t') == fields
assert row['change_id'].encode() not in old_defects
with (ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv').open(newline='') as stream:
    owner, = [r for r in csv.DictReader(stream, delimiter='\t') if r['paper'] == 'III' and r['unit_id'] == row['statement_id'] and r['defect_type'] == 'D23']
assert owner['status'] == 'open'
now = datetime.now(timezone.utc).isoformat()
row['review_status'] = ('root admitted ' + now + '; root read the complete proposal/program/output/reason, affected Q140 and theorem source boundaries, and both complete actual current09 images382–383; literal full-source inverse verified; successor build/anchor/image closure pending')
stream = io.StringIO(newline='')
writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
writer.writerow(row)
new_defects = old_defects + stream.getvalue().encode()
assert new_defects.startswith(old_defects)
assert b'\r' not in new_source and b'\r' not in new_defects
assert SOURCE.read_bytes() == old_source and DEFECTS.read_bytes() == old_defects
SOURCE.write_bytes(new_source)
DEFECTS.write_bytes(new_defects)
assert SOURCE.read_bytes() == new_source and DEFECTS.read_bytes() == new_defects
print('Admitted', row['change_id'], now)
print('Source SHA-256', hashlib.sha256(new_source).hexdigest())
print('Only source and one appended exact D23 defect record changed; no event, counts or criterion closure.')
print('Root actually read complete diagnostic images382–383 and source33025–33175; no successor image credit.')
print('All original source bytes recover by deleting the sole added reservation.')
