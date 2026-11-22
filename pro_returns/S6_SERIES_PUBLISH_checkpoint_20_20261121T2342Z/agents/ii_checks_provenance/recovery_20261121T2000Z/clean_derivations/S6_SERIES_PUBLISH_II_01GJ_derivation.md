# Prerelease derivation: 01GJ / cdp:st:E12

Checker: `i_provenance_recovery`. The exact safe statement and its empty
supplement were read. Neither the II target proof, another checker's
reconstruction, nor `E_checks.py` has been opened. Related Paper I
cohomology calculations are disclosed prior exposure. The published
CDP98 Lemma 1.5 and its complete proof were independently read at
pp.79–80 in the journal PDF (SHA256
`7e97396a1bea596bd086f6f1fb948ac418a2455a4562b24ad37e38227f512b7e`).
That lemma claims local freeness for every locally free sheaf on every
smooth compact threefold mapping surjectively to a smooth curve, so
the present product and line bundle satisfy its stated hypotheses.

Write p:A×A→A for projection to the second factor, and write B0={0}×A.
The given bundle is P=O(Δ−A×{0}−B0). Put

    N=P(B0)=O(Δ) tensor p*O_A(−0).

There is the actual Cartier restriction sequence

    0 → P → N → N|B0 → 0.

The restriction of O(Δ) to B0 is O_A(0), since the diagonal meets B0
transversely at (0,0). Thus N|B0 is O_A. For each t, O(Δ)|A×{t}
is O_A(t), a degree-one bundle. Riemann–Roch and Serre duality on
the elliptic curve give h0=1 and h1=0. The canonical section of
O(Δ) is nonzero as a section on every fibre, and therefore identifies
p_*O(Δ) with O_A; cohomology and base change gives R1p_*O(Δ)=0.
Projection formula gives p_*N=O_A(−0), R1p_*N=0.

Under these identifications the pushforward of the restriction map
is the canonical inclusion O_A(−0)→O_A. Indeed it is restriction of
the canonical diagonal section to B0; in a local coordinate at the
origin the diagonal has equation z−t, and its restriction to z=0
has a simple zero. Consequently the direct-image sequence is

    0 → p_*P → O_A(−0) → O_A → R1p_*P → 0,

with middle map locally multiplication by a uniformizer times a unit.
It follows that p_*P=0 and R1p_*P=C_0, of length exactly one. There
are no higher direct images for this relative curve. Equivalently
Rp_*P is represented by [O_A(−0)→O_A] in degrees zero and one,
and has the single cohomology sheaf C_0 in degree one.

Let q:Y→A×A forget the P1 factor, so g=pq. The two-chart Laurent
Čech calculation for O_P1(−2) gives H0=0 and H1=C, with the class
of z^(−1) as basis: the coboundaries contain every Laurent monomial
of exponent at least zero or at most −2, and those two sets leave
exactly exponent −1. Therefore Rq_*V=P[−1]. Composing the two
derived direct images shifts the preceding two-term complex by one;
its only cohomology is R2g_*V=C_0. This proves g_*V=R1g_*V=0.
The Leray sequence over A now has the single term H0(A,C_0)=C
in total degree two. Thus h•(Y,V)=(0,0,1,0).

For a fixed t, P restricted to A×{t} is O_A(t−0) tensored with a
one-dimensional constant vector space. The Abel map A→Pic0(A),
t↦O_A(t−0), identifies its trivial member precisely at t=0.
One can verify that injectivity here without a general Picard
identification: a function with divisor t−0 for t≠0 would give a
degree-one map from the elliptic curve to P1, contradicting the
genus formula. A nontrivial degree-zero line bundle has no nonzero
section, since an effective divisor of degree zero is empty and
such a section would trivialize the bundle. Serre duality gives
H1=0 as well. At t=0, H0=H1=C. Tensoring the actual fibre complex
with the one-dimensional H1(P1,O(−2)) shifts these degrees by one,
giving zero in every degree for t≠0 and (0,1,1) for t=0.

The fresh local-complex certificate records both the order-one
uniformizer and the fibre-derived specialization. It supplies a
finite exact check of the displayed numbers; the full sheaf and
all-orders length argument above proves the statement. The target
proof remains unopened until this derivation freezes.

Prerelease computation file: `agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_01GJ_preproof_complex.py`, SHA256 `f537f01eca64dbf070617c1b84e5b61fc6a142fb94d490bf5e310fc4024dde7d`.

Prerelease computation file: `agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_01GJ_preproof_complex.output.json`, SHA256 `1367ac776bd98776dcfeea8e489c8988d89bbe27563ccc583fd9fab5603a261f`.
