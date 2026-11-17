#!/usr/bin/env python3
"""Build the bounded, source-specific 30-row WORKING_CDP credit overlay.

This does not mutate the master inventory, manuscript, or original sources.
Searches and receiving proof readings are separate evidence classes.
"""
from pathlib import Path
import csv
import hashlib
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
D = ROOT / 'deliverables'
OUT = D / 'work/cdp_audit/II_working_credit'
READER = {'model': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode)', 'effort': 'Pro',
          'date': '2026-11-17 UTC', 'agent': '/root/cdp_audit'}

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def dump(p, value):
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

inventory = list(csv.DictReader((D / 'S6_09_PAPERS_inventory.csv').open()))
fields = list(inventory[0])
assert len(fields) == 17
selected = [r for r in inventory if r['source_run'] == 'WORKING_CDP' and r['paper'] == 'II']
assert len(selected) == 30
mapping = {r['source_id']: r for r in json.loads((D / 'work/cdp_audit/working_supplement_mapping.json').read_text())['rows'] if r['source_run'] == 'WORKING_CDP'}
proofs = {r['source_id']: r for r in json.loads((D / 'work/cdp_audit/working_edition_inventory.json').read_text()) if r['source_run'] == 'WORKING_CDP'}
searches = json.loads((OUT / 'searches_150.json').read_text())
search_by = {(r['source_id'], r['corpus']): r for r in searches['records']}

# Exact source scopes opened in the current attribution pass. Earlier complete
# receiving-proof checks remain separate and are incorporated without upgrading
# their historical scope.
contexts = {
 'AC26': {
  'path': 'sources/external/root/AC26_pdf_text.txt',
  'ranges': [[5430,5618],[5615,5713],[5840,5875],[5970,6048],[4150,4252]],
  'locators': ['Setup10.1 and conormal sequence (10.1), p.86',
   'Lemma10.2 and normalization-conductor square (10.2), p.87',
   'Lemma10.3 and full proof, pp.87–88',
   'Theorem10.5(a), proof Steps1–3, equation(10.5), pp.88–89',
   'Corollary10.6, p.89; §10.4, pp.89–90',
   'Proposition10.8 normalization argument, p.93',
   '§10.6, pp.94–95, generic endpoint argument and its limitation',
   'Lemma9.4, pp.66–67, integral invariant Hodge form of type(1,6)'],
  'scope': 'Controlling original PDF text actually reopened; original pp.84–95 were also visually opened in the earlier canonical credit audit. These are exact indicated contexts, not a claim that all 150-query hits were read.'},
 'E26': {
  'path': 'sources/papers/arXiv_2609.38442_Engel_src/S6.tex',
  'ranges': [[1275,1330],[1665,1740]],
  'locators': ['§6, The integral homology: invariant-form and open-invariants lemmas, source lines1275–1330',
   'Concluding comparison and invariant-form remark, source lines1665–1740'],
  'scope': 'Actual displayed primitive invariant form and rank-one invariant lattice read, together with the comparison explicitly crediting AC26 §9.1. No full conductor or arbitrary-line-bundle boundary theorem identified in these contexts.'},
 'DGKX_v1': {
  'path': 'sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex',
  'ranges': [[220,325],[3350,3405],[3765,3810],[9050,9149]],
  'locators': ['Introduction: Oka/family setting, lines220–325',
   'Local C* times C Picard calculation, lines3350–3405',
   'Deleted-lines pullback argument, lines3765–3810',
   'Analytic Grauert and analytic relative-duality lemmas and complete proofs, lines9050–9149'],
  'scope': 'The relative-duality lemma assumes proper flat relative dimension2, Gorenstein fibres, a smooth DM base, p_*O=O and local freeness of the relevant direct images. The Grauert lemma assumes constant fibre dimensions. Those related classical inputs are not equated with the broader absolute Cartier duality or the top-degree jumping case.'},
 'DGKX_v2': {
  'path': 'sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex',
  'ranges': [[230,330]],
  'locators': ['Introduction and construction scope, source lines230–330'],
  'scope': 'Version2 searched independently. The introduction and relevant geometry context were read; a Version1 analytic-duality lemma is not silently attributed to Version2.'},
 'CDP98': {
  'path': 'sources/papers/arXiv_math_9607215_CDP98_src/main.tex',
  'ranges': [[210,315]],
  'locators': ['Proposition1.1 and proof; Corollaries1.2–1.3 and their proofs; beginning of Lemma1.5'],
  'scope': 'The descending finite-dimensional section-space proof, generic endpoint argument, and exact b2=0 threefold hypothesis read. The receiving arbitrary-dimensional O(D) in Pic0 formulation is the same Proposition1.1 proof plus Serre duality. The false full local-freeness conclusion of Lemma1.5 is not endorsed.'},
 'CDP2020': {
  'path': 'reference_downloads/cdp_audit/CDP2020_layout.txt',
  'ranges': [[80,155]],
  'locators': ['Published Proposition2.4, p.680, and surrounding proof discussion, pp.680–681'],
  'scope': 'The intact conditional R2 f_*(TX tensor L)=0 criterion is explicitly stated in the original; receiving stronger topology assumptions imply its stated b2=0 hypotheses.'},
 'RR70': {
  'path': 'reference_downloads/cdp_audit/RamisRuget1970.txt',
  'ranges': [[250,435]],
  'locators': ['Theorem2, pp.82–83, and complete proof through p.84',
    'Previously opened Proposition2 and complete-intersection calculation, p.91'],
  'scope': 'Compact-support duality is an ordinary perfect finite-dimensional pairing for compact W. The one-step Cartier resolution identifies the dualizing complex with omega_W[2], without reducedness or normality. This closes the formerly unresolved original-source entries; it is not a new full reading of the whole RR70 paper.'},
 'BS76': {
  'url': 'https://djvu.online/file/2hQiOnz8WuoQk',
  'web_refs': ['turn345view0','turn347view0','turn347view1','turn348view0'],
  'locators': ['ChapterIII §3 Theorem3.4 and proof, pp.116–120',
    'ChapterIII §3 Corollary3.5 and complete proof, pp.120–121',
    'ChapterIII §4 Theorem4.1, complete statement p.124; only the opened portion of its long proof, pp.124–130'],
  'scope': 'Original book reproduction opened. Properness, coherence and flatness match the canonical base-change map; Corollary3.5 at q=3 proves degree2 base change. Theorem4.1 supplies a bounded finite-free complex because the sheaf is flat. No book binary hash or complete proof-reading of Theorem4.1 is claimed.'},
 'Stacks_flatness': {
  'url': 'https://stacks.math.columbia.edu/tag/0AUW',
  'web_refs': ['turn349view0','turn350view0'],
  'locators': ['Lemma15.22.11(1), Tag0AUW; Lemma15.22.10, Tag0539, entire statements and proofs'],
  'scope': 'Torsion-free is equivalent to flat for arbitrary, not necessarily finite, modules over a DVR or valuation ring. The analytic target stalk is a DVR and the nonconstant holomorphic parameter is a non-zero-divisor on the manifold stalk.'},
 'Yang_attached': {
  'path': 'sources/papers/arXiv_2609.29666_Yang_src/Compact_Complex_Threefolds_REPAIRED_v4_5.tex',
  'ranges': [[390,433]],
  'locators': ['Central obstruction for affine symplectic monodromy: statement and complete short proof'],
  'scope': 'Actual quadratic central-extension obstruction read. This is a general affine lift obstruction; it does not state the present three boundary norms, cusp restriction divisor or marked support-degree theorem.'},
 'Wang_attached': {
  'path': 'sources/papers/arXiv_2609.11541_Wang_src/order_two_rational_homology_sphere_new.tex',
  'ranges': [[1732,1772]],
  'locators': ['Explicit theta factors and rank-one/periodic support functions in the order-two example'],
  'scope': 'Actual support-function passage read. It concerns the distinct order-two construction, its parity characters and support function -m(m-1)/2+3n^2, not the receiving six degrees (-12,2,0,-12,2,0) or its -2q descent.'},
 'shared_classical_scopes': {
  'records': ['deliverables/work/root/references_verified.json', 'deliverables/work/maps_audit/references_verified.json', 'deliverables/work/cdp_audit/references_verified.json'],
  'locators': ['Birkenhake–Lange1999, Chapter1 §2, Appell–Humbert Theorem2.1 p.7; semicharacters pp.6–7 (root source read)',
   'Cartan1957, §2 fundamental theorem(B), p.80 (root source read)',
   'Cox–Little–Schenck2010 author preprint, Example1.2.21 p.31, Propositions4.1.1–2 p.171, Theorems4.2.8 p.181,4.2.12 p.184,9.2.3 p.410 (root source read)',
   'Brown1982, I§5 pp.18–19 and VII§§5–6 pp.170–172 (maps source read)',
   'Dimca2004, Theorem2.3.26 pp.41–42, Proposition4.2.11 p.109 and its full proof (maps source read)',
   'Schnell Lecture3, equations(3.3)–(3.10), pp.3–7 (prior CDP source read)'],
  'scope': 'Exact existing opened-source records reused and attributed to their readers. This attribution pass inspected those records; it does not falsely claim a new independent reading of these entire sources.'}
}
for c in contexts.values():
    if 'path' in c:
        p = ROOT / c['path']; assert p.exists(), p
        c['sha256'] = sha(p)
    c['reader'] = READER

