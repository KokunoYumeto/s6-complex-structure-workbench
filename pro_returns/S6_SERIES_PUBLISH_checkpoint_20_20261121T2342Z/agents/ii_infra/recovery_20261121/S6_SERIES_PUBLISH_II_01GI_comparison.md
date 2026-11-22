# 01GI / E11: complete comparison and final publication pair

The derivation was frozen at 23:13:36 UTC, before release of the target
proof or old E11 routine. The complete released owner is byte-identical
to the current original block c81d7360…. I read its proposition and all
four proof items. I then read the whole final v2 proposed owner, hash
8f9afcbf…, including every retained argument and all added maps. Both
complete bibliography entries have also been read.

## Mathematical result and exposed inputs

The result is h(T_X)=(1,1,1,0), with a smooth reduced one-dimensional
Kuranishi germ and a locally miniversal nonzero-scale family, for exactly
the sphere data and the original admissible p!=0 affine-twist data in
the statement. No wider collection of logarithmic data is asserted.

The input receipt discloses the earlier local Paper I p321 reading and
the already released full GK/E13 proof. The current-I input theorem's
statement itself contains the desired conclusion; the fresh derivation
explicitly does not use that conclusion as a premise. It uses the given
root bundles and supplies their actual higher-root/affine transport,
then derives all tangent dimensions and the scale class. Neither the
GI target proof nor E11 old computation was read before the freeze.

## All four original proof items

1. **Root transport and logarithmic sequence.** The global morphism is
   [x:y]->[x^l:y^k] from P(3k,4l) to P(3,4); its degree line is O(kl)
   and its coarse coordinate is unchanged. At the order-three and
   order-four points it is exactly the two local higher-root maps.
   The actual finite filling is the smooth pulled-back torus chart
   with affine action t_a B. Its derivative on invariant fields is B,
   and its translation acts identically on Hq(O). This proves the
   equivariant descent comparison for the fixed period family. The
   final wording states this map explicitly, avoiding a claim that an
   arbitrary varying Hodge bundle is determined by monodromy alone.
   The cusp uses the same hexagon and constant boundary cocycles, so
   the resulting V,G,R2 bundles are O+O(-kl),O+O(-kl),O(-kl).
   The ordinary horizontal tangent must change to O(r+s); the log
   correction at the one cusp is O(-rs). Thus the printed L and
   canonical bundle are exactly those obtained by the actual sequence.

2. **Low-degree cohomology.** The root-stack pushforward of O under
   each additional finite cyclic root has exact invariants, giving
   H^*(O(-kl))=H^*(O(-2kl))=0. My independent proof establishes the
   same vanishing by the universal equation 3a+4b=1 or2 with a,b>0.
   The printed horizontal line L=O(r+s-rs) has coarse degree -1:
   an invariant ordinary vector field vanishes at each root point,
   and the additional cusp condition subtracts one ordinary point.
   Both L and L(-kl) have negative weighted degree, so the relevant
   H0 terms vanish. The logarithmic and normal exact sequences then
   give h0=h1=1 exactly as printed.

3. **Degree three, Euler characteristic and affine twists.** The
   cotangent boundary has full generic rank by its stated E7 input.
   A holomorphic ambient one-form is horizontal, and submersion points
   on the root charts and on a smooth point of the cusp component
   force its base coefficient to extend. This proves the actual
   pushforward morphism to Omega_B. Weighted Serre duality reduces
   h3 to H0(O(kl-2r-2s)). The displayed congruence gives b+2>=k and
   a term at least4kl, so this group is zero. I also expanded
   ch(T)*td(T): chi(T)=integral(c1^3/2-19c1c2/24+c3/2). On S6 the
   first two Chern-number terms vanish and integral c3=2, hence chi=1.
   The original affine-twist argument uses instead the acyclic root
   lines O(-5),O(-6) and the dP6 normal quotient. It therefore proves
   all of its stated admissible p!=0 cases directly, including |p|>1.
   That entire calculation is retained; only its trailing reassurance
   is removed.

   My prerelease route gives an additional exact comparison. With
   Jimage the image of df and Q its reduced critical-conductor quotient,
   h(Q)=(1,2,0,0). Put epsilon=1 for k=1 and0 otherwise. Weighted
   arithmetic gives h(f^*T_B)=(1,1+epsilon,epsilon,0). Evaluation at
   the cusp is an isomorphism on H0 and injective on H1, using the
   nonzero monomials xy and, when present, x^(l+1) in different
   summands. Therefore h(Jimage)=(0,0,1,0), and the vertical exact
   sequence yields (1,1,1,0) without RR. This is an actual map
   comparison, and keeps the change of intermediate cohomology when
   k>1 visible.

