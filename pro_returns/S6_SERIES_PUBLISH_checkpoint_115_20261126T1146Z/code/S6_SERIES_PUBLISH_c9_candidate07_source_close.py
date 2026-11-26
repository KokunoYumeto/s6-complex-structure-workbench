"""Admit completed source criteria after root's complete combined comparison."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse
import csv
import hashlib
import io

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-sha', required=True)
parser.add_argument('--reviewed', required=True)
parser.add_argument('--event-id', action='append', required=True)
args = parser.parse_args()
source = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert hashlib.sha256(source).hexdigest() == args.source_sha
assert args.source_sha != '178fc512258907264ab80d01e426ca269b975a0ee5bf6b005bfb5aaaeee861c2'
review_path = 'agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate07_source_packet_review.md'
review = (ROOT / review_path).read_text()
assert 'All four whole-proof source comparisons completed' in review
now = datetime.now(timezone.utc).isoformat()

def table(name):
    path = ROOT / name
    raw = path.read_bytes()
    reader = csv.DictReader(io.StringIO(raw.decode(), newline=''), delimiter='\t')
    return path, raw, reader.fieldnames, list(reader)

def replace_row(raw, fields, old, new):
    def encode(row):
        stream = io.StringIO(newline='')
        csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n').writerow(row)
        return stream.getvalue().encode()
    a, b = encode(old), encode(new)
    assert raw.count(a) == 1 and b not in raw
    changed = raw.replace(a, b, 1)
    assert changed.replace(b, a, 1) == raw and b'\r' not in changed
    return changed

_, event_bytes, _, events = table('CHECK_EVENTS.tsv')
assert len(set(args.event_id)) == len(args.event_id) == 4
selected = [r for r in events if r['event_id'] in set(args.event_id)]
owners = {'maps:src:D.2.24', 'maps:src:D.2.40', 'maps:src:D.2.41', 'wb:sphere-metric-scaling-trichotomy'}
assert len(selected) == 4 and {r['statement_id'] for r in selected} == owners
assert len({r['evidence_group'] for r in selected}) == 3
assert all(r['type'] == r['source_event_type'] == 'used and rechecked in this run' for r in selected)

up, ub, uf, units = table('S6_SERIES_PUBLISH_unit_progress.tsv')
ua = ub
for owner in sorted(owners):
    row, = [r for r in units if (r['paper'], r['unit_id'], r['row_kind'], r['defect_type']) == ('III', owner, 'defect', 'D20')]
    assert row['status'] == 'open'
    old = dict(row)
    row.update(status='done', date_utc=now,
        evidence=row['evidence'] + '; ' + review_path,
        detail=row['detail'] + ' Source criterion completed after the exact combined candidate07 corrections: ' + args.reviewed + ' Every original/proposed scope, retained typed argument and actual caller import has its recorded object map and inverse. The four exposed owner associations retain three evidence groups. Fresh builds and actual successor-page reading remain separate gates.')
    ua = replace_row(ua, uf, old, row)

fp, fb, ff, findings = table('S6_SERIES_PUBLISH_findings_III.tsv')
finding, = [r for r in findings if r['id'] == 'P15']
assert finding['status'] == 'open'
old = dict(finding)
finding.update(status='done', date_utc=now,
    source_resolution=finding['source_resolution'] + ' All four whole-proof source comparisons completed and exact corrections admitted:02KZ,02LH,02LI and03DC. Root read each complete original/proposed scope and all final guards/reasons; the coordinated peer comparisons, exact object assignments, retained formal-input domains and literal inverses are recorded in ' + review_path + '. ' + args.reviewed,
    remaining_gate='Source naming criterion complete. Reconcile the newly admitted exposed-event counts; obtain accepted current/legacy builds and actually read all changed successor pages. D23, final provenance, records and joint-series gates remain separately open.',
    evidence=finding['evidence'] + '; ' + review_path)
fa = replace_row(fb, ff, old, finding)

bp, bb, bf, builds = table('S6_SERIES_PUBLISH_build_progress.tsv')
build, = [r for r in builds if r['paper'] == 'III']
assert build['status'] == 'done'
assert build['pdf_sha256'] == 'de3ac6c29a2794176a70a4abf0c40c4702ad27a08d2c13ea223f6b509ca98bca'
old = dict(build)
build.update(status='open', date_utc=now,
    evidence=build['evidence'] + '; ' + review_path,
    detail=build['detail'] + ' Reopened because the reviewed candidate07 correction batch changed canonical source to SHA256 ' + args.source_sha + '. The preceding current07/legacy06 acceptance remains historical; a fresh pair after exact count reconciliation and actual changed-page reading is required.')
ba = replace_row(bb, bf, old, build)

assert up.read_bytes() == ub and fp.read_bytes() == fb and bp.read_bytes() == bb
assert (ROOT / 'CHECK_EVENTS.tsv').read_bytes() == event_bytes
assert (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes() == source
up.write_bytes(ua)
fp.write_bytes(fa)
bp.write_bytes(ba)
assert up.read_bytes() == ua and fp.read_bytes() == fa and bp.read_bytes() == ba
print('UTC', now)
print('Four actual D20 owners and P15 source criterion: open -> done.')
print('III build gate: done -> open after the actual admitted source change.')
print('III unit state', dict(Counter(r['status'] for r in units if r['paper']=='III')))
print('All bytes outside these six exact rows preserved; source/events/counts/required/deposits unchanged.')