AC = 'AC26'
# Each entry: classification, exact AC comparison/locator, operative credit,
# distinct scope. This table is intentionally per result, not a universal credit
# sentence copied over the thirty different assertions.
cfg = {
 'prop:missing-cotangent-filtration': (
  'broader formal filtration; known normal-crossing mechanism credited',
  'Setup10.1, equation(10.1), p.86; Lemma10.3 and §10.4, pp.87–90',
  'AC26 isolates the normal-crossing ambient differential whose intrinsic image is torsion. The receiving statement gives both exact sequences for every reduced Cartier surface, so the full broader formulation is not identified there.',
  'Classical conormal and torsion exact sequences; AC26 Setup10.1, Lemma10.3 and §10.4 for the normal-crossing obstruction. The complete broader formulation is rederived as CDP A.1.1.',
  'The exact preimage K of the torsion sheaf and its two sequences are retained; the shared A.1.1 label does not turn the source NC special case into the full general theorem.'),
 'prop:missing-global-section-criterion': (
  'formal connecting-map criterion with known obstruction input',
  'Lemma10.3 and §10.4, pp.87–90',
  'AC26 exhibits the surviving torsion-supported ambient section and refutes the endpoint inference. The exact criterion ker(delta_A), for arbitrary reduced Cartier S, is a separate long-exact-sequence formulation.',
  'Classical long exact cohomology sequence; AC26 Lemma10.3 and §10.4 for the missing torsion obstruction; full connecting-map criterion rederived in CDP A.1.1.',
  'The statement specifies the two endpoint vanishings and the necessary-and-sufficient injectivity of delta_A. No literature novelty is inferred from not finding the same packaged criterion.'),
 'lem:conormal-injective': (
  'known source normal-crossing statement; broader canonical alias retained',
  'Setup10.1 and equation(10.1), p.86',
  'The original source uses the xy and xyz normal-crossing local models and proves injectivity of h maps to h dg. This is the same NC statement, although the receiving canonical A.1.1 also treats general reduced Cartier divisors.',
  'AC26 Setup10.1, equation(10.1), p.86, for the normal-crossing conormal injection; the complete local proof is rederived.',
  'Credit applies to the actual narrower WB source, not to every generalization carried by its canonical alias.'),
 'lem:conductor-square': (
  'known source normal-crossing conductor square; general canonical extension distinguished',
  'Lemma10.2, equation(10.2), p.87',
  'The normalization-conductor fibre-product exact sequence, including the minus sign in the last arrow, is stated and proved in AC26 under the same NC setup.',
  'AC26 Lemma10.2, p.87; complete conductor fibre-product proof rederived. The broader inverse-Jacobian consequences in canonical CDP A.2.2 have their separate attribution.',
  'The locally free tensor and section-compatibility applications follow the same square; this row does not claim AC26 proves the full broader A.2.2 statement.'),
 'prop:conductor': (
  'known compact normal-crossing conductor mechanism with explicit local scope refinement',
  'Lemma10.3(a)–(c), pp.87–88',
  'The section with pullback dg tensor e and zero conductor restriction, its torsion image, descent criterion and nontrivial-A obstruction are exactly the compact NC conclusion of AC26. The corrected receiving proof isolates local existence from the compactness needed for the final H0(A)=0 clause.',
  'AC26 Lemma10.3, pp.87–88, for the conductor-supported differential and compact-fibre conclusions; independently worded full rederivation and explicit local/nonproper scope separation retained.',
  'The local existence and uniqueness proof works without properness; compact connected S is retained where used to force a nonzero section to be nowhere vanishing.'),
 'prop:nodal-counterexample': (
  'explicit formal counterexample; known obstruction mechanism credited',
  'Lemma10.3 and §10.4, pp.87–90',
  'AC26 gives the conductor mechanism and the constructed global counterexample. The particular nodal cubic times P1 family, its extending non-torsion gluing line bundle and both endpoint cohomology calculations are not identified in the bounded baseline comparison.',
  'AC26 Lemma10.3 and §10.4 for the obstruction mechanism; the complete nodal-cubic test family and its extending twist are retained as a separate construction, canonical CDP B1.',
  'The test refutes the formal sheaf implication, not by itself the CDP global theorem: its ambient family does not meet all global CDP hypotheses.'),
 'thm:cartier-duality': (
  'classical analytic duality rederived for compact Cartier divisors',
  'Theorem10.5 proof Step2, p.88',
  'AC26 uses Gorenstein duality for its reduced normal-crossing fibre. The arbitrary effective Cartier divisor, possibly nonreduced, is supplied by the classical analytic duality theorem rather than asserted as a new result.',
  'Ramis–Ruget1970, Theorem2 pp.82–84 and Proposition2/complete-intersection calculation p.91; Cartier adjunction and finite-dimensional compact duality fully rederived. AC26 Theorem10.5 Step2 is the specific cusp application.',
  'No normality or reducedness is required. The existing one-step Cartier resolution and locally free Ext reduction are part of the complete receiving proof.'),
 'prop:cartier-duality-absolute': (
  'classical compact-support analytic duality rederived without compact ambient space',
  'Theorem10.5 proof Step2, p.88',
  'AC26 uses the same compact-fibre duality in its global example, but does not formulate the noncompact-ambient scope separately.',
  'Ramis–Ruget1970, Theorem2 pp.82–84 and complete-intersection calculation p.91; fibre adjunction trivializes the normal line. AC26 Theorem10.5 Step2 provides the specific application.',
  'Compactness belongs to W, not X. The full scheme-theoretic Cartier fibre may be nonnormal or nonreduced.'),
 'lem:curve-flatness': (
  'classical DVR flatness and analytic identity-theorem consequence',
  'Theorem10.5 proof Step3, p.88',
  'The same flatness/properness input is used in AC26 for its map to the curve. The general lemma is a direct standard local-algebra consequence.',
  'The Stacks Project, Tags0AUW and0539, for torsion-free/flat equivalence over a DVR; the identity theorem and compact-to-Hausdorff properness supply the remaining elementary steps. AC26 Theorem10.5 Step3 uses this input.',
  'The map is nonconstant and X connected, ensuring that a nonzero target germ does not vanish identically on a source germ; no finiteness of the source module over the DVR is assumed.'),
 'prop:analytic-base-change': (
  'known exact analytic base-change corollary',
  'Theorem10.5 proof Step3, p.88',
  'AC26 applies the same top-degree base-change argument to the cusp family. The precise theorem is classical and stated in BS76.',
  'Bănică–Stănăşilă1976, ChapterIII §3 Corollary3.5, pp.120–121, using Theorem3.4; q=3 gives the degree2 canonical base-change isomorphism. AC26 Theorem10.5 Step3 uses this input.',
  'Properness, coherence, flatness and the single H3 fibre vanishing match exactly; no constancy of h2 or local freeness of all direct images is used.'),
 'cor:surface-top-base-change': (
  'classical top-degree base change; separate DVR finite-complex derivation retained',
  'Theorem10.5 proof Step3, p.88',
  'AC26 already uses top-degree base change for surface fibres. The receiving uniform formulation includes full nonreduced fibres and explicitly avoids an all-direct-images-local-free assertion.',
  'Bănică–Stănăşilă1976, ChapterIII §3 Corollary3.5 pp.120–121 and §4 Theorem4.1 p.124; full DVR universal-coefficient argument retained. AC26 Theorem10.5 Step3 supplies the earlier cusp application.',
  'A precise citation locator was corrected from §3 Theorem3.4 to §4 Theorem4.1 for the bounded finite-free complex. The mathematical proof is unchanged.'),
 'prop:pic0-pullback': (
  'classical exponential-sequence argument; weaker-hypothesis formulation retained',
  'Theorem10.5 proof Step1, equation(10.5), p.88',
  'The same c1=0 and H1(O_dP6)=0 argument occurs in AC26 for every line bundle on the actual X. This WB version only needs a Pic0 twist and a local canonical trivialization, not global H2(X;Z)=0.',
  'AC26 Theorem10.5 proof Step1, equation(10.5), p.88, for the normalization-triviality argument; classical exponential sequence and H1(O_dP6)=0. The weaker Pic0-only hypotheses are made explicit.',
  'The hypothesis improvement is not a different underlying Picard mechanism; arbitrary global line bundles require a separate restriction argument.'),
 'prop:all-pic-restriction': (
  'formal pullback criterion; known actual-family vanishing distinguished',
  'Theorem10.5 proof Step1, equation(10.5), p.88',
  'AC26 establishes r=0 for the actual family. The receiving tensor-pullback identity eta*A_L=r(L)^dual is formal and records exactly the additional condition needed beyond Pic0.',
  'Functoriality of line-bundle pullback and tensor duality; AC26 Theorem10.5 Step1, equation(10.5), p.88, for r=0 in the actual construction.',
  'This row is a criterion, not an independent theorem that every local cusp line bundle is normalization-trivial.'),
 'prop:leray-edge-restriction': (
  'known actual-family conclusion; separate integral Leray proof retained',
  'Theorem10.5 proof Step1, equation(10.5), p.88, with the established H2(X;Z)=0',
  'The all-line-bundle normalized restriction is explicitly zero in AC26; its H2(X;Z)=0 also implies the edge section is zero. The receiving proof avoids the packaged topological conclusion by following the integral edge and local specialization.',
  'AC26 Theorem10.5 proof Step1, equation(10.5), p.88, for the all-Picard restriction conclusion; the complete integral Leray-edge method is retained as a distinct rederivation.',
  'No new conclusion is claimed merely because the proof bypasses a global cohomology package.'),
 'lem:picard-crossed-defect': (
  'explicit marked boundary cocycle; classical cohomological inputs credited',
  'Lemma9.4, pp.66–67; construction and monodromy context',
  'AC26 supplies the monodromy-invariant Hodge form and underlying marked construction. The specific pair-of-pants defect, based no-translation relation and base-first sweep sign are not identified as a complete theorem in the bounded comparison.',
  'Brown1982 I§5 and VII§§5–6 for crossed cochains, group extensions and their spectral sequence; AC26 and Engel §6 for the actual invariant form/monodromy. The complete marked defect and sweep-sign calculation is retained separately.',
  'The affine gluing class is fixed to mu=0; changing that class changes the boundary relation and is not covered by this assertion.'),
 'lem:picard-finite-norm': (
  'explicit finite-filling norm identity; classical extension formalism credited',
  'Lemma9.4, pp.66–67; finite-filling geometry used by the construction',
  'The invariant form and finite fillings are existing inputs. The exact clockwise identity N_T d=iota_v E for this marked line-bundle boundary class is not identified as a complete baseline theorem.',
  'Brown1982 I§5 and VII§§5–6 for extension/cochain formalism; the AC26/Engel finite-filling geometry and invariant form. The full logarithmic overlap, lift and norm computation is retained.',
  'The sign uses clockwise base meridians and the translation +v after m turns; a finite matrix check is not substituted for this geometric lift proof.'),
 'lem:picard-cusp-defect': (
  'explicit cusp boundary calculation and classical Chern specialization',
  'Lemma9.4, pp.66–67; local cusp geometry',
  'The underlying cusp construction is known. The stated zero cusp-defect via the concrete solid torus, together with this marked Chern specialization, is not identified as a complete baseline theorem.',
  'Dimca2004 Theorem2.3.26 pp.41–42 and Proposition4.2.11 p.109 for proper nearby-cycle comparison; functoriality of c1. The solid-torus boundary proof is retained for the actual cusp coordinates.',
  'The nearby-cycle statement is integral with the specified coefficient hypotheses. The proof uses the actual locally compact proper analytic cusp neighbourhood.'),
 'prop:direct-boundary-picard': (
  'known actual-family conclusion; independent boundary-norm proof retained',
  'Theorem10.5 proof Step1, equation(10.5), p.88',
  'AC26 explicitly gives normalized restriction zero for all global line bundles; its c1(L)=0 implies the smooth-fibre assertion too. The receiving norm/solid-torus proof is independent of the global Leray transgressions.',
  'AC26 Theorem10.5 proof Step1, equation(10.5), p.88, for the conclusion; the complete marked boundary-Picard rederivation is retained, with Brown/Dimca classical inputs separately credited.',
  'The arithmetic 4n delta and -3n delta forces n=0 only after the finite-filling and cusp identities have been geometrically proved.'),
 'cor:candidate-pic0-route': (
  'known nonvanishing conclusion; proof with weaker topological inputs retained',
  'Theorem10.5(a), proof Steps1–3, pp.88–89',
  'The original proves the nonzero H2 fibre and R2 direct image for every line bundle. Its proof contains the ambient differential. Restriction to Pic0 is therefore wholly known as a conclusion.',
  'AC26 Theorem10.5(a), pp.88–89, and Lemma10.3 for the conductor section; the complete Pic0-only route without global topology is retained as a rederivation.',
  'The distinctive feature is the reduced dependency set, not a new nonvanishing conclusion.'),
 'thm:candidate-conductor': (
  'hypothesis-isolated conductor theorem; known actual application and proof mechanism',
  'Theorem10.5(a), proof Steps1–3, pp.88–89',
  'The proof uses precisely the normalization-triviality, conductor, Cartier-duality and top-base-change mechanism of AC26. The WB formulation separates four sufficient hypotheses rather than assuming the entire named construction.',
  'AC26 Lemma10.3 and Theorem10.5(a), pp.87–89, for the conductor mechanism and constructed-family conclusion; RR70 and BS76 for duality and base change. The full hypothesis-isolated proof is retained.',
  'The four stated geometric/topological assumptions must all hold. This row does not independently reconstruct or revalidate the global family.'),
 'cor:candidate-conductor-actual': (
  'known exact constructed-family nonvanishing',
  'Theorem10.5(a), pp.88–89',
  'Both nonzero H2 on the cusp fibre and nonzero R2 direct image for every global L are the explicit conclusion of AC26 Theorem10.5(a).',
  'AC26 Theorem10.5(a), pp.88–89; complete application of the separated hypotheses retained as a rederivation.',
  'The construction/topology inputs are separately proved in Paper I; this short application is not credited as a new global construction proof.'),
 'lem:cdp-generic-endpoints': (
  'known endpoint argument in explicit arbitrary-dimensional formulation',
  '§10.6, pp.94–95',
  'AC26 explicitly invokes CDP98 Corollary1.3 for H0 and Serre duality for H3. The WB arbitrary-dimensional statement with O(D) in Pic0 is the same elementary Proposition1.1 argument.',
  'Campana–Demailly–Peternell1998 Proposition1.1, Corollaries1.2–1.3, plus Serre duality; AC26 §10.6 explicitly preserves this valid input. Full decreasing-section-space proof retained.',
  'The complete proof does not require a false all-direct-images-local-free conclusion or a non-torsion assertion on every fibre.'),
 'thm:corrected-cdp-global': (
  'conditional repair with known endpoint/semicontinuity/RR inputs',
  '§10.6, pp.94–95',
  'AC26 states the valid endpoint vanishings, chi=-h1+h2 and the need for extra H2 control. The exact one-twist H2=0 sufficient hypothesis is not identified there as a separate theorem.',
  'CDP98 Proposition1.1/Corollary1.3, analytic semicontinuity and Hirzebruch–Riemann–Roch; AC26 §10.6 for the surviving endpoint argument and missing H2 condition. The explicit one-twist conditional repair is proved in full.',
  'The result is conditional. It does not restore the invalid published universal vanishing theorem; the constructed example fails the added hypothesis.'),
 'cor:corrected-cdp-relative': (
  'known intact relative sufficient criterion',
  '§10.6, pp.94–95, surviving argument context',
  'AC26 separates intact endpoint arguments from the false global claim; the exact sufficient relative condition is directly printed in CDP2020 Proposition2.4.',
  'Campana–Demailly–Peternell2020 Proposition2.4, p.680; full relative-to-global projection-formula/Leray proof rederived. The receiving stronger topology hypotheses imply the original b2=0 assumptions.',
  'Credit is to the valid conditional proposition, not to the later invalid attempt to prove its premise universally.'),
 'thm:corrected-cdp-fibrewise': (
  'explicit reduced-fibre repair; classical duality/base-change and known defect credited',
  'Lemma10.3, §10.4 and §10.6, pp.87–90,94–95',
  'AC26 supplies the torsion obstruction and shows the original two endpoint vanishings are insufficient. The exact additional injectivity condition delta_c and its full fibrewise-to-relative implication are not identified as a complete earlier statement.',
  'AC26 Lemma10.3 and §§10.4,10.6 for the identified defect; RR70 Cartier duality, BS76 top-degree base change, and CDP2020 Proposition2.4 for the intact final implication. The corrected fibrewise criterion is proved in full.',
  'Every full scheme-theoretic fibre is assumed reduced; the argument does not silently handle nonreduced conormal layers.'),
 'test:cdp-comparison': (
  'comparison/status consequence, not a new independent theorem',
  'Theorem10.5(a), Corollary10.6, pp.88–89; §10.6, pp.94–95',
  'The all-L nonzero R2 and theorem-level CDP counterexample are already established in AC26. The WB summary also distinguishes the added hypotheses of its corrected criteria.',
  'AC26 Theorem10.5 and Corollary10.6 for the constructed theorem-level counterexample; CDP98/2020 for the intact conditional inputs. This row records the logical comparison of those results and the fully printed repairs.',
  'No independent global-construction proof or literature novelty is claimed for this summary row.'),
 'prop:local-cusp-picard-obstruction': (
  'explicit local support divisor and descent; existing invariant form credited',
  'Lemma9.4, pp.66–67',
  'AC26 supplies q=u wedge w+6 gamma wedge delta, its integral Hodge property and type(1,6). It does not give in the checked context the precise Q(v)=v1^2-6v2^2 equivariant divisor, six degrees (-12,2,0,-12,2,0), and c1=-2q descent.',
  'AC26 Lemma9.4 and Engel §6 for the invariant type(1,6) form; Cox–Little–Schenck divisor/support-function conventions and Schnell Lecture3 for factor-of-automorphy Chern signs. The explicit local divisor and full descent calculation are retained separately.',
  'This nonzero local restriction is consistent with zero restriction for bundles extending to the complete global threefold; local and global Picard groups are not conflated.'),
 'prop:analytic-ah-boundary': (
  'explicit analytic boundary identities; Appell–Humbert and group-cochain inputs credited',
  'Lemma9.4, pp.66–67; Theorem10.5 Step1, p.88, for the eventual conclusion',
  'The invariant Hodge form and eventual normalized restriction conclusion are known. The exact three boundary identities derived from holomorphic factors and the argument principle are not identified as a complete earlier baseline theorem.',
  'Birkenhake–Lange1999 Appell–Humbert Theorem2.1 p.7 and semicharacters pp.6–7; Brown1982 cochain/extension formalism; AC26/Engel invariant form and construction. The complete analytic marked boundary proof is retained.',
  'The torus need not be projective and the Hermitian form need not be positive. The no-terminal-translation based relation and inverse-transpose convention are essential hypotheses.'),
 'lem:analytic-support-specialization': (
  'explicit analytic toric support specialization; classical support and Stein inputs credited',
  'Lemma9.4, pp.66–67; Theorem10.5 Step1, p.88, for the global application',
  'AC26 proves the global all-line-bundle restriction by topology. The precise arbitrary local analytic M support-degree identity E_M((lambda,0),(0,m))=-B(B0 lambda,m) is not identified there.',
  'Cox–Little–Schenck2010 preprint Propositions4.1.1–2 p.171, Theorems4.2.8 p.181 and4.2.12 p.184 for toric Cartier/support data; Cartan1957 theorem(B) p.80 and the exponential sequence for analytic local Picard triviality. The mixed Chern-block formula is proved in full.',
  'An algebraic toric divisor theorem alone does not classify arbitrary analytic line bundles. The receiving proof separately proves triviality on the actual Stein annular charts and controls horizontal winding.'),
 'thm:analytic-all-picard': (
  'known global conclusion; third independent analytic proof retained',
  'Theorem10.5 proof Step1, equation(10.5), p.88',
  'The zero homomorphism Pic(X) to Pic(dP6) is explicitly established in AC26. The receiving proof via holomorphic factors, boundary norms and support functions avoids both global Leray and integral nearby cycles.',
  'AC26 Theorem10.5 proof Step1, equation(10.5), p.88, for the entire all-Picard restriction conclusion; the complete independent analytic proof is retained with its classical Appell–Humbert, Cartan and toric inputs.',
  'A different complete proof is preserved without presenting its already known conclusion as a new theorem.')
}
assert set(cfg) == {r['source_id'] for r in selected}

