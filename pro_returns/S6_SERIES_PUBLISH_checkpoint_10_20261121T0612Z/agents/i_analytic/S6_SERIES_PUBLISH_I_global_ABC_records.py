"""Write scoped exposed-comparison events and primary/status receipts.

No publication source or global metadata is written.
"""
from pathlib import Path
import csv, datetime, hashlib, json

ROOT=Path('/workspace/scratch/653608133b22')
OUT=Path(__file__).parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
record=OUT/'S6_SERIES_PUBLISH_I_global_ABC_comparison.md'
digest=sha(record)
group='eg:publish-ianalytic-globalABC-'+digest[:16]
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, S6_SERIES_PUBLISH/v_analytic_check'
scopes=[
 ('series:I:A','PASS: EXPOSED FINAL GLOBAL COMPARISON. Statement-directed record frozen before current outlines/table; all six outline steps compared with the current body. Checked exact pointed maps/differential and discriminant scales, cusp branch, determinant sign and radii216/46656, division/torsion hypotheses, local/global maximum coverage, critical/level scope and eleven height factors. Uses existing scoped arithmetic calculations without rerun or new computation credit. Guards repeat inherited m>=2 and clarify two phrases; no theorem value changed.'),
 ('series:I:B','PASS: EXPOSED FINAL GLOBAL COMPARISON. All six outline steps and full current discrete/collar and real-form proofs read. Checked base recovery, exact norm/cusp sufficiency, p/parity invariants, higher2kl congruences and Viaclovsky map, positive-u loop c->c-1, Albanese nomes, reflected affine normalization, both real classes and cap-meridian scope. DGKXv1 known2Z theorem credited with existing exact particular-solution translation. No fresh Hermite/Smith execution or independent real-locus credit; historical computation scope disclosed.'),
 ('series:I:C','PASS: EXPOSED FINAL GLOBAL COMPARISON. All five outline steps read against actual group-kernel, fundamental-set, proper-action, period-embedding and NS/quotient proofs. Checked vector/line index12/24 scopes, d/body-e/vertical-Pi(d) dictionary, q_d=-6/D sign, dense null stabilizers, j left inverse/properness and orientation/Pfaffian tests. Guards name Gamma\\P_d(R) and give the existing saturated-null-lattice connected quotient morphisms. No new independent or computational credit; no mathematical counterexample found.'),
 ('fam:src:B.1.1','PASS: EXPOSED SOURCE/APPLICATION REWRITE COMPARISON. Full attached and current proof read. Merged with B1.3 while preserving quotient/divisor-section map, f_sc equations/cusp branch and differential scale, explicit source cubic map, nodal U map/inverse and all labels/tags. Known MW generator/Abel-Jacobi -mu from personally viewed AC Remark3.12 p19; exact xi->-xi and cubic maps transport zero/generator assertions. Full removed logarithm reproof archived. No targeted/independent credit.'),
 ('fam:src:B.1.3','PASS: EXPOSED SOURCE/APPLICATION REWRITE COMPARISON. Full original blow-up, E6 inverse-intersection matrix and height-projection proof read against the merged receiving proof. AC source x0(P0)=0 with Abel-Jacobi -mu gives wp(mu)=0 by explicit scale and evenness; the pointed map carries source generators to the two visible sections. Engel Lemma2.1 proof pp3-4, actually viewed, supplies Shioda self-pairing1/6. B1.4 retains actual cusp sign; all old proof content and locators archived. No new independent or computation credit.')]
rows=[]
for st,outcome in scopes:
    eid=hashlib.sha256((group+'\n'+st+'\n'+outcome).encode()).hexdigest()[:16]
    rows.append({'statement_id':st,'date':'2026-11-21','who':who,
      'type':'used and rechecked in this run','outcome':outcome,
      'event_id':'ce:publish-ianalytic-'+eid,'phase':'S6_SERIES_PUBLISH',
      'source_file':str(record),'source_row':'',
      'source_event_type':'used and rechecked in this run','evidence_group':group})
tsv=OUT/'S6_SERIES_PUBLISH_I_global_ABC_CHECK_EVENTS.tsv'
with tsv.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
meta={'created_utc':now,'comparison':str(record),'comparison_sha256':digest,
      'evidence_group':group,'events':rows,'events_sha256':sha(tsv),
      'guards_sha256':sha(OUT/'S6_SERIES_PUBLISH_I_global_ABC_guards.json'),
      'pending_applied_source_binding':True,
      'no_events_for_primary_locator_or_search':True,
      'main_source_written':False}
(OUT/'S6_SERIES_PUBLISH_I_global_ABC_comparison.json').write_text(json.dumps(meta,indent=2)+'\n')

