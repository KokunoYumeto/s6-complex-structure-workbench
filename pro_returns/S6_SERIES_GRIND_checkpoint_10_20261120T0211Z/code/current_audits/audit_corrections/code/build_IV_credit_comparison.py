"""Bounded IV primary-source attribution and exact transport inventory."""
from pathlib import Path
import csv,json,hashlib
root=Path(__file__).resolve().parents[1]
actor='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed), S6_SERIES_GRIND/corrections_audit'
base='E26 attached S6.tex: Section2 lines289–558 (Lemma2.1, Definition2.3, Propositions2.4,2.7,2.8), Remark8.5 lines1738–1760; AC26 original Proposition9.24 and Remarks9.25–9.26, pp82–83; Jin arXiv2608.26698v2 Proposition3.1 pp10–11, Lemma4.4 pp16–17, Lemma4.8 p23, Theorem4.9 p24, Lemma6.2 pp34–35.'
transport='IV_source_morphisms.tex: tau=4/(27t+4), X=(9/2)tau²x, Y=27tau³y/(2sqrt2), with explicit inverses/minimal charts and marked point; regular point-line map F_a(p,v)=(p,f_a(p)v^a), F_a B1=B_a^a F_a, degree a², exact reference-scalar transport. Each named statement retains its own full root/fan/collar extension. K68 carries the physical M to U=M^(-1) and the inverse-clutch orientation before applying Jin.'
rows=[]
def add(label,status,claim,credit,scope,locators=base,morphism=transport,risk=''):
 rows.append({'label':label,'status':status,'precise_claim_compared':claim,
 'credited_to':credit,'source_locators':locators,'explicit_transport':morphism,
 'contribution_and_credit_verdict':scope,'bounded_search_status':'Complete at the named corpus and logged queries; no worldwide absence assertion.',
 'remaining_risk':risk or 'The comparison is source-specific and bounded. Retained prior proof/source readings remain credited at their exact scopes; this is not a fresh whole proof of every dependency.'})

add('night:P3F.21','proved','Weighted I7+III+2I1 source, M7, translation−2G, degree-four parameter cover, page(H,chi)=(14,3), physical return4.',
 'E26 Remark8.5 supplies the elliptic quotient/Mumford/log-transform construction; Shioda1990 Theorem8.6 and Proposition8.12 supply the height and base-change laws; Jin supplies the characteristic/mapping-torus classification.',
 'Credit the construction and height/classification inputs explicitly. The source equation, genuine M7 Hom section, integral cusp basis, page and positive physical class4 are the displayed source-specific derivation. The bounded AC26/E26/DGKX comparison located no identical marked weighted-return assertion.',
 locators=base+' Shioda original pp228–231, Theorem8.6/eq8.12, table8.16, Proposition8.12/eq8.25 (retained original scan reading).',
 morphism='Set E26 Remark8.5 data equal to the printed source, M=O(7G−O), and t=t_(2G). Its Hom degree is the explicit intersection1+1−1+0=1, and the induced bundle map covers−2G by E26 Definition2.3. At I7 use H=h^(−1)g^(−2), K=h^4g^7, with determinant-one matrix[[-1,4],[-2,7]]. The actual page and physical-dual/clutch maps produce class4.')
add('night:P3F.35','proved','Every one-vertex unimodular periodic fan is a basis fan; actual periodic flops preserve sphere topology; every prime cusp fixed set has total Betti number2, forcing cap freeness.',
 'AC26 Proposition9.24 and Remarks9.25–9.26 provide the reference fixed curve, normal weights and all finite-subgroup fixed sets; E26 Proposition2.8 provides periodic simplicial Mumford fillings; Floyd1952 Theorem4.4 gives the mod-prime fixed-set inequality.',
 'The reference-fan assertions are credited known results. The proof extends their actual quotient-lattice calculation to all basis fans and combines it with the displayed integral common-blowup maps and Floyd inequality. This comparison does not assign a new source-free novelty claim to those known ingredients.',
 locators=base+' Floyd original Theorem4.4 p146; coefficient convention p139. Fresh publisher retrieval returned403; the exact earlier original-source reading remains credited.',
 morphism='AC26 triangles become T(e1,−e2) by the explicit diag(1,−1) basis adapter and lattice translation. For every edge e, Z²→Z²/Ze sends delta to det(e,delta). The three edge orders are|b|,|a|,|a−b|. Each periodic flop is the common blowup with exceptional P1×P1 and the two ruling contractions; exceptional degree−1 proves integral primitivity before the sphere and fixed-set deductions.')