known_ac_full = {'lem:conormal-injective','lem:conductor-square','prop:leray-edge-restriction',
 'prop:direct-boundary-picard','cor:candidate-pic0-route','cor:candidate-conductor-actual','thm:analytic-all-picard'}
boundary = {'lem:picard-crossed-defect','lem:picard-finite-norm','lem:picard-cusp-defect',
 'prop:direct-boundary-picard','prop:local-cusp-picard-obstruction','prop:analytic-ah-boundary',
 'lem:analytic-support-specialization','thm:analytic-all-picard'}
duality = {'thm:cartier-duality','prop:cartier-duality-absolute'}
basechange = {'prop:analytic-base-change','cor:surface-top-base-change'}
known_elsewhere = duality | basechange | {'lem:curve-flatness','lem:cdp-generic-endpoints','cor:corrected-cdp-relative'}
elsewhere_inputs = known_elsewhere | boundary | {
 'prop:pic0-pullback','prop:leray-edge-restriction','thm:candidate-conductor',
 'thm:corrected-cdp-global','thm:corrected-cdp-fibrewise','test:cdp-comparison'}

def evidence(sid, corpus, full, comparison, locator, positive=False):
    s = search_by[sid, corpus]
    return {'status': ('found_matching_known_conclusion_in_specified_scope' if full else
                       'found_known_input_or_special_case_in_specified_scope' if positive else
                       'full_counterpart_not_identified_in_bounded_checked_scope'),
     'full_statement_or_conclusion_found': full,
     'comparison': comparison, 'positive_or_context_locator': locator,
     'terms_searched': s['patterns'], 'searched_files': s['searched_files'],
     'search_record': 'deliverables/work/cdp_audit/II_working_credit/searches_150.json#' + sid + '|' + corpus,
     'full_search_hits': 'deliverables/' + s['full_hit_file'],
     'actual_context_readings': 'deliverables/work/cdp_audit/II_working_credit/context_readings.json#' + (corpus if corpus != 'elsewhere_attached' else 'CDP98/CDP2020/RR70/BS76/shared_classical_scopes'),
     'negative_search_limit': 'A bounded search and the listed opened contexts do not establish absence from all literature or that every unrelated hit was read.'}

