# 02WM / night:P4.15: independent preproof derivation and scope refutations

The target printed proof, outline and prior target programs have not been
opened. The exact target statement and its safe input packets have been
read. This record proves its differential identity, derives the
classification and conductor conclusions in their precise applicable
scopes, and preserves two explicit counterexamples to broader readings of
the original wording. The original wording is not certified unchanged.

## 1. Exact objects and the two scope tests

The standing map is f:Y→B, proper and surjective with connected fibres,
where Y is a smooth compact complex threefold with b1(Y)=b2(Y)=0 and the
smooth general fibre is a complex two-torus. For the classification proof,
let mS be the actual full fibre with S irreducible, reduced and singular.
Let ν:T→S be its smooth normalization, and let j:T→Y be ν followed by the
closed inclusion of S. The differential called dν in the target is dj.
Its maximal-minor scheme is Z and its length is ℓ; by the stated rank
hypothesis Z is finite. Write D for the full conductor divisor on T,
R=D_red and C=Sing(S)_red.

The original opening merely says “irreducible singular fibre.” The separate
record `S6_SERIES_PUBLISH_II_A_02WM_multiple_smooth_fibre_preproof.md`
constructs actual fibres 3S1 and 4S2 of this same completed sphere family:
their supports are smooth finite étale quotients of products of elliptic
curves, their normalizations are the identity, and the differential has
rank two everywhere. Their π1 and b1, transported by the explicit covers,
exclude all three listed surface alternatives. Their canonical characters
also give κ=0. Thus a definition allowing a singular full multiple fibre
with smooth reduced support requires an explicit opening-scope repair.

The original final conductor sentence is unqualified. The separate record
`S6_SERIES_PUBLISH_II_A_02WM_scope_counterexample_preproof.md` gives the
actual cusp W in the completed same family, with ν:dP6→W, ℓ=0, and reduced
conductor the six rational boundary curves. Its exact conductor
normalization η_R has Euler number 6; a disjoint union of smooth elliptic
curves has Euler number zero. This refutes the universal final sentence
in the rational alternative. The proof below establishes that sentence
for the last two alternatives, with the exact same ν and conductor maps.
Both complete refutation records are part of this frozen derivation.

## 2. The differential cokernel and its finite scheme

Set E=j*T_Y and F=T_T. The rank-two map a=dj:F→E is injective as a sheaf
map: its generic kernel is zero, and its locally free source has no torsion.
Its cokernel M has rank one and is locally free off Z. At a point of Z,
the length-one locally free resolution 0→F→E→M→0 gives depth(M)≥1 over
the regular local surface ring. Hence M has no finite-length torsion.
It has no divisorial torsion because the differential has rank two at the
generic point of every divisor. Every possible torsion subsheaf would
therefore be supported in dimension zero, so M is torsion-free.

Its double dual is the line bundle

L=M**=det(E)⊗det(F)^(-1).

In local frames, a is a three-by-two matrix. The signed maximal-minor row
defines E→L, annihilating a(F). Where a minor is a unit, choose the two
columns of a as the first two frame vectors of E; the wedge row is then
projection onto the remaining quotient coordinate. The determinant
transition functions identify these rows on overlaps. The row therefore
descends to a generically injective map M→L. Its kernel is a torsion
subsheaf of the torsion-free M and is zero. Its image is exactly I_Z L,
because its local coefficients are precisely the declared maximal
minors. This proves the needed local exactness directly. The resulting
exact global sequence is

0→T_T→j*T_Y→I_Z L→0.

This specifies the scheme whose colength is ℓ, rather than replacing it
by the cardinality of the rank-drop points.

## 3. Chern character, sign and Noether relation

Poincaré duality on the compact oriented real six-manifold Y gives
H4(Y;Q)=0 from H2(Y;Q)=0. Thus c1(E)=c2(E)=0 rationally. Consequently
c1(L)=K_T. Put k=c1(K_T), e=c2(T_T) and [Z]=ℓ[point]. The K-theory
identity [I_Z L]=[L]−[O_Z L] gives the degree-four Chern character directly:

