"""Admit whole source reviews only after actual shared-owner placement."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now = datetime.now(timezone.utc).isoformat()
note = 'agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_carriers_metrics_and_shared_owners_admission.md'
df, ds = r.table(r.DEFECTS)
ef, es = r.table(u.ROOT / 'CHECK_EVENTS.tsv')
pf, ps = r.table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
nd = ne = 0
packages = [
 ('continuation8_iii_later', 'S6_SERIES_PUBLISH_III_carriers_publication', 74, 24),
 ('continuation8_iii_later', 'S6_SERIES_PUBLISH_III_metrics_publication', 41, 9),
 ('continuation8_iii_later', 'S6_SERIES_PUBLISH_III_limits_publication', 4, 5),
 ('continuation8_iii_later', 'S6_SERIES_PUBLISH_III_regular_publication', 33, 7),
 ('continuation8_iii_later', 'S6_SERIES_PUBLISH_III_carrier_wedge_followup', 1, 2),
 ('continuation8_iii_weighted_units', 'S6_SERIES_PUBLISH_SPHERE_PAIRING', 15, 3),
]
for lane, stem, dc, ec in packages:
    folder = u.ROOT / 'agents' / lane
    dname = stem + ('_publication_defects.tsv' if 'SPHERE_PAIRING' in stem else '_defects.tsv')
    edits = r.table(folder / dname)[1]
    events = r.table(folder / (stem + '_CHECK_EVENTS.tsv'))[1]
    assert (len(edits), len(events)) == (dc, ec), stem
    for row in edits:
        assert not any(x['change_id'] == row['change_id'] for x in ds)
        out = {k: row.get(k, '') for k in df}
        out['review_status'] = row.get('review_status', '') + '; complete attributed review and actual shared-owner placement admitted ' + now + '; ' + note
        ds.append(out)
        nd += 1
    for row in events:
        assert row['type'] == 'used and rechecked in this run'
        assert not any(x['event_id'] == row['event_id'] for x in es)
        out = {k: row.get(k, '') for k in ef}
        out['outcome'] = row['outcome'] + ' Root read every complete substantive review and criterion assessment, all bounded final changes and actual canonical successor outputs. Whole mathematical readings retain their stated attribution. No new independent credit. ' + note
        es.append(out)
        ne += 1
assert (nd, ne) == (168, 50)
root_events = {
 'mapsIII:carrier-three-complex-wedge': 'Whole current proof, full199-line historical comparison, entire79-line initial rewrite and all final84-line contexts read. Both cylinders, relative maps, chosen generators and based inverse were compared completely; actual early placement and exact037M application read.',
 'mapsaudit:finite-degree-three': 'Whole current proof, full340-line historical comparison, entire169-line initial rewrite and all final173-line contexts read. Exact affine input, fixed lattices, J inverse, basis sign, full integral pullback images, Smith/kernel data and typed duality/transfer identities compared; actual cell/Kummer boundaries read.',
 'mapsIII:def:finite-band-coverings': 'Complete Q020 input and bounded cell datum/premises read. The two actual affine actions, orientation, quotient maps and inverse naming maps are explicit and preserve the complete original scope.',
 'mapsIII:angle-forgotten-one-copy-null': 'Full27-line existing Q7 proof reread; actual lines7998-8024 and following named-family subsection read. Its earlier D14 placement description is corrected: the complete unit was moved from the manuscript end after its actual quotient-map prerequisite. No new completed criterion is counted for this evidence correction.'
}
for label, outcome in root_events.items():
    eid = 'publish:c8:III:shared-owner-admission:' + label
    assert not any(x['event_id'] == eid for x in es)
    row = {k: '' for k in ef}
    row.update(statement_id=label, date='2026-11-25',
        who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',
        type='used and rechecked in this run', outcome=outcome + ' Actual editor/application outputs and empty errors read. No historical program rerun, new primary opening, independent-check increment or final-page credit. ' + note,
        event_id=eid, phase='continuation8 publication unit comparison', source_file=note,
        source_event_type='used and rechecked in this run', evidence_group='publish:c8:III:shared-owners', date_utc=now, where=note)
    es.append(row)

units = [
 ('wb:cusp-cone-section', 'The marked quotient over the punctured cusp', True),
 ('mapsIII:def:two-torus-suspension', 'The two-torus suspension carrier', False),
 ('mapsIII:def:circle-suspension', 'Circle suspensions and finite fillings', False),
 ('wb:cusp-cone-target-slice-embeddings', 'Radial embeddings and intrinsic metrics', False),
 ('wb:cusp-cone-obstructions', 'Finite-cover and extension obstructions', False),
 ('wb:cusp-cone-optimal-exponents', 'Minimum smash dimensions and compactification maps', False),
 ('wb:cusp-cone-angle-forgotten-sphere-carriers', 'Collapsed sphere targets and their intrinsic metrics', False),
 ('wb:cusp-cone-sphere-map-homotopy-status', 'Homotopy classes and suspension factorizations', False),
 ('wb:cusp-cone-literal-R4-open-cells', 'Open four-cells and moving spheres', False),
 ('wb:cusp-cone-explicit-carriers', 'Conical carriers and their homotopy types', False),
 ('wb:cusp-cone-exact-decompactification-space', 'Decompactification spaces', False),
 ('wb:sphere-metric-limit-note', 'Fixed targets and radial collapse', True),
 ('mapsIII:lem:fixed-conical-metrics', 'Compatible length metrics and slice forms', False),
 ('wb:sphere-metric-scaling-trichotomy', 'Arbitrary radial scaling', False),
 ('wb:sphere-metric-fixed-realization', 'Native and unit-volume scaling', False),
 ('wb:sphere-metric-tangent-scope', 'Vertex links and pointed limits', False),
 ('mapsIII:rem:source-and-moving-metrics', 'Source pullbacks and moving sphere metrics', False),
 ('wb:cusp-cone-sharp-global-R4-scope', 'Euclidean cells, intrinsic limits and boundary fibres', False),
 ('maps:rem:natural-sphere-sector-scope', 'Section lines and sphere multiplicities', False),
 ('mapsIII:problem:finite-cusp-cover-compactification', 'Compactifications and raw carrier classes', False),
 ('maps:src:D.2.4', 'Recognition by complete integral invariants', True),
 ('mapsIII:sec:regular-quotients', 'Invariant characters and compactification', True),
 ('wb:cusp-s12-full-carrier-null', 'External smash products of sphere maps', False),
 ('mapsIII:carrier-three-complex-wedge', 'Recognition of a two-sphere and three-sphere wedge', False),
 ('mapsaudit:finite-degree-three', 'Integral degree-three maps of the finite band', False),
]
source = u.repairs.SOURCE.read_text()
closed = added = 0
for ident, title, existing in units:
    assert '\\label{' + ident + '}' in source, ident
    selected = [x for x in ps if x['paper'] == 'III' and x['unit_id'] == ident]
    if existing:
        assert len(selected) == 28 and all(x['status'] == 'open' for x in selected), ident
    else:
        assert not selected, ident
        for c in [f'D{i:02d}' for i in range(1, 28)] + ['structure']:
            row = {k: '' for k in pf}
            row.update(paper='III', unit_id=ident, row_kind='structure' if c == 'structure' else 'defect', defect_type='' if c == 'structure' else c)
            selected.append(row)
            ps.append(row)
            added += 1
    for row in selected:
        c = row['defect_type'] or 'structure'
        done = c not in {'D04', 'D06', 'D09', 'D18'}
        row.update(unit_title=title, status='done' if done else 'open', date_utc=now,
            evidence=note, detail='Complete whole-unit reviews and all28 criteria admitted with exact shared-proof maps/inverses and actual prerequisite/successor boundaries. Four common gates and final PDF remain.')
        closed += done
assert (closed, added) == (600, 588), (closed, added)
for row in ps:
    if row['paper'] == 'III' and row['unit_id'] == 'mapsIII:carrier-extension-section' and row['defect_type'] == 'D14':
        assert row['status'] == 'done'
        row.update(date_utc=now, evidence=note, detail='Actual Q7 placement corrected and reread after quotient_maps; earlier placement description was premature. Evidence correction adds no completed criterion.')
for row in ds:
    if row['change_id'] in {'III-C8-ROOT-WEDGE-UNIT', 'III-C8-ROOT-FINITE-BAND-UNIT', 'III-C8-ROOT-BASED-CYLINDER', 'III-C8-ROOT-BASED-HOMOTOPIES', 'III-C8-ROOT-TRANSFER-DOMAINS'}:
        row['review_status'] = 'Complete predecessor/current source, full historical comparison, all final contexts and actual placements read; admitted with four common/final PDF gates. ' + note
r.write_table(r.DEFECTS, df, ds)
r.write_table(u.ROOT / 'CHECK_EVENTS.tsv', ef, es)
r.write_table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', pf, ps)
print('UTC', now)
print('IMPORTED_EXACT_DEFECT_ROWS', nd, 'ATTRIBUTED_EVENTS', ne, 'ROOT_USED_EVENTS', len(root_events))
print('ACTUAL_UNITS', len(units), 'SOURCE_CRITERIA_CLOSED', closed, 'NEW_ACTUAL_UNIT_ROWS', added)
print('COMMON_AND_FINAL_PDF_GATES_OPEN; NATIVE_RETAINED_ANGLE_PUBLICATION_PENDING')
