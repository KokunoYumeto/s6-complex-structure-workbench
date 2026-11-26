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

pre='agents/continuation2_B/01CH/S6_SERIES_PUBLISH_II_B2_CH_'
ip=pre+'packet_index.json';idx=read(ip)
assert bind(ip)['sha256']=='9c1ec24fc41cd22a1c0f9eadd631728520f0bef8175449f2f9bb528733f3bc4a'
for b in [idx['admission'],idx['events'],*idx['files'],*idx['external_frozen_inputs']]:check(b)
ap=pre+'admission_proposal.json';a=read(ap);t=a['targets'][0]
assert bind(ap)['sha256']=='9b695bba0591a8758537e0cd49af72d7aca26aad9a630671f2e3212908080382'
guards=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason']) for g in t['guards']]
assert len(guards)==11
old=(R/t['original_full_block']['path']).read_text()
new=(R/t['proposed_full_block']['path']).read_text()
w=old
for g in guards:
 assert w.count(g['old'])==1
 w=w.replace(g['old'],g['new'],1)
assert w==new
assert old.count('\\item')==new.count('\\item')==4
ds=re.findall(r'\\\[(.*?)\\\]',old,re.S)
assert len(ds)==5 and ds==re.findall(r'\\\[(.*?)\\\]',new,re.S)
for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}']:
 assert re.findall(pat,old)==re.findall(pat,new)

evidence=[bind(ip),bind(ap),a['review'],a['draft_refinement_guards'],
 a['draft_refinement_diff'],a['identity_guard_replay'],a['final_read_receipt'],
 t['derivation'],t['prerelease_read_receipt'],t['freeze_receipt'],t['release_receipt'],
 *a['development_corrections'],
 bind(pre+'prereading_certificate_failed_v0_receipt.json'),
 bind(pre+'prereading_certificate_failed_v0_stderr.txt')]
for cp in a['computations']:
 evidence.extend([cp['program'],cp['output'],cp['receipt']])
for b in evidence:check(b)
now=dt.datetime.now(dt.timezone.utc).isoformat()
repair=dict(owner=t['statement_owner'],tag=t['tag'],type='D22,D25',
 original_error='The original proof identified the full conductor unit with the cubic derivative away from H.',
 corrected_identity='For P(w,y,z)=q3(w,1,z)+yA(w,y,z), u(y,z)=P_w(lambda(y,z),y,z); its restriction to y=0 is the cubic derivative.',
 exact_witness='P=(w-t-y)(w-1)(w-2), lambda=t+y gives P_w-q_w=-y(2w-3), equal to 7/25 at t=0,y=1/10,w=1/10.',
 scope='This exact polynomial is an algebraic witness for the functional identity, with no claim to be a compact torus degeneration. The nonzero value on H, conductor ideal, theorem hypotheses and Euler conclusion are unchanged.',
 error_settled=True,statement_refuted=False)
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch73_review.json'
rd=dict(created_utc=now,
 checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
 actual_reading='Root read the complete13451-byte frozen CH derivation before opening the packet comparison or original proof. Root then read the complete index and7974-byte comparison, all four original/final proof items and five displays, the entire18597-byte admission proposal with11 target guards and Programs guard, both complete standalone program sources and all33+10 successful output checks, both execution receipts, freeze/release, prerelease/final reading receipts, identity replay, all draft/code correction records, the failed-run receipt/stderr, and all three proposed events. Every reading was untruncated. No new primary-source or PDF-page reading is claimed.',
 mathematical_review=[
  'The original domain is retained: an irreducible nonnormal torus-fibre support with rational normalization resolution, the specified morphism to a Hirzebruch surface and its positive anticanonical boundary, smooth rational H, generic ordinary triple transversal, nonzero total cubic at every H point, and a locally unibranch degree2 or3 root component. Every map and datum is carried by the identity on that domain.',
  'The total cubic divisor is proper and finite of degree3 because no projective fibre is contained in it. Its generic ordinary-triple roots are distinct, and a nonreduced horizontal component would remain repeated generically; vertical components are excluded. The tangent ratio x/y gives the isomorphism of the generic branch field and the root field. Their normalization extends it and its inverse to C=R_d^nu. Local unibranchedness gives one normalization point over each root point; distinct C points over an H value therefore have distinct root directions.',
  'At a simple total root, F(yw,y,z)=y cubed P(w,y,z), and the implicit root lambda(y,z) gives the actual monic factor X=x-y lambda. The triangular coordinate map has determinant1 and explicit inverse x=X+y lambda. Analytic division and differentiation yield G mod X=y squared P_w(lambda,y,z). This is a unit times y squared. The product-normalization inclusion shows that functions supported on the smooth X branch come from the hypersurface ring exactly in the ideal generated by G mod X; the other reduced factor injects into its normalization. Multiplication by the inverse unit identifies the conductor ideal with(y squared), and the minimal resolution is an isomorphism there.',
  'The original literal off-H unit description has the precisely recorded error. The new formula restricts to the same nonzero cubic derivative on H and changes no inference about the conductor. The independent factored polynomial computes the nonzero correction7/25 at the stated rational point. This is a proof-identity repair, without a refuted statement or a change of theorem scope.',
  'Every vertical attachment lies at a multiple root of the total cubic, including a root shared with the remaining linear component. A cubic has at most one distinct multiple root. Together with the bijection C->R_d on points this makes distinct attachment points have distinct H images. The argument does not assume any unproved property of the other root component.',
  'The three generic normalization branches give rdom<=3-d through their finite map degrees. The actual reverse blowup divisor formula Dnew=sigma*D-E preserves a rational tree. A wholly exceptional original positive vertical tree requires a multiplicity-one blowup; otherwise the square-zero total ruling fibre is supported in a negative-definite exceptional matrix. Distinct original fibres require distinct such centres, so z<=N0. For every remaining nondominating tree the path from C through contracted components to its first strict component yields an actual image intersection with a curve different fromH. There are K=r-z-rdom such trees.',
  'The exact complement comparison Z minus D_red -> S minus Gamma_red and h inverse(Gamma)=D_red give the compact pushout homeomorphism. Compatible triangulation makes the boundary inclusion a cofibration; the rational surface and rational boundary tree are simply connected. Van Kampen gives pi1(Gamma)=pi1(S). Rational normalization components make the former the free incidence-graph group. The full local torus group input has an abelian normal subgroup of finite cyclic quotient, so two free generators and their mth powers exclude graph rank>=2. Thus beta<=1, eGamma=n+1-beta>=n.',
  'The K distinct H intersection values give distinct incidence edges. Delete H and collapse spanning trees in the c receiving components; K-c<=beta, and each receiving component contains another curve vertex, so c<=n-1. Hence n>=K and eGamma>=K. For K0 the inequality is immediate. The exact complement formula gives eS>=2-r+N0+K=2-rdom+(N0-z)>=d-1. All differences are explicitly nonnegative. This uses the graph argument of RAT3 on its actual shared premises and does not transfer its degree-one conclusion to this higher-degree cover.',
  'The maps t->(t squared,t to power2k+1), inverse t=v/u to powerk, and integral equation t squared=u give the finite normalization of v squared=u to power2k+1. For k1 or2 the unique point over the origin proves the A2/A4 examples. All five original displayed environments remain byte-identical.',
  'The prerelease33-check program uses exact triangular-coordinate identities, localized-ideal Groebner equality with UJ=1, every cubic multiplicity partition and degree allocation, cusp parametrizations and symbolic Euler gap identities. Finite grids are explicitly supporting calculations. The postrelease10-check program uses a separately factored polynomial with a moving root to distinguish the full derivative from its restriction. Both sources and all successful outputs are read;43 checks constitute one computation event. The pre-execution parenthesis correction, failed constant-gcd invocation, explicit-generator repair, and unadmitted wording/pushout refinement remain in their records with no failed-run credit.'
 ],
 chronology='Freeze08:50:12.845884 precedes release08:50:15.401431. Agent declares no CH target exposure before the freeze and declares supporting CF,02Y2,B5,B7,CE,CG inputs. Root read the frozen derivation first but claims comparative review only. No dependency event is added.',
 mathematical_errors_found_in_original=[repair],
 original_proof_items_preserved=4,original_displays_preserved=5,
 publication_page_reading_credit=0,evidence=evidence)
