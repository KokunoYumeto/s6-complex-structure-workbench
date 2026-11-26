"""Record the concrete remaining P15 instances found in final reconciliation."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
now = datetime.now(timezone.utc).isoformat()
instances = {
    'maps:src:D.2.18': '02KS: graph D and the later explicitly chosen five-disc D.',
    'maps:src:D.2.32': '02L8: the whole-fibre F and italic finite-option label F.',
    'maps:src:D.2.33': '02L9: geometric functions/maps and later enumeration letters and numeric table headers.',
    'maps:src:D.2.34': '02LA: group-ring indeterminate t and the geometric sweep t.',
    'maps:src:D.2.35': 'Containing section16 unit, formal02LC/maps:src:D.2.36: the integer/site N and a later bordism manifold N.',
    'maps:src:D.2.39': 'Containing subsection17.1 unit, formal02LJ/maps:src:D.2.42: finite cap/return F and later generic fixed-curve F.',
    'maps:src:D.2.44': 'Containing subsection17.2 unit, formal02LM/maps:src:D.2.45: odd factor q and later coefficient q=4,5, plus named local kernel coefficients and earlier matrices.',
    'night:P3F.31': '02S8: suspension and binary-sheet a parameters versus the graph cochain a.',
    'night:P3F.32': '02S9: angular a and imported graph cochain a; cubic function f and return diffeomorphism f.',
}


def read(name):
    with (ROOT / name).open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)


def write(name, fields, rows):
    with (ROOT / name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


fields, units = read('S6_SERIES_PUBLISH_unit_progress.tsv')
for subject, instance in instances.items():
    matches = [r for r in units if r['paper'] == 'III' and r['unit_id'] == subject and r['defect_type'] == 'D20']
    assert len(matches) == 1, (subject, len(matches))
    row, = matches
    assert row['status'] == 'done', (subject, row['status'])
    row.update(status='open', date_utc=now,
        evidence=row['evidence'].rstrip('; ') + '; agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_P11_P15_final_source_disposition.md; root final source-scope reconciliation',
        detail=row['detail'] + ' Reopened for the concrete residual name assignment: ' + instance + ' A local paragraph boundary alone does not settle this instance. Exact bounded repair and full affected-use comparison remain; no required mathematical conclusion is reopened.')
write('S6_SERIES_PUBLISH_unit_progress.tsv', fields, units)
fields, findings = read('S6_SERIES_PUBLISH_findings_III.tsv')
row, = [r for r in findings if r['id'] == 'P15']
assert row['status'] == 'open'
row['date_utc'] = now
row['remaining_gate'] = 'Complete the final02L9 packet and concrete residual-rebinding addenda for02KS,02L8,02LA,02LC,02LJ,02LM,02S8,02S9. Each needs exact source rows and full affected-use readback; then final source disposition, counts, both builds and changed-page reading. Genuine same-object redeclarations and supplied font/index distinctions keep their documented scope.'
row['source_resolution'] += ' Final reconciliation identified nine remaining local name assignments; the corresponding D20 unit rows were reopened explicitly. Mere paragraph rebinding is not taken as a source closure.'
write('S6_SERIES_PUBLISH_findings_III.tsv', fields, findings)
print('Reopened nine identified D20 rows for exact current-source instances:')
for subject, instance in instances.items():
    print(subject, instance, sep=' | ')
print('All128 required mathematical checks and all prior exact defect/event rows remain. P15 source closure is held.')
