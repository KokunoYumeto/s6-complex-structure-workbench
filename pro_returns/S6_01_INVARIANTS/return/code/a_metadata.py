"""Write the Part A statement register and source/provenance records."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
data=[
('A1.0','Structure-sheaf direct images, fixed gamma subbundle, finite eigencharacters, and cusp cup product in the form used here.','Proved','Explicit local models; modular discriminant; root-curve Picard presentation; fibrewise duality','A.1','F1','Independent determinant-line derivation: the vertical quotient has twelfth power Delta inverse with one cusp pole, hence root line R^(-1); duality and exact cyclic invariants give the coarse O(-1). No reliance on AC26 Proposition 9.13.'),
('A1.1','Logarithmic cotangent bundles are locally free at all strata; det E=omega_f(-2S1-3S2) and 0->det E->E->O->0.','Proved','AC26 local construction; toric charts','A.1','F1','Includes both triple points, all double curves and finite etale descent.'),
('A1.2','Rq E=(O+O(-1),O^2+O(-1)^2,O+O(-1)) by O(2S1+3S2) and fibrewise duality.','Proved','A1.0;A1.1','A.1','F1','Independent global method: vertical line-bundle upper modifications followed by duality, not the workbench tensor-lattice filtration.'),
('A1.3','All six Rq Omega1/Omega2 are computed; Omega1 images O(-2),O+O(-1)^2,O+O(-1), and Omega2 images O(-2)+O(-1),O(-2)+O(-1)^2,O.','Proved','A1.2;A2.1;A2.2;A2.4','A.1','F1','Full residue torsion cancellation and relative duality are spelled out.'),
('A2.1','Exact determinant identity 6 mu_z^2-tau_z beta_z=tau_z^2 E4(tau)^2/E6(tau); orders2,0 at z1,z2 and coarse divisor p1+p2.','Proved','AC26 period laws and regularity; classical modular zero facts','A.2;A.1','F1;F19','Descent through the normal closure of g2^2 is proved; no coarse degree count is used.'),
('A2.2','In the specified fourth-root coordinate mu_s(0)=0.2366093140807852246877051134504496062943... i, with exact gamma expression and order-three K coefficient.','Proved','A2.1;A2.3 for independent geometric proof','A.2','F1;F19','100-digit E4 Fourier and independent Abel-period quadrature agree; wp Newton symmetric derivative agrees past30 decimal places. Nonvanishing is analytic, not numerical.'),
('A2.3','The period section is +/- P*; wp(mu,tau)=0; the Eichler-Zagier formula is correctly normalized and an exact Duke-Imamoglu branch is given; mu-(2-tau)/3 has order2 at z1.','Proved','AC26 period laws; Engel Section2; EichlerZagier1982 theorem; DukeImamoglu2008 Theorem1','A.2','F5;F19','Own rational-section logarithm cocycle and explicit height projection establish identification; x(3P*) has limit512/81.'),
('A2.4','kappa1 is sheaf-surjective, its global rank is1, signed value on h gamma is -mu_s(0)/4, and Lead2 equivalence holds.','Proved','A1.2;A2.1;A2.2','A.2;A.1','F1','The invariant target frame is corrected by a unit normalized to1 at the centre.'),
('A3.1','The complete Hodge table is h01=h32=1,h11=h22=2,h12=h21=1, endpoints1, others0, for every admissible c.','Proved','A1.0;A1.3','A.3','F1','Obtained from the six sheaves by Leray, not by Euler consistency.'),
('A3.2','Explicit Leray associated-graded generators, trace duals, base Cech class and eta relative class; global Dolbeault lift Q restricting to eta exists.','Proved','A1.3;A2.4;A3.1','A.3','F1;F7','Leray lifts are noncanonical with their exact ambiguity named; no elementary coefficient formula for Q is claimed.'),
('A4.1','Relative Omega^p local modules for t=xy,t=xyz,t=s^m, including torsion-free degree1 at cusp and explicit degree2 cusp torsion.','Proved','Local analytic algebra','A.4;A.1','F1','Exact syzygies and polynomial relations checked in code.'),
('A4.2','AC26 Remark9.21 cusp torsion claim for Omega1 is false; support is S1 union S2. Remark1.3 must distinguish p=1 from p=2.','Refuted','A4.1;finite etale comparison','A.4','F1','Authority PDF pages5 and81 visually inspected; transcription4330 and workbench984-1006 precisely located. No workbench numerical Hodge value is refuted.')
]
rows=[]
for id,statement,status,depends,item,findings,notes in data:
    rows.append(dict(id=id,statement=statement,status=status,where_proved='fragments/part_A.tex, Statement '+id,depends_on=depends,item_of_the_prompt=item,findings_of_the_survey_settled=findings,notes=notes))
(root/'outputs/part_A_statements.json').write_text(json.dumps(rows,indent=2)+'\n')
(root/'outputs/part_A_references.bib').write_text(r'''@article{EichlerZagier1982,
  author = {Eichler, Martin and Zagier, Don},
  title = {On the zeros of the {Weierstrass} {$\wp$}-function},
  journal = {Mathematische Annalen},
  year = {1982}, volume = {258}, number = {4}, pages = {399--407},
  doi = {10.1007/BF01453974},
  url = {https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01453974/fulltext.pdf},
  note = {Verified: original PDF opened; theorem on page 399 checked, 12 November 2026}
}
@article{DukeImamoglu2008,
  author = {Duke, William and Imamo{\u g}lu, {\"O}zlem},
  title = {The zeros of the {Weierstrass} {$\wp$}-function and hypergeometric series},
  journal = {Mathematische Annalen},
  year = {2008}, volume = {340}, number = {4}, pages = {897--905},
  doi = {10.1007/s00208-007-0174-3},
  url = {https://www.math.ucla.edu/~wdduke/preprints/},
  note = {Verified: attached full PDF opened; Theorem 1 and equation (6) read; author publication list confirms journal metadata}
}
''')
(root/'outputs/part_A_sources.md').write_text('''# Part A source and calculation record

## Sources actually read

- Entire attached development prompt.
- Entire `workbench/hodge_frolicher.tex`, with particular attention to lines218-1188.
- Original AC26 transcription: Definition3.1 and Theorem3.4; Lemma3.10; Section9.3 Proposition9.13 and its full proof; canonical line statements; Remarks1.3 and9.21. Original PDF pages5 and81 rendered and visually inspected: the claimed degree-one relative torsion along W appears in the authority itself.
- Engel attached PDF, Section2 and its Weierstrass equation, Mordell-Weil and fibre description; Lemma2.1 and its height computation; relevant topology/linearization passages.
- Attached Duke-Imamoglu PDF: introduction, Theorem1, equations(4)-(6), and Section2.
- Eichler-Zagier original PDF opened from the author's official MPIM page; theorem on printed page399 and both proofs read via extracted text. Formula coefficient, denominator and path checked against Duke-Imamoglu equation(6).
- Course `cusp-and-compact-threefold.md`, Sections9-11 and13: read as untrusted comparison material. The rational-section cocycle and height argument were independently checked and written with explicit reductions.
- Reader B notes opening source index and Hodge references; survey findings F1,F5,F19.

## Searches

Web searches on12 November2026 included `Shioda 1990 On Mordell Weil lattices Theorem8.6 pdf`, `Eichler Zagier On the zeros of the Weierstrass function 1982 pdf`, exact Shioda title with8.6, and exact Duke-Imamoglu title/year/DOI. Original Shioda PDF fetch returned HTTP429; indexed author-upload text exposed the height formula. It is not used as an unexamined authority in the proof: the needed height calculation is derived directly from the E6/A1 intersection matrices. No priority claim is made. Root literature searches cover newer S6 papers.

## Computations actually run

`code/a_calculations.py` and its complete `outputs/a_calculations.txt` include exact covariance residuals for g1,g2,g2_squared, invariant exponents for(3,2),(4,1),(9,6),(20,5), exact triple-chart torsion syzygies, exact E6 Cartan inverse, and elliptic addition formulas for2P* and3P* with zero curve-equation residuals.

At100 decimal working digits it evaluates the order-four scalar by an E4 divisor-sum Fourier series and an independent Abel-period quadrature. Gamma and Duke-Imamoglu hypergeometric evaluations agree as additional checks. A separate Newton solver evaluates two nearby Weierstrass zeros using the wp Fourier expansion, for s=10^-5,10^-10,10^-15; the symmetric derivative agrees to31 decimal places at the last step. The order-three K coefficient is computed from independent E6 Fourier and Jacobi-theta evaluations. These are numerical corroborations, not interval certificates; analytic proofs establish nonzero values and exact orders.

An initial Sympy structural equality assertion for the already equal factorizations of x(3P*) failed because multiplication trees differed. Replacing it with exact factor(left-right)==0 passed; no mathematical formula was changed. The final rerun output is attached in full.

## Decisions and corrections

The workbench's cotangent direct images and h12=1 are confirmed by a different global computation: calculate O(2S1+3S2), apply relative duality to detE, and use the globally nonzero logarithmic vertical vector. A second independent modular identity determines the full period determinant. The scalar is normalized to a named fourth-root coordinate; the prompt's equation t-1=s^4 alone leaves four possible phases, while the workbench's ds/dz=1 normalization is different.

AC26 Remark9.21, transcription line4330, is false about Omega1 relative torsion at W. The corrected local modules prove torsion exactly at the two multiple fibres. Degree2 has cusp torsion, so Remark1.3's plural wording needs this distinction. The workbench's lines984-1006 are correct in degree1.

All four A items have proofs in the fragment. Explicit generators are supplied in the requested Leray associated-graded sense; lifting the second H11 class has exactly the stated one-dimensional ambiguity. No elementary atlas coefficient formula for a distinguished global Q is claimed.
''')
print(f'Wrote {len(rows)} Part A statement rows, two verified bibliography entries, and source record.')
