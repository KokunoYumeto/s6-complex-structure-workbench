#!/usr/bin/env python3
"""Apply the 33 receiving corrections without overwriting historical claims.

All exact text changes and original inventory fields are recorded for undo.
The source/proof of every old false row remains byte-for-byte present after
the generated link.  Construction locators and refutation locators are typed
separately from whole corrected-conclusion dependencies.
"""
from __future__ import annotations
import argparse,csv,datetime,hashlib,json,re
from pathlib import Path
from corrected_items import ITEMS

csv.field_size_limit(16*1024*1024)
ROOT=Path(__file__).resolve().parents[2]
AUD=ROOT/'analysis/continuation_IV'
WHO='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation'
RECEIPT=AUD/'correction_split_patch.json'
BEGIN='% BEGIN CONTINUATION_CORRECTED_33'
END='% END CONTINUATION_CORRECTED_33'

# These proofs produce correction inputs.  Their references to older rows
# locate concrete maps, initial data, or the claim being refuted, rather than
# assert the false compound theorem.  Redirecting them to the whole corollary
# that uses their conclusion would be an untyped circular dependency.
INPUT_PRODUCERS={
 'night:P3K.'+str(n) for n in [61,62,64,65,67,68,69,70,73,74,76,77]
}

def sha(data):return hashlib.sha256(data if isinstance(data,bytes) else data.encode()).hexdigest()
def write_csv(path,rows,fields,delimiter=','):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fields,delimiter=delimiter);w.writeheader();w.writerows(rows)
def obj(s):
 try:v=json.loads(s);return v if isinstance(v,dict) else {'raw':v}
 except (ValueError,TypeError):return {'raw':s}
def braced(s,at):
 assert s[at]=='{';d=1;i=at+1
 while d:
  if s[i]=='{' and s[i-1]!='\\':d+=1
  if s[i]=='}' and s[i-1]!='\\':d-=1
  i+=1
 return s[at+1:i-1],i
def records(s):
 out=[]
 for m in re.finditer(r'\\StatementRecord\s*\{',s):
  vals=[];ranges=[];at=m.end()-1
  for _ in range(4):
   while s[at].isspace():at+=1
   start=at;val,at=braced(s,at);vals.append(val);ranges.append((start,at))
  out.append(dict(start=m.start(),end=at,values=vals,ranges=ranges))
 return out

