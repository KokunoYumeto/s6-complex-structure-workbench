from pathlib import Path
import csv,json,re,hashlib
root=Path(__file__).resolve().parents[1]
source=root.parent.parent/'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15/S6_10_PAPERS_IV.tex'
tex=source.read_text()
actor='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed), S6_SERIES_GRIND/corrections_audit'
rows=[]
def row(n,source_locator,known_input,retained_map,disposition,fresh='Receiving proof read; retained source-opening record credited at its exact locus.'):
 rows.append({'label':f'night:P3F.{n}','source_locator':source_locator,'known_input':known_input,
              'retained_map_or_calculation':retained_map,'condition_4_4_2_disposition':disposition,
              'opening_and_check_scope':fresh})
row(1,'Oguiso–Shioda1991 Main Theorem table pp.85–86; Miranda1990 §3 pp.202–205, Prop.3.4 p.204',
    'The eight torsion-free rank-one Mordell–Weil rows and the realization theorem for the specified j-map data.',
    '24 Kodaira candidates; the three negative Riemann–Hurwitz excesses; explicit transitive permutation covers using local z→z^e; the two A7 Weierstrass models and the rational-root torsion exclusion.',
    'Cite the eight-row classification; retain the refinement/existence and explicit source calculations.',
    'Full receiving proof read. New independent_IV_classical_inputs.py constructs21 fresh permutation certificates and verifies them with SymPy, together with both A7 models; it imports no supplied code. The OS91/Miranda primary openings are retained readings, not claimed fresh here.')
row(2,'Shioda1990 Theorem8.6/equation8.12 p.228; table8.16 p.229; Prop.8.12 p.231',
    'Height formula, local component corrections and height multiplication under base extension.',
    'Exact rearrangement (P.O)=(h−2chi+sum contr)/2; the eight component-choice enumerations; actual cubic base change t=z^3 and the resulting3II+I6 surface.',
    'Short specialization: retain the finite table and explicit cubic map; cite the general height theorem.',
    'Full receiving proof read; fresh exact enumeration verifies all8 contribution bounds/component choices and the positive/negative-sign numerical examples.')
row(3,'Jin2026 arXiv2608.26698v2 Prop.3.1 pp.10–11; Lemma4.4 pp.16–17; Lemma4.8/table p.23; Thm4.9 p.24',
    'I(S2×S3)=Z² with coordinates(A,k), and twist values(1,4),(8,8).',
    'The literal twist(x,y)→(alpha(y)x,y), preferred p1 clutch4, reverse-seam mapping torus and inverse[f]=(k−8A)a+Ab.',
    'Replace by short cited application. Root integrated IV_F3_cited_proof.tex and retained the full k/ell/mapping-torus definitions.',
    'Fresh source reading already documented in Jin_primary_verification.md; receiving short substitution checked now. No new proof of Jin’s classification claimed.')
row(4,'Jin2026 coordinate input through F3; explicit F4 construction',
    'The chosen a twist and its normalization.',
    'Quaternionic lift A_n(u,y)=(alpha_tilde(y)^n u,y), extension E_n(q,y) on D4×S3, its inverse and orientation; the gauge logarithm and the MV determinant.',
    'Retain the short explicit Hopf extension and gluing map. The map is the input used by F22, beyond the coordinate classification.')
row(5,'Takase2005 corrected Cor.2.6, as cited/opened in the retained record',
    'Haefliger invariant of an embedded Seifert surface from its actual normal Euler class.',
    'The actual degree12 genus3 surface, parity of K+2M, and equality (K+2M)^2=4M² from K²=KM=0.',
    'Retain the characteristic-normal-class specialization; cite the invariant formula.')
row(6,'Shioda1990 Theorem8.6 and Prop.8.12; displayed marked-cover construction',
    'Height and signature inputs for the elliptic pullback.',
    'C:b³=a⁴+1, x=b³; the actual Mobius map t_*x/(x+t_*−1) and inverse; branch profiles3^4,4^3,12 and the different completed fibres.',
    'Retain both explicit maps and the resulting page comparison.',
    'Full receiving proof read; the new low-F program checks the Mobius inverse/marked images and Riemann–Hurwitz genus3.')
