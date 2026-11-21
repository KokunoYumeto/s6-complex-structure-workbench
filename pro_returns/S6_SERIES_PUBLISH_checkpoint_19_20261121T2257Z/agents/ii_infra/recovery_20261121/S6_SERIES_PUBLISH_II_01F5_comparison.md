# 01F5 / cdp:st:C.3.10: complete comparison

The fresh smooth-scope derivation was frozen on 21 November 2026 at
22:26:22 UTC, before release of the printed proof. I then read the entire
released proposition and all twelve proof items, and subsequently read
the entire proposed v2 proposition/proof and both complete bibliography
before/after pairs. The final guard preserves the printed logarithmic
argument. It does not replace it with the independent fibre-integral
argument.

The original potentially singular domain is not established. The precise
mathematical repair is “smooth compact complex threefold.” Its use is
bound to D1.9's manifold hypothesis, D1.12's index calculation, and the
smooth resolution/logarithmic comparison. All actual receiving claims
already have this domain: C3.1 explicitly; C3.11 through C3.1; C4e through
the exact integral-CDP definition; and main Theorem B and its outline
explicitly. The identifier-only frontmatter occurrences add no domain.
The root's complete input/frontmatter audit and the statement-only body
receiver audit are bound in the JSON receipt.

## Comparison of every printed item

| Printed item | Actual comparison and disposition |
|---|---|
| 1 | Borcea pp.373–374 supplies all complex structures on the fixed differentiable type. SS §1 pp.2–3 supplies the intrinsic elliptic reduction, degree, Picard quotient and contraction parameter. The family construction and descent character are given explicitly below. Bounded extension of α to P1 is valid. |
| 2 | The full cited D1.9 construction supplies the actual γ and β, including all-full-fibre naturality and nonvanishing. The full cited D1.12 index/cup argument supplies the locally free E,G, base change and determinant isomorphism. The coefficient lattice maps through the exponential quotient exactly as in the frozen derivation, so λ(β) is an integer and is constant. |
| 3 | Matching the quotient class α^n identifies the actual line bundle with the pullback of a degree-nd line, with a degree-zero twist allowed explicitly. For nd≥2 the elliptic linear system is nonconstant. Coherent direct image on P1 and a sufficiently positive base twist produce global sections whose ratio varies on the fibre. This proves the stated algebraic-dimension contradiction. The frozen derivation used a further power with degree≥3, which gives the same required nonconstant function. |
| 4 | The real coefficient map for an elliptic curve is a real isomorphism. Together with real injectivity on the Kodaira surface this proves the displayed real-subspace implication. Saturation follows also directly from the torsion-free quotient of Hom(π1,Z). Fixing a primitive integral vector makes monodromy parabolic; the bounded exponential of its period is constant on P1, forcing the translation integers to vanish. |
| 5 | The two intrinsic moduli and degree determine the isomorphism class. In Borcea's complete family, the local period map lies in one countable integral-cohomology orbit. Shrinking to a coordinate chart, a nonconstant coordinate would have an uncountable connected image. Thus the parameter is constant and its pullback family is a product. This verifies the actual local holomorphic comparison, rather than inferring it just from a pointwise label. |
| 6 | In the central extension, identity on the base quotient fixes the commutator w^d. Torsion-freeness of the centre implies w itself is fixed. The holomorphic elliptic-fibre linear part is a scalar fixing that nonzero period, hence is 1 and fixes the other central generator. The remaining two generator images retain all central shears. |
| 7 | The complete real-group pullback fixes the actual four H2 basis classes modulo explicitly exact multiples of the base wedge. The calculation below and the fresh postrelease program give every shear and primitive. This verifies the full linear action, not merely its projectivization. Contractibility of the universal cover identifies the original map with the group-model map up to homotopy. |
| 8 | For each smooth-centre blowup, the exceptional fibres are projective spaces and the successive formal conormal layers have nonnegative twists. Their higher cohomology vanishes, so analytic formal functions and coherence give R^jρ_*O=0 for j>0. Proper bimeromorphic normality gives ρ_*O=O. Derived composition gives the displayed canonical map R²h_*O≅R²f_*O. This uses the smooth total-space scope, now explicit. |
| 9 | I re-viewed the complete Steenbrink pp.234,237–239. Section2.1 states the proper holomorphic, connected complex-manifold, normal-crossing-fibre setting without a Kähler assumption. Theorem2.18 gives the logarithmic hypercohomology bundle/base change; §§2.19–2.21 give the connection, residue eigenvalues in [0,1), and T=exp(−2πiR). With T=I the eigenvalues are 0 and the nilpotent part is 0 as well, since the polynomial logarithm of exp(−2πiN) recovers N. The connection therefore has no pole. The degree-zero projection is a chain map: its positive-degree components are zero and the target differential is zero. Its derived pushforward and the item8 identification give the stated holomorphic map p, with the correct smooth-fibre coefficient map. |
| 10 | In the actual product charts the coefficient map and its kernel are fixed. The invariant (0,2) form is closed because its differential contains the repeated base (0,1) factor; its pairing with the holomorphic two-form is nonzero. Thus the map is surjective. A constant class outside that common kernel gives a global section nonzero on the regular base; the proof does not require nonvanishing at the missing points. |
| 11 | The cup map with nowhere-zero β gives the exact bundle sequence on the entire P1. H¹(P1,O)=0 lifts the global section to v. Both displayed maps on each product chart are nonzero linear maps with the same one-dimensional kernel; their ratio is a nonzero constant because β, the de Rham class, its coherent projection and the oriented quotient are all fixed there. The actual global maps make these constants agree on overlaps. The frozen invariant-form Serre-pairing calculation gives an explicit version of the same scalar relation. |
| 12 | The nonzero constant quotient differential permits one fixed exponential parameter z. The resulting ambient line bundle restricts to the pullback of positive degree nd≥2 on every regular elliptic base. The item3 coherent-section construction produces the surface image/nonconstant fibrewise meromorphic function and contradicts a(Y)=1. |