ch(T_T)=2−k+(k²−2e)/2,
ch(I_Z L)=1+k+k²/2−[Z].

Adding in the exact sequence yields

ch(E)=3+k²−e−[Z].

Its degree-four term is zero, hence e(T)=K_T²−ℓ. This is an additive
Chern-character computation, independently written here; it does not use
the previous WU total-Chern-polynomial routine. Noether's formula
K_T²+e(T)=12χ(O_T) then gives

2e(T)+ℓ=12χ(O_T).

The exact new program certifies both the additive coefficients and the
degree-one elimination identity. The identity e(T)=K_T²−ℓ itself applies
to the smooth multiple supports in Section 1 as well; the restriction to
singular reduced support enters the subsequent κ argument.

## 4. Canonical conductor and the complete surface alternatives

Input A.5.3 is applied with the identity as the minimal resolution of the
smooth normalization T. It gives the effective full conductor and
ω_T(D)=ν*ω_S. Input P4.12 gives ω_S^m=O_S, hence K_T+D is numerically zero.
Since S is singular, that same input makes S nonnormal and gives κ(T0)=−∞
on a minimal resolved model T0. The reduction S is a hypersurface in a
smooth threefold, hence satisfies S2. Its nonnormal locus consequently
contains a curve by the R1/S2 normality criterion, so D is nonempty.

Write q:T→T0 as a finite sequence of r point blowups. Pluricanonical
sections are preserved by each blowup: pullback multiplies the local
canonical generator by the Jacobian; conversely a section on the blowup
restricts to the complement of the centre and its coefficients extend
across that point by Hartogs. Thus κ(T)=κ(T0)=−∞ and p_g(T0)=0.

Here is a primary-source derivation of the alternatives, including its
analytic-to-projective map. It avoids importing an unopened classification
table.

### 4a. Kähler minimal model

For a Kähler T0, p_g=0 implies H^(2,0)=H^(0,2)=0, so H2(T0;R) is of type
(1,1). Choose a rational class sufficiently close to a Kähler class in
this finite-dimensional space. Represent the difference by the harmonic
real (1,1)-form for a fixed Kähler metric; a sufficiently small perturbation
preserves positive definiteness on the compact surface. Scaling by an
integer gives an integral Kähler class. Kodaira's original Main Theorem,
PNAS 40 (1954), p.314, now supplies an actual embedding

Φ:T0→P^N,  z↦[s0(z):...:sN(z)],

from sections of a sufficiently high tensor power of the positive line
bundle. Its proof on pp.314–315 separates points and tangent directions
using the indicated blowup restriction sequences. The map is a
biholomorphism onto a nonsingular projective algebraic surface. The
pluricanonical systems are transported by pullback through this Φ.

Beauville's original monograph, Theorem VI.17 and Corollary VI.18,
pp.111–112, now apply to Φ(T0): all plurigenus systems vanish, so the
surface is ruled. His minimal-model results V.10, pp.79–80, and III.10,
p.40, give either a rational surface or a projective-line bundle over a
curve. The birational and bundle maps pull back through Φ to T0. Thus
this use specifies the actual embedding and ensuing ruled morphism.

### 4b. Non-Kähler minimal model, including the elliptic overlap

In the exact opened arXiv1810.05768v3 edition, Ornea–Verbitsky–Vuletescu
Theorem 5.1, p.27 (complete proof pp.27–29), states that a minimal
non-Kähler surface is isotrivial elliptic or class VII, explicitly allowing
both. A class-VII model already has b1=1 and κ=−∞ by their Definition1.6.

For its isotrivial elliptic alternative, Theorem4.2 and its local-model
Remark4.4 give the actual local maps

(E×Δ_s)/⟨(z,s)↦(z+e,ζ_m s)⟩ → Δ_t,  t=s^m,

