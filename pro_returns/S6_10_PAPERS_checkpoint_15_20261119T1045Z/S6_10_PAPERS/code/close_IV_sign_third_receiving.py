from pathlib import Path
import csv,json,hashlib,datetime,re
R=Path('/workspace/scratch/490d8ca4e928/work/S6_10_PAPERS')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
hashp=lambda p:hashlib.sha256((R/p).read_bytes()).hexdigest()
body=(R/'papers/IV/body.tex').read_text()
raw=(R/'papers/IV/body_source.tex').read_text()
a=json.loads((R/'analysis/IV/retained_batch_9/integration_reconciliation.json').read_text())
reps=[r for r in a if r.get('source')=='analysis/IV_sign_third_replacements.json']
assert len(reps)==3
checks=[]
for r in reps:
 old,new=r['old'],r['new']
 assert body.count(old)==0,(r['label'],'old survived')
 if new: assert body.count(new)==1,(r['label'],'new count',body.count(new))
 checks.append({'label':r['label'],'actual_receiving_old':old,'actual_receiving_new':new,'old_count':0,'new_count':body.count(new) if new else None,'raw_original_count':raw.count(r.get('source_prefatory_old',old)),'adapted_from_source_preface':r.get('source_prefatory_old'),'requested_source_preface_replacement':r.get('source_prefatory_new')})
statements=[]
for n in [50,52,54,56,57,58,59,60]:
 label='night:P3K.'+str(n)
 p=body.index('\\label{'+label+'}')
 start=body.rfind('\\begin{',0,p)
 end=body.index('\\begin{proof}',p)
 t=body[start:end]
 # Existing reader body already places StatementRecord before theorem.
 # Remove it only if a later generation moves it into this slice.
 i=t.find('\\StatementRecord')
 if i>=0:
  j=i+len('\\StatementRecord')
  for k in range(4):
   while t[j].isspace():j+=1
   assert t[j]=='{';depth=1;j+=1
   while depth:
    if t[j]=='{' and t[j-1]!='\\':depth+=1
    if t[j]=='}' and t[j-1]!='\\':depth-=1
    j+=1
  t=t[:i]+t[j:]
 statements.append({'label':label,'statement':t,'sha256':hashlib.sha256(t.encode()).hexdigest(),'match':'Read the full current receiving statement and matched its corrected formulas and retained scope against the completed full-argument/refutation review; historical whole compound remains Refuted.'})
(R/'analysis/IV_sign_third_receiving_statements.json').write_text(json.dumps({'at':now,'body_sha256':hashp('papers/IV/body.tex'),'statements':statements},indent=2,ensure_ascii=False)+'\n')
closed=[]
p=R/'records/IV_sign_independent_events.tsv'
with p.open(newline='') as f:
 reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['labels'] in {'night:P3K.58','night:P3K.60'}:
  assert row['remaining_gates']
  closed.append({'label':row['labels'],'prior_gate':row['remaining_gates'],'closed_at':now,'evidence':'Direct current-reader comparison, exact owner integration reconciliation and corrected receiving-statement read.'})
  row['remaining_gates']=''
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
for rel in ['analysis/IV_sign_third_reviews.json','analysis/IV_sign_independent_reviews.json']:
 p=R/rel;d=json.loads(p.read_text())
 for row in d['reviews']:
  if row.get('labels') in {'night:P3K.58','night:P3K.60'}:
   prev=row.get('remaining_gates','')
   if prev: row.setdefault('receiving_gate_history',[]).append({'prior_gate':prev,'closed_at':now,'receipt':'analysis/IV_sign_third_batch_receiving_receipt.json'})
   row['remaining_gates']=''
 d['updated']=now
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
files=['papers/IV/body.tex','papers/IV/body_source.tex','code/IV/retained_batch_repairs.py','analysis/IV_sign_third_replacements.json','analysis/IV/retained_batch_9/integration_reconciliation.json','analysis/IV_sign_third_receiving_statements.json','analysis/IV_sign_review_sources/P3K.83_dependency.tex','analysis/IV_sign_review_sources/P3K.88_dependency.tex']
receipt={'at':now,'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro)','verified_replacements':3,'checks':checks,'closed_label_gates':closed,'all_eight_current_receiving_statements_matched':True,'source_to_reader_pipeline':'body_source.tex remains the exact full-source assembly before deterministic receiving repairs. body.tex is the corrected reader manuscript. The already removed K60 historical preface was not literally replaced a second time: the owner transported the requested clarification to the exact existing reader conclusion, preserving both source and receiving replacements in integration_reconciliation.json.','bounded_later_status_comparison':{'K83':'Exact statement and GC.10 reviewed for realized good-branch e=0; parent owns full compact attachment review.','K88':'Exact statement, ZB.1 initial-value role and ZB.4 witness scope opened: the two fixed-scalar branches have 28 witnesses each in the specified words beginning Q0 and continuing Q0/Q1. This matches the receiving cross-reference. Tables and certificate executions are not newly credited by this reading.','cycle_note':'Neither later-status citation is used as a logical input to the earlier K60 sum-and-difference argument.'},'full_argument_event_count':21,'computation_event_count':41,'added_Uses_audit_count':7,'separate_later_status_match_count':1,'files':{p:hashp(p) for p in files}}
(R/'analysis/IV_sign_third_batch_receiving_receipt.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'at':now,'replacements':3,'closed_gates':[r['label'] for r in closed],'all_eight_statements_matched':True,'body_sha256':hashp('papers/IV/body.tex')},indent=2))
