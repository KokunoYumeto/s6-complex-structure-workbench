#!/usr/bin/env python3
"""Bounded, per-statement attribution checks for the36 transferred PUSH/FAM rows.

Every term search is executed against the named full supplied source. Negative
results mean only that no match was located in those searches and the recorded
opened passages. The attached AC26 PDF controls its text index.
"""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
D = ROOT/'deliverables'
W = D/'work/invariants_arithmetic'
META = dict(checker='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17 UTC')


def load(p):
    return json.loads((ROOT/p).read_text())


def save(name, value):
    (W/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')


def digest(p):
    return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()


targets = [x for x in load('deliverables/work/root/III_remaining_run_credit_targets.json')
           if x['source_run'] in ['S6_02_PUSH', 'S6_02_FAMILY']]
assert len(targets) == 36
paths = {r['source']:r['index_source'] for r in load('deliverables/work/invariants_arithmetic/maps_D_credit_search_log.json')}
baseline = {r['citation_key']:r for r in load('deliverables/work/invariants_arithmetic/source_credit_map.json')}

# The declared search expressions are literal phrases except where explicitly
# using the short regular expressions needed for hyphens and LaTeX variants.
specs = {
 'E.2.2': ('parameter monodromy; explicit clutching and residue', ['parameter','clutch','Eells','Kuiper','mapping torus','spin','punctured'], ['Cerf1970','Poenaru1971','EellsKuiper1962','KervaireMilnor1963']),
 'E.2.3': ('historical filling and one-loop targets, now answered at specified scopes', ['central fi[bv]','punctured','filling','monodromy','Pontryagin','Eells','Kuiper'], []),
 'C.1.1': ('mapping-torus connected sum, sphere gluing and either spin structure', ['mapping torus','connected.sum','pseudo.isotopy','Eells','Kuiper','spin structure'], ['Cerf1970','Poenaru1971','KervaireMilnor1963','EellsKuiper1962']),
 'C.1.2': ('positive Euler-one sphere-bundle generator', ['Eells','Kuiper','sphere bundle','rank.four','896','1/28'], ['EellsKuiper1962','KervaireMilnor1963','Davis1982D']),
 'C.2.1': ('spin/spin-c boundary characteristic formula and relative lifts', ['spin','Eells','Kuiper','896','192','relative lift'], ['EellsKuiper1962','CrowleyNordstrom2020']),
 'C.2.2': ('actual untwisted cap intersection lattice and signature', ['untwisted','intersection form','signature','Smith','coboundary'], ['Shioda90']),
 'C.2.3': ('actual untwisted cap Pontryagin covector and4512/11', ['untwisted','Pontryagin','4512','Riemann.Roch','coboundary'], ['AtiyahSinger1968IIIE']),
 'C.3.1': ('semifree fixed-sphere geometry and marked shear', ['fixed locus','normal weights','circle',r'E_\{41\}','integer-period-shear','semifree'], []),
 'C.3.2': ('global circle gauge isotopy and nonextension of primitive gamma', ['gauge','logarithm','simply connected','primitive','isotop'], []),
 'C.3.3': ('all28 classes admit one fixed semifree action', ['Blakers','Massey','reentrance','28','semifree','quaternion'], ['DuranRigas2007','KervaireMilnor1963']),
 'C.3.4': ('sixfold base-change loss of the order-two residue', ['base change','six','28','14','mapping.class'], ['KervaireMilnor1963','EellsKuiper1962']),
 'C.3.6': ('uniqueness of equivariant lift class and compactly supported orbit isotopy lifting', ['orbit.preserving','equivariant','gauge','logarithm','Haefliger','Salem'], ['HaefligerSalem1991D','KarshonOrbitSlidesD']),
 'C.3.7': ('central cusp orbit homology and primitive fixed sphere', ['orbit','central fi[bv]','homology','normalisation','normalization','double curve'], []),
 'C.3.8': ('equivariant cusp retraction and primitive fixed-sphere class in quotient body', ['equivariant','retract','fixed','primitive','Thom'], []),
 'C.3.9': ('marked conductor loops u,gamma+u and normal circle minusgamma', ['conductor','marking','normalization','normalisation','gamma','primitive'], []),
 'C.3.10': ('actual six-loop annular gamma translation', ['annular','six','gamma','translation','parameter','loop'], []),
 'C.3.11': ('doublecircle and oriented normal Euler number minus2', ['double.circle','normal bundle','Euler','fixed','weights','self.intersection'], []),
 'C.3.12': ('obstruction to the literal translational Seifert quotient extension', ['Seifert','quotient','continuously','hexagon','kernel','covector'], []),
 'C.3.13': ('corrected smooth Seifert comparison, marking and regular-fibre linking12', ['Seifert','quotient','linking','twelve','12','weighted'], []),
 'C.3.14': ('actual standard orbit pair, specified surgery cap and Wall integer', ['Haefliger','Wall','orbit','Pontryagin','framing','cap','Eells'], ['FintushelPao1983D','Haefliger1966D','KervaireMilnor1963','Olbermann2010D','Wall1966VE','Wall1967CorrE','Davis1982D']),
 'C.3.15': ('zero integer of the actual annular cap', ['annular','24','relative square','framing','Wall','Eells'], ['Wall1966VE','Olbermann2010D']),
 'C.3.16': ('actual signed gamma linking12 and boundary H1 map', ['linking','gamma','transgression','twelve','12','Seifert'], []),
 'C.3.17': ('marked cusp product, freely extended gamma action and primitive H3 sweep', ['product model','nodal','gamma','sweep','nonbounding','primitive'], []),
 'C.3.18': ('actual twelve-node page and relative affine frame defect minus24', ['Lefschetz','twelve','Pontryagin','24','framing','affine'], ['manSS10']),
 'C.3.19': ('actual cap Pontryagin pairing24 and framing coordinate6', ['Pontryagin','framing','Wall','24','cap'], ['Wall1966VE']),
 'C.3.20': ('actual delta-line relative square and cubic transgression coefficient3', ['Chern.Simons','transgression','relative square','delta','cubic'], ['ChernSimons1974E']),
 'C.3.21': ('actual relative Picard-line square minus2', ['Picard','multiplier','Leray','nodal','P-O','relative square'], ['Shioda90','manSS10']),
 'C.3.22': ('one common orientation sign in the actual cap formulas', ['Pontryagin','orientation','relative square','transgression','cap'], ['Wall1966VE','ChernSimons1974E']),
 'C.3.23': ('integer orbit-knot additivity before reductionmod28', ['Haefliger','Davis','orbit.knot','integer','additiv','28'], ['Smale1959E','Haefliger1966D','Davis1982D','Wall1966VE']),
 'C.3.24': ('actual positive parameter-loop smooth monodromy iszero', ['parameter','monodromy','Eells','Kuiper','mapping.class','isotop'], ['Cerf1970','Poenaru1971','EellsKuiper1962','Davis1982D']),
 'C.3.25': ('actual Hopf-handle spin-c coboundary and mu=(p−4k)/672', ['Hopf','handle','spin','672','CP','coboundary'], ['Jiang2014E','CrowleyNordstrom2020','EellsKuiper1962','MontgomeryYang1968E']),
 'C.3.26': ('direct characteristic-index additivity and framing independence', ['index','additiv','framing','sphere.bundle','24','spin'], ['Smale1959E','Olbermann2010D','Wall1966VE','Jiang2014E']),
 'C.3.27': ('independent one-loop zero determination by integer index', ['parameter','monodromy','index','Eells','Kuiper','28','spin'], ['EellsKuiper1962','CrowleyNordstrom2020','Jiang2014E']),
 'C.4.1': ('common positive-loop class for all sphere twist data', ['twist','parameter','monodromy','classification','isotop','28'], []),
 'C.4.2': ('antiholomorphic symmetry and two compensating signs', ['antiholomorphic','conjugation','orientation','Eells','Kuiper','negation'], ['EellsKuiper1962']),
 'C.5.1': ('nonexistence of the specified analytic filling and zero smooth monodromy', ['filling','non.normal','monodromy','Pontryagin','Eells','Kuiper'], []),
}
assert set(specs)=={x['source_id'] for x in targets}

# Actual bounded original-source readings. Later entries here extend earlier
# INV/ARI reading records; they do not retrospectively broaden those records.
openings = {
 'AC26': dict(citation_key='AC2026', local_source='sources/original/AC26_original_manuscript.pdf',
   opened_locator='Attached original PDF, pp.29–31 Proposition4.6 and Proposition4.7/Corollary4.8; p.41 Proposition7.2 and Lemmas7.3–7.4; pp.50–51 full conclusion of the retraction proof and Proposition7.11; pp.62–63 Proposition7.27 (earlier full reading); pp.82–83 Proposition9.24 and Remark9.25. Original pp.41 and83 newly visually opened. The original PDF controls its extracted text index.',
   actual_use='Exact fixed sphere, normal weights and freeness; torus-equivariant cusp retraction; original toric normalization/gluing and integral transgression predecessors. No parameter-loop mapping-class value is inferred.'),
 'E26': dict(citation_key='Engel2026', local_source=paths['E26'],
   opened_locator='Original S6.tex §2 lines288–400, Lemma2.1 and full height/intersection proof; §8 lines1647–1763, all Additional remarks, including Remark8.1/Conjecture8.2 and exact Remark8.3 lines1684–1723. Previous receiving checks cover construction §§2–4 and integral homology §7.',
   actual_use='Elliptic surface/line-bundle antecedent; punctured degeneration question; literal Seifert quotient statement being corrected. No smooth parameter-monodromy integer is calculated there.'),
 'DGKX_v1': dict(citation_key='DuEtAl2026v1', local_source=paths['DGKX_v1'],
   opened_locator='Original v1 §7, exact roots, integer period shear and core-shift descent lines10385–10476; complete cusp extension and marking lines10560–10675; constructed C*×2Z groupoid lines11955–12023. Earlier reads also covered §§6–7 family construction, deformation and automorphisms at the locators in source_credit_map.json.',
   actual_use='Known commuting scalar action and exact marked integral period shear/core shift. This is the historical first version, independently of its omission from v2.'),
 'DGKX_v2': dict(citation_key='DuEtAl2026v2', local_source=paths['DGKX_v2'],
   opened_locator='Original v2 introduction lines312–320 and section inventory were previously opened. Current whole-source searches are saved per target, including Eells/Kuiper, parameter, mapping-class, spin, framing and relevant geometric terms. No v1 deformation/shift theorem is attributed to v2.',
   actual_use='Explicit version comparison; v2 does not become a source for a v1 statement merely because the authors coincide.'),
 'manViaclovskyLogs26': dict(citation_key='manViaclovskyLogs26', local_source=paths['manViaclovskyLogs26'],
   opened_locator='Original lines325–396, invariant sublattices and The fillings and logarithmic transformations; rotations extending over the toric boundary and commuting with period identifications, especially lines366–378. Broader original topology/translation scopes are in maps_D_references_verified.json.',
   actual_use='Known circle actions on the toric filling and logarithmic-transform framework; not the actual parameter-loop integer.'),
 'manViaclovskyTwo26': dict(citation_key='manViaclovskyTwo26', local_source=paths['manViaclovskyTwo26'],
   opened_locator='Previously opened original two-parameter family, fibrewise period/Picard and boundary-marking scopes in maps_D_references_verified.json; current full-source target-term searches separately saved.',
   actual_use='Bounded comparison with another complex-family construction, without claiming an exhaustive absence result.'),
 'manWang26': dict(citation_key='manWang26', local_source=paths['manWang26'],
   opened_locator='Original lines1618–1710, topological-classification setup and complete scalar-involution fixed-set lemma, newly read; the fixed elliptic curve plus rational curve and odd normal weights are for Wang\'s different torsion family.',
   actual_use='Distinguishes the scalar involution/torsion-family normal-weight computation from the present scalar circle and parameter-loop class.'),
 'manLR26': dict(citation_key='manLR26', local_source=paths['manLR26'],
   opened_locator='Earlier exact original deck-involution lines539–558 and torus-map/cusp construction readings in maps_D_references_verified.json; current target searches, including the mapping-torus/coboundary hits, are retained.',
   actual_use='The located mapping-torus and local-system coboundary language concerns the torus fibration, not a computed homotopy-seven-sphere parameter invariant.'),
 'manYang26': dict(citation_key='manYang26', local_source=paths['manYang26'],
   opened_locator='Earlier complete original Whitney/Thom, compatible level-tube collapse and cusp cohomology blocks lines3340–3695; complete sweep-chain proof lines3851–3983; exact boundary ledger lines5340–5461, as registered in maps_D_references_verified.json. Current full-source target searches are retained.',
   actual_use='Known stratified cusp retraction and integral sweep-chain machinery; not the actual S1 quotient cap or one-loop mapping class.'),
}
for key,r in openings.items():
    r.update(META)
    r['source_sha256']=digest(r['local_source'])
save('push_C_credit_opened_scopes.json',openings)

logs=[]
for target in targets:
    sid=target['source_id']
    for source,path in paths.items():
        lines=(ROOT/path).read_text(errors='replace').splitlines()
        query=[]
        for expression in specs[sid][1]:
            pat=re.compile(expression,re.I)
            hits=[i+1 for i,line in enumerate(lines) if pat.search(line)]
            query.append(dict(expression=expression,hit_count=len(hits),line_numbers=hits))
        logs.append(dict(source_run=target['source_run'],source_id=sid,source=source,
            index_source=path,index_sha256=digest(path),search_scope='Whole supplied source file',queries=query,**META))
assert len(logs)==324
save('push_C_credit_search_log.json',logs)
look={(r['source_id'],r['source']):r for r in logs}

# Relations are result-specific, not generic family credits.
ac = {
 'C.3.1': ('found_exact_structural_clauses','Proposition9.24 pp.82–83 and Remark9.25 p.83',
  'Already proves the same fixed double P1, the(+1,−1) normal weights and freeness of the effective circle off it. Together with the exact DGKXv1 shear below, this row is Cited/re-derived; the full averaged-metric transport argument is preserved.'),
 'C.3.7': ('found_geometric_antecedent','Proposition4.6 p.29; Proposition7.11 pp.50–51',
  'The dP6 normalization, opposite-edge identification and original central-fibre homology are known. This row computes the scalar-circle quotient, its lower-dimensional homology and its primitive fixed-sphere class; those are not Proposition7.11\'s homology of W itself.'),
 'C.3.8': ('found_exact_retraction_clause','Proposition7.2 p.41, proof conclusion p.50',
  'The torus-equivariant strong deformation retraction onto W is explicit in the original. Its restriction to the scalar circle supplies the existence clause. The primitive nonzero H2 class of the fixed sphere in the quotient body is the added C.3.7-dependent clause. Keep this additional result in the main text and credit the retraction at use.'),
 'C.3.9': ('found_marking_antecedent','Proposition4.6 p.29; Proposition4.7 p.30; Proposition7.2 p.41',
  'The actual opposite-edge deck arrows, tautological lattice marking and honeycomb directions are original data. This row reads their two conductor loops and real-normal circle in the FAMILY marking; it is an explicit calculation from those known charts.'),
 'C.3.11': ('found_geometric_antecedent','Proposition4.6 p.29; Proposition7.11 p.50; Proposition9.24 pp.82–83',
  'The opposite(-1)-curves and fixed double curve/weights are known. The real-normalization immersion, its one doublecircle and the oriented normal Euler evaluation−2 are the added quotient calculation.'),
 'C.3.12': ('found_geometric_antecedent','Proposition4.6 p.29 and Proposition4.7 p.30',
  'The dense cusp torus and exact deck gluing support the correction. AC26 does not make Engel Remark8.3\'s literal continuous translational quotient assertion in these opened passages.'),
 'C.3.13': ('found_geometric_antecedent','Introduction p.1 Seifert discussion; §§4–5 and Proposition7.27 pp.62–63',
  'The(3,4) Seifert interpretation and integral finite-twist/transgression data are already present. This result constructs a modified smooth cusp comparison with its specified marking, not the impossible literal translational quotient.'),
 'C.3.16': ('found_integral_antecedent','Proposition7.27 pp.62–63',
  'The original invariant lattice/transgression calculation contains the factor12 and the signed finite-twist relation. The assertion here is the stronger marked link inclusion into the actual orbit complement, with(12,0,1) and a specified positive orientation; the geometric quotient/link comparison is separately proved.'),
 'C.3.17': ('found_geometric_antecedent','Proposition4.6 p.29; Proposition4.7 p.30; Proposition7.2 p.41',
  'The toric cusp quotient and lattice labels are known source data. The marked E_I1×S1 orbit-body model, extending gamma action and primitive nonbounding three-torus are additional quotient constructions.'),
 'C.3.21': ('found_period_and_picard_antecedent','§9.1 and Proposition9.11 pp.70–71; Proposition4.7 p.30',
  'The original period/Picard data and canonical toric marking are predecessors. The exact actual delta-line identification on the chosen twelve-node page, nodal excision and relative square−2 require the receiving comparison; no square of an unspecified line is substituted.'),
}

e = {
 'E.2.2': ('found_family_question_antecedent','Remark8.1, lines1647–1683',
  'Explicit punctured proper family and smooth S6 bundle already stated. The marked gluing and its Eells–Kuiper reduction use classical sources and the later strict endpoint maps; E26 gives no parameter-loop residue.'),
 'E.2.3': ('found_historical_question','Remark8.1/Conjecture8.2, lines1647–1683',
  'The proposed nonnormal ruled normalization, section gluing and sphere-limit question are an explicit source antecedent. The retained historical targets are now answered at the specified scopes by PUSH B.4.33 in PaperI and C.3.24/C.3.27 here; this is not attributed as an answer in E26.'),
 'C.2.2': ('found_geometric_antecedent','§2 Lemma2.1 lines330–390; Remark8.1/Conjecture8.2 lines1647–1683',
  'The untwisted section-line construction and P1-bundle pinching are E26 antecedents. The actual modified tubular cap, integral form[[6,1],[1,2]], radical and Smith factors1,11 are not supplied by that conjecture.'),
 'C.2.3': ('found_geometric_antecedent','§2 Lemma2.1 lines330–390; Remark8.1/Conjecture8.2 lines1647–1683',
  'The rational elliptic surface and section line provide the known geometric input. The actual modified cap\'s Pontryagin covector,4512/11 square and nontrivial boundary determinant are additional computations; they are not a sphere-monodromy evaluation.'),
 'C.3.1': ('found_circle_antecedent','Remark8.3 lines1695–1703',
  'The scalar C* action and its distinguished fixed edge are explicitly described; the exact free-complement/normal-weight clauses are proved in AC26, and the marked shift is in DGKXv1.'),
 'C.3.12': ('found_exact_statement_being_corrected','Remark8.3 lines1684–1723, especially1699–1704',
  'The source explicitly says the quotient by the rank-three ker(psi) translational subtori extends continuously at infinity to a further quotient of the hexagon to a circle. C.3.12 disproves that literal equivalence relation by cusp saturation. It does not refute a separately modified smooth map or the scalar-circle quotient.'),
 'C.3.13': ('found_claim_and_corrected_construction_antecedent','Remark8.3 lines1684–1723',
  'The target Seifert S3 with multiplicities3,4 is the original proposal. The receiving map changes the nearby-leaf equivalence relation in the cusp and proves its boundary marking; it is a correction, not a verification of the literal false extension.'),
 'C.3.16': ('found_seifert_antecedent','Remark8.3 lines1715–1721',
  'The Seifert(3,4) target is a source antecedent. The actual gamma-linking map(12,0,1) in the actual quotient complement is a separately specified and proved object.'),
 'C.3.18': ('found_surface_antecedent','§2 lines288–400, Weierstrass model and Lemma2.1',
  'The rational elliptic surface withIV*,III,I1 and its section/line data are known. The marked positive twelve-node page inside the actual orbit space and its boundary-frame defect−24 are additional constructions/comparisons.'),
 'C.3.21': ('found_exact_line_and_intersection_antecedent','§2 Lemma2.1 and full proof, lines330–390',
  'M=O(P−O), P·O=0, O²=−1 and the height/intersection normalization are explicit original input; on the rational elliptic surface P²=−1 gives M²=−2. The receiving theorem still has to identify the actual delta line, its boundary framing, and the twelve-I1 comparison before using this number.'),
 'C.3.24': ('found_question_antecedent','Remark8.1 lines1647–1683',
  'The proper punctured S6 bundle is explicit. No evaluation of its smooth parameter-loop mapping class is located in this opened remark or the saved whole-source searches.'),
 'C.3.27': ('found_question_antecedent','Remark8.1 lines1647–1683',
  'The proper punctured S6 bundle is the source antecedent; the independent integer-index zero determination is not printed there.'),
 'C.5.1': ('found_question_antecedent','Remark8.1/Conjecture8.2 lines1647–1683',
  'The proposed filling is historical context. The nonexistence statement is exactly the later B.4.33 obstruction for the specified family/filling data, and the zero smooth monodromy comes from the two later arguments. The conjectural source does not supply an analytic object to which Chern numbers could be assigned.'),
}

dg = {
 'E.2.2': ('found_exact_endpoint_family_antecedent','§7 integer-period-shear/core-shift lines10440–10476 and constructed action groupoid lines11955–12023',
  'The strict2Z shifts and their commuting C* family arrows already supply the endpoint gluing data. E.2.2 adds its smooth connection-based monodromy interpretation and applies the classical sphere invariant.'),
 'C.3.1': ('found_exact_marked_shear_clause','integer-period-shear/core-shift lines10440–10476; constructed action groupoid lines11955–12023',
  'The original formula Ω_(a+k)=Ω_a(I+kE41), at k=−2, is exactly I−2 delta-hat⊗gamma in the same ordered marking. The C* factor commutes with the strict shifts. Combined with AC26\'s fixed-circle geometry this is Cited/re-derived; the averaged metric proof is retained in full.'),
 'C.3.10': ('found_marked_endpoint_antecedent','global root logarithm and core-shift lines10385–10476; full cusp extension lines10560–10675',
  'The actual torus-valued endpoint translation and its finite/cusp extension are explicit known maps. The six-loop annular support reduction and lift-class comparison are the added smooth arguments.'),
 'C.4.1': ('found_fixed_twist_family_antecedent','§7 exact-period/core-shift construction and constructed action groupoid lines11955–12023',
  'The original fixed-twist family has exact even shifts and connected scalar automorphisms. The receiving theorem also compares every allowed sphere twist datum using PUSH E.1; no extension of DGKX\'s fixed-twist scope or numerical zero value is attributed to it.'),
}

else_rel = {
 'E.2.2':'The gluing comparison and Eells–Kuiper residue are established Cerf/Poenaru/Kervaire–Milnor/Eells–Kuiper results. The particular endpoint map is the supplied family calculation; this row does not evaluate the residue.',
 'E.2.3':'A retained historical target, not a new theorem to claim absent from literature. Exact later answers are PUSH B.4.33 and C.3.24/C.3.27. The search record must not be read as a general nonexistence theorem for unrelated degenerations.',
 'C.1.1':'Known classical sphere-gluing identification and Eells–Kuiper additivity, with the complete seam-sign/mapping-torus derivation retained. Cited/re-derived.',
 'C.1.2':'Known positive Milnor-sphere generator and1/28 computation, exactly Eells–Kuiper §6 equations(11)–(13), with the direct Gysin/intersection calculation retained. Cited/re-derived.',
 'C.2.1':'Known spin and spin-c characteristic formula: Eells–Kuiper §6 equation(11) and Crowley–Nordström published p35 equation(2.1). The receiving boundary cohomology and lift-independence proof is an explicit specialized rederivation. Cited/re-derived.',
 'C.2.2':'Shioda\'s section/height lattice supplies known intersection inputs. No complete statement of the actual untwisted cap lattice was located in the declared additional modern comparisons; the integral calculation is retained.',
 'C.2.3':'Analytic Riemann–Roch without a Kähler hypothesis is exactly Atiyah–Singer III Theorem(4.3) pp564–565. This source does not calculate the actual modified cap or its rational square.',
 'C.3.1':'Known-source structural combination, AC26 plus DGKXv1, and the standard averaging construction. Move the full distinct receiving proof to the known-results appendix as agreed with root.',
 'C.3.2':'The scalar gauge is null-homotopic by its real logarithm on a simply connected space; the obstruction to extending gamma is the retained elementary H1 argument. No exact separately printed family statement found in the declared modern comparison; no novelty claim for these standard mechanisms.',
 'C.3.3':'Durán–Rigas Theorem2.1 and §3.2 supply the equivariant Blakers–Massey generator and its powers; the fixed effective circle restriction is explicitly rederived. Cited/re-derived.',
 'C.3.4':'The28-element group is classical. The two possibilities differing by14 are the elementary kernel of multiplication by6; no separate novel classification is claimed.',
 'C.3.6':'The equivariant orbit-preserving multiplier theorem is known in the precise corrected scope of Karshon\'s2020 lecture. The old Haefliger–Salem non-equivariant slice lemma is false. The full direct scalar-slice proof, gauge/logarithm isotopy and support-controlled lift argument are retained; no reliance on the defective lemma.',
 'C.3.7':'The toric normalization is known; the actual scalar-circle quotient cell calculation and primitive fixed sphere are retained. Wang\'s different involution fixed elliptic/rational curves are not this statement.',
 'C.3.8':'Yang\'s complete Whitney/Thom and finite-cover-compatible collapse is a further known retraction antecedent. The actual scalar-circle quotient\'s primitive fixed-sphere class is the additional clause, already established in C.3.7; do not present the general existence of a retraction as new.',
 'C.3.9':'The exact loops are computed from the known marked toric charts. The declared comparisons located no separate printed statement with these precise FAMILY labels/signs.',
 'C.3.10':'The endpoint/core translation is known from DGKXv1. The annular reduction is a complete receiving geometric argument; generic translation language elsewhere does not certify its support or relative lift.',
 'C.3.11':'The−1 boundary-curve geometry is classical toric input. The orientation-sensitive real-normal Euler computation and immersed doublecircle are the additional marked quotient calculation.',
 'C.3.12':'This is a scoped correction to an identified original assertion, not an inference of novelty from a failed search. The proof preserves the literal nearby equivalence relation it refutes.',
 'C.3.13':'Known Seifert geometry is the target. The complete corrected map and actual cusp matching remain part of the receiving proof; a Seifert target alone is not a calculation of an orbit-knot integer.',
 'C.3.14':'The orbit smoothing, unknotting range, framed-knot/Wall surgery coordinates and Davis generator are exact opened classical results. The specified annular cap and its actual gluing comparison are the family-specific additional content.',
 'C.3.15':'The Wall/Olbermann integer is known. Its zero value requires the actual−24 and−2 inputs of C.3.18/C.3.21 and their common-sign comparison; no source classifies this specific map by its circle action alone.',
 'C.3.16':'The product3·4 linking coefficient is standard for the oriented weighted Seifert model; the complete proof identifies that model with the actual orbit-complement inclusion. The exact actual identification is not replaced by literature on a target link.',
 'C.3.17':'Known cusp toric geometry and nodal degeneration are antecedents; the complete marked product, free extension and sweep class are retained. No unmarked homotopy equivalence is credited as this marked result.',
 'C.3.18':'The rational elliptic Weierstrass/canonical/Euler framework is known, with the opened Schütt–Shioda scopes recorded. The chosen actual page,12 positive nodes and relative affine framing comparison are the retained additional geometric construction.',
 'C.3.19':'Wall\'s framing/Pontryagin normalization is known. The specific absolute value24 and framing coordinate6 are consequences of the actual relative-frame construction and its comparison.',
 'C.3.20':'Chern–Simons §3 Props3.2/3.8 supplies the standard transgression. The factor3 is directly expanded; the actual line, boundary gauge and marked lifted-torus linking remain independently identified.',
 'C.3.21':'Shioda and Schütt–Shioda provide known section and surface ingredients. The exact family-specific content is the actual relative Picard multiplier comparison and nodal excision needed to transfer the standard line square−2.',
 'C.3.22':'Standard Wall/Chern–Simons formulas are ingredients. The theorem keeps the same explicit orientation sign in both actual cap pairings, a receiving comparison needed before cancellation.',
 'C.3.23':'Haefliger/Davis supply the integer knot group and its relation to the sphere generator; Smale normalizes the fixed sphere. The actual equivariant composition and additivity proof is fully retained, with all marked/framing hypotheses.',
 'C.3.24':'The classification framework is classical. No exact zero parameter-loop value was located in the declared modern searches/opened passages; the full actual geometric integer proof supplies it. No global literature-absence or priority claim is made.',
 'C.3.25':'Jiang Lemma3.5 Case2 already uses the Hopf-handle/CP2 cap with mu=p/(24·28) at k=0, and Lemma3.6 exhibits(p−4k)/24. Crowley–Nordström supplies the spin-c formula; Montgomery–Yang is historical context. The receiving proof adds the general-k actual boundary identification and complete characteristic calculation.',
 'C.3.26':'The index integer is standard (Wall/Olbermann); fixed-sphere normalization uses Smale. The explicit characteristic bordisms and vertical Euler framing correction constitute the retained direct additivity proof.',
 'C.3.27':'The invariant and Hopf-handle machinery are known. The independent actual zero conclusion is obtained from the complete one-loop integer-index proof; it is not a conclusion of the general source formulas alone.',
 'C.4.1':'Known family-shift/classification ingredients are credited. The full parameter-dependent twist comparison and positive-loop preservation are retained; the common zero is inherited from C.3.24.',
 'C.4.2':'Eells–Kuiper orientation reversal is explicitly classical. The parameter map w→−bar(w) and the two cancelling signs are the direct given-family calculation; no order-two conclusion follows.',
 'C.5.1':'This is a precise consequence of the separately checked B.4.33 noncompletion theorem and both zero-monodromy proofs, not an invariant of an invented analytic filling. No modern source is credited with an unconstructed object\'s Chern numbers.',
}

# Load exact original-source ledgers. Each retained entry records who opened the
# original. Referencing root\'s actual check is not a claim of a second opening.
ledger_paths = [
 'deliverables/work/root/references_verified.json',
 'deliverables/work/root/classical_references_verified.json',
 'deliverables/work/maps_audit/references_verified.json',
 'deliverables/work/invariants_arithmetic/maps_D_references_verified.json',
 'deliverables/work/invariants_arithmetic/push_C_references_verified.json',
]
refs={}
for path in ledger_paths:
    values=load(path)
    if isinstance(values,dict): values=values.get('references',values)
    if isinstance(values,dict): values=[dict(v,citation_key=k) for k,v in values.items() if isinstance(v,dict)]
    for r in values:
        if not isinstance(r,dict): continue
        keys=r.get('keys',[]) or [r.get('citation_key',r.get('key',r.get('bibkey','')))]
        if isinstance(keys,str):keys=[keys]
        aliases=r.get('aliases',[])
        keys=keys+([aliases] if isinstance(aliases,str) else aliases)
        for k in keys:
            if not k:continue
            refs[k]=dict(citation_key=k,ledger=path,
                status=r.get('status'),original_source=r.get('local_source',r.get('local_opened_source',r.get('source'))),
                source_sha256=r.get('source_sha256',r.get('sha256')),
                opened_locator=r.get('opened_locator',r.get('locator',r.get('opened_locators',r.get('verification_scope')))),
                exact_scope=r.get('actual_use',r.get('verification',r.get('verification_scope'))),
                source_reader=r.get('checker',r.get('reader')),source_date=r.get('date'),
                attribution_reader_scope='This exact source-check record was read; original opening belongs to the reader identified in that record. The present investigator independently opened all records in push_C_references_verified.json.')

# The just-opened ordinary HRR scope supplements root\'s equivariant scope.
as_record=dict(citation_key='AtiyahSinger1968IIIE',status='verified_for_stated_use',verified=True,
    local_source='sources/external/root/retrieved/AtiyahSinger1968IIIE.pdf',
    source_sha256=digest('sources/external/root/retrieved/AtiyahSinger1968IIIE.pdf'),
    url='https://math.uchicago.edu/~shmuel/tom-readings/AS%20III.pdf',
    opened_locator='This reader: original §4 pp.563–565 (PDF pages19–21), visually opened, full derivation through Riemann–Roch Theorem(4.3). Independently, root opened pp.565–566 formula(4.4)/Theorem(4.6), recorded in work/root/references_verified.json.',
    actual_use='PUSH C.2.3 analytic Hirzebruch–Riemann–Roch for a compact complex manifold without assuming Kählerness; root\'s separate fixed-point/finite-group application remains covered by the preserved root record.',
    hypotheses_and_normalization_check='The original theorem assumes compact complex X and a holomorphic vector bundle V. The proof uses the Dolbeault symbol and general elliptic index theorem; the remark explicitly contrasts this general case with previously known projective cases. The stated Euler characteristic equals ch(V)Td(X)[X]. This authorizes the receiving line-bundle RR polynomial on the non-Kähler compact modification; it does not identify its own characteristic numbers.',
    extent='Exact theorem and complete displayed derivation read. Root\'s separate equivariant source opening is explicitly attributed, not silently claimed as this reader\'s opening.',
    independently_matching_record='deliverables/work/root/references_verified.json: AtiyahSinger1968IIIE',**META)
save('push_C_additional_references_verified.json',[as_record])
refs['AtiyahSinger1968IIIE'].update(opened_locator=as_record['opened_locator'],
    ledger='deliverables/work/invariants_arithmetic/push_C_additional_references_verified.json',
    exact_scope=as_record['actual_use'],source_reader=META['checker'],source_date=META['date'])


def compare(sid,source,relation=None):
    log=look[sid,source]
    op=openings[source]
    result=dict(status='not_found_in_bounded_comparison',full_statement_found=False,
       citation_key=op['citation_key'],local_source=op['local_source'],source_sha256=op['source_sha256'],
       opened_scope_record='work/invariants_arithmetic/push_C_credit_opened_scopes.json#'+source,
       opened_locator=op['opened_locator'],
       search_scope=dict(log='work/invariants_arithmetic/push_C_credit_search_log.json',
         record=sid+'|'+source,index_source=log['index_source'],index_sha256=log['index_sha256'],
         expressions=specs[sid][1],hit_counts={q['expression']:q['hit_count'] for q in log['queries']}),
       relation='No exact statement of '+specs[sid][0]+' was located in the declared whole-source term searches and explicitly opened passages. This bounded result is not an assertion of absence from unsearched sections, versions or literature.')
    if relation:
        result.update(status=relation[0],matched_locator=relation[1],relation=relation[2])
    return result


def source_statement(target):
    run,sid=target['source_run'],target['source_id']
    filename=target['source_file'].split(';')[0].split(' ')[0].rstrip(':')
    path='sources/returns/'+run+'/'+filename
    s=(ROOT/path).read_text()
    pat=re.compile(r'\\begin\{(proposition|theorem|lemma|corollary|problem)\}\['+re.escape(sid)+r'(?:\b|;)')
    m=pat.search(s)
    assert m,(sid,path)
    close='\\end{'+m.group(1)+'}'
    end=s.index(close,m.end())+len(close)
    return dict(path=path,source_sha256=digest(path),statement_lines=[s.count('\n',0,m.start())+1,s.count('\n',0,end)+1],
                statement=s[m.start():end],statement_sha256=hashlib.sha256(s[m.start():end].encode()).hexdigest())


placements={(r['source_run'],r['source_id']):r['printed_label'] for r in load('deliverables/work/root/III_source_placements.json')}
rows=[]
known={'C.1.1','C.1.2','C.2.1','C.3.1','C.3.3'}
for target in targets:
    sid=target['source_id'];row=dict(source_run=target['source_run'],source_id=sid,**META)
    row['printed_label']=placements.get((target['source_run'],sid),('fam' if target['source_run']=='S6_02_FAMILY' else 'push')+':src:'+sid)
    row['compared_assertion']=specs[sid][0]
    row['source_statement']=source_statement(target)
    row['scope_of_this_check']='Attribution comparison only. Source statements, cited contexts and listed primary passages checked; the parent\'s full receiving-proof check is preserved separately, not claimed as a new whole-proof reading here.'
    row['receiving_proof_check']=target['your_check']
    row['found_in_AC26']=compare(sid,'AC26',ac.get(sid))
    row['found_in_E26']=compare(sid,'E26',e.get(sid))
    row['found_in_DGKX_v1']=compare(sid,'DGKX_v1',dg.get(sid))
    row['found_in_DGKX_v1']['version2_comparison']=compare(sid,'DGKX_v2')
    ingredients=[]
    for key in specs[sid][2]:
        assert key in refs,(sid,key)
        assert str(refs[key]['status']).startswith('verified'),(sid,key,refs[key]['status'])
        ingredients.append(refs[key])
    modern=[compare(sid,k) for k in paths if k not in ['AC26','E26','DGKX_v1','DGKX_v2']]
    if sid in ['C.3.1','C.3.8','C.3.9','C.3.11','C.3.17']:
        item=next(x for x in modern if x['citation_key']=='manViaclovskyLogs26')
        item.update(status='found_circle_action_antecedent',matched_locator='Original lines366–378',
            relation='The two toric circle rotations extend across the Mumford boundary and commute with its period arrows. This is a known local-action ingredient, not the actual parameter-loop mapping class.')
    if sid=='C.3.8':
        item=next(x for x in modern if x['citation_key']=='manYang26')
        item.update(status='found_retraction_antecedent',matched_locator='Original lines3340–3460, Whitney–Thom and level-tube collapse lemmas',
            relation='The complete general toroidal cusp-retraction construction was independently read. It precedes the current scalar quotient\'s primitive fixed-sphere clause, which is not asserted by that lemma.')
    row['found_elsewhere']=dict(status='found_known_classical_results' if sid in known else ('found_classical_ingredients' if ingredients else 'bounded_comparison_recorded'),
        full_statement_found=False,known_result_rederived=sid in known,relation=else_rel[sid],
        sources_checked=ingredients,additional_modern_comparisons=modern,
        nonabsence_policy='Only the named files, searches and opened scopes are compared. No global priority or absence inference is authorized.')
    row['credit_classification']='Cited/re-derived' if sid in known else ('Historical target with later scoped answer' if sid=='E.2.3' else 'Exact source ingredients credited; additional marked assertion retained')
    if sid in known:
        row['printed_placement']='Known-results appendix; retain the complete source proof and exact primary credit.'
    if sid=='C.3.8':
        row['printed_placement']='Main text for the added primitive quotient-class clause; exact AC26 Proposition7.2 credit inserted at the retraction use.'
    if sid=='E.2.3':
        row['later_resolution']=['PaperI push:src:B.4.33 (specified analytic filling)', 'PaperIII push:src:C.3.24 and push:src:C.3.27 (actual positive-loop class)']
        row['historical_status_policy']='Do not relabel this historical open formulation as a present unresolved proof or a failure to read. Preserve its attempted targets with these exact later resolutions.'
    rows.append(row)

save('push_C_and_family_credit_comparison.json',rows)
fields=['source_run','source_id','printed_label','checker','effort','date','compared_assertion','found_in_AC26','found_in_E26','found_in_DGKX_v1','found_elsewhere','credit_classification']
with (W/'push_C_and_family_credit_comparison.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for r in rows:
        w.writerow({k:json.dumps(r[k],ensure_ascii=False) if isinstance(r[k],(dict,list)) else r[k] for k in fields})

insertions=[
 dict(source_run='S6_02_PUSH',source_id='C.3.1',printed_label='push:src:C.3.1',classification='Cited/re-derived',
   placement='After the statement, before its complete proof in the known-results appendix.',
   tex=r'''The fixed sphere, its normal weights, and freeness of the effective circle outside it are already established in \citet[Proposition~9.24 and Remark~9.25, pp.~82--83]{AC26}. The marked period shear and the commuting scalar action are the integer-period-shear and constructed-action-groupoid formulas of the original first version \citep[Section~7]{DGKXv1}: at $k=-2$, $\Omega_{a+k}=\Omega_a(I+kE_{41})$ is the displayed $I-2\widehat\delta\otimes\gamma$ in the ordered marking. The proof below retains the explicit equivariant-transport construction. These known formulas do not evaluate the smooth mapping class of the parameter loop.'''),
 dict(source_run='S6_02_PUSH',source_id='C.3.8',printed_label='push:src:C.3.8',classification='Main result with a known retraction clause',
   placement='At the first use of existence of an equivariant cusp retraction, without deleting any proof paragraph.',
   tex=r'''The existence of the torus-equivariant strong deformation retraction is already \citet[Proposition~7.2, p.~41; proof completed on p.~50]{AC26}. Restricting that equivariance to the scalar circle gives the retraction used here. The additional assertion is the primitive nonzero class of the fixed sphere in the quotient body; its identification uses the quotient calculation of \cref{push:src:C.3.7}. The complete retraction argument below is retained.'''),
 dict(source_run='S6_02_PUSH',source_id='C.3.25',printed_label='push:src:C.3.25',classification='Known construction credit; actual general-k comparison retained',
   placement='Existing literature-context remark after the proof already provides this credit; do not duplicate it.',
   tex=r'''The Hopf-handle and $\mathbb{CP}^2$ cap are established surgery constructions: \citet[Lemma~3.5, Case~2, manuscript pp.~13--15]{Jiang2014E} computes $p/(24\cdot28)$ when $k=0$, and Lemma~3.6 records the characteristic integer $(p-4k)/24$. The present proof retains the general-$k$ calculation and the identification of its boundary with the actual clutching sphere.'''),
]
save('push_C_credit_insertions.json',insertions)
(W/'push_C_credit_insertions.tex').write_text('\n\n'.join('% '+x['source_id']+' — '+x['placement']+'\n'+x['tex'] for x in insertions)+'\n')
save('push_C_credit_closure_summary.json',dict(rows=36,search_records=324,baselines=list(paths),
    known_rows=sorted(known),additional_main_clause='C.3.8 primitive fixed-sphere class in the actual quotient body',
    historical_target='FAMILY E.2.3, resolved at the specified B.4.33 and C.3.24/C.3.27 scopes',
    source_keys_in_insertions={'AC26':'attached original PDF, not a transcription','DGKXv1':'historical first version; adapt to the already established main bibliography alias if needed'},
    mathematical_changes='None; attribution and exact version/source metadata only.',**META))
print('Saved36 complete credit rows,324 whole-source search records, three insertion records and the exact HRR source extension.')
