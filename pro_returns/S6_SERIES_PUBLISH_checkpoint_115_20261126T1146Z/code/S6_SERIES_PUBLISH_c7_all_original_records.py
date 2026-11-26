#!/usr/bin/env python3
"""Write one local L7 or L8 admission packet; never write global files.

The explicit target argument permits the other packet to be completed
without rerunning an already admitted target's writer.
"""
from argparse import ArgumentParser
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import re

parser=ArgumentParser()
parser.add_argument('tag',choices=['02L7','02L8'])
args=parser.parse_args()
tag=args.tag
ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_all_original'
STEM='S6_SERIES_PUBLISH_III_'+tag+'_'
SID='maps:src:D.2.31' if tag=='02L7' else 'maps:src:D.2.32'
SOURCE_ROW=14016 if tag=='02L7' else 14273

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
frozen={
 LANE/'S6_SERIES_PUBLISH_III_02L7_fresh_derivation.md':'d29faf27713be6424413df5b9cd308b0cccf071b43b711c2503042837661e071',
 LANE/'S6_SERIES_PUBLISH_III_02L8_fresh_derivation.md':'83485fa9ce093b60d62db33c9fca1c826d0241520cf379c5da37c1e931dba3e4',
 LANE/'S6_SERIES_PUBLISH_III_all_original_inputs_and_primary_reading.md':'a44682df8db8ea90fd541df1121518a8edab4648c68f8d6e811423eb08231fb4',
 ROOT/'code/S6_SERIES_PUBLISH_c7_all_original.py':'526f9b1857fbc179324868c0a939294c06d2504d3283e3ea309877c73985fb98',
 ROOT/'code/S6_SERIES_PUBLISH_c7_all_original.out':'29e9081cb06caf8e485655e26ea3abe2968d3595e4b78676953cb78d896c5226',
 LANE/'S6_SERIES_PUBLISH_III_all_original_fresh_data.json':'add1915f08f6819d648bcfa0a8dd196b3f368f204787f7bbe4d032346266f586',
 LANE/'S6_SERIES_PUBLISH_III_02L7_fresh_patterns.tsv':'795d966ecc2c493eaf91a32db897861dc0e8b144ca33cc914c2d33c546a7cdf7',
 LANE/'S6_SERIES_PUBLISH_III_02L8_fresh_patterns.tsv':'7d81a8bc8317a8169afdb286c84c6b5de2ed7f5bcf14d648d901aabce029d146',
}
for p,h in frozen.items():assert sha(p)==h,p

def block(s,env):
    begin=r'\begin{'+env+'}'; end=r'\end{'+env+'}'
    assert s.count(begin)==s.count(end)==1
    start=s.index(begin)
    return s[start:s.index(end,start)+len(end)]

old_statement=block((LANE/(STEM+'released_statement.tex')).read_text(),'theorem')
old_proof=block((LANE/(STEM+'released_proof.tex')).read_text(),'proof')
expected={'02L7':'643a6662ff26b9a304c19837302e813046f79102aeef1ec8ea0707678ba950fe',
          '02L8':'904f1c35dcb6db30c62ff3d2b8b7aa2eaa5b2b1397a6f59fe510557c58c44945'}
assert hashlib.sha256(old_proof.encode()).hexdigest()==expected[tag]
assert len(re.findall(r'^\\item',old_proof,re.M))==({'02L7':12,'02L8':9}[tag])
receiver_path=LANE/(STEM+'receiving.tex')
receiver=receiver_path.read_text()
new_statement=block(receiver,'theorem'); new_proof=block(receiver,'proof')
old=old_statement+'\n\n'+old_proof
new=new_statement+'\n\n'+new_proof
assert receiver.rstrip('\n')==new
for kind in ['label','hypertarget','tag']:
    pat=r'\\'+kind+r'\{([^{}]+)\}'
    before=Counter(re.findall(pat,old)); after=Counter(re.findall(pat,new))
    assert before==after,(kind,before,after)
    print(kind,dict(after))
assert len(re.findall(r'\\label\{',new))==({'02L7':6,'02L8':8}[tag])
assert r'\textnormal{\small tag'+tag+r'.}' in new_statement
for token in [r'\StatementRecord',r'\SeriesRef','records/','.json','code/','SHA256','the program',"KY's",'admitted','fresh']:
    assert token not in receiver,token
