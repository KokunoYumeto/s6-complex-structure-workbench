from pathlib import Path
import json,datetime,hashlib,csv
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I')
for env,lab,title in [('theorem','push:src:B.1.2','Finite deck quotients and central cycles'),('proposition','push:src:B.2.1','Period-invariant fans after base change')]:
 p=ed.text.index(r'\label{'+lab+'}');a=ed.text.rfind(r'\begin{'+env+'}',0,p)
 old=ed.text[a:p+len(r'\label{'+lab+'}')]
 new=old.replace(r'\begin{'+env+'}',r'\begin{'+env+'}['+title+']',1)
 ed.replace(old,new,'D12','Give the existing numbered result a short mathematical title; statement and proof are unchanged.',lab)

reps=[
 (r'''The residue
connecting map is evaluated as an actual nonzero scalar, fixing
the remaining Hodge integer at one''',r'''The residue
connecting scalar is $-iC_4/4\ne0$, which fixes the
remaining Hodge integer at one''','series:I:D','Expose the exact nonzero scalar and its consequence in the outline.'),
 (r'''Aeppli tables and the explicitly checked square-zero products''',r'''Aeppli tables; wedge products of the specified representatives
give the square-zero multiplication''','series:I:D','State the mathematical operation determining the product, without check narration.'),
 (r'''The actual integral cocycle
modulo the two period rows''',r'''The integral cocycle
modulo the two period rows''','series:I:E','Remove a process modifier without altering the cocycle map.'),
 (r'''point make every actual jump locus locally discrete''',r'''point make every jump locus locally discrete''','series:I:E','Use the exact coherent-family conclusion without a process modifier.'),
 (r'''(\hyperref[push:src:E.1.2]{\ref*{push:src:E.1.2}},
\hyperref[push:src:E.2.1]{\ref*{push:src:E.2.1}}).
\item\hypertarget{step-I-E-6}{} Differentiating the actual''',r'''(\hyperref[fam:src:B.3.1]{\ref*{fam:src:B.3.1}},
\hyperref[push:src:E.2.1]{\ref*{push:src:E.2.1}}).
\item\hypertarget{step-I-E-6}{} Differentiating the''','series:I:E','Point to the unique weighted-root proof now consolidated in B3.1 and remove a process modifier.'),
]
for old,new,lab,reason in reps:ed.replace(old,new,'D07',reason,lab)
p=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_program_scope_guards.json'
for x in json.loads(p.read_text())['changes']:ed.replace(x['old'],x['new'],'D09',x['reason'],x['statement_id'])
ed.save()

intake=json.loads((r/'records/S6_SERIES_PUBLISH_I_global_DE_intake.json').read_text())
freeze=r/'records/S6_SERIES_PUBLISH_I_global_DE_freeze.json'
out={
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'freeze_path':str(freeze.relative_to(r)),
 'freeze_sha256':hashlib.sha256(freeze.read_bytes()).hexdigest(),
 'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),
 'scope':'Final global main-theorem/outline/body consistency comparison for D and E. Prior exposure to historical outlines and full body proofs is disclosed in the frozen derivation; no new independent proof is claimed. Current complete D/E outlines and all seven main statements were reopened only after that freeze.',
 'D':{
  'outcome':'PASS after scalar and wedge-product wording made precise; no mathematical conclusion changed.',
  'claim_map':['Nonzero scalar -i C4/4 gives rank one and fixes h=1.','Four rank-one d1 arrows leave only E2^(0,0) and E2^(3,3).','Bott–Chern/Aeppli dimensions have the exact (p,q)↔(3-p,3-q) duality; all positive-degree products vanish by the stated representative wedges.','Ordinary relative modules are exterior quotients by dt; the exact presentation retains the nonreduced-fibre torsion.','The full coefficient atlas yields G and Q with the factor twelve; conjugation, H2=0 and the restriction square -12 exclude a real representative.']},
 'E':{
  'outcome':'PASS after the vertical bundle notation was aligned and the root-map reference pointed to its unique proof.',
  'claim_map':['The weighted degrees and Leray yield all four integer-twist dimensions and the tuple (1,1,1,0) at zero.','Distinct base points, the regular stalk lengths, finite character lengths and cusp contribution one give (0,J,1+J,0).','Finiteness and local discreteness use the complete proper coherent-family argument.','The root-forgetting map and tangent sequence give the higher-multiplicity tuple in the stated coprime range.','The nonzero Kodaira–Spencer class and its exact change under u=exp(-2 pi i c) give the reduced smooth Kuranishi line; exp(2 pi i a) identifies C/Z with C*.'],
  'additional_after_outline_read':'The coefficient 123 i k/(64 pi) in E step 3 was compared after the current outline was read: nu2^2=9 F^2/512, tau1=i pi F^2/2 and K2=3 F^2/4 imply -k(K2+12 nu2^2)/tau1=123 i k/(64 pi). This coefficient check receives exposed reread scope only; it was not in the frozen pre-outline derivation.'},
 'computational_scope':'The saved fresh consistency program checks the printed D arrays, four d1 ranks, dual dimensions, square-zero ideal dimension, all twelve residue classes of d(n), its period shift and the n=0 E tuple. It does not supply a new analytic proof of the body inputs.',
 'status_claims':'Final literature status and source/date claims remain under separate provenance verification.'}
receipt=r/'records/S6_SERIES_PUBLISH_I_global_DE_comparison.json'
receipt.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group']
rows=[]
for typ,scope,group in [
 ('used and rechecked in this run',out['scope'],'exposed-comparison'),
 ('computation or formal certificate',out['computational_scope'],'consistency-computation')]:
 for lab in ['series:I:D','series:I:E']:
  rows.append(dict(zip(fields,[lab,'2026-11-21','GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; S6_SERIES_PUBLISH root',typ,'PASS: '+scope,'publish-I-global-DE-'+group+'-'+lab.rsplit(':',1)[1],'Paper I final global comparison',str(receipt),'',typ,'publish-I-global-DE-'+group])))
events=r/'records/S6_SERIES_PUBLISH_I_global_DE_CHECK_EVENTS.tsv'
assert not events.exists()
with events.open('w') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'comparison':str(receipt),'events':len(rows),'groups':2}))
