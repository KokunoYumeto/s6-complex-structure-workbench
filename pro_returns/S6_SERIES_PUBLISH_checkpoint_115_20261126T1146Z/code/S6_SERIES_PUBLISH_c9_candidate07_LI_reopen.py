"""Reopen the observed whole-proof 02LI criterion; preserve all other rows."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import io

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
SHA = '178fc512258907264ab80d01e426ca269b975a0ee5bf6b005bfb5aaaeee861c2'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SHA
csv.field_size_limit(100000000)
now = datetime.now(timezone.utc).isoformat()
evidence = 'agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate07_new_source_findings.md'

def read(name):
    path = ROOT / name
    body = path.read_bytes()
    reader = csv.DictReader(io.StringIO(body.decode()), delimiter='\t')
    rows = list(reader)
    fields = reader.fieldnames
    assert encode(fields, rows) == body
    return path, body, fields, rows

def encode(fields, rows):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode()

path, before, fields, rows = read('S6_SERIES_PUBLISH_unit_progress.tsv')
selected = [i for i,r in enumerate(rows) if (r['paper'],r['unit_id'],r['row_kind'],r['defect_type']) == ('III','maps:src:D.2.41','defect','D20')]
assert len(selected) == 1
i = selected[0]
assert rows[i]['status'] == 'done'
untouched = [dict(r) for j,r in enumerate(rows) if j != i]
rows[i]['status'] = 'open'
rows[i]['date_utc'] = now
rows[i]['evidence'] += '; ' + evidence
rows[i]['detail'] += ' Reopened after root read frozen source32970–33590, including the complete520-line02LI proof and Q140/Q141: selected torsion T/bar two-chain T(k), averaging P/free-lift matrix P, and logarithmic powers v_j/bar-list v_j need exact whole-proof qualifications. The coordinated packet must retain every map, inverse and actual LH import. Prior closure remains historical; no source or check count changes here.'
assert [r for j,r in enumerate(rows) if j != i] == untouched
after = encode(fields, rows)

fp, fb, ff, fr = read('S6_SERIES_PUBLISH_findings_III.tsv')
fi, = [j for j,r in enumerate(fr) if r['id'] == 'P15']
assert fr[fi]['status'] == 'open'
fu = [dict(r) for j,r in enumerate(fr) if j != fi]
fr[fi]['date_utc'] = now
fr[fi]['source_resolution'] += ' Additional root full520-line02LI caller reading confirms the selected T/T(k), two P maps and indexed v_j cases recorded in ' + evidence + '; its actual D20 row maps:src:D.2.41 is reopened.'
fr[fi]['remaining_gate'] += ' Include the complete02LI caller and all propagated bar-chain/averaging/list qualifications, alongside its three actual LH imports, in the whole-proof comparison and successor image check.'
assert [r for j,r in enumerate(fr) if j != fi] == fu
fa = encode(ff, fr)
assert b'\r' not in after and b'\r' not in fa
assert path.read_bytes() == before and fp.read_bytes() == fb
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SHA
path.write_bytes(after)
fp.write_bytes(fa)
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SHA
print('UTC', now)
print('Reopened actual III D20 maps:src:D.2.41 after complete520-line caller reading.')
print('P15 remains open; its existing resolution and gate are extended to this actual scope.')
print('All other unit/finding row bytes are preserved by the exact roundtrip and row comparisons.')
print('III units', Counter(r['status'] for r in rows if r['paper']=='III'))
print('Source unchanged; build/event/count/required/derived records untouched.')
