# Isolated OS45 Borel characteristic and framing transport

## Scope frozen before receiving any D2.53 proof

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited reasoning effort not separately exposed; the same model family as the other reviewers.

The only target-specific input for this derivation is the message from corrections_audit: the fixed OS45 complex threefold X is closed and simply connected, has integral homology H_2(X)=Z^15 direct-sum Z/8 and H_3(X)=Z/8, and has c_1=c_2=lambda=0. Its scalar circle action is semifree, with sixteen fixed projective lines. On each line the tangent weight is zero and the two normal complex lines are O(-1), with circle weights +1 and -1. The additional isolated input describes an invariant embedded free-circle three-sphere N, whose orbit bundle is the primitive Hopf circle bundle over S^2; the actual based collar and its map into X have not been supplied here.

I have not substantively opened D2.53's printed proof in this branch. I have previously seen extensive Paper II/IV material and V contact sheets, and I make no blanket claim about the absence of all incidental image exposure. This derivation uses only the above isolated data and the explicitly named classical topology below. It precedes any receiving comparison for the present target. It does not supply the still-unreceived actual collar or identify a paper's concrete reference framing by assertion.

### Conclusions at this isolated-input scope

The Borel tangent bundle has a unique spin structure and its integral spin characteristic is

    lambda_{S^1}(TX) = u^2 in H^4(X_{S^1};Z),

where u is the first Chern class of the universal circle bundle, with either choice of sign. The restriction of any global stable tangent framing to the supplied Hopf N differs by an odd stable clutch from a framing descending from the quotient bundle over S^2. That descending framing itself differs by an odd clutch from the bounding stable tangent framing of S^3. Consequently the stable tangent framing induced on N by the global framing and an oriented rank-three normal framing has even parity relative to the bounding stable framing. Changing the oriented normal framing changes its stable clutch by an even integer.

These statements include the actual relative Borel-to-framing map below. They do not infer a framing from the ordinary equation lambda=0 alone. Application to a specific embedded sphere/reference collar in the receiving paper still requires identifying the actual supplied N and its normal/collar maps. No value of the paper's final diffeomorphism or extension obstruction is asserted here.

## 1. Ordinary and equivariant low-degree groups

Integral universal coefficients give H^2(X;Z)=Z^15 and H^3(X;Z)=Z/8. Rational Poincare duality and the supplied homology show H^{odd}(X;Q)=0. In the Borel fibration

    X -> E=X_{S^1} -> BS^1=CP^infinity

the base has trivial fundamental group, so all local coefficient systems in the Serre sequence are constant. Write u for the degree-two generator pulled back from the base.

In integral total degree four, the filtration F^2=ker[H^4(E;Z)->H^4(X;Z)] has associated pieces E_infinity^{4,0}=Z and E_infinity^{2,2}=Z^15. For (4,0), the only potentially nonzero incoming differential is d_4 from H^3(X;Z)=Z/8 to Z and is zero. For (2,2), the only potentially nonzero incoming differential is d_2 from Z/8 to Z^15 and is zero; the outgoing possibilities have H^1(X)=0 or an odd base degree. Therefore

    0 -> Z*u^2 -> F^2 -> Z^15 -> 0,

and F^2 is torsion free. This statement does not assume that all of H^4(E;Z) is torsion free. A fixed point gives a section BS^1->E, so the displayed u^2 is a primitive nonzero summand.

Over Q the full Serre sequence collapses because all base and fibre groups are in even degrees. Choose lifts of a basis of H^*(X;Q); Leray-Hirsch gives H^*(E;Q) free over Q[u]. The circle localization theorem then says that restriction to the fixed set is injective over Q: its kernel is u-torsion, and this free module has none. The localization theorem, Serre sequence, Leray-Hirsch theorem, universal coefficients and ordinary duality are the named classical inputs used here; no fresh original-source opening is claimed in this freeze.

## 2. Equivariant spin structure, without assuming a spin lift

The ordinary w_2 vanishes. In total degree two with Z/2 coefficients, the kernel of restriction H^2(E;Z/2)->H^2(X;Z/2) is exactly (Z/2)*u: H^1(X;Z/2)=0 excludes the only possible incoming differential. On any fixed line C, the three complex tangent roots are

    2x, -x+u, -x-u,

with x=c_1(O_C(1)) and x^2=0. Their sum is zero, so w_2(TX_{S^1}) restricts to zero on C x BS^1, and in particular on a fixed point's BS^1. The coefficient of u must therefore be zero. Thus w_2(TX_{S^1})=0.

The Borel space E is simply connected by the homotopy sequence of X->E->BS^1. Hence H^1(E;Z/2)=0 and its tangent Borel bundle has a unique spin lift. Its integral class lambda=p_1/2 is therefore defined via BSpin, without dividing an arbitrary integral class by two or choosing away possible two-torsion.

## 3. Integral calculation of lambda_{S^1}

On C x BS^1, the equivariant first Pontryagin class is

    (2x)^2 + (-x+u)^2 + (-x-u)^2 = 6x^2+2u^2 = 2u^2.

