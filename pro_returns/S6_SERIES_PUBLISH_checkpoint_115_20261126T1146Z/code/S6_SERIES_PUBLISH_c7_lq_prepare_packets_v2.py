#!/usr/bin/env python3
"""Prepare local LQ records with exact guards; mutate no canonical/global file."""
import csv
from datetime import datetime, timezone
from hashlib import sha256
from itertools import islice
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_star_logs_receiving'
FRESH=ROOT/'agents/continuation7_iii_star_logs'
P='S6_SERIES_PUBLISH_III_02LQ_'
ID='maps:src:D.2.49'
CANON=ROOT/'S6_SERIES_PUBLISH_III.tex'
SOURCE_SHA='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
SPANS={'statement':(20164,20294),'proof':(20297,20692),'following_auxiliary':(20694,20710)}
OLD_SHA={
 'statement':'ca8893559a21a03486134e8257d722cc423e9d89c76e489c3d87c5d6964490d9',
 'proof':'e755fa5a2329c11f7ac19c27d931075dd114cbe90470a76598efedf6d8e6400e',
 'following_auxiliary':'b5b8c09831e7c346d72a294cea9045cf74bf837acbea9586431a7be4f57d68bf'}

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

frozen={
 FRESH/(P+'fresh_derivation.md'):'69b2ebce3c94b2c6c178b63699972997c8d8c28d2985a39cc8cfff88f53058d9',
 FRESH/(P+'fresh_scope.md'):'7815dcc77070b72e8dbb4191c2b1bbf005343b168764b5dc35c241820322086c',
 FRESH/(P+'fresh_calculation_note.md'):'62946fe34cdd36ada6c5e0af6c64a228b7232a5f693dcd9fb27a9d171b173278',
 FRESH/(P+'fresh_data_v1.json'):'92cf4fd21ae852c2d286e72a57163bb99702b5ef5db77fe208a577db7a02e87d',
 LANE/(P+'receiving.tex'):'8fb5f9436aad1b1cf09a27734076a598a34e8ac05bb005fc35d1cae72fb06a7e',
 LANE/(P+'post_exposure_derivation.md'):'96d681bbe331735ed9569d0f6c087147dec82938dcdef06e55aaeb0a8b03c459',
 LANE/(P+'basis_transition_readback.md'):'ed7b3f501cce0064259b9c715631e95ce9feca6ddace7b0830e4705742937b7d',
 LANE/(P+'post_exposure_data_v2.json'):'8c5ff277170ed8d63a3064b747b833e2f128724e37199ebde4d930d224ac9d56'}
assert digest(CANON)==SOURCE_SHA
for path,expected in frozen.items():
    assert digest(path)==expected,path

def environment(text,name):
    start=text.index('\\begin{'+name+'}')
    end=text.index('\\end{'+name+'}',start)+len('\\end{'+name+'}')
    return text[start:end]

old={}
for kind,(lo,hi) in SPANS.items():
    text=(LANE/(P+'released_'+kind+'.tex')).read_text()
    old[kind]=(environment(text,'theorem' if kind=='statement' else 'proof')
               if kind!='following_auxiliary' else text.rstrip('\n'))
    with CANON.open() as f:
        bounded=''.join(islice(f,lo-1,hi)).rstrip('\n')
    assert bounded==old[kind]
    assert len(bounded.splitlines())==hi-lo+1
    assert sha256(bounded.encode()).hexdigest()==OLD_SHA[kind]
    print('PASS exact',kind,'guard',lo,hi,OLD_SHA[kind])
for lo,hi in ((20295,20296),(20693,20693),(20711,20712)):
    with CANON.open() as f:
        assert ''.join(islice(f,lo-1,hi))=='\n'*(hi-lo+1)
print('PASS only the five specified intervening lines are blank; next statement remains unopened')
receiver_path=LANE/(P+'receiving.tex')
receiver=receiver_path.read_text()
new={'statement':environment(receiver,'theorem'),'proof':environment(receiver,'proof'),
     'following_auxiliary':''}
