#!/usr/bin/env python3
"""Produce reviewable TeX metadata replacements; do not edit any paper."""
import collections,csv,json,re
csv.field_size_limit(16 * 1024 * 1024)
from pathlib import Path

P=Path(__file__).resolve().parents[2]
A=P/'analysis/continuation_ledger'

def tex(s):
 table={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
 return ''.join(table.get(c,c) for c in s)

def display_date(s):
 if s=='2026-11-16/2026-11-18':return '16--18 November 2026'
 m=re.fullmatch(r'2026-11-(\d\d)(.*)',s)
 if m:
  suffix=m[2]
  # Only the ISO date/time separator is converted; the T in UTC is literal.
  if suffix.startswith('T'):suffix=' '+suffix[1:]
  return str(int(m[1]))+' November 2026'+suffix
 return s

def metadata_operation(event):
 """Identify actual administrative outcomes, never infer from date/type."""
 outcome=event['outcome']
 rules=(
  ('Administrative status reconciliation:', 'status-vocabulary reconciliation'),
  ('Imported the exact checkpoint36 results row,', 'source-row intake'),
  ('Exact cp36 receiving placement:', 'receiving source placement'),
  ('Exact cp36 source delta audit:', 'source-delta and receiving-status reconciliation'),
 )
 for prefix,operation in rules:
  if outcome.startswith(prefix):return operation
 if 'metadata reconciliation only; no new mathematical check' in outcome.lower():
  return 'explicitly scoped metadata reconciliation'
 return None

def grouped_type_tex(events,heading):
 groups=collections.defaultdict(set)
 for event in events:groups[(event['who'],event['date'])].add(event['type'])
 clauses=[]
 for (who,date),types in sorted(groups.items()):
  clauses.append(tex(who+(', '+display_date(date) if date else ''))+': '+tex('; '.join(sorted(types))))
 return heading+': '+'. '.join(clauses)+'. ' if clauses else ''

def main():
 events=list(csv.DictReader((P/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
 by=collections.defaultdict(list)
 for e in events:by[e['statement_id']].append(e)
 rows=list(csv.DictReader((P/'S6_10_PAPERS_inventory.csv').open()))
 out=[]
 for r in rows:
  groups=collections.defaultdict(set)
  for e in by[r['label']]:
   if e['phase']=='historical':groups[(e['who'],e['date'])].add(e['type'])
  clauses=[]
  for (who,date),types in sorted(groups.items()):
   label=who+(', '+display_date(date) if date else '')
   clauses.append(tex(label)+': '+tex('; '.join(sorted(types))))
  hist='Historical events: '+'. '.join(clauses)+'. ' if clauses else 'No earlier separately identified check is recorded. '
  prior=[e for e in by[r['label']] if e['phase']=='current']
  continuation=[e for e in by[r['label']] if e['phase']=='continuation']
  administrative=[e for e in continuation if metadata_operation(e)]
  actual=[e for e in continuation if not metadata_operation(e)]
  prior_tex=grouped_type_tex(prior,'Pre-continuation writing events')
  actual_tex=grouped_type_tex(actual,'Continuation mathematical and source checks')
  admin_clauses=[]
  admin_mapping=[]
  for e in sorted(administrative,key=lambda x:(x['who'],x['date'],x['event_id'])):
   operation=metadata_operation(e)
   label=e['who']+(', '+display_date(e['date']) if e['date'] else '')
   admin_clauses.append(tex(label)+': '+tex(e['type'])+'; '+tex(operation)+'; metadata reconciliation only; no new mathematical check')
   admin_mapping.append(dict(event_id=e['event_id'],operation=operation,outcome=e['outcome'],display_scope='metadata reconciliation only; no new mathematical check'))
  admin_tex='Continuation metadata events: '+'. '.join(admin_clauses)+'. ' if admin_clauses else ''
  current_tex=prior_tex+actual_tex+admin_tex
  declaration=('Also checked in this writing. ' if clauses else 'Checked only in this writing. ') if prior or actual else ('This writing records metadata reconciliation only; no new mathematical check. ' if administrative else '')
  out.append(dict(paper=r['paper'],label=r['label'],status=r['status'],historical_tex=hist,current_type_tex=current_tex,
   pre_continuation_type_tex=prior_tex,continuation_actual_type_tex=actual_tex,continuation_metadata_tex=admin_tex,
   writing_declaration_tex=declaration,continuation_metadata_event_mapping=admin_mapping,
   continuation_actual_event_ids=[e['event_id'] for e in actual],
   legacy_scope_marker_tex=r'\emph{Pre-continuation recorded proof scope.} ',
   continuation_scope_marker_tex=r'\emph{Continuation recorded proof scope.} ',
   scope_rule='Retain exact event outcome and original scope from CHECK_EVENTS.tsv / event_provenance.jsonl. The retained legacy narrative is pre-continuation proof scope; only an explicit owner-written replacement may be labelled continuation scope. Administrative events are identified by their actual outcome and each is explicitly metadata reconciliation only; no new mathematical check.',
   replacement_rule='Replace only check-record metadata. Separate pre-continuation events, actual continuation mathematical/source checks, and administrative receipts. Keep the original narrative with the pre-continuation marker unless the paper owner supplies an explicit new scope override.'))
 (A/'printed_typed_check_prefixes.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
 print(json.dumps({'rows':len(out),'path':str(A/'printed_typed_check_prefixes.json')},indent=2))

if __name__=='__main__':main()
