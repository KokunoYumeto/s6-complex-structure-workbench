"""Record completed primary readings and searches, without refreshing the inventory.

Only locators, hashes and our own descriptions are written. Published-source
bytes and text are neither copied nor incorporated into these records.
"""
from S6_SERIES_PUBLISH_c4_edit import *
import hashlib

NOW = datetime.now(timezone.utc).isoformat()
BASE = ROOT.parent / 'S6_GRIND_6_literature'
fields = ['source', 'url', 'version', 'locus', 'date_utc', 'sha256',
          'own_word_summary', 'use']
rows = []


def reading(key, relative, url, version, locus, summary, use):
    path = BASE / relative
    rows.append(dict(source=key, url=url, version=version, locus=locus,
        date_utc=NOW, sha256='Attached source: ' + hashlib.sha256(path.read_bytes()).hexdigest(),
        own_word_summary=summary, use=use))


reading('II-C4-CDP98', 'papers/arXiv_math_9607215_CDP98_src/main.tex',
    'https://arxiv.org/abs/math/9607215', 'Attached arXiv source; published locators retained',
    'Proposition 1.1 and complete proof; Lemma 1.5 and complete proof; source lines 235–320, published pp.78–80',
    'The divisor-twisting assertion permits nonreduced spaces and requires the divisor to meet every irreducible component. The direct-image lemma asserts local freeness in every degree for every locally free sheaf on the stated compact threefold.',
    'Read against complete current E12, E17 and P267. P267 has the square-zero algebra O(P1) plus C_p, with D=q distinct from p. The direct module decomposition O_Z(-kD)=O_P1(-kq) plus C_p retains a section for every k, while meeting the single irreducible component. E12 uses the moving degree-one section evaluation with simple zero to obtain Rp_*P=C_0[-1], then the P1 factor gives Rg_*V=C_0[-2]. These are the exact two counterexamples; merely choosing an irreducible component disjoint from D would violate the source hypothesis.')
reading('II-C4-CDP20', 'papers/arXiv_1904.11179v2_CDP20_corrigendum_src/main.tex',
    'https://arxiv.org/abs/1904.11179v2', 'arXiv version 2; published locators retained',
    'Theorem 2.2; section 7 opening conormal reduction and complete Proposition 7.3 proof; source lines 304–319, 968–1129; published pp.680,692–695',
    'The global tangent-vanishing assertion uses integral ambient H1 and H2, algebraic dimension one and a holomorphic reduction. The section-7 step passes from restricted ambient cotangents to the intrinsic torsion-free quotient. The later proposition proves a vanishing for that quotient.',
    'A retains the inverse image K of cotangent torsion and its connecting map. Its exact sequences make the ambient section space the connecting-map kernel under the two endpoint vanishings. The claim being corrected is the unrestricted ambient/global inference, with the intrinsic quotient argument separately credited. This is exposed source and statement comparison; no independent proof credit.')
reading('II-C4-ENGEL-EULER', 'papers/arXiv_2609.38442_Engel_src/S6.tex',
    'https://arxiv.org/abs/2609.38442v1', 'arXiv version 1',
    'Proposition 7.1 and complete proof, preprint p.17; source lines 1263–1283',
    'Euler localization leaves the toric special fibre. Its two point strata contribute two; each positive-dimensional stratum has a multiplicative-group factor and contributes zero.',
    'The same reduced-support stratification gives the standard-family value e=2 in C. This compares the identical central support and Euler-additivity map; no absence-of-prior-work inference is made.')
reading('II-C4-COMBS-QUESTIONS', 'papers/arXiv_2610.10451_Viaclovsky_combs_src/Viaclovsky_Comb_S6_Draft_October_7_2026.tex',
    'https://arxiv.org/abs/2610.10451v1', 'arXiv version 1, 7 October 2026',
    'Section 10(1)–(2), preprint p.33; attached source lines 2680–2725',
    'The questions concern the complete Kuranishi germ and persistence of the fibration, and the Hodge diamond across comb sizes and members.',
    'F states the full comb germ of dimension 8m+1. Its Hodge pair (49,48) is confined to the nonempty open twelve-tooth family with kernel O(-8) plus O(-9)^2. The general and special-member splitting questions remain explicit in the final problem. Current arXiv metadata was opened online; the precise questions were read in the attached source.')