The degree-four cohomology of C x BS^1 is torsion free, so the spin class there is exactly u^2. Thus d=lambda_{S^1}-u^2 restricts to zero on all sixteen fixed components. Rational localization and the free Q[u] module proved above give d=0 rationally. The ordinary restriction of d is zero because lambda(TX)=0 and u|_X=0. Consequently d lies in the torsion-free group F^2. A torsion class in that group is zero, establishing the integral identity lambda_{S^1}=u^2.

The integral filtration argument is essential: merely applying rational localization would leave a possible integral torsion class unaddressed.

## 4. Global stable framings and their restriction to N

For a six-dimensional CW complex, the stable spin classifying map is nullhomotopic exactly when its degree-four lambda class vanishes: through degree six, BSpin has only pi_4=Z, and lambda identifies that generator. Thus the supplied lambda(TX)=0 supplies a global stable real tangent framing after adding sufficiently many trivial real lines. This assertion concerns the stable real bundle; it makes no claim that the complex tangent bundle is trivial.

Two global stable framings differ by a map X->Spin. Through dimension six, Spin has only pi_3=Z, so their differences are H^3(X;Z)=Z/8. The restriction map to H^3(N;Z)=Z is zero. Thus every global stable framing induces the same homotopy class of stable framing of TX|_N. In particular their parity on N cannot be chosen arbitrarily.

The exact representation computations in sections 8-9 below identify the stable clutch generator through lambda; no unstated change of generator is used.

## 5. Quotient bundle and its descending framing

Let B=N/S^1=S^2 and let V=(TX|_N)/S^1 be the rank-six oriented real quotient vector bundle. The equivariant spin structure pulls back to a spin structure on V. Because oriented real bundles of rank at least three over S^2 are classified by w_2, V is trivial. Two trivializations of V are homotopic, since pi_2(SO(6))=0; after stabilization the same conclusion holds.

Pulling such a trivialization back along N->B gives a distinguished homotopy class tau_eq of stable frames of TX|_N. It is the class descending from V, not a global tangent framing of X asserted to be equivariant.

An invariant metric and a connection on N->B give the actual equivariant splitting

    TX|_N = TN direct-sum nu,
    TN/S^1 = R_vertical direct-sum TB.

Here the vertical line is explicitly generated by the fundamental vector field of the circle action. Since w_2(TB)=e(TS^2) mod 2=0 and w_2(V)=0, the rank-three oriented quotient nu_bar=nu/S^1 has w_2=0 and is trivial over S^2. Hence an equivariant oriented normal frame exists, obtained by pulling back a frame of nu_bar. This supplies the exact normal splitting used in the parity comparison.

## 6. Explicit relative map from the Hopf disk bundle

Use the supplied Hopf-bundle identification v:N->S^3 subset C^2, equivariant for scalar multiplication. For Euler class -1 rather than +1, reverse the corresponding bundle/base convention; every sign below reverses consistently and the parity is unchanged. The required specific identification with a receiving collar is not claimed to have been read.

Form the disk bundle

    W=(N x D^2)/[(x,z)~(g x,g z)], g in S^1.

Its boundary is identified with N by

    [x,z] |-> z^{-1}x,  |z|=1.

Use ES^1=S^infinity with first three complex coordinates C direct-sum C^2, diagonal action, and basepoint e_0=(1,0,0). There is a literal map of pairs

    F:(W,N)->(E,X),
    F([x,z])=[x,(z,sqrt(1-|z|^2) v(x))],

where X is included into E by y|->[y,e_0]. Equivariance of v proves this formula is independent of the representative: replacing (x,z) by (g x,g z) multiplies the ES^1 coordinate by g. On the boundary,

    [x,(z,0,0)]=[z^{-1}x,e_0],

so the boundary map is exactly the stated inclusion of N into X after its explicit boundary identification. A smooth radial reparameterization can replace the square root without changing the map of pairs or any characteristic evaluation.

The pulled-back vector bundle F^*(TX_{S^1}) is exactly

    (TX|_N x D^2)/[(a,z)~(d g(a),g z)] = pi^*V.

On the boundary its identification with TX|_N is a|->d(z^{-1})(a). Thus the bundle comparison includes the actual derivative action; it is not just an equality of characteristic classes.

The base composite pF is

    [x,z] |-> [z : sqrt(1-|z|^2) v(x)] in CP^2.

