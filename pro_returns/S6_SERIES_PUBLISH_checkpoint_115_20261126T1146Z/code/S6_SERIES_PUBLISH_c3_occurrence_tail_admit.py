"""Admit complete Hopf/ruled occurrence receivers and the elliptic root owner."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_provenance/occurrence_tail'
prefix='S6_SERIES_PUBLISH_tail_'
before=SOURCE.read_text(); after=before
_,guards=read_tsv(folder/(prefix+'guards.tsv'))
assert len(guards)==5
for row in guards:
    assert after.count(row['old_text'])==1,row['change_id']
    after=after.replace(row['old_text'],row['new_text'],1)
assert after.index('\\label{lem:II:moving-marked-cycle}')<after.index('\\label{cdp:st:C.2.UN.41}')
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
_,statuses=read_tsv(folder/(prefix+'unit_status.tsv'))
bounded='subsec:II:elliptic-root-fillings (bounded P336/UN6 change)'
incoming={r['unit'] for r in statuses if r['unit']!=bounded}
assert len(incoming)==4
progress=[r for r in progress if not(r['paper']=='II' and r['unit_id'] in incoming)]
titles={label:title for title,label in re.findall(r'^\\subsection\{([^\n]+)\}\\label\{([^}]+)\}',after,re.M)}
for row in statuses:
    if row['unit']==bounded:continue
    kind=row['type']; status='open' if kind in ['D14','D18','D23','D24'] else 'done'
    progress.append(dict(zip(fields,['II',row['unit'],titles.get(row['unit'],row['unit']),
        'defect',kind,status,now(),'CHECK_EVENTS.tsv: II-C3-ROOT-OCCURRENCE-TAIL-ADMISSION',
        row['evidence']+' Provenance read complete original and receiving proofs; root read every complete receiving proof and the comparison. P329/P333 are already admitted before UN41. Whole-paper order, bibliography, first part and final pages remain open. The original occurrence remainder stays open; no subdivision movement credit.'])))
for unit in sorted(incoming):
    progress.append(dict(zip(fields,['II',unit,titles[unit],'structure','','open',now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-OCCURRENCE-TAIL-ADMISSION',
        'The complete receiving subsection has one proof for each construction and explicit maps to shared owners. Final integrated whole-paper order remains open.'])))
for row in progress:
    if row['paper']=='II' and row['unit_id'] in ['subsec:II:marked-cycle-lattices','subsec:II:moving-marked-cycles'] and row['defect_type']=='D12':
        assert row['status']=='open'
        row.update(status='done',date_utc=now(),evidence='CHECK_EVENTS.tsv: II-C3-ROOT-OCCURRENCE-TAIL-ADMISSION',
            detail='UN41 now applies the admitted P329/P333 before it: two minus-swap edges, identical core/neck charts, opposite cycle generator, second-core maps differing by the exact integral cycle period, and inverse base map tau=Q(t). Root and provenance read the complete receiving proof; the duplicate plumbing/coframe proofs have one earlier owner.')
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,progress)
_,sources=read_tsv(folder/(prefix+'sources.tsv'))
incoming=[dict(source=r['source_key']+' (third-continuation occurrence tail)',url=r['url'],version=r['version'],
    locus=r['locus_read']+'; '+r['read_extent'],date_utc=r['date_utc'],sha256=r['sha256'],own_word_summary=r['own_paraphrase'],
    use=r['exact_application']) for r in sources]
print('Sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',incoming,'source'))
add_event('lem:II:elliptic-root-surface;cdp:st:C.2.UN.6;cdp:st:C.2.UN.41;cdp:st:C.2.UN.42;cdp:st:C.2.UN.43;cdp:st:C.2.UN.45;def:II:marked-normal-cycle;lem:II:moving-marked-cycle',
    'II-C3-ROOT-OCCURRENCE-TAIL-ADMISSION','used and rechecked in this run',
    'Provenance read complete original and receiving UN6/41/42/43/45, the complete P336/P329/P333 owners and the named complete inputs. Root read the complete receiving P336/UN6/41/42/43/45 proofs, full comparison and exact source records. P336 retains arbitrary elliptic B, complex contraction beta and m>=1; its explicit phase isotopy identifies the whole integral pair, and the identity on UN6 plus (a,ell)=(x,z e) on UN42 preserves every chart, deck map and product inverse. UN6 statement is byte-identical and its ambient ER3–11 duplicate remains for the separate P339 transfer. UN41 applies the identical two-edge P333 plumbing and its full punctured quotient through the stated integral-period and inverse-base maps. All nodal pencil, Tate, suspension, nonlinear weighted quotient, secondary finite action, ruled all-genus construction and cohomology maps remain proved. P327/P337/P234 and the exact opened source statements replace only their duplicated arguments. All original labels and targets retain exact multiplicity. No independent proof, required-check increment, program execution or final-page credit. Original occurrence remainder and final integrated gates stay open.',
    'Elliptic root surface; diagonal, nonlinear and secondary Hopf occurrence; ruled occurrence; exact P329/P333 application',source=__file__)
print('Five tail guards admitted; four actual subsection assessments and the exact earlier cycle-owner D12 applications recorded.')
