# Independent derivation: cdp:st:D.1.15 (tag01FZ)

The target proof has not been opened. Its statement and empty supplement were read; no construction from the target has been supplied. I construct both examples here. Fresh exact algebra is in `code/S6_SERIES_PUBLISH_II_A_01FZ_twistor.py`, authored without reading any older program.

The first family is (C^2/Z[i]^2) times P^1, projected to P^1. It is smooth and proper, its marked first integral cohomology is the constant lattice Z^4, and invariant anti-holomorphic forms identify its R^1f_*O with O^2. Its underlying smooth manifold has H_1=Z^4.

For the second family let V=O(1) direct-sum O(1) on P^1. On the affine coordinate z define four global sections by the columns of

P(z)=[[1,i,z,i z],[-z,i z,1,−i]].

They are linear polynomials and hence extend as sections of V through infinity. For a real vector (a,b,c,d), put A=a+i b and B=c+i d. Evaluation is the real-linear map

(A,B)↦(A+z B,−z bar(A)+bar(B)).

The squared norm of the image is (1+|z|^2)(|A|^2+|B|^2): the two cross terms cancel exactly. Thus the evaluation is an invertible real-linear map at every finite z. On the infinity chart u=1/z its expression, after the O(1) transition, is (u A+B,−bar(A)+u bar(B)), whose squared norm is (1+|u|^2)(|A|^2+|B|^2), and it is invertible there as well. The fresh program verifies the real determinant as −(1+x^2+y^2)^2 in the stated coordinate order; its nonzero sign is only an orientation choice.

The four sections give a real-vector-bundle trivialization P^1 times R^4→V_R. Their integer span acts by holomorphic fibrewise translations. In this trivialization the action is the standard Z^4 translation action, which is free, properly discontinuous and has compact torus quotient on each fibre. The quotient X=V/Z^4 is therefore a smooth complex manifold, and its projection f:X→P^1 is a proper holomorphic submersion with complex two-torus fibres. Its underlying smooth bundle is explicitly P^1 times(R^4/Z^4). The marking by the four chosen lattice sections identifies R^1f_*Z with the same constant lattice as in the first example and gives b_1(X)=4.

It remains to compute the coherent bundle, with an explicit quotient map. Translation-invariant relative holomorphic forms give f_*Omega^1_{X/P^1}=V^*=O(−1)^2. Their periods in the marked homology basis are the injection P(z)^t:V^*→O^4. On a torus the map from constant cohomology to H^1(O) has kernel the classes of holomorphic one-forms, so fibrewise Hodge decomposition and constant dimensions give the exact holomorphic sequence

0→V^* --P^t→ O^4→R^1f_*O_X→0.

Define the constant alternating matrix J=diag([[0,1],[-1,0]],[[0,1],[-1,0]]). Direct multiplication gives P J P^t=0. The map P J:O^4→V is onto at every point, because P has complex rank2: at finite z≠0, proportionality of its two rows would require ratios −z and z in the first two entries; at z=0 the first and third entries already give rank2; the leading coefficient matrix has rank2 at infinity. The fresh program computes all2×2 minors and the identical zero P J P^t. Thus im(P^t) is exactly ker(P J), both being rank2 subbundles. The induced map [v]↦P J v gives a specified isomorphism

R^1f_*O_X=O^4/im(P^t) → V=O(1)^2.

This proves the required two splitting types while exhibiting the precise common marking of their integral local systems. The first Chern degrees of the coherent bundles are0 and2 respectively, so a bundle isomorphism between them would preserve degree and force0=2. That degree obstruction is independent of the common local-system marking. Both total spaces have b_1=4, as directly computed above.