where e has exact order m and the action is free. Proposition4.5 supplies
the global elliptic action along the fibres. A nonzero infinitesimal
generator v is therefore a nowhere-vanishing holomorphic vector field.
There is an exact sequence 0→O→T_T0→Q→0. The differential of the ruling
p:T0→B0 factors through Q. In the displayed local chart it sends the
class of ∂/∂s to m s^(m−1)∂/∂t. Therefore, for the ramification divisor
R_p=Σ(m_i−1)E_i of multiple reduced fibres,

Q=p*T_B0⊗O(−R_p),   K_T0=p*K_B0⊗O(R_p).

This gives K_T0²=0: the pullback of a base divisor and every E_i are
rational multiples of fibre classes, which have zero pairings. The
nowhere-zero vector field gives c2(T_T0)=0. Noether then gives χ(O_T0)=0.
Since p_g=0, h^(0,1)=1. OVV Theorem2.5, pp.7–9, gives the exact Hodge
decomposition b1=2h^(0,1)−1, so b1(T0)=1. Consequently this elliptic
alternative also satisfies their definition of class VII. The argument
uses the actual action, tangent quotient and ramification map, and does
not treat the two source alternatives as disjoint categories.

We have proved that the minimal model needed here is rational, ruled over
a positive-genus curve, or class VII. All source statements above were
opened before this derivation is frozen. The retrieved v3 source member
matches the attached OVV source byte for byte; no edition is inferred
from its filename alone.

## 5. Numerical restrictions and the Hopf cover

For a rational T, χ(O_T)=1. This follows from the common blowup maps to
P2, or from Beauville's birational invariants III.20 and the local
blowup formulas. A rational minimal model is P2 or F_n, so e(T)≥3.
Thus e(T)=6−ℓ/2 and 0≤ℓ≤6. Integrality also forces ℓ even; the stated
interval is retained rather than adding this stronger restriction to the
target statement.

For T0=P_B0(V) over a curve of genus g≥1, Beauville III.18 gives
K_T0²=8(1−g), and the actual P1-bundle has e(T0)=2e(B0)=4(1−g).
For the r point blowups, e(T)=4(1−g)+r and K_T²=8(1−g)−r.
The differential identity is therefore

2r+ℓ=4(1−g).

The nonnegative left side excludes every g≥2. For g=1 it gives r=ℓ=0,
so T is minimal ruled over an elliptic curve.

For a minimal class-VII model let b2(T0)=k≥0. Here b1=1, so e(T0)=k.
The vanishing p_g and OVV's Hodge formula give h^(0,1)=1 and χ=0;
Noether gives K_T0²=−k. Under r blowups, e(T)=k+r and K_T²=−k−r.
The differential identity gives 2(k+r)+ℓ=0. Therefore k=r=ℓ=0.

Apply the actual finite-cover conclusion of Buonerba–Bogomolov–Kurnosov,
arXiv1709.00062v3, Theorem1, p.1, to this minimal class-VII surface T.
It gives an étale covering p:T'→T with T' Hopf or Inoue. These covering
surfaces are compact, so p is finite. The preimage p^(-1)(D_red) is a
nonempty analytic curve, because p is finite, surjective and étale and D
is nonempty. Inoue's original paper proves absence of curves for all
three families: Proposition2(i), pp.274–275; Proposition3(i), p.277;
and the S-minus double-cover construction after equation(21), p.279.
Those complete source loci were actually viewed. Hence T' is Hopf.

Let u:C²\{0}→T' be its universal covering. The composite p∘u is a
covering of T. The source retracts onto S3 and is simply connected,
so p∘u is T's universal covering as well. Thus T is Hopf by the
universal-cover definition. This explicitly transports the finite-cover
theorem to the required assertion about T itself.

## 6. Immersion and the elliptic-ruled conductor

Both last alternatives have ℓ=0. The maximal-minor ideal is then the
unit ideal everywhere, so dj is an immersion everywhere.

On a minimal ruled surface T→E with g(E)=1, push no divisor through an
unstated modification: use the actual conductor D on T. Its intersection
with a ruling fibre F is D·F=−K_T·F=2. The horizontal possibilities are
two coefficient-one sections, one coefficient-one bisection, or twice a
section, plus a vertical sum V=Σa_iF_i.

