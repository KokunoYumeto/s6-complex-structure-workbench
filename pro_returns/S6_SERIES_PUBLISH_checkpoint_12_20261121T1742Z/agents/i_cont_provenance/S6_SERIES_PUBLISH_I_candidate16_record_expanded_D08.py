#!/usr/bin/env python3
"""Serialize actual row-by-row contextual D08 dispositions, without page/check credit."""
from pathlib import Path
from datetime import datetime, timezone
import collections
import hashlib
import json
ROOT=Path(__file__).resolve().parents[2]; OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bind=lambda p:{'path':str(p.relative_to(ROOT)),'sha256':sha(p)}
SOURCE_SHA='61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc'
PDF_SHA='4a1633d9e19a82e3df92a0e3c31ada306b3e801f3051b0c1b7f0018d873f51a2'
scan_path=OUT/'S6_SERIES_PUBLISH_I_candidate16_D08_expanded_scan.json'
compute_path=OUT/'S6_SERIES_PUBLISH_I_candidate16_D08_compute_scan.json'
scan=json.loads(scan_path.read_text()); compute=json.loads(compute_path.read_text())
assert scan['source_sha256']==compute['source_sha256']==SOURCE_SHA
assert scan['pdf_sha256']==compute['pdf_sha256']==PDF_SHA
# Each entry is the disposition written after the displayed context was actually read.
NOTES='''
1|Below compares a level value with the maximum; it is an inequality relation.
2|Following points directly to the three displayed cohomology tables and their indexing conventions.
3|Below identifies the dependency table under the figure in the organization section.
4|The chart maps specify the coarse invariant direct image beyond the exact cited Picard/cohomology result.
5|The same normalized theta norm is transported by the explicit scalar and subsequent period map.
6|Below identifies division functions transported by the displayed change of Weierstrass coordinates.
7|Below one is the asserted location of real roots.
8|The recurrence gives the displayed polynomial identities over Q[t]; the ring and exact recurrence are substantive.
9|Following points to the rational bound table used in the multiplication estimate.
10|Following introduces the displayed derivative inequalities on the stated disc.
11|Following introduces the differentiated-theta upper-bound table and the tail method.
12|Below qualifies the finite covers whose exact maps and degrees are then constructed.
13|Bounded below is the explicit barycentric inequality.
14|Following introduces the rational columns, cocycles and translation vectors in the displayed formulas.
15|Below one is the nome-modulus condition for convergence.
16|Following introduces the precise arithmetic classification conditions and linear parts.
17|Root-owned standalone cusp-necessity announcement; exact local-lift argument is retained by I16-root-01.
18|Same root-owned announcement as row 17; no duplicate guard.
19|Following introduces the rational solutions of the stated linear equations, followed by their maps and inverses.
20|We prove is immediately attached to the explicit equality Gamma=ker chi and the kernel/generator construction. Retain this mathematical proof target.
21|Following introduces the full central-extension group law and cocycle.
22|Following introduces the exact matrices giving an infinite stabilizer.
23|Standalone properness announcement; I16-prov-03 removes only this sentence after full-proof review.
24|The sentence identifies the dense infinite-stabilizer locus used for maximality; the explicit Hermitian comparison and rational-density argument follow. Retain the mathematical criterion and construction.
25|Below identifies the arithmetic equation related by the explicit mutually inverse maps.
26|Following introduces the defining lattice equation in Z^6.
27|Following introduces the exhaustive list of compact curves by fibre type.
28|Below identifies the positive Appell--Humbert theta sections that define the stated divisors.
29|Below fixes the toric character convention for the three gluing constants.
30|Following introduces an exact sequence of specified locally free sheaves.
31|Below refers to the normalization of the target frame in the scalar formula.
32|Below points to the common Hodge pattern and its explicit evaluation map.
33|Below identifies the invariant fibre class used in the algebra generators.
34|The source attribution is retained. Its adjacent production announcement is removed by I16-prov-16, also found in compute row C3.
35|The remark describes the precise cocycle and smooth-coefficient form supplied by the construction, with exact original chart/parameter comparisons. Retain this mathematical scope and source credit.
36|Below identifies the exact scalar cocycle equality on generating arrows.
37|Following introduces the displayed affine line lift and its phases.
38|Following points to the finite derivative recursion; all local inverse branches are part of its mathematical definition.
39|Following introduces the explicit Green/operator normalization and the primitive class relation.
40|The sentence identifies the cocycle/weight changes between two coefficient gauges, followed by the exact coboundary maps in the remark.
41|Following introduces the frames for the chain-level comparison.
42|Following introduces the finite complex of holomorphic bundles representing the invariant complex.
43|For clarity introduces evaluation in the original Weierstrass normalization, with exact coordinate identities and coefficients. Retain the mathematical normalization and calculation.
44|Following refers to the nonzero scalar whose sign changes under the displayed resonance sign.
45|The computed nonzero coefficient determines the two transverse orders in the subsequent Smith presentation.
46|Following introduces the invariant-exponent and pullback-frame character convention.
47|Following introduces the ordered meridian slopes and determinant defining the lens-space convention.
48|Following introduces the even-shift translation formula used in the specified conjugation.
49|Following introduces the ordinary-chart translation with its logarithm convention and formula.
50|Following is part of the precise published-source locator for the noncompact analytic-resolution extension.
51|The sentence states applicability to a smooth given total space; it preserves a mathematical scope of the ensuing argument.
52|The local graph construction proves analytic closure and properness using its displayed equation and dominating component.
53|Following identifies coefficients unchanged by the stated central correction, before their explicit definitions.
54|Standalone extension announcement; I16-prov-04 preserves every determinant, direct image and parameter-recovery step.
55|Following introduces the canonical base-change exact sequence and its torsion term.
56|Below identifies the exact dual-lattice formula yielding the continuous extension.
57|Following introduces the complete limit-group description, subgroup and functional.
58|Below points to the explicit Hausdorffization of the named rank-three quotient.
59|Below this height is the stated sign inequality.
60|Below the maximum is the level inequality used for the star-shaped curve.
61|For clarity accompanies the explicit value on v0 and its intersection derivation. It states mathematical content, not a run/check record.
62|Following introduces the product presentations and their exact maps to the marked central tori.
63|Root-owned Tate-chart announcement, I16-root-02; no duplicate guard.
64|Same root-owned announcement as row 63.
65|Following introduces the finite-data mathematical parametrization by fan tests.
66|Following introduces the exact determinant, common-face, volume and boundary tests defining a fan datum.
67|Following introduces finite arithmetic counts of rays and unimodular subsets, with the complete-collection tests separately stated.
68|Following introduces the actual normalization/modification algorithm and its input/output maps.
69|Following introduces the explicit centres and section coordinates whose flatness is proved.
70|Standalone integral-check announcement; I16-prov-05 retains the node generizations and unimodular matrix.
71|Following is the exact primary-source locator for the analytic-resolution extension.
72|Below one is the uniform exponent inequality for the gradient retraction.
73|Standalone closing inventory of maps; I16-prov-06 retains every computed integral map and its uses.
74|Standalone factorization announcement; I16-prov-07 retains boundary, subdivisions, factorization theorem and all analytic comparison maps.
75|The sentence states that additional mixed-height rays have no effect on the punctured-base argument, following their exact support q=0.
76|We record specifies the deck-identification convention for peripheral permutations. Retain that convention and the exact inverse relation with path holonomy.
77|The inverse-permutation relation preserves the same group relation and contradiction; the rotations and orientation options remain explicit.
78|The intersection computation fixes component indices for the height lattice; its role is a mathematical dependency, followed by exact local expansions and intersections.
79|Following introduces the entries of the integral intersection matrix and the resulting index bound.
80|Following is part of the precise published-source locator for the transgression remark.
81|Following introduces the cap assembly with its exact hypotheses and conductor pullbacks.
82|Following introduces the precisely quantified impossible extension, retaining all base-change and line-bundle conditions.
83|Below identifies the holomorphic section establishing the zero cusp torsor class.
84|Below refers to groups invariant under reversal of the explicitly fixed loop convention.
85|Below identifies the specific normal-line matching; the nearby gluing announcement is separately guarded at row 86.
86|Standalone gluing-domain announcement; I16-prov-08 retains all domains, constants, inequalities, maps and quotient construction.
87|Following all n stages describes the actual composition of blow-ups and its weighted normal-line effect.
88|Two standalone obstruction announcements, I16-prov-09 and I16-prov-10; the positive criterion, single-singularity hypothesis and complete Stein-cover calculation remain.
89|Following is part of the exact published-source discussion locator.
90|Standalone three-piece-recording announcement; I16-prov-11 retains all divisors, normal products and evaluation maps.
91|Following introduces the displayed cohomology groups and representations.
92|I16-prov-12 retains the exact Fujiki credit positively and the entire vector-field calculation, removing the record-a-check wording.
93|For clarity introduces the explicit node-coordinate convention and chart-index map. Preserve all coordinates and the closing-period relation.
94|Below identifies the exact local ambient base equation uv-h.
95|Following introduces the properties of the explicitly counted point/curve modification.
96|Following introduces the local coordinate description, divisor, parameters and unit.
97|Standalone verification announcement; I16-prov-13 retains the asserted product, all character orders and the complete comparison maps.
98|Standalone deformation announcement; I16-prov-14 retains the exact normal sequence and deformation argument.
99|Following is the exact published-source locator for the noncompact analytic-resolution extension.
100|The sentence identifies the finite-multisection consequence of the explicitly cited log-torsor obstruction. Retain this named mathematical dependency and the ensuing normalized finite-base-change operation.
101|Below identifies the same trivializing central section used in two named mathematical arguments.
102|Following is part of the exact Oda source locator for the lattice/unit construction.
103|Following introduces the explicit automorphism properties in the mathematical example.
104|Following introduces a quantified vanishing-cycle property and its exact lattice target.
105|Bounded below describes the Laurent expansion and valuation inequality.
106|Following introduces six substitution values of the displayed formulas.
107|Root-owned derived-duality positive restatement, I16-root-03; the sheaf, derived map and torsion contribution remain.
108|Retain the rational topology computation by the actual attachment maps, as reviewed by root; the exact Mayer--Vietoris matrices follow.
109|Following introduces the two explicit Mayer--Vietoris matrices and their ordered bases.
110|Below identifies the table contributions produced by the exact local-height formula.
111|Following introduces the CM minimal-model and height tables with the exact pointed isomorphism.
112|Following introduces numerical approximations qualified by explicit error bounds and the cited enclosures.
113|Following is part of the exact Call--Silverman source locator.
114|Below identifies the Fourier/product algorithms that prove the stated enclosure radius.
115|Below identifies the Fourier intervals used with integrality to identify the singular modulus.
116|Below identifies the derivative sums and error bounds that support the analytic-rank statement.
117|Below 10000 is a numerical comparison of the Sturm bounds.
118|Following introduces central-derivative values with explicit error and exact-zero qualifications.
119|Cut below is the numerical remainder cutoff; the context also identifies the exact cancellation allowance.
120|Below identifies the rounding allowance controlling the stated kernel-series cancellation.
121|Below identifies the derivative allowance resulting from the stated elementary-evaluation and Taylor errors.
122|Below is the numerical comparison between intermediate terms and the stated bound.
123|Below is the numerical comparison between accumulated errors and the allowance.
124|Below identifies the rational denominator bound supplied by the Gross--Zagier formula.
125|Following introduces explicit base curves, discriminants and Heegner data.
126|Below identifies intervals proving the positive auxiliary central values used in the rank argument.
127|Below is the central-value-tail numerical bound.
128|Below is the derivative-tail numerical bound.
129|Following introduces the rational error-bound table used for exact separation.
130|Below identifies the estimates that ensure regularity of the defined branch on its disc.
131|Below identifies the estimates proving the explicitly needed nonvanishing of C.
132|Editor-owned four-bound announcement, I16-edits-01.
133|Same editor-owned announcement as row 132.
134|Editor-owned recurrences/tails announcement, I16-edits-02; all recurrences and bounds remain.
135|For clarity is attached to the explicit unrounded rational bounds and their constants. Retain these substantive numerical expressions.
136|Editor-owned polarization roadmap, I16-edits-03; the exact cited group statements remain.
137|The phrase introduces the principal polarization, Q0 and Rosati/dual convention as an actual coordinate operation. Preserve the convention and every displayed relation.
138|Below quantifies the field of definition of the endomorphisms and extensions in the definition.
139|Editor-owned positive period-comparison restatement, I16-edits-07; its nearby closing sentence is I16-edits-06.
140|Editor-owned polynomial-identity announcement, I16-edits-10; the values and polynomial map remain.
141|Editor-owned section roadmap, I16-edits-11; exact coordinate/source reference retained by that guard.
142|The statement links the rank/growth data to the explicitly numbered numerical inequality. Preserve that mathematical comparison and reference.
143|The coefficient estimate names the method of the uniform-height proof, followed immediately by the polynomial degree, circle and Cauchy estimate. Retain this substantive dependency, consistently with the attachment-map wording retained at row 108.
144|First approved visual guard I16-prov-01; full local-lift and parity argument preserved.
145|Below fixes the evaluation point for all functions in the statement, a necessary convention.
146|Second approved visual guard I16-prov-02; complete critical-scheme calculation preserved.
147|Below identifies the coprime multiplicities of the following theorem while preserving the exact standard-case credit.
148|The closing sentence identifies the analytic Picard conclusion of the displayed group presentation, used in the succeeding bundle calculation.
149|The statement names Koszul maps as the computational method for coarse direct images. Preserve this method and every exact map.
150|Following fixes a local frame convention and gives its explicit transformation and relation to the original cocycle.
151|Permitted Programs-table introduction, with historical commit and complete source paths; no body bookkeeping is introduced.
'''
notes={int(line.split('|',1)[0]):line.split('|',1)[1] for line in NOTES.strip().splitlines()}
assert set(notes)==set(range(1,152))
owned={17:['I16-root-01'],18:['I16-root-01'],63:['I16-root-02'],64:['I16-root-02'],107:['I16-root-03'],
       132:['I16-edits-01'],133:['I16-edits-01'],134:['I16-edits-02'],136:['I16-edits-03'],
       139:['I16-edits-06','I16-edits-07'],140:['I16-edits-10'],141:['I16-edits-11']}
