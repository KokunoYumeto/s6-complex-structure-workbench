import datetime
import hashlib
import json
from pathlib import Path

H=Path(__file__).resolve().parents[1]; W=H.parent
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
fm=json.loads((H/'frontmatter_II_map.json').read_text())
front=(H/'frontmatter_II.tex').read_text()
changes=[
('A',3,
 'Transgression gives unitary\ninfinite-order twists on every fibre support; the canonical\ninjection of twisted torsion-free forms into local-system\ncohomology gives their vanishing',
 'Transgression gives unitary\ninfinite-order twists on every fibre support. The explicit\nfibre-group calculation and neighbourhood comparison make\ndegree-one local-system cohomology vanish. The canonical\ninjection then kills the twisted torsion-free forms',
 'A.4.9 Steps2-7 calculate the zero target before applying A.4.7; injectivity alone does not imply vanishing.'),
('C',5,
 'support. The Gauduchon degree and conductor calculation makes\nits normalization geometric genus zero; vertical resolution\npreserves that property on all components.',
 "support. The finite \\'etale root cover, twisted cotangent\ncomparison and Cartier-layer filtration exclude this obstruction\non a smooth support. For a singular support, Gauduchon degree\nand the nonzero conductor make its normalization have geometric\ngenus zero; vertical resolution preserves that property on all\ncomponents.",
 'D.2.5 Step2 first excludes a smooth support as the persistent obstruction by the literal root equations w^m=u, s=wz and finite cyclic invariants; its later conductor argument concerns the singular nonnormal branch.')
]
guards=[]; map_updates=[]
for letter,n,old,new,reason in changes:
    assert front.count(old)==1,(letter,front.count(old))
    step=next(m for m in fm['main_theorems'] if m['letter']==letter)['steps'][n-1]
    assert step['claim_tex'].count(old)==1
    guards.append({'target':'audit_sign/frontmatter_II.tex','label':f'series:II:{letter}',
                   'old_text':old,'new_text':new,'expected_count':1,'reason':reason})
    map_updates.append({'letter':letter,'step':n,'old_claim_tex':step['claim_tex'],
                        'new_claim_tex':step['claim_tex'].replace(old,new)})
g={'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'frontmatter_sha256':sha(H/'frontmatter_II.tex'),'map_sha256':sha(H/'frontmatter_II_map.json'),
   'guards':guards,'map_updates':map_updates,
   'scope':'Two outline clarifications. No theorem hypothesis/conclusion or body proof changes. Root integration only; this script does not mutate receiving frontmatter.'}
(H/'II_main_outline_guards_07.json').write_text(json.dumps(g,indent=2)+'\n')

