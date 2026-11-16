"""Integrate the unrestricted irreducible classification and source audits."""
from pathlib import Path
import csv
from datetime import datetime, timezone
root=Path(__file__).resolve().parents[1]
p=root/'records/root_results.csv'
with p.open(newline='') as f:
    rd=csv.DictReader(f); fields=rd.fieldnames; rows=list(rd)
new={
 'id':'C.2.UN.12',
 'statement':'Complete zero-Euler criterion and nonnegativity for every irreducible torus-degeneration support without ambient Betti assumptions',
 'status':'Proved',
 'where_proved':'sections/part_C2_irreducible_zero.tex',
 'depends_on':'C.2.UN.5; C.2.UN.7; C.2.VII.1-4; A.5.17; exact normalization-complement isomorphism',
 'item_of_the_prompt':'C.2',
 'findings_of_the_survey_settled (F-numbers)':'F16',
 'notes':'Normal supports are tori or bielliptic; noncontracted irrational ruled supports have the four constant elliptic conductor types; rational and contracted irrational cases have e>=2. Class VII zero criterion is b2(Z)=r with exact conductor branch patterns. A5.17 removes both old exceptional terms outside conductor. This classifies actual irreducible fibres, with no abstract gluing smoothability claim.'}
rows=[r for r in rows if r['id']!=new['id']]+[new]
for r in rows:
    if r['id']=='C.2.G.1':
        r['depends_on']+='; C.2.UN.7; C.2.UN.12'
        r['notes']='All singularities and multiplicities. Irreducible rational normalization contributes two and every other irreducible support zero. Contracted irrational sections are excluded by UN7 and D1.9. Reducible equality is exactly the smooth minimal Hopf/elliptic and elliptic unramified-conductor geometry. Independent audits accepted.'
