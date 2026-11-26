"""Keep source and build gates truthful after candidate02 repair admissions."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
now = datetime.now(timezone.utc).isoformat()


def table(name):
    with (ROOT / name).open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)


def write(name, fields, rows):
    with (ROOT / name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


ef, events = table('CHECK_EVENTS.tsv')
assert sum(r['event_id'] == 'publish:c9:III:02LP:full-notation-context' for r in events) == 1
df, defects = table('S6_SERIES_PUBLISH_defects_III.tsv')
assert any('02LP' in r['change_id'] and 'Root admission' in r['review_status'] for r in defects)
uf, units = table('S6_SERIES_PUBLISH_unit_progress.tsv')
row, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == 'maps:src:D.2.48' and r['defect_type'] == 'D20']
assert row['status'] == 'open'
row.update(status='done', date_utc=now,
    evidence=row['evidence'] + '; agents/continuation9_02LP_notation/S6_SERIES_PUBLISH_III_02LP_notation_review.md; code/S6_SERIES_PUBLISH_c9_admit_02LP_notation.out',
    detail=row['detail'] + ' Source disposition complete: the full 935-line original and 941-line proposed statement/proof were compared, all34 exact fragments were read and admitted with full reverse source recovery, and the scoped used-event is retained. The final changed-page and other common gates remain separately open.')

ff, findings = table('S6_SERIES_PUBLISH_findings_III.tsv')
for row in findings:
    if row['id'] not in ('P11', 'P15'):
        continue
    assert row['status'] == 'open'
    row['date_utc'] = now
    row['source_resolution'] += ' Candidate02 now has all696 actual-image notes. Its observed02LP repair is admitted. Further image-discovered repairs are being admitted with full affected-scope readings and exact inverse substitutions; canonical defect rows and scoped check events identify each admission.'
    row['remaining_gate'] = 'Finish all observed candidate02 source instances, including remaining02LM,02S8,02S9,02SB,02L8,02L9,02LA packets; compare their complete affected source scopes; then rebuild and actually read changed final pages. The exact later disposition must also include all already admitted packets.'
    row['evidence'] += '; S6_SERIES_PUBLISH_reading_III.md > complete attributed candidate02 reading; canonical candidate02 defect admissions'

bf, builds = table('S6_SERIES_PUBLISH_build_progress.tsv')
row, = [r for r in builds if r['paper'] == 'III']
assert row['status'] == 'done'
row.update(status='open', date_utc=now,
    detail=row['detail'] + ' After that frozen-source build, exact image-discovered source/layout repairs were admitted. This current-source build gate is reopened. The retained PDF and diagnostics still identify the completed candidate02 reading input; they do not certify the repaired source.')

write('S6_SERIES_PUBLISH_unit_progress.tsv', uf, units)
write('S6_SERIES_PUBLISH_findings_III.tsv', ff, findings)
write('S6_SERIES_PUBLISH_build_progress.tsv', bf, builds)
print('Closed02LP D20 at the admitted full-source scope; expanded the still-open P11/P15 remaining gates; reopened the current-source full-build gate.')
print('No raw check event, mathematical assertion, final-page gate or independent-proof scope changed.')
