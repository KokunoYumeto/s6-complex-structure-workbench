#!/usr/bin/env python3
"""Reconcile received event records without awarding a mathematical check.

Every canonical row retains a raw-record provenance object.  The executable
mapping between original types and the prompt's six types is exported.  This
program performs no proof review and makes no publication-readiness claim.
"""
from __future__ import annotations
import argparse, collections, csv, hashlib, json, re
csv.field_size_limit(16 * 1024 * 1024)
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORKSPACE = ROOT.parents[1]
MATERIALS = WORKSPACE / 'materials'
AUDIT = ROOT / 'analysis/continuation_ledger'
AUDIT.mkdir(parents=True, exist_ok=True)
WHO_CURRENT = 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS'
WHO_CONTINUATION = WHO_CURRENT + ' continuation'
TYPES = (
 'targeted proof check', 'independent re-proof',
 'computation or formal certificate', 'used and rechecked in this run',
 'carried as background without fault found',
 "refuted, with the refined statement's id",
)
S6_09 = MATERIALS/'S6_10_PAPERS_1_s6_09/s6_09/S6_09_PAPERS_inventory.csv'
SUPPLIED_LEDGER = MATERIALS/'S6_10_PAPERS_3_plan_and_checks/checks/S6_CHECK_LEDGER.tsv'
SWEEP = MATERIALS/'S6_10_PAPERS_4_sweep1/sweep1_s6'

def sha(data):
 return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()

def obj(value):
 if isinstance(value, dict): return value.copy()
 try:
  v=json.loads(value)
  return v if isinstance(v,dict) else {'raw':v}
 except (ValueError,TypeError): return {'raw':value}

def read_tsv(path):
 with path.open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))

def write_tsv(path, rows, fields):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)

def labels_of(value):
 if isinstance(value,list):values=value
 elif str(value).strip().startswith('['):
  values=json.loads(value)
  if not isinstance(values,list):raise ValueError('Expected label list')
 else:values=re.split(r'\s*[;,]\s*',str(value or ''))
 return [s.strip().replace('s6:night:','night:') for s in values if str(s).strip()]

def current_who(value, source):
 if str(value).startswith('GPT-6 Astra'):
  return WHO_CONTINUATION if 'continuation' in str(value).lower() or 'continuation' in source else WHO_CURRENT
 return str(value)

def classify(original, record, phase='current'):
 """Explicit, conservative map. Derivation after source-reading is targeted."""
 t=str(original).strip().lower(); text=' '.join(str(v) for v in record.values()).lower()
 if t in TYPES:
  if t=='independent re-proof' and phase!='continuation':
   return TYPES[0], 'Earlier recorded independent re-proof: pre-reading derivation order is not established by this record; its original claim is preserved.'
  return t, 'The received type already belongs to the six-type vocabulary.'
 if t in {'r-refutation','r'}:
  return TYPES[5], 'The received event verifies a refutation; the refined statement is identified in its outcome and provenance.'
 if t in {'d','l','f-partial','targeted open-boundary check'}:
  return TYPES[0], 'A mathematical reading or bounded derivation is recorded; no pre-reading whole-proof derivation is inferred.'
 if t in {'c'} or any(w in t for w in ('comput','certificate','replay','execution','integral computation')):
  return TYPES[2], 'Execution/certificate scope is retained, including whether the program was unchanged or newly written.'
 if t in {'s','e','a-identity','p-provenance','scope-record','scope correction','editorial_reconciliation','used/rechecked'}:
  return TYPES[3], 'The event rechecks use, identity, provenance, placement or scope; its outcome awards no additional proof check.'
 if any(w in t for w in ('citation','primary-source','software-source','source reading','source opening','dependency audit','dependency application','receiving-status','reconciliation')):
  return TYPES[3], 'Source, dependency or status comparison is retained at its stated bounded scope.'
 if any(w in t for w in ('rederivation','re-derivation','reproof','re-proof','proof reading','proof check','argument','local map','local-formula','deduction')):
  if phase=='continuation' and ('before reading' in text or 'prewritten' in text) and ('whole' in text or 'complete' in text):
   return TYPES[1], 'The continuation record expressly states that the complete derivation was written before reading the printed proof.'
  return TYPES[0], 'A mathematical reading/rederivation is recorded; the whole-proof pre-reading requirement is not inferred.'
 if phase=='historical':
  return TYPES[4], 'Historical statement/register intake is carried at its recorded scope.'
 raise ValueError('Unmapped event type '+repr(original))

def braced(s, at):
 if s[at]!='{':raise ValueError('Expected brace')
 d=1;i=at+1
 while d:
  if s[i]=='{' and s[i-1]!='\\':d+=1
  if s[i]=='}' and s[i-1]!='\\':d-=1
  i+=1
 return s[at+1:i-1],i

