"""Record the exact original-source passages actually opened during this review."""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parents[2];R=P.parents[1]
data={}
def add(key,path,locator,scope,url=''):
 p=Path(path);p=p if p.is_absolute() else P/p
 data[key]={'exact_locator':locator,'scope':scope,'date':'2026-11-18','checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro','status':'opened and matched at stated locus','local_file':str(p.relative_to(P)) if p.is_relative_to(P) else str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'url':url}
add('HaefligerSalem1991D','analysis/IV/references/KarshonOrbitSlidesD.pdf','Theorem3.1 and original Lemma3.2, original facsimile reproduced on PDFp6 of Karshon, Equivariant orbit preserving diffeomorphisms.',
'Original statement in facsimile visually opened; the complete1991 journal article was not available and is not claimed read. The equivariant orbit-preserving theorem supplies the invariant smooth torus-valued multiplier. The non-equivariant auxiliary lemma counterexample and correction are explicitly credited to Karshon and the original authors.','https://www.fields.utoronto.ca/talk-media/1/23/28/slides.pdf')
add('KarshonOrbitSlidesD','analysis/IV/references/KarshonOrbitSlidesD.pdf','Complete20-page slide deck text; corrected torus theorem PDFp2; original-source facsimile and conjugation counterexample p6; proof outline pp13–17.',
'Read the corrected equivariant statement, the z-conjugation quotient counterexample, and the stated proof outline. Page6 visually inspected. This is the author presentation of the correction, not a complete reading of the1991 journal proof. Receiving C3.6 retains its explicit real lift and connection-flow application.','https://www.fields.utoronto.ca/talk-media/1/23/28/slides.pdf')
add('AC26',R/'sources/original/AC26_original_manuscript.pdf','Original attached108-page manuscript, Proposition7.2 statement p41 and final proof p50.',
'Read the torus- and Gamma-equivariant strong deformation retraction statement and the final proof invoking Lemmas7.5 and7.7–10. This event does not claim all intervening lemmas were read. The receiving C3.8 proves its own orbit-quotient homotopy and primitive fixed-sphere application.','https://alpo.ge/s6.pdf')
add('AtiyahSinger1968IIIE','analysis/I_sources/AtiyahSinger1968IIIE.pdf','The index of elliptic operators III, original pp564–565 (PDF20–21), equations4.1–4.2, Riemann–Roch Theorem4.3 and its displayed proof.',
'Original scan visually opened. The Dolbeault symbol and Todd-class calculation applies to the compact complex manifold and holomorphic bundle as stated. This adds Theorem4.3 to the separately recorded holomorphic Lefschetz loci, without claiming a full reading of the60-page article.')
add('ChernSimons1974E','analysis/IV/references/ChernSimons1974E.pdf','Original pp51–54, equations2.10–2.11 and Theorem2.12; equation3.1, Proposition3.2 with full proof pp52–53; Propositions3.6–3.7 with proofs p53; Proposition3.8 with full proof pp53–54.',
'Read the invariant-polynomial transgression and its naturality, variation and relative boundary differential identities. The applications use the actual connection path and common boundary framing described in the receiving proof; no whole-paper reading is claimed.')
add('CrowleyNordstrom2020','analysis/IV/references/CrowleyNordstrom2020.pdf','arXiv1411.0656v4, pp4–5, Sections2.1–2.2, definition 2 p-hat=p1+z squared and equation2.1.',
'The displayed specialization assumes torsion-free H4 of the seven-manifold. It is applied to M_Phi with H4=0. Expanding the spin-c formula and dividing its Z/28 normalization by28 gives (p1 squared minus4 signature)/896 minus p1 z squared/192 plus z fourth/384. The free-circle boundary with possible H4 torsion uses the separately opened Crowley–Nordstrom2019 torsion-p1 formula.')
add('FintushelPao1983D','analysis/IV/references/FintushelPao1983D.pdf','Original p351 dimension n greater than5; Proposition1.3 and proof pp352–353; Proposition1.4 and proof pp353–354.',
'Read the local smooth Hopf quotient, equivariant homotopy-sphere model and fixed-knot construction in the stated dimension range, including the complete proofs of the two operative propositions. The receiving application has n=6 and retains its actual equivariant framing.')
add('Wall1966VE','analysis/IV/references/Wall1966VE.pdf','Original Theorem4 and full proof pp360–361, visually opened in the original scan; Theorem5 statement and its short proof p361.',
'The actual framed-link parameter beta-prime has p1 evaluation4 beta-prime, while the cubic evaluation is6 phi plus beta-prime. These exact formulas identify (p1 x minus4 x cubed)/24 as minus the framed-knot parameter in the receiving marking. Earlier classification sections are not claimed fully read in this event.')
add('Wall1967CorrE','analysis/IV/references/Wall1967CorrE.pdf','Complete one-page published corrigendum p306.',
'The corrigendum changes Theorem14 on almost-smooth embeddings into R9: the required integral condition is x squared minus p1=0. Its text concerns that embedding criterion; it supplies no alteration to the opened Theorem4 formulas on pp360–361.')
add('Olbermann2010D','analysis/IV/references/Olbermann2010D.pdf','Original pp1906–1907, Theorems1.2–1.4; complete Section3 on pp1910–1911 through the displayed rank-one invariants.',
'Read the stated involution/fixed-knot restrictions and the rank-one simply connected spin six-manifold correspondence. The invariant is ((p1 x minus4 x cubed)/24,x cubed), with the stated cohomology hypotheses. This event does not claim the complete later proof of the global involution classification.')
add('GauniyalTurchin2026Root','analysis/IV/references/GauniyalTurchin2026Root.pdf','Published pp1492–1493, Section4.1 and Theorem4.1 with equation4.3; primary publisher online metadata25September2026.',
'Read the exact generic-immersion hypothesis, Ekholm orientations, the pushed double-locus invariant E and the rational Smale coefficient defined by the sphere-to-Stiefel fibre map. The formula combines one-half linking, one-sixth E and one-third that Smale coefficient. The receiving comparison uses these actual definitions to specify the data a projection computation would need. No computation of the receiving orbit knot by this formula or full proof reading is claimed.',
'https://doi.org/10.1017/S0013091526101485')
add('Sakai2015Root','analysis/IV/references/Sakai2015Root.pdf','arXiv1405.1947v2 pp3–5, Section2 definitions, Lemma2.3 orientation proof, Definition2.4, and Theorem2.5 equations2.1–2.2 with the cancellation calculation.',
'Read the actual reflection implementing a chosen crossing change, the oriented two preimages of each double component, and the difference formula. The receiving comparison cites that difference theorem and retains the required comparison embedding and value. The later configuration-integral proof is not claimed fully read.',
'https://arxiv.org/pdf/1405.1947v2')
add('MontgomeryYang1968E','analysis/IV/references/MontgomeryYang1968E.pdf','Complete publisher preview, original introduction pp125–126.',
'Read the correspondence from oriented embedded three-spheres in S6 to semifree actions, the equivariant-class homomorphism to oriented homotopy seven-spheres, the surgery/free-circle correspondence and the displayed p1=(f(alpha)+4)a squared with image24Z. The source also explicitly corrects an older claim about free actions. Only these historical correspondences and normalization enter the receiving comparison; the rest of the chapter and its proofs were not opened.',
'https://page-one.springer.com/pdf/preview/10.1007/978-3-642-46141-5_4')
(P/'analysis/IV/root_source_matches.json').write_text(json.dumps(data,indent=2,ensure_ascii=False))
f=P/'analysis/bibliography_aliases.json';aliases=json.loads(f.read_text())
aliases['mapsOlbermann10']={'canonical':'Olbermann2010D','identity_evidence':'Identical author, title, journal volume10(2010), pages1905–1932 and DOI10.2140/agt.2010.10.1905; publisher primary PDF. Only the explicitly opened loci are inherited.','additional_independent_reading_credit':False}
aliases['E26']={'canonical':'mapsEngel','identity_evidence':'Identical Philip Engel manuscript title and arXiv2609.38442; compared source entry and exact current v1 original PDF. Only the separately recorded v1 loci are inherited.','additional_independent_reading_credit':False}
f.write_text(json.dumps(aliases,indent=2,ensure_ascii=False))
print('Recorded',len(data),'bounded source openings and2exact identity mappings.')
