from pathlib import Path
import csv,datetime as dt,hashlib,json,re

R=Path(__file__).resolve().parents[1]
def bind(p): return {'path':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}
def read(p): return json.loads((R/p).read_text())
def verify(o):
    if isinstance(o,dict):
        if 'path' in o and 'sha256' in o: assert bind(o['path'])['sha256']==o['sha256'],o['path']
        for v in o.values(): verify(v)
    elif isinstance(o,list):
        for v in o: verify(v)

p='agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_WV_v1_20261122/S6_SERIES_PUBLISH_II_A2_WV'
index=p+'_admission_recommendation.json'
assert bind(index)['sha256']=='2ecff51cef2a5c755f67cd9d6c80e054a37785bd1aff372b7e2851d5046be890'
ar=read(index);verify(ar);verify(read(p+'_v1_manifest.json'))
t=ar['targets'][0];pr=read(ar['proposal']['path'])
o=(R/t['full_original_block']['path']).read_text();n=(R/t['proposed_full_block']['path']).read_text();w=o
for g in pr['guards']:
    assert hashlib.sha256(w.encode()).hexdigest()==g['intermediate_before_sha256']
    assert w.count(g['literal_old'])==1
    w=w.replace(g['literal_old'],g['literal_new'])
    assert hashlib.sha256(w.encode()).hexdigest()==g['intermediate_after_sha256']
assert w==n
for g in reversed(pr['guards']):
    i=g['offset_before'];assert w[i:i+len(g['literal_new'])]==g['literal_new']
    w=w[:i]+g['literal_old']+w[i+len(g['literal_new']):]
assert w==o
assert o.count('\\item ')==n.count('\\item ')==6
assert re.findall(r'\\\[(.*?)\\\]',o,re.S)==re.findall(r'\\\[(.*?)\\\]',n,re.S)
assert re.findall(r'(?<!\\)\$(.*?)(?<!\\)\$',o,re.S)==re.findall(r'(?<!\\)\$(.*?)(?<!\\)\$',n,re.S)
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch54_review.json'
assert not (R/review).exists()
rd=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
 checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
 actual_reading='Entire 405-line frozen derivation read in two bounded outputs; complete original and final six-item proofs and all displays read separately; complete comparison read in two bounded outputs; both full program sources and outputs, source and program-scope receipts and event proposals read. An earlier combined output truncated and contributes no separate complete-reading credit. All nested bindings and twelve guards are verified. No III/IV proof or closed I/V source was opened.',
 mathematical_review=[
 'Evaluation at one identifies the finite conductor with Hom_A(B,A), with inverse multiplication; finite hypersurface duality gives omega_T(D)=nu^*omega_S. The same common ideal proves nu^-1(C)=D_red and that C is the full singular locus. A point blowdown gives exceptional coefficient mu-1 by pairing K+D with E; injectivity of pullback on Pic carries the torsion line to T0. K_T0^2=-n excludes D0=0. The torsion twist is flat, so the opened NAC definition and theorem apply to the actual T0.',
 'The frozen rational route keeps every connected conductor component and every image-curve identification. The explicit compact-to-Hausdorff pushout map T union_D C -> S is a homeomorphism. Compatible triangulation makes the inclusion a cofibration and identifies its cylinder model. Van Kampen with actual j_* and eta_* gives 1+b+r-s generators and r relations. In an N-sheeted free-abelian cover, the presentation has deficiency N(b-s)+1. The H2 surjection from its two-complex to the torus K(Z^q,1) gives deficiency at most q-q(q-1)/2<=1, including q=0,1. Thus b<=s and e(C)=c+s-b>=c>0. The declared open-support Euler input completes this case.',
 'The frozen elliptic route uses the exact ratio of the two anticanonical sections to obtain D0=E+Gamma. The mu-1 blowup formula preserves reduced conductor and a node of its rational cycle. At a generic point, A, B and B/A are flat over the curve parameter. The hypersurface Ext vanishing yields Hom_A(B,A)/z=Hom_(A/z)(B/z,A/z), compatibly with evaluation at one. The reduced slice conductor is the sum of maximal ideals of the smooth normalization branches; the local reduced quotient inside C^ell is diagonal C. The common-constant ring has embedding dimension ell, forcing ell=2. The written map from C{x,y}/(xy) and its inverse prove the node; the explicit parameter-preserving square-root Morse coordinates give g=UV. Normal crossings and the retained conductor node give a triple point, hence strict positivity.',
 'The original proof first excludes the two Inoue configurations. In the negative-definite Inoue-Hirzebruch cycle matrix, adjunction makes the difference D0-Z orthogonal to every component and hence zero. For the parabolic configuration, Gamma^2=0 in the negative-definite surface lattice gives Gamma numerically zero; E^2=-n fixes its coefficient one. The negative cycle Laplacian has constant kernel, including [0] for one nodal component and the two-parallel-edge matrix for two components. Therefore D0=E+k Gamma. Torsion of O((k-1)Gamma), using the dual for k=0, contradicts the nonempty zero divisor of a power of its defining section unless k=1.',
 'Reduced nodal conductor survives all allowed blowups. Normal crossings make T->Y an immersion with line quotient L, and the exact tangent sequence gives c1(L)=-c1(T), c2(T)=c1(T)^2. Class VII instead gives e(T)=b2(T)>0 and K_T^2=-b2(T). The exact Chern residual is 2(n+k). This stronger original exclusion was verified only after release and receives no prerelease credit; it remains in the printed proof.',
 'For the remaining connected cycle-with-trees, the conductor and ambient blowdown maps induce the two specified Z fundamental groups. The frozen cylinder presentation specializes with r=s=1, a->t,d1->k,w1->w and the same image graph basis. This gives precisely the original relation t^k=w. For k nonzero and w nontrivial, both cyclic edge maps inject and reduced amalgam normal forms embed F_b. For w=1, the retraction onto F_b proves its inclusion. For k=0 and w nontrivial, Z*H contains the free subgroup generated by t and g t g^-1 for every nontrivial g in H, including finite-order g; expanded reduced words prove injectivity. Virtual abelianness forces H=1, and its one-relator abelianization has rank at least b-1. Every case gives b<=1. The exact curve count gives e(C)=c+1-b>=1, and the support decomposition finishes the original proof.',
 'Both programs were fully inspected. The prerelease graph/pole program recomputes Euler and finite-cover counts and both blowup Jacobians; its truncated node-ring computation is explicitly diagnostic. The postrelease program expands the Chern product, computes the general edge quadratic identity and checks the exceptional cycle sizes and Euler specialization. Neither is a complete geometry/group certificate. Original six steps, six displays and all inline mathematics are preserved.'
 ],
 primary_readings=[
 dict(source='../S6_PUBLISH_literature_arxiv/math_0406387/VII-Dloussky-04-05.tex',sha256='e1f894c1c727cb45e86b63e27e76f4b294c8d85d4d7306e4ddffd2929a3e6aed',locus='Full attached lines65-120,512-575,643-742 read: introduction NAC theorem and terminology; NAC definition, support lemma and anticanonical relation; complete relevant cycle classification proposition and proof. Agent receipt binds arXiv-v3 page numbers. Root web PDF attempt returned DisabledError and is not a PDF-opening claim.'),
 dict(url='https://www.jstage.jst.go.jp/article/tmj/55/2/55_2_283/_pdf/-char/en',root_web_ref='turn157723027view1',locus='Complete extracted pp284-285 read: intermediate connected cycle with trees, deformation to primary Hopf, pi1=Z and flat line bundle parametrization. No whole-article or image-reading claim.')],
 chronology='Complete prerelease alternative frozen at06:08:30UTC and released at06:08:46UTC. The original stronger Inoue Chern exclusion, official DOT source and original-cycle program were checked after release. Agent event timestamps retained. Root review, sources, computations and packaging add no event.',
 statement_conclusions_and_domains_preserved=True,mathematical_steps_changed=0,independent_required_owners=1,independent_evidence_groups=1,proposed_events=2,publication_page_reading_credit=0,
 editorial_scope='Twelve title/header/internal-reference/exact-citation guards; the cited anticanonical identity and deduced numerical triviality are attributed separately. The original production-style enumerate marker and brief preview sentence remain for the global editorial pass; no global defect closure is claimed.',
 evidence=[bind(index),ar['comparison'],ar['display_preservation'],ar['program_scope']])