row(7,'AC26 original Prop.9.24/Remarks9.25–26 pp.82–83; HKS2020 Thm4.1 pp.2094–2095; KM1963 pp.504–505; Haefliger1966 Thm1.2 pp.404–405/Cor.6.6 p.422',
    'The reference delta-circle action/fixed curve; classification from the whole orbit-pair and Euler class; low-dimensional sphere/embedding inputs.',
    'Literal cocharacter e2; normal rays and conifold charts AD=BC; smoothing SL2(C) and polar decomposition; actual orbit homology, meridian Euler class and orbit-normal SU2 clutch contraction.',
    'Replace only the repeated AC26 action calculation (proof item2) by the exact citation. Retain the orbit-pair, normal and conifold maps. HKS4.1 is used after the orbit-pair calculation.',
    'AC26 original loci freshly read in prior part of this run; HKS Thm4.1 freshly reopened now from the journal PDF. Its invariant is(M*,F,e), so it supplies no automatic identification of this orbit space with S5.')
row(8,'F4/F7 inputs and the explicit forward return construction',
    'Equivariant Ehresmann and the chosen Torelli/Hopf data.',
    'Return fixed near the tube; quotient relative-boundary map; actual D4×D3 cut and regluing with its orientation.',
    'Retain the family’s map from the smooth return to the specified sphere gluing.')
row(9,'Displayed node/conifold charts and their physical reference data',
    'Local smooth-node and conifold models.',
    'Unique positive solution of the displayed radial equation, triangular coordinate-flow derivative, bounded-unit logarithms and retained meridian line class.',
    'Retain the relative-framed node product; it supplies the actual comparison required downstream.')
row(10,'F6/F9; Shioda1990 cited height inputs',
    'Elliptic surface height and signature formulas.',
    'Regular-binding degree12 map; actual Seifert matrix determinant−1; weighted Milnor-page scaling; Picard torsor section, normalized point line and triangular stable frame.',
    'Retain the page/collar/line map and characteristic evaluation.')
row(11,'Jin2026 additivity and clutch normalization; cited Smale sphere-diffeomorphism input',
    'Additivity of(A,k) and preferred p1(alpha)=4.',
    'Actual normal-framing alpha:S3→SO3 twist; phase-line classes h−n_-t and−h+n_+t; adjoint p1=−4(n_-+n_+)ht.',
    'Retain the short phase/framing specialization and cite additivity.')
row(12,'Shioda height input; displayed compact torsor and local translation maps',
    'Height formula and the nodal identity-component logarithm.',
    'C:y^12=t^4/(t−1)^3; G=[[1,−1], [−1,2]], det(G−I)=−1; actual torsor-section extension and degree-zero Cartier norm frames.',
    'Retain the source/compact-torsor/line identification.',
    'Full receiving proof read; fresh program verifies the unimodular coinvariant determinant.')
row(13,'Displayed two-parameter corner charts and cited real-trace inputs',
    'Local node resolutions and the real trace used in the stated comparison.',
    'Actual origins theta gamma+6theta(1−theta)delta and winding−12; the exact local XY=Qr maps and the explicit remaining analytic descent scope.',
    'Retain the local calculation with its stated limit of analytic descent; no global corner theorem is inferred.')
row(14,'Cited spin-c index/Riemann–Roch input; displayed opposite-weight projective bundle',
    'Index theorem and Riemann–Roch formula.',
    'B=P(L_+⊕conj L_-), roots a,−b, pushforward x,x²,x³ and characteristic D=d+a+b; explicit reduction to chi(S,L_+).',
    'Retain the short projective-bundle calculation in this specific form; cite the general index theorem.',
    'Full receiving proof read; fresh symbolic pushforward proves the displayed index polynomial, including the fixed-sheet zero specialization.')
row(15,'Displayed twelve-node cyclic charts',
    'Local rank-one toric charts.',
    'Full labelled deck maps, twelvefold scalar rho^-12, source translation−6P and winding−12; the stated outer-cusp comparison scope.',
    'Retain the explicit local descent and precisely stated remaining outer comparison.')
