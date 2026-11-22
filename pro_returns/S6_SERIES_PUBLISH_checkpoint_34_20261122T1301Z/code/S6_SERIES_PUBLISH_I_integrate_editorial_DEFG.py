from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor

r=Path(__file__).resolve().parents[1]
paths=[r/'agents/i_provenance/S6_SERIES_PUBLISH_I_editorial_famD_C34_guards.json']
paths += [r/f'agents/i_analytic/S6_SERIES_PUBLISH_I_editorial_batch_{x}_guards.json' for x in 'efg']
ed=Editor('I');sources=[]
for p in paths:
 d=json.loads(p.read_text());changes=d.get('guards',d.get('changes'))
 for x in changes:
  new=x['new']
  if x['id']=='I-DC-title-D.1.4':
   new=new.replace('The Neron--Severi lattice',r"The N\'eron--Severi lattice")
  if x['id']=='IA-G-01':
   new=new.replace('Let $R_N=(P,r_N)$ be the actual compact point specified by','Let $R_N=(P,r_N)$ be the complex compact point specified by')
   new=new.replace('This statement makes no assertion that $R_N$ is algebraic.\n','')
  if x['id']=='IA-G-21':
   new='\\part{Results not yet established}\n'+new
   new=new.replace('The Relative Semi-abelian Conjecture\n',
      'The open lower-bound question is the Relative Semi-abelian Conjecture\n')
   new=new.replace('proposes, for\nalgebraic lifts in the indicated semiabelian varieties, the bound',
      'which asks whether algebraic lifts in the indicated semiabelian\nvarieties satisfy the bound')
  if x['id']=='IA-F-12':
   new=new.replace('parameters C.6 therefore makes',r'parameters \cref{ari:C.6.1} makes')
  ed.replace(x['old'],new,x.get('type','D08'),x['reason'],x['id'],count=x.get('expected_count',1))
 sources.append({'path':str(p.relative_to(r)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'guards':len(changes)})
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_editorial_DEFG_integration.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':sources,
 'root_review':'All proposed new passages and guard reasons read; D/C3/C4 full comparison report read. The agents read and compared all affected old/new proofs; their scoped evidence records document that work. Root has not claimed a second full old-proof reread for this integration.',
 'scope':'Editorial integration and exact-anchor verification, with no additional independent proof event.',
 'open_part':'The former conjectural theorem is moved to final open prose with the original C7.4 identifiers. Its unconditional period-field calculation is a proved lemma. The original C7.5 question anchor is restored. The final open part heading is explicit.',
 'changes_to_proposed_text':['Add the final open part heading.','Use an open-question formulation for the relative-period bound.','Remove the defensive sentence about algebraicity of the compact point.','Resolve the residual C.6 prose reference to the exact global-height proposition.','Restore the Neron accent.']
},indent=2)+'\n')
