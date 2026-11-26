#!/usr/bin/env python3
"""Stage LN's exact replacement guards, defect rows and narrowly typed events.
Only this receiving lane is written; no canonical/global table is mutated.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import csv,re
ROOT=Path.cwd();LANE=ROOT/'agents/continuation7_iii_general_initial_receiving'
canonical=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
assert sha256(canonical.encode()).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
fresh=ROOT/'agents/continuation7_iii_general_initial/S6_SERIES_PUBLISH_III_02LN_fresh_derivation.md'
assert sha256(fresh.read_bytes()).hexdigest()=='5ec1801a4ab89089407ce1c069bdeb64e4ca3f14c5e3c6bdb36996cea8417ce3'
SID='maps:src:D.2.46';PREFIX='S6_SERIES_PUBLISH_III_02LN_'
receiver=(LANE/(PREFIX+'receiving.tex')).read_text()
assert sha256(receiver.encode()).hexdigest()=='eadeaeb34b25651ae161a269fc19d504e57ce6486a3c2c4aceeff608630a37f2'

def env(text,name):
 start=text.index('\\begin{'+name+'}')
 end=text.index('\\end{'+name+'}',start)+len('\\end{'+name+'}')
 return text[start:end]

oldstatement=env((LANE/(PREFIX+'released_statement.tex')).read_text(),'theorem')
oldproof=env((LANE/(PREFIX+'released_proof.tex')).read_text(),'proof')
oldaux=(LANE/(PREFIX+'released_following_auxiliary.tex')).read_text()
newstatement,newproof=env(receiver,'theorem'),env(receiver,'proof')
assert len(oldstatement.splitlines())==161 and len(oldproof.splitlines())==302
assert sha256(oldproof.encode()).hexdigest()=='5811e05a3a989272b994a5a0196848f4eea96362d2ab8f7abeab492fb59c248a'
blocks={'statement':oldstatement,'proof':oldproof,'following_auxiliary':oldaux}
starts={}
for name,text in blocks.items():
 assert canonical.count(text)==1,name
 starts[name]=canonical.index(text)
assert starts['statement']<starts['proof']<starts['following_auxiliary']
for c in ('label','hypertarget','tag'):
 p=r'\\'+c+r'\{([^{}]+)\}'
 assert sorted(re.findall(p,oldstatement+oldproof+oldaux))==sorted(re.findall(p,receiver))
assert receiver.count('\\begin{proof}')==receiver.count('\\end{proof}')==1

def write_tsv(name,headers,rows):
 p=LANE/(PREFIX+name+'.tsv')
 with p.open('x',newline='') as f:
  w=csv.DictWriter(f,fieldnames=headers,delimiter='\t',lineterminator='\n')
  w.writeheader();w.writerows(rows)
 return p

replacements=[];guards=[]
for name,new in [('statement',newstatement),('proof',newproof),('following_auxiliary','')]:
 old=blocks[name];start=canonical[:starts[name]].count('\n')+1
 end=start+len(old.splitlines())-1
 replacements.append(dict(statement_id=SID,old_text=old,new_text=new))
 guards.append(dict(statement_id=SID,kind=name,start_line=start,end_line=end,
                    old_sha256=sha256(old.encode()).hexdigest(),new_sha256=sha256(new.encode()).hexdigest()))
write_tsv('replacements',['statement_id','old_text','new_text'],replacements)
write_tsv('guards',['statement_id','kind','start_line','end_line','old_sha256','new_sha256'],guards)
items=oldproof.split('\\item ')[1:]
assert len(items)==16
items[-1]=items[-1].split('\\end{enumerate}')[0]
newloc=str((LANE/(PREFIX+'receiving.tex')).relative_to(ROOT))
def old_location(block,text):
 assert text in blocks[block]
 # Restrict every snippet search to its actual released block.
 offset=starts[block]+blocks[block].index(text)
 return 'S6_SERIES_PUBLISH_III.tex:'+str(canonical[:offset].count('\n')+1)
def proof_excerpt(needle,length=180):
 start=newproof.index(needle)
 return newproof[start:start+length].rstrip()
rows=[]
def defect(suffix,typ,block,old,new,reason,new_location=None):
 rows.append(dict(change_id='c7-III-02LN-'+suffix,type=typ,statement_id=SID,
  old_location=old_location(block,old),old_page='',new_location=new_location or newloc,
  new_page='pending final typeset page concordance',old_text=old,new_text=new,
  reason=reason,review_status='staged for root comparison; canonical application and final page review pending'))

header=next(x for x in oldstatement.splitlines() if x.startswith('\\StatementRecord'))
defect('machine-header','D10','statement',header,r'\textup{\scriptsize[02LN]}','Remove the machine dependency/check header while preserving the permanent theorem tag and label.')
defect('implementation-path','D09','statement',r'\path{code/III/manifolds_general_initial.py}',
 'The algorithm below applies to every finite input list and all\nintegers $a,b,w_i$, logarithmic orders and affine numerators satisfying\nthe stated conditions.','State the finite integer algorithm in the theorem/proof; archive implementation and execution scope belong to the check records.')
defect('group-presentation-clause','D02','statement','This is a complete finite presentation, not just\nits abelianization.',
 'This is a finite presentation of the fundamental group.','State the group conclusion directly; the inverse maps in the proof establish it.')
defect('marked-monodromy-wording','D08','statement','actual marked monodromies.','marked monodromies.','Use mathematical marking terminology throughout the statement; order, affine power, permutation and gamma numerator definitions remain explicit.')
defect('line-isomorphism','D22','proof',items[0].strip(),proof_excerpt('Multiplication by'),
 'Complete the true line-pullback assertion by the group-law rational function, whole-fibre divisor, height identity and reciprocal line isomorphism. No theorem refutation.')
defect('literal-cusp-periods','D22','proof',items[3].strip(),proof_excerpt('C=\\begin{pmatrix}',220),
 'Give the literal long-to-short matrix, exponential/log inverse, unit-preserving same-fan comparison, full unsaturated kernel and both boundary torsion maps.')
defect('rank-one-section','D22','proof',items[4].strip(),proof_excerpt('l x_1+h x_2',200),
 'Supply primitive Bezout period coordinates, node charts, reciprocal character and endpoint gauges, four primitive specialization images and inverse sections.')
defect('nontransitive-original','D22','proof',items[5].strip(),proof_excerpt('L(x)=',220),
 'Prove arbitrary powered component-orbit and nontransitive zero-Chern fibre maps with primitive rows L,D and the multiplicative Bezout inverse. The original conclusion stands.')
defect('primitive-chern-map','D22','proof',items[6].strip()+ '\n\\item '+items[7].strip(),proof_excerpt('If the component met',310),
 'Complete the same-germ flow/unit/roof comparison and primitive Gysin coefficient maps for nongenerating P components. The true free-group/kernel conclusions retain their full scope.')
defect('fixed-normal-rim','D22','proof',items[8].strip(),proof_excerpt('In the exterior, the return',250),
 'Give the integral rim bound with Bezout-adjugate inverse and the geometric normal winding; retain torsion in the full fibre coinvariant.')
defect('exceptional-inverse','D22','proof',items[12].strip(),proof_excerpt('The action \\(\\gamma',300),
 'Give both generator homomorphisms for the Klein-four semidirect product, all affine power residues, and the full Z3 quotient with arbitrary regular logarithms.')
defect('finite-first-injection','D22','proof',items[13].strip(),proof_excerpt('At least one weight',330),
 'Supply the missing finite-first relative injection argument: a positive nonlog cap forces the constant peripheral coefficient to vanish, so all power-disc boundaries are independent.')
defect('relative-integral-section','D22','proof',items[15].strip(),proof_excerpt('Here is an inverse splitting',400),
 'Give all Cartier component-disc columns and solve Mz=Pz-prime with P injective; closing chains and coefficient readings supply the integral splitting and rank formula.')
defect('proof-spine','D14','proof',r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
 r'\smallskip\noindent\emph{The line and its marked return.}',
 'Organize one proof by geometric line/caps, bar and group maps, algorithm, relative splitting and duality; retain all sixteen original argument-bearing items.')
defect('workflow-and-defensive-proof','D08','proof','The implementation reconstructs \\eqref{maps:eq:D.GI2} directly from\nthe saved cocycles and verifies integrality and product,\nrather than treating a numerical monodromy output as\na topology theorem.',
 proof_excerpt('It follows geometrically',230),
 'Move implementation/check history to the comparison. The receiver also removes repetitive actual/retained/recorded modifiers and defensive alternatives while preserving the mathematical maps and quantified scope.')
defect('poincare-accent','D23','proof','The rigidified Poincare\nbundle',"The Poincar\\'e period map",
 'Restore the mathematical accent consistently, including Poincare-Lefschetz duality; no mathematical change.')
defect('period-index-exclusion','D25','following_auxiliary','Its rank-two cusp has period index $16$, so it is\noutside the scalar iterations of the natural\nindex-one initial catalogue.',proof_excerpt('The scalar iteration map',600),
 'Refute only the index-based reason: the D=16 iterate of the natural OS45 a=1,b=8 I1 datum also has period index16. The exact period-subgroup map fixes support, so the positive I8 example remains outside the natural I1 iterates. All example homology and theorem conclusions stand.')
defect('following-auxiliary-placement','D13','following_auxiliary',oldaux,
 proof_excerpt('\\smallskip\\noindent\\emph{A pair beyond',1000),
 'Move the complete mathematical OS45 example into the proof; move archive counts and exact execution/source scope to the comparison; remove the repeated closing scope exclusions. The separate guard deletes only this released following block.')
defect('archived-check-counts','D09','following_auxiliary','The replay \\path{code/III/manifolds_general_initial_audit.py}\nstores all $284$ normal-closure cases, $912$ local\nrank-one projections, $21$ generator height products\nand elliptic unit lattices, $90$ complete overlaps\nwith \\ref{maps:src:D.2.41}, and $148$ full Smith examples in the\nlarger parameter sector.',
 'All284+912+21 stored constants, all148 full examples and all90 overlaps were independently checked after exposure; the exact source/input/default-marking/failed-run scope is recorded.',
 'Preserve the correct numerical archive claims with their complete check scope outside the receiving mathematics.',
 str((LANE/(PREFIX+'comparison.md')).relative_to(ROOT)))
# Bibliography is staged separately; there is no canonical bibliography mutation.
bib=(ROOT/'S6_SERIES_PUBLISH_references.bib').read_text()
bstart=bib.index('@article{manSS10,');bend=bib.index('\n}',bstart)+2
rows.append(dict(change_id='c7-III-02LN-height-bibliography',type='D18',statement_id=SID,
 old_location='S6_SERIES_PUBLISH_references.bib:'+str(bib[:bstart].count('\n')+1),old_page='',
 new_location=str((LANE/(PREFIX+'staged_bibliography.bib')).relative_to(ROOT)),new_page='bibliography finalization pending',
 old_text=bib[bstart:bend],new_text=(LANE/(PREFIX+'staged_bibliography.bib')).read_text(),
 reason='Preserve manSS10; identify the exact author version and remove workflow verification text from publication fields. The actual page50-52 reading/hash scope stays in source_checks.',
 review_status='staged bibliography only; root integration and final printed-page check pending'))
write_tsv('defects',['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status'],rows)

now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation seven LN'
events=[]
def event(suffix,typ,outcome,source,phase,date=now,group=None):
 events.append(dict(statement_id=SID,date='2026-11-25',who=who,type=typ,outcome=outcome,
  event_id='publish:c7:III:02LN:'+suffix,phase=phase,source_file=source,source_row='1',
  source_event_type=typ,evidence_group=group or 'publish:c7:III:02LN:'+suffix,
  publish_input_file=str((LANE/(PREFIX+'CHECK_EVENTS.tsv')).relative_to(ROOT)),
  publish_input_row=str(len(events)+2),date_utc=date,
  where=str((LANE/(PREFIX+'comparison.md')).relative_to(ROOT))))
event('fresh-complete','targeted proof check',
 'Before original release, derived every claim for arbitrary compatible whole-fibre a,b, multiple zero fibres, all permitted logarithms and integer clutches: literal period/unit maps, noncyclic cusp torsion, all original cap H1/H2 sections, full bar columns, relative Gamma/P inverse, all ranks/groups and the Klein-four exception with exact splitting and Z3 surjection. Disclosed admitted LI/LH/LK inputs; root read the complete1078-line proof.',
 str(fresh.relative_to(ROOT)),'before original exposure','2026-11-25T08:13:52+00:00','publish:c7:III:02LN:fresh')
event('fresh-exact-computations','computation or formal certificate',
 'Two new different-method programs each executed once successfully, complete sources and combined89/68-line outputs read. Exact symbolic21 products/rim inverses, coarse universal normal closures and64 full all-parameter-formula instances including five noncyclic cusps and the exceptional case. Finite executions accompany the universal proof; no failed fresh mathematical run. Frozen note-edit failure is separately retained.',
 'code/S6_SERIES_PUBLISH_c7_ln_integral_gluing_v001.py','before original exposure','2026-11-25T08:13:52+00:00','publish:c7:III:02LN:fresh')
event('primary-height-scope','used and rechecked in this run',
 'Read primary Schutt-Shioda0907.0298v3 author pages50-52 as extracted full text: section projection, height pairing and Section11.8 mixed local correction formula. Exact PDF hash/version/locator and failed web open recorded. No new visual or whole-article credit; canonical bibliography remains unchanged.',
 str((LANE/(PREFIX+'source_checks.md')).relative_to(ROOT)),'after original exposure')
event('archived-record-comparison','computation or formal certificate',
 'Read both whole historical LN sources without running them. New post-exposure checks parsed and verified all284 residue closures,912 projected vanishing records,21 products/unit lattices,654 local kernel lattices,148 full Smith examples and90 complete LI overlap tables. Exact30 historical inputs and default finite-vector rule are attributed; all actual power vectors printed. Constants v001-v003 failures and v004 success plus overlap v001 success retained; all173/93 success-output lines and all tracebacks read. No historical algorithm execution or manual whole-JSON reading claimed.',
 'code/S6_SERIES_PUBLISH_c7_ln_archived_constants_examples_v004.py','after original exposure')
event('period-index-reason','refuted',
 'Refuted only the auxiliary inference that period index16 excludes scalar iterations: the D16 cover of natural OS45 a1,b8 at I1 has index16 via S_D=diag(1,1,1,D). The same base-identity period map preserves positive support, proving the stated a2,b8 positive-I8 example is outside those I1 iterates. The example values and theorem maps:src:D.2.46 remain valid; D25 correction only, no D27 theorem refutation.',
 str((LANE/(PREFIX+'comparison.md')).relative_to(ROOT)),'after original exposure')
event('whole-original-receiving','used and rechecked in this run',
 'Read the entire161-line statement, all302 original proof lines/16 items and full23-line following auxiliary; compare every assertion to the frozen proof and complete archive checks. One1191-line receiver gives all maps/inverses and preserves12 labels,12 targets,11 equation tags. All assembly attempts/outputs retained; root wholly read the1191-line mathematical version and requested one exact grammatical correction. Three separate guards stage statement/proof/auxiliary replacement. Incidental truncated broader rg exposure is disclosed with no inference or whole-reading credit. Canonical/global records, build and printed-page concordance remain root gates.',
 str((LANE/(PREFIX+'comparison.md')).relative_to(ROOT)),'after original exposure')
headers=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
write_tsv('CHECK_EVENTS',headers,events)
assert (ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()==canonical
assert sha256(fresh.read_bytes()).hexdigest()=='5ec1801a4ab89089407ce1c069bdeb64e4ca3f14c5e3c6bdb36996cea8417ce3'
for g in guards:print('GUARD',g['kind'],g['start_line'],g['end_line'],g['old_sha256'],g['new_sha256'])
for r in rows:print('DEFECT',r['change_id'],r['type'],r['old_location'])
for e in events:print('EVENT',e['event_id'],e['type'],e['phase'])
print('COMPLETE',len(guards),'guards',len(rows),'defects',len(events),'events; all permanent identities; no canonical/global/fresh mutation.')
for name in ('receiving.tex','comparison.md','source_checks.md','staged_bibliography.bib','guards.tsv','replacements.tsv','defects.tsv','CHECK_EVENTS.tsv'):
 p=LANE/(PREFIX+name);print('FILE',p.relative_to(ROOT),sha256(p.read_bytes()).hexdigest())
