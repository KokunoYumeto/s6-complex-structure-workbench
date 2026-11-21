from pathlib import Path
import json, hashlib, csv, datetime, re

BASE=Path('/workspace/scratch/653608133b22/work/agents/i_provenance')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=BASE/'S6_SERIES_PUBLISH_I_common_family_guards.json'
g=json.loads(p.read_text())
evidence='eg:publish-iprovenance-common-family-editorial-'+g['source_sha256'][:16]
g['proof_reread_status']='Complete bounded comparison: all old affected proof/discussion blocks and all exact proposed changes were read; B3.1 and pushE1.2 were compared in full after consolidation. No independent derivation, applied-source verification or PDF reading is claimed.'
g['reread_completed_utc']=now
g['evidence_group']=evidence
p.write_text(json.dumps(g,indent=2,ensure_ascii=False)+'\n')

scopes={
'fam:src:B.1.1':'Complete quotient/Mordell--Weil proof read. Exponentiation and local logarithm inverse, pointed scaling, rational extension, cusp inverse, integral affine defects and MW generator argument are unchanged; only the attached-source phrase and map-description prose change.',
'fam:src:B.1.3':'Complete intersection/height proof read. Both blow-up systems, exact ab=X^4 map, all resolution charts/multiplicities, inverse Cartan matrix, canonical form and height projection are unchanged. Removed numerical-check narration and clarified retention of higher terms.',
'fam:src:B.1.4':'Complete divisor-section and reference-linearization proof read. Retained exact theta/divisor rigidification, finite/cusp orders, scalar-ratio transformation and signed section. Replaced Part C navigation by the explicit already established cusp branch; added actually opened Engel locators.',
'fam:src:A.4.1':'Complete Albanese and generic-recovery proof read. Product-isogeny/deck projection lattices and multiplication maps are unchanged. Derived the replacement Im(kappa1-kappa2)=-3 log(4/3)/(2 pi) directly from the definitions and ari:C.1.2, checked cancellation of 1/sqrt(3) and 3/2, and reread the two-real-circles argument with this exact nonzero value. Old cd_special_intervals enclosure is archived as a diagnostic, not used as a proof input.',
'fam:src:A.4.3':'Complete old proposition/proof and proposed numbered remark read. Preserved the countability argument, derivative example z->z^2, exact centralizer/first-column/norm substitutions and nonzero KS application. Primary Viaclovsky4.7 pp14--15 and Yang6.6--9/6.15/6.18 locators were opened separately; source opening adds no mathematical event.',
'fam:src:A.5.1':'Scope limited to the former poststatement rank-one model paragraph and its numbered IP09 replacement, not the parent-owned deferred theorem proof. Compared the quotient R=(P1 x C*)/<(gamma0 z,c0 v)>, boundary translation, local canonical quotient, ruled-surface cohomology (0,1,1), connecting-map source/target and full-unit/monodromy inputs. Explicit gamma0=gamma(0), beta0=beta(0), c0=lambda delta(0) is the primary equation3.1 dictionary; no evaluation of the connecting map or new classification is asserted.',
'fam:src:B.2.1':'Complete seven-step arbitrary-data proof read. Kept the exact norm equation, parity, generic-component toric character map, clockwise cusp-defect equality p\'=ap, adjustment of the second residual coordinate, holomorphic torsor correction, essential-singularity collar data, and inverse gluing. Replaced defensive prose by these existing positive scopes.',
'fam:src:B.2.2':'Complete two-class and marking proof read. Replaced the repeated P_E matrix and its already established intertwining calculation by P_E=P_mark with the exact earlier proposition; retained P_E epsilon, epsilon-prime, psi and circle identities, both complex-linear period maps, inverse-generator signs and positive-u-circuit permutation.',
'fam:src:B.2.3':'Complete two obstruction proofs read. Retained the nonzero order-two root-quotient class, non-even Albanese Laurent coefficient, local logarithm families and global double-cover family; changed title/source-history wording only. The same fixed-sphere logarithmic datum and morphism u=w^2 remain.',
'fam:src:B.3.1':'Read both complete pre-consolidation proofs and the full combined proof. Retained intrinsic base recovery, repeated norms, primitive sphere relation, all class counts and cyclic action. Imported the unique exact ell_j, b_j, normalized-root maps, cusp translation and unit maps, enlarged-root invariant coefficients and H1=0 gluing from pushE1.2. Explicit local identification alpha=a, h=n and covering m,n=m1,m2 preserves every formula; local translation is named mathcal A_j and unit u(t_c) to avoid collisions. Repeated necessity arguments remain at their original B2.1/A2.1 suppliers. Five-pair adjacent_exact corroboration moves to records.',
'push:src:E.1.1':'Complete integral dictionary proof read. Preserved P_V=Q_E^-1 P_mark, determinant, both monodromy conjugacies, all invariant-vector transports, affine inversion and p=-b. Clarified the literal quotient map v_i -> v_i+m_i lambda, which leaves [v_i/m_i] unchanged; removed diagnostic filename and source-reading narration.',
'push:src:E.1.2':'Read both complete old classification proofs and the exact replacement. Unique construction data move to B3.1. The receiving proof retains r1=N0,s1=-rho0,r2=N1,s2=-(rho1+N1),p=-b; reduction modulo4l cancels N1\'-alpha N1 and yields the stated congruence. Base, parameter and positive-circle conclusions transfer through this explicit P_V map.',
'push:src:E.1.3':'Complete family-comparison proof read. Rational/integral vectors now cite their relocated B3.1 proof; product sheaf, vanishing H1, exact W=(-1)^s2 w, connected automorphism transition isotopies and monodromy conjugacy proof remain unchanged.'
}
record=BASE/'S6_SERIES_PUBLISH_I_common_family_reread.md'
lines=['# Paper I common/family editorial reread','',f'Completed: {now}',f'Source snapshot: `{g["source_sha256"]}`.',f'Evidence group: `{evidence}`.','',
'This is an exposed-source comparison. It contributes only used-and-rechecked associations. The full old/new blocks, exact guards and diff are retained. No PDF page was certified, and no new independent, targeted or computation check is claimed.','',
'## Scope and redistribution','']
for k,v in scopes.items():lines+=['### '+k,'',v,'']
lines+=['## Preservation checks','',
'Every old label and hypertarget in a replaced block is present in its replacement. The deferred `app:rederive:fam-src-A.5.1` span was neither edited nor reread under this record. IP09--IP11 number existing mathematical material; no independent credit follows from adding those wrappers. Pure title/accent edits in B1.2 and A1.2 and the two definition wrappers produce no mathematical rows.','',
'The removed standard/tangent re-derivation navigation and post-E1.2 return-history paragraph remain in the guarded old text and comparison JSON. The repeated P_E matrix is supplied by `inv:B1.0`; its unique fixed-vector and complex-period applications remain in B2.2.','',
'## Proposal validation','',
'The transformation script asserts a unique source match for each guard and preservation of all pre-existing statement/equation labels and tags. During draft review, a broad symbol substitution was caught before delivery; the final proof instead declares alpha=a and h=n explicitly and changes only the covering-degree names. The draft was regenerated and the entire combined proof reread. This was an editorial draft correction, not a defect in the receiving mathematical statement.','']
record.write_text('\n'.join(lines))

