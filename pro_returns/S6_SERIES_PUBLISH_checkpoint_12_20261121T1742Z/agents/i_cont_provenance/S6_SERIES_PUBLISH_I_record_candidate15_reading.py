#!/usr/bin/env python3
"""Serialize the actual full-image reading of candidate15 pages 308--345."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SOURCE_SHA = '45bf46fc14a50f7a148cdd34bf2be68b04cd89e1cb7d620191c6e8518f7249f8'
PDF_SHA = 'b72c6da6acddfd797c82837fbd086e222eeef8e4526ed736328affde474df780'

NOTES = {
308: 'Read the continued statement of Proposition 26.19 and proof steps 1--3: complexified norm, rank-four sampling subgroup, derivative fields, periodicity and fixed-field identity. Displays and text are legible. Two D02 tails follow their positive periodicity and rank conclusions; exact proposals are being prepared.',
309: 'Read proof steps 3--7: one fixed number field, logarithmic gradient and Hessian, vector-extension argument for transcendence, normalized second derivative and differential criterion. D02: the extra no-algebraicity-assumption clause repeats the explicitly stated K[H0] conclusion. The mathematical calculations remain intact.',
310: 'Read the rank/growth inequality, the algebraic-independence argument, packing estimate, and the opening of Proposition 26.20 on division ratios. The displayed inequality and constants, equations (26.19)--(26.20), title and small tag are legible. No additional concrete defect found.',
311: 'Read the remainder of Proposition 26.20 and proof step 1: degree and height envelopes, changes of parameter, translated functions, unique division ratio and torsion limit. The final sentence of the statement announces what the following calculations record; proposed removal preserves every bound and the pointer to the open question.',
312: 'Read the real/complex degree bounds, uniform-height argument, division-polynomial coefficient estimate and the real division-logarithm group with its additive coefficient map. All formulas, exponents and nested enumeration levels fit. No concrete defect found.',
313: 'Read the scalar transformation, common-denominator isogeny, algebraic multipliers, upper and lower transcendence-degree arguments, recovery of the elliptic coordinate and complex-shift formula. Every displayed map and denominator is legible. No concrete defect found.',
314: 'Read the semi-abelian sampling map, joint O(n^5) degree envelope, height bounds, exact interpolation inequality and exponent comparison, then the arithmetic-germ citation. Source locators, operators and displayed inequalities fit. No concrete defect found.',
315: 'Read the logarithmic tangent, Mahler/entropy inputs, period-refined rank coefficient and period-line calculation. Two closing scope sentences repeat the open-question status already given with the exact reduction; deletion proposals retain all stated inputs, ranks and source locators. The remainder of the page is legible.',
316: 'Read all of Remark A.1 and its proof: four DGKX assertions, precise parameter map and inverse, half-plane comparison, and comparison of the two external versions. The title, re-derived wording and two own-chronology sentences are body-history residues; the final no-reason-for-change sentence is a repeated scope disclaimer. The integral-obstruction statement at the foot remains legible.',
317: 'Read Proposition A.2 proof steps 1--5: source-to-target lattice map, fixed vectors/covectors, rational centralizer, affine lift and the complete period equation. Matrices, indices and equation (A.3) are clear. No concrete defect found.',
318: 'Read the finite-root obstruction in full: two cyclic norm matrices, normalized branch lifts, logarithmic translation, iterated equation and finite obstruction class. The negative conclusions are derived from the displayed exact equalities and divisibility. No concrete defect found.',
319: 'Read the end of the parity obstruction and Proposition A.3 with proof steps 1--2: real-linear period map, transported tangent coefficient, Kodaira--Spencer convention, real determinant and inverse. The hypotheses, signs, equation labels and tag fit. No concrete defect found.',
320: 'Read Proposition A.3 proof steps 3--7: integral obstruction to exactness, sign conversion, relative canonical pencil, dual-number base change and the intrinsic deformation comparison. All connecting maps, sections and displays are legible. No concrete defect found.',
321: 'Read the scheme-sensitive critical-locus argument, first-order projective automorphism and Kodaira--Spencer conclusion. Read Remark B.1 and the opening of Theorem B.2. B.1 contains an incomplete are [citation] construction and a redundant re-derivation sentence; exact editorial proposals preserve its standard-case credit and the weighted extension.',
322: 'Read Theorem B.2 continuation and proof steps 1--5: tangent dimensions, Kodaira--Spencer classes, root-forgetting map, Picard calculation, structure-sheaf direct images and logarithmic tangent sequence. The weighted monomial calculation and all displayed bundles are legible. No concrete defect found.',
323: 'Read proof steps 6--9: weighted cohomology, cusp normal sequence, connecting-map rank, constant cocycle, sign convention and analytic miniversality via the cited Douady statements. All locators, cohomological indices and proof transitions are clear. No concrete defect found.',
324: 'Read the coarse direct-image calculation through the extension: first Koszul matrix, explicit frame changes, next differential, cokernel Q and the vanishing Ext group. The previously removed canonicity disclaimer is absent; its positive splitting argument remains. All matrices and equations fit. No concrete defect found.',
325: 'Read the normal-coefficient sequence, fibre-sensitive top-degree calculation, complete direct images and finite invariants. Read Definition C.1, its conductor ideal and root-line identifications. All formulas and heading transitions are legible. No concrete defect found.',
326: 'Read Theorem C.2 and its proof, Theorem C.3 with the complete direct-image table, and proof steps 1--3. The introductory citation sentence has incomplete are [result/citation] phrasing; a grammatical proposal preserves both internal references and all DGKX locators. The mathematical table and maps fit.',
327: 'Read the conductor-square incidence calculation and completion of Theorem C.3, then Theorem C.4 and proof steps 1--4: automorphism group, finite-root exclusion and the translation sheaf. The incidence matrix, exact sequence and toric local argument are legible. No concrete defect found.',
328: 'Read the continuation of the translation extension, integral lattice matrix and inverse, and completion of the automorphism proof. Read Theorem C.5 and its affine, finite-root and torsor setup. Mathematical uses of normalization, exact comparisons and the additive choice are supported by the displayed maps. No concrete defect found.',
329: 'Read the rest of Theorem C.5: complex ranks, explicit degree-two presentation, constant-sheaf comparison, torsor character, parity and extension over all special charts. The matrix dimensions describe the mathematical complex and carry no saved-file bookkeeping. No concrete defect found.',
330: 'Read the complete final open-question section: two exact normalized-norm examples, unresolved group-order identification, the cited relative-period conjecture and its motivic/central-coordinate reduction. The section expressly states open questions and retains all formulas and source locators. No concrete defect found.',
331: 'Read the Programs heading, pinned historical commit, table headings and every first-page row from period determinants through genus and descent computations. Filenames occur in the required program table with receiving mathematical statements. Columns, links and rules fit. No concrete defect found.',
332: 'Read every continuation row of the Programs table, from Bernstein bounds through the integral E8/neck calculation. Natural matrix/point counts describe the stated computations; filenames and historical words inside filenames remain program citations. No clipping or concrete defect found.',
333: 'Read every final Programs-table row, from cone/orbit counts through the trace-obstruction and section computations. Every source filename remains aligned with its mathematical scope; the continuation headings and closing rule fit. No concrete defect found.',
334: 'Read the bibliography from Abasheva--Deev through the beginning of Bertolin et al. Names, accents, titles, publisher information and line-broken URLs are legible and ordered. No concrete defect found on this page.',
335: 'Read the bibliography from the continuation of Bertolin et al. through Cai--Shu--Tian. The BFH1990 entry points to a third-party personal-site copy; its exact Springer publisher DOI has now been opened for the proposed replacement. The remainder is legible.',
336: 'Read the bibliography from Cai et al. through Darmon. Conrad, Cornulier and Cossec--Dolgachev--Liedtke use joined field paragraphs that differ from the surrounding entry format; the proposals insert the same field separation and preserve their complete edition/pagination statements. URLs and accents fit.',
337: 'Read the bibliography from de Cataldo et al. through Duke--Imamoglu, including both DGKX versions. Drinfeld has joined field paragraphs; a formatting proposal preserves both the Russian original and English translation, DOI and archive link. No additional concrete defect found.',
338: 'Read the bibliography from Eichler--Zagier through Fujiki--Pontecorvo. Author names, titles, exact arXiv version labels, publisher identifiers and wrapped URLs are legible. No concrete defect found.',
339: 'Read the bibliography from Fujimoto through the beginning of Gross1991. The journal/preprint pagination qualification for Gross--Zagier is explicit; author/publisher/archive links and accents fit. No concrete defect found on this page.',
340: 'Read the bibliography from Gross1991 through Jetchev--Lauter--Stein. Gross1991 has a third-party personal-site chapter-scan link in addition to its publisher DOI; the exact Cambridge chapter record has been opened and the scan-link deletion is proposed. The remaining entries and edition qualifications are legible.',
341: 'Read the bibliography from Kajiwara--Kato--Nakayama through McHugh. Lin--Wang and Mazur--Stein--Tate use joined field paragraphs; field-separation proposals retain every bibliographic datum and link. The long Cambridge URL and all remaining entries fit.',
342: 'Read the bibliography from McMullen through Noguchi. Merkulov repeats the identical DOI as a second URL; Movasati repeats the year after its full dated-version statement. Exact deletions preserve the remaining DOI and complete date. No additional concrete defect found.',
343: 'Read the bibliography from Oda through Schroeer--Siebert. The Ramis--Ruget and Ramis--Ruget--Verdier entries use a different author/year arrangement and joined fields; precise presentation changes retain author initials, titles, year, pages and DOI. The official TIFR pagination qualification and remaining links are legible.',
344: 'Read the bibliography from Shin through both Viaclovsky entries. Silverman repeats 2006 after January 2006; the proposal removes only the duplicated year. All remaining author names, version labels, identifiers and wrapped URLs are legible.',
345: 'Read all final bibliography entries: the five Waldschmidt sources, Xiao, Xie, Yang and Yuan--Zhang--Zhang. The chronological subdivision, author URLs, publication data and version labels are legible; the final page and bibliography ending fit. No concrete defect found.',
}
PENDING = {
308: [1,2], 309: [3], 311: [4], 315: [5,6], 316: [7,8,9,10],
321: [11,12], 326: [13], 335: [14], 340: [15], 342: [16,17],
344: [18], 336: [19,20,21], 337: [22], 341: [23,24], 343: [25,26],
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


source = ROOT / 'S6_SERIES_PUBLISH_I.tex'
pdf = ROOT / 'build/I_candidate15/S6_SERIES_PUBLISH_I.pdf'
manifest_path = ROOT / 'render/I_candidate15/manifest.json'
assert sha(source) == SOURCE_SHA and sha(pdf) == PDF_SHA
manifest = json.loads(manifest_path.read_text())
assert manifest['pdf_sha256'] == PDF_SHA
pages_by_num = {row['page']: row for row in manifest['rendered_pages']}
assert set(NOTES) == set(range(308,346))
rows = []
for page, note in sorted(NOTES.items()):
    image = ROOT / f'render/I_candidate15/page_{page:03d}.png'
    digest = sha(image)
    assert digest == pages_by_num[page]['image_sha256']
    guards = [f'I15-prov-{n:02d}' for n in PENDING.get(page, [])]
    rows.append({'page': page, 'image': str(image.relative_to(ROOT)),
                 'image_sha256': digest, 'pdf_sha256': PDF_SHA,
                 'finding': note, 'actual_full_page_image_read': True,
                 'pending_guards': ', '.join(guards)})
result = {
    'paper': 'I', 'candidate': 15,
    'reader': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation provenance agent',
    'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'source_sha256': SOURCE_SHA, 'pdf_sha256': PDF_SHA,
    'render_manifest_sha256': sha(manifest_path),
    'register': 'S6_DEFECT_REGISTER.csv',
    'register_sha256': sha(ROOT / 'S6_DEFECT_REGISTER.csv'),
    'register_types_read': [f'D{n:02d}' for n in range(1,26)],
    'pages': rows,
    'actual_full_page_images_read': 38,
    'pending_guards': [f'I15-prov-{n:02d}' for n in range(1,27)],
    'guard_file': 'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate15_provenance_guards.json',
    'guard_status': 'Exact guard file in preparation; source remains unchanged. Candidate15 is not certified while these proposals are pending.',
    'mathematical_events_added': 0,
    'source_changes_applied': False,
    'scope': 'Actual complete image reading of each of pages 308--345 against all 25 register types. The images were individually emitted at full size in consecutive batches and read. The record claims publication/page review only; it adds no mathematical proof-check event.',
}
dest = OUT / 'S6_SERIES_PUBLISH_I_final_candidate15_reading_provenance.json'
dest.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
md = ['# Paper I candidate15: provenance-agent page reading', '',
      f'Source SHA-256: `{SOURCE_SHA}`. PDF SHA-256: `{PDF_SHA}`.', '',
      'All 38 complete images on pages 308--345 were actually viewed and read against D01--D25. Pending exact editorial guards are recorded below; no source changes or mathematical events were made.', '',
      '| Page | Actual finding | Pending guards | Image SHA-256 |',
      '|---:|---|---|---|']
for row in rows:
    md.append('| '+str(row['page'])+' | '+row['finding'].replace('|', '\\|')+' | '+row['pending_guards']+' | `'+row['image_sha256']+'` |')
(OUT / 'S6_SERIES_PUBLISH_I_final_candidate15_reading_provenance.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'record': str(dest.relative_to(ROOT)), 'sha256': sha(dest),
                  'actual_full_page_images_read': 38, 'pending_guards': 26,
                  'mathematical_events_added': 0}, indent=2))
