from pathlib import Path
import csv, datetime as dt, hashlib, json, re

R=Path(__file__).resolve().parents[1]
def bind(p):
 b=(R/p).read_bytes()
 return dict(path=p,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
def read(p):return json.loads((R/p).read_text())
def check(b):
 actual=bind(b['path'])
 assert actual['sha256']==b['sha256'] and actual['bytes']==b['bytes'],b['path']

pre='agents/continuation2_B/01CJ/S6_SERIES_PUBLISH_II_B2_CJ_'
ip=pre+'packet_index.json';idx=read(ip)
assert bind(ip)['sha256']=='daaa957f9535fbac7a358876a8539027156f473fe61dbea49229b0838cae9701'
for b in [idx['admission'],idx['events'],*idx['files'],*idx['external_frozen_inputs']]:check(b)
ap=pre+'admission_proposal.json';a=read(ap);t=a['targets'][0]
assert bind(ap)['sha256']=='a832bade014bbcc39762cf57530150a17e8104574f5650347f459e4304fafc25'
guards=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason']) for g in t['guards']]
assert len(guards)==23
old=(R/t['original_full_block']['path']).read_text()
new=(R/t['proposed_full_block']['path']).read_text()
w=old
for g in guards:
 assert w.count(g['old'])==1
 w=w.replace(g['old'],g['new'],1)
assert w==new
assert old.count('\\item')==new.count('\\item')==7
pattern=r'(?<!\\)\\\[(.*?)(?<!\\)\\\]'
ds=re.findall(pattern,old,re.S)
assert len(ds)==8 and ds==re.findall(pattern,new,re.S)
for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}']:
 assert re.findall(pat,old)==re.findall(pat,new)

evidence=[bind(ip),bind(ap),a['review'],a['postrelease_comparison'],
 a['draft_notation_guard'],a['draft_notation_diff'],a['identity_guard_replay'],
 a['final_read_receipt'],t['derivation'],t['prerelease_read_receipt'],
 t['freeze_receipt'],t['release_receipt'],*a['development_corrections'],
 a['completed_CI_read'],a['completed_BW_postrelease_locator_read'],
 bind(pre+'dependency_01CI.tex'),bind(pre+'dependency_01BW.tex')]
for cp in a['computations']:
 evidence.extend([cp['program'],cp['output'],cp['receipt']])
