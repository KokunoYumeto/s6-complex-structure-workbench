# Paper I — preread derivation of inv:D1.2 [01SN] and push:src:E.2.1 [032U]

## Source boundary

Both full target proofs remain unopened. The statement of inv:D1.2 and inv:D1.1, the normalized torus-root model fam:A.1.2, inv:A1.0's precise structure-sheaf statement, and inv:A2.1's raw determinant statement were read from the all-proofs-masked source. The independently checked E.3.1 supplies the atlas base-change/duality result, with its local fibre calculation removed from the E.2.1 dependency. A location-only rg search accidentally exposed the two isolated phrases “The logarithmic tangent sequence is” and “... T=T_X(-log W)” from E.2.1, with no formula or proof argument; the exact boundary is recorded in access_scope.json. The substantive derivations below were written before any target argument was read. inv:D1.2 has no recorded prior proof exposure.

Put m=3k, n=4l, z=kl, d=m+n, gcd(m,n)=1, and Broot=P(m,n). Thus k is odd, l is not divisible by3, and gcd(k,l)=1. Let L=O(z), and let H=T_Broot(-p0)=O(d-12z). The ordinary source's symbol E for the vertical vector bundle is used below; it is distinct from the logarithmic cotangent quotient bearing the same letter elsewhere.

## 1. The actual root lift and logarithmic tangent sequence

The identities f*p1=mS1 and f*p2=nS2 supply the line bundles O_X(Sj), their tautological sections, and their mth/nth power identifications. The universal root construction therefore gives the representable map fbar:X→Broot. On each finite root atlas its pullback is the original torus family J′, before its free affine cyclic quotient. At the cusp it is unchanged. It is proper and flat on this atlas: finite charts are submersions; at the cusp q=z0z1z2 (with the lower-depth products on other strata). The source is smooth.

For the cusp divisor W, the logarithmic differential map to the base sends z_i∂_(z_i) to q∂q. Its kernel is the rank-two relation sum(coefficients)=0. The toric transition maps act by integral changes of basis on these logarithmic vector fields; the rank-two lattice is the same fibre Lie algebra as on the punctured torus chart. Thus the vertical logarithmic bundle is fbar*E. The logarithmic differential is surjective also at the triple points, giving

0→fbar*E→T_X(-log W)→fbar*H→0.

For k=l=1, H=O(-5), exactly the quotient in inv:D1.2. This local map proves exactness; it is not inferred merely from ranks.

## 2. Vertical characters and determinant, including the cusp

The ordinary transition matrices are R1=[[-1/τ,0],[(1−μ)/τ,1]], R2=[[1/τ,0],[−μ/τ,1]], R0=I. The vector e=(0,1) is fixed, giving the global trivial line Oe in E. At τ=ρ=e^(πi/3), detR1=e^(2πi/3); at τ=i, detR2=−i. For clockwise root generators ζ_m=e^(−2πi/m), ζ_n=e^(−2πi/n), the determinant characters are ζ_m^(2k) and ζ_n^l.

These equal the characters of O(-z): since O(a) has local character a n^(−1) mod m at p1 and a m^(−1) mod n at p2, one has (4l)(2k)≡−kl mod3k and (3k)l≡−kl mod4l. Characters determine the residue class modulo mn; to fix the actual line, use the modular discriminant. With the transformation dζ1↦(cτ+d)^(-1)dζ1, the expression Δ0(τ)(dζ1)^12 defines a section of (det E)^(-12). It has no zero at either finite root and has exactly a simple zero at the cusp: Δ0=q·unit and dζ1 is a nonzero logarithmic relative covector on the toric cusp. Thus (detE)^(-12)=O(p0)=O(12z). Pic(Broot)=Z and has no12-torsion, so detE=O(-z), with the characters just computed. This fixes the full line, not only its characters.

The extension 0→Oe→E→O(-z)→0 lies in H1(O(z)). Weighted Serre duality gives H1(O(z))=H0(O(-z-d))*=0; alternatively the exact coarse degree of O(z) is −1. Hence E=O⊕O(-z). The chosen e is the first summand. In fact H0(O(z))=0 too, so the splitting preserving both fixed ends is unique.

## 3. Structure direct images and cup product

