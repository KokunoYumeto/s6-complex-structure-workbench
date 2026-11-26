from S6_SERIES_PUBLISH_c3_edit import *
import json
folder=ROOT/'agents/continuation3_foundations/sec07'
fragment=folder/'S6_SERIES_PUBLISH_II_sec07_class_vii.tex'
guards=json.loads((folder/'S6_SERIES_PUBLISH_sec07_class_vii_guards.json').read_text())
before=SOURCE.read_text();after=before
for guard in guards:
 assert after.count(guard['old'])==1,guard['key']
 after=after.replace(guard['old'],guard['new'],1)
 print('Applied',guard['key'])
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
 for name,count in old.items():assert new[name]==count,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
 _,rows=read_tsv(folder/('S6_SERIES_PUBLISH_sec07_class_vii_'+suffix))
 print(suffix,append_rows(ROOT/target,rows,key))
import_restructured_status(set(),fragment,folder/'S6_SERIES_PUBLISH_sec07_class_vii_unit_progress.tsv')
add_event('cdp:st:C.2.VII.1; cdp:st:C.2.VII.2; cdp:st:C.2.VII.3; cdp:st:C.2.VII.4; night:P4.23; cdp:st:C.2.INT.3',
 'II-C3-ROOT-CLASS-VII-ADMISSION','used and rechecked in this run',
 'Root read the complete early VII.1 and the complete receiving class-VII subsection, then reread the amended P244 classification citation and the separate sigma/pi isomorphism arguments. The agent full old/current P4.23 and INT.3 comparisons are imported as exposed reading. All11 guards matched once and all old labels and targets retain their multiplicity. The root requires P244 at the nonempty effective divisor, P246 for torsion-character descent, and P243 after P291 to prove that the normalization resolution itself is an isomorphism. Local section status is imported; final global placement and PDF gates remain open.',
 'S6_SERIES_PUBLISH_II.tex: class VII minimal-model prerequisite and canonical-boundary subsections',source='code/S6_SERIES_PUBLISH_c3_class_vii_admit.py')
print('Admitted class-VII owners and exact applications.')
