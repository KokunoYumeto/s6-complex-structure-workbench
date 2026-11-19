"""Bounded passages actually opened on 18 November; no inferred proof credit."""
from pathlib import Path
import hashlib,json

P=Path(__file__).resolve().parents[2]
f=P/'analysis/I_sources/current_source_matches.json'
data=json.loads(f.read_text())
receipts={r['key']:r for r in json.loads((P/'analysis/I_sources/remaining_primary_downloads.json').read_text())}
checks={
'BourdonClarkStankewicz2017':('arXiv:1411.2742v3, Theorem4.15 and Remark4.16, p23.', 'Parish torsion restriction for F=Q(j(E)), and its separately stated CM-field extension. The source theorem statement was matched; no reading of Parish original proof is claimed.'),
'Shin2015':('arXiv:1009.2253v6: equation(1), p1; modular-function setup p2; Remark2.2 and complete Proposition2.3 with its proof pointers, pp3–4.', 'The product convention, q-order, lattice-translation factor and modular-unit exponent match the receiving Siegel-function identities. This checks the explicit source statement; the cited earlier book proofs were not newly opened.'),
'Sutherland2023CM':('MIT18.783 Fall2023 Lecture20, Theorem20.12 with its full displayed proof and Corollary20.13, p6; Galois/class-group discussion p7.', 'CM j-invariants are algebraic integers. The proof uses a cyclic prime-degree self-isogeny and the monic diagonal modular polynomial; the conjugation map on endomorphism rings is written explicitly.'),
'agboola2006':('Published PDF pp1001–1002; Rubin AppendixA setup p1042, TheoremA.1 and LemmaA.2 with proof p1043 (PDFpp2–3,43–44).', 'Recorded maximal-order CM, class number one, p>3 good ordinary setup and the appendix sign convention. TheoremA.1 gives the one-prime height; LemmaA.2 gives the relation among the three projected heights. No nondegeneracy theorem for an entire height pairing is attributed to this passage.'),
'BM97':('ChapterI preprint alg-geom/9508005: Theorem1.6 and following analytic paragraph p5; Remark1.7 p6; Theorem1.10 p7; analytic-category setup (0.2) p3 was opened in the earlier BM95AB record.', 'The downloaded edition contains30pages. Operative references to its absent Section13 were replaced with the inspected ChapterI statements. Smooth-centre analytic resolution and ideal principalization are used with their explicit local/proper-neighborhood hypotheses; no reading of Theorem13.3 is claimed.'),
'Movasati24':('Author version dated13May2024: Theorem8.5 and its complete displayed proof, printed pp80–81 (PDFpp94–95); browser PDF lines4700–4758.', 'Stein factorization of a proper holomorphic map, including connected fibres, finite second map, direct-image identity and uniqueness. This is the exact factorization used for the proper divisor-to-curve map in P2.6.'),
'KatzarkovEtAl2025Root':('Publisher full text reproduced at PMC12012539: Example1 and Theorem4, lines352–358.', 'The explicit Hopf-surface and elliptic-product compactifications share an analytic open set. Theorem4 separately requires definable analytic isomorphism of the open subsets; that hypothesis is not supplied for the present family.'),
'Merkulov1995D':('Publisher extract for Moduli spaces of compact complex submanifolds of complex fibered manifolds, Mathematical Proceedings118(1),1995,pp71–91, DOI10.1017/S0305004100073473; abstract/extract paragraph on Kodaira completeness.', 'The opened extract states the compact-submanifold H1(normal)=0 completeness criterion, smooth parameter-space dimension H0(normal), and tangent-space identification. This is an extract-only check; the full article was not read.')
}
checks.update({
'EichlerZagier1982':('Published scan, main theorem p399 (PDFp1) opened visually; corollary p400 read in extracted text.', 'Exact zero formula for the Weierstrass function, including logarithmic constant, factor144*pi*i*sqrt(6), vertical integral and the normalized weight6 and weight12 forms. The source formula and branch conventions are matched; no full-paper re-proof credit.'),
'DukeImamoglu2008':('Author manuscript pp1–3: equations(1)–(5), Theorem1 and Corollaries1–2.', 'The map x=1-1728/j and the hypergeometric quotient for the zero are matched with the receiving period convention. Bounded statement check; later proof sections were not newly read in this event.'),
'Knudson2004':('arXiv math/0409133, Theorem4.1 and full proof p10; Theorem4.2 and full proof p11.', 'Prime-order Smith fixed-point conclusions for finite-dimensional G-CW complexes, and the finite-complex acyclic quotient statement. The dimensions and coefficient fields are retained in the actual application.'),
'McMullen1996Complex':('Author course notes, numbered item67, p15, together with surrounding items63–66.', 'Infinitesimal deformation space H1(Theta) and the curve duality with quadratic differentials. This is a course-note statement check, not a new proof of general Kuranishi theory.'),
'bost2009':('Published source title and abstract pp361–362; Theorems3.1.1–3.1.2 with surrounding equivalence discussion, p386 (PDFp27).', 'The compact-point criterion is stated for the universal vector extension of an abelian variety over a number field. The precise extension and its dual line-bundle/connection interpretation are retained; no identity with the diagonal metric norm is supplied by this theorem.'),
'callSilverman1993':('Theorem4.1 and following Tate remark, journal pp183–184 (PDFpp22–23), both opened visually.', 'The height ratio limit uses a degree-one height on the base. The following elliptic-family remark gives the divisor-height formula with bounded error. Reading of the original Tate paper is not claimed.'),
'xie2024algebraicity':('arXiv2202.09032: Theorem1.3 and its setup p3; Theorem2.3 and full proof pp12–14; Theorem2.5 and full proof pp14–15.', 'Recorded the K-defined formal germ, K-rational approximating points and positive local approximation/height ratio. These hypotheses are retained explicitly in the discussion of the attempted application.'),
'nguyen2023':('arXiv2112.14937: Definition1.3 and Bottcher-domain setup p2; Theorem1.4 and Corollary1.6, p3.', 'Polynomial hypotheses, functional basin, common degree and non-integrability are recorded exactly. The receiving discussion gives the explicit elliptic duplication quotient and its ramification instead of applying this polynomial result to it.'),
'noguchi2024':('Author PDF: subgroup condition1.2 and Theorem1.3 p2; Section3 proof pp7–9; jet description4.3–4.5 p10.', 'The entire-map semi-abelian Ax–Schanuel statement and its exact subgroup nondegeneracy hypothesis match the fixed-extension functional application. This event is a source reading, not an independent check of every external input to that proof.'),
'bertrand2017':('Author Fields Institute slides,13–17February2017, all15slides read; operative loci slides5–8 and final comment(c).', 'The explicit real compactness determinant and Green-function formula are matched. The pointwise conjecture, known CM antisymmetric case and functional results remain attributed with their own stated status.'),
'waldschmidt1979sigma':('Author-hosted June2015 English translation by K.Senthil Kumar and S.Kannappan of the1979 note, all3pages; Theorem1 and Corollaries1–2 p3.', 'The sigma quotient with its zeta exponential and the nontorsion/algebraic-invariant hypotheses are matched. The translation date is distinguished from the1979 article date.'),
'waldschmidt1988theta':('Original scanned lecture, printed pp15-03 and15-05 (PDFpp4 and6), both opened visually.', 'The CM holomorphic sigma normalization and the algebraic-q hypothesis of the periodic-functional-equation theorem were checked directly. The sigma factor and the Hermitian metric factor remain related by the explicit Gaussian in the receiving text.')
})
urls={
'Movasati24':'https://w3.impa.br/~hossein/myarticles/ComplexGeometry.pdf',
'KatzarkovEtAl2025Root':'https://pmc.ncbi.nlm.nih.gov/articles/PMC12012539/',
'Merkulov1995D':'https://doi.org/10.1017/S0305004100073473'}
for key,(locator,scope) in checks.items():
 filekey='BM95AB' if key=='BM97' else key
 r={'exact_locator':locator,'scope':scope,'date':'2026-11-18',
    'checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro',
    'verification':'opened and matched at listed scope'}
 q=P/'analysis/I_sources'/(filekey+'.pdf')
 if q.exists():r.update(source_path=str(q.relative_to(P)),sha256=hashlib.sha256(q.read_bytes()).hexdigest())
 if filekey in receipts:r['url']=receipts[filekey]['url']
 if key in urls:r['url']=urls[key]
 data[key]=r
f.write_text(json.dumps(data,indent=2,ensure_ascii=False))
f=P/'S6_10_PAPERS_references.bib';s=f.read_text()
if '@misc{Movasati24,' not in s:
 s+='''\n@misc{Movasati24,
  author = {Hossein Movasati},
  title = {A Course in Complex Geometry and Holomorphic Foliations},
  year = {2024},
  howpublished = {Author version dated 13 May 2024},
  url = {https://w3.impa.br/~hossein/myarticles/ComplexGeometry.pdf},
  verification = {verified at listed scope},
}\n'''
 f.write_text(s)
print('Recorded',len(checks),'bounded source matches.')
