"""Admit root's completed candidate05 source disposition at its exact scope."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import io
import os
import tempfile

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
REVIEW = 'agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate05_combined_source_review.md'
APPLY = 'code/S6_SERIES_PUBLISH_c9_candidate05_admission_apply.out'
NAMES = ('S6_SERIES_PUBLISH_unit_progress.tsv',
         'S6_SERIES_PUBLISH_findings_III.tsv',
         'S6_SERIES_PUBLISH_build_progress.tsv')
original = {name: (ROOT / name).read_bytes() for name in NAMES}

def parse(body):
    reader = csv.DictReader(io.StringIO(body.decode(), newline=''), delimiter='\t')
    return reader.fieldnames, list(reader)

def encode(fields, rows):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode()

review_bytes = (ROOT / REVIEW).read_bytes()
assert review_bytes and b'159 exact old/new defect rows' in review_bytes
apply_bytes = (ROOT / APPLY).read_bytes()
assert b'ROOT APPLY: 159 source rows and 4 used-and-rechecked events admitted.' in apply_bytes
source_bytes = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()
_, defects = parse((ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv').read_bytes())
packet_rows = defects[-159:]
assert len(packet_rows) == 159 and all(REVIEW in row['review_status'] for row in packet_rows)
inverse = source_bytes.decode()
for row in reversed(packet_rows):
    assert inverse.count(row['new_text']) == 1, row['change_id']
    inverse = inverse.replace(row['new_text'], row['old_text'], 1)
assert hashlib.sha256(inverse.encode()).hexdigest() == '7769c410dbc30e0171a298400d54baf75481a4c358133564fac064b9da5598f4'
_, events = parse((ROOT / 'CHECK_EVENTS.tsv').read_bytes())
event_ids = {
    'publish:c9:III:02L0:candidate05_notation',
    'ce:c9-iii-candidate05-02l4-role-reconciliation',
    'ce:c9-iii-candidate05-02lf-role-transport-reconciliation',
    'publish:c9:III:02LJ:final-rendered-bindings',
}
for identifier in event_ids:
    row, = [r for r in events if r['event_id'] == identifier]
    assert row['type'] == row['source_event_type'] == 'used and rechecked in this run'
    assert 'Source packet admitted by root' in row['outcome']
_, required = parse((ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv').read_bytes())
assert len(required) == 128 and all(row['status'] == 'done' for row in required)

uf, units = parse(original[NAMES[0]])
ff, findings = parse(original[NAMES[1]])
bf, builds = parse(original[NAMES[2]])
now = datetime.now(timezone.utc).isoformat()
subjects = {
    'maps:src:D.2.25': '02L0: all complete-proof named roles, the actual CRT covector/shear comparison, and the exact period, fan, graph and gluing maps/inverses.',
    'maps:src:D.2.29': '02L4: Smith quotient/section maps, actual boundary generators, finite-vector transport and both normal-torus parameterizations.',
    'maps:src:D.2.39': 'Whole containing section17.1: both 02LF and 02LJ complete-proof role families; physical/rank-one/cusp coordinate and Gaussian identities; the selected-cusp support binding; I2 shears; coefficient and bordism imports with their inverses.',
}
changed = []
for key, conclusion in subjects.items():
    row, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == key and r['defect_type'] == 'D20']
    assert row['status'] == 'open', key
    row.update(status='done', date_utc=now,
        evidence=row['evidence'] + '; ' + REVIEW + '; ' + APPLY,
        detail=row['detail'] + ' Root completed the recorded whole-proof source comparison and admitted the exact repair: ' + conclusion + ' Earlier source evidence is retained. Actual new-build pages and all final layout/provenance gates remain open; no independent proof credit follows.')
    changed.append((key, 'D20', 'open', 'done'))
row, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == 'night:P3F.28' and r['defect_type'] == 'D23']
assert row['status'] == 'done'
row.update(status='open', date_utc=now,
    evidence=row['evidence'] + '; ' + REVIEW + '; agents/continuation9_findings/S6_SERIES_PUBLISH_c9_candidate05_02S4_fibre_names_review.md',
    detail=row['detail'] + ' Actual candidate05 pages565–567 exposed two literal I2 and one literal IV* type names. Their exact mathematical-format repairs are admitted; the containing D23 criterion is reopened for actual new-build page inspection. The same fibres, components and maps are retained.')
changed.append(('night:P3F.28', 'D23', 'done', 'open'))
assert all(r['status'] == 'done' for r in units if r['paper'] == 'III' and r['defect_type'] == 'D20')
for key in ('P11', 'P15'):
    row, = [r for r in findings if r['id'] == key]
    assert row['status'] == 'open'
    row.update(status='done', date_utc=now,
        source_resolution=row['source_resolution'] + ' The four concrete candidate05 owners now have complete bounded source comparisons, explicit coordinate/coefficient maps and inverses, and exact admitted old/new fragments. Root accepted the recorded symbol roles through every proof and the actual LF/LJ import square. The selected-cusp rho correction is stated with its exact residual and repaired pullback. Paragraph/item separation supplies no rebinding exception. Prior full-source and retained-scope evidence remains at its recorded scope.',
        remaining_gate='Source disposition complete. The four-event count paragraph, fresh current/legacy builds, actual changed-page reading, final layout/provenance and joint-series gates remain separately open. No new final-PDF or independent-proof credit.',
        evidence=row['evidence'] + '; ' + REVIEW + '; ' + APPLY)
assert all(r['status'] == 'done' for r in findings if r['id'] not in ('P4', 'T1'))
build, = [r for r in builds if r['paper'] == 'III']
assert build['status'] == 'done'
build.update(status='open', date_utc=now,
    detail=build['detail'] + ' Candidate05 repair batch changed the canonical source after that completed pair. This build row is reopened. Its existing identity fields and prior diagnostics describe the preceding historical pair; fresh current06/legacy05 source, convergence, diagnostics, T1 and formal-anchor inspection are required.',
    evidence=build['evidence'] + '; ' + REVIEW + '; ' + APPLY)
result = {NAMES[0]: encode(uf, units), NAMES[1]: encode(ff, findings), NAMES[2]: encode(bf, builds)}
assert all(b'\r' not in b for b in result.values())
for name, body in original.items():
    assert (ROOT / name).read_bytes() == body
assert (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes() == source_bytes
assert (ROOT / REVIEW).read_bytes() == review_bytes and (ROOT / APPLY).read_bytes() == apply_bytes
temporary = {}
try:
    for name, body in result.items():
        with tempfile.NamedTemporaryFile(dir=ROOT, prefix='c9-source-disposition-', delete=False) as stream:
            stream.write(body)
            temporary[name] = Path(stream.name)
    for name, body in original.items():
        assert (ROOT / name).read_bytes() == body
    for name, temp in temporary.items():
        os.replace(temp, ROOT / name)
finally:
    for temp in temporary.values():
        temp.unlink(missing_ok=True)
for name, body in result.items():
    assert (ROOT / name).read_bytes() == body
counts = Counter(r['status'] for r in units if r['paper'] == 'III')
print('UTC', now)
print('Actual criterion transitions:', changed)
print('Paper III units:', dict(counts))
print('P11/P15 done at the exact source scope; build row reopened; all128 required checks retained.')
print('No final-image, provenance, count or independent-proof credit; IV and joint phase unchanged.')
