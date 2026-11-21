# Paper V final-reading rewrite comparisons

These are scoped proof rereads under the publication prompt sections4.2–4.3. The attached original proof had already been read before these final rewrites were formulated; none of the five rows claims an independent re-proof, targeted preread check, or new computation. Grammar-only changes are excluded.

## Evidence binding

- Attached original: `/workspace/scratch/653608133b22/source/S6_series_V_corrected_20261120.tex`.
- Attached-original SHA-256: `c6e366ad871ae320c50b0ddb0f947d422ec229e6c7e776b1a706d435039efcea`.
- Compared rendered candidate: `V_candidate_01`, PDF SHA-256 `8b2d18bb43fedda842510e01967074589e0439c491fa3bb53928ab1d7eeedc2d`.
- Guard source SHA-256: `ca6b2dd8860b1d31bf4b8f5cd5165dc48c8dd08ac22ba47ce9a98bed6f6d35bb`.
- Exact old/new text: `S6_SERIES_PUBLISH_V_final_reading_analytic_guards.json`.
- These records concern the reviewed guarded replacements. Their integration and subsequent layout will be checked on candidate02.

## Scope and outcomes

### night:P1.16 — Height at the marked basepoint

Candidate V_01 Theorem7.2, p.42; analytic_final_05.

**Reread outcome: PASS within this scope.** Reread the attached original height theorem and its exclusion proof, then compared the new reason sentence with the unchanged determinant calculation of night:P1A.2. The coefficient relation is z=(625pi i/128)xi. At xi=ic, 384z+3125=3125-1875pi c, whose unique zero is c=5/(3pi). The height bound, exceptional value, strict inequality and transversality proof remain unchanged. The edit names the existing reason at the value’s first occurrence; it proves no new parameter claim.

### night:P1A.2 — Hodge connecting-map proof and coordinate order

Candidate V_01 Theorem8.3, pp.45–46; analytic_final_06–08.

**Reread outcome: PASS within this scope.** Reread the original projected residue, connecting matrices and exceptional-zero paragraph against the proposed relocation. The exact relation z=(625pi i/128)xi is moved from Step5 to Step1, before the entries that use it; z=-(625pi/128)c on xi=ic is retained. Every residue coefficient, determinant, source/target basis, cohomology dimension and connecting rank is unchanged. The removed final citation sentence repeats the same bound and theorem already used immediately before it.

### night:P1A.4 — Canonical splitting in the isomorphism statement

Candidate V_01 Theorem8.5, pp.48 and50; analytic_final_09–10.

**Reread outcome: PASS within this scope.** Reread the attached original fixed-splitting statement and graph-comparison step against the canonical-family wording. Remark3.8 gives the exact relation sigma_alt=sigma_b-a alpha e and xi_b=xi_alt-a. Therefore xi_b=eta_b holds exactly when xi_alt=eta_alt, and the two period graphs are identical under the displayed conversion. The canonical statement and sigma_b graph retain the original isomorphism criterion; the any-fixed-splitting formulation follows by that exact common translation. The automorphism and translation calculations are unchanged.

### night:P1.17 — Consolidation of intrinsic algebraic reduction

Candidate V_01 Theorem8.6, p.50, proof Step1; analytic_final_11.

**Reread outcome: PASS within this scope.** Reread the full original Step1 and the first proof step of night:P1A.4. The latter already establishes that the meromorphic function field is C(lambda) and that its intrinsic algebraic reduction is the given base map, for every admissible member. The replacement invokes precisely that result and preserves the anti-Mobius conclusion and the argument fixing the three real marked values. The finite affine obstruction, exact anti-intertwiner, based cusp and fan computations are untouched. The complete original Step1 and exact replacement are copied below. This is proof consolidation, not an independent re-proof.

### night:P1A.5 — Scope of the boundary-extension contradiction

Candidate V_01 Theorem9.3, p.54, final proof paragraph; analytic_final_12.

**Reread outcome: PASS within this scope.** Reread the attached original closing paragraph and the new numbered analytic-extension definition. The replacement retains the noncentral compact smooth torus fibre on which the contradiction is obtained and the proper modifications preserving the prescribed open family. Reference to Definition9.1 retains every permitted central-space singularity, multiplicity and extra component. The finite-boundary, infinity and finite-ramified-change arguments are unchanged. No central-fibre hypothesis is added or removed.

## Preserved original algebraic-reduction proof

Original locator: `/workspace/scratch/653608133b22/source/S6_series_V_corrected_20261120.tex`, label `night:P1.17`, tag `02QQ`, first proof item, source lines10867–10880. The source content below is copied exactly; no original PDF page number is inferred.

Candidate locator before consolidation: Theorem8.6, proof Step1, page50 of V_candidate_01. Replacement locator: the same label/tag and first proof item, guarded by `analytic_final_11`; the replacement cites `night:P1A.4` (candidate Theorem8.5, first proof item, pp.48–49).

Original Step1 SHA-256: `f341c1b92d3b6847551cfcf7f9ba864c9ad344e9a5d43ac4182e64a596bb1b11`.

### Full original first proof item

```tex
\item We first recover the base intrinsically.  An effective divisor on
$M_c$ cannot be horizontal: its first Chern class vanishes by
$H^2(M_c;\mathbb Z)=0$, whereas its nonzero effective restriction to a
general torus fibre would have positive pairing with the square of a
flat K\"ahler class.  The pole divisor of any meromorphic function is
therefore vertical.  On every regular fibre outside that divisor the
function is holomorphic and hence constant.  It factors through a
meromorphic function on the base, which is rational on
$\mathbb P^1$.  Thus the function field is exactly $\mathbb C(\lambda)$.
An anti-biholomorphism consequently induces an anti-M\"obius map of
the base.  The two distinct multiplicities $5,4$ and the singular cusp
support distinguish the three special values, so this base map fixes
$\infty,0,\lambda_*$.  As those points are real, the map is precisely
$\lambda\mapsto\bar\lambda$.
```

### Exact consolidated first proof item

```tex
\item By \cref{night:P1A.4}, the meromorphic function field of each
member is $\mathbb C(\lambda)$, with the given base map as its
algebraic reduction.  An anti-biholomorphism therefore induces an
anti-M\"obius map of the base.  The two distinct multiplicities $5,4$
and the singular cusp
support distinguish the three special values, so this base map fixes
$\infty,0,\lambda_*$.  As those points are real, the map is precisely
$\lambda\mapsto\bar\lambda$.
```

The first item after the consolidated paragraph and all later proof items are unchanged. The original independent divisor/H2 argument is preserved here as a check record rather than repeated in the paper.