rows, overlay = [], []
for old in selected:
    sid = old['source_id']; m = mapping[sid]; p = ROOT / m['source_file']
    lines = p.read_text().splitlines()
    block = '\n'.join(lines[m['source_line_start']-1:m['source_line_end']])
    blocksha = hashlib.sha256(block.encode()).hexdigest()
    assert blocksha == m['full_statement_and_proof_sha256'], (sid, blocksha)
    classification, acloc, accomparison, credit, distinction = cfg[sid]
    r = {'source_run': old['source_run'], 'source_id': sid, 'paper': 'II',
      'printed_label': old['printed_label'], 'canonical_or_retained_label': m['printed_label'],
      'source_file': m['source_file'], 'source_lines': [m['source_line_start'],m['source_line_end']],
      'source_file_sha256': sha(p), 'source_statement_and_full_proof_sha256': blocksha,
      'source_slice_matches_existing_mapping_hash': True,
      'reader': READER, 'classification': classification, 'credited_to': credit,
      'precise_scope_and_distinct_proof': distinction,
      'current_mapping': {'assembly_action': m['assembly_action'], 'alias': m['alias_label'],
       'record': 'deliverables/work/cdp_audit/working_supplement_mapping.json'},
      'receiving_proof_check_preserved': proofs[sid]['own_check'],
      'receiving_proof_check_record': 'deliverables/work/cdp_audit/working_edition_inventory.json#' + sid,
      'new_check_scope': 'Attribution/source-hypothesis comparison and exact source-slice concordance. All thirty receiving statements and existing complete-proof check records were reviewed. This event does not claim a fresh second complete reading of every long receiving proof.',
      'historical_inventory_row': old,
      'historical_working_source_check': proofs[sid],
      'novelty_limit': 'No worldwide novelty assertion follows from bounded negative searches. Known conclusions and classical inputs receive explicit credit even when a distinct proof is retained.'}
    r['found_in_AC26'] = evidence(sid, 'AC26', sid in known_ac_full, accomparison, acloc, True)
    if sid in boundary:
        ec = 'Engel §6 supplies the primitive invariant integral form of elementary divisors(1,6) and the rank-one invariant lattice; the concluding remark explicitly credits AC26 §9.1. Those are partial inputs, not the whole marked boundary or support-divisor assertion.'
        eloc = '§6 The integral homology, invariant-form/open-invariants lemmas, source lines1275–1330; concluding comparison lines1665–1740'
    else:
        ec = 'No full counterpart to this exact receiving statement was identified in the per-row queries and opened Engel contexts. The construction and invariant-form discussion is not equated with a conductor, duality, or coherent vanishing theorem.'
        eloc = 'Opened §6 invariant-form context and final comparison; see context_readings.json#E26'
    r['found_in_E26'] = evidence(sid,'E26',False,ec,eloc,sid in boundary)
    if sid in duality:
        dc = 'Version1 contains a related relative Gorenstein-duality lemma over a smooth DM base, with p_*O=O and local freeness assumptions. The receiving absolute compact-Cartier pairing, including nonreduced W and noncompact ambient X, follows from RR70 and is not equated with that differently scoped relative theorem.'
        dl = 'Analytic relative-duality lemma and full proof, source lines9091–9149'
    elif sid in basechange:
        dc = 'Version1 analytic Grauert lemma assumes constant fibre cohomology dimensions and concludes local freeness/base change. This is a related classical input; it is weaker in scope than the receiving top-degree statement allowing h2 jumps.'
        dl = 'Analytic Grauert lemma and full proof, source lines9050–9090'
    elif sid in {'prop:local-cusp-picard-obstruction','prop:analytic-ah-boundary','lem:analytic-support-specialization'}:
        dc = 'Version1 explicitly uses Cartan/exponential-sequence Picard triviality on C* times C or C2 in local Oka constructions. That standard local input is related; the present equivariant support divisor, arbitrary analytic cusp restriction, and boundary norm identities are not identified there as complete statements.'
        dl = 'Source lines3350–3405 and3765–3810'
    else:
        dc = 'No full matching receiving assertion was identified in the per-row Version1 searches and the listed opened contexts. Relative tangent/cohomology or construction statements are not treated as an identical conductor/Picard result.'
        dl = 'Version1 introduction and analytic foundational lemmas; see context_readings.json#DGKX_v1'
    r['found_in_DGKX_v1'] = evidence(sid,'DGKX_v1',False,dc,dl,sid in duality | basechange | {'prop:local-cusp-picard-obstruction','prop:analytic-ah-boundary','lem:analytic-support-specialization'})
    r['found_in_DGKX_v2'] = evidence(sid,'DGKX_v2',False,
       'No full counterpart was identified in the independently executed Version2 query and the opened Version2 construction context. No Version1 theorem is silently assigned to Version2.',
       'Version2 introduction and construction scope, lines230–330; exact per-result full-file query retained')
    elsewhere_comparison = (credit + ' ' + distinction if sid in elsewhere_inputs else
       'No additional full counterpart was identified in the bounded 43-file attached-literature search and opened contexts. The positive AC26 credit is recorded separately, not relabelled as an elsewhere discovery. ' + distinction)
    r['found_elsewhere'] = evidence(sid,'elsewhere_attached',sid in known_elsewhere,
       elsewhere_comparison,
       'Exact operative originals and existing checked loci are itemized in the credited_to text and context_readings.json; 43 attached-source files were separately searched.',sid in elsewhere_inputs)
    r['found_elsewhere']['special_apparent_hit_checks'] = ['Yang central affine obstruction, lines390–433; distinct statement', 'Wang order-two theta/support-function passage, lines1732–1772; distinct construction'] if sid in boundary else []
    closure = ''
    if sid in duality:
        closure = 'Original-source closure completed: RR70 Theorem2 pp.82–84 and the already opened Proposition2/complete-intersection calculation p.91 match the compact Gorenstein Cartier pairing. Compactness of W, finite-dimensionality and the locally free twist were checked; no reducedness/normality assumption is added.'
    elif sid in basechange:
        closure = 'Original-source closure completed: BS76 III§3 Corollary3.5 pp.120–121 (q=3) and Theorem3.4 pp.116–120 match top-degree base change; III§4 Theorem4.1 p.124 supplies the bounded finite-free complex under flatness. The complete proof of Corollary3.5 and the full statement, not the whole long proof, of Theorem4.1 were opened.'
    r['current_original_source_closure'] = closure
    new = dict(old)
    for key in ['found_in_AC26','found_in_E26','found_in_DGKX_v1','found_elsewhere']:
        new[key] = json.dumps(r[key], ensure_ascii=False, separators=(',',':'))
    new['credited_to'] = credit
    if closure:
        new['your_check'] = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, 17 November 2026 UTC: Existing complete receiving proof reading preserved in working_credit_comparison_30.json. ' + closure
        new['check_outcome'] = 'Complete receiving proof and exact operative original-source hypotheses checked in the specified scopes. ' + ('Finite-complex citation locator corrected; mathematical proof unchanged.' if sid == 'cor:surface-top-base-change' else 'Historical unresolved-source wording is preserved only in the audit history.')
    else:
        new['your_check'] += ' | Attribution/source-concordance pass, same reader and date: precise bounded four-baseline and operative-original comparisons saved in work/cdp_audit/II_working_credit/working_credit_comparison_30.json.'
    new['notes'] = old['notes'].replace('distinct_proof=pending comparison', 'distinct_proof=completed exact source-to-print mapping; full proofs retained or canonical aliases recorded')
    new['notes'] += ' | Current attribution: ' + classification + '. ' + distinction + ' | DGKX_v2: bounded independent query and opened-context comparison; no full counterpart identified, no global absence claim. Full separate v2 evidence and all historical fields: work/cdp_audit/II_working_credit/working_credit_comparison_30.json#' + sid
    assert list(new) == fields
    rows.append(r); overlay.append(new)

