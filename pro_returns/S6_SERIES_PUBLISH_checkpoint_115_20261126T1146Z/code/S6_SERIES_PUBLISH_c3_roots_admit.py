"""Admit the full cyclic-root owner and its three exact receiving comparisons."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder = ROOT / 'agents/continuation3_foundations/sec11'
prefix = 'S6_SERIES_PUBLISH_sec11_roots_'
before = SOURCE.read_text()
after = before
guards = json.loads((folder / (prefix + 'guards.json')).read_text())
assert len(guards) == 5
for row in guards:
    assert after.count(row['old']) == 1, row['key']
    after = after.replace(row['old'], row['new'], 1)
preserve_identifiers(before, after)
for old, new in zip(identifiers(before), identifiers(after)):
    assert all(new[k] == v for k, v in old.items())
    assert all(new[k] == 1 for k in new - old)
assert r'\eqref{cdp:eq:C.AR.2}--\eqref{cdp:eq:C.AR.3}' not in after
SOURCE.write_text(after, newline='\n')
for suffix, target, key in [
    ('defects.tsv', 'S6_SERIES_PUBLISH_defects_II.tsv', 'change_id'),
    ('CHECK_EVENTS.tsv', 'CHECK_EVENTS.tsv', 'event_id')
]:
    _, rows = read_tsv(folder / (prefix + suffix))
    if suffix == 'CHECK_EVENTS.tsv':
        assert all(row['type'] == 'used and rechecked in this run' for row in rows)
        assert all('effort' in row['who'] for row in rows)
    print(suffix, append_rows(ROOT / target, rows, key))

fields, progress = read_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
_, statuses = read_tsv(folder / (prefix + 'unit_progress.tsv'))
incoming = {row['unit'] for row in statuses}
assert len(incoming) == 4 and len(statuses) == 104
progress = [row for row in progress if not (row['paper'] == 'II' and row['unit_id'] in incoming)]
titles = {label: title for title, label in re.findall(r'^\\subsection\{([^\n]+)\}\\label\{([^}]+)\}', after, re.M)}
for row in statuses:
    kind = 'structure' if row['row'] == 'restructuring' else row['row']
    status = 'open' if kind in ['D14', 'D23', 'D24', 'structure'] else row['status']
    progress.append(dict(zip(fields, [
        'II', row['unit'], titles.get(row['unit'], row['unit']),
        'structure' if kind == 'structure' else 'defect',
        '' if kind == 'structure' else kind, status, now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-ROOTS-ADMISSION',
        row['basis'] + ' Foundations read all complete old/current and receiving proofs, including the complete bounded UN73 proof. Root read the full P342, P349/UN76, UN78 and P341/UN86 receivers, comparison, status and source rows, and the complete bounded UN73 determinant diff. Original sec11/12 remainders and whole-paper placement remain open. No movement credit for subdivision.'
    ])))
keys = [(row['paper'], row['unit_id'], row['defect_type'] or row['row_kind']) for row in progress]
assert len(keys) == len(set(keys))
write_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', fields, progress)

_, sources = read_tsv(folder / (prefix + 'sources.tsv'))
incoming_sources = [dict(
    source=row['source_id'] + ' (third-continuation root consolidation)',
    url=row['url'], version=row['version'],
    locus=row['exact_locus'] + '; ' + row['reader'],
    date_utc=row['date_utc'], sha256=row['sha256'],
    own_word_summary=row['own_paraphrase'],
    use='Analytic embedded resolution near the same compact central support. The source reading is the exact recorded statement/setup reading; no full desingularization-proof credit. The manuscript retains the complete cyclic-root, labelled monomial coarsening, canonical-order, finite-quotient, stratum-Euler and inverse compact maps.'
) for row in sources]
print('Sources', append_rows(ROOT / 'S6_SERIES_PUBLISH_c3_primary_readings.tsv', incoming_sources, 'source'))
add_event('prop:II:cyclic-root-normalization;def:II:marked-weighted-toric-support;cdp:st:C.2.UN.76;cdp:st:C.2.UN.78;def:II:finite-rooted-reconstruction;cdp:st:C.2.UN.86;cdp:st:C.2.UN.73',
          'II-C3-ROOT-ROOTS-ADMISSION', 'used and rechecked in this run',
          'Foundations read the complete old/current and receiving UN76/78/86 proofs, all original data paragraphs and both full UN73 proofs. Root read complete P342, P349/UN76, UN78 and P341/UN86, comparison/status/source records and the bounded old/new UN73 determinant. P342 owns the full smooth-threefold arbitrary-support root construction, its unit-dependent normalized star-ideal charts, invariant algebra, canonical ray minima, intrinsic component covers and threshold, Euler correction and compact cyclic base map. UN76 applies (pi,Y,N,Z,Y_N)=(id_X,X,M,tilde X,X_M), explicitly defines rho_tot=rho composed with q, and transports the four real columns by diag(P^-1,P^-1), with positive determinant factor (det P)^2 and finite angular enlargement. UN78 and UN86 retain every full multiplicity, both reconstruction directions, all transverse terms, inverse-before-quotient order, and compact conclusions. UN86 names q/pi as punctured isomorphisms and rho as the finite etale root map. All old labels and targets retain exact multiplicity; AR2/AR3 remain aliases of one displayed correction formula cited once. No independent proof, required-check increment, final page, whole UN73 closure or subdivision movement credit.',
          'Cyclic-root normalization; weighted toric descent; canonical-flat root descent; finite rooted generation; bounded UN73 determinant alias', source=__file__)
print('P341/P342/P349 and full receiving UN76/78/86 admitted; UN73 determinant alias preserved; original remaining units stay open.')
