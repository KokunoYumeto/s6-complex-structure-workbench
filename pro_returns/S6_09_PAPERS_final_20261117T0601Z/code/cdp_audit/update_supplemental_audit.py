"""Publish only the working/INV proofs actually followed in this writing run."""
from pathlib import Path
import csv, hashlib, json, re
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'work/cdp_audit'
SOURCES = ROOT.parent/'sources'
PROVENANCE='GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, writing run; 17 November 2026 UTC'
rows=json.loads((OUT/'working_edition_inventory.json').read_text())
scopes={
'prop:missing-cotangent-filtration': ('CDP A.1.1','same filtration, earlier separate labelled statement','Conormal kernel and torsion quotient exact sequences followed.'),
'prop:missing-global-section-criterion': ('CDP A.1.1','same exact criterion, separately labelled in source','Long exact sequence and injectivity of the connecting map followed.'),
'lem:conormal-injective': ('CDP A.1.1','full local reduced-Cartier proof retained','Local reduced-Cartier non-zero-divisor and conormal map followed.'),
'lem:conductor-square': ('CDP A.2.2','normalization–conductor square proof retained','Exact fibre-product conductor square and dual differential consequence followed.'),
'prop:conductor': ('CDP A.5.1','more explicit hypotheses in working edition retained','Gorenstein finite duality, torsion injection and normalization-trivial twist followed.'),
'prop:nodal-counterexample': ('CDP B1','CDP B1 strengthens the range of extending gluing parameters','All normalization sections, cohomology and actual line-bundle extension followed.'),
'thm:cartier-duality': ('','retain as foundational result with full proof','Every Cartier thickening, dualizing line and absolute cohomological duality followed; original analytic duality theorem opening still pending.'),
'prop:cartier-duality-absolute': ('','retain the explicit absolute formulation','Compact Cartier Gorenstein duality and reduced fibre comparison followed; RR70 original theorem opening pending.'),
'lem:curve-flatness': ('','retain the automatic-flatness lemma','Properness, torsion-free DVR modules and non-zero-divisor fibre equation followed.'),
'prop:analytic-base-change': ('','retain exact analytic finite-complex input','Precise flatness and base-change hypotheses read and used correctly; original BS76 theorem opening remains pending.'),
'cor:surface-top-base-change': ('','retain top-degree specialization consequence','Top cohomology, Nakayama and constant-zero base-change argument followed; depends on previous analytic finite-complex result.'),
'prop:pic0-pullback': ('','retain weaker-hypothesis Pic0 argument','Topologically trivial pullback and normalization H¹(O)=0 followed.'),
'prop:all-pic-restriction': ('','retain obstruction formulation','Exact all-Picard restriction criterion followed; distinguishes topological vanishing from the Pic0 statement.'),
'prop:leray-edge-restriction': ('','retain as first proof of global all-Picard restriction','Integral Leray edge, local specialization and normalization restriction followed; upstream topology is an explicit dependency.'),
'lem:picard-crossed-defect': ('','retain explicit crossed-defect computation','Actual logarithmic factor cocycle and d1+T1 d2+T1T2 d0=0 followed.'),
'lem:picard-finite-norm': ('','retain finite-cover norm computation','Clockwise logarithmic lift with translation +v, central extension and norm N_T d=iota_v E followed.'),
'lem:picard-cusp-defect': ('','retain cusp filling and specialization computation','Solid torus u=t/(x1x2), x1=1, |u|=rho, |x2|<=1 and its oriented boundary followed.'),
'prop:direct-boundary-picard': ('','retain second global restriction proof','For E=2nq the coinvariants 4n delta and -3n delta force n=0; local integral specialization and Pic0-triviality followed.'),
'cor:candidate-pic0-route': ('','retain the explicit no-topology Pic0 route','Conductor ambient-section mechanism with normalization Pic0 triviality followed.'),
'thm:candidate-conductor': ('CDP A.4.1','retain exact abstract hypotheses and resulting conductor obstruction','All four geometric hypotheses, ambient cotangent section and full-fibre duality followed.'),
'cor:candidate-conductor-actual': ('CDP A.4.1','application retained with construction dependency explicit','Application to the supplied constructed threefold followed; this does not independently validate the entire construction.'),
'lem:semidirect-abelianization': ('CDP D.1.1','same group identity; Paper I source concordance','Abelianization by the action commutators and splitting followed.'),
'lem:cdp-generic-endpoints': ('','retain in corrected global criterion','Finite-dimensional decreasing sections and Serre-dual generic endpoint vanishing followed.'),
'thm:corrected-cdp-global': ('','retain exact extra H²-vanishing hypothesis','Picard vector group, one H²-vanishing twist, generic endpoint vanishing, semicontinuity and HRR c3<=0 followed.'),
'cor:corrected-cdp-relative': ('','retain genuine sufficient relative condition','Projection formula, R²=0 and positive base twist give one H²-vanishing twist; global criterion then applies.'),
'thm:corrected-cdp-fibrewise': ('','retain exact reduced-fibre repair with connecting map','Two endpoint vanishings plus injectivity of delta, absolute Gorenstein duality and top-degree base change followed; nonreduced layers remain a separate requirement.'),
'test:cdp-comparison': ('','retain as program-status consequence, not a new theorem','Read the complete test and its stated dependence on global construction/topology and the corrected criterion; not an independent proof of the construction.'),
'lem:torsion-identification': ('CDP A.1.1','same local torsion identification, earlier explicit lemma','Localization at generic points and kernel of pullback to normalization followed.'),
'lem:conormal': ('CDP A.1.1','same local left exactness, earlier separate lemma','Reduced-Cartier local conormal injection proof followed.'),
'prop:filtration': ('CDP A.1.1','same filtration, earlier labelled statement','Both short exact sequences followed.'),
'prop:criterion': ('CDP A.1.1','same exact criterion, earlier labelled statement','Connecting homomorphism and exact H0 criterion followed.'),
'lem:conductor': ('CDP A.2.2','earlier conductor-square proof retained','Normalization–conductor exact sequence followed.'),
'prop:conductor-differential': ('CDP A.5.1','retain explicit conductor criterion','Duality comparison and canonical-section ambient injection followed.'),
'cor:normal-crossing-kernel': ('CDP A.2.1','retain normal-crossing specialization','Explicit simple-normal-crossing kernel and conductor line calculation followed.'),
'prop:family-geometry': ('CDP B1','earlier explicit nodal family retained','Smooth total space, nodal central cubic and elliptic nearby fibres followed.'),
'lem:gluing-bundle': ('CDP B1','specific non-torsion gluing construction retained','Degree-zero line bundle on nodal normalization and gluing ratio followed.'),
'lem:extending-gluing': ('CDP B1','explicit earlier choice; B1 extends every lambda','O=[0:1:0], P=[3:sqrt(36+t):1], rational normalization function with gluing ratio 1/3 followed.'),
'thm:nodal-test': ('CDP B1','same endpoint defect with explicit extension','Full table and extending twist followed; refutes a local implication, not by itself the global theorem.'),
'lem:generic-endpoints': ('WORKING prop:cdp-generic-endpoints','same proof with matching hypotheses','Full generic endpoint proof followed; source label in cdp_program is lem:cdp-generic-endpoints.'),
'thm:corrected-global': ('WORKING thm:corrected-cdp-global','same global repair; retain source concordance','Full corrected global criterion followed, with the essential existence of one H²-vanishing twist.'),
'cor:relative': ('WORKING cor:corrected-cdp-relative','same relative sufficient condition','Full Leray and positive-base-twist argument followed.'),
'prop:relative-local': ('','retain all three module examples','xy and xyz relative differential modules: torsion-free, rank two, three minimal generators; t=s^m torsion R/(s^(m-1)) ds. UFD syzygy arguments followed.'),
'prop:local-cusp-picard-obstruction': ('','retain genuine local nonzero counterexample','Full integral support divisor, automorphy factors and exact descent cocycle followed; program rerun. Normalization degree vector (-12,2,0,-12,2,0) and generic c1=-2q confirmed. Schnell cocycle convention opened.'),
'prop:analytic-ah-boundary': ('','retain independent analytic boundary-cocycle argument','Full logarithmic factors, real pushout central extension, typed quotient square, endpoint lifts, finite norms, cusp solid-torus filling and branch independence followed. Original analytic/cohomological foundations tracked separately.'),
'lem:analytic-support-specialization': ('','retain support-function specialization replacing integral topology','Full quadratic support function, Stein toric charts, zero horizontal winding, residual factors and E=-B(B0 lambda,m) followed; program rerun.'),
'thm:analytic-all-picard': ('','retain third global restriction proof, distinct dependence','Full coinvariant norm calculation d1=2k delta, d2=-3k/2 delta, d0=0 forces k=0; support-function lemma then trivializes normalization restriction. No parity assumption or integral-specialization theorem used.'),
}
for r in rows:
    taken,distinct,scope=scopes[r['source_id']]
    r.update(taken_over_by=taken,distinct_proof=distinct,own_check=PROVENANCE+': '+scope,
             check_outcome='full displayed argument followed; dependencies as specified',
             notes='Preserve exact source label and all hypotheses. No published-source or upstream global construction verification is implied by this local argument check.')
    if r['source_id']=='test:cdp-comparison': r['check_outcome']='consequence/status statement read; no separate proof claimed'
    if r['source_id']=='lem:semidirect-abelianization': r['paper']='I'
    if r['source_id']=='lem:generic-endpoints': r['taken_over_by']='WORKING lem:cdp-generic-endpoints'
