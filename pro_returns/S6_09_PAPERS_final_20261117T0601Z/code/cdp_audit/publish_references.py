"""Record actually opened sources, with scope and file fingerprints where available."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3]; OUT=ROOT/'deliverables/work/cdp_audit'
D={x['key']:x for x in json.loads((ROOT/'reference_downloads/cdp_audit/downloads.json').read_text())}
more=ROOT/'reference_downloads/cdp_audit/downloads_foundations_more.json'
if more.exists(): D.update({x['key']:x for x in json.loads(more.read_text())})
components=ROOT/'reference_downloads/cdp_audit/downloads_components.json'
if components.exists(): D.update({x['key']:x for x in json.loads(components.read_text())})
topology=ROOT/'reference_downloads/cdp_audit/downloads_local_topology.json'
if topology.exists(): D.update({x['key']:x for x in json.loads(topology.read_text())})
classvii=ROOT/'reference_downloads/cdp_audit/downloads_classvii.json'
if classvii.exists(): D.update({x['key']:x for x in json.loads(classvii.read_text())})
singularity=ROOT/'reference_downloads/cdp_audit/downloads_singularity.json'
if singularity.exists(): D.update({x['key']:x for x in json.loads(singularity.read_text())})
for name in ['downloads_classification.json','downloads_periods.json','downloads_interfaces.json']:
 p=ROOT/'reference_downloads/cdp_audit'/name
 if p.exists():D.update({x['key']:x for x in json.loads(p.read_text())})
P='GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, writing run; 17 November 2026 UTC'
rows=[]
def add(key,title,url,locators,uses,scope,web_refs=(),download_key=None):
 d=D.get(download_key or key,{})
 rows.append({'key':key,'title':title,'url':url,'status':'verified in the specified scope','opened_locators':locators,'uses':uses,'verification_scope':scope,'own_check':P,'web_refs':list(web_refs),'local_pdf':d.get('path'),'sha256':d.get('sha256'),'download_status':d.get('status','not attempted in this checkpoint'),'not_verified':[]})
add('GS2014','Normal crossing properties of complex hypersurfaces via logarithmic residues','https://arxiv.org/pdf/1109.2612',
['arXiv:1109.2612v7, Theorems 1.1 and 1.3, p.3','Proposition 3.4, p.9; Corollary 3.5, p.10; proof of Theorem 1.3, p.12'],
['CDP A.2.1 inverse Jacobian/residue identification','CDP A.2.2 Jacobian-conductor inclusion','CDP A.2.3 normalization-residue normal-crossing criterion'],
'Opened and matched reduced hypersurface hypotheses. No free-divisor hypothesis from the later Corollary 3.7 is imported. The residue criterion is known; these algebraic identifications are re-derived.', ['turn18view0'])
add('Kulikov1981','On modifications of degenerations of surfaces with kappa=0','https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1953&what=fullteng',
['All four English pages, 339–342','Theorem 1-prime p.340; modification definition §2 p.339; finite reduction §§7–10 pp.341–342; corrections §11 p.342'],
['CDP C.2.UN.75 Hopf-minimum canonical-flat reduction','CDP UN77/81 restored ruled cleanup and UN84 stopped selection'],
'Theorem1-prime applies to good analytic degenerations with trivial canonical class on nearby fibres; class-VII components must attain the minimum canonical coefficient. Projectivity is not a hypothesis. Independently, §7 expressly states the selector needs only ruled current maxima; §8 removes H¹(dual complex)=0 and distinguished-component steps, inserts missing fibre links in actual smooth charts, assigns them orderq+1 and adds none for a maximal-order selected component. §9 proves finite full-positive-order card induction. This matches the stopped/cleanup uses without invoking the final theorem outside its hypothesis. Opened via web PDF; no successful direct-download hash claimed.', ['turn18view1','turn11view0','turn12view0','turn64view0'])
add('Kulikov1977','Degenerations of K3 surfaces and Enriques surfaces','https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1877&what=fullteng',
['Definition of good degeneration, p958; §§2.18–2.21 pp964–965','§§4.5–4.8.12 pp970–976; §§4.9–4.10.8 pp977–982','§4.11.2 and §§4.12–4.14.5 pp982–985; §§4.16.2–4.17 pp986–988'],
['CDP C.2.UN.75 retained-overlap interpretation of local modifications','CDP UN77/81 cleanup of actual sigma-atlas and UN84 stopped component selection'],
'Read the specified actual local contractions, typeI/II and chain/cycle selector, fibre minimization, reverse-order restoration of overlap, singular sigma-atlas, last-locally-blown-branch reordering and Lemma4.14 conditions(a)–(e). The maximum chosen last branch gives condition(e) because every local child has order one larger. The auxiliary resolution is diagnostic, not a retained global semistable stage. Read4.17 final smoothness and the same-receiver typeII balance. Original TheoremI is projective; the applications use the1981 explicit changes to its algorithm, not an unrestricted1977 theorem.', ['turn18view2','turn11view1','turn12view1','turn72view1','turn73view0','turn73view1','turn75view0','turn75view1','turn75view2','turn77view0','turn77view1'])
add('CDP2020','The algebraic dimension of compact complex threefolds with vanishing second Betti number','https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CDF2D04CFB35CEE105E10B188D97D68A/S0010437X19007802a.pdf/the-algebraic-dimension-of-compact-complex-threefolds-with-vanishing-second-betti-number.pdf',
['Published pp.680,684–685,692–694','Theorem 2.2, Corollary 2.3, Proposition 2.4; Lemmas 4.2–4.3; §7 endpoint inference and Proposition 7.3 through its ruled-surface step'],
['Working corrected global/relative criterion','Correction note exact p.692 endpoint implication','CDP A.4.2 constant genus-one family counterexample','CDP D.1.1–D.1.3 coinvariant correction'],
'Exact printed hypotheses and failed inferences opened. The original p.692 endpoint implication drops cotangent torsion. Proposition7.3 expressly permits constant normalized twists before concluding genus at least2. Lemma4.2 repeats the unsound direct-sum abelianization. No theorem-level refutation is inferred without the constructed global example.', ['turn23view0','turn22search6'])
add('CDP1998','The algebraic dimension of compact complex threefolds with vanishing second Betti number','https://arxiv.org/pdf/math/9607215',
['arXiv:math/9607215v1, pp.11–12, Lemma5.2(1)–(3)'],
['CDP D.1.1–D.1.2; working semidirect abelianization'],
'The opened preprint numbers the published Lemma3.2 as Lemma5.2. Its proof explicitly passes from a split group extension to a direct sum with full H1(fibre). The published page numbering has not yet been independently checked in a journal scan.', ['turn23view1'],download_key='CDP1998_preprint')
add('HKP2000','Group actions on S6 and complex structures on P3','https://arxiv.org/pdf/math/9812076',
['arXiv:math/9812076v1, p.2, Corollary1.3 and its complete proof; Corollary1.4'],
['INV E2.4 universal two-vector-field bound and the precise failed CDP dependence'],
'The universal h0(T)<=2 assertion is printed. The proof uses constancy of meromorphic functions attributed to CDP1998. It does not establish the bound independently of that input. The audit distinguishes this corollary from non-almost-homogeneity itself.', ['turn23view2'],download_key='HKP2000_preprint')
add('ACampo1975',"La fonction zêta d'une monodromie",'https://www.e-periodica.ch/cntmng?bot=1&pid=com-001%3A1975%3A50%3A%3A27',
['Theorem1, p.235 (PDF page4), formula inspected in rendered image','§2.1–§2.2, pp.237–241, proper analytic normal-crossing global boundary construction and fibration lemma'],
['CDP C.2.UN.11 monodromy-to-stratum Euler formula','Boundary retraction/normal-crossing support comparisons'],
'The source supports sum_{m|k} m chi(S_m) for the kth Lefschetz number, and its global construction is explicitly for a proper analytic map from a smooth space with normal-crossing divisor. Initial web bot failure was bypassed by downloading and opening the genuine journal scan. The formula was visually checked because OCR omitted symbols.', ['turn22search7'])
add('SchnellLecture3','MAT615 Lecture3: Holomorphic line bundles, Appell–Humbert theorem','https://www.math.stonybrook.edu/~cschnell/mat615/lectures/lecture3.pdf',
['Equations(3.3)–(3.10), pp.3–7; explicit exponential connecting two-cocycle and alternating Chern form'],
['Working prop:local-cusp-picard-obstruction exact c1=-2q sign','Working prop:analytic-ah-boundary factor extension','Working lem:analytic-support-specialization mixed-block sign'],
'Opened the actual author notes and matched the factor-of-automorphy and antisymmetrized logarithm convention. The bespoke descent/cusp support computations remain independently proved in the manuscript.', ['turn23view3'])
add('Guillot2024','On the singularities of complete holomorphic vector fields in dimension two','https://www.matem.unam.mx/~guillot/guillot-singularities.pdf',
['Theorem3.3 and complete proof, p.9','Theorem9.2 and preceding scope definition, p.28'],
['CDP C.2.UN.15/16 closure of the semicomplete locus on the smooth threefold and component','CDP C.2.UN.16/22 algebraic-dimension-zero birational holomorphic/fibration alternative'],
'Theorem3.3 expressly works on a complex manifold of any dimension; Theorem9.2 expressly covers compact complex surfaces with meromorphic fields semicomplete on their holomorphic locus. Thus neither Kählerness nor entire solutions are silently inserted.', ['turn29view0','turn31view0','turn31view1'])
add('Guillot2019','Meromorphic vector fields with single-valued solutions on complex surfaces','https://arxiv.org/pdf/1603.02288',
['Main Theorem and following clarification, p.2','Proposition22, p.25'],
['CDP C.2.UN.15 exclusion of general-type components','CDP C.2.UN.22 dense-leaf projective branch'],
'The main theorem requires compact Kähler surface and a Zariski-dense univalent maximal solution. The uses checked here are on projective models and supply semicompleteness, hence meet those hypotheses. Holomorphic branch is controlled by Proposition22; no non-Kähler use of this theorem is made.', ['turn29view1','turn31view2','turn30view3'])
add('DOT2000','Surfaces de la classe VII0 admettant un champ de vecteurs','https://ems.press/content/serial-article-files/42865?nt=1',
['Introduction p.256; opening of §2 p.260'],
['CDP C.2.UN.16 at most one holomorphic field on minimal classVII with b2>0','CDP C.2.UN.19 algebraic dimension zero of that class'],
'The exact dimension bound is stated under minimality,b1=1,b2>=1. These hypotheses are the ones used after descending the two fields to the same minimal model.', ['turn29view2','turn31view4'])
add('DOT2001','Surfaces de la classe VII0 admettant un champ de vecteurs, II','https://ems.press/content/serial-article-files/42912?nt=1',
['Theorem0.3, pp.641–642, full minimal-surface list'],
['CDP C.2.UN.16 classification with two holomorphic fields','CDP C.2.UN.22 nonnegative-Kodaira branches'],
'Opened the complete list and its compact minimal surface hypothesis. In algebraic dimension zero, elliptic Seifert alternatives are excluded by their fibration. The theorem is cited as established classification, not re-proved.', ['turn29view3','turn31view3'])
add('RR70','Complexe dualisant et théorèmes de dualité en géométrie analytique complexe','https://www.numdam.org/article/PMIHES_1970__38__77_0.pdf',
['§3, Theorem1, published p.81; dualizing-complex amplitude on p.89; Proposition2 and complete-intersection calculation p.91'],
['Compact singular or nonreduced Cartier-fibre Serre duality in working thm:cartier-duality and prop:cartier-duality-absolute','PUSH E.2.9 absolute fibre duality','UN65/68 Gorenstein SNC surface duality'],
'Original journal PDF read locally. Countable-at-infinity bounded-dimensional analytic spaces are allowed. On compact fibres the coherent groups are finite-dimensional and separated; the Cartier Gorenstein dualizing complex is an invertible sheaf shifted by dimension. A locally free twist reduces Ext to cohomology of its dual tensor the dualizing line. No smoothness or reducedness is inserted.',[],download_key='RamisRuget1970')
add('BS76','Algebraic Methods in the Global Theory of Complex Spaces','https://djvu.online/file/2hQiOnz8WuoQk',
['ChapterIII Theorem4.1, p.124, complete statement','ChapterIII Theorem4.12(i)–(iii) and proof, pp.134–135; cohomological-flatness criteria immediately before'],
['Proper finite free cohomology complexes and analytic jumping loci','Semicontinuity and constant-zero top-cohomology base change in working and PUSH E.2.9','Euler characteristic invariance in UN65/68'],
'Actual book transcription opened through web retrieval. Theorem4.1 is bounded when the coherent sheaf is flat over the base. Theorem4.12(ii) converse requires a reduced base; the uses on P1, discs and affine Picard lines meet it. Do not replace finite-complex reasoning on nonreduced bases by this converse. Direct HTML download returned an anti-bot challenge, not a copy of the book; no source hash is claimed.', ['turn46view0','turn48view0','turn48view1'])
rows[-1]['local_pdf']=None; rows[-1]['sha256']=None
add('Nakano1970','On the Inverse of Monoidal Transformation','https://ems.press/content/serial-article-files/41677',
['Main Theorem, published p.484; ordinary blowdown local conclusion'],
['CDP UN64 smooth ordinary blowdown of a projective-space-bundle divisor'],
'Original theorem statement read. It has both normal O(-1) condition alpha and an extra canonical condition beta. The latter is removed by Fujiki–Nakano1971; the original alone is not the cited sufficient theorem.', ['turn46view2'])
add('FujikiNakano1971','Supplement to On the Inverse of Monoidal Transformation','https://www.jstage.jst.go.jp/article/kyotoms1969/7/3/7_3_637/_pdf/-char/ja',
['Introduction p.637; §2 Theorem2-prime pp.640–641 and Proposition9-prime p.642 with its local chart conclusion'],
['CDP UN64 curve and point blowdowns with normal O(-1) on every projective fibre','Subsequent actual contraction records using UN64'],
'The supplement explicitly repairs the earlier cohomological proof and makes normal condition alpha sufficient. The local maps give ordinary blowups of smooth centres and glue off the exceptional divisor. UN64 supplies the prescribed holomorphic projective bundle and exactly this normal restriction.', ['turn46view1','turn47view2','turn48view2'])
add('Grauert1960','Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen','https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf',
['§6 HauptsatzI, HauptsatzII and HauptsatzIIa p59; IIa formula and complete proof visually inspected on originalPDF page58','§7 Satz2 p61, read together with the1963 correction'],
['Proper direct-image coherence; separation of coherence from base-change/jumping-locus claims','PUSH B4.11 analytic formal-functions comparison'],
'HauptsatzIIa is the analytic formal-functions isomorphism between the inverse limit of higher direct images of S/S.m_tilde^nu and the maximal-ideal completion of the stalk of R^i pi_* S. It requires a proper holomorphic map of complex spaces and coherent S, without projectivity or reducedness. Formula and full short proof were read in the original scan, rendered as reference_downloads/cdp_audit/Grauert1960_IIa.png. Its §7 Satz2 assertion about the failure locus must be read with the later correction. For closed analytic cohomology-jumping loci and base change this audit uses the separately opened BS76 finite-complex and flatness theorems.', ['turn50view2','turn52view4'])
add('Grauert1963','Berichtigung: Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen','https://www.numdam.org/item/PMIHES_1963__16__35_0.pdf',
['Entire two-page correction pp.35–36, particularly item2 p.36'],
['PUSH E.2.9 and working analytic-base-change source qualification'],
'Read all corrections. Item2 explicitly withdraws the closedness assertion for the locus where the §7 Satz2 base-change map is not bijective. It does not invalidate the proper-coherence theorem or the independently established finite-complex approach.', ['turn50view1','turn52view3'])
add('GrossSiebert2006I','Mirror symmetry via logarithmic degeneration data I','https://arxiv.org/pdf/math/0309070',
['arXiv:math/0309070v3: Definition1.60 pp.45–46; Theorem3.22 pp.95–97; Example3.30 p.106','Definition4.3 pp.108–109; complete units-to-residues comparison in Theorem4.14 pp.114–116','Theorems5.2 pp.128–129 and5.4 p.134, statements and the latter proof'],
['CDP UN71 central-log-space gluing classification after its analytic-to-algebraic comparison'],
'Opened the original preprint and matched the hypotheses. The classification is for proper reduced toric log Calabi–Yau algebraic spaces; no polarization is required by Theorem5.4. UN71 supplies algebraicity via its SNC conductor gluing and constant residue maps. Empty affine discriminant gives p=0 simplicity. The source classifies central log spaces, not analytic smoothing germs; actual proper smoothing is separately constructed in UN71.', ['turn50view0','turn52view0','turn52view1','turn52view2','turn53view0','turn53view1'])
add('Viaclovsky2026Combs','Combs and complex structures on the six-sphere','https://arxiv.org/abs/2610.10451',
['Supplied TeX dated7October2026: t:main (lines236–258), allfree (490–576), degrees (699 onward)','localquotient (1882–1901); degreechange (2139); normalbundle/parambundles (2149–2177)','paramspace (2182–2240), effective (2242–2285), initial bundles (2330–2428), smoothingbound (2454–2478)'],
['INV E2.1 known coherent degrees and dimensions','CDP E15 and INV E2.2 comparison with the previously established 8m-8 lower bound'],
'The actual supplied source was opened and its stated hypotheses matched, including m>=12, unchanged singular-fibre types and fixed limiting periods. It establishes det degree2m-1, nonnegative splitting, h(O) and a section-family lower bound8m-8. It does not establish the later exact tangent dimensions or smooth miniversal8m+1 germ; those require the separate complete E15 proof. No independent online metadata verification is claimed.',[])
vfile=ROOT/'sources/papers/arXiv_2610.10451_Viaclovsky_combs_src/Viaclovsky_Comb_S6_Draft_October_7_2026.tex'
rows[-1]['supplied_source']=str(vfile.relative_to(ROOT));rows[-1]['sha256']=hashlib.sha256(vfile.read_bytes()).hexdigest();rows[-1]['download_status']='supplied source opened';rows[-1]['aliases']=['ViaclovskyCombs2026']

add('Buchdahl1999','On compact Kähler surfaces','https://www.numdam.org/article/AIF_1999__49_1_287_0.pdf',
['Theorem11, printed p.297'],
['CDP C.2.UN.5 smooth central surface with b1=4 is Kähler'],
'The exact theorem statement was opened: a compact complex surface with even first Betti number is Kähler. The application supplies a smooth compact connected surface and b1=4 by the actual smooth family. The entire analytic metric proof was not audited.', ['turn79view0','turn80view1'])
add('Catanese2002','Deformation types of real and complex manifolds','https://arxiv.org/pdf/math/0111245',
['arXiv:math/0111245v2: Definition3.1 and Theorems3.2–3.3, p.9','Theorem4.6, full statement and proof, pp.13–14; Lemma4.7 and Proposition4.8, p.15'],
['CDP C.2.UN.5 smooth torus specialization and bielliptic deck-quotient classification'],
'Opened the torus deformation result and its proof, and the cohomological-torus criterion with closed holomorphic one-forms. The manuscript supplies its own Kähler Albanese argument. Opened the complete seven-type bielliptic list and the E×F/G definition, including translations on E and F/G=P1. These are established classification inputs; no audit of every classification proof is claimed.', ['turn79view1','turn80view2','turn80view3','turn81view1','turn81view2','turn82view1'])
add('AKMW2002','Torification and factorization of birational maps','https://arxiv.org/pdf/math/9904135',
['arXiv:math/9904135v4: §1.2.4 and Lemma1.3.1, including its full short proof, p.6','§5.1 analytic-extension remark'],
['CDP C.2.UN.3 elimination of the inverse bimeromorphic map by smooth blowups off the common open subset'],
'The elimination proof uses Chow flattening and principalization and expressly extends to analytic spaces. Its centres lie away from the common isomorphism locus. After shrinking the proper fibre tube, the vertical centres in this application are compact. The full weak-factorization theorem is not needed or claimed to have been audited.', ['turn79view2','turn80view4','turn80view5','turn81view0','turn82view2'])
add('Fujimoto1988Log','Logarithmic transformations on elliptic fiber spaces','https://scispace.com/pdf/logarithmic-transformations-on-elliptic-fiber-spaces-1uinrvp8jj.pdf',
['Original pp.91–92, definition of elliptic fibre space','Theorem2.8 and full proof, pp.96–97; Corollary2.10','§3 construction and Example3.4(1), pp.97–99'],
['CDP C.2.UN.6 credit for Kodaira-dimension-one components','CDP C.2.UN.6 explicit counterexample to Theorem2.8 and Corollary2.10 as printed'],
'The printed definition imposes properness, smooth source and base, connected fibres and generically elliptic fibres, with no Kähler or projectivity hypothesis. The weighted Hopf threefold [a:b:c] modulo (qa,q^m b,q^m c), mapped by [a^m:b:c] to P2, meets all these hypotheses and has a multiplicity-m line with self-intersection1. The original proof treats the normalization of xi^m=s_D^m as a connected degree-m Stein cover, although that equation splits into m graphs. The assertion about divisibility and the resulting P2 corollary fail; no blanket refutation of the paper is intended. The original example already supplies a Kodaira-dimension-one component. Actual journal pages were opened through web retrieval; the failed direct download is not recorded as a PDF.', ['turn79search12','turn80view0','turn81view3','turn81view4','turn81view5','turn82view0'])

add('Nemethi1991Join','Generalized local and global Sebastiani–Thom type theorems','https://www.numdam.org/article/CM_1991__80_1_1_0.pdf',
['§2.1, TheoremL1 p.2; Example2.4(a) p.3'],
['CDP A5.15 independent join-model check for nonisolated Hirzebruch germs'],
'The statement expressly allows arbitrary analytic germs g and h. The auxiliary p=c+d has connected Milnor fibre, so its hypothesis is met. Example2.4(a) identifies the direct sum with the join. The manuscript separately computes the annulus components and wedge ranks and constructs an explicit spherical cycle, including reducible monomials. The full general proof of the theorem was not audited.', ['turn96view0'])
add('MPW2005Hirzebruch','The boundary of the Milnor fiber of Hirzebruch surface singularities','https://arxiv.org/pdf/math/0509451',
['arXiv:math/0509451v1: scope p.2; Theorem4.1 and comments pp.6–7','Theorem4.2(1)–(3) p.7; rational Euler formula p.8; Lemma4.6 and complete proof p.11'],
['CDP A5.15 independent Seifert boundary and intersection-rank check'],
'The body permits 1≤k≤l, including equality, although the abstract uses a strict inequality. Its irreducibility hypothesis is gcd(m,k,l)=1 and is retained in the manuscript supplementary calculation. The genus, rational Euler number and lens-space specialization match after (m,k,l)=(a,b,c), with b and c exchanged if necessary. The elementary congruence proof of Lemma4.6 was read; the entire Seifert-foliation proof was not audited.', ['turn96view1','turn97view1','turn97view2'])
add('vanStraten1987','Weakly Normal Surface Singularities and Their Improvements','https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/DvS-Publikationen/DvS_1987_weakly%20normal%20Surface%20Singularities%20and%20their%20improvements.pdf',
['§§2.2.2–2.2.5, printed pp.60–61, original PDF pages63–64'],
['CDP C2.CR2 analytic canonical-module defect and length comparison'],
'Opened proper analytic duality, the proper bimeromorphic vanishing theorem for smooth source, and the normal Cohen–Macaulay isolated-singularity canonical-form defect. These exactly give length(ω_T/pi_*ω_Z)=length(R¹pi_*O_Z). The source attributes duality to RRV and vanishing to Grauert–Riemenschneider; this record is an opening of the thesis, not a claim that those two original papers have both been opened.', ['turn97view0','turn100view1','turn100view2','turn100view3','turn105view0'])
add('Milnor1968','Singular Points of Complex Hypersurfaces','https://djvu.online/file/kCFrJq27uCPRi',
['Lemma6.1 and complete proof pp.55–56','AppendixB LemmasB1–B3 and positivity proof pp.111–114'],
['CDP A5.17 Milnor boundary transversality and morsification of isolated critical points'],
'Read the actual book transcription at the specified pages. The boundary submersion argument uses curve selection; the gradient perturbation creates a nonempty cluster of nondegenerate critical points by positivity of local degree. The manuscript supplies its own proper boundary transport into the global torus and the sphere self-intersection. No downloaded book file is claimed.', ['turn100view0','turn103view1','turn103view2','turn105view1'])
add('Steenbrink1999','Cup products and mixed Hodge structures','https://arxiv.org/pdf/math/9902134',
['§3 Lemma1, Theorem1 and full residue proof, Corollaries1–2, pp.5–7','§4 equation(3) and excision comparison, pp.8–9'],
['CDP C2.MH1 restricted logarithmic complex and actual support-to-restriction arrow'],
'The source starts with a complete smooth algebraic ambient space. The matched local proof is holomorphic-coordinate residue algebra; its graded terms are de Rham complexes of intersections with the stratum. MH1 explicitly extends that construction to an analytic neighbourhood whose compact strata are projective and proves its support weight bound by Thom/Gysin complexes. The global complete-algebraic theorem is not cited as if its ambient hypothesis were absent.', ['turn108view0','turn110view0','turn112view0','turn112view1','turn114view0'])
add('Rossi2017','A small and non-simple geometric transition','https://arxiv.org/pdf/1211.6329',
['arXiv:1211.6329v3: §3 Proposition4, construction and local resolution calculation pp.10–11','Remark5 Hodge-number comparison p.20'],
['CDP C2.UN8 credit for Namikawa cuspidal self-product, graph blowups and known ambient Hodge numbers'],
'Opened the original double graph-blowup construction and two-projective-line exceptional chain, plus h11=21 and h21=3. These construction and Hodge-number claims are known. The manuscript separately derives the integral central-fibre groups, generic Picard ranks and exact obstruction to a nonzero local character. The later local-deformation assertions in Rossi are not used or audited here.', ['turn108view1','turn110view1','turn110view2','turn112view2','turn114view1'])

add('Dloussky2006','On surfaces of class VII_0^+ with numerically anticanonical divisor','https://arxiv.org/pdf/math/0406387',
['arXiv:math/0406387v3: Theorem0.2 p.2; Lemma2.22 and following paragraph p.15','Corollary2.25 and proof pp.16–17; Proposition2.27 and complete proof pp.17–19; Proposition2.29 and proof p.19','Theorem2.38 and its proof pp.24–25, with the preceding square-zero Enoki/Inoue case'],
['CDP VII1 torsion-anticanonical support and rational-curve configuration','CDP UN17/19 and subsequent class-VII recognition restricted to surfaces with the required anticanonical divisor'],
'Matched the numerically anticanonical hypothesis, the connected cycle-with-trees or Inoue alternatives, and the prohibition of isolated tree support. Theorem2.38 itself excludes square-zero divisors; the immediately preceding paragraph handles that separate Enoki case and characterizes the anticanonical parabolic Inoue case. VII1 independently uses positivity of the Gauduchon degree to force coefficient one on its square-zero cycle. The complete proofs of the listed elementary support statements were read; the entire classification proof through every earlier lemma was not audited.', ['turn137view0','turn139view2','turn139view3','turn139view4','turn139view5','turn139view6'])
add('DOT2003','Class VII_0 surfaces with b_2 curves','https://www.jstage.jst.go.jp/article/tmj/55/2/55_2_283/_pdf/-char/en',
['Introduction p.283; §1 pp.284–285 including Lemma1.1 and its proof','§3 p.296, actual divisor-neighbourhood and fundamental-group identifications'],
['CDP VII1 rational-curve count and intermediate cycle-with-trees configuration','Class-VII divisor comparisons retaining the actual neighbourhood maps'],
'The original publisher PDF states at most b2 rational curves for minimal class VII surfaces and exactly b2 for surfaces with a global spherical shell. Its intermediate configuration has one cycle with attached trees; the opened page296 identifies the actual inclusion-induced fundamental groups. The manuscript supplies the point-blowup transfer and does not invoke a classification of all class VII surfaces without an anticanonical divisor. The full global-spherical-shell theorem proof was not audited.', ['turn137view1','turn139view1'])
add('KamenovaTori','Degenerations of 2-Dimensional Tori','https://www.math.stonybrook.edu/~kamenova/homepage_files/degen.pdf',
['All four author-hosted pages, especially Theorem3.1 and proof pp.2–3'],
['CDP UN65 and IRR1 comparison with the known Kähler semistable classification'],
'Read the entire four-page manuscript. It assumes a Kähler total space and trivial total canonical line. Its list includes an elliptic-ruled path; CDP supplies a separate residue and finite-trace exclusion of that path in its exact setting. The source is used for attribution and comparison, not to remove its Kähler hypothesis or to establish the new analytic classification. No publication year is stated in the source or inferred here.', ['turn137view2','turn139view0'])
add('HuybrechtsK3Draft','Lectures on K3 Surfaces','https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf',
['Author-hosted prepublication draft, Chapter1 Example1.3(iii), pp.8–9, including both quotient/blowup maps and canonical/cohomology calculation'],
['CDP UN13 attribution for the classical Kummer construction'],
'Opened the exact construction of the resolution of A/{±1}, the alternative blow-up-then-quotient map, and the form and trace calculation making the result K3. UN13 retains its independent threefold quotient charts, support cohomology and vertical-refinement proof. The rest of the book is not recorded as read.', ['turn137view3'])

add('MerleTeissier1977',"Conditions d’adjonction, d’après Du Val",'https://www.numdam.org/item/SSS_1976-1977____A16_0.pdf',
['Exposé14, §2 Theorem2.1.1 and complete toric determinant proof; Corollary2.1.3 (PDF pages14–16, visually inspected)'],
['CDP D4.1 and RAT6 geometric genera of cubic ADE suspensions','CDP RAT8 cusp-plus-two-branches and four-transverse-branches Newton computations'],
'The theorem requires an isolated hypersurface singularity nondegenerate for its Newton polyhedron. The original proof identifies the adjunction ideal by strict interior membership after multiplying by every coordinate; Corollary2.1.3 counts strictly positive lattice points outside that interior, so the inequality in the manuscript is correctly non-strict. The ADE and two additional equations have their face nondegeneracy checked in the proof. The determinant proof and displayed hypotheses were read; the full background theory of toric resolution is not claimed as independently reproved.', ['turn145view0'])
add('Steenbrink1989Spectrum','The spectrum of hypersurface singularities','https://www.numdam.org/article/AST_1989__179-180__163_0.pdf',
['§1, printed pp.165–167: weighted Jacobian-monomial formula, Thom–Sebastiani convolution theorem and geometric-genus interval'],
['CDP D4.1 and RAT6 weighted suspension monodromy, geometric genus and link Betti numbers'],
'Opened the original scan at all three pages. The monomial formula has spectral value sum((a_i+1)w_i)-1; the geometric-genus interval is(-1,0], and convolution adds one. The uses here are isolated weighted homogeneous germs, hence have semisimple monodromy; the manuscript separately explains the Milnor-fibre variation and exceptional-intersection comparisons giving link b1. The general nonisolated spectrum theorem is not needed or independently audited.', ['turn145view1'])
add('Arnold1976NormalForms','Local normal forms of functions','https://webhomes.maths.ed.ac.uk/~v1ranick/papers/arnold15.pdf',
['Analytic equivalence and normal-form conventions pp.87–88; §1 I.1.0 simple A–D–E list p.92','§2 notation p.100 and determinator items2–9 p.101, including E6/E7/E8 weighted initial forms'],
['CDP RAT6 analytic normal forms for all reduced plane germs of delta at most five'],
'Matched actual analytic-equivalence conventions and the zero-modality A–D–E forms. RAT6 supplies the exhaustive low-delta branch/Puiseux case analysis; the opened determinator gives the analytic reduction of its weighted initial forms. This is not an attribution of the entire low-delta argument to the source, nor a claim to have checked every proof in the article.', ['turn145view2'])

add('RRV71','Dualité relative en géométrie analytique complexe','https://gdz.sub.uni-goettingen.de/id/PPN356556735_0013',
['Introduction equation(1), original p.261; §1 proper-duality trace quasi-isomorphism p.264','§2 relative trace, pp.265–268; Proposition2.1 continuity statement p.266'],
['PUSH E3.1 analytic relative duality for proper flat Gorenstein surface families over curve charts','CDP CR2 proper analytic duality for a resolution of a normal Cohen–Macaulay surface'],
'Opened the original journal scan through its public GDZ IIIF manifest and visually checked pp.261,264,265,266 after reading the text of §§1–2. The introduction explicitly asserts that equation(1) is an isomorphism for a proper morphism of complex analytic spaces; §1 writes the required Rf_*RHom(F,K_X•)→RHom(Rf_*F,K_Y•). No projectivity or Kähler hypothesis occurs. For E3.1 the smooth total space and base give absolute dualizing complexes ω_Y[3] and ω_U[1]; projection and cancellation give Rp_*ω_Y/U[2]≅RHom(Rp_*O_Y,O_U), and the independently checked locally free cohomology gives the degree−2 edge. Proposition2.1 is the continuity step for the trace construction, not a theorem numbered as the general duality result. The article’s remaining functional-analytic proofs in §§3–4 were not audited.',
['turn123view0','turn125view0'])
rows[-1]['aliases']=['RRV71push','RamisRugetVerdier1971']
rows[-1]['original_page_files']=json.loads((ROOT/'reference_downloads/cdp_audit/RRV71_pages.json').read_text())
rows[-1]['manifest_url']='https://manifests.sub.uni-goettingen.de/iiif/presentation/PPN356556735_0013/manifest?version=8b7f2484'
rows[-1]['manifest_sha256']=hashlib.sha256((ROOT/'reference_downloads/cdp_audit/RRV71_manifest.json').read_bytes()).hexdigest()
rows[-1]['download_status']='original journal pages261–268 downloaded; inspected in the specified scope'
rows[-1]['not_verified']=['Complete functional-analytic proofs of §§3–4 were not audited.']

add('Peters2021','On complex surfaces with definite intersection form','https://nyjm.albany.edu/j/2021/27-32p.pdf',
['Published pp842–843, Noether formula(2), Proposition2.1 and complete classification table Theorem2.2'],
['CDP A5.2 negative holomorphic Euler classification','CDP NC4 non-Kähler normalization invariants','CDP C3.1 preliminary surface list'],
'Original published table opened. All Chern numbers refer to minimal models; blowing up preserves coherent Euler and adds one to topological Euler. This supplies the stated numerical branches, not a proof of the full Enriques–Kodaira classification.', ['turn158view0','turn162view0'])
add('Peters1990','Compact Complex Surfaces','https://cpeters1.win.tue.nl/ConfsAndSchools/Canada/surface.pdf',
['Front matter: Canadian Mathematical Society Summer Meeting, June1990','Theorem1.1 p6; Theorem3.1 pp9–10 and surrounding definitions'],
['CDP C3.1 full preliminary classification','CDP C3.7 even-b1 Kähler criterion'],
'Author-hosted lecture text opened. The compact complex surface hypotheses match. The classification theorem is imported as known; its full historical proof is not asserted to have been audited. Publication details beyond the supplied front matter are not inferred.', ['turn158view2','turn161view5','turn163view1'])
add('BMS2012','Three manifold groups, Kähler groups and complex surfaces','https://mathweb.tifr.res.in/~mahan/kahler3fld.pdf',
['Author PDF dated27October2011, Theorem3.2 p16','Opening of §3.3 pp17–18'],
['CDP NC4 minimal non-Kähler elliptic Euler zero','CDP C3.12 elliptic/classVII alternatives and orbifold quotient comparison'],
'Matched only the odd-b1 elliptic-or-classVII classification, Euler-zero minimal elliptic conclusion and fibration group sequence. The paper’s unrestricted Hopf cyclic-group wording is not used; secondary Hopf groups need not be cyclic. No unrelated three-manifold classification argument is imported.', ['turn158view1','turn161view2','turn162view2'])
rows[-1]['not_verified']=['Do not use this record to assert that every Hopf surface has infinite cyclic fundamental group.']
add('Teleman2008','Gauge theoretical methods in the classification of non-Kählerian surfaces','https://www.i2m.univ-amu.fr/perso/andrei.teleman/documents/postnikov.pdf',
['Author PDF dated3April2008, introduction pp1–2, especially p2 classVII b2=0 statement'],
['CDP C3.1 Hopf/Inoue classification; VII branch'],
'The exact minimal classVII b2=0 statement and definition of Hopf/Inoue surfaces opened. The survey credits Bogomolov and the completed Teleman and Li–Yau–Zheng proofs. Those complete classification proofs were not rechecked here.', ['turn158view3','turn161view6'])
add('BBK2019','Classifying VII0 surfaces with b2=0 via group theory','https://arxiv.org/pdf/1709.00062',
['arXiv1709.00062v3,20May2019, Theorem1 p1'],
['CDP C3.1 precise finite-etale-cover scope'],
'The original theorem gives a Hopf or Inoue finite etale cover. This qualification is retained in the fibre exclusions; the article’s complete group-theoretic proof is not claimed checked.', ['turn158view4'])
add('Kawai1969','On compact complex analytic manifolds of complex dimension3, II','https://www.jstage.jst.go.jp/article/jmath1948/21/4/21_4_604/_pdf/-char/en',
['Published pp604–605 Theorem1 and Proposition2','Proposition2 entire relative period, translation-gluing and compactification proof pp605–608','Following corollary p608 read to separate it from the imported construction'],
['CDP C3.7 relative Albanese map for bielliptic fibres'],
'Full Proposition2 proof read in the original PDF. The source’s selected divisor need not be invariant: the CDP proof uses its finite orbit sum, after resolution, and takes the image of the induced projective map. This preserves the Albanese curve and supplies the necessary linearization. The later multiple-fibre corollary is not used.', ['turn163view0'])
add('SS2002','Irreducible degenerations of primary Kodaira surfaces','https://arxiv.org/pdf/math/0001077',
['arXivmath/0001077v2, §1 pp2–3: degree, intrinsic Picard quotient and (d,j,alpha) coordinates','Definition2.1 and Propositions2.4–2.6 with full proofs pp4–6','Proposition3.1 with full contraction-normal-form proof pp6–7','Proposition4.1 with full proof p13'],
['CDP C3.8 Hopf normal forms','CDP C3.9–10 intrinsic primary-Kodaira moduli coordinate','CDP A4.5 normalization cases and translation gluing'],
'The admissibility definition requires irreducible normal crossings, d-semistability and trivial dualizing line, without assuming an existing Kodaira smoothing. The normalized surface cases, diagonal Hopf criterion and ruled translation criterion match these hypotheses. In §1 the positive-degree class fixes the inversion ambiguity in C*.', ['turn161view0','turn162view3','turn179view1','turn179view2','turn179view3'])
add('Borcea1984','Moduli for Kodaira surfaces','https://www.numdam.org/article/CM_1984__52_3_373_0.pdf',
['Introduction pp373–374, fixed differentiable type','§3 equations(9)–(12), pp376–377; Remark1 complete holomorphic period family p377','Theorem3 and proof pp378–379; Theorem4 and Remark2 p380'],
['CDP C3.9–10 primary-Kodaira Picard/moduli comparison and actual local product','CDP D1.12 invariant-form cup product'],
'Opened the complete-family statement and its explicit quotient construction, the period-line classification and the product C times punctured-disc moduli. The C3.10 local product follows by a holomorphic map into a countable integral-cohomology orbit; central shear effects are computed independently in CDP.', ['turn164view1','turn175view1','turn176view1','turn177view2'])
add('Steenbrink1976','Limits of Hodge structures','https://www.academia.edu/47027671/Limits_of_Hodge_structures',
['Original authored scan transcription, §2.1 p234','Theorem2.18 and full proof pp237–238; §2.19, Proposition2.20 and proof, Theorem2.21 pp238–239'],
['CDP D2.3 logarithmic period comparison with arbitrary multiplicities','CDP C3.10 holomorphic extension of a constant H2 frame and projection to R2O'],
'Section2 assumes a proper holomorphic map, smooth connected total space, smooth punctured family and normal-crossing support. It does not assume Kählerness. The relative logarithmic complex is locally free in direct hypercohomology; residues lie in[0,1) and exponentiate to monodromy. Thus identity monodromy forces zero residue. Later mixed-Hodge assertions have additional hypotheses and are not imported by this record.', ['turn164view2','turn175view2','turn176view0','turn177view3'])
rows[-1]['not_verified']=['No unrestricted non-Kähler global invariant-cycle or Hodge-degeneration theorem is claimed.','The complete proofs of all preliminary local lemmas in §§1–2 were not newly rederived in this check.']
add('Inoue1974','On surfaces of class VII0','https://www.digizeitschriften.de/download/pdf/356556735_0024/log19.pdf',
['Original indexed journal scan, Propositions2 and5 and full proofs pp274–275,280','Propositions3–4 and full proofs pp277–279; explicit transition formula in Proposition4'],
['CDP C3.12 rigidity and complete S+ family with constant first-coordinate affine transformations'],
'The original propositions establish rigidity for SM and S− and a locally complete one-parameter S+ family. Its parameter changes only z; w_i=alpha^m w_j+a has constant real-affine coefficients. The full local-completeness Kodaira–Spencer argument was read. The remaining classification §§5–9 is outside this check.', ['turn175view0','turn176view2','turn176view3','turn176view4','turn177view0','turn177view1'])
add('Kodaira1963II','On compact analytic surfaces: II','https://it.scribd.com/document/480913137/kodaira1963-II',
['Public transcription of original Annals77(1963)563–626 scan','Definition and relative-minimality hypothesis pp563–564; Theorem6.2 pp564–566, proof opening pp566–568','TableI and Theorem9.1 p604; group-law formulas on p605'],
['CDP UN20/22/29/33/66/67 elliptic-fibre types and identity-monodromy comparisons'],
'Opened the original theorem, including its no-exceptional-fibre-curve hypothesis. The source allows analytic elliptic surfaces over compact curves, not just projective total spaces. Fibre types and multiplicities were read. The TableI OCR is partly damaged; exact individual monodromy matrices are not certified from that transcription alone.', ['turn174view0','turn175view3'])
rows[-1]['not_verified']=['Exact individual TableI matrix entries require visual verification; the present record does not certify those OCR-damaged entries.']

add('Brunella1999Forms','On holomorphic forms on compact complex threefolds','https://ems.press/content/serial-article-files/42850',
['Original published PDF title page p642','§2 pp648–650: standing a(M)=1 and nonclosed-global-one-form hypotheses; Lemmas4/5 and full proofs; Proposition2 conclusion'],
['CDP records/D_notes.md relative-Albanese comparison preceding the completed C3.10 proof','Clarifies why a compactified relative Albanese cannot be imported for primary Kodaira fibres'],
'The original author is Marco Brunella; the EMS landing-page attribution to Luis Paris is erroneous and is not used. Lemma5 constructs the elliptic relative Albanese over the smooth open base and expressly permits a noncompactifiable quotient. Its boundary-integral proof shows closedness of an already existing global one-form via a uniform positive lower bound on areas of compact curves. It does not construct a global one-form or compactify the quotient. The final CDP C3.10 proof uses Borcea and logarithmic periods instead, so this citation is a methodological comparison, not a dependency of that completed theorem. This is the CMH74(1999)642–656 paper, distinct from Brunella’s Doc.Math.4(1999)451–462 sphere paper.', ['turn188view0','turn189view0'])
rows[-1]['aliases']=['Brunella1999']
rows[-1]['not_verified']=['No compactifiability assertion for the relative Albanese is supported.','The remaining integrable-form and foliation theorems of §§1/3 are outside this specified check.']

add('KhaledTeleman2026','On the classification of Inoue surfaces','https://arxiv.org/pdf/2406.15158',
['arXiv2406.15158v4,13July2026, §§2.1–2.3 pp6–11','Definitions2.5/2.16/2.25, Remarks2.7–2.8/2.18–2.21/2.27','TypeIII double-cover statement p14'],
['CDP C3.12 exact surface-group presentations, affine first coordinates and finite-cover type comparisons','CDP A4.9 local-system eigenvalue assertions'],
'Read the original affine generators and complete stated group normal forms. TypeI has Z^3 semidirect Z with real eigenvalue alpha>1; typeII has the Heisenberg subgroup and alpha,alpha^-1 on its rank-two quotient; typeIII has alpha,-alpha^-1 and inverts the central generator, with a typeII double cover. Every first coordinate is alpha^m*w+a with a real. This record does not import the article’s later full biholomorphism classification or claim its entire proof audited.', ['turn164view3','turn172view3'])

add('Wang2026','A complex rational homology six-sphere','https://arxiv.org/abs/2609.11541',
['Supplied original source order_two_rational_homology_sphere_new.tex, intro:main and main:theorem','Complete proofs of fill:tate/fill:rankone, fill:a2, fill:good and fill:log, lines294–671','Complete mon:jacobi-lemma and mon:representation proofs, lines907–1027'],
['CDP D1.6 actual compact example and exact integral-homology theorem','CDP D1.13 canonical-line computation through the actual fillings'],
'Opened the supplied source, matched the primitive (2,1) rank-one exponent, the q=z0*z1*z2 rank-two charts, the normalized cubic comparison v->r^2*v and the free invariant translation. The named local-filling and displayed monodromy proofs were read in full. The main integral-homology theorem is imported at its exact statement; this record does not claim an independent audit of its entire topology section.', [])
rows[-1]['local_source']='sources/papers/arXiv_2609.11541_Wang_src/order_two_rational_homology_sphere_new.tex'
rows[-1]['source_sha256']=hashlib.sha256((ROOT/rows[-1]['local_source']).read_bytes()).hexdigest()
rows[-1]['download_status']='user-supplied original source opened in specified scope'
rows[-1]['not_verified']=['The complete integral homology calculation and cited Mumford/Engel construction theorems are not independently audited by this source-opening record.']

add('BrinzanescuMoraru2005','Holomorphic rank-2 vector bundles on non-Kähler elliptic surfaces','https://arxiv.org/pdf/math/0306191',
['arXivmath/0306191v3, section2 pp3–6','Lemma2.2 with complete cyclic-cover proof p4; principal-bundle and Picard automorphy formulas pp5–6'],
['CDP INT1 actual finite cover and identity component of the elliptic restriction kernel','CDP INT2–3 non-Kähler elliptic normalization/conductor comparisons'],
'The exact hypothesis is a minimal non-Kähler elliptic surface over a smooth compact connected curve. The source supplies its fixed Jacobian, smooth multiple fibres, an actual cyclic cover removing multiplicities and the principal model Theta* modulo tau. The Picard description is by base pullbacks and constant automorphy factors; restricting the latter to C*/tau^Z has discrete kernel tau^Z. The CDP proof separately checks the reduced multiple-fibre isogeny and its Gauduchon-degree consequence. No rank-two vector-bundle classification theorem is used.', ['turn195view0','turn197view0','turn197view1','turn197view2'])
add('DlousskyTeleman2012','Infinite bubbling in non-Kählerian geometry','https://arxiv.org/pdf/1012.5247',
['arXiv1012.5247v2, Remark2.7 and its preceding scope paragraph, p9'],
['CDP UN17 and INT1–2 classification of zero-real-Chern effective divisors on a minimal classVII surface'],
'The source states the complete Hopf-or-Enoki alternatives for a nonempty homologically trivial effective divisor on a MINIMAL classVII surface. The application first kills integral torsion and uses Poincaré duality; it then descends the support conclusion. The source cites the established classification, and no audit of the entire classification or of this paper’s infinite-bubbling proof is claimed.', ['turn195view1','turn197view3'])
add('Khaled2024Hopf','Real structures on primary Hopf surfaces','https://arxiv.org/pdf/2310.05265',
['arXiv2310.05265v2, Definition1.3 and all five contraction normal forms, p3','Theorem2.1 and full centralizer table, p5, visually inspected'],
['CDP UN19/38/40 primary Hopf contraction and automorphism normal forms','CDP UN43 exact secondary nonlinear deck calculation input'],
'Matched the primary-cover hypotheses, all diagonal/resonant/nonlinear cases and the displayed centralizers. The source expressly attributes this classification to Kodaira and Wehler; the full historical classification proof is not newly audited. Its real-structure theorems are not used.', ['turn195view2','turn197view4'])
rows[-1]['not_verified']=['The full original Kodaira/Wehler classification proofs were not read in this source-opening event.']
add('Kato1975Hopf','Topology of Hopf surfaces','https://www.jstage.jst.go.jp/article/jmath1948/27/2/27_2_222/_pdf/-char/en',
['Original introduction p222, finite-index contraction and nonabelian-linear alternatives','Section3 complete nonlinear abelian deck-group calculation, pp230–232, visually read in the scan'],
['CDP UN43 nonlinear secondary Hopf finite deck group and coprime root-order condition'],
'For a nonlinear contracting generator the original calculation gives a finite torsion element (z,w)->(a^r z,a w); finite order kills the resonant shear, and freeness gives gcd(order(a),r)=1. All intermediate derivative/eigenfunction equations were checked visually. The diagonal sentence on p230 is used only under the a=0 nonresonance hypothesis of the CDP proof; it is not imported as an unrestricted diagonal-centralizer assertion. No diffeomorphism-classification theorem is used.', ['turn195view3','turn196view4'])
rows[-1]['not_verified']=['No certification of the entire diffeomorphism classification or the general resonant diagonal centralizer claim.']
add('Nakamura2008VII','Survey on VII0 surfaces','https://www.math.sci.hokudai.ac.jp/~nakamura/70surfaces080306.pdf',
['Author survey dated14April2008, section1.1, Theorems1.1.1–1.1.2 on p2, visually read'],
['CDP UN19/38 finite unramified primary Hopf cover for the algebraic-dimension-zero branch'],
'Theorem1.1.2 assumes b1=1,b2=0 and no nonconstant meromorphic functions, and relates existence of a curve to a finite unramified primary Hopf cover. This is exactly the specified a=0 application. The displayed contraction and positive-power resonance criterion were also opened. The adjacent Theorem1.1.3 and the rest of the survey are not imported by this verification record.', ['turn195view4','turn197view5'])
add('Horikawa1974','On deformations of holomorphic maps II','https://www.jstage.jst.go.jp/article/jmath1948/26/4/26_4_647/_pdf/-char/en',
['Section4 Definition4.1/Lemma4.2 p648; equations4.3–4.5 and Theorem4.4 p649','Section6 Theorem6.1 and its displayed proof pp660–661'],
['CDP E6 map-obstruction Cech cocycles and the exact comparison with the older stability theorem'],
'The original theorem requires H1(T_X)->H1(f*T_Y) surjective AND H2 injective. E6 does not import that theorem without the second hypothesis: it uses its explicitly written source-torus unobstructedness and the full independent small-extension calculation. The original coordinate compatibility and cocycle formulas were read. The entire convergent construction in the cited earlier PartI and section5 was not independently audited.', ['turn205view2'])
rows[-1]['not_verified']=['No claim that H1 surjectivity alone is the hypothesis of Horikawa Theorem6.1.']
add('Douady1966',"Le problème des modules pour les sous-espaces analytiques compacts d'un espace analytique donné",'https://www.numdam.org/article/AIF_1966__16_1_1_0.pdf',
['Introduction p1 footnote allowing nilpotent local rings','Section9.7 Theorem1 and complete displayed proof pp83–84; section9.8 Theorem2/proof pp84–85','Section10.1 Proposition1 and proof p86; section10.2 Theorem1 and proof p87'],
['CDP E6 analytic representability and open graph locus over nonreduced parameter germs'],
'The original graph theorem is section10.2, not an Appendix, and is stated for a fixed compact source. The corrected E6 block explicitly constructs its required relative graph germ using the absolute Douady space, the unit in a finite cohomology complex, and the original open isomorphism-locus proposition. The existence and finiteness statements permit analytic spaces with nilpotents. Their displayed final proofs were read, but the preceding eighty-page Banach-analytic construction was not wholly re-audited.', ['turn205view3'])
rows[-1]['not_verified']=['The fixed-source graph theorem is not by itself a statement of relative representability for a varying compact source.','The complete Banach-analytic construction in sections1–8 was not independently audited.']
add('Mumford1972','An analytic construction of degenerating abelian varieties over complete rings','https://www.numdam.org/article/CM_1972__24_3_239_0.pdf',
['Entire section6, published pp264–268, including Propositions6.1/6.3/6.7, Corollaries6.4–6.6 and condition(D)'],
['CDP C2c polyhedral orbit correspondence, unimodular central model and polarization data'],
'The original base is a complete discrete valuation ring. Its polyhedral correspondence gives components from vertices and orbit dimension complementary to face dimension, and condition(D) states regularity for unimodular simplices. The source omits the general proof of(D) and Proposition6.7. The corrected C2c proof independently gives the special integral fan, smooth charts and convergent complex-disc quotient with free properly discontinuous lattice action and compact fundamental-domain proof; analytic convergence is not attributed to a theorem stated only over the complete ring.', ['turn205view4'])
rows[-1]['not_verified']=['No formal-to-convergent analytic theorem is inferred from the title or from section6.','The source omits proofs of condition(D) and Proposition6.7; the audit does not label those omitted general proofs read.']
add('LRS2019','The complex geometry of a hypothetical complex structure on S6','https://arxiv.org/abs/1912.09719',
['Supplied original main.tex lines772–837: theorem main2 new, higher-direct-image and effective-divisor lemmas, exceptional-cubic example','Entire graph proof and following correction remark, lines837–958'],
['CDP E2 and E17 corrected graph argument for a nonholomorphic meromorphic pencil','CDP C1 endpoint-vanishing credit and CDP1998 correction history'],
'The complete graph proof in the20December2019 arXiv version was read. The weight induction, every-full-fibre requirement and exceptional-divisor cohomology mechanism were matched to E2/E17. The CDP return explicitly supplies the correct adjunction sign, coherent-sheaf support/embedded-point condition, all full-fibre layers and actual pencil-divisor higher-image calculation; these repairs are distinguished from the original proof. The arXiv record gives the related2018 journal publication, but the check is of the2019 version and does not silently equate the two texts.', ['turn208view0'])
rows[-1]['local_source']='sources/papers/arXiv_1912.09719_Lehn_Rollenske_Schinko_src/main.tex'
rows[-1]['source_sha256']=hashlib.sha256((ROOT/rows[-1]['local_source']).read_bytes()).hexdigest()
add('Lagrange1770',"Démonstration d'un théorème d'arithmétique",'https://yuvalfilmus.cs.technion.ac.il/Manuscripts/Lagrange%20four%20square%20theorem.pdf',
['Retypeset original memoir, TheoremII CorollaryII, final page6; memoir provenance stated on p1'],
['CDP UN24 rational four-square construction of a nonzero isotropic divisor class'],
'Opened the exact original statement that every integer is a sum of at most four integer squares, with its displayed multiplicative identity. For a positive rational a/b the application to ab and division of the four roots by b is independently checked. This is a retypeset reproduction of the primary memoir, not a photographed1770 journal scan. The full historical proof was not newly audited.', ['turn205view1','turn208view2'])
add('PiatetskiShapiroShafarevich1971','A Torelli theorem for algebraic surfaces of type K3','https://www.mathnet.ru/links/d196eacc3f43d40b240d91a43e0339ac/im2021_eng.pdf',
['Original English paper, section3 pp558–560: Lemma1, Theorem1 and Corollaries1–3 with complete proofs','Section6 Theorem1 and complete reflection argument plus corollary, pp573–574'],
['CDP UN24 elliptic-pencil criterion from a nonzero isotropic integral divisor class on the projective K3 branch'],
'Read the exact divisor-lattice criterion and its base-point-free conclusion. The source works here with algebraic K3 surfaces; UN24 invokes it only after establishing projectivity. The descending ample intersection proves finite reflection reduction, and section3 converts a nef isotropic divisor into a multiple of an elliptic curve. The global Torelli theorem and the other applications are not independently audited by this record.', ['turn210view0','turn211view0','turn211view1','turn211view2'])

aliases={'RR70':['RR70push','RamisRuget1970'],'BS76':['BS76push','BanicaStanasila1976'],'Grauert1960':['Grauert60push','Grauert1960D'],'Grauert1963':['Grauert63push','Grauert1963ErratumD'],'Fujimoto1988Log':['Fujimoto1988Root']}
for row in rows:
 if row['key'] in aliases:row['aliases']=aliases[row['key']]

add('Kurdyka1998','On gradients of functions definable in o-minimal structures','https://www.numdam.org/article/AIF_1998__48_3_769_0.pdf',
['Original Theorem(LI) p775 and its derivation pp775–776','Theorem1 complete proof pp776–778; Theorem2 complete proof pp778–780; Proposition3 complete proof pp780–781'],
['CDP UN44 actual strong deformation retraction of a sufficiently small compact tube onto its central support'],
'The source gives the local subanalytic gradient inequality with exponent strictly less than one; the analytic function |f| squared in a relatively compact coordinate chart satisfies the hypothesis. The application separately compares the smooth metric with chart Euclidean metrics, takes a finite compact cover, integrates the uniform remaining-length bound and constructs the actual normalized-gradient flow. The entire cited theorem proof and the related gradient-retraction proofs were read. The source credits the classical analytic inequality to Lojasiewicz and the subanalytic extension to Kurdyka–Parusinski.', ['turn221view0','turn222view0'])

add('Albanese2020','The Yamabe invariants of Inoue surfaces, Kodaira surfaces, and their blowups','https://arxiv.org/pdf/2005.09494',
['arXiv2005.09494v2, 6November2020, section2.1.1 and Theorem2.2, p3','Entire section2.1.2, pp3–6, including all explicit generators, conjugation relations, nilmanifold constructions and Proposition2.3'],
['CDP A4.9 primary Hopf topology, finite primary covers and exact Inoue mapping-torus/cohomology calculation'],
'The Hopf topology and finite-cover statements were opened in the original author article; they are established inputs credited there to Kodaira and Kato. Read the complete displayed mapping-torus constructions: SM has Z3 kernel and M-transpose monodromy, while S-plus/minus has a Heisenberg lattice and a circle bundle with nonzero Chern class r over T2. The displayed conjugations give the quotient eigenvalues alpha,alpha^-1 or alpha,-alpha^-1; the centre is inverted in the minus case. These exact hypotheses match the Gysin and twisted Wang arguments in A4.9. No Yamabe theorem or proof is imported or audited by this record.', ['turn242view0','turn243view0','turn244view1'])
add('GHK2015','Mirror symmetry for log Calabi–Yau surfaces I','https://www.numdam.org/item/10.1007/s10240-015-0073-1.pdf',
['Published pp75–77: Definition1.1, Definition1.2 and Proposition1.3 with its complete proof'],
['CDP UN68 toric-model comparison for a smooth rational anticanonical pair'],
'Opened and read the exact toric blowup/model definitions and full minimal-surface/ruled-surface proof. The standing hypotheses are a smooth rational projective surface and a reduced nodal anticanonical divisor with a singular point. Proposition1.3 supplies a toric model after toric blowups; it does not assert that the original pair is toric. UN68 independently proves charge nonnegativity and the zero-charge equality case using retained contractions. The theorem is cited only as the stated comparison, and not as a substitute for that additional equality argument.', ['turn242view1','turn243view1','turn244view0'])
add('Reid1994Nonnormal','Nonnormal del Pezzo surfaces','https://ems.press/content/serial-article-files/40537',
['Original pp716–717: section3.9 and its full derivation-kernel proof','Original pp720–724: sections4.4–4.8, including the complete trace-coordinate calculation and characteristic-zero pole argument','Published pp722–724 visually read in retained scans to verify formula(1), the derivative term and the trace pairing obscured by OCR'],
['CDP A5.7 pure-double-conductor cusp calculation and its explicit attribution'],
'The general section3.9 works with the normalization of a reduced S2 scheme and its specified generic double-conductor case. Sections4.4–4.8 develop the local derivation graph and dualizing trace calculation within the del Pezzo discussion. I read the unit criterion, coordinate change xi=x-(a/b1)y1 and eta_i=yi-(bi/b1)y1, and the residue evaluation giving fi/bi=f1/b1 and (a*f1/b1)prime=-sum(gi). In characteristic zero a pole cannot meet that unit criterion. This is the known local mechanism credited in A5.7; the manuscript proves its analytic canonical-module version directly and does not invoke the global del Pezzo classification or assume an anticanonical polarization. The global classification and positive-characteristic examples are outside this check.', ['turn242view2','turn243view2','turn243view3','turn245view0','turn245view1','turn245view2'])

add('UlmerUrzua2021','Bounding tangencies of sections on elliptic surfaces','https://dlulmer.github.io/research/papers/2021a.pdf',
['Author version dated4August2020: section2.1 pp3–4, section2.2 p5 and section2.3 pp5–6','Complete matrix/period/root-character table on p6, visually inspected in retained UlmerUrzua2021_p6.png'],
['CDP UN22/29/67: only the nonmultiple smooth type I0 has identity integral monodromy','CDP UN33: finite-order fibre characters, distinguishing II from II-star, III from III-star and IV from IV-star','Transitive use in UN20/66/70 after the explicit actual root and relative-minimality arguments'],
'Read the entire local-invariant setup and every displayed matrix. An oriented H1 basis and a positively oriented loop are fixed in sections2.1 and2.3; the lattice uses a right action. The rows are I0=I; Ib=[[1,b],[0,1]]; Ib-star=-Ib; I0-star=-I; II=[[1,1],[-1,0]]; III=[[0,1],[-1,0]]; IV=[[0,1],[-1,-1]]; IV-star,III-star,II-star are the respective inverses. Their finite orders are6,4,3,2,3,4,6. For constant period, f_gamma=(c*tau+d)^(-1) is zeta_d^r: r=1 for II/III/IV and r=d-1 for their stars, exactly the positive deck-rotation convention in UN33. Only this matrix and character statement is imported. The general infinite-order-section hypothesis in the tangency theorem is not used in the local classification. The actual non-Jacobian surface arguments first pass to the explicit root/relative-minimal model; the independent root construction, not this Jacobian table, handles multiples.', ['turn282view0'])
rows[-1]['not_verified']=['No claim that the entire tangency theorem or its proof was audited.','This is an author original research article reproducing Kodaira local invariants; it is not a visual check of the1963 TableI scan.']
rows[-1]['visual_evidence']='reference_downloads/cdp_audit/UlmerUrzua2021_p6.png'
for r in rows:
 if r['key']=='Kodaira1963II':
  r['opened_locators'] += ['Section8(ii), pp581–582: positive local loop, finite-order root and actual quotient construction','Section8(iii), pp583–585: cyclic quotient resolutions; section8(iv)(11), p585: identity matrix gives a regular fibre']
  r['verification_scope'] += ' The original p585 identity-matrix case was subsequently opened and read directly: its cyclic group is trivial, the root coordinate equals the base coordinate, and the model is the smooth family F. The finite-order construction and positive-loop convention on pp581–585 were also read. The exact matrix entries are now checked separately in Ulmer–Urzua section2.3 p6, without mislabelling the damaged1963 OCR as a visual check.'
  r['web_refs'] += ['turn275view1','turn276view1','turn283view0']
  r['not_verified']=['The1963 TableI matrix entries were not visually checked; the original p585 regular-fibre case and the separate clear Ulmer–Urzua table provide the scoped verification.']
  r['local_public_html']='reference_downloads/cdp_audit/KodairaII_attempt_1.html'
  r['public_html_sha256']=hashlib.sha256((ROOT/r['local_public_html']).read_bytes()).hexdigest()

# Preserve the independent reader's exact source-opening scope and limitations.
independent_refs=ROOT/'deliverables/work/invariants_arithmetic/cdp_references_verified.json'
if independent_refs.exists():
 for source in json.loads(independent_refs.read_text()):
  rows.append({'key':source['citation_key'],'title':source['title'],
   'url':source['url'],'status':'verified in the specified scope',
   'opened_locators':[source['opened_locator']],'uses':[source['actual_use']],
   'verification_scope':source['hypotheses_and_normalization_check'],
   'own_check':source['reviewer']['checker']+', effort '+source['reviewer']['effort']+', '+source['reviewer']['date']+'; independent source reader /root/invariants_arithmetic',
   'web_refs':source['web_refs'],'local_pdf':source['local_source'],
   'sha256':source['source_sha256'],'download_status':'original journal PDF retained and opened by the identified independent reader',
   'not_verified':['The complete proof of the triangulation theorem in section4 was not independently audited.'],
   'independent_record':'deliverables/work/invariants_arithmetic/cdp_references_verified.json#'+source['citation_key']})

# Recover a successfully retained genuine PDF even if a later network refresh failed.
for r in rows:
 candidate=ROOT/'reference_downloads/cdp_audit'/(r['key']+'.pdf')
 if candidate.exists() and candidate.read_bytes().startswith(b'%PDF'):
  r['local_pdf']=str(candidate.relative_to(ROOT));r['sha256']=hashlib.sha256(candidate.read_bytes()).hexdigest();r['download_status']='genuine PDF retained and opened in stated scope'
(OUT/'references_verified.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('Published',len(rows),'opened reference records')