(R/review).write_text(json.dumps(rd,indent=2)+'\n')
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:pages={x['tag']:x['page'] for x in csv.DictReader(f,delimiter='\t')}
target=dict(owner=t['statement_owner'],tag=t['tag'],old_page=pages[t['tag']],original=t['full_original_block'],proposed=t['proposed_full_block'],freeze=t['freeze_receipt'],release=t['release_receipt'],events=ar['event_proposals'],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation2_A; reasoning effort not separately exposed',guards=[dict(old=g['literal_old'],new=g['literal_new'],type=','.join(g['defect_types']),reason=g['reason']) for g in pr['guards']],scope='Positive Euler number for singular supports with smooth class-VII normalization of positive minimal second Betti number.',event_note='Root complete frozen/original/final comparison; all original six mathematical steps retained. Stronger original Inoue exclusion verified after release only. No additional independent group or mathematical repair.')
s=(R/'S6_SERIES_PUBLISH_II.tex').read_text();a=s.index('\\section*{Programs}');b=s.index('\\end{longtable}',a);last=s[s.rfind('\n',a,b-1)+1:b];assert last.strip()
rows=(R/ar['program_rows']['path']).read_text()
extra=dict(old=last,new=last+rows,type='D09,D18',reason='List each new bounded exact algebra program once, with the retained proof calculations it checks.',location='Programs')
scope=read(ar['program_scope']['path']);copies=[dict(**{'from':c['output']},to='code/'+Path(c['output']['path']).name) for c in scope['new_computations']]
cfg=dict(batch=54,root_review_complete=True,source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],review_evidence=[bind(review),bind(index),ar['comparison'],ar['proposal'],ar['program_scope'],ar['display_preservation'],*ar['sources']],targets=[target],additional_source_edits=[extra],code_copies=copies,mathematical_repairs=[],scope='02WV admitted after full frozen derivation, six-item original/final comparison and exact algebra/source checks. Original proof and all mathematical claims are preserved; twelve editorial guards and two program rows. Two events in one independent group; no final page or global defect-class credit.')
assert cfg['source_before_sha256']=='54fda00c812b3ea09eb35a68fcc79267a80525fe4fdf334d907fa76185d427e7'
assert cfg['ledger_before_sha256']=='f9645b7546815b5b0861fdd4cade83858ed731959a0308663bbb99ade35f11f6'
out='records/S6_SERIES_PUBLISH_II_continuation2_batch54_config.json';assert not (R/out).exists();(R/out).write_text(json.dumps(cfg,indent=2)+'\n');print(json.dumps(bind(out)))
