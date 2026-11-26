#!/usr/bin/env python3
"""Prepare the local LC admission records; never write a global file."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import hashlib
import re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_odd_cubic'
STEM='S6_SERIES_PUBLISH_III_02LC_'
SID='maps:src:D.2.36'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

frozen={
 LANE/(STEM+'fresh_derivation.md'):'c0347fd7972a634b7ac60330ea6045271211b9da398ff534fb1e72f12edffcb5',
 LANE/(STEM+'inputs_and_primary_reading.md'):'73708d76946a2942616f1abf6f3b4ef303aa90e40cc045eaf52a72c014606e05',
 ROOT/'code/S6_SERIES_PUBLISH_c7_lc_odd_cubic.py':'9c85b255302e7bbc31fcfd82333173068c04ecdfde27c7746755900908d3f2e6',
 ROOT/'code/S6_SERIES_PUBLISH_c7_lc_odd_cubic.out':'fb1079b5bf2cf00592cdc1959b6d72ca2947fd86149e50989a6815865b3bdf5d',
 LANE/(STEM+'fresh_data.json'):'8503ee12fd4374c45fe42cfa6d2e571a1b7e874b6ff50de7f0ebe129f8a31795',
 LANE/(STEM+'fresh_patterns.tsv'):'ace964a86684da8aed584992c8fdb33f4064921fe87f2a73b32a14290e2b46f3',
}
for p,h in frozen.items(): assert sha(p)==h,p

def block(s,env):
    begin=r'\begin{'+env+'}';end=r'\end{'+env+'}'
    assert s.count(begin)==s.count(end)==1
    start=s.index(begin)
    return s[start:s.index(end,start)+len(end)]

old_statement=block((LANE/(STEM+'released_statement.tex')).read_text(),'theorem')
old_proof=block((LANE/(STEM+'released_proof.tex')).read_text(),'proof')
assert hashlib.sha256(old_proof.encode()).hexdigest()=='813c61ad7dedf7acd3427cd53b5675489e26069f4da23e063c4f28af9cdb51dd'
assert len(re.findall(r'^\\item',old_proof,re.M))==11
canonical=ROOT/'S6_SERIES_PUBLISH_III.tex'
assert sha(canonical)=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
canonical_text=canonical.read_text()
assert canonical_text.count(old_statement)==1
assert canonical_text.count(old_proof)==1
assert canonical_text.count('\n',0,canonical_text.index(old_proof))+1==15562

receiver_path=LANE/(STEM+'receiving.tex')
receiver=receiver_path.read_text()
new_statement=block(receiver,'theorem')
new_proof=block(receiver,'proof')
old=old_statement+'\n\n'+old_proof
new=new_statement+'\n\n'+new_proof
assert receiver.rstrip('\n')==new
assert len(re.findall(r'^\\item',new_proof,re.M))==13
for kind in ['label','hypertarget','tag']:
    pattern=r'\\'+kind+r'\{([^{}]+)\}'
    before=Counter(re.findall(pattern,old));after=Counter(re.findall(pattern,new))
    assert before==after,(kind,before,after)
    print(kind,dict(after))
assert len(re.findall(r'\\label\{',new))==13
assert r'\textnormal{\small tag02LC.}' in new_statement
for token in [r'\StatementRecord',r'\SeriesRef','records/','.json','code/','SHA256','the program','admitted','fresh']:
    assert token not in receiver,token
assert not re.search(r'(?<!\\)\b(qquad|quad)\b',new)
assert not re.search(r'\\\\\s*\n\[',new)
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',new):
    action,env=m.groups()
    if action=='begin':stack.append(env)
    else:assert stack and stack.pop()==env,m.group()
assert not stack
depth=0
for c in re.sub(r'\\[{}]','',new):
    if c=='{':depth+=1
    elif c=='}':
        depth-=1
        assert depth>=0
assert depth==0
for left,right in [(r'\[',r'\]'),(r'\(',r'\)')]:
    assert len(re.findall(r'(?<!\\)'+re.escape(left),new))==len(re.findall(r'(?<!\\)'+re.escape(right),new))
assert new.count('$')%2==0
for m in re.finditer(r'\\\[([\s\S]*?)\\\]',new):assert '\n\n' not in m.group(1)

def write(name,fields,rows):
    p=LANE/(STEM+name+'.tsv')
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)
    with p.open(newline='') as f:assert list(csv.DictReader(f,delimiter='\t'))==rows
    return p

reason=('Complete pre-exposure proof and new computation fully reviewed before individual original release; '
        'all statement clauses and all eleven original proof items, including every auxiliary, compared. '
        'Retain maps:src:D.2.36, all thirteen labels/hypertargets and all twelve equation tags. '
        'Refine the false local assignment rule by P=(b/p-a nu)/2 and w^2=nu^2, with all ten assignments explicit; '
        'retain mu=0 and the two/one oriented type counts. Supply the actual global line, support pullback, '
        'subgroup and marking maps with inverses, full integral invariant maps and exact primary classification scope.')
guards=[dict(statement_id=SID,old_text=old_statement,new_text=new_statement,reason=reason),
        dict(statement_id=SID,old_text=old_proof,new_text=new_proof,reason=reason)]
guard_path=write('replacements',['statement_id','old_text','new_text','reason'],guards)
replay=old
for g in guards:
    assert replay.count(g['old_text'])==1
    replay=replay.replace(g['old_text'],g['new_text'],1)
assert replay==new
print('guard_replay: two separate complete exact blocks; canonical matches, local replay and TSV roundtrip PASS')

def span(s,start,end):
    i=s.index(start)
    return s[i:s.index(end,i)+len(end)]

def defect(suffix,kind,location,oldtext,newtext,why,identity=SID):
    assert oldtext in old,(suffix,'old fragment')
    assert newtext in new,(suffix,'new fragment')
    return dict(change_id='c7-III-02LC-'+suffix,type=kind,statement_id=identity,
        old_location='S6_SERIES_PUBLISH_III.tex; '+location,old_page='',
        new_location=str(receiver_path.relative_to(ROOT)),new_page='',
        old_text=oldtext,new_text=newtext,reason=why,
        review_status='whole comparison submitted to root; admission pending')

defects=[
 defect('machine-header','D10',SID,
        next(x for x in old_statement.splitlines() if x.startswith(r'\StatementRecord')),
        r'\textnormal{\small tag02LC.}',
        'Remove the machine status/dependency header and print the small theorem tag; all permanent identities are preserved.'),
 defect('local-assignment','D27',SID,
        span(old_statement,r'Then $\mathfrak p=0$',r'value is $1$.'),
        span(new_statement,r' P_X=\frac{Q_f}{2}',r'w^2=\nu^2.'),
        'Refined statement retains maps:src:D.2.36 and D.OP1. Prescribed-fan normal weights are +/-nu at the cusp and +/-w at I_p. '
        'The exact integral invariant is mathfrak p=((b/p-a nu)/2)s, zero exactly when w^2=nu^2. '
        'Pattern 21 (OS56,2,5,I3 zero,e=1) has w=2 but actual refined class zero from p1 pairing -50=0 mod5. '
        'Pattern 30 (OS56/III,1,10,I3 zero,m=4,e=1,n=3,r0=0) has w=4 but actual refined class 2s from pairing -22=3 mod 5. '
        'A unit automorphism cannot exchange zero and nonzero. Exactly ten assignments change; type counts two and one stand.'),
 defect('physical-wall','D25','original proof item4; D.OP5--D.OP6',
        span(old_proof,'The wall expression, using the two',r'\label{maps:eq:D.OP6}'),
        span(new_proof,r' &\psi_{\rm ph}(C_0e_1)',r'\label{maps:eq:D.OP6}'),
        'The old polynomial identity is algebraically correct, but the four untransformed physical vertices are not the prescribed short-fan wall in general. '
        'The explicit C0 map and inverse give psi_ph(C0 t)=-t^tKt+a(nu t1-br t2); its actual wall is -2a(nu+br) and complex line degree +2a(nu+br). '
        'All physical support differences and unit factors are retained; D.OP6 is refined under the same identity.',
        'maps:eq:D.OP6'),
 defect('normal-weight-normalization','D25','original proof items9--10; D.OP9--D.OP10',
        'The two complex normal weights\nat $C$ are $1,-1$, and those at $E$ are $w,-w$.',
        span(new_proof,'The subgroup automorphism',r'and $(w/\nu,-w/\nu)$ at $E$.'),
        'The physical cusp chart has weights +/-nu. The subgroup map exponent nu^-1, with inverse nu, changes both local pairs to +/-1 and +/-w/nu. '
        'D.OP9 and D.OP10 retain their identities with the corrected denominators; the original u[C]=1 normalization has pairing -2(1-w^2/nu^2).'),
 defect('global-line-isomorphism','D22','original proof items3 and6; D.OP4',
        span(old_proof,'Comparison with the flat real',r'zero values on every swept cycle.'),
        span(new_proof,'Here is also a holomorphic description',r'the explicit gauges supply the overlap isomorphisms.'),
        'Give the complete Gaussian gauge, its reciprocal, and z^a with inverse z^-a. They recover the literal original h,F,J maps, every inverse and all unit functions. '
        'Their scalar-invariant overlap composites identify the single global real line exactly, including swept cycles and scalar lift; no fibrewise-only comparison is used.'),
 defect('rank-one-extension','D22','original proof item5; D.OP5a',
        span(old_proof,'The elliptic combination',r'retain their actual boundary marking.'),
        span(new_proof,r'\item \emph{Nodal extension, including nonprimitive first periods.}',r'\deg(\mathcal L|_E)=-2Q_f.'),
        'Supply primitive short and long matrices and their inverses, original-germ/unit/collar transport, full nonsymmetric pairing Gaussian gauge, and rank-one support differences for alpha>1 and beta=0. '
        'All 96 occurrences and the 24 nonprimitive-H occurrences are verified after exposure. The original support identity and I_p primitive-period conclusion stand.'),
 defect('global-borel-shift','D22','original proof item8; D.OP8',
        span(old_proof,'The whole scalar circle fixes that point',r'In particular both restrictions have zero coefficient of $t$.'),
        span(new_proof,'Choose a toric endpoint of $C$ as basepoint.',r'retains the possible mixed term.'),
        'Choose a whole-circle-fixed endpoint, prove the split fundamental group and unique order-p subgroup, and compute the complete degree-two restriction kernel. '
        'A single global t shift with its inverse removes the common character while retaining eta H1(E). This resolves the global comparison at its actual scope.'),
 defect('full-invariant-maps','D22','original proof item10; D.OP10--D.OP11',
        span(old_proof,'Lemma '+r'\ref{maps:src:D.1.10}',r'claimed oriented diffeomorphism classification.'),
        span(new_proof,r'\item \emph{The full integral fundamental-class invariant.}',r'This fixes the factor and the integral torsion class in'+ '\n'+r'\eqref{maps:eq:D.OP1}.'),
        'Keep the full CP3 generator detector and inverse, the marked classifying map, the integral H4 reduction isomorphism, and exact quarter-Pontryagin map. '
        'The final classification uses marked Theorems 3 and 5 with the Section 4.1 uniqueness map and its induced H2 inverse, not homology alone.'),
 defect('historical-computation','D09','original proof items2 and11',
        span(old_proof,'The code checks all $30$ actual marked rows;',r'This proves the final counts.'),
        span(new_proof,'The divisor and component calculation gives the complete table below.',r'factor pairs are bounded and the displayed site options are complete.'),
        'Replace the historical execution/certificate assertion by the explicit factor/component/option enumeration and complete 36-pattern table. '
        'The newly written raw-fixture computation is separately recorded; the historical target program and output remain unopened and uncredited.'),
 defect('primary-locators','D18','original proof item10; classification citation',
        span(old_proof,"Zhubr's Theorem~1",r'claimed oriented diffeomorphism classification.'),
        span(new_proof,'Theorem~5 of '+r'\cite[p.~796]{manZhubr75}',r'both free ranks $H_2,H_3$ vanish in the present application.'),
        'Use complete marked Theorem 3 p.795, Theorem 5 p.796 and the actual Section 4.1 proof p.809, together with the quarter-map and Section 3.13 definition. '
        'The admitted bounded K9 source-description correction is retained; both LC free ranks vanish. No claim that printed p.793 says H3 and no whole-PDF credit is made.'),
]
defect_path=write('defects',['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status'],defects)
timestamp=datetime.now(timezone.utc).isoformat()
group='publish:c7:III:02LC'
who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; seventh continuation'
evidence=[str(p.relative_to(ROOT)) for p in frozen]
evidence += [str((LANE/(STEM+x)).relative_to(ROOT)) for x in ['released_statement.tex','released_proof.tex','receiving.tex','comparison.md','post_exposure_auxiliary.md','replacements.tsv','defects.tsv']]
evidence += ['code/S6_SERIES_PUBLISH_c7_lc_post_exposure.py','code/S6_SERIES_PUBLISH_c7_lc_post_exposure.out',
             'code/S6_SERIES_PUBLISH_c7_lc_receiver_edit.py','code/S6_SERIES_PUBLISH_c7_lc_receiver_edit.out',
             'code/S6_SERIES_PUBLISH_c7_lc_records.py','code/S6_SERIES_PUBLISH_c7_lc_records.out']
common=(' Exact input, primary and exposure scopes are recorded. All six fresh hashes are unchanged. '
        'No historical target execution, extra independent-family count, canonical/global mutation, current-PDF build/reading, unit closure or publication-gate credit. Root admission pending.')
events=[]
def event(suffix,typ,outcome,phase):
    events.append(dict(statement_id=SID,date=timestamp[:10],who=who,type=typ,outcome=outcome,
        event_id=group+':'+suffix,phase=phase,source_file='S6_SERIES_PUBLISH_III.tex',source_row='15562',
        source_event_type=typ,evidence_group=group,publish_input_file=str((LANE/(STEM+'CHECK_EVENTS.tsv')).relative_to(ROOT)),
        publish_input_row=str(len(events)+2),date_utc=timestamp,where='; '.join(evidence)))
event('targeted','targeted proof check',
      'Complete pre-exposure derivation frozen 2026-11-25T02:16:02.099240+00:00 and fully root-reviewed before release. '
      'Reconstructed all 172 natural rows and 36 minimal patterns on 30 rows from the defining fixture, with every finite order and free simply connected twist. '
      'Derived actual original-period maps/inverses, prescribed-fan Cp fixed data, a single global equivariant line and Borel character comparison, full integral mu=0, '
      'PD p1=2(b/p-a nu)s and mathfrak p=((b/p-a nu)/2)s. Proved exact Tate conversion, all generator/action inverses and full oriented classification. '
      'Entire 474-line new program and 690-line output read, including all 36 raw patterns, ten changed assignments and 432 marked diffeomorphism H2 maps/inverses. '
      'The counts remain two order-five types and one order-seven type; every realization is an actual constructed member.'+common,
      'complete fresh derivation and new computation before original exposure')
event('assignment-refuted',"refuted, with the refined statement's id",
      'D27: refutes the local w^2=1 assignment in maps:src:D.2.36; refined statement retains maps:src:D.2.36, D.OP1 and all permanent identities. '
      'The corrected full formula is H2=H3=Z/p, b3=0, spin, mu=0, PD p1=2(b/p-a nu)s, mathfrak p=((b/p-a nu)/2)s '
      'and P=(b/p)/2(1-nu^2/w^2); zero iff w^2=nu^2. '
      'OS56(2,5), I3 zero, e=1 gives w=2 but actual P=0 from pairing -50=0 mod 5; '
      'OS56/III(1,10), I3 zero, m=4,e=1,n=3,r0=0 gives w=4 but actual P=2 from pairing -22=3 mod 5. '
      'Exact unit marking maps cannot interchange zero/nonzero. Ten assignments 21,22,25,26,27,28,29,30,33,34 change; '
      'the zero list is 21,22,25,26,27,28,29,33, with P30=2 and P34=3. The two/one type counts and mu=0 stand. '+common,
      'refuted theorem assignment with complete refined proof under the retained theorem identity')
event('fan-and-action-refuted',"refuted, with the refined statement's id",
      'D25: refutes only the physical-wall identification and inconsistent normal-weight normalization in the proof of maps:src:D.2.36. '
      'Refined intermediate identities retain maps:eq:D.OP5, maps:eq:D.OP6, maps:eq:D.OP9 and maps:eq:D.OP10. '
      'The exact period map C0=[[nu,-br],[ar,rho]], inverse [[rho,br],[-ar,nu]], gives psi_ph(C0 t)=-t^tKt+a(nu t1-br t2); '
      'the actual prescribed wall is -2a(nu+br) and positive complex line degree +2a(nu+br). '
      'The physical cusp weights are +/-nu, while the subgroup map exponent nu^-1 with inverse nu gives cusp +/-1 and elliptic +/-w/nu. '
      'Thus the corrected localization is alpha_C/nu^2+alpha_E/w^2=0; in u_C[C]=1 marking its pairing is -2(1-w^2/nu^2). '
      'True original h,F,J and rank-one support identities are retained through explicit gauges and inverses. '+common,
      'narrow intermediate-assertion refutations identified after whole-original exposure')
event('whole-original-used','used and rechecked in this run',
      'After individual release 2026-11-25T02:30:46.039005+00:00, read the complete statement and all 11 original proof items, every auxiliary, '
      'the complete 13-item receiving proof and final focused edits. New post-exposure mathematics proves the literal Gaussian/z^a comparison to D.OP4, '
      'full support pullback, nonprimitive-period extension, unit/collar compatibility and exact original C-normalized subgroup conversion. '
      'The complete new auxiliary program/output verifies all 96 rank-one occurrences including 24 with nonprimitive H and all 36 generator conversions; '
      'historical computation claims removed. Whole primary scopes and the admitted K9 source correction retained. '
      'All 13 label/hypertarget pairs and 12 equation tags survive two exact canonical-matching guards; local replay, TSV roundtrip and balanced structures pass. '+common,
      'whole original/receiver reading and post-exposure auxiliary derivation and computation')
event_path=write('CHECK_EVENTS',['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where'],events)
print('record_timestamp_utc',timestamp)
print('original_items',11,'receiver_items',13,'receiver_lines',len(receiver.splitlines()),'defects',len(defects),'events',len(events))
for d in defects:print('defect',d['change_id'],d['type'],d['statement_id'],d['reason'])
for e in events:print('event',e['event_id'],e['type'],'group='+e['evidence_group'],e['outcome'])
for p in [receiver_path,LANE/(STEM+'comparison.md'),LANE/(STEM+'post_exposure_auxiliary.md'),guard_path,defect_path,event_path,
          ROOT/'code/S6_SERIES_PUBLISH_c7_lc_post_exposure.py',ROOT/'code/S6_SERIES_PUBLISH_c7_lc_post_exposure.out',
          ROOT/'code/S6_SERIES_PUBLISH_c7_lc_receiver_edit.py',ROOT/'code/S6_SERIES_PUBLISH_c7_lc_receiver_edit.out',Path(__file__)]:
    print('sha256',sha(p),str(p.relative_to(ROOT)))
assert sha(canonical)=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
print('PASS: frozen evidence, exact canonical guards, all permanent identities, local replay, structure and records. No global file written.')
