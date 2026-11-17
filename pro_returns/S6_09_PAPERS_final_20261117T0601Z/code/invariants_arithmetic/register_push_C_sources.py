#!/usr/bin/env python3
"""Register the actual 17-Nov-2026 original-source readings for PUSH C.

This script records human mathematical checks. It does not infer verification
from a bibliography entry, successful retrieval, text search, or another row.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'deliverables/work/invariants_arithmetic'
CACHE = 'sources/audit_cache/inv_ari/push_C_literature/'
MAPS = 'sources/external/maps_audit/'
SECTIONS = 'sources/returns/S6_02_PUSH/sections/'
READER = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode)'
DATE = '2026-11-17 UTC'


def record(key, local, url, locator, use, check, extent, contexts, **kw):
    row = dict(citation_key=key, status='verified_for_stated_use', verified=True,
               checker=READER, effort='Pro', date=DATE,
               local_source=local, source_sha256=hashlib.sha256((ROOT/local).read_bytes()).hexdigest(),
               url=url, opened_locator=locator, actual_use=use,
               hypotheses_and_normalization_check=check, extent=extent,
               receiving_contexts=[], historical_source_note_policy=
               'Earlier producing-session claims in source bibliography notes are retained as historical provenance only; this record certifies the independent readings stated here.')
    for filename, lines in contexts:
        path = SECTIONS + filename
        row['receiving_contexts'].append(dict(path=path, lines=lines,
            source_sha256=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()))
    row.update(kw)
    return row


rows = [
record('ChernSimons1974E', MAPS+'chern_simons.pdf',
 'https://math.mit.edu/juvitop/pastseminars/notes_2019_Fall/Chern-Simons.pdf',
 'Published original §3, Propositions 3.2 and 3.8, pp.52–54; text lines207–367 read, and all three original pages visually opened (PDF pages6–8). Intervening definitions and equations (3.6)–(3.7) were read.',
 'Normalized characteristic-form transgression used in the cubic relative-line calculation, PUSH C.3.20. The coefficient three is also expanded directly in the receiving proof.',
 'For an invariant polynomial P of degree l, TP(theta)=l integral_0^1 P(theta wedge phi_t^(l-1)) dt and dTP=P(Omega^l); the variation has l P(theta_prime wedge Omega^(l-1)) plus an exact term. Taking the normalized curvature of a complex line and l=3 gives the receiving coefficient. This does not determine the family gluing or its framing comparison.',
 'Operative definitions, statements and the displayed proofs on pp.52–54 opened. No claim to reprove every theorem of the article.',
 [('C_cubic_transgression.tex','136–140')],
 author='Shiing-Shen Chern and James Simons', title='Characteristic Forms and Geometric Invariants',
 year=1974, journal='Annals of Mathematics', volume='99', issue='1', pages='48–69', doi='10.2307/1971013',
 dependence='operative standard transgression; numerical coefficient independently expanded'),

record('CrowleyNordstrom2020', MAPS+'crowley_nordstrom2021_published.pdf',
 'https://link.springer.com/article/10.1007/s00208-020-02009-1',
 'Published 2021 edition, §2.1 Lemma2.1 and §2.2 equation(2.1), p.35 (PDF page7), visually opened in full; text lines310–402 read.',
 'The spin-c coboundary expression for the Eells–Kuiper invariant of the actual homotopy seven-sphere; used in PUSH C.2 and the direct eight-dimensional coboundary proof.',
 'Closed spin seven-manifold with torsion-free H4; spin-c eight-dimensional coboundary and relative lift of its determinant class. For a homotopy sphere H4=0, choose n=0 and d=0; the generalized invariant has target Z/28. Divide by28 and substitute p-hat=(p1+z^2)/2. Independent expansion gives (p1^2−4 sigma)/896 − p1 z^2/192 + z^4/384 in Q/Z. The relative lift, boundary orientation and fixed determinant conventions remain requirements of the receiving cap proof.',
 'Exact published lemma, formula and normalization opened. The parent separately checks construction of the required coboundary. This does not certify unrelated G2 or diffeomorphism-classification results.',
 [('C_push.tex','184–189'),('C_actual_eight_coboundary.tex','185–191')],
 author='Diarmuid Crowley and Johannes Nordström', title='Exotic G2-manifolds', year=2021,
 journal='Mathematische Annalen', volume='381', issue='1–2', pages='29–74', doi='10.1007/s00208-020-02009-1',
 version_note='Historical key2020 refers to online publication in2020; the issue and opened published original are2021. The arXiv1411.0656v4 version is not silently substituted for the published pagination.',
 independently_matching_record='deliverables/work/maps_audit/remaining_primary_source_checks.json: mapsCrowleyNordstrom21',
 dependence='operative normalized formula; receiving coboundary separately checked'),

record('Davis1982D', MAPS+'davis.pdf',
 'https://people.math.osu.edu/davis.12/old_papers/AJM-82.pdf',
 'Published original §7, pp.87–89, text lines1340–1450; Example7.14, Proposition7.15 and Corollary7.16, p.89 (PDF page32), visually opened.',
 'Comparison of the integer orbit-knot generator with the ordinary oriented homotopy-seven-sphere generator in PUSH C.3.14 and C.3.23.',
 'The biaxial SO(2) setting is a semifree oriented circle action with fixed S3 of codimension4, with the equivariant connected-sum structure fixed. Example7.14 identifies M_3^7 with S_(2,-1)(H), and Proposition7.15 gives the cyclic generator of the orbit-knot action group. Its associated bundle has Euler evaluation1 and Pontryagin evaluation6; the independently checked Eells–Kuiper expression gives (36−4)/896=1/28. A convention-dependent sign is retained when comparing the manuscript knot coordinate. No numerical value for the actual annular map is imported.',
 'Operative classification statement, preceding geometric interpretation, example and corollary read. The receiving proof separately specifies its orbit knot and cap.',
 [('C_characteristic_cap.tex','134–145'),('C_equivariant_integer.tex','100–111')],
 author='Michael W. Davis', title='Some group actions on homotopy spheres of dimension seven and fifteen',
 year=1982, journal='American Journal of Mathematics', volume='104', issue='1', pages='59–90',
 dependence='operative generator normalization; actual map comparison separately proved'),

record('FintushelPao1983D', MAPS+'fintushel_pao.pdf',
 'https://msp.org/pjm/1983/109-2/pjm-v109-n2-p09-p.pdf',
 'Published original introduction and §1, pp.349–354, text lines1–257 read. Propositions1.3–1.4 on pp.352–353 (PDF pages5–6) visually opened with the local quotient formulas and proof.',
 'Smooth orbit structure and homotopy-five-sphere conclusion for the specified semifree action on S6, used in PUSH C.3.14.',
 'The source assumes n>5 and codimension-four fixed set. Here n=6 and the fixed set is the already constructed S2; no exceptional orbits occur. Proposition1.3 gives the compatible smooth quotient structure and embedded fixed set; Proposition1.4 gives a homotopy(n−1)-sphere. The further identification with standard S5 uses the separate Theta5=0 prerequisite. The source convention permits weak equivalence by circle inversion; the receiving proof instead fixes the signed primitive Euler class and supplies its own bundle-lifting argument, so it does not silently infer orientation-preserving equivariant equivalence from weak classification.',
 'Full stated operative section and its local constructions read. No assertion that Proposition1.4 alone identifies the smooth quotient with standard S5.',
 [('C_characteristic_cap.tex','37–75')],
 author='Ronald Fintushel and Peter Sie Pao', title='Circle actions on homotopy spheres with codimension 4 fixed point set',
 year=1983, journal='Pacific Journal of Mathematics', volume='109', issue='2', pages='349–362',
 dependence='operative orbit smoothing and homotopy type'),

record('GauniyalTurchin2026Root', CACHE+'GauniyalTurchin2026.pdf',
 'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FDBF3CFC3531902C45DE9C1D0F8D9A28/S0013091526101485a.pdf/goussarovpolyakviro_type_formulas_for_4k1dimensional_knots_and_links_in_mathbbr6k.pdf',
 'Published original §4.1 definitions, pp.1492–1493, and §4.2 Theorem4.1/equation(4.3), p.1493 (PDF page28), visually opened. Text lines1480–1601 read.',
 'Comparison of a possible projected-knot route and its missing inputs in C_recent_literature; no theorem of the checked construction depends on evaluating this formula.',
 'The theorem assumes a long knot F:R^(4k−1)→R^(6k) whose specified projection is a generic immersion, Ekholm orientations on the two double-preimage links, the normal-push-off invariant E(f), and the normalized Smale invariant. The formula is H(F)=lk(L+,L−)/2+E(f)/6+Omega_S^(2k)(f)/3. The spherical version requires care in the Smale normalization. A double-circle count alone supplies none of the missing immersion/framing data; this citation does not calculate the family monodromy.',
 'Exact definitions and theorem opened; full proof of this comparative formula was not independently reread. No operative dependence on an unperformed numerical application.',
 [('C_recent_literature.tex','1–12')],
 author='Neeti Gauniyal and Victor Turchin', title='Goussarov–Polyak–Viro type formulas for (4k−1)-dimensional knots and links in R^(6k)',
 year=2026, journal='Proceedings of the Edinburgh Mathematical Society', volume='69', issue='4', pages='1466–1505', doi='10.1017/S0013091526101485',
 aliases=['GauniyalTurchin2026D'], dependence='comparative only; missing-input diagnosis'),

record('Haefliger1966D', MAPS+'haefliger.pdf',
 'https://www.maths.ed.ac.uk/~v1ranick/tda/haefliger.pdf',
 'Published original §5.1, Theorem5.3 and proof, §§5.9–5.10, §§5.16–5.17, and §6 through Corollary6.6: pp.416–422, text lines710–1048 read. Theorem5.17 p.421 and Corollary6.6 p.422 (PDF pages20–21) visually opened.',
 'Unknotting of S2 in S5 for PUSH C.3.14; separate knot and framing coordinates for framed S3 in S6 in C.3.23.',
 'The codimension is q>2. Corollary6.6 states C_n^q=0 when n<2q−3; (n,q)=(2,3) satisfies2<3. This cannot be applied to (3,3). Theorem5.17 gives FC_3^3=Z+Z and C_3^3=Z, with the described generators and even suspension image. The two integer coordinates are retained separately; no unframed conclusion substitutes for a framing check.',
 'Operative original statements and surrounding constructions/proofs read at the stated locators. No claim that arbitrary S3 knots in S6 are unknotted.',
 [('C_characteristic_cap.tex','42–47'),('C_equivariant_integer.tex','49–61')],
 author='André Haefliger', title='Differentiable embeddings of S^n in S^(n+q) for q>2',
 year=1966, journal='Annals of Mathematics', volume='83', issue='3', pages='402–436',
 dependence='operative unknotting range and framed/unframed exact-sequence context'),

record('HaefligerSalem1991D', CACHE+'KarshonOrbitSlides.pdf',
 'https://link.springer.com/article/10.1007/BF02411354',
 'Exact original facsimiles: §3 Theorem3.1 and Lemma3.2 on Karshon slide6; original proof opening p.43 on slide7; original introduction on slide3. Slide6 visually opened. Original publisher metadata opened separately at DOI10.1007/BF02411354.',
 'Historical comparison and correction in the concluding paragraph of the complete direct proof C.3.6. No operative invocation of the defective slice lemma.',
 'Theorem3.1 explicitly assumes that the orbifold diffeomorphism commutes with the torus action and preserves its orbits. Lemma3.2 as printed omits equivariance. For scalar S1 on C, conjugation preserves orbits but its required quotient function is bar(z)/z=e^(−2i theta), which has no continuous extension at0. This counterexample is independently checked. C.3.6 proves the equivariant scalar-slice case directly and keeps all of its overlap and logarithm steps.',
 'Original theorem/lemma facsimiles and proof opening only. Full1991 article retrieval timed out and the publisher page confirms subscription access. The full article was not opened; no general theorem or full proof is certified beyond this precisely identified comparison.',
 [('C_orbit_lift_comparison.tex','1–92')],
 status='verified_original_excerpt_for_stated_use', author='André Haefliger and Eliane Salem',
 title='Actions of Tori on Orbifolds', year=1991, journal='Annals of Global Analysis and Geometry', volume='9', issue='1', pages='37–59', doi='10.1007/BF02411354',
 facsimile_url='https://www.fields.utoronto.ca/talk-media/1/23/28/slides.pdf',
 web_refs=['turn334search5','turn335view0'], dependence='historical comparison only; defective lemma explicitly rejected'),

record('Jiang2014E', CACHE+'Jiang2014.pdf',
 'https://archive.ymsc.tsinghua.edu.cn/pacm_download/613/12072-v4Regular_circle_actions_on_2-connected_7-manifolds.pdf',
 'Author manuscript dated19April2014, Lemmas3.5–3.6 and complete proof of Lemma3.5 Case2, manuscript pp.12–15, text lines668–858. All four original pages visually opened; title/date on page1 checked.',
 'Credit for the existing Hopf-handle/CP2 cap and the characteristic integer in the literature-context remark following the receiving direct coboundary proof C.3.25.',
 'Source conventions are oriented smooth circle-bundle total spaces with delta=0. Lemma3.5 additionally assumes k=0. In Case2 epsilon=0, N is spin, the S2×D4 tube pulls back to S3_Hopf×D4, and Wprime=Wt union CP2×D4 has trivial normal CP2. The hyperbolic intersection matrix gives p1^2=6p, z^2 p1=p, z^4=sigma=0, hence mu=p/(24·28). Lemma3.6 has r=(1−epsilon)(p−4k)/24. These signs were checked visually. The receiving proof supplies its own general-k calculation and identifies its actual boundary; those extra conclusions are not attributed to Jiang Lemma3.5.',
 'Relevant lemma statements, orientation setup and full operative comparison proof read. This is credit for standard machinery, not an imported classification of the actual family map.',
 [('C_index_literature_context.tex','1–14')],
 author='Yi Jiang', title='Regular circle actions on 2-connected 7-manifolds', year=2014,
 journal='Journal of the London Mathematical Society', volume='90', issue='2', pages='373–387', doi='10.1112/jlms/jdu028',
 version_note='Opened later author manuscript19April2014; not arXiv1302.0923v3 of18September2013. Manuscript pagination is preserved.',
 dependence='known-source credit; direct receiving construction remains complete'),

record('KarshonOrbitSlidesD', CACHE+'KarshonOrbitSlides.pdf',
 'https://www.fields.utoronto.ca/talk-media/1/23/28/slides.pdf',
 'All20 original slides read in extracted text; torus theorem slide2, type-HS version slide5, original Haefliger–Salem facsimiles and counterexample slides6–7, proof outline and stages slides8–17, and failure examples slides18–19. Slide6 visually opened. Official Fields event page separately opened.',
 'Corrected scope of the orbit-preserving theorem and explanation of the missing equivariance in the old slice lemma; comparison following C.3.6.',
 'For a connected manifold with faithful torus action, a smooth orbit-preserving equivariant diffeomorphism admits a smooth invariant torus-valued multiplier. The slide counterexample uses complex conjugation and fails equivariance. Faithfulness, connectedness, smoothness and compactness are not dropped. The slides contain a proof outline, not the operative full proof used here: C.3.6 supplies its own scalar-slice argument, so no general outline is promoted to a new receiving proof.',
 'Complete research slides read at their actual level of detail. Bibliographic date now verified from the official event listing, rather than inferred from the undated PDF.',
 [('C_orbit_lift_comparison.tex','84–92')],
 author='Yael Karshon', title='Equivariant orbit preserving diffeomorphisms', year=2020,
 publication_type='Research lecture slides, joint work with Gerald W. Schwarz',
 event='Fields Institute, Workshop on Torus Actions in Topology,13May2020',
 event_url='https://www2.fields.utoronto.ca/talks/Equivariant-orbit-preserving-diffeomorphisms',
 web_refs=['turn334search3','turn335view1'], dependence='historical correction and hypothesis comparison only'),

record('MontgomeryYang1968E', CACHE+'MontgomeryYang1968.pdf',
 'https://page-one.springer.com/pdf/preview/10.1007/978-3-642-46141-5_4',
 'Publisher-authorized original preview, complete pp.125–126: introduction and stated TheoremsA–C, including the Pontryagin-offset convention and correction of an earlier free-action assertion.',
 'Historical credit in C_index_literature_context for the relation among semifree circle actions, fixed three-sphere knots and surgery to homotopy CP3.',
 'The stated correspondence is for semifree circle actions with fixed S3 and the indicated orientations; the forgetful map to homotopy spheres is distinguished from the free-action classification. The convention p1=(f(alpha)+4)a^2 and image f=24Z agrees with the offset24 comparison. Page126 explicitly corrects an earlier assertion that every homotopy7-sphere admits a free action; that false earlier claim is not used. The manuscript derives its second proof by explicit bordisms and does not import a complete knot classification from this preview.',
 'Only the full two-page primary preview was available/opened. The remaining eight pages and their proofs were not opened. This record authorizes historical context only.',
 [('C_index_literature_context.tex','15–23')],
 status='verified_original_excerpt_for_stated_use', author='Deane Montgomery and C. T. Yang',
 title='Differentiable actions on homotopy seven spheres, II', year=1968,
 booktitle='Proceedings of the Conference on Transformation Groups', editor='Paul S. Mostert', publisher='Springer', pages='125–134', doi='10.1007/978-3-642-46141-5_4',
 dependence='historical correspondence and normalization credit only'),

record('Olbermann2010D', MAPS+'olbermann.pdf',
 'https://msp.org/agt/2010/10-4/agt-v10-n4-p03-p.pdf',
 'Published original pp.1906–1908, text lines70–164, Theorems1.2–1.5 and their surrounding scope; Theorems1.3–1.5 pp.1907–1908 (PDF pages3–4) visually opened. §3 opening pp.1910–1911, text lines250–289; characteristic-pair display p.1911 (PDF page7) visually opened.',
 'PUSH C.3.14 credits the characteristic integer (p1 x−4x^3)/24. MAPS B.6.2 compares involution classification with a historical attempted knot route; the distinction between a knot and an equivariant conjugation is retained.',
 'The §3 invariant concerns closed simply connected spin six-manifolds with H2=Z and H3=0, a chosen generator x and an orientation. Both sign changes negate the pair. Theorem1.3 concerns even knot classes in C_3^3, each with exactly four relative-S3 conjugations, and none for odd classes. Theorem1.4 assumes a Z2-homology3-sphere and the zero H1 embedding orbit;2Z acts freely/transitively. Theorem1.5 uses orientations of both ambient S6 and fixed set and has group Z plus Z4. This is not an unframed knot-only or circle-action classification and supplies no value for the annular map. The receiving integer is independently integral by the twisted spin index formula.',
 'Exact operative characteristic formula and all requested comparative theorem statements/definitions opened; no claim that the entire involution-classification proof was independently reread.',
 [('C_characteristic_cap.tex','109–124')],
 author='Martin Olbermann', title='Involutions on S6 with 3-dimensional fixed point set', year=2010,
 journal='Algebraic & Geometric Topology', volume='10', pages='1905–1932', doi='10.2140/agt.2010.10.1905',
 aliases=['mapsOlbermann10'], dependence='independent characteristic-integer credit; involution statements comparative only'),

record('Sakai2015Root', CACHE+'Sakai2015.pdf',
 'https://arxiv.org/pdf/1405.1947v2',
 'Original author preprint arXiv1405.1947v2,5December2015: §2 pp.3–5, text lines103–245, definitions of double-preimages/crossings, Lemma2.3 and proof, Definition2.4, Theorem2.5 and Corollary2.7.',
 'Comparison of the crossing-change formula and its need for an identified reference embedding; no absolute family knot value is inferred.',
 'A long embedding in R^(6k) has a specified generic immersed projection into R^(6k−1), double loci with the prescribed upper/lower labels and orientations, and an almost-planar crossing-change representative. Theorem2.5 computes H(f)−H(f_S) from signed linking differences; it is a change formula. The manuscript correctly retains the need for an actual crossing set, framing conventions and a known comparison value. Corollary2.7 is not an automatic explicit unknotting projection for this family.',
 'Exact definitions, theorem and corollary opened; full proof of the comparative crossing-change theorem was not independently reread. No operative numerical dependence.',
 [('C_recent_literature.tex','14–20')],
 author='Keiichi Sakai', title='Lin–Wang type formula for the Haefliger invariant', year=2015,
 journal='Homology, Homotopy and Applications', volume='17', issue='2', pages='317–341', doi='10.4310/HHA.2015.v17.n2.a15',
 version_note='The actually retrieved original is arXiv1405.1947v2 dated5December2015. Published pagination is bibliographic metadata, not the opened preprint locator.',
 dependence='comparative only; missing-reference-value diagnosis'),

record('Smale1959E', CACHE+'Smale1959_facsimile.pdf',
 'https://www.ams.org/journals/proc/1959-010-04/S0002-9939-1959-0112149-8/S0002-9939-1959-0112149-8.pdf',
 'Original first-page scan p.621 including TheoremA, reproduced on PDF page6 of Pedro Boavida de Brito\'s March2024 MMAC lecture slides, visually opened.',
 'An orientation-preserving smooth diffeomorphism of the fixed S2 is isotopic to the identity, used to normalize its restriction in C.3.23 and the index-additivity proof.',
 'The original theorem concerns orientation-preserving C-infinity diffeomorphisms of S2 with C^r topology for infinity>=r>1 and identifies a strong deformation retraction to SO(3). Its component consequence gives the stated isotopy; the receiving argument needs no stronger arbitrary relative or equivariant deformation theorem. The subsequent normal-framing correction remains separately proved.',
 'The exact original theorem statement was visually opened in facsimile. The publisher full PDF returned HTTP403; the remaining original proof pages were not opened. No full-paper verification is asserted.',
 [('C_equivariant_integer.tex','27–35'),('C_index_additivity.tex','74–82')],
 status='verified_original_excerpt_for_stated_use', author='Stephen Smale', title='Diffeomorphisms of the 2-Sphere', year=1959,
 journal='Proceedings of the American Mathematical Society', volume='10', issue='4', pages='621–626', doi='10.1090/S0002-9939-1959-0112149-8',
 facsimile_url='https://math.tecnico.ulisboa.pt/seminars/download.php?fid=2693',
 dependence='operative component consequence of exact original TheoremA'),

record('Wall1966VE', CACHE+'Wall1966.pdf',
 'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/wclass5.pdf',
 'Original scan pp.360–361 (PDF pages6–7), Theorem4, its preceding framing conventions and proof, and Theorem5, visually opened in full. OCR is blank for this scan; verification is from the images.',
 'The framed three-knot surgery formula for the actual specified six-dimensional cap in PUSH C.3.14.',
 'Wall\'s chosen framing coordinate beta-prime and knot coordinate phi give the diagonal cubic k=6phi+beta-prime and Pontryagin evaluation p1 x=4beta-prime. Consequently J=(p1 x−4k)/24=−phi. The manuscript retains one fixed overall sign when comparing Wall\'s knot generator with its Eells–Kuiper generator. Rank-one, simply connected, spin and torsion-free homology conditions are verified in the receiving cap construction; an abstract classification does not replace its actual gluing identification.',
 'Original theorem, proof and neighboring classification statement visually read. The unrelated embedding theorem is excluded; the1967 corrigendum was opened separately.',
 [('C_characteristic_cap.tex','125–141')],
 author='C. T. C. Wall', title='Classification problems in differential topology. V: On certain 6-manifolds', year=1966,
 journal='Inventiones Mathematicae', volume='1', issue='4', pages='355–374', doi='10.1007/BF01389738',
 dependence='operative framed-surgery formula'),

record('Wall1967CorrE', CACHE+'Wall1967Corr.pdf',
 'https://link.springer.com/content/pdf/10.1007/BF01425407.pdf',
 'Entire original one-page corrigendum, p.306.',
 'Confirms that the cited correction does not alter Wall Theorems4–5 or the framed-surgery formula used in C.3.14.',
 'The corrigendum changes Theorem14 on p.371: the relevant condition concerns the normal bundle for an almost-smooth embedding into R9 and a class X in2H satisfying X^2−p1=0. It does not modify the cubic/Pontryagin formulas of Theorem4. No assertion using the incorrect earlier embedding criterion is present in the receiving proof.',
 'Whole original corrigendum read. The corrected embedding criterion itself is not an operative prerequisite here.',
 [('C_characteristic_cap.tex','132–135')],
 author='C. T. C. Wall', title='Corrigendum of the paper: Classification problems in differential topology. V', year=1967,
 journal='Inventiones Mathematicae', volume='2', pages='306', doi='10.1007/BF01425407',
 dependence='correction-scope check')
]

assert len(rows) == 15 and len({r['citation_key'] for r in rows}) == 15
OUT.mkdir(parents=True, exist_ok=True)
(OUT/'push_C_references_verified.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')

# Copy the already established metadata, replacing dated producing-session
# notes by the precise scope of the actual current reading. Parse balanced
# braced fields so that formula braces and quoted umlauts are preserved.
bibtext = (ROOT/'sources/returns/S6_02_PUSH/S6_02_PUSH_references.bib').read_text()


def get_entry(key):
    m = re.search(r'@[A-Za-z]+\{'+re.escape(key)+r',', bibtext)
    assert m, key
    start = m.start()
    depth = 1
    i = m.end()
    while depth:
        if bibtext[i] == '{' and (i == 0 or bibtext[i-1] != '\\'):
            depth += 1
        elif bibtext[i] == '}' and (i == 0 or bibtext[i-1] != '\\'):
            depth -= 1
        i += 1
    return bibtext[start:i]


def replace_braced_field(entry, field, value):
    m = re.search(r'\b'+re.escape(field)+r'\s*=\s*\{', entry, re.I)
    if not m:
        body = entry[:-1].rstrip()
        if not body.endswith(','):
            body += ','
        return body+'\n '+field+'={'+value+'}\n}'
    depth, i = 1, m.end()
    while depth:
        if entry[i] == '{' and entry[i-1] != '\\': depth += 1
        elif entry[i] == '}' and entry[i-1] != '\\': depth -= 1
        i += 1
    return entry[:m.start()]+field+'={'+value+'}'+entry[i:]


notes = {
 'Smale1959E': 'Exact original Theorem A, p.621, visually opened in reproduced first-page facsimile; the full publisher PDF was inaccessible. Used only for the component consequence. See the scoped source verification record.',
 'HaefligerSalem1991D': 'Exact original Theorem3.1 and Lemma3.2 facsimiles opened in Karshon slides6--7; full1991 article not opened. The non-equivariant lemma as printed is false; the receiving proof is independent and equivariant. See the scoped verification record.',
 'MontgomeryYang1968E': 'Primary publisher preview pp.125--126 opened in full. Historical correspondence and normalization only; remaining chapter and its proofs not opened.',
}
entries = []
for row in rows:
    key = row['citation_key']
    entry = get_entry(key)
    note = notes.get(key, 'Original cited statement and hypotheses checked independently on17November2026. Exact opened locators, versions, application and limitations are recorded in push_C_references_verified.json.')
    entry = replace_braced_field(entry, 'note', note)
    if key == 'KarshonOrbitSlidesD':
        entry = replace_braced_field(entry, 'year', '2020')
        entry = replace_braced_field(entry, 'howpublished', 'Fields Institute research lecture,13May2020; joint work with Gerald W. Schwarz')
    if key == 'HaefligerSalem1991D':
        entry = replace_braced_field(entry, 'doi', '10.1007/BF02411354')
        entry = replace_braced_field(entry, 'url', 'https://link.springer.com/article/10.1007/BF02411354')
    if key == 'Sakai2015Root':
        entry = replace_braced_field(entry, 'eprint', '1405.1947v2')
        entry = replace_braced_field(entry, 'url', 'https://arxiv.org/abs/1405.1947v2')
    entries.append(entry)
(OUT/'push_C_checked_references.bib').write_text('\n\n'.join(entries)+'\n')

summary = {
 'checker': READER, 'effort': 'Pro', 'date': DATE,
 'records': len(rows),
 'operative_or_formula_scopes': [r['citation_key'] for r in rows if r['dependence'].startswith('operative')],
 'original_excerpt_only': [r['citation_key'] for r in rows if r['status']=='verified_original_excerpt_for_stated_use'],
 'unresolved_mathematical_dependency_in_these_cited_scopes': [],
 'important_limits': [
   'Verification is scoped to actual operative or comparative use, not to complete independent proofs of every source theorem.',
   'Smale original TheoremA is verified from a first-page facsimile; original full proof was inaccessible.',
   'Haefliger–Salem full paper was inaccessible; its exact reproduced theorem/lemma is sufficient for the nonoperative historical comparison and rejection of the defective lemma.',
   'Montgomery–Yang two-page original preview supports historical context only.',
   'Gauniyal–Turchin and Sakai were not applied numerically to the actual family; the missing input diagnosis is the only use.',
   'The pure framing, actual gluing, coboundary and zero integer evaluations remain the full direct receiving proofs; source statements do not replace them.'
 ],
 'metadata_corrections': {
    'KarshonOrbitSlidesD':'2020,13May, verified official Fields event; replaces n.d.',
    'CrowleyNordstrom2020':'Online2020, actual issue2021; published p35 governs.',
    'Sakai2015Root':'Actually opened arXiv1405.1947v2,5December2015.',
    'Jiang2014E':'Actually opened19April2014 author manuscript, not2013arXivv3.'
 },
 'editorial_note': 'C_recent_literature.tex still contains producing-session search-date/priority prose. Root may remove the sentence beginning Searches on15November2026 and its following priority sentence, preserving the substantive missing-input comparison. No mathematical result changes.'
}
(OUT/'push_C_source_closure_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print('Saved', len(rows), 'scoped source records and15 clean bibliography entries.')
