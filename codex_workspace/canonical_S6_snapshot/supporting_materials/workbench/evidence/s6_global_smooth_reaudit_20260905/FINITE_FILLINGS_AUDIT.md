# Finite logarithmic fillings and analytic gluing: direct proof audit

5 September 2026. This audit reads the actual `candidate_geometry.tex`,
lines 1036 through the end, and the matrices in `exact_algebra.tex`.
It checks the two finite local fillings, their punctured identifications,
and the gluing argument. The separate period-existence and toric-cusp
audits are not replaced by this calculation. No identification with the
six-sphere, integral cohomology calculation, or counterexample to CDP20
is inferred from this local result.

## 1. The literal action and its invariant integral covectors

The ordered marked lattice is

Λ = ℤ〈γ̂, û, ŵ, δ̂〉,

with column vectors. The matrices and translation vectors are exactly

```text
A₁ = [ 1  0  0  0 ]      A₂ = [ 1  0  0  0 ]
     [ 6  0  1  0 ]           [ 0  0 -1  0 ]
     [-6 -1 -1  0 ]           [-6  1  0  0 ]
     [-2  1  0  1 ]           [ 3  0  1  1 ]

v₁ = (1, 2, -4, 0)ᵗ,      v₂ = (-1, -3, 3, 0)ᵗ,
m₁ = 3,                    m₂ = 4.
```

Multiplication gives Aⱼᵐʲ = I and Aⱼvⱼ = vⱼ. The covectors are
γ = (1,0,0,0), ψ₁ = (0,2,1,3), ψ₂ = (0,1,1,2).
For every 1 ≤ k < mⱼ, γAⱼᵏ = γ and ψⱼAⱼᵏ = ψⱼ.
The matrix Aⱼᵏ − I has rank two. The two covectors therefore span the
rational invariant space. Their two-row matrix has a 2-by-2 minor 1
(columns γ̂, ŵ for ψ₁; columns γ̂, û for ψ₂), so their span is a
primitive sublattice of Λ*. This proves that it is the entire integral
invariant lattice, not merely a finite-index sublattice. The exact
checker records each power and minor.

Their evaluations are γ(v₁)=1, γ(v₂)=−1, ψ₁(v₁)=ψ₂(v₂)=0.
If x mod Λ were fixed by x ↦ Aⱼᵏx + kvⱼ/mⱼ, then

(Aⱼᵏ−I)x + kvⱼ/mⱼ ∈ Λ.

Applying γ gives respectively k/3 ∈ ℤ or −k/4 ∈ ℤ, impossible for
the specified nonidentity powers. This tests every nonidentity power,
not only a chosen generator.

For completeness, the general fixed-point criterion quoted in the source
is valid too. If A has order m, put p=(I+A+⋯+Aᵐ⁻¹)/m on Λℝ.
Then p²=p, im p=ker(A−I), and ker p=im(A−I), as follows by applying
A−I and comparing dimensions on the eigenspaces of a finite-order
linear map over ℂ. The group pΛ is a lattice in im p: it spans im p
and is contained in (1/m)Λ, hence is discrete. A functional on im p
integral on pΛ pulls back by p to an invariant integral covector on Λ;
restriction is the inverse operation. Thus the dual lattice of pΛ is
exactly the invariant integral covector lattice. If every such covector
takes an integral value on b, then pb∈pΛ. Choose λ∈Λ with pλ=pb;
b−λ lies in ker p=im(A−I). Solving (A−I)x=λ−b supplies a fixed
point mod Λ. The converse follows by applying an invariant covector to
the fixed-point equation. No assumption of an integral direct-sum
decomposition of Λ into invariant and moving parts is used.

## 2. Actual holomorphic family, not a constant complex torus substitution

The source period map Π(z):Λℝ→ℂ² is real-linear invertible at each z.
Its complex entries are holomorphic and it satisfies

R_gⱼ(z)Π(z) = Π(gⱼz)Aⱼ.

For a compact base set, the inverse matrices Π(z)⁻¹ have uniformly
bounded real operator norm. Consequently a bounded set in the fibre
coordinates meets only finitely many of its translates by Π(z)Λ.
No nonzero lattice vector acts trivially. These observations give the
free properly discontinuous lattice action defining the holomorphic
family and the real-analytic marking