assert re.findall(r'\\tag\{([^{}]+)\}',new)==(['D.OD'+str(i) for i in range(1,6)] if tag=='02L7' else ['D.OC'+str(i) for i in range(1,8)])
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',new):
    a,e=m.groups()
    if a=='begin':stack.append(e)
    else:assert stack and stack.pop()==e,m.group()
assert not stack
depth=0
for c in re.sub(r'\\[{}]','',new):
    if c=='{':depth+=1
    elif c=='}':
        depth-=1
        assert depth>=0
assert depth==0
for left,right in [(r'\(',r'\)'),(r'\[',r'\]')]:
    # A row-space command such as \\[3pt] is not a display opener.
    assert len(re.findall(r'(?<!\\)'+re.escape(left),new))==len(re.findall(r'(?<!\\)'+re.escape(right),new))
for m in re.finditer(r'\\\[([\s\S]*?)\\\]',new):assert '\n\n' not in m.group(1)

def write(name,fields,rows):
    p=LANE/(STEM+name+'.tsv')
    with p.open('w',newline='') as h:
        w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)
    with p.open(newline='') as h:assert list(csv.DictReader(h,delimiter='\t'))==rows
    return p

reason=('Complete fresh proof accepted before individual original release; every statement clause and original auxiliary compared. '
        'Preserve all permanent identities, supply complete neighbourhood/line/roof/period/cap and global maps with inverses; '
        'remove machine headers and historical execution claims. '+
        ('Repair only the intermediate physical-circle assertion by the proved global fan diffeomorphism preserving component sections; every theorem conclusion stands.' if tag=='02L7' else
         'Every theorem and auxiliary conclusion stands; distinguish the integral wedge preimage kernel from its primitive boundary Wang image and retain the full zero-Euler bridge.'))
guards=[dict(statement_id=SID,old_text=old_statement,new_text=new_statement,reason=reason),
        dict(statement_id=SID,old_text=old_proof,new_text=new_proof,reason=reason)]
guard_path=write('replacements',['statement_id','old_text','new_text','reason'],guards)
replay=old
for g in guards:
    assert replay.count(g['old_text'])==1
    replay=replay.replace(g['old_text'],g['new_text'],1)
assert replay==new
print('guard_replay','two separate complete blocks; exact local replay and TSV roundtrip PASS')

def span(s,a,b):
    start=s.index(a)
    return s[start:s.index(b,start)+len(b)]

def defect(suffix,kind,location,oldtext,newtext,why,identity=None):
    assert oldtext in old,(suffix,'old fragment')
    assert newtext in new,(suffix,'new fragment')
    return dict(change_id='c7-III-'+tag+'-'+suffix,type=kind,statement_id=identity or SID,
                old_location='S6_SERIES_PUBLISH_III.tex; '+location,old_page='',
                new_location=str(receiver_path.relative_to(ROOT)),new_page='',
                old_text=oldtext,new_text=newtext,reason=why,
                review_status='whole comparison submitted to root; admission pending')

defects=[defect('machine-header','D10',SID,
               next(x for x in old_statement.splitlines() if x.startswith(r'\StatementRecord')),
               r'\textnormal{\small tag'+tag+r'.}',
               'Remove the production header while preserving every label, hypertarget and equation tag; print only the small theorem tag.')]

