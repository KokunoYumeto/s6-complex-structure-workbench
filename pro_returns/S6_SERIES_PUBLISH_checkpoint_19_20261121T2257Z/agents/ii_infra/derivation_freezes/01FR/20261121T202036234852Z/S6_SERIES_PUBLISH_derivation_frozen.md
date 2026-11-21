# Derivation before target proof: 01FR

Owner `cdp:st:C5a`; checker `i_provenance`. I have read the complete exact
safe statement packet and its empty supplement. No target proof, old
check, or old program has been opened. The related Paper I normalization
and tangent-sheaf mathematics is disclosed prior exposure.

In a smooth local chart with S=(x_1...x_r=0), r<=3, the logarithmic
tangent sheaf consists of the vector fields

    sum_(i<=r) x_i a_i partial_(x_i)
      + sum_(j>r) a_j partial_(x_j).

To prove this characterization directly, delta(x_1...x_r) belongs to
the principal ideal (x_1...x_r) exactly when, modulo (x_i), the term
delta(x_i) product_(j!=i)x_j is zero. The latter product is a non-zero-
divisor in the regular quotient ring O_Y/(x_i), so delta(x_i)=0 modulo
x_i. These conditions for all i are exactly those in the display.

The canonical normal map restricts an ambient vector field to each
normalized local branch and then takes its class modulo that branch's
tangent space. In these coordinates it is

    sum a_j partial_(x_j) |-> (a_i mod x_i)_(i=1,...,r).

Each component a_i can be lifted independently, so the map is surjective.
Its kernel is precisely the logarithmic tangent sheaf just computed.
Each local target is the normal line of the corresponding branch. These
maps are defined by the differential of the normalization immersion and
therefore glue to nu_*N_nu, including permutations and self-intersections
of global branches. This proves the stated coherent exact sequence.

The actual normal-bundle sequence on the smooth normalization is
0 -> T_(tilde S) -> nu^*T_Y -> N_nu ->0. Taking determinants gives
N_nu=det(nu^*T_Y) tensor det(T_(tilde S))^(-1)
=K_(tilde S) tensor nu^*K_Y^(-1), exactly the line in the statement.

Tensor the coherent sequence by the invertible L. The projection formula
identifies the quotient with nu_*(N_nu tensor nu^*L). A finite holomorphic
map has exact direct image on these coherent modules (locally the map is
finite and its fibres are zero-dimensional), so its cohomology is the
cohomology of that line bundle on tilde S. The long exact sequence gives
the exact equality of the stated image and kernel in degree two, with
its next term H3(Y,T_Y(-log S) tensor L).

Finally Serre duality on each compact smooth normalization component
identifies H2(N_nu tensor nu^*L) with the dual of
H0(K_(tilde S) tensor N_nu^(-1) tensor nu^*L^(-1)). Substitution of the
determinant-line isomorphism above cancels K_(tilde S) and gives
H0(nu^*(K_Y tensor L^(-1))) dual. Taking the direct sum over components
preserves this identification. No surjectivity of the resulting H2 map
is asserted beyond its exact kernel criterion. No numerical calculation
is used. The target proof remains unopened until this derivation freezes.