ours={23:[3],54:[4],70:[5],73:[6],74:[7],86:[8],88:[9,10],90:[11],92:[12],97:[13],98:[14],34:[16],144:[1],146:[2]}
rows=[]
for r in scan['rows']:
    i=r['index']; guards=owned.get(i,[])+[f'I16-prov-{n:02d}' for n in ours.get(i,[])]
    rows.append({**r,'row_id':f'R{i:03d}','context_actually_read':True,
                 'disposition':'confirmed D08; exact proposal pending application' if guards else 'retained mathematical use or permitted table text',
                 'reason':notes[i],'guard_ids':guards,'full_page_reading_credit_added':0,'mathematical_events_added':0})
cnotes={
1:'Abstract-level summary of the actual integral-monodromy, domain and fibre-dimension results; permitted concise result summary.',
2:'The proof computes the named line bundle O_X(H) via exact invariant exponents and upper modifications. Retain the mathematical target and operation.',
3:'Statement-level production announcement removed by I16-prov-16; exact source credit, Chern map and Green representative remain.',
4:'Generic sign-that-matters announcement removed by I16-prov-17; complete orientation and sign calculation remains.',
5:'The numbered proof step identifies the cusp fixed-set calculation, immediately defining its normalization and involution. Retain this actual mathematical operation.',
6:'Closing promise to compute the already displayed sequence maps, removed by I16-prov-18; all primitive images and their proofs remain.',
7:'The sentence identifies the neck decomposition used to compute the monodromy map; the sweep/Gysin construction immediately realizes it. Retain the method.',
8:'The sentence names the normalization mapping cylinder as the reference-centre computation method; the concrete base change and conductor resolution follow. Retain the method.',
9:'The sentence introduces an actual calculation using the cited cusp functions and immediately lists their defining formulas. Preserve the source reference and coordinates.',
10:'The proof identifies and computes the local higher direct image through the Atiyah extension and its restriction maps. Retain this scoped mathematical operation.',
11:'Standalone finishing announcement referred by the editor; I16-prov-15 preserves the complete polynomial/Bernstein proof.',
12:'The sentence identifies the Koszul-map method for the direct images, with exact coefficients and frame changes; retain the mathematical method.',
13:'The numbered proof step computes components of the translation group via the explicit lattice sheaf and exact sequence. Retain that scoped mathematical operation.',
}
cguards={3:[16],4:[17],6:[18],11:[15]}
for r in compute['rows']:
    i=r['index']; ids=[f'I16-prov-{n:02d}' for n in cguards.get(i,[])]
    rows.append({**r,'row_id':f'C{i:03d}','context_actually_read':True,
                 'disposition':'confirmed D08; exact proposal pending application' if ids else 'retained mathematical use or abstract result summary',
                 'reason':cnotes[i],'guard_ids':ids,'full_page_reading_credit_added':0,'mathematical_events_added':0})