if tag=='02L7':
    defects += [
     defect('complete-catalogue','D09',SID,r'\path{records/manifolds_original_zero_degree.json}.',
            span(new_proof,r'\item \emph{The natural rows and additive choices.}','affine parameter and every positive allowed order within each list.'),
            'Replace the historical table pointer by the complete profile totals, factor-divisor criterion and exact option rule; 228 patterns on 160 rows and 30 positive defects are independently reconstructed.'),
     defect('same-germ-roof-line','D22','14018--14036',
            span(old_proof,'Its underlying line on the rational Kodaira tree is trivial.','not the number of component orbits.'),
            span(new_proof,r'\item \emph{The original neighbourhood, section and line.}',r'pp.~33--34]{manSS10}.'),
            'Supply the original-germ retraction, forward minus-Q sign, local torsion/logarithm isotopy, smooth variable-roof diffeomorphism, angular line frame, reciprocal unit and full collar transport. III/IV use their common-point topology.'),
     defect('primitive-boundary-map','D22','14048--14093',
            span(old_proof,'The two full normal tori are still primitive.','free summand in '+r'\eqref{maps:eq:D.OD5}.'),
            span(new_proof,'For the full boundary marking put',r'\tag{D.OD5}\hypertarget{tag-0216}{}\label{maps:eq:D.OD5}'+'\n'+r'\]'),
            'Give F=qW, the primitive vector W, the full mixed-torus map and integral section, exact fixed basis and both extending normal three-chains; this proves the full kernel and cokernel, including odd stars.'),
     defect('folded-matrices','D09','14063--14075',
            'The exact folded matrices are also\nretained in the certificate.',
            span(new_proof,'The component-intersection description gives the same primitive','\\eqref{maps:eq:D.OD5}.'),
            'Replace the uncredited historical certificate claim by the four displayed integral folds I^t Q_K R_0, their W kernels and nonzero leading minors. The new post-exposure program verifies all 80 additive occurrences.'),
     defect('local-occurrence-count','D09','14118--14124',
            'There are $396$ exact local zero-degree original certificates.',
            'The natural factor-pair enumeration gives 316 such multiplicative\noccurrences and 80 additive occurrences, hence 396 unselected\nzero-Chern original occurrences in total.',
            'New raw enumeration verifies the mathematical occurrence count and the transitivity/primitive-pair claim for all 316 multiplicative positions; no historical execution or certificate count is claimed.'),
     defect('integral-global-maps','D22','14102--14117',
            span(old_proof,'The subgroups in '+r'\eqref{maps:eq:D.OD5}'+' are primitive,','spectral-sequence splitting.'),
            span(new_proof,r'\item \emph{The full integral global calculation.}','the free component defect cannot conceal a torsion extension.'),
            'Give the primitive cap-elimination inverse, complete finite/regular/norm matrix, integral bounding-chain bridge section and dual torsion coordinates, including zero rational Euler number.'),
     defect('physical-fan-step','D25','14139--14146',
            span(old_proof,'The rank-two zero has the same full original short lattice','Thus this is the actual semifree circle action on $X$.'),
            span(new_proof,r'\item \emph{The global comparison of cusp fans.}',r'\item \emph{The angular quotient, its integral homology and spin.}'),
            'The allowed simply connected OS47 default I2-zero row (a,b)=(7,1), with an order-one regular v=gamma, has C=[[2,1],[-7,-3]] and C^-1 delta=(-1,2). The first edge quotient is z to z^2, hence has mu2 isotropy. Replace the false initial physical-circle assertion by the complete global Farey-flip diffeomorphism and inverse, after proving s=0 and choosing balls away from every primitive component section. The theorem and D.OD3 remain proved and unchanged.'),
     defect('direct-smooth-reconstruction','D22','14166--14200',
            span(old_proof,'The equivariant surgery of '+r'\ref{maps:src:D.2.14}'+' now gives','all two-primary data.'),
            span(new_proof,r'\item \emph{Localizing the fixed sphere while fixing every free section.}',r'\eqref{maps:eq:D.OD3} includes the full refined data for even \(M\) as well.'),
            'Give the component-section-preserving quotient localization, global Euler gauge, oriented twist-conjugation map, linking realization and connected-sum neck maps. The post-exposure note checks the original applied surgery/base pair and zero stabilization contribution; the receiver uses a direct unstabilized diffeomorphism without an unverified general cancellation attribution.'),
     defect('primary-locators','D18','14166--14200',
            r'\cite[Theorem A]{manGR25}',
            r'\cite[Theorem B(2), Proposition 5.6, pp.~22--23]{manGR25}',
            'Use the actual product-clutching result at T=I, base S3, fibre S2, together with exact previously read Barden and Ulmer-Urzua/Schuett-Shioda loci. No new primary-PDF or visual reading is claimed.'),
    ]