def printed_metadata():
 by_label=collections.defaultdict(list)
 for paper in ['I','II','III','IV','V','VI']:
  path=ROOT/f'S6_10_PAPERS_{paper}.tex'
  if not path.exists():continue
  s=path.read_text()
  for m in re.finditer(r'\\StatementRecord\s*\{',s):
   fields=[];at=m.end()-1
   for _ in range(4):
    while s[at].isspace():at+=1
    value,at=braced(s,at);fields.append(value)
   rec=dict(paper=paper,label=fields[0],status=fields[1],check_record=fields[2],uses=fields[3])
   by_label[fields[0]].append(rec)
   # Exact co-located label arrows: every alias in the environment prefix
   # points to this same StatementRecord, without creating another proof.
   begins=list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|remark|problem|openq|definition|counterexample|auditrecord)\}',s[:m.start()]))
   if begins:
    prefix=s[begins[-1].start():m.start()]
    end=s.find('\\end{'+begins[-1][1]+'}',m.start())
    segment=s[begins[-1].start():end] if end>=0 else prefix
    if '\\end{' not in prefix and '\\StatementRecord' not in prefix and segment.count('\\StatementRecord')==1:
     for alias in re.findall(r'\\label\{([^}]+)\}',segment):
      if alias!=fields[0]:by_label[alias].append(dict(rec,alias_of=fields[0]))
 return by_label

def historical_person(s):
 if 'Claude Fable 5.2' in s or 'prior-fable-' in s:
  effort='max' if re.search(r'effort[ \"\':]+max|Fable 5\.2 at effort max',s) else 'high'
  return 'Claude Fable 5.2 (Anthropic), effort '+effort
 if 'Claude Opus 5.5' in s:return 'Claude Opus 5.5 (Anthropic), effort max'
 if 'GPT-6 Astra' in s:return 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_09_PAPERS'
 if 'GPT-6.1 Sol' in s:return 'GPT-6.1 Sol (OpenAI), effort Ultra'
 if 'GPT-5.6 Sol' in s:return 'GPT-5.6 Sol (OpenAI), effort ultra'
 return ''

def historical_date(s, default=''):
 m=re.search(r'2026-\d\d-\d\d(?:[ T]\d\d:\d\d(?:\s*UTC)?)?',s)
 if m:return m[0]
 m=re.search(r'(\d{1,2}) November 2026',s)
 return '2026-11-'+m[1].zfill(2) if m else default

def historical_type(s):
 l=s.lower()
 if ('register intake' in l or 'statements only' in l or 'statement and setup' in l or 'no proof was read' in l or 'cursory' in l):return TYPES[4]
 if ('source-to-print' in l or 'token comparison' in l or 'comparison:' in l):return TYPES[3]
 if ('checked step' in l or 'proof' in l or 'derivation' in l or 'recomputed' in l or 'hand-check' in l):return TYPES[0]
 return TYPES[4]

