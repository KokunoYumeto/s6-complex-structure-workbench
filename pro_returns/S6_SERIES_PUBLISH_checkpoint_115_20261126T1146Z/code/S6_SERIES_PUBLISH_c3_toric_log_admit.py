"""Admit the complete toric-log and compact-occurrence comparisons."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder = ROOT/'agents/continuation3_foundations/sec11'
prefix = 'S6_SERIES_PUBLISH_sec11_toric_log_'
before = SOURCE.read_text()
after = before
guards = json.loads((folder/(prefix+'guards.json')).read_text())
assert len(guards)==4
for guard in guards:
    assert after.count(guard['old'])==1,(guard['key'],after.count(guard['old']))
    preserve_identifiers(guard['old'],guard['new'])
    after=after.replace(guard['old'],guard['new'],1)
old_labels,old_tags=identifiers(before)
new_labels,new_tags=identifiers(after)
assert old_tags==new_tags
assert not old_labels-new_labels
assert new_labels-old_labels==Counter({
    'subsec:II:toric-central-log-spaces':1,
    'subsec:II:compact-toric-occurrence':1})
assert guards[2]['old'].split(r'\end{proposition}',1)[0]==guards[2]['new'].split(r'\end{proposition}',1)[0]
for label in ['push:src:E.5.2','push:src:E.5.3']:
    def statement(t):
        i=t.index(r'\label{'+label+'}')
        a=t.rfind(r'\begin{',0,i)
        env=re.match(r'\\begin\{([^}]+)\}',t[a:])[1]
        b=t.index(r'\end{'+env+'}',i)+len(r'\end{'+env+'}')
        return t[a:b]
    assert statement(before)==statement(after),label
assert after.count(r'\label{cdp:eq:C.WF.18}')==before.count(r'\label{cdp:eq:C.WF.18}')==1

_,statuses=read_tsv(folder/(prefix+'unit_progress.tsv'))
assert len(statuses)==52
units={r['unit'] for r in statuses}
assert units=={'subsec:II:toric-central-log-spaces','subsec:II:compact-toric-occurrence'}
fields,progress=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
assert not any(r['paper']=='II' and r['unit_id'] in units for r in progress)
titles={label:title for title,label in re.findall(r'^\\subsection\{([^\n]+)\}\\label\{([^}]+)\}',after,re.M)}
for row in statuses:
    kind='structure' if row['row']=='restructuring' else row['row']
    progress.append(dict(zip(fields,['II',row['unit'],titles[row['unit']],
        'structure' if kind=='structure' else 'defect','' if kind=='structure' else kind,
        'open' if kind in {'D14','D23','D24','structure'} else row['status'],now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-TORIC-LOG-ADMISSION',
        row['basis']+' Foundations read complete old/current and receiving UN71/UN73 and the full bounded UN76 receiver. '
        'Root read both complete UN71/UN73 receivers, the exact two UN76 application changes against its previously read complete proof, '
        'all comparison/status/equation/source/event records and the final closing-sentence changes. '
        'Original sec11 and its remaining reduction units remain open. No subdivision, independent-check, required-check or final-page credit.'])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys)==len(set(keys))
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
                         ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    if suffix=='CHECK_EVENTS.tsv':
        assert all(r['type']=='used and rechecked in this run' and 'effort' in r['who'] for r in rows)
    print(suffix,append_rows(ROOT/target,rows,key))
SOURCE.write_text(after,newline='\n')
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,progress)
_,sources=read_tsv(folder/(prefix+'sources.tsv'))
incoming=[dict(source=r['source_id']+' (third-continuation toric log spaces)',url=r['url'],version=r['version'],
    locus=r['exact_locus']+'; '+r['reader'],date_utc=r['date_utc'],sha256=r['sha256'],
    own_word_summary=r['own_paraphrase'],
    use='Foundations freshly opened the exact stated primary loci and their complete proofs where specified. '
        'Root read the receiving central-space and log-section morphisms, source comparison and attribution. '
        'No additional root primary-source reading or journal-proof reading is claimed.') for r in sources]
print('Sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',incoming,'source'))
add_event('cdp:st:C.2.UN.71;cdp:st:C.2.UN.73;cdp:st:C.2.UN.76',
    'II-C3-ROOT-TORIC-LOG-ADMISSION','used and rechecked in this run',
    'Four exact guards admitted after the complete exposed foundations old/current/receiving comparisons. '
    'Root read all UN71 and UN73 receiving statements/proofs, both UN76 changed applications against its previously completely read proof, '
    'and the full comparison, all-class status, source, event and equation records. '
    'UN71 identifies the same analytic central log space with the proper algebraic toric conductor colimit, '
    'the constant smoothing sections, normalized log structure and exact Gross--Siebert gluing cocycle. '
    'Its single occurrence construction now states the full holomorphic Gamma-to-T_N homomorphism family already used by its consumers: '
    'commuting shears, uniform K(t)/log|t| bounds, barycentric properness, independent periods and invariant canonical form. '
    'UN73 applies it through d0(u) and dInfinity(v), with u=kappa*t, v=kappa/t and the explicit exponential quotient maps; '
    'its complete determinant proof remains. The two UN76 applications use their exact period homomorphisms and coarsening maps; '
    'its statement and all other paragraphs/equations remain unchanged. Final recap sentences are removed after rereading. '
    'All old targets remain, no new tag is used, and E.5.2/E.5.3 statements are byte-identical. '
    'The cited Gross--Siebert v3 and the journal metadata are distinguished explicitly. '
    'Original sec11 and global/final-page gates stay open; no independent-check, required-check or subdivision credit.',
    'Toric central log spaces; compact toric occurrence; bounded UN76 filling applications; Gross--Siebert entry',
    source='code/S6_SERIES_PUBLISH_c3_toric_log_admit.py')
print('Toric-log package admitted; original section11 reduction remainder remains open.')
