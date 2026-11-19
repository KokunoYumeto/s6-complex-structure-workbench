"""Create Paper I receiving fragments without assigning proof checks.

The source map and explicit current event scopes drive every record. Complete
proofs are retained for new statements. Known inputs retain their statement
and citation; their long re-derivation remains in the unchanged compendium.
"""
from pathlib import Path
import csv,importlib.util,json,re,sys

OUT=Path(__file__).resolve().parents[2]; BASE=OUT.parents[1]
sys.path.insert(0,str(OUT/'code'))
from inventory_reconcile import TexIndex,commands,argument
from clean_checkrecord_scopes import clean_check_scope
spec=importlib.util.spec_from_file_location('iii_body',OUT/'code/III/build_body.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
SOURCE=BASE/'sources/s6_09/S6_09_PAPERS_I.tex';IDX=TexIndex(SOURCE);S=IDX.text
ROWS=list(csv.DictReader((OUT/'S6_10_PAPERS_inventory.csv').open()))
INDEX=json.loads((OUT/'analysis/inventory_source_index.json').read_text())
HIST=json.loads((OUT/'analysis/inventory_history_by_label.json').read_text())
EVENTS={}
for row in csv.DictReader((OUT/'records/root_events.tsv').open(),delimiter='\t'):
 EVENTS.setdefault(row['statement_id'],[]).append(row)
BLOCK_ALIASES={}
for loc in INDEX.values():
 if loc.get('container_kind')=='statement_environment':
  key=(loc['file'],loc['start'],loc['end'])
  BLOCK_ALIASES.setdefault(key,set()).add(loc['label'])

RANGES={
 '00_conventions':[(231,278),(25046,25259)],
 '01_periods':[(586,710),(925,1415),(5244,5398),(5709,5992),(7434,7889)],
 '02_moduli':[(279,585),(711,924),(23978,24257)],
 '03_monodromy_and_fibres':[(2010,2578),(1629,2009),(1416,1628),(10981,11441)],
 '04_hodge':[(2579,3473),(4155,4756)],
 '05_twisted_tangent':[(4757,5243),(24258,24705)],
 '06_ends':[(11442,22599),(22600,23977)],
 '07_arithmetic':[(5399,5708),(5993,7433),(7890,8898)],
 '08_higher_multiplicities':[(3474,4154)],
 '09_integral_circle':[(10676,10980)],
 '10_interval_certificate':[(24706,25042)],
 '90_credited_appendices':[(34806,35957),(35995,36341),(37241,37649)],
 '99_open_questions':[(8899,10675),(38209,38323)],
}

def escape(value):
 table={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','_':r'\_',
 '#':r'\#','^':r'\textasciicircum{}','{':r'\{','}':r'\}',
 '$':r'\$','~':r'\textasciitilde{}'}
 return ''.join(table.get(c,c) for c in value)

def history(label):
 names=[]
 for h in HIST.get(label,[]):
  for rec in h.get('named_historical_checks',[]):
   who=rec['who']
   if who.startswith('Claude') and '(Anthropic)' not in who:who+=' (Anthropic)'
   val=who+(', effort '+rec['effort'] if rec.get('effort') else '')+(', '+rec['date'] if rec.get('date') else '')
   if rec.get('record_kind') and rec['record_kind']!='proof check':val+=' ('+rec['record_kind']+')'
   if val not in names:names.append(val)
 return names

def record_block(block,loc,row,known=False):
 label=row['label']
 aliases=BLOCK_ALIASES.get((loc.get('file'),loc.get('start'),loc.get('end')),{label})|{label}
 names=[];ev=[];seen_events=set()
 for alias in sorted(aliases):
  for name in history(alias):
   if name not in names:names.append(name)
  for event in EVENTS.get(alias,[]):
   signature=tuple(event.get(x,'') for x in ['date','who','type','outcome'])
   if signature not in seen_events:ev.append(event);seen_events.add(signature)
 if label=='fam:src:B.4.1':
  block=block.replace(r'\citet[Theorem~1.4]{DuEtAl2026v1}',r'\citet[Theorem~7.14, label \nolinkurl{p2:thm:full-automorphisms}]{DuEtAl2026v1}')
 old=row['status'].lower()
 status='open' if old.startswith('open') or label=='ari:C.7.4' else 'proved'
 if 'refuted' in old:status='false as stated; correction and proof follow'
 checks=('Historical records: '+escape('; '.join(names))+'. ') if names else ''
 if ev:
  checks+=('Also checked in this writing by ' if names else 'Checked only in this writing by ')+r'\CurrentChecker. '
  checks+=' '.join(escape(x['outcome']) for x in ev)
 else:
  checks+='Current-writing verification remains in progress. The earlier checks named above retain their recorded scope.'
 checks=clean_check_scope(label,checks)
 if not ev:status+='; current-writing re-derivation pending'
 elif all('computation' in x['type'] for x in ev):status+='; current computational scope recorded below'
 else:status+='; current checks have the scopes recorded below'
 if known:status='known cited input; current exact-source match is recorded separately'
 actual_uses=[x['value'] for x in commands(block,'Uses')]
 uses='; '.join(actual_uses or loc.get('uses_raw',[])) or row.get('uses') or 'the definitions and exact calculations in this statement'
 if label=='fam:src:B.4.1':
  uses=uses.replace(r'\citet[Theorem~1.4]{DuEtAl2026v1}',r'\citet[Theorem~7.14, label \nolinkurl{p2:thm:full-automorphisms}]{DuEtAl2026v1}')
 for cmd in sorted(commands(block,'Uses'),key=lambda c:c['start'],reverse=True):
  block=block[:cmd['start']]+block[cmd['end']:]
 env=loc.get('env','theorem')
 if known:
  block=re.sub(r'\\begin\{'+re.escape(env)+r'\}',r'\\begin{cited}',block,count=1)
  block=block.replace('\\end{'+env+'}',r'\end{cited}',1);env='cited'
 rec='\n\\StatementRecord{'+label+'}{'+status+'}{'+checks+'}{'+uses+'}\n'
 m=re.search(r'\\begin\{'+re.escape(env)+r'\}(?:\[[^\]]*\])?',block)
 if m:
  at=m.end();labs=re.match(r'(?:\s*\\label\{[^}]+\})*',block[at:]);at+=labs.end()
  block=block[:at]+rec+block[at:]
 else:
  block=rec+block
 for m in list(re.finditer(r'\\begin\{proof\}(?:\[[^\]]*\])?(.*?)\\end\{proof\}',block,re.S))[::-1]:
  block=block[:m.start(1)]+'\n'+helper.numbered(m.group(1))+'\n'+block[m.end(1):]
 return block

def remove_duplicate_uses(body):
 """Delete only byte-identical dependencies already in a statement record."""
 recorded=set()
 for m in commands(body,'StatementRecord'):
  at=m['end']
  for _ in range(3):
   while body[at].isspace():at+=1
   value,at=argument(body,at)
  recorded.add(value)
 for m in sorted(commands(body,'Uses'),key=lambda x:x['start'],reverse=True):
  if m['value'] in recorded:body=body[:m['start']]+body[m['end']:]
 return body

def repair_outside_source_metadata(body):
 body=body.replace(r'Theorem 1.4 and Sections 2--3]{Nishiguchi1988IIRoot}',r'Theorem 1.4, preprint p.~7, and Example 2.1, p.~13]{Nishiguchi1988IIRoot}')
 body=body.replace(r'Theorem 1.4 and Example 2.1]{Nishiguchi1988IIRoot}',r'Theorem 1.4, preprint p.~7, and Example 2.1, p.~13]{Nishiguchi1988IIRoot}')
 body=body.replace(r'Section 3, especially Propositions 3.1--3.4]{SS00}',r'Propositions 3.1--3.4, preprint pp.~6--9]{SS00}')
 body=body.replace(r'Section 3, Proposition 3.1]{SchroeerSiebert2002Root}',r'Proposition 3.1, preprint pp.~6--7]{SchroeerSiebert2002Root}')
 body=body.replace(r'Theorem~1.4]{DuEtAl2026v1}',r'Theorem~1.4, p.~3]{DuEtAl2026v1}')
 body=body.replace(r'Theorem~6.12 and Proposition~6.16]{DuEtAl2026v1}',r'Theorem~6.12, pp.~81--82, and Proposition~6.16, p.~85]{DuEtAl2026v1}')
 body=body.replace(r'Proposition~7.8 and Appendix~C, Proposition~C.2]{DuEtAl2026v1}',r'Proposition~7.8, pp.~91--92, and Proposition~C.2, p.~102]{DuEtAl2026v1}')
 body=body.replace(r'Theorem~7.14, label',r'Theorem~7.14, p.~95, label')
 body=body.replace(r'Sections 2--3]{Johansson2016}',r'Section~2, pp.~2--4, and Section~3, pp.~4--6]{Johansson2016}')
 body=body.replace(r'manuscript pp.~3--5]{Parusinski1990E}',r'manuscript pp.~3--6]{Parusinski1990E}')
 body=body.replace(r'Theorems 1.6 and 13.3',r'Theorem 1.6 and the following analytic-neighborhood paragraph, preprint p.~5')
 body=body.replace(r'Theorem 1.10 and its analytic extension in Section 13',r'Theorem 1.10, preprint p.~7, with the analytic category in (0.2), p.~3')
 old=r'The full automorphism group is \citet[Theorem~1.4]{DuEtAl2026v1}.'
 new=r'The full automorphism group is \citet[Theorem~7.14, label \nolinkurl{p2:thm:full-automorphisms}]{DuEtAl2026v1}.'
 body=body.replace(old,new)
 # This obsolete Uses command is outside its source statement interval;
 # the replacement block has its own newly checked dependency list.
 for m in sorted(commands(body,'Uses'),key=lambda x:x['start'],reverse=True):
  if r'app:rederive:ari-C.6.R4' in m['value']:
   body=body[:m['start']]+body[m['end']:]
 old=(r'The three exact cases specialize \citet[Theorem~1.2 and Table~9]{miller2011}; their full arithmetic derivation is retained. '
      r'A complete re-derivation is given in Appendix~\ref{app:rederive:ari-C.6.R4}.')
 new=(r'The three exact cases specialize \citet[Definition~1.1, Theorem~1.2 and Table~9]{miller2011}. '
      r'The complete application is retained in the proof compendium, Paper~I, label \nolinkurl{app:rederive:ari-C.6.R4}.')
 return remove_duplicate_uses(body.replace(old,new))

def main():
 offsets=[0]
 for line in S.splitlines(keepends=True):offsets.append(offsets[-1]+len(line))
 groups={}
 for row in ROWS:
  loc=INDEX.get(row['source_run']+':'+row['source_id'])
  if row['paper']=='I' and loc and loc.get('file')==str(SOURCE.relative_to(BASE)) and loc.get('container_kind')=='statement_environment':
   groups.setdefault((loc['start'],loc['end']),[]).append((row,loc))
 manifest=[]
 for name,ranges in RANGES.items():
  pieces=[]
  for first,last in ranges:
   a,b=offsets[first-1],offsets[last];text=S[a:b];edits=[]
   for (x,y),entries in groups.items():
    if not (a<=x and y<=b):continue
    wanted=[(row,loc) for row,loc in entries if not row['in_compendium_only_because']]
    if wanted:
     row,loc=wanted[0];raw=S[x:y]
     rev=OUT/'papers/I/revisions'/(row['label'].replace(':','_')+'.tex')
     if rev.exists():raw=rev.read_text()
     replacement=record_block(raw,loc,row)
     manifest.append({'label':row['label'],'fragment':name+'.tex','source_start':x,'source_end':y,'current_events':len(EVENTS.get(row['label'],[])),'assembly_grants_no_check':True})
    else:
     row,loc=entries[0];reason=row['in_compendium_only_because']
     if reason.startswith(('known','classical')):
      raw=S[x:loc['statement_end']]
      rev=OUT/'papers/I/revisions'/(row['label'].replace(':','_')+'.tex')
      if rev.exists():raw=rev.read_text()
      replacement=record_block(raw,loc,row,known=True)
      replacement+='\nThe expanded source derivation is retained in the proof compendium, Paper~I, label \\nolinkurl{'+row['label']+'}.\n'
     else:
      replacement='\n% Compendium-only '+row['label']+': '+reason+'\n'
    edits.append((x-a,y-a,replacement))
   for x,y,repl in sorted(edits,reverse=True):text=text[:x]+repl+text[y:]
   pieces.append(text)
  body='\n'.join(pieces)
  body=re.sub(r'% (?:BEGIN|END) [^\n]*\n','',body)
  body=re.sub(r'\\begin\{remark\}(?:\[([^\]]*)\])?',lambda m:'\n\\paragraph{'+(m.group(1) or 'Scope')+'}',body)
  body=body.replace(r'\end{remark}','\n')
  body=repair_outside_source_metadata(body)
  if name=='90_credited_appendices':
   body='\\appendix\n\\section{Credited proofs of parameter equivalence and deformation results}\n'+body
  (OUT/'papers/I'/f'{name}.tex').write_text(body)
 # Latest night proofs retain the source IDs and their original proof text.
 for part,ids in [('11_uniform_end',[f'P2.{i}' for i in range(1,12)]),('91_credited_night',[f'P5.{i}' for i in range(1,7)])]:
  content=['\\section{'+('The uniform corner obstruction' if part.startswith('11') else 'The integral parameter comparison')+'}\n'];night_edits=[];last_end=0
  for sid in ids:
   row=next(r for r in ROWS if r['source_run']=='S6_06_BLIND' and r['source_id']==sid)
   loc=INDEX[row['source_run']+':'+sid];source=(BASE/loc['file']).read_text();block=source[loc['start']:loc['end']]
   block=re.sub(r'\\begin\{statement\}\{[^}]+\}\{[^}]+\}',r'\\begin{theorem}\\label{'+row['label']+r'}\\label{stmt:'+sid+'}',block,count=1)
   block=block.replace(r'\end{statement}',r'\end{theorem}',1)
   receiving=record_block(block,{**loc,'env':'theorem'},row)
   night_edits.append((loc['start'],loc['end'],receiving));last_end=max(last_end,loc['end'])
   manifest.append({'label':row['label'],'fragment':part+'.tex','source_file':loc['file'],'source_start':loc['start'],'source_end':loc['end'],'current_events':len(EVENTS.get(row['label'],[])),'assembly_grants_no_check':True})
  full=source[:last_end]
  for a,b,replacement in sorted(night_edits,reverse=True):full=full[:a]+replacement+full[b:]
  (OUT/'papers/I'/f'{part}.tex').write_text(repair_outside_source_metadata('\n'.join(content)+'\n'+full))
 (OUT/'analysis/I_body_manifest.json').write_text(json.dumps(manifest,indent=2))
 print(json.dumps({'retained_new_statement_blocks':len(manifest),'fragments':len(RANGES)+2,'with_scoped_current_events':sum(bool(r['current_events']) for r in manifest),'rule':'No proof check is granted by assembly'},indent=2))

if __name__=='__main__':main()
