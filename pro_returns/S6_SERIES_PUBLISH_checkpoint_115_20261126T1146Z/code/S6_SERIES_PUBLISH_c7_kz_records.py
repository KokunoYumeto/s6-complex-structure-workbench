"""Exact KZ receiving guards and proposed records, before admission only."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from collections import Counter
import csv
import re

ROOT=Path(__file__).resolve().parents[1]
F=ROOT/'agents/continuation7_iii_star_exclusion'
STEM='S6_SERIES_PUBLISH_III_02KZ_'
SID='maps:src:D.2.24'

def block(s,env):
    a,b='\\begin{'+env+'}','\\end{'+env+'}'
    assert s.count(a)==s.count(b)==1
    return s[s.index(a):s.index(b)+len(b)]

fresh=F/(STEM+'fresh_derivation.md')
assert sha256(fresh.read_bytes()).hexdigest()=='5e6c69cf8bcebb9393d2bb42e0926b1a0197abbf156ea47db063ba6e2a6ee6d0'
old_s=block((F/(STEM+'released_statement.tex')).read_text(),'theorem')
old_p=block((F/(STEM+'released_proof.tex')).read_text(),'proof')
assert sha256(old_p.encode()).hexdigest()=='f77eb2008bb98d96891def1dd3f2538480a35b923cc2d149a69b9fd29317bed4'
new=(F/(STEM+'receiving.tex')).read_text()
new_s,new_p=block(new,'theorem'),block(new,'proof')
assert new.rstrip('\n')==new_s+'\n\n'+new_p
for kind in ['label','hypertarget','tag']:
    pattern=r'\\'+kind+r'\{([^{}]+)\}'
    assert Counter(re.findall(pattern,old_s+old_p))==Counter(re.findall(pattern,new))
    print(kind,dict(Counter(re.findall(pattern,new))))
assert not any(s in new for s in ['\\StatementRecord','\\SeriesRef','code/','records/','.json','SHA256'])
stack=[]
for action,env in re.findall(r'\\(begin|end)\{([^{}]+)\}',new):
    if action=='begin':stack.append(env)
    else:assert stack and stack.pop()==env
assert not stack
for p in [fresh,F/(STEM+'receiving.tex'),F/(STEM+'comparison.md'),F/(STEM+'post_exposure_derivation.md')]:
    assert b'\r' not in p.read_bytes()

def write(suffix,fields,rows):
    p=F/(STEM+suffix+'.tsv')
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)
    with p.open(newline='') as f:assert list(csv.DictReader(f,delimiter='\t'))==rows
    return p

reason='Complete fresh proof, full original and auxiliary comparison; preserve all identities and supply actual period, cap, boundary and global quotient maps.'
guards=[dict(statement_id=SID,old_text=o,new_text=n,reason=reason) for o,n in [(old_s,new_s),(old_p,new_p)]]
gp=write('replacements',['statement_id','old_text','new_text','reason'],guards)
replay=old_s+'\n\n'+old_p
for g in guards:
    assert replay.count(g['old_text'])==1
    replay=replay.replace(g['old_text'],g['new_text'],1)
assert replay==new.rstrip('\n')

specs=[
 ('header','D10',next(l for l in old_s.splitlines() if l.startswith('\\StatementRecord')),
  r'\textnormal{\small tag02KZ.}','Remove production header; preserve theorem and equation identities.'),
 ('marked-blocks','D22','The exact matrices also give',
  'Literal multiplication, with $T$ either matrix, gives',
  'Give both literal physical matrices, primitive bases and integer inverses, quotient coordinates and exterior-square dimensions proving D.IS1 and D.IS2.'),
 ('all-star-cap-maps','D22',
  'An original cap has more than one component orbit, so was already',
  'For the original cap with $(a,b)=(4,1)$, the line multidegree is',
  'Write both actual original-cap Chern cases and their full local quotient maps. Give primitive node charts, flat-unit inverses, every deck offset, full boundary image and transfer. The original conclusions stand.'),
 ('refinement-map','D22',
  'Toric refinements can only add component',
  'A toric refinement has a degree-one map $f:(U\',L\')\\to(U,L)$,',
  'Prove relative cokernel persistence by degree-one push-forward and the explicit Poincare--Lefschetz right inverse; no factorization is assumed.'),
 ('single-global-obstruction','D11',
  'The rank budget of \\ref{maps:src:D.2.22} is saturated:',
  'Finally let $E_0$ be the exterior and $U_i$ all the attached caps.',
  'The original strengthened budget and every auxiliary claim were fully verified in the post-exposure note. Use the stronger computed local cokernel and one Mayer--Vietoris injection for the receiving proof; retain the eight-row scope of positive b2.')
]
defects=[]
for name,kind,old,newtext,why in specs:
    assert old in old_s+old_p and newtext in new
    defects.append(dict(change_id='c7-III-02KZ-'+name,type=kind,statement_id=SID,
      old_location='S6_SERIES_PUBLISH_III.tex; maps:src:D.2.24',old_page='',
      new_location=str((F/(STEM+'receiving.tex')).relative_to(ROOT)),new_page='',
      old_text=old,new_text=newtext,reason=why,
      review_status='whole comparison submitted to root; admission pending'))
dp=write('defects',['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status'],defects)
now=datetime.now(timezone.utc).isoformat()
event_id='publish:c7:III:02KZ:targeted'
event=dict(statement_id=SID,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; seventh continuation',
 type='targeted proof check',
 outcome='The theorem and all original auxiliary conclusions stand. Complete fresh proof frozen22:38:28.424937 UTC before individual original release22:42:02.930329 UTC. Full original theorem and all three proof items read, including D.IS1/D.IS2, exact8 rows, all component/transverse actions, b2=rho+1, arbitrary orders/affine lifts, both original Chern cases, refinements and strengthened MV rank budget. Fresh proof gives the complete local cokernel with explicit period bases/inverses, toric charts, bounding sweeps, reflection offsets, transfer, Euler kernel, invariant D7 form and global injection. Every allowed star cap forces positive rational H2 on the eight necessary rows. New fresh and auxiliary programs and all output read;234 offset examples support the independently proved universal formula. Exact original blocks and all3 label/target pairs plus2 equation tags preserved in two separate guards. KX/KY and graph reflection input scopes are attributed; historical KZ programs remain unopened/uncredited. No D25/D26/D27 alleged. One targeted event, no extra independent-family count, canonical application, unit, build, page or paper-gate credit; root admission pending.',
 event_id=event_id,phase='complete fresh proof, individual release, full original and receiver comparison',
 source_file='S6_SERIES_PUBLISH_III.tex',source_row='12406',source_event_type='targeted proof check',evidence_group=event_id,
 publish_input_file=str((F/(STEM+'CHECK_EVENTS.tsv')).relative_to(ROOT)),publish_input_row='2',date_utc=now,
 where='; '.join([str((F/(STEM+s)).relative_to(ROOT)) for s in ['fresh_derivation.md','released_statement.tex','released_proof.tex','post_exposure_derivation.md','comparison.md','receiving.tex','replacements.tsv','defects.tsv']]+['code/S6_SERIES_PUBLISH_c7_kz_star.py','code/S6_SERIES_PUBLISH_c7_kz_star.out','code/S6_SERIES_PUBLISH_c7_kz_auxiliary.py','code/S6_SERIES_PUBLISH_c7_kz_auxiliary.out','code/S6_SERIES_PUBLISH_c7_kz_records.py','code/S6_SERIES_PUBLISH_c7_kz_records.out']))
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
ep=write('CHECK_EVENTS',fields,[event])
print('PASS exact two-block guards; unchanged fresh hash; preserved identities; complete receiver structure and LF.')
print('UTC',now,'defects',len(defects),'targeted_events',1)
for p in [F/(STEM+'receiving.tex'),F/(STEM+'comparison.md'),F/(STEM+'post_exposure_derivation.md'),gp,dp,ep]:
    print('SHA256',sha256(p.read_bytes()).hexdigest(),p.relative_to(ROOT))
