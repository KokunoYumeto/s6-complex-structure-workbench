"""Reopen two source-confirmed D20 owners and the existing P15 finding."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import io

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
source = SOURCE.read_bytes()
assert hashlib.sha256(source).hexdigest() == '178fc512258907264ab80d01e426ca269b975a0ee5bf6b005bfb5aaaeee861c2'
REVIEW = 'agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate07_new_source_findings.md'
review = (ROOT / REVIEW).read_text()
assert 'all1675 lines' in review and 'all601 original source lines' in review
now = datetime.now(timezone.utc).isoformat()

def read_table(path):
    raw = path.read_bytes()
    reader = csv.DictReader(io.StringIO(raw.decode(), newline=''), delimiter='\t')
    return raw, reader.fieldnames, list(reader)

def replace_row(raw, fields, old, new):
    def encode(value):
        stream = io.StringIO(newline='')
        csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n').writerow(value)
        return stream.getvalue().encode()
    a, b = encode(old), encode(new)
    assert raw.count(a) == 1 and b not in raw
    result = raw.replace(a, b, 1)
    assert result.replace(b, a, 1) == raw and b'\r' not in result
    return result

unit_path = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
unit_before, unit_fields, units = read_table(unit_path)
unit_after = unit_before
details = {
    'maps:src:D.2.40': 'Root read the complete1675-line original02LH statement/proof and the following Q139 remark. Actual whole-proof selected roles include the finite and cusp Q maps, fixed basis and multiplicity F, elliptic matrix and attached-space E, multiple selected Bezout/period/holonomy/roof/Chern roles, and the final oddness example. Backend is comparing the complete coordinated qualification and actual02LI period import. No paragraph-only retention or source completion is asserted.',
    'wb:sphere-metric-scaling-trichotomy': 'Root actually read complete current07 images671–677 and all601 original03DC source lines. Plain rho names a selected positive chart-exit constant and a separately selected chord-radius function. The statement limit beta also shares its plain name with the proof beta=beta_T varying-scale alias. The exact same-object qualifications, formal input domains and caller comparisons remain pending.'
}
for key, detail in details.items():
    row, = [x for x in units if (x['paper'], x['unit_id'], x['defect_type']) == ('III', key, 'D20')]
    assert row['status'] == 'done'
    old = dict(row)
    row.update(status='open', date_utc=now,
               evidence=row['evidence'] + '; ' + REVIEW,
               detail=row['detail'] + ' Reopened after current07 actual finding: ' + detail)
    unit_after = replace_row(unit_after, unit_fields, old, row)

finding_path = ROOT / 'S6_SERIES_PUBLISH_findings_III.tsv'
finding_before, finding_fields, findings = read_table(finding_path)
finding, = [x for x in findings if x['id'] == 'P15']
assert finding['status'] == 'done'
old_finding = dict(finding)
finding.update(status='open', date_utc=now,
    source_resolution=finding['source_resolution'] + ' Current07 actual changed-image reading and root complete original-source readings confirm new whole-proof naming cases in02KZ,02LH and03DC. The three actual containing D20 owners are explicitly reopened. Their exact qualification/import packets and root comparison remain pending; prior complete-source statements retain only their historical scope. Paragraph/item separation supplies no rebinding exemption.',
    remaining_gate='Complete and admit the exact current07 naming packets for02KZ,02LH with its actual downstream period import, and03DC; compare every original/proposed role, typed formal input and inverse. Then reconcile actual used-event counts, accepted current/legacy builds and all changed-page images. Final layout/provenance and joint-series gates remain separate; no new independent-proof credit.',
    evidence=finding['evidence'] + '; ' + REVIEW + '; code/S6_SERIES_PUBLISH_c9_candidate07_KZ_reopen.out')
finding_after = replace_row(finding_before, finding_fields, old_finding, finding)
assert unit_path.read_bytes() == unit_before
assert finding_path.read_bytes() == finding_before
assert SOURCE.read_bytes() == source
unit_path.write_bytes(unit_after)
finding_path.write_bytes(finding_after)
assert unit_path.read_bytes() == unit_after and finding_path.read_bytes() == finding_after
print('UTC', now)
print('Actual D20 done -> open:', list(details))
print('Actual supplied finding P15 done -> open; prior evidence retained.')
print('Paper III unit statuses:', dict(Counter(x['status'] for x in units if x['paper'] == 'III')))
print('All bytes outside these three exact rows preserved; source unchanged.')
print('No event, count, build-status, required-check or derived-record write.')
