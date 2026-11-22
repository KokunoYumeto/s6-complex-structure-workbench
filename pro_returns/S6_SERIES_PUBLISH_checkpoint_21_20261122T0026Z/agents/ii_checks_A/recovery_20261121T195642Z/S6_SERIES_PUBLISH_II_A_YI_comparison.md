# 02YI / night:P4R.6 — complete postrelease comparison

Checker: ii_check_a. This record is written after the independent derivation was frozen and the complete target proof was released. It supplies comparison, source transport, computational method comparison and record precisions. It creates no additional independent derivation.

## 1. Order of work and immutable evidence

The independent derivation is `S6_SERIES_PUBLISH_II_A_02YI_derivation.md`, SHA256 `54b6004e38920e7b31087fae4fe08988a24c660f6b6279a170b6e197ca76cd0c`. Its input binding is SHA256 `3f955d06dbf1209c997c29c1d5e70b0eda4b27af714d39a9e5620a3f5dcc55a0`. The first input-binding attempt encountered the absent pre-reset WJ standing-hypotheses file; the failure record preserves that fact. The exact common standing paragraph was then read from the safe WW/WX named-input packet, paragraph SHA256 `e0c83437d70bfb93061f7a12854252269d7219914c152d17a269cbfc08871dab`. No target proof was opened to fill that input gap.

The fresh mathematical program ran successfully at 23:47:14.237053–23:47:14.262731 UTC on 21 November 2026. Its complete source and every output field were read before the derivation freeze. The freeze receipt at 23:50:34.339146 UTC is SHA256 `97a5d63e002e0753b161607f9ff617d467004029a6916ea82b472215ffe096e3`; the subsequent release receipt is SHA256 `2a57e58b7ea8676986d51fe837204bb104e75710f8e57600313766584cacf57e`. The entire released statement and all four proof items have been read. The frozen derivation remains byte-identical.

The exact statement A.5.3 was an input, with η=ν, Z=T and h=ρ, and already states the canonical integral divisor and strict conductor multiplicities for this minimal resolution. Its proof was not opened. The present derivation proves the duality identity directly and, in addition, the incidence, exceptional positivity and full support assertions of YI. No independent review of A.5.3 is claimed here.

## 2. Statement and first proof item: canonical divisor and conductor

The original statement uses the common torus-fibration setting and the minimal resolution of the normalization. The proposed statement spells out that same setting, names π:T→N, and defines ρ=ν∘π. The hypotheses b1(Y)=b2(Y)=0, proper surjectivity, connected fibres, smooth compact ambient threefold, smooth compact base curve and general complex two-torus are retained. The central full scheme fibre is still mS, with S reduced, irreducible and singular. The conclusion is the same integral effective divisor identity, exact support, torsion, conductor coefficients and exceptional incidence.

Printed item 1 constructs the divisor by pulling local meromorphic canonical forms to T. This is exactly frozen §2: if η is a generator of ω_S, the coefficient of a prime divisor is minus its order in ρ*η. Replacing η by a unit multiple preserves every order, so the local definitions patch. The resulting line-bundle isomorphism is ω_T(D)≅ρ*ω_S, not a numerical equivalence.

The printed finite-duality formula agrees with the local evaluation map Hom_A(B,A)→A, φ↦φ(1), whose image is {a:aB⊂A}. At a generic regular point of a conductor branch, the ideal is (z^c), and ω_N=𝔠⊗ν*ω_S identifies ρ*η with z^−c times a regular canonical generator. Thus the coefficient is the positive integer c. The proposed proof writes this local map explicitly. The original defensive sentence about a Q-Cartier assumption is replaced by this positive description of the exact reflexive canonical module; every divisor and intersection computation still takes place on T or uses the invertible ω_S. No mathematical conclusion is deleted.

## 3. Second proof item: intersection form and inverse signs

The printed principal-divisor construction is the same as frozen §4, with the following exact dictionary:

| Frozen notation | Printed/proposed notation | Meaning |
| --- | --- | --- |
| w_i | n_i | positive valuation of a local function along E_i |
| a_i | h_i | H·E_i |
| x_i | v_i | arbitrary real vector |
| u_i | w_i in the quadratic display | diagonal rescaling x_i=w_i u_i in the frozen notation |
| L | −M | positive intersection form |

