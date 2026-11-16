# Fibre homotopy-module continuation after E.2.15

Status: historical continuation note. The full integral modules and these coinvariants are now proved and registered in E.2.16-E.2.17; the former central-intersection gap is resolved there. The L2 observation below remains an unregistered consequence. These results are not a smooth classification.

Put Pi=ker(chi)=pi1(Y), z=h1 h2, S=ZPi[(z-1)^(-1)], and R=ZG. The group Pi is the circle-bundle group of Euler number -1 over Sigma6.

## Exact coinvariants

The level of the aspherical N→S1 is the closed aspherical circle bundle Z3 over Sigma6. It splits along a torus into two copies of Sigma_(3,1)×S1. Its top cohomology generator is the Mayer–Vietoris connecting class of gamma1 gamma2. The actual classifying map c_Y:Y→Z restricts on the separating boundary T8→T2 to these two coordinates.

The saturated boundary image from either Y piece contains gamma1 gamma2 primitively. This is checked exactly by code/maps_shifted_fibre_module.py. It also follows from the first degree-two column in E.S38: its pullback is a nonzero multiple of gamma1 gamma2, and the actual image is primitive by E.2.15. Hence c_Y^*:H3(Z;Z)→H3(Y;Z) is zero. Therefore c_Y*:H3(Y;Z)→H3(Z;Z) is zero too.

The low-degree covering spectral sequence gives

0→Z→M=(pi2(Y))_Pi→ker[H2(Y)→H2(Z)]→0.

Here the last map is onto, H2(Z)=Z^12, and E.2.15 gives H2(Y)=Z^121⊕(Z/6)^2. Thus its kernel is Z^109⊕(Z/6)^2. Relative Hurewicz identifies M with H3(Z,Y), while H2(Z,Y)=0. The universal-coefficient theorem identifies H3(Z,Y) cohomology with Hom(M,Z). Since c_Y^* on H3 is zero, the cohomology sequence makes evaluation on the injected Z surjective. That injection splits. Therefore

(pi2(Y))_Pi = Z^110 ⊕ (Z/6)^2.

This computes exact coinvariants, not the full module.

## Every localized universal-cover homology module

Work first over R[(z-1)^(-1)]. Let a=h1-1 and b=h2-1. The identity

z-1 = a+h1 b

makes the central ideals (a),(b) comaximal after this localization. For any module the two-open Cech sequence is exact. E.2.12 gives zero homology after inverting both a and b, while the individual localizations are direct sums of R[a^(-1)]/(b) and R[b^(-1)]/(a), with multiplicities r_j=(1,3,4,4,3,1) in degrees j=2,...,7. Therefore

H_j(Ptilde)[(z-1)^(-1)] = [R[(z-1)^(-1)]/(h1-1) ⊕ R[(z-1)^(-1)]/(h2-1)]^(r_j).

Restrict to Pi. The intersection Pi∩<hi> is trivial because chi(hi)=±12. Thus Pi injects into G/<hi>, with index12. Each quotient group ring R/(hi-1) is free of rank12 as a ZPi-module. Localizing the central z-1 preserves that freeness. Since Ptilde is Pi-equivariantly homotopy equivalent to Ytilde×R, it follows that

H_j(Ytilde)⊗S is free of ranks (24,72,96,96,72,24) in degrees2,...,7 and is zero in all other degrees.

In particular pi2(Y)⊗S=S^24. The full module at z=1 is still uncomputed. The Cech splitting needs no speculative assumption about an integral extension at that locus.

## Manifold L2-Betti numbers

These same ranks compute the L2-Betti numbers of the manifold Y (not of the group Pi's aspherical model). The localized finite free cellular chain complex of Y has free homology in every degree. By induction from its bottom degree, split off boundaries and homology; it is chain-homotopy equivalent over S to that graded free homology with zero differential plus a contractible projective complex.

The infinite-order central z acts by a bilateral shift on l2(Pi). The kernel of z-1 and of its adjoint is zero, since an l2 function constant on an infinite cyclic orbit vanishes. Thus z-1 is a weak isomorphism, hence is invertible in the algebra U(Pi) of affiliated operators. There is a ring map S→U(Pi). Tensoring the established chain homotopy equivalence, rather than assuming U(Pi) flat over the group ring, gives U(Pi)-homology of exactly the free ranks above. The normalized affiliated dimension and Lück's Theorem8.31 give

b_j^(2)(Y)=(24,72,96,96,72,24) for j=2,...,7, and zero otherwise.

For P, invert both h1-1 andh2-1. E.2.12 makes the localized finite free chain complex acyclic, hence contractible by the same bounded-projective splitting. Both central elements become invertible in U(G), so all manifold L2-Betti numbers of P are zero.

Primary source read: Wolfgang Lück, *L2-Invariants: Theory and Applications to Geometry and K-Theory*, author manuscript dated1July2002, Springer. Full primary PDF opened at https://www.math.uchicago.edu/~shmuel/L%5E2%20cohomology%20readings/Lueck_L2-invariants.pdf. Theorem8.22(1),(2),(5), printedpp327–328/PDF339–340, identifies affiliated operators as the localization and weak isomorphisms as invertible. Theorem8.29 and Definition8.30/Theorem8.31, printedpp330–331/PDF342–343, identify affiliated homology dimensions with L2-Betti numbers. Web references turn307view0 andturn307view1, exact lines26463–26488 and26672–26710. No full external PDF was stored inside the deliverable project.