Ξ(z,x mod Λ) = [z,Π(z)x].

Its inverse is obtained by Π(z)⁻¹ on local fibre representatives; changing
a representative changes x by a member of Λ. Over a compact base set K,
the image of K×[0,1]⁴ under this marking is the full inverse image of K.
It is compact. Thus the family projection is proper, with no requirement
that the real marking be holomorphic in x.

The actual logarithmic lift is

Gⱼ(z,ζ) = (gⱼz, R_gⱼ(z)ζ + Π(gⱼz)vⱼ/mⱼ).

This map is holomorphic in (z,ζ). The covariance formula shows that it
respects the varying lattice. In the marking Ξ it is precisely
(z,x)↦(gⱼz,Aⱼx+vⱼ/mⱼ), and its k-th power is
(gⱼᵏz,Aⱼᵏx+kvⱼ/mⱼ). The base has no fixed point away from the
elliptic centre, and section 1 rules out every fixed point above that
centre. At k=mⱼ its translation is vⱼ∈Λ; hence the quotient action has
exact order mⱼ and is free.

A free finite holomorphic action has disjoint sufficiently small
neighbourhoods of the points in each orbit. Their images give quotient
charts isomorphic to the original neighbourhoods. Distinct finite orbits
can also be separated by such neighbourhoods. Thus the quotient Nⱼ is
Hausdorff and smooth, and the quotient map is a degree-mⱼ holomorphic
cover, not a branched cover. This explicitly verifies the trivial-
stabilizer case of Cartan's quotient construction (citation below).

The base invariant is tⱼ=sⱼᵐʲ. Its divisor upstairs is mⱼ times the
central torus. Local biholomorphy of the quotient preserves orders of
vanishing; downstairs fⱼ*(pⱼ)=mⱼSⱼ. For a compact K⊂Dⱼ, its inverse
image under sⱼ↦sⱼᵐʲ is compact, the torus family above that set is
compact, and its finite-quotient image is fⱼ⁻¹(K). This proves the local
properness assertion, including the multiple scheme fibre.

## 3. Logarithm, signs, and the punctured overlap

The chosen elliptic orientations are retained:
sⱼ(gⱼz)=exp(−2πi/mⱼ)sⱼ(z). On a simply connected punctured chart
choose ℓ(z)=log sⱼ(z). Write α(z)=ℓ(z)/(2πi).
Translation by [α(z)Π(z)vⱼ] defines hⱼ. A branch change ℓ↦ℓ+2πin
adds nΠ(z)vⱼ∈Π(z)Λ, so hⱼ is globally well-defined on the punctured
torus family. It is holomorphic and invertible by opposite translation.

On the gⱼ-translated chart take
ℓ′(w)=ℓ(gⱼ⁻¹w)−2πi/mⱼ. Thus α′(gⱼz)=α(z)−1/mⱼ. Using
Aⱼvⱼ=vⱼ, direct composition gives

Gⱼ hⱼ⁻¹(z,ζ)
 = (gⱼz,R_gⱼ(z)ζ−(α(z)−1/mⱼ)Π(gⱼz)vⱼ).

Applying hⱼ at gⱼz cancels the displayed term. Therefore
hⱼGⱼhⱼ⁻¹=Gⱼ⁰, where Gⱼ⁰ is the linear lift. This is the exact
punctured-filling identification; its inverse is induced by hⱼ⁻¹.

Importantly, α is complex. This proof does not substitute x↦x+αvⱼ in
the real marking. The correct real shift is

a(z) = Re(α(z))vⱼ + Im(α(z))J_zvⱼ,
J_z = Π(z)⁻¹ i Π(z).

The global object is a(z) mod Λ; changing the logarithm branch adds nvⱼ
to this local representative. It satisfies Π(z)a(z)=α(z)Π(z)vⱼ.
Since R_gⱼ is complex-linear,
J_gⱼz Aⱼ=AⱼJ_z, and consequently
a(gⱼz)=Aⱼa(z)−vⱼ/mⱼ for the compatible local branches above.
These are exactly the corrected formulas used
in the current integral-Leray proof. The holomorphic conjugacy above
was already valid; this audit does not reintroduce its formerly incorrect
real-coordinate shorthand.

