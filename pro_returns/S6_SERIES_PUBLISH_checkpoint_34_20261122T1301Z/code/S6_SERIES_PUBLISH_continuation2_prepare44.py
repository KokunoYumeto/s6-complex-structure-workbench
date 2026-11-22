from pathlib import Path
import csv,datetime as dt,hashlib,json,re,collections
R=Path(__file__).resolve().parents[1]
def bind(p):return {'path':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}
def read(p):return json.loads((R/p).read_text())
p='agents/continuation2_B/01B5/S6_SERIES_PUBLISH_II_B2_B5_'
proposal=p+'admission_proposal.json';d=read(proposal);t=d['targets'][0]
assert bind(proposal)['sha256']=='46d678ef37c83845b7093ec0d17ef757670e3d887bfcd0fa2f4a7c5d5be1fdb8'
assert bind(t['proposed_full_block']['path'])['sha256']=='6b49524fcbda0c5fb3c509e9e0101cf79d2c1d8ad396a1323a8ddadf56745327'
event=p+'event_proposals.json';assert bind(event)['sha256']=='d9737531836531a9a45f85a15b6133557d2909b0ebb5651490dd3aba251d04a7'
cm=read(d['consolidation_map']['path'])
bindings=[d[k] for k in ['consolidation_map','review','primary_reading','exact_target_diff','WP_preexisting_admission_transport']]
bindings.extend(cm[k] for k in ['retired_full_original_block','retired_location_after_block','statement_and_content_map','receiving_owner_map','preservation_receipt','wp_historical_freeze','wp_historical_release','wp_historical_derivation','wp_existing_admission'])
bindings.extend(t[k] for k in ['original_full_block','proposed_full_block','freeze_receipt','release_receipt','derivation'])
for c in d['computations']:bindings.extend(c.values())
for b in bindings:assert bind(b['path'])['sha256']==b['sha256'],b['path']
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text();before=source
original=(R/t['original_full_block']['path']).read_text();proposed=(R/t['proposed_full_block']['path']).read_text()
assert source.count(original)==1
temp=original
for g in t['guards']:
 assert temp.count(g['old'])==g['expected_occurrences_in_owning_block']
 temp=temp.replace(g['old'],g['new'],g['expected_occurrences_in_owning_block'])
assert temp==proposed
source=source.replace(original,proposed,1)
for g in d['additional_source_guards']:
 assert source.count(g['old'])==g['expected_occurrences_in_source'],g['change_id']
 source=source.replace(g['old'],g['new'],g['expected_occurrences_in_source'])
ids={}
for key,pat in [('labels',r'\\label\{([^{}]+)\}'),('hypertargets',r'\\hypertarget\{([^{}]+)\}'),('display_tags',r'\\tag\{([^{}]+)\}')]:
 old=re.findall(pat,before);new=re.findall(pat,source);assert collections.Counter(old)==collections.Counter(new),key
 ids[key]=dict(before_count=len(old),after_count=len(new),occurrence_multiset_preserved=True)