else:
    defects += [
     defect('complete-catalogue','D09',SID,r'\path{records/manifolds_original_chern.json}.',
            span(new_proof,r'\item \emph{The complete 282-pattern enumeration.}','is used in this comparison.'),
            'Replace the historical file pointer by the complete profile counts and exact site option sets, proving 282 patterns and 54 with nonzero Chern class on all 172 rows.'),
     defect('same-germ-nontrivial-line','D22','14275--14302',
            span(old_proof,'The local Neron logarithm of $Q$','normal-meridian winding.'),
            span(new_proof,r'\item \emph{The nonzero-Chern original neighbourhood and its roof.}','unchanged by this displayed map.'),
            'Retain the primitive nonzero Chern vector and construct the lifted translation flow, residual real logarithm, smooth positive-roof map, forward quotient and inverses on the same original neighbourhood.'),
     defect('old-number-reference','D06','14286--14293',
            'This is the actual relative construction of\nD.2.20:',
            'The neighbourhood retractions in\nTheorem~\\ref{maps:src:D.2.31}, part 3, give',
            'Replace the typed historical construction number by a resolving series reference and the complete maps in the receiving proof.'),
     defect('primitive-fibre-and-forgetful-map','D22','14320--14361',
            span(old_proof,'The logarithm comparison identifies the elliptic projection','ambient free component group.'),
            span(new_proof,'Let \\(R\\) be the integral matrix','with section \\(F\\mapsto e_{12}\\).'),
            'Supply the actual period change R and inverse, primitive coinvariant row, Bezout kernel generator, integral fibre quotient and the forgetful-map proof that its mixed generator maps to zero.'),
     defect('kernel-domain-map','D20','14342--14383',
            'The full boundary kernel consists of both normal tori and\n$\\ker w_i$; its fibre part cannot be omitted.',
            span(new_proof,'The kernel of the area row on the original six-dimensional wedge','the same integral image, including its sign in the global group.'),
            'Distinguish the rank-five preimage ker(w) in wedge²Lambda from its rank-one image in the boundary Wang quotient; give the exact quotient map, inverse generator and integral relation preimages. The kernel and h=b/q are unchanged.',
            'maps:eq:D.OC7'),
     defect('46-occurrences','D09','14362--14383',
            span(old_proof,'The actual $46$ integral $z_i$ vectors give','enumerating them.'),
            'The natural component equations give 46 marked occurrences, with\ncounts 13, 9, 4, 8, 8 and 4 in the displayed type order.',
            'New post-exposure raw enumeration verifies all 46 vectors and gcds, with exact Wang lifts. The receiving proof derives h=b/q uniformly from the least denominator of z and gcd(a,b)=1, without historical execution credit.'),
     defect('global-bridge-inverses','D22','14384--14412',
            span(old_proof,'All local cokernels in '+r'\eqref{maps:eq:D.OC6}','when $r=1$.'),
            span(new_proof,r'\item \emph{The integral global quotient with every original cap.}','This follows by substitution into the integral cap and bridge maps.'),
            'Supply cap-elimination maps and inverses, the complete finite norm shear and torsion columns, full nonabelian peripheral maps, and integral bounding-chain sections of the L+r bridge. This includes zero rational Euler number and arbitrary regular sites.'),
    ]

defect_path=write('defects',['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status'],defects)
timestamp=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; seventh continuation'
group='publish:c7:III:'+tag
evidence=[str(p.relative_to(ROOT)) for p in frozen]
evidence += [str((LANE/(STEM+x)).relative_to(ROOT)) for x in ['released_statement.tex','released_proof.tex','receiving.tex','comparison.md','replacements.tsv','defects.tsv']]
evidence += ['agents/continuation7_iii_all_original/S6_SERIES_PUBLISH_III_all_original_post_exposure.md',
             'agents/continuation7_iii_all_original/S6_SERIES_PUBLISH_III_all_original_auxiliary_data.json',
             'code/S6_SERIES_PUBLISH_c7_all_original_auxiliary.py','code/S6_SERIES_PUBLISH_c7_all_original_auxiliary.out',
             'code/S6_SERIES_PUBLISH_c7_all_original_receivers.py','code/S6_SERIES_PUBLISH_c7_all_original_receivers.out',
             'code/S6_SERIES_PUBLISH_c7_all_original_receiver_edit.py','code/S6_SERIES_PUBLISH_c7_all_original_receiver_edit.out',
             'code/S6_SERIES_PUBLISH_c7_all_original_records.py','code/S6_SERIES_PUBLISH_c7_'+tag.lower()+'_records.out']
common=(' Full primary/input and exposure scopes are recorded. Frozen fresh proof, program, output and data bytes are unchanged. '
        'Historical target algorithms/outputs remain unopened and uncredited. Shared evidence group supplies no extra independent-family count. '
        'No canonical/global mutation, build, full-PDF or rendered-page reading, unit closure or paper-gate credit; root admission pending.')
fresh_outcome=(
 'Complete pre-exposure derivation frozen 2026-11-24T23:41:19.206106+00:00 and fully root-reviewed before release. '
 'Derived same-germ original-cap/line/roof maps, primitive fibre sections and full fixed-sweep kernels; integral exterior on all 172 rows, '
 'every finite/regular order and free twist with norm maps, complete global bridge and dual groups. New raw-fixture program and all 729 output lines read. '+
 ('Reconstructed 228 patterns on 160 rows with 30 positive defects and proved the full b=1 oriented smooth classification, including even M, by actual s=0, global fan maps preserving component sections, quotient Euler/spin and framed reconstruction.' if tag=='02L7' else
  'Proved nonzero-Chern product cap, primitive component complement, exact kernel k and signed pairing -b/q, all 282 patterns on 172 rows with 54 nonzero-Chern patterns, the full L+r bridge and zero-Euler case.')+common)
