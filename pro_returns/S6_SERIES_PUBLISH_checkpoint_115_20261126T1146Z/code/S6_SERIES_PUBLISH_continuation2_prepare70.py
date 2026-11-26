from pathlib import Path
import csv, datetime as dt, hashlib, json, re

R=Path(__file__).resolve().parents[1]
def bind(p):
    b=(R/p).read_bytes()
    return dict(path=p,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
def read(p):return json.loads((R/p).read_text())
def verify(o):
    if isinstance(o,dict):
        if 'path' in o and 'sha256' in o:
            assert bind(o['path'])['sha256']==o['sha256'],o['path']
        for v in o.values():verify(v)
    elif isinstance(o,list):
        for v in o:verify(v)

pre='agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_XA_v1_20261122/S6_SERIES_PUBLISH_II_A2_XA_'
ap=pre+'admission_recommendation.json'
mp=pre+'v1_manifest.json'
assert bind(ap)['sha256']=='1d1a73a2aa23cf21aabb52edcb138e3fcf017586e775d196c0e3bf2d17ff44ab'
assert bind(mp)['sha256']=='9a533fa3a0b45b9f4bad7c0435b2802d0583c4b8d7c40ea7ecf5772cac4a4057'
a=read(ap)
verify(a)
verify(read(mp))
t=a['targets'][0]
p=read(a['proposal']['path'])
guards=[dict(old=g['literal_old'],new=g['literal_new'],type=','.join(g['defect_types']),reason=g['reason']) for g in p['guards']]
assert len(guards)==18
old=(R/t['full_original_block']['path']).read_text()
new=(R/t['proposed_full_block']['path']).read_text()
w=old
for g in guards:
    assert w.count(g['old'])==1
    w=w.replace(g['old'],g['new'],1)
assert w==new and old.count('\\item')==new.count('\\item')==7
stripped=new
for label in p['new_equation_labels']:
    assert stripped.count('\\label{'+label+'}')==1
    stripped=stripped.replace('\\label{'+label+'}','')
assert re.findall(r'\\\[(.*?)\\\]',old,re.S)==re.findall(r'\\\[(.*?)\\\]',stripped,re.S)
assert len(re.findall(r'\\\[(.*?)\\\]',old,re.S))==7
for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}']:
    assert re.findall(pat,old)==re.findall(pat,stripped)
scope=read(a['program_scope']['path'])
now=dt.datetime.now(dt.timezone.utc).isoformat()
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch70_review.json'
evidence=[bind(ap),bind(mp),a['derivation'],a['frozen_derivation'],a['input_receipt'],a['postrelease_comparison_receipt'],a['comparison'],a['proposal'],a['event_proposals'],a['program_scope'],a['program_rows'],a['display_preservation'],a['block_diff'],a['bibliography_entries'],*a['primary_sources']]
for cp in scope['new_computations']:
    evidence.extend([cp['source'],cp['output']])