def proof_review(event):
 return event['type'] in (TYPES[0],TYPES[1],TYPES[5])

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
 with (ROOT/'S6_10_PAPERS_inventory.csv').open() as f:
  rd=csv.DictReader(f);fields=rd.fieldnames;inventory=list(rd)
 # Parent-resolved cp36 additions retain received status and exact statement;
 # no continuation proof/computation/literature check is inferred from intake.
 night36=WORKSPACE/'night36/S6_06_BLIND/S6_06_BLIND_results.csv'
 new_night=[]
 if night36.exists():
  present={r['source_id'] for r in inventory if r['source_run']=='S6_06_BLIND'}
  for r in csv.DictReader(night36.open()):
   if r['id'] in present:continue
   lab='night:'+r['id']
   n=dict(row_key='S6_06_BLIND:'+r['id'],night_checkpoint='36',source_file=str(night36.relative_to(WORKSPACE)),where_proved=r['where_proved'],source_statement=r['statement'],source_status=r['status'],item_of_the_prompt=r.get('item_of_the_prompt',''),stated_value_compared=r.get('stated_value_compared (run and id)',''),agrees_with_stated_value=r.get('agrees_with_stated_value',''),source_notes=r.get('notes',''),continuation_intake='New cp36 source row imported 19 November 2026; receiving proof, independent new computation, and literature checks pending.',receiving_text_pending=True)
   cr=dict(historical_source_record='S6_06_BLIND reported re-derivation by GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, producing run 16–18 November 2026; checkpoint 36 snapshot 18 November 2026; source status '+r['status']+'. Imported continuation review remains pending.')
   n['continuation_main_result_allocation']='Parent review pending; provisionally supporting.'
   nr={k:'' for k in fields};nr.update(paper='IV',label=lab,source_run='S6_06_BLIND',source_id=r['id'],kind='night-run result',status='open',main_or_supporting='main',uses='; '.join('night:'+x.strip() for x in r['depends_on'].split(';') if x.strip()),check_record=json.dumps(cr,ensure_ascii=False),credited_to='S6_06_BLIND; comparison against attached literature pending',notes=json.dumps(n,ensure_ascii=False))
   inventory.append(nr);new_night.append(lab)
 source_map={r['source_run']+':'+r['source_id']:r['label'] for r in inventory}
 by_label={r['label']:r for r in inventory}
 by_label_rows=collections.defaultdict(list)
 for r in inventory:by_label_rows[r['label']].append(r)
 events={}; sources=[]; type_map=collections.Counter(); omitted=[]; discussions=[]
 def add(label,date,who,typ,outcome,source,source_row,raw,phase='current',original_type=None,mapping_reason=''):
  label=label.strip().replace('s6:night:','night:')
  if not label:raise ValueError('Empty label '+source)
  if not who or 'effort' not in who:raise ValueError('Unqualified checker '+repr(who)+' '+source)
  if typ not in TYPES:raise ValueError('Noncanonical type '+typ)
  key=(label,date,who,typ,outcome)
  if key not in events:
   digest=sha(json.dumps(key,ensure_ascii=False))
   events[key]=dict(statement_id=label,date=date,who=who,type=typ,outcome=outcome,event_id='ce:'+digest[:20],phase=phase,provenance=[])
  p=dict(source=source,source_row=source_row,raw_event=raw,original_type=original_type if original_type is not None else raw.get('type',''),mapping_reason=mapping_reason)
  if p not in events[key]['provenance']:events[key]['provenance'].append(p)
  type_map[(phase,str(original_type if original_type is not None else raw.get('type','')),typ,mapping_reason)]+=1
  return events[key]

 # Exact original current sources. Preserve inventory-enriched metadata separately.
 paths=sorted((ROOT/'records').glob('*events.tsv'))+sorted((ROOT/'analysis').glob('*/current_check_events.tsv'))
 raw_locations={}
 for path in paths:
  rel=str(path.relative_to(ROOT));rows=read_tsv(path);sources.append(dict(path=rel,sha256=sha(path.read_bytes()),rows=len(rows)))
  phase='continuation' if 'continuation' in rel else 'current'
  for num,raw in enumerate(rows,2):
   raw_locations[(rel,num)]=raw
   labels=labels_of(raw.get('statement_id') or raw.get('label') or raw.get('labels'))
   typ,reason=classify(raw.get('type',''),raw,phase)
   outcome=' '.join(str(raw[k]) for k in ('verdict','scope','derivation','outcome','independence') if raw.get(k))
   if raw.get('remaining_gates'):outcome+=' Remaining gates: '+raw['remaining_gates']
   if typ==TYPES[5]:
    refined=raw.get('refined_statement_id','') or ('ii:LR:covering; night:P3K.74' if 'night:P3K.36' in labels else '')
    if refined:outcome+=' Refined statement id: '+refined+'.'
   for label in labels:add(label,raw.get('date') or raw.get('recorded_at') or '',current_who(raw.get('who') or raw.get('checker'),rel),typ,outcome,rel,num,raw,phase,raw.get('type',''),reason)

 # Owner-issued event-type corrections supersede the prior type of the same
 # check. The exact old canonical event and every raw source field remain in
 # a separate archive and in the corrected event's provenance, rather than
 # being counted as a second mathematical check.
 superseded_path=AUDIT/'superseded_event_records.json'
 superseded_records=json.loads(superseded_path.read_text()) if superseded_path.exists() else []
 for correction in superseded_records:
  old=correction['superseded_canonical_event']
  new_label=correction.get('new_statement_id',old['statement_id'])
  matches=[event for event in events.values() if event['statement_id']==new_label and event['date']==old['date'] and event['who']==old['who'] and event['outcome']==old['outcome'] and event['type']==correction['new_type']]
  if len(matches)!=1:raise ValueError('Corrected event is not uniquely present: '+correction['correction_key'])
  if any(event['statement_id']==old['statement_id'] and event['date']==old['date'] and event['who']==old['who'] and event['outcome']==old['outcome'] and event['type']==old['type'] for event in events.values()):
   raise ValueError('Superseded type remains as a duplicate event: '+correction['correction_key'])
  matches[0]['provenance'].append(dict(source=str(superseded_path.relative_to(ROOT)),source_row=correction['correction_key'],raw_event=old,original_type=old['type'],mapping_reason=correction['reason'],superseded_event_id=old['event_id'],original_source_sha256=correction['original_source_sha256'],correction_source=correction['correction_source'],correction_sha256=correction['correction_sha256']))
  type_map[(old['phase'],old['type'],correction['new_type'],correction['reason'])]+=1

 # Inventory records are the complete received current-event list. An event
 # already found at the exact source row transports only metadata provenance.
 inventory_events_seen=0; inventory_only=0
 for row in inventory:
  cr=obj(row['check_record'])
  for raw in cr.get('current_writing_events',[]):
   inventory_events_seen+=1;loc=(raw.get('source',''),raw.get('source_row',0))
   if loc in raw_locations:
    base=raw_locations[loc]
    labels=labels_of(base.get('statement_id') or base.get('label') or base.get('labels'))
    if row['label'] in labels:continue
   inventory_only+=1
   typ,reason=classify(raw.get('type',''),raw)
   outcome=' '.join(str(raw[k]) for k in ('verdict','scope','derivation','independence') if raw.get(k))
   add(raw.get('label') or row['label'],raw.get('date',''),current_who(raw.get('who',''),'inventory'),typ,outcome,'S6_10_PAPERS_inventory.csv',row['label'],raw,'current',raw.get('type',''),reason)

 # Prior consolidated file has a complete row-to-source map. Its events are
 # recovered above from their original labels, including JSON-array labels.
 prior=ROOT/'CHECK_EVENTS.tsv';prev_prov=ROOT/'analysis/check_event_provenance.json'
 previous=list(csv.DictReader(prior.open(),delimiter='\t'))
 if previous and 'event_id' not in previous[0]:
  prov={int(v['output_row']):v for v in json.loads(prev_prov.read_text())} if prev_prov.exists() else {}
  for num,raw in enumerate(previous,2):
   p=prov.get(num,{})
   if (p.get('source'),p.get('source_row')) in raw_locations:continue
   typ,reason=classify(raw['type'],raw)
   for label in labels_of(raw['statement_id']):add(label,raw['date'],current_who(raw['who'],'legacy'),typ,raw['outcome'],'CHECK_EVENTS.tsv checkpoint06',num,raw,'current',raw['type'],reason)

 # Source openings have their actual receiving labels and count as use checks.
 for path in sorted((ROOT/'records').glob('*source_reads.tsv')):
  rel=str(path.relative_to(ROOT));rows=read_tsv(path);sources.append(dict(path=rel,sha256=sha(path.read_bytes()),rows=len(rows)))
  for num,raw in enumerate(rows,2):
   labels=labels_of(raw.get('used_by',''))
   outcome='Source '+raw.get('source_key','')+'; opened locus: '+raw.get('locus','')+'. '+raw.get('scope','')
   outcome+=' Source-opening record only; no additional whole-proof review is inferred.'
   for label in labels:add(label,raw.get('date',''),current_who(raw.get('who',''),rel),TYPES[3],outcome,rel,num,raw,'current','primary-source opening','The source locus was opened and compared with its stated use.')

 # S6_09 historical records are taken from complete supplied fields, not the
 # truncated "recorded check (unparsed)" snippets in the summary ledger.
 old=list(csv.DictReader(S6_09.open()))
 for num,row in enumerate(old,2):
  label=row['printed_label'];label=source_map.get(row['source_run']+':'+row['source_id'],label)
  raw=row['your_check'];d=obj(raw)
  date=historical_date(raw,'2026-11-17')
  outcome='Received S6_09 writing record: '+raw+' Recorded outcome: '+row.get('check_outcome','')+'. This continuation preserves the earlier scope; pre-reading derivation order is not inferred.'
  add(label,date,'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_09_PAPERS',TYPES[0],outcome,str(S6_09.relative_to(WORKSPACE)),num,dict(your_check=raw,check_outcome=row.get('check_outcome','')),'historical','S6_09 recorded writing check','Complete historical field is retained; this import adds no new mathematical check.')
  recorded=row['recorded_checks'];parts=recorded.split(' | ')
  for ix,part in enumerate(parts):
   part=part.strip()
   if not part:continue
   vals=[]
   if part.startswith(('[','{')):
    try:
     v=json.loads(part);vals=v if isinstance(v,list) else [v]
    except ValueError:pass
   if vals:
    for v in vals:
     text=json.dumps(v,ensure_ascii=False);who=historical_person(text)
     if not who:omitted.append(dict(label=label,reason='No individually named checker in this provenance declaration',raw=part));continue
     date=str(v.get('date',''));typ=historical_type(text)
     add(label,date,who,typ,'Received historical check: '+text,str(S6_09.relative_to(WORKSPACE)),str(num)+':'+str(ix),v,'historical','structured historical record','Type follows the exact recorded scope; no additional check is inferred.')
    continue
   low=part.lower()
   if (any(q in low for q in ['no other independent','no earlier named','provenance only','self-check','selfcheck','verification badges','not treated as a proof check','reader-specific matching pending','not an inherited historical','current independent','current complete proof']) and 'checked step' not in low):
    omitted.append(dict(label=label,reason='Producer/provenance declaration or absence statement; retained in original inventory, no separate historical event created',raw=part));continue
   who=historical_person(part)
   if not who:
    # Register descriptors use the review's named author; inspectable source
    # metadata, not a person inferred from subject matter.
    if 'prior-fable-' in part:who='Claude Fable 5.2 (Anthropic), effort high'
    elif part.startswith('prior-') and 'survey' in low:who='Claude Fable 5.2 (Anthropic), effort high'
    else:omitted.append(dict(label=label,reason='No separately identifiable historical checker in this declaration',raw=part));continue
   date=historical_date(part)
   if not date:
    m=re.search(r'202611(\d\d)',part);date='2026-11-'+m[1] if m else ''
   add(label,date,who,historical_type(part),'Received historical check: '+part,str(S6_09.relative_to(WORKSPACE)),str(num)+':'+str(ix),dict(recorded_check=part),'historical','historical textual record','Historical type follows the exact statement/proof/comparison scope.')

 # Supplied ledger's document references add bounded record-intake events.
 # Discussions remain a separate provenance table and create no check event.
 review_root=MATERIALS/'S6_10_PAPERS_3_plan_and_checks'
 historical_docs={}
 for num,row in enumerate(read_tsv(SUPPLIED_LEDGER),2):
  label=source_map.get(row['source_run']+':'+row['source_id'],row['printed_label'])
  for piece in row['checks'].split(' || '):
   if piece.startswith('discussed in '):
    discussions.append(dict(label=label,raw=piece));continue
   if not piece.startswith('checked in '):continue
   m=re.match(r'checked in (.+?\.md) \((.+)\)$',piece)
   if not m:omitted.append(dict(label=label,reason='Unparsed historical ledger descriptor',raw=piece));continue
   doc,person=m.groups();who=historical_person(person)
   if not who:raise ValueError('Historical checker unresolved '+piece)
   source=review_root/doc
   if source.exists():
    content=source.read_text();historical_docs[doc]=dict(sha256=sha(source.read_bytes()),bytes=source.stat().st_size)
   else:content=''
   if doc.endswith('DRAFT_CHECK.md'):
    typ=TYPES[3];scope='Source-to-print statement/proof comparison and the bounded readings specified in this document. This is not an additional full-proof verification.'
   elif doc.endswith('READING_S6_01_A1.md'):
    typ=TYPES[0];scope='Full A1.0–A1.3 source reading with the character, degree, extension and duality derivations specified in that document; dependencies retain their recorded scopes.'
   elif '/S6_02_REVIEW_FABLE/' in doc:
    typ=TYPES[0];scope='The review names this result; its exact per-result checked step and verdict are in the supplied review. No larger proof scope is inferred.'
   else:
    typ=TYPES[4];scope='The intake names this statement. Register/statement comparison is carried as background; any separately documented mathematical reading has its own event and scope.'
   # The summary ledger often projects an event whose complete field has
   # already been imported. Match exact document, label, checker and day;
   # retain this second provenance path without counting a second check.
   day=historical_date(person)[:10]
   matches=[e for e in events.values() if e['phase']=='historical' and e['statement_id']==label and e['who']==who and e['date'][:10]==day and doc in e['outcome']]
   raw=dict(descriptor=piece,document_sha256=historical_docs.get(doc,{}).get('sha256',''))
   if matches:
    for e in matches:e['provenance'].append(dict(source=str(SUPPLIED_LEDGER.relative_to(WORKSPACE)),source_row=num,raw_event=raw,original_type='checked in document',mapping_reason='Exact same document, statement, checker and day as the complete historical event; no extra check counted.'))
   else:
    add(label,historical_date(person),who,typ,'Historical document record: '+doc+'. '+scope,str(SUPPLIED_LEDGER.relative_to(WORKSPACE)),num,raw,'historical','checked in document','A document mention supplies only its explicit bounded scope.')

 # The night run's own reported derivation is the historical check identified
 # by the task. Its open/refuted status is retained and is never promoted.
 for row in inventory:
  if row['source_run']!='S6_06_BLIND':continue
  notes=obj(row['notes']);cr=obj(row['check_record']);raw=str(cr.get('historical_source_record',cr.get('raw','')))
  outcome=raw+' This is the producing run’s recorded re-derivation; the continuation creates no additional proof review by importing it.'
  add(row['label'],'2026-11-16/2026-11-18','GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_06_BLIND',TYPES[0],outcome,'S6_10_PAPERS_inventory.csv',row['label'],dict(historical_source_record=raw,source_status=notes.get('source_status','')),'historical','night-run reported re-derivation','Recorded producer check, retaining the received proved/open/refuted scope.')

 # Sweep arithmetic is a computation; statement/correction comparisons are use
 # checks. Raw prose is never silently upgraded to a proof derivation.
 for num,raw in enumerate(read_tsv(SWEEP/'CHECK_EVENTS.tsv'),2):
  tag=raw['statement tag']
  if tag.startswith('Q03_DEPOSIT:'):
   omitted.append(dict(label=tag,reason='Q03 is outside these papers',raw=raw));continue
  label=source_map.get(tag,tag)
  typ=TYPES[2] if 'comput' in raw['type'].lower() else TYPES[3]
  add(label,raw['date'],'Claude Opus 5.5 (Anthropic), effort max, sweep 1, scope s6',typ,raw['outcome']+' Read scope: '+raw.get('what was read',''),str((SWEEP/'CHECK_EVENTS.tsv').relative_to(WORKSPACE)),num,raw,'historical',raw['type'],'Sweep scope is its exact statement or arithmetic comparison, not a reread of the full proof.')

 canonical=list(events.values());canonical.sort(key=lambda e:(e['statement_id'],e['date'],e['event_id']))
 canonical_by_label=collections.defaultdict(list)
 for e in canonical:canonical_by_label[e['statement_id']].append(e)
 metadata=printed_metadata()
 status_changes=[];status_ambiguous=[];patches=[]
 overrides_path=AUDIT/'owner_overrides.json'
 overrides=json.loads(overrides_path.read_text()) if overrides_path.exists() else {}
 # A gate is closed only by the named owner's explicit evidence receipt.
 # The merger transports that decision and its raw record; it does not
 # infer completion from event counts or the mathematical status.
 gate_receipts=collections.defaultdict(list)
 allowed_gates={'proof_rederivation_before_reading','new_independent_computations','renewed_main_result_credit_check'}
 for gp in sorted((ROOT/'analysis').glob('continuation_*/completed_row_gates.json')):
  raw_receipts=json.loads(gp.read_text())
  if not isinstance(raw_receipts,dict):raise ValueError('Owner gate receipt must be keyed by statement label: '+str(gp))
  for label,values in raw_receipts.items():
   if label not in by_label:raise ValueError('Owner gate receipt has no inventory row: '+label)
   if not isinstance(values,dict) or not set(values)<=allowed_gates:
    raise ValueError('Unexpected owner gate fields for '+label+' in '+str(gp))
   gate_receipts[label].append(dict(source=str(gp.relative_to(ROOT)),sha256=sha(gp.read_bytes()),raw_owner_receipt=values))
 # Preserve mathematical statuses from actual receiving statements. Remaining
 # renewed checks are separate row gates, never converted into theorem status.
 for row in inventory:
  notes=obj(row['notes']);cr=obj(row['check_record']);old_status=row['status'];lab=row['label']
  printed=metadata.get(lab,[]);ps=printed[0]['status'] if printed else ''
  low=ps.lower()
  if low.startswith('open'):new='open'
  elif low.startswith(('false','refuted')):new='false as stated'
  elif low.startswith(('proved','known','verified bounded')):new='proved'
  elif old_status.lower().startswith('open'):new='open'
  elif old_status.lower().startswith(('refuted','false')):new='false as stated'
  elif row['in_compendium_only_because']:
   src=str(notes.get('source_status',''))+' '+str(notes.get('historical_source_notes',''))
   if re.search(r'SOURCE STATUS: Open\b',src,re.I):new='open'
   elif re.search(r'SOURCE STATUS: Refuted\b',src,re.I):new='false as stated'
   elif 'Proved conditionally' in src:new=old_status;status_ambiguous.append(dict(label=lab,reason='Exact H needs mathematical restoration',status=old_status))
   else:new='proved'
  elif notes.get('receiving_text_pending'):
   new='open';status_ambiguous.append(dict(label=lab,reason='Received source status preserved separately; receiving text and all three continuation checks pending',status=old_status))
  else:
   new=old_status;status_ambiguous.append(dict(label=lab,reason='No printed status located; no mathematical status inferred',status=old_status))
  # ARI C.7.4 is deliberately left to the paper owner: its exact H must be
  # restored from source and checked, not invented by a metadata transform.
  if lab=='ari:C.7.4' and not low.startswith('proved under hypotheses'):
   new='open';status_ambiguous.append(dict(label=lab,reason='Parent is restoring and checking the source theorem with its exact H',status=old_status))
  elif low.startswith('proved under hypotheses'):
   new=ps
  if lab in overrides:
   override=overrides[lab];new=override['status']
   if override.get('kind'):row['kind']=override['kind']
   notes['continuation_owner_status_override']=override
   if new.startswith('proved under hypotheses'):
    notes['hypothesis_H']=override.get('hypothesis_H','')
    notes['hypothesis_H_holds_in_used_cases']=override.get('holds_in_cases_used','')
    notes['receiving_open_problem']=False
   status_ambiguous=[x for x in status_ambiguous if x['label']!=lab]
  if new!=old_status:status_changes.append(dict(label=lab,paper=row['paper'],old_status=old_status,new_status=new,basis=ps or 'received compendium classification; no new proof verdict'))
  notes.setdefault('continuation_received_status',old_status)
  notes['continuation_status_basis']=ps or 'Received compendium/source classification; current review gates remain separate.'
  ev=canonical_by_label.get(lab,[])
  cr['canonical_check_events']=[dict(event_id=e['event_id'],date=e['date'],who=e['who'],type=e['type'],phase=e['phase']) for e in ev]
  cr['canonical_event_provenance']='analysis/continuation_ledger/event_provenance.jsonl'
  cr['canonical_type_policy']='Every event has one of the six task types. Exact original type, scope and source row are preserved; imported events add no new review.'
  cr['current_writing']=new
  continuation=[e for e in ev if e['phase']=='continuation']
  notes.setdefault('continuation_three_check_gates',{})
  gates=notes['continuation_three_check_gates']
  gates.setdefault('proof_rederivation_before_reading','pending; only explicit continuation evidence can close this gate')
  gates.setdefault('new_independent_computations','pending; unchanged historical replays do not close this gate')
  gates.setdefault('renewed_main_result_credit_check','pending for main rows; applicable scope must be recorded by paper owner')
  receipt_values={}
  for receipt in gate_receipts.get(lab,[]):
   for gate,value in receipt['raw_owner_receipt'].items():
    if gate in receipt_values and receipt_values[gate]!=value:
     raise ValueError('Conflicting explicit owner gate receipts for '+lab+' / '+gate)
    receipt_values[gate]=value
  gates.update(receipt_values)
  if gate_receipts.get(lab):notes['continuation_gate_owner_receipts']=gate_receipts[lab]
  notes['canonical_event_count']=len(ev)
  row.update(status=new,notes=json.dumps(notes,ensure_ascii=False),check_record=json.dumps(cr,ensure_ascii=False))
  if printed:
   hist=collections.defaultdict(set)
   for e in ev:
    if e['phase']=='historical':hist[(e['who'],e['date'])].add(e['type'])
   patches.append(dict(paper=row['paper'],label=lab,status=new,prior_printed_status=ps,historical_types=[dict(who=k[0],date=k[1],types=sorted(v)) for k,v in hist.items()],event_ids=[e['event_id'] for e in ev]))

 # Preserve every merge and flag as a typed relation. A merge is never inserted
 # into Uses as a proof premise unless its mathematical role has been checked.
 relation_rows=[]
 for num,r in enumerate(read_tsv(SWEEP/'MERGES.tsv'),2):
  a,b=r['canonical tag'],r['member tag'];ca,mb=source_map.get(a,a),source_map.get(b,b)
  relation_rows.append(dict(canonical_label=ca,member_label=mb,relation=r['relation (member relative to canonical)'],reason=r['reason'],source_row=num))
  for label in [ca,mb]:
   if label in by_label:
    for row in by_label_rows[label]:
     notes=obj(row['notes']);v=dict(canonical=ca,member=mb,relation=r['relation (member relative to canonical)'],reason=r['reason'],source='sweep1/MERGES.tsv',source_row=num)
     rels=notes.setdefault('sweep1_merge_relations',[])
     if v not in rels:rels.append(v)
     notes['sweep1_relations_are_not_unchecked_proof_premises']=True
     row['notes']=json.dumps(notes,ensure_ascii=False)
 flag_rows=[]
 for num,r in enumerate(read_tsv(SWEEP/'FLAG_VERDICTS.tsv'),2):
  label=source_map.get(r['tag'],r['tag']);flag_rows.append(dict(label=label,**r,source_row=num))
  if label in by_label:
   for row in by_label_rows[label]:
    notes=obj(row['notes']);v=dict(r,source_row=num);flags=notes.setdefault('sweep1_flag_verdicts',[])
    if v not in flags:flags.append(v)
    notes['dependency_scope_reviews']=flags
    row['notes']=json.dumps(notes,ensure_ascii=False)
 dependency_label_arrows=[]
 for row in inventory:
  notes=obj(row['notes'])
  relations=notes.get('sweep1_merge_relations',[])
  if relations:
   marker=' | Sweep1 cross-run comparison: '
   prior=row['credited_to'].split(marker)[0]
   pieces=[x['member']+' '+x['relation']+' '+x['canonical'] for x in relations]
   row['credited_to']=prior+marker+'; '.join(pieces)+'. These are the supplied statement-level comparison relations; their proof scopes remain in the event ledger.'
  if row['source_run']=='S6_06_BLIND':
   pieces=[]
   for token in row['uses'].split(';'):
    old=token.strip();new=source_map.get('S6_06_BLIND:'+old,old)
    pieces.append(new)
    if old!=new:dependency_label_arrows.append(dict(label=row['label'],source_id=old,receiving_label=new,basis='Exact source-run/id lookup in this inventory; no mathematical dependency added.'))
   if row['uses']!='; '.join(pieces):
    notes.setdefault('source_uses_before_label_resolution',row['uses']);row['uses']='; '.join(pieces)
  row['notes']=json.dumps(notes,ensure_ascii=False)

 outfields=['statement_id','date','who','type','outcome','event_id','phase']
 write_tsv(AUDIT/'CHECK_EVENTS.proposed.tsv',canonical,outfields)
 with (AUDIT/'event_provenance.jsonl').open('w') as f:
  for e in canonical:f.write(json.dumps(e,ensure_ascii=False)+'\n')
 write_tsv(AUDIT/'type_mapping.tsv',[dict(phase=k[0],original_type=k[1],canonical_type=k[2],reason=k[3],count=v) for k,v in type_map.items()],['phase','original_type','canonical_type','reason','count'])
 write_tsv(AUDIT/'status_changes.tsv',status_changes,['label','paper','old_status','new_status','basis'])
 histpath=AUDIT/'status_changes_history.tsv'
 history=read_tsv(histpath) if histpath.exists() else []
 for x in status_changes:
  if x not in history:history.append(x)
 write_tsv(histpath,history,['label','paper','old_status','new_status','basis'])
 write_tsv(AUDIT/'sweep1_relations.tsv',relation_rows,['canonical_label','member_label','relation','reason','source_row'])
 write_tsv(AUDIT/'sweep1_flag_verdicts.tsv',flag_rows,['label','tag','flag','verdict','place','note','source_row'])
 write_tsv(AUDIT/'dependency_label_arrows.tsv',dependency_label_arrows,['label','source_id','receiving_label','basis'])
 (AUDIT/'printed_metadata_patch.json').write_text(json.dumps(patches,ensure_ascii=False,indent=2))
 (AUDIT/'excluded_provenance_declarations.json').write_text(json.dumps(omitted,ensure_ascii=False,indent=2))
 (AUDIT/'historical_discussions.json').write_text(json.dumps(discussions,ensure_ascii=False,indent=2))
 (AUDIT/'historical_document_hashes.json').write_text(json.dumps(historical_docs,ensure_ascii=False,indent=2))
 (AUDIT/'source_manifest.json').write_text(json.dumps(sources,indent=2))
 (AUDIT/'status_requires_owner.json').write_text(json.dumps(status_ambiguous,ensure_ascii=False,indent=2))
 summary=dict(inventory_rows=len(inventory),printed_inventory_rows=sum(not r['in_compendium_only_because'] for r in inventory),
  source_record_tables=len(sources),inventory_current_events_received=inventory_events_seen,inventory_only_events=inventory_only,new_night36_rows=new_night,
  canonical_events=len(canonical),canonical_statements=len(canonical_by_label),events_by_type=dict(collections.Counter(e['type'] for e in canonical)),
  events_by_phase=dict(collections.Counter(e['phase'] for e in canonical)),
  printed_rows_without_any_event=[r['label'] for r in inventory if not r['in_compendium_only_because'] and not canonical_by_label.get(r['label'])],
  unmatched_event_labels=sorted(set(canonical_by_label)-set(by_label)),status_changes=len(status_changes),status_requires_owner=status_ambiguous,
  merge_relations=len(relation_rows),flag_verdicts=len(flag_rows),excluded_provenance_declarations=len(omitted),discussion_records=len(discussions),
  policy='This script performs record reconciliation only. Neither importing a reported proof check nor assigning a mathematical status closes the renewed three-check gates.')
 (AUDIT/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
 with (AUDIT/'S6_10_PAPERS_inventory.proposed.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fields);w.writeheader();w.writerows(inventory)
 if args.apply:
  (ROOT/'CHECK_EVENTS.tsv').write_bytes((AUDIT/'CHECK_EVENTS.proposed.tsv').read_bytes())
  (ROOT/'S6_10_PAPERS_inventory.csv').write_bytes((AUDIT/'S6_10_PAPERS_inventory.proposed.csv').read_bytes())
 print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