assert not (R/review).exists()
(R/review).write_text(json.dumps(rd,indent=2)+'\n')
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:
 pages={x['tag']:x['page'] for x in csv.DictReader(f,delimiter='\t')}
target=dict(owner=t['statement_owner'],tag=t['tag'],old_page=pages[t['tag']],
 original=t['original_full_block'],proposed=t['proposed_full_block'],
 freeze=t['freeze_receipt'],release=t['release_receipt'],events=idx['events'],guards=guards,
 who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort not separately exposed; checker continuation2_B',
 scope='Full specified rational ruled-boundary domain, smooth rational ordinary-triple image, nonzero total cubic, locally unibranch degree2 or3 root component: e(S)>=d-1, including A2/A4 cusps.',
 event_note='Root complete comparative review at '+now+'. Four original proof items and all five displays retained. Correct full derivative-unit identity and explicit normalization/conductor/pushout maps; no theorem change. One evidence group; root adds no independent or primary/final-page credit.')
extra=[dict(old=g['old'],new=g['new'],type=g['defect_type'],owner=g['location'],
 location=g['location'],reason=g['reason']) for g in a['additional_source_guards']]
copies=[dict(**{'from':cp[k]},to='code/'+Path(cp[k]['path']).name)
 for cp in a['computations'] for k in ('program','output')]
cfg=dict(batch=73,root_review_complete=True,
 source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],
 ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],
 review_evidence=[bind(review),*evidence],targets=[target],
 additional_source_edits=extra,code_copies=copies,mathematical_repairs=[repair],
 scope='01CH admitted after complete frozen derivation and complete four-item original/final comparison. All five original displays and every label/tag remain. Eleven target guards and one Programs guard; full off-H derivative-unit identity repaired, with unchanged conductor/theorem. Three events in one group,43 exact checks. All development failures retained honestly. No global defect, provenance or final-page gate is closed.')
assert cfg['source_before_sha256']=='d082e8cc1d290deca9e8c1855010e6789dd93c9b6fea01c5233984ee0f4120c8'
assert cfg['ledger_before_sha256']=='144e70bf7b2d051cfa29f320403f5d0ff9ac2997e067ad87fbd6ebdccb3614d4'
out='records/S6_SERIES_PUBLISH_II_continuation2_batch73_config.json'
assert not (R/out).exists()
(R/out).write_text(json.dumps(cfg,indent=2)+'\n')
print(json.dumps(bind(out)))
