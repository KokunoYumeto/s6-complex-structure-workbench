from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy
P=Path("agents/ii_checks_provenance/recovery_20261121T2000Z")
O=P/"clean_group09"
def bind(p):
    p=Path(p)
    return {"path":str(p),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
def save(p,o):
    p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+"\n")
    return bind(p)
now=datetime.now(timezone.utc).isoformat()
image_dir=P/"primary_inputs/analytic_batch_images"
image_specs=[
 ("CDP98_p078.png",78,"CDP98 Proposition1.1 and its complete proof"),
 ("CDP98_p079.png",79,"CDP98 Corollaries1.2 and1.3; only the precise smooth receiving scopes are used"),
 ("CDP2020_p680.png",681,"This old filename was inaccurate: the actual rendered printed page is681, not680"),
 ("CDP2020_printed680.png",680,"Correct printed page containing Proposition2.4"),
 ("AC2026_printed088.png",88,"Section10.3 and Theorem10.5, first page"),
 ("AC2026_printed089.png",89,"Theorem10.5 proof continuation and Corollary10.6 with proof"),
 ("SerreGAGA_printed019.png",19,"Comparison morphism and section12 Theorem1, with q>=0")]
images=[{"file":bind(image_dir/n),"printed_page":p,"actual_whole_image_viewed":True,"scope":s} for n,p,s in image_specs]
primary={
 "schema_version":1,"paper":"II","checker":"i_provenance_recovery","created_utc":now,
 "download_receipt":bind(P/"primary_inputs/S6_SERIES_PUBLISH_II_analytic_batch_primary_download_receipt.json"),
 "sources":[
 {"key":"AC2026","file":bind(P/"primary_inputs/AC2026_current_primary.pdf"),
  "primary_url":"https://alpo.ge/s6.pdf","edition":"The exact108-page author PDF bound by SHA256; fresh download matches the earlier saved primary file.",
  "read_scope":"Complete Theorem10.5 and its five-step proof, and Corollary10.6 with proof, printedpp.88–89, were read in text and full page images. The actual section is10.3. Theorem10.5(a) gives all-twist fibre/relative nonvanishing; part(c) gives generic global nonvanishing. IV's all-twist global conclusion is separately derived by its Euler/J0 argument.",
  "web_refs":["turn852782535view1","turn955390328view2"],
  "correction":"Section10.2 -> Section10.3; add Corollary10.6 and printedpp.88–89 for the credited CDP counterexample."},
 {"key":"Serre1956GAGA","file":bind(P/"primary_inputs/Serre1956GAGA_primary.pdf"),
  "primary_url":"https://www.numdam.org/article/AIF_1956__6__1_0.pdf",
  "read_scope":"Section11's comparison map and section12 Theorem1, printedp.19, were actually viewed; the complete section13 proof, pp.20–22, was read as primary text, not claimed as whole-page image reading. Projectivity and coherence apply to dP6 and its structure sheaf; the natural comparison map identifies its algebraic and analytic H1.",
  "web_refs":["turn955390328view1","turn487086311view1"]},
 {"key":"CoxLittleSchenck2011","primary_author_url":"https://dacox.people.amherst.edu/toric.html",
  "original_text_retrieval_url":"https://pi.math.cornell.edu/~tsh/cornell-only/cox-little-schenck-toric.pdf",
  "edition_evidence":"Original text title page names David Cox, John Little, Hal Schenck and copyright2010; preface dated September2010. Author page identifies the AMS Graduate Studies in Mathematics124 publication.",
  "read_scope":"The complete Theorem9.2.3 statement and proof on originalp.410 were read in indexed original-book text. Its convex fan support and zero nef divisor hypotheses apply to the complete dP6 fan. The proof uses convexity and reduced cohomology of the specified support sets.",
  "web_refs":["turn889096218view1","turn889096218view2","turn525378517view0","turn525378517view1"],
  "local_pdf_or_rendered_page_reading_claimed":False,
  "failed_endpoint":"https://dacox.people.amherst.edu/toric/toric.pdf returned404; no local PDF hash is invented.",
  "bibliography_scope":"The bibliography retains the publisher DOI and author homepage; no mirror URL is proposed there."},
 {"key":"CDP98","file":bind(P/"primary_inputs/CDP98_journal.pdf"),
  "primary_url":"https://doi.org/10.1023/A:1000313214795",
  "read_scope":"Proposition1.1 and complete proof onp.78, with corollaries onp.79, were read in text and images. Only the connected smooth manifold, nonzero effective Cartier divisor and locally free sheaf instance is used. Corollary1.3 is narrower (threefold and b2=0) and does not replace the general I7 input. No broader nonreduced validity or blanket Lemma1.5 local-freeness claim is inferred."},
 {"key":"CDP20","file":bind(P/"group03/primary/CDP2020_journal.pdf"),
  "primary_url":"https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CDF2D04CFB35CEE105E10B188D97D68A/S0010437X19007802a.pdf/the-algebraic-dimension-of-compact-complex-threefolds-with-vanishing-second-betti-number.pdf",
  "read_scope":"The exact Proposition2.4 statement on printedp.680 was read. DT supplies the complete independent projection-formula, Serre-vanishing and Leray argument. A mistaken initial render displayedp.681; that filename/page distinction is explicitly recorded."},
 {"key":"BS76push","page":bind(P/"primary_inputs/BS76_p124.webp"),
  "read_scope":"The full Theorem4.1 statement on printedp.124 was actually viewed again. A proper map and coherent sheaf have a locally finite-rank free complex; for a relatively flat sheaf it is bounded. The Poincare/vector-bundle families are relatively flat, so rank conditions yield the local analytic jump loci. No full pp.124–130 proof reading is claimed.",
  "earlier_bound_receipt":bind(P/"clean_group05/S6_SERIES_PUBLISH_II_clean_group05_final_proposals.json")}
 ],
 "primary_images":images,"paper_II_manuscript_page_credit":0,
 "events_added":0,"scope":"Actual primary reading and exact edition/locator transport only; no source-opening event is automatically added."}
