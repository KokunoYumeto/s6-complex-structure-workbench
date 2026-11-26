"""Admit the complete contracted-boundary unit and exact local support owner."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations/sec07'
prefix='S6_SERIES_PUBLISH_sec07_contracted_'
guards=json.loads((folder/(prefix+'guards.json')).read_text())
assert len(guards)==6
before=SOURCE.read_text();after=before
for row in guards:
 assert after.count(row['old'])==1,row['key']
 after=after.replace(row['old'],row['new'],1)
 print('Applied',row['key'])
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
 for name,count in old.items():assert new[name]==count,name
 for name,count in (new-old).items():assert new[name]==1,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
 _,rows=read_tsv(folder/(prefix+suffix));print(suffix,append_rows(ROOT/target,rows,key))
_,statuses=read_tsv(folder/(prefix+'unit_progress.tsv'))
for row in statuses:
 kind='structure' if row['row']=='restructuring' else row['row']
 if kind in ['D10','D16']:continue
 set_unit_status(row['unit'],kind,row['status'],row['basis'],row['fragment'])
for old,new,tag in [
 (r'\item \SeriesRef{cdp:st:C.2.CR.2}\quad The ruling genus is at most two.',r'\item \SeriesRef{lem:II:contracted-section-duality}\quad Duality and ruling genus for a contracted section.','P293'),
 (r'\item \SeriesRef{cdp:st:C.2.CR.5}\quad A contracted horizontal section is elliptic.'+'\n','','CR5'),
 (r'\item \SeriesRef{cdp:st:C.2.MH.3}\quad The contracted irrational section contributes zero.'+'\n','','MH3'),
 (r'\item \SeriesRef{cdp:st:C.2.UN.10}\quad A contracted irrational horizontal section is elliptic without ambient Betti assumptions.',r'\item \SeriesRef{cdp:st:C.2.UN.10}\quad Contracted irrational sections and their Euler number.','UN10')]:
 apply_edit(old,new,'II-C3-CONTRACTED-RESULTS-'+tag,['D12','D24'],'cdp:st:C.2.CR.2; cdp:st:C.2.CR.5; cdp:st:C.2.MH.3; cdp:st:C.2.UN.10','Further results',
  'Make each consolidated mathematical owner appear once in the further-results list, under its current title. All old statement labels and tags remain at the full receiving owners.')
add_event('subsec:II:contracted-ruled-boundaries; lem:II:proper-conductor-divisor; night:P4R.6; cdp:st:C.2.UN.7',
 'II-C3-ROOT-CONTRACTED-BOUNDARY-ADMISSION','used and rechecked in this run',
 'The foundations reviewer read every complete old/current and receiving proof, including the full R6 and UN7. Root read the full receiving contracted subsection, P300, R6, every remote guard and the complete comparison. P293 and UN9 retain their full proof payloads. CR2, CR5 and MH3 are exact stated restrictions at P293/UN10, with original global hypotheses retained in CR3 and in the Euler clause. P300 proves divisor effectiveness for a compact reduced hypersurface by finite duality and Md=-b, and then proves its proper-torus support clause through the exact unit root and A517 fibre inclusion. CR1/UN7 identify their identical divisors and maps; P452 receives only the general first clause in its separate forthcoming proof. Root verified all six guards, label/target multiplicities and the full old/new owner comparison; further-results aliases are consolidated. This is same-run exposed rechecking, with no independent credit or final-page reading.',
 'S6_SERIES_PUBLISH_II.tex: contracted-boundary unit, P300/R6 and bounded UN7 application',source=__file__)
set_unit_status('night:P4R.6','D12','done','The full shared pullback/duality/intersection proof is at P300; the original global R6 statement applies it to the identical proper fibre and derives its original torsion conclusion.','CHECK_EVENTS.tsv: II-C3-ROOT-CONTRACTED-BOUNDARY-ADMISSION')
print('Contracted subsection and proper conductor owner admitted; global placement and final typography remain open.')
