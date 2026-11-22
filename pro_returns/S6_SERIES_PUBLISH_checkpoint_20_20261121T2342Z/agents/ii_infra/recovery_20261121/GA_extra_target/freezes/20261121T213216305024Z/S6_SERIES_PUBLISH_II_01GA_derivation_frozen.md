# Fresh derivation of 01GA / cdp:st:D.2.3

Checker: restore_build, GPT-6 Astra (OpenAI), ChatGPT Pro mode.

This is the separately authorized additional dependency check for GD. It does not alter or complete a row of the immutable 197-candidate index. I have read the statement and the primary analytic inputs listed in the adjacent packet receipt. I have not opened the target proof, its internal displays D.18/D.19, or any old target check. The six actually viewed primary scan pages are bound in the primary-reading receipt. All arguments below were developed before target release.

## 1. Exact claim and analytic setup

The given map is a proper holomorphic map h:U→Δ from a smooth complex threefold, with connected fibres and smooth two-dimensional complex torus fibres over Δ*. Its full central fibre is F=Σ m_i D_i; the reduced support D has normal crossings. Every smooth normalization component of D has geometric genus zero. The conclusion is that the action on H² of a smooth fibre is nonidentity, hence its action on rational H¹ is nonidentity.

The map is surjective: its proper image is closed and contains Δ*. Its total space is connected: a decomposition of U into two open and closed sets would give two disjoint closed images covering Δ, because each fibre is connected; each image would also be open, contradicting connectedness of Δ. Locally h is a nonzero divisor in the smooth local ring, so it is flat over the disc. The smooth full fibres off zero make h a submersion there. Shrinking the disc about zero preserves every issue at hand.

Write θ=dh/h and

L^q=Ω^q_U(log D)/(θ∧Ω^{q-1}_U(log D)).

The relation is exact locally: after absorbing the nonzero unit in h by a holomorphic root in one coordinate, h=x_0^{m_0}⋯x_ν^{m_ν}, and θ=Σm_i dx_i/x_i. At least one coefficient m_i is an invertible complex constant, so θ spans a direct summand of Ω¹_U(log D). Thus L¹ is locally free of rank two and L² is an invertible sheaf. The wedge map with θ identifies the corresponding kernel in the absolute logarithmic complex. This is the quotient and local coordinate model of Steenbrink §1.4, actually viewed on printed p.231.

For the unit absorption used here, start with h=u(x)x_0^{m_0}⋯x_ν^{m_ν}, choose a holomorphic logarithm of the unit u on a sufficiently small polydisc, and set x'_0=x_0 exp(log(u)/m_0), x'_j=x_j for j>0. The derivative in the first normal direction is a unit at the origin, hence this is a biholomorphic change of coordinates. It preserves each local branch of the support and makes the displayed monomial identity exact.

## 2. A primitive relative logarithmic top form

Proper direct-image coherence applies to M=h_*L². Multiplication by a nonzero function of the base is injective on L², and therefore on M; M is torsion-free. On Δ*, h⁰ of the fibre canonical bundle is one, so proper base change for this constant h⁰ gives rank one and identifies M with the holomorphic top-form bundle there. A coherent torsion-free rank-one module over the local ring of a smooth disc is free. Choose a generator α of M after shrinking the disc.

For every t≠0, α_t is a nonzero holomorphic two-form on the compact complex torus U_t. Such a form is translation invariant: after lifting to C² its coefficient is periodic, hence bounded on C² by compactness of a fundamental parallelepiped, and thus constant. It is therefore nowhere zero. Consequently the divisor of the section α of L² is supported in F, say Σ a_iD_i, with integers a_i≥0.

There is an index i with a_i<m_i. Indeed, if every a_i≥m_i, then α/h is holomorphic in every normal-crossing coordinate chart, and hence globally a section β of L². This would give α=tβ in the rank-one free module M, contradicting that α is a generator. This argument is division in the actual local invertible sheaf, not an identification of reduced and full fibres.

## 3. Identity monodromy makes the analytic connection holomorphic

Assume, for contradiction, that T₂ is the identity. Apply Steenbrink's analytic results under the hypotheses explicitly stated in §2.1 (printed p.234). Theorem 2.18 (pp.237–238) gives a locally free sheaf

H=R²h_*L^•

and its canonical base-change isomorphism

H/tH → hypercohomology²(F,L^•⊗O_F).

On a smooth fibre the right-hand complex is the usual holomorphic de Rham complex, and its de Rham comparison gives H²(U_t,C). Section 2.19 constructs the logarithmic connection by the exact absolute/relative logarithmic sequence. Proposition 2.20 states that the eigenvalues of its residue R lie in [0,1), and Theorem 2.21 gives T₀=exp(−2πiR). These results were read in the original scan, including their stated analytic scope and the local eigenvalue computation. No mixed-Hodge or projective degeneration assertion is being substituted.

