"""Record seven complete mathematical argument reviews and exact receiving edits.

The reviewer read every source block and re-derived the displayed arguments.
The script records that work; its execution itself grants no proof credit.
"""
from pathlib import Path
import csv,hashlib,json
P=Path(__file__).resolve().parents[1];ROOT=P.parents[1]
idx=json.loads((P/'analysis/inventory_source_index.json').read_text())
source=(ROOT/'sources/s6_09/S6_09_PAPERS_II.tex').read_text()
outcomes={
'C5a':'Full branch-normal quotient, coordinate-change descent, immersion determinant, twisted exact sequence, finite pushforward and compact-surface Serre pairing read and rederived. The target is H0(nu*(K_Y tensor L^-1)) dual and its image is the stated boundary kernel; no surjectivity is inferred without the exact boundary condition. DGKXv1 Lemma6.11 p81 was opened as the specific-family quotient counterpart; the short general twisted application retains that granular credit.',
'C4g':'Full three-family comparison rederived: finite ambient H2 pulls to zero in free H2(dP6), H1(O_dP6)=0 makes every pulled-back line trivial, and Serre duality gives the one-dimensional normal target. Checked the C1.3 global nonvanishing route without claiming normalization-map surjectivity; toric strata give2, elliptic-ruled conductor subtraction gives0, and the actual unibranch cuspidal normalization is a proper bijection. All full multiple fibres have the stated actual root covers and pass A3.4 including nilpotent layers. E13/E14/E19 remain named reviewed dependencies.',
'C5c':'Full nonintegral-twist proof read and rederived, including Picard cocycle equations, smooth Fourier contraction, exact local Koszul complexes, regular C^2 versus O/(s^2) modules, order-three joint coefficient123ik/(64pi), both finite-character invariant counts, cusp character acyclicity and Leray. Verified epsilon_n=0 for3|n and1 otherwise by required Taylor exponents n+2 modulo3. Added the missing explicit passage from isolated zeros for each integer tuple to existence of a nonresonant fibre, then finite coherent support. The unchanged earlier root Koszul replay is reused at its recorded scope; this review adds no second execution credit.',
'E5':'Full degree-one Leray edge and smooth-locus tangent boundary rederived. Cup product sends a eta1+b eta2 to (b u1-a u2) eta1 wedge eta2, so its rank equals the Kodaira–Spencer rank. The image section vanishes on the rank-two open set and globally by the locally free R1O theorem E4, whose exact source statement was opened. Critical ideals (z^(m-1)),(x,y),(xy,xz,yz) and the onto logarithmic map were checked; no ordinary special-fibre surjectivity was used. Smooth source and nonsingular compact base are now explicit.',
'E8':'Full theta determinant proof rederived. Adjoining(mu,beta/6) gives an exact index-six lattice enlargement and the identity-induced degree-six isogeny, preserving Kodaira–Spencer rank. Heat equation, eta derivative and h_mu=-wp-pi^2E2/3 cancel the E2 terms; differentiating wp(mu)=0 gives determinant -g2^2/(36pi^2g3). Checked root orders1 and2, the resulting determinant order2 at the order-three point, cancellation at the order-four point, and the nondegenerate cusp logarithmic diagonal.',
'E10':'Full explicit counterexample rederived: the two Hesse critical-value sets are disjoint; the fibre product and moving genus-two double-cover base change are smooth and proper. Fixing five branch points forces the infinitesimal PGL2 field to vanish while the sixth moves, so theta_C is nonzero. Relative duality/Kunneth and genus-two Riemann–Roch give the three printed cohomology rows. The exact class dg(theta_Y)=g*theta_C is nonzero by the Leray injection and obstructs fixed-target extension. Status is proved counterexample; the rejected unrestricted assertion remains false.',
'E11':'Full coprime-multiplicity tangent/Kuranishi argument rederived. The actual root morphism has sigma*O(1)=O(kl), its finite invariant pushforward is exact, and fixed affine translations preserve the vertical/H1O representations. Checked horizontal root tangent versus pulled vertical line, all low-degree vanishings, the actual horizontal-one-form extension, and weighted-monomial contradiction3k(a+2)+4l(b+2)=kl. HRR on each verified six-sphere gives h2=1; the original affine case has its direct acyclic log calculation. Fixed three critical sections kill every infinitesimal base projective motion; the nonzero scale class then forces the Kuranishi local-ring ideal to be zero. All stale PaperI Theorem3.9 references in this block are replaced by the exact canonical fam:src:A.5.2.'
}
events=[];reviews=[]
for sid,outcome in outcomes.items():
 loc=idx['S6_03_CDP:'+sid];raw=source[loc['start']:loc['end']]
 reviews.append({'label':loc['label'],'source_file':loc['file'],'start':loc['start'],'end':loc['end'],'block_sha256':hashlib.sha256(raw.encode()).hexdigest(),'date':'2026-11-18','checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro','type':'targeted proof check','outcome':outcome})
 events.append({'statement_id':loc['label'],'date':'2026-11-18','who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS','type':'targeted proof check','outcome':outcome})
