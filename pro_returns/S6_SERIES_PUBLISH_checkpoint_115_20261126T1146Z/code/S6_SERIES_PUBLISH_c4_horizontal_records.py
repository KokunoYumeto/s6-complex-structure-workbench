#!/usr/bin/env python3
"""Write compact, bounded records for the exposed horizontal receiving review."""
from pathlib import Path
import csv
import re
import difflib
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'agents/continuation3_provenance/sec07_tail'
OUT=ROOT/'agents/continuation4_horizontal'
STAMP='2026-11-23T11:19:20+00:00'
WHO='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited reasoning effort not separately exposed; fourth continuation, horizontal review'
csv.field_size_limit(10_000_000)
def rows(p):
    with p.open() as f:return list(csv.DictReader(f,delimiter='\t'))
def write(p,data,fields):
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)

guards=rows(OUT/'S6_SERIES_PUBLISH_horizontal_guards.tsv')
source=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
receiver=source
for g in guards:
    assert receiver.count(g['old_text'])==1,g['change_id']
    receiver=receiver.replace(g['old_text'],g['new_text'],1)

def owner_at(text,at):
    env=list(re.finditer(r'\\begin\{(?:proposition|lemma|theorem|maintheorem|citedresult|definition|remark)\}',text[:at]))
    if not env:return 'source front matter'
    p=env[-1].start()
    m=re.search(r'\\label\{([^}]+)\}',text[p:at+200])
    return m.group(1) if m else 'source statement'

def equation_at(text,label):
    at=text.index(r'\label{'+label+'}')
    start=text.rfind(r'\begin{equation}',0,at)
    end=text.index(r'\end{equation}',at)+len(r'\end{equation}')
    assert start>=0 and '\\end{equation}' not in text[start:at]
    return text[start:end],owner_at(text,at)

def compact_pair(a,b,context=100):
    if max(len(a),len(b))<=1200:return a,b
    lo=0
    while lo<min(len(a),len(b)) and a[lo]==b[lo]:lo+=1
    tail=0
    while tail<min(len(a)-lo,len(b)-lo) and a[-tail-1]==b[-tail-1]:tail+=1
    a_end=len(a)-tail;b_end=len(b)-tail
    left=max(0,lo-context)
    return a[left:min(len(a),a_end+context)],b[left:min(len(b),b_end+context)]

defects=[]
def add(kind,owner,old,new,reason,oldloc=None,newloc=None):
    if not old and not new:return
    defects.append(dict(change_id=f'II-C4-HORIZONTAL-{len(defects)+1:03d}',type=kind,
        statement_id=owner,old_location=oldloc or owner,old_page='checkpoint 44 source; final page concordance pending',
        new_location=newloc or owner,new_page='receiving source; integrated PDF pending',old_text=old,new_text=new,
        reason=reason,review_status='Complete original/receiving proof comparison in this continuation; used and rechecked. Guarded admission and integrated render remain root-owned.'))

# Exact numbered displays, with each final location resolved from the actual receiver.
for r in rows(BASE/'S6_SERIES_PUBLISH_sec07_defects.tsv'):
    if r['type']=='D19':
        m=re.search(r'cdp:eq:[A-Za-z0-9.]+',r['old_location'])
        if not m:m=re.search(r'\\label\{([^}]+)\}',r['old_text']);label=m.group(1)
        else:label=m.group(0)
        new,owner=equation_at(receiver,label)
        add('D19',r['statement_id'],r['old_text'],new,r['reason']+' Final receiving owner: '+owner+'.',r['old_location'],label+' at '+owner)
    elif r['type']=='D06' and r['old_text'] in source and r['new_text'] in receiver:
        add('D06',r['statement_id'],r['old_text'],r['new_text'],r['reason'],r['old_location'],r['new_location'])

