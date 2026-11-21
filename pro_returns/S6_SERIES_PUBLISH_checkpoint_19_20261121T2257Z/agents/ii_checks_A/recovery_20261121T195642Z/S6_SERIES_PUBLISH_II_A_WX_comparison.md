# 02WX / night:P4.25: complete comparison after release

## Exposure and timing

The independent derivation was completed from the statement, immutable
supplement, root's safe standing-domain/citation packet, and actually opened
primary literature. It froze at 2026-11-21 22:42:29.842434 UTC. Receipt:
`agents/ii_infra/derivation_freezes/02WX/20261121T224229842434Z/S6_SERIES_PUBLISH_derivation_freeze_receipt.json`,
SHA 165aa156c61940fe37163d577db4c3d9e687700a91f37b6fbd994c6e076cbc8f.
The frozen derivation SHA is e67761a264149aade70024cce485a83a31a574bd9bd6e5603aa9f30ba566b3df.
Release receipt SHA is 2f83b5312b48e8c0fe49c6e5ff729b5e3a1bed66b3dd6445d2be27f56ac805eb.
Only after release did this checker open and read the entire original
statement, record line, seven proof items, all displays and final conclusion.

The first new program was written, executed and its full output read before
freeze. The second program below is explicitly postrelease. It supplies
checks of computations first exposed in the printed proof and does not
receive a separate independent or prereading event.

## Statement and each proof item

The full setting is the proper connected-fibre holomorphic map f:Y→B,
Y a connected smooth compact complex threefold with b1=b2=0, B a smooth
compact curve, and smooth general fibre a complex two-torus. The initial
assertion is about every reduced support, including reducible supports whose
components have unequal multiplicities. The second assertion specifies an
irreducible support and a resolution of its normalization. These are both
preserved. The final unqualified P4.6–P4.8 invocation must state the
all-supports hypotheses of its global conclusions. The individual-support
normal-crossing and smooth-normalization assertions are proved without
adding such a global hypothesis.

1. **Resolved conductor.** The printed branch exponent formula
   c_i=2δ_i+Σ_{j≠i}I_ij agrees with the independent total-conductor argument
   Σc_i=2δ. With every c_i=1, positivity of I_ij and nonnegative δ_i
   force two smooth branches with intersection multiplicity one. To spell
   out the one-branch case, c_1=2δ_1 cannot be one; for r≥3 the sum of
   positive intersections is at least two. For r=2 the formula is
   1=2δ_i+I_12, hence δ_i=0 and I_12=1. The hypersurface is S2 and
   Gorenstein. The exact maps are normalization ν:N→S, resolution
   π:T→N, and ρ=ν∘π. The residue generator Ω defines
   D=−div(ρ*Ω). Its strict part is the conductor divisor D_N and
   K_T+D=π*(K_N+D_N), with K_N+D_N=ν*K_S. Thus the two log pairs
   are related by this precise crepant pullback. The coefficient under a
   blowup is the sum of the coefficients of branches through the centre
   minus one. Reduced SNC starts with values at most one; SNC and this
   bound persist under point blowups. The opened Liu–Rollenske Lemma2.2
   and Definition2.3, published p.189, therefore give the printed slc
   assertion. A bare line-bundle isomorphism alone would not select a
   divisor; the proposed wording binds the existing intended residue
   identification explicitly.

2. **Classification and isolated germs.** The complete published table
   and both classification proofs were read before freeze. The precise
   source is Liu–Rollenske2012, Theorem1.1 p.186, Table1 p.187,
   Proposition3.1 pp.192–196 and Proposition4.1 pp.196–200. The normal
   singular entries are isolated. The frozen argument constructs the
   ambient analytic coordinate map from the cotangent isomorphism and
   writes the full function U g^m, then h=U^(1/m)g. It proves the positive
   degree of ∇h using Milnor's AppendixB pp.111–114 and provides all
   boundary and horizontal-flow maps, plus the Morse coordinate map.
   This verifies the original perturbation and negative-sphere mechanism
   in the actual fibre. The printed constant perturbation can be chosen
   outside the finite set of critical values, so the claim that their
   values are nonzero is valid.

   The exact equality with the printed gradient colength is as follows.
   Write A=C{u1,u2,u3}, B=C{z1,z2,z3}, with A→B given by
   u_i↦h_{z_i}. The isolated zero gives a finite analytic map after
   choosing small neighborhoods, equivalently a finite A-module B;
   this is the finite-map form of Weierstrass preparation. The three
   parameters h_{z_i} form a regular sequence in the regular local ring
   B: they generate an ideal of height three and B is Cohen–Macaulay.
   The Koszul resolution gives Tor_1^A(B,A/(u))=0. Lift a basis of
   B/(u)B of size ℓ to B. Nakayama gives a surjection A^ℓ→B; its
   kernel K satisfies K/(u)K=0 by that Tor vanishing and the chosen
   basis. Nakayama gives K=0, so B is free of rank ℓ. At a regular
   small value c the fibre is reduced and has ℓ points. The boundary
   degree argument counts these same points with positive degree one,
   so ℓ=μ. This proves the exact map between the colength in the
   original and the topological degree in the independent derivation.
   Milnor p.115 Problem3 states this equality but does not supply its
   proof; the module argument here is the supplied verification.

