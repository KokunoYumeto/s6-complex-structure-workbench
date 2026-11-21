# Independent prereading derivation: 01GF / cdp:st:D.2.8

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode | restore_build.
The exact statement/input packet is SHA a9fbea1609e6a53f291e29af6e6649b42e6d72806747dcab02782af84d4d447a. Root's construction-only supplemental packet SHA4112dd78ef95ec40705ddf294ac2dec2935bb3dae934fffb827488e98cdc8fc7 gives ten exact source spans at source459c8c7c3dff70ff2621e567383ac56eaf92fd271b02f83775d2cb994f332d6e. It includes D.22–D.30 definitions and stated local boundary maps and excludes the GF argument and D.36 calculation. The GF target proof has not been opened. Before the executor reset I had seen the D.31–D.32 global homology conclusions of the cited D.2.7 construction; those are already conclusions of its supplied statement, not a derivation of the GF result. They are not being claimed as a fresh blind check of D.2.7.

Inputs used as statements: D.2.7 supplies the exact compact smooth threefold, three reduced normal-crossings exceptional fibres, fixed torus A and H1(Y,Z)=H2(Y,Z)=0 in homology; D.1.12 supplies base change and the cup-product isomorphism for R1/R2O, since this Y is smooth and has b2=0 and torus general fibre; D.1.7 supplies the real coefficient injection for compact complex fibres. The claim below is checked independently from those declared inputs and the explicit local bundle, without reading their target proofs.

## Local topology and the integral generization image

Fix one local product marking A=C×B. The filling is p:U=L×/q^Z→V with V the blowup of B×Δ at one central point, L=O_V(R), and q=exp(-2π)>0. The fibre C=C*/q^Z is identified with C/(Z+iZ) by z↦exp(2πiz); the cycles w,u are respectively the real and imaginary lattice generators. The infinite cyclic cover L×→U defines an integral class β_u which sends u to1 and w to0. Pullback by U→V→B supplies the two integral B classes. On the punctured product these are exactly u*, b1*, b2*.

Their restrictions also form an integral basis on the central fibre F=K∪H. This is checked directly, including the required maps. Choose a Hermitian metric on L. The smooth map
[l]↦(l/||l||, log||l|| modulo log(q)Z)
identifies L×/q^Z with the unit-circle bundle S(L) times the u-circle; its inverse sends a unit vector and a representative r to the class of exp(r) times that vector. Replacing r by log(q) changes the result by the quotient action, so the inverse is well-defined. For K over B the first circle has Chern degree1; for H over P1 it has degree−1. The Gysin sequence consequently gives
H1(K,Z)=H1(B,Z)⊕Zu, and H1(H,Z)=Zu.
For the common elliptic fibre C, the inclusion kills w in both groups and sends u to the u generator. The Mayer–Vietoris map on H0(C) is injective because K,H,C are connected. Thus
H1(F,Z)=(H1(B,Z)⊕Zu_K⊕Zu_H)/Z(u_K−u_H)=H1(B,Z)⊕Zu.
This proves the claimed basis of cohomology by exact dualization, with no finite torsion factor hidden. The global classes above restrict to that dual basis and to the three marked nearby covectors. Their generization image in H1(A,Z)=Λ* is therefore precisely Ann_Z(w).

Equivalently, the supplied D.25 nearby-fibre quotient H1(U,Z)=Λ/Zw and Leray on a contractible disc give Γ(Δ,R1f_*Z)=Ann_Z(w). Its map into the punctured constant sheaf is injective. Thus there is no extra section supported only at the critical point. This also verifies the sheaf-level identification independently of a choice of a deformation retraction.

## The coherent local frame is the fixed product frame

The two global coherent classes can be chosen explicitly: pull back a generator of H1(B,O_B), and take the coefficient image of β_u. On the central Hopf component H, the B class is zero while β_u is nonzero by the real coefficient injection of D.1.7. On K, the B class is nonzero, since the principal elliptic bundle has p_*O_K=O_B and hence injective pullback on H1(O). They are therefore linearly independent over C on the whole central fibre. Its h1(O)=2 and base change hold by the supplied D.1.12. These classes are a holomorphic frame of R1f_*O on the disc; over the puncture they are the constant product classes.

To fix the scale and conjugation exactly, write z=x+iy on E. The (0,1) parts are
[dx]↦(1/2)[dbar z], [dy]↦(i/2)[dbar z].
The C class β_u therefore restricts to (i/2)[dbar z_C]; multiplying it by−2i gives the standard C generator. Twice the pullback of the real B class gives the standard B generator. Their full-fibre values are independent as just proved, so this is the same constant marked coherent frame all the way to zero, rather than an unspecified extension frame.

