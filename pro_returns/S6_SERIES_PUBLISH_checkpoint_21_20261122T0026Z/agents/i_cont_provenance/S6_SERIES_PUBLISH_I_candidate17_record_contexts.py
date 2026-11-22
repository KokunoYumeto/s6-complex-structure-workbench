#!/usr/bin/env python3
"""Record manually read candidate17 context dispositions; no new check events."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,collections
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source_sha='5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
pdf_sha='3c9f15b28d768f305ab09dfb86ef98365aeb4659329b33e6faedb91864094ab0'
assert sha(ROOT/'S6_SERIES_PUBLISH_I.tex')==source_sha
p=ROOT/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_all_first_person_contexts.json'
allrows=json.loads(p.read_text())
reasons={
53:'Retain the explicit antiholomorphic target datum and all its parameter values; this sentence is the mathematical conclusion used in the next normalization.',
54:'Remove the standalone splitting announcement; the complete involution construction remains.',
55:'Retain the resulting antiholomorphic involution and its specified exponential action; these are mathematical conclusions of the square-zero calculation.',
56:'Retain the chosen upper-half-plane continuation and logarithm-cover convention; these fix the roots and the reflection lift.',
57:'Retain the real-part identities over t>1, which compute the squares of the involutions.',
58:'Remove the promise of equations; all exact branch maps, matrices and fixed-point equations remain.',
59:'Remove the standalone cusp computation announcement after full-proof review. The exact cusp normalization and all fixed-set calculations remain; this explicitly reopens the earlier bounded compute-scan retention.',
60:'Retain the derived genus and boundary count g_B=0, b_B=1 and the resulting three-sphere identification.',
61:'Remove the standalone check announcement; the torus transport and primitive meridian determinant remain.',
62:'Retain the exact modular lifts and their three-coordinate maps; these are mathematical choices in the domain description.',
63:'Retain the substitution c=-12v and cusp expansions; this performs the matrix calculation.',
64:'Retain the exact cusp coordinate eta=zeta+l_0 z_gamma and collar integer convention.',
65:'Retain the explicit translation sigma-o used to glue the finite and cusp fillings and the resulting local properness/flatness argument.',
66:'Retain the application of the cited analytic resolution theorem, including the unchanged nonsingular locus and proper modification.',
67:'Retain shrinking the parameter disc as the local mathematical operation under which the relative bundle calculation is made.',
68:'Retain the further cover, dominating-component resolution and marked-map graph construction.',
69:'Retain the concrete logarithmic datum, cover, rotations and descent values.',
70:'Retain removing the discrete analytic bad-value locus and the proof that the remaining curve stays connected.',
71:'Retain the holomorphic base restriction and preserved properness/flatness. Root separately owns the printed extraneous comma in the canonical-evaluation sentence.',
72:'Root owns the pure limiting-group announcement at page140; preserve the actual fixed-boundary formula and dual-lattice argument in the root guard.',
73:'Retain the fixed complex-linear coordinate convention and explicit period-matrix variables.',
74:'Remove the normalization announcement; retain the Jacobi product, exact mean computation and zero-mean conclusion.',
75:'Retain the projective-bundle lines convention, finite coordinate, zero/infinity sections and their normal bundles.',
76:'Retain R as the named projective bundle; it is an actual definition.',
77:'Retain the exact fibre-product ring used to define the gluing; this is the construction of the local complex space.',
78:'Retain the chosen section and its divisor, with its exact source locator and bundle-map interpretation.',
79:'Retain subtraction of bx in the b>=0 monoid computation.',
80:'Retain subtraction of (-b)y in the b<0 monoid computation.',
81:'Retain the uniform metric inequality over all points of the compact surface and all small parameters.',
82:'Remove the normalization-calculation announcement; the singular-centre charts and all normalization maps remain.',
83:'Remove the filling roadmap after zero winding; the untwisted hypothesis and entire construction remain.',
84:'Remove the generic-fibre announcement; all marked cusp and coordinate comparisons remain.',
85:'Remove the geometric-description announcement; the explicit algorithmic blow-up chart and all inputs remain.',
86:'Retain the concrete comparison of fundamental cycles on a smooth proper modification, which satisfies the stated ambient-manifold hypothesis for triangulation.',
87:'Retain the cited compatible triangulation operation and its specified endpoint fibres and singular strata.',
88:'Retain e(R)=2e(S)=24 and the ensuing Chern-number calculation.',
89:'Retain the indefinite iteration of the exhibited point modification; it asserts the mathematical infinite family and explains its distinct component counts.',
90:'Retain the exact lattice, fibre and section-difference conventions inherited from Proposition21.11.',
91:'Retain the choice of the semistable model and removal of conductor tubular neighbourhoods that defines the decomposition.',
92:'Remove the rank/saturation announcement; all explicit restriction maps and primitive images remain.',
93:'Retain the concrete computation of monodromy from the preceding boundary decomposition, whose neck and tube map immediately follow. Two separate D02 tails in this complete proof are removed by guards17/18.',
94:'Retain the concrete normalization mapping-cylinder method for the reference centre; its integral sequence and elimination maps immediately follow.',
95:'Remove the classification announcement; the complete centre classification and cohomology consequences remain.',
96:'Replace the verification/use recap with the positive quotient-identification comparison, retaining the exact numbered reference.',
97:'Retain the reduction to the standard reduced twelve-cycle after the explicit alternative-fan exclusion.',
98:'Retain the deck-identification convention for peripheral permutations and the corresponding inverse-path holonomy convention.',
99:'Remove the intersection-computation roadmap; every intersection, component index and height argument remains.',
100:'Retain the consequence of the index bound giving the exact half/quarter section expression.',
101:'Retain continuous-cochain Galois cohomology as the concrete method for the displayed transgression sequence.',
102:'Remove the local-ramification roadmap; the explicit norm construction, localization and unchanged transgression conclusion remain.',
103:'Retain the multidegree-zero choice in the gluing of the Poincare lines; it is a mathematical normal-line convention.',
104:'Retain the explicit neighbourhood-retraction method and both application references. Remove only the separate For completeness qualifier before the actual monomial estimate.',
}
guardnums={54:[3],58:[4],59:[5],61:[6],74:[7],82:[8],83:[9],84:[10],85:[11],92:[12],93:[17,18],95:[13],96:[14],99:[15],102:[16],104:[19]}
assert set(reasons)==set(range(53,105))
rows=[]
for r in allrows:
 if 53<=r['id']<=104:
  rr=dict(r); rr['context_sha256']=hashlib.sha256(r['context'].encode()).hexdigest()
  rr['actual_context_read']=True;rr['disposition']=reasons[r['id']]
  rr['linked_guard_ids']=[f'I17-prov-{n:02d}' for n in guardnums.get(r['id'],[])]
  rr['status']='root-owned pending guard' if r['id']==72 else ('retained mathematical content with separate root D23 guard' if r['id']==71 else ('guard proposed; exact retained content described' if rr['linked_guard_ids'] else 'retained ordinary mathematical operation, conclusion or convention'))
  rows.append(rr)
hp=ROOT/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_here_contexts.json'
hereall=json.loads(hp.read_text());hguards={4:20,6:19,9:21,11:22,12:23,19:2}
hrows=[]
for r in hereall:
 if r['id'] in hguards:
  rr=dict(r);rr['actual_context_read']=True;rr['linked_guard_ids']=[f"I17-prov-{hguards[r['id']]:02d}"]
  rr['disposition']='Pure announcement or completeness qualifier; full owning statement/proof read. Preserve all mathematical inputs and exact maps in the linked guard.'
  hrows.append(rr)
gf=OUT/'S6_SERIES_PUBLISH_I_candidate17_provenance_guards.json'
gr=OUT/'S6_SERIES_PUBLISH_I_candidate17_provenance_guard_receipt.json'
result={'paper':'I','candidate':17,'recorded_utc':datetime.now(timezone.utc).isoformat(),
 'source_sha256':source_sha,'pdf_sha256':pdf_sha,
 'first_person_input':str(p.relative_to(ROOT)),'first_person_input_sha256':sha(p),
 'first_person_rows':rows,'first_person_contexts_actually_read':52,
 'here_input':str(hp.relative_to(ROOT)),'here_input_sha256':sha(hp),'here_rows':hrows,
 'here_contexts_actually_read':6,'guard_file':str(gf.relative_to(ROOT)),'guard_sha256':sha(gf),
 'guard_receipt':str(gr.relative_to(ROOT)),'guard_receipt_sha256':sha(gr),
 'reading_record':'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_final_candidate17_reading_provenance.json',
 'reading_record_sha256':'65e544a998acb4810742e3b0c9d4a706d3c76f1166a06069bb33986ba3e4450e',
 'historical_reopening':'The earlier bounded compute-scan retention of the cusp-fixed-set announcement is reopened by I17-prov-05. Root separately reopens the translation-group announcement retained in the immutable candidate17 page326 observation. No historic reading or audit receipt is rewritten.',
 'D08_final_type_closed':False,'pending':'Exact proposals await root review and source application; final source/PDF/coverage rebinding remains required.',
 'mathematical_events_added':0,'full_page_reading_credit_added':0,'source_changes_applied':False}
dest=OUT/'S6_SERIES_PUBLISH_I_candidate17_first_person_here_dispositions.json'
assert not dest.exists()
dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
md=['# Candidate17: assigned first-person and qualifier dispositions','',
 'All 52 first-person contexts (53--104) and six assigned qualifier contexts were read. Complete owning statements/proofs were read for each proposed edit. These contextual readings add no mathematical event or page-image credit. D08 remains open pending application and final binding.','',
 '| Input row | Page | Disposition | Guards |','|---|---:|---|---|']
for prefix,rs in [('we',rows),('here',hrows)]:
 for r in rs:md.append(f"| {prefix} {r['id']} | {r['page']} | {r['disposition']} | {', '.join(r['linked_guard_ids'])} |")
dest.with_suffix('.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'path':str(dest.relative_to(ROOT)),'sha256':sha(dest),'first_person_rows':52,'here_rows':6,'mathematical_events_added':0},indent=2))