This is the invertible linear map v=diag(n_i)w with all n_i>0. The principal divisor gives Mn=−h and h_i≥0 with h≠0. Its strict transform meets the fibre by properness. The original quadratic identity is precisely the negative of the frozen identity for L. Therefore the two expressions have identical signs and equality conditions.

The proposed proof also supplies the connectedness argument used by both versions: properness reduces a hypothetical separation of the exceptional fibre to disjoint neighborhoods over a small normal neighborhood; the locally constant 0/1 function descends off the exceptional point and normality extends it, contradicting the two limiting values. This proves the required graph connectivity at the analytic local scope.

The original assertion about −M^−1 follows from the row equation b_i=h_i u_i+Σ_{j≠i}M_ij n_j(u_i−u_j), with d_i=n_i u_i. At a negative minimum every summand is nonpositive, so b_i≥0 forces all neighbors to have the same value and h_i=0. Propagation reaches a positive h_i and contradicts the minimum. This proves d≥0 for every b≥0. If b≠0 and d_i=0, the same equation forces every adjacent d_j=0, then all d=0, contradicting Md=−b. In particular each column of −M^−1 is strictly positive. This settles the printed matrix claim for arbitrary connected exceptional graphs, not only tested configurations.

Mumford's original printed p.6 was opened and read before freeze, including its full-page image. His hyperplane difference is replaced here by the local function on N; its pullback is H+Σn_iE_i. The same diagonal matrix gives the same weighted quadratic identity. This explicit local construction proves the analytic form used in YI. The source's projective hyperplane construction and later plumbing blowups are not imported as hypotheses on T. The proposed citation is to that exact printed page.

## 4. Third proof item: adjunction and the zero block

The printed D_h is the frozen D_str, the strict-transform conductor. The proposed notation D_str is the identity element of Div(T) represented by the same sum of strict conductor components with the same coefficients; the change has no geometric effect.

Both proofs intersect ω_T(D)≅ρ*ω_S with E_i. The right side has degree zero because ρ(E_i) is a point. This gives Md=−b, b_i=K_T·E_i+D_str·E_i. The strict part is effective and shares no exceptional component, so its intersections are nonnegative. Adjunction gives K_T·E_i=2p_a(E_i)−2−E_i². Negative definiteness gives E_i²<0; arithmetic genus zero makes an integral curve smooth rational, and the minimal resolution excludes an exceptional (−1)-curve. Therefore every b_i≥0.

The printed zero-coefficient conclusion follows exactly from the second item's propagation: one zero coefficient implies d=0 and hence b=0 throughout that connected fibre. Each nonnegative summand K_T·E_i and D_str·E_i must then vanish. Adjunction forces p_a(E_i)=0 and E_i²=−2; the block is disjoint from the strict conductor. The proposed proof retains this conclusion even though the final item proves the stronger incidence statement directly.

## 5. Fourth proof item: incidence, the analytic Morse sphere and support

Finite duality makes the conductor ideal on N equal to ω_N⊗ν*ω_S^−1, a rank-one reflexive ideal. The closed conductor locus is Supp(O_N/𝔠). A rank-one reflexive ideal is the intersection of its codimension-one localizations in the fraction field, so this locus has no isolated point. Any conductor curve through the image of an exceptional fibre has strict transform meeting that fibre by properness. A block disjoint from the strict conductor therefore maps to a point outside the conductor; there ν is an isomorphism. Its image in S would be a normal isolated hypersurface singularity.

The printed local Milnor argument agrees with frozen §1. The proposed proof makes its unit map explicit: f=u g^m, choose log u, set h=exp((log u)/m)g, so f=h^m exactly. The local level h=δ is included by the identity coordinate map in the global fibre f=δ^m. This avoids leaving the relation between the reduced equation and the unit-multiplied equation implicit. It preserves the printed local-fibre inclusion and contradiction. The original phrase about copies of a Milnor fibre is implemented by the level equations h=ζ·t^(1/m), for the m roots ζ, on the chosen coordinate ball; the particular copy used in the proof is h=δ.

The isolated critical point of h follows from the isolated singular locus of its zero surface. Its analytic gradient is finite over a small target neighborhood, and every regular local preimage has positive real Jacobian |det_C d(∇h)|². Hence a small regular target value a supplies finitely many, and at least one, nondegenerate critical points of h_a=h−a·z. Milnor Appendix B, pp.111–114, supplies the opened degree/positivity locus. The analytic boundary argument is provided explicitly in the frozen derivation and proposed proof using the actually opened Łojasiewicz Theorem 2, p.464: a critical-radius locus accumulating at the origin would contain an analytic simplex with the origin in its closure, on which squared radius is constant, hence zero, a contradiction. Compactness gives the transverse boundary for small values and perturbations.

