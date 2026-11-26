"""Admit exact published-resolution application and reconcile the star navigation aliases."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_provenance/resolution_locator'
prefix='S6_SERIES_PUBLISH_UN11_resolution_'
before=SOURCE.read_text();after=before
_,guards=read_tsv(folder/(prefix+'guards.tsv'))
assert len(guards)==2
for row in guards:
    assert after.count(row['old_text'])==1,row['change_id']
    after=after.replace(row['old_text'],row['new_text'],1)
for old,new in zip(identifiers(before),identifiers(after)):assert old==new
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    if suffix=='CHECK_EVENTS.tsv':assert all(r['type']=='used and rechecked in this run' for r in rows)
    print(suffix,append_rows(ROOT/target,rows,key))
_,rows=read_tsv(folder/(prefix+'sources.tsv'))
sources=[dict(source=r['source_key']+' (third-continuation projective quotient resolution)',
    url=r['url'],version=r['version'],locus=r['locus_read'],date_utc=r['date_utc'],sha256=r['sha256'],
    own_word_summary=r['own_paraphrase'],use=r['exact_application']+' Reading limits: '+r['read_extent']) for r in rows]
print('Sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',sources,'source'))
add_event('cdp:st:C.2.UN.11','II-C3-ROOT-UN11-RESOLUTION-ADMISSION','used and rechecked in this run',
    'Provenance read complete old and receiving UN11 statement/proof and the exact published Bierstone-Milman setup, theorem and remarks. Root read both exact guards and the full application/source comparison. The same projective quotient X embeds in projective space; rho resolves X and sigma resolves its reduced two-value divisor D. The projective blowup maps are isomorphisms on the same punctured family, with the same A and monodromy. The printed statement, nineteen signature rows, parity and Euler modifications remain unchanged. Root claims this bounded receiving comparison, not a new full root proof reading or algorithm-proof check. No independent-check, required-check or final-page credit.',
    'UN11 hidden locator and projective-resolution paragraph',source=__file__)

old=r'\cite[\S1, universal and canonical desingularization]{BierstoneMilman1997}'
new=r'\cite[\S1, Universal and canonical desingularization, arXiv v2 p.~11]{BierstoneMilman1997}'
apply_edit(old,new,'II-C3-BM-CLASS-VII-VERSION',['D18'],
    'cdp:st:C.2.UN.19','UN19 hidden resolution input',
    'Identify the already opened exact preprint version and locus of the equivariant analytic resolution input, matching the current earlier P240 owner. This is a bounded locator correction, not another source reading.')

text=SOURCE.read_text()
start=text.index(r'\begin{proposition}[Reduced Hopf stars with torus smoothings]')
end=text.index(r'\end{proposition}',start)
for label in ['cdp:st:C.2.UN.49','cdp:st:C.2.UN.50','cdp:st:C.2.UN.53']:
    assert r'\label{'+label+'}' in text[start:end]
for n,old in enumerate([
    r'\item \SeriesRef{cdp:st:C.2.UN.49}\quad Exact nonlinear Hopf star criterion and compact realization.'+'\n',
    r'\item \SeriesRef{cdp:st:C.2.UN.50}\quad Complete primary and secondary nonlinear Hopf star criterion.'+'\n'
],1):
    apply_edit(old,'',f'II-C3-FURTHER-STAR-ALIAS-{n:02}',['D12','D15','D24'],
        'cdp:st:C.2.UN.53','Further results',
        'The complete primary, secondary and arbitrary-P star conclusions now have one printed owner with all three original labels. Remove only the duplicate navigation entry; every body statement identity and conclusion remains.')
apply_edit(r'\item \SeriesRef{cdp:st:C.2.UN.53}\quad Complete reduced Hopf-star support criterion.',
    r'\item \SeriesRef{cdp:st:C.2.UN.53}\quad Reduced primary and secondary Hopf stars: the full marked criterion and compact realization.',
    'II-C3-FURTHER-STAR-OWNER',['D15','D24'],'cdp:st:C.2.UN.53','Further results',
    'Describe the complete merged criterion, including the exact primary/secondary and compact-realization scopes, in its one required navigation line.')
add_event('cdp:st:C.2.UN.19;cdp:st:C.2.UN.49;cdp:st:C.2.UN.50;cdp:st:C.2.UN.53',
    'II-C3-STAR-NAVIGATION-BM-LOCATOR','used and rechecked in this run',
    'The three star labels were verified inside the one complete merged statement before consolidating their Further results entries. UN19 receives the version/page qualifier of the already opened P240 resolution source. These are exact navigation/locator comparisons; no theorem, source-reading, independent-check or whole first-part completion credit.',
    'Further results and UN19 hidden source record',source=__file__)
print('Published UN11 resolution locator and exact maps integrated; star navigation aliases consolidated.')
