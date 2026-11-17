"""Merge actual scoped audit records into the fixed 17-column inventory.

This script records evidence and extracts the statement actually printed. It
does not infer mathematical correctness from presence, a source badge, or a hash.
"""
from pathlib import Path
import csv,json,re,collections
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'deliverables';W=OUT/'work'
path=OUT/'S6_09_PAPERS_inventory.csv'
with path.open(newline='') as f:
 reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
index={(r['source_run'],r['source_id']):r for r in rows}
def string(x):
 return x if isinstance(x,str) else json.dumps(x,ensure_ascii=False)
def add(r,k,x):
 if not x:return
 x=string(x)
 if x not in r.get(k,''):r[k]=(r.get(k,'')+' | '+x).strip(' |')
def load(p):return json.loads((W/p).read_text())
sources=[('invariants_arithmetic/result_audit.json',None),
 ('invariants_arithmetic/working_edition_inventory.json',None),
 ('maps_audit/results_audit.json','S6_04_MAPS_MANIFOLDS'),
 ('maps_audit/push_C_audit.json','S6_02_PUSH'),
 ('maps_audit/working_results_inventory.json',None),
 ('cdp_audit/result_audit.json','S6_03_CDP'),
 ('cdp_audit/invariants_part_E_audit.json','S6_01_INVARIANTS'),
 ('cdp_audit/working_edition_inventory.json',None),
 ('root/cdp_reserved_full_checks.json','S6_03_CDP'),
 ('root/II_comb_full_check.json','S6_01_INVARIANTS'),
 ('root/II_push_E5_full_checks.json','S6_02_PUSH')]
merged=0
for source,default_run in sources:
 for x in load(source):
  sid=x.get('source_id',x.get('id'));run=x.get('source_run',default_run)
  r=index.get((run,sid))
  if r is None:
   # Working inventories occasionally normalize a source-run's capitalization.
   candidates=[z for z in rows if z['source_id']==sid and not z['source_run'].startswith('S6_')]
   if len(candidates)==1:r=candidates[0]
   else:raise ValueError(('unmatched existing inventory row',source,run,sid))
  merged+=1
  own=x.get('own_check',x.get('your_check'))
  if own:r['your_check']=string(own)
  rec=x.get('recorded_checks')
  if rec:r['recorded_checks']=string(rec)
  elif x.get('recorded_check_absence'):
   r['recorded_checks']=string(x['recorded_check_absence'])
  outcome=x.get('check_outcome',x.get('audit_state'))
  if isinstance(own,dict) and own.get('proof_outcome'):outcome=own['proof_outcome']
  if outcome:r['check_outcome']=string(outcome)
  p=x.get('printed_paper',x.get('paper'))
  if p:r['paper']=p.split()[0].rstrip(';')
  label=x.get('printed_label')
  if label:r['printed_label']=label
  for k in ['change_notes','audit_notes','remarks','source_sha256','proof_sha256','printed_proof_label','printed_proof_file']:
   if x.get(k):add(r,'notes',k+': '+string(x[k]))
  credits=x.get('credit_checks',x.get('source_credit'))
  if credits:
   add(r,'notes','Credit evidence ('+source+'): '+string(credits))
   if isinstance(credits,list):
    for c in credits:
     st=string(c);basis=st.lower()
     k='found_in_AC26' if 'ac26' in basis else 'found_in_E26' if 'engel' in basis else 'found_in_DGKX_v1' if 'dgkx' in basis or 'duetal' in basis else 'found_elsewhere'
     r[k]=st
   elif isinstance(credits,dict):
    for k,v in credits.items():
     target={'AC26':'found_in_AC26','E26':'found_in_E26','DGKX_v1':'found_in_DGKX_v1','elsewhere':'found_elsewhere'}.get(k)
     if target:r[target]=string(v)
   else:r['found_elsewhere']=string(credits)

