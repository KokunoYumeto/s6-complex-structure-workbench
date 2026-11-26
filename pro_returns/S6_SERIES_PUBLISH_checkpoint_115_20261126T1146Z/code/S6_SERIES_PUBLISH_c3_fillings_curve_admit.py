from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_conductor'
fragment=folder/'S6_SERIES_PUBLISH_c3_conductor_05_replacement.tex'
before=SOURCE.read_text();after=before
start=r'\subsection{Vertical modifications and component covers}\label{subsec:II:vertical-modification-inputs}'
end=r'\begin{proposition}[No component of a torus degeneration has general-type normalization]\hypertarget{tag-01CS}{}\label{cdp:st:C.2.UN.15}'
assert after.count(start)==after.count(end)==1
left,right=after.index(start),after.index(end)
after=after[:left]+fragment.read_text()+after[right:]
_,remote=read_tsv(folder/'S6_SERIES_PUBLISH_c3_conductor_05_remote_repairs.tsv')
for row in remote:
 assert after.count(row['old_text'])==1,row['statement_id']
 after=after.replace(row['old_text'],row['new_text'],1)
 print('Applied remote',row['statement_id'])
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
 for name,count in old.items():assert new[name]==count,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
 _,rows=read_tsv(folder/('S6_SERIES_PUBLISH_c3_conductor_05_'+suffix))
 print('05',suffix,append_rows(ROOT/target,rows,key))
path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,rows=read_tsv(path)
for row in rows:
 if row['paper']=='II' and row['unit_id']=='subsec:II:vertical-modification-inputs':
  row.update(unit_id='subsec:II:component-field-inputs',unit_title='Translation fields and component surfaces',detail=row['detail']+' Remaining unreviewed material begins at UN.15; this boundary migration earns no closure credit.')
_,incoming=read_tsv(folder/'S6_SERIES_PUBLISH_c3_conductor_05_unit_status.tsv')
for item in incoming:
 criterion=item['criterion'];status=item['status'];detail=item['reason']
 if criterion in ['D14','structure']:status='open';detail+=' Final whole-paper placement remains open.'
 matches=[x for x in rows if x['paper']=='II' and x['unit_id']==item['unit'] and (x['defect_type'] or x['row_kind'])==criterion]
 assert len(matches)<=1
 values=dict(paper='II',unit_id=item['unit'],unit_title=item['title'],row_kind='structure' if criterion=='structure' else 'defect',defect_type='' if criterion=='structure' else criterion,status=status,date_utc=now(),evidence=str(fragment.relative_to(ROOT)),detail=detail)
 if matches:matches[0].update(values)
 else:rows.append(values)
write_tsv(path,fields,rows)
add_event('lem:II:blowup-topology; lem:II:boundary-blowup-groups; cdp:st:C.2.UN.2; cdp:st:C.2.UN.3; cdp:st:C.2.UN.4; cdp:st:C.2.UN.14',
 'II-C3-ROOT-FILLINGS-ADMISSION','used and rechecked in this run',
 'Root read every line of the complete receiving 498-line filling fragment, the37-line blowup owner, and both complete remote receiving proofs UN.2 and P246. The exposed agent comparisons retain all original statements, the integral torsion map, the compact-tube boundary scope, all finite-base-change charts and compact gluing. The n=1 use is the identity on E×Delta, its blowup and O(R) in the already admitted P4.1; the all-n group calculation precedes every torsion obstruction. Main replacement and three remote repairs preserve every old label and target multiplicity. Local statuses are admitted with D14/structure and final PDF gates open. The remaining UN.15 subsection retains its open rows.',
 'S6_SERIES_PUBLISH_II.tex: blowup topology, vertical modifications and distinct fillings',source='code/S6_SERIES_PUBLISH_c3_fillings_curve_admit.py')

folder=ROOT/'agents/continuation3_foundations/sec07'
before=SOURCE.read_text();after=before
for guard in json.loads((folder/'S6_SERIES_PUBLISH_sec07_curve_guards.json').read_text()):
 assert after.count(guard['old'])==1,guard['key']
 after=after.replace(guard['old'],guard['new'],1)
 print('Applied curve',guard['key'])
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
 for name,count in old.items():assert new[name]==count,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
 _,rows=read_tsv(folder/('S6_SERIES_PUBLISH_sec07_curve_'+suffix))
 print('curve',suffix,append_rows(ROOT/target,rows,key))
add_event('lem:II:plane-branch-conductor; night:P4.25; night:P4.34','II-C3-ROOT-PLANE-CONDUCTOR-ADMISSION','used and rechecked in this run',
 'Root read the complete receiving P282 proof. Its exact A-module Hom/Ext sequence supplies all length assertions before the first P4.25 use; the finite map to each normalized branch identifies the residue generators and additional intersection poles. The agent complete old/current P4.25 and P4.34 comparisons are imported as exposed reading. All4 guards match once and preserve labels and targets; the derivative-valuation and conormal-length calculation remains in P4.34. No consumer subsection completion is claimed by this bounded admission.',
 'S6_SERIES_PUBLISH_II.tex: plane-branch conductor owner and applications',source='code/S6_SERIES_PUBLISH_c3_fillings_curve_admit.py')
print('Admitted05 and earlier plane-conductor owner.')
