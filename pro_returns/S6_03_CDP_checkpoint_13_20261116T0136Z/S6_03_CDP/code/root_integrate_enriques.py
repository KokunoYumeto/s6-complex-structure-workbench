"""Record the complete root audits of UN25/26 and update the living report."""
from pathlib import Path
from datetime import datetime, timezone
import csv

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
audit = f'''# Root proof audit: Enriques occurrence and intrinsic rank-one fields

UTC: {stamp}

The root read the entire final UN25 source, its support-cohomology input, the discriminant/chart computation source and both saved exact computation outputs. The compact Weierstrass model has precisely the displayed degree-twelve squarefree discriminant. Substitution x=1+xi gives y²−xi²(3+xi)=T[1+T³(1+xi)+T⁵], so the written coordinates give XY=T exactly and have nonzero coordinate Jacobian. The quadratic resolution and its involution are actual charts, and all four root centres occur in exchanged pairs away from the two nodes. The signed divisor and section-preserving dualization have square one and conjugate the infinite cyclic contraction to its inverse. The exact product cover has free eta, while k has sixteen fixed points and eta k is free. The resulting intermediate Kummer resolution carries a free eta involution, including paired exceptional curves, so its quotient is the stated Enriques surface. The two ambient A1 charts restrict to its eight minimal surface resolutions. Their base monomials give every full-fibre coefficient and establish SNC. The global fixed curves at infinity and the other nodal values have zero-Euler supports. Six negative blocks can be placed in the open exceptional ruled surfaces away from M and leave M unchanged. This completes the exact compact occurrence argument. Root audit: PASS.

For the support, the actual incidence complex has degree-zero ranks7 and8. The ten rational curves on M have direct-sum affine-D4 intersection form; its two-dimensional numerical kernel consists of the two full fibre vectors. Equality and nonvanishing of the fibre classes give exactly one homology relation. The full curve-to-component map then has two kernel parameters, namely the equal half-fibres and the difference of the I0* fibres, and rank14. The Hopf-to-elliptic H1 maps have separate rank-one images. All higher differentials have zero targets. This gives b(S)=(1,1,8,4,8), h(O_S)=(1,1,0). The existing exact modification maps give b(Sbal)=(1,1,20,40,20), coherent dimensions unchanged. Root audit of the full fragment: PASS.

The root read the entire UN26 proof. Proper coherence and torsion-freeness give an actual rank-one bundle q_*omega. Curve Riemann-Roch supplies its meromorphic section; evaluation and contraction by the resulting meromorphic two-form give a global vertical field across critical fibres, with the displayed coordinate-change identity. On the dense regular-fibre locus its time form is a nonzero elliptic differential, so every constant combination of V and hV is complete there. The exact closedness theorem previously checked in Guillot2024 extends semicompleteness to the full holomorphic locus. The finite map h on B has q as the connected-fibre Stein factor of hq. In the equivariant case the finite orbit span gives an eigenvector and a function from B/G gives a stable two-dimensional space; the same fibre and Stein maps prove all claims. Root audit: PASS. E and A independently accepted this proof.

The new example proves occurrence of its specified Enriques surface, not occurrence of every Enriques surface. UN26 proves the scope of the intrinsic field condition, not an arbitrary elliptic-surface filling construction. The main remaining issue is the actual normal-germ, period and gluing information in a torus degeneration. The proposed arbitrary central-period lifting has no comparison map and is not used. A first normal coefficient of V2−hV1 would require an extension of h beyond the central component; no such extension has been established, and the induced transverse object can carry a normal-line twist.
'''
(root / 'records/root_research_enriques.md').write_text(audit)
p = root / 'S6_03_CDP_report.md'
s = p.read_text().replace('C.2.UN.1–24; A.5.18–21', 'C.2.UN.1–26; A.5.18–21')
s = s.replace('projective/nonprojective properly elliptic and Kummer K3 components are constructed.', 'projective/nonprojective properly elliptic, Kummer K3 and Enriques components are constructed.')
s += '''
## Enriques occurrence and the exact rank-one limitation

UN25 constructs an explicit compact torus fibration containing a smooth Enriques component. The base equation, signed root charts, cyclic component cover, finite quotient and ambient resolution are all written, and their finite calculations are executed. Before balancing, the full central divisor is 2M+2A+4Q1+4Q2+E1+E2+E3+E4, where M is Enriques, A is P1×P1, the Qj are primary Hopf surfaces and the Ei are F2. The initial reduced support has Euler12 and Betti numbers (1,1,8,4,8). Six exact vertical modification blocks away from M give Euler0 and Betti numbers (1,1,20,40,20), retaining M itself. Both supports have h(O)=(1,1,0). The complete source and support cohomology passed root and independent team audits. This establishes the specified Enriques occurrence; the general occurrence question remains open in this INCOMPLETE report.

UN26 proves that every compact elliptic surface has a two-dimensional space of commuting semicomplete meromorphic vector fields of generic rank one, with its elliptic map recovered by the actual Stein factor of their ratio. The space can be chosen stable under every specified cyclic fibration action. Thus the intrinsic field-space restrictions alone allow every elliptic surface. The remaining occurrence analysis must retain normal-germ and period data from an actual degeneration; an unproved extension of a central meromorphic function or central period is not used.

Checkpoint07 was created at2026-11-15T19:38:33.117566+00:00 with952members,382478790bytes and SHA-25647ce227813415511ab7a60db56bd6b1bb8a34867549b6501cef076709523fb4c. Its PDF cutoff is explicitly throughUN24; the complete UN25/26 sources and source-specific metadata are included. The saved receipt confirms successful creation under the new filename. The next hourly checkpoint and progress review are due20:36UTC.
'''
p.write_text(s)
for name, identifier in [('E_critical_results.csv','C.2.UN.25'),('D_results.csv','C.2.UN.26')]:
    path = root / 'records' / name
    with path.open(newline='') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    for row in rows:
        if row['id'] == identifier:
            row['notes'] += ' Root read and accepted the complete final source, all exact comparison maps and available computation outputs at19:41UTC.'
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
print('Root full-source audits UN25, UN26: PASS. Report and source-specific CSV updated.')