rd=dict(
    created_utc=now,
    checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
    actual_reading='Root read the entire351-line17326-byte frozen derivation before opening the complete original target. All seven original and final items, all seven displays, the complete comparison, all eighteen owner guards, bibliography insertion and Programs row, both complete programs and their complete outputs, freeze/release, input/postrelease/primary-source receipts, events and exact display/inline-preservation records were read in bounded untruncated outputs. Agent progress summaries had already described the two routes; root claims comparative review only. No new root reading of the Favre or Dloussky--Oeljeklaus primary pages is claimed.',
    mathematical_review=[
        'The exact maps are nu:N->S, sigma:T->N minimal resolution, i:S->Y embedding, rho=i*nu*sigma and beta:T->T0 the blowdown to the minimal model. The effective pole identity is omega_T(D)=(nu sigma)^*omega_S, whose mth power is trivial. At a point blowup Kprime=beta^*K+E and Dprime=beta^*D+(a-mu)E; the torsion intersection with E forces a=mu-1 and hence Dprime=beta^*D-E. Projection formula and beta_*O=O make line-bundle pullback injective. Thus the effective pushdown D0 satisfies K0+D0 torsion. Positive n=b2(T0) and K0^2=-n make D0 nonzero. Torsion has locally constant transition functions after taking roots of the trivializing power, so the opened NAC theorem applies in its flat-twist scope and gives a global spherical shell.',
        'The frozen proof uses the opened Dloussky--Oeljeklaus foliation existence theorem. A local primitive vector column gives a saturated tangent line. In the two blowup charts (u,uv) and (uv,v), the columns (u*a,b-v*a) and (a-u*b,v*b) push forward to u or v times the original column, as checked by their actual Jacobians. Dividing common height-one factors produces the lifted line on the blowup. The proper image of the meromorphic-function graph gives inverse pullback/descent maps through each blowdown, so a(T)=a(T0)=0. Ratios of sections then give h0(M)<=1 and h2(M)<=1 for every line bundle M; Riemann--Roch on all positive tensor powers forces c1(M)^2<=0. For an actual line class e with square0, the bundles M tensor E^t for every integer t give a^2+2t*a.e<=0, forcing a.e=0.',
        'For B=rho^*TY, b2(Y)=0 and rational Poincare duality give c1(B)=c2(B)=0. Divide the foliation composite by its effective common divisor Z to obtain Lbar=L(Z). Its primitive column is saturated by the factorial local-ring denominator argument. Q=B/Lbar is torsionfree, Q** is locally free, and Q**/Q has finite length z0. The saturation E of the rank-two differential image is locally free by the depth lemma; det(T_T)->det(E) has an effective zero divisor R and e=-K+R. Torsionfreeness of B/E places Lbar inside E. Saturation of E/Lbar in Q** gives line J of class j=e-ell, and quotient I_Z1 tensor J1 of class-e. The exact K-theory identity gives (ell^2+j^2+e^2)/2=z0+z1. All three squares are nonpositive and both lengths nonnegative; hence e^2=0 and beta^*K0.e=0.',
        'For every irreducible curve C on the minimal T0, a square-zero class has K0.C=0 by that same polarization. Negative square with positive arithmetic genus gives K0.C=2pa-2-C^2>0. Arithmetic genus0 forces a smooth rational curve through normalization genus and delta; minimality excludes square-1, giving K0.C>=0. The effective R0=beta_*R consequently satisfies K0.R0>=0. Projection formula and the exceptional canonical divisor yield beta^*K0.e=-K0^2+K0.R0=n+K0.R0>0, the contradiction. This complete general-foliation proof remains checking evidence; it is not substituted into the printed proof.',
        'The retained first item uses the stronger conclusions inside the previously completed WV and WY proofs: the Inoue--Hirzebruch and parabolic models have reduced nodal pole divisor, the normal-crossing conclusion makes the normalization smooth, and the immersive tangent exact sequence gives c2(T)=K_T^2. Since the former equals positive b2 and the latter equals its negative, both cases are excluded. The remaining intermediate model has the connected maximal rational cycle with trees; the prior NAC support propagation makes Supp(D0)=A0. No stronger classification theorem is silently used.',
        'Favre Theorem1.2.24(1)-(2), printed p35, gives n independent rational-curve classes and their negative-definite intersection form in this intermediate case. The actual theorem and construction/conormal pages42,44,46 give N_F^*=O(-A0) tensor a flat line. Its determinant with the tangent line gives c1(T_F)=-K0-A0, extending across the finite singular set by Hartogs. Favre Theorem1.2.32 and its proof give local first integrals z^alpha*w^beta, with positive orders alpha,beta, so the primitive tangent field is beta*z*d_z-alpha*w*d_w. The two blowup charts give beta*u*d_u-(alpha+beta)*v*d_v and (alpha+beta)*u*d_u-alpha*v*d_v; a regular centre gives a simple saddle in one chart and regular points elsewhere. Thus the original epsilon=0,1 blowup formulas apply. Dloussky--Oeljeklaus Theorem3.1, pp1528-1529, supplies the specifically cited invariant-curve and order-one assertions. The citation is corrected to identify p44 as the foliation construction rather than falsely calling its printed heading a proof of Theorem1.2.30.',
        'The rational cycle with attached trees has n components and n nodes, including self-nodes. Its normalization exact sequence maps branch values to their differences, giving chi(O_A0)=n-n=0. The divisor exact sequence and Riemann--Roch give (K0+A0)A0=0. With V0=-A0, this yields K0V0-V0^2=0. A blowup changes KV-V^2 by epsilon^2-epsilon=0 and reduces K^2 by1, so KV=V^2 and K^2=-n-k. To identify the frozen and printed sheaf computations, select the actual Favre tangent line in the same diagram: ell=-K+V+Z, e=-K+R, j=R-V-Z, c1(J1)=K-R. Substitution into the identical quotient-Chern identity gives exactly the printed B(R,Z)=n+k+z0+z1.',
        'The universal bilinear intersection update is Delta B=-c^2+cd-d^2+(1+epsilon)c+(1-2epsilon)d. Substituting c=1+u,d=1-epsilon+v gives1-(u^2-uv+v^2). Twice that quadratic is u^2+v^2+(u-v)^2, proving Delta B<=1 without restrictions on the integral relative coefficients. On T0 put D=D0,A=A0 and K=-D,V=-A. The exact remainder n+q(R0+D,Z0+D-A)-B0 equals n+D^2-DA+A^2, which is0 because D^2=-n and DA=A^2. Negative definiteness gives q(X,Y)=(X^2+Y^2+(X-Y)^2)/2<=0, with equality only X=Y=0. The effective nonzero D and effective R0 have a nonzero sum in the independent curve basis, so B0<n strictly. After k increments at most1, B<n+k, contradicting its nonnegative-length Chern expression. All original displayed mathematical content is retained.',
        'For b2=0, the nonempty pole pushdown rules out torsion canonical class and pulls back nontrivially under the known finite etale Hopf/Inoue cover. The curve-free Inoue case is excluded. Composing the Hopf universal covering C2 minus0 with that finite etale cover gives the exact universal covering of T0, identifying it as Hopf. The completed X9 statement applied to the same normalization and minimal resolution gives smooth minimal Hopf normalization and e(S)=0; the normalization Euler number is also0. Both target sentences therefore retain their full scope.',
        'The prefreeze program uses the Chern character with its finite-length contributions, quotient Chern classes, Riemann--Roch leading coefficient, polarization, canonical/adjunction pairing and the exact two chart Jacobians. The postrelease program independently expands the retained proof in formal bilinear products, checks every blowup coefficient and maximum, KV-V^2 invariance, the exact initial-completion remainder and strict-gap propagation. Both complete sources and outputs were read; all assertions pass. The specialized calculations and primary openings remain honestly dated after release. The precise missing bibliography entries and one printed-calculation Programs row are added. No theorem or proof error was found and no computational event is added.'
    ],
    chronology='Complete agent freeze08:14:57.354413 precedes release08:15:05.730225. Completed WV/WY/X9 and other supporting exposure is disclosed. Root full frozen-text reading precedes full original target reading, with prior agent status summaries acknowledged. The specialized initial completion and Favre source checks remain postrelease, and root contributes no independent event.',
    original_proof_items_preserved=7,
    original_displays_preserved=7,
    original_inline_formulas_preserved=50,
    semantic_labels_added=p['new_equation_labels'],
    mathematical_errors_found_in_original=[],
    publication_page_reading_credit=0,
    evidence=evidence,
)
assert not (R/review).exists()
(R/review).write_text(json.dumps(rd,indent=2)+'\n')
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:
    pages={x['tag']:x['page'] for x in csv.DictReader(f,delimiter='\t')}
