# 02YI / night:P4R.6 — independent derivation before target release

Checker: ii_check_a, GPT-6 Astra, ChatGPT Pro mode, effort Pro. The complete target statement and its WJ statement supplement have been read. The target proof, printed outline, historical derivations and old target programs remain closed. Root supplied citation metadata only: the printed proof has no formal citation command; its named notions include Milnor, Morse and Laplacian. No target argument was transmitted.

## 0. Exact standing morphisms and conclusion

Let f:Y→B be the standing proper holomorphic torus fibration, with Y a smooth compact complex threefold, b1(Y)=b2(Y)=0, connected fibres and smooth general fibre a complex two-torus. Choose a disk about the specified value and write its central scheme fibre mS, with S irreducible, reduced and singular. Let ν:N→S be the finite normalization and π:T→N its minimal resolution. Set ρ=ν∘π. These are the target's maps; T is the minimal resolution of N, and need not be its minimal model as a compact surface.

The target claims an effective integral divisor D on T, ω_T(D)≅ρ*ω_S, support D equal to ρ^−1(Sing S)_red, strictly positive usual conductor coefficients on the nonexceptional part and strictly positive coefficients on every exceptional configuration. Every such configuration must meet the strict conductor. WJ then gives (K_T+D)^⊗m trivial.

The exact safe A.5.3 statement was already supplied for the independently checked BB target. For this hypersurface S and this minimal resolution it supplies the same canonical integral effective divisor identity and identifies its nonexceptional part with the divisorial conductor. I bind that statement as an additional input, with the exact substitution η=ν, Z=T, h=ρ. The local duality and intersection arguments below independently establish the identity and coefficient signs needed here; they also prove the stronger asserted support and incidence conclusion.

## 1. Normal points of the reduced support are smooth

Take a point p at which S is normal. A normal surface germ is regular outside an isolated subset. Thus a singular p of this kind is an isolated hypersurface singularity in the smooth threefold Y. In a coordinate ball write the reduced equation as g=0 and f=u g^m, where u is a holomorphic unit. A logarithm of u exists on a sufficiently small ball. The holomorphic function h=u^(1/m)g has the same reduced zero germ and satisfies f=h^m exactly.

The critical point of h at p is isolated. Indeed a positive-dimensional component of Crit(h) through p has h constant along its smooth curve arcs, hence h=0 there, which would give a positive-dimensional singular locus of {h=0}. This contradicts normality of the surface germ. Shrink the ball so p is its only critical point.

Here is the precise local Morse-sphere construction, including the analytic and boundary scope. The holomorphic gradient G=(∂h/∂z1,∂h/∂z2,∂h/∂z3) has an isolated zero. Its local degree is a positive integer. The opened Milnor Appendix B, pp.111–114, proves the degree, perturbation and positivity assertions; the analytic form also follows directly as follows. On a small source neighborhood G is proper over a sufficiently small target neighborhood, since the norm of G has a positive minimum on the chosen source boundary. The fibre over zero is finite, and after shrinking every nearby fibre is finite. The image is an analytic subset of full dimension, hence the whole target neighborhood. A regular target value has at least one preimage and the real Jacobian at each preimage is |det_C dG|^2>0. Thus the degree is positive. A sufficiently small regular value a gives a perturbation h_a=h−Σ a_j z_j whose critical points in the ball are finite, nonempty and nondegenerate.

A suitable ball boundary meets {h=0} transversely. To justify this for an analytic h, use the already opened real-analytic triangulation theorem of Łojasiewicz, Theorem 2, p.464, rather than extending a polynomial statement by notation. The locus in {h=0}\{p} where the derivative of squared radius vanishes on its tangent space is semianalytic. In a compatible locally finite analytic triangulation, accumulation at p would give a positive-dimensional connected simplex whose closure contains p. Squared radius has zero derivative along that simplex, so is constant there, and continuity at p would make the constant zero. This contradicts the simplex lying outside p. Hence small spheres are transverse to the smooth zero set.