primary_binding=save(O/"S6_SERIES_PUBLISH_II_clean_group09_primary_receipt.json",primary)
ownership={
 "created_utc":now,"source_at_review":bind("S6_SERIES_PUBLISH_II.tex"),
 "incoming_uses":bind(P/"S6_SERIES_PUBLISH_II_J0_current_incoming_uses.json"),
 "J0_smooth_scope":{"reason":"The target uses T_X as a rank-three bundle, oriented six-manifold Poincare duality, and smooth compact HRR. The frozen derivation explicitly establishes the smooth scope.",
   "receivers":[
    {"owner":"wbII:cor:corrected-cdp-relative","tag":"03DT","transport":"Its first hypothesis invokes the setting of J0, so the same X and f inherit smoothness."},
    {"owner":"wbII:thm:corrected-cdp-fibrewise","tag":"03IZ","transport":"Its first hypothesis invokes the setting of J0; its proof explicitly uses the regular local rings of X."},
    {"owner":"wbII:test:cdp-comparison","tag":"03IV","transport":"The constructed standard threefold is smooth; the proposed first proof sentence makes that input explicit."}],
   "other_coded_uses":"A hidden reference macro, the further-results index, and unowned explanation/citation lists introduce no additional space. The unowned global/relative comparison inherits the named settings; the standard-family application has the constructed smooth X. This is only the coded-reference scope, not a claim about all uncited prose."},
 "IA_I7_exact_ownership":{
   "IA":"Its parameter space P is an explicitly given irreducible reduced analytic subspace of Pic0 with a Poincare bundle and two specified zero points. The proof uses these actual hypotheses. Removing its unused stabilization paragraph changes none of them.",
   "I7":"Its parameter space is the whole connected Pic0 group. CDP98 Proposition1.1 yields negative-divisor twists with vanishing sections for B and B-dual tensor omega. Local universal families and inversion give the dense-open conclusions.",
   "maps":"The inclusion P -> Pic0 pulls a universal family back where defined; dualization restricts by the stated stability hypothesis. The two assumed zero points in IA remain indispensable to its stated proof. No claim is made that an arbitrary subspace P meets I7's dense open set.",
   "consolidation":"The duplicate stabilization proof is removed from IA; I7 cites the exact classical result and states the section-space inclusion. Both owning statements and proofs remain, with separate exact scopes."},
 "events_added":0}