notes={
'A':[
'The generic-point injection is valid because the hypersurface is reduced; the preimage of torsion and two long exact sequences yield exactly ker(delta_A), with both endpoint vanishings retained.',
'The normalization parameter identifies precisely u=1 and u=-1. Multiplication by 1-lambda is invertible for lambda!=1, whereas the torsion preimage is the pushforward of the trivial normalization line. The product projection to P1 retains the ambient one-dimensional section.',
'A.4.9 uses the actual torus Koszul complexes, finite-cover transfer, central-extension spectral sequence and Inoue mapping-torus eigenvalues; actual smooth-fibre transport and neighbourhood restriction then give H1=0 on every support. A.4.7 injects into that zero target. Proposed wording makes the target calculation explicit.',
'C4f retains every full Cartier multiplicity, uses the fixed critical-fibre persistence argument, and measures the actual pullback Pic(Y)->Pic(T_S). Only irreducible nonnormal critical supports enter the criterion; the zero map produces persistence for every L.',
'E12 uses the normalized Poincare line and the actual projection plus H1(P1,O(-2)); the result is a length-one R2 at the origin. E17 retains the associated-component hypotheses needed to exclude sections supported away from D.'],
'B':[
'The punctured base has free fundamental group, so lifts of its chosen generators split the extension. Its abelianization retains integral coinvariants. The compact-support sequence gives r=2g+s-1+tprime-b1 under b2=0; integral H1/H2 cohomology vanishings also force the indicated coinvariant quotient to be free.',
'Adjunction restricts KY to the fibre, the ambient rational H2 vanishing kills its rational first Chern class, and the divisor Riemann-Roch calculation gives c2=chi(O)=0. The intermediate necessary list is not substituted for the final exclusions.',
'The named exclusion statements apply to the exact algebraic-reduction and rational-Betti hypotheses. The algebraic-dimension-zero qualification modifies the surviving Hopf fibres; a general torus is not asserted to have algebraic dimension zero.',
'C.3.6 realizes both primary and secondary Hopf cases through the displayed quotient maps. D.2.7 realizes an abelian general fibre with its actual three-piece filling, so the surviving list has the stated realization scope.'],
'C':[
'Connected-fibre Leray injects base H1 and gives P1. P4.58 retains arbitrary singularities and multiplicities for the irreducible classification; MH2 supplies the stated normal-crossing triple count. The rational-normalization branch has Euler2, while each other irreducible branch has Euler0.',
'The divisor comes from an actual adjacent component pulled through the normalization-resolution map, so its rational Chern class is zero by H2(Y;Q)=0. INT1/2 retain that hypothesis and use the explicit interface vanishing sphere to exclude the Enoki possibility.',
'INT3 explicitly includes H2(Y;Q)=0, in addition to the INT2 hypotheses. Its conductor branches and blowup contributions are nonnegative; equality imposes smooth minimal normalizations and unramified elliptic conductor maps, with the original full-fibre multiplicities retained.',
'Euler additivity over the finite exceptional base set gives the sum of support Euler numbers. Poincare duality gives e(Y)=2-b3; the skew nondegenerate middle pairing makes b3 even. Nonnegativity leaves exactly0 or2. The actual body route uses P4.36 for the Hopf input, not an inferred use of UN1 parity.',
'D2.5 needs only rational b1=b2=0. Its smooth persistent-obstruction branch is excluded by w^m=u,s=wz, local-system transport, conormal/Cartier layers and exact cyclic invariants. The remaining singular support is nonnormal; Gauduchon degrees and the nonzero conductor give pg=0. Vertical resolution and D2.3 logarithmic periods contradict identity monodromy. Proposed wording restores this branch order.',
'D2.7 has fixed abelian general fibre E x E and identity monodromy. Its three reduced SNC exceptional fibres have primary Kodaira and Hopf components meeting elliptic curves, without triple points; its integral Mayer-Vietoris maps give H1=H2=0 and Euler0.'],
'D':[
'The full tube retracts onto the actual reduced support, and its boundary is the nearby torus mapping torus. Pair duality yields the displayed semi-characteristic parity without ambient compactness or Betti-number assumptions.',
'Wang reduces that parity to the kernel of wedge2(T)-I. The preserved wedge pairing and determinant/Cayley argument give even kernel dimension. UN1 retains its unresolved historical before-reading-order completion gate despite this receiving comparison.',
'The exceptional projective bundle replaces the actual centre, giving (r-1)e(C). A point contributes+2; a genus3 plane quartic in its exceptional plane contributes-4, hence a two-operation decrement2. These modifications are supported over the chosen base point.',
'Normalization strict transforms are related by the actual birational maps and retain the base-function valuation, hence the original multiplicity. New exceptional surfaces are projective bundles over a curve or rational, so the non-uniruled multiset is transported through those maps.',
'The projective construction uses genus2 centres and disjoint point blowups, producing2(m-k). Its total space remains smooth and projective; it does not assert preservation of the b2=0 hypothesis of Theorem C.'],
'E':[
'The root characters are r1=n mod3 and r2=3n mod4; the four degree shifts and the mod3 finite-root term match C5b exactly. The fixed source, physical line and period normalization are retained.',
'P1 line cohomology gives the displayed four dimensions. The cusp map has rank1 exactly when u(n+6)>0, namely n=-6,-3,-2 or n>=0; at n=-1 the source is one-dimensional but the map is zero. The new universal residue certificate checks every integer, rather than a bounded sample.',
'C5c uses the actual translation-character complex, its regular resonance modules, and the exact order3/order4 root characters. The formulas for ell1 and ell2 retain their distinct congruence and nonzero-k conditions.',
'The proper direct-image support makes the regular resonance set finite. The cusp contributes one reduced degree2 skyscraper and the stated nonzero map. The resulting tuple(0,J,1+J,0) has persistent H2 and Euler1.',
'The actual identity-induced degree6 isogeny fixes the period matrix. Substitution of the heat equation, eta derivative and hprime=-wp-pi^2 E2/3 gives the printed determinant with its Weierstrass term; the branch equation is required before its removal. Root coordinate changes retain the squared derivative factor.'],
'F':[
'The displayed boundary map is the actual cup map (a,b)->b u1-a u2. Rank2 of the two classes gives injectivity and the stated first-order map result; the all-orders assertion is supplied separately by E6.',
'E6 includes all Artin orders and the relative graph construction for the analytic germ, with connected torus fibres and the stated algebraic dimension. The outline does not substitute the first-order E5 statement for this stronger input.',
'E13 and E14 use their own root-curve cohomology and actual two-parameter sections. Each tuple(1,2,2,0) has Euler1; neither proof is credited as an application of the standard-family C5b/C5c formulas.',
'E15 is restricted to the constructed positive combs m>=12. The actual period-family tangent map is an isomorphism, which makes the Kuranishi ideal zero. This leaves the separate rank3 K_m splitting problem inv:E2.3 open.',
'E2.23 retains its connected reduced analytic base and fixed ordered-pair hypotheses. Disc propagation and finite curve projections supply both openness and closedness, hence separation through finite chains.',
'E2.24 uses the actual Kuranishi retraction and the specified diffeomorphism action to transport the same ordered-pair separation to the stated smooth topology and quotients. No extra quotient or topological equivalence is inferred.'],
'G':[
'The scalar is literally alpha=c u in the fixed normalization. The four lattice columns and affine fourth-root shift retain the marked half-period and kappa, with4kappa integral.',
'The projection to eta induces the actual Albanese lattice(1/2)Z+(tau/4+kappa)Z. The u-turn takes Q to-Q and the exact leading j term gives Q(j(Q)-j(-Q))->2, excluding a biholomorphism of these reduced fibres.',
'The divisor argument under H2(Y;R)=0 makes the torus map the intrinsic meromorphic reduction; an endpoint must preserve its unique multiplicity4 fibre. This connects the previous fibre invariant to every possible threefold endpoint.',
'The source translation, rational square root, retained cusp fan and cap commutators give an actual two-turn endpoint whose two-step norm is the prescribed one-gamma gluing. Both quotient maps u=w^2 and w=r^2 are retained. Full live proof pages403-407 were viewed after all four headings were repaired.']}
records=[]
for m in fm['main_theorems']:
    assert len(notes[m['letter']])==len(m['steps'])
    for step,note in zip(m['steps'],notes[m['letter']]):
        records.append({'main':m['letter'],'step':step['number'],'anchor':step['anchor'],
                        'body_targets':step['body_targets'],'used_conclusion_and_scope':note,
                        'result':'matches body with proposed outline clarification' if (m['letter'],step['number']) in [('A',3),('C',5)] else 'matches body at recorded receiving scope'})