For a coefficient-one horizontal component H, adjunction gives
2p_a(H)−2=−(D−H)·H≤0. Its normalization maps finitely and nonconstantly
to E, so Riemann–Hurwitz gives genus at least one. Therefore H is smooth
elliptic and (D−H)·H=0. Any vertical fibre would have positive
intersection with H, so V=0; two sections are disjoint. This settles the
reduced horizontal cases, including the bisection.

In the remaining case D=2H+V, the degree-one map of H to E makes H a
section: its normalization is E and its map into the bundle is a section
with closed smooth image. If V has v distinct fibres, each rational
fibre meets H once and contributes 2−1 to the reduced conductor Euler
number. Hence e(R)=v and e(T\R)=−v, since e(T)=e(H)=0. The exact
normalization complement is T\R≅S_reg. Input P4.13 gives its Euler
number nonnegative, so v=0. Thus in every elliptic-ruled case R is a
disjoint union of smooth elliptic curves.

## 7. Hopf conductor curves and their exact image germs

In the Hopf alternative b2(T)=0. Consequently all rational divisor
intersection classes vanish. Every irreducible curve A⊂T has
2p_a(A)−2=(K_T+A)·A=0, hence p_a(A)=1. Its normalization cannot be
P1: the map P1→T lifts through the simply connected domain to
C²\{0}, whose two coordinate functions on the compact P1 would be
constant. Its image would then be a point, contradicting that A is a
curve. Thus its geometric genus is one and its delta defect is zero,
so A is smooth elliptic. Two distinct curves have nonnegative local
intersection multiplicities and total intersection zero, hence are
disjoint. This proves the same description of R in the Hopf case.

It remains to prove the actual image and covering claim, rather than
deduce it solely from genus. At p∈C each point of ν^(-1)(p) has a
neighbourhood mapped by the immersion as an embedded smooth surface
germ in the smooth threefold. These are the distinct local branches of
S. Two such branches through p meet in a curve, by the dimension
inequality in the threefold; their intersection lies in the conductor.
On each normalization sheet the conductor has just one smooth curve
germ, because R's components are disjoint and smooth. Hence all these
pairwise intersections on that sheet have the same reduced curve germ.
Since every pair of surface branches through p intersects, these image
curve germs all coincide. Their image is smooth, being the restriction
of an embedded sheet to its smooth conductor curve. A single embedded
sheet would make S smooth at p, so it produces no extra isolated
singular case. Therefore C is smooth at every point and is a disjoint
union of smooth compact curves.

The restriction ν|R:R→C is finite and has injective derivative at each
point, since dj is immersive. It is therefore unramified. For each
connected component mapping with degree d onto an image component,
Riemann–Hurwitz reads 0=d(2g(C_i)−2), so g(C_i)=1. Thus these are
exactly the asserted finite unramified elliptic-curve maps in the last
two alternatives. Euler additivity through the finite normalization
pushout gives e(S)=e(T)−e(R)+e(C)=0.

This geometric argument is local to the specified support and its ν.
It does not import the stronger global hypothesis that every support
of the fibration has normal crossings from P4.8.

## 8. Fresh computation and actual output reading

The independently written program
`code/S6_SERIES_PUBLISH_II_A_02WM_chern_character_cells.py` was completed
while the target proof remained closed. It adds Chern characters in
K-theory, checks the Noether elimination using exact degree-one
evaluation, lists the allowed integral rational values, and checks the
ruled and class-VII nonnegative equations. Its geometric certificates
give the coordinate-plane Jacobians with unit minors for the actual
cusp normalization, the hexagon cell complex and the dP6 blowdown
intersection basis. For the actual multiple smooth supports it computes
the moving rotations in the exact declared F_j period bases, the
determinants of I−A, and the canonical characters in the exact quadratic
coefficient rings. Their cover degrees are the supplied 9 and 8; their
local base powers are the supplied 3 and 4.

