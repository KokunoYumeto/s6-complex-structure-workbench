"""Admit fully compared elliptic lifts and close the exhausted original sec09 remainder."""
from S6_SERIES_PUBLISH_c3_edit import *
import hashlib

folder = ROOT / 'agents/continuation3_provenance/equivariant_lift'
prefix = 'S6_SERIES_PUBLISH_lift_'
before = SOURCE.read_text()
after = before
_, guards = read_tsv(folder / (prefix + 'guards.tsv'))
assert len(guards) == 8
for row in guards:
    assert after.count(row['old_text']) == 1, row['change_id']
    after = after.replace(row['old_text'], row['new_text'], 1)
preserve_identifiers(before, after)
for old, new in zip(identifiers(before), identifiers(after)):
    assert all(new[k] == v for k, v in old.items())
    assert all(new[k] == 1 for k in new - old)

def statement(text, tag):
    pos = text.index(r'\hypertarget{tag-' + tag + '}{}')
    start = text.rfind(r'\begin{', 0, pos)
    env = re.match(r'\\begin\{([^}]+)\}', text[start:]).group(1)
    end = text.index(r'\end{' + env + '}', pos) + len(r'\end{' + env + '}')
    return text[start:end]

for tag, digest in {
    'P306': '88c977958cb2fabec31aaf49c3099a99c14c5dd45b20c4f5854ad7b7acf6839f',
    'P317': 'f60f9b5bd3f11e945854e60071494b63a719616597adf7c1c489ab5c175daba7',
    '01D9': 'd75f822a0ac56cd7e406d6384b703b95090581235628bf4ec75208cdcf6ddcf5',
}.items():
    if tag == '01D9':
        pos = before.index(r'\label{cdp:st:C.2.UN.31}')
        tag = re.findall(r'\\hypertarget\{tag-([^}]+)\}', before[before.rfind(r'\begin{', 0, pos):pos])[-1]
    old_statement = statement(before, tag)
    assert hashlib.sha256(old_statement.encode()).hexdigest() == digest, tag
    assert old_statement == statement(after, tag), tag

def proof_after(text, tag):
    pos = text.index(r'\hypertarget{tag-' + tag + '}{}')
    start = text.index(r'\begin{proof}', pos)
    end = text.index(r'\end{proof}', start) + len(r'\end{proof}')
    return text[start:end]
assert proof_after(before, 'P337') == proof_after(after, 'P337')
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

_, source_rows = read_tsv(folder / (prefix + 'sources.tsv'))
sources = [dict(
    source=row['source_key'] + ' (third-continuation equivariant elliptic lift)',
    url=row['url'], version=row['version'], locus=row['locus_read'],
    date_utc=row['date_utc'], sha256=row['sha256'],
    own_word_summary=row['own_paraphrase'],
    use=row['exact_application'] + ' Reading scope: ' + row['read_extent']
) for row in source_rows]
print('Sources', append_rows(ROOT / 'S6_SERIES_PUBLISH_c3_primary_readings.tsv', sources, 'source'))

fields, progress = read_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
_, assessments = read_tsv(folder / (prefix + 'unit_status.tsv'))
scopes = {'subsubsec:II:elliptic-torsor-lifts', 'subsubsec:II:cyclic-elliptic-quotients', 'subsubsec:II:elliptic-hopf-occurrence'}
actual_unit = 'subsec:II:enriques-elliptic-occurrence'
assert not any(row['paper'] == 'II' and row['unit_id'] == actual_unit for row in progress)
event = 'II-C3-ROOT-ELLIPTIC-LIFT-ADMISSION'
read_scope = (' Provenance read every complete old/current and receiving statement and proof; root read the complete new P344/P345/P346/P348 owners, UN34/35/37 and the full P306/UN31/P317/P337 receiving blocks, the comparison and source rows. The three subsubsections constitute this one actual subsection. Bounded P306/UN31/P317/P337 changes confer no containing-unit closure. All source-reading and final-page limits remain explicit.')
open_kinds = {'D14', 'D18', 'D23', 'D24', 'structure'}
for kind in [f'D{i:02d}' for i in range(1,26)] + ['structure']:
    items = [x for x in assessments if x['unit'] in scopes and x['type'] == kind]
    assert len(items) == (0 if kind == 'structure' else 3)
    basis = ' '.join(dict.fromkeys(x['evidence'] for x in items)) if items else 'Local order is compared; global section placement and final subsection spans remain pending.'
    if kind == 'D15':
        basis = 'No front-matter instance occurs in this body subsection. First-part and original-section global correspondence remain open.'
    progress.append(dict(zip(fields, ['II', actual_unit, 'Elliptic torsors and Hopf components',
        'structure' if kind == 'structure' else 'defect', '' if kind == 'structure' else kind,
        'open' if kind in open_kinds else 'done', now(), 'CHECK_EVENTS.tsv: ' + event, basis + read_scope])))

