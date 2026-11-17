#!/usr/bin/env python3
"""Persist the actual retained-angle primary-source readings of 17 Nov 2026.

This is a record generator, not a mathematical certificate. Verification is
scoped to the pages actually read; retrieval alone never sets its status.
"""
from pathlib import Path
import copy
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'deliverables/work/invariants_arithmetic'
CACHE = 'sources/audit_cache/inv_ari/retained_angle_literature/'
READER = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode)'
DATE = '2026-11-17 UTC'
RECEIVING = 'sources/workbench/higher_rung_24d_continuation.tex'


def digest(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def source(key, filename, url, aliases, locators, use, check, extent, **extra):
    path = CACHE + filename
    row = {
        'citation_key': key,
        'aliases': aliases,
        'status': 'verified_for_stated_use',
        'verified': True,
        'checker': READER,
        'reader': READER,
        'effort': 'Pro',
        'date': DATE,
        'local_source': path,
        'source_sha256': digest(path),
        'url': url,
        'opened_locators': locators,
        'actual_use': use,
        'hypotheses_and_normalization_check': check,
        'extent': extent,
        'receiving_context': {
            'source': RECEIVING,
            'source_sha256': digest(RECEIVING),
            'lines_personally_read_for_this_check': '4840–5015',
            'full_receiving_proof_reader': '/root; independently reported full reading of lines4378–5111',
        },
        'historical_provenance_policy': 'Earlier source-bundle verification claims are not substituted for these dated original-source readings.',
    }
    row.update(extra)
    return row


rows = [
    source(
        'Pontryagin1950Root', 'Pontryagin1950.pdf',
        'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/pont3.pdf',
        ['h24:retbib:Pontryagin1950', 'Pontryagin1950'],
        ['Complete original Russian pp.957–959: PDF1 right page and PDF2 both pages, visually opened; theorem at p.957 additionally enlarged.',
         'p.958 equations(1)–(4), including the intersection correction; p.959 parts(e)–(f), bordism invariant and explicit rotating torus normal frame.'],
        'Classical computation pi_(n+2)(S^n)=Z/2 for n≥2, hence the stable second stem. Known-source credit for the framed-surface quadratic obstruction.',
        'The printed range is n≥2, checked in the original image. The curve invariant includes both component parity and frame-loop parity. Its quadratic identity includes mod-two intersection; the paper explicitly corrects the earlier omission of that term. The torus normal frame rotates by the difference of the two angular coordinates. This is an antecedent, not a calculation of the manuscript’s particular inverse image.',
        'All three original pages read. The paper imports the at-most-two bound from Freudenthal; no claim of independently opening that 1937 paper here. PDF3 is an appended review and was not treated as the original.',
        title='Homotopy classification of mappings of an (n+2)-dimensional sphere on an n-dimensional one',
        author='L. S. Pontryagin', year=1950, journal='Doklady Akademii Nauk SSSR',
        volume='70', pages='957–959', language='Russian',
        visual_evidence=[CACHE+'views/Pontryagin1950_1.png', CACHE+'views/Pontryagin1950_2.png', CACHE+'views/Pontryagin1950_theorem.png'],
    ),
    source(
        'Pontryagin1955Root', 'Pontryagin1955.pdf',
        'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/pont4.pdf',
        ['h24:retbib:Pontryagin1955', 'Pontryagin1955'],
        ['English translation introduction pp.1–2 and contents/translator p.114, visually opened.',
         '§12(D), pp.86–87: frame-loop parity and its additivity.',
         '§13, p.90: explicit Hopf normal-frame formula and end of Lemma1; Lemma2 and Theorem19 pp.90–92.',
         'Entire §14, pp.92–101: smoothing lemma, Theorem20 with full proof pp.96–99, and Theorem21 with full proof pp.99–101.',
         'Entire §15, pp.101–112: Theorem22 pp.103–106, Theorem23 pp.106–109, Theorem24 pp.109–112, including equations(23)–(29) and torus calculation pp.110–111.',
         'Critical original spreads visually opened: PDF44 pp.90–91, PDF48 pp.98–99, PDF49 pp.100–101, PDF50 pp.102–103, PDF53 pp.108–109, PDF54 pp.110–111. Other stated pages read from local OCR of the original scan, with mathematical formulas checked against the visible source where operative.'],
        'Classical framed-circle invariant, stable Hopf generator, and framed-surface computation of the second stable stem. The receiving proof retains its explicit Hopf-frame contraction and torus calculation.',
        'Theorem20 uses an orthonormally normally framed closed one-manifold in oriented Euclidean space and gives delta=frame-loop parity plus component parity. A constant full stable frame on a circle therefore has delta=1. Theorem21 identifies the stable one-dimensional group for n≥3 and reduces the Hopf invariant modulo2. Theorem24 gives the two-dimensional group for n≥2 and uses the quadratic invariant and a torus with values1 on both basic cycles. Stabilization preserves delta. These conventions match the receiving Lie framing.',
        'The cited operative §§14–15 and their proofs were read in the 1959 English translation. The scan omits printed pp.88–89: no complete §13/Lemma1 reading is claimed. Its p.90 conclusion and the later theorems were opened; the receiving Hopf formula is independently derived in full. No unexamined chapter is marked read.',
        title='Smooth manifolds and their applications in homotopy theory',
        author='L. S. Pontryagin', year=1955,
        original_publication='Trudy Matematicheskogo Instituta imeni V. A. Steklova45 (1955)',
        edition_opened='English translation by P. J. Hilton, American Mathematical Society Translations, Series2, volume11 (1959), pp.1–114.',
        source_scan_limitation='The Rochester copy jumps from printed p.87 to p.90. This bounded scan omission is outside the fully read §§14–15 and does not hide an operative receiving gap.',
        ocr_scope=[CACHE+f'Pontryagin1955_{i}_ocr.txt' for i in range(43,56)],
    ),
    source(
        'Johnson1980Root', 'Johnson1980.pdf',
        'https://math.mit.edu/~hrm/palestine/johnson-spin-structures.pdf',
        ['h24:retbib:Johnson', 'Johnson1980'],
        ['§2 pp.365–366: closed orientable surface, unit tangent bundle, and spin-class convention.',
         'Entire §3 pp.366–370: Theorems1A–1C and their proofs, including the component/fibre correction and quadratic canonical lift.',
         'Entire §4 pp.370–372: Lemma2, Theorems3A–3B with proofs; p.371 visually opened.',
         '§5 pp.372–373: Lemma3, its proof and corollaries; Theorem4 and proof read for scope but not used in the receiving argument.'],
        'Original surface proof of the spin-structure/quadratic-refinement correspondence and its naturality; exact normalization for the receiving Arf calculation.',
        'Johnson’s spin class evaluates1 on the fibre class z. The quadratic lift of an embedded circle is its tangential lift plus z, so q is not the raw spin-class evaluation on the tangent lift. The additional z makes the bounding-disc circle have q=0 and the Lie circle q=1. Theorem1B produces the intersection term; Theorem3A gives the affine bijection. The receiving closed oriented torus and mod-two coefficients satisfy all hypotheses.',
        'The complete nine-page original was read in extracted text, with the operative p.371 equations and proofs visually checked. No appeal to the analytic theta-parity theorem is required.',
        author='Dennis Johnson', title='Spin structures and quadratic forms on surfaces',
        journal='Journal of the London Mathematical Society', series='2', volume='22', issue='2',
        year=1980, pages='365–373', doi='10.1112/jlms/s2-22.2.365',
        visual_evidence=[CACHE+'views/Johnson1980_7.png'],
    ),
    source(
        'DebrayGunningham2018Root', 'DebrayGunningham2018.pdf',
        'https://adebray.github.io/papers/arf_brown.pdf',
        ['h24:retbib:DebrayGunningham', 'DebrayGunningham2018'],
        ['Author version arXiv1803.11183v1 dated29March2018, §3.1.1 p.6, complete text and original page visually opened.',
         'Equation(3.1), Theorem3.2, Remark3.3, Definition3.4/equation(3.5), Theorem3.6/equation(3.7), and Example3.8.'],
        'Modern statement of spin/quadratic correspondence and Arf bordism invariance; exact existing Lie-framed-torus calculation requiring explicit credit.',
        'The source assumes a closed oriented surface. Remark3.3 uses bounding=0 and nonbounding=1. Theorem3.6 gives Arf:Omega_2^Spin→Z/2. Example3.8 explicitly has q(e)=q(f)=1 for the Lie-framed torus. Forgetting a framed bordism yields a spin bordism; only that implication is needed for the obstruction. No general injectivity of framed-to-spin bordism is assumed.',
        'The exact expository theorem statements and example were opened. Their original attributions to Johnson/Atiyah and Kirby–Taylor are retained; the manuscript supplies its own handle proof of the needed bordism invariance. Proposition5.1 and pin-minus TQFT claims are not operative here and were not certified.',
        author='Arun Debray and Sam Gunningham', title='The Arf–Brown TQFT of Pin-minus surfaces',
        year=2018, arxiv='1803.11183v1', edition_opened='Author preprint,29March2018; source-page locators refer to this edition.',
        known_source_credit='The intrinsic Lie-torus Arf calculation is already Example3.8. The manuscript’s separately checked actual-inverse-image framing comparison is additional.',
        visual_evidence=[CACHE+'views/DebrayGunningham2018_6.png'],
    ),
]

# Preserve the earlier agent’s exact scopes when extending a shared key. They
# remain attributed to that agent; they are not represented as new personal reads.
prior = json.loads((ROOT/'deliverables/work/maps_audit/references_verified.json').read_text())
hatcher = copy.deepcopy(next(r for r in prior if r.get('key') == 'Hatcher2002'))
hatcher['citation_key'] = 'Hatcher2002'
hatcher.setdefault('aliases', []).append('h24:retbib:Hatcher')
hatcher['preserved_prior_record'] = 'deliverables/work/maps_audit/references_verified.json#Hatcher2002'
hatcher.setdefault('additional_dated_checks', []).append({
    'reader': READER, 'agent': '/root/invariants_arithmetic', 'effort': 'Pro', 'date': DATE,
    'opened_locators': ['§4.2 pp.384–385, complete text; PDF393–394 both visually opened, including the bitmap stable-stem table and eta/eta-squared diagram.'],
    'verification_scope': 'The second stable stem in the p.384 table is Z/2. The stabilization range is pi_i^S=pi_(i+n)(S^n) for n>i+1, hence n=4,i=2 applies to S6→S4. The p.385 diagram and its explanation identify eta as the stable complex Hopf class and eta-squared as the nonzero second-stem element. Proposition4.56 states the composition product; the receiving proof independently checks the product tubular collapse.',
    'edition_opened': 'Current author-hosted Algebraic Topology PDF, a revised electronic edition of the 2002 book; the text following the stable-stem diagrams credits Isaksen2014. No claim that this is an unchanged 2002 print scan.',
    'source': 'sources/external/maps_audit/hatcher.pdf',
    'sha256': digest('sources/external/maps_audit/hatcher.pdf'),
    'visual_evidence': [CACHE+'views/Hatcher_393.png', CACHE+'views/Hatcher_394.png'],
})
rows.append(hatcher)

milnor = copy.deepcopy(next(r for r in prior if r.get('key') == 'CuspNullMilnor1965'))
milnor['citation_key'] = 'CuspNullMilnor1965'
milnor.setdefault('aliases', []).append('h24:retbib:Milnor1965')
milnor['preserved_prior_record'] = 'deliverables/work/maps_audit/carrier_source_checks.json#CuspNullMilnor1965'
milnor['new_reading_claim'] = False
milnor['provenance_note'] = 'Alias registered from maps_audit’s explicit full §7 pp.42–50 reading; no additional personal opening is claimed here.'
rows.append(milnor)

(OUT/'retained_angle_references_verified.json').write_text(json.dumps(rows, indent=2, ensure_ascii=False)+'\n')
alias_map = {alias: r['citation_key'] for r in rows for alias in r.get('aliases', [])}
(OUT/'retained_angle_reference_aliases.json').write_text(json.dumps(alias_map, indent=2, ensure_ascii=False)+'\n')
insertions = [
    {'receiving_label': 'h24:ret:eq:quadratic', 'action': 'Use exact original surface locator.',
     'tex': r'The original surface construction and its naturality are Johnson’s Theorems~1A--1C and~3A--3B \cite[pp.~366--371]{Johnson1980Root}; his corrected tangent lift gives the bounding-zero convention used here.'},
    {'receiving_label': 'h24:ret:eq:actual-Arf', 'action': 'Credit the existing intrinsic Lie-torus computation; retain the complete direct computation and actual frame comparison.',
     'tex': r'The intrinsic Lie-framed-torus calculation below is already \cite[Example~3.8]{DebrayGunningham2018Root}. The preceding comparison identifies the specific differential framing of the actual inverse image with this Lie framing.'},
    {'receiving_label': 'h24:ret:eq:actual-Arf', 'action': 'Precise classical stable-group locators in the following paragraph.',
     'tex': r'The classical group calculation is \cite[pp.~957--959]{Pontryagin1950Root}, expanded in \cite[\S15, Theorem~24, pp.~109--112 of the English translation]{Pontryagin1955Root}; see also \cite[pp.~384--385]{Hatcher2002}.'},
    {'receiving_label': 'paragraph on the Hopf inverse-image framing', 'action': 'Narrow the classical circle reference to the actually opened theorem.',
     'tex': r'The framed-circle parity and its relation to the stable Hopf generator are \cite[\S14, Theorems~20--21, pp.~96--101 of the English translation]{Pontryagin1955Root}.'},
]
(OUT/'retained_angle_credit_insertions.json').write_text(json.dumps(insertions, indent=2, ensure_ascii=False)+'\n')
(OUT/'retained_angle_credit_insertions.tex').write_text('\n\n'.join('% '+r['action']+'\n'+r['tex'] for r in insertions)+'\n')
summary = {
    'date': DATE, 'checker': READER, 'effort': 'Pro',
    'new_exact_keys': [r['citation_key'] for r in rows[:4]],
    'extended_shared_key': 'Hatcher2002',
    'preserved_existing_key_alias': 'CuspNullMilnor1965',
    'operative_source_gaps': [],
    'bounded_access_limitations': ['Rochester’s Pontryagin1959 translation scan lacks pp.88–89; no complete §13 or Lemma1 proof opening is asserted. §§14–15, the actual cited operative scopes, are present and read.'],
    'mathematical_correction_needed': False,
    'credit_correction': 'Add explicit Debray–Gunningham Example3.8 credit for the intrinsic Lie-torus calculation; keep the distinct actual inverse-image/framing comparison and full direct proof.',
    'files': ['retained_angle_references_verified.json', 'retained_angle_checked_references.bib', 'retained_angle_reference_aliases.json', 'retained_angle_credit_insertions.json', 'retained_angle_credit_insertions.tex'],
}
(OUT/'retained_angle_source_closure_summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False)+'\n')
print(json.dumps({'records': len(rows), 'aliases': len(alias_map), 'operative_source_gaps': 0}))