Choose Δⱼ=sⱼ⁻¹({|sⱼ|<ρⱼ}) with a sufficiently small positive ρⱼ;
this round coordinate disc preserves rotation invariance and
translate-disjointness. Radial contraction sⱼ↦(1−u)sⱼ in Ξ commutes with Gⱼ, since it keeps
x fixed and the affine action on x is constant. It descends to a strong
deformation retraction Nⱼ→Sⱼ. A nearby fibre above a chosen root s
of tⱼ meets each Gⱼ-orbit exactly once. Its retraction is therefore
x mod Λ ↦ orbit of x in Sⱼ. The induced central-to-nearby cohomology
map is exactly πⱼ*:Hʳ(Sⱼ;ℤ)→Hʳ(Λℝ/Λ;ℤ), including all integral
indices; passing merely to invariant rational cohomology is not used.

## 4. Global gluing: the Hausdorff argument in full

The base cover consists of B°=B\{p₀,p₁,p₂} and pairwise disjoint
small discs D₀,D₁,D₂. The middle piece J lies above B° and each Nⱼ
lies above Dⱼ. Each prescribed gluing identifies the entire restriction
over Dⱼ*=Dⱼ\{pⱼ} by a biholomorphism over the identity on the base.
There are no overlaps between different Nⱼ, and hence no triple-overlap
cocycle left to specify.

In the disjoint union J⊔N₀⊔N₁⊔N₂, an equivalence class has at most
one point in each piece. Saturating an open subset applies only these
open-overlap biholomorphisms, and produces an open subset. Thus every
piece embeds openly in the quotient. It follows that the local complex
charts give a complex atlas. A countable union of the countable bases
from these four pieces gives a countable base for the quotient.

The local maps to B induce a continuous quotient map f. Two quotient
points over distinct base values are separated by inverse images of
disjoint base neighbourhoods. If their base value is pⱼ, both points
belong to the openly embedded Hausdorff piece Nⱼ. If their common
base value is not special, both have representatives in the openly
embedded Hausdorff piece J. In either case, disjoint open
neighbourhoods in that single piece remain disjoint open neighbourhoods
in the quotient. This proves Hausdorffness; an unrestricted gluing
principle that could allow doubled origins is not being invoked.

More precisely f⁻¹(Dⱼ) is exactly the image of Nⱼ, since every point
from J over Dⱼ* was identified with its unique representative in Nⱼ.
Likewise f⁻¹(B°) is exactly the image of J. Thus local properness refers
to the complete inverse images of the base cover, not just to selected
open subsets of those inverse images.

Here is a direct passage to global properness. For compact K⊂B,
choose finitely many open base neighbourhoods Vₐ whose closures are
compact and contained in one member Uₐ of that base cover, such that
K⊂⋃Vₐ. This is possible because the Riemann surface B is locally
compact and Hausdorff. The sets K∩closure(Vₐ) are compact subsets of
Uₐ, and their inverse images are compact by local properness. Their
finite union is f⁻¹(K), hence compact. With K=B, the total space is
compact. All pieces are connected and each Nⱼ meets J through a
nonempty punctured restriction, so the total space is connected.
The local descriptions also give connected fibres and surjectivity.

This checks the finite-filler and gluing portions. The cusp piece still
has its own explicit construction to audit; neither this argument nor
Cartan's theorem supplies it automatically.

## 5. Literature and verification receipt

Henri Cartan, *Quotient d'une variété analytique par un groupe discret
d'automorphismes*, Séminaire Henri Cartan 6 (1953-1954), exposé 12,
pp. 1-13, especially conditions (I)-(II) and Theorem 1 on pp. 12-1--12-2,
and the finite-action local-coordinate Lemma 1 on p. 12-3.
[Primary archive](https://www.numdam.org/item/SHC_1953-1954__6__A12_0/).
The existing local primary scan was checked visually on those complete
three pages. The present free-action case is proved directly above.
No publisher PDF is added to the public evidence by this audit.

`FINITE_EXACT_RESULTS.json` records source hashes and the finite matrix
certificates. Those certificates do not prove analytic existence; the
analytic and gluing arguments are articulated here. No substantive error
was found in these portions of the current source. The extra separation
and compact-cover details above expand valid arguments rather than
repair a mathematical contradiction.