# Source comparison summaries are short exact excerpts; full guarded texts are elsewhere.
proof_pairs=[
 ('IRR_1','cdp:st:C.2.IRR.1','D12','The blowup Jacobian is owned by P232 under (Z1,Z2,D1,D2,m,a)=(W,Wprime,DW,sigma_*DW,d,a); every effectivity, exceptional, involution and pinch-map step remains in this proof.'),
 ('RAT_1','cdp:st:C.2.RAT.1','D12','The low-delta embedded ideals and symbolic-square identities use P228 and A5.18 on identical generators; the complete A2 radical-cubic and attachment calculation remains.'),
 ('RAT_3','cdp:st:C.2.RAT.3','D12','One attachment calculation gives K>=r-N0-r_dom, k=K-ell and e(S)>=2-r_dom-ell. The original degree-one conclusion is the same normalization map with ell=0 and r_dom<=2.'),
 ('D4_1','cdp:st:C.2.D4.1','D12','P361 and P362 own the normal-level transport and cyclic-boundary pairing; the connected cubic genus and common-zero exclusions use the same N,P,mS and remain proved here.'),
 ('D4_2','cdp:st:C.2.D4.2','D12','The tautological clause uses only deg N=-2. Reduced and doubled-fibre clauses of P362 are applied after their divisor hypotheses are proved, with exact c,b0,g_B,r_B,epsilon substitutions.'),
 ('UN_7','cdp:st:C.2.UN.7','D12','The rational case is P360 on the identical proper map, mS,eta,pi. The four original conclusions, monodromy formula, proper ruled transfers and contracted-section group proof remain.'),
 ('UN_12','cdp:st:C.2.UN.12','D12','The same proper mS and normalization maps feed UN7, VII1/VII2 and P300. Every ruled row, Hopf conductor alternative and both directions of the zero criterion remain.'),
 ('MH_4','cdp:st:C.2.MH.4','D12','P289 owns the finite-character comparison; the original class-VII Betti cases, parity and equality conclusion remain under the original full compact Betti hypotheses.'),
 ('INT_1','cdp:st:C.2.INT.1','D18','Use the published Brinzanescu-Moraru locator and the exact finite principal-cover/isogeny and Picard restriction maps; the complete interface proof remains.'),
 ('INT_2','cdp:st:C.2.INT.2','D25','Before applying Dloussky Definition2.20/Lemma2.22 and its following paragraph, the multiple canonical-boundary line is identified as complex-flat through CA11. All maximum-ratio and unit-bearing vanishing-sphere calculations remain.'),
 ('INT_3','cdp:st:C.2.INT.3','D18','Proper analytic duality is applied to the same pi and CM surface dualizing complexes; conductor schemes, Picard restrictions, exact exceptional counts and both equality directions remain.'),
]
for name,owner,kind,reason in proof_pairs:
    old=(BASE/f'S6_SERIES_PUBLISH_{name}_original.tex').read_text()
    new=next((g['new_text'] for g in guards if g['change_id']=='II-C4-HORIZONTAL-TAIL'))
    at=new.index(r'\label{'+owner+'}')
    lo=new.rfind(r'\begin{proposition}',0,at)
    oldline=old.splitlines()[0]
    newline=new[lo:new.find('\n',lo)]
    if oldline==newline:
        # Record a changed complete paragraph, not a whole proof copy.
        candidates=[x for x in rows(OUT/'S6_SERIES_PUBLISH_horizontal_local_edits.tsv') if x['owner']==owner and x['type']!='D12' and len(x['old'])<1500]
        if candidates:oldline,newline=compact_pair(candidates[0]['old'],candidates[0]['new'])
        else:oldline=old.split(r'\begin{proof}',1)[1].split('\n\n',2)[-1][:600];newline=new[at:at+600]
    add(kind,owner,oldline,newline,reason)

for name in ['RAT_4','RAT_5','RAT_7','RAT_8','RAT_9','D4_3']:
    old=(BASE/f'S6_SERIES_PUBLISH_{name}_original.tex').read_text()
    header=old.split(r'\end{proposition}',1)[0]
    label=re.search(r'\\label\{([^}]+)\}',header).group(1)
    # The exact original assertion begins after its hidden record.
    paragraphs=[p for p in header.split('\n\n') if not p.startswith('\\') and p.strip()]
    old_assertion='\n\n'.join(paragraphs) or header
    if len(old_assertion)>1600:old_assertion=old_assertion[-1600:]
    p360=guards[0]['new_text']
    lo=p360.index('Let $f:Y\\to B$');hi=p360.index('\n\nFor the effective',lo)
    add('D12',label,old_assertion,p360[lo:hi],
        'The old Euler conclusion is implied by P360 with the exact disc restriction (f,mS,eta,pi)->(f|f^-1(Delta),mS,eta,pi). Fibre-product projections (x,b)->x and inverses x->(x,b) commute with eta and pi and preserve e(S). RAT4’s additional loss calculation is at RAT2; all ordinary-triple root and attachment bounds are at P380, with every old formula target preserved.',name+' complete original assertion','prop:II:rational-torus-fibre-euler; prop:II:cubic-root-attachments or RAT2')

