# C.4 prereading analytic arguments

Written before opening any of FK, FL, FM, FN or FQ. This record supplies the common arguments cited explicitly by the five individual derivations. Their original source statements and input packets remain immutable. FK/FL/FM/FN have a separate ambient-domain question; the arguments below use the smooth total-space domain required by the displayed tangent, adjunction and index inputs. No singular counterexample and no assertion of singular generality is made.

## Picard components and a holomorphic parameter family

For a connected smooth compact Y with b1(Y)=b2(Y)=0, H1(Y,Z)=0 and H2(Y,Z) is finite. The exponential sequence therefore identifies Pic0(Y) with the complex vector space H1(Y,O), and c1 identifies the finite component group with H2(Y,Z): the next map to H2(Y,O), a complex vector space, kills torsion. Choose additive Cech cocycles representing a basis of H1(Y,O). Exponentiating their linear combination on Y times this vector space constructs a holomorphic family realizing every Pic0 parameter. Tensor by a representative L_P to obtain the family on any component P. Thus proper cohomology semicontinuity gives closed analytic jumping loci in P; one parameter with a vanishing group proves a dense open vanishing locus in that component.

Each component contains a finite-order line bundle. Indeed, choose N killing c1(L_P). Write L_P^N=exp(alpha). Then T=L_P tensor exp(-alpha/N) has T^N=O and stays in P. Choosing local N-th roots of a trivialization of T^N expresses T by constant roots of unity; hence it is unitary flat. This is an explicit construction, rather than an identification of all topologically trivial bundles with flat bundles on an arbitrary analytic space.

## Full-fibre duality and the base-change map

For f:Y to P1 with Y smooth and connected and f nonconstant, a base parameter t cuts out its full fibre F. Multiplication by t is a nonzero divisor in the regular local domains of Y, so f is flat over the smooth curve. Each full F is a compact Gorenstein surface, with its scheme structure and multiplicities. Adjunction is
omega_F = (K_Y tensor O_Y(F))|F.
The local generator t of I_F gives I_F/I_F^2 the frame [t], and the dual frame identifies O_Y(F)|F with O_F. This supplies the explicit local identification omega_F with K_Y|F. Rescaling t rescales this identification by an invertible scalar and leaves the cohomology vanishing tests unchanged. Serre duality then gives
H2(F,(T_Y tensor L)|F)^dual = H0(F,Omega_Y^1|F tensor (K_Y L^-1)|F).

Analytic cohomology and base change in the top fibre degree gives
(R2 f_* E) tensor C(c) = H2(F_c,E|F_c)
for a locally free E on Y. One way to see the exact map is to represent proper relative cohomology locally on the base by a finite free complex with no term above degree two; its last cokernel commutes with tensoring by C(c). The fibre dimension is two, so no R3 occurs. Nakayama thus makes R2 f_*E vanish exactly when all these full-fibre H2 groups vanish. No local-freeness assumption on R1 or R2 is imposed.

The Leray spectral sequence on P1 has only columns zero and one. Hence there is an exact sequence
0 -> H1(P1,R1 f_*E) -> H2(Y,E) -> H0(P1,R2 f_*E) -> 0.
In particular a nonzero torsion R2 sheaf forces H2(Y,E) nonzero, since a nonzero coherent sheaf supported on finitely many points has nonzero global sections.

## From full-fibre vanishing to a generic global vanishing

Suppose a line L in a prescribed component P has H2(F_c,(T_Y L)|F_c)=0 at every c. Then R2 f_*(T_Y L)=0. For k sufficiently large, Serre vanishing on P1 makes H1(P1,R1 f_*(T_Y L) tensor O(k)) zero. Projection formula and Leray give H2(Y,T_Y L f^*O(k))=0. Choose k divisible by the finite order of c1(f^*O(1)) in H2(Y,Z); then L f^*O(k) remains in P. Proper semicontinuity on the constructed Picard family proves generic H2 vanishing in P. This argument uses a projective-base Serre twist and does not assume a direct-image sheaf is locally free.

For a smooth regular two-torus fibre F and a nontrivial degree-zero line A, Hq(F,A)=0 for all q. Its degree-zero holomorphic class has a unitary-flat representative; the flat torus Dolbeault Laplacian has a zero mode exactly for the trivial character. Also
0 -> O_F^2 -> T_Y|F -> O_F -> 0.
Tensoring this exact sequence by A makes all its cohomology zero. Since a line on Y has torsion c1 and H2(F,Z) is torsion free, every restriction has degree-zero topological class. The cited D.1.11 input supplies a dense G_delta set of lines, in every component, whose restrictions to every full fibre are non-torsion. Such a line has the preceding acyclicity on all regular torus fibres. Its R2 direct image is therefore a torsion sheaf, though it can be nonzero at singular values.

## Generic H0 and H3, with a primary binding

The checker actually read the complete published CDP98 pp78 and79 images: Proposition1.1 and its proof, and Corollary1.3 and its proof. For a smooth compact threefold with b2=0 and a nonzero effective Cartier divisor D, Corollary1.3 gives generic H0(Y,B tensor A)=0 in Pic0 for every vector bundle B. The elementary underlying construction is B(-kND), with N killing c1(D), followed by analytic semicontinuity. Apply it to B=T_Y tensor L_P and to B=T_Y^* tensor K_Y tensor L_P^-1. Inversion of the Pic0 parameter and Serre duality turn the second H0 vanishing into H3(Y,T_Y tensor L)=0. Intersect the two dense open sets in P. The corrected current C.1.1 index input gives
chi(Y,T_Y tensor L)=c3(Y)/2=1-b3(Y)/2.
The current complete C.1.3 proof was read as a cited input; it also proves the pointwise lower bound h2 >= max(0,1-b3/2) by this generic argument and closed cohomology-jump loci. No assertion from CDP98 Lemma1.5 is used.

## The finite cyclic torus-cover calculation, including nilpotents

Let a neighbourhood of a full smooth multiple fibre be the free cyclic quotient of a smooth torus family tildeU -> Delta_u, with quotient base coordinate t=u^m. The quotient map pi:tildeU -> U is finite etale. The inverse image of the full fibre is the thickened divisor mT, cut out by u^m, not only its reduced torus T. The conormal O_T(-T) is explicitly trivialized by u. Thus every graded piece of the u-adic filtration of Omega_tildeU^1 tensor pi^*A on mT is
(Omega_tildeU^1|T) tensor pi^*A|T,
and 0 -> O_T du -> Omega_tildeU^1|T -> O_T^2 -> 0.
A nontrivial unitary pi^*A|T has zero H0 on all these pieces. Induction through the exact filtration proves zero H0 on the entire mT. Since pi is faithfully flat and pi^*Omega_U^1=Omega_tildeU^1, pulling back a section is injective; the full-fibre group downstairs is zero.

For the real transgression lines, the cited D.1.9 construction gives beta|F as the coefficient image of a nonzero integral gamma_F in H1(F,Z). A finite-order representative T times exp(2 pi i r beta) restricts to the corresponding unitary character. On a smooth cyclic cover of the reduced fibre, gamma remains nonzero rationally because the transfer composed with pullback is the finite degree. For irrational real r, multiplication by a finite-order character cannot make it trivial: a cycle on which gamma has nonzero integer value gives an irrational argument, up to a rational one. This proves the nontriviality needed in the preceding full-thickening argument. It applies to rational-Betti-zero actual families even when integral H2 has torsion.
