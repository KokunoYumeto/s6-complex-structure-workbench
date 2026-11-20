"""Build scoped proposals from checked V records; never edit shared sources/inventory."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re

root=Path(__file__).resolve().parents[2]
own=root/'audit_corrections'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
actor='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed), S6_SERIES_GRIND/corrections_audit'
old_rows={r['label']:r for r in csv.DictReader((root/'S6_SERIES_GRIND_inventory.csv').open())}
credit={}
searches=('Current bounded corpus and literal searches: audit_corrections/V_literature_searches.tsv '
          '(V-L01–V-L12), V_literature_comparison.tsv/report; AC26 original PDF §§3–8, '
          'E26 received §2 and its stated degeneration discussion, DGKX v1 §§2/6/7 and v2 §§2–3, '
          'plus the exact operative classical sources named in this row. Retained historical '
          'source events remain at their recorded scope; this consolidation does not repeat those searches '
          'or claim universal absence.')
def add(label,credited,transport,verdict,disposition='Supporting assertion at its exact displayed data; no broader novelty claim.'):
    cross=old_rows[label]['credited_to']
    cross=cross[cross.index(' | Sweep1 cross-run comparison:'):] if ' | Sweep1 cross-run comparison:' in cross else ''
    credit[label]={'credited_to':credited+cross,'credit_transport':transport,
                   'source_credit_verdict':verdict,'literature_disposition':disposition,
                   'literature_searches':searches}

add('night:P1.1',
    'The literal rank-six tuple is the receiving construction. Its power, Smith, invariant and affine-freeness assertions are explicit integral calculations; no external classification is substituted.',
    'Use the literal convention of sec:fourfold and F2.5: M1=A^t and M2=B^t on homology, with M0=(M1 M2)^(−1). The actual common coinvariant homomorphism is ell(x)=x0. The given S conjugates M0 to the primitive square-zero cusp; the affine generators use the actual specified v_i/m_i. Exact nonidentity powers and their integral obstruction are checked in that basis.',
    'Full statement/proof and the new matrix, marking and topology-input outputs match; bounded antecedent comparison credits the marked-period/filling method separately. This row claims the displayed tuple, not a classification of all tuples.')
add('night:P1.2',
    'Explicit primitive/exterior-quotient calculation of the receiving pencil; the separately stated integral marking is P1.7/F3.5.',
    'For the rank-four marked lattice H and polarization bivector Pi, the natural inclusion then quotient j:Pi-perp→wedge²H/ZPi is the comparison. Its Smith factors are1,1,1,1,2. The lower simultaneous rational centralizer is scalar, so every rational intertwiner is cj; integral unimodularity would require1+5v2(c)=0. The same j supplies the rational isomorphism.',
    'The exact map, its index and scalar rigidity prove the integral assertion. No nonisomorphism is inferred merely from the index of one arbitrarily chosen map; supplied cross-run equality is kept as a source relation, not an extra proof.')
add('night:P1.3',
    'The standard free finite-affine filling construction is specialized to the two explicitly supplied generators; its two integral first-homology groups are the receiving calculation.',
    'Equivariant radial retraction takes each root-disc filling to its central free torus quotient. Abelianizing its actual deck presentation gives the relations (M_i−I)Lambda and m_i beta_i−v_i in the fibre lattice plus its base generator. The two seven-generator Smith calculations give Z² and Z²⊕Z/2.',
    'Known local quotient/retraction method is used in a short explicit specialization. The finite-cap torsion is kept; no rational quotient or global homology inference replaces these maps.')
add('night:P1.4',
    'Explicit hyperelliptic pencil and differential calculation in the receiving paper; root-base methods are compared with the opened AC26/E26/DGKX corpus at their actual scope.',
    'For y²=x⁵+lambda³x+lambda⁴, the zero chart is lambda=u⁸,x=u⁶X,y=u¹⁵Y and gives Y²=X⁵+X+u². The infinity chart is lambda=u^(−5),x=u^(−4)X,y=u^(−10)Y and gives Y²=X⁵+uX+1. The orders of dx/y and xdx/y give T³ and T with T=O((2/5)infinity−(3/8)0); the discriminant gives lambda*=−256/3125.',
    'Every displayed substitution, node and divisor was checked. The whole before-printed-proof reconstruction gate remains separate from the mathematical/source comparison.')
add('night:P1.5',
    'Short elementary exterior-algebra specialization for the actual genus-two Hodge line; corrected receiving statement is retained.',
    'The first map is ell0⊗Hodge→wedge²Hodge and has one-dimensional image. The second is ell0⊗(H_dR/ell0)→wedge²H_dR/ZPi. A nonzero vector in its source gives a decomposable bivector, whereas the nondegenerate Pi has nonzero square; hence the second kernel is zero and its image has rank3.',
    'The exact domain, quotient and polarization map are stated and independently derived. Its short proof records the form used here; no new general exterior-algebra theorem is asserted.')
add('night:P1.7',
    'The rational pencil/rigidity input remains F3.5. This row supplies the actual primitive integral companion marking and exterior-quotient transport.',
    'The vanishing-cycle orbit has unimodular Gram matrix. Pairing an integral class against that orbit proves its coordinates integral. The displayed mu=q/k map and its inverse therefore identify the actual H1 lattice with the companion lattice, including the antidiagonal pairing sign, based cusp word Cf Cg^(−1), and the two exterior-quotient basis maps of P1.2.',
    'Full receiving six-step proof, retained prior derivation and fresh exact marking checks agree. The source rigidity input is credited at its statement scope and is not rebranded as this integral calculation.')
add('night:P1.8',
    'Marked-period construction methods are credited to AC26 original §3 and DGKX v1 §2. The displayed rank-six scalar/transversality calculation uses the receiving P1.5 plane and P1.15 connection.',
    'The actual lift is F_c=(sigma+ic alpha e)(P). Its intersection with its conjugate is evaluated through the printed quotient-kernel map and scalar a0 b0; the resulting h satisfies h=y+O(1) in the actual invariant-line cusp convention. The genus-two root actions descend through the exterior quotient to orders5,4, and the completed-base test includes both finite roots. Splitting changes retain the full complex translation recorded in P1.18.',
    'The exact shared construction maps and the source-specific scalar criterion are distinguished by their stated maps and hypotheses. Current complete proof and fresh identities pass; the before-printed-proof route is not newly claimed.')
add('night:P1.9',
    'Yang2026, received Compact_Complex_Threefolds_REPAIRED_v4_5.tex, Theorem8.7 and Corollary8.8, source4674–4848; attached rendered editionpp57–59. Public arXiv-v1 equality was not verified.',
    'Set n=3, t=q, D=C and the source lattice matrix B=I for the index-one model. The identity on the dense torus extends over the identical marked Kuhn monomial charts and intertwines their deck maps. A finite-index lattice of index d gives the stated quotient and n!d=6d Euler formula.',
    'Known and cited specialization. The integrated short proof credits exactly the received edition and retains the actual map; it does not claim a newly proved higher-dimensional local filling theorem.',
    'Known local theorem, credited at exact attached-source statement, edition and page; no novelty claim.')
add('night:P1.10',
    'Yang/P1.9 supplies the actual local index-one Kuhn filling. AC26 original Construction6.1/Theorem6.2 and E26 §2 are antecedent marked toroidal/finite-filling methods. The rank-six global gluing is proved here.',
    'The P1.8 rank-three period quotient supplies the regular family; the specified free affine actions give the order5 and4 root quotients. The same S-marked boundary periods identify these with the n=3,D=C,B=I cusp. The actual van Kampen quotient retains the ordered signed pair(ell(v1),ell(v2))=(1,−1) and the coprime orders; all regular and finite torus fibres have Euler0 and the cusp has Euler6.',
    'Retained whole construction derivation plus full receiving and fresh33-check topology-input calculation agree at every admitted parameter and the fixed fan. The source local construction is credited; the printed global marked maps are retained.')
add('night:P1.11',
    'Yang/P1.9 analytic Kuhn model; Cox–Little–Schenck equations12.2.3–4 and Theorem12.2.5p571 (retained exact primary indexed-text opening ce:178e72a187d8957da453); Achinger–Ogus2020 formula3-3-1p478, Theorem4.1.1 and Lemmas4.1.2–3pp480–482 (retained original-PDF opening).',
    'On each nonnegative component use its actual squared-weight monomials, character polytope−2P_v and moment scaling mu_v=−(1/2)mu_standard. Common-face and deck identifications give the complete quotient cellular complex. The proper log-smooth chart N→N^r,1→(1,...,1), with its angular arguments, identifies the log-forgetful map with the actual nearby-fibre collapse. New integral cells/collapse matrices use the same marked angular/base cycles.',
    'Known component moment and log-topology results are cited in their exact scope. All common-face/deck/collapse maps and every integral row are supplied by the receiving proof and fresh186-check reconstruction. The named historical analysis receipts are not present; their detailed retained events, source hashes and locators remain evidence, not newly opened local files.')
add('night:P1.12',
    'AC26 original Construction6.1/Theorem6.2 and Corollary7.29pp36,61–63, E26 main/integral-topology result and both DGKX choice/sphere-type statements are credited antecedents. Operative local input: Achinger–Ogus4.1.1/4.1.2–3pp480–482; Hatcher2002 Theorems3.2p195,3.30p241,4.32p366.',
    'Retain the actual marked evaluation/collar maps and the P1.11 boundary collapse. The new unimodular target/source adapters identify the literal current kernel matrices; the displayed j4 map is primitive. Hatcher UCT applies to these free integral chain complexes; its Ext injection retains the actual torsion cycle. Closed oriented duality and successive Hurewicz apply only after the printed finite-cap/complement computation, with dimension8 and integral coefficients.',
    'Full source-specific homology proof passes, with retained444-check prereading route and fresh989 reconstruction plus914 saved-certificate verification. Hatcher exact three statements were freshly reopened; Achinger–Ogus original opening and exact log-map application remain the retained ce:10c3b530fb82b98d68e5 evidence. No absent historical file is represented as freshly replayed.')
add('night:P1.13',
    'Esole–Kang arXiv1807.08755v1 equations1.2–1.4pp3–4, used only as universal characteristic polynomials; Peters–Sterk June2024 author draft Theorem2.2.1p61, retained full theorem/proof opening. Spin Wu and integral duality are applied to the actual tangent bundle.',
    'The Chern-root map gives p1=−2c2 and p2=c2²+2c4. With c4=6, Todd integrality gives c2²=2+240k and signature=2+16k; rank4 forces k=0. The actual unimodular pairing has indices3,1. The class lambda=p1/2=−c2 reduces to w4 and is characteristic by spin Wu. The explicit integral norm-two reflection and sign maps send it to(1,1,1,1), with inverse the reversed word.',
    'Exact classical substitutions and lattice hypotheses are retained; no numerical square alone identifies the characteristic orbit. Prior isolated item1 and item3 derivations remain separate. The new sign-reviewer isolated item2 route is frozen with its disclosed possible earlier contact-sheet exposure; receiving comparison is the last procedural check for this row.')
add('night:P1.15',
    'The literal rational Gauss–Manin, exterior-quotient and root-regular extension calculations are receiving results. P1.1/P1.4/P1.7 supply the explicitly marked input systems; general marked-period methods receive the bounded AC26/DGKX credit.',
    'Solve the polynomial exact-differential identity for each x^k dx/y and pass through the actual relation3omega03+omega12=0. Root regularity gives the four allowed upper-row coefficients; cusp square-zero equations leave a two-dimensional space modulo the one-dimensional middle-row coboundary. The nonzero class s=c+4d/5 is sent to the chosen class by the printed e-fixing block map and inverse. The exact invariant-line contraction is alpha=(625 pi i/128)alpha_alg; Xe0=e0 fixes the scalar of the common intertwiner.',
    'All existence and uniqueness steps are algebraic/holomorphic. Fresh70+26checks and the sign reviewer frozen40-check upper-extension route agree with the full receiving proof. Prior incidental QA exposure is disclosed. Interval monodromy residuals are not used as an existence proof.')
add('night:P1.17',
    'Explicit fixed-marking/fixed-fan anti-isomorphism obstruction of the receiving rank-six family; source toroidal methods retain the Yang/AC26/DGKX credit already stated.',
    'The integral anti-intertwiner space is exactly±R. The finite affine norm excludes R. For−R the actual based cusp map is H=M2^(−1)(−R), with S-block(P,Q;0,−P). Its ray image−Pe2=(0,−1,1) lies outside the actual component rays±({0,1}³\\{0}). Period translations change the selected chart and units act by torus translation, retaining that linear ray action; the displayed one-parameter arc then contracts a divisor.',
    'Full current proof and fresh39-check anti-intertwiner/cusp/ray calculation pass. Scope stays with this S and Kuhn fan; no assertion about a differently compactified family is inferred. A complete before-printed-proof route remains undocumented here.')
add('night:P1.19',
    'Hatcher2002 Theorem3.43 printedp254, original author PDF physicalp263 (zero-based index262), freshly opened; Yang/P1.9 and P1.11 supply the actual analytic and topological cusp. The full integral global complex is reconstructed here.',
    'The cusp retraction rho:W→C pulls the actual cohomology class back to H^4(W), then cap product with[W,boundary] gives H_4(W,boundary): use n=8,k=4,R=Z,A=empty,B=boundary in Hatcher. The explicit K/cokernel maps, actual psi/e/r/t and all W/X/T chains identify the receiving Ext class and every incoming Smith factor. The new saved-certificate verifier checks those exact adapters and relative equations; global Poincare duality is not an input to that independent complex calculation.',
    'Full after-reading reconstruction989 and saved verifier914 assertions close the mathematical/missing-implementation gate, with exact basis maps integrated. Historical executions are preserved without pretending their absent programs were replayed. A separate root-owned fresh statement-only derivation is still pending; it is not supplied by this branch.')

root_map=('Set t=lambda*/(lambda*−lambda), and use the common root curve R of orders15,4. '
          'The root maps are s3=s15^5, s5=s15^3, with the order4 coordinate fixed. '
          'For T=O(4D1−D2), q5*L54=T³ and q3*L34→T⁵ is multiplication by(t−1)/t, '
          'with inverse t/(t−1), since15D1−4D2=div(t/(t−1)). '
          'The pullback direct images are O⊕T^(−5) and O⊕T^(−3)⊕T^(−6), and the exterior maps are cup products. ')
add('night:P1A.1',
    'DGKX v1 Lemmas6.1–6.2pp74–75 and Proposition6.10pp79–80, primary PDF reopened, supply the root-base/direct-image method. Grauert1960 §6 HauptsatzIp59,§7Satz5pp63–64 freshly opened; Cox–Little–Schenck9.2.3p410 retained exact opening.',
    root_map+'For the receiving family the actual wedge pairing gives W/P→K-dual, K=L⊕L²; the two root-line H1 groups vanish. On the cusp the constant cocycle model is the periodic Kuhn triangulation modulo Z³, with its actual Alexander–Whitney cup product. Proper flat root charts with constant structure-cohomology dimensions meet Grauert; determinants of dq/q→sum dx_i/x_i give K_M=h*L^(−6).',
    'Known source method and exact root/line/cup transports are credited. The receiving rank-three quotient, coherent cusp extension and all root weights remain fully proved and freshly checked. This root-line comparison does not supply an unproved full-family identification.',
    'Source-specific direct-image/canonical calculation, compared in the bounded corpus; known method credited.')
add('night:P1A.2',
    'DGKX v1 root/direct-image method as P1A.1; Cox–Little–Schenck9.2.3p410 for the zero toric divisor; Serre1955§13Theorem4p22/§15p23; Hirzebruch1978 Theorem25.3.1p187 and§25.4(a)pp188–190 (retained official-MPIM opening ce:bbc63cca96013598c42f).',
    root_map+'Apply Serre through the evaluation/wedge pairing on the actual compact smooth complex fourfold. The two displayed projected residue matrices have opposite nonzero determinants away from xi=5i/(3pi); the complete P1.18 certificate places that point below the admissible half-plane. Apply analytic Dolbeault RR to Omega^p with c1=c3=0,c2²=2,c4=6, giving chi_y=−y+4y²−y³.',
    'Every connecting rank is computed by the actual residue map; associated-graded dimensions are not used in its place. Full prior derivation, current nine-step proof and fresh51checks agree. The historical-program sentence has been removed and current build28p132 actually viewed clean.',
    'Specific Hodge table proved here using credited toric, duality and index inputs; bounded comparison only.')
add('night:P1A.3',
    'Serre1955§13Theorem4p22/§15p23 and Douady1974VII.8pp598–599/VIII.1pp599–600 freshly opened. DGKX v1 Theorem6.12p81 and Proposition6.16p85 were reopened for the shared tangent/Kuranishi mechanism.',
    root_map+'The receiving branchwise logarithmic/residue maps are tensored by the actual K_M=h*L^(−6). Their unique residue is a^(−5)≠0. Serre uses the pointwise tangent/cotangent evaluation pairing. The actual parameter KS map has rank1 and the base KS map has nonzero determinant3/[625(1−a)³], so the global class is nonzero. Douady supplies a classifying germ map; its actual convergent-ring homomorphism u→g(s),gprime(0)≠0, forces the defining ideal to vanish.',
    'The proof retains all source hypotheses and actual class maps. The resulting rank-six tangent tuple and miniversal germ are verified by the full receiving proof, retained frozen route and new exact root/KS calculations.',
    'Specific tangent and family calculation with credited duality/versality and DGKX method; no universal priority assertion.')
add('night:P1A.4',
    'Grauert1960§7Satz1p60 supplies the proper-image input, freshly opened. DGKX v1 Proposition7.13/Theorem7.14 and bare-equivalence proofp95, together with Lemma6.17p85, are explicitly compared at the source group/parameter scope.',
    root_map+'DGKX has the actual action c→[z,zeta+c u2] with kernelZ, hence C/Z→C*,c→exp(2pi i c). Here the receiving invariant alternating forms vanish, the exact simultaneous centralizer is QI, the finite affine norm excludes−I, and the primitive quotient kerN1∩kerN2/(B−I)ker(AB−I) has Smith factors1,1,2. The bounded cusp representative tau−e4 extends the order2 section; the actual translation field and this section give C×Z/2. Equality of the graph planes forces equality of their parameters.',
    'Both source group maps and receiving group/parameter maps are stated explicitly. The source automorphism theorem is credited in its own standard family. The receiving rank-six result follows from its actual integral quotient and fixed parameter graph, with retained full prior routes and new exact checks.',
    'Specific automorphism/isomorphism calculation with exact source comparison; shared root-base method credited.')
add('night:P1A.5',
    'Catanese2004 definitionp261/Theorem2.1p264 (proofpp267–268) supplies the compact-torus deformation input. Bierstone–Milman alg-geom/9508005Theorem1.6 and analytic-neighbourhood paragraphp5/Remark1.7p6; Grauert1960§6HauptsatzIp59/§7Satz1p60/Satz5pp63–64 were freshly opened. E26 received degeneration discussion source1647–1683 states its untwisted filling conjecture and subsequent transformed-family question.',
    'The actual K^(−4) sections lambda18,lambda19 have ratio lambda after their common base ideal is cancelled. Proper resolution/graph modification retains the known smooth open family; coherent relative forms define the actual C³/Gamma tori outside the proper analytic exceptional set. Their marked period planes continue by the same flat marking. The real hypersurface Imxi+h(lambda)=0 has points outside that complex analytic set, including after the displayed finite ramified-coordinate map; at infinity use u=1/xi.',
    'The source results apply to the specific proper maps, coherent sheaves and relatively compact central neighbourhood. The endpoint nonextension proof retains singular/nonreduced/additional central components and all actual recovery maps. E26 is not credited with proving its conjectural filling.',
    'Specific full-disc boundary obstruction in the bounded corpus; known resolution, proper-image and torus-deformation inputs credited.')
add('night:P1A.6',
    'Actual local miniversality and group/classification inputs are P1A.3/P1A.4. Cartan1952, Expose19§5pp19-14–19-15, original Numdam source freshly opened including its degree1 proof, supplies the additive coherent-cohomology vanishing.',
    'The proper holomorphic submersion has local pullback isomorphisms into the constructed family; uniqueness of its parameter glues the holomorphic classifying map. Its displayed Cayley transform has modulus<1 and extends to an interior value. The actual relative automorphism group is O⊕Z/2: a degree-at-most2 cover kills the finite cocycle and Cartan-B on Delta* makes the additive cocycle a coboundary. The coordinate z and z^(−1) confine every holomorphic hull to a compact annulus and verify the exact Stein hypotheses.',
    'Full three-step receiving proof, retained frozen derivation and actual P1A.3/P1A.4 maps agree. The proper-submersion scope is explicit. A two-line exact Cartan citation/specialization guard is supplied for root integration; it adds source precision rather than a new mathematical hypothesis.',
    'Specific punctured-disc family classification and interior filling; scope linked to the exact class map, not to arbitrary families of assigned sets.')
add('night:P1B.1',
    'Short elementary integral-basis specialization of the square-zero primitive-image hypothesis, also the receiving F2.1 statement; no general normal-form novelty is asserted.',
    'For N²=0 of rank3, imN⊂kerN have equal rank and the primitive-image quotient forces equality. Choose an integral basis e_i of that subgroup and lifts f_i with Nf_i=e_i. The quotient map identifies their images as an integral quotient basis, so (e1,e2,e3,f1,f2,f3) is unimodular. Direct block multiplication CN=NC gives C=(P,Q;0,P), detC=(detP)².',
    'The exact coordinate map and inverse basis construction are the short form used here. Frozen elementary derivation and full receiving comparison agree; no unsupported classification source is needed for this explicit proof.')
add('night:P1B.2',
    'Explicit finite cyclotomic enumeration for real rank6 with a free finite affine lift; elementary semisimplicity and real-eigenspace criteria are used in their displayed form.',
    'An affine lift without eigenvalue1 has a fixed point by solving(I−A)x=b; hence the characteristic product has a positive Phi1 exponent. Euler phi(n)≤4 leaves the displayed index list, and the exact exponent enumeration gives38 products. Companion blocks realize them; a rational translation in the trivial eigenline of denominator divisible by the linear order supplies the finite free lift. Even real ±1 eigenspace multiplicities give the19 commuting-complex-structure products.',
    'Frozen spectral derivation, full receiving proof and independent finite enumeration agree. This list is a preliminary spectral filter; it does not certify all integral gluing inputs or any unbounded search.')
add('maps:src:F.4.1',
    'Wall smooth extended-form classification as Conway–Crowley–Powell–Sixt authorv3§3.3pp11–12,Definition3.6p12,Theorem3.7(1)pp13–14; Kramer–Stolz TheoremAp178; Mandal Lemma2.1p5/Theorem2.4p7 and Corollary1.4p4. These precise source statements were opened and matched. Earlier BHS/Nikulin/Nagy comparisons remain historical evidence, not the current operative citation chain.',
    'The actual Spin4 clutch map is(a,b)→(e,p1/2)=(a−b,a+b), inverse((e+p1/2)/2,(p1/2−e)/2). The integral reflection word sends the characteristic vector to(1,1,1,1). Poincare duality transports the cohomology isometry psi to Phi=PD_N psi PD_M^(−1), preserving both normal coordinates. Wall gives M=N#Sigma; the oriented connected-sum maps place Sigma at a positive HP² summand and Kramer–Stolz absorbs it with degree+1. The actual forgetful realification of the transported integrable tangent structure gives c2=−sum u_i,c4=6,p2=14, matching Mandal.',
    'Smooth classification and almost-complex compatibility are explicitly credited. The proof keeps the family-specific normal-clutch, PD and connected-sum maps needed for the short specialization. The integrable realization is supplied by the separately proved rank-six construction and its integral topology.',
    'Known classification applied through explicit maps to the constructed integrable fourfold; bounded corpus/search comparison retained.')

assert len(credit)==24
(own/'V_source_credit_import_08.json').write_text(json.dumps(credit,indent=2,ensure_ascii=False)+'\n')

# Preserve and correct the direction sentence in our own current report only.
report=own/'V_literature_comparison_report.md'
text=report.read_text()
old='the first identity is multiplication by t/(t−1) in the explicitly stated direction.'
new=('the map q3*L34→T^5 is multiplication by (t−1)/t, and its inverse T^5→q3*L34 '
     'is multiplication by t/(t−1). In the meromorphic-function convention for O(D), '
     'the divisor difference is div(t/(t−1))=15D1−4D2, so these two coefficient maps '
     'preserve the corresponding holomorphic sheaves.')
if old in text:
    receipt={'utc':now,'file':str(report),'old_sha256':sha(report),'old_text':old,'new_text':new,
             'reason':'Direction already repaired in the shared manuscript by root; this corrects a stale current-audit summary. Original V_root_curve_comparison.tex explicitly gives the valid inverse T^5→q3*L34 and remains unchanged as evidence.'}
    report.write_text(text.replace(old,new,1));receipt['new_sha256']=sha(report)
    (own/'V_root_line_direction_receipt_08.json').write_text(json.dumps(receipt,indent=2)+'\n')

# Fresh precise source openings, not new proofs of the external theorems.
openings=[
 {'source':'DGKX v1 primary PDF','file':'audit_paper_i/open_atlas/DGKX_v1_primary.pdf',
  'sha256':sha(root/'audit_paper_i/open_atlas/DGKX_v1_primary.pdf'),
  'locators':['Lemmas6.1–6.2 and full proofs pp74–75','Proposition6.10 and full proof pp79–80',
              'Theorem6.12 and proof p81','Proposition6.16 and full proof p85',
              'Lemma6.17 and proof p85','Proposition7.13/Theorem7.14 and bare-equivalence proof p95'],
  'scope':'Actual root/line/cup-product comparison and tangent/classifying/group-map comparison stated in V_source_credit_import_08.json. No full-family identification is inferred from common root-line pullback.'},
 {'source':'Hatcher2002 author PDF','file':'audit_corrections/primary_sources/Hatcher2002_author_07.pdf',
  'sha256':sha(own/'primary_sources/Hatcher2002_author_07.pdf'),
  'locators':['Theorem3.2 printed195 / one-basedPDF204','Theorem3.30 printed241 / one-basedPDF250',
              'Theorem4.32 printed366 / one-basedPDF375','Theorem3.43 printed254 / one-basedPDF263 = zero-basedindex262'],
  'scope':'Fresh exact UCT, oriented duality and Hurewicz statement matching for P1.12; clarified physical/index terminology for the previously opened local relative duality used in P1.19. No full proof reading of every textbook theorem claimed.'},
 {'source':'Cartan1952 Expose19 original Numdam PDF',
  'url':'https://www.numdam.org/article/SHC_1951-1952__4__A19_0.pdf',
  'refs':['turn587336987view0','turn247141134view0'],
  'locators':['Stein hypotheses §4 p19-11','TheoremB proof §5 pp19-14–19-15, including explicit q=1 case'],
  'scope':'Fresh original source text opening; O on Delta* is coherent, and z,z^−1 verify the Stein hull/coordinate hypotheses. Thus additive degree1 torsors are coboundaries. No fresh screenshot viewing is claimed; screenshot tool returned only an image reference.'}]
(own/'V_exact_primary_openings_08.json').write_text(json.dumps({'utc':now,'actor':actor,'openings':openings,
    'retained_source_limits':'Cox, Hirzebruch, Peters–Sterk and Achinger–Ogus primary readings are retained at exact event scopes. Historical analysis/continuation_V/*.json/md files named in those events are absent from the attachment; their detailed event records remain available. Root reports no fresh Hirzebruch opening receipt, and none is assigned to root here.'},indent=2,ensure_ascii=False)+'\n')

events=[
 ('night:P1A.1','Fresh primary DGKX v1 exact source comparison: Lemmas6.1–6.2pp74–75, Proposition6.10 full proofpp79–80, Theorem6.12p81, Proposition6.16/Lemma6.17p85, Proposition7.13/Theorem7.14 and bare-equivalence proofp95 reopened. The actual common(15,4) root maps, q3*L34→T^5 multiplication(t−1)/t and inverse, cup products and source group/classifying maps are matched in V_source_credit_import_08.json. This is source scope, not a new independent whole proof of P1A.1–4. A stale directional sentence in this audit report is corrected with preserved receipt; current manuscript already had the correct direction.'),
 ('night:P1.12','Fresh Hatcher original author-PDF statements3.2printedp195,3.30p241 and4.32p366 reopened and matched to the actual free chain complexes, closed complex-oriented dimension8 manifold and successive connectivity inputs of P1.12. Source/physical-page locators and exact maps in V_exact_primary_openings_08.json. No new independent whole proof or textbook-proof review claimed.'),
 ('night:P1A.6','Fresh Cartan1952 original Numdam Expose19§4Stein hypothesesp19-11 and§5TheoremB proofpp19-14–19-15, including q=1 case, opened. For Delta*, z and z^−1 confine every holomorphic hull to a compact annulus and z supplies separation/local coordinates; O is coherent. The actual additive torsor is therefore a coboundary. Exact citation/specialization guard in V_exact_source_locators_guard_08.json; this source check is not a new independent whole proof.')]
ledger=own/'CHECK_EVENTS.tsv'
with ledger.open(newline='') as f:reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
ids={r['event_id'] for r in rows}
newids=[]
for label,outcome in events:
    eid='s6sg:'+hashlib.sha256((label+'|'+outcome).encode()).hexdigest()[:20]
    if eid not in ids:
        row={k:'' for k in fields};row.update(statement_id=label,date=now,who=actor,type='targeted proof check',outcome=outcome,event_id=eid,phase='S6_SERIES_GRIND')
        rows.append(row);newids.append(eid)
with ledger.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)

# Current complete source/block and layout gates; mathematical exposure is independent.
assessment=json.loads((own/'row_assessments.json').read_text())
body=(root/'S6_SERIES_GRIND_V.tex').read_text();linked=(root/'parts/V.body.linked.tex').read_text()
qa=json.loads((own/'V_build28_visual_QA_08.json').read_text())
assert sha(root/'S6_SERIES_GRIND_V.pdf')==qa['pdf_sha256']
proofchecks={}
for label in credit:
    start=body.index('\\label{'+label+'}');end=body.index('\\end{proof}',start)+len('\\end{proof}')
    block=body[start:end]
    record=re.search(r'\\StatementRecord\{'+re.escape(label)+r'\}\{([^}]*)\}\{([^}]*)\}',block)
    assert record and record.group(1)=='proved' and record.group(2)
    assert r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.}]' in block
    assert not re.search(r'historical continuation program|code/part1/|certified_lift_bound\.py|tuple_check\.py|pencil_charts\.py|spectral_filter\.py',block)
    proofchecks[label]={'body_start':start,'body_end':end,'block_sha256':hashlib.sha256(block.encode()).hexdigest(),
                        'status':record.group(1),'tag':record.group(2),'numbered_proof':True}

pending={
 'night:P1.4':'Full receiving proof and every displayed root/node/divisor computation pass. A complete written derivation before receiving all current proof steps remains undocumented; initial root steps were exposed during setup.',
 'night:P1.8':'Full scalar/transversality/root/cusp proof and fresh exact identities pass. A complete written derivation before receiving all current steps remains undocumented. The P1.18 numerical minimum dependency is complete and is not the remaining gate.',
 'night:P1.17':'Full fixed-S/fan proof and fresh exact anti-intertwiner/based-cusp/ray computation pass. A complete written derivation before receiving all current steps remains undocumented. Scope cannot be widened to other fans without their actual maps.',
 'night:P1.19':'Full mathematical reconstruction, supplied executable and output/basis/Ext gates pass. The root-owned isolated statement-only reviewer is working; its frozen derivation and receiving comparison are not yet received here. No after-reading computation is relabelled as that route.',
 'night:P1.13':'Retained item1 integrality and item3 reflection were frozen before their respective steps. Sign reviewer item2 derivation is now frozen at the disclosed possible prior contact-sheet exposure; its receiving comparison remains pending at this proposal snapshot.',
 'night:P1A.6':'All mathematical, prior derivation and proper-submersion gates pass. The exact Cartan-B citation/specialization guard in V_exact_source_locators_guard_08.json remains to be integrated and the resulting changed page inspected.'}
scopes={
 'night:P1.1':'Literal marked rank-six tuple, cohomology/homology dual convention and specified finite affine actions.',
 'night:P1.2':'Actual primitive/exterior-quotient map, rational comparison and all integral intertwiners.',
 'night:P1.3':'The two specified finite root fillings only.',
 'night:P1.4':'Given genus-two pencil, both root charts and the exact Hodge divisors.',
 'night:P1.5':'The actual Hodge line and rank-three quotient wedge map.',
 'night:P1.7':'Actual integral companion marking and based cusp word, at the cited rigidity input.',
 'night:P1.8':'Corrected P, fixed splitting, both finite roots and the stated cusp asymptotic.',
 'night:P1.9':'Exact n=3,D=C,Kuhn-fan specialization of the received Yang edition.',
 'night:P1.10':'Every admitted parameter of the specified rank-six family with its fixed marked finite caps and Kuhn cusp.',
 'night:P1.11':'Full stated index-one Kuhn topology, quotient cells and marked specialization maps.',
 'night:P1.12':'Actual marked global manifold and its full integral homology, including torsion cancellation.',
 'night:P1.13':'Complex-oriented characteristic numbers and the actual integral characteristic lattice pair.',
 'night:P1.15':'Exact rational quotient/extension connection and normalized common-intertwiner existence/uniqueness.',
 'night:P1.17':'Only the specified S-marked Kuhn compactification and its actual toric ray action.',
 'night:P1.19':'Full actual global cellular complex and extension class, with the supplied exact basis maps.',
 'night:P1A.1':'Actual coherent extension on all finite/cusp fibres and its direct-image cup maps.',
 'night:P1A.2':'Complete Hodge table on the whole admissible half-plane, with actual connecting maps.',
 'night:P1A.3':'Full tangent tuple and miniversality of the actual parameter family at every member.',
 'night:P1A.4':'Full automorphism group and exact equality of parameters in the fixed splitting.',
 'night:P1A.5':'Proper Hausdorff full-disc boundary extension, including the stated singular central-space possibilities and finite ramified changes.',
 'night:P1A.6':'Proper holomorphic submersion over the punctured disc, with actual interior class-map filling after degree at most2.',
 'night:P1B.1':'Primitive rank3 square-zero integral endomorphism on Z6 and its full integral centralizer.',
 'night:P1B.2':'Only the38-polynomial spectral list and19-product complex-compatibility filter.',
 'maps:src:F.4.1':'Oriented smooth classification of the constructed fourfold, with actual unstable normal transport and homotopy-sphere absorption.'}
out={}
for label in credit:
    r=dict(assessment[label])
    r['remaining_risk']=pending.get(label,'No remaining mathematical or row-specific format/source/layout gate at this exact statement scope. Established dependencies retain their separately recorded source and proof scope. '+scopes[label])
    r['format_check']='PASS: current whole statement/proof block has status, tag, links, explicit scope, numbered proof and available method/input/output descriptions; integration receipts current_certificate_integration_06.json, I_V_current_program_integration_07.json, received_proof_integration_07.json and received_guards_integration_08.json checked. Exact source metadata in V_source_credit_import_08.json.'
    if label=='night:P1A.6':r['format_check']='Current proof form and explicit proper-submersion statement pass; exact Cartan-B locator/specialization guard awaits integration. No mathematical gap found.'
    r['layout_check']='PASS at listed sample and all current overflow checks: audit_corrections/V_build28_visual_QA_08.json, PDF SHA'+qa['pdf_sha256']+'. All61 sampled pages are accounted for by actual views or exact full-page pixel equality; current log has no overflow>2pt, missing glyphs or unresolved-reference warnings.'
    r['completion_state']='not done; '+pending[label] if label in pending else 'done'
    r['scope']=scopes[label]
    r['source_credit_import']='audit_corrections/V_source_credit_import_08.json'
    out[label]=r

out['night:P1.13']['independent_routes']+=' Retained isolated step1 ce:5040d640152b8e539237 with independent Fraction computation ce:e688b68dd8fc2dcab242, and isolated step3 ce:196754ab2fecdedc4703 with621+48+10 cases ce:4f8afbfe0257c201cfa3. Sign reviewer frozen item2 route audit_sign/V_P113_item2_before_receiving_08.md SHA7caa6b888dd846b0eb6a35df4ffb295afe4e07962200e8367d36260e19dad0b9 is not yet promoted until its receiving comparison.'
(own/'V_whole_row_completion_proposal_08.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
receipt={'utc':now,'actor':actor,'source_import':{'path':'audit_corrections/V_source_credit_import_08.json','sha256':sha(own/'V_source_credit_import_08.json'),'rows':24},
         'whole_row_proposal':{'path':'audit_corrections/V_whole_row_completion_proposal_08.json','sha256':sha(own/'V_whole_row_completion_proposal_08.json'),'done':sum(r['completion_state']=='done' for r in out.values()),'pending':list(pending)},
         'linked_body_sha256':sha(root/'parts/V.body.linked.tex'),'standalone_tex_sha256':sha(root/'S6_SERIES_GRIND_V.tex'),
         'pdf_sha256':qa['pdf_sha256'],'proof_block_checks':proofchecks,'new_event_ids':newids,'own_event_count':len(rows),
         'canonical_ownership':'This script does not change row_assessments.json, shared inventory, body, frontmatter or bibliography. P1.16/P1.18 remain paper_i owned; P1.19 fresh-review target is not exposed to this proposal by communication.'}
(own/'V_whole_row_receipt_08.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'source_rows':24,'proposal_done':receipt['whole_row_proposal']['done'],'proposal_pending':list(pending),'own_events':len(rows),'new_events':newids},ensure_ascii=False))