Since T₂=I, its extension T₀ is also I. Every eigenvalue of R is therefore zero; R is nilpotent. In the identity exp(−2πiR)−I=R q(R), the polynomial q has nonzero constant term −2πi, so q(R) is invertible. Hence R=0. In a holomorphic frame write ∇=d+A(t)dt/t. The equality A(0)=0 makes this connection holomorphic at zero. Solving the holomorphic linear differential equation gives a holomorphic horizontal frame on a smaller disc.

The inclusion of the last term L² in degree two into L^• induces a map h_*L²→H. Let v(t) be the image of α in this horizontal frame. It is holomorphic at zero. The flat integral homology marking identifies its coordinates with the periods of α_t. Let Q be the constant cup-product pairing in this frame. Then

V(t)=∫_{U_t} α_t∧overline(α_t)=Q(v(t),overline(v(t))).

This is bounded as t→0. The integral is positive for t≠0: in complex coordinates α_t=f dz_1∧dz_2, the density is a positive constant times |f|² times real oriented volume. The formula uses the exact de Rham cup-product comparison and the flat pairing; it does not introduce a polarization on the total space.

## 4. Bounded volume eliminates logarithmic residue poles

For a local branch D_i, the form θ∧α is an absolute logarithmic three-form. The map

α ↦ (1/m_i) Res_{D_i}(θ∧α)

is independent of the representative of α modulo θ∧Ω¹(log D), because θ∧θ=0. It defines a logarithmic two-form on the corresponding normalization component, with at most simple poles along its branch-intersection divisor. At a generic smooth point of D_i it agrees with the ordinary restriction of the relative top form.

A pole along a double curve would give a logarithmic divergence of V(t). To check this explicitly, use a chart h=x^m y^n with a remaining coordinate z. The relation m dx/x+n dy/y=0 in L¹ makes dx/x∧dz a local generator of L². Write α=f(x,y,z) dx/x∧dz. A nonzero pole of either branch residue is exactly a nonzero value f(0,0,z) at a generic point of that double curve, up to a nonzero constant factor m/n or n/m.

Choose a small z-disc where |f(0,0,z)| is bounded below by a positive constant. Shrink the x,y discs so the same lower bound, possibly divided by two, holds whenever both |x| and |y| are small. On the nearby fibre x^m y^n=t, project to x. Over the annulus

|t|^{1/m} ε^{−n/m}<|x|<ε

the inverse images have |y|<ε. The unramified finite covering over this annulus permits integration of the pulled-back density; it is a positive integer multiple of the annular integral. The local volume is bounded below by a positive constant times

∫ (i dx∧dbar(x))/|x|²,

times the fixed positive z-area. This integral grows as a positive multiple of log(1/|t|). It contradicts the bounded global volume, whose density is nonnegative. A residue pole through a triple point would be nonzero at a generic point of a double curve; the same estimate excludes it.

All these logarithmic residue forms therefore have zero divisorial residues along their boundary. In a local normal-crossing chart, cancellation of the coefficient of each logarithmic denominator makes the form holomorphic. Holomorphic extension across the isolated triple points follows from the same coordinate divisibility, or from Hartogs extension on the smooth normalization. Thus each restriction is a holomorphic two-form on a compact normalization component. Its geometric genus is zero, so it vanishes.

The vanishing implies that the local coefficient of α is divisible by every local branch equation x_i: away from other branches, the residue map is restriction in a local trivialization. Holomorphic divisibility extends across the other branches. Since the distinct coordinate functions are relatively prime in the regular local ring, their product divides that coefficient. Consequently

α belongs to I_D L²,

where I_D=O_U(−D). This is a statement about actual holomorphic sections. It has not replaced F by its reduced support.

## 5. The nonreduced ideal has no zero residue eigenvalue

Let

K^•=(I_D L^•)/(hL^•).

The denominator is a subcomplex of the numerator: h vanishes on D, and the relative differential of h is zero. The ideal I_D is also stable under logarithmic differentiation, since locally d(product x_i)=(product x_i)Σ dx_i/x_i. Hence the absolute logarithmic sequence used in §2.19 restricts to the coefficient module I_D/(h); it remains exact because the quotient by the direct summand θ is locally split in each degree. Its connecting morphism defines a residue operator R_K on hypercohomology of K. Inclusion K→L^•⊗O_F intertwines R_K with R.

Here is the full local computation, including the effect of the ideal. In a chart h=x_0^{m_0}⋯x_ν^{m_ν}, put e=gcd(m_0,…,m_ν), n_i=m_i/e, and y=product x_i^{n_i}; then h=y^e. The relative logarithmic differential in the normal coordinates is the Koszul differential for

