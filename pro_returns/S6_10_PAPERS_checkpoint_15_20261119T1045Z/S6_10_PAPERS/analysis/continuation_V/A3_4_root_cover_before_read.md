# A.3.4: actual root cover, local-system transport and thickening descent

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation. This derivation is written only from `analysis/continuation_II_ledger/A3_4_root_cover_clean_assertions_packet.md` and ledger's additional clean Picard-family assertion. No A.3.4 target proof, isolated target excerpt or producing program has been opened. The allowed D.1.9 character, A.4.9 smooth-fibre vanishings, A.4.7 injection, A.3.1 ideal-power sequences and proper smooth local triviality are used exactly as supplied. No new singular-support vanishing is asserted.

## A. Normalize the actual base change, keeping the unit

On a sufficiently small ambient chart V meeting S, write t∘g=u z^m with z a reduced smooth divisor coordinate and u a nowhere-zero holomorphic function. Shrink V so that u has a holomorphic m-th root v: choose a holomorphic logarithm of u and put v=exp(log(u)/m). The base-change hypersurface in V×Delta' has equation s^m-u z^m=0. Its exact factorization is

    product_{ζ in μ_m}(s-ζ v z)=0.

Each graph s=ζ v z is isomorphic to V by the projection to V, hence is normal. The factors are distinct and the hypersurface is reduced; outside z=0 they are disjoint. Its normalization is therefore the disjoint union of these m graph copies of V. The normalization map is explicitly x↦(x,s=ζ v(x)z(x)); the map p restricted to this copy is the identity x↦x. In particular p is étale and has degree m on these charts.

Here is the actual overlap map. On V_i∩V_j let z_i=a_ij z_j, where a_ij is a holomorphic unit. Equality of t∘g gives u_i a_ij^m=u_j. Choose roots v_i^m=u_i and v_j^m=u_j. Then c_ij=v_i a_ij/v_j lies in μ_m and is locally constant. The sheet labeled ζ_i on the i-chart is identified with the sheet labeled ζ_j=ζ_i c_ij on the j-chart, with the same ambient point x. These maps preserve the same coordinate s; their cocycle identity follows from that of a_ij and the displayed ratios. They give the actual glued normalized cover, without setting u equal to one or replacing the original parameter.

Properness and shrinking can be checked before using transport. The reduced support S is compact. On each of the above charts,

    d(u z^m)=z^{m-1}[(m u+z ∂_z u) dz + z sum_{j>1}(∂_j u) dx_j].

After shrinking around S, m u+z ∂_z u is nonzero. Thus g is a submersion off S in their union. Choose a relatively compact closed base disc whose inverse image is compact by properness. The closed complement of the chart union in this compact inverse image has image compact and disjoint from0. A smaller disc therefore has its entire inverse image in the chart union. On this shrunken U, the cover is the finite étale degree-m cover just constructed. Alternatively, its finiteness is the finite normalization of the finite base-change hypersurface, and the explicit local graph description supplies that finite map directly here.

The base-changed map to Delta' is proper because properness is preserved under base change and composition with the finite normalization. On a graph, g'=s=ζ v z, so at z=0 its differential is ds=ζ v dz, which is nonzero. The central fibre S'=(s=0) is smooth and reduced. After another shrink, properness excludes any remaining critical point of g' from the inverse image of the disc. Thus g' is a proper submersion on the resulting U'.

The actual Cartier pullback is immediate on a graph: z=(ζ v)^{-1}s. Hence p^*S=S', with multiplicity one, and p^*(mS)=mS'. The unit (ζ v)^{-1} is retained in this equality of local ideal generators.

## B. The fibre maps and local-system transport

