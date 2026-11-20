# Weighted OS45: based Hopf sphere and equivariant stable-frame derivation

## Freeze and exposure

This document is the corrections reviewer's full proposed derivation, frozen before receiving or opening the sign reviewer's independent conclusion. Author: GPT-6 Astra, ChatGPT Pro mode; reasoning effort inherited from root, not separately exposed. The root-authorized source/proof exposure is the one in `III_OS45_local_geometry_receiving_08.md`. The sign reviewer received only the isolated global action/homology/fixed-normal data and the desired Borel-to-framing question. At this writing I have received that reviewer's file path, hash and readiness only; I have not opened the file or received its mathematical conclusion. This derivation is for full receiving comparison, and makes no canonical status change.

The fixed target is exactly the weighted OS45/default example of D.2.53: P=2G, Q=8G, weight two at I8, zero at the other four I1 sites, the specified triangular Mumford caps and ordinary clutch e=1. The derived conclusion below is that its refined class is zero. Every transport used to obtain that conclusion is stated below. Independent receiving review remains required before that conclusion is imported into the manuscript.

## 1. The existing integral inputs

The received exact proof gives H2(X)=Z15 plus Z8, H3(X)=Z8, and c1=c2=lambda=0 integrally. In particular all odd rational cohomology vanishes. The actual scalar circle action is semifree. Its entire fixed locus is sixteen CP1 curves; on each curve, the tangent line has degree two and weight zero, and the two normal lines have degree minus one and weights +1,-1. These are the actual D.OL4–8 data, not merely abstract representations at a point.

The first two based elliptic matrices are T^8,T, with T=(1 1;0 1); their G cocycles are (3,0),(0,0). The full weighted short/long lattice has

  l1=(8,-6), l2=(24,-16), L=8Z plus 2Z,

in the fixed short basis (e1,delta). On the cusp boundary alpha=e1 wedge delta has exact order two. It bounds in both the cusp and the filled exterior; the first I1 gives the explicit exterior image. These are the complete root boundary-prism checks, not an inference from rational homology.

The exact local relative characteristic formula is lambda(TX,rho)=-PD(Ccrit), with every actual complex double curve appearing once. The abstract kernel of df has a nowhere-zero delta section and a smooth second frame vector; the target line has a smooth frame. Off Ccrit these give rho. D44.6 verifies the unit Bott residue, and D44.7/D.WI13 derive the corresponding integral linking and reference-framing formula. The relative-class proof works for the embedded torsion sphere constructed below by the same Thom/cochain pairing, as explained in Section 7.

## 2. The literal source-line graph and its meridian

The Tate source calculation D.FI2 uses the canonical meromorphic section s of M=O(P-O) and

  sigma(Z)=theta(Z/P;q_E)/theta(Z;q_E),   sigma(q_E Z)=P sigma(Z).

Thus e_flat=s/sigma is a nonzero flat frame on the Tate universal cover. It gives the physical coordinate W_flat. The manuscript's coordinate is the dual coordinate V=W_flat^{-1}; the map is literal tautological duality of nonzero lines, with every multiplier inverted. This explains the negative scalar entries in the displayed long periods.

At I8, the actual P lift has valuation 6 and the Q lift has valuation 24. The flat-frame extending heights are F_i=max(6-i,0) for 0<=i<8, with F_(i+8)=F_i-6. The graph edge between (0,6) and (1,5) is therefore an actual source-line edge. It belongs to the supplied fan. An adjacent regular cone has rays

  (1,0,5), (1,1,5), (1,0,6).

Its determinant is one. In its coordinates,

  q=xyz, Z=y, V=x^5 y^5 z^6,
  W_ext=q^6/(ZV)=x,
  (X,Y,W_ext)=(xz,y,x).

The inverse is (x,y,z)=(W_ext,Y,X/W_ext), and the Jacobian is -x. The frame e_ext=(Z/q^6)e_flat is the exact extending frame on this node neighborhood: its divisorial orders on the two branches are zero, neither P nor O meets the node, and the frame and its inverse extend across the remaining codimension-two point. This specifies the frame rather than omitting an unspecified unit.

