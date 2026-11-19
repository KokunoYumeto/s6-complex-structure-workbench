"""Record observed source passages and reconcile bibliography aliases.

This file records source reading only.  It confers no receiving-proof credit.
"""
from pathlib import Path
import json, re

B = Path(__file__).resolve().parents[2]
P = B / 'analysis/III_references_opened.json'
rows = json.loads(P.read_text())
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro)'

def add(key, path, locator, scope, refs, **extra):
    value = dict(key=key, date='2026-11-18', who=who,
                 status='verified in the stated scope', url_or_path=path,
                 locator=locator, scope=scope, retrieval_reference=refs, **extra)
    if not any(x['key'] == key and x['locator'] == locator for x in rows):
        rows.append(value)

add('Pontryagin1950Root',
    'analysis/III_sources/Pontryagin1950.pdf; https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/pont3.pdf',
    'Original Russian paper, printed pp. 957–959, theorem and its framed-surface proof',
    'Original scanned pages visually read. The quadratic intersection correction, bordism invariant and explicitly rotated torus prove the two-element stable second stem. The appended review was not used as the operative source.',
    'Local original-page images Pontryagin1950_pdf1.png and Pontryagin1950_pdf2.png; turn693142625view1')
add('Pontryagin1955Root',
    'analysis/III_sources/Pontryagin1955.pdf; https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/pont4.pdf',
    'English translation: Theorems 20–21 and full proofs, pp. 96–101; Theorem 24 and full proof, pp. 109–112',
    'Original translation scans visually read: the framed-circle invariant, twisted-frame generator and suspension; the framed-surface Arf invariant, bordism handle calculation, and rotated torus generator. Intermediate pages 104–105 and 108 were also read, but a complete separate reading of Theorems 22–23 is not claimed.',
    'Local images Pontryagin1955_pdf47.png, pdf48.png, pdf49.png, pdf51.png, pdf53.png, pdf54.png, pdf55.png; turn332717469view1')
add('manReiser24',
    'analysis/III_sources/Reiser2024.pdf; https://arxiv.org/pdf/2401.06587',
    'Version 3, section 4.3, pp. 17–19, including the discussion immediately before Remark 4.7',
    'The spin five-manifold N_k, twisted suspension and homology, Zhubr quadruple, explicit plumbing W_k and the map x to (x,0) establishing zero cubic and refined Pontryagin invariant. Pagination refers to the opened preprint, not an inferred journal location.',
    'turn757100629view0;turn344863154view0;turn344863154view1;turn396953739view0')
add('manExplorer26',
    'https://philip-engel.github.io/threefold-explorer/docs/',
    'Primary documentation, rational elliptic configurations, local models and computation sections',
    'Documentation identity and the stated finite configuration/model counts, matrix/Mayer–Vietoris method and explicit warning that detailed local-model derivations are not published. This is not a new remote API run or geometric validation. The receiving fifty-reply archive audit retains its bounded scope.',
    'turn332717469view3;turn683251287view0;turn683251287view1')
add('mapsMilne2017',
    'https://www.jmilne.org/math/CourseNotes/MF.pdf',
    'Proposition 2.16 and proof pp. 34–35; Proposition 4.3 and Remark 4.4 p. 49',
    'Finite-index coset fundamental-domain map and the normalization of the modular J and j coordinates used in the explicit collision construction; complements the already opened compactification and cusp-coordinate results.',
    'turn922136592view1;turn922136592view0;turn396866187view1')
add('manViaclovskyLogs26',
    'sources/papers/arXiv_2610.39102_Viaclovsky_log_transformations_src/Logarithmic_S6_October_28_2026_Final.tex',
    'Lemma 2.1, label mono, lines 288–315; invariant covectors/forms and the finite-filling setup, lines 316–390',
    'Full determinant-one change of basis and its three displayed monodromy matrices, primitive invariant circle/covector and exact filling coordinates. This extends the prior equations (2.11)–(2.12) and logarithmic-clutch reading.',
    'Local attached primary TeX, observed ranges 280–390')
add('manViaclovskyTwo26',
    'sources/papers/arXiv_2609.33785_Viaclovsky_two_parameter_src/Viaclovsky_S6_September_26_2026.tex',
    'Proposition 5.4, label d2, and full proof, lines 1264–1309; preceding Leray and primitive-pairing setup, lines 1220–1263',
    'The integral primitive differential d2(4 psi)=omega and the four multiplicative differentials, using the actual clutch calculation and the alternative torsion-free H2 argument.',
    'Local attached primary TeX, observed range 1220–1315')
add('manLR26',
    'sources/papers/arXiv_2609.33826_Liu_Rollenske_src/S6_arxiv.tex',
    'Proposition labelled prop: global monodromy and Corollary labelled cor: local invariants common basis, lines 1116–1285; Proposition labelled prop: Leray differentials and proof, lines 1568–1676',
    'Full common marking, centralizer and simultaneous integral basis maps, and the primitive meridian/Leray calculation. The source line assigning the Mayer–Vietoris image to H1(P1,Z) is a target-degree typo: its displayed connecting map has target H2(P1,Z), which is the receiving proof target. No external source text was altered.',
    'Local attached primary TeX, observed ranges 1112–1285 and 1559–1676')
add('manEngel26',
    'sources/papers/arXiv_2609.38442_Engel_src/S6.tex',
    'Remark 8.3, rank-three real-torus quotient and hexagon/coarse-circle argument, lines 1684–1735',
    'The exact proposed quotient extension was read. Paper III retains the literal-character obstruction and constructs its corrected map; this source reading does not endorse the rejected unmodified global quotient claim.',
    'Local attached primary TeX, observed ranges 1670–1698 and 1695–1735')

aliases = {'AC26':'mapsAC26', 'BHS19':'manBHS19', 'manCDP98':'CDP1998',
           'mapsViaLog':'manViaclovskyLogs26', 'mapsVia2':'manViaclovskyTwo26',
           'mapsLR':'manLR26', 'mapsEngel':'manEngel26'}
for alias, canonical in aliases.items():
    for source in [x for x in rows if x['key'] == canonical]:
        copy = dict(source, key=alias, alias_of=canonical,
                    reading_event_kind='bibliographic alias of the same observed source passage',
                    additional_independent_reading_credit=False)
        if not any(x['key'] == alias and x['locator'] == copy['locator'] for x in rows):
            rows.append(copy)
P.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + '\n')
texts = '\n'.join(p.read_text() for p in (B/'papers/III').glob('*.tex'))
keys = set()
for found in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', texts):
    keys.update(found.split(','))
known = {x['key'] for x in rows}
report = dict(cited_keys=sorted(keys), current_scoped_records=len(rows),
              missing_cited_keys=sorted(keys-known), alias_map=aliases,
              scope='Coverage means an observed bounded passage is recorded for each citation key. It is not a claim that every work or every external proof was read in full, or a new independent receiving-proof check.')
(B/'analysis/III_citation_scope_reconciliation.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
