"""Admit the fully compared Hopf boundary, topology and toric units."""
from S6_SERIES_PUBLISH_c3_edit import *

folder = ROOT/'agents/continuation3_provenance/hopf_toric'
prefix = 'S6_SERIES_PUBLISH_hopf_toric_'
_, guards = read_tsv(folder/(prefix+'guards.tsv'))
assert len(guards) == 3
before = SOURCE.read_text()
after = before
for row in guards:
    assert after.count(row['old_text']) == 1, row['change_id']
    after = after.replace(row['old_text'], row['new_text'], 1)
    print('Applied', row['change_id'])
preserve_identifiers(before, after)
for old, new in zip(identifiers(before), identifiers(after)):
    assert all(new[k] == v for k,v in old.items())
    assert all(new[k] == 1 for k in new-old)
SOURCE.write_text(after, newline='\n')
for suffix, target, key in [
    ('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
    ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _, rows = read_tsv(folder/(prefix+suffix))
    print(suffix, append_rows(ROOT/target, rows, key))

fields, progress = read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
old_units = {'subsec:II:hopf-component-boundaries','cdp:st:C.2.UN.68'}
retained = [r for r in progress if not(r['paper']=='II' and r['unit_id'] in old_units)]
_, proposed = read_tsv(folder/(prefix+'unit_status.tsv'))
titles = dict((m.group(2),m.group(1)) for m in re.finditer(
    r'^\\subsection\{([^\n]+)\}\\label\{([^}]+)\}', after, re.M))
unit_map = {'subsec:II:rational-toric-components':'cdp:st:C.2.UN.68'}
seen = set()
for row in proposed:
    unit = unit_map.get(row['unit'],row['unit'])
    kind = row['defect_type']
    status = 'open' if kind in ['D14','D23'] else 'done'
    detail = row['outcome']
    if kind == 'D14':
        detail += ' Final whole-paper placement and the contiguous UN64–68 move remain open.'
    if kind in ['D15','D24']:
        detail = 'No instance in this mathematical body unit; the separate front-matter units retain their own open criteria.'
    retained.append(dict(zip(fields, [
        'II',unit,titles[row['unit']],'defect',kind,status,now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-HOPF-TORIC-ADMISSION',detail])))
    seen.add((unit,row['unit']))
for unit, heading in sorted(seen):
    retained.append(dict(zip(fields,[
        'II',unit,titles[heading],'structure','', 'open',now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-HOPF-TORIC-ADMISSION',
        'Complete local ownership and proof comparison admitted; final whole-paper placement remains open. Subdivision and alias migration earn no movement credit.'])))
assert len(seen)==5 and len(proposed)==125
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in retained]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,retained)

_, sources = read_tsv(folder/(prefix+'sources.tsv'))
source_rows=[]
for row in sources:
    source_rows.append(dict(
        source=row['source_key']+' (third-continuation Hopf and toric comparison)',
        url=row['url'],version=row['version'],
        locus=row['locus_read']+'; '+row['read_extent'],
        date_utc=row['date_utc'],sha256=row['sha256'],
        own_word_summary=row['own_paraphrase'],use=row['exact_application']))
print('Primary readings',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',source_rows,'source'))
add_event('cdp:st:C.2.UN.38;cdp:st:C.2.UN.39;cdp:st:C.2.UN.44;cdp:st:C.2.UN.47;cdp:st:C.2.UN.68',
    'II-C3-ROOT-HOPF-TORIC-ADMISSION','used and rechecked in this run',
    'The delegated reviewer read every complete original and receiving proof; root read the complete comparison and all five receiving proofs, then the full corrected UN38 and UN47 items. The P248 statement was checked directly and its axis-list overreach corrected by the precise freshly opened Abasheva–Deev loci, with z^q/w^p excluding resonance at algebraic dimension zero. The UN47 common resolution uses the same maps to the component normalization and exact analytic point-blowup factorization. Canonical-neighbourhood powers, higher jets, all nineteen index rows, full-support blowup maps, meridian/root covers, integral lattices, hocolimit and dual-complex maps, finite component-cover degrees, subgroup separability and geometric-genus consequences remain. UN68 retains the full residue, rationality, cochain and Euler arguments; GHK rho/tau apply to the proved projective pair, their factorization computes charge, and fan-ray deletion descends the action to that given pair. All old targets and labels occur exactly once at their receiving owners. D10/D16 remain done; global placement and final rendered typography stay open. No independent derivation or final-page credit.',
    'Complete Hopf boundary/topology and toric units; exact C.ZC.8 alias at P234',source=__file__)
print('Five local units admitted; stable UN38 and UN68 unit identities preserved.')
