#!/usr/bin/env python3
"""Record the actual, individually viewed candidate16 full-page PNG reading."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SOURCE_SHA = '61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc'
PDF_SHA = '4a1633d9e19a82e3df92a0e3c31ada306b3e801f3051b0c1b7f0018d873f51a2'

NOTES = {
308: 'Read the continued Proposition 26.19 statement and proof steps 1--4: normalized second derivative, periodicity on C^2, rank-four subgroup, fixed-field identity and logarithmic differentiation. The two previously removed defensive tails are absent; the displayed maps and rank argument remain legible. No new concrete defect found.',
309: 'Read the logarithmic gradient and Hessian, transcendence argument, exact second-derivative field, differential criterion, Waldschmidt inequality and start of the algebraic-independence argument. The phrase To prove k transcendental, recall introduces the immediately used real-period identity and proof operation. All formulas and primary-source locators fit. No new concrete defect found.',
310: 'Read the growth and packing comparison, the end of Proposition 26.19, and the complete opening statement of Proposition 26.20: division ratios, exact scalar change, degree/height bounds, translated functions and joint degree envelope. The pointers to the final open question state mathematical dependencies. No new concrete defect found.',
311: 'Read proof steps 1 and 2 of Proposition 26.20: uniqueness and kernel of the division-ratio map, CM and torsion identities, real/complex degree estimates, and division-polynomial coefficient bounds. The prior statement-level D08 announcement is absent. The coefficient-estimate sentence names the mathematical method that the immediately following Cauchy estimate supplies; it is retained. No new concrete defect found.',
312: 'Read the uniform-height argument, real division-logarithm group, coefficient map, exact scalar transformation and common-denominator isogeny. Every displayed domain, exponent and quotient is legible, and the proof operations are mathematical uses of the indicated maps. No new concrete defect found.',
313: 'Read the lower transcendence-degree argument, recovery of the elliptic coordinate, complex-shift formula, semi-abelian sampling map and joint O(n^5) degree envelope. The explicit map from normalized to raw translates remains in the proof. No new concrete defect found.',
314: 'Read the joint height argument, interpolation inequality and exponent comparison, logarithmic tangent, Mahler input and entropy citation. The comments about sharper bounds and the base field describe the displayed numerical comparison and exact field issue. Formulas, exponents and source locators are legible. No new concrete defect found.',
315: 'Read the period-refined rank coefficient and the complete period-line calculation ending Proposition 26.20. The two approved D11 closing sentences are absent; the period ranks, exact independence statement and pointer to Proposition 26.14 remain. The deliberate appendix page break leaves clear whitespace. No new concrete defect found.',
316: 'Read all of Remark A.1 and its proof, including the exact parameter map and inverse, half-plane map, tangent/deformation comparison and the two external-version descriptions, then the opening of Proposition A.2. The approved own-history and scope removals are visible. No new concrete defect found.',
317: 'Read Proposition A.2 proof steps 2--6: fixed vectors and covectors, rational centralizer, affine torus lift, complete period equation and first cyclic norm matrix. All matrices, indices and equation labels are legible. No new concrete defect found.',
318: 'Read the rest of Proposition A.2 in full: second norm matrix, branch normalization, marked torus map, local-ring lift, deck-equivariance identity, iterated equation and finite parity obstruction. D08: We first justify why a local isomorphism must satisfy the exact affine equations on the marked finite cover is a standalone announcement preceding the complete derivation. Exact deletion proposal I16-prov-01 preserves every displayed equation and the entire local-to-global argument.',
319: 'Read Proposition A.3 and proof steps 1--3: real-linear period map, inverse, transported tangent matrix, sign convention, determinant and integral obstruction. The admissible-domain exclusion follows from the displayed determinant and is mathematical proof content. No new concrete defect found.',
320: 'Read Proposition A.3 proof steps 4--8: sign conversion, relative canonical pencil, dual-number base change, projective comparison and beginning of the critical-scheme argument. D08: Here is a scheme-sensitive check is a standalone announcement; proposal I16-prov-02 removes it while retaining the positive first-order assertion and every critical ideal, chart and parameter-ring map.',
321: 'Read the complete critical-scheme calculation, first-order projective automorphism and Kodaira--Spencer conclusion, followed by Remark B.1 and the opening of Theorem B.2. The prior B.1 grammar and D08 fixes are visible; exact standard-case citations and weighted hypotheses remain. The sentence ending in choose local product charts performs the proof operation it introduces and is retained. No further concrete defect found.',
322: 'Read the remainder of Theorem B.2 and proof steps 1--5: root-forgetting morphism, analytic Picard calculation, structure-sheaf direct images, logarithmic tangent sequence and weighted monomial cohomology. Closing phrases identify the mathematical conclusions of the displayed maps. No new concrete defect found.',
326: 'Read Theorem C.2 and its full proof, Theorem C.3 and its full direct-image table, then proof steps 1--3. The approved grammatical corrections are visible; both internal and external locators, determinant line, invariant-section map and conductor sequence remain. No new concrete defect found.',
}
PENDING = {318: ['I16-prov-01'], 320: ['I16-prov-02']}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

source = ROOT / 'S6_SERIES_PUBLISH_I.tex'
pdf = ROOT / 'build/I_candidate16/S6_SERIES_PUBLISH_I.pdf'
manifest_path = ROOT / 'render/I_candidate16/manifest.json'
assert sha(source) == SOURCE_SHA and sha(pdf) == PDF_SHA
manifest = json.loads(manifest_path.read_text())
assert manifest['pdf_sha256'] == PDF_SHA
manifest_pages = {r['page']: r for r in manifest['rendered_pages']}
assert set(NOTES) == set(range(308, 323)) | {326}
rows = []
for page, finding in sorted(NOTES.items()):
    path = ROOT / f'render/I_candidate16/page_{page:03d}.png'
    digest = sha(path)
    assert digest == manifest_pages[page]['image_sha256']
    rows.append({'page': page, 'image': str(path.relative_to(ROOT)),
                 'image_sha256': digest, 'pdf_sha256': PDF_SHA,
                 'finding': finding, 'actual_full_page_image_read': True,
                 'pending_guards': ', '.join(PENDING.get(page, []))})
result = {
    'paper': 'I', 'candidate': 16,
    'reader': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation provenance agent',
    'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'source_sha256': SOURCE_SHA, 'pdf_sha256': PDF_SHA,
    'render_manifest_sha256': sha(manifest_path),
    'register': 'S6_DEFECT_REGISTER.csv',
    'register_sha256': sha(ROOT / 'S6_DEFECT_REGISTER.csv'),
    'register_types_read': [f'D{n:02d}' for n in range(1, 26)],
    'pages': rows, 'actual_full_page_images_read': 16,
    'pending_guards': ['I16-prov-01', 'I16-prov-02'],
    'guard_file': 'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate16_provenance_guards.json',
    'guard_status': 'Two exact D08 proposals in preparation; source unchanged. Broader contextual D08 audit is separate and gives no full-page reading credit.',
    'mathematical_events_added': 0, 'source_changes_applied': False,
    'scope': 'Actual complete image reading of each of pages 308--322 and 326 against all 25 register types. Each complete PNG was individually emitted and read after context restoration. An earlier truncated multi-image tool output is not credited. This record adds no mathematical proof-check event. The candidate15 reading record remains immutable.',
}
dest = OUT / 'S6_SERIES_PUBLISH_I_final_candidate16_reading_provenance.json'
md_dest = dest.with_suffix('.md')
assert not dest.exists() and not md_dest.exists(), 'Immutable reading record already exists'
dest.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
md = ['# Paper I candidate16: provenance-agent page reading', '',
      f'Source SHA-256: `{SOURCE_SHA}`. PDF SHA-256: `{PDF_SHA}`.', '',
      'All 16 complete PNGs on pages 308--322 and 326 were individually viewed and read against D01--D25. Two D08 proposals remain pending. No source mutation or mathematical event is claimed.', '',
      '| Page | Actual finding | Pending guards | Image SHA-256 |',
      '|---:|---|---|---|']
for r in rows:
    md.append(f"| {r['page']} | {r['finding'].replace('|', chr(92)+'|')} | {r['pending_guards']} | `{r['image_sha256']}` |")
md_dest.write_text('\n'.join(md) + '\n')
print(json.dumps({'record': str(dest.relative_to(ROOT)), 'sha256': sha(dest),
                  'actual_full_page_images_read': 16, 'pending_guards': 2,
                  'mathematical_events_added': 0}, indent=2))
