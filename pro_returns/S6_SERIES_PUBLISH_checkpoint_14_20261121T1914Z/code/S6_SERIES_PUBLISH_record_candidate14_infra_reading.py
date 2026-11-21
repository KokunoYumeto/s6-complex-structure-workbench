#!/usr/bin/env python3
"""Record the actual continuation-infrastructure reader's page observations.

The observations below were written after viewing every complete assigned
PNG in the conversation. This program binds those observations to the exact
images and saves two proposed editorial guards; it creates no check event.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'agents/continuation_infra'
SOURCE = ROOT/'S6_SERIES_PUBLISH_I.tex'
MANIFEST = ROOT/'render/I_candidate14/manifest.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


observations = {
228: 'Read Section22.9 and Proposition22.42 through proof step4: the effective Cartier axis, normal multiplier, contraction coordinates, reduced cycle and node equation. All text and displays are legible; references and small tag fit. No concrete defect found.',
229: 'Read the remainder of Proposition22.42: degree-zero normal line, scaling action, root-interface comparison, distinct critical loci, local plumbing equation and the compact-curve obstruction. The negative conclusions have their explicit coordinate/curve arguments on the page. No concrete defect found.',
230: 'Read Proposition22.43 and proof steps1–3: six point blow-ups, the two displayed charts, exponent sequence and the twelve-component central cycle. All formulas, indices and statement text fit. No concrete defect found.',
231: 'Read proof steps4–7: normal-divisor coefficients, the72 curve blow-ups, normal comparison by s^-12, local character exponents and holomorphic H. Displays and numbered equations are clear. No concrete defect found.',
232: 'Read proof steps8–11: the product-model charts, exact characters and divisorial orders, convergent product G, and the linear closing formula. The source confirms that the short transition says following characters. No typography or mathematical error established.',
233: 'Read the end of Proposition22.43 and Section22.10/Proposition22.44 through proof step2, including the full chart table and toric subdivision. D02 residue: after the positive dense-torus closure description, the clause no additional component of the naive total transform is included repeats a defensive exclusion. Exact deletion proposed in guardI14-infra-01; source is unchanged by this reading.',
234: 'Read Proposition22.44 proof steps3–7: chart gluing, normal crossings, fibre equations, comparison with the modified collar, the product G and rational W-coordinate map. Read the beginning of Proposition22.45. All text and the long statement title fit; no concrete defect found.',
235: 'Read the continuation of Proposition22.45 and proof steps1–3: winding of the exceptional intersection, proper analytic-closure contradiction, and proper-modification/meromorphic-graph argument with the source locator. No concrete defect found.',
236: 'Read Proposition22.45 proof steps4–6 and the opening of Proposition22.46. The normal exact sequence, Kodaira deformation application, conductor example and displayed cohomology dimensions are legible. D02 residue: That proposition does not require the submersion to be proper. The preceding text gives its positive application hypotheses and exact source locator; exact deletion proposed in guardI14-infra-02. No source edit made.',
237: 'Read Proposition22.46 proof steps1–3: character/period lattices, multiplicative pairing, all logarithmic admissibility faces, residual units and extending axial origin. The citation locators and pairing table are clear. No concrete defect found.',
238: 'Read proof steps4–9: axial origins, overlap translation, deck differences, period-sheaf exact sequence, ghost valuation, injectivity and finite root covers. The lattice exclusions are supported by the explicit exponentiation and valuation maps. No concrete defect found.',
239: 'Read the ordinary-gauge comparison and start of Proposition22.47: Hopf surfaces, anticanonical automorphy, resonance equations and the dimension formula. All mathematical signs and ranges are legible. No concrete defect found.',
240: 'Read Proposition22.47 proof steps2–6: accumulating resonances by Rouche, nonresonant points, coherent direct images, the exact base-change sequence and reduction/resolution of a proposed completion. Source locators and displays fit. No concrete defect found.',
241: 'Read the completion of Proposition22.47, Remark22.48 with explicit toric-ray and anticanonical blow-up comparisons, and Proposition22.49 through its initial finite-cover setup. New section heading and statement remain together; no concrete defect found.',
242: 'Read Proposition22.49 proof steps2–7: holomorphic trace, local root covers, explicit multiplicative norms and the exact dF obstruction. The sign in the norm formula, exponents and equation references are clear. No concrete defect found.',
243: 'Read proof steps8–9, then Section22.13 and Proposition22.50 through the bounded-character sheaf. The finite-projection locator, dimension argument, boundary divisors and sheaf display are legible. No concrete defect found.',
244: 'Read Proposition22.50 proof steps2–6: bounded character support, blow-up cohomology, exceptional intersection basis, exponential/divisor sequences and degree-two period map. All cohomological superscripts and direct sums are legible. No concrete defect found.',
245: 'Read the valuation block and end of Proposition22.50, then Proposition22.51 and the start of its surface/Euler analysis. The N=0 scope, monodromy rank, canonical-divisor identities and Kahler accent are correctly displayed. No concrete defect found.',
246: 'Read Proposition22.51 proof steps3–10: rational, ruled, Hopf and Inoue cases with exact locators, blow-up contributions, Euler integration and elliptic normal-degree balance. No overflow, unresolved reference or concrete mathematical error found in this page reading.',
247: 'Read proof steps10–13: elliptic dual-graph rank bound, hyperbolic toric mapping torus, marked Clifford torus, homology vanishing, base-change section and local logarithmic two-form. Source locators, matrices and displayed forms are legible; no concrete defect found.'
}

source = SOURCE.read_text()
source_sha = sha(SOURCE)
assert source_sha == '1f2d0d376f71e7843265976aeeb72cf8e1ff77aea176ff5dbb4e67446c25b36f'
manifest = json.loads(MANIFEST.read_text())
assert manifest['pdf_sha256'] == '1abe0fc16350045cd2ce0aae57ce377dcfe2400de0b0bf58ba7e559d360bcb37'
pages = {x['page']: x for x in manifest['rendered_pages']}
rows = []
for number, observation in observations.items():
    page = pages[number]
    assert sha(Path(page['image'])) == page['image_sha256']
    rows.append(dict(page=number, image_sha256=page['image_sha256'],
                     pdf_sha256=manifest['pdf_sha256'], finding=observation,
                     actual_full_page_image_read=True,
                     pending_guards=({'233':'I14-infra-01', '236':'I14-infra-02'}.get(str(number), ''))))

guard_specs = [
 ('I14-infra-01', 233, 'D02',
  'on the closure of the dense torus; no additional\ncomponent of the naive total transform is included.',
  'on the closure of the dense torus.',
  'The positive closure and cancellation operation remains exactly stated, followed by all three charts and their smoothness calculation. The extra negative clause repeats that same choice.'),
 ('I14-infra-02', 236, 'D02',
  'That proposition does not require the submersion to be\nproper. ',
  '',
  'The preceding sentence states the holomorphic submersion, relative dimension two and compact simply exceptional divisor, with the exact primary locator. The negative reminder is redundant to that explicit application; the Kodaira credit and Merkulov locator remain.')
]
guards = []
for key, page, kind, before, after, reason in guard_specs:
    assert source.count(before) == 1
    at = source.index(before)
    start = source.rfind(r'\begin{proof}', 0, at)
    end = source.index(r'\end{proof}', at) + len(r'\end{proof}')
    original = source[start:end]
    replacement = original.replace(before, after, 1)
    math_pattern = r'\$[^$]*\$|\\\[.*?\\\]'
    assert re.findall(math_pattern, original, re.S) == re.findall(math_pattern, replacement, re.S)
    assert re.findall(r'\\(?:label|hypertarget)\{[^}]*\}', original) == re.findall(r'\\(?:label|hypertarget)\{[^}]*\}', replacement)
    old_path = OUT/f'S6_SERIES_PUBLISH_{key}_original_full_proof.tex'
    new_path = OUT/f'S6_SERIES_PUBLISH_{key}_proposed_full_proof.tex'
    old_path.write_text(original)
    new_path.write_text(replacement)
    guards.append(dict(id=key, page=page, type=kind, line=source.count('\n',0,at)+1,
                       before=before, after=after, reason=reason,
                       source_sha256=source_sha,
                       original_full_proof=str(old_path.relative_to(ROOT)), original_full_proof_sha256=sha(old_path),
                       proposed_full_proof=str(new_path.relative_to(ROOT)), proposed_full_proof_sha256=sha(new_path),
                       mathematical_display_and_inline_segments_identical=True,
                       labels_and_targets_identical=True,
                       comparison='Both complete proofs were read in the rendered pages and compared with their source. The proposal deletes only the quoted prose; all mathematical inputs, equations, claims, proof steps and source locators used remain.',
                       status='proposed, not applied', mathematical_events_added=0))
record = dict(paper='I', candidate=14, reader='GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation infrastructure agent',
              recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(), source_sha256=source_sha,
              pdf_sha256=manifest['pdf_sha256'], render_manifest_sha256=sha(MANIFEST),
              pages=rows, pending_guards=[x['id'] for x in guards], mathematical_events_added=0,
              scope='Actual complete rendered-page reading of pages228–247 against all25 register types; two exact editorial guard proposals remain for root integration. No mathematical re-proof, targeted proof check or certification is claimed.')
record_path = OUT/'S6_SERIES_PUBLISH_I_final_candidate14_reading_infra.json'
record_path.write_text(json.dumps(record,indent=2)+'\n')
(OUT/'S6_SERIES_PUBLISH_I_candidate14_infra_guards.json').write_text(json.dumps(guards,indent=2)+'\n')
md = ['# Paper I candidate14: infrastructure-agent rendered-page reading', '',
      f'Source SHA-256: `{source_sha}`. PDF SHA-256: `{manifest["pdf_sha256"]}`.', '',
      'Every assigned full-page image228–247 was actually viewed and read. Two D02 prose residues are proposed for correction; no source was edited and no mathematical check event was added.', '',
      '| Page | Finding |', '|---:|---|']
md += [f'| {x["page"]} | {x["finding"].replace("|", "\\|")} |' for x in rows]
(OUT/'S6_SERIES_PUBLISH_I_final_candidate14_reading_infra.md').write_text('\n'.join(md)+'\n')
print(json.dumps(dict(reading_record=str(record_path), pages=len(rows), proposed_guards=[x['id'] for x in guards], mathematical_events_added=0)))
