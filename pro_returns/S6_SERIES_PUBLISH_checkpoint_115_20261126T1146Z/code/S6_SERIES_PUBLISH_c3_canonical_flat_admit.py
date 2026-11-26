"""Admit canonical direct-image transport and the full canonical-flat comparison."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations/sec11'
prefix='S6_SERIES_PUBLISH_sec11_canonical_flat_'
before=SOURCE.read_text(); after=before
guards=json.loads((folder/(prefix+'guards.json')).read_text())
assert len(guards)==3
for row in guards:
    assert after.count(row['old'])==1,row['key']
    after=after.replace(row['old'],row['new'],1)
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    assert all(new[k]==v for k,v in old.items())
    assert all(new[k]==1 for k in new-old)
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    for row in rows:
        if suffix=='CHECK_EVENTS.tsv' and 'effort' not in row['who']:
            row['who']+='; effort setting not separately exposed'
    print(suffix,append_rows(ROOT/target,rows,key))
fields,progress=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
_,statuses=read_tsv(folder/(prefix+'unit_progress.tsv'))
incoming={r['unit'] for r in statuses}
progress=[r for r in progress if not(r['paper']=='II' and r['unit_id'] in incoming)]
titles={label:title for title,label in re.findall(r'^\\subsection\{([^\n]+)\}\\label\{([^}]+)\}',after,re.M)}
for row in statuses:
    kind='structure' if row['row']=='restructuring' else row['row']
    status='open' if kind in ['D14','D23','D24','structure'] else row['status']
    progress.append(dict(zip(fields,['II',row['unit'],titles.get(row['unit'],row['unit']),
        'structure' if kind=='structure' else 'defect','' if kind=='structure' else kind,status,now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-CANONICAL-FLAT-ADMISSION',
        row['basis']+' Foundations read all complete original/current and receiving proofs. Root read complete P340/UN75/P343 and comparison, and every changed P335 line against its earlier completely read proof. Global order and the original section11 remainder remain open; subdivisions earn no movement credit.'])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,progress)
_,sources=read_tsv(folder/(prefix+'sources.tsv'))
incoming=[dict(source=r['source_id']+' (third-continuation canonical-flat comparison)',url=r['url'],version=r['version'],
    locus=r['exact_locus']+'; '+r['reader'],date_utc=r['date_utc'],sha256=r['sha256'],own_word_summary=r['own_paraphrase'],
    use='The exact analytic good-degeneration and local modification maps are applied to the same total spaces, canonical orders and normalized branches. Source reading is limited to the recorded printed passages and statements; no omitted proof is credited.') for r in sources]
print('Sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',incoming,'source'))
add_event('def:II:overlap-compatible-modification;lem:II:canonical-bimeromorphic-direct-image;cdp:st:C.2.UN.75;prop:II:section-fibre-contraction',
    'II-C3-ROOT-CANONICAL-FLAT-ADMISSION','used and rechecked in this run',
    'Foundations read complete original/current/receiving UN75 and P335, the full overlap datum, full new P340/P343 and the complete P236/P234 inputs. Root read all of P340/UN75/P343 and the comparison, and every changed P335 line in its bounded old/new diff against the previously read complete proof. P343 preserves the full canonical direct-image argument and its surviving-divisor orders; P335 uses the same ordinary curve blowdown and keeps its statement and Jacobian discrepancy. P340 records the actual arrows and overlap isomorphisms. UN75 builds the proper composite graph, applies P236 only between smooth endpoints, and preserves the full canonical-flat criterion, inverse analytic reconstruction, normalized branches and singular-centre Euler formula. Its type-II contraction uses the exact Fujiki–Nakano normal-line theorem on the specified P1 by P1 exceptional surface; the narrower one-section P335 is not used there. Every original label/target has exact multiplicity. No independent proof, required-check increment, final-page or subdivision movement credit.',
    'Canonical direct images; analytic modification data; canonical-flat reduction; bounded section-contraction application',source=__file__)
print('P340/P343, full UN75 and bounded P335 application admitted.')
