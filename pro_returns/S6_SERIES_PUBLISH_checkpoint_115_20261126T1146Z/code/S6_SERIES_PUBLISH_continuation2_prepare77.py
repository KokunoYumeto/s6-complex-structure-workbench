from pathlib import Path
import csv, datetime as dt, hashlib, json, re

R=Path(__file__).resolve().parents[1]
def bind(p):
    b=(R/p).read_bytes()
    return dict(path=p,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
def read(p): return json.loads((R/p).read_text())
pre='agents/continuation2_B/01CK/S6_SERIES_PUBLISH_II_B2_CK_'
ip=pre+'packet_index.json'; ap=pre+'admission_proposal.json'
assert bind(ip)['sha256']=='73794042176b2b6c7d5ddea0f140c50fe83a6f63b72b6008fb71de0237747452'
assert bind(ap)['sha256']=='7637f2166fc080a312958395972207b9fba401e1a48c455e8ad5be92e7909e4d'
idx=read(ip); a=read(ap); t=a['targets'][0]
ev={}
def bindings(x):
    if isinstance(x,dict):
        if 'path' in x and 'sha256' in x:
            b=bind(x['path']); assert b['sha256']==x['sha256'],x['path']
            if 'bytes' in x: assert b['bytes']==x['bytes'],x['path']
            ev[x['path']]=b
        for v in x.values(): bindings(v)
    elif isinstance(x,list):
        for v in x: bindings(v)
bindings(idx);bindings(a)
for p in [ip,ap,'agents/ii_infra/recovery_20261121/primary_inputs/S6_SERIES_PUBLISH_II_Grauert1963_primary.txt']:
    ev[p]=bind(p)
guards=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason']) for g in read(pre+'body_guards.json')]
assert len(guards)==26
old=(R/t['original_full_block']['path']).read_text();new=(R/t['proposed_full_block']['path']).read_text()
w=old
for g in guards:
    assert w.count(g['old'])==1
    w=w.replace(g['old'],g['new'],1)
assert w==new
assert old.count('\\item')==new.count('\\item')==8
pat=r'(?<!\\)\\\[(.*?)(?<!\\)\\\]'
od=re.findall(pat,old,re.S);nd=re.findall(pat,new,re.S)
assert od==nd and len(od)==11
for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}']:
    assert re.findall(pat,old)==re.findall(pat,new)