with p.open('w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=fields); wr.writeheader(); wr.writerows(rows)
p=root/'S6_03_CDP_report.md'
s=p.read_text()
lines=s.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| C.2 |'):
        lines[i]=('| C.2 | C2a–C2d; C.2.NC.1–5; C.2.VII.1–4; C.2.INT.1–3; '
        'C.2.RAT.1–9; C.2.IRR.1; C.2.D4.1–3; C.2.CR.1–6; C.2.MH.1–4; '
        'C.2.G.1; C.2.UN.1–12; A.5.18–21 | The full CDP sign and geometric equality '
        'theorem is proved for every singularity and multiplicity: every fibre Euler number '
        'is nonnegative and c3 is 0 or 2. Contracted irrational sections are now excluded '
        'entirely under these hypotheses. Without the CDP assumptions, the exact Euler '
        'range is 2Z, and every irreducible fibre is nonnegative with a complete zero '
        'criterion in UN12. Normal supports are smooth tori or bielliptic surfaces; '
        'the nonnormal zero cases have the specified elliptic ruled conductor types or '
        'exact class VII equality data. Rational and contracted irrational irreducible '
        'supports have Euler number at least 2. UN11 gives the full 19-row cyclotomic '
        'stratum-signature table. Universal zero-Euler refinements and essential Kodaira, '
        'Hopf and properly elliptic components are constructed. The remaining unresolved '
        'clause is the unrestricted geometric classification of all reducible zero-Euler '
        'supports; neither the signature table nor cofinal refinements are presented as '
        'that classification. |')
s='\n'.join(lines)+'\n'
s=s.replace('C.2.MH.3 now proves Euler number zero in this contracted case.',
  'C.2.MH.3 gives the necessary zero equation in that contracted case; the later '
  'C.2.UN.7 proves its strict positivity and trivial fundamental group, thereby '
  'excluding the case completely under the CDP hypotheses. The earlier equations '
  'are retained as proved necessary reductions, without an existence assertion.')
s+='''
## Unrestricted fibres: the irreducible classification and the remaining reducible problem

C.2.UN.5 classifies every normal irreducible support: it is smooth and is a torus or bielliptic surface, with the exact cyclic cover, canonical-order multiplicity constraint and compact realizations. C.2.UN.7 proves the strict-transform A'Campo identity m e(S_reg)=det(I−T^m), using the proper analytic boundary construction and its actual nearby-cycle spectral sequence. Every exceptional multiplicity is at least 2m. The SNC stalk calculation proves quasi-unipotence, so the determinant is nonnegative. A nonzero integral degree-one class on a support extends to a tube and injects rationally into a nearby torus; the finite-character proof then gives Euler 2 for rational normalization and 2−2g for ruled normalization. The conductor pushout excludes zero for every rational normalization and proves that every contracted irrational section has positive Euler number and trivial fundamental group. The latter cannot occur under CDP hypotheses. The source was read directly in A'Campo's original journal scan, Section 2 and the trace computation on pages 243–244.

C.2.UN.12 assembles a complete unrestricted irreducible zero criterion. The normal cases are exactly those of UN5. The irrational ruled cases have smooth minimal elliptic ruled normalization and one of four constant transversal conductor types: node, cusp, tacnode or ordinary triple point, with elliptic conductor-cover degrees 2, 1, 2 or 3. The class VII case has the exact equation e(S)=b2(Z)−r+e(C), where r counts rational resolution-conductor components. Every normalization singularity outside the conductor is excluded by the actual isolated Milnor-sphere comparison, so both older exceptional correction terms vanish. Zero holds exactly for b2(Z)=r and the displayed conductor branch/delta patterns. These are equivalences for fibres of the given map; no claim that arbitrary abstract gluings are smoothable is made.

C.2.UN.11 computes all 19 cyclotomic possibilities for orientation-preserving rank-four integral quasi-unipotent monodromy and every associated open-stratum Euler sum. The code verifies the full exterior-power zeta identities and Möbius inversion over the integers and Q(t). A nonreduced irreducible fibre necessarily has e(S_reg)=0; positive smooth-locus Euler forces multiplicity one. The earlier provisional coarse bound m<=16 has been strengthened by this exact argument and is not used as the final conclusion.

C.2.UN.4 proves that every filling has vertical smooth blowup refinements of every even Euler number, with exact point and plane-quartic comparisons; its zero refinements are cofinal. C.2.UN.6 constructs essential properly elliptic components in infinitely many non-bimeromorphic zero-Euler fillings of one fixed punctured product. Its weighted Hopf threefold map [a,b,c] -> [a^m:b:c] refutes the connected-root-cover conclusion and divisibility assertions of Fujimoto (1988), Theorem 2.8, as printed. The exact printed hypotheses, quotient map and disconnected normalization of the proposed root cover are checked. That paper's Example 3.4 is cited for the prior occurrence of Kodaira-dimension-one components.

C.2.UN.8 uses the known Namikawa cuspidal self-product, compared with Rossi (2017), Proposition 4 and Remark 5. Its six irreducible rational-normalized supports have integral cohomology (Z,0,Z^4,0,Z), trivial fundamental group and Euler number 6. The compact ambient rational Betti numbers are (1,0,21,8,21,0,1). Explicit graph blowups, the quotient cofibration, the sextic-base-change Picard comparison and two independent audits verify these numbers. This example disproves extension of the nonzero local-character premise beyond its hypotheses. No priority is claimed for the construction or ambient Hodge numbers.

The CR4 pinch calculation has been numerically corrected: the Hirzebruch spherical class in Y^3+x^2 Z has square -4, not -2, and is supplied by a continuous sphere map; embeddedness is not asserted. Its nonzero square is the property used by the transport proof. The isolated Morse sphere in UN5 remains an embedded sphere of square -2. UN9 proves product-node rigidity with uniform compact-boundary transport, and UN10 gives the unrestricted genus-one conclusion for contracted irrational sections. All earlier source passages remain recoverable in the immutable preceding checkpoints.

The sole remaining requested clause is an exhaustive geometric classification of unrestricted reducible zero-Euler supports. The irreducible classification, the finite numerical signature table, the universal refinement theorem, and explicit non-bimeromorphic essential-component examples are proved progress on it. They do not supply the missing exhaustive analytic gluing and modification description. The ongoing attack examines which essential component types and interfaces can occur, while retaining the full nonreduced fibre and its actual map.
'''
p.write_text(s)
with (root/'records/visual_qa.md').open('a') as f:
    f.write('''
## 18:24 UTC build and inspection

The build `root_build_1824.out` compiled 162 statements into 235 pages. All four stages exited zero, with zero TeX errors, overfull boxes, unresolved references and missing glyphs. The root inspected rendered pages 107, 110, 129, 131 and 132, covering the new cusp-product statement and source comparison, properly elliptic example, node transport, contracted-genus comparison and normal-support classification. The split cusp-product display fits; all inspected pages are legible without clipped or overlapping material. UN7, UN11 and UN12 will be rendered after their final integration.
''')
print('Integrated UN12 and sharpened G1; remaining unrestricted classification is reducible.')
print('UTC:',datetime.now(timezone.utc).isoformat())