reading('II-C4-LOG-QUESTIONS', 'papers/arXiv_2610.39102_Viaclovsky_log_transformations_src/Logarithmic_S6_October_28_2026_Final.tex',
    'https://arxiv.org/abs/2610.39102v1', 'arXiv version 1, submitted 29 October 2026',
    'Theorem 1.1 and Section 1.1(1), preprint pp.1–2; source lines 214–247',
    'The construction specifies coprime ordered multiplicities (3k,4l) and asks whether the corresponding structures have different deformation classes.',
    'F keeps this same ordered pair. Its propagation maps preserve the two multiple-fibre divisors throughout the stated connected reduced bases and finite chains; the fixed-pair converse is the connected period and attachment family. Current metadata and the exact attached theorem/question were opened.')
reading('II-C4-LR-MARKING', 'papers/arXiv_2609.33826_Liu_Rollenske_src/S6_arxiv.tex',
    'https://arxiv.org/abs/2609.33826v2', 'arXiv version 2',
    'Equation (2.3), p.4; Lemma 2.7 and Corollary 2.8, pp.6–7; Proposition 3.6 and Definition 3.7, pp.9–10; attached source lines 483–564,725–758,829–846',
    'The good-root construction gives the displayed rank-four lattice and translated fourth-root action; the scalar determines the logarithmic period.',
    'G fixes the scalar and root-line character. Projection onto the second coordinate gives the Albanese lattice; multiplication by two gives modulus tau/2+2kappa. A scalar turn adds one-half and two turns add one. The manuscript must also retain its source-line and cap gluing maps; the lattice calculation alone is not credited as the entire descent proof. Fresh binary-access hash is separately in c4_source_access.tsv.')
reading('II-C4-DGKX-V1-TANGENT', 'papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex',
    'https://arxiv.org/abs/2610.00250v1', 'arXiv version 1; current version 2 metadata opened separately',
    'Lemma 6.11 and Theorem 6.12, full displayed sequence and proof, pp.81–82; attached source lines 9374–9508',
    'The logarithmic-to-ordinary tangent sequence has a normalization-supported correction, and the untwisted tangent tuple is (1,1,1,0).',
    'At n=0 the formulas of E give the identical tuple, and that assertion remains credited to version 1. Current version 2 has a changed title and shorter Oka-geometric scope; the cited theorem is kept at its recorded version and pages. Reading was after exposure; no independent proof event.')
reading('II-C4-AC26-LOCATORS', 'original/AC26_original_manuscript.pdf',
    'https://alpo.ge/s6.pdf', 'Attached 108-page version; current primary PDF opened through web retrieval',
    'Fresh online reading: Theorem 7.22 and complete proof, p.60; Lemma 10.3, Theorem 10.5, Corollary 10.6, Sections 10.4–10.5, pp.87–91',
    'The standard-family Euler number is two. The conductor calculation gives tangent nonvanishing; the conormal discussion retains the torsion obstruction. The component-count correction uses fibre homology coinvariants.',
    'A and E retain the same ambient-to-normalization restriction; B uses the same abelianization onto coinvariants; C specializes to the identical toric support. The displayed hash identifies the attached bytes only: this continuation opened the current web PDF but its independent binary download returned HTTP 403, so no new binary identity is asserted.')
write_tsv(ROOT / 'S6_SERIES_PUBLISH_c4_primary_readings.tsv', fields, rows)

