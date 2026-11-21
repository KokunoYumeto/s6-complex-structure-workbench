# Derivation before target proof: 01C9

Owner `cdp:st:C.2.NC.2`; checker `i_provenance`. The complete safe
statement packet and empty supplement have been read. No target proof,
previous target check, or old target program has been opened. Related
Paper I and the released Paper II normal-crossing checks are prior exposure.

Let T be the disjoint union of the smooth normalization components T_i.
The local residue formula for a reduced normal-crossing equation gives
omega_(T_i)(D_i)=nu_i^*omega_S. Here omega_S=(omega_Y tensor O_Y(S))|_S.
Both ambient line bundles have rationally zero Chern class. Thus
c1(K_(T_i)+D_i)=0 rationally on T_i.

Normalize every conductor curve in T. Its map to the normalization C_alpha
of the double locus is an etale cover of total degree two, including at
preimages of triple points: in the chart xyz=0 a chosen double branch,
say x=y=0, lifts to one axis in each of the x and y surface branches.
The two lifts remain distinct at the origin. Let C' be a connected cover
component of degree d over C_alpha. In the normalized surface its
conductor has ordinary nodes at the preimages R' of triple points.
Adjunction with the other conductor branch gives the actual line map

    (K_(T_i)+D_i)|_(C') = K_(C') tensor O_(C')(R').

This formula also applies to a self-node of a global conductor component
after normalizing that component; each node contributes one point on
each local branch. Its degree is zero. Since C' -> C_alpha is etale and
R' is the inverse image of R_alpha, division of the degree equation by d
gives 2g(C_alpha)-2+deg R_alpha=0. Therefore e(C_alpha)=deg R_alpha.
Each triple point contributes one marked point on each of its three
normalized double branches, so sum_alpha e(C_alpha)=3 tau. In particular
each genus is at most one.

For the coherent Euler characteristic, use the exact local restriction
complex of x_1...x_r=0, r<=3:

    0 -> O_S -> direct-sum O_(surface branches)
      -> direct-sum O_(pair intersections)
      -> direct-sum O_(triple intersections) ->0,

with alternating restriction maps. Exactness is verified successively
from (x) intersection (y)=(xy) in the regular local ring, or directly
by the monomial decomposition according to the coordinates dividing
each monomial. The branch-index permutations preserve this complex
with the ordinary alternating signs. Hence it descends even when local
branches belong to the same global component. Its pair term on C_alpha
is a line L_alpha from the sign representation of the branch-ordering
double cover; L_alpha^2=O. Its triple term has one-dimensional stalk
at each triple point. Thus

    chi(O_S)=sum_i chi(O_(T_i))-sum_alpha chi(L_alpha)+tau.

The ambient ideal sequence and smooth threefold Riemann--Roch give
chi(O_S)=0: c1(O_Y(S)) vanishes rationally, so
ch(O_Y)-ch(O_Y(-S))=0. On the smooth compact C_alpha, the torsion line
L_alpha has degree zero and chi(L_alpha)=1-g(C_alpha)=e(C_alpha)/2.
The displayed coherent formula and sum e(C_alpha)=3 tau now give
sum_i chi(O_(T_i))=tau/2. Its left side is integral, proving tau even.
This calculation does not replace a branch-ordering local system by the
trivial line; it uses its actual torsion degree and Riemann--Roch.

For the topological identities let D^circ be the double locus with all
triple points removed, and let S^circ be the smooth locus. Normalization
of the double locus deletes 3 tau points to give D^circ, so
e(D^circ)=sum e(C_alpha)-3 tau. The normalization map has exactly
one, two, and three points over the S^circ, D^circ, and triple strata.
Euler characteristic of a finite cover multiplies by its degree, so

    sum_i e(T_i)=e(S^circ)+2e(D^circ)+3tau,
    e(S)=e(S^circ)+e(D^circ)+tau.

Subtracting gives e(S)=sum_i e(T_i)-sum_alpha e(C_alpha)+tau.
The union of conductor curves in the normalization has degree two over
D^circ and has three points over each triple point (each is a node of
the conductor). Hence

    sum_i e(D_i)=2e(D^circ)+3tau
               =2sum_alpha e(C_alpha)-3tau.

These are the stated topological identities. The fresh finite certificate
constructs the actual alternating branch-index matrices and solves the
resulting universal rational Euler relations. It does not assume that
branches globally split or that their monodromy is trivial. The target
proof remains unopened until this derivation freezes.

Preproof certificate: `agents/ii_checks_provenance/computations/S6_SERIES_PUBLISH_II_01C9_preproof_branch_complex.py`, SHA256 `d9a4a9ab7f26e25e2fb4969e280e5278362ee1d6bdeb43ff9375bc3884db1332`; output `agents/ii_checks_provenance/computations/S6_SERIES_PUBLISH_II_01C9_preproof_branch_complex.output.json`, SHA256 `0b627b22cb5a097cf7d492a7a2ef0e07956f18a4ac74264279e6c809602e1b14`. Both existed before freeze.