## Actual Picard-family construction and the descent convention

The source loci are Borcea printed p.377, Remark1 (complete holomorphic
family), pp.379–380 (the two quotient parameters), and SS author pp.2–3,
also actually read in the pinned arXiv v2 pp.2–3. The arXiv source member
kodaira.tex matches the supplied source byte for byte; this edition
transport does not claim that the author PDF and arXiv PDF are identical.
Both page pairs were actually viewed. All existing SS citations in this
paper point to §1, Proposition3.1, Definition2.1 or Lemma1.1; the shared
bibliography now explicitly preserves the supplied v2 statement/page
edition and separately gives the published chapter DOI and pages.

Locally pull the given smooth family back from Borcea's complete family.
In its marked model the rank-two elliptic-base lattice and its holomorphic
coefficient line A vary inside the rank-three integral H1 lattice and
rank-two coherent H1 bundle E. The quotient lattice is rank one. If e is
its primitive generator and \bar e its nowhere-zero image in E/A, the
actual quotient homomorphism is

    (E/A)/(Z·bar e) → C*,    [z·bar e] ↦ exp(2πiz).

The map is holomorphic in the base because the coefficient morphism from
the flat de Rham bundle to the coherent bundle is holomorphic, and the
elliptic-base line comes from the explicit holomorphic family. Changing
the primitive generator changes this homomorphism only by inversion.
The contraction parameter of the model lies in 0<|α|<1; the
positive-degree class selects the sign and excludes that inversion.
This constructs the actual oriented relative quotient, and its
intrinsic kernel generator α varies holomorphically. SS p.3 identifies
that kernel and gives the explicit commuting transformations on C*×C*.

For the character convention, let A0 be the degree-d line on the
elliptic base, let T(v)=αv on A0\0, and define

    Lχ = ((A0\0)×C)/((v,z) ~ (T(v),χ^(-1)z)).

The explicit map

    Lα → p*A0,    [v,z] ↦ z v

is well defined because (αv)(α^(-1)z)=vz. It is holomorphic and
fibrewise linear and invertible. Local lifts of the cyclic covering with
transition T^n give line-bundle frame transition χ^n, so χ=exp(2πit)
is exactly the exponential of t times the primitive integral
coefficient class, with the same convention as the printed λ equation.
This proves the descent identification and its sign. It does not merely
rename a topologically trivial line bundle as a positive-degree pullback.
Any other bundle with that quotient coordinate differs by p*Pic0(B);
the degree therefore stays d, or nd after taking a power.

