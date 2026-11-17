"""Persist actual, scoped source openings for the sphere-carrier audit.

This is a provenance writer, not a mathematical verifier. Existing entries and
earlier limits are retained; new openings have their own dated records.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'deliverables/work/maps_audit'
EXT = ROOT / 'sources/external/maps_audit'
ACTOR = dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',
             effort='Pro', date='2026-11-17')

def record(key, filename, url, locators, match, edition, aliases=()):
    p = EXT / filename
    return dict(key=key, aliases=list(aliases), source=str(p.relative_to(ROOT)),
                url=url, sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                opened_locators=locators, verification_scope=match,
                edition_opened=edition,
                status='verified only in the specified scope', **ACTOR)

rows = [
    record('BorelSerre1953', 'borel_serre1953.pdf',
           'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/borelserre.pdf',
           ['Section 12, Proposition 12.4, Lemma 12.5 and Proposition 12.6, printed p.430 (PDF page 23)',
            'Section 15, Proposition 15.1 and following remark, printed p.434 (PDF page 27)'],
           'Original reduced-power formula and sphere obstruction opened visually. '
           'For complex rank six on a smooth manifold homeomorphic to S^12, lower '
           'Chern classes vanish and c6=2u. At p=5 the splitting-principle '
           'calculation gives P^1(c2)=s5*s1-s6=6*c6 modulo the lower-Chern ideal, '
           'contradicting 0=2u modulo 5. Proposition 15.1 excludes almost complex '
           'S^(2n) for n>=4; the following remark explicitly covers every '
           'differentiable structure. It therefore also applies to S^24.',
           'Original 1953 journal scan, American Journal of Mathematics 75(3), 409–448.'),
    record('Husemoller1994', 'husemoller1994.pdf',
           'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/husemoller.pdf',
           ['Chapter 20, Section 9, Theorem 9.6 and Corollary 9.8, printed p.308 (PDF page 329)'],
           'The exact Bott-integrality corollary was opened visually: for a complex '
           'bundle over S^(2n), its nth Chern class is divisible by (n-1)!. '
           'For a hypothetical almost complex structure on a smooth homotopy '
           'S^12, pullback by a degree-one homotopy equivalence gives a complex '
           'bundle on S^12 with c6=2u, contradicting divisibility by 120. '
           'Only this locator is certified; the separate Chapter 17 citation '
           'elsewhere in the working bibliography is not covered by this record.',
           'Third edition, Springer, 1994; original book scan.'),
    record('KonstantisParton2018', 'konstantis_parton2018.pdf',
           'https://arxiv.org/pdf/1707.03883',
           ['Lemma 4.1 and Theorem 4.2, preprint p.8',
            'Section 5.2, Theorem 5.1, preprint p.10',
            'Section 6, Proposition 6.1 and proof of Theorem 1.1, preprint pp.11–12'],
           'Lemma 4.1 and Theorem 4.2 were read with their full proofs; the stable '
           'triviality proof for the standard S^12 gives p3=-2*c6=-4u whereas '
           'p3=0. Section 6 and its K-theoretic input were read in full: Chern '
           'characters on spheres are integral and Newton identities force '
           '(n-1)! to divide 2. This independently matches the second working '
           'proof. The source itself treats alternative smooth sphere structures '
           'in Remark 6.2. The third proof in the working text deliberately uses '
           'the standard sphere stable trivialization only.',
           'arXiv:1707.03883v1, 13-page author preprint; published journal metadata '
           'is Differential Geometry and its Applications 57 (2018), 10–22.'),
    record('IsaksenWangXu2023', 'isaksen_wang_xu2023.pdf',
           'https://www.numdam.org/item/10.1007/s10240-023-00139-1.pdf',
           ['Table 1, printed p.113 (PDF page 7), rows k=3 and k=4',
            'Table 1 notation and decomposition into v1-torsion and periodic parts, Section 1.2'],
           'The original journal table was opened visually. The k=3 row has '
           'periodic subgroup 8*3 and no torsion columns, hence pi3^S=Z/24; '
           'the k=4 row has zero in every stable-homotopy column, hence pi4^S=0. '
           'Only these two low stems are imported; no claim to have independently '
           'verified the full 137-page high-stem computation is made.',
           'Published journal PDF, Publications mathématiques de l’IHÉS 137 '
           '(2023), 107–243, DOI 10.1007/s10240-023-00139-1.'),
    record('HatcherSpectralSequences', 'hatcher_spectral_sequences.pdf',
           'https://pi.math.cornell.edu/~hatcher/AT/ATch5.pdf',
           ['Theorem 5.41(a),(b), printed p.573, and full proof pp.573–577',
            'Suspension diagram and integral 2- and 3-primary comparison, printed p.578 (PDF page 62)'],
           'The author-hosted chapter statement, complete text proof and final '
           'suspension diagram were opened. The source gives pi6(S3)=Z/12, '
           'pi7(S4)=Z plus Z/12, and pi_(n+3)(Sn)=Z/24 for n>=5. The p.578 '
           'argument identifies stabilization of pi6(S3) with the even subgroup '
           'of Z/24, including the 3-primary component; it also states '
           'eta^3=12*nu in the stable three-stem. These are the exact hypotheses '
           'and dimensions of the one-copy invariant remark. The draft is '
           'explicitly preliminary and incomplete; its date is not inferred '
           'from a crawler timestamp.',
           'Author-hosted preliminary Chapter 5 draft, 117 pages; no publication '
           'year recorded on the opened title page.'),
    record('CuspNullMilnor1965', 'milnor1965_viewpoint.pdf',
           'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/milnortop.pdf',
           ['Section 7, definitions and Theorems A–C, printed pp.42–44',
            'Product Neighborhood Theorem and proof of Theorem C, pp.46–48',
            'Lemma 4 and full proof, pp.48–49',
            'Proof of Theorem B and boundary-relative remarks, p.50'],
           'All of Section 7 pp.42–50 was read. The hypotheses match the '
           'candidate map after the explicitly supplied relative smoothing: '
           'compact smooth source; smooth map to S3; complete regular inverse '
           'image with its differential framing; compact framed nullbordism in '
           'source times interval with product collars. The proof and p.50 '
           'relative formulation keep a boundary ball at the basepoint. Thus '
           'the constructed bordism proves the based nullhomotopy, not merely '
           'vanishing of an abstract stable bordism class.',
           'Original University Press of Virginia 1965 scan, 76 PDF pages.',
           aliases=('Milnor1965Viewpoint',)),
]

path = OUT / 'references_verified.json'
refs = json.loads(path.read_text())
for row in rows:
    old = next((x for x in refs if x.get('key') == row['key']), None)
    if old is None:
        refs.append(row)
    elif old != row:
        old.setdefault('additional_dated_checks', [])
        if row not in old['additional_dated_checks']:
            old['additional_dated_checks'].append(row)

hatcher = next(x for x in refs if x.get('key') == 'Hatcher2002')
extra = dict(**ACTOR,
             opened_locators=['Opening homotopy-group table p.339, rows n=3,i=6 and n=6,i=12',
                              'Corollary 4.24 and full proof pp.360–361'],
             verification_scope='The original author PDF gives pi6(S3)=Z/12 and '
             'pi12(S6)=Z/2, with the table credited to Toda. Freudenthal gives '
             'an isomorphism for i<2n-1. Thus pi12(S8) is in the stable fourth '
             'stem (12<15), and pi12(S9) in the stable third stem (12<17). '
             'The group order argument for any smash of two maps S6→S3 uses '
             'postcomposition as a group homomorphism, not unjustified '
             'bilinearity of unstable composition.')
hatcher.setdefault('additional_dated_checks', [])
if extra not in hatcher['additional_dated_checks']:
    hatcher['additional_dated_checks'].append(extra)
path.write_text(json.dumps(refs, ensure_ascii=False, indent=2)+'\n')
(OUT/'carrier_source_checks.json').write_text(json.dumps(rows+[dict(key='Hatcher2002', **extra)], ensure_ascii=False, indent=2)+'\n')

provenance_path=OUT/'external_provenance.json'
provenance=json.loads(provenance_path.read_text())
for row in rows:
    new=dict(filename=row['source'],url=row['url'],sha256=row['sha256'],
             read_locators=row['opened_locators'],edition_opened=row['edition_opened'],**ACTOR)
    if not any(x.get('filename') == new['filename'] and x.get('sha256') == new['sha256'] for x in provenance):
        provenance.append(new)
provenance_path.write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')

(OUT/'carrier_checked_references.bib').write_text(r'''@article{BorelSerre1953,
  author={Borel, Armand and Serre, Jean-Pierre},
  title={Groupes de Lie et puissances réduites de Steenrod},
  journal={American Journal of Mathematics}, volume={75}, number={3},
  year={1953}, pages={409--448}, doi={10.2307/2372495}}
@book{Husemoller1994,
  author={Husemoller, Dale}, title={Fibre Bundles}, edition={3},
  series={Graduate Texts in Mathematics}, volume={20},
  publisher={Springer}, address={New York}, year={1994},
  doi={10.1007/978-1-4757-2261-1}}
@article{KonstantisParton2018,
  author={Konstantis, Panagiotis and Parton, Maurizio},
  title={Almost complex structures on spheres},
  journal={Differential Geometry and its Applications}, volume={57},
  year={2018}, pages={10--22}, doi={10.1016/j.difgeo.2017.10.010},
  eprint={1707.03883}, archivePrefix={arXiv}}
@article{IsaksenWangXu2023,
  author={Isaksen, Daniel C. and Wang, Guozhen and Xu, Zhouli},
  title={Stable homotopy groups of spheres: from dimension 0 to 90},
  journal={Publications mathématiques de l'IHÉS}, volume={137},
  year={2023}, pages={107--243}, doi={10.1007/s10240-023-00139-1}}
@misc{HatcherSpectralSequences,
  author={Hatcher, Allen}, title={Spectral Sequences},
  note={Preliminary extra Chapter 5 for Algebraic Topology; author-hosted draft},
  url={https://pi.math.cornell.edu/~hatcher/AT/ATch5.pdf}}
@book{CuspNullMilnor1965,
  author={Milnor, John W.}, title={Topology from the Differentiable Viewpoint},
  publisher={University Press of Virginia}, address={Charlottesville},
  year={1965}, note={Based on notes by David W. Weaver}}
''')
print(json.dumps({'new_scoped_records':len(rows),'total_reference_records':len(refs)},indent=2))
