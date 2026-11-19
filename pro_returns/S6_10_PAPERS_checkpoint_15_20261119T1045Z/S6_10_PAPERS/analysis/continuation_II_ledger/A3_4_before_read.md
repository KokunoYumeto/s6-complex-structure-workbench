# A.3.4 — full assertion derivation before reading the receiving proof

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation.

The A.3.4 receiving proof, historical scope narrative and producer code remain unopened. Opened inputs are the exact A.3.4 statement, the named statements D.1.9/A.4.9/A.4.7/A.3.1, and D.1.9's already-proved construction (opened explicitly as an input). A.3.1 has a separate complete current receipt. A.4.9 is used as a named proved input; no new re-proof of that dependency is claimed. The original CDP20 p.693 Remark7.2/Proposition7.3 and p.695 Remark7.4 were opened for exact source attribution. The argument below establishes the stated full-fibre result under its given hypotheses, with the actual maps retained.

## 1. The specified transgression family and its actual unitary restriction

The hypotheses give H^1(Y,Z)=H^2(Y,Z)=0 and base P^1. The exponential sequence therefore gives a group isomorphism

exp(2 pi i -): H^1(Y,O_Y) -> Pic(Y).

D.1.9 constructs gamma in H^0(P^1,R^1 f_* Z), a generator mapped to 1 by its integral Leray transgression (the opposite sign convention would reverse both orientations). Coherent Leray identifies the coefficient image of gamma with beta in H^1(Y,O_Y). Its actual restriction to every full fibre F is iota(gamma_F), with gamma_F a nonzero integral class. The underlying topological spaces of F and its reduction S agree, so gamma_S is the same nonzero class in H^1(S,Z). This is a coefficient/restriction map, not an identification of their structure sheaves.

On a sufficiently fine cover of S, represent gamma_S by locally constant integer transition cocycles n_ab. The holomorphic line with constant transitions exp(2 pi i r n_ab) represents exp(2 pi i r iota(gamma_S)). If b_ab is a holomorphic cocycle representing beta|_S, equality of the two cohomology classes writes b_ab-n_ab=u_b-u_a after refinement. Use the frame convention e_b=exp(2 pi i r b_ab)e_a and f_b=exp(2 pi i r n_ab)f_a. The map e_a -> exp(2 pi i r u_a) f_a is compatible on overlaps because exp(2 pi i r u_b)exp(2 pi i r n_ab)=exp(2 pi i r b_ab)exp(2 pi i r u_a). It is the actual isomorphism from L_r|_S to the constant-transition line. Thus for real r the specified line is unitary flat; no holomorphic unit is dropped.

The nonzero integral class gamma_S gives a nonzero integral period n along a loop. For irrational real r, the character exp(2 pi i r n) has infinite order. A nontrivial unitary-flat holomorphic line on the connected compact smooth surface S has no nonzero holomorphic section: its flat metric makes the squared norm of a section globally plurisubharmonic; at a maximum it is constant, and the holomorphic coefficients in unitary-flat frames are constant. A nonzero section would then be a nowhere-zero parallel trivialization and would force the character to be trivial. This proves H^0(S,L_r|_S)=0, and also proves injectivity of unitary characters into holomorphic line classes in this setting.

## 2. The actual rational shifts supplied by the normal line

The following argument identifies the divisor line without choosing an unproved sign or a global unit equal to 1. Define L_t=exp(2 pi i t beta) with beta fixed exactly as above.

Since beta's relative cohomology class comes from gamma, the image of L_1 in R^1 f_* O^* is zero. Locally on the base it therefore has a trivialization on f^{-1}(U_i). The ratios of these trivializations descend to units on U_i intersect U_j because f_* O_Y^*=O_{P^1}^* for this proper connected-fibre map. Their actual descended cocycle defines a line M on P^1 and an isomorphism L_1=f^*M. Write M=O(k) in Pic(P^1)=Z, retaining the isomorphism from the descended cocycle. Pullback on Pic(P^1) is injective: pushing forward an isomorphism f^*M=O_Y and using f_*O_Y=O_{P^1} gives M=O_{P^1}.

