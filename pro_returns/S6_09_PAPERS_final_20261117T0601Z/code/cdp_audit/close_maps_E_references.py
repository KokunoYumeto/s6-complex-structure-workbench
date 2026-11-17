"""Persist the exact primary-source scopes actually opened for MAPS E."""
import hashlib
import json
from pathlib import Path

ROOT = Path('/workspace/scratch/037cd144174c')
OUT = ROOT / 'deliverables/work/cdp_audit/maps_E'
path = OUT / 'references_verified.json'
rows = json.loads(path.read_text())
downloads = {r['key']: r for r in json.loads((ROOT / 'reference_downloads/maps_E/download_manifest.json').read_text())}
meta = {'model': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode)', 'effort': 'Pro', 'date': '2026-11-17', 'timezone': 'UTC', 'reader': '/root/cdp_audit'}

def add(key, download, title, aliases, locator, uses, verification, web_refs=(), visual=(), restrictions=()):
    d = downloads[download]
    row = {'key': key, 'aliases': aliases, 'title': title, 'url': d['url'],
           'status': 'verified in the specified scope', 'locator': locator,
           'uses': uses, 'verification': verification, 'web_refs': list(web_refs),
           'visual_pages': list(visual), 'not_verified': list(restrictions),
           'reader': meta, 'local_pdf': str(Path(d['path']).relative_to(ROOT)) if Path(d['path']).is_absolute() else d['path'],
           'sha256': d['sha256']}
    rows[:] = [r for r in rows if r['key'] != key] + [row]

add('rootScott83', 'Scott1983', 'The geometries of 3-manifolds', ['Scott1983'],
    'Bull. London Math. Soc. 15 (1983), pp.424–428, Theorems 2.3–2.5 and orbifold Euler-characteristic discussion; pp.434–436, circle Euler convention, Lemma 3.5 and Theorem 3.6.',
    ['MAPS E2.3/E2.9 good hyperbolic orbifold cover and asphericity', 'MAPS E2.13 surface cover and Euler number'],
    'Read the bad-orbifold proof and finite-surface-cover explanation, the stated uniformization theorem, the orbifold Riemann–Hurwitz derivation, and the full good-base covering calculation. S2(3,4,3,4) is good with Euler characteristic -5/6; its degree-12 torsion-free cover has genus 6. For the principal circle subgroup the fibre degree is one, and Theorem 3.6 multiplies Euler number by the base degree. The negative Euler sign convention was matched to the independently computed connection orientation.',
    ['turn302view0', 'turn303view0', 'turn305view4', 'turn306view2'],
    restrictions=['The proof of uniformization imported by Scott from Thurston is not re-proved here.', 'The source E2.9 Euler discussion must be cited in Section 3, not Section 2.'])

add('rootDavisKirk01', 'DavisKirk2001', 'Lecture Notes in Algebraic Topology', ['DavisKirk2001'],
    'Graduate Studies in Mathematics 35 (2001), pp.206–210: Theorem 8.13, Corollary 8.15, Definition 8.16, Theorem 8.17 and the complete supplied proof outline; stable-stem table p.208.',
    ['MAPS E2.9 framed bordism of maps and Pontryagin–Thom product calculation'],
    'Read the stable tangent/normal equivalence proof and the exact definition of framed bordism over X. Theorem 8.17 identifies this group with stable homotopy of X with a disjoint basepoint, with the stated collapse/transversality construction. This is the precise form used for the two sphere splittings and the relative inverse image of the embedded target.',
    ['turn302view1'],
    restrictions=['Theorem 8.17 supplies an outline rather than a complete independent proof of every Pontryagin–Thom construction; the record describes exactly that scope.'])

add('rootHirsch76', 'Hirsch1976', 'Differential Topology', ['Hirsch1976'],
    'Graduate Texts in Mathematics 33 (1976), Chapter 3, Section 2: pp.74–78, Theorems 2.1, 2.2, 2.5, Lemma 2.3, and their supplied proofs.',
    ['MAPS E2.8 relative perturbation at three critical values', 'MAPS E2.9 relative transverse inverse image'],
    'Visually read the original scan, including the localized perturbation with a smooth cutoff and the finite-family transversality theorem. The receiving construction is already transverse on a boundary collar. Its perturbation is supported in an interior compact set, so the collar is fixed by the same cutoff argument. The relative form is derived from the opened proof; it is not falsely quoted as the literal wording of Theorem 2.5.',
    ['turn297view0'],
    ['reference_downloads/maps_E/visual/Hirsch-044.png', 'reference_downloads/maps_E/visual/Hirsch-045.png', 'reference_downloads/maps_E/visual/Hirsch-046.png'])

add('mapsWhitehead50', 'Whitehead1950', 'A certain exact sequence', ['Whitehead1950'],
    'Proc. Natl. Acad. Sci. USA 36 (1950), pp.55–58: Theorem 1 and naturality, Section 2 quadratic relations and weak direct sums, Theorem 5.',
    ['MAPS E2.18 natural quadratic exact sequence and direct-sum mixed component'],
    'Read the exact sequence, functorial construction, infinite-complex scope, quadratic relations and direct-sum decomposition. Visually checked Theorem 5 on p.58 against OCR. These apply to the simply connected universal covers, including their infinite CW structures, and make the deck action and inclusion maps natural. The receiving proof computes the actual attaching quadratic image and does not infer a full higher homotopy classification from the theorem.',
    ['turn303view1', 'turn306view0', 'turn305view2'],
    ['reference_downloads/maps_E/visual/Whitehead-4.png'],
    ['This six-page announcement does not contain full proofs of all its exact-sequence theorems; no such reading is claimed.'])

