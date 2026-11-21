from pathlib import Path
from datetime import datetime,timezone
import json,re,hashlib
R=Path('/workspace/scratch/653608133b22');B=R/'work/agents/i_provenance';p=R/'work/S6_SERIES_PUBLISH_I.tex';s=p.read_text();intake=json.loads((B/'S6_SERIES_PUBLISH_I_residual_prebuild_intake.json').read_text())
sha=lambda t:hashlib.sha256(t.encode()).hexdigest()
changes=[]
def add(i,old,new,why):
 assert s.count(old)==1,(i,s.count(old))
 changes.append(dict(id='I-residue-provenance-'+str(i),candidate_indices=i if isinstance(i,list) else [i],old=old,new=new,reason=why))
add(2,'This proves descent under the actual period identifications.','This proves descent under the period identifications.','Remove a redundant adjective; the displayed rigidified line-bundle isomorphism and its descent argument remain unchanged.')
add(5,r'''Their remaining defect differs from $\ell_0$ by an actual toric lattice vector;''',r'''Their remaining defect differs from $\ell_0$ by a toric lattice vector;''','Remove a redundant adjective; the integral toric defect and subsequent choice of q remain unchanged.')
add(6,r'''The terms $a\sigma-\sigma'$ are retained, even when their chosen lifts have essential singularities at the puncture; they belong to the specified collar reference, while differences of allowed extensions are holomorphic $\eta_0$.''',r'''The specified collar reference contains the full terms $a\sigma-\sigma'$, including any essential singularities of their chosen lifts at the puncture; differences of allowed extensions are holomorphic $\eta_0$.''','State the inclusion in the fixed collar reference positively; keep the full singular terms and holomorphic difference space.')
add(7,'Thus the comparison fixes the positive circle class and the actual local complex structures, in addition to their monodromy matrices.','Thus the comparison fixes the positive circle class and the local complex structures, in addition to their monodromy matrices.','Remove a redundant adjective; preserve the displayed integral and complex-linear comparison maps.')
add(8,'with $m_j$ replaced by these actual covering degrees','with $m_j$ replaced by these covering degrees','Remove a redundant adjective; the degree3k/4l root maps and norms remain unchanged.')
add(9,'Consequently the actual\ncounterclockwise translation vector','Consequently the\ncounterclockwise translation vector','Remove a redundant adjective; the inverse-generator sign and exact vector remain unchanged.')
add(13,'$\\gamma$ to the actual gluing translation therefore gives the','$\\gamma$ to the gluing translation therefore gives the','Remove a redundant adjective; preserve the actual character applied to the same gluing translation.')
add(14,r'''For \(h=12\), remove the actual period''',r'''For \(h=12\), remove the period''','Remove a redundant adjective; the exact integral period and following scalar are unchanged.')
add(15,r'''The original
uniformizers are retained: these are units because''',r'''With the original
uniformizers, these are units because''','Keep the original root parameters and both stated unit identities, expressed positively.')
add([16,17],'''restriction of $f$ to each indicated fibre, with its scheme
multiplicity retained. The ordinary period quotient, finite affine
quotients and the paired hexagon are the three actual local models''','''restriction of $f$ to each indicated fibre, with its scheme
multiplicity. The ordinary period quotient, finite affine
quotients and the paired hexagon are the three local models''','Keep scheme multiplicities3S1 and4S2 and all three exact local models; remove redundant modifiers only.')
add(18,'Choose an\nactual lift $g(A,y,s)\\in\\Gamma$','Choose a\nlift $g(A,y,s)\\in\\Gamma$','Remove a redundant adjective; the lift remains in Gamma under the already stated surjection.')
add(19,'All three are actual left translations\nin $\\Gamma$','All three are left translations\nin $\\Gamma$','Remove a redundant adjective; the exact Heisenberg translations and coset conclusion remain unchanged.')
add(27,'Thus the constructed finite models fill the actual local\npullback by $w=r^6$','Thus the constructed finite models fill the local\npullback by $w=r^6$','Remove a redundant adjective; keep the specified punctured holomorphic conjugacy and degree-six pullback.')
add('27-opening','\\item We retain source and target arguments. Write primes for','\\item Write primes for','The next sentence already specifies evaluation at the target g_j s, and every primed/unprimed matrix entry is unchanged; remove introductory process language.')
proposed=s
for c in changes:proposed=proposed.replace(c['old'],c['new'])
proofrows=[]
mathpat=re.compile(r'(?s)\$(?:\\.|[^$])*\$|\\\(.*?\\\)|\\\[.*?\\\]|\\begin\{(?:equation\*?|align\*?|gather\*?)\}.*?\\end\{(?:equation\*?|align\*?|gather\*?)\}')
for row in intake['proof_scopes']:
 old=Path(row['old_file']).read_text();assert s.count(old)==1,(row['label'],s.count(old))
 new=old
 ids=[]
 for c in changes:
  if c['old'] in new:new=new.replace(c['old'],c['new']);ids.append(c['id'])
 path=Path(row['old_file'].replace('_old.tex','_proposed.tex'));path.write_text(new)
 assert mathpat.findall(old)==mathpat.findall(new),row['label']
 assert re.findall(r'\\(?:label|tag|hypertarget)\{[^}]*\}',old)==re.findall(r'\\(?:label|tag|hypertarget)\{[^}]*\}',new)
 start=s.index(old);pre=s[max(0,start-15000):start];rec=list(re.finditer(r'\\StatementRecord\{([^}]+)\}',pre));canonical=rec[-1][1] if rec else row['label']
 proofrows.append({**row,'canonical_statement_id':canonical,'old_sha256':sha(old),'proposed_file':str(path),'proposed_sha256':sha(new),'changes':ids,'complete_old_proof_read':True,'complete_proposed_proof_read':False,'all_math_tokens_labels_tags_identical':True,'scope':'Terminology/presentation comparison only; no new mathematical conclusion or independent checking credit.'})
