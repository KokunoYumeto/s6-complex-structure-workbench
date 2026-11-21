# Preread derivation — push:src:E.1.1 [032R] and E.1.2 [032S]

Both target proofs remain unopened. Inputs read: the target statements, the primary Viaclovsky attached TeX §2 matrices, u_i, torsion-point definitions and inverse lattice action B_s; and the statement of fam:B.3.1, the general clockwise classification. I have independently checked the root/canonical construction in E.2.1 in this run. No retained classification program has been read.

## E.1.1: actual integral and affine maps

Let P be the displayed P_V. Direct integer products give
P δhat=δ,
P(1,2,−4,0)^t=(0,−2,−2,−1)^t=−u0,
P(1,3,−3,0)^t=(1,−3,−3,−1)^t=δ−u1.
Expansion of its determinant gives −1, so P is an isomorphism of integral lattices. With the primary matrices V0,V1 in basis(δ,a,b,d), multiplication must give P A1=V0 P and P A2=V1 P; a new exact program will record both products and P^(-1). These maps compare the same counterclockwise base-loop monodromies. The analytic root generators themselves have opposite directions in the two conventions.

For the affine root action (x,s)↦(B_s x+a_i(s),ζs), the inverse is (x,s)↦(B_(ζ^-1s)^(-1)(x−a_i(ζ^-1s)),ζ^-1s). The period v_i is invariant under the transported linear action, so its inverse translation is exactly −v_i/m_i. Hence the clockwise lift is determined by P w_j=−v_i. Substituting the three displayed P images gives
w1=N0 ε−ρ0 δhat,
w2=N1 ε′−(ρ1+N1)δhat.
This proves the two extra signs and the N1 term by an actual inverse affine map. It does not conflate base-loop monodromy with root deck orientation.

The stipulated section-preserving cusp comparison has zero winding l0. The ordinary clockwise sphere integer is p=mn l0−n r1−m r2. With r1=N0,r2=N1, it is p=−(nN0+mN1)=−b. Therefore p=±1 is exactly b=±1. The torsion point uses the full smooth root-torus period vector. Changing v_i by m_i times an integral period changes v_i/m_i by that actual period and hence leaves its torus point unchanged; its chosen lifted connector must still be changed accordingly, as the statement warns.

## E.1.2: transport of the classification congruences

In fam:B.3.1 set r_j=N_j, s1=−ρ0, s2=−(ρ1+N1), p=−b, and use h=c′−c for its integer shift. Its sign equation becomes b′=alpha b. Subtracting this equation gives
n(N0′−alpha N0)+m(N1′−alpha N1)=0.
Since gcd(m,n)=1, the two differences are divisible by m and n, respectively. Thus the r-congruences follow, rather than being dropped without justification.

The first remaining congruence becomes hN0′≡ρ0′−alphaρ0 modk. The second initially reads
hN1′≡ρ1′−alphaρ1+(N1′−alpha N1) mod2l;
the last term is divisible by4l, so the stated second congruence follows. Every substitution is reversible, hence the iff claim follows from the given clockwise classification.

For fixed discrete data b′=b=±1 forces alpha=1. The sphere relation modulo m and n gives gcd(N0,m)=gcd(N1,n)=1. Therefore hN0≡0 modk and hN1≡0 mod2l are equivalent to k|h and2l|h. As gcd(k,2l)=1, the exact identification subgroup is2klZ.

Fix a reference Bezout datum with b=1. For any sphere datum choose alpha=b′. The two congruences determine h modulo k and2l because their N′ coefficients are invertible; CRT gives exactly one h modulo2kl. Thus every datum at fixed u is represented by the reference datum with c shifted by an integer, uniquely modulo2kl. There are exactly2kl classes. A positive u-loop changes c by−1 since u=e^(−2πic), giving the single cycle j↦j−1 on Z/(2kl).

Every biholomorphism covers the identity of the coarse base. This is already included in the geometric classification input; it also follows intrinsically from the canonical line checked independently in E.2.1. Put a=z−d. It cannot be zero: kl=3k+4l would give k|4 while k is odd and coprime to l, hence k=1 and the resulting equation is impossible. A suitable positive or negative canonical Veronese of degree mn pulls back the complete linear system O_B(|a|), recovering f. The cusp and the two finite multiplicities distinguish all three special points; m is divisible by3 and n by4, with gcd(m,n)=1. Thus the induced base automorphism fixes0,1,infinity. If this argument is made explicit in an early publication proof, its canonical-line calculation should be placed before it; it must not cite a later miniversality conclusion.

## Pending exact recomputation

A fresh program will verify the determinant, both intertwining matrices, the three marked vector images, the inverse affine substitution, and the CRT orbit for all admissible pairs k,l≤20. The general arithmetic proof above supplies the infinite scope; the finite orbit check only independently recomputes the stated algorithm and period length. The full fam:B.3.1 classification proof is a cited input and is not independently re-proved here.

Saved UTC: 2026-11-21T01:24:51.740813+00:00