It is constant on the boundary. The induced W/N->CP^2 is a homeomorphism, with the orientation sign determined by the Euler convention. Away from [1:0:0], choose a unit representative (Z_0,Z') with Z' nonzero; put z=Z_0 and x=v^{-1}(Z'/||Z'||). Changing the common unit phase changes (x,z) by exactly the displayed diagonal relation. This is the inverse. The collapsed boundary maps to [1:0:0]. In particular

    <F^*p^*(u^2), [W,N]> = +1 or -1.

This calculation is the required integral relative map, not a deduction from the vanishing of u^2 on the two-dimensional orbit space.

## 7. Relative lambda and the global/descending clutch

A global stable tangent framing tau on X gives a nullhomotopy of its spin classifying map, hence a relative lift

    lambda_tau in H^4(E,X;Z)

of lambda_{S^1}. The class p^*u^2 has a canonical relative lift because p maps X to the chosen basepoint. Their difference lies in the image of H^3(X;Z)=Z/8 under the boundary homomorphism of the pair. This difference is torsion. Pullback to H^4(W,N;Z)=Z kills it. Section 6 therefore gives

    <F^*lambda_tau,[W,N]> = +1 or -1.

The bundle over W is pi^*V and has the extended descending trivialization tau_eq. With the boundary trivialization tau|_N, this relative lambda number is the stable clutch integer between tau|_N and tau_eq, up to the uniform boundary orientation convention. One can see this directly by gluing the two trivializations along the boundary, collapsing to a clutch bundle over S^4, and using that lambda evaluates as the generator on pi_3(Spin). Thus their difference is odd.

This relative statement does not discard the torsion ambiguity: it proves explicitly that the ambiguity maps to zero in the actual target Z. It also explains why the ordinary equation lambda=0, without the nonzero Borel class u^2 and the Hopf relative map, cannot by itself supply this integer.

## 8. The descending Hopf framing has odd parity relative to the bounding one

Identify the standard Hopf S^3 with unit quaternions q, with the circle acting by left multiplication. Its tangent vectors q i, q j, q k and outward normal q form the frame given by the real matrix L_q of left multiplication by q. It is equivariant: L_g(L_q a)=L_{gq}a. Therefore, together with a constant oriented equivariant normal frame of nu_bar, this realizes a framing descending from the quotient bundle over S^2.

The stable tangent framing bounding the standard D^4 is induced by its constant real coordinate frame. The comparison matrix is q|->L_q in SO(4), stabilized into SO. The associated clutch bundle is the quaternionic line, equivalently the complex rank-two SU(2) bundle with identity clutch q:S^3->SU(2). Its c_2 evaluates as +1 or -1 by the usual orientation convention. The exact underlying-real characteristic relation is p_1=c_1^2-2c_2=-2c_2, so lambda=-c_2 evaluates as +1 or -1. Thus this stabilized clutch is an odd generator.

Any chosen trivialization of V over S^2 gives the same descending stable framing class, because maps S^2->SO in this range are null. Hence the descended tangent framing supplied in section 5 has this odd parity, independently of the selected quotient frame. Reversing the Hopf/base orientation changes a sign but not parity.

## 9. Normal-frame changes are even under stabilization

Any two oriented framings of the rank-three normal bundle over N differ by a map S^3->SO(3). Lift it to Spin(3)=SU(2). Under the adjoint representation, the complexified three-dimensional real representation has SU(2) roots 2x,0,-2x. For the fundamental rank-two representation, c_2=-x^2. Hence

    c_2(ad_C)=4 c_2(fundamental),
    p_1(ad_R)=-4 c_2(fundamental),
    lambda(ad_R)=-2 c_2(fundamental).

Since lambda evaluates as one on the stable Spin clutch generator, the inclusion pi_3(SO(3))->pi_3(SO) is multiplication by two, up to the fixed orientation sign. This is an explicit representation transport. Thus replacing the equivariant normal frame by any oriented normal frame changes the induced stable tangent-framing class by an even integer.

## 10. Parity obtained from the supplied isolated data

The global frame differs from the quotient-descending frame by odd parity (section 7). The quotient-descending tangent frame differs from the bounding stable framing by odd parity (section 8). Their sum is even. Section 9 proves that this even parity survives every oriented rank-three normal-frame choice. Section 4 proves that it also survives every global stable tangent-frame choice.

Thus the supplied circle action, ordinary spin class, homology, and Hopf sphere data determine even parity in the stated bounding-framing convention. The proof uses the literal derivative bundle map on W and the degree-one relative map W/N->CP^2. It does not use a numerical substitution for a boundary identification.

## 11. Remaining receiving and source tasks

1. Read the actual locally constructed N, the principal Hopf identification, and its based collar after this freeze. Check that the source is an embedded invariant sphere in the stated OS45 X and that its action is the same scalar circle used for the fixed-point weights.
2. Identify the receiving paper's parity reference with the bounding stable tangent framing used here through the actual tangent/normal/collar maps. The argument above proves invariance under oriented rank-three normal-frame changes, but does not invent the receiving reference or its convention.
3. Compare the receiving obstruction map from this parity to its stated 0/4 alternative. No conclusion about that final obstruction has been made in this isolated derivation.
4. Open precise primary references for localization, the relevant stable Spin homotopy/classification, and the universal characteristic relations. These are the named standard inputs to the freeze, not newly opened sources.
5. Receive a separate mathematical check of the relative characteristic/clutch calculation. In particular the normal rank-three stabilization factor must not be confused with the rank-four quaternionic generator, and the relative Hopf disk map must not be replaced by restricting degree-four cohomology only to S^2.

No computation is needed to replace these exact bundle maps; the displayed weight and representation expansions are universal polynomial identities written out above. No historical producer or target proof has been imported into this derivation.
