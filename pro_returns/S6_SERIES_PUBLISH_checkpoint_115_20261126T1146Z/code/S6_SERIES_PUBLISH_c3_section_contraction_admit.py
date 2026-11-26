"""Admit the full section/fibre contraction owner and its ruled-leaf application."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations/sec11'
prefix='S6_SERIES_PUBLISH_sec11_section_contraction_'
before=SOURCE.read_text(); after=before
for row in json.loads((folder/(prefix+'guards.json')).read_text()):
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
for row in statuses:
    kind='structure' if row['row']=='restructuring' else row['row']
    status='open' if kind in ['D14','D23','D24','structure'] else row['status']
    progress.append(dict(zip(fields,['II',row['unit'],'Section and ruling-fibre contractions',
        'structure' if kind=='structure' else 'defect','' if kind=='structure' else kind,status,now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-SECTION-CONTRACTION-ADMISSION',
        row['basis']+' Complete receiving P335 and UN64 read by root; complete original/receiving proofs compared by foundations. New subsection migration earns no movement credit; original sec11 remainder stays open.'])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,progress)
_,sources=read_tsv(folder/(prefix+'sources.tsv'))
incoming=[dict(source=r['source_id']+' (third-continuation section/fibre contraction)',url=r['url'],version=r['version'],
    locus=r['exact_locus']+'; '+r['reader'],date_utc=r['date_utc'],sha256=r['sha256'],own_word_summary=r['own_paraphrase'],
    use='P335 applies the corrected normal-line theorem to (U,T,B,2), with the specified ruling and normal O(-1). Its exact local boundary and weighted normal calculations give the marked degeneration. UN64 uses m=1,r=0,p=q; the separate plane contraction uses (U,T,{p},3).') for r in sources]
print('Sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',incoming,'source'))
add_event('prop:II:section-fibre-contraction;cdp:st:C.2.UN.74;cdp:st:C.2.UN.64',
    'II-C3-ROOT-SECTION-CONTRACTION-ADMISSION','used and rechecked in this run',
    'Foundations read the complete original/current and receiving UN74/P335 and UN64, complete P234, and both exact primary analytic contraction loci. Root read every receiving P335 and UN64 line and the full comparison, source records and scoped statuses. The full weighted construction has one earlier owner P335 with UN74/tag01EL as an alias. All twelve original equation labels and targets remain. The normal-degree criterion, corrected analytic source map (U,T,B,2), first normal/tangent terms, exact blowup chart, weighted normal extension, canonical generator pullback, splitting calculation, full inverse-image Euler formula and compact converse are preserved. UN64 is the exact m=1,r=0,p=q application, yielding M=O, L=K_B and quotient df-prime with the same endpoint frames. Its full statement, classification, residue argument, plane case and compact extension realizations are unchanged. The new actual subsection is before UN64; sec11 unread remainder retains its open identity. Exposed rereading only; no independent-check or final-page credit.',
    'Section and ruling-fibre contraction owner and terminal ruled application',source=__file__)
print('P335/UN74 and complete bounded UN64 application admitted.')
