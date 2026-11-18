"""Consolidate actual current events, preserving scopes and source rows."""
from pathlib import Path
import csv,re,json
OUT=Path(__file__).resolve().parents[1]
paths=sorted((OUT/'records').glob('*events.tsv'))+sorted((OUT/'analysis').glob('*/current_check_events.tsv'))
types={'D':'targeted proof check','C':'computation or formal certificate','S':'used and rechecked in this run','R':'refuted, with correction recorded','E':'editorial reconciliation; no proof check awarded'}
rows=[];provenance=[]
for p in paths:
 for n,r in enumerate(csv.DictReader(p.open(),delimiter='\t'),2):
  labels=r.get('statement_id') or r.get('label') or r.get('labels') or ''
  who=r.get('who') or r.get('checker') or ''
  if who.startswith('GPT-6 Astra'):
   who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS'
  typ=types.get(r.get('type'),r.get('type',''))
  outcome=' '.join(r[k] for k in ('verdict','scope','derivation','outcome','independence') if r.get(k))
  for label in re.split(r'\s*;\s*',labels):
   row={'statement_id':label,'date':r.get('date') or r.get('recorded_at') or '', 'who':who,'type':typ,'outcome':outcome}
   rows.append(row);provenance.append({'output_row':len(rows)+1,'source':str(p.relative_to(OUT)),'source_row':n})
with (OUT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(rows)
(OUT/'analysis/check_event_provenance.json').write_text(json.dumps(provenance,indent=2))
print('Consolidated',len(rows),'scoped events; no verdicts inferred.')