scope_binding=save(O/"S6_SERIES_PUBLISH_II_clean_group09_scope_and_ownership.json",ownership)
comparison={
 "03DS":"The frozen derivation pulls A_L to the trivial bundle on dP6 through Pic0, applies the exact conductor section, absolute Cartier duality and the top-degree base-change map. All three nonvanishings and the complete original/proposed proof agree. Its historical Compendium I cusp locator is retained as the supplied cited input; no nonexistent current owning label is substituted.",
 "03IX":"The frozen derivation kills c1 of the dual-canonical twist by H2(X,Z)=0, pulls it to dP6, uses H1(O)=0 and the exponential kernel to trivialize it, and applies conductor descent, Cartier duality and top-degree base change. The complete proposed proof preserves all four hypotheses and every displayed map. Exact CLS and GAGA inputs were independently opened and matched.",
 "03IA":"The frozen derivation constructs the two proper analytic jump loci in the actual Poincare family, uses the two assumed zero points, inversion and Serre duality, and intersects their dense-open complements. The complete pair was read. The redundant stabilization paragraph is deleted without weakening either zero-point hypothesis; the rank maps in a finite free complex now identify the analytic loci precisely.",
 "03I7":"The frozen derivation proves the negative-divisor stabilization with the regular local intersection argument, constructs Pic0 as the exponential quotient with discrete integer image, and uses local holomorphic families, inversion and Serre duality. The complete revised proof cites the exact primary stabilization input, with its smooth connected hypothesis map, and retains the local-family endpoint argument. No global Poincare bundle is asserted.",
 "03J0":"The frozen derivation explicitly assumes smooth X, uses the exponential-cocycle family, three proper analytic jump loci and the dense-open intersection. Oriented Poincare duality kills rational H4; the degree-six HRR scalar is c3/2. The original proof requires precisely this smooth scope, so its statement is clarified and all receiving coded uses are mapped. No singular-total-space assertion is certified. The entire revised proof was read after the two grammatical/punctuation corrections.",
 "03DT":"The frozen derivation takes E=T_X tensor L, twists by f* A^m, uses projection formula, Serre vanishing of H1(C,R1f*E tensor A^m), and the two Leray columns to obtain L0=L tensor f* A^m with H2=0. The complete original/proposed proofs agree, including the inherited smooth X scope. CDP20 Proposition2.4 is precisely located onp.680.",
 "03IZ":"The frozen derivation applies the section-kernel isomorphism to each full reduced Cartier fibre, gives H0(V)=ker(delta)=0, uses its one-dimensional normal factor and Cartier duality, then top-degree base change and Nakayama at every stalk. The complete pair preserves all hypotheses and quantifiers; the filtration is now named by its exact current reference.",
 "03IV":"The frozen derivation verifies the standard smooth X has H1=H2=0, c3=2 and holomorphic algebraic reduction, then applies the global and relative criteria by contradiction for every line bundle. The conductor route is an additional independent implication from its cited statement. The AC attribution is retained at its actual section10.3, Theorem10.5 and Corollary10.6 onpp.88–89. All-twist global nonvanishing follows from this Euler argument, not from misreading AC10.5(c)'s generic statement.",
 "03IP":"The frozen derivation writes both module maps and proves their kernels exactly by convergent-power-series divisibility; it computes generic rank2 and origin generator number3, and identifies the full multiple-fibre torsion R/(s^(m-1)) ds. The fresh prerelease program computes graded coefficient-matrix ranks by Fraction elimination and multiplication cokernels; finite checks corroborate the separate all-degree/all-m proof. The full proposed proof retains every map and image; its first sentence correctly differentiates the two crossing equations named by its reference."}
