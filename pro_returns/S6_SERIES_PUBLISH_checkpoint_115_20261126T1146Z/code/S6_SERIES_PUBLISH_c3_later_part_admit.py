from S6_SERIES_PUBLISH_c3_edit import *
from S6_SERIES_PUBLISH_c3_start import units
import json
import re

folder=ROOT/'agents/continuation3_provenance/later_part'
fragment=folder/'S6_SERIES_PUBLISH_later_part_proposed.tex'
after=fragment.read_text()
guards=json.loads((ROOT/'agents/continuation3_foundations/S6_SERIES_PUBLISH_torus_consolidation_guards.json').read_text())
for guard in guards:
    if guard['key'] in ['P213_exact_local_cycle_name','D28_exact_global_cycle_names']:
        assert after.count(guard['old'])==1,guard['key']
        after=after.replace(guard['old'],guard['new'],1)
        print('Retained already admitted construction consumer:',guard['key'])

text=SOURCE.read_text()
start=r'\section{Tangent cohomology, normalization restrictions and resonance}'
end=r'\section{Connected deformation chains and two independent periods}'
a=text.index(start);b=text.index(end,a);before=text[a:b]
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    for name,count in old.items():assert new[name]==count,name
newtext=text[:a]+after+'\n\n'+text[b:]
for label in ['push:src:E.5.2','push:src:E.5.3']:
    def statement(s):
        i=s.index('\\label{'+label+'}')
        matches=list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary)\}',s[:i]))
        m=matches[-1]; ender='\\end{'+m.group(1)+'}'
        j=s.index(ender,i)+len(ender)
        return s[m.start():j]
    assert statement(text)==statement(newtext),label
SOURCE.write_text(newtext,newline='\n')

for sub,name in [('section12','section12'),('later_part','later')]:
    location=ROOT/'agents/continuation3_provenance'/sub
    for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
                              ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
        _,rows=read_tsv(location/('S6_SERIES_PUBLISH_'+name+'_'+suffix))
        print(name,suffix,append_rows(ROOT/target,rows,key))

oldunits={x[0] for x in units('\\begin{document}\n'+before)}
newunits=list(units('\\begin{document}\n'+after))
path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,rows=read_tsv(path)
removed=[r for r in rows if r['paper']=='II' and r['unit_id'] in oldunits]
assert len(removed)==26*len(oldunits),(len(removed),oldunits)
rows=[r for r in rows if r not in removed]
known={(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in rows}
for unit,title in newunits:
    for criterion in [f'D{x:02}' for x in range(1,26)]+['structure']:
        assert ('II',unit,criterion) not in known,(unit,criterion)
        opened=criterion in ['D14','D23','D24','structure']
        detail=('Final whole-paper placement and organization remain open.' if criterion in ['D14','D24','structure']
            else 'Integrated rendered typography and all final-page readings remain open.' if criterion=='D23'
            else 'Complete original and receiving text read by the provenance agent against all25classes; exact changes and exposed proof comparisons imported. Scope subdivision itself carries no movement credit.')
        rows.append(dict(zip(fields,['II',unit,title,'structure' if criterion=='structure' else 'defect',
            '' if criterion=='structure' else criterion,'open' if opened else 'done',now(),
            'CHECK_EVENTS.tsv; agents/continuation3_provenance/later_part/S6_SERIES_PUBLISH_later_report.md',detail])))
write_tsv(path,fields,rows)
add_event('sec:II:12; sec:II:13; sec:II:14','II-C3-ROOT-LATER-PART-ADMISSION',
    'used and rechecked in this run',
    'Admitted one final receiving fragment with both sec12 and later exact instance/event tables. Complete full-proof comparison credit is the agent exposed reading; root read the full integration report, first receiving global-cohomology blocks, and the complete P213/D2.8 guards. Reapplied the already admitted exact w=a,w_i=a_i and earlier-retraction references before replacement, so the new construction names are preserved. All current old labels/targets retain multiplicity; restored E2 owns01GR. E5.2/E5.3 statement bytes are unchanged. Eleven actual subsection/section units replace six old units; final global order, organization, typography and page reading remain open.',
    'S6_SERIES_PUBLISH_II.tex',source='code/S6_SERIES_PUBLISH_c3_later_part_admit.py')
print('One later part admitted; exact protected statements and current construction consumer edits preserved.')