The bounded α used here is the intrinsic SS contraction coordinate.
The frozen argument additionally used Borcea's separate explicit
coordinate exp(πims). It made no unsupported assertion that those
two written exponential expressions were equal.

## Full H2 action and its transport to the printed forms

Borcea's notation has V=−(2/m)X4. When M=I,k=0,e=1, his formula (15)
retains the four arbitrary central shears

    X1 ↦ X1+rX3+zV,       X2 ↦ X2+pX3+qV,
    X3 ↦ X3,             V ↦ V.

The actual dual one-form pullbacks are

    θ1 ↦ θ1,                        θ2 ↦ θ2,
    θ3 ↦ θ3+rθ1+pθ2,
    θ4 ↦ θ4−(2z/m)θ1−(2q/m)θ2.

Thus the four ordered cohomology basis representatives
θ13,θ23,θ14,θ24 change, respectively, by

    pθ12,  −rθ12,  −(2q/m)θ12,  (2z/m)θ12.

Since dθ4=−2θ12, their explicit primitives are
−(p/2)θ4, (r/2)θ4, (q/m)θ4, −(z/m)θ4. Hence the actual
linear matrix on H²(R) and H²(C) is I4. The free integral lattice
injects into real cohomology, so its action is I as well. F5 needs
no assertion about the torsion action.

The exact conversion to the printed forms is

    a=θ1, b=θ2, c=−(d/2)θ4, e=θ3.

It gives dc=d a∧b exactly. The printed basis (ac,bc,ae,be)
is obtained from the Borcea basis (θ13,θ23,θ14,θ24) by
the invertible permutation/rescaling

    (ac,bc,ae,be)=(-(d/2)θ14, -(d/2)θ24, θ13, θ23).

This exhibits the precise cohomology morphism relating the two
calculations. The fresh postrelease certificate retains every shear
and computes its exact primitive. Formula(17)'s use of homogeneous
coordinates therefore does not hide an untested scalar action.

## Independent extension method and printed-method preservation

The frozen derivation uses the top-form fibre integral for a generator
of f_*ω. It fixes the measures and proves the exact identity

    ∫Δ (∫Yt Ωt∧barΩt) i dt∧dbar t
      = ∫f^{-1}(Δ) iΩ3∧barΩ3.

Finite right side gives L²-removability of the scalar period. Primitivity
gives a divisor component with a<m; the coordinate t=z^m gives the
relative exponent a−m+1 and the uniform lower bound
4u0²π²r⁴/m². This establishes a nonzero extension directly in the
original smooth Y. The target instead obtains a sufficient coherent
section from the logarithmic de Rham projection after a resolution.
Both yield the concrete global section needed for the final quotient
argument, through the maps checked above. The stronger trivialization
proved in the independent route is not inserted into the printed proof.

The released target cites no computer routine for these algebraic
steps. The prereading exterior-algebra program checks the coefficient
maps, volume, Serre pairing and exact coarea sign. The separate
postrelease program checks all central shear primitives and records
its later timing. Neither program receives an extra independent event.

## Exact editorial scope and reading attestation

The final batch consists of one complete proposition/proof pair and
two complete bibliography pairs. It contains 28 literal edits.
The sole domain change is the explicit smoothness repair. All twelve
proof items, every display formula, and every stable C.PK.1–8 label and
hypertarget are preserved. Eight manual number tags are replaced by
the current equation counter. The whole-source exact-token audit
found no outside-owner bare C.PK.1–8 receiver.

Two literal C.SK.2 references are transported to the already present
exact quotient label; its display is archived by hash. One unchanged
C.PK.2 reference moves within item11 from an announcement to the
actual quotient assertion. The remaining references retain their order.
Only the iteration prefix and four duplicated announcement/reassurance
inline mentions are removed; their retained witnesses are recorded in
the guard. The statements, deductions and logarithmic chain map remain.

I actually read the entire original and final v2 proposition/proof
and both original/proposed bibliography entries, rather than only
examining a generated diff. There is no unresolved mathematical
discrepancy within the corrected smooth domain. Application of the
scope repair, exact source/log rebinding, and root admission are still
required. One targeted independent check and one actual full
comparative rereading are proposed for this printed owner only.
Bibliography, program execution, page images and metadata add no
separate mathematical event. No canonical files have been changed.