The three marked weights in this cone are

  e1=(-1,1,0), delta=(-1,0,1), e1-delta=(0,1,-1).

In the product-node source/line coordinates, delta is inverse physical line rotation and e1-delta is the source vanishing circle at constant W_ext. At the first I1, the supplied cocycle is zero, the flat frame extends, and the source vanishing circle is e1. Both oriented boundary areas equal alpha. The two primitive meridians (1,-1),(1,0) have determinant one.

The graph representatives are not silently translated. The period relation (0,-6)=9l1-3l2 would carry the actual source multiplier q_E^9 Q^{-3} and its actual scalar unit. It need not be the identity. The construction below keeps the unshifted edge, so that additional translation is never applied.

## 3. A based collar map that retains all point and line factors

Take the actual based arc from the selected I8 site to the first I1 site, contained in the two edges of the received peripheral tree. Choose a narrow neighborhood Omega containing that arc and those two singular points, with no other singular point. On the punctured neighborhood the based monodromies T^8,T fix the same e1, and the two section cocycles have zero second component. The exponential period coordinate q_E, and the multiplicative lifts of P and Q, are single-valued there. Their actual valuations are (8,6,24) at the cusp and (1,0,0) at the finite node. These are fixed by the received lifts, not by reducing their valuations modulo the fibre multiplicity.

Use the above canonical theta frame on this based cover. Let F be the actual forward suspension lift, in the direction defining the received gamma. If its coefficient in the canonical meromorphic section is c_F(Z), its coefficient in the flat frame is the explicit expression

  kappa(t)=c_F(Z) sigma(QZ)/sigma(Z).

It is independent of Z: the two factors cancel its zero/pole divisor, its automorphy is trivial, and it is a nonzero holomorphic function on the compact elliptic fibre. This is the exact conjugation of the received point/line map, not the choice of a new lift. Its valuation at I8 is 16 and at I1 is zero, as follows either from the actual gamma column or from 8w-(-6)(24)=16 and the forward inverse-lift convention in D.FI2.

Consequently the actual two-period quotient on Omega is

  (Z,V) -> (q_E Z,P^{-1}V),
  (Z,V) -> (QZ,kappa^{-1}V).

Every phase and holomorphic unit is retained in q_E,P,Q,kappa. The source origin is O, namely Z=1, and the line frame is s/sigma; there is no additional independently chosen endpoint origin. Changing a local scalar frame would change c_F and sigma by their displayed conjugation, and therefore gives the same map of the original nonzero line.

For completeness, the base transport need not be assumed holomorphic. Parametrize the fixed embedded based arc by a smooth regular p:[0,1]->Omega, chosen linear in an affine base coordinate near its endpoints. In that coordinate an actual tubular map is

  t(s+iu)=p(s)+i u p'(s)

on a sufficiently thin strip, with the endpoint holomorphic expressions retained. Its Jacobian along the arc is |p'(s)|^2>0, so shrinking the strip gives an orientation-preserving diffeomorphism onto its image. The construction uses that chosen map, not an equality of two base coordinates. Put q0(t(f))=f c0(f) near zero and q1(t(f))=(1-f)c1(f) near one, where c0,c1 are the actual nonzero endpoint units.

On Q={ad-bc=1}, f=ad, define the actual collar map to the received quotient by

  Phi(a,b,c,d)=[t(f), Z=ab, V=f^6/a].

The brackets are precisely the two-period quotient above. At the first end it extends in the actual selected graph cone as

  (x,y,z)=(c0^6/b, ab, c0^{-5}d).

At the second end it extends in the original node/line chart as

  X=-c1 c/a, Y=ab, W=a/f^6.