assert len(rows)==164
guard_paths=[OUT/'S6_SERIES_PUBLISH_I_candidate16_provenance_guards.json',OUT/'S6_SERIES_PUBLISH_I_candidate16_expanded_guards.json',ROOT/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_root_guards.json',ROOT/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_edits_guards.json']
result={
 'created_utc':datetime.now(timezone.utc).isoformat(),'paper':'I','candidate':16,
 'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,
 'source_snapshot':bind(OUT/'candidate16_review_blocks/S6_SERIES_PUBLISH_I_candidate16_source_snapshot.tex'),
 'scans':[bind(scan_path),bind(compute_path)],'contexts_actually_read':164,
 'source_count_binding':bind(OUT/'S6_SERIES_PUBLISH_I_candidate16_source_count_rebinding.json'),
 'rows':rows,'disposition_counts':dict(collections.Counter(r['disposition'] for r in rows)),
 'guard_files':[bind(p) for p in guard_paths],
 'additional_own_guards':'I16-prov-03 through I16-prov-18; root approved after reviewing the exact replacements and preservation scopes.',
 'already_owned_loci_outside_selected_pattern':['I16-edits-04','I16-edits-05','I16-edits-06','I16-edits-08','I16-edits-09'],
 'candidate15_reopening':bind(OUT/'S6_SERIES_PUBLISH_I_candidate15_D08_reopening_receipt.json'),
 'reopening_explanation':'The earlier selected-keyword audit did not include the two D08 passages subsequently found by actual candidate15 page reading (I15-prov-04 and I15-prov-12). Those findings reopened the bounded disposition and their exact fixes are among the 62 candidate16 edits. Candidate16 actual image reading and this expanded contextual pass found further announcements; D08 remains open until these approved proposals are applied and the settled PDF coverage is certified.',
 'mathematical_events_added':0,'full_page_reading_credit_added':0,'shared_files_modified':False,
 'D08_final_type_closed':False,
 'scope':'Every extracted context in the two finite scans was actually read. Full affected statements/proofs were additionally read for the 16 own added proposals, with exact before/proposed blocks. Mathematical operations, coordinate conventions, displayed inequalities and specific computational methods were retained with explicit row reasons. This is a bounded contextual audit, not a keyword-absence certificate or an additional full-page reading.'}
dest=OUT/'S6_SERIES_PUBLISH_I_candidate16_D08_expanded_dispositions.json'
dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
md=['# Candidate16: expanded D08 contextual dispositions','',f'Source `{SOURCE_SHA}`; PDF `{PDF_SHA}`.','',
    'All 164 contexts were actually read. Exact pending guards are linked; retained mathematical operations and conventions are explained row by row. D08 remains open pending application and final certified coverage. No mathematical event or full-page reading credit is added.','',
    '| Row | Page | Hit | Disposition and reason | Guards |','|---|---:|---|---|---|']
for r in rows:md.append('| '+r['row_id']+' | '+str(r['page'])+' | '+r['hit'].replace('|','\\|')+' | '+r['reason'].replace('|','\\|')+' | '+', '.join(r['guard_ids'])+' |')
dest.with_suffix('.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'receipt':str(dest.relative_to(ROOT)),'sha256':sha(dest),'contexts_actually_read':164,'disposition_counts':result['disposition_counts'],'D08_final_type_closed':False},indent=2))