assert old['proof'].count(r'\item ')==16
for kind in ('statement','proof'):
    for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}'):
        assert re.findall(pattern,old[kind])==re.findall(pattern,new[kind])
    assert (LANE/(P+'receiving_'+kind+'.tex')).read_text()==new[kind]+'\n'
assert len(re.findall(r'\\label\{',receiver))==25
assert len(re.findall(r'\\hypertarget\{',receiver))==25
assert len(re.findall(r'\\tag\{D\.SL\d+\}',old['statement']+old['proof']))==24
assert r'\tag{' not in receiver
assert not re.search(r'\\(?:label|hypertarget)\{',old['following_auxiliary'])
print('PASS sixteen original items, twenty-four equations and all twenty-five permanent identities')

def write_tsv(name,fields,records):
    path=LANE/(P+name+'.tsv')
    expected={'replacements':'0a74c202a9c566cbc61c82d2157ede48722a306ee0e7d7690b74282059625c9d','defects':'21cbe65331a320b097b4a97c69ff3f3261c28e23ce7064884f6bd1f786dc7aeb','CHECK_EVENTS':'8d96a31eddf972d783f13e9e36ef70c09468ea07e7874b685f8f1577a399070f'}
    assert digest(path)==expected[name],path
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(records)
    with path.open(newline='') as f:
        actual=list(csv.DictReader(f,delimiter='\t'))
    assert actual==[{key:str(row[key]) for key in fields} for row in records]
    assert b'\r' not in path.read_bytes()
    return path

replacements=[dict(statement_id=ID,old_text=old[kind],new_text=new[kind],
    reason=('Complete LQ '+kind+' replacement after all statement clauses, sixteen original proof items and the entire following auxiliary were compared. '
            'Preserve every permanent identity and all theorem conclusions. Correct only the stated complex-orientation assertion through the displayed involution; '
            'give all exact maps and inverse markings in one proof. Move the historical execution apparatus to the full comparison at its actual 95/1638 finite and one local symbolic scope. '
            'This proposal applies no canonical change.')) for kind in SPANS]

def between(text,first,last=None):
    assert text.count(first)==1,(first,text.count(first))
    start=text.index(first)
    return (text[start:] if last is None else text[start:text.index(last,start)]).strip()

def nb(first,last=None):
    return between(receiver,first,last)

def location(text,snippet,base,filename):
    assert snippet and text.count(snippet)==1,(snippet[:100],text.count(snippet))
    start=text.index(snippet)
    lo=base+text[:start].count('\n')
    return f'{filename}:lines {lo}--{lo+snippet.count(chr(10))}'

defects=[]
def defect(slug,kind,part,before,after,reason):
    defects.append(dict(
      change_id=f'III-c7-02LQ-{len(defects)+1:02d}-{slug}',type=kind,statement_id=ID,
      old_location=location(old[part],before,SPANS[part][0],'S6_SERIES_PUBLISH_III.tex ('+part+' guard)'),
      old_page='not asserted; exact released source interval',
      new_location=location(receiver,after,1,str(receiver_path.relative_to(ROOT))),
      new_page='pending final III PDF build and page review',
      old_text=before,new_text=after,reason=reason,
      review_status='local whole comparison complete; root admission and final page review pending'))

s,p,a=old['statement'],old['proof'],old['following_auxiliary']
defect('machine-header','D10','statement','\n'.join(s.splitlines()[:2]),
       '\n'.join(new['statement'].splitlines()[:2]),
       'Replace the machine uses/status header by the mathematical heading and small printed tag; preserve label and hypertarget.')
defect('machine-proof-enumeration','D10','proof',
       r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
       r'\emph{The twelve marked boundaries.}',
       'Use coherent mathematical proof paragraphs in one proof. All sixteen original items and their auxiliaries remain accounted for.')
tags={1:'0247',2:'024I',3:'024O',4:'024P',5:'024Q',6:'024R',7:'024S',8:'024T',9:'024U',
      10:'0248',11:'0249',12:'024A',13:'024B',14:'024C',15:'024D',16:'024E',17:'024F',
      18:'024G',19:'024H',20:'024J',21:'024K',22:'024L',23:'024M',24:'024N'}