These formulas prove extension and give nonzero local Jacobians at the two compact core circles. On the regular collar the map is fibrewise complex linear in logarithmic torus coordinates with a unimodular character matrix, and its base derivative is positive. It is therefore a local real diffeomorphism. No claim of holomorphicity is needed for the middle base transport.

There is also an explicit bundle comparison for the framing: in vertical/horizontal splittings, the derivative has complex-linear vertical block and an orientation-preserving real base block a+b conjugation, with |a|>|b|. The homotopy a+(1-r)b conjugation, 0<=r<=1, remains invertible. The off-diagonal horizontal-to-vertical block contracts linearly. Near both critical ends the map is already holomorphic. This transports the complex framing calculation through an actual homotopy of oriented bundle isomorphisms, retaining delta and the vertical kernel. It introduces no degree-three change.

## 4. The actual odd three-sphere

The compact real form in Q is

  g(alpha,beta)=(alpha,beta;-bar beta,bar alpha),
  |alpha|^2+|beta|^2=1.

Its generic f level is the short two-torus. At zero and one its primitive meridians are e1-delta and e1. The physical line transition is W1=(Z/f^6)W0; the factor f^6 is retained in Phi, and the source equator factor Z has winding one. These are the usual two explicit Hopf bundle charts, so the compact model is S3, not merely a chain with a Smith generator.

Phi is injective on this compact sphere. At a regular point of the arc, the short real two-plane intersects the full period lattice precisely in Z e1 plus Z delta; otherwise the four marked real periods of the compact complex torus would be linearly dependent. Thus its short two-torus is embedded. Distinct arc parameters lie over distinct base points. At either endpoint the selected toric/node core circle is embedded; no nonzero period translation fixes the selected finite edge. The local Jacobians above prove immersion there. Compactness now gives an embedded sphere and a neighborhood on which Phi is an embedding.

Move it by left multiplication with L_epsilon=(1 epsilon;0 1), taking epsilon>0 small enough that the moved sphere stays in that neighborhood. The map is explicitly

  a=alpha-epsilon bar beta, b=beta+epsilon bar alpha,
  c=-bar beta, d=bar alpha.

It misses both local critical curves a=d=0 and b=c=0. The chosen neighborhood meets no other critical curve. Thus the resulting embedded N is disjoint from the complete Ccrit. The move is an isotopy, retaining the scalar circle, since left multiplication commutes with its right action.

The Mayer–Vietoris boundary of the unperturbed sphere is alpha, with the displayed meridian/area orientation. Since alpha is nonzero of order two in the cusp boundary, and H3(X)=Z8, the sphere's integral class is odd. The displaced N has the same class. This proves that N detects the two-primary refined choice.

## 5. Integral equivariant lambda and the actual Borel transport

Write t for the positive generator of H2(BS1;Z). On a fixed CP1 write x for its positive degree-two generator. The actual equivariant Chern roots of TX there are

  2x, -x+t, -x-t.

They sum to zero and their second elementary symmetric function is -t^2, since x^2=0. First, c1_S1(TX) is zero globally: ordinary c1 vanishes, the integral circle Gysin sequence makes the kernel in degree two the multiples of t, and its fixed-point weight is zero. Hence the Borel real tangent bundle is spin, with lambda_S1=-c2_S1. Its fixed-locus restriction is t^2.

Apply the integral Gysin sequence to X times ES1 -> X_S1. Its total space is homotopy equivalent to X. Since ordinary lambda=0, exactness gives

  lambda_S1(TX)-t^2=t eta,  eta in H2_S1(X;Z).

That degree-two group is free: the same sequence is 0->Z t->H2_S1(X;Z)->H2(X;Z)=Z15->0. Restricting to each fixed CP1 gives t eta|=0, hence eta|=0.

There is no hidden torsion conclusion in the next step. With rational or complex coefficients the Borel spectral sequence has only even entries, so every differential vanishes. Multiplication by t on its associated graded is injective, and no nonzero class is t-torsion. Atiyah–Bott's localization theorem therefore makes fixed-locus restriction injective over that field. Thus eta is zero rationally. Since its integral group is free, eta=0 integrally. We obtain the full identity

  lambda_S1(TX)=t^2.

