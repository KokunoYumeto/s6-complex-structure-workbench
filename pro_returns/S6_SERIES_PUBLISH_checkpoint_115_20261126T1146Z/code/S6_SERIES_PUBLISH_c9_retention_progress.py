"""Resolve admitted P15 scopes and reopen actual remaining named-role cases."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
now = datetime.now(timezone.utc).isoformat()

def read(name):
    with (ROOT / name).open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)

def write(name, fields, rows):
    with (ROOT / name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

closed = {
    'maps:src:D.2.18': ('ce:c9-iii-current02-02ks-retention-reconciliation', 'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_current02_02KS_retention_review.md', 'The complete current1366-line02KS scope and its24 exact additional fragments were compared after the separate graph-map repair. Every earlier concrete retention now has an actual name or a documented full-symbol/formal-argument binding.'),
    'maps:src:D.2.32': ('ce:c9-iii-current02-knownroles-02l8', 'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_current02_known_roles_review.md', 'The exact finite-option bijection is admitted, preserving the complete fibre vector, quotient and section from the full631-line source review.'),
    'maps:src:D.2.33': ('publish:c9:III:02L9:full-notation-context', 'agents/continuation9_02L9_notation/S6_SERIES_PUBLISH_III_02L9_notation_review.md', 'The expanded eight-fragment packet is admitted, including the explicit holomorphic-unit binding, every enumeration variable and upright table heading. The complete540-to542-line scope was compared.'),
    'maps:src:D.2.34': ('ce:c9-iii-current02-knownroles-02la', 'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_current02_known_roles_review.md', 'The cyclic ring generator and both actual downstream coefficient-ring imports have exact inverse substitutions. The geometric sweep and every cap column retain their stated objects.'),
    'night:P3F.31': ('ce:c9-iii-current02-knownroles-02s8', 'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_current02_known_roles_review.md', 'The suspension parameter and binary sheet index are qualified throughout their actual maps and inverse/collision equations. The imported graph cochain retains its object; remaining scalar arguments retain their explicit binders.'),
    'night:P3F.32': ('publish:c9:III:02S9:retained-role-readback', 'agents/continuation9_retained_scopes/S6_SERIES_PUBLISH_c9_retained_scope_review.md', 'The cap angle, norm-ratio logarithm and cubic inversion function now have separate full names in every affected use. The return map and imported graph cochain retain their definitions and actual inverse maps.'),
}
opened = {
    'maps:src:D.2.9': '02LZ: the root coordinate u and the named homology class u=e_3.',
    'maps:src:D.2.10': '02KK: the Bezout integer alpha and invariant cohomology class alpha; physical lattice u and the final CRT inverse integer u.',
    'maps:src:D.2.13': '02KN: graph matrix K and transvection K(u); deformation h and later cochain vector h.',
    'maps:src:D.2.37': '02LD: additive/multiplicative beta_0, inverse-exponent E and attached space E, plus concrete option and enumeration labels.',
    'maps:src:D.2.49': '02LQ: torsion group T, averaging operator T and central Wang generator T.',
    'maps:src:D.2.50': '02LS: divisor/Smith/graph D roles, elliptic/scalar/prism/presentation B roles, fibration/cutoff f, and named cap maps with different domains.',
    'maps:src:D.2.51': '02LT: initial retraction r, monodromy row r and Dynkin rank r; the roof is already qualified.',
    'maps:src:D.2.53': '02LV: transverse period r and component index r; curve cohomology generator x and group-ring variables.',
    'night:P3F.26': '02S2: the height coefficient a and later holomorphic unit a.',
}
ef, events = read('CHECK_EVENTS.tsv')
uf, units = read('S6_SERIES_PUBLISH_unit_progress.tsv')
for subject, (event, evidence, detail) in closed.items():
    assert sum(r['event_id'] == event for r in events) == 1, event
    assert (ROOT / evidence).is_file(), evidence
    row, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == subject and r['defect_type'] == 'D20']
    assert row['status'] == 'open', subject
    row.update(status='done', date_utc=now, evidence=row['evidence'] + '; ' + evidence,
        detail=row['detail'] + ' Current-source retained-role disposition admitted: ' + detail + ' Changed-page and whole-paper gates remain separately open.')
for subject, detail in opened.items():
    row, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == subject and r['defect_type'] == 'D20']
    assert row['status'] == 'done', subject
    row.update(status='open', date_utc=now,
        evidence=row['evidence'] + '; continuation9 actual-source retention reconciliation',
        detail=row['detail'] + ' Reopened for this concrete live role assignment: ' + detail + ' Exact bounded repair and affected-use comparison remain. Paragraph boundaries alone provide no naming exception; all required mathematical conclusions retain their existing checks.')
row, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == 'wb:cusp-cone-angle-forgotten-sphere-carriers' and r['defect_type'] == 'D20']
assert row['status'] == 'done'
assert sum(r['event_id'] == 'publish:c9:III:036J:retained-role-readback' for r in events) == 1
row.update(date_utc=now,
    evidence=row['evidence'] + '; agents/continuation9_root_image_repairs/S6_SERIES_PUBLISH_c9_root_retained_carrier_review.md',
    detail=row['detail'] + ' Actual-current302-line reread identified the final collapsed-subset W reuse. Its five W_col uses were repaired and admitted with full-source reversal and the unchanged ball-map inverse. Earlier0374 and037M candidate retentions were already repaired and receive no additional edit or event.')
ff, findings = read('S6_SERIES_PUBLISH_findings_III.tsv')
row, = [r for r in findings if r['id'] == 'P15']
assert row['status'] == 'open'
row['date_utc'] = now
row['source_resolution'] += ' Six initially reopened D20 scopes now have admitted exact final retained-role dispositions; nine further actual source cases are explicitly reopened. The live036J collapsed-subset case was repaired immediately. Historical0374/037M candidates were compared with current source and are already resolved by the first root image packet.'
row['remaining_gate'] = 'Finish the documented02S2,02LZ,02KK,02KN,02LD,02LQ,02LS,02LT,02LV packets and the remaining02LB/02LE/02LF/02LL scopes in their existing containing units. Compare every affected definition/use and exact inverse substitution; complete the authored whole-paper P11/P15 source disposition, then final counts, both builds and actual changed-page reading. Already admitted local scope closures retain separate final-page gates.'
write('S6_SERIES_PUBLISH_unit_progress.tsv', uf, units)
write('S6_SERIES_PUBLISH_findings_III.tsv', ff, findings)
print('Closed six admitted current-source D20 scopes:', ', '.join(closed))
print('Reopened nine concrete remaining current-source D20 scopes:', ', '.join(opened))
print('Recorded the admitted036J repair in its already complete source row. Whole-paperP15 and final rendering remain open.')
