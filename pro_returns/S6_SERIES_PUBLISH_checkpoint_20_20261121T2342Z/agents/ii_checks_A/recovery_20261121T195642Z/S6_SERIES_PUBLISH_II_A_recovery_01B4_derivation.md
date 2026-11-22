# Independent recovery derivation: cdp:st:A.5.14, tag 01B4

Checker identity: ii_check_a_recovery_blind. The target printed proof and B's reconstruction/proposal remain unopened. Read the original statement/input packet and its empty supplement. The only substantive cited input supplied there is the statement A.5.5 about conductor-cleared jets on a locally complete-intersection curve. The derivation below proves the genus bound and embedded delta-one step directly before applying that input. All line bundles, conductor ideals and curve maps are specified.

## The dualizing line and the structure-sheaf Euler characteristic of S

Write f^-1(c)=mS with S irreducible and reduced. Restrict to a sufficiently small disc about c, containing no other singular value, and trivialize its canonical line. The direct image f_*K_Y is torsion-free of generic rank one: multiplication by a nonzero base function is injective on sections of the line K_Y, and on a smooth general fibre the canonical line is trivial with one-dimensional H0. Thus it is a line bundle on the disc. A generator evaluates to a holomorphic canonical form on its inverse image. On each smooth nearby fibre its restriction is a nonzero generator, so its zero divisor is supported on S. Since S is irreducible, that divisor is aS for an integer a>=0. Consequently K_Y is O_Y(aS) on this neighbourhood. The full-fibre equation gives O_Y(mS) trivial there. Adjunction for the Cartier hypersurface gives

    omega_S = (K_Y tensor O_Y(S))|S = O_Y((a+1)S)|S,

so omega_S^m is trivial. The source S is a compact Gorenstein surface because it is a reduced Cartier hypersurface in the smooth threefold.

The rational class c1(O_Y(S)) vanishes since H2(Y,Q)=0. The Cartier exact sequence 0 to O_Y(-S) to O_Y to O_S to 0 and analytic Hirzebruch–Riemann–Roch therefore give chi(O_S)=0: the two line bundles on Y have identical rational Chern characters. Since S is compact, reduced and irreducible, H0(O_S)=C. Write r=h2(O_S)=h0(omega_S) by Serre duality. The Euler identity gives h1(O_S)=1+r. A torsion line bundle on a compact connected reduced space has at most one independent global section: a nonzero section has a tensor power that is a nonzero holomorphic function and hence is nowhere zero, trivializing the line. This observation will also be used on the normalization below.

## A conductor calculation controlling H2(I_D)

Let eta:T to S be the finite normalization and let B=eta_*O_T. Its conductor c is the largest ideal of B contained in O_S. Since D is a reduced component of the conductor image, c is contained in its ideal I=I_(D/S). Both I and c contain a nonzero divisor on each local irreducible component. A homomorphism I to O_S is therefore multiplication by a meromorphic element q of the total quotient ring, and qI subset O_S implies qc subset O_S.

Here qc is an ideal of B, because c is a B-ideal and multiplication by q commutes with B. The defining maximality of the conductor gives qc subset c. Locally choose finite generators of c as a faithful B-module. Multiplication by q is then represented by a matrix with entries in B on those generators. The determinant trick gives a monic polynomial in q annihilating c. Faithfulness implies that this polynomial in q is zero in the total quotient ring. Thus q is integral over B; normality of B gives q in B. This proves the exact inclusion

    Hom_S(I,O_S) -> eta_*O_T,

by multiplication inside the same total quotient sheaf. Conversely B preserves c, so the intermediate identity c^-1=B also follows, although only the displayed inclusion is needed.

Tensor by the invertible dualizing sheaf. The projection formula identifies

    Hom_S(I,omega_S) -> eta_* eta*omega_S.

The normal compact surface T is connected because S is irreducible, and eta*omega_S is torsion. The preceding nonzero-section argument gives h0(T,eta*omega_S)<=1. Serre duality for the coherent sheaf I on the compact Gorenstein surface now gives

    h2(S,I)=dim Hom_S(I,omega_S)<=1.

The exact sequence 0 to I to O_S to O_D to 0 contains

    H1(O_S) -> H1(O_D) -> H2(I) -> H2(O_S) -> H2(O_D)=0.