for b in evidence:check(b)
now=dt.datetime.now(dt.timezone.utc).isoformat()
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch74_review.json'
rd=dict(created_utc=now,
 checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
 actual_reading='Root read the complete16591-byte frozen CJ derivation before the original or comparison. Root then read every item of the complete original6659-byte and final8355-byte blocks, the6067-byte postrelease comparison,7537-byte review, all23 guards and Programs guard, the complete24738-byte admission proposal, both standalone program sources, all92+27 successful checks and their evidence and every local output row, execution and freeze/release receipts, prereading/final receipts, identity replay, development corrections and all3 proposed events. The completed supporting CI and BW blocks were read in full after the CJ comparison. These readings were untruncated. No new primary-source or final-PDF-page reading is claimed.',
 mathematical_review=[
  'The admissible tuple and all hypotheses are carried by identity: full fibre mS in the smooth torus-fibred threefold, rational normalization resolution with the specified ruled-boundary morphism, coefficient-two section C, degree-two cover of the ordinary-triple image H and a cubic normal tensor with no common coefficient zero. B9 excludes the singular rational image for a degree-two connected normalized cover, and Riemann-Hurwitz excludes a smooth elliptic image. H is therefore P1. Ambient rational Chern-class vanishing gives deg N=-2 and the trivial line O_Y(S)|H.',
  'For the convention P(N) of lines and xi=c1(O(1)), xi squared=2 and K=-2xi. The reduced finite root divisor R=R1+R2 has class3xi, degrees1and2 overH, and both normalizations rational. The tangent ratio identifies the root fields; integral closure extends the field maps and inverse to the complete normalized curves. A finite degree-one component over normalH equalsH by integral closure. Adjunction gives arithmetic genus4; the normalization exact sequence gives total delta5 even for disjoint components.',
  'The finite algebra O+O(-1)+O(-2), multiplied by the cubic, defines the cyclic cover. It is Cohen-Macaulay and regular in codimension1 because the branch divisor is reduced, and a smooth branch meridian is a three-cycle. For a root functional w on a line ell, the unique vector v satisfying w(v)=1 has q3(v)=1. Conversely v gives ell=Cv and that functional. These inverse evaluation maps agree with transitions and identify the complement with the normal cubic level for every normal splitting.',
  'The original relative-cohomology route is retained. Fibre cohomology kills both direct images of O(-1) and p_*O(-2). Relative Serre trace pairs R1p_*O(-2) with (detN)*, so the former is detN=O_P1(-2), whose H0 vanishes. Leray and the character decomposition yield H1(X0,O)=0. Resolution Leray injects H1(X,O) into the sum of local geometric-genus spaces, at most1 by CI; projectivity gives b1(X)<=2. The independently frozen RR/Hartogs argument gives the same bound and remains in the check record.',
  'Let nu be total local branch excess, c the number of connected root components and lambda the sum of link first Betti numbers. The actual exceptional intersection matrices identify exceptional H1 with link H1 by the pair sequence. The boundary incidence graph has2+s vertices,nu+s edges andc components, so b1(D)=nu-2+c+lambda. Extra boundary blowups subdivide an edge or add a rational leaf. The Euler values e(R)=4-nu and e(U)=3nu and this boundary formula retain the disconnected case exactly.',
  'Write g*R_i=3B_i+sum a_ji E_j. Pullback divided by3 sends a base relation alpha to the boundary relation with exceptional coefficients Aalpha/3 and strict coefficients alpha. Pushforward kills exceptional classes and sends B_i toR_i. The two maps are inverse because exceptional classes are independent by negative definiteness. Thus epsilon=d_D-dimV=2-dim span(R1,R2) lies in{0,1}. In the xi,F basis R1=(1,s),R2=(2,-s), their determinant is-3s; at s0 the kernel is generated by(2,-1). No equality of unrelated relation spaces is assumed.',
  'The boundary span contains g*R of square54. Hodge index makes its orthogonal complement inside the divisor space negative definite, hence the boundary span nondegenerate. The pair sequence gives b1(U)=b1(X)+epsilon<=3 and image H2(U)=Vperp. Compact cycles mapping to zero inH2(X) pair trivially; the image form is nondegenerate, so rank I_U=b2(X)-d_D+epsilon. Euler substitution gives exactly2nu+2b1(X)-lambda+epsilon>=2nu-2. The frozen lower bound is the same expression after b1=2q and omission of the nonnegative epsilon term.',
  'The completed BW transport is proved before any normal-splitting specialization, using the leading normal jet and a smooth tubular map on a compact core. Thus it embeds the present core in a nearby torus with its compact intersections preserved. Its fundamental-group image A has rank<=3; the map lifts to R4/A, which retracts to the torus span(A)/A. The H2 image lies in Lambda2(A_Q), and the wedge form is zero since Lambda4(A_Q)=0. The positive pairing for nu>=2 is impossible, so nu<=1.',
  'At a simple root of the total cubic, CH identifies the exact conductor with(y squared) on the smooth normalized branch and the resolution is the identity. Two attached C-points over oneH value therefore give two multiple roots unless their root points coincide; a cubic cannot have two distinct multiple roots. The coincident point is multibranch and costs at least1 in nu. Distinct paired values cost separately, so at most1 is possible. K surviving original vertical trees yield at leastK-1 distinct H incidence edges, rdom<=1 from the remaining generic triple branch, and the proved graph inequality gives eGamma>=K-1. The exact Euler decomposition then gives eS>=2-r+N0+K-1>=1-rdom>=0.',
  'The prerelease program derives the19 Jacobian quotient bases by Groebner leading ideals. Weighted phases have constant multiplicity across primitive cyclotomic roots; evaluation and inverse Lagrange interpolation identify the rational companion blocks with the weighted monodromy eigenspaces. Tensoring with the reduced cubic-root block and computing the rational kernel gives the stated link dimensions. Newton lattice counts give the local genera, and112 multisets under delta5 satisfy the total bounds. All92checks pass. The27postrelease checks independently verify the exact boundary formulas, the exceptional-correction congruence and relation map, and relative cohomology. The arbitrary exceptional-rank map is proved in prose; the two-variable symbolic matrix check is correctly limited. These119checks comprise one computation event.',
  'All7original items and8actual displays are preserved. The earlier metadata count9 was an accounting error corrected against the full block; no display is lost. The integer-division precision adjustment occurred before first execution, the rejected AddFile patch wrote no file, and the unadmitted draft projection-notation clarification is retained. No original mathematical error was found, no supporting theorem receives new independent credit, and no global defect or final-page gate is closed.'
 ],
 chronology='Agent freeze09:06:29.920851 precedes release09:06:34.219399. Supporting BW frozen derivation and CI application were disclosed before that freeze. Root reviewed the frozen derivation first, then originals; root claims comparative review only. No extra independent/root/dependency event is proposed.',
 mathematical_errors_found_in_original=[],original_proof_items_preserved=7,
 original_displays_preserved=8,publication_page_reading_credit=0,evidence=evidence)