prep=O/"S6_SERIES_PUBLISH_II_clean_group09_preparation.json"
r=json.loads(prep.read_text())
r["preparation"]=bind(prep)
r["primary_receipt"]=primary_binding
r["scope_and_ownership"]=scope_binding
r["completed_utc"]=now
r["source_at_final_review"]=bind("S6_SERIES_PUBLISH_II.tex")
r["status"]="Nine frozen derivations, complete original/proposed proof readings and exact guards complete; awaiting root integration."
r["prior_program_scope"]="All31 exact historical/current owner associations were read after freeze/release, including separately rereading the initially truncated middle rows. They identify no target-specific computational program for these nine owners. This is limited to those records. The reused HRR identity is already bound to the fresh different-method C1.1 program; the whole old D_exact_checks.py remains unopened."
r["computation_evidence"]=[
 {"tag":"03IP","code":bind(P/"clean_derivations/S6_SERIES_PUBLISH_II_03IP_preproof_module_maps.py"),
  "output":bind(P/"clean_derivations/S6_SERIES_PUBLISH_II_03IP_preproof_module_maps.output.json"),
  "timing":"Written, executed and output read before the03IP freeze and target-proof release.",
  "method":"Exact rational elimination of homogeneous coefficient maps, degrees0–7, plus truncated multiplication cokernels for m2–9. The complete analytic divisibility proof establishes all degrees and every m.",
  "method_comparison":"The printed proof and the three inspected prior03IP records use analytic UFD syzygy divisibility and a generic-rank/minimal-generator argument. The new matrix-rank/cokernel algorithm is different finite corroboration. No unidentified historical program is claimed compared."},
 {"tag":"03J0","earlier_method_receipt":bind("agents/ii_checks_provenance/group01/v2_addendum/S6_SERIES_PUBLISH_II_B_group01_scope_methods_addendum.json"),
  "code":bind("agents/ii_checks_provenance/computations/S6_SERIES_PUBLISH_II_01BN_new_HRR.py"),
  "output":bind("agents/ii_checks_provenance/computations/S6_SERIES_PUBLISH_II_01BN_new_HRR.output.json"),
  "transport":"Use Y=X and the same tangent bundle with L=M. H1(X,Z)=H2(X,Z)=0 gives b1=b2=0, so the previously checked smooth C1.1 scope applies. The fresh sparse Fraction convolution yields c3/2; the old identified routine used SymPy expansion in u. This is reuse of that actual new computation, not another event."}]
r["prospective_counts"]={"targeted proof check":9,"used and rechecked in this run":9}
prior="Related Paper I construction and previously checked Paper II inputs had already been read; these are disclosed input exposure. Each of the nine own target proofs and old owner outcomes remained closed until its derivation froze at21:37:31. The entire original and proposed named proofs were then actually read. No ancillary proof or new derivation is inferred from software comparisons."
for t in r["targets"]:
 t["comparison"]=comparison[t["tag"]]
 t["actual_complete_proposed_proof_read"]=True
 t["full_pair_review_completed_utc"]=now
 t["actual_rereading_scope"]="Complete named statement and its entire attached proof, before and after all listed exact guards."
 t["prior_exposure"]=prior
 t["proposed_event_counts"]={"targeted proof check":1,"used and rechecked in this run":1}
fb=save(O/"S6_SERIES_PUBLISH_II_clean_group09_final_proposals.json",r)
events=[]
fields=["tag","statement_owner","checker","freeze_receipt","frozen_derivation","release_receipt","release_envelope","named_statement_scope","original_full_block","proposed_full_block","prior_exposure"]
for t in r["targets"]:
 for typ in ["targeted proof check","used and rechecked in this run"]:
  e={k:copy.deepcopy(t[k]) for k in fields}
  e.update(paper="II",event_type=typ,event_count=1,proposal_only=True,proposal_bundle=fb,
    scope=t["comparison"] if typ=="targeted proof check" else t["actual_rereading_scope"],
    source_application_pending=True,no_extra_computation_event=True)
  events.append(e)
eb=save(O/"S6_SERIES_PUBLISH_II_clean_group09_event_proposals.json",
 {"schema_version":1,"paper":"II","created_utc":now,"proposal_only":True,"events":events,
  "prospective_counts":r["prospective_counts"],"canonical_mutations":0,"events_added":0})
print(json.dumps({"final":fb,"events":eb,"primary":primary_binding,"scope":scope_binding,"guards":sum(len(t["guards"]) for t in r["targets"]),"bibliography_guards":len(r["bibliography_guards"])},indent=2))