for n,tag in tags.items():
    tail=r'\hypertarget{tag-'+tag+r'}{}\label{maps:eq:D.SL'+str(n)+'}'
    defect('sl'+str(n)+'-number','D19','statement' if n<=9 else 'proof',
           r'\tag{D.SL'+str(n)+'}'+tail,r'\begin{equation}'+tail,
           'Replace the inherited manual SL number by automatic section equation numbering; preserve the exact permanent label and hypertarget. '
           'The separate D25/D20 rows give the hatted orientation transport for SL15, SL16 and SL20.')
defect('basis-certificate-wording','D08','statement',
       between(s,'There are twelve actual marked star positions','Take a root'),
       nb('There are twelve marked star positions','Take a root'),
       'Give the twelve basis formulas and their inverses in the mathematical proof; replace file/certificate workflow terminology without changing the displayed-basis scope.')
defect('peripheral-lift-wording','D08','statement',
       'retained in the peripheral marking.','part of the peripheral marking.',
       'State that the integer lift is part of the mathematical marking.')
defect('root-unit-wording','D08','statement',
       between(s,'Every $j,r$','Put\n\\['),
       nb('Every $j,r$','Put\n\\['),
       'Describe the free root maps, units and integer twists as mathematical data.')
defect('normal-origin-marking','D20','statement',
       'Let $D,L$ be its literal fixed-normal tori in the\n$\\delta,\\ell$ directions.',
       'Let $D,L$ be the fixed normal tori defined by the marked origin\nsection in the $\\delta,\\ell$ directions.',
       'Specify the origin-section convention used by the full Wang section and its inverse; the geometric tori are unchanged.')
defect('positive-kernel-wording','D02','statement',
       between(s,'These are unsaturated marked kernels','These columns'),
       nb('These equations specify integral sublattices','These columns'),
       'State the exact integral sublattices, indices, full free cokernel and both nonzero torsion coordinates positively; remove the defensive rank/determinant comparison.')
defect('bar-presentation-wording','D08','statement',
       between(s,'These columns can be inserted','There is also a closed'),
       nb('These columns enter','There is also a closed'),
       'Use the integral bar presentation and marked representatives; retain every other cap/finite Thom column at its proved scope.')
defect('homology-scope-disclaimer','D11','statement',
       'These are nonminimal star-log outputs, and no smooth\nclassification is inferred from their homology.',
       nb('Cyclic summands of order one','\\end{theorem}'),
       'The statement gives homology and a fundamental-group specialization. Remove the repeated disclaimer without adding any smooth-classification conclusion.')
defect('affine-heading','D08','proof',r'\emph{The actual unbounded affine actions.}',
       r'\emph{Flat sections and the holomorphic root.}',
       'Use the mathematical subject of the complete period/root construction as the proof heading.')
defect('missing-parity-heading','D01','proof',r'\emph{The regular-fibre map and its missing parity.}',
       r'\emph{The fibre and the complete torsion marking.}',
       'Remove wording about a missing earlier parity calculation; prove the complete marked torsion map.')
defect('unit-collar-reason','D22','proof',
       between(p,'The usual root-and-unit isotopy','\\item \\emph{The normalization'),
       nb('The period units give the same marked smooth diagrams','\\emph{Normalization, conductor'),
       'Supply the explicit logarithmic unit maps, inverse collars, invariant flow, proper tube and normalized-gradient retraction needed by the original short isotopy assertion.')
defect('independent-wang-placement','D12','proof',
       between(p,'As an\nindependent calculation','\\item \\emph{The regular-fibre'),
       nb('Consequently \\eqref{maps:eq:D.SL12}','The free-cover path lifting'),
       'Retain one normalization proof in the receiver. The entire independent Wang calculation, cut/sheet inverse and coordinate transport are proved in post-exposure note section 2 and compared in item 7.')
defect('complex-orientation-sign','D25','proof',
       'The regular torus $\\alpha\\beta$\nspecializes to the sum of the $q$ complex\ncomponent spheres, each with degree one.',
       nb('In the displayed holomorphic chart','For the second equation'),
       'The ordered angular/outward-radial torus has negative complex orientation for beta=-q log(s)/(2pi i)+unit. '
       'Correct this intermediate assertion only. The explicit hatted conductor involution and inverse preserve all theorem conclusions and the numerical SL15/SL16/SL20 formulas; refined receiver id maps:src:D.2.49.')