dump(OUT / 'context_readings.json', {'reader': READER, 'contexts': contexts,
  'scope': 'Only listed source contexts and receiving statements/check records are newly read here. Search hits alone are not source matches. Shared exact original-source scopes retain the original reader provenance.'})
dump(OUT / 'working_credit_comparison_30.json', {'reader': READER,
 'timestamp_utc': datetime.now(timezone.utc).isoformat(), 'scope': '30 WORKING_CDP PaperII rows only',
 'counts': {'rows':30,'executed_searches':150,'corpora_per_row':5,'attached_elsewhere_files':43},
 'rows': rows, 'manuscript_mutated': False, 'master_inventory_mutated': False,
 'historical_checks_preserved': True,
 'source_reading_policy': 'Full receiving proof checks remain their prior exact events; this event is the bounded attribution/source-hypothesis and source-slice comparison. Positive original-source matches are explicit and negative searches are not novelty proofs.'})
dump(OUT / 'working_credit_inventory_overlay_30.json', {'reader': READER, 'fields': fields, 'rows': overlay,
 'merge_key': ['source_run','source_id'], 'history_record': 'work/cdp_audit/II_working_credit/working_credit_comparison_30.json',
 'scope': 'Replace these 30 current attribution/mapping fields from the exact rows; preserve their embedded historical inventory/check records. No INV or correction-note rows are included.'})