srcs=[
 ('AC2026 primary 108-page edition','https://alpo.ge/s6.pdf',
  ROOT/'work/agents/i_provenance/literature/S6_SERIES_PUBLISH_I_AC26_primary.pdf',
  ROOT/'work/agents/i_provenance/literature/S6_SERIES_PUBLISH_I_AC26_p019.png',19,
  'Personally viewed/read full printed p19. Remark3.12 gives source cubic, MW generator P0=(0,i t^2(t-1)), and Abel-Jacobi coordinate -mu. No height1/6 on this page.'),
 ('Engel arXiv2609.38442v1','https://arxiv.org/abs/2609.38442v1',
  ROOT/'work/agents/provenance/literature/S6_SERIES_PUBLISH_Engel.pdf',
  OUT/'literature/S6_SERIES_PUBLISH_I_Engel_v1_p003.png',3,
  'Personally viewed/read full printed p3. Initial construction specifies exact geometric cubic, cyclic MW and nonidentity components; Lemma2.1 statement/proof begins.'),
 ('Engel arXiv2609.38442v1','https://arxiv.org/abs/2609.38442v1',
  ROOT/'work/agents/provenance/literature/S6_SERIES_PUBLISH_Engel.pdf',
  ROOT/'work/agents/i_provenance/literature/S6_SERIES_PUBLISH_I_Engel_p004.png',4,
  'Personally viewed/read full printed p4. Lemma2.1 proof gives self-pairing2-4/3-1/2=1/6, multiples/intersections and line degree1. Corollary2.2 states the reference linearization.'),
 ('Engel arXiv2609.38442v1','https://arxiv.org/abs/2609.38442v1',
  ROOT/'work/agents/provenance/literature/S6_SERIES_PUBLISH_Engel.pdf',
  ROOT/'work/agents/i_provenance/literature/S6_SERIES_PUBLISH_I_Engel_p006.png',6,
  'Personally viewed/read full printed p6. Proposition2.7 is the holomorphic-unit cusp quotient; it is not the height supplier. Proposition2.8 begins below.')]
receipt={'created_utc':now,'purpose':'Source/application split of fam:B1.1/B1.3; locator-only source reading has no mathematical event of its own.',
 'coordination_corrections':'Earlier messages merged AC MW scope with Engel height and misidentified Engel2.7. Both corrected before guards; exact scopes below.',
 'no_whole_paper_read_claim':True,'pages':[]}
for name,url,pdf,img,page,scope in srcs:
    receipt['pages'].append({'source':name,'primary_url':url,'pdf':str(pdf),
      'pdf_sha256':sha(pdf),'printed_page':page,'pdf_page':page,
      'image':str(img),'image_sha256':sha(img),'actual_image_read':True,'scope':scope})
(OUT/'literature/S6_SERIES_PUBLISH_I_elliptic_source_split_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')

queries=[
 {'engine':'system1','queries':['"complex six-spheres" theta period maximum','"complex six-spheres" real structures classification','"six-spheres" monodromy "proper" domain'],'domains':['arxiv.org'],'recency':365,'result':'No results.'},
 {'engine':'system2','queries':['complex six sphere Engel holomorphic families period theta maximum','complex six sphere Du Guo Kusakabe Xie moduli real structures','symplectic monodromy parabolic U(1,1) proper discontinuity elliptic surfaces'],'result':'Known DGKX/Engel records, author repository/series and secondary hits; only primary source records used for claims.'},
 {'engine':'system2','queries':['"six-spheres" "216"','"six-spheres" "real structures"','"six-spheres" "monodromy group"','"theta" "Weierstrass" "zeros" "maximum"'],'open':['https://arxiv.org/abs/2610.00250v1','https://arxiv.org/abs/2609.38442v1'],'result':'No separate matching primary theorem found in returned search hits. Official Engelv1 record opened; DGKXv1 open returned DisabledError.'},
 {'engine':'system1','queries':['"2610.00250" "v1" "period"','"six-spheres" "Klingler" monodromy','"Weierstrass" "theta norm" maximum'],'result':'Mirrors and own-series pages; no new primary result relied on. FLINT primary documentation is general theta/wp identities, not the exact norm-maximum theorem.'}]
search={'created_utc':now,'main_theorems':['series:I:A','series:I:B','series:I:C'],
 'raw_output':str(OUT/'literature/S6_SERIES_PUBLISH_I_global_ABC_status_search_raw.json'),
 'raw_output_sha256':sha(OUT/'literature/S6_SERIES_PUBLISH_I_global_ABC_status_search_raw.json'),
 'queries':queries,
 'primary_records_used':['https://arxiv.org/abs/2609.38442v1','https://alpo.ge/s6.pdf','Previously authenticated primary DGKXv1 PDF/metadata receipt in i_provenance'],
 'secondary_hits_used_as_math_evidence':False,
 'outcome':'Bounded current search found the known source family/classification and self-series claims, but no additional primary result changing the displayed A-C source/application split. This is not an exhaustive novelty or priority conclusion.',
 'counts_credit':'No mathematical check events for searches or locator retrieval.',
 'source_relationships':{
  'A':'Known elliptic surface/marked generator: AC Remark3.12 p19. Known self-pairing/linearization input: Engel Lemma2.1 pp3-4. Exact normalized period, maximum/domain and displayed arithmetic/critical application proved in current body.',
  'B':'Known standard2Z classification: DGKXv1 Theorem1.4 p3, with recorded additive particular-solution translation. Current body provides the displayed all-data/higher and real-form comparison maps.',
  'C':'Known integral (1,1) wedge equation: AC Lemma9.2 p65. Proper-action question: Engel Remark8.4 pp23-24. Current body computes exact integral kernel/maximal domain and applies saturated null-lattice/definiteness tests.'}}
(OUT/'literature/S6_SERIES_PUBLISH_I_global_ABC_status_search_scope.json').write_text(json.dumps(search,indent=2)+'\n')
print(json.dumps({'rows':len(rows),'ledger_sha256':sha(tsv),'evidence_group':group,
 'comparison_sha256':digest,'main_source_written':False},indent=2))