D_i=x_i ∂/∂x_i−(m_i/m_0)x_0∂/∂x_0,  i=1,…,ν.

The ordinary coordinate directions are contracted by the usual holomorphic Poincaré homotopy; this preserves the coefficient ideal, which involves only the normal coordinates. A monomial x^b in I_D has b_i≥1 for every i. Its Koszul weights are b_i−(m_i/m_0)b_0. If at least one weight is nonzero, contraction by the corresponding exterior basis vector divided by that weight makes its Koszul summand exact. These divisions preserve convergent power series: the nonzero weights have denominator dividing m_0 and absolute value at least 1/m_0, so the inverse factors are uniformly bounded.

All weights vanish exactly when b_i=a n_i for every i. The integer a exists because the n_i have greatest common divisor one: a=b_0/n_0 is rational, and integers c_i with Σc_i n_i=1 give a=Σc_i b_i in Z. The condition b_i≥1 forces a≥1. The quotient by (h) removes exactly the resonant monomials with a≥e. Thus the local cohomology of K is generated by

y^a times exterior products of the relative logarithmic classes,  1≤a<e.

For e=1 there are no such generators and the local cohomology is zero. For e>1 the connecting map acts on each displayed class by a/e. This follows directly from d(y^a)=(a/e)y^a θ and the same connecting-map convention used by Steenbrink; it is also the coefficient computation at the top of printed p.239. In particular every local residue eigenvalue on K is nonzero and belongs to (0,1).

To pass from this local calculation to hypercohomology, use the residue-equivariant local-to-global spectral sequence

H^p(D,H^q(K^•)) ⇒ hypercohomology^{p+q}(D,K^•).

There are finitely many irreducible components of the compact fibre and finitely many possible gcd's of the multiplicities at its strata. Choose the product P(z) of z−a/e over these finitely many possible eigenvalues. The local monomial description proves P of the residue is zero on each cohomology sheaf. Thus it is zero on the E₂ page and on each associated graded piece of the finite abutment filtration. Some fixed power of P(R_K) is therefore zero on each relevant total hypercohomology group. Since P(0)≠0, the polynomials z and P(z)^N are relatively prime, and Bézout's identity supplies a polynomial inverse for R_K. Therefore R_K is invertible.

The inclusion-induced map j_* from hypercohomology²(K) to hypercohomology²(F,L^•⊗O_F) satisfies j_*R_K=Rj_*=0. Invertibility of R_K gives j_*=0. Since α lies in I_D L², its central hypercohomology class factors through hypercohomology²(K). By the exact base-change map in §3, this says v(0)=0.

## 6. The incompatible volume orders

The holomorphic vector v now has v(t)=t w(t) with w bounded in the horizontal frame. Hence V(t)=O(|t|²).

Choose the component from §2 with a_i<m_i and a generic point of it away from other components. In local coordinates h=x^{m_i}, the relative logarithmic bundle L² is generated by dz_1∧dz_2, and

α=x^{a_i}u(x,z_1,z_2) dz_1∧dz_2

with u a holomorphic unit. Fix a small polydisc in (z_1,z_2), and use one local sheet x=ζ t^{1/m_i} of the nearby fibre. The unit is bounded below on the chosen neighbourhood, so its positive local contribution to V(t) is at least c|t|^{2a_i/m_i} for some c>0 independent of small t. Because a_i/m_i<1, this contradicts V(t)=O(|t|²). Thus T₂ cannot be the identity.

Finally, for a complex two-torus the cup-product map Λ²H¹(U_t,Q)→H²(U_t,Q) is an isomorphism. One explicit proof identifies the real torus with R⁴/Λ, chooses a lattice basis and its four invariant dual one-forms, and observes that the six ordered wedges pair as the standard basis with the six coordinate two-tori. This map is natural under the monodromy diffeomorphism. If the monodromy on H¹ were identity, its exterior square and therefore H² monodromy would be identity, contrary to the conclusion just proved.

## 7. Scope and release boundary

This proof handles every positive multiplicity m_i, using I_D/(h) precisely where a reduced-fibre argument would be insufficient. It uses the actual analytic de Rham comparison, its exact residue morphism, an explicit local volume estimate, and exact monomial contraction. No target computational program has been opened or used. No Kähler or projective hypothesis is introduced; the positive quantity is the integral of the fibre top form against its conjugate, identified with the de Rham cup pairing.

The target proof remains closed at completion of this text. The next action is an immutable timestamped derivation freeze, followed by a separately timestamped release and an actual complete target comparison. This document alone adds no event and certifies no canonical record.
