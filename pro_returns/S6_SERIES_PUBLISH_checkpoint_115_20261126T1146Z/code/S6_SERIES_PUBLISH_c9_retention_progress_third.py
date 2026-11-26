"""Record six admitted strict source dispositions; leave final PDF gates open."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
now = datetime.now(timezone.utc).isoformat()

def read(name):
    with (ROOT / name).open(newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)

def write(name, fields, rows):
    with (ROOT / name).open('w', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

gauge = 'agents/continuation9_gauge_role_addenda/S6_SERIES_PUBLISH_c9_gauge_role_review.md'
geo = 'agents/continuation9_geometric_role_addenda/S6_SERIES_PUBLISH_c9_geometric_role_review.md'
ls = 'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_current02_02LS_retention_review.md'
closed = {
    'maps:src:D.2.35': (
        ['publish:c9:III:02LC:retained-role-readback', 'publish:c9:III:02LB:retained-gauge-role-readback', 'publish:c9:III:02LE:retained-gauge-role-readback'],
        gauge,
        'The complete section16 scope has the admitted LC manifold/fixed-component packet and LB/LE gauge-role addendum. All finite indices, prime coefficients, fixed-curve maps, Tate weights and CRT inverse uses were traced; genuine same-object and formal-argument retentions have their exact domain explanations.'),
    'maps:src:D.2.39': (
        ['publish:c9:III:02LF:retained-gauge-role-readback', 'publish:c9:III:02LJ:retained-gauge-role-readback'],
        gauge,
        'The LF/LJ roof, affine, Tate, root, vertical-index and prime roles are followed through the full maps and inverse substitutions. The previously admitted LJ finite and fixed component repairs remain in place.'),
    'maps:src:D.2.50': (
        ['ce:c9-iii-current02-02ls-retention-reconciliation'],
        ls,
        'All22 fragments, including the explicit LU component-name import, are admitted. The local Smith preimage, two cap specialization maps with sections, K_0/K_0^vee identities, prism splitting, ordinary clutch and final quotient/transport inverses retain their exact values.'),
    'maps:src:D.2.51': (
        ['publish:c9:III:02LT:retained-geometric-role-readback'],
        geo,
        'The retraction is followed through both mapping-torus homotopies; E_Bez retains its exact inverse, r_mon its original displacement and clutch pairing, and r_Dyn its original permutation and inverse tuple.'),
    'maps:src:D.2.53': (
        ['publish:c9:III:02LV:retained-geometric-role-readback'],
        geo,
        'The selected period vectors retain their original entries. The Laurent-ring generator map and inverse preserve all annular Picard columns; x_C retains the fixed-curve evaluation, localization inverse and characteristic roots.'),
    'night:P3F.34': (
        ['publish:c9:III:02SB:retained-geometric-role-readback'],
        geo,
        'The zero-sector Bezout coefficients preserve the full transfer combination. The final p_spl map and both explicit splitting composites preserve the exact sequence; the initial affine vector and boundary cohomology class keep their original meanings.'),
}
_, events = read('CHECK_EVENTS.tsv')
uf, units = read('S6_SERIES_PUBLISH_unit_progress.tsv')
for subject, (event_ids, evidence, detail) in closed.items():
    assert (ROOT / evidence).is_file(), evidence
    for event_id in event_ids:
        event, = [e for e in events if e['event_id'] == event_id]
        assert event['source_event_type'] == 'used and rechecked in this run', event_id
    row, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == subject and r['defect_type'] == 'D20']
    assert row['status'] == 'open', subject
    row.update(status='done', date_utc=now,
        evidence=row['evidence'] + '; ' + evidence,
        detail=row['detail'] + ' Strict retained-role source disposition admitted: ' + detail + ' Root read all final differences and exact comparison records. Complete source reversal and permanent identifiers passed. This closes the source naming criterion only; all changed-page and final-PDF gates remain open.')

ff, findings = read('S6_SERIES_PUBLISH_findings_III.tsv')
row, = [r for r in findings if r['id'] == 'P15']
assert row['status'] == 'open'
row['date_utc'] = now
row['source_resolution'] += ' Six further source naming units are closed by the root-reviewed gauge25/4, geometric11/3 and LS22/1 packets, with all exact maps and inverses compared and no paragraph-only retention.'
row['remaining_gate'] = 'Finish the actual02LL and early02KD packets, admit all exact affected-use and downstream-import comparisons, then read the final authored-retention and whole-paper P11/P15 source disposition. Counts and builds follow source closure. All final-page/layout gates remain separately open.'
write('S6_SERIES_PUBLISH_unit_progress.tsv', uf, units)
write('S6_SERIES_PUBLISH_findings_III.tsv', ff, findings)
print('Closed six actual D20 source units:', ', '.join(closed))
print('02LL and early02KD remain open; whole-paper P11/P15, changed-page and final build gates remain open.')
print('No raw event, derived count or paper other than III changed.')