source=bind('S6_SERIES_PUBLISH_II.tex'); ledger=bind('CHECK_EVENTS.tsv')
assert source['sha256']=='e2b6b5bdca297f1ada515b77141450c353f3a089810a2d38b0039321b2797684'
assert ledger['sha256']=='02be5550f0936ece4fbf92d12c2c41ef3ba8bc0191940f8b6714d9a359aa31f8'
extra=[dict(old=g['old'],new=g['new'],type=g['defect_type'],owner='Programs',location=g['location'],reason=g['reason']) for g in a['additional_source_guards']]
assert len(extra)==1
assert (R/'S6_SERIES_PUBLISH_II.tex').read_text().count(old)==1
assert (R/'S6_SERIES_PUBLISH_II.tex').read_text().count(extra[0]['old'])==1
now=dt.datetime.now(dt.timezone.utc).isoformat()
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch77_review.json'
rd=dict(created_utc=now,
 checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
 actual_reading='Root read all26197 bytes of the complete frozen CK derivation before opening the target. Subsequently read all8 original and final proof items, both intervening headings, all11 displays, the full postrelease comparison and review, both complete program sources, every object of both complete outputs including the13-type local table and all76 budget collections, all26 target guards and the Programs guard, the3 events, freeze/release receipts, supporting-exposure receipt, both execution receipts and final reading/identity receipts. One combined metadata/guard call was truncated; the guards, admission metadata, primary receipts and events were subsequently read in bounded untruncated calls. Root additionally viewed and read the entire Grauert1960 printed59 primary image and read all4602 bytes of the attached1963 corrigendum text. Root assigns no fresh Merle-Teissier or A Campo primary-page reading here; the agent actual readings remain bound and explicitly scoped. No final publication-page credit is assigned.',
 mathematical_review=[
  'The exact RAT1 domain is retained: the full torus fibre, rational normalization, specified ruled-boundary morphism, noncontracted degree-two ordinary-triple conductor component, and a common normal-cubic zero divisor of degree one. The earlier image argument gives smooth rational H without using primitive cubic coefficients. On W=P(N) with the lines convention, deg N=-2, xi^2=2 and K_W=-2xi. The complete root divisor B=R1+R2+F has class3xi; B_h has class3xi-F. Adjunction gives p_a(B_h)=2, horizontal delta3, total delta6, and F.B_h=3. The tangent-root field map identifies the normalization of R2 with the actual degree-two cover C.',
  'At fibre intersection multiplicity one the full branch germ is a node. At multiplicity two, square completion and analytic unit rescaling give t(x^2-t^mu); mu1 is A3 by x=sqrt(2)X,t=T+X^2, and mu>=2 gives D_(mu+2). The horizontal delta bound yields the exact even D4,D6,D8 and odd D5,D7,D9 lists. Unit cube-root maps identify the actual suspension equations. When the whole fibre intersection lies at one point, the section is transverse to F. The possible quadratic branch gives either a tangent smooth branch, two smooth branches, or a cusp. The exact delta formula floor(k/2)+ord(a(t)^2-t^k)<=3 leaves k1, k2 without cancellation, or k3 with ord a=1. These produce D6, four transverse branches, or the ordinary cusp transverse to both lines; no additional local type remains.',
  'For D6 the exact map u=x*sqrt(phi(x)/(2x^2)),v=t-phi(x)/2 and inverse x=psi(u),t=v+u^2 send the branches to u=0 and v=plus-or-minus u^2. For the four-branch case, axes transverse to all tangents make the quartic Newton face convenient. For the actual cusp equation the linear inverse maps u=alpha*s+beta*t,v=beta*t and s=(u-v)/alpha,t=v/beta preserve both smooth branches. The printed nonconvenient Newton vertices are(3,1,0),(2,2,0),(0,5,0),(0,0,3). Its compact normals are(1/4,1/4,1/3),(3/10,1/5,1/3), and its noncompact inequality is j+k/3>=1. The complete analytic remainder bounds are5/4,11/10 and3/2,6/5. The only positive integral point outside the interior is(1,1,1), weight5/6 on both compact facets; every positive increment makes both weights exceed one and the noncompact weight is at least4/3. The actual faces are nondegenerate and the suspension derivative in z is nonzero on the torus. Merle-Teissier gives p_g=1.',
  'The full analytic comparison to the frozen convenient cusp route uses Weierstrass preparation u^2+b(v)u+c(v), d(v)=-(c(v)-b(v)^2/4)/v^3, x=(u+b(v)/2)/sqrt(d(v)),t=v, with inverse u=sqrt(d(t))*x-b(t)/2,v=t. The other branch becomes x-a(t), where a(t)=(t+b(t)/2)/sqrt(d(t)) has nonzero derivative. The equation unit is carried by its explicit cube-root change in z. The subsequent linear map y=t+x/a_prime(0) has its stated inverse. This proves the exact correspondence between the two calculations; the original nonconvenient calculation remains in the manuscript.',
  'A nonzero p_g over F requires intersection at least2 and horizontal delta at least1. The fibre intersection sum3 permits at most one such value, while every nonzero value away from F costs horizontal delta at least3. Thus total p_g<=1. The independently frozen embedded-resolution route gives characteristic polynomials(T-1)(T^4-1)^2 and(T-1)(T^4-1)(T^5+1) for the two delta-six cases, respectively. Its exact Bezout identities with Phi3 and the two spectral projectors for the cubic factor prove absence of fixed suspension vectors without identifying actual monodromy with a companion matrix. The determinant27 or9 is an arithmetic cross-check. This alternate local-link proof stays in the records.',
  'The original shorter formal-functions proof remains. For the proper analytic resolution over a Stein representative, M=(R1rho_*O)_x is finite length of dimension p_g and equals its completion. For I=O(-E),J=m_x O, compactness and common radical give I^c subset J subset I, hence cofinal powers. Actual quotient restriction maps induce mutually inverse maps of inverse limits. Grauert Hauptsatz IIa on printed59 gives the required formal-functions isomorphism, and Hauptsatz I supplies coherence. The whole printed59 image and complete corrigendum text were actually read by root. The successive H1 restrictions are surjective since their kernels have curve support and H2=0; compatible lifting gives M onto H1(E,O_E). The coherent normalization sequence and its node-difference map give h1=sum g_i+beta, and the topological normalization sequence gives b1=2sum g_i+beta. The negative-definite exceptional matrix in the local pair sequence identifies link H1 with E H1. Therefore the total link bound lambda<=2 follows from total p_g<=1.',
  'The cyclic algebra O plus O(-1) plus O(-2) gives chi(O_X0)=2 and the resolution inequality b1(X)<=2. Its complement is identified with {q3(v)=1} by the existing evaluation map and its inverse. All three boundary components are retained. The relation map sends base coefficients alpha_i to strict coefficients alpha_i and exceptional coefficients sum_i a_ji alpha_i/3; pushforward and projection give the inverse. Their classes have exactly one relation because F and R1 span the base Picard group. Hence b1(U)=b1(X)+1<=3. Euler, normalization and the nondegenerate boundary span yield e(U)=3(nu-2),b1(D)=nu-2+lambda, and compact rank2nu-4+2b1(X)-lambda>=2nu-6. Radial derivative3 on q3=1 permits the existing exact compact transport into the nearby torus. Its fundamental-group image has rank at most3; the lift to the corresponding torus cover and the exterior-square map make the intersection pairing zero. Thus nu>=4 is impossible and nu<=3.',
  'Above the common zero, every normalization branch is counted, giving nu_F=1+a with a1 or2. The loss of distinct attachments there is at most a-1; away from it each duplicate costs at least one in nu_out through the primitive-cubic conductor calculation. Hence ell<=nu_F-2+nu_out=nu-2<=1. The remaining degree budget gives r_dom<=1, and the actual conductor graph gives at least K-ell distinct edges with K>=r-N0-r_dom. The existing graph and Euler maps yield e(S)>=2-r_dom-ell>=0. Every original item and display agrees with this independently frozen result. No original mathematical error, scope restriction or proof substitution was found.',
  'Both standalone program sources and their complete outputs were read:95 prereading checks and27 postrelease checks, with all76 allowed local-budget collections. They use distinct exact symbolic and polyhedral methods, with general analytic and topological arguments supplied in prose. The unavailable historical A_cubic_scalar_one.py was not represented as executed. Exactly3 events in one evidence group are admitted for this owner, without dependency or independent root credit. The packet retains every label, hypertarget and equation tag. Its removal of the visible StatementRecord call is left to the already pending consistent global printed-tag restoration. No global defect class, final provenance or final rendered-page gate closes here.'
 ],
 chronology='Agent freeze09:36:39.359677 UTC precedes target release09:36:45.449667 UTC. Root read the complete frozen derivation before target opening. The formal-functions route was compared after release, with this timing disclosed. Agent primary readings and development corrections retain their original receipts.',
 primary_image_actually_read=dict(path='/workspace/scratch/e3bb51a74e2f/S6_SERIES_PUBLISH/temporary_B_pdf/S6_SERIES_PUBLISH_CK_Grauert1960_p59.png',sha256='86dd6b0c6c8e37b715de8e15d76e36e6e7e6a8c646a52fa608768999e733cbca',scope='Full printed59 image; temporary published-source material omitted from checkpoint'),
 original_proof_items_preserved=8,original_displays_preserved=11,mathematical_errors_found_in_original=[],publication_page_reading_credit=0,evidence=list(ev.values()))
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:
    pages={x['tag']:x['page'] for x in csv.DictReader(f,delimiter='\t')}