assert not (R/review).exists()
(R/review).write_text(json.dumps(rd,indent=2)+'\n')
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:
 pages={x['tag']:x['page'] for x in csv.DictReader(f,delimiter='\t')}
target=dict(owner=t['statement_owner'],tag=t['tag'],old_page=pages[t['tag']],
 original=t['original_full_block'],proposed=t['proposed_full_block'],
 freeze=t['freeze_receipt'],release=t['release_receipt'],events=idx['events'],guards=guards,
 who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort not separately exposed; checker continuation2_B',
 scope='Full primitive rational degree-two ordinary-triple domain with the specified ruled-boundary morphism, for every normal-bundle splitting: e(S)>=0.',
 event_note='Root complete comparative review at '+now+'. All7original items and8actual displays retained; exact relative trace, boundary incidence, exceptional relation inverses and compact torus pairing verified. No original mathematical error. One evidence group; root adds no independent, primary or final-page event.')
extra=[dict(old=g['old'],new=g['new'],type=g['defect_type'],owner=g['location'],location=g['location'],reason=g['reason']) for g in a['additional_source_guards']]
copies=[dict(**{'from':cp[k]},to='code/'+Path(cp[k]['path']).name) for cp in a['computations'] for k in ('program','output')]
cfg=dict(batch=74,root_review_complete=True,
 source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],
 ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],
 review_evidence=[bind(review),*evidence],targets=[target],additional_source_edits=extra,
 code_copies=copies,mathematical_repairs=[],
 scope='01CJ admitted after the complete frozen derivation and every original/final proof step. Seven items and8displays remain;23target guards and1Programs guard,3events in1group,119exact checks. The original relative-cohomology and exact disconnected-boundary routes remain. No original error or theorem-scope change. Development corrections retained; no global defect, provenance or final-page closure.')
assert cfg['source_before_sha256']=='53b3c435bf45d126b9091236e4f563709b3945b5644f63db68680421cd971816'
assert cfg['ledger_before_sha256']=='312f7606b80161ed3c261c07cb019c431f31bf05fdc8a29492607b6b91386fcb'
out='records/S6_SERIES_PUBLISH_II_continuation2_batch74_config.json'
assert not (R/out).exists()
(R/out).write_text(json.dumps(cfg,indent=2)+'\n')
print(json.dumps(bind(out)))