defect('ruling-coordinate-convention','D20','proof',
       between(p,'Choose a section $\\sigma$','\\item Every conductor flag'),
       nb('We distinguish the geometric complex-oriented classes','In these coordinates'),
       'Keep the complex geometric F and section square separate from Fhat=-F and fixed sigmahat=S-sigma. '
       'The involution fixes every double curve, carries each relation by its stated integral chain map, and is its own inverse.')
defect('nonabelian-group-notation','D20','proof',
       between(p,'\\begin{gathered}\n \\Gamma=','Additive notation'),
       nb('\\begin{equation}\\hypertarget{tag-024C}', 'The inverse writes'),
       'Write the cap relation multiplicatively before abelianization, with its exact lift/inverse words; preserve the same group and permanent identity.')
defect('torsion-cokernel-wording','D02','proof',
       between(p,'Both order-two terms are forced','\\item \\emph{The literal'),
       nb('Killing the two fibre images','\\emph{Normal discs'),
       'Give the cyclic quotient and inverse tau-to-kD0 coordinate directly, instead of contrasting it with an omitted torsion term.')
defect('normal-lift-convention','D20','proof',
       between(p,'Here the first symbol denotes','\\item \\emph{The closed'),
       nb('Its inverse adds $hnw$','The independent free coordinate'),
       'Distinguish the old normal torus from the old endpoint class. Show D0=D0old+h tau, the old-frame L correction and both inverse substitutions for every integer lift.')
defect('primitive-cokernel-lifts','D22','proof',
       between(p,'The cokernel of the full boundary map','The projected-kernel indices'),
       nb('The full boundary image has primitive complement','In the integral bar splitting'),
       'Supply explicit Bezout lifts of the conductor and torsion generators and the inverse quotient maps; the duality injection gives the same free cokernel.')
defect('duality-typography','D23','proof','Poincare--Lefschetz',
       'Equivalently it injects into\n$H_2(U,\\partial U)=H^4(U)=\\mathbb Z^\\rho$.',
       'Replace the unaccented duality-name shorthand by the exact integral duality isomorphism used.')
defect('global-inverse-quotients','D22','proof',
       between(p,'Set $u=b-4ec$','\\item The one-log'),
       nb('Set $u=b-4ec$','For the fundamental group'),
       'Give each unbounded two-generator relation basis, explicit residue quotient and inverse representative, including |s|=1 and f=0 two-torsion.')
defect('seifert-vanishing-words','D22','proof',
       'The one-log Seifert presentation gives\n$\\pi_1=\\mathbb Z/|s|$.',
       nb('For the fundamental group','Every boundary $H_1$'),
       'Derive the actual vanishing-word quotient and gamma inverse, including the OS46/II index-three lattice and its coprime star-disc relation.')
defect('integral-mv-bridge','D22','proof',
       between(p,'The free local\nboundary defect','Thus $b_2='),
       nb('Every boundary $H_1$','The sole-log clause'),
       'Use torsion-free boundary H1, equal source/target ranks and finite cokernel to prove the entire integral degree-one MV kernel vanishes.')
defect('following-program-scope','D09','following_auxiliary',
       between(a,'The exact script','Root actions'),
       nb('Set $u=b-4ec$','For the fundamental group'),
       'Move the program apparatus to the check comparison. Actual pinned replay is byte-identical, but source scope is 95 finite local, 1638 finite global and one local symbolic expansion; '
       'no generic symbolic global Smith or separate executed bar proof is claimed. The receiver supplies the full unbounded quotient/inverse proof.')
defect('following-repeated-scope','D11','following_auxiliary',
       between(a,'Root actions'),
       nb('Let a marked zero-free star boundary','There are twelve marked'),
       'State the integral star-block scope in the theorem, with primitive N and the unweighted construction following there; delete the repeated following exclusion paragraph.')