For s_0≠0 the original fibre F=g^{-1}(s_0^m) is smooth. In the fibre product at this fixed s_0, the projection (x,s_0)↦x is an isomorphism onto F. Its space is already smooth and normal, so the normalization changes nothing there. Consequently

    p_{s_0}: (g')^{-1}(s_0) -> F

is the actual biholomorphism x↦p(x), not a degree-m map on this single fibre. The degree m of p on U' comes from the m values of s over a fixed nonzero t.

Let A'=p^{-1}A_U. Its character on π_1(U') is exactly χ∘p_*, where χ(a)=exp(2π i r〈gamma_U,a〉). It remains unitary, and on (g')^{-1}(s_0) it is exactly p_{s_0}^{-1}(A_U|F). The allowed nearby smooth-fibre assertion therefore gives H^0=H^1=0 on that fibre with these coefficients.

Use the allowed proper smooth local-triviality theorem on g'. A trivialization along the segment from0 to s_0 is a smooth map Φ:S'×[0,1]→U' with Φ(x,0)=x and Φ_t:S'→(g')^{-1}(t s_0) a diffeomorphism. For each x, parallel transport in the locally constant sheaf A' along τ↦Φ(x,τ) identifies its fibre at x with its fibre at Φ_1(x). These maps define an isomorphism of local systems on S': the square obtained by transporting an ambient path in S' through Φ is a homotopy, and local-system transport is invariant under such fixed-endpoint homotopy.

The cochain map is explicit. Pull a singular simplex back by Φ_1, and transport its value at the initial vertex back along the reverse Φ-path. The compatibility just described makes this map commute with the local-coefficient coboundary. The inverse is the diffeomorphism Φ_1^{-1} together with forward coefficient transport. Hence this is an isomorphism on cohomology in all degrees, and it transfers the given degree-zero and degree-one vanishings to S'.

There is no hidden component assumption. Nearby F is connected by the stated connected-fibre hypothesis, and p_{s_0} is a biholomorphism. The same actual trivialization therefore shows S' is connected. Its map p|S':S'→S is the étale degree-m cover; it need not be a disjoint union of trivial covers of S, and none is assumed.

## C. Unitary holomorphic sections and the actual conormal map

For a unitary local system on a compact connected complex manifold, its parallel local frames have constant unitary transition functions and hence define the associated holomorphic line. Parallel sections are holomorphic. Conversely, let σ be a holomorphic section. Its norm in these frames is a globally defined continuous function and attains a maximum. If that maximum is zero then σ=0. Otherwise, in a flat frame near a maximum, σ is represented by a holomorphic scalar function attaining an interior maximum of its modulus, so it is constant there. The section is parallel on that open set. On an overlapping connected chart the transition is a constant unitary scalar, so its holomorphic representative is constant there too by the identity theorem. Continuation across connected charts proves that σ is globally parallel. This proves the actual natural isomorphism from parallel H^0 to holomorphic H^0, with no Kähler hypothesis.

Apply this to A'|S'. By part B,

    H^0(S',p^*L_r|S')=0.

The allowed natural A.4.7 injection

    H^0(S',Ω^1_{S'}⊗p^*L_r|S') -> H^1(S',A'|S')

has zero target, so the cotangent-twisted H^0 also vanishes.

Since S' is the reduced fibre of the submersion g', its global ideal generator is s. The conormal map is exactly

    O_{S'} -> Ω^1_{U'}|S',      f -> f ds,

which is injective because ds is nowhere zero. The ideal-class map [s]↦ds identifies N_{S'}^*=I/I^2 with the trivial line in this sequence. Thus the actual conormal sequence is

    0 -> O_{S'} ds -> Ω^1_{U'}|S' -> Ω^1_{S'} -> 0.

Tensoring with the locally free p^*L_r preserves exactness. Both outer H^0 groups just proved vanish, so

    H^0(S', (Ω^1_{U'}⊗p^*L_r)|S')=0.

## D. Every thickening layer and the finite étale descent map