On the compact sphere, transversality persists for all sufficiently small values of h. It also persists under the small C1 perturbations h_s=h−sΣa_jz_j, 0≤s≤1. Choose a small nonzero value δ and then choose a small enough that every critical value of every h_s in the ball has absolute value less than |δ|/2. This is possible because any sequence of critical points for a→0 accumulates at p, and their h_s values therefore tend to zero. The manifolds with boundary h_s^−1(δ)∩closed-ball then form a proper smooth family over [0,1], including their boundaries. A horizontal vector field tangent to the boundary integrates for the entire compact parameter interval and gives an orientation-preserving diffeomorphism of h_a^−1(δ)∩ball with h^−1(δ)∩ball.

Choose one nondegenerate critical point of h_a, with value c. In its holomorphic Morse coordinates, h_a=c+z1^2+z2^2+z3^2. For a small positive real ε the locus

    z_j=x_j real,    x1^2+x2^2+x3^2=ε

is an embedded two-sphere in the regular local fibre h_a=c+ε. A path from c+ε to δ in the small value disk avoids the finite critical values. Horizontal transport in the large ball, tangent to its boundary, carries this sphere to h_a^−1(δ), and the preceding parameter-family diffeomorphism carries it to h^−1(δ). These are explicit fibre identifications through proper submersions; the orientation is the one induced by the complex surface fibres.

The sphere has self-intersection −2. At its real points the normal bundle in the complex quadratic surface is J(TS2). With complex orientation ordered (e1,Je1,e2,Je2), tangent-then-J-normal order is (e1,e2,Je1,Je2), an odd permutation. The oriented normal bundle is therefore the tangent bundle with opposite orientation, so its Euler number is −χ(S2)=−2. The fresh program independently computes the permutation sign, sphere cell Euler number and the quadratic Hessian determinant.

Because f=h^m on the ball, the final local fibre embeds in the smooth global fibre f^−1(δ^m), a complex two-torus. The embedded sphere lifts through its universal cover C2→f^−1(δ^m), since S2 is simply connected. C2 is contractible, so the sphere is null-homotopic and its integral H2 class in the torus is zero. Its self-intersection in the torus is consequently zero. The normal bundle of the local embedding equals the restriction of the torus normal bundle, whereas the constructed sphere has self-intersection −2. This contradiction excludes p. Thus every point where the reduced support is normal is smooth.

This uses neither a global normality assumption on S nor the n=2-excluding assertion in Milnor Theorem 6.6. It proves the local assertion needed for the normalization map.

## 2. Conductor duality and the canonical integral pole divisor

Write I for the conductor of O_S⊂ν_*O_N. Locally, for the finite birational extension A⊂B in their common total fraction field, every A-linear homomorphism B→A is multiplication by an element x with xB⊂A. Evaluating at1 identifies Hom_A(B,A) with this conductor ideal. Because A is a hypersurface Gorenstein ring, finite duality gives

    ω_N ≅ Hom_{O_S}(ν_*O_N,ω_S)
        ≅ I·ν*ω_S.

One can obtain this identity by dualizing the one-step ambient hypersurface resolution: its Ext^1 is ω_S, and the finite algebra B then gives Hom_A(B,ω_S) as its canonical module. On the regular locus of N this is the residue-form identity; its extension across the isolated normal singularities is the reflexive canonical module. This identifies exactly the usual scheme-theoretic conductor orders at every codimension-one point.

At a regular generic point of a conductor curve with parameter z, write I=(z^c), c a positive integer. A generator σ of ω_S pulls back as z^−c times a regular generator of ω_N. Pull these meromorphic two-forms to T. Their orders along every prime divisor are integers. Changing σ by a holomorphic unit changes its pullback by a unit, so the negatives of these orders define a global integral divisor D and a canonical isomorphism

    ω_T(D) ≅ ρ*ω_S.

On the strict transforms of conductor curves the coefficients are the positive integers c just described. Elsewhere outside the exceptional locus and this strict conductor, ρ is an isomorphism onto the smooth locus of S, so D has coefficient zero. This is the same divisor and the same isomorphism as the exact A.5.3 input under the substitution in §0. The remaining task is to prove every exceptional coefficient is strictly positive and that no exceptional configuration is separated from the strict conductor.

