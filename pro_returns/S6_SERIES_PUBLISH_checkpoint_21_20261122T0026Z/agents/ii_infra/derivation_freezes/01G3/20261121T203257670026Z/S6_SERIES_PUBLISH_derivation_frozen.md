# Independent prereading derivation: 01G3 / cdp:st:D.1.5

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode | restore_build.
The exact root-separated manual statement packet has SHA-256 384e142dcebb620aa248c8387147a66412dc6441a59c68ea73940712017f58b8. The mixed target statement/argument has not been opened. The inherited first-part headings and this manual packet are the target exposure. Root has corrected its earlier warning: the recorded false statement belonged to another owner; no mathematical objection to this packet was supplied or used.

Permitted external inputs actually read: the exact historical split-extension statement in the statement supplement; attached AC26 manuscript printed p91, Section10.5, including its bielliptic example paragraph. Its PDF SHA is 283bba102dd1d5dc346af81b28145bdaaea6654398d5032e76e97bafb9a858f2. The argument below is written from the construction, not from the embargoed II block. External primary input receipt is G3_G4_primary_inputs/S6_SERIES_PUBLISH_II_AC26_external_input_receipt.json.

## The quotient and its integral complement homology

Write L=Z+iZ. The generator g(e,z)=(e+1/2,-z) has exact order two on E0×F0. Its fixed-point equation e+1/2=e contradicts 1/2 not in L. Thus the quotient is smooth and finite étale, and the invariant projection to C=E0/<1/2> is a smooth fibre bundle with fibre F0. Its product with E' has fibre F0×E'. On the connected double cover E0→C the fibration is the product; the deck transformation acts on the fibre by (-1,id), so it acts on integral H1 by diag(-I2,I2).

The map c↦([e,0],0), for a lift e of c, is well-defined: replacing e by e+1/2 changes (e,0) by g. It is a holomorphic section. For C° obtained by deleting s≥1 points, C° retracts onto a bouquet of s+1 circles. The fibration exact sequence and the section give
π1(U)=Z4 ⋊ π1(C°),
with action through the nontrivial double-cover character. The character remains surjective after puncturing: the fundamental group of the punctured curve surjects onto that of C, as can be seen by moving its two standard loops away from the punctures.

Here is the exact abelianization map, including its inverse. Send (k,q) to ([q],[k]) in π1(C°)_ab ⊕ (Z4)_π1(C°). Multiplication becomes addition because ρ(q)k−k vanishes in coinvariants. Conversely include fibre elements and the section lift of base generators into the abelianization. Their commutator relations identify ρ(q)k with k, so this descends to the claimed inverse. The only fibre relations are 2e1=2e2=0; e3,e4 survive freely. Therefore
H1(U,Z)=Z^(s+1) ⊕ ((Z/2)^2 ⊕ Z2)=Z^(s+3) ⊕ (Z/2)^2.
The expression retaining all four free fibre generators gives s+1+4=s+5, while the explicit quotient above has free rank s+3. This is a proved rank comparison for this fibration.

The same section over the complete elliptic base identifies π1(Y) with Z4⋊Z2, since π2(C)=0. Its abelianization is Z4 ⊕ (Z/2)^2, and hence b1(Y)=4. No integral torsion has been discarded.

## Coherent direct images and restriction

Let p:E0→C be the double cover. The anti-invariant summand of p_*O_E0 is the character line η. Its square is O_C, and p^*η is trivial. Consequently degη=0. An anti-invariant global section would be an anti-invariant holomorphic function on the connected compact E0; all such functions are constant, and an anti-invariant constant is zero. Thus η is nontrivial and H0(C,η)=0. Serre duality on the elliptic curve gives H1(C,η)=0 as well, since η^−1=η and ω_C=O_C.