assert before.count('\\begin{proof}')-source.count('\\begin{proof}')==1
for s in re.findall(r'\\\[.*?\\\]',original,re.S):assert s in proposed
completed=read('records/S6_SERIES_PUBLISH_required_check_completion_manifest.json')['rows']
assert completed['night:P4.18']['evidence_sha256']==d['WP_preexisting_admission_transport']['sha256']
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch44_review.json';assert not (R/review).exists()
rd=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
 actual_reading='Complete original B5 nine-item proof, complete WP five-item proof, full prerelease B5 derivation and final ten-item merged proof read. Final merged block reread after D02 correction; complete 21 body guards, nine supplementary guards, exact statement/content map, receiver map, chronology, primary-source receipt and preservation receipt reviewed. Full fresh code and output and both full historical program sources/stdout read. No full visual publication-page reading is claimed.',
 mathematical_review=[
  'For h=x^a-y^bz^c and D=a(b+c), v=u^(1/(mD)) gives Phi=(v^(b+c)x,v^a*y,v^a*z). The scalar equation tau^(mD)=u(tau^(-(b+c))X,tau^(-a)Y,tau^(-a)Z) has nonzero tau derivative mD*v(0)^(mD-1). Psi uses those inverse powers; uniqueness of the selected root proves v o Psi=tau and tau o Phi=v, hence both composition identities and f=(h o Phi)^m. The repeated-factor derivative argument proves reducedness for every allowed triple. The reverse statement-scope map uses u=1, preserving the global proper fibration and common multiplicity.',
  'The independent frozen proof uses the proper finite map pi:(x,y,z)->(x,y^b,z^c) to x^a-UV=1. Coordinate bounds prove properness and root counts give degree bc. Its matching sphere is smooth in the explicit endpoint disks and Lagrangian by cancellation of the two polar-coordinate area forms. The complex tangent-normal frame reverses the normal orientation, giving square -2. The class PD_M^(-1) pi^* PD_M0 has square -2bc by compact-support pullback and oriented degree; no division of an integral class is used.',
  'The frozen two-open-set maps identify Re(x^a)<2/3 with a contractible x-domain times the monomial fibre, and Re(x^a)>1/3 with a contractible monomial domain times a roots. Their overlap has a*d circle components. The displayed Bezout inverse identifies each monomial component with C*. Mayer-Vietoris sends e_ij to e_j, with kernel basis e_ij-e_1j. Explicit endpoint cone disks joined by cylinders in the first open set realize these basis elements by spheres. The pinch map realizes every integral sum, including the transferred class. Positive weighted dilation and Psi place its compact representatives in a global torus fibre with preserved square; its lifted sphere contracts in C^2.',
  'The retained printed witness is the explicit circle-cylinder map over an embedded arc in x^a-v^d=1. Both endpoint links have slope (c/d,-b/d); meridian disk intersection gives framing product -(b/d)(c/d), and replacing cone caps by transverse relative chains gives the same local intersection. Both orientation reversals at the second endpoint cancel, giving square -2(b/d)(c/d). The frozen class of square -2bc and this printed class both imply the same proved existential obstruction through their specified embeddings. No unproved equality between the two classes is asserted.',
  'The primary join theorem applies to the analytic summands. The annulus parametrization has the stated Bezout inverse and exact radius interval. On the cone-product pushout, ([g,t],h)->[g,h,(1-t)/2] and (g,[h,t])->[g,h,(1+t)/2] form a homeomorphism to a cones on H with common base. The piecewise inverse is written. Contraction of the first cone has inverse homotopies by the homotopy extension property; the meridian collapse and backtracking attaching homotopies yield the preserved wedge with (a-1)d two-spheres and (a-1)(d-1) circles.',
  'The MPW variables (z,x,y;m,k,l) map to (x,y,z;a,b,c), with the explicit coordinate exchange ordering b,c. The stated irreducible domain is gcd(a,b,c)=1. Normalized residue relations give rational Euler number a/((b/d)(c/d)); order-one terms contribute zero. Rational elimination in the Seifert presentation leaves exactly 2g base generators. The exact pair sequence and Poincare-Lefschetz duality give rank(I)=b2+b1-b1(boundary)=a-1. For a=2,b=1,c=l, the lens calculation uses MPW4.2(2) for l>=2 and its 4.2(1) quadratic case for l=1; the integral pair sequence gives determinant absolute value2l.',
  'The moved mixed-example map (u,v)->(u^3v^2,v,u^2) is finite because u is integral with u^2=z, and birational with u=x/(z*y^2). Its image ring is C{u^2,v} direct-sum u^3v^2*C{u^2,v}, with both inclusions proved. Since 1,u generate the normalization module, h and u*h in the image ring give conductor u^2v^2*C{u,v}. The three minors3u^2v^2,-4u^4v,-2u generate(u), and that divisor maps to the line (0,v,0). This preserves every assertion of the WP statement and the exact failed finite-rank-drop hypothesis.'
 ],
 computation_review='New standard-library extended Euclid, Fraction elimination, split-kernel maps, generated exponent semigroups and sparse derivatives were read with the complete output:576 exponent matrices,5207 Seifert/rank triples,23100 kernel identities,10 determinants,750 conductor memberships. Historical E_Hirzebruch.py and binomial_milnor.py and their full stdout were read; no full by-eye reading of the separately truncated64-entry JSON is claimed. These finite computations support the general algebraic proofs and add one computation event only.',
 primary_root_readings=[
  dict(url='https://www.numdam.org/item/CM_1991__80_1_1_0.pdf',locus='Nemethi1991 section2.1 domain and TheoremL1 p2, Example2.4(a) p3, full statements read',web_refs=['turn255037267view0','turn133043869view3','turn924248129view1']),
  dict(url='https://webhomes.maths.ed.ac.uk/~v1ranick/papers/mpw.pdf',locus='MPW arXiv math/0509451v1: full domain p2; Theorem4.1 p6, Theorem4.2 p7, rational Euler formula p8, Lemma4.6 and proof p11 read. Agent official-primary PDF has identical extracted texts on all13pages.',web_refs=['turn133043869view0','turn175577541view0','turn175577541view1','turn175577541view2','turn924248129view0']),
  dict(url='https://pi.math.cornell.edu/~hatcher/AT/AT.pdf',locus='Hatcher Propositions0.16-0.18 pp15-16, full statements and proofs read',web_refs=['turn255037267view2','turn133043869view1','turn133043869view2'])
 ],
 consolidation=dict(surviving_owner='cdp:st:A.5.15',moved_aliases=['night:P4.18','stmt:P4.18'],moved_tag='02WP',full_statement_assertion_union_preserved=True,original_B5_display_blocks_preserved=9,all_source_identities=ids,removed_proof_count=1,old_WP_unlabelled_alternative_proof_displays='Retained in the complete original WP block record; the one merged proof supplies their asserted spherical conclusion.',required_row_policy='B5 receives one new independent completion; WP already completed in CLEAN05 and retains its exact existing completion and event rows. Its source authority is now the B5 owner through the preserved labels. No extra WP completion or new mathematical event.',dependency_map='All49 coded occurrences and the three literal uses are mapped by the preserved labels. The old P4.16--P4.18 numeric interval is expanded to exact labels. The stronger combined statement retains the full hypotheses imported by A.5.17.'),
 no_mathematical_value_refuted=True,page_reading_credit=0,evidence=[bind(proposal)]+bindings)
