from pathlib import Path
import json, hashlib, datetime, re
from S6_SERIES_PUBLISH_editing import Editor

r=Path(__file__).resolve().parents[1]
ed=Editor('I'); sources=[]
for rel,key in [
 ('agents/i_topology/editorial/S6_SERIES_PUBLISH_I_boundary_batch4_guarded.json','patches'),
 ('agents/i_analytic/S6_SERIES_PUBLISH_I_analytic_setup_guards.json','guards'),
 ('agents/i_provenance/S6_SERIES_PUBLISH_I_primary_citation_guards_05.json','changes')]:
 p=r/rel; d=json.loads(p.read_text())
 for x in d[key]:
  new=x['new']
  if key=='guards':
   new=re.sub(r'(\\hypertarget\{tag-(IA2[1-8])\}\{\}\\label\{([^}]+)\})',
    lambda m:m[1]+'\n'+r'\StatementRecord{'+m[3]+r'}{proved}{'+m[2]+r'}{}',new)
  ed.replace(x['old'],new,x.get('type','D12'),x['reason'],x['id'],count=x.get('expected_count',1))
 sources.append({'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'guards':len(d[key])})
ed.replace(r'\begin{proposition}[The repaired local plumbing model]',
 r'\begin{proposition}[The local plumbing model]','D01',
 'Remove revision history from the mathematical title.','push:src:B.4.23')

# This correction was applied inside boundary batch 3. Record its exact scope
# separately, without applying the overlapping old guard a second time.
p=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_push_A12_selected_diagonal_guard.json'
x=json.loads(p.read_text())['changes'][0]
assert r'(v,Y,a)\longmapsto(av,uY,aY,v)' in ed.text
ed.record('D25',x['old'],x['new'],
 x['reason']+' Applied as part of boundary batch 3; this row isolates the proof error. The theorem statement is unchanged. Evidence: S6_SERIES_PUBLISH_I_push_A12_selected_diagonal_ERROR_EVENT.json.',
 'push:src:A.1.2')

bp=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_shared_bib_guards_05.json'
bd=json.loads(bp.read_text()); bib=r/'S6_SERIES_PUBLISH_references.bib'; bt=bib.read_text()
for x in bd['changes']:
 assert bt.count(x['old'])==x.get('expected_count',1),x['id']
 bn=x['new'].replace('}\n  current_run_additional_locators', '},\n  current_run_additional_locators')
 bt=bt.replace(x['old'],bn)
ed.save();bib.write_text(bt)

receipt={
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'sources':sources,'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),
 'root_review':'Read the full boundary4 comparison, all changed passages, all ten arithmetic setup guards, all primary05 guards, and the A1.2 exact error record and applied comparison. Complete old/new boundary proof comparisons are in the agent record. Integration creates no additional independent mathematical credit.',
 'root_variations':['Add the eight missing printable tag records to new arithmetic Definitions and Remarks.','Remove repaired from the local plumbing title.','Insert the missing BibTeX field commas before two added verification fields.','Isolate the already applied selected-diagonal proof correction as D25.'],
 'remaining':'Full candidate build, equation numbering, final program table and all final rendered pages remain open.'}
(r/'records/S6_SERIES_PUBLISH_I_boundary4_setup_primary5_integration.json').write_text(json.dumps(receipt,indent=2)+'\n')
with (r/'S6_SERIES_PUBLISH_report.md').open('a') as f:
 f.write('\n### Paper I: selected-diagonal chart correction, 21 November 2026\n\n'
 'The frozen A1.2 check found that the proof\'s charts x=za and z=xb describe the opposite diagonal to the selected toric edge. The corrected maps use Y=y/u and (v,Y,a) to (av,uY,aY,v), and (x,z,b) to (x,ubz,z,bx), with b=1/a and (x,z)=a(v,Y). Their character valuation selects [e1,e2]. Both resolutions contract to xY=zv; the common O(-1,-1) over the Segre quadric gives the two ruling projections. The theorem is unchanged. The existing targeted and computational evidence group records the correction; no false statement or new independent check is invented. The exact error, frozen derivation, and applied-source comparison are retained in agents/i_provenance.\n')