consistency=[
 {'pair':'A/E','map':'Under integral CDP, Pic(Y) is the connected vector space H1(O_Y). Its actual pullback to the discrete Picard group of the rational dP6 normalization is zero. C4f therefore gives persistent H2 for every twist. The universal residue calculation proves h2>=1 for every integer n, and C5c gives1+J for nonintegral z.'},
 {'pair':'C/D','map':'For each smooth centre of complex codimension at least2, the actual blowup cohomology decomposition is H2(Bl_Z Y;Q)=pi*H2(Y;Q) plus H0(Z;Q). A point followed by the connected plane quartic adds two independent exceptional classes while changing the support Euler number by-2. The punctured-family identification thus coexists with the loss of the ambient b2=0 hypothesis.'},
 {'pair':'C equality / B realization','map':'D2.7 has identity monodromy, general E x E, primary Kodaira/Hopf components and unramified elliptic intersection maps. Its three SNC supports have no triple points, so their Euler numbers vanish; the actual integral Mayer-Vietoris calculation gives the Betti hypotheses and b3=2.'},
 {'pair':'E/F','map':'The standard E source has multiplicity3 and4 root fibres. The E13 source y^2=x^3+t x+mu t+1 with P=(-mu,b), b^2=1-mu^3 has three distinct nodal values and only the order4 root at infinity; the E14 displayed coordinate transformation produces y^2=x^3+t x+t and its stated deformation. A biholomorphism of these algebraic-dimension-one threefolds induces an isomorphism of their meromorphic function fields and hence a Mobius map of the bases, preserving the Cartier multiplicities. This actual map would preserve both multiplicity3 and4, so it cannot identify the specified standard member with either stated one-order4 family. Their different tangent tuples are therefore consistent in the exact source scope.'},
 {'pair':'E/F Euler','map':'The new certificate proves the integral E tuple has alternating sum1 for every integer through all12 residue classes and every affine region; the nonintegral tuple has sum1. Both two-parameter tuples and the comb tuple(2m+1,8m+1,6m+1,0) also have sum1.'},
 {'pair':'G / smooth-class correction','map':'The parameter proof retains the actual source/period/cap norm maps. K36 is separately a refuted smooth-class assertion with numerical correction26 versus historical0; this branch retains its precise arithmetic/LR comparison scope and does not claim a fresh complete K74/K105 geometric proof.'}
]
report={'date_utc':g['date_utc'],
 'reviewer':'GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; same current model family.',
 'exposure':'Targeted global receiving comparison. This branch wrote these outlines and had already read the recorded source/proof scopes. The frozen plan is II_main_global_review_plan_06.md. All35 outline steps were compared against their40 distinct linked targets. The broader statement packet contains42 distinct targets, including statements linked by the main theorem outside its outline. This is not a fresh blind re-proof of those42 full proofs. Current full-proof scopes and retained before-reading receipts remain separately recorded.',
 'frontmatter_sha256':sha(H/'frontmatter_II.tex'),'map_sha256':sha(H/'frontmatter_II_map.json'),
 'linked_body_sha256':sha(W/'parts/II.body.linked.tex'),
 'statement_packet':'II_main_linked_statements_07.json','statement_packet_sha256':sha(H/'II_main_linked_statements_07.json'),
 'outline_steps':records,'special_case_morphisms':consistency,
 'dependency_edges':json.loads((H/'frontmatter_II_dependency_edges.json').read_text()),
 'new_computation':'II_global_outline_identities_07.json','new_computation_sha256':sha(H/'II_global_outline_identities_07.json'),
 'proposed_guards':'II_main_outline_guards_07.json','proposed_guards_sha256':sha(H/'II_main_outline_guards_07.json'),
 'remaining_scope':'Global outline consistency passed with the two proposed clarifications. This does not close seven main inventory rows: each imported row keeps its exact existing reading-order, external-source, computation and layout gates. UN1 before-reading order and the rank3 comb splitting remain explicitly unresolved at their stated scopes; the K36 full geometric source checks are not newly claimed.'}