original_read_scope = ('Original sec09 owners UN6/8/13/18/21/25/27/30 were fully compared in the earlier admitted root packages; the admitted occurrence-tail package fully compared UN41/42/43/45 and UN6; the present full receiving comparison completes UN34/35/37. Provenance reconciled this exact original owner inventory with current II and the admissions on 22 November 2026. The original unread remainder is exhausted by these full comparisons, not by subdivision. The three new subsubsections do not create ledger units or movement credit. Global D14/D15/D18/D23/D24 and structure remain open; inherited D10/D16 remain done.')
original_open = open_kinds | {'D15'}
original_count = 0
for row in progress:
    if row['paper'] == 'II' and row['unit_id'] == 'sec:II:09':
        kind = row['defect_type'] or row['row_kind']
        row.update(status='open' if kind in original_open else 'done', date_utc=now(),
                   evidence='CHECK_EVENTS.tsv: ' + event, detail=original_read_scope)
        original_count += 1
assert original_count == 26
keys = [(row['paper'], row['unit_id'], row['defect_type'] or row['row_kind']) for row in progress]
assert len(keys) == len(set(keys))
write_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', fields, progress)

add_event('def:II:elliptic-root-curve;lem:II:equivariant-elliptic-torsor-lift;cdp:st:C.2.UN.34;cdp:st:C.2.UN.35;cdp:st:C.2.UN.37;cdp:st:C.2.UN.31;lem:II:identity-monodromy-elliptic;lem:II:local-cyclic-elliptic;lem:II:hopf-curve-restriction;sec:II:09',
          event, 'used and rechecked in this run',
          'Complete compared receivers admitted with eight exact guards and all old labels/targets at their original multiplicity. P306/P317/UN31 complete statement hashes agree and P337 proof is unchanged. P344 gives the reduced-Cartier normalized root chart before the smooth-elliptic clause. P345 gives the same full torsor and finite descent through the exact marked lattice map and algebraic torus lift; the cited C1/Steinberg result is applied to P. P346 preserves the explicit integral character comparisons. P348 proves the exact finite-kernel bielliptic orbit pencil. UN34/35/37 retain all full component, multiplicity, monodromy, punctured-product, quotient and Euler conclusions. The erroneous general torus-quotient citation to current K3-scoped UN24 is replaced by the full (A x P1)/G map and strict-component resolution comparison; no theorem is refuted or narrowed. The original sec09 body remainder is exhausted by the exact owner inventory and admitted full comparisons. These are used-and-rechecked events, with no new independent proof, required-check increment, final-page credit or subdivision movement credit.',
          'One complete elliptic-occurrence subsection and bounded root/orbit/Hopf receivers; original sec09 inventory', source=__file__)

report = ROOT / 'S6_SERIES_PUBLISH_report.md'
report_text = report.read_text()
note = ('## Paper II current proof-scope repair — elliptic occurrence\n\n'
        'The final UN35 paragraph cited current UN24 for the full torus-quotient class, although the current shared UN24/UN32 result has the K3 symplectic domain. The complete replacement constructs (A × P1)/G with faithful base character T=t^|G| for the given two-torus A and cyclic G, identifies the generic fibre with A and the distinguished quotient with A/G, and follows the same component through compact analytic resolution and minimal contraction. Thus UN35 retains its full original statement. This is an intermediate proof-citation scope error, not a refutation of that statement. The exact old/new text and comparisons are recorded in the elliptic-lift defect rows and II-C3-ROOT-ELLIPTIC-LIFT-ADMISSION.\n\n')
assert note not in report_text
report.write_text(report_text.replace('# S6 series publication revision\n\n', '# S6 series publication revision\n\n' + note, 1), newline='\n')
print('Elliptic lift admitted; original sec09 local remainder closed; global gates retained.')
