"""Record the precise primary-source readings completed on 18 November."""
from pathlib import Path
import json, hashlib, re

P=Path(__file__).resolve().parents[2]
f=P/'analysis/I_sources/current_source_matches.json'
data=json.loads(f.read_text())
checks={
 'CrRubin1999': ('Definition5.1/Proposition5.3 and proof p15; maximal-order convention p16; Theorem10.1 and complete Section10 argument pp47–50.',
 'Coates–Wiles central-value/rank implication, with the explicit isogeny to maximal order. Applied by contrapositive to the nontorsion points already verified; it supplies no rank-one leading-factor formula.'),
 'CrGrossZagier1986': ('Original MPIM85-30 preprint: I.7.3 pp11–12 (PDFspread8) and its final proof V.2 p129 (PDFspread67), both opened visually; setup pp125–126 and TheoremV.2.1 p127 read in extracted text.',
 'The rational nonzero factor connecting the derivative, a rational point height and a rational differential period. The exact trace and period-product step on p129 is matched; the surrounding BSD conjectures are not assumptions in the receiving proof.'),
 'CrGross1991': ('Original scan: Section1 setup/formula1.1 p235; Theorem1.3 p236; opening of Section2 p237. PDFspreads1–2 opened visually.',
 'Rank one and finite Tate–Shafarevich group from a nontorsion Heegner point. The non-CM restriction starts in the subsequent illustrative proof, not in Theorem1.3. No full re-proof of Kolyvagin is claimed.'),
 'CrJetchev2008': ('arXiv:0707.0032v1, Introduction Theorem1.1 p2.',
 'Primary research statement of equality of analytic and Mordell–Weil ranks for the verified simple-zero rows. Finite Sha is supported separately by Gross Theorem1.3.'),
 'miller2011': ('arXiv:1010.2431v3: Definition1.1/Theorem1.2 p2; isogeny-invariance explanation p2; Section7 opening/Theorems7.1–7.2 p16; complete exception Table9 p23 and its setup p22.',
 'The three analytic-rank-one curves have conductors3136,3136,361, below5000 and outside every exception conductor. This proves full BSD for those curves; the separate exact local data and certified height/derivative intervals isolate the positive integer Sha order as1.'),
 'CgzStein2007': ('Author-hosted book: Theorem9.18 and complete proof pp171–173; Corollaries9.19–9.20 pp173–174 (PDFpp185–188).',
 'Sturm coefficient bounds, including fixed character. The receiving characteristic-zero identity follows also from its displayed coset-product/valence proof; all coefficient comparisons reach the required bounds.'),
 'CrBDP2012': ('Published PDF: Introduction setup p261 and Theorem1 with all preceding prime/CM hypotheses p262 (PDFpp2–3).',
 'The Katz p-adic value/formal-logarithm identity modulo K-star in analytic rank one at a split good prime for maximal-order CM. Corrected the bibliography title to the exact title in this DOI-bearing PDF.'),
 'CrCastella2025': ('Current author PDF: TheoremA/Remark1.1.1 p2; period conventions and L(E/K)=L(E/Q)^2 explanation p3.',
 'Recorded all full-CM, abelian torsion-extension, split-prime, p prime to6hK and conductor, and exact-different hypotheses. This is a bounded source check of the stated context, with no extension to the excluded -16 application or the inert prime3 in the last row.')
}
for key,(locator,scope) in checks.items():
    p=P/'analysis/I_sources'/(key+'.pdf')
    data[key]={'exact_locator':locator,'scope':scope,'source_path':str(p.relative_to(P)),
               'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
               'date':'2026-11-18','checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro',
               'verification':'opened and matched at listed scope'}
f.write_text(json.dumps(data,indent=2,ensure_ascii=False))
f=P/'S6_10_PAPERS_references.bib';s=f.read_text()
old='Chow--{H}eegner points on {CM} elliptic curves and values of {$p$}-adic {L}-functions'
new='{$p$}-adic {Rankin} {L}-series and rational points on {CM} elliptic curves'
s=s.replace(old,new);f.write_text(s)
print('Recorded',len(checks),'exact primary-source matches; corrected BDP title.')