target=dict(owner=t['statement_owner'],tag=t['tag'],old_page=pages[t['tag']],original=t['full_original_block'],proposed=t['proposed_full_block'],freeze=t['freeze_receipt'],release=t['release_receipt'],events=a['event_proposals'],guards=guards,who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort not separately exposed; checker ii_checks_a2',scope='Complete exclusion of positive-b2 class-VII minimal models for the stated possibly singular normalization, and smooth minimal Hopf/Euler conclusion in the remaining class-VII case.',event_note='Root full comparative review at '+now+'. All seven original steps and seven displays retained, with only two semantic display labels added. Fifty original inline formulas preserved. The general foliation derivation remains check evidence; all specialized Kato steps were verified after release. Two events in one group; no extra root or computational event.')
extra=[dict(old=g['literal_old'],new=g['literal_new'],type=','.join(g['defect_types']),owner='Bibliography',location='Bibliography',reason=g['reason']) for g in p['bibliography_guards']]
anchor=r'Quartic invariant and ruled-boundary Euler counts (\cref{cdp:st:C.2.RAT.2}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/S6_SERIES_PUBLISH_II_B2_CE_comparison_certificate.py}{\nolinkurl{S6_SERIES_PUBLISH_II_B2_CE_comparison_certificate.py}} \\[3pt]'
row=(R/a['program_rows']['path']).read_text().strip()
extra.append(dict(old=anchor,new=anchor+'\n'+row,type='D09',owner='Programs',location='Programs',reason='Add the standalone program for the retained class-VII initial completion. The prefreeze general-foliation program remains evidence without a printed row.'))
copies=[dict(**{'from':cp['output']},to='code/'+Path(cp['output']['path']).name) for cp in scope['new_computations']]
cfg=dict(batch=70,root_review_complete=True,source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],review_evidence=[bind(review)]+evidence,targets=[target],additional_source_edits=extra,code_copies=copies,mathematical_repairs=[],scope='02XA admitted after complete prerelease general-foliation derivation and full original/final seven-item comparison. The original intermediate-Kato proof, all seven mathematical displays and fifty inline formulas are preserved; two semantic equation labels are added. Eighteen owner guards, two missing primary bibliography entries in one insertion, and one Programs row. Two events in one evidence group. No mathematical correction, proof substitution, global defect closure or page-reading credit.')
assert cfg['source_before_sha256']=='42566030873b53d7308facf452ef07fd74d3c3d14d461c839a14d9d88e74060c'
assert cfg['ledger_before_sha256']=='6ff6f51c7c798f9b04c6acd31f64fb3b7ab11ff3288c53c7b9dbcaa9d6643694'
out='records/S6_SERIES_PUBLISH_II_continuation2_batch70_config.json'
assert not (R/out).exists()
(R/out).write_text(json.dumps(cfg,indent=2)+'\n')
print(json.dumps(bind(out)))