row(16,'Viaclovsky Combs §7 equations7.1–7.3, Prop.7.3, Remark7.4; original label topology lines2008–2121',
    'Smooth annular attachments phi_i,s extending to s=0 and the local K_s extension.',
    'The fixed real lattice outside caps, radial parameter horizontal flow, relative-boundary cutoff isotopy, and resulting single-valued smooth product over the punctured parameter disc.',
    'Retain the explicit parameter-family coherence argument and cite the construction it uses.',
    'Full receiving proof read. sign_theorem_audit independently reopened the attached source on19November: it supplies the local smooth maps and source-fibration monodromy, while the global parameter-loop product is the explicit F16 construction. This audit does not count that other agent’s source opening as its own.')
row(17,'Viaclovsky cited logarithmic-family construction; Shioda height formula; F10',
    'The source log families and elliptic height inputs.',
    'Actual coprime(3k,4l) source caps, signed weighted Seifert action and page b^m−a^n=1, degree mn, line square−2kl and p1−24kl.',
    'Retain the explicit source-to-page and framing specialization.')
row(18,'Viaclovsky2609.33785 cited source; Liu–Rollenske source; Shioda height input',
    'The specified Weierstrass source and section for each construction.',
    'Actual(1,4) degree4 regular-binding page and retained order4 cap; source point/line transport and completed fibre lists.',
    'Retain the explicit page computation with its source identification.')
row(19,'Yang attached REPAIRED_v4_5, Lemma7.1/Theorem7.2, attached-source pp.40–41; TeX lines3210–3320','Complete boundary fundamental-group presentation and canonical exact groups for Type B/C.','Kill the fibre loops and send the finite meridians to1,−1 and the cusp meridian to0 in Z/g, with g=gcd(m1,m2)=2 or3. Every relation is killed for every admitted twist; the first meridian maps to1.','Retain the already-short cited specialization. The canonical exact groups are explicitly credited to Yang; no long proof replacement is needed.','Actual F19 proof read; attached Yang theorem and complete proof freshly opened. The adjacent iv:rank_two_specialization lemma has its own independent lattice/cross-line audit and is not attributed to F19.')
row(20,'Wang Thm1.1 p.2 and proof §§4–6 pp.9–15; Shioda height formula',
    'The quoted global topology of Wang’s construction.',
    'I2 monomial map(x,y)=(v,v²/z), inverse(z,v)=(x²/y,x), primitive collapsing ray(2,1), actual delta isotropy and OS49 page/line calculation.',
    'The global topology is already cited directly. Retain the monomial and page/fan comparison.')
row(21,'E26 §2 and Remark8.5; Miranda1990 Prop.3.4; KM1963 p.512',
    'The generalized elliptic-surface construction and the marked-cover realization inputs.',
    'Literal I7 source, M7/translation−2G, period matrix[[-1,4],[-2,7]], degree9 modular marking, Jacobi lift, full parabolic/cap contraction and degree-four elliptic page.',
    'Retain the explicit source/lattice/topology/page calculation; cite the generalized construction. Its exact E26 relation is IV_source_morphisms.tex.',
    'Full receiving proof read, including the finite-cap specialization indices and all contraction maps; bounded source comparison separately recorded. New independent_IV_OS47_topology.py completes142 exact assertions for the literal source, based modular subgroup, full Jacobi lift, integral parabolic and finite-cap maps, and degree-four page. Its full output and geometric proof scope are in IV_OS47_topology_review.md.')