named={
99:('Selected-other-node M6 source loop, quadratic cap, initial pair(−27,−12), physical index−4.','The actual source loop and marked-node exchange, fixed scalar/reference and completed cap/ordinary maps are retained before its characteristic calculation.'),
100:('All-basis-fan formula−4+3(Q−1)/2−27(Q²−1)/8, Q=x²+xy+y²; exact16-residue image.','The physical pair from K99 is transported through the ordered full fan maps. The complete primitive-residue image was freshly checked modulo112 in independent_IV_checks.py.'),
101:('Selected-infinity full epsilon loop, r=epsilon²(3epsilon²−2)/(1−3epsilon²)², original scalar fixed, initial pair(−4,8), physical index−1.','The displayed map has the stated local degree2 to the r coordinate. The initial return belongs to the full epsilon loop with its prescribed original heights, roots and endpoints.'),
102:('Selected-infinity all-fan formula(2/3)(S6(P)+1)−Q; exact14 odd residues; vertical pair(−4−12j(j−1),8).','The source-specific native and stable tangent systems determine the fan polynomial/image. The all-fan image is compared at the full marked source and actual parameter degree.'),
103:('The K99 pair and fan values persist for every reduced infinity cap m=3l+2, both signed norms and retained finite characters.','The full original/root Cartier correspondence and relative cap product identify k and ell separately. The comparison has the exact K99 initial-pair input scope.'),
104:('Selected-infinity K101/K102 returns for every reduced infinity cap, with the same14 odd residues.','The proof carries the original source loop, all root characters and complete annular reference through the actual cap comparison; numerical equality alone is not used.'),
105:('M2/−3G selected-infinity family with every good infinity cap m=3l; the same14 odd residues.','The genuine M2 point line and its full chronological map enter the proof. The displayed regular degree-four isogeny to the M1 construction supplies a concrete literature relation, while this statement supplies its own completed-root and parameter maps.'),
106:('Selected-I3 M6 quadratic-cap source loop, initial pair(47,−4), physical index8; vertical k=47−2j³+18j²−52j, ell=−4; all28 residues.',
     'The full source normal form, original heights, physical line, cap extension and target-prism construction determine these numbers. This audit freshly reconstructed complete finite words witnessing all28 residues by depth7, with the source-specific initial pair retained from its complete supplied proof.'),
107:('Selected-other-node M2 good-cap family, initial pair(−3,−12), index0; all-fan formula−3(Q−1)(Q−3)/8 and the same exact16 residues.',
     'The M2 point-line chronology and original cap maps are retained. The closed primitive image was freshly exhausted modulo112; the geometry and the full initial pair remain the named proof inputs.'),
108:('The selected-I3 K106 construction for every reduced infinity cap m=3l+2, both norms and all retained finite characters; separate pair preservation and all28 fan returns.',
     'The complete K108 proof and K103 source/root inputs were freshly read. Actual signed meridian inverses, source chords, point/O Cartier graphs, and relative cap products identify each characteristic integer before invoking K106’s fan witnesses.')}
for n,(claim,detail) in named.items():
 add('night:P3K.'+str(n),'proved',claim,
 'E26 Section2/Remark8.5, AC26 toroidal construction, Shioda height laws and Jin exact characteristic/mapping-torus classification are credited inputs; the named source-loop and fan computation is retained as the manuscript contribution.',
 detail+' The bounded searches of AC26 original, E26 and both DGKX versions located no identical marked numerical-return statement. This is a statement about the checked corpus and queries, without a universal literature-absence claim.')