start=s.rfind('\\begin{figure}',0,s.index('The arrows denote the'));end=s.index('\\end{figure}',start)+len('\\end{figure}')
capold=s[start:end];capnew=capold
for c in changes:capnew=capnew.replace(c['old'],c['new'])
for suffix,t in [('old',capold),('proposed',capnew)]: (B/f'S6_SERIES_PUBLISH_I_residual_prebuild_orbifold_figure_{suffix}.tex').write_text(t)
assert mathpat.findall(capold)==mathpat.findall(capnew)
record={'created_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(s),'intake_source_sha256':intake['source_sha256'],'guard_count':len(changes),'dispositions':[{'candidate':10,'outcome':'retained','reason':'Corrected divisor class is the mathematical perpendicular projection obtained by zero-section, fibre and rational component corrections; the following complete proof defines that operation explicitly. It is not production history.'}],'proof_scopes':proofrows,'figure_scope':{'label':'fig:I:orbifold','complete_old_and_proposed_read':False,'old_sha256':sha(capold),'proposed_sha256':sha(capnew)},'mathematical_check_events_added':0,'independent_credit_added':0,'classification':'Full affected-proof text read for wording preservation. These edits are presentation QA, with all mathematical expressions identical; no CHECK_EVENTS file is created.','final_status':'proposed texts await complete rereading before ready notice'}
(B/'S6_SERIES_PUBLISH_I_residual_prebuild_guards.json').write_text(json.dumps({'source_sha256':sha(s),'changes':changes,'mathematical_check_events_added':0},ensure_ascii=False,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_residual_prebuild_comparison.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'guards':len(changes),'proofs_changed':sum(bool(x['changes']) for x in proofrows),'proofs_reviewed':len(proofrows),'source_sha256':sha(s),'mathematical_check_events_added':0},indent=2))