used_outcome=(
 'After individual release, read the whole original statement and all '+('12' if tag=='02L7' else '9')+' proof items; compared every clause and auxiliary. '
 'Read the complete receiver and focused final corrections. Post-exposure raw program/output verifies 396 zero-Chern occurrences (316 multiplicative plus 80 additive), '
 'all 46 nonzero-Chern area rows/gcds with integral Wang preimages, all folded ranks and initial angular isotropy. '+
 ('The proof-step D25 is recorded separately; theorem clauses D.OD1--D.OD3 remain proved. The applied surgery/base-pair and zero stabilization contribution are checked; receiver uses the explicit unstabilized framed map. '
  'Six label/target pairs and five equation tags survive two separate exact guards.' if tag=='02L7' else
  'All theorem and auxiliary conclusions stand. The rank-five ker(w) preimage and primitive rank-one boundary kernel are related by explicit inverse maps; all seven D.OC identities stand. '
  'Eight label/target pairs and seven equation tags survive two separate exact guards.')+
 ' Exact local replay, balanced structures and TSV roundtrip passed; post-exposure work receives used/rechecked scope only.'+common)
events=[]
def event(suffix,typ,outcome,phase):
    events.append(dict(statement_id=SID,date=timestamp[:10],who=who,type=typ,outcome=outcome,
        event_id=group+':'+suffix,phase=phase,source_file='S6_SERIES_PUBLISH_III.tex',source_row=str(SOURCE_ROW),
        source_event_type=typ,evidence_group=group,publish_input_file=str((LANE/(STEM+'CHECK_EVENTS.tsv')).relative_to(ROOT)),
        publish_input_row=str(len(events)+2),date_utc=timestamp,where='; '.join(evidence)))
event('targeted','targeted proof check',fresh_outcome,'complete pre-exposure derivation, independently reviewed before individual release')
if tag=='02L7':
    event('physical-fan-refuted',"refuted, with the refined statement's id",
          'Refutes only the intermediate claim in the proof of maps:src:D.2.31 that the defining physical scalar circle at the prescribed rank-two cusp is already semifree. '
          'OS47 default, I2 zero, (a,b)=(7,1), kappa=1 gives C=[[2,1],[-7,-3]], C^-1 delta=(-1,2); its e1-edge quotient is z to z^2 and has mu2 isotropy. '
          'An order-one regular v=gamma makes this member simply connected. The refined intermediate assertion retains id maps:src:D.2.31: the completed output has a proved oriented global Farey-flip diffeomorphism, with reverse-word inverse and preservation of every primitive component section, to a delta-edge model carrying the semifree action. '
          'Fresh parts 8--12 prove actual s=0, every null flip and the full oriented reconstruction. Theorem D.OD3 is proved and unchanged; this event is not a theorem refutation. D25 only; no D26/D27.'+common,
          'narrow post-exposure identification of a false intermediate assertion, repaired by the completed pre-exposure global construction')
event('whole-original-used','used and rechecked in this run',used_outcome,'whole original and receiver reread; new post-exposure auxiliary mathematics and computation')
event_path=write('CHECK_EVENTS',['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where'],events)
print('record_timestamp_utc',timestamp)
print('original_items',12 if tag=='02L7' else 9,'receiver_lines',len(receiver.splitlines()),'defects',len(defects),'events',len(events))
for d in defects:print('defect',d['change_id'],d['type'],d['statement_id'],d['reason'])
for e in events:print('event',e['event_id'],e['type'],'group='+e['evidence_group'],e['outcome'])
for p in [receiver_path,LANE/(STEM+'comparison.md'),LANE/'S6_SERIES_PUBLISH_III_all_original_post_exposure.md',guard_path,defect_path,event_path,ROOT/'code/S6_SERIES_PUBLISH_c7_all_original_auxiliary.py',ROOT/'code/S6_SERIES_PUBLISH_c7_all_original_auxiliary.out',Path(__file__)]:
    print('sha256',sha(p),str(p.relative_to(ROOT)))
print('PASS: frozen fresh bytes, exact original hash, all permanent identities, separate guards, local replay, receiver structure, local defect/event proposals. No canonical/global file written.')
