from pathlib import Path
import csv,json
root=Path(__file__).resolve().parents[1]
path=root/'CHECK_EVENTS.tsv'
with path.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;events=list(r)
changes=[]
for e in events:
 if e['statement_id']=='night:P3F.21' and 'degree28 page' in e['outcome']:
  old=e['outcome'];e['outcome']=old.replace('degree28 page','degree-four elliptic page')
  changes.append({'event_id':e['event_id'],'old_outcome':old,'new_outcome':e['outcome']})
with path.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
(root/'IV_known_input_table_correction.json').write_text(json.dumps({'reason':'Audit table transcription corrected against F21 section6: the base cover has degree4, with4 I7 fibres and8 I1;28 is not its cover degree. No manuscript equation or proof changed.','changes':changes},ensure_ascii=False,indent=2)+'\n')
print('Corrected',len(changes),'source-review event outcome; stable event identifier retained.')
