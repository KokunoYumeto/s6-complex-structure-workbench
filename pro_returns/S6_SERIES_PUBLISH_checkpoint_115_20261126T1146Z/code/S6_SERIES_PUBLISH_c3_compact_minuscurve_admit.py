"""Admit the complete compact negative-curve construction and its exact maps."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder = ROOT / 'agents/continuation3_foundations/sec11'
prefix = 'S6_SERIES_PUBLISH_sec11_compact_minuscurve_'
before = SOURCE.read_text()
after = before
guards = json.loads((folder / (prefix + 'guards.json')).read_text())
assert len(guards) == 1
for row in guards:
    assert after.count(row['old']) == 1, row['key']
    after = after.replace(row['old'], row['new'], 1)
preserve_identifiers(before, after)
for old, new in zip(identifiers(before), identifiers(after)):
    assert all(new[k] == v for k, v in old.items())
    assert all(new[k] == 1 for k in new - old)
SOURCE.write_text(after, newline='\n')
for suffix, target, key in [
    ('defects.tsv', 'S6_SERIES_PUBLISH_defects_II.tsv', 'change_id'),
    ('CHECK_EVENTS.tsv', 'CHECK_EVENTS.tsv', 'event_id')
]:
    _, rows = read_tsv(folder / (prefix + suffix))
    if suffix == 'CHECK_EVENTS.tsv':
        assert all(row['type'] == 'used and rechecked in this run' and 'effort' in row['who'] for row in rows)
    print(suffix, append_rows(ROOT / target, rows, key))
fields, progress = read_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
_, statuses = read_tsv(folder / (prefix + 'unit_progress.tsv'))
incoming = {row['unit'] for row in statuses}
assert len(incoming) == 1 and len(statuses) == 26
progress = [row for row in progress if not (row['paper'] == 'II' and row['unit_id'] in incoming)]
titles = {label: title for title, label in re.findall(r'^\\subsection\{([^\n]+)\}\\label\{([^}]+)\}', after, re.M)}
for row in statuses:
    kind = 'structure' if row['row'] == 'restructuring' else row['row']
    status = 'open' if kind in ['D14', 'D23', 'D24', 'structure'] else row['status']
    progress.append(dict(zip(fields, ['II', row['unit'], titles.get(row['unit'], row['unit']),
        'structure' if kind == 'structure' else 'defect', '' if kind == 'structure' else kind,
        status, now(), 'CHECK_EVENTS.tsv: II-C3-ROOT-COMPACT-MINUSCURVE-ADMISSION',
        row['basis'] + ' Foundations read complete old/current and receiving UN79. Root read the full receiver, comparison, status and check records and followed the complete displayed coordinate, divisor and Euler calculations. The following elliptic-model and original sec11 remainder stay open; no subdivision movement credit.'])))
keys = [(row['paper'], row['unit_id'], row['defect_type'] or row['row_kind']) for row in progress]
assert len(keys) == len(set(keys))
write_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', fields, progress)
add_event('cdp:st:C.2.UN.79', 'II-C3-ROOT-COMPACT-MINUSCURVE-ADMISSION',
          'used and rechecked in this run',
          'Foundations read complete old/current and receiving UN79; root read the entire receiver, comparison/status and check records. The single explicit Weierstrass construction retains every original conclusion and coordinate map. The discriminant h(t^4), infinity factor, complete A2 charts, residue divided by s^2, O(-1) plus O(-2) neighbourhood and Jacobian orders are explicit. P343 applies to pi0:X1 to J times E over the same disc; P234 applies to the compact full supports with the same smooth centres B0,B1,D. The genus-three cover includes the exact infinity parameter; component Euler numbers 0,4,4,6,6,-8, double-curve Euler 24 and twelve triple points remain with their geometric derivation. All original labels and targets retain exact multiplicity. No independent proof, required-check increment, final-page reading or surrounding-unit closure is credited.',
          'Compact negative-curve subsection and its canonical/direct-image and support-Euler applications', source=__file__)
print('Full UN79 compact construction admitted; one actual subsection assessed; following elliptic-model remainder stays open.')