Put E'=Ω^1_{U'}⊗p^*L_r. The supplied A.3.1 sequence for k≥2 is

    0 -> E'|S'⊗(N_{S'}^*)^(k-1)
      -> E'|kS' -> E'|(k-1)S' -> 0.

The first map is multiplication by s^(k-1), and the second is reduction modulo s^(k-1). The explicit trivialization [s] of the conormal line identifies every first term with E'|S'. Its H^0 is zero by part C. Starting at k=1, induction in this exact sequence therefore gives H^0(kS',E'|kS')=0 for every1≤k≤m. No H^1 vanishing of these coherent layers is used or inferred.

Because p is étale, the actual differential pullback p^*Ω^1_U→Ω^1_{U'} is an isomorphism: on each of the graph sheets p is the ambient identity, so the map sends each coordinate differential to the same differential. It glues by the usual chain rule under the overlap maps already written. With E=Ω^1_U⊗L_r|U, the actual tensor map identifies p^*E with E'.

The Cartesian divisor identity p^*(mS)=mS' gives the finite flat degree-m map p_m:mS'→mS. Pullback on sections sends σ to σ⊗1, followed by the étale cotangent map. For a local ring R of mS, the algebra B of its finite étale pullback is a locally free R-module of rank m, even though R can have nilpotents. Multiplication by b on B has an R-linear trace Tr(b). In particular Tr(1)=m. The projection formula gives the actual map

    E|mS ⊗_R B -> E|mS,    e⊗b -> e Tr(b)/m.

It is a left inverse to e↦e⊗1. These trace maps are compatible with restriction and hence give a left inverse on global sections as well. Thus the pullback from H^0(mS,E|mS) to H^0(mS',E'|mS') is injective. Its target is zero by the preceding induction. This proves the required scheme-theoretic ambient vanishing on mS, retaining the degree factor rather than treating the cover as an isomorphism there.

## E. Exact singular-support scope and the Jacobian term

Now take the asserted arbitrary reduced Cartier support T=(h=0) in the same smooth ambient chart, with t=u h^m. On a chart carrying a unit root v, the same factorization is s^m-u h^m=product_ζ(s-ζ v h). Each graph s=ζ v h is still isomorphic to the smooth ambient chart, whatever the singularities of h=0. Thus its normalization is again the disjoint union of these graph sheets, and the map p remains étale. The reduced central support on a sheet is exactly h=0, with its original local analytic ring. Its singularity germ is therefore preserved by the actual local isomorphism p. Moreover ds|T=ζ v dh|T. At a singular point dh vanishes, so g' is not a submersion there. The smooth trivialization argument from parts B–D does not acquire an application to such a singular fibre.

The conormal base-change map sends [h] to [h∘p]. In terms of the new divisor generator s=ζ v(h∘p), this is [h∘p]=(ζ v)^(-1)[s]. Differentiating gives d(h∘p)=(ζ v)^(-1)ds plus a term divisible by s; that term vanishes on T'. Consequently the conormal and ambient cotangent maps commute with precisely this retained unit.

In coordinates, J is generated on O_T by the components of dh. An étale coordinate change has an invertible Jacobian matrix, and multiplication of the divisor equation by the above unit multiplies dh|T by that same unit. These actual two invertible operations give J'=J O_{T'} as an ideal under the local ring pullback. Regard J^(-1) as Hom_{O_T}(J,O_T), or equivalently the fractional multipliers q for which qJ⊂O_T on the total quotient ring of the reduced hypersurface. Since J is finitely presented and p is flat, tensoring a finite presentation and its Hom-kernel gives the exact natural isomorphism

    p^*Hom(J,O_T) -> Hom(p^*J,O_{T'}),
    (φ⊗b)(j⊗b') = bb' φ(j).

Together with the conormal isomorphism this gives

    p^*(N_T^*⊗J^(-1)) -> (N_{T'}^*)⊗(J')^(-1).

The map into the restricted ambient cotangent sheaf is the actual fractional product q[h]↦q dh, whose regularity is exactly qJ⊂O_T. Its pullback is the same product after the displayed unit and differential maps. Thus the term K=N^*⊗J^(-1), wherever used as the stated saturated hypersurface cotangent kernel, is preserved. No vanishing for this generally nontrivial term follows from the unit-root cover, and none is claimed here.

## F. The actual Picard family restriction

The supplied input provides an actual holomorphic Picard family P on Y×Pic(Y). Let j:U'→Y be inclusion U→Y composed with p, let i:S'→U' be the inclusion, and let f=(j∘i)×id_{Pic(Y)}. On S'×Pic(Y) define the holomorphic family

    E_all = pr_{S'}^*(i^*Ω^1_{U'}) ⊗ f^*P.

For B∈Pic(Y), the inclusion of S'×{B} forms a Cartesian square with Y×{B}. Functoriality of pullback identifies its restriction exactly with

    i^*Ω^1_{U'} ⊗ (j∘i)^*B
      = (Ω^1_{U'}⊗p^*(B|U))|S' = E_B.

These are the same pullback/tensor maps, with no replacement of the chosen universal family or parameter. This proves the requested geometric family identification. The analytic exceptional-locus and finite-kernel argument are separate ledger scopes and are not rederived or inferred here.

## Scope and chronology

All assertions A–E and the additional actual Picard restriction have been derived from the clean hypotheses and the named allowed results before the target was read. The steps are exact local factorizations, functorial maps and vanishing deductions; no numerical execution is claimed. The receiving isolated steps must now be compared, and any additional retained route beyond this note will be reported separately rather than retrospectively credited.