Choose δ and then a small enough that every critical value of h−s a·z has modulus below |δ|/2 for 0≤s≤1. Boundary-tangent horizontal fields give diffeomorphisms over δ throughout this proper family. At a nondegenerate critical point, the real sphere in z1²+z2²+z3²=ε has normal bundle JTS². The tangent-then-normal permutation (e1,e2,Je1,Je2), relative to complex orientation (e1,Je1,e2,Je2), has one inversion. The oriented normal bundle has Euler number −χ(S²)=−2. Regular-value transport in h_a and then the parameter-family transport embed it into h=δ and hence f=δ^m. Its lift to the torus universal cover C² makes its homology class zero. Inclusion preserves the local normal bundle, so self-intersection would be both −2 and zero. This proves that every normal point of S is smooth and excludes the disjoint block.

Every exceptional block consequently meets the strict conductor; some b_i is positive there, and item 2 makes all d_i positive. The singular locus of S is its nonnormal conductor locus, whose inverse image under ρ is the strict conductor together with these exceptional fibres. This proves the asserted support equality. Finally, WJ gives ω_S^⊗m≅O_S for this same fibre mS, and pullback yields (ω_T(D))^⊗m≅O_T. Every original conclusion has now been compared and proved.

## 6. Fresh prerelease computation and its mathematical scope

The fresh file `code/S6_SERIES_PUBLISH_II_A_02YI_interpolation_certificate.py` is SHA256 `6f7be3d806ce94409858dab8db60f7ab272853fbf9dd716d7866e351ec15cb80`; its output is SHA256 `ca3c6a6ddba79fbc966dd3f3ba2857726723cb3317aea283be2d5121898f739f`. It uses exact rational evaluation on full tensor grids, with separate-degree bounds and explicit denominator cancellation. This proves the universal edge identity on 72 grid points, the anchor identity on 12 points and the row identity on 32 points. Successive one-variable interpolation promotes each full grid to a polynomial identity. Summation over the actual finite graph gives the arbitrary-size quadratic and row formulas. Positivity, integrality, connectivity and the maximum principle are mathematical arguments in the derivation; they are not inferred from a finite list of graphs.

The same program computes the explicit orientation permutation, χ(S²)=2 from cells in degrees 0 and 2, and self-intersection −2. It computes the determinant of the displayed Hessian 2I by its complete six-term Leibniz expansion, obtaining 8. The Hessian entries are supplied by differentiating q=Σz_j² in the derivation; the program verifies the matrix determinant and does not independently implement symbolic differentiation. The source and all output fields were reread after release as well.

## 7. Bounded historical association and the related older A1 calculation

The bounded scope JSON contains the entire released owner, the heading/whitespace gap before it, the whitespace gap after it, all four exact night:P4R.6 historical ledger rows and the then-current 21-row Programs table. All these contents were actually read. They name no direct YI routine. One historical row records an opening of Mumford p.6 with the same PDF hash; it was read only after the present freeze and gives no reading credit to this check. The bounded finding makes no claim about programs outside the inspected scope.

There is a positive related computation: `milnor_intersection.py`, previously read in the completed WN/WO check, treats x²−z y^n=1. Its pinned source is SHA256 `85f4d954285277ad3a51ee75ba7e91fb99013ba73609fb3529c5935adce99127`, Git blob `177932d388443f5dc6cd33252e919b8f184c5e58`, commit `83d76022bcd442278b760db9ff438afceed6c6ea`. Its complete source had been exposed before YI through that earlier owner, and was read again after YI release. The frozen statement that old target programs were closed means no historical YI routine had been opened or used to design the new program; it does not erase this earlier related-owner exposure. The fresh YI computation uses a different method for the shared sphere square: normal-bundle orientation and sphere cells, whereas the older program uses a compactification intersection lattice, boundary restriction matrix, rank and nullspace, followed by vᵀQv.

An initial postrelease message incorrectly associated the quadratic A1 surface with n=2. Reading the exact old source corrected this to n=1. For n=1 the old surface is x²−zy=1 and its primitive kernel vector is (0,0,1,−1), square −2. The n=2 input is x²−zy²=1 and the program's square is −4. This correction is preserved here and in the related-run receipt. Neither the frozen derivation nor the prerelease program contains the incorrect association; their bytes and evidence count remain unchanged.