(OUT/'working_edition_inventory.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
with (OUT/'working_edition_inventory.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

file=SOURCES/'returns/S6_01_INVARIANTS/fragments/part_E.tex'
text=file.read_text();matches=list(re.finditer(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}',text))
scopes_inv={
'E1.1':('Full proof followed: actual miniversal parameter, relative canonical root identity, complete |-2K| pencil and Kähler-fibre meromorphic descent.', 'INV D3.1 and D1.2; parent audits these dependencies.', 'Related to CDP E1 and family miniversality; retain precise anticanonical pencil statement.'),
'E2.1':('Full displayed derivation of degrees, splitting alternatives, determinant cup product and Leray dimensions followed; corresponding original supplied combs theorem and exact labelled passages opened.', 'Viaclovsky combs source t:main, allfree, degrees, localquotient, degreechange, initial bundles and smoothingbound matched; full earlier construction remains a dependency.', 'Known result; do not relabel as new. Source establishes these sheaves and h(O), and only an8m-8 lower bound on local deformation dimension.'),
'E2.2':('Entire proof followed: root bundle characters, Hodge equations, cusp cup-product map, tangent direct-image modification, cohomology and K_m residue formula.', 'INV E2.1; CDP E15; root-period and cusp normalization construction.', 'Tangent dimensions match CDP E15; exact Hodge formulas with h0(K_m) are additional retained content.'),
'E2.3':('Open-status statement read and compared with later CDP E15.', 'CDP E15 full displayed proof followed in this run.', 'Split the stale combined status: later E15 gives the smooth reduced Kuranishi germ; individual K_m splitting and resulting explicit Hodge numbers remain unresolved unless another source resolves them.'),
'E2.4':('Full conditional-refutation proof followed; original HKP2000 preprint p.2 Corollary 1.3 and its proof opened.', 'INV E2.2: h0(T)=2m+1>=25; parent verifies full construction/topology.', 'Refutes the unrestricted h0(T)<=2 statement with these examples; does not refute the a=0 bound or independently settle almost homogeneity.'),
}
out=[]
for i,m in enumerate(matches):
    end=matches[i+1].start() if i+1<len(matches) else len(text)
    block=text[m.start():end];dst=OUT/'extracted'/('INV_'+m[1].replace('.','_')+'.tex');dst.write_text(block)
    scope,dependencies,notes=scopes_inv[m[1]]
    out.append(dict(source_run='S6_01_INVARIANTS',source_id=m[1],source_status=m[2],source_title=m[3],
        canonical_file=str(file.relative_to(ROOT.parent)),canonical_line_start=text.count('\n',0,m.start())+1,
        canonical_line_end=text.count('\n',0,end)+1,extracted_file=str(dst.relative_to(ROOT.parent)),
        proof_sha256=hashlib.sha256(block.encode()).hexdigest(),paper='II',printed_label='',
        own_check=PROVENANCE+': '+scope,check_outcome='full displayed proof followed; dependencies explicit' if m[1]!='E2.3' else 'open-status statement reconciled with later result',
        depends_on=dependencies,recorded_checks='',notes=notes))
(OUT/'invariants_part_E_audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
with (OUT/'invariants_part_E_audit.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
print('Published',len(rows),'working-edition records and',len(out),'INV Part E records.')