3. **Ordinary, pinch and two-branch double germs.** Smooth, ordinary
   double and xyz germs have the stated NC local models. The pinch map
   is the coordinate change z↦−z to P4.16 with n=2; the irreducible
   germ has a common multiplicity, which P4.16 permits. For
   x²+y²z² the two graph derivatives are (1,∓iz,∓iy), so the planes
   coincide exactly at the origin and are distinct at nonzero points of
   either double axis. The printed deformation argument invokes the
   local mechanism of P4.20 but leaves the independent multiplicities
   of these two branches untracked. The frozen conic argument supplies
   this missing case explicitly: U=x−iyz, V=x+iyz, full function
   U^aV^b, d=gcd(a,b), a'=a/d, b'=b/d, U=t^b', V=t^(−a') on one
   component, inverse t=U^rV^s for rb'−sa'=1. Hence
   yz=(t^(−a')−t^b')/(2i) has a'+b'≥2 simple roots. Its circle
   fibration over an arc joining two roots is an embedded Lagrangian
   sphere. The normal orientation differs from J(TS²) by one
   transposition, giving square−2. Positive weights(2,1,1) and the
   explicit unit coordinate map carry it into the full nearby fibre.
   This is a repair of the full-multiplicity proof gap, not a restriction
   of the original theorem.

4. **Finite-q double germs.** All printed formulas are correct. The
   independent proof used the exact conic map
   (x,y,z)↦(s=y,a=x/y+iz,b=x/y−iz) on g=1, giving
   ab=(1−s^q)/s²; it then used positive weights(q,2,q−2).
   This is different from the printed perturbation
   G_s=x²+y²(z²+y^(q−2)+s). In the printed route the map
   (x,y,z)↦(x,y,Z=z²+y^(q−2)+s) has Jacobian2z0 at
   z0²=−s, so it is the exact pinch coordinate chart. The transverse
   two-jet along the boundary z-axis is x²+(z²+s)y² and its Hessian
   determinant is4(z²+s). The terms y^q with q≥3 contribute zero
   to that two-jet. The compact boundary has |z| bounded away from
   zero, giving the required uniform nonvanishing for small s.
   Boundary smoothness persists by openness and compactness. The
   already checked P4.20 horizontal-flow construction transports the
   square−4 class from P4.16. The germ is irreducible by the weighted
   initial-form argument, so the full function has a single common
   multiplicity; the weighted unit map makes this transport exact.

5. **Two-factor triple germs.** The printed identity
   G_s=x(yz+x^(p−1)+sx), p≥3, its smooth branch claim and both
   Hessian determinants−y² and−z² are correct. The transverse jets
   are sx²+xyz on the corresponding axes; x^p has degree≥3.
   Unequal multiplicities again need their explicit map. One repair
   keeps the original deformation and replaces it by the full function
   x^a(yz+x^(p−1)+sx)^b. On its boundary double strata, two free
   normal coordinates u,v give u^a v^b, a submersion at nonzero
   values; the same boundary horizontal-flow proof therefore applies.
   For nonzero small s, set X=x(s+x^(p−2)). This is a local
   biholomorphism and x is X times a unit. Thus the deformed full
   function is a unit times X^a(X+yz)^b. The explicit map
   x'=X+yz/2, y'=y, z'=z/(2i) gives
   x'−iy'z'=X and x'+iy'z'=X+yz. The unit is absorbed with
   weights(2,1,1), reducing this exact full function to the case in
   item3. A negative sphere then transports to the original full
   fibre. This preserves the printed deformation and its computations
   while filling the multiplicity gap. Independently, the frozen proof
   used the undeformed conic yz=t^(−a')−t^((p−1)b') with
   a'+(p−1)b'≥3 roots and weights(2,p−1,p−1).

6. **Finite-p, finite-q triple germs.** The printed formulas and map
   all agree with a complete independent calculation after exposure.
   The boundary z-axis two-jet is sx²+zxy, determinant−z².
   The implicit equation yz+pξ^(p−1)+2sξ=0 gives ξ=yzA(y,z)
   with A(0,z)=−1/(2s), because p≥3. Substitution into the
   critical value and division by y² gives H. On y=0 its exact
   value is z²A+s z²A²=−z²/(4s); the term ξ^p/y² vanishes
   there. On z=0 one has ξ=0 and H(y,0)=y^(q−2)+sy.
   Therefore H_y(0,0)=1+s for q=3 and s otherwise. A small
   nonzero s makes it nonzero. The finite map
   (v,y,z)↦(X=yv,y,z), v²+H=0, is birational over y≠0;
   the source is smooth since H_y≠0, and the monic equation for
   v gives finiteness. It is exactly the normalization. At the origin
   the equation gives dy=0, and dX=0, so the differential has rank
   one, with dz as its sole image direction. An NC hypersurface
   has normalization maps which immerse their coordinate-plane
   branches; the explicitly computed rank excludes that local model.
   The local P4.20 argument then gives the claimed nonzero-square
   sphere and boundary transport. The original germ is irreducible by
   the positive weighted initial form, so the common multiplicity is
   legitimate. The frozen independent route used instead the conic
   map s=x,a=y,b=xz+y^(q−1), inverse z=(b−a^(q−1))/s,
   which gives ab=1−s^p and p simple roots.

7. **Exhaustion and normalization.** The table has precisely the normal
   isolated families, the nonnormal double families, and the triple
   families covered above. The three surviving local models are the
   smooth surface, uv=0 via (u,v)=(x+iy,x−iy), and xyz=0.
   Their normalization morphisms are the inclusions of their disjoint
   smooth coordinate planes. This proves the printed NC and smooth
   normalization conclusions with the exact maps.

## Computations and method comparison

Prerelease program `code/S6_SERIES_PUBLISH_II_A_02WX_conic_maps.py`:
SHA2b782256fbf968a1ae674a05f70c787ea9099d38c641ab6f426d8931138ffa5b;
output SHAbae9e32d1088fcb8ae2c722eae39d0c2b61fc5dc7bea059a4e3a66d8fbd0535e.
Exact Gaussian rational evaluations with certified separate-degree bounds
check the algebraic maps, and integer Euclidean recursions check the
displayed inverse exponents. The complete output was read before freeze.

Postrelease program
`code/S6_SERIES_PUBLISH_II_A_02WX_deformation_jets_postrelease.py`:
SHA978e636f3331b49f08c96be118899f8af73d44e4ec0ec6ae4325611e62914023;
output SHAad8b0382f030038cb6c07736f9f362275e94d4ef0475ebd15ffa0bdcb13bf2ab.
It ran22:45:17.740882–22:45:17.792104UTC, exit0. Its full16 transverse
two-jet rows, all48 rational evaluations and all12 Morse-remainder rows
were actually read. It uses sparse coefficient collection and a fixed-point
recursion of the implicit critical graph over exact rational arithmetic.
The universal exponent arguments and the exact restrictions H(0,z),H(y,0)
are proved above; finite sample rows check the implementation and do not
stand in for those universal proofs. No old routine has been asserted to
have been run. Root's bounded association report will be bound separately.

## Source-edit policy and receiving scope

The continuation prompt §4.2 was reread from its retained exact path. It
permits wording/order/presentation changes and mathematical-step changes
only to correct an error. Accordingly the proposal preserves the seven
printed proof items, all their displayed deformation formulas, Hessian
values, critical-value formulas and normalization map. The independent
conic proofs remain in the check record except where they fill the genuine
untracked-multiplicity gap. The final global invocation is made precise;
the theorem's full reduced-support assertion is preserved.

Root's receiver receipt SHA9531e0acb7cf3042c1081dcff2c5e45d75790ac211c2a9df288eee4c8d2c6797
reports two index occurrences, a metadata dependency, and two future WY
proof calls which invoke retained local conclusions. This checker has
not opened the root-only receiving-proof fragments in that receipt.
The exact safe receiver statement is read and its proof remains closed.
The whole eventual proposed block will be reread against the whole
original, and its precise hashes recorded after preparation.

## Final bounded association and paired reading

Root's bounded prior-program record is
`records/S6_SERIES_PUBLISH_II_WX_prior_program_scope.json`,
SHA91c5a350f9e286a0b2e1b55a99f073742dc2a4356067e7033e06114cea23c4df.
This checker read its two complete adjacent gaps, all four exact-owner
historical rows and all ten Programs rows after release. None names a WX
routine. Related rows explicitly belong to P4.14, P4.16/P4.17 and
P4.18/P4.19; they are not reassigned. No claim about an unexamined repository
routine is made. The historical outcome describing full multiplicities is
preserved byte-for-byte; the current check explicitly supplies the maps
needed in the printed proof.

At 2026-11-21T22:51:54.189018+00:00 this checker had actually reread the complete original and
complete proposed statement/proof pair in full, including all seven items,
every display and the final global invocation. Original SHA
124f594fe2e4942cd4bee9308d2837c4011f82e3f2f913087da0383dc283ef95 and final proposed SHA
29c5ba1316f50e00336054bbc49bbb8782258017220f420484daef0996343e18 bind that rereading. The final pair preserves the original
deformation expressions, their Hessian determinants, the two exact H
restrictions, the finite normalization morphism, and all local conclusions.
The added common-power level decomposition and the two-factor full
deformation carry every original multiplicity. The final global sentence
states the all-supports domain of P4.7/P4.8, and the residue divisor has
its explicit sign. The two new exact computational programs are proposed
once each in the end Programs table. No extra independent event is assigned
to the postrelease calculation or to the receiver audit. Enumeration
wrappers remain for the root-owned final global map.