f=P/'records/root_events.tsv';rows=list(csv.DictReader(f.open(),delimiter='\t'))
for event in events:
 if event not in rows:rows.append(event)
with f.open('w',newline='') as o:
 w=csv.DictWriter(o,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(rows)
(P/'analysis/II_root_seven_review.json').write_text(json.dumps(reviews,indent=2))
replacements={
'cdp:st:C5a':[
 {'old':r'\Uses{the hypotheses, notation and definitions stated here; the explicit constructions and calculations in the proof}',
  'new':r'\Uses{the local branch-normal coefficient map and adjunction; \citet[Lemma~6.11, p.~81]{DGKXv1} for the original-family quotient; finite direct image and Serre duality on the smooth compact normalization}'},
 {'old':r'\begin{proof}', 'new':r'The branch-normal quotient specializes to \citet[Lemma~6.11, p.~81]{DGKXv1} in the original family. We retain the short argument for its general ambient line-bundle twist and the exact image of its cohomology map.'+'\n\n'+r'\begin{proof}'}],
'cdp:st:C5c':[
 {'old':'The direct-image support is consequently finite, since it is a proper analytic subset of a compact curve.',
  'new':r'We verify that this analytic support is proper. Fix a simply connected disc in the regular base. For each fixed integer tuple $(n,p,q,r)$, a resonance has $r\ne0$ and $a^\prime=\kappa^t(q,r)^t\ne0$, so its zeros are isolated. Each such zero set is countable on this disc, and the union over the countably many tuples is countable. The disc has a point outside this union. At that fibre the preceding line-bundle acyclicity and tangent extension give zero cohomology in every degree. Upper semicontinuity gives a neighbourhood with the same vanishing. Each coherent higher direct image therefore has proper analytic support on the compact base curve, hence finite support. Every regular resonance lies in that support by its computed nonzero local modules, proving that $\mathcal R_z$ is finite.'},
 {'old':'A length-three summand has one invariant coefficient in every character; a length-two summand has one except for residue two.',
  'new':r'Here an invariant exponent is the required Taylor exponent modulo the stabilizer order. Thus the length-two summand retains precisely the monomials $s^j$ with $0\le j<2$ and $j\equiv n+2\pmod3$: its invariant lengths for $n\equiv0,1,2$ are $0,1,1$. A length-three summand retains one coefficient in every residue class.'}],
'cdp:st:E5':[
 {'old':'Let $g:Y\\to C$ be a proper connected-fibre map from a compact complex\nthreefold whose smooth general fibre is a two-dimensional complex\ntorus.',
  'new':'Let $g:Y\\to C$ be a proper surjective holomorphic map with connected fibres\nfrom a smooth connected compact complex threefold to a nonsingular compact\nconnected complex curve. Its smooth general fibre is a two-dimensional complex\ntorus.'}],
'cdp:st:E11':[
 {'old':'Paper~I, Theorem~3.9','new':r'\cref{fam:src:A.5.2}'}]
}
(P/'analysis/II_root_replacements.json').write_text(json.dumps(replacements,indent=2))
print('Recorded seven complete argument reviews and exact replacements; total root events',len(rows))