Conversely let alpha be the unique exponential preimage of f^*O(1). Its relative class has zero exponential, so locally it lifts through R^1 f_*Z -> R^1 f_*O. The coefficient map is injective on these integral stalks by the real-coefficient injectivity used and proved in D.1.9's cited D.1.7 input; thus the lifts are unique and glue. Hence this global lift is n gamma for some integer n, and coherent Leray gives alpha=n beta. Consequently

f^*O(1)=L_n=(f^*O(k))^n=f^*O(kn).

Injectivity of pullback gives kn=1. Thus k=n=epsilon with epsilon in {+1,-1}; epsilon is the degree of the actual descended M, not a freely assigned replacement of beta. We have the actual isomorphism f^*O(1)=L_epsilon.

For a full fibre mS, the divisor identity mS=f^*(c) gives O_Y(S)^m=f^*O_{P^1}(c), and a chosen nonzero identification of O(c) with O(1) identifies this with L_epsilon. The exponential group isomorphism and uniqueness of division by m in the vector space H^1(Y,O_Y) give O_Y(S)=L_(epsilon/m). One can write the resulting line map on transition functions: take logarithmic cocycles for the topologically trivial divisor line and for L_(epsilon/m); their difference is a holomorphic additive coboundary because the two H^1(O_Y) classes agree. The exponentials of its local zero-cochain are the multiplication maps between their local frames. Any remaining root-of-unity frame choices are retained by those same cocycles, not set to 1.

Writing N=O_Y(S)|_S, restriction and tensor multiplication now give, for every integer j,

L_r|_S tensor (N^*)^j = L_(r-epsilon j/m)|_S.

This isomorphism uses the actual line map just constructed and its j-th tensor power. Every shifted parameter is still real and irrational. In particular N^m is the pullback of the fixed one-dimensional fibre O(c)|_c; choosing a basis of that fixed line gives its usual torsion trivialization, with that choice explicit.

## 3. Every conormal graded factor vanishes

Since S is smooth in smooth Y, its conormal sequence is

0 -> N^* -> Omega_Y^1|_S -> Omega_S^1 -> 0.

Locally S=(s=0), the first map sends the class of s to ds; the last is restriction modulo ds. This uses the reduced divisor equation s, not df for the multiple fibre s^m. Tensor with L_r|_S tensor (N^*)^j. Its outside terms are

L_(r-epsilon(j+1)/m)|_S
and
Omega_S^1 tensor L_(r-epsilon j/m)|_S.

The first H^0 vanishes by Section1. The second H^0 vanishes by the irrational-parameter conclusion of the named A.4.9 input on every smooth reduced support; its torsion-free cotangent sheaf is Omega_S^1 here because S is smooth. Left exactness therefore gives H^0(S,G_j)=0 for G_j=(Omega_Y^1 tensor L_r)|_S tensor (N^*)^j, for all j=0,...,m-1. Every shift and every conormal arrow has been specified.

A.3.1 gives the actual exact sequences

0 -> G_(k-1) -> (Omega_Y^1 tensor L_r)|_(kS) -> (Omega_Y^1 tensor L_r)|_((k-1)S) -> 0.

Their maps are inclusion of the (k-1)-st Cartier ideal power and reduction of the truncated local module. Induction starting from k=1 proves H^0(mS,(Omega_Y^1 tensor L_r)|_(mS))=0. No splitting and no discarded nilpotent layer enters this argument.

## 4. Finiteness of the full fibres that need simultaneous treatment

The critical set of f is a compact analytic subset of Y, hence has finitely many irreducible components. On the smooth locus of each component df=0, so f is constant there and, by continuity, on that component. Its image is a finite set. Every fibre mS with m>=2 and smooth support is critical along S because its local base function is a unit times s^m. Thus there are only finitely many such fibres. This gives a genuinely finite set of multiplicities and graded factors to treat.

## 5. An explicit holomorphic finite-dimensional kernel map

For completeness, we prove analyticity of the required exceptional set on these smooth supports by a finite reduction, rather than inferring it from numerical upper semicontinuity alone. Pic(Y)=H^1(Y,O_Y) is a finite-dimensional complex vector space under the exact exponential isomorphism. Choose a basis and additive Cech representatives. Exponentiating their linear combinations gives a holomorphic family of the actual line bundles on Y and hence on each S. On a small parameter ball about t0, a smooth partition of unity applied to holomorphic parameter-dependent logarithms of the transition ratios gives smooth gauges, holomorphic in the parameter, identifying the underlying smooth bundles with the central bundle. In that gauge the Dolbeault operator is D_t=D_0+A_t, with A_t a degree-one, order-zero operator depending holomorphically on t, A_t0=0, and