The three complex product matrices, whose columns are C_i and the stated complement B_i, are
M1=[[0,1],[1,0]], M2=[[i,0],[i,1]], M3=[[1,0],[i,1]].
Their determinants are−1,i,1. Let K_i be the corresponding real integral4×4 matrices in real/imaginary order. They are unimodular. For every integral covector α, the coefficient map obeys the exact identity
ι(K_i^t α)=bar(M_i)^t ι(α),
where ι(a,b,c,d)=((a+ib)/2,(c+id)/2). This is precisely pullback of the (0,1) form under z=M_i ζ; the fresh Gaussian-rational program verifies it on all four basis covectors for each marking. It gives the exact transport between all three local frames and the fixed A frame.

On all overlaps, the remaining clutching maps are translations of A depending holomorphically on the base. Their pullbacks act as the identity on each fibre Hq(A,O), since a translation fixes the constant (0,q) forms. Consequently the local frames glue to
R1 f_*O_Y=O_P1⊗H1(A,O_A)=O_P1^2.
The cup-product isomorphism from the declared D.1.12 input gives R2 f_*O_Y=∧²R1 f_*O_Y=O_P1. Connected fibres and properness give R0 f_*O_Y=O_P1. All three identifications are compatible with every full-fibre base-change map.

Leray over P1 now has only trivial bundles in degrees0,1,2, whose H1 on P1 vanishes. Thus Hq(Y,O_Y)=(1,2,1,0), and its restriction to each full fibre is onto in every relevant degree; in degrees0,1,2 it is the evaluation isomorphism of the corresponding trivial direct image.

## Global integral sections

Over the smooth locus the marking gives the constant lattice Λ*=Z4. By the local calculation a global section must annihilate all three w_i. D.27 gives
w1=e3, w2=e2+e4, w3=e1+e4.
For α=(a,b,c,d), the three equations are
c=0, b+d=0, a+d=0.
Their integral solutions are exactly n(1,1,0,−1), n∈Z. Conversely every such covector extends uniquely over each disc as the integral class just constructed, and these local extensions agree with the constant section on the punctured overlaps. Therefore
H0(P1,R1f_*Z)=Z(e1*+e2*−e4*)
inside H1(A,Z)^π1=Z4. The map is exactly restriction to the smooth base. The clutching translations do not alter this sheaf calculation because they act identically on fibre H1. The primitive kernel has rank1, so the inclusion is proper. The exact new integer calculation also finds the gcd of all maximal minors equal to1, verifying its primitivity.

## Picard coordinates and torsion on full fibres

The construction's integral homology H1=H2=0 gives H1(Y,Z)=H2(Y,Z)=0 in cohomology by the UCT. The exponential sequence, with exp(2πi·), therefore identifies Pic(Y) with H1(Y,O_Y) without a lattice kernel. Restriction to a smooth fibre identifies this vector space with H1(A,O_A); the preceding coherent frames fix its coordinates exactly.

For a full fibre F_s, exp(v)|F_s is torsion precisely when some positive integer n has n v_s in the coefficient image of H1(F_s,Z). This is exactly the kernel statement in the exponential long exact sequence, so the local exceptional set is the rational span of that integral coefficient image. On a smooth fibre it is ι(Λ*⊗Q)=ι(Q4). On a central fibre the integral image is Ann_Z(w_i), and the commuting coefficient/generization diagram puts its rational image inside ι(Q4). Thus the union of exceptional sets over all full fibres is exactly ι(Q4): every smooth fibre already realizes this set, and each of the three central sets is a subset of it.

The displayed ι is a real-linear isomorphism R4→C2 with inverse(v1,v2)↦(2Re v1,2Im v1,2Re v2,2Im v2). The image of Q4 is countable and dense. Its complement is nonempty, and every neighborhood of every point in that complement contains a rational-image point. Hence the all-fibre nontorsion set is not open. This conclusion uses the same explicitly marked Picard isomorphism and the integral vanishing already supplied by D.2.7.

## Computation, exposure and status

Fresh standard-library Gaussian-rational and integer program SHA904f0a1808f601211d0f08d839d76c1324c088272ceb5538d0e65db8a1f9b2fd; output SHA349cf54909bf81e7c8eb1a441efa6d0a346b9a8854c7a892fcd8137758d4c21b. It proves the three marking determinants, identifies their w/u columns, checks all twelve coefficient-transport basis identities, and verifies the primitive kernel. No old GF program has been read. The construction input's proof narratives are excluded, and the GF target/D.36 remain unopened. All target conclusions have been derived from the declared inputs; actual target comparison follows only after this freeze. No canonical files or ledger events are changed by this derivation.
