# Derivation before target proof: 01CA

Owner `cdp:st:C.2.NC.3`; checker `i_provenance`. The complete safe target
packet, its cited compendium C.2.NC.1 statement, and the C.2.NC.2 statement
have been read. No target proof, previous target check, or old program has
been opened. Related Paper I mathematics is prior exposure. The adjacent
C.2.NC.2 derivation has been written independently and will freeze before
either target proof is opened.

The exact supplied local-to-global input for a fibre sum m_i S_i is
e(Y_t)=sum_i m_i e(T_i minus D_i), where T_i normalize its support and
D_i are their reduced conductors. Apply it to the uniform multiplicity
m. The smooth general fibre has Euler number zero, so

    sum_i e(T_i)=sum_i e(D_i).

The C.2.NC.2 formulas give sum e(C_alpha)=3tau and consequently
sum e(D_i)=3tau. Their second topological identity then gives

    e(S)=sum e(T_i)-sum e(C_alpha)+tau=3tau-3tau+tau=tau.

All multiplicities in this argument are the actual uniform multiplicity
m>0, which is divided out only after the stated local-to-global formula.

Here is the normalized base-change map. At any point of S choose local
normal-crossing coordinates x_1,...,x_r, r<=3, and write
f^*t=u(x)(x_1...x_r)^m, with u a holomorphic unit. On a simply connected
coordinate neighborhood choose a holomorphic root v with v^m=u.
The fibre product for t=s^m has equation

    product_(zeta^m=1)(s-zeta v x_1...x_r)=0.

Its normalization is the disjoint union of the m smooth graphs
s=zeta v x_1...x_r. Each graph maps isomorphically to the original
coordinate neighborhood by forgetting s, and its map to the s-disc
has reduced normal-crossing zero divisor. These local normalizations
glue by the uniquely determined root permutations to a finite etale
degree-m map Y'->Y over a sufficiently small neighborhood of the compact
central fibre. No global choice of v is required.

Restriction gives an etale degree-m cover S'->S of the reduced supports;
it has degree m on every stratum. Each triple point has m preimages,
all triple points, by the graph coordinates. Thus e(S')=m e(S) and
tau(S')=m tau(S). These are statements for the entire covers, so their
validity does not depend on connectedness of Y' or S'. The target proof
remains unopened until this complete derivation freezes.

Preproof certificate: `agents/ii_checks_provenance/computations/S6_SERIES_PUBLISH_II_01C9_preproof_branch_complex.py`, SHA256 `d9a4a9ab7f26e25e2fb4969e280e5278362ee1d6bdeb43ff9375bc3884db1332`; output `agents/ii_checks_provenance/computations/S6_SERIES_PUBLISH_II_01C9_preproof_branch_complex.output.json`, SHA256 `0b627b22cb5a097cf7d492a7a2ef0e07956f18a4ac74264279e6c809602e1b14`. Both existed before freeze.