add('mapsVogel09', 'Vogel2009', 'Existence of Engel structures', ['Vogel2009'],
    'Annals of Mathematics 169 (2009), Section 4.1: Definition 4.1 p.102, equation (16) and its following handle decomposition p.103.',
    ['MAPS E2.21 ordinary handles from the two-semicircle decomposition'],
    'Read the literal product description and its decomposition into handles of consecutive indices. The receiving proof uses only this elementary local decomposition and supplies its own full coordinate attaching maps, endpoint normal discs and relative smooth comparison.',
    ['turn303view2', 'turn306view1', 'turn305view3'],
    restrictions=['Neither the Engel existence theorem nor the Asimov round-handle existence theorem is an imported premise.'])

add('mapsWinter08', 'Winter2008', 'The classification of spun torus knots', ['Winter2008'],
    'arXiv:0711.1638v3 (7 August 2008), Section 3 p.4, ordinary-spin paragraph before Theorem 3.4 and its proof; Sections 4–4.1 pp.7–10, peripheral definitions, Theorem 4.5 and full proof, following longitude qualification.',
    ['MAPS E2.10 ordinary-spin convention and original peripheral subgroup'],
    'Opened the directly downloaded original v3 PDF and read its extracted text. The definitions fix which spun knot is meant and the peripheral calculation retains the zero-linking longitude. The source theorem applies to the first ordinary spin. The receiving proof independently gives the general T3 single-spin Mayer–Vietoris argument and does not extend the source theorem by assertion.',
    restrictions=['The internal PDF header has a later generation date; the archived version is explicitly v3 dated 7 August 2008.', 'No general classification of the receiving six-dimensional complement is imported.'])

add('mapsMilnor65', 'Milnor1965', 'Lectures on the h-Cobordism Theorem', ['Milnor1965'],
    'Princeton Mathematical Notes 1 (1965): Theorem 1.4 p.2 and proof pp.25–26; Definitions 3.9/3.11 pp.28–30, Theorems 3.12–3.13 pp.30–32; cutoff vector-field extension pp.62–63 and Theorem 5.8 pp.63–64.',
    ['MAPS E2.21 full characteristic embeddings, gluing and relative isotopy extension'],
    'Read the complete supplied gluing and elementary-cobordism proofs and the stated isotopy-extension theorem. Visually checked the exact theorem and proof pages. Characteristic embeddings include the open normal disc, so the receiving argument preserves the attaching framing rather than only its core sphere. For its relative isotopies, the velocity field is extended on a neighbourhood and multiplied by a cutoff away from fixed faces; its compactly supported flow preserves those faces. The original Theorem 5.8 is stated for an ambient manifold without boundary, as is the relevant smooth ambient boundary before attaching the next handle.',
    ['turn311view0', 'turn311view2', 'turn313view0', 'turn313view1', 'turn313view2', 'turn321view0'],
    ['reference_downloads/maps_E/visual/Milnor-008.png', 'reference_downloads/maps_E/visual/Milnor-032.png', 'reference_downloads/maps_E/visual/Milnor-037.png', 'reference_downloads/maps_E/visual/Milnor-038.png', 'reference_downloads/maps_E/visual/Milnor-069.png', 'reference_downloads/maps_E/visual/Milnor-070.png'],
    ['Milnor refers to Munkres for the collar-uniqueness input and elsewhere for a full general isotopy-extension proof; these underlying sources were not opened in this event.', 'No h-cobordism classification theorem is used.'])

for row in rows:
    if row['key'] == 'ffPetersSterk':
        d = downloads['PetersSterk2024']
        row['local_pdf'] = str(Path(d['path']).relative_to(ROOT))
        row['sha256'] = d['sha256']
        row['verification'] = row['verification'].replace(' Author PDF download was incomplete; the exact primary PDF pages were opened through the web tool.', ' The initial download was incomplete; a subsequent retry retained the complete original PDF with the recorded hash.')

iwx_path = ROOT / 'sources/external/maps_audit/isaksen_wang_xu2023.pdf'
iwx = {'key': 'IsaksenWangXu2023', 'aliases': [],
       'title': 'Stable homotopy groups of spheres: from dimension 0 to 90',
       'url': 'https://www.numdam.org/item/10.1007/s10240-023-00139-1.pdf',
       'status': 'verified in the specified scope',
       'locator': 'Publications mathématiques de l’IHÉS 137 (2023), pp.112–113, Corollary 1.3, the table convention, and Table 1 rows 3, 4 and 6.',
       'uses': ['MAPS E2.9 the vanishing of the fourth stable stem'],
       'verification': 'Opened the primary published PDF and visually read Table 1. Each of the three stable-homotopy columns in row 4 is trivial. The table convention was read explicitly, distinguishing its three stable-homotopy columns from the final smooth-structure column. Only these low-stem values are imported; no independent audit of the full high-stem computation is claimed.',
       'not_verified': ['This record does not verify the different 2020 version or its Theorem 2.1. The manuscript citation must name the 2023 edition explicitly.'],
       'web_refs': ['turn322view0', 'turn323view0'],
       'visual_pages': ['reference_downloads/maps_E/visual/IWX2023-p113.png'],
       'local_pdf': str(iwx_path.relative_to(ROOT)), 'sha256': hashlib.sha256(iwx_path.read_bytes()).hexdigest(), 'reader': meta}
rows[:] = [r for r in rows if r['key'] != iwx['key']] + [iwx]
path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
print('Saved', len(rows), 'exact primary-source scope records.')