row(22,'Jin2026 Lemma6.2 pp.34–35; Jiang2014 §3.1(v) pp.5–6/Lemma3.5 Case2 pp.13–15; Davis1982 §§2–3 pp.67–69',
    'The marked-double bordism, Jiang’s characteristic-number calculation and the normalized Eells–Kuiper classification.',
    'The exact reverse-seam collar, quaternionic removal f→f a^-k, source substitution(N,t,k,p,epsilon,delta)=(N_f0,x,0,ell−4k,0,0), and oriented surgery boundary−lambda(f0).',
    'Replace repeated Jiang computation by cited specialization; preserve the actual orientation map. Root integrated IV_F22_cited_specialization.tex.',
    'Fresh Jiang PDF reading covers definitions pp.3–4, formula pp.5–6, and Lemma3.5 statement/proof pp.12–15. Fresh Davis pp.67–69 verifies the positive generator. Fresh arithmetic gives6/896−1/192=1/672 and μ(lambda b)=+1/28. Earlier Jin primary opening retained.')
row(23,'F21/F68 marked-family construction',
    'The fixed source/cap and physical reference convention.',
    'Actual ordinary and cusp origins, full angular difference theta gamma+2theta(theta−1)delta, parameter deck and fourth-root winding+4.',
    'Retain the short full-origin/deck calculation.',
    'Full receiving proof read; fresh symbolic program checks both origins, all four deck equations, full angular identity, winding and both endpoint values.')
row(24,'Davis1982 §3 p.69; Crowley–Nordström2019 arXiv1406.2226v3 §1.4 equations2–3 p.5',
    'Theta7=bP8 and the classical invariant for each chosen spin structure with torsion p_M.',
    'Actual disc-supported sphere return; ball crossing the forward seam; boundary-collar connected-sum map; both spin structures bounded by S1×D7 boundary-summed with a sphere bound.',
    'Retain the seam/collar and spin-bound maps. Replace the general index-invariance derivation by the cited formula with p_W=p1/2 and division by28.',
    'Fresh CN v3 PDF opened and saved; opening spin conventions and §1.4 equations2–3 read. Root integrated IV_F24_known_invariant.tex. The actual both-spin argument is retained, and no whole mapping-torus assertion is attributed to Davis.')