target=dict(owner=t['statement_owner'],tag=t['tag'],old_page=pages[t['tag']],
 original=t['original_full_block'],proposed=t['proposed_full_block'],freeze=t['freeze_receipt'],release=t['release_receipt'],events=idx['events'],guards=guards,
 who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort not separately exposed; checker continuation2_B',
 scope='Complete single common cubic zero in the rational degree-two ordinary-triple case: all local analytic cases, total p_g and link bounds, exact compact pairing and attachment maps, and e(S)>=0.',
 event_note='Complete root comparative review at '+now+'. All8 original items and11 displays preserved;95+27 exact checks fully read, analytic formal-functions comparison and precise primary locator verified. No mathematical error, scope restriction or independent root event. Three events in one evidence group.')
copies=[]
for c in a['computations']:
    for kind in ['program','output','receipt']:
        b=c[kind];copies.append(dict(**{'from':b},to='code/'+Path(b['path']).name))
cfg=dict(batch=77,root_review_complete=True,source_before_sha256=source['sha256'],ledger_before_sha256=ledger['sha256'],
 review_evidence=[],targets=[target],additional_source_edits=extra,code_copies=copies,mathematical_repairs=[],
 scope='01CK admitted after full frozen derivation and all8 original/final items. Eleven displays, all labels, targets and equation tags retained. Twenty-six target guards and one Programs guard;3 events in1 group. Original formal-functions and nonconvenient Newton routes preserved with exact maps/citations. No scope restriction, original mathematical error, global-defect, final-provenance or publication-page closure.')
out='records/S6_SERIES_PUBLISH_II_continuation2_batch77_config.json'
assert not (R/review).exists() and not (R/out).exists()
(R/review).write_text(json.dumps(rd,indent=2)+'\n')
cfg['review_evidence']=[bind(review),*ev.values()]
(R/out).write_text(json.dumps(cfg,indent=2)+'\n')
print(json.dumps(dict(config=bind(out),review=bind(review),bindings=len(ev))))