The final vanishing is coherent cohomology on a compact curve. The last map from H2(I) is surjective, so the middle image has dimension h2(I)-r. Therefore

    h1(O_D) <= (1+r)+(h2(I)-r) = 1+h2(I) <= 2.

D is compact, reduced, irreducible and connected, so h0(O_D)=1 and its arithmetic genus is h1(O_D). This proves p_a(D)<=2.

## Positive geometric genus and the local embedded curve

Let nu:C to D be the curve normalization. The exact normalization sequence has finite-length quotient of total length delta, and h0(O_C)=h0(O_D)=1. Hence p_a(D)=g(C)+delta. If g(C)>0, this gives delta<=1. Every singular local germ therefore has delta one, and there is at most one such germ; a delta-zero germ is normal and hence smooth.

For completeness classify the delta-one germs as embedded in the given smooth threefold. Let R be the reduced local curve ring and B its normalization, a direct sum of r one-variable convergent power-series rings. The difference between arbitrary constants on the r branches and their common value at the point gives r-1 independent elements of B/R. Thus r<=2.

For r=2, the subalgebra of pairs of series with the same constant term already has codimension one in B and contains R. Since B/R has dimension one, these subalgebras are equal. Its explicit presentation is C{x,y}/(xy), by x mapping to (t,0) and y to (0,s). Each branch is smooth and the germ is an ordinary node.

For r=1 and a singular germ, write B=C{t}. If an element of the maximal ideal of R had order one, its analytic inverse would make t an analytic function of that element, giving R=B. Thus all nonconstant elements of R have order at least two. Since B/R has dimension one, the class of t spans it. Write t²=r_2+c t with r_2 in R. A nonzero c would make r_2 have order one; hence c=0 and t² is in R. Similarly t³=r_3+d t forces d=0. Therefore C{t²,t³} is contained in R. The former algebra is C plus t²C{t}, also of codimension one in B, so equality follows. The presentation x=t³,y=t² identifies it with C{x,y}/(x²-y³), the ordinary cusp.

These local rings have embedding dimension two. For their actual embedding D in the smooth threefold Y, the map on cotangent spaces is a surjection from a three-dimensional space to a two-dimensional one. Its kernel contains the nonzero differential of an element of I_D. Use that function as one local coordinate of Y; it cuts out a smooth surface containing D. The remaining codimension-one reduced curve ideal on this smooth surface is principal. Equivalently its convergent power-series ring is factorial. Thus the original ideal of D in Y is generated by this first coordinate and one node or cusp equation, a regular sequence. Smooth points are also local complete intersections by the submanifold coordinate theorem. This proves the claimed lci property everywhere on D through the embedding map, not merely through an abstract curve isomorphism.

## The transverse-type conclusion

The hypotheses of the supplied A.5.5 now hold for this same embedding D subset S subset Y: Y is smooth compact with H2(Y,Q)=0, D is a reduced irreducible compact lci curve, and its normalization C has positive genus. For each of the stated generic types A2, A3 or ordinary triple point, that input yields that D is smooth elliptic and its transverse type is the same at every point. This is the identity application on Y,S,D and nu; no ambient Picard hypothesis is added.

The accompanying fresh prefreeze program records the elementary genus cancellation, the delta-one node/cusp quotient descriptions and the jet identities needed for the simultaneously derived C2d input. Its computations are supplemental to the complete arguments above. The target proof remains unopened until the derivation and program are frozen.

## Exact prefreeze input and computation bindings

Binding written 2026-11-21T20:16:19.048539+00:00, before target proof release.

- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_01B4_statement_inputs.tex — SHA256 5df5ba39589474b44c93c02df93ece3c16aea2c7c305685d5f2e2ffeaaf2f619.
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_01B4_cited_input_supplement.tex — SHA256 cd6622f93c9c139daac4af17056ed3aa114109175c364fd330432a56f3a7a249.
- code/S6_SERIES_PUBLISH_II_A_recovery_blind_curve_jets.py — SHA256 5a4352b704ac498f87e0634248255c71ee90027dd1749e63cc115d3acd62e316.
- code/S6_SERIES_PUBLISH_II_A_recovery_blind_curve_jets.out — SHA256 4044a85c9c780c25d9bf27aab9eb2e255ffc981fac02bb8ee7269649696407f5.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_recovery_blind_curve_jets_run.json — SHA256 f23651498e08873dd8420a0e3100dc56c4afbcb4a14c4b9acf72669b773ee4d0.