papers={p:(OUT/f'S6_09_PAPERS_{p}.tex').read_text() for p in ['I','II','III'] if (OUT/f'S6_09_PAPERS_{p}.tex').exists()}
labels={p:set(re.findall(r'\\label\{([^}]+)\}',s)) for p,s in papers.items()}
aliases={}
for name in ['invariants_arithmetic/statement_aliases.json','invariants_arithmetic/working_statement_aliases.json','maps_audit/paperI_topology_aliases.json','cdp_audit/paperII_statement_aliases.json']:
 if not (W/name).exists():continue
 obj=load(name)
 if isinstance(obj,list):obj={x['source_label']:x['shared_printed_label'] for x in obj}
 aliases.update(obj)
special={('S6_03_CDP','D.1.14'):('I','fam:src:F.1.1'),
         ('S6_03_CDP','E9'):('I','fam:src:A.5.2'),
         ('S6_02_PUSH','C.3.5'):('I','push:src:C.3.5'),
         ('S6_02_PUSH','E.4.3'):('I','fam:src:C.2.3'),
         ('S6_05_ARITHMETIC','C.8.5'):('I','fam:src:C.2.3')}
def candidates(r):
 sid=r['source_id'];run=r['source_run'];cur=r['printed_label'].split(' (')[0]
 yield cur
 prefix={'S6_02_FAMILY':'fam:src:','S6_02_PUSH':'push:src:',
         'S6_01_INVARIANTS':'inv:','S6_05_ARITHMETIC':'ari:',
         'S6_04_MAPS_MANIFOLDS':'mapsI:src:','S6_03_CDP':'cdp:st:'}.get(run,'wb:')
 yield prefix+sid
 yield sid
 yield 'wb:'+sid
 yield 'wbII:'+sid
 yield aliases.get(prefix+sid,'')
 yield aliases.get(sid,'')
def statement(s,label):
 pos=s.index('\\label{'+label+'}')
 starts=list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|claim|statement|remark|question|problem|conjecture|definition|example|test)\}',s[:pos]))
 if starts:
  m=starts[-1];end=s.find('\\end{'+m[1]+'}',pos)
  if end>=0 and '\\end{'+m[1]+'}' not in s[m.end():pos]:
   return s[m.start():end+len('\\end{'+m[1]+'}')],m[1]
 # Non-statement source rows (a historical question, provenance, or a calculation).
 tail=s[pos:];end=re.search(r'\n\\(?:sub)*section|\n\\begin\{(?:theorem|proposition|lemma|corollary|remark|question|problem)\}',tail)
 return tail[:end.start() if end else min(len(tail),5000)],'record'

for r in rows:
 key=(r['source_run'],r['source_id'])
 if key in special:r['paper'],r['printed_label']=special[key]
 p=r['paper'].split()[0].rstrip(';')
 if p not in papers:continue
 found=next((c for c in candidates(r) if c and c in labels[p]),None)
 if not found:continue
 r['printed_label']=found
 r['statement_as_printed'],env=statement(papers[p],found)
 if r['kind'].lower() in ['result','theorem','proposition','lemma','remark','question','corollary','claim']:
  r['kind']={'question':'Open question','problem':'Open question'}.get(env,env.title())
 r['wording_vs_source']='Full printed statement extracted from the indicated label. Source-aware label and citation normalization; duplicate statements shared with all distinct proofs retained. Content changes are recorded in the per-result audit and editorial transform manifests.'
 # Remove duplicated transfer notes without erasing historical evidence.
 r['notes']='; '.join(dict.fromkeys(r['notes'].split('; ')))

late_path=W/'root/late_carrier_inventory_additions.json'
late_rows=json.loads(late_path.read_text()) if late_path.exists() else []
late_working_count=sum(r['source_run']=='working_edition' for r in late_rows)
assert len([r for r in rows if r['source_run'] not in {'WORKING_EDITION_COURSE_PROVIDER','WRITING_REPAIR'}])==928+late_working_count and len(fields)==17
assert len({(r['source_run'],r['source_id']) for r in rows})==len(rows)
with path.open('w',newline='') as f:
 w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
report={'rows':len(rows),'merged_agent_rows':merged,'papers':dict(collections.Counter(r['paper'] for r in rows)),
        'printed_labels_present':sum(any(r['printed_label'] in v for v in labels.values()) for r in rows),
        'by_paper_printed':{p:sum(r['paper']==p and r['printed_label'] in labels[p] for r in rows) for p in papers}}
(OUT/'records/inventory_merge.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