with (root/'IV_known_input_specializations.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)

original=[]
for n in [3,7,22,24]:
 pos=tex.index(r'\label{night:P3F.'+str(n)+'}')
 begin=tex.index(r'\begin{proof}',pos);end=tex.index(r'\end{proof}',begin)+len(r'\end{proof}')
 original.append('% Original attached proof of night:P3F.'+str(n)+'; retained solely as audit evidence.\n'+tex[begin:end])
(root/'IV_displaced_classical_proofs_evidence.tex').write_text('\n\n'.join(original)+'\n')

report='''# IV known inputs and short specializations

## Scope and completed replacements

This review covers the complete receiving proofs of `night:P3F.1`–`night:P3F.24`, together with the exact primary-source comparisons specified in the table. It applies prompt condition4.4(2): use the cited theorem directly, and retain the short computation that supplies the actual form or map needed here. It makes no worldwide absence or priority claim.

The four concrete changes are F3’s short Jin application, the AC26 input in F7’s proof item2, F22’s shortened Jiang specialization, and F24’s direct citation for the fixed-spin Eells–Kuiper invariant. Root reports these integrated, retaining all F3 definitions and all four F22 equation tags/subsection anchors. The original four proofs are preserved in `IV_displaced_classical_proofs_evidence.tex`.

F22 retains the exact orientation map: removing the cubic coordinate uses the actual quaternionic extension, and the handle attachment has boundary **−lambda(f0)**. The source indicators are zero because the marked double is smooth and spin, and its cubic coordinate is zero after this explicit change. Substituting the cited characteristic numbers gives μ(−lambda)=p/672 with p=−24A, hence μ(lambda)=A/28. The positive generator therefore remains +1/28. Nothing in this replacement assigns a parameter-loop sign without its actual return map.

F24 retains the actual forward-seam ball regluing and its inverse direction. The fixed-spin formula is cited at a source that treats arbitrary closed spin seven-manifolds with torsion spin characteristic class. The exact normalization transport is p_W=p1(W)/2 and μ_here=μ_source/28. Both spin structures in the particular product bound are still handled by the explicit S1×D7 construction in the proof.

## Fresh source openings

* Jiang2014: the exact downloaded19April2014 author edition, definitions pp.3–4, §3.1(v) pp.5–6, Lemma3.5 statement p.12 and complete Case2 pp.13–15. SHA256 `1bc65d56cb2dd79e9c08f4dee3dab5fd4f82c65b0bdb6b95ebc5a3336504e762`.
* Harvey–Kerin–Shankar2020: journal Theorem4.1 pp.2094–2095, including both classification and realization hypotheses. The invariant is the whole orbit pair with Euler class. SHA256 `2330706f3e68a3bdfe19d8068e4ce5c520e2123c85952d655254cbe734295870`.
* Davis1982: §§2–3 pp.67–69, the oriented positive Milnor generator and additive Eells–Kuiper identification. SHA256 `1c42dd240d64efc5378b052ffa18431622ff412fcf5f4887cb875f5f3d34ba9b`.
* Crowley–Nordström2019: arXiv1406.2226v3 opening spin conventions and §1.4 equations(2)–(3), p.5. SHA256 `1a9f89bd57dd8709395b6eab3e41226da4ec260de79417dd447da70c9f97d45a`.

All four PDFs, extracted texts, URL/size/hash metadata and download programs are preserved under this audit. Jin and AC26 were freshly opened earlier in this run, with their exact reading scopes in the existing reports. OS91, Shioda and other listed sources use their retained opened-source evidence; this review does not count those as new source openings. The Combs source was independently reopened by sign_theorem_audit; the table attributes that reading explicitly.

## Independent finite inputs

`code/independent_IV_classical_inputs.py` completed **265 exact assertions**. It generates all24 fibre candidates, excludes the exact3 with excess−1, and constructs21 new transitive permutation tuples by involution enumeration. SymPy independently checks each tuple’s profiles and transitivity. It also checks the actual two A7 models/torsion obstruction, all8 height component tables, the explicit degree12 Mobius map, the projective-bundle index polynomial, F22 normalization, the OS47 full origins and root-deck winding, and the compact-torsor unimodular matrix. All new tuples are retained in its JSON output. No supplied program or old certificate is imported.

The first execution used structural equality for one factored SymPy polynomial and stopped. The failure was repaired by testing the expanded polynomial difference. The exact first-run program and output remain under `code/independent_IV_classical_inputs_attempt01.*`. No paper equation changed.

This finite computation supplies explicit arithmetic witnesses and polynomial identities. The geometric branched-cover construction, cited realization theorem, source/Cartier/collar maps, orientations, analytic extensions and unbounded integer arguments remain the displayed proofs. In particular, this265-check run does not replay F21’s parabolic topology matrices.

## Classification of the24 proofs

`IV_known_input_specializations.tsv` supplies one row for every F1–F24, with the exact cited input, the retained map/calculation, disposition and honest opening/check scope. The largest remaining blocks contain actual geometric constructions: F1’s21 realization refinements; F7’s orbit-pair/conifold comparison; the separate `iv:rank_two_specialization` integral cross-generator; and F21’s literal I7 source, marked lattice and cap contraction. The table identifies the corresponding source theorems and the additional maps the receiving arguments use.

Format/layout remain root-owned. Mathematical row assessments are added only at the explicit reviewed scopes; no rendering or completed-layout field is inferred from the source review.
'''
(root/'IV_known_input_review.md').write_text(report)

path=root/'CHECK_EVENTS.tsv'
with path.open(newline='') as f:
 reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;events=list(reader)
def event(label,kind,outcome):
 e={'statement_id':label,'date':'2026-11-19','who':actor,'type':kind,'outcome':outcome,'phase':'S6_SERIES_GRIND'}
 e['event_id']='s6sg:'+hashlib.sha256((label+'|'+kind+'|'+outcome).encode()).hexdigest()[:20]
 if not any(p['event_id']==e['event_id'] or (p['statement_id']==label and p['type']==kind and p['outcome']==outcome) for p in events):events.append(e)
for r in rows:
 event(r['label'],'targeted proof check','Condition4.4(2) receiving-proof/source-scope review. Cited input: '+r['source_locator']+'. '+r['known_input']+' Retained actual map/calculation: '+r['retained_map_or_calculation']+' Disposition: '+r['condition_4_4_2_disposition']+' Check scope: '+r['opening_and_check_scope']+' This is not a newly claimed blind reproof of an entire source theorem.')
for n in [1,2,6,12,14,22,23,24]:
 event(f'night:P3F.{n}','computation or formal certificate','New code/independent_IV_classical_inputs.py and JSON completed265 exact assertions in0.141seconds across the stated low-F inputs. This row uses only its named identity/profile checks listed in the JSON. The F1 output includes21 newly generated transitive permutation certificates with independent SymPy verification; no supplied code or previous certificate is imported. The first structural-equality failure and its code repair are retained as attempt01; no mathematical source was changed. This event does not imply a replay of any other row’s historical atlas.')
for label,outcome in [
 ('night:P3F.22','Freshly opened Jiang2014 definitions pp.3–4, §3.1(v) pp.5–6 and Lemma3.5/complete Case2 pp.12–15, and Davis1982 §§2–3 pp.67–69. Matched the exact marked double, k=0/spin/smooth indicators, circle-bundle/product-framed handle and characteristic table. The receiving proof preserves the actual boundary direction −lambda; its scalar substitution yields +1/28 for lambda(b). File hashes and primary URLs are in IV_known_input_review.md and primary_sources metadata. Root integrated the bounded cited-specialization replacement while retaining all four equation tags and anchors. This is a source and receiving-map check, not a fresh proof of the cited classification.'),
 ('night:P3F.7','Freshly reopened HKS2020 Theorem4.1 pp.2094–2095 in the journal PDF. Verified codimension4 fixed set, H2(F;Z) without2-torsion, and invariant(M*,F,e). The AC26 reference cocharacter is literally e2 in the chosen marking. Root replaced only the duplicate AC26 action calculation; the actual orbit-pair, normal clutch and conifold maps remain. No source reading is claimed to identify the orbit pair before those calculations.'),
 ('night:P3F.24','Freshly opened/saved Crowley–Nordström arXiv1406.2226v3, opening spin conventions and §1.4 equations(2)–(3), p.5. Verified the fixed-spin torsion-pM scope and exact normalization p_W=p1/2, μ_here=μ_source/28. Root substituted this citation for the general index-invariance derivation while retaining the explicit forward/reverse seam collars and both-spin bounding maps. This source comparison does not attribute the entire mapping-torus diffeomorphism to Davis.')]:
 event(label,'targeted proof check',outcome)
with path.open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(events)

assess=json.loads((root/'row_assessments.json').read_text())
for n in [1,2,3,4,7,14,16,22,23,24]:
 r=rows[n-1]
 assess[r['label']]={
  'confidence_state':'proved at the stated scope',
  'confidence_line':'The retained complete proof and this source/map comparison establish the printed scope. '+r['condition_4_4_2_disposition'],
  'independent_routes':[r['opening_and_check_scope'],'The complete receiving proof was read with the actual line, marking, parameter and orientation maps retained.',r['retained_map_or_calculation']],
  'remaining_risk':'No mathematical gap identified in the stated scope. The source theorem is used only for '+r['known_input']+' The new review is targeted; it does not claim a blind reproof or new opening of sources attributed only to the retained record. Source integration/rendering remains root-owned.',
  'format_check':None,'layout_check':None,'completion_state':None}
(root/'row_assessments.json').write_text(json.dumps(assess,ensure_ascii=False,indent=2)+'\n')
search={'date':'2026-11-19','query':'Crowley Nordstrom classification 2-connected 7-manifolds Eells Kuiper invariant spin manifold torsion p1 spin structures arxiv',
 'engine':'system2','primary_opened':['https://arxiv.org/pdf/1406.2226','https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/plms.12222'],
 'source_refs':['turn296527932academia12','turn635316957view0','turn635316957view1','turn183382834view1'],
 'scope':'Located and opened the exact fixed-spin torsion-pM invariant used in F24; no broad literature absence claim.'}
(root/'IV_classical_source_search.json').write_text(json.dumps(search,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'review_rows':len(rows),'events':len(events),'row_assessments':len(assess)},indent=2))