D_0 A_t + A_t D_0 + A_t^2=0.

This construction applies to each fixed bundle Omega_Y^1|_S tensor (N^*)^j tensored by the varying parameter line.

Choose Hermitian metrics on S and the fixed bundle. The classical elliptic Dolbeault Laplacian Delta=D_0 D_0^*+D_0^* D_0 has finite-dimensional harmonic spaces, orthogonal projection P, inclusion I, and Green operator G. Let h=D_0^*G. The actual operators satisfy

D_0 h+h D_0=1-IP,  P I=1,  P h=0, h I=0.

These inputs have been opened in Demailly's author-hosted Introduction to Hodge Theory PDF: Part I Theorem3.15, printed p15/physical27, and Theorems7.1–7.2, printed p32/physical44. They apply to arbitrary compact Hermitian manifolds and Hermitian holomorphic vector bundles; no Kähler identity is used here.

On a fixed sufficiently high Sobolev space, h A_t is bounded and small after shrinking the parameter ball; the same is true on the adjacent degree/regularity spaces used below. Set T_t=(1+h A_t)^(-1) by the convergent Neumann series. Its coefficients depend holomorphically on t. Define the finite matrix

M_t=P^1 A_t T_t^0 I^0 : H^0_harmonic -> H^1_harmonic.

Here superscripts designate form degrees, not cohomology assumptions. We now give both maps proving

ker(D_t in degree0) = T_t^0 I^0 ker(M_t).

If D_t u=0, the degree-zero contraction gives u-IPu=hD_0u=-hA_tu, hence u=T_t I(Pu). Conversely, put u=T_t I v. Since u=Iv-hA_tu, applying D_0 and the contraction identity gives

D_t u = I P A_t u + h D_0 A_t u
       = I P A_t u - h A_t D_t u.

Thus D_t u=T_t^1 I^1 M_t v. If M_t v=0 then D_tu=0. Also P T_t I=1 follows from Ph=0, so projection P is the inverse map on kernels. Sobolev solutions with D_tu=0 are smooth by elliptic regularity. Every map has now been specified, and the finite matrix is holomorphic in the parameter.

The locus where the section space is nonzero is consequently the locus where M_t fails to have full column rank, cut out by its maximal minors (with the usual empty-domain and too-few-row cases treated directly). This is a closed complex analytic subset locally at every parameter, hence globally for the family. The construction is a kernel calculation on smooth S, so no claim about a nonreduced Dolbeault resolution is needed.

## 6. The stated proper analytic exceptional set

For each of the finitely many smooth multiple fibres mS and each j=0,...,m-1, apply Section5 to its bundle G_j. Let Z be the finite union of the resulting analytic nonzero-section loci in Pic(Y). Section3 supplies one common parameter L_r, for every irrational real r, outside all these loci; thus Z is proper. For B outside Z all its graded groups vanish. The actual sequences in A.3.1 then give simultaneous full-fibre vanishing for every listed mS. This proves the generic assertion with all nilpotent layers retained.

## 7. Computation and source scope

A fresh exact symbolic program will check the finite-kernel identity above on perturbed complexes with nonzero contractible blocks, including inverse maps and ranks at the stated rational parameter grid. It also checks the rational-shift identities and finite-order powers for the stated m/j/epsilon bounds. No finite computation is used to infer an irrational nontriviality statement or a universal analytic theorem; those are proved above.

The source input from CDP20 is the original Remark7.2 p693 and the stated Proposition7.3 context, with Remark7.4 p695 distinguished as the singular-support comment. The actual full scheme-theoretic vanishing and all irrational parameters are established by the maps above, using the named A.4.9 proved input. Demailly's classical Green/Hodge input is credited at the exact author-PDF pages opened. Grauert1960 §7 Satz3 gives upper semicontinuity; its 1963 correction retracts closedness of the general Satz2 base-change-failure locus. Neither unqualified failure-locus assertion is used to replace the finite kernel argument in Section5.