assert sum(row['type']=='D19' for row in defects)==24
assert sum(row['type']=='D25' for row in defects)==1
assert not any(row['type'] in ('D26','D27') for row in defects)
write_tsv('replacements',['statement_id','old_text','new_text','reason'],replacements)
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
write_tsv('defects',fields,defects)
print('PASS',len(defects),'narrow defect rows, including 24 D19, one D25 and its explicit D20 transport')
for row in defects:
    print('DEFECT',row['type'],row['change_id'],row['old_location'],'->',row['new_location'])

fresh_where=[str((FRESH/(P+suffix)).relative_to(ROOT)) for suffix in
 ('fresh_derivation.md','fresh_scope.md','fresh_calculation_note.md','fresh_data_v1.json','failed_patch_supplement.md',
  'failed_prose_patch_01.patch','failed_prose_patch_01_diagnostic.txt','failed_prose_patch_02.patch','failed_prose_patch_02_diagnostic.txt')]
fresh_where += ['agents/continuation7_iii_lq_statement/S6_SERIES_PUBLISH_III_02LQ_statement_only.tex',
                'agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02LQ_root_fresh_review.md']
for stem in ('fresh_v1','saved_audit_v1','toric_units_v1'):
    fresh_where += ['code/S6_SERIES_PUBLISH_c7_lq_'+stem+ext for ext in ('.py','.out','.err')]
post_where=[str((LANE/(P+suffix)).relative_to(ROOT)) for suffix in
 ('released_statement.tex','released_proof.tex','released_following_auxiliary.tex','receiving.tex',
  'receiving_statement.tex','receiving_proof.tex','receiving_proof_part.tex','post_exposure_derivation.md',
  'comparison.md','basis_transition_readback.md','post_exposure_data_v2.json',
  'historical_manifolds_star_log_caps.py','historical_manifolds_star_log_caps.json',
  'historical_manifolds_sphere_monodromies.json','historical_replay_v1.generated.json',
  'replacements.tsv','defects.tsv')]
for name in ('PAIRS','decomp','ikernel','wedge','biv','bezout','integer_solution','group'):
    post_where.append(str((LANE/(P+'historical_helper_'+name+'.py')).relative_to(ROOT)))
for stem in ('historical_cache_v1','historical_cache_v2','historical_replay_v1',
             'post_exposure_v1','post_exposure_v2','basis_readback_v1',
             'assemble_receiver_v1','assemble_receiver_v2','assemble_receiver_v3'):
    post_where += ['code/S6_SERIES_PUBLISH_c7_lq_'+stem+ext for ext in ('.py','.out','.err')]
post_where += ['code/S6_SERIES_PUBLISH_c7_lq_historical_main_v1'+ext for ext in ('.out','.err')]
for stem in ('historical_fetch_v1','historical_fetch_followups_v1','historical_fetch_blob_v1'):
    post_where += ['code/S6_SERIES_PUBLISH_c7_lq_'+stem+ext for ext in ('.js','.tool_result.json')]
assert all((ROOT/path).exists() for path in fresh_where+post_where)
now=datetime.now(timezone.utc).isoformat()
common=dict(statement_id=ID,date='2026-11-25',
 who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed',
 source_file='S6_SERIES_PUBLISH_III.tex',source_row=20164,
 evidence_group='publish:c7:III:02LQ:check-sequence',
 publish_input_file=str((LANE/(P+'comparison.md')).relative_to(ROOT)),publish_input_row=1,date_utc=now)
