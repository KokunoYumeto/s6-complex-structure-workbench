"""Admit complete weighted-cycle owners and their two earlier receivers."""
from S6_SERIES_PUBLISH_c3_edit import *

folder = ROOT / 'agents/continuation3_conductor'
prefix = 'S6_SERIES_PUBLISH_c3_conductor_17_'
before = SOURCE.read_text()
after = before
original = (folder / (prefix + 'input.tex')).read_text()
receiving = (folder / (prefix + 'replacement.tex')).read_text()
assert after.count(original) == 1
after = after.replace(original, receiving, 1)
_, guards = read_tsv(folder / (prefix + 'remote_repairs.tsv'))
assert len(guards) == 4
for row in guards:
    assert after.count(row['old_text']) == 1, row['statement_id']
    after = after.replace(row['old_text'], row['new_text'], 1)
preserve_identifiers(before, after)
for old, new in zip(identifiers(before), identifiers(after)):
    assert all(new[k] == v for k, v in old.items())
    assert all(new[k] == 1 for k in new - old)
assert identifiers(after)[1] - identifiers(before)[1] == Counter({'tag-P355': 1, 'tag-P356': 1, 'tag-P357': 1, 'tag-P358': 1, 'tag-P359': 1})
for label in ['push:src:E.5.2', 'push:src:E.5.3']:
    def statement(text):
        i = text.index(r'\label{' + label + '}')
        a = text.rfind(r'\begin{', 0, i)
        env = re.match(r'\\begin\{([^}]+)\}', text[a:]).group(1)
        b = text.index(r'\end{' + env + '}', i) + len(r'\end{' + env + '}')
        return text[a:b]
    assert statement(before) == statement(after), label
order = ['lem:II:moving-marked-cycle', 'cdp:st:C.2.UN.48', 'def:II:weighted-normal-cycle', 'lem:II:weighted-cycle-roots', 'lem:II:weighted-cycle-affine-data', 'lem:II:finite-equivariant-periods', 'cdp:st:C.2.UN.59', 'cdp:st:C.2.UN.56', 'ex:II:weighted-cycle-examples']
positions = [after.index(r'\label{' + x + '}') for x in order]
assert positions == sorted(positions)

fields, progress = read_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
_, statuses = read_tsv(folder / (prefix + 'unit_status.tsv'))
incoming = {r['unit'] for r in statuses}
assert len(incoming) == 11 and len(statuses) == 286
old_weighted = 'subsec:II:weighted-hopf-cycles'
progress = [r for r in progress if not (r['paper'] == 'II' and r['unit_id'] in incoming | {old_weighted})]
for row in progress:
    if row['paper'] == 'II' and row['unit_id'] == 'sec:II:10':
        assert row['status'] == ('done' if row['defect_type'] in {'D10', 'D16'} else 'open')
        row.update(unit_title='Hopf support-graph and elliptic-tree remainder', date_utc=now(),
            evidence='CHECK_EVENTS.tsv: II-C3-ROOT-CONDUCTOR17-ADMISSION',
            detail='Original sec10 open identity remains on the complete UN54 and UN58/60–63 support/tree remainder. The full weighted UN52/56/59 proofs are consolidated with all exact maps in seven actual subsections. Neither their subdivision nor the weighted-unit identity migration supplies original-row movement credit. D10/D16 stay done; every other original remaining criterion stays open.')
for row in statuses:
    kind = 'structure' if row['criterion'] == 'restructuring' else row['criterion']
    status = 'open' if kind in {'D14', 'D23', 'D24', 'structure'} else row['status']
    progress.append(dict(zip(fields, ['II', row['unit'], row['title'],
        'structure' if kind == 'structure' else 'defect', '' if kind == 'structure' else kind, status, now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-CONDUCTOR17-ADMISSION',
        row['reason'] + ' Conductor read every full original/current and receiving proof and all 48 formula identities. Root read all P355–P359 owners, full UN59 and merged UN56 receiver, complete P333 and UN48 receivers, then the final h=1 and resolved-length/coframe edits, full comparison and all event/source scopes. Original sec10 stays open; identity migration earns no movement. No independent-check, required-check or final-page credit.'])))
keys = [(r['paper'], r['unit_id'], r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys) == len(set(keys))

for suffix, target, key in [('defects.tsv', 'S6_SERIES_PUBLISH_defects_II.tsv', 'change_id'), ('CHECK_EVENTS.tsv', 'CHECK_EVENTS.tsv', 'event_id')]:
    _, rows = read_tsv(folder / (prefix + suffix))
    if suffix == 'CHECK_EVENTS.tsv':
        assert all(r['type'] == 'used and rechecked in this run' and 'effort' in r['who'] for r in rows)
    print(suffix, append_rows(ROOT / target, rows, key))
SOURCE.write_text(after, newline='\n')
write_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', fields, progress)
_, sources = read_tsv(folder / (prefix + 'primary_sources.tsv'))
incoming_sources = [dict(source=r['source_id'] + ' (third-continuation weighted cycles)', url=r['url'], version=r['version'],
    locus=r['exact_locus'] + '; ' + r['reader'], date_utc=r['date_utc'], sha256=r['sha256'], own_word_summary=r['own_paraphrase'],
    use='Exact source statements and setup applied through the marked lift, central finite-cover and punctured-disc torsor maps in the complete weighted-cycle receivers. Conductor opened the specified loci. No unprinted external classification proof, full theorem-B proof or additional root source opening is claimed.') for r in sources]
print('Sources', append_rows(ROOT / 'S6_SERIES_PUBLISH_c3_primary_readings.tsv', incoming_sources, 'source'))
add_event(';'.join(order), 'II-C3-ROOT-CONDUCTOR17-ADMISSION', 'used and rechecked in this run',
    'Five exact guards admitted after complete conductor old/current/new comparisons and root full receiving-proof readings. Seven weighted owners consolidate all UN52/56/59 conclusions with complete normal-line, root normalization, inertia, affine action, period, quotient and compact gluing maps. P333 supplies the previously implicit moving compressed-neck input: four radii, full proper graph-closure resolution, h=1 identity and h-weighted coframe periods; every earlier smooth clause remains. UN48 states the arbitrary q0,a,d pencil/Tate/suspension scope already established by that construction and applies the same earlier monomial resolution. The resolved length sum h_j, vector u=sum(-h_j n_j), root map t=s^N and coframe identify the suspension integer d/N exactly. The finite-equivariant construction preserves every affine constant at zero and infinity. All 48 old equation identities and old labels/tags preserve multiplicity; only tags P355–P359 are new. Protected E.5.2/E.5.3 statements are byte-identical. Original sec10 and following UN54/58/60–63 units remain open. No mathematical program execution, independent proof, required-check increment, subdivision movement or final-page credit.',
    'Seven complete weighted-cycle subsections; complete earlier P333 and UN48 receiving proofs', source=__file__)
print('Weighted-cycle package admitted; original section10 support/tree remainder stays open.')