header=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group']
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH/provenance_inventory'
out=BASE/'S6_SERIES_PUBLISH_I_common_family_CHECK_EVENTS.tsv'
with out.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=header,delimiter='\t');w.writeheader()
 for i,(sid,scope) in enumerate(scopes.items(),1):
  w.writerow(dict(statement_id=sid,date='2026-11-21',who=who,type='used and rechecked in this run',outcome=scope+' Scoped editorial comparison; no independent proof credit.',event_id='ce:publish-iprovenance-common-family-'+re.sub('[^A-Za-z0-9]+','-',sid),phase='S6_SERIES_PUBLISH_I_editorial_reread',source_file=str(record),source_row=i,source_event_type='used and rechecked in this run',evidence_group=evidence))
receipt=dict(source_sha256=g['source_sha256'],guard_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),completed_utc=now,evidence_group=evidence,event_associations=len(scopes),declared_evidence_groups=1,independent_credit=0,rendered_page_credit=0,scopes=scopes,pure_metadata_subjects_excluded=['fam:src:B.1.2','fam:src:A.1.2','I:def:higher-multiplicity-coordinates','I:def:residual-cusp-defect'])
(BASE/'S6_SERIES_PUBLISH_I_common_family_reread_receipt.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'guards':len(g['changes']),'used_and_rechecked_associations':len(scopes),'evidence_group':evidence,'guard_sha256':receipt['guard_sha256']},indent=2))
