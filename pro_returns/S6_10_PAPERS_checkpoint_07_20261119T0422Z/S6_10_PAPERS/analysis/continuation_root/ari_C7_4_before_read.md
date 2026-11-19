# ARI C.7.4: derivation written before reading either full printed proof

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.

Read before this record: the current receiving statement and its historical check metadata; the S6_09 statements C.7.2, C.7.3, C.7.4; the displayed definitions cp-periods, cp-v, cp-chi, cp-positive-centre, cp-MTdim, cp-real-linear; the attached Bertolin–Philippon–Saha–Saha source, especially Conjecture WSA-V2 and its deduction and Remark 4.13. Neither the original C.7.4 proof nor the receiving C.7.4 proof has yet been read. This record checks the source's actual implication with its named hypothesis; it introduces no new conjecture.

## Derivation from the cited statements

1. The compact-character formula in C.7.2 identifies an algebraic value of N(P) with an algebraic lift R of P in the maximal compact subgroup of the extension G_P. Algebraicity of the required positive modulus follows from the formula for chi: |r| = |wp'(u)| N(P)^2 |Delta|^(-1/6). The factors |a| for a algebraic are algebraic, since |a|^2=a conjugate(a). A positive algebraic number r gives an algebraic fibre coordinate. Thus an algebraic norm would supply the algebraic 1-motive M_R=[Z -> G_P] used in the source statement.

2. Write h_j=zeta(u) omega_j-eta_j u for the extension's two period entries. The determinant of the system h_j=omega_j zeta(u)-eta_j u is the nonzero Legendre determinant eta_1 omega_2-eta_2 omega_1, up to the stated sign convention. Hence u and zeta(u) belong to the field of the complete period matrix of G_P. Applying the same inversion to its conjugate places conjugate(u) and conjugate(zeta(u)) in K_0. The displayed real-linear formula for eta(u) has nonzero determinant omega_1 conjugate(omega_2)-conjugate(omega_1) omega_2. Therefore eta(u), its conjugate, and the right side of cp-relation all belong to K_0.

3. The maximal-compact condition annihilates the real homomorphism Re(v-(zeta(u)-eta(u))u). Adding its complex conjugate gives v+conjugate(v)=u zeta(u)+conjugate(u) conjugate(zeta(u))-u eta(u)-conjugate(u) conjugate(eta(u)). Thus the two central logarithm coordinates satisfy a K_0-linear affine relation whose linear functional is ell(z_1,z_2)=z_1+z_2.

4. In the doubled motive the base projection P is already among the algebraic extension parameters Q: for G_P x G_conjugate(P), Q consists of (P,0) and (0,conjugate(P)), and the point below R is their sum. Accordingly B_Q has dimension zero, directly from the B_Q definition in the opened source. The generalized logarithms other than the two central coordinates belong to K_0 by step 2. The Relative Semi-abelian Conjecture WSA-V2 therefore requires transcendence degree at least dim Z over K_0, while the algebraic period-torsor relations bound the central logarithm locus by dim Z.

5. The central additive action associated to the bracket group in C.7.3 translates (v,conjugate(v)) along the full plane when the two generators are independent; on the rank-one branch it contains the line (1,c) with c=a a^dagger/d>0. The sum functional evaluates to 1+c, which is strictly positive, on that vector. Thus the affine relation in step 3 is nonconstant on the connected central fibre and cuts its dimension by at least one. The resulting upper bound dim Z-1 contradicts the source conjecture's lower bound dim Z. An extra quotient central torus does not remove this cut: the bracket line remains inside the full central tangent space.

6. Consequently the algebraic-norm assumption cannot hold together with the source's explicitly named relative conjecture for these algebraic lifts. The full period conjecture supplies that relative inequality by the opened source's Proposition lem:equivWSA-V2-GPC. For the conductor-361 point this applies once its algebraicity and nontorsion statement are used. The named period conjecture remains open in that case. The implication is the original C.7.4 assertion, whose proof is to be compared next.

## Specific comparison obligations

- Check the central coordinate identification: the analytic conjugate coordinate must be identified with the second algebraic Tate direction without silently changing the sign of its bracket.
- Check that the cited source's B_Q and Z concern the same doubled motive and not an unrelated extension.
- Check that the dimension cut is a relation on the actual period torsor, not merely a numerical real relation without algebraic coefficients; K_0 must contain every coefficient, as established in step 2.
- Check the real-embedding handling. The doubled argument above avoids presuming that an arbitrary algebraic compact lift is fixed by conjugation. The real case may instead be treated using a real algebraic lift and the single central direction, with its logarithm conjugation equation explicitly stated.

No comparison outcome is asserted by this before-read derivation.