(H/'II_main_global_outline_comparison_07.json').write_text(json.dumps(report,indent=2)+'\n')
lines=['# Paper II: complete seven-main-outline receiving comparison','',report['exposure'],'',
       '## Outcome','',report['remaining_scope'],'',
       'Two minimal guards make A3 name the zero local-system target and C5 retain the smooth-support exclusion before the nonnormal conductor branch. Both body proofs already contain these steps; no main mathematical conclusion changes.','']
for m in fm['main_theorems']:
    lines += ['## Theorem '+m['letter']+': '+m['title'],'']
    for r in [r for r in records if r['main']==m['letter']]:
        lines += [str(r['step'])+'. '+r['used_conclusion_and_scope']+' Targets: '+', '.join('`'+x+'`' for x in r['body_targets'])+'.','']
lines+=['## Special-case comparisons through exact maps','']
for c in consistency:lines += ['### '+c['pair'],'',c['map'],'']
lines+=['## Main-conclusion dependency','',
        'The retained B-to-A edge uses C.3.1 in A.4.9 and C4e, then C4f. The actual used conclusion is the smooth-fibre surface list. No additional edge is added merely from a shared input. In particular E13/E14/E15 calculate their own tangent cohomology rather than invoking C5b/C5c; D2.5 uses intermediate sheaf lemmas with rational Betti hypotheses rather than the full integral C4f criterion; and G does not use F\'s Kuranishi or retention conclusions. Absence of an asserted edge is not a claim of mathematical independence.','',
        '## Exact new certificate','',
        'The newly written program partitions n=12k+r into all12 residues and every affine region of the maxima in u and v. It proves the Euler identity, persistent H2 and exact cusp-rank threshold for all integers, checks both distinguished tuples, the nonintegral and comb Euler identities, and the exact theta determinant. The initial singleton-region comparison failure is preserved with its corrected evaluation rule. The program was written after the formulas were read and receives computation credit only.','',
        'Evidence files: `II_global_outline_identities_07.json`, `II_main_outline_guards_07.json`, `frontmatter_II_dependency_edges.json`, `II_main_linked_statements_07.json`, and the per-row exact evidence map.','']
(H/'II_main_global_outline_comparison_07.md').write_text('\n'.join(lines))
print(json.dumps({'steps':len(records),'distinct_targets':len({v for r in records for v in r['body_targets']}),
 'report_sha256':sha(H/'II_main_global_outline_comparison_07.json'),
 'guard_sha256':sha(H/'II_main_outline_guards_07.json'),
 'computation':json.loads((H/'II_global_outline_identities_07.json').read_text())['checks']},indent=2))