Let R be the real representation underlying C0 plus C1 plus C(-1). It is spin and lambda_S1(R)=t^2. Thus the virtual spin bundle TX-R over the Borel space has lambda zero.

Here is the specific space needed for the framing comparison, so no genuine global equivariant framing is assumed. For N parametrized above, the circle acts by (alpha,beta)->(s^{-1}alpha,s beta). In ES1=S(infinite complex space), set

  e_r(alpha,beta)=(cos(pi r/2), sin(pi r/2) bar alpha,
                   sin(pi r/2) beta,0,...), 0<=r<=1.

Use the diagonal Borel convention (n,e)~(s n,s e). At r=0 this gives the ordinary inclusion of N over a fixed e0. At r=1 it is equivariant and factors through the actual Hopf quotient N/S1=S2. It defines a map of the finite-dimensional space

  Y = X union_N (mapping cylinder of N->S2)

to X_S1. Its restriction on X is the ordinary fibre inclusion. Its restriction on S2 classifies the **actual** Hopf bundle and quotient tangent bundle. Y has dimension six.

The stable spin classifying space has pi4=Z detected by lambda and no other homotopy group in dimensions at most seven. This follows from Bott's displayed stable O period, together with the unit quaternionic/Bott generator already fixed in D44.6. Consequently the pulled-back bundles TX and R are stably spin-isomorphic over Y: the only obstruction in this range is their lambda difference, which is zero. This is a bundle isomorphism over the displayed mapping-cylinder comparison, not a declaration that ordinary lambda supplies an equivariant frame.

On X the representation bundle is canonically trivial, yielding a global stable tangent frame F. On S2 it yields an isomorphism of the actual quotient tangent bundle with the bundle associated to the Hopf bundle by weights (0,+1,-1). Along the displayed cylinder the pullbacks of TX and R are identified with their fixed vector spaces at n; the isomorphism therefore supplies the actual homotopy from F|N to a weight-one equivariant frame. This is the Borel-to-framing map used below.

## 6. Explicit weight-one and weight-two frame maps

In the complex left-invariant frame of SL2C, delta is the constant diagonal generator. On the other two Lie coordinates (u,v),

  df=ac u+bd v.

Put A=ac,B=bd. After subtracting the delta component of e1, the local reference frame has the normalized Bott first column (B,-A). On the displaced sphere,

  A=-alpha bar beta+epsilon bar beta^2,
  B=beta bar alpha+epsilon bar alpha^2.

Let A2 be the corresponding SU2 matrix. Its pair never vanishes for epsilon>0; a common zero would force z1=-epsilon^2 z1 with z1=bar alpha,z2=bar beta, while the axis cases are nonzero. Increasing epsilon gives a homotopy to (z1^2,-z2^2). The simultaneous complex conjugation preserves real orientation in dimension four, and the holomorphic squaring pair has four positive preimages of a regular value. Therefore deg A2=4 in the fixed coordinate orientation.

Write D_j(s)=diag(s^j,s^{-j}). The exact equivariance is

  A2(n s)=D2(s) A2(n).

Define the degree-one Hopf map

  A1(alpha,beta)=(bar alpha,-beta;bar beta,alpha).

Its first column is (bar alpha,bar beta), it has determinant one, and

  A1(n s)=D1(s) A1(n),  deg A1=1.

Therefore C=A2 A1^{-1} is a literal degree-three gauge and satisfies

  C(n s)=D2(s) C(n) D1(s)^{-1}.

The left Lie frame transforms by D2 under the scalar right action. Multiplying it by C gives exactly a weight-one equivariant frame, as required by Section 5. It differs from the reference frame by A1^{-1}, of degree minus one.