events=[
 dict(common,type='targeted proof check',event_id='publish:c7:III:02LQ:fresh-complete-derivation',
 phase='before whole original LQ exposure',source_event_type='targeted proof check',where='; '.join(fresh_where),
 outcome=('Complete 736-line statement-only proof frozen 2026-11-25T08:47:03.397764 UTC before individual release 08:54:58.364200 UTC. '
 'Derived all positive k, n=1 or 3, every integer j,r and N coprime to 2k through actual unit-bearing toric root maps/inverses, '
 'every-power freeness, normalization/conductor integral maps, boundary H1 section, central-group torsion marking, '
 'full nonsaturated H2 kernels and free cokernel, all integer component lifts, global bar insertion and unbounded sole-log groups. '
 'All 534 new source lines, 44 actual stdout lines and three empty stderr streams read. Independent raw arithmetic has 12 bases, 80 complexes, '
 '1260 local inverse cases, 11340 global cases and 1500 ordered-word/H1 evaluations; all saved fresh matrices were computationally validated. '
 'Large JSON matrices were not all manually read. Generic Euclidean-helper reuse, admitted inputs and the bounded abstract peer check are disclosed; '
 'the named pending LN formula was derived locally and not used unproved. Both failed prose patches and actual visible diagnostics are retained separately. '
 'No original/historical target exposure occurred before this freeze. Post-exposure orientation transport, original comparison and historical replay are excluded.')),
 dict(common,type="refuted, with the refined statement's id",event_id='publish:c7:III:02LQ:complex-orientation-refinement',
 phase='after whole original LQ exposure',source_event_type="refuted, with the refined statement's id",where='; '.join(post_where),
 outcome=('Refuted only original proof item 8 at canonical 20465-20467: its ordered alpha-beta torus was asserted to specialize to the positive sum of complex-oriented component spheres. '
 'The beta=-q log(s)/(2pi i)+unit period has angular then outward-radial orientation, hence negative complex orientation. '
 'Refined receiver id maps:src:D.2.49 preserves every theorem conclusion and the permanent SL15/SL16/SL20 identities through Fhat=-F and fixed sigmahat=S-sigma, '
 'with S and all double curves fixed. The integral conductor map is an involution with its explicit chain inverse and intertwines all boundary images. '
 'A narrow D25 and D20 record this geometric sign and coordinate transport. No whole-theorem refutation, parameter refinement or additional blind credit.')),
 dict(common,type='used and rechecked in this run',event_id='publish:c7:III:02LQ:whole-original-comparison',
 phase='after whole original LQ exposure',source_event_type='used and rechecked in this run',where='; '.join(fresh_where+post_where),
 outcome=('Read and compared the entire 131-line statement, 396-line proof with 16 items, 24 formulas and 17 following auxiliary lines. '
 'Settled both norm conventions, actual flat-to-holomorphic conjugacy, every half-edge count, independent Wang alternative, exact hatted orientation chain transport, '
 'endpoint loops, quadratic bar correction, cyclic vertical cokernel, full normal maps, all integer j lifts and every global quotient/inverse. '
 'The 725-line one-theorem/one-proof receiver preserves 25 identities and theorem conclusions; the narrow geometric refutation is separately typed. '
 'Pinned 210-line historical main and seven exact helpers plus PAIRS were fully read and executed with exact input; other helper bodies were cached/parsed only. '
 'The 12/95/1638 historical JSON was reproduced byte for byte; eight wrapper and five main stdout lines plus actual empty stderr were read. '
 'The code performs 95 finite local and 1638 finite global comparisons and one local symbolic expansion; no generic symbolic global Smith or separately executed bar proof is claimed. '
 'New validator source v1 and full v2 diff, 14 + 18 stdout and the 8-line v1 traceback were read; v2 proves exact quotient/bounding-column comparisons,'
 'both kernel inverses and all saved global matrices. Its 12 basis-transition pairs were also manually read; larger arrays retain computational-audit scope. '
 'All fetch sources and decoded responses, cache/replay sources/streams, assembly versions and caught delimiter repair remain; no connector stderr is invented. '
 'Three exact guards, narrowly typed defects and three events are proposed without canonical application, admission, unit closure, PDF build or page-review credit.'))]
event_fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type',
              'evidence_group','publish_input_file','publish_input_row','date_utc','where']
write_tsv('CHECK_EVENTS',event_fields,events)
assert len({row['evidence_group'] for row in events})==1
assert digest(CANON)==SOURCE_SHA
for path,expected in frozen.items():
    assert digest(path)==expected,path
print('PASS three distinct scoped events in one evidence group; no extra independent-blind credit')
print('PASS canonical/global files and all frozen fresh evidence unchanged')
for suffix in ('receiving.tex','post_exposure_derivation.md','comparison.md','basis_transition_readback.md',
               'replacements.tsv','defects.tsv','CHECK_EVENTS.tsv'):
    print('FINAL_SHA256',P+suffix,digest(LANE/(P+suffix)))
print('PACKET_PREPARED_UTC',now)
