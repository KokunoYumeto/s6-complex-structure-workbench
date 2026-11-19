"""Record bounded primary-source readings; assembly creates no proof credit."""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parents[2]
f=P/'analysis/I_sources/current_source_matches.json'
data=json.loads(f.read_text())
receipts={r['key']:r for r in json.loads((P/'analysis/I_sources/remaining_primary_downloads.json').read_text())}
checks={
 'IKN2005E':('Introduction pp1–4; Proposition6.1 and proof pp30–32; Theorem6.2 and full proof pp32–33; Theorem6.3 and full proof p34; Remarks6.3.1–3 pp34–35; Theorem6.4 p35.','Proper separated log-smooth fs analytic hypotheses, the log-smooth-base or exact-morphism alternative, torsion-free characteristic cokernels and unipotent coefficients are retained. Ordinary log-de-Rham and nilpotent Gauss–Manin conclusions were matched at this precise scope.'),
 'IKN2007ErratumE':('Entire mathematical note, journal pp113–115 (PDFpp1–3); addresses on PDFp4 were not read.','Theorem7.1 correction and full proof read, including the use of Theorem6.2(2), saturation, etale localization and flatness.'),
 'EH2024E':('arXiv2404.05124v3, Definition2.13 and Lemma2.14 statement p6, full proof p7; adjacent Lemma2.15 and Definition2.16.','Strict analytic toroidal proper modifications correspond to fan subdivisions through the displayed Specan gluing. The projective hypotheses of the paper main theorem are not imported into this local analytic lemma.'),
 'Parusinski1990E':('MPIM preprint, introduction printedp1 (PDF3); Theorem1.1 printedp2; Corollary1.2 with complete proof printedpp3–6 (PDF5–8).','The compact sets and local blowup neighborhoods, finite coefficient ideal, decreasing fibre excess and smooth-centre principalization were read. Receiving references to pp3–5 are corrected to pp3–6.'),
 'bertrand1995':('Original public PostScript, converted locally to PDF; all7published pages145–151, including Theorem2.1, Proposition2.2 and Theorem3.1 with proof.','Read the explicit antisymmetric endomorphism h-h-dual, the resulting Ribet section and the stated lifting/compactness relation. Conversion of the original PostScript supplies this reading; no modern source substitution.'),
 'Reyssat1982weierstrass':('Primary indexed PDF text, introduction and Corollary2 printedp292; Section5.1 proof printedp301 was inspected as indexed text.','Matched the source definitions of g_u,omega and s_omega and the three quantities in the transcendence-degree-at-least-two statement. Local PDF download failed; no visual scan check or independent verification of the OCR half-argument identity is claimed.'),
 'BiliottiGhigi2021Root':('arXiv1901.10724, Theorem1.2 and its surrounding graph-compactification setup p3.','The standing Fujiki class C assumption is retained in the receiving comparison; this event checks the exact statement and context.'),
 'AbashevaDeev2024AB':('arXiv2303.10764, Section2.2 pp4–6.','Read diagonal Hopf multipliers, the line-bundle quotient parameter, exponential map and explicit translation extension formulas.'),
 'KamenovaToriRoot':('Author four-page manuscript, all4pages; Theorem3.1 and proof pp2–3.','Proper family with Kahler total space and trivial canonical class hypotheses were read with the complete proof. These hypotheses are recorded in the receiving application.'),
 'Chen2026HodgeRoot':('arXiv2404.19229v2, Section2.1 p8.','Read the same-dimensional domination statement for the ddbar lemma and the Kahler case. Scope is the statement used in the receiving text.'),
 'Meersseman2011Root':('Published p511 (PDF18): Theorem3, Corollaries3–4 and proof opening; preceding examples on PDF17.','Reduced base and locally constant h0 are retained in the local-isomorphism statement. The later proof pages were not read in this event.'),
 'GrafKovacs2014Root':('Published pp117–118 (PDF1–2): abstract, equation1.1, Definition1.3 and Theorem1.4.','Read the proper/projective complex context of the cohomological surjectivity statement and the Du Bois pair theorem. The receiving analytic comparison has its own displayed proof.'),
 'Fujimoto1990AB':('Contribution in a263-page conference volume: Definition1.1 printedpp85–86 (PDF89–90), preceding introduction printedpp81–84, and printedpp93–94 (PDF97–98).','Read the Cartier logarithmic cocycle definition, codimension-at-least-three extension statement and Example1.15 cocycle1/(xy), including the stated1990 relative-compactification question. No general nonexistence claim is inferred.'),
 'Illman1972':('Original1972 thesis scan: Theorem3.1 printedp48 (PDF53) opened visually; following proof and Lemma3.2 through printedp51 read by OCR.','The equivariant triangulation statement for differentiable G-manifolds is matched. The application is a compact smooth manifold with a finite involution, yielding finite-dimensional equivariant cells. This event does not claim a reading of the entire triangulation proof.')
}
urls={
 'IKN2005E':'https://www.ms.u-tokyo.ac.jp/journal/pdf/jms120101.pdf',
 'IKN2007ErratumE':'https://www.ms.u-tokyo.ac.jp/journal/pdf/jms140105.pdf',
 'bertrand1995':'https://www.maths.tcd.ie/EMIS/journals/EM/restricted/4/4.2/bertrand.ps',
 'Reyssat1982weierstrass':'https://matwbn.icm.edu.pl/ksiazki/aa/aa41/aa4137.pdf',
 'KamenovaToriRoot':'https://www.math.stonybrook.edu/~kamenova/homepage_files/degen.pdf'}
for key,(locator,scope) in checks.items():
 r={'exact_locator':locator,'scope':scope,'date':'2026-11-18','checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro','verification':'opened and matched at listed scope'}
 q=P/'analysis/I_sources'/(key+'.pdf')
 if q.exists():r.update(source_path=str(q.relative_to(P)),sha256=hashlib.sha256(q.read_bytes()).hexdigest())
 if key in receipts:r['url']=receipts[key]['url']
 if key in urls:r['url']=urls[key]
 data[key]=r
f.write_text(json.dumps(data,indent=2,ensure_ascii=False))
print('Recorded',len(checks),'bounded source matches; total',len(data))