The weight-one isomorphism supplied by the Borel mapping cylinder and this explicit one have no unrecorded degree-three difference. On the Hopf quotient they differ by an automorphism of the same stable spin bundle over S2. A spin bundle over S2 is trivial (pi1 Spin=0), and every map S2->Spin is nullhomotopic (pi2 Spin=0). Thus that automorphism is homotopic to the identity over S2. Pulling the homotopy back to N proves zero difference of their integer framing degrees.

A left Lie frame on the displaced SU2 is a tangent Lie parallelization with its imaginary normal parallelization. Its framed parity is one, either directly or by the received actual-parallelization formula 1+dim H1(S3;F2). The degree-three change C makes the induced global stable framing parity even. Equivalently, the reference frame has parity one (degree four from the Lie frame), and the actual global frame differs from it by an odd degree-one change.

## 7. The critical-link intersection and refined class

All the preceding statements use actual maps. The residue comparison can now be applied without inferring anything from even core coefficients. Compare the reference rho to the global stable frame F on X minus Ccrit. The unit local Bott residue is one on every actual double curve. Its degree-three comparison class evaluates on N as an odd integer; the explicit comparison above has absolute degree one, with the common residue orientation sign fixed by the convention for lambda(TX,rho)=-PD(Ccrit).

To see why this computes the intersections with a complete prescribed critical nullchain, let D be any integral three-chain with boundary Ccrit, including the sum of the actual specialization chains and the complete D.OS8 core chain. The Thom intersection cochain of D has exactly those unit residues. Its difference from the framing comparison class extends over X and lies in H3(X;Z). Its evaluation on the torsion class [N] is zero. Hence N dot D equals the same comparison integer, in particular it is odd. This does not assume that a chosen specialization chain has zero intersection. It proves that the sum of those actual intersections, with the full core contribution, is odd. Since the supplied core coefficients are even, the specialization contribution is odd as well. No separate individual-curve intersection values are asserted.

Finally the received relative formula gives

  lk(N,PD P_ref)=-ell(N,Ccrit)/2-epsilon_rho/2 in Q/Z.

Both ell and epsilon_rho are odd, so the right-hand side is zero. N is an odd generator of H3(X)=Z8, and the torsion linking pairing is nondegenerate. Also 2P_ref=lambda=0. It follows that P_ref=0 for the fixed D2.53 manifold. The same conclusion follows from the received Brown/Zhubr admissibility criterion, because the induced global stable framing on this embedded odd sphere is even.

This computes the required linking **parity and total intersection**, not individual local crossing tables. It does not promote the horizontal-edge S2xS1 attempt, which remains unproved in the earlier receipt. It uses no worldwide literature absence claim and no proposed change-of-frame conjecture.

## Primary-source loci actually opened for this derivation

- Atiyah–Bott, The moment map and equivariant cohomology, Topology23(1984), original §2 pp2–3 and Theorem3.5 plus circle discussion p8. Full localization statement and surrounding argument were freshly opened at https://www.math.stonybrook.edu/~mmovshev/MAT570Spring2008/BOOKS/atiyahbott_moment.pdf . This supplies the localization kernel assertion only. The even-degree spectral-sequence and torsion-free integral lift arguments above are written here explicitly.
- Bott, The stable homotopy of the classical groups, Annals70(1959), Corollary to TheoremII, equation(1.5), pp314–315, especially the full stable O period printed p315. Fresh original opening: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/bott.pdf . This supplies the stable homotopy groups; the mapping-cylinder obstruction application is given above.
- Hatcher, Algebraic Topology, §4.D, Gysin sequence printed p438 and complete final Thom-pair derivation p444. Fresh local source reading from `audit_corrections/primary_sources/Hatcher2002_author_07.pdf`, PDF one-based447 and453. The canonical bundle here is explicitly X times ES1 -> X_S1, with Euler class t. No finite-cap diagram claim is imported from this opening.

The old local code/output (115 assertions) remains a local certificate. New gauge identities and the full receiving comparison will be recorded separately after this freeze. No independent reviewer output has been read in writing this document.