The conductor ideal on N is a rank-one reflexive ideal, since it is ω_N⊗ν*ω_S^−1. In a normal local ring a reflexive rank-one module is the intersection of its codimension-one localizations inside its fraction field. Thus a point of its support lies on a conductor curve: a proper conductor ideal supported only at an isolated point would have every codimension-one localization equal to O_N, and reflexivity would make the ideal O_N itself.

## 3. Every exceptional configuration meets the strict conductor

Let p∈N be a singular point, and put q=ν(p). Outside the support of the conductor, ν is a local isomorphism. If q lay outside that support, p would correspond to a normal singular point of S, contradicting §1. Consequently p belongs to the conductor support on N. By the reflexive-ideal argument in §2 a conductor curve passes through p.

Its strict transform meets π^−1(p). For example, take smooth points of that curve tending to p; their inverse images under the isomorphism off the exceptional fibre have a convergent subsequence by properness, and the limit belongs to both the strict transform and π^−1(p). The exceptional fibre is connected. Here is the local normality argument for that familiar fact: if it split into two disjoint nonempty compact pieces, disjoint neighborhoods of them would, by properness, contain π^−1(U) for a small neighborhood U of p. The function taking the values0 and1 on those two neighborhoods descends on U\{p}, because π is an isomorphism there. It is bounded and holomorphic, so normality extends it across p. Each exceptional piece is approached by points outside the exceptional set, giving two different limiting values at p, a contradiction. Thus the exceptional intersection graph over p is connected, and its unique configuration meets the strict conductor.

## 4. Weighted exceptional intersection form

Let E1,…,Er be the irreducible exceptional curves over p. Set M_ij=E_i·E_j. Off-diagonal entries are nonnegative intersection multiplicities. Choose a nonzero local holomorphic function z on N vanishing at p. On a neighborhood of the exceptional fibre,

    div(z∘π)=H+Σ_i w_i E_i,

where H is the effective strict transform and every integer w_i is positive: the valuation defined by E_i has centre p and z belongs to its maximal ideal. The curve {z=0} has a nonexceptional part through p, so H meets the exceptional fibre. Intersecting the principal divisor with E_i gives

    Σ_j M_ij w_j = −a_i,    a_i=H·E_i≥0,

with at least one a_i>0. Put L=−M. For x_i=w_i u_i one obtains the exact identity

    x^t L x
      = Σ_{i<j} M_ij w_i w_j (u_i−u_j)^2
        + Σ_i a_i w_i u_i^2.

The graph is connected and at least one anchor a_i is positive. Hence zero on the right first forces all u_i equal, and then forces that common value to vanish. Therefore L is positive definite and M negative definite.

I opened Mumford's original 1961 article at its exact printed p.6, reading the entire negative-definiteness argument in both text and full-page image. His global hyperplane difference becomes the local function z above; the intersection identity and diagonal weight map x_i=w_i u_i are the precise transport to the present analytic germ. This gives the local proof with no projectivity assumption on T or N. Mumford first makes extra blowups for his later plumbing discussion; the identity here applies directly to the minimal exceptional curves, since it uses their intersection multiplicities and the principal divisor only.

## 5. Exceptional pole coefficients and strict positivity

Write D=D_str+Σ_j d_j E_j near this configuration. Restriction of ρ*ω_S to E_i has degree zero, because E_i maps to one point. The divisor identity therefore gives

    Σ_j M_ij d_j = −b_i,
    b_i=K_T·E_i + D_str·E_i.

Adjunction gives K_T·E_i=2p_a(E_i)−2−E_i^2. Negative definiteness makes E_i^2<0. Minimality of π excludes a smooth rational exceptional curve of self-intersection −1; hence a rational component with p_a=0 has E_i^2≤−2, giving K_T·E_i≥0. A component with p_a≥1 also gives K_T·E_i≥0. The strict conductor is effective and shares no component with E_i, so D_str·E_i≥0. Thus b_i≥0 for every i, and at least one b_i>0 because the strict conductor meets this configuration.

The equation is Ld=b. To prove d≥0, use the positive weights w from §4 and put u_i=d_i/w_i. The row identity is

    b_i = a_i u_i + Σ_{j≠i} M_ij w_j(u_i−u_j).