Choose s=√ε. The exact complex-linear map from q(z1,z2,z3)=ε to the n=1 affine surface is

    x=z1/s,    y=(z2+i z3)/s,    z=−(z2−i z3)/s.

It satisfies x²−zy=q/ε=1. The inverse is

    z1=s x,    z2=s(y−z)/2,    z3=s(y+z)/(2i).

In normalized coordinates its determinant is 2i, so its real determinant is positive. The compactification's last exceptional affine curves are E_+={x=1,y=0} and E_-={x=−1,y=0}; in the blowup chart a=x²−1, b=y, the equation a=bz gives these same curves. In the local complex coordinates (y,z), the real sphere has graph z=−conjugate(y). Its outward orientation at the north pole gives intersection +1 with E_+; at the south pole it gives intersection −1 with E_-. The old primitive class v=E_+−E_- has pairings −1 and +1 with these curves. The completed WN compactification identifies the compact H2 image with Z·v, so the outward real sphere maps to −v=E_-−E_+. This proves the cycle map, not merely agreement of the numerical squares.

The exact old prefix was rerun after release with its loop restricted from n=1,…,12 to n=1. All arithmetic is otherwise unchanged; the extraction ends before its file-writing routines. The run at 23:53:46.790800–23:53:47.109539 UTC exited 0. The excerpt SHA256 is `1eac2351e3a285ee7828b42ad1895712d473ca750366833826a957fd00a2699d`, and output SHA256 is `19cc038bef28297a235318cedba5ef9814cfc2f4f7aefb1d4a7d596f544a5d66`. Its complete output gives compactification rank 4, boundary rank 3, the primitive vector (0,0,1,−1), square −2, a tree boundary and weights (3,2,4), degree 6. The extraction/source-span receipt binds the exact pinned source.

The postrelease coordinate program is `code/S6_SERIES_PUBLISH_II_A_02YI_A1_transport_postrelease.py`, SHA256 `5eec0ea52b8fe255a63f7b5572c7b403daa84a505574bea7d03f99e22061f3e0`. Its output is SHA256 `b6231f11da1bd8a4753db025c3744895cc496c805c426c2ef70cd0669d662b54`; it ran at 23:54:10.469763–23:54:10.494734 UTC, exit 0. Gaussian rationals are represented as rational pairs. The full 3³ grid and separate degree bounds (2,2,2) prove the quadratic identity and both inverse identities; the program also computes determinant 2i and the real north/south intersection determinants +1 and −1. The complete source and every output field have been read. The first tool response containing these results was truncated; the receipt and complete output were subsequently reopened at 23:57 UTC before any result was credited. This supplement receives no new independent-check event.

## 8. Record precisions, editorial scope and bibliography

The frozen prose uses “support of the conductor ideal” in the usual locus sense. Its precise set here is Supp(O_N/𝔠), not the module-theoretic support of the nonzero rank-one ideal 𝔠. The actual argument already uses properness of the ideal and its codimension-one localizations. The proposed proof states the quotient support explicitly. Frozen bytes are preserved; this is a wording precision in the check record, with no change to its argument or conclusion.

All four proof items remain. The proposed source replaces the run title and prompt reference by a mathematical title and the exact standing hypotheses, uses ordinary item numbering, names the morphisms and local conductor ideal, supplies the row and analytic fibre maps, replaces bare WJ numbers by stable cross-references, and cites the opened primary loci. No false target assertion or changed statement scope has been found. The source changes carry explicit maps in the guard record; no D25 mathematical correction is proposed.

The bibliography proposal removes the third-party Milnor viewer URL from the manuscript and gives both publishers printed on the actually read 1968 title page. The public viewer remains fully identified in the primary-access evidence. No unverified DOI is inserted. The Mumford entry's trailing “Verified” process marker is removed while author, title, journal, year, pages, DOI and Numdam URL retain their bytes. The source Programs table receives the fresh interpolation/orientation program and the postrelease exact coordinate-transport program, with their actual scopes. The old n=1 excerpt is provenance evidence of the already cited WN program, not a new direct YI historical routine.

The exact full-pair rereading, final hashes, sequential literal guards, forward/inverse validation and three proposed event outcomes are recorded separately. The proposed targeted event is one complete independent check; the actual editorial rereading and computation are separately typed evidence within the same group.
