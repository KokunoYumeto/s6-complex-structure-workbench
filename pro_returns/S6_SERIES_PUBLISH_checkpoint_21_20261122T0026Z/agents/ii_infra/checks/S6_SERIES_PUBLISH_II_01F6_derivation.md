# Frozen-before-target derivation: 01F6 / cdp:st:C.3.11

I read the exact statement-only target and dependencies, including D.1.12, D.1.9, C.3.1 and the separate exclusion/occurrence statements. The E4 cited input is now bound to Viaclovsky arXiv2610.10451, Theorem2.2,pp4–5 by root's source transport. It asserts locally free R1f_*O and H0(O_full-fibre)=C for a proper connected-fibre map from a complex manifold to a nonsingular curve. I have not read C.3.11's target proof. The ambient smoothness scope used below is the intended scope of C.3.1 and must be explicit there.

## Very general types and smooth-locus alternatives

Compose the supplied C.3.1 list with C.3.7,C.3.8,C.3.9,C.3.10,C.3.12. This leaves two-tori and primary/secondary Hopf surfaces of algebraic dimension zero for the very general smooth fibre. C.3.6 and D.2.7 give the named occurrences. Over the connected smooth locus, the proper submersion is a differentiable bundle, so the first two Betti numbers are constant. The torus branch has (b1,b2)=(4,6); the Hopf branch has (1,0). In the latter branch the surface Hodge identities give (h0(O),h1(O),h2(O))=(1,1,0) on every smooth fibre. In the torus branch the supplied D.1.12 statement gives the full-fibre dimensions and cup-product isomorphism directly.

## Torus branch

Apply D.1.12 to the proper map with b2(Y)=0 and general fibre a two-torus. Its full hypotheses are retained. It supplies h^q(O_{Y_c})=(1,2,1) on every full scheme-theoretic fibre, base change for both direct images, and the actual cup-product isomorphism wedge^2 R1f_*O_Y→R2f_*O_Y. Since R1 has rank two, its second exterior power is its determinant. This identifies the first displayed direct-image relation by the stated morphism. Nothing here supplies any further splitting-degree or positivity statement.

## The rank-one branch, including all full fibres

Write L=R1f_*O_Y. The primary E4 input makes L a locally free rank-one sheaf on P1, and makes f_*O_Y=O_{P1} with fibre H0=C. The class beta supplied by D.1.9 restricts nontrivially to H1(O_{Y_c}) for every full fibre: a zero restriction would make exp(2pi i r beta) trivial on that fibre, contradicting its asserted infinite order at irrational real r.

The Leray sequence on P1 identifies H1(Y,O_Y) with H0(P1,L), since H1(P1,O)=H2(P1,O)=0. Let s be the section of L corresponding to beta. Its value at any c is nonzero: evaluation followed by the natural base-change map gives beta|Y_c, so a zero value would give a zero restriction. A nowhere-zero section of a line bundle is an isomorphism O_{P1}→L. Thus L is trivial, using precisely this section as the identification.

Let T=R2f_*O_Y. Its generic rank is zero because the general smooth fibre has h2=0; hence T is a torsion coherent sheaf on the compact smooth curve. I do not discard possible jumping cohomology at this stage. Hirzebruch–Riemann–Roch on the smooth compact threefold gives chi(Y,O_Y)=integral c1(T_Y)c2(T_Y)/24=0, since c1(T_Y)=0 rationally when b2(Y)=0. The coherent Leray Euler characteristic gives

chi(Y,O_Y)=chi(P1,O)-chi(P1,L)+chi(P1,T)=1-1+length(T).

Therefore length(T)=0, and T=0. This is the step that excludes torsion/jumps; local freeness of R1 alone would not justify it.

The map to the nonsingular curve is flat: its local parameter is a non-zero-divisor on the smooth total space, and the local module is torsion-free over the discrete valuation ring. The proper-flat cohomology complex locally on the base can be taken finite free. The universal-coefficient/base-change exact sequence then identifies the degree-one fibre cohomology with L tensor k(c), because R2=0, and identifies degree-two fibre cohomology with zero because R2=R3=0. Thus (1,1,0) holds on every scheme-theoretic full fibre and base change holds in both degrees. This includes nonreduced and singular fibres without replacing them by their supports.

## Absolute cohomology and Picard component

With R0=O, R1=O, R2=0 on P1, the Leray sequence gives H^q(Y,O_Y)=(C,C,0,0). Since b1(Y)=0, integral H1-cohomology is Hom(H1(Y;Z),Z)=0. In the exponential sequence the map H1(Y,O_Y)→Pic(Y) consequently has zero lattice kernel and identifies its image with the identity component Pic0(Y). The preceding nonzero beta spans H1(Y,O_Y). Hence Pic0(Y)=C beta with the exact exponential normalization exp(2pi i beta), as stated through D.1.9.

This derivation resolves the torsion issue explicitly before opening the target proof. Its use of D.1.12 and the primary E4 theorem is recorded as use of supplied results; their independent checks have separate owners. The source's final splitting disclaimer has no additional mathematical input. No target proof was read and no event is added.
