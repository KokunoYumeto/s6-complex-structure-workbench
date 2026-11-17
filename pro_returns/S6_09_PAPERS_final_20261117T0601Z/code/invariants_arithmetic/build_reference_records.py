from pathlib import Path
import json, hashlib, re
ROOT=Path(__file__).resolve().parents[3]
D=ROOT/'deliverables/work/invariants_arithmetic'
cache=ROOT/'sources/audit_cache/inv_ari/literature'
fetch={x['key']:x for x in json.loads((cache/'fetch_manifest.json').read_text())}
contexts=json.loads((D/'citation_contexts.json').read_text())
refs={}
def add(key,locator,use,hypotheses,source=None,url=None,web=None,status='verified_for_stated_use'):
 rec={'citation_key':key,'status':status,'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)',
      'effort':'Pro','date':'2026-11-17','opened_locator':locator,'actual_use':use,
      'hypotheses_and_normalization_check':hypotheses,'citation_contexts':contexts.get(key,[]),
      'extent':'Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.'}
 if key in fetch:rec['retrieval']=fetch[key]
 if source:
  p=ROOT/source
  rec['local_source']=source
  if p.exists():rec['source_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
 if url:rec['url']=url
 if web:rec['web_open_locator']=web
 refs[key]=rec

add('AC2026','Attached original PDF: Remark 1.3 p.5; Proposition 7.27 pp.62–63; Theorem 9.1 pp.64–65; Proposition 9.11 pp.70–71; Lemma 9.12 pp.71–74; Proposition 9.13 pp.74–75; Remark 9.21 p.81; Theorem 10.5 pp.88–89; Proposition 10.8 pp.92–94.',
 'Credit for construction, canonical pencil, structure-sheaf cohomology/direct images, cusp cup product, transgression factor twelve, Picard restriction injection and uniform fibrewise non-torsion. The precise full Hodge table and twisted tangent formulas require the later computations.',
 'Original PDF controls transcription. Remark9.21 p.81 explicitly claims degree-one relative torsion along W union S1 union S2; the local-module proof refutes its cusp clause. Remark1.3 p.5 uses the plural Omega^p and must be qualified by degree, since degree-two cusp torsion is nonzero. This is a correction to the original PDF itself, not merely its transcription. Scheme fibres include 3S1 and 4S2. AC Proposition7.27 leaves a common orientation sign; the family marking fixes it. Theorem10.5 gives nonzero R2 for every twist and H2 for general twists, not every precise jump multiplicity.',
 'sources/original/AC26_original_manuscript.pdf')
add('Engel2026','S6.tex §1 lines235–280; §2 lines288–390; main-thm lines882–910; integral homology lines1617–1643; remarks1647–1725.',
 'Comparison of equivalent elliptic-surface construction, section height 1/6, line-bundle lift, sphere criterion, automorphism identity component and period signatures.',
 'The introduction explicitly omits Dolbeault calculations. Do not credit E26 with the INV full Hodge/Bott–Chern table or exact twisted tangent jumps. Sphere criterion is |12 psi(a0+a1)|=1.',
 'sources/papers/arXiv_2609.38442_Engel_src/S6.tex')
add('DuEtAl2026v1','v5oka_maps_modifications_deformations.tex intro lines300–345; Theorem6.12 (p2:thm:tangent-cohomology) lines9445–9487; Corollary6.13 lines9490ff.; Proposition6.16 (p2:prop:kuranishi-line) lines9876–9917; connected automorphisms lines9967–10010.',
 'Credit for original-family tangent cohomology (1,1,1,0), nonzero parameter Kodaira–Spencer map, smooth reduced one-dimensional Kuranishi germ; original-family classification and automorphisms in Theorem1.4.',
 'This is the historical first version. The exact statements are known-source duplicates of INV D1.3–D3.1/FAM A5.2; the printed explicit Koszul and gluing proofs are preserved. The second version omits these results, which alone is not a mathematical refutation.',
 'sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex')
add('DuEtAl2026v2','submited-tams.tex introduction lines312–320 and whole-file searches for tangent/Kuranishi/classification; section inventory.',
 'Version comparison for scope of Oka construction, maps and point-deletion results.',
 'The relevant deformation and global parameter-classification assertions of v1 are absent. Do not cite v2 as a proof of the v1 tangent theorem.',
 'sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex')
add('Yang2026','Compact_Complex_Threefolds_REPAIRED_v4_5.tex main statements lines174–205,207ff.,249–261,320ff.',
 'Compare B(4,6), C(3,6) rational-homology families, r cusp components, fundamental groups and affine deformation/period statements.',
 'These are different finite filling types. Their Hodge/rational Betti statements must not be substituted for the original AC26 family. Detailed Lemmas6.6–6.9/Proposition6.15 centralizer transfer still requires its separate root-owned application check.',
 'sources/papers/arXiv_2609.29666_Yang_src/Compact_Complex_Threefolds_REPAIRED_v4_5.tex')
add('Wang2026','order_two_rational_homology_sphere_new.tex main statement lines99ff.,775ff.; Prop2.4 init:open lines218ff.; specialization/filling propositions375ff.,499ff.',
 'Compare order-two rational homology sphere, contracting quotient construction, and finite filling mechanism.',
 'Curve configuration IV*, I2, I1, I1 with P(t)=(1,sqrt(2)t); H2/H3=Z/2 and simple connectivity. These results are not a proof of the original full Hodge/tangent computation.',
 'sources/papers/arXiv_2609.11541_Wang_src/order_two_rational_homology_sphere_new.tex')
add('ViaclovskyLog2026','Logarithmic_S6_October_28_2026_Final.tex main theorem lines219–229; questions233–250; simply-connected theorem606ff.',
 'Credit for logarithmic transformation sphere families with coprime 3k,4l and invariance of those multiplicities; compare generalized INV B canonical calculations.',
 'The source asserts positive Kuranishi dimension and asks for exact deformation dimension/miniversality. It does not supply the INV exact tangent theorem for every generalized pair.',
 'sources/papers/arXiv_2610.39102_Viaclovsky_log_transformations_src/Logarithmic_S6_October_28_2026_Final.tex')
add('ViaclovskyTwoParameter2026','Viaclovsky_S6_September_26_2026.tex main theorem256ff.; canonical/algebraic-dimension proposition1339ff.; cohomology lines1433–1470.',
 'Compare two-parameter III*,I1^3 construction and structure-sheaf Hodge numbers.',
 'The source computes h0q=(1,1,0,0) and explicitly leaves remaining Hodge numbers open; no full-table credit.',
 'sources/papers/arXiv_2609.33785_Viaclovsky_two_parameter_src/Viaclovsky_S6_September_26_2026.tex')
add('ViaclovskyCombs2026','Viaclovsky_Comb_S6_Draft_October_7_2026.tex main theorem236–260; general flat-torus cohomology theorems418ff.,490ff.; original-family Hodge proposition2430ff.; comb cohomology2471ff.; questions2695ff.',
 'Credit for comb families h01=2m+1, h02=2m, h03=0 and lower deformation bound; general direct-image local-freeness and cup-product results.',
 'm>=12 in the construction theorem; deformation lower bound 8m−8 is not an exact dimension. CDP agent owns INV E application and full comb proof dependency audit.',
 'sources/papers/arXiv_2610.10451_Viaclovsky_combs_src/Viaclovsky_Comb_S6_Draft_October_7_2026.tex')
add('LiuRollenske2026','S6_arxiv.tex theorem and proof lines1702–1728; Remark1729ff.; following begin{comment} block explicitly excluded.',
 'Credit for distinct sphere construction and singular-fibre distinction.',
 'Remark leaves canonical/Hodge invariants for later. Unpublished commented calculations after line1732 are not theorem assertions or proof sources.',
 'sources/papers/arXiv_2609.33826_Liu_Rollenske_src/S6_arxiv.tex')
add('McHugh2018','BCA-FonCmpctCmplx3flds-111518.tex lines600–810: Theorem6.3, Proposition6.4, hBC22 formula and §7.1.',
 'Independent derivation of the Bott–Chern dimension table in INV C2.2 and the working edition.',
 'Compact complex threefold; substitute b1=b2=0, h20=h02=0, E2^{3,1}=0 and the relevant k^{p,q}=0. The latter vanishing is established from the actual Betti data, not assumed from a generally false injection.',
 'sources/papers/arXiv_1708.03251_src/BCA-FonCmpctCmplx3flds-111518.tex')
add('Angella2018','angella-5-final.tex §4 lines975–1155, including the complex-six-sphere Bott–Chern calculations and Schweitzer duality.',
 'Independent known-source Bott–Chern formulas specialized to the computed Hodge numbers.',
 'Conditional general formulas for a complex structure on S6; the input Hodge numbers come from INV A, not from this external article.',
 'sources/papers/arXiv_1705.10518_src/angella-5-final.tex')
add('huber2022','gesamt-ams.tex lines2138–2205, Theorem6.1 (analytic subgroup theorem), refined annihilator formulation and proof.',
 'Transcendence of the compact slope via non-splitting of the universal vector extension; limits of exponential arguments in C7.7/C7.9/C7.11.',
 'Connected commutative algebraic group over Qbar; an algebraic Lie subspace containing a logarithm of a nonzero algebraic point forces an algebraic subgroup. The actual subspace must be algebraic: the real compact slope is not silently treated as algebraic.',
 'sources/papers/arXiv_1805.10104_Huber_Wuestholz_src/gesamt-ams.tex',web='turn32view1')
add('bertolin2022','SemiAbelianTowers-final.tex Construction3.4 and Lemma3.5 lines580–658; remaining detailed period-conjecture case references tracked separately.',
 'Mumford–Tate unipotent dimensions for the 1-motive and explicit diagonal bracket calculation.',
 'Base field algebraically closed. B is the smallest abelian subvariety containing the point/extension data, Z includes bracket image plus the remaining torus point; dim UR=2dim B+dim Z. C7.4 stays conditional on the stated period conjecture.',
 'sources/papers/arXiv_2010.15170_Bertolin_Philippon_Saha_Saha_src/SemiAbelianTowers-final.tex',web='turn32view0')
add('demarco2017','VCHequidistribution_arxiv_v_2.tex Theorem1.1/Corollary1.2 lines142–172; local heights/divisor degree/continuity lines237–311.',
 'Local-height measure and small-height equidistribution, including C8.10.',
 'Nonrepeating Galois orbits of small points; generic height positive. Height normalization is relative to (O), so the measure has mass1/12 and 12m_P is the probability measure. No additional isotriviality hypothesis is inserted.',
 'sources/papers/arXiv_1701.07947_DeMarco_Mavraki_src/VCHequidistribution_arxiv_v_2.tex',web='turn27view2')
add('DukeImamoglu2008','Original attached PDF, Theorem1 p.2 and formula(6) p.4.',
 'Explicit zero of the Weierstrass function in INV A2.3.',
 'The branch used in the family is mu=1−z0. Period and hypergeometric normalizations checked; zero replacement is not a pole.',
 'sources/papers/Duke_Imamoglu_zeros_of_Weierstrass_p.pdf')
add('EichlerZagier1982','Original author-hosted scan, pp.399–403, zero formula and its normalizations.',
 'Independent Weierstrass zero formula, modular determinant constants and chosen branch.',
 'Matched the article lattice/eta conventions to mu=1−z0 and the family marking; no phase inferred from absolute values.',web='turn5view0; turn7view2')
add('Stelzig2021','Original arXiv1812.00865v3, Theorem A (=Theorem3), p.2; bounded double-complex decomposition.',
 'Square/zigzag decomposition for INV C2.1.',
 'Bounded double complex over a field; vector spaces need not be finite-dimensional. Infinite cardinal square multiplicities are allowed, while the finite cohomological summands are counted separately.',url='https://arxiv.org/pdf/1812.00865v3',web='turn7view0')
add('Gauduchon1985','Original eight-page paper, Theorem2 pp.132–133.',
 'Existence/uniqueness up to scale of Gauduchon conformal representative.',
 'Compact connected complex manifold of dimension at least2; the actual manifold has dimension3. This is not a Kähler assertion.',web='turn16view1; turn17view0')
add('STW2017','Original arXiv1503.04491v2, Theorem1.3 p.3.',
 'Prescribed Chern–Ricci form in a fixed Gauduchon Aeppli class in INV C3.6.',
 'Real Bott–Chern representative of c1BC, compact Hermitian manifold with Gauduchon initial form. The nonzero c1BC excludes a Ricci-flat representative.',url='https://arxiv.org/pdf/1503.04491v2',web='turn5view2')
add('BourdonClarkStankewicz2017','Original arXiv1411.2742v3, Theorem4.15 p.23.',
 'Rational CM torsion possibilities for all orders in ARI C5.1.',
 'The field is Q(j), including nonmaximal CM orders. Applied with rational j, so no maximal-order-only restriction is silently ignored.',url='https://arxiv.org/pdf/1411.2742v3',web='turn25view0;turn26view0')
add('Sutherland2023CM','MIT18.783 Lecture20, Theorem20.12 and Corollary20.13 p.6.',
 'Algebraic integrality of CM j for arbitrary orders and class-polynomial route.',
 'Theorem covers orders, not merely maximal rings. Rational algebraic integer j is integral; finite class-number-one enumeration is separately rerun.',url='https://math.mit.edu/classes/18.783/2023/LectureNotes20.pdf',web='turn25view1;turn26view1;turn27view1')
add('Shin2015','Original arXiv1009.2253v6, definition p.1, Remark2.2 p.3, Proposition2.3(ii),(iii) pp.3–4.',
 'Siegel-function multipliers and modular-unit normalization in C4.1.',
 'g_a transformation under T, S and lattice translation matched exactly; power12N removes multipliers under the stated congruence group. Local-height zero-mean constant checked independently.',url='https://arxiv.org/pdf/1009.2253v6',web='turn25view2;turn27view0')
add('Schnell19','Lecture4 (February6), Theorem4.1 p.1; equation4.3 and Cases1–2 p.2; Theorem4.4 and quotient statement p.3.',
 'Appell–Humbert classification, nonnegative Hermitian form for an effective line bundle, pullback of an ample bundle from a quotient, Riemann projectivity criterion.',
 'Compact complex torus V/Lambda; integral imaginary Hermitian form and semicharacter. A nonzero section excludes negative directions, forces semicharacter trivial on the null lattice, and descends to the quotient; positivity there proves ampleness.',web='turn42view0')
add('CrCremonaSiksek2006','Original author PDF §1–2 pp.1–3, Proposition3 §5, Theorem1 §6 p.8.',
 'Automatic eclib lower-height saturation bound in C6.R1.',
 'Minimal Weierstrass model and Egr=E(Q)∩E0(R)∩prod E0(Qp). Their canonical height is the x-height/2(O) convention, twice the paper height relative to (O). Bounds and regulator use the same convention; all component primes are included.')
add('CrRubin1999','Original notes §10, Theorem10.1 p.47; surrounding standing CM setup.',
 'Coates–Wiles contrapositive to deduce central vanishing from nontorsion, including sign+1 curves in C6.R2.',
 'Full maximal CM over K is the stated setup. Nonmaximal cases first pass to an isogenous maximal-order curve; rational full-CM L(E/K)=L(E/Q)^2. The theorem conclusion is E(K) finite when L(bar psi,1) nonzero, not the whole BSD formula.')
add('CrGrossZagier1986','Original preprint Theorem I.7.3, printed pp.11–12 (PDFpage8, visually read); proof V§2 printed pp.128–130, textlines5653ff.',
 'Rational nonzero factor between simple central derivative, a rational point height and real period in C6.R3.',
 'Modularity is assumed in the source and holds for the CM curves via Hecke theta series. L(E,1)=0 is checked. Proof chooses a quadratic twist with nonzero central value by Waldspurger. Full real period and (O)-height change the source normalization only by rational factors.')
add('CrGross1991','Original scan §1 printed pp.235–236 (PDFpages1–2 visually read), Theorem1.3; §2 opening p.237.',
 'Kolyvagin finite Sha and rank1 conclusion for a non-torsion Heegner point in C6.R3.',
 'Imaginary quadratic K with all primes of N split, D≠3,4, and non-torsion y_K. The non-CM assumption on p.237 applies to the subsequent simplified proof, not Theorem1.3 on p.236. The analytic-rank-one application uses the nonzero Heegner height. Restriction/corestriction and finite 2-torsion descend finiteness from K to Q.')
add('CrJetchev2008','Original arXiv0707.0032, Introduction Theorem1.1 p.2, textlines53–70.',
 'Modern primary statement of Gross–Zagier–Kolyvagin rank equality in analytic rank<=1.',
 'Theorem1.1 itself asserts rank equality, not Sha finiteness. The latter is separately sourced to Gross Theorem1.3; no stronger conclusion is assigned to Jetchev1.1.')
add('miller2011','Original arXiv1010.2431v3, Definition1.1/Theorem1.2 p.2; Table9 p.23.',
 'Full BSD for the three conductor3136,3136,361 curves in C6.R4.',
 'Analytic rank<=1, conductor<5000. The eleven exceptional curve-prime pairs have conductors546,570,858,870,1050,1230,1938,1950,2370,2550,3270. None is one of the three curves; isogeny invariance noted before the theorem. The integer analytic quotient is then isolated independently by exact doublings/Arb.')
add('CgzCai2014','Original publisher PDF Theorem1.1 pp.2524–2525; conventions pp.2523–2524 and pairing discussion p.2531.',
 'Exact Gross–Zagier denominator bound for C6.R5.',
 'Conductor-one genus character, conductor prime to N, no inert prime dividing N, repeated primes split, and shared N,D local-character compatibility checked in the exact metadata program. Formula factor2^-mu 8pi²(f,f)/(u²sqrt(|D|c²)deg f) uses the number-field-normalized height pairing; YZZ normalization below supplies the extra factor4.')
add('CgzBelabas2019','Original publisher PDF AppendixB p.102, unnumbered 26569a1/26569a2 table (PDFpage23), visually read.',
 'Manin constant1 and modular degree59368 for 26569a1 in C6.R5.',
 'Table columns are deg and c_E; 26569a1 has59368 and1, 26569a2 has9676984 and1. No nonexistent Table5 is cited. Optimality/homology columns are (1,1) for a1.')
add('CgzYZZ2011','Original complete preprint §7.1.1 pp.218–219, Theorems7.1.1–7.1.2 and Proposition7.1.3; textlines11243–11328.',
 'Resolve field-degree and polarization factors in C6.R5.',
 'The absolute values are normalized over K and the displayed height divides by[K:F], hence over quadratic F it is2 times the absolute height over Q. Pairing is h(x+y)−h(x)−h(y), hence its diagonal is2h, not h. Together the diagonal over the quadratic base is4 times the paper (O)-height. L is symmetric ample, as O(origin) on E.')
add('CgzStein2007','Original book §9.4.1.2, Theorem9.18 printed pp.171–172.',
 'Finite coefficient equality via Sturm bound in C6.R5.',
 'Weight2, congruence subgroup Gamma0(N), integral coefficients; agreement beyond k[SL2Z:Gamma]/12 suffices. Congruence for every prime ideal gives exact equality of integral coefficients; only this elementary corollary is used.')
add('CrBDP2012','Original publisher-format author PDF Theorem1 printed p.262, standing assumptions pp.261–262.',
 'Precise ordinary p-adic Rubin formula in the scope discussion after C6.R4.',
 'Curve over Q with full CM, prime split and prime to conductor, simple central zero. Katz special value equals p-adic logarithm square divided by p-adic period modulo K*. It does not give algebraicity of the real exponential height.')
add('CrCastella2025','Original author PDF dated2025-02-14, TheoremA and Remark1.1.1 p.2.',
 'Precise p-primary BSD scope discussion after C6.R4.',
 'Full CM, F(Etors)/K abelian, ord L(psi)=1, p not dividing6hK and split, Hecke conductor prime to p, different divides conductor exactly. Source explicitly distinguishes K⊂F (rank2) and K not⊂F (rank1). Nonmaximal orders require isogeny; the -16 different condition is not claimed. p=3 is excluded and inert at -163, so no actual Sha=9 conclusion.')
add('agboola2006','Original publisher PDF introduction pp.1001–1002; Rubin AppendixA pp.1042–1043, TheoremA.1 and LemmaA.2.',
 'Nonzero ordinary p-adic height of the rank-one CM point in C7.8.',
 'Standing hypotheses: full CM, class number1, p>3 good ordinary; appendix sign−1. TheoremA.1 only guarantees nonzero height of an actual non-torsion algebraic point, not arbitrary pairing nondegeneracy after tensoring. Rational point has zero anticyclotomic projection, and the three projections in LemmaA.2 are pairwise independent linear forms.')
add('waldschmidt1979sigma','Author-hosted English translation of the1979 paper, §4 Theorem1 and §5 Corollary1 p.3; whole pp.1–3 read.',
 'Transcendence of algebraically twisted third-kind sigma value and sigma(u) exp(−u zeta(u)/2) in C7.7.',
 'Algebraic invariants and algebraic elliptic points, u0 nontorsion, u and u+u0 not poles, algebraic beta. The word algebraic point means algebraic wp-coordinate, not algebraic logarithm. The bare real norm contains an extra nonholomorphic Gaussian and is excluded.')

# Preserve every citation in the bibliography ledger even while an exact-source
# check is still open.  A retrieved file alone is never marked verified.
for key in contexts:
 if key not in refs:
  add(key,'Exact primary locator check pending in this working ledger.',
      'See the exact printed citation contexts; no theorem status is inferred from retrieval alone.',
      'Not yet promoted to verified; remaining checks will replace this record.',status='pending_exact_primary_check')
for alias,canonical in [('DuGuoKusakabeXie2026v1','DuEtAl2026v1')]:
 r=dict(refs[canonical]);r['citation_key']=alias;r['same_source_as']=canonical;r['citation_contexts']=contexts.get(alias,[]);refs[alias]=r
for key,explanation in {
 'CrRubin1991':'Complete original theorem text not obtained; metadata only. No additional hypothesis-free consequence is based on it. Verified replacement formulations are CrBDP2012 and CrCastella2025.',
 'bertrand1984':'Complete original Corollary3 and its lift convention not obtained. Unrestricted theta-lift criterion is withdrawn. Only the precisely reproduced p-adic nonvanishing theorem in Rubin AppendixA of agboola2006 is invoked.',
 'pham2025sigma':'Publisher abstract only; no proof or precise hypotheses opened, and no theorem is invoked from it.',
 'tate1983variation':'Original full paper not obtained; the actual invoked specialization statement is checked in Call–Silverman1993 and Silverman2006 below.',
 'silverman1983specialization':'Original full paper not obtained; the actual invoked specialization statement is checked in Call–Silverman1993 and Silverman2006 below.'}.items():
 if key in refs:
  refs[key]['status']='unverified_original_not_used_for_strengthening';refs[key]['opened_locator']=explanation;refs[key]['hypotheses_and_normalization_check']=explanation

(D/'references_verified.json').write_text(json.dumps(list(refs.values()),indent=2,ensure_ascii=False)+'\n')
credits=[]
for key in ['AC2026','Engel2026','DuEtAl2026v1','DuEtAl2026v2','Yang2026','Wang2026','ViaclovskyLog2026','ViaclovskyTwoParameter2026','ViaclovskyCombs2026','LiuRollenske2026','McHugh2018','Angella2018']:
 r=refs[key];credits.append({k:r[k] for k in ['citation_key','local_source','source_sha256','opened_locator','actual_use','hypotheses_and_normalization_check','status']})
(D/'source_credit_map.json').write_text(json.dumps(credits,indent=2,ensure_ascii=False)+'\n')
print('Saved',len(refs),'reference records and',len(credits),'source-credit comparisons.')