with (OUT / 'working_credit_inventory_overlay_30.csv').open('w', newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(overlay)

# A separate, status-only closure for a transferred PaperI row. Its positive
# AC26 credit and full universal-property proof already exist and are unchanged.
sem = next(r for r in inventory if r['source_run']=='WORKING_CDP' and r['source_id']=='lem:semidirect-abelianization')
semnew = dict(sem)
semnew['notes'] = sem['notes'].replace('distinct_proof=pending comparison', 'distinct_proof=completed; transferred full credited universal-property proof in Paper I, with AC26 Lemma10.7 p.90 explicitly credited')
semnew['notes'] += ' | Current mapping closure: work/cdp_audit/working_supplement_mapping.json#lem:semidirect-abelianization and paperI_transfer_credit_audit.json; historical note preserved in semidirect_status_overlay.json.'
dump(OUT / 'semidirect_status_overlay.json', {'reader':READER,'rows':[semnew], 'historical_row':sem,
 'scope':'Status-only replacement of the obsolete distinct-proof comparison note. No new proof reading, attribution search, statement or manuscript change.'})

# Reference scopes are supplemented, never replaced by a blanket verification.
refpath = D/'work/cdp_audit/references_verified.json'
refs = json.loads(refpath.read_text()); changed=[]
for r in refs:
    if r.get('key') == 'RR70':
        loc = 'Theorem2, published pp.82–83, and complete proof through p.84; text lines250–435 reopened in final WORKING_CDP attribution pass'
        if loc not in r['opened_locators']: r['opened_locators'].append(loc)
        r.setdefault('additional_scope_checks',[])
        if not any(e.get('record')=='work/cdp_audit/II_working_credit/context_readings.json#RR70' for e in r['additional_scope_checks']):
            r['additional_scope_checks'].append({'reader':READER,'record':'work/cdp_audit/II_working_credit/context_readings.json#RR70','scope':contexts['RR70']['scope']})
        changed.append('RR70')
    if r.get('key') == 'BS76':
        for loc in contexts['BS76']['locators']:
            if loc not in r['opened_locators']:r['opened_locators'].append(loc)
        for ref in contexts['BS76']['web_refs']:
            if ref not in r['web_refs']:r['web_refs'].append(ref)
        r.setdefault('additional_scope_checks',[])
        if not any(e.get('record')=='work/cdp_audit/II_working_credit/context_readings.json#BS76' for e in r['additional_scope_checks']):
            r['additional_scope_checks'].append({'reader':READER,'record':'work/cdp_audit/II_working_credit/context_readings.json#BS76','scope':contexts['BS76']['scope']})
        changed.append('BS76')
    if r.get('key') == 'Viaclovsky2026Combs':
        r['opened_locators']=[x.replace('degrees=Theorem3.2 p8','degrees=Proposition3.2 p8') for x in r['opened_locators']]
        r.setdefault('metadata_corrections',[])
        correction={'date':'2026-11-17 UTC','reviewer':'/root/invariants_arithmetic','scope':'Exact original compiled PDF p.8 and source newtheorem declaration: degrees is Proposition3.2, not Theorem3.2. Receiving INV text was already correct. Proposition9.2 analytic and Proposition9.3 canonical are on p.31; Questions §10 p.33. No paper statement changed.'}
        if correction not in r['metadata_corrections']:r['metadata_corrections'].append(correction)
        changed.append('Viaclovsky2026Combs')
if not any(r.get('key')=='StacksDVRFlatness' for r in refs):
    refs.append({'key':'StacksDVRFlatness','aliases':['StacksProject'],'title':'Torsion-free modules over valuation rings and Dedekind domains',
      'url':'https://stacks.math.columbia.edu/tag/0AUW','status':'verified in the specified scope',
      'opened_locators':contexts['Stacks_flatness']['locators'], 'web_refs':contexts['Stacks_flatness']['web_refs'],
      'verification_scope':contexts['Stacks_flatness']['scope'],'own_check':READER,
      'uses':['WORKING_CDP lem:curve-flatness'], 'not_verified':[]})
    changed.append('StacksDVRFlatness')
dump(refpath,refs)
dump(OUT/'reference_scope_updates.json',{'reader':READER,'updated_keys':changed,
 'source_record':'work/cdp_audit/references_verified.json',
 'scope':'Exact RR70/BS76 source closures, Stacks DVR lemma, and correction of one already checked Viaclovsky statement-type metadata typo; historical entries/scopes preserved.'})
print(json.dumps({'rows':len(rows),'overlay_columns':len(fields),'source_slice_hashes_matched':len(rows),
 'reference_scope_updates':changed,'outputs':str(OUT)},ensure_ascii=False))