queries = [
 ('A/B/E', '"complex six-spheres" Campana Demailly Peternell normalization cotangent', 'recency 30 days', 'Primary CDP and recent six-sphere sources compared at exact loci.'),
 ('F', '"complex six-spheres" Viaclovsky combs logarithmic transformations deformation', 'recency 30 days', 'Combs and logarithmic-transformation constructions and questions located.'),
 ('G', '"complex six-spheres" Liu Rollenske scalar covering', 'recency 30 days', 'Liu–Rollenske fixed scalar/root construction located.'),
 ('F', '"Combs and complex structures on the six-sphere" Viaclovsky', 'arxiv.org; recency 60 days', 'arXiv version and date checked; exact question read in the attached source.'),
 ('F', '"Logarithmic transformations on the six-sphere"', 'arxiv.org; recency 60 days', 'arXiv metadata and precise ordered-multiplicity question compared.'),
 ('G', '"Liu" "Rollenske" "six-sphere"', 'arxiv.org; recency 60 days', 'Version 2 scalar, lattice and root data compared.'),
 ('C', '"complex six-sphere" "Euler" "torus"', 'arxiv.org, alpo.ge; recency 60 days', 'AC26, Engel and Yang examples identified; their specializations are recorded, with no novelty inference from search absence.'),
 ('B/C', '"complex" "threefolds" "b_1=b_2=0" "Euler" torus sign', 'recency 60 days', 'Search retained as discovery; current unrestricted theorem still requires the manuscript proof.'),
 ('D', 'torus degeneration "Euler" "parity" complex two tori', 'recency 60 days', 'Local-parity search; the known semistable subclass is compared through the same proper family and reduced support.'),
 ('A', '"complex six-sphere" "normalization" "cotangent" vanishing', 'recency 60 days', 'Normalization and cotangent sources compared at their stated hypotheses.'),
 ('E', '"complex six-spheres" "tangent cohomology" "twist"', 'recency 60 days', 'Untwisted DGKX v1 value retained with exact version; no universal priority claim inferred.')
]
search_fields = ['date_utc','engine','main_theorems','query','recency_days_and_domain','use']
write_tsv(ROOT / 'S6_SERIES_PUBLISH_c4_literature_searches.tsv', search_fields, [
    dict(date_utc='2026-11-23; searches performed in this continuation before this record',
         engine='system1_search_query',main_theorems=t,query=q,
         recency_days_and_domain=d,use=u+' Merge into final inventory when text is final.')
    for t,q,d,u in queries])

# Clarify the concrete embedded-point counterexample in the live claim record.
path = ROOT / 'S6_SERIES_PUBLISH_provenance_checks.tsv'
f, claims = read_tsv(path)
claim = next(r for r in claims if r['claim_id']=='II-C3-LIT-A2')
claim['current_resolution'] = (
    'For E12 the evaluation map O_A(-0) to O_A has one simple zero, giving Rp_*P=C_0[-1]; tensoring with RΓ(P1,O(-2)) gives Rg_*V=C_0[-2]. '
    'For divisor twisting the concrete counterexample is P267: O_Z=O_P1 plus the square-zero embedded module C_p, and D=q with p distinct from q. '
    'D meets the sole irreducible component and is Cartier, but O_Z(-kD)=O_P1(-kq) plus C_p keeps a section for every positive k. '
    'Thus the source hypothesis is met; the surviving support is the embedded associated point. E17 proves the associated-support criterion in A. '
    'Fourth-continuation root read the two full source assertions/proofs and all three current receiving proofs; no new independent re-derivation is claimed.')
claim['evidence'] += '; S6_SERIES_PUBLISH_c4_primary_readings.tsv: II-C4-CDP98'
write_tsv(path, f, claims)
for label,event,outcome in [
    ('cdp:st:E12','II-C4-READ-E12','Complete current proof and CDP98 Lemma 1.5 read. Evaluation has a simple zero along the diagonal, so the displayed derived-image and fibre-cohomology calculations give the exact counterexample under the source hypotheses.'),
    ('cdp:st:E17','II-C4-READ-E17','Complete current proof read. Krull intersection identifies precisely the sections supported away from D; the no-embedded-component hypothesis then gives vanishing. The graph fibre and the Cartier equation have identical local analytic rings.'),
    ('ex:II:embedded-point-divisor-twist','II-C4-READ-P267','Complete current proof and CDP98 Proposition 1.1 read. The square-zero point module is embedded, D meets the only irreducible component, and the split O_P1-module calculation gives every stated cohomology dimension. The live provenance record now names this precise counterexample.')
]:
    add_event(label,event,'used and rechecked in this run',outcome,
              'S6_SERIES_PUBLISH_II.tex; S6_SERIES_PUBLISH_c4_primary_readings.tsv',
              source='code/S6_SERIES_PUBLISH_c4_literature_records.py')
print('Primary reading rows:',len(rows))
print('Recorded discovery searches:',len(queries))
print('Live A2 provenance map clarified against P267; manuscript unchanged.')
print('Exposed-reading events: 3; no independent or required-check credit.')
print('Inventory and final derived counts not refreshed.')