(R/review).write_text(json.dumps(rd,indent=2)+'\n')
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:pages={x['tag']:x['page'] for x in csv.DictReader(f,delimiter='\t')}
extra=[]
for i,g in enumerate(d['additional_source_guards'],1):
 loc='Bibliography' if i>=7 else ('Programs' if i==6 else ('night:P4.18' if i==1 else 'cdp:st:A.5.15' if i==2 else 'night:P4.28' if i in [3,4] else 'night:P4R.15'))
 extra.append(dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason'],owner=loc,location=loc))
copies=[]
for key,name in [('program','S6_SERIES_PUBLISH_II_B2_B5_comparison_certificate.py'),('output','S6_SERIES_PUBLISH_II_B2_B5_comparison_certificate_output.json')]:copies.append({'from':d['computations'][0][key],'to':'code/'+name})
target=dict(owner=t['statement_owner'],tag=t['tag'],old_page=pages[t['tag']],original=t['original_full_block'],proposed=t['proposed_full_block'],freeze=t['freeze_receipt'],release=t['release_receipt'],events=bind(event),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation2_B; reasoning effort not separately exposed',guards=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason'],occurrences=g['expected_occurrences_in_owning_block']) for g in t['guards']],scope='Complete all-exponent binomial exclusion, spherical class, full retained homotopy/intersection calculations and mixed normalization example, with exact B5/WP statement consolidation. One new B5 independent check; existing WP completion retained.',event_note='Root fully read the frozen derivation, both original proofs and the final ten-item merged proof and verified the exact maps. The source merge adds no independent WP group and no page-reading credit.')
cfg=dict(batch=44,root_review_complete=True,source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],review_evidence=[bind(review),bind(proposal)]+bindings,targets=[target],code_copies=copies,additional_source_edits=extra,mathematical_repairs=[],scope='The new01B5 check is admitted after a complete frozen/printed comparison. The two overlapping binomial propositions are consolidated at cdp:st:A.5.15 by the explicit unit-coordinate maps and full assertion-preservation map. Both permanent tags and all statement labels remain on that proposition; all nine original B5 displays and every labeled identity remain. The merged proof retains the mixed normalization, conductor and rank-drop calculation, and the old complete WP proof is preserved in its original-block record. WP was independently completed in CLEAN05; its completion and historical events are unchanged and it earns no new check. Exact primary locators, coordinate/homeotopy maps, Programs rows and bibliography entries are corrected. No false numerical value was found; source authority is one merged owner while the197-row audit history remains intact.')
out='records/S6_SERIES_PUBLISH_II_continuation2_batch44_config.json';assert not (R/out).exists();(R/out).write_text(json.dumps(cfg,indent=2)+'\n');print(json.dumps(bind(out),indent=2))