After the étale base change p, Rq f_*O is the constant bundle with fibre Hq(F0×E',O). This follows directly from the product and finite étale base change. The deck action on H1 is (-1,+1), and on its second exterior power it is -1. Descending these eigenspaces gives
R0 f_*O=O_C, R1 f_*O=η⊕O_C, R2 f_*O=η.
All fibres have these dimensions and the descent is locally free, so no torsion direct-image term is being suppressed. The Leray spectral sequence has only base degrees0 and1 and therefore degenerates. Using h0(O_C)=h1(O_C)=1 and both cohomologies of η zero gives
(h0,h1,h2,h3)(Y,O)=(1,2,1,0).
The restriction map on H1 factors through the Leray edge map to H0(C,R1 f_*O). The base H1(C,O) restricts to zero, and the global section of the trivial summand evaluates nontrivially in the E' direction. The anti-invariant summand has no global section. The image is exactly that one-dimensional direction; the rank is one.

Projectivity and scope are also explicit. E0×F0×E' is projective and the finite group acts algebraically, so its finite quotient Y is projective. Averaging rational cohomology under this finite étale quotient shows b2(Y)=7: three degree-two factors and the four E0–E' cross terms are invariant; terms with exactly one degree-one F0 factor are anti-invariant. Thus this example has a precisely computed positive second Betti number; it establishes the displayed complement and restriction calculations with its stated invariants.

## The Weierstrass surface and its product

Homogenize A(t)=t4+1 as a section of O(4) and B(t)=t6 as a section of O(6). On the infinity chart u=1/t, set x'=u2 x and y'=u3 y. Then
y'2=x'3+(1+u4)x'+1.
The invariant fibre differential dx/(2y) transforms to u^−1 dx/(2y), the transition of O(1). For this flat plane-cubic family it is the residue generator of the relative dualizing line, including the nodal fibres. Thus the fundamental line is L=O(1), ω_R/P1=h^*L, and relative Serre duality, together with h_*O_R=O_P1, gives R1 h_*O_R=L^−1=O(-1).

The discriminant is -16 P(t), where
P(t)=4(t4+1)^3+27t12=31t12+12t8+12t4+4=Q(t4),
Q(z)=31z3+12z2+12z+4.
The fresh Fraction program gives the exact Bezout identity
(5/36−31z/54) Q(z) +(1/27−7z/324+31z2/162) Q'(z)=1.
So Q has three distinct roots; Q(0)=4, hence they are nonzero. Each has four distinct fourth roots, giving twelve simple finite zeros of P. The infinity-chart discriminant has value -16·31, so there is no extra zero at infinity. A and B cannot vanish simultaneously: B=0 forces t=0 and A=1. At a simple discriminant zero the cubic has one ordinary node and the total space is smooth: a singularity of the total space would also make the discriminant derivative vanish. Thus all twelve singular fibres are irreducible nodal cubics and are relatively minimal; the smooth projective Weierstrass surface has section at infinity.

Leray with O and O(-1) on P1 gives q(R)=pg(R)=0. The smooth torus fibres have Euler number zero, each nodal cubic has Euler number one, and stratified fibre additivity gives e(R)=12. Since R is projective, b1(R)=2q(R)=0; Poincaré duality gives b3=0, b0=b4=1, hence b2(R)=10. Also K_R=h^*(O(1)⊗O(-2))=h^*O(-1), so its plurigenera vanish. Together with q=0, the classification of smooth projective surfaces gives rationality; the numerical product conclusions below already follow from the direct computations above.

For the fixed product Y'=R×E' over P1, relative Künneth gives
R1 f_*O=R1 h_*O_R⊕(h_*O_R⊗H1(E',O))=O(-1)⊕O,
R2 f_*O=R1 h_*O_R⊗H1(E',O)=O(-1).
Ordinary Künneth gives H1(Y',O)=H1(E',O), so restriction to a smooth torus fibre is exactly the E' summand and has rank one. Integral/rational Künneth gives b1(Y')=2 and b2(Y')=10+1=11, since H1(R,Q)=0. The product is a projective threefold, so its field of rational functions has transcendence degree3, giving a(Y')=3.

## Fresh computation and status

The fresh exact program S6_SERIES_PUBLISH_II_G3_G4_fresh_exact.py has SHA836a1e0b329113a2f155d076f2ad3caa6672e375ba0f06e139bc44090b8f3487; output SHA b9a03670ba017a155708650225b2c32a9e58b21ccfd2b7aae71b172b37a94c64. It uses standard-library rational Euclidean algorithms and explicit integral matrices, and checks the two Bezout identities, discriminant polynomial and order-two lattice relation. A console-serialization failure after the first successful mathematical checks was corrected before this freeze; the original code/output and correction note are preserved. No old target program or embedded II argument was read. All claims in the manual packet have now been derived; proof comparison remains to be performed only after this freeze. No event is added by this document.
