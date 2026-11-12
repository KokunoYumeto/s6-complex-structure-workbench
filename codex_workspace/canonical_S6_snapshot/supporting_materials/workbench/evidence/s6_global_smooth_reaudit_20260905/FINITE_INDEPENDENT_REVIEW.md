# Independent review of finite fillings and global gluing audit

2026-09-05. Reviewed the complete staged `agent_work/s6_global_reaudit_20260905/FINITE_FILLINGS_AUDIT.md` and `check_finite_fillings.py` against `candidate_geometry.tex` lines 1036–1378, `exact_algebra.tex` lines 1–90, and the logarithmic real-coordinate formulas in `integral_leray.tex` around lines 806–859. No canonical or root-owned file was modified.

## Verdict

No substantive error found in the staged finite-filling or gluing proof. Its primitivity argument, freeness test for every power, negative-orientation logarithmic conjugacy, properness on compact base sets, and Hausdorff gluing argument are valid. The small exact checker was replayed successfully through all 25 assertions, stopping before its output/provenance-writing section. The replay returned `gamma(v1)=1`, `gamma(v2)=-1`, `psi1(v1)=psi2(v2)=0`. This verifies the certificate's literal matrices; it does not certify the separate existence of the period family or any sphere conclusion.

## Exact mathematical checks

1. **Matrices and primitive invariant lattices.** The four matrices T1,T2,A1,A2 in the script agree entry-for-entry with the source, and `Aj=(Tj^{-1})^t`. The marked translations are exactly `v1=(1,2,-4,0)^t` and `v2=(-1,-3,3,0)^t`. Each gamma/psi row pair is invariant under all its nonidentity powers; each `Aj^k-I` has rank two. For j=1, a rational invariant row `r gamma+s psi1` has entries `(r,2s,s,3s)`, so integrality forces `r,s∈Z`. For j=2 its entries are `(r,s,s,2s)`, with the same conclusion. This directly proves the claimed saturated integral lattices and agrees with the script's gcd-of-minors check. Also `gamma(vj)=±1` proves that each vj itself is primitive in Lambda.

2. **Affine freeness and exact order.** Since `Aj vj=vj`, the kth affine power is `x↦Aj^k x+k vj/mj`. Applying gamma to a fixed-point equation in the real torus gives `k/3∈Z` for j=1 and `-k/4∈Z` for j=2. None of the required nonidentity powers meets that condition. At k=mj the map is translation by the integral vector vj, hence is the identity on the torus, while its base action has order mj. Thus no hidden fixed points of proper powers remain. Completeness of the invariant lattice is stronger than needed for this particular obstruction, but the audit proves it correctly.

3. **General fixed-point criterion.** For the averaging projector p, the inclusions `pLambda⊂(1/m)Lambda` and `span_R(pLambda)=im p` show that pLambda is a full lattice in its real invariant subspace. Pullback through p identifies its dual with the invariant integral covectors. Integral evaluation of pb against that dual implies `pb∈pLambda`; choose lambda with `p lambda=pb` and solve `(A-I)x=lambda-b`. This gives the fixed point. The sign matches `Ax+b=x mod Lambda`. The proof does not require an integral splitting of Lambda.

4. **Holomorphic action and proper local family.** The source covariance is `R_g(z)Pi(z)=Pi(gz)A`. Therefore the holomorphic lift with translation `Pi(gz)v/m` is exactly the printed affine action in the real marking. The compact-set bound on the inverse of Pi gives proper discontinuity of the lattice action: for compact K1,K2 in the total covering, their fibre coordinates have finite norm bounds, their base projections lie in a compact set, and an intersecting lattice translate must obey `|lambda|≤sup||Pi^{-1}|| (sup|zeta_1|+sup|zeta_2|)`. Only finitely many integral lambda satisfy this. The continuous map `K×[0,1]^4→J'` has image the full inverse image of a compact K in the base, proving properness of the torus-family projection.

5. **Negative logarithmic orientation.** With `s(gz)=exp(-2 pi i/m)s(z)`, the compatible local logarithm is `ell'(gz)=ell(z)-2 pi i/m`. Put `alpha=ell/(2 pi i)`. Then

   \[
   G h^{-1}(z,\zeta)=
   (gz,R_g(z)\zeta-(\alpha(z)-1/m)\Pi(gz)v).
   \]

   Translation by h at gz adds exactly `(alpha(z)-1/m)Pi(gz)v`. Thus `hGh^{-1}=G^0`, with h (not its inverse) mapping the affine quotient to the linear quotient. Changing ell by `2 pi i n` changes its section by the lattice vector `nPi(z)v`; the descended map is branch independent. No orientation reversal or undeclared change of v2 occurs.