If a negative minimum u_i existed, every term on the right at a minimum would be nonpositive. Nonnegativity of b_i would force all neighboring u_j to equal that minimum and would force a_i=0. Propagating along the connected graph reaches an index with a_i>0, where the right side is strictly negative. This is a contradiction. Therefore every d_i≥0.

For strict positivity, suppose d_i=0. Then the equation (Ld)_i=b_i reduces to b_i=−Σ_{j≠i}M_ij d_j≤0. Because b_i≥0, every neighboring d_j is zero. Connectedness propagates zero to all d_j, contradicting the existence of a positive b_i. Thus every exceptional coefficient d_i is strictly positive. They were already integers by their meromorphic-form definition in §2; solving the real linear system proves their signs without changing that integrality.

## 6. Full support and torsion

We have proved that the strict conductor has its usual positive integral multiplicities, that every exceptional curve lies over a point on that conductor, and that every exceptional coefficient is strictly positive. Outside their union, ν and π identify T with the smooth locus of S, so D has no further support. Conversely §1 shows that all singular points of S belong to its nonnormal locus. The conductor ideal defines that locus, and its inverse image in N is the divisorial support described in §2. Pullback to the resolution adds exactly the exceptional fibres just treated. Consequently

    Supp D = ρ^−1(Sing S)_red.

The target's incidence and positivity assertions all follow. Finally WJ states ω_S^⊗m≅O_S for this same mS. Pullback along the exact map ρ and the canonical divisor isomorphism give

    (ω_T(D))^⊗m ≅ ρ*(ω_S^⊗m) ≅ O_T.

Thus K_T+D is torsion exactly as claimed.

## 7. Independent computation and source scopes

The fresh program `code/S6_SERIES_PUBLISH_II_A_02YI_interpolation_certificate.py` was written with the target proof and old target programs closed. It ran successfully at 23:47:14.237053–23:47:14.262731 UTC. Code SHA256 is `6f7be3d806ce94409858dab8db60f7ab272853fbf9dd716d7866e351ec15cb80`; output SHA256 is `ca3c6a6ddba79fbc966dd3f3ba2857726723cb3317aea283be2d5121898f739f`. The complete code and every output field have been read before this freeze.

For one arbitrary weighted edge the substituted 2×2 quadratic form has separate polynomial degree at most (1,1,1,2,2) in (c,w_i,w_j,u_i,u_j); the denominator cancellation is recorded as explicit monomial exponents. Evaluation at the complete product grid of sizes (2,2,2,3,3), with exact rational arithmetic, proves its identity at72 points. Successive one-variable interpolation proves the universal identity from those degree bounds. The same method checks the anchor term on12 points and the weighted-row identity on32 points with bounds (1,0,1,1,1,1). Summing these universal local blocks gives the displayed arbitrary-size graph identities; positivity and the minimum principle are proved in §§4–5. The program also computes the normal orientation sign −1 from its explicit permutation, χ(S2)=2 from cells in dimensions0 and2, self-intersection −2, and determinant8 for the quadratic complex Hessian.

The new Mumford primary PDF, publisher archive URL `https://www.numdam.org/item/PMIHES_1961__9__5_0.pdf`, is SHA256 `10bed3a0c3fba035f0e1e29103c3d4810abf283f85f4b03c2c06c98d98477343`. The complete printed p.6 was actually viewed and read, as was the surrounding opening text online. No whole-article reading is claimed. The opened Milnor scope is the already preserved exact page-image receipt for WX; the relevant Appendix B pages111–114 and the fibre identification on pp.51–54 were read in full before this target was considered. The analytic boundary argument in §1 explicitly uses the previously opened Łojasiewicz real-analytic triangulation theorem. The public viewer's polynomial curve-selection OCR was consulted during this derivation, but its polynomial statement is not used as an analytic theorem. The primary/source binding file records these distinctions and their hashes.

All target conclusions have now been derived before target-proof exposure. The argument is ready to freeze; comparison with the complete printed proof will begin only after the freeze receipt is obtained.
