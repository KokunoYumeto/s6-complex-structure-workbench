#!/usr/bin/env python3
"""Serialize the actually completed 26 individual candidate17 full-page readings."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SOURCE_SHA = '5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
PDF_SHA = '3c9f15b28d768f305ab09dfb86ef98365aeb4659329b33e6faedb91864094ab0'
NOTES = {
  "302": "Read the statement continuation and all five visible proof steps: the real logarithm and transcendental slope, the dual polarization convention, endomorphism factorization, the concrete 2P and discriminant calculation, and the analytic subgroup argument. The convention sentence introduces the displayed morphisms; the conclusions and cited theorem are attached to their mathematical use. No new register defect found.",
  "303": "Read the final compactness/logarithm calculation, Remark 26.15 and its cited graph-dimension theorem, Definition 26.16, and the opening of Proposition 26.17. The Gaussian term, retained curve/logarithm conventions, and algebraic field of definition remain explicit. The graph statement is supported by the displayed dimension argument and keeps its separate point-value question. No new register defect found.",
  "304": "Read Proposition 26.17's full displayed conclusion on the CM action, compact point, Gaussian eigenprojection and nonexistence assertions, followed by proof steps 1–3. The character calculation, Rosati convention, endomorphism injection and theta quotient are all retained mathematical operations with their formulas. No new register defect found.",
  "305": "Read the remaining logarithm calculation and proof steps 4–7 of Proposition 26.17, including the period comparison fixing the matrix entry, Gaussian identity, uniform eigenvalue error bound, and irrational toric line argument. The removed announcements leave continuous derivations and all displayed identities intact. No new register defect found.",
  "306": "Read proof steps 8–10: the ordinary prime 5 comparison, conductor-361 constants, degree-19 CM map, explicit kernel polynomials, coprimality identities and rational function. The new positive prime-5 opening and shortened transitions retain the exact coordinate conventions, kernel counts and formulas. No new register defect found.",
  "307": "Read the CM witness evaluations and norm, Remark 26.18's determinant-one period basis and analytic branch, and the opening of Proposition 26.19. The conjugation convention now appears inside the proposition, followed by the curve, point, logarithm, entire norm function, rank-four subgroup and derivative formulas. No orphaned roadmap remains at the section opening; no new register defect found.",
  "308": "Read Proposition 26.19's remaining derivative assertion and proof steps 1–5 on conjugation, periodicity, the rank-four lattice, the fixed number field, logarithmic derivatives and the real period. The field and squaring explanation is tied to the exact identity (26.18), and the positive Hessian calculation remains explicit. No new register defect found.",
  "309": "Read the end of the nonsplitting argument and proof steps 6–10: the second-jet field identity, cited differential criterion, exact growth inequality (26.19), algebraic independence argument, and rank/growth substitution. The numerical obstruction is given by its explicit inequalities and sampling count. No new register defect found.",
  "310": "Read all of Proposition 26.20's division-ratio, rescaling, height, degree and translated-function assertions, then the opening uniqueness and division-identity proof. The hypotheses, positive real logarithm convention, real/complex degree bounds and stated field scopes remain visible and attached to their formulas. No new register defect found.",
  "311": "Read Proposition 26.20's algebraicity and torsion limits, separate real/complex degree estimates, coefficient bound and complete visible height calculation. The phrase introducing the coefficient estimate states the mathematical method immediately implemented by the fixed circle, Cauchy estimate and height inequalities. No new register defect found.",
  "312": "Read the normalized-translate identities, additive coefficient map on division logarithms, scalar parameter transformation, common-denominator isogeny argument and transcendence-degree lower bound. All equations and the sampling-group map remain explicit; no workflow residue or new register defect found.",
  "313": "Read the exact multiplication map from normalized to raw translates, the complex-shift identity and all visible joint degree/height estimates on the sampling group. The section coordinate, character, abstract group homomorphism, exceptional-point treatment and O(n^5) degree calculation are retained with their stated fields. No new register defect found.",
  "314": "Read all interpolation inequalities and the arithmetic-germ, Mahler, entropy and period-rank comparisons through the end of Proposition 26.20. The envelope exponents, tangent ratio, transcendental Taylor coefficient, coefficient alpha(G_Q)=4 and rank-two/rank-three comparison are explicit mathematical grounds for the stated scopes. No new register defect found.",
  "315": "Read Remark A.1 and its complete period/deformation comparison, including the exact parameter translation and inverse, the cited version-specific assertions and retained data scope. Also read Proposition A.2 and its initial integral-monodromy proof. The literature comparison has a displayed morphism and explicit cited claims; no new register defect found.",
  "316": "Read Proposition A.2's fixed vectors and covectors, rational centralizer calculation, affine lift argument, exact period equation and the opening finite-root norm matrix. The argument retains every displayed map and its integrality conclusion. No new register defect found.",
  "317": "Read the finite-cover normalization and unique lifted map, deck-equivariance identity, iterated lattice equation, exclusion of the negative linear part and the exact parity quotient. The source-to-normalization map and all norm-image lattices remain explicit; the final sentence concludes the displayed parity calculation. No new register defect found.",
  "318": "Read Proposition A.3's exact real-linear period map, tangent-space convention, Kodaira–Spencer sign and nonzero class, followed by proof steps 1–3. The marked lattice map, determinant, inverse-domain justification and integral obstruction remain explicit. No new register defect found.",
  "319": "Read the explicit minus-sign conversion between tangent conventions, relative canonical pencil, degree-two system over dual numbers, and start of the complete-threefold nontriviality argument. The scheme-sensitive argument begins directly with its critical ideal and injective parameter-ring map. No new register defect found.",
  "320": "Read the cusp critical-ideal continuation, identity of the base automorphism, complete Kodaira–Spencer trivialization argument, and opening of Appendix B through Theorem B.2. The Čech spelling is corrected; the transition cocycle, chart change, cited interpretation, coarse direct-image credit and theorem's arrow convention remain explicit. No new register defect found.",
  "321": "Read the standard coarse direct images and Theorem B.2 proof steps 1–5, including the root-forgetting morphism, Picard presentation, structure-sheaf direct images, logarithmic tangent exact sequence and weighted Laurent cohomology calculation. The exact morphisms and basis conventions remain in place. No new register defect found. Page 322 is outside this new-reading assignment and receives no new credit here.",
  "323": "Read the complete visible Koszul-map computation in Theorem B.2 step 10, including the coefficient matrix, explicit frame changes, both connecting maps, cokernel sequence and length-two root-point sheaf. The opening identifies the actual computational method whose maps follow; the c_0 convention and geometric cocycle scaling are explicit. No new register defect found.",
  "324": "Read the normalization tangent quotient, fibre calculation of the extension at p_0, completed root and coarse direct images, and Definition C.1 with its divisor weights. Potential D08 residue: the standalone sentence 'We give a fibre-sensitive calculation.' after the extension-at-p_0 introduction. Full-source statement/proof review is required before proposing any exact deletion; no source change or new event is recorded here.",
  "325": "Read Theorem C.2 with its complete local differential-image proof and Theorem C.3 through the conductor-square opening. The direct-image table, determinant-line identity, invariant-section map and root-to-coarse formula retain the precise sheaves and divisor conventions. No new register defect found.",
  "326": "Read the conductor incidence matrix and direct-image conclusion, then Theorem C.4 and proof steps 1–4. The exact exponential group isomorphism, affine centralizer, finite-root obstruction and translation-sheaf sequence remain explicit. 'We compute all components' introduces the substantive component calculation carried by that exact sequence, consistent with the inherited contextual disposition. No new register defect found.",
  "327": "Read the end of the translation-sheaf proof, integral cocycle parametrization and determinant-minus-one inverse, completion of Theorem C.4, and Theorem C.5 through the restriction map. Potential D08 residue: 'Here is the integral lattice calculation, including torsion.' before the exact matrix calculation. The matrix, integral inverse and H^1=0 conclusion provide the positive mathematical scope; full-source review will precede any exact guard.",
  "328": "Read all remaining Theorem C.5 proof steps: total-complex ranks and Smith reductions, the exact degree-two relations, conductor/cohomology identification, torsor character, parity class and extension of the isomorphism across all three charts. The Čech spelling is corrected and every displayed relation and shearing map is retained. No new register defect found."
}
NOTES = {int(k): v for k,v in NOTES.items()}
PENDING = {324: ['I17-prov-01'], 327: ['I17-prov-02']}
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
source = ROOT / 'S6_SERIES_PUBLISH_I.tex'
pdf = ROOT / 'build/I_candidate17/S6_SERIES_PUBLISH_I.pdf'
manifest_path = ROOT / 'render/I_candidate17/manifest.json'
assert sha(source) == SOURCE_SHA and sha(pdf) == PDF_SHA
manifest = json.loads(manifest_path.read_text())
assert manifest['pdf_sha256'] == PDF_SHA
manifest_pages = {r['page']: r for r in manifest['rendered_pages']}
assert set(NOTES) == set(range(302,329)) - {322}
rows = []
for page,finding in sorted(NOTES.items()):
    path = ROOT / f'render/I_candidate17/page_{page:03d}.png'
    digest = sha(path)
    assert digest == manifest_pages[page]['image_sha256']
    rows.append({'page': page, 'image': str(path.relative_to(ROOT)),
                 'image_sha256': digest, 'pdf_sha256': PDF_SHA,
                 'finding': finding, 'actual_full_page_image_read': True,
                 'pending_guards': ', '.join(PENDING.get(page,[]))})
result = {
 'paper': 'I', 'candidate': 17,
 'reader': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation provenance agent',
 'recorded_utc': datetime.now(timezone.utc).isoformat(),
 'source_sha256': SOURCE_SHA, 'pdf_sha256': PDF_SHA,
 'render_manifest_sha256': sha(manifest_path),
 'register': 'S6_DEFECT_REGISTER.csv', 'register_sha256': sha(ROOT / 'S6_DEFECT_REGISTER.csv'),
 'register_types_read': [f'D{n:02d}' for n in range(1,26)],
 'pages': rows, 'actual_full_page_images_read': 26,
 'pending_guards': ['I17-prov-01','I17-prov-02'],
 'guard_file': 'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate17_provenance_guards.json',
 'guard_status': 'Two D08 loci require complete-source proof review before exact proposals; source unchanged.',
 'mathematical_events_added': 0, 'source_changes_applied': False,
 'scope': 'Actual complete image reading of each of pages 302--321 and 323--328 against all 25 register types. Each full PNG was individually emitted and read. The initial truncated page-302 tool output is not credited; page 302 was reopened and fully read. Page 322 has no new reading credit here. Historical candidate15 and candidate16 reading receipts remain immutable. This record adds no mathematical proof-check event.',
}
dest = OUT / 'S6_SERIES_PUBLISH_I_final_candidate17_reading_provenance.json'
md_dest = dest.with_suffix('.md')
assert not dest.exists() and not md_dest.exists(), 'Immutable reading receipt already exists'
dest.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
md = ['# Paper I candidate17: provenance-agent page reading', '',
 f'Source SHA-256: `{SOURCE_SHA}`. PDF SHA-256: `{PDF_SHA}`.', '',
 'All 26 assigned complete PNGs were individually viewed and read. Page 322 receives no new reading credit. Two D08 loci await complete-source review and exact guard preparation. No source change or mathematical event is claimed.', '',
 '| Page | Actual finding | Pending guards | Image SHA-256 |',
 '|---:|---|---|---|']
for r in rows:
    finding = r['finding'].replace('|', chr(92)+'|')
    md.append(f"| {r['page']} | {finding} | {r['pending_guards']} | `{r['image_sha256']}` |")
md_dest.write_text('\n'.join(md)+'\n')
print(json.dumps({'record': str(dest.relative_to(ROOT)), 'sha256': sha(dest),
 'actual_full_page_images_read': len(rows), 'pending_guards': 2,
 'mathematical_events_added': 0}, indent=2))