The E.3.1 derivation gives locally free Rq fbar*O of ranks1,2,1 and canonical base-change maps on the root atlas. On finite atlas fibres the model is a two-torus. At the cusp the normalization resolution has one rational toric surface, three rational double curves and two triple points; its degree-one differential is [[1,−1,−1],[−1,1,1]]. The resulting H1 basis is the two deck-coordinate classes (γ,u), and their cup matrix is [[0,1],[−1,0]], by the already completed independent coordinate calculation. The collapse sends angular cycles to zero and retains the two deck cycles, so the identification of these classes with the marking is explicit.

The invariant integral cocycle γ is holomorphic as a section of R1 fbar*O by its local Čech construction. On a smooth torus, its image in H^(0,1) is nonzero: a nonzero real degree-one class cannot be purely of type(1,0), because its conjugate is the same real class. At the cusp γ is one of the two normalization-resolution basis classes. Hence Oγ⊂G:=R1fbar*O is a subbundle on every atlas chart.

The logarithmic relative cotangent determinant is the actual relative dualizing line. Indeed
K_X(W) ⊗ fbar*K_Broot(p0)^(-1) = K_X ⊗ fbar*K_Broot^(-1),
since W=fbar*p0. Thus ω_(X/Broot)=fbar*L. The canonical trace isomorphism checked in E.3.1 gives R2 fbar*O=L^(-1). The cup map ∧²G→R2 fbar*O is an isomorphism at every smooth/root torus and at the cusp by the explicit cup matrix. Fibrewise base change therefore makes it a bundle isomorphism. The quotient of Oγ is L^(-1), so H1(L)=0 splits G=Oγ⊕L^(-1). Consequently K_X=fbar*O(z-d).

For k=l=1, the root-atlas stabilizer characters of E and G are (1,ζ3²) and (1,ζ4). These are the fibre-action conventions, fixed by the maps above. Form or pullback representatives may display inverse characters; their comparison must use the actual pushforward/pullback map rather than change the convention silently. The determinant/cup/trace maps identify the determinant characters exactly as above.

This proves every assertion of inv:D1.2 before opening that proof, using the checked local E.3.1 argument and the discriminant section to determine the global degree.

## 4. Tangent H0 and H1 for all admissible multiplicities

Write Tlog=T_X(-log W), V=fbar*E. Projection formula gives RqV=E⊗RqO. The connecting map θ0:H→E⊗G is the Kodaira–Spencer class of base variation. Project to the quotient line (E/Oe)⊗(G/Oγ)=L^(-2). This is the elliptic-modulus derivative. In the actual full roots, τ−ρ has order k at p1 and τ−i has order2l at p2, so the projected map has orders k−1 and2l−1. At the cusp it uses q∂q and τ=(logq)/(2πi)+holomorphic, and is nonzero. Its divisor is exactly
(k−1)p1+(2l−1)p2,
whose line class is (k−1)4l+(2l−1)3k=10z-d=class(H^(-1)L^(-2)).

For a weighted line O(a), the exact coarse degree is
D(a)=(a−n r_m(a)−m r_n(a))/(mn),
where r_m(a) is the representative in[0,m−1] of a n^(-1) modm and r_n(a) is that of a m^(-1) modn. Direct substitution gives
D(0)=0, D(−z)=D(−2z)=D(d−12z)=−1.
Thus after the exact invariant pushforward to the coarse P1, the projected θ0 is a nonzero map O(-1)→O(-1), hence an isomorphism. It follows that the coarse cokernel of θ0 is O⊕O(-1)^2, with its O generated by e⊗γ. The full θ0 is injective because it is generically nonzero.

The next connecting map θ1:H⊗G→E⊗L^(-1) is cup product with θ0. Generically its determinant is a nonzero multiple of the raw period determinant. The separately stated input inv:A2.1 gives
6μ_t²−τ_t β_t = τ_t² E4(τ)^2/E6(τ),
which is not identically zero. Therefore θ1 is injective as a map of vector bundles, even where its cokernel has finite support. This generic-injectivity argument does not assert that it is everywhere an isomorphism for general k,l.

The direct-image exact sequence consequently gives fbar*Tlog=E and R1fbar*Tlog=cokerθ0. Since the coarse curve is P1 and stabilizer invariants are exact, the previous splittings imply h0(Tlog)=1 and h1(Tlog)=1. The latter is represented by e⊗γ.