historical={
10:('The same primitive OS45 positive family has physical class3 rather than25.','Use M8 on the displayed I8+4I1 source, the fixed ordinary norm-one cap and positive primitive loop. K68’s exact physical line/dual/inverse-clutch maps turn the retained page H=8,chi=1 into(24,24), A_M=3.'),
22:('The ten primitive-source profiles have physical integers3,6,9,14 for d=8,14,20,30.','The Oguiso–Shioda source rows and actual line/page/cap data are retained. K68/K69 transport U=M^(−1) to physical M and give A_M=d/2−1. The smooth-cap torsion is the injective degree-two H2 contribution, as repaired in proposed_patches.json.'),
23:('The specified fixed-edge physical flop gives7A_M and the profile residues21,14,7,14.','The same quaternion common-link and oriented commutator maps give native right integer n=6A_M. Adding that integer to A_M gives7A_M; the concrete centre, exterior and positive parameter are fixed.'),
30:('Physical characteristic pair(3H,24chi), integerH/2−chi; retained native pair(6chi,3H−6chi).','The explicit nonzero-line dual map v↦v^vee, v^vee(v)=1, reverses the fibre circle and carries c1(U)=−c1(M), hence negates both cubic and p1-line pair. K68’s fixed quotient orientation and inverse endpoint give the stated sphere transfer.'),
31:('The universal norm-only fan polynomial is refuted by the actual OS45 T0/T2 pair of returns3,2 with the same old norm input1.','The exact vertical fan basis is T_j=(e1+je2,e2); delta has coordinates(0,1) for T0 andT2. The full directed K64 comparison subtracts J*j(j−1)/2=1 atJ=1,j=2. K73 supplies the ordered target-prism replacement.'),
33:('The original shorter K=L=1 family has T2 return26; its exact all-fan image is all28 classes.','Retain w_h=exp(−pi i c/(KL))=r^6 and u=kappa w_h^(2KL), the actual endpoint/root/cap arrows and completed sixfold covering. Their primitive inputs are J=2KL,Hhat=KL/3,chihat=KL/6. The K73 vertical term is−2 atK=L=1,T2; fresh Q0² gives3 for the actual unscaled profile.'),
'F53':('The received catalogue’s physical reference and all-fan polynomial columns are corrected; primitive OS45 reference is3.','The source-pair/root table retains its explicit sixteen-profile,twenty-six-pair,thirty-one-branch constructive scope. K68/K69 give(3H,24chi), H/2−chi. The full K73 period/seed maps apply to whole-zero I1 cases, and the explicit K77 seed/period maps apply to the component-supported OS49 cases.')}
for key,(claim,morphism) in historical.items():
 label='night:P3F.53' if key=='F53' else 'night:P3K.'+str(key)
 add(label,'false as stated; refined receiving proposition proved',claim,
 'The located received source claim and its concrete construction are credited at the original label. The corrected conclusion is iv:correction:'+('P3F.53' if key=='F53' else 'P3K.'+str(key))+'. External construction and classification inputs retain their own credit.',
 'This is a scoped correction/counterexample to the printed received compound claim. The exact construction, orientation, parameter degree and morphism identify both the historical assertion and the corrected value. Known elliptic-surface, toroidal and bordism inputs remain cited at their original loci.',
 locators=base+' Oguiso–Shioda1991 Main Theorem pp85–86 rows43–61; Shioda1990 pp228–231 (retained exact original readings).',morphism=morphism)