4. **Scale class and miniversality.** The original argument correctly
   rules out trivialization of the nonzero torus class by a base
   automorphism: the two multiple values and the hexagonal value are
   fixed, including over the dual numbers. I retained this full
   argument. The vague nonzero-scalar comparison preceding it has
   been replaced with the exact maps verified before target release.

   In the primary integral basis, C*P_V=P_mark and the marked
   coordinates are (-d,-b,6d-a,delta+b-2d). Hence
   Pi_c*P_V^-1 has columns (0,1),(-1,0),(-tau,1-mu),
   (6-6mu,-beta_c-2). The additive map diag(-1,1) gives the normalized
   semiabelian period matrix with zP=1-mu and rho=-beta_c-2.
   It follows that gamma_marked=-psi_primary. Under
   W=exp(2*pi*i*zeta2), e=partial_zeta2 maps to2*pi*i times the Euler
   field Xi. With the specified inverse-period reference, the actual
   forward generator is Phi_u=u*phi and u=exp(-2*pi*i*c). Thus

       kappa_u=u^-1 Xi tensor psi
              =-(2*pi*i*u)^-1 e tensor gamma,
       kappa_c=e tensor gamma.

   These are coherent fibre classes and their coherent Leray extensions.
   No global integral H1(X,Z) class is inferred; on the sphere it is
   zero. The unique coherent class is determined by its nonzero edge
   image. The final paragraph supplies the complete one-variable local
   algebra: a nonzero-derivative classifying map is an analytic
   substitution isomorphism before quotienting; its obstruction ideal
   is killed by that isomorphism, hence is zero. This proves the full
   smooth reduced germ and miniversality.

## Exact computation-method comparison

The prerelease program checks the higher-root degree map, all marking
matrices, both finite-monodromy conjugacies and every period coefficient.
It also enumerates weighted monomials for1,965 coprime pairs with
1<=k,l<=80. The unrestricted claims are proved by congruences in the
frozen derivation; the finite range is only an implementation check.

The old E11-only slice, supplied after the freeze, is bytes1634–2419,
lines51–74 of the pinned original, plus its two imports. I read and ran
only that slice. It checks489 pairs through40 using modular inverses,
fractional residue degrees and a direct monomial search. Its execution
passes. The full E_checks file and its E14 block remain closed.

The new postrelease program uses a different method. It forms the
coefficients of H(T)=1/((1-T^r)(1-T^s)) by the exact recurrence

    H(n)=H(n-r)+H(n-s)-H(n-r-s), H(0)=1, H(n)=0 for n<0.

Weighted Serre duality supplies H1, and chi-1 supplies the coarse degree.
No modular inverse, fractional residue formula or monomial search is
used. Every old identity passes for the full1,965-pair range. The largest
coefficient index is81,046. There is also a universal proof for the
old coarse-degree L-kl identity: its Serre-dual monomial equation is
3a+4b=13 with positive a,b, whose only solution is(3,1). Its exponents
are(3l-2,k-2), which are allowed exactly when k>1. This gives coarse
degree -1 for k=1 and -2 otherwise, with no finite-range inference.
The same program expands the RR polynomial above by exact rational
coefficient multiplication. Both complete programs and outputs were read.
This postrelease work adds no new independent event.

## Primary edition and publication changes

I retrieved the exact public PDF from arxiv.org/pdf/2610.39102v1,
SHA4e6bd3d2…, and actually viewed/read complete printed pages1 and2.
The full Theorem1.1 is onp1. The public margin identifies v1 of
29October2026, while the manuscript date is28October2026; both are
preserved in the proposed bibliography entry. I also retrieved the
exact v1 source archive. Its member
Logarithmic_S6_October_28_2026_Final.tex is57,465 bytes and matches
the supplied source byte-for-byte, SHAde895f47… . The official arXiv
version page supplies DOI10.48550/arXiv.2610.39102. The entry keeps
the citation key, author, title and author-year label, adds the pinned
version and DOI, and removes the verification-status label. No universal
claim about absence of a journal publication is made.

The final combined guard contains two complete pairs and11 literal edits:
ten in the mathematical owner and one complete bibliography entry.
All four proof items, original mathematical conclusions, labels and
hypertargets are retained. The iteration-only inline marker is removed;
the exact root map, KS normalization and local-algebra formulas are
explicitly declared additions. The two public-theorem locators and three
new current-I input references are bound. Exact forward/inverse
reconstruction passes. Both full proof versions and both full entries
were actually read. All earlier draft guards remain preserved.

One targeted independent-check proposal and one actual full comparative
rereading owner are sent to root for separate admission. No canonical
source, defect log, ledger or Paper II page coverage was changed.
