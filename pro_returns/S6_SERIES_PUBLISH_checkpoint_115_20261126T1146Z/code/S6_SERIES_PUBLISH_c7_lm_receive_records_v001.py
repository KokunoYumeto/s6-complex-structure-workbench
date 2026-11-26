#!/usr/bin/env python3
"""Prepare local LM exact guards, defects and scoped events; no global writes."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
from hashlib import sha256
import csv,re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_residual_twenty_receiving'
FRESH=ROOT/'agents/continuation7_iii_residual_twenty_root'
STEM='S6_SERIES_PUBLISH_III_02LM_'
SID='maps:src:D.2.45'
def digest(p):return sha256(p.read_bytes()).hexdigest()
frozen={
 FRESH/(STEM+'fresh_derivation.md'):'270796a05fe92ac57c84d8b46497e252265eb62da270047e6b98e63877b605f1',
 FRESH/(STEM+'fresh_geometry_v003.json'):'f8f2f4ddde0a3335642367eace855003084a8014a358fad340bbea7b4e1a8936',
 ROOT/'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json':'6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522',
}
for p,h in frozen.items():assert digest(p)==h,(p,digest(p))
def block(s,env):
    start=r'\begin{'+env+'}';end=r'\end{'+env+'}'
    assert s.count(start)==s.count(end)==1
    a=s.index(start);return s[a:s.index(end,a)+len(end)]
old_statement=block((FRESH/(STEM+'released_statement.tex')).read_text(),'theorem')
old_proof=block((FRESH/(STEM+'released_proof.tex')).read_text(),'proof')
assert len(old_proof.splitlines())==429
assert sha256(old_proof.encode()).hexdigest()=='20a49e2970aca07f0aad7cad7317b918be6b2bac8898eb2f76d0ef98e18625c0'
canonical=ROOT/'S6_SERIES_PUBLISH_III.tex'
canonical_hash='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
assert digest(canonical)==canonical_hash
# Only the two individually released exact strings are selected/exposed.
source=canonical.read_text()
assert source.count(old_statement)==source.count(old_proof)==1
assert source.count('\n',0,source.index(old_proof))+1==18368
receiver_path=LANE/(STEM+'receiving.tex')
assert digest(receiver_path)=='04e7fd4c3921313739d256192ca482fdf54de78b12fc204ac89e6989d09c66c9'
receiver=receiver_path.read_text()
new_statement=block(receiver,'theorem');new_proof=block(receiver,'proof')
old=old_statement+'\n\n'+old_proof;new=new_statement+'\n\n'+new_proof
assert receiver.rstrip('\n')==new
assert len(receiver.splitlines())==998
for kind in ('label','hypertarget','tag'):
    pattern=r'\\'+kind+r'\{([^{}]+)\}'
    before=Counter(re.findall(pattern,old));after=Counter(re.findall(pattern,new))
    assert before==after,(kind,before,after)
    print('PERMANENT',kind,dict(after),flush=True)
assert len(re.findall(r'\\label\{',new))==23
assert len(re.findall(r'\\tag\{',new))==22
assert r'\textnormal{\small tag02LM.}' in new_statement
for forbidden in (r'\StatementRecord',r'\SeriesRef','code/','records/','.json',
                  'SHA256','the program','fresh','admitted'):
    assert forbidden not in new,forbidden
assert not re.search(r'(?<!\\)\b(?:quad|qquad)\b',new)
assert not any(ord(c)<32 and c not in '\n\t' for c in new)
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',new):
    action,env=m.groups()
    if action=='begin':stack.append(env)
    else:assert stack and stack.pop()==env,m.group()
assert not stack
depth=0
for c in re.sub(r'\\[{}]','',new):
    if c=='{':depth+=1
    elif c=='}':depth-=1;assert depth>=0
assert depth==0
for left,right in ((r'\[',r'\]'),(r'\(',r'\)')):
    assert len(re.findall(r'(?<!\\)'+re.escape(left),new))==len(re.findall(r'(?<!\\)'+re.escape(right),new))
assert new.count('$')%2==0
for m in re.finditer(r'\\\[([\s\S]*?)\\\]',new):assert '\n\n' not in m.group(1)
def write(name,fields,rows):
    p=LANE/(STEM+name+'.tsv');assert not p.exists(),p
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)
    assert b'\r' not in p.read_bytes()
    with p.open(newline='') as f:assert list(csv.DictReader(f,delimiter='\t'))==rows
    return p
reason=('Complete whole-original comparison with the actual prescribed fan and all twenty-two equation identities preserved. '
        'Retain maps:src:D.2.45 and maps:eq:D45.3; refine eight of eleven P/model assignments by actual K and P=-K/2 mod b, '
        'with H2=H3=Z/b, spin, free b3=0 and full mu=0. '
        'Use the original five-copy Tors_2 admissibility bridge after exact primary rechecking, followed by full b20 integer transgression. '
        'Supply all period, fan, line, presentation, Borel, model and coprime inverses; every allowed finite parameter remains included. '
        'Separate exact statement/proof guards; no canonical/global mutation.')
replacements=[dict(statement_id=SID,old_text=old_statement,new_text=new_statement,reason=reason),
              dict(statement_id=SID,old_text=old_proof,new_text=new_proof,reason=reason)]
replacement_path=write('replacements',['statement_id','old_text','new_text','reason'],replacements)
replay=old
for row in replacements:
    assert replay.count(row['old_text'])==1
    replay=replay.replace(row['old_text'],row['new_text'],1)
assert replay==new
print('EXACT_GUARDS separate statement/proof; canonical unique matches; complete identity multisets; replay and TSV roundtrip PASS',flush=True)
def span(s,a,b):
    i=s.index(a);return s[i:s.index(b,i)+len(b)]
def display(s,label):
    i=s.index(r'\label{'+label+'}')
    a=s.rfind(r'\[',0,i);b=s.index(r'\]',i)+2
    assert a>=0;return s[a:b]
def defect(suffix,typ,location,oldtext,newtext,why,identity=SID):
    assert oldtext in old,(suffix,'old')
    assert newtext in new,(suffix,'new')
    return dict(change_id='c7-III-02LM-'+suffix,type=typ,statement_id=identity,
                old_location='S6_SERIES_PUBLISH_III.tex; '+location,old_page='',
                new_location=str(receiver_path.relative_to(ROOT)),new_page='',
                old_text=oldtext,new_text=newtext,reason=why,
                review_status='whole comparison submitted to root; admission pending')
defects=[
 defect('machine-header','D10',SID,
        next(l for l in old_statement.splitlines() if l.startswith(r'\StatementRecord')),
        r'\textnormal{\small tag02LM.}',
        'Remove the machine status/dependency record from mathematical prose and print the small tag; all permanent identities remain.'),
 defect('smooth-types','D27','statement D45.3',
        display(old_statement,'maps:eq:D45.3'),display(new_statement,'maps:eq:D45.3'),
        'The full actual formula is P=-K/2 mod b, lambda=-K mod b, mu=0 with the eleven corrected K values in D45.18. '
        'Eight P/model assignments change: OS45/II(1,8) zero2 O/F gives P4 and Z8,1; '
        'OS55/II(5,4) zero3 O/F gives P0 and Z4,0; '
        'OS55/default(1,20) zeros2,4 and OS55/II(1,20) zero3 O/F give P4 and Z4,0#Z5,1. '
        'Other three assignments remain. The preserved orders of P are respectively2 versus0,0 versus2,5 versus10; '
        'every group automorphism is multiplication by a unit with inverse unit and preserves these orders. '
        'All eleven patterns and all allowed finite parameters stand under retained maps:src:D.2.45, maps:eq:D45.3, tag028V.'),
 defect('critical-fan','D25','proof item6(a); D45.18',
        display(old_proof,'maps:eq:D45.18'),display(new_proof,'maps:eq:D45.18'),
        'The historical cusp routine puts a unit fan in S with long basis LC^-1. '
        'The stipulated fan uses short SC and long L. The exact coordinate map is diag(C,C), inverse diag(C^-1,C^-1), '
        'with character exponent C^t and actual cone map C Sigma. The line map is the actual Gaussian plus reciprocal integral monomial '
        'from phi(Cj)=-psi(j)+L0j. Its positive critical sum has Omega=a-ab kappa-b+ab^2 kappa^2. '
        'All eleven corrected integers and full integral return preimages are supplied. This is a false intermediate geometric input; '
        'the symbolic Smith equations on the old supplied vectors do not identify the actual curves.',
        'maps:eq:D45.18'),
 defect('rational-character','D25','proof item7; b20 C4 fixed characters',
        'The $C_4$ action\nhas only the rational fixed curve and the $I_4$\nelliptic fixed curve, with characters $2,0$.',
        span(new_proof,'For clarity, the cusp characters for the seven rows',
             'Every five-part cusp character is zero.'),
        'For the actual prescribed fan r_C=(b/2)(a kappa(b kappa-1)-1). At b20 the C4 pair is (0,0) '
        'except default zero3, where it is (2,0). A common Borel shift changes both characters together and cannot turn relative0 into relative2. '
        'The corrected whole-coefficient localization polynomial still vanishes, so full mu=0 is retained.'),
 defect('global-line-maps','D22','proof item7; common exterior/line comparison',
        span(old_proof,'The global auxiliary-line comparison and localization',
             r'extends for every parameter in \eqref{maps:eq:D45.2}.'),
        span(new_proof,r'\item \emph{One exterior line with its full finite lift.}',
             r'$u|W=\rho_b c_1(\mathcal A)$ and the finite lift $T_v$.'),
        'Supply the actual angular-disc inverse and omitted-II exterior Z² generator, zero swept values, literal C_b lift, '
        'period Gaussian and integral Cartier/monomial factors with reciprocal inverses and every unit. '
        'The common Borel shift and integrally lifted mixed term are then proved on the full exterior group in the next items.'),
 defect('coprime-inverses','D22','proof item7(a); wedge, bordism and connected sum',
        span(old_proof,'The inclusion\n$K(',r'give all the oriented'+'\n'+r'diffeomorphisms in \eqref{maps:eq:D45.3}.'),
        span(new_proof,'For $b=20$ the connected sum',
             'same marked $P,\\mu$ as $X$.'),
        'The full CW homotopy equivalence stands; supply its cellular inverse q with qi=id and iq homotopic to id relative wedge. '
        'The coefficient CRT inverse is5x4+16x5; bordism inverse is factor inclusions then that map. '
        'The model marking is Phi(e4)=5s,Phi(e5)=4s with inverse x->(x mod4,4x mod5). '
        'The constant-neck spin one-handle gives connected-sum addition. Both refined b20 types are retained.'),
 defect('recognition-locus','D18','proof item7(a); Zhubr recognition',
        "Zhubr's Theorems 3 and 5\n"+r'\cite{manZhubr75} give all the oriented'+'\n'+r'diffeomorphisms in \eqref{maps:eq:D45.3}.',
        span(new_proof,r'Finally, \cite[Theorem~5, p.~796]{manZhubr75}',
             'Their inverses induce the corresponding inverse group maps.'),
        'Use Theorem5 pair injection at p796 and Theorem3/Section4.1 marked zero-free-H3 construction and uniqueness at pp795,809–810. '
        'Both free ranks vanish and the unique spin structure is fixed. The displayed marked models agree in the full P and mu, '
        'so the recognized oriented diffeomorphism and its inverse induce the exact stated marking maps.'),
 defect('execution-prose','D09','proof item8; historical computation assertions',
        span(old_proof,r'\item \emph{Exact computations and their bounds.}',r'\hfill$\square$'),
        span(new_proof,'Every return fixes the single loop',
             'for every integer $m,n,e,r$.'),
        'Replace historical execution prose by the actual polygon, bar-correction, integral return-section and unbounded Thom proof. '
        'All three historical sources and four stored outputs are disclosed after release. '
        'The new verifier checks1056 raw semicharacters,62 physical rows,158 retained pairing records,11 old/new constant R-preimages, '
        'all actual fresh inverses and symbolic parameter maps. It does not execute/import the historical scripts or reconstruct their '
        'unretained full global Smith matrices; that limit is explicit in the auxiliary and comparison notes.'),
]
defect_path=write('defects',
 ['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status'],
 defects)
now=datetime.now(timezone.utc).isoformat()
group='publish:c7:III:02LM'
who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; root fresh work and disclosed post-exposure receiving review'
evidence=[str(p.relative_to(ROOT)) for p in frozen]
for name in ('source_and_computation_scope.md','released_statement.tex','released_proof.tex'):
    evidence.append(str((FRESH/(STEM+name)).relative_to(ROOT)))
for name in ('receiving.tex','comparison.md','post_exposure_auxiliaries.md','post_exposure_data_v001.json','replacements.tsv','defects.tsv'):
    evidence.append(str((LANE/(STEM+name)).relative_to(ROOT)))
for name in ('historical_v001','historical_outputs_v001','aux_v001','textfix_v001','records_v001'):
    evidence.extend('code/S6_SERIES_PUBLISH_c7_lm_receive_'+name+ext for ext in ('.py','.out','.err'))
for name in ('raw_intake_v001','fresh_geometry_v001','geometry_revision_v002','fresh_geometry_v002','geometry_revision_v003','fresh_geometry_v003'):
    evidence.extend('code/S6_SERIES_PUBLISH_c7_lm_'+name+ext for ext in ('.py','.out','.err'))
evidence.extend([
 'agents/continuation7_iii_all_parity/S6_SERIES_PUBLISH_III_02LM_bounded_peer_review.md',
 'agents/continuation7_iii_all_parity/S6_SERIES_PUBLISH_III_02LM_bounded_mu_review.md',
 'agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02LM_fresh_review.md'])
common=(' All events share this evidence group. Frozen fresh bytes are unchanged. '
        'The fresh proof lines318–321 over-invoked the primary sphere criterion at b20; the original five-copy bridge is used and rechecked '
        'after exposure and earns no fresh b20 admissibility credit. No second independent derivation, historical target execution, '
        'full historical Smith reconstruction, whole-PDF/build, unit closure, or canonical/global write is claimed. Root admission pending.')
events=[]
def event(suffix,typ,outcome,phase):
    events.append(dict(statement_id=SID,date=now[:10],who=who,type=typ,outcome=outcome+common,
      event_id=group+':'+suffix,phase=phase,source_file='S6_SERIES_PUBLISH_III.tex',source_row='18368',
      source_event_type=typ,evidence_group=group,
      publish_input_file=str((LANE/(STEM+'CHECK_EVENTS.tsv')).relative_to(ROOT)),
      publish_input_row=str(len(events)+2),date_utc=now,where='; '.join(evidence)))
event('targeted','targeted proof check',
 'Root pre-exposure proof froze2026-11-25T06:02:01Z and was reviewed before individual release. '
 'Its fresh raw geometry establishes7 initial rows/11 patterns, actual periods and integral inverses, primitive angular/exterior sections, '
 'prescribed-fan critical vectors and exact K, all finite integer Thom maps and full-order detector pairing, b4/8 framing, '
 'global actual line and common Borel comparison, full cyclic mu0 and explicit marked surgery models. '
 'All6 source programs and complete streams, including the failed first geometry run and preserved revisions, were read. '
 'This event retains those precise scopes; the full-order b20 sphere attribution is corrected after exposure as separately disclosed.',
 'pre-exposure fresh geometry, arithmetic and bounded framing scope')
event('smooth-identification-refuted',"refuted, with the refined statement's id",
 'D27: refined identity maps:src:D.2.45, result maps:eq:D45.3/tag028V. '
 'Full result H2=H3=Z/b, spin,b3free0,mu0,lambda=-K modb,P=-K/2 modb. '
 'K values by expanded table are24,40,-32,-16,72,80,352,-68,352,352,392. '
 'The eight changed P/model assignments are45/II(1,8)zero2 O/F:P4,Z8,1;55/II(5,4)zero3 O/F:P0,Z4,0; '
 '55/default(1,20)zeros2,4 and55/II(1,20)zero3 O/F:P4,Z4,0#Z5,1. '
 'Other three assignments remain P0,Z8,0 or P14,Z4,1#Z5,1. '
 'Actual original e1 representatives have refined P of order2 versus0,0 versus2,or5 versus10 in the claimed models. '
 'Every marking automorphism and its inverse preserve that order, proving the smooth-identification contradiction. '
 'All eleven patterns, all finite m=6k,r,e,n-me=+-1 and all affine twists are retained.',
 'refuted smooth identification with complete retained-identity refinement')
event('fan-character-refuted',"refuted, with the refined statement's id",
 'D25: narrow intermediate refutation under retained maps:eq:D45.18 and the fixed-character claim. '
 'The exact basis map diag(C,C), inverse diag(C^-1,C^-1), carries the unit fan in SC to C Sigma in S; '
 'the character map is C^t, inverse C^-t, and phi(Cj)=-psi(j)+L0j carries actual Cartier frames and units by reciprocal monomials. '
 'The actual critical sum has Omega=a-ab kappa-b+ab^2 kappa². '
 'The corrected rational character rC=(b/2)(a kappa(b kappa-1)-1) is0 mod4 at b20 except default zero3, where it is2. '
 'The common-character localization polynomial with all mixed terms still gives full mu0.',
 'intermediate actual-fan and character comparison after individual release')
event('whole-original-used','used and rechecked in this run',
 'After release2026-11-25T06:02:47.144873+00:00, the entire statement, all429 original proof lines, eight top-level items and every nested '
 'auxiliary were read. The full998-line one-proof receiver and all corrected passages were read. '
 'Zhubr2013 printed5,6,8,9 were visually inspected: Theorem1 requires a Tors_2 basis, so the original five-copy bridge at b20 is retained '
 'with actual framed tubes, prescribed-spin two-handles and complementary Spin3 extension; the full b20 integer transgression follows. '
 'All3 historical sources were read after retrieval, without execution/import. The new202-line auxiliary output was wholly read: '
 '1056 raw refinement checks,62 physical valuation rows,all158 stored pairing replays,11 old/new constant R-preimages,full actual inverses, '
 'all-parameter core/Thom maps and both CRT markings. '
 'The quotient source maps satisfy BA=I3,AB=I4−sigma(r,n,-m,0)^t(0,1,e,0). '
 'The full coprime CW and spin-bordism inverses, connected-sum markings and exact zero-free-H3 recognition scope are proved. '
 'Separate exact canonical statement/proof guards preserve23 labels/hypertargets and22 tags; structural and TSV replay checks pass.',
 'whole-original use, primary-scope repair, post-exposure arithmetic and full receiving proof')
event_path=write('CHECK_EVENTS',
 ['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type',
  'evidence_group','publish_input_file','publish_input_row','date_utc','where'],events)
print('RECORD_TIMESTAMP_UTC',now,flush=True)
print('COUNTS receiver_lines',len(receiver.splitlines()),'original_proof_lines',len(old_proof.splitlines()),
      'defects',len(defects),'events',len(events),flush=True)
for d in defects:print('DEFECT',d['change_id'],d['type'],d['statement_id'],d['reason'],flush=True)
for e in events:print('EVENT',e['event_id'],e['type'],e['outcome'],flush=True)
paths=[receiver_path,LANE/(STEM+'comparison.md'),LANE/(STEM+'post_exposure_auxiliaries.md'),
       LANE/(STEM+'post_exposure_data_v001.json'),replacement_path,defect_path,event_path,Path(__file__)]
for name in ('historical_v001','historical_outputs_v001','aux_v001','textfix_v001'):
    paths.extend(ROOT/('code/S6_SERIES_PUBLISH_c7_lm_receive_'+name+ext) for ext in ('.py','.out','.err'))
for p in paths:print('SHA256',digest(p),str(p.relative_to(ROOT)),'bytes',p.stat().st_size,flush=True)
for p,h in frozen.items():assert digest(p)==h
assert digest(canonical)==canonical_hash
print('PASS frozen inputs, exact canonical guards, identities, structure, local replacement replay and records. No global mutation.',flush=True)
