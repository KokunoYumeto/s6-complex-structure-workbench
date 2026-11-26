"""Admit the final identity phrases, carrier names and actual matrix replay event."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)

def read_table(path):
    with path.open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)

def write_table(path, fields, rows):
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

df, defects = read_table(ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv')
ef, events = read_table(ROOT / 'CHECK_EVENTS.tsv')
_, final = read_table(ROOT / 'agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_final_identity_defects.tsv')
_, carrier = read_table(ROOT / 'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_carrier_notation_defects.tsv')
assert len(final) == 3 and len(carrier) == 1
added_events = []
for name in ('agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_final_identity_events.tsv',
             'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_carrier_CHECK_EVENTS.tsv',
             'agents/continuation9_computation_method/S6_SERIES_PUBLISH_c9_KU_CHECK_EVENTS.tsv'):
    fields, rows = read_table(ROOT / name)
    assert fields == ef
    added_events.extend(rows)
source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
before = source.read_text()
after = before
for row in final + carrier:
    assert after.count(row['old_text']) == 1, row['change_id']
    after = after.replace(row['old_text'], row['new_text'], 1)
inverse = after
for row in reversed(final + carrier):
    assert inverse.count(row['new_text']) == 1, row['change_id']
    inverse = inverse.replace(row['new_text'], row['old_text'], 1)
assert inverse == before
identifiers = lambda s: Counter(re.findall(r'\\(?:label|hypertarget)\{[^{}]*\}', s))
assert identifiers(before) == identifiers(after)
assert not {r['change_id'] for r in defects} & {r['change_id'] for r in final + carrier}
assert not {r['event_id'] for r in events} & {r['event_id'] for r in added_events}
now = datetime.now(timezone.utc).isoformat()
for row in final + carrier:
    row['review_status'] += ' Root read exact difference and interpretation; admitted ' + now + '; final page review remains open.'
source.write_text(after, newline='\n')
write_table(ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv', df, defects + final + carrier)
write_table(ROOT / 'CHECK_EVENTS.tsv', ef, events + added_events)
ff, findings = read_table(ROOT / 'S6_SERIES_PUBLISH_findings_III.tsv')
for row in findings:
    if row['id'] in ('P2', 'P11', 'P14'):
        assert row['status'] == 'open'
        row.update(status='done', date_utc=now,
            source_resolution='Named loci and the complete source-wide contextual sweep are settled; all exact edits and scoped checks admitted.',
            remaining_gate='Final rendered-page reading remains in the separate paper PDF gate.',
            evidence='agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_source_wording_review.md; code/S6_SERIES_PUBLISH_c9_close_wording_findings.py/.out')
        if row['id'] == 'P14':
            row['source_resolution'] += ' All58 actual integral cochain and peripheral calculations agree with the archive, with explicit cone, Smith projection/lift maps and centrality witnesses at the cited marked-model scope.'
            row['evidence'] += '; agents/continuation9_computation_method/S6_SERIES_PUBLISH_III_02KU_matrix_method_review.md; publish:c9:III:02KU:matrix-replay'
write_table(ROOT / 'S6_SERIES_PUBLISH_findings_III.tsv', ff, findings)
uf, units = read_table(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
row, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == 'methodology' and r['defect_type'] == 'D15']
assert row['status'] == 'done'
row.update(status='open', date_utc=now,
    evidence='New c9 intake and scoped events are admitted; final c9 exact count selector in preparation.',
    detail='The current printed methodology counts describe cp100. Reopened for final-text count derivation with the eight exact descriptive-intake subject associations and newly admitted scoped events; raw event subjects remain unchanged.')
write_table(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', uf, units)
print('Admitted three P11 phrases, one carrier symbol correction and', len(added_events), 'exact events including the actual58-input computation.')
print('P2, P11 and P14 source findings are done; fifteen of eighteen supplied findings are done.')
print('T1 full builds and P15 complete source disposition remain open; P4 is deferred to joint phase.')
print('Methodology D15 reopened for the final source count update. No PDF-page credit assigned.')