fields=list(rows[0])
with (root/'IV_literature_comparison.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
(root/'IV_literature_inventory_updates.json').write_text(json.dumps({r['label']:{
 'credited_to':r['credited_to'],
 'literature_searches':r['source_locators']+' '+r['bounded_search_status'],
 'in_compendium_only_because':r['contribution_and_credit_verdict'],
 'credit_transport':r['explicit_transport'],
 'source_credit_verdict':'bounded primary-source comparison complete; exact known inputs credited'
} for r in rows},ensure_ascii=False,indent=2)+'\n')

front={
'A':r'''The characteristic classification and native generators are the known results of \cite[Proposition~3.1, Lemmas~4.4 and~4.8, Theorem~4.9, and Lemma~6.2]{Jin2026}. The source uses the seam $(x,0)\sim(f(x),1)$, its preferred clutch generator has $\langle p_1,[S^4]\rangle=4$, and its pairs are $(1,4)$ and $(8,8)$. The exact line-duality, Hopf-normal and inverse-endpoint maps in \cref{night:P3K.68} transport those data to the physical $M$ and the forward seam here. The resulting source-page formula and the corrections to \cref{night:P3K.30} are stated with that fixed transport.''',
'B':r'''The elliptic-surface input is \cite[Main Theorem, pp.~85--86]{OguisoShioda1991}, with the height and base-change laws of \cite[Theorem~8.6 and Proposition~8.12, pp.~228--231]{Shioda1990}. The actual quotient, Mumford filling and logarithmic modifications instantiate \cite[Section~2 and Remark~8.5]{Engel2026}; the specified surface, point line and translation are the input maps. The page and physical-clutch calculations give the displayed source-specific integers, including the weighted $M_7,-2G$ class four. The corrected fixed-edge rule uses the retained common-link map and native right integer $6A_M$, hence $A_M+6A_M=7A_M$. The precise historical claims are \cref{night:P3K.10,night:P3K.22,night:P3K.23,night:P3F.53}.''',
'C':r'''Periodic simplicial fillings are already provided by \cite[Proposition~2.8]{Engel2026}. For the original reference fan, the fixed curve, its weights and finite-subgroup fixed sets are \cite[Proposition~9.24 and Remarks~9.25--9.26, pp.~82--83]{AC26}; the basis adapter and quotient-lattice map are retained in \cref{night:P3F.35}. Here the complete parameter endpoint and each target prism determine the physical return on the ordered fan. The explicit pairs of actual returns in \cref{iv:correction:P3K.31,iv:correction:P3K.33} locate the failed norm-polynomial assertions and identify their replacement.''',
'D':r'''The elliptic quotient and logarithmic-cap construction is \cite[Section~2 and Remark~8.5]{Engel2026}. At $r=0$, the literal source map is $\tau=4/(27t+4)$, $X=(9/2)\tau^2x$, $Y=27\tau^3y/(2\sqrt2)$; it preserves the marked point and extends by the displayed minimal-coordinate unit maps. For each point line, multiplication by its full Miller function gives $M_1^{\otimes a}\to M_a$, and the chronological identity $\mathcal F_a\mathcal B_1=\mathcal B_a^a\mathcal F_a$ relates the regular quotients. The present source-loop assertions include their additional original-height, root, fan and endpoint maps, and retain the exact parameter degrees when evaluating returns.''',
'E':r'''The elliptic/toroidal construction is credited to \cite[Section~2 and Remark~8.5]{Engel2026}, and the physical characteristic classification to \cite[Theorem~4.9 and Lemma~6.2]{Jin2026}, through the explicit transports of \cref{night:P3K.68}. The additional conclusions here are the marked-source pairs $(-27,-12)$ and $(-3,-12)$, the full cap products preserving both integers, and the two ordered-fan formulas with their exact sixteen-element image. The comparison with AC26, E26 and both DGKX versions is recorded at these precise marked-return claims.''',
'F':r'''The construction and bordism inputs are \cite[Section~2 and Remark~8.5]{Engel2026} and \cite[Theorem~4.9 and Lemma~6.2]{Jin2026}. The actual source-coordinate map, its degree-two parameter arrow, original scalar/reference and point-line maps identify the loop whose pair is $(-4,8)$. The full root and cap comparisons carry that marked loop to the displayed families; the ordered target-prism calculation gives the exact fourteen odd residues. The source comparison retains those maps and parameter degrees.''',
'G':r'''The elliptic quotient/Mumford construction and the characteristic classification are the credited inputs \cite[Section~2 and Remark~8.5]{Engel2026} and \cite[Theorem~4.9 and Lemma~6.2]{Jin2026}. The source-specific calculation in \cref{night:P3K.106} gives $(47,-4)$ and the actual integral fan words. The full relative cap products in \cref{iv:i3_all_reduced_caps} identify $k$ and $\ell$ separately for every stated reduced cap and both signs before carrying those words to the completed family. The exact comparison keeps the original source height, line, annular reference and physical inverse-clutch map.'''}
(root/'IV_literature_front_patches.json').write_text(json.dumps({
 'patch_scope':'Replace only Relation to literature paragraphs in the seven IV front statements; optional IV_source_morphisms.tex supplies the full receiving derivation of the cited comparisons.',
 'main_theorems':{k:{'label':'series:IV:'+k,'literature_tex':v} for k,v in front.items()}},ensure_ascii=False,indent=2)+'\n')

queries=[
 ('system1','"six-sphere" "monodromy" complex Eells Kuiper','arxiv.org;365 days','No matching result returned in the prior recorded search.'),
 ('system1','"elliptic" "exotic spheres" "monodromy"','arxiv.org;365 days','No matching result returned in the prior recorded search.'),
 ('system1','"complex" "six-sphere" "logarithmic"','arxiv.org;365 days','No matching result returned in the prior recorded search.'),
 ('system2','"sphere" "monodromy" "Engel" complex structures','arxiv.org','No matching result returned in the prior recorded search.'),
 ('system2','"2608.26698"','arxiv.org','No result from this engine; stronger search below located the primary article.'),
 ('system2','"six-sphere" "family" exotic','arxiv.org','No matching result returned in the prior recorded search.'),
 ('system1','"Eells-Kuiper" "circle actions" "Jin"','arxiv.org;365 days','No matching result returned in this query.'),
 ('system1','E E Floyd "On periodic maps" "4.4"','ams.org','Primary publisher PDF attempt HTTP403; retained exact original reading is credited.'),
 ('system1','Primary Jin-title search; exact query text not reconstructed','arxiv.org','Located primary arXiv2608.26698v2; complete cited loci freshly opened. This row records the actual source-discovery event and does not present an invented literal query.'),
 ('system1','"Complex structures" "six-sphere" "monodromy" "family"','arxiv.org','No exact marked numerical-return assertion located.'),
 ('system1','"exotic spheres" "complex structures" "six-sphere"','arxiv.org;365 days','Combined query batch returned Viaclovsky2610.10451 and other records; no exact target return statement was displayed. Ref turn201138492academia0.'),
 ('system1','"scalar" "monodromy" "six-sphere"','arxiv.org;365 days','Combined batch mostly unrelated hits; no exact marked return claim located.'),
 ('system1','"rational elliptic surfaces" "logarithmic transformations" sphere complex','arxiv.org;365 days','Combined batch returned no exact target marked numerical-return assertion.'),
 ('system2','Oguiso Shioda1991 Mordell Weil lattice rational elliptic surface Main Theorem pdf','projecteuclid.org;jstage.jst.go.jp','Search located bibliographic references but not exact original table; exact original Rikkyo URL and earlier visual reading are preserved in bibliography.'),
 ('system2','Shioda1990 Mordell Weil lattices Theorem8.6 8.12 pdf','rikkyo.ac.jp;jstage.jst.go.jp;projecteuclid.org','Search located related primary papers and references; exact original Rikkyo URL, printed pages and earlier complete cited proofs are retained.')]
with (root/'IV_literature_searches.tsv').open('w',newline='') as f:
 wr=csv.writer(f,delimiter='\t');wr.writerow(['date','engine','query','scope','result_and_limit'])
 for q in queries:wr.writerow(['2026-11-19',*q])

p=root/'CHECK_EVENTS.tsv'
with p.open(newline='') as f:
 rd=csv.DictReader(f,delimiter='\t');fields=rd.fieldnames;events=list(rd)
for row in rows:
 outcome=('Bounded primary-source comparison completed. '+row['source_locators']+' '+
 row['contribution_and_credit_verdict']+' Exact transport: '+row['explicit_transport']+
 ' Inventory: IV_literature_comparison.tsv; searches: IV_literature_searches.tsv; full receiving comparison: IV_source_morphisms.tex. The source equation transport is independently checked in independent_IV_joint_checks.py. No worldwide absence or fresh complete reading of every retained dependency is claimed.')
 event={'statement_id':row['label'],'date':'2026-11-19','who':actor,'type':'targeted proof check','outcome':outcome,'phase':'S6_SERIES_GRIND'}
 event['event_id']='s6sg:'+hashlib.sha256((row['label']+'|source comparison|'+outcome).encode()).hexdigest()[:20]
 if not any(x['event_id']==event['event_id'] for x in events):events.append(event)
with p.open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=fields,delimiter='\t');wr.writeheader();wr.writerows(events)
print(len(rows),'source comparison rows;',len(queries),'bounded search records;',len(events),'typed events retained')
