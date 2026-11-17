"""Record the actual source passages opened and matched during Paper II editing.
This script stores a manual reading record; it does not verify proofs.
"""
from pathlib import Path
import json
D=Path(__file__).resolve().parents[2];p=D/'work/root/references_verified.json'
rows=json.loads(p.read_text())
items=[
 {'keys':['BirkenhakeLange1999'],'source':'https://www.scribd.com/document/600709618/Complex-Tori-Birkenhake-Lange','locator':'Original book Chapter1 section2, pp5–8, Appell–Humbert Theorem2.1 p7','verification':'Opened original book reproduction, pp6–7 semicharacter, canonical factor and quotient line bundle; Theorem2.1 exact-sequence isomorphism. Arbitrary complex torus V/Lambda, integral imaginary Hermitian form, unitary semicharacter. Matched the alternating integral Chern cocycle and factor-of-automorphy commutator in analytic_picard_completion.tex; no projectivity or positivity is assumed. Web refs turn253view0,turn254view0. Publisher metadata checked at Springer DOI10.1007/978-1-4612-1566-0.'},
 {'keys':['Cartan1957'],'source':'https://www.numdam.org/article/BSMF_1957__85__77_0.pdf','locator':'Section2, fundamental theorem(B), printed p80; Theorem1 p81','verification':'Original PDF opened and exact hypotheses read. Coherent sheaf on a Stein manifold has Hq=0 forq>=1. The finite product annulus times two discs in the WB cusp proof is Stein, and the structure sheaf is coherent. The source citation p81 for the fundamental theorem was off by one: p81 contains the closed-subset Stein-neighbourhood extension. Printed citation normalized to p80. The exponential sheaf sequence and H2(Z)=0 give Pic=0 in full in-paper reasoning. Web refs turn249view0,turn253view2.'},
 {'keys':['Bingener1980'],'source':'https://www.numdam.org/article/ASENS_1980_4_13_3_317_0.pdf','locator':'Satz6.2, printed p337, definition/setup pp336–337','verification':'Original PDF statement and beginning of proof read. Proper flat holomorphic map, cohomologically flat in dimension0, represents the relative Picard functor by a possibly nonseparated complex space. This is background representability; it gives no closedness/properness of a torsion locus. The WB explicit local obstruction does not infer a global count from representability. Web refs turn249view1,turn253view3.'},
 {'keys':['CoxLittleSchenck2011'],'source':'https://pi.math.cornell.edu/~tsh/cornell-only/cox-little-schenck-toric.pdf','locator':'Original 2010 preprint: Example1.2.21 p31; Propositions4.1.1–4.1.2 p171; Theorem4.2.8 p181; Theorem4.2.12 p184','verification':'Opened complete indicated statements and proofs: primitive ray gives C times (C*)^(n-1), character valuation equals pairing with primitive generator, divisor is sum of pairings, invariant Cartier data are cone-wise integral characters agreeing on faces, support functions encode them with the source minus-sign convention. Applied to finite smooth toric cusp charts and integral lattice after finite base change. No algebraic Picard statement is substituted for arbitrary analytic Picard triviality; that step uses Cartan and the exponential sequence. Root source pages181/184 replace draft179/182. Web refs turn257view3,turn258view0,turn258view1,turn258view2. Earlier scopes in maps source records remain separately valid.'}
]
for item in items:
 item.update(status='verified in the specified scope',reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November2026')
 for i,r in enumerate(rows):
  if r.get('keys')==item['keys'] and r.get('source')==item['source']:
   rows[i]=item;break
 else:rows.append(item)
p.write_text(json.dumps(rows,indent=2)+'\n')
(D/'work/root/II_working_sources.bib').write_text(r'''@book{BirkenhakeLange1999,
 author={Birkenhake, Christina and Lange, Herbert},
 title={Complex Tori},
 series={Progress in Mathematics}, volume={177},
 publisher={Birkh\"auser}, year={1999},
 doi={10.1007/978-1-4612-1566-0}
}
@article{Cartan1957,
 author={Cartan, Henri},
 title={Vari\'et\'es analytiques r\'eelles et vari\'et\'es analytiques complexes},
 journal={Bulletin de la Soci\'et\'e Math\'ematique de France},
 volume={85}, pages={77--99}, year={1957},
 url={https://www.numdam.org/article/BSMF_1957__85__77_0.pdf}
}
@article{Bingener1980,
 author={Bingener, J\"urgen},
 title={Darstellbarkeitskriterien f\"ur analytische Funktoren},
 journal={Annales scientifiques de l'\'Ecole Normale Sup\'erieure},
 series={4},volume={13},number={3},pages={317--347},year={1980},
 doi={10.24033/asens.1385}
}
''')
(D/'records/II_working_citation_normalizations.json').write_text(json.dumps({'opened':items,'replacements':[{'source':'Lee2024 Proposition6.28 and(6.35–6.36),pp180–182','state':'Not opened in full; author metadata only','action':'Replace redundant citation with the explicit exponential sheaf exact sequence, its cohomology exact segment, Cartan1957p80 and elementary H2 vanishing. Source text and original citation remain in provenance.'},{'source':'Fulton1993 sections2.1,3.3,3.4','state':'OnlyChapter1 was previously verified; the newchapterlocations notopened','action':'Use the opened CoxLittleSchenck2010preprint propositions and theorems for exactly the same ray-chart and Cartier claims. Record source edition/page normalization; do not claim FultonCh3verification.'}]},indent=2)+'\n')
print('Stored',len(items),'scoped original-source openings and two transparent citation replacements')