The ordinary tangent correction is the coefficient map at each normal-crossing branch:
0→Tlog→T_X→ν_*K_F→0,
where F=dP6 is the normalization of W. In local coordinates q=xyz, the quotient records (normal coefficient on x=0, normal coefficient on y=0, normal coefficient on z=0); its transition line is the branch normal line O_X(W)|_(branch)⊗O_branch(−double locus)=O_branch(−double locus)=K_F, since the full fibre line restricts trivially. At a double/triple point the independent coordinate normal coefficients prove surjectivity. Thus the map and its line identification are explicit. Since F is a smooth complete rational toric surface, H0(K_F)=H1(K_F)=0 and H2(K_F)=C. Hence H0,H1 of T_X equal those of Tlog.

## 5. H3 and H2 without assuming a standard-multiplicity formula

The generic base Kodaira–Spencer matrix has rank two by the same raw determinant input. The relative cotangent edge map is therefore generically injective on invariant vertical one-forms. A global holomorphic one-form on X has no vertical component; on the smooth locus it is pulled back from the base. At a generic smooth point of every cusp component, q is a local coordinate, so a coefficient of dq with a pole at q=0 cannot extend holomorphically. The finite root-atlas submersion gives the identical conclusion there. Thus fbar*Ω_X^1=Ω_Broot^1 exactly, with its actual root representations.

Projection formula and Serre duality then give
h3(T_X)=h0(Ω_X^1⊗K_X)=h0(Broot,O(z−2d)).
This weighted H0 vanishes for every admissible k,l. An elementary proof avoids an asymptotic degree shortcut: a monomial of weighted degree z−2d would satisfy 3ka+4lb=kl−6k−8l. Reduction modulo k gives b+2≡0 modk. For k>1, b≥k−2, and then 4lb≥4kl−8l>kl−6k−8l. For k=1, the requested degree is −5−8l<0. Equivalently D(z−2d)=−1 for k>1 and −2 for k=1. Thus h3=0.

Analytic HRR applies to the compact complex threefold. Since its underlying manifold is S6, c1=c2=0 and ∫c3=2. The degree-three part of ch(T_X)Td(T_X) is c3/2 in this specialization, so χ(T_X)=1. Combining h0=h1=1 and h3=0 yields h2=1. This route checks the general multiplicities without assuming that θ1's finite-support cokernel vanishes; it bypasses a potentially delicate cusp connecting map.

## 6. Parameter class and Kuranishi germ

The period derivative is ∂cΠ=e⊗γ on the fixed integral lattice. Differentiating the groupoid gluing maps with κ(Φ)=(∂cΦ)Φ^(-1) therefore gives the class e⊗[γ]; the finite/cusp comparison maps are differentiated in the same convention, so the class extends to the actual compact family. It is the nonzero H1 generator computed above. For u=e^(−2πic), the chain rule gives ∂c/∂u=−(2πiu)^(-1), exactly the second class.

The explicit period and comparison maps depend holomorphically on c, and the already constructed compact gluing over a sufficiently small parameter disc supplies an actual deformation, with nonzero Kodaira–Spencer derivative. The Kuranishi tangent space has dimension1. Embedding its analytic germ in that one-dimensional tangent space, the induced disc map has nonzero derivative and hence open image; every defining holomorphic function vanishes on that image and is identically zero. Thus the germ is a smooth reduced line and this family is locally miniversal. No inference is made from the obstruction-space dimension alone.

## Additional dependency to make visible

This derivation uses inv:A2.1 for the generic rank-two raw period derivative. E.2.1's short StatementRecord currently lists only E.1 and E.3.1; the full proof should cite the exact determinant input where used. The E.3.1 local-model facts must precede the global splitting, as recorded in the first-four comparison.

## Pending comparison and computation

The full target proofs have not yet been opened. A new program will verify the weighted residue formula on admissible pairs, the symbolic characters/divisor identities, and the Chern-character specialization; the algebraic proofs above cover all pairs and do not rely on a finite test range. It will then be compared with the actual proof line by line. This preread does not pre-certify agreement with unseen steps.

Saved UTC: 2026-11-21T01:10:17.988674+00:00
