from pathlib import Path
import json,csv,hashlib
base=Path(__file__).resolve().parents[1]
src=(base.parents[2]/'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15/S6_10_PAPERS_IV.tex').read_text()
a=src.index('\\begin{theorem}[Source result P3K.117');b=src.index('\\subsection{The original E6 source with both additive caps',a);body=src[a:b]
old=r'v^2=4u^3+3,\qquad q=t-t_c .'+ '\n'+r'\]'
new=old+'''
The lifted family is the fixed-$C_*$ continuation of
\\cref{night:P3K.116}:
\\[
 B_\\lambda(p,v_M)=\\bigl(p-G,\\lambda C_*qB_{8,1}(p)v_M\\bigr),
 \\qquad B_{8,1}=f_2^8\\frac{f_8\\circ t_{-G}}{f_8}.
\\]
The chronological tangent quotients and the single nonzero $C_*$
are those fixed by the prescribed initial source and Cartier frames.'''
pairs=[('fixed-family',old,new),
('orbit-locator-author','F8 five-sphere and fixed-pair classification','F7 five-sphere and fixed-pair classification'),
('orbit-locator-root','proved F8 fixed-pair hypotheses','proved F7 fixed-pair hypotheses'),
('orbit-locator-peer','The F8 fixed-pair result applies','The F7 fixed-pair result applies'),
('current-proof-state','This\nworking completion is awaiting full independent geometric audit\nbefore its reserved numbered export P3K.117.','The displayed source, point-line, cap, relative-connection and\nfan maps establish the asserted ordered-loop return in the stated\nfixed-scalar family.')]
patch=[]
for name,old,new in pairs:
    assert body.count(old)==1,(name,body.count(old));assert src.count(old)==1,(name,src.count(old))
    reason={'fixed-family':'Make the actual fixed-C_* K116 continuation explicit; no inferred disc extension of an independently varying directed map.','current-proof-state':'Current mathematical review closes this gate; preserve historical awaiting-review state in event/source records, not as an active claim inside the proof.'}.get(name,'F7 proves the orbit-pair classification; F8 is the subsequent Hopf-lift return construction. Use the exact direct locator.')
    patch.append({'id':'IV-K117-'+name,'statement_id':'night:P3K.117','operation':'replace_exact','old':old,'new':new,'reason':reason})
(base/'K117_patches.json').write_text(json.dumps(patch,indent=2)+'\n')
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family'
events=[
('independent re-proof','Statement-first source algebra, fourfold parameter map, kappa winding, collision separation and universal prism uniqueness frozen before proof arguments; complete geometric return excluded from prereading scope.','IV-K117-prereading'),
('targeted proof check','All five complete K117 arguments checked: actual trace, original height and point line, relative Chern caps, physical duality/inverse clutch, vertical and full-fan maps. Used F7/F8/F9/F55/F56/K68/GF/OR ingredients read at exact scopes in K117_REVIEW.md. Mathematical gate closed for ordered-loop fixed-C_* family.','IV-K117-complete-proof'),
('computation or formal certificate','Fresh post-proof program: 288 named checks, 217 independent nine-variable solves, 868 complete atom exponent round trips. Full source/Miller/conormal/determinant/quaternion/Chern/fifth-form/native-reset algebra checked; finite paths supplement the universal geometric and Euclidean proof.','IV-K117-fresh-code'),
('targeted proof check','Six primary PDFs reopened at exact cited theorem/orientation scopes: Gauniyal–Turchin2026, Némethi–Pintér2015, corrected Takase2005, Sakai2015v2, Haefliger1966, Kervaire–Milnor1963. Exact hashes retained. F7 direct locator repaired. No exhaustive priority claim.','IV-K117-primary-sources')]
eventpath=base/'events.tsv';existing=eventpath.read_text()
with eventpath.open('a',newline='')as f:
    writer=csv.writer(f,delimiter='\t')
    for kind,outcome,eid in events:
        if eid not in existing:writer.writerow(['night:P3K.117','2026-11-19',who,kind,outcome,eid,'S6_SERIES_GRIND'])
assess=base.parent/'row_assessments.json';data=json.loads(assess.read_text())
data['night:P3K.117']={
'confidence_state':'high_scoped_mathematical_gate_closed',
'confidence_line':'High confidence: complete K117 receiving proof closes for the positive ordered v-loop (four original-a turns), genuine M8 point line, fixed-C_* continuation, original order-one cap/full reference, every integral selected basis fan and every admitted fixed physical scalar. Initial physical pair (-6,0), native pair (0,-6), class -1; vertical and terminating all-fan formulae checked through exact maps.',
'independent_routes':['Statement-first source/parameter/collision/kappa algebra and universal prism derivation frozen before proof arguments; 50 named checks plus 1001 fan cases/7343 steps, at that partial scope.','Full post-reading geometric audit of all five proofs and used dependencies, including point/normal modules, both caps, relative line and tangent, physical inverse clutch and full fan maps.','Fresh Python/SymPy: 288 named checks, 217 independent nine-variable Gaussian solves and 868 atom coefficient round trips; no historical checker imported.','Fresh bounded reopening of six primary papers establishes the actual classical theorem/sign hypotheses; F7 direct locator repaired.'],
'remaining_risk':'No remaining mathematical continuation gate at stated scope. Classical smooth topology/theorem inputs and exact-arithmetic implementation remain trusted; no formal-assistant or different-family certification. Shorter original-a loops and independently varying line coefficients are not assigned a return by this row. Exhaustive priority comparison and global layout are separate.',
'format_check':'Exact keyed patches supplied in iv_os45/K117_patches.json for fixed-C_* family, three F7 locators and obsolete in-proof awaiting-review prose. Root owns application, bibliography and layout.'}
assess.write_text(json.dumps(data,indent=2)+'\n')
receipt={'statement':'night:P3K.117','patch_count':len(patch),'each_old_count_in_original':1,'fresh_output_sha256':hashlib.sha256((base/'output/k117_afterreading_exact.json').read_bytes()).hexdigest(),'fresh_code_sha256':hashlib.sha256((base/'code/k117_afterreading_exact.py').read_bytes()).hexdigest(),'review_sha256':hashlib.sha256((base/'K117_REVIEW.md').read_bytes()).hexdigest(),'row_assessment_written':True}
(base/'K117_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
