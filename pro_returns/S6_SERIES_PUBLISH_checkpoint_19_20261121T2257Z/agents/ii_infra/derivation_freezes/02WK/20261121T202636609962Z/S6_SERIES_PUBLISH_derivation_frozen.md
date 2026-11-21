# Prerelease derivation: 02WK / night:P4.13

Checker: `i_provenance_recovery`. I read the exact original safe
statement and its empty supplement. I have not read the target
proof, its method outline, or any former A/C computation or repair
record. Related Paper I degeneration mathematics is prior exposure.
The primary input actually read is A'Campo, *La fonction zêta d'une
monodromie*, Comment. Math. Helv. 50 (1975), 233–248: Theorem 1
on p.235, the complete proper-analytic normal-crossing construction
in §2, pp.237–243, and the local-trace/spectral-sequence calculation
in §3, pp.243–245. Exact journal scan SHA256
`8562e8ca2b2ab297873b2c07929d73910585072b286e390d4c0dbf028a75c03d`,
retrieved from the archive's advertised bot PDF endpoint. Its §2
starts with a proper analytic map from a smooth analytic space to
a disc; no Kähler total-space hypothesis is present.

Work over a sufficiently small closed subdisc of the given
degeneration g:U→Δ. Its compact central support is S and its
smooth nearby fibre F is a complex two-torus. Choose an embedded
resolution π:U'→U of the reduced divisor S, with all centres over
Sing(S), isomorphic over U\Sing(S), and with total transform a
simple normal-crossing divisor. The resolution can first
principalize the singular-locus ideal, so that its inverse image
is contained in the exceptional divisor. Write

    (gπ)^*(0)=m E0 + Σ_j N_j E_j,

where E0 is the strict transform of the single irreducible S and
the E_j are exceptional. The local coordinate changes identifying
U' and U off S identify their nearby fibres, including their
monodromy maps, exactly.

Every N_j is at least 2m. To see this for its divisorial valuation
v_j, let B be its centre in U, which lies in Sing(S). At a general
smooth point of B, a reduced local equation h of S has no constant
or linear normal term, because h and its first derivatives vanish
on B. Thus h∈I_B² locally at that generic point. The integral
valuation v_j is positive on I_B, hence v_j(h)≥2. The given full
fibre has local equation g=u h^m for a unit u, giving
N_j=v_j(g)=m v_j(h)≥2m. The strict-transform multiplicity is m
because π is an isomorphism over the smooth locus of S.

For each irreducible component E_i of the total transform, let
E_i° be its complement of the other components. In particular
π:E0°→S_reg is an isomorphism: π is an isomorphism over S_reg,
and every point lying over Sing(S) belongs to the exceptional
divisor and has been removed from E0°. This identifies the exact
open stratum, rather than replacing a resolution Euler number by
the Euler number of a different surface.

Here is the global trace calculation from the normal-crossing
model. Near a point on r components, a unit can be absorbed into
one coordinate and the map is z1^n1...zr^nr. The local nearby
fibre has d=gcd(n1,...,nr) connected components, each homotopy
equivalent to (S1)^(r−1). Monodromy cyclically permutes those
d components; its d-th power acts on each by a torus translation,
which induces the identity on cohomology. For r=1, the alternating
trace of the k-th monodromy is n1 when n1 divides k and is zero
otherwise. For r>1, it is zero: without a fixed component its
trace is zero, and with fixed components the alternating trace
is d times the Euler number of a positive-dimensional torus.

The Leray/nearby-cycle spectral sequence in A'Campo §2.4,
pp.242–243, identifies the cohomology of F with the hypercohomology
of this local system of nearby-cycle complexes on the compact
central divisor. A finite stratified triangulation computes the
alternating trace by summing each open-cell trace with its cellular
sign. Therefore the trace integral of a locally constant stalk
trace on a stratum is its Euler characteristic times that trace.
This argument allows nontrivial local systems along strata; it
does not assume a global splitting of their finite covers. It
gives the proper-analytic formula

    L(T^k;H•(F,Q))= Σ_(n_i divides k) n_i e(E_i°).

The Euler characteristic here agrees with the ordinary one in
the statement: the open strata E_i° and S_reg are smooth complex
surfaces, so Poincaré duality in even real dimension identifies
their compact-support and ordinary Euler characteristics. The
finite analytic triangulations make all these Euler numbers finite.

Set k=m. None of the exceptional N_j≥2m divides m, so only E0°
contributes. The proved open-stratum isomorphism gives

    L(T^m;H•(F,Q))=m e(S_reg).

The cohomology ring of the real torus underlying F is canonically
the exterior algebra on H1(F,Q)^∨. If A is the given monodromy on
H1(F,Q), natural evaluation gives T on H1(F,Q)^∨ as A^T: for a
cohomology functional α and a cycle c, (Tα)(c)=α(Ac). On degree q
it is Λ^q(A^T). Hence the exterior-character identity gives

    L(T^m)=Σ_(q=0)^4 (−1)^q tr Λ^q((A^m)^T)
          =det(I−(A^m)^T)=det(I−A^m).

This proves the required equality with the exact homology-to-
cohomology transport, rather than identifying their matrices
without the dual map.

For the numerical bounds, the same normal-crossing model proves
quasi-unipotence without a polarization assumption. Let N be a
common multiple of the finitely many component multiplicities.
On every local nearby-cycle cohomology group T^N is the identity,
by the finite permutation and translation computation above.
It is consequently the identity as a morphism of each nearby-
cycle cohomology sheaf, and also on the cohomology of those sheaves.
The spectral sequence gives a finite T-invariant filtration of
H1(F,Q) on whose associated graded T^N is the identity. Thus
(T^N−I)^M=0 for some finite filtration length M. Every eigenvalue
of T, and therefore of A, is a root of unity.

The real 4×4 matrix A^m has nonreal eigenvalues in conjugate
pairs. The factor for such a pair is |1−λ^m|², which lies in
[0,4]. Each real root-of-unity eigenvalue is ±1 and contributes
0 or 2 to det(I−A^m). Multiplying the four factors, grouped into
conjugate pairs, gives 0≤det(I−A^m)≤2^4=16. Jordan blocks do
not affect the determinant. Dividing the proved equality by
the actual positive integer m yields 0≤e(S_reg)≤16/m.

The new exact exterior-matrix certificate below checks the
universal trace identity on a symbolic 4×4 matrix. The eigenvalue
bound and all multiplicity/stratum arguments above are universal
proofs; no sample family or bounded list of monodromies is used.
No compactification or its Betti numbers enters any step.
The target proof remains unopened until this derivation freezes.

Prerelease computation: `agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_02WK_preproof_exterior.py`, SHA256 `a03cab94eb5e74f798a66663ca77dbd2915a64f6a049426f7f4e0d11e9e197f4`.

Prerelease computation: `agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_02WK_preproof_exterior.output.json`, SHA256 `585777327ef3cff33104ada77a91ce66432b09a276b603508a1a3632e34b3cde`.