6. **Complex-to-real marking.** If `J_z=Pi(z)^{-1} i Pi(z)`, then the real representative of the complex translation `alpha Pi(z)v` is exactly `a(z)=Re(alpha)v+Im(alpha)J_zv`. The equality `J_gz A=A J_z` follows by the covariance and complex linearity of R_g. For the compatible local branches from item 5, `a(gz)=Aa(z)-v/m`. This is the correct real formula and agrees with the checked source. The globally defined object is `a mod Lambda`; a itself is a local representative, changing by nv under a logarithm branch change.

7. **Finite-quotient properness and multiplicity.** For compact K in Dj, the full preimage under `s↦s^m` is compact and contained in the chosen invariant linearizing domain. Its inverse image in the proper torus family is compact; the image under the quotient is precisely `fj^{-1}(K)`. The quotient has no branch points because the finite action is free. The holomorphic function `s^m` has divisor m times the central torus, so in these local covering charts `fj^*(pj)=mSj`. This proves the full scheme multiplicity, not only a set-theoretic fibre description.

8. **Retraction and stalk map.** Choosing a round disc in the s coordinate makes `(1-u)s` remain in the domain for all `0≤u≤1`. Keeping x fixed in Xi commutes with the constant affine map on x and the rotation on s, hence the radial homotopy descends. At a nonzero base value choose one root s; every finite orbit meets that root fibre once. The retraction is then exactly the quotient covering `x mod Lambda↦orbit of x` on the central torus. Its cohomological pullback is the claimed integral specialization map. No assertion that this real marking is holomorphic is used.

9. **Hausdorffness of global gluing.** The equivalence relation meets any single summand at most once, because special discs are pairwise disjoint and the whole punctured restriction is glued by a bijection. Saturations of open sets are open. Each summand therefore embeds openly and injectively. At a common special base value two points belong to the same open Hausdorff summand Nj; at a common nonspecial value they belong to J. Disjoint neighborhoods there have disjoint images because the summand map is injective, and those images are open. Different base values are separated by the base. This proves Hausdorffness; the usual doubled-origin counterexample cannot occur because the special fibre is present in only one summand above its value.

10. **Global compact-cover properness.** The proof explicitly establishes `f^{-1}(Dj)=Nj` and `f^{-1}(B°)=J`, so the relevant local maps are restrictions to whole inverse images. For compact K, choose finitely many Va with compact closures contained in members Ua of this cover and covering K. Each `K∩closure(Va)` is compact in Ua. Their inverse images are compact by local properness. Their union is exactly `f^{-1}(K)`: every point maps to K and some Va covers its image, while every member of the union maps to K. The finite union is compact. This justifies the step to compact X when K=B.

## Minor wording clarifications, not mathematical failures

- In §3 of the staged audit, write “for these compatible local branches” immediately before `a(gj z)=Aj a(z)-vj/mj`, and “the global class is a(z) mod Lambda.” The surrounding discussion already supplies this meaning, but the addition prevents the real local representative from being mistaken for a globally single-valued map.
- Before the radial-retraction paragraph, explicitly choose `Delta_j=s_j^{-1}({|s_j|<rho_j})`. An injective linearizing coordinate on an arbitrary invariant neighborhood need not have a star-shaped image. Taking a sufficiently small round coordinate disc is an available shrink already authorized by the local construction and preserves all translate-disjointness conditions. It introduces no new hypothesis and leaves the filling arguments unchanged. The source itself calls these linearizing discs, so this is an explicit choice, not a contradiction in the intended construction.
- The checker records the precise gamma/psi evaluations as detail fields but asserts only invariance at that step. Later assertions already test the required nonintegral obstructions, and the replay confirms the exact evaluations. Adding explicit equality assertions for those four displayed evaluation values would make the receipt match the prose more literally, but the existing certificate and mathematical proof are correct for the actual inputs.

## Source hashes at review

SHA256:

| File | Hash |
|---|---|
| `agent_work/s6_global_reaudit_20260905/FINITE_FILLINGS_AUDIT.md` | `B2A7E709C5A6105F6AD38F3A1A04EF1B65FCBC8FEFE8C596D02284C13BD328CE` |
| `agent_work/s6_global_reaudit_20260905/check_finite_fillings.py` | `0A3356EB273FB8009848189070E493285243864753FFD4FAB756CC20413FA653` |
| `candidate_geometry.tex` | `261350305E2A62116D491A0AA4F6470D636B18285786FE5A266AC48717323172` |
| `exact_algebra.tex` | `264D8D889F38818B2D33289D2C3E4DB50D3290ABE969B29BA3B9D7DF868ED018` |

The two TeX paths are under `output/s6_consolidated_canonical_2026-08-26/supporting_materials/workbench/research/`. Replay evaluated the existing checker AST only through the matrix-check loop, before the `records=[]` section and every output write; 25 assertions passed. No new external source claim or remote action was needed for this bounded review. The full first cusp audit remains in AUDIT.md beside this file.