The run completed at 22:05:57.631674 UTC with exit code zero, program
SHA256 `b546e111d003d9e75185ed4d72c88f8f49e0315c4617fed0ee41b8c2d6626373`
and output SHA256
`d4d156b6967f2418ebccdcbd4c526e8fa5655cc1de91ea017610bc30be77ea30`.
The entire output, including every ruled sample and both finite-support
records, was printed and read before this derivation is frozen. The
general inequalities and maps have been proved above; samples do not
replace those proofs. No target historical program has yet been opened.

## 9. Receiving-map audit and disposition before release

The safe all-five-paper coded receiving scan and root's further literal
audit are bound separately. The front occurrence is an index row.
P4.18 uses the exact normalization map whose minors generate (u), and
only observes that its divisorial rank drop fails this proposition's
finite-rank hypothesis. That observation is unchanged. The two WU
applications have singular reduced supports by their statement and use
the elliptic-ruled alternative, whose full proof and conductor maps
above remain valid. Preamble links preserve the same owner/tag. No
unreleased receiving proof was opened for this audit.

The numerical identity is proved exactly as stated. The classification
is proved for singular reduced support, and the elliptic conductor and
zero-Euler conclusion are proved for the last two alternatives. The
two broader readings have actual source-bound counterexamples. These
are settled preproof findings, to be compared with every printed proof
step after the freeze; they are not an assertion that the original
statement was true without correction.

## Binding appendix

Exact input, primary-reading and computation hashes are appended by a
hash-only step before the freeze. The target proof remains unopened.

Binding recorded 2026-11-21T22:08:29.085197+00:00.

- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_02WM_statement_inputs.tex — SHA256 66775641c7276bf12f3f2dbca5aed2303319ea4a2d230a9d540d1e8a9e59152e.
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_02WM_cited_input_supplement.tex — SHA256 4c2ca22c3274f29cf1f04798f9d6bd3794bdce5bbc2f705a534128319417462f.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_WM_WS_safe_scope_01.json — SHA256 8070638508547ad0e9b1b5748f4562bd65c387c4161d55c8bc9f30b2c2fbc7c4.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_01BB_resolution_conductor_inputs.tex — SHA256 dc327be8fa7560c681198fed9fca6e88468ddbb830008c4975753e9e6220a4b0.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_02WM_construction_scope_inputs.json — SHA256 3ce326b9666d3e88a88aeb18f1e9186ad16aa940cb70482075b9a26607aae0d1.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_02WM_root_finite_support_inputs.json — SHA256 06685207ba73969637c15402ccb77a3ef4f998b8015a77af1d66b5f71826b448.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_02WM_scope_counterexample_preproof.md — SHA256 4235b850c8c66d6a1e4da7e7330e1f1858d2abbe87a4af924501c24db471c1bc.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_02WM_multiple_smooth_fibre_preproof.md — SHA256 49f8eaad419417468606e8233d6eea94dc6585671051242025769acd7b0d1bca.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_02WM_incoming_uses.json — SHA256 6f387f9d26fe6850bd3e3553cc9eb4be675d0e87e718f18af16ea805d15b1f69.
- records/S6_SERIES_PUBLISH_II_WM_root_receiving_scope.json — SHA256 487b8d860eccb788ea54888a83e927d6811b93c5b908da7e912d5fed0884b343.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_02WM_primary_scope.json — SHA256 ffe43323d8c04d31d4bbf2cec656f1ea3ee31a5b652ca903f0b83256072ba330.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_02WM_chern_character_cells_run.json — SHA256 b8c38773d72e5c344e943f65ab464391d4dfb70074807b60f526fab46495c780.
- code/S6_SERIES_PUBLISH_II_A_02WM_chern_character_cells.py — SHA256 b546e111d003d9e75185ed4d72c88f8f49e0315c4617fed0ee41b8c2d6626373.
- code/S6_SERIES_PUBLISH_II_A_02WM_chern_character_cells.out — SHA256 d4d156b6967f2418ebccdcbd4c526e8fa5655cc1de91ea017610bc30be77ea30.