def new_fragment():
 parts=[BEGIN, r'''\section{The separately stated physical and fan corrections}
The following items separate the corrected conclusions from the
historical compound assertions retained in the next section.  The
physical line is \(M\), its outward-meridian-one dual is
\(U=M^{-1}\), and the quotient orientation is fixed throughout.
Each historical source locator identifies the concrete construction
or the false claim being corrected; its false numerical conclusion
is not a premise.  The full physical transfer and fan proofs cited
below appear earlier in this paper, with their own check scopes.
The remaining renewed checks of those input proofs are recorded
separately in the inventory.
''']
 for x in ITEMS:
  refs=','.join(x['correction_inputs'])
  extra=sorted(set(re.findall(r'\\(?:c|C)ref\{([^}]+)\}',x['statement']+' '+x['proof'])))
  internal=[]
  for group in extra:
   for lab in group.split(','):
    if lab.startswith('iv:correction:') and lab not in internal:internal.append(lab)
  if internal:refs+=','+','.join(internal)
  check=(r'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, '
   r'S6\_10\_PAPERS continuation, 19 November 2026: targeted proof check '
   r'of this receiving correction from its named inputs; computation or '
   r'formal certificate at the exact arithmetic scope recorded in the event '
   r'ledger. The retained geometric input proofs keep their own check '
   r'records; this split does not close their renewed whole-proof gates.')
  uses=r'\cref{'+refs+r'}; the concrete construction locators retained at \cref{'+x['historical_label']+'}'
  parts.extend([
   '\n\\begin{proposition}\\label{'+x['label']+'}',
   '\\StatementRecord{'+x['label']+'}{proved}{'+check+'}{'+uses+'}',
   '\\textbf{'+x['title']+'.}\\par',
   x['statement'],r'\end{proposition}',r'\begin{proof}',x['proof'],r'\end{proof}',''])
 parts.append(END)
 return '\n'.join(parts)+'\n\n'

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');ap.add_argument('--undo',action='store_true');a=ap.parse_args()
 if a.undo:
  receipt=json.loads(RECEIPT.read_text())
  for f in receipt['files']:
   p=ROOT/f['path'];s=p.read_text()
   if sha(s)!=f['after_sha256']:raise ValueError('Refusing undo after intervening source changes: '+str(p))
  for f in receipt['files']:
   p=ROOT/f['path'];s=p.read_text()
   for e in reversed(f['edits']):
    if s.count(e['new'])!=1:raise ValueError('Undo match not unique')
    s=s.replace(e['new'],e['old'],1)
   assert sha(s)==f['before_sha256'];p.write_text(s)
  print('Source changes reversed. Inventory/event provenance remains; use recorded field patches explicitly to reverse inventory.');return
 if RECEIPT.exists():raise ValueError('Split receipt already exists. Do not silently overwrite historical patch provenance.')
 with (ROOT/'S6_10_PAPERS_inventory.csv').open() as f:
  rd=csv.DictReader(f);fields=rd.fieldnames;inv=list(rd)
 bylabel={r['label']:r for r in inv}
 old_to_new={x['historical_label']:x['label'] for x in ITEMS}
 assert not set(old_to_new.values())&set(bylabel)
 for x in ITEMS:assert bylabel[x['historical_label']]['status']=='false as stated'
 flags=list(csv.DictReader((ROOT/'analysis/continuation_ledger/sweep1_flag_verdicts.tsv').open(),delimiter='\t'))
 flagby={r['label']:r for r in flags}
 dependency=[]
 for row in inv:
  if row['label'] in old_to_new:continue
  targets=sorted(set(re.findall(r'night:P3[FK]\.\d+',row['uses']))&set(old_to_new))
  if not targets:continue
  flag=flagby.get(row['label'],{})
  refutation=flag.get('verdict','')=='sound: uses the refutation'
  if refutation:action='retain historical refutation locator'
  elif row['label'] in INPUT_PRODUCERS:action='retain construction/input locator; corrected conclusion not a premise'
  elif row['paper']!='IV':action='paper-owner patch recommended'
  else:action='redirect receiving dependency to corrected item'
  for old in targets:
   dependency.append(dict(dependent=row['label'],paper=row['paper'],historical_locator=old,
    corrected_item=old_to_new[old],action=action,
    scope=flag.get('verdict','fresh receiving dependency classification'),
    detail=flag.get('note','Uses the marked source/comparison construction or the corrected receiving conclusion at its stated scope; historical false conclusion remains excluded.'),
    sweep_source_row=flag.get('source_row','')))

 depby={}
 for d in dependency:depby.setdefault(d['dependent'],[]).append(d)
 fragment=new_fragment()
 source_results=[]
 # Only owned IV files are changed.  Root assembles canonical paper TeX.
 for rel in ['papers/IV/body.tex','papers/IV/body_source.tex']:
  p=ROOT/rel;before=p.read_text();s=before;edits=[]
  assert BEGIN not in s
  # Every macro replacement is made from the exact current row, preserving
  # all four original fields before a scoped Uses change.
  rs=records(s)
  for r in reversed(rs):
   lab=r['values'][0]
   if lab in old_to_new:
    note=('\n% BEGIN HISTORICAL_REFINED_LINK '+lab+'\n'
     '\\par\\noindent\\textbf{Refined receiving item:} '
     '\\cref{'+old_to_new[lab]+'}. '
     'The full historical statement and argument below are retained as the '
     'located false compound claim. Only the construction or comparison '
     'subclaims expressly identified in that correction are used subsequently.\n'
     '% END HISTORICAL_REFINED_LINK '+lab+'\n')
    old=s[r['start']:r['end']];new=old+note
   elif lab in depby:
    ds=depby[lab];vals=r['values'].copy()
    mapping={d['historical_locator']:d['corrected_item'] for d in ds if d['action']=='redirect receiving dependency to corrected item'}
    for oldlab,newlab in mapping.items():
     vals[3]=re.sub(r'(?<![A-Za-z0-9.:])'+re.escape(oldlab)+r'(?![0-9])',lambda m:newlab,vals[3])
    note_parts=[]
    for d in ds:
     oldlab=d['historical_locator'];newlab=d['corrected_item']
     if d['action']=='retain historical refutation locator':
      note_parts.append(r'\cref{'+oldlab+r'} locates the historical claim refuted here; its separate corrected item is \cref{'+newlab+'}')
     elif d['action'].startswith('retain construction'):
      note_parts.append(r'\cref{'+oldlab+r'} supplies only its explicitly retained source, cap, framing or comparison data; the corrected conclusion at \cref{'+newlab+r'} is not an input to this correction-producing proof')
     else:
      note_parts.append(r'the receiving dependency formerly written as \cref{'+oldlab+r'} now points to \cref{'+newlab+r'} at the retained construction or corrected-conclusion scope; any old locator inside the source argument continues to locate its actual maps')
    note=('\n% BEGIN CORRECTION_DEPENDENCY_SCOPE '+lab+'\n'
     '\\par\\noindent\\textit{Dependency scope.} '+'; '.join(note_parts)+'.\n'
     '% END CORRECTION_DEPENDENCY_SCOPE '+lab+'\n')
    old=s[r['start']:r['end']]
    new='\\StatementRecord'+''.join('{'+v+'}' for v in vals)+note
   else:continue
   assert s.count(old)==1,(rel,lab)
   s=s.replace(old,new,1);edits.append(dict(label=lab,old=old,new=new))
  heading=r'\section{Corrections with their located counterexamples}'
  assert s.count(heading)==1
  s=s.replace(heading,fragment+heading,1);edits.append(dict(label='33 receiving corrections',old=heading,new=fragment+heading))
  # The old mathematical theorem/proof bytes are untouched: all patches
  # above affect metadata plus generated links and insert a new section.
  source_results.append(dict(path=rel,before_sha256=sha(before),after_sha256=sha(s),edits=edits,new_text=s))

 patches=[]
 for row in inv:
  lab=row['label'];new=row.copy();notes=obj(row['notes'])
  if lab in old_to_new:
   notes.setdefault('source_statement_preserved_manifest','analysis/continuation_IV/corrected_rows_source_manifest.json')
   notes['refined_statement_id']=old_to_new[lab]
   notes['historical_false_claim_preserved_in_full']=True
   notes['correction_split_receipt']='analysis/continuation_IV/correction_split_patch.json'
   new['notes']=json.dumps(notes,ensure_ascii=False)
  if lab in depby:
   notes['corrected_row_dependency_roles']=depby[lab]
   for d in depby[lab]:
    if d['action']=='redirect receiving dependency to corrected item':
     new['uses']=re.sub(r'(?<![A-Za-z0-9.:])'+re.escape(d['historical_locator'])+r'(?![0-9])',lambda m:d['corrected_item'],new['uses'])
   new['notes']=json.dumps(notes,ensure_ascii=False)
  changed={k:dict(before=row[k],after=new[k]) for k in fields if row[k]!=new[k]}
  if changed:patches.append(dict(label=lab,fields=changed));row.update(new)

 # New rows inherit allocation and credit provenance, not old check events.
 newrows=[]
 for x in ITEMS:
  original=bylabel[x['historical_label']]
  refs=list(x['correction_inputs'])
  for group in re.findall(r'\\(?:c|C)ref\{([^}]+)\}',x['statement']+' '+x['proof']):
   for lab in group.split(','):
    if lab.startswith('iv:correction:') and lab not in refs:refs.append(lab)
  notes=dict(source_status='Receiving corrected consequence of the named proved physical/fan results',
   source_false_claim=x['historical_label'],refines=x['historical_label'],
   source_statement_preserved_manifest='analysis/continuation_IV/corrected_rows_source_manifest.json',
   retained_construction_scope=x['retained_construction_scope'],
   original_construction_locator_role='Data and retained construction maps only; the historical false numerical conclusion is not a premise.',
   receiving_source='papers/IV/corrected_physical_items.tex',
   complete_receiving_statement=x['statement'],complete_receiving_proof=x['proof'],
   correction_inputs=refs,
   continuation_three_check_gates={
    'proof_rederivation_before_reading':'pending for full geometric input chain; targeted receiving corollary derivation and exact comparison recorded',
    'new_independent_computations':'fresh exact arithmetic verified at the event scope; input geometric computation gates remain separate',
    'renewed_main_result_credit_check':'pending as a new receiving item; original correction/producer credit retained, no unrestricted novelty claim'},
   correction_split_receipt='analysis/continuation_IV/correction_split_patch.json')
  cr=dict(current_writing='proved',current_writing_event_rule='Only exact continuation correction and arithmetic events are attached. Historical input proof checks remain at their own labels.',
   inherited_input_event_locators=[x['historical_label']]+refs)
  r={k:'' for k in fields};r.update(paper='IV',label=x['label'],source_run='S6_10_PAPERS',source_id='correction:'+x['source_id'],
   kind='Correction',status='proved',main_or_supporting=original['main_or_supporting'],
   uses='; '.join(refs),check_record=json.dumps(cr,ensure_ascii=False),
   credited_to='S6_06_BLIND physical corrections K68--K69 and the exact fan/endpoint results listed in Uses; receiving split requested by sweep1 correction4. Original credit record: '+original['credited_to'],
   notes=json.dumps(notes,ensure_ascii=False))
  newrows.append(r)
 inv.extend(newrows)

 arith=json.loads((AUD/'corrected_items_arithmetic.output.json').read_text())
 events=[]
 def event(label,typ,outcome,refined=''):
  events.append(dict(statement_id=label,date='2026-11-19',who=WHO,type=typ,outcome=outcome,refined_statement_id=refined))
 for x in ITEMS:
  event(x['label'],'targeted proof check',
   'Derived the full stated receiving correction from its explicitly named physical/fan inputs and compared the relevant K69/K74 correction proofs after saving the initial derivation. Exact proof is printed at this label. Retained construction scope: '+x['retained_construction_scope']+'. The underlying geometric input proofs were not all freshly rederived; this event does not close their whole prereading gates. Receipt: analysis/continuation_IV/corrected_items_derivation_receipt.json; comparison: analysis/continuation_IV/corrected_items_comparison.md.')
  cs=[q['name'] for q in arith['checks'] if x['label'] in q['labels']]
  event(x['label'],'computation or formal certificate',
   'Fresh independent exact correction arithmetic program PASS, with this item covered only by: '+'; '.join(cs)+'. Code: code/continuation_IV/verify_corrected_items.py; output: analysis/continuation_IV/corrected_items_arithmetic.output.json. No full geometric proof or complete fan-image theorem is certified by these arithmetic tests.')
  event(x['historical_label'],"refuted, with the refined statement's id",
   'Targeted comparison preserves the entire historical compound claim and its argument, and locates its corrected convention, numerical value, or scope in the separate proved receiving item '+x['label']+'. No historical source row is deleted. Exact statement/proof and retained construction scopes: code/continuation_IV/corrected_items.py. Refutation is at this corrected-conclusion scope; no fresh full geometric re-proof is inferred.',x['label'])
  event(x['label'],'used and rechecked in this run',
   'Metadata reconciliation only; no new mathematical check. Created the separate receiving correction, linked the historical false claim, preserved its complete source/proof, retained original allocation and credit, and mapped dependencies by construction/refutation/conclusion role. Sweep correction4; patch receipt analysis/continuation_IV/correction_split_patch.json.')
 for lab,ds in depby.items():
  event(lab,'used and rechecked in this run',
   'Metadata reconciliation only; no new mathematical check. Correction4 dependency roles explicitly mapped: '+'; '.join(d['historical_locator']+' -> '+d['corrected_item']+' ['+d['action']+']' for d in ds)+'. Actual mathematical scope follows the cited source/map comparison, not the false historical numerical conclusion. Full table: analysis/continuation_IV/corrected_dependency_map.tsv.')

 summary=dict(created_at=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
  new_items=len(ITEMS),new_main_items=sum(r['main_or_supporting']=='main' for r in newrows),
  historical_claims_preserved=len(ITEMS),dependent_rows=len(depby),dependency_edges=len(dependency),
  actions={a:sum(d['action']==a for d in dependency) for a in sorted({d['action'] for d in dependency})},
  events=len(events),scope='Receiving correction split and exact corollary derivations. Historical source/proof bytes retained. No blanket whole-input reproof gate is closed.')
 receipt=dict(summary=summary,files=[{k:v for k,v in f.items() if k!='new_text'} for f in source_results],
  inventory_original_field_patches=patches,new_inventory_labels=[r['label'] for r in newrows])
 if a.apply:
  for f in source_results:(ROOT/f['path']).write_text(f['new_text'])
  (ROOT/'papers/IV/corrected_physical_items.tex').write_text(fragment)
  write_csv(ROOT/'S6_10_PAPERS_inventory.csv',inv,fields)
  write_csv(ROOT/'records/continuation_IV_correction_events.tsv',events,list(events[0]),'\t')
  write_csv(AUD/'corrected_dependency_map.tsv',dependency,list(dependency[0]),'\t')
  write_csv(AUD/'corrected_main_results_map.tsv',[
   dict(historical_label=x['historical_label'],corrected_label=x['label'],title=x['title'],
    allocation=bylabel[x['historical_label']]['main_or_supporting']) for x in ITEMS],
   ['historical_label','corrected_label','title','allocation'],'\t')
  ovpath=ROOT/'analysis/continuation_ledger/owner_overrides.json';ov=json.loads(ovpath.read_text())
  for x in ITEMS:
   ov[x['label']]=dict(status='proved',kind='Correction',basis='Explicit receiving corollary proof in papers/IV/corrected_physical_items.tex, from named physical/fan inputs; full renewed input-chain gates remain separate.')
  ovpath.write_text(json.dumps(ov,indent=2,ensure_ascii=False)+'\n')
  RECEIPT.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
 else:
  (AUD/'correction_split_preview.json').write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
