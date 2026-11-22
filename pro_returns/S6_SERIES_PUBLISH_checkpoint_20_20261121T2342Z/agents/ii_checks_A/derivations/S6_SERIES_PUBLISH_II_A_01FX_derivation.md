# Independent derivation: cdp:st:D.1.12 (tag01FX)

The target proof has not been opened. Inputs read: the exact statement, supplemental E4, CDP20 Section5's published assertions, and Borcea1984 §§1–3 (including visual inspection of pp.374,376). The fresh calculation program is `code/S6_SERIES_PUBLISH_II_A_01FX_index.py`; it is independently written and uses no earlier target code.

Let E=R^1f_*O_Y and Q=R^2f_*O_Y. E4 makes E a vector bundle and gives h^0(F_c,O_{F_c})=1 for every full fibre. The general fibre is a two-torus or primary Kodaira surface; both have (h^0,h^1,h^2)=(1,2,1), so E has rank2 and Q rank1.

The cup product wedge^2 H^1(F,O_F)→H^2(F,O_F) is nonzero, hence an isomorphism, on a general fibre. For a torus, invariant anti-holomorphic one-forms compute these Dolbeault groups, and the wedge of a basis is a nonzero volume class. For a primary Kodaira surface use Borcea's quotient transformations (z,w)↦(z+alpha,w+bar(alpha)z+beta). The forms phi1=dz and phi2=dw−bar(z)dz descend. They satisfy d phi1=0, d phi2=phi1 wedge bar(phi1). Thus bar(phi1),bar(phi2) are bar-partial-closed, as is their wedge. The holomorphic form Omega=phi1 wedge phi2 is closed and nowhere zero. The integral of Omega wedge bar(Omega) is nonzero, since its constant orientation factor times the positive volume has positive integral. Stokes' theorem would make that integral zero for a bar-partial-exact bar(Omega). Hence the wedge class is nonzero. This also proves the independence of the two degree-one classes. The trivial canonical bundle gives h^2=1 by Serre duality, and the elliptic bundle topology gives Euler number0, so the surface Riemann–Roch identity gives chi(O_F)=0 and h^1=2.

Set T=torsion(Q), A=Q/T. On a nonsingular curve A is a line bundle. The cup product induces a generically nonzero map det(E)→A, therefore a nonzero section of A tensor det(E)^{-1}. Its zero divisor is effective, and consequently deg A−deg E is a nonnegative integer. This is an explicit line-bundle degree comparison; the map is the induced cup product.

The holomorphic Euler characteristic of the compact complex threefold Y is (1/24) integral c_1(T_Y)c_2(T_Y). This is the degree-six Todd class in the complex analytic index formula; the fresh program expands its three Chern roots exactly and verifies that coefficient. Because H^2(Y;R)=0, c_1(T_Y) is zero rationally and chi(Y,O_Y)=0. The Leray Euler characteristic gives

0=chi(C,O_C)−chi(C,E)+chi(C,Q)
 = (1−g)−(deg E+2(1−g))+(deg A+(1−g)+length T)
 = deg A−deg E+length T.

Every higher direct image above R^2 vanishes because fibres have complex dimension2. The rank terms and genus terms cancel with the displayed signs. The program independently checks this polynomial identity as well. Both summands in the final equality are nonnegative integers; hence each is zero. It follows that T=0 and that the cup-product map det(E)→Q has zero divisor of degree0, hence no zero and is an isomorphism.

Finally all R^qf_*O_Y, q=0,1,2, are locally free. The local base-change complex over the regular one-dimensional base may be chosen as a finite complex of finite free modules. Its fibre-cohomology exact sequence has the form 0→(R^qf_*O_Y)⊗C(c)→H^q(F_c,O_{F_c})→Tor_1(R^{q+1}f_*O_Y,C(c))→0. All right-hand terms vanish by the just-established local freeness (and R^3=0). This proves base change at each fibre and fixes the dimensions as (1,2,1). The map obtained by evaluating the global cup product agrees with the fibre cup product by functoriality of multiplication of cochains, so the isomorphism claimed in the statement has precisely that meaning.

The argument uses b_2(Y)=0 only in the index vanishing. It retains the full scheme-theoretic fibre throughout and introduces no reducedness assumption.