for g in guards[1:9]:
    if 'A516' in g['change_id']:
        old=g['old_text'].split(r'\begin{proof}',1)[0]
        new=g['new_text'].split(r'\begin{proof}',1)[0]
        old='\n'.join(old.splitlines()[2:11]);new='\n'.join(new.splitlines()[2:16])
        add('D25','cdp:st:A.5.16',old,new,'Close the proper-tube application gap: state torsion omega_S and chi(O_S)=0, prove their compact specialization by canonical evaluation and HRR, and recheck every subsequent rational-resolution/conductor step and consumer.')
    else:
        kind='D18' if 'BM-PUBLISHED' in g['change_id'] else 'D09' if 'PROGRAM' in g['change_id'] else 'D12'
        a=g['old_text'].splitlines(keepends=True);b=g['new_text'].splitlines(keepends=True)
        for tag,i,j,k,l in difflib.SequenceMatcher(a=a,b=b,autojunk=False).get_opcodes():
            if tag=='equal':continue
            old=''.join(a[max(0,i-1):min(len(a),j+1)])
            new=''.join(b[max(0,k-1):min(len(b),l+1)])
            add(kind,owner_at(g['new_text'],len(g['new_text'])//2),old,new,
                'Transfer the identical formula to its complete earlier owner, preserving all target labels; bibliography and appendix guards retain the exact source/program scope.',g['change_id'],g['change_id'])

# Final local repairs discovered during this continuation, in bounded exact quotations.
for r in rows(OUT/'S6_SERIES_PUBLISH_horizontal_local_edits.tsv'):
    if r['type']=='D12':continue
    old,new=compact_pair(r['old'],r['new'])
    if max(len(old),len(new))>2400:continue
    add(r['type'],r['owner'],old,new,r['reason'],
        r['owner']+(' in checkpoint-44 source' if old in source else ' in prepared receiving text'),r['owner']+' in final guarded receiver')

for g in guards[9:]:
    if g['change_id'].endswith('FURTHER-RESULTS'):
        add('D12','further-results-II',g['old_text'],g['new_text'],'Replace repeated Euler entries by one P360 entry, list the distinct attachment and cyclic-cover results once, and match their body order.')

add('D20','prop:II:cubic-root-attachments',r'q_3(\lambda,1,z)+y\,A(\lambda,y,z)',
    r'q_3(\lambda,1,z)+y\,\Phi(\lambda,y,z)',
    'The local holomorphic remainder is renamed Phi by the identity Phi=A_local, so A consistently denotes the common coefficient divisor. Coordinates and equation are identical.',
    'RAT5 local expansion','P380, RD3')
add('D20','prop:II:cubic-root-attachments','$(1,d)$ and $(2,3-v-d)$, with $d\\ge0$',
    '$(1,b)$ and $(2,3-v-b)$, with $b\\ge0$',
    'The section bidegree is renamed by b=d_old, preserving its exact degree inequalities; d consistently denotes the conductor-cover degree in the consolidated statement.',
    'RAT9 split-bundle degree bound','P380 common-divisor degree bound')
for heading in re.findall(r'\\subsection\{[^\n]+',guards[0]['new_text']):
    if heading not in guards[0]['old_text']:
        add('D14','sec:II:07','',heading,'Insert the descriptive mathematical subsection at the explicit dependency order in the comparison notes. The stable original unit remains sec:II:07, with no subdivision movement credit.')
rd2,_=equation_at(receiver,'cdp:eq:C.RD.2')
add('D12','lem:II:normal-cubic-compact-core',r'\begin{proposition}[A locally unibranch tangent-root component gives positive Euler number]',
    'Let $R_h\\subset\\PP(N)$ be the horizontal root divisor of $P$.\nFor a connected normalized conductor cover $C\\to H$ of degree\n$d$, let $R_d$ be its generic tangent-root component. There is\na finite-cover isomorphism over $H$:\n'+rd2,
    'Move the complete tangent-ratio field map, common-factor gluing and integral-closure inverse to P361. The proof uses any connected normalized conductor cover; D4.2 therefore applies before knowing the genus of C. P380 uses the same map with its rational section.',
    'RAT5, RD2 field identification','P361, RD2 field identification before D4.2')

fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
write(OUT/'S6_SERIES_PUBLISH_horizontal_defects.tsv',defects,fields)

# Every event below describes a complete exposed original/receiving read, not an independent derivation.
outcomes={
'cdp:st:C.2.IRR.1':'Read both complete proofs. Checked the exact P232 blowdown substitution, reverse effectivity, zero-coefficient exceptional curves, conductor support, A subset A-prime finite-length CM comparison, involution quotient, pinch coordinate map and full-multiplicity exclusion. All elliptic minimality and étale conclusions remain.',
'cdp:st:C.2.RAT.1':'Read both complete proofs. Checked the P228 ring maps and A5.18 symbolic-square transfers, the rank-one determinant poles, explicit dual normal lifts, A2 radical cubic pole bounds 10 and 6+2, conductor-cleared degree and attachment table. Concurrent-line and Hirzebruch bounds remain.',
'cdp:st:C.2.RAT.2':'Read the entire original smooth proof and both parts of the combined receiving proof. The generic d<=1 attachment calculation gives r_dom=0 and ell<=1; smooth Xi=0 gives two branch zeros, A=2, r<=2 and e>=2+N0. The repeated smooth hypotheses are removed.',
'cdp:st:C.2.RAT.3':'Read both complete proofs. The wholly exceptional-tree count, incidence graph with individual normalization branches, K/k/ell maps and zero-edge case prove e>=2-r_dom-ell. The degree-one specialization preserves the original conclusion.',
'cdp:st:C.2.RAT.4':'Read the complete original generic tacnode proof and its combined receiver. Its positive Euler assertion specializes P360 through identical full-fibre and normalization maps; the additional loss calculation remains in RAT2. Checked inverse quadratic-field maps, singular Hessian zeros and the smooth refinement.',
'cdp:st:C.2.RAT.5':'Read the entire original and proposed proof, then the complete P380 receiving proof. The Euler label aliases P360. The exact tangent-ratio field map, integral-closure inverse, X=x-y lambda inverse, conductor (y^2), locally-unibranch zero-loss calculation and A2/A4 cusp normalization maps remain in P380.',
'cdp:st:C.2.RAT.6':'Read the complete cited statement and application proof; its bytes remain unchanged. Verified the cited local delta/genus/link bounds are invoked for the same isolated cubic suspensions. No fresh independent proof or fresh reading of every historical singularity-classification source is claimed.',
'cdp:st:C.2.RAT.7':'Read the complete original, prepared and consolidated P380 proofs. P360 owns the sign. P380 retains delta five, the connected/disjoint boundary graph, rank=2nu+2b1-lambda+epsilon, the preserved compact pairing, nu<=1, and the exact duplicate-attachment loss.',
'cdp:st:C.2.RAT.8':'Read the complete original, prepared and P380 proofs. P360 owns the sign. Kept all intersection-1/2/3 local forms and inverse coordinates, the Newton faces and higher terms, pg/link bounds, nu<=3, nu_F=1+a and ell<=nu-2. Reopened Merle-Teissier Theorem2.1.1 and Corollary2.1.3 at the stated pages.',
'cdp:st:C.2.RAT.9':'Read all complete proofs. P360 owns the sign; P380 retains the common-zero degree bound, the two-simple-zero rank/branch count and every doubled-fibre weighted blowup, character-generator map, quotient-ring normalization and rationality argument. Corrected the finite-algebra locator from the H1 formula to DD6.',
'cdp:st:C.2.D4.1':'Read both complete proofs. The same f,mS,H,N,P enter P361 and P362. Checked the O plus O(-2) spherical obstruction, splitting and bidegree bounds, delta budgets, exact rank substitutions and exclusion of positive genus and primitive connected cubic covers.',
'cdp:st:C.2.D4.2':'Read both complete proofs. Checked the tautological-only application before branch classification, every v=0/1/2 splitting case, global square-completion bundle map, reduced and doubled-fibre character data and contact-resolution substitutions. The irrational ruled elliptic/minimality consequence remains.',
'cdp:st:C.2.D4.3':'Read all complete proofs and the full P380 receiver. P360 owns its Euler assertion. P380 retains v=1, the two-simple-zero P=0/1/2 contact analysis, the exact q and pairing formulas, the attachment losses, and the weighted double-zero exclusion with identical algebra and contact maps.',
'cdp:st:C.2.UN.7':'Read both complete proofs. Checked T=T1 and m0=m in P4.13, angular multiplicities in NC1, P360 on the same proper tube, and every proper-domain transfer of the reduced/twice-section ruling arguments. P300 and P294 use (U,T,Z,eta,eta*pi) and their exact support maps; the contracted case still has pi1=1 and positive Euler number.',
'cdp:st:C.2.UN.12':'Read both complete proofs. Checked torsion canonical and chi(O)=0 inputs on the proper tube, all normal/ruled/Hopf alternatives, same-map applications of UN7/VII1/VII2/P300, and each Euler, delta and branch term in both directions of the zero criterion.',
'cdp:st:C.2.MH.4':'Read both complete proofs. D1.9 gives the same integral class and P289 its prime augmentation system. The H3 surjection, H4 isomorphism, both character restrictions, class-VII Betti numbers and parity still force Euler zero with the same equality data.',
'cdp:st:C.2.INT.1':'Read both complete proofs. Checked the adjacent effective divisor and blowdown, Hopf coefficient square, principal elliptic cover, normalized root chart and isogeny, scalar-automorphy kernel and Gauduchon contradiction. Freshly read published Brinzanescu-Moraru pp1663-1667 and attached Dloussky-Teleman Remark2.7; the integral torsion-killing application is explicit.',
'cdp:st:C.2.INT.2':'Read both complete proofs. Checked complex-flat NAC scope, maximum ratios, the two-component reduction, self/external conductors, nodal intersection, inverse unit removal and P297 coordinate permutation/vanishing sphere. Freshly read attached Dloussky Definition2.20, Lemma2.22 proof and following paragraph; PDF page binding remains the attached prior source record.',
'cdp:st:C.2.INT.3':'Read both complete proofs. Checked sigma=tau*pi, rational normalization singularities, proper analytic/finite conductor duality, descended line bundles, finite Picard avoidance, full scheme-conductor cohomology, exact exceptional-tree Euler counts and the last-blowup proof of both equality directions. Arbitrary full component and conductor multiplicities remain.',
'prop:II:rational-torus-fibre-euler':'Read the complete P360 proof against the rational part of original UN7 and final receiver. A5.16 inputs are established by P281; P210 gives elliptic minimal complements 3/4; P294 identifies the nonzero H1 kernel; P289 and parity exclude zero. Six compact Euler labels specialize through explicit fibre-product projections and inverses preserving f,mS,eta,pi.',
'lem:II:normal-cubic-compact-core':'Read the complete P361 proof against original D4.1 and the final receiver. Checked primary powers, full-jet scaling with unit and multiplicity, right-inverse transport and reverse embeddings, compact core, torus-cover exterior-square map and spherical square zero.',
'lem:II:cyclic-cubic-boundary':'Read the complete P362 proof against the transferring originals. Checked both character algebras, w(v)=1 inverse maps, relative H1, lifted boundary relations and inverse pushdown, compact pairing rank, cofinal formal-functions ideals, q=max(Pg-1,0), and every w^3=s^2(s-u^k) blowup with character increment one.',
'prop:II:cubic-root-attachments':'Read the complete consolidated P380 statement and proof after its full constituent comparisons. All six rows are the exact proved nu/ell bounds. The degree-three two-zero row has (P,nu)=(1,3) or (2,2); the doubled degree-three zero is excluded. The definition of R_d, common-factor gluing, degree bound, conductor inverse and all local charts remain explicit. The local coefficient Phi and bidegree b avoid collisions with the common divisor A and cover degree d.',
'cdp:st:A.5.16':'Read complete original and receiving statements/proofs, then final changed paragraphs. Proved the proper-domain torsion-omega and chi(O)=0 inputs and compact specialization, and checked every duality/Leray/coefficient-square, conductor, exceptional-support and negative-Euler exclusion step. Rechecked P210 and the compact/proper consumers; no original conclusion is removed.',
'lem:II:delta-two-curve-rings':'Read complete original and receiving owner. RA7 aliases the cusp-plus-line ideal row and RA8 the (3,4,5) row of the identical A.T.14 display, using the same normalization parameters and ambient coordinate lifts.',
'cdp:st:A.5.18':'Read the complete original proof and compared the entire receiver. Its only content change is a numbered display for the three exact zG products; other changes are equation aliases RA9/RA11. Checked the nine-element finite module, Hessian determinant, normal lifts, quartic poles, branch parity and final ruled minimality proof.',
'lem:II:canonical-boundary-blowup':'Read both complete owners. The exact Jacobian and inverse blowup charts are unchanged. CIR4 aliases A.RC.5 under (W,Wprime,DW,sigma_*DW,d,a); the permanent target is outside the one aliases invocation.',
'night:P4.13':'Read complete original and receiving proposition/proof. UI5/6/8 aliases use the same minimum multiplicity, exceptional valuation bound, Lefschetz determinant and H1/H1-duality transpose. No assertion or numerical bound changes.',
'cdp:st:C.2.NC.1':'Read both complete cited owners. UI7 receives the same angular equation, gcd-component count and torus translations/permutations; the exact full multiplicities and normalization complements give the same Euler identity.',
'prop:II:minimal-boundary-complements':'Read the complete current consumer proof. The A5.16 scope repair preserves the same anticanonical divisor, blowdown sequence, complement increments, minimal boundary table, conductor pushout, virtually abelian quotient and endpoint hypersurface-branch contradiction; its full-CDP clause keeps its global hypotheses.',
'cdp:st:A.5.3':'Read the complete current divisor proof while checking A5.16. Finite conductor duality and the exceptional matrix produce the effective D on the same minimal resolution; the general hypersurface statement supplies the required proper-tube canonical-boundary identity.',
'cdp:st:A.5.12':'Read the complete current proof while checking A5.16. The initial canonical evaluation and compact Cartier-sequence HRR calculations establish torsion omega_S and chi(O_S)=0 before the subsequent Picard restriction argument; the proper-tube applications establish those inputs separately by P281.',
}
outcomes['lem:II:normal-cubic-compact-core'] += ' The final complete receiver was reread after adding RD2: division by the common coefficient factor glues the horizontal root divisor, the generic tangent ratio identifies the branch fields, and integral closure gives the finite-cover isomorphism for any genus of C before D4.2.'
outcomes['cdp:st:C.2.D4.2'] += ' Its RD2 input is now the earlier general conductor-cover clause of P361, on the same f,mS,H and C; the receiving tail has no later-owner mathematical dependency.'
outcomes['cdp:st:C.2.RAT.5'] += ' The field-isomorphism formula RD2 and its full proof are owned by earlier P361; P380 applies the identical cover map before its attachment arguments.'
events=[]
fields_event=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
for owner,outcome in outcomes.items():
    ident=f'publish:c4:horizontal:{len(events)+1:03d}'
    events.append(dict(statement_id=owner,date='2026-11-23',who=WHO,type='used and rechecked in this run',
        outcome=outcome+' No independent, mathematical-program execution or final-PDF credit.',event_id=ident,
        phase='complete original and receiving proof comparison',source_file='agents/continuation4_horizontal/S6_SERIES_PUBLISH_horizontal_comparison.md',
        source_row='',source_event_type='used and rechecked in this run',evidence_group=ident,publish_input_file='',publish_input_row='',date_utc=STAMP,
        where='Complete original/proposed files in continuation3_provenance/sec07_tail; final guarded receiver and comparison notes in continuation4_horizontal'))
write(OUT/'S6_SERIES_PUBLISH_horizontal_CHECK_EVENTS.tsv',events,fields_event)

evidence='agents/continuation4_horizontal/S6_SERIES_PUBLISH_horizontal_comparison.md; S6_SERIES_PUBLISH_horizontal_guards.tsv'
unit=[]
explanations={
'D01':'Removed the UN12 earlier-ambient/replacement narrative; the full original remainder has been read.',
'D02':'Removed defensive clauses while keeping all explicit hypotheses, maps and positive scope assertions.',
'D04':'All references in the receiving mathematical body resolve through current paper statement/equation labels.',
'D06':'Moved references point to exact earlier owners and the consolidated companion; no old document numbering is printed.',
'D08':'Removed actual/retained/owner/process wording; selected trees and blowup divisors are named geometrically.',
'D09':'No body program path remains. Existing appendix paths are preserved; eleven owner links are retargeted to the receiving proofs.',
'D11':'Duplicate scope assurances and closing recaps are removed; the full scheme and multiplicity hypotheses remain where needed.',
'D12':'P360 owns the general rational Euler conclusion and six exact compact specializations; P380 owns all distinct cubic root/attachment bounds; RAT2 owns the distinct tacnode bounds. P361/P362 and earlier formula owners eliminate repeated calculations.',
'D13':'Every mathematical result belongs to a titled numbered statement and proof; five nonempty subsections contain the entire original remainder.',
'D14':'The local dependency order is complete: P360; attachment owners; P361/P362/RAT6/D4.1/D4.2 before P380; UN7/UN12/MH4; INT1/2/3. Whole-paper placement/proportion and final PDF remain root gates.',
'D15':'The bounded Further-results guard lists each receiving result once and matches the body.',
'D17':'Known inputs use their cited statements with exact scope. The source-specific analytic, field, conductor and boundary maps remain proved where those applications require them.',
'D18':'Published Brinzanescu-Moraru pages freshly read; Merle-Teissier theorem/corollary freshly reopened; Dloussky/Teleman attachment passages reread. Prior analytic-duality/GR/formal-functions primary readings are retained with their stated limits.',
'D19':'All 157 old equation targets survive exactly once at their numbered receiving formula or explicit alias; every original statement label/tag is preserved.',
'D20':'Every shared notation has an explicit receiving map. P380 uses Phi for a local remainder and b for the section bidegree, preserving A for the common divisor and d for cover degree.',
'D22':'Every threshold and local choice is derived in the same proof: degree, branch count, contact order, positive pairing rank, Gauduchon degree or full-function map.',
'D23':'Source typography and alias placement are repaired. Integrated typesetting and every final PDF page remain unclaimed.',
'D24':'The receiving interface and proper irreducible results match main C/G1 domains. A separate final current-form main-C/abstract/outline comparison follows integration.',
'D25':'A5.16 proper-domain scope is proved explicitly; RAT9 finite-algebra locator and the NAC complex-flat input are corrected. Every original and receiving inference was read; no original theorem was refuted.',
}
for r in rows(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv'):
    if r['paper']!='II' or r['unit_id']!='sec:II:07':continue
    t=r['defect_type']
    state='done after guarded admission'
    if t in ['D10','D16']:state='keep inherited done'
    if t in ['D14','D23','D24'] or r['row_kind']=='structure':state='local comparison complete; root final placement/render/front-body gate pending'
    unit.append(dict(paper='II',unit_id='sec:II:07',unit_title=r['unit_title'],row_kind=r['row_kind'],defect_type=t,
        prior_status=r['status'],proposed_status=state,date_utc=STAMP,evidence=evidence,
        detail=explanations.get(t,'Full original/receiving remainder read for this defect class; no local instance remains. New subsection rows receive no movement credit.') if t else explanations['D14']))
write(OUT/'S6_SERIES_PUBLISH_horizontal_unit_proposals.tsv',unit,['paper','unit_id','unit_title','row_kind','defect_type','prior_status','proposed_status','date_utc','evidence','detail'])

print(f'Wrote {len(defects)} compact exact defect rows, {len(events)} honest receiving-review events, and {len(unit)} stable original-unit proposals.')
print('No shared source, shared table, derived inventory or source copy modified.')
