# Part E proof and audit record

AI-produced mathematical working record, GPT-6 Astra, 15 November 2026.
This records proved arguments and current attacks; it is not a completion
declaration for the whole prompt.

## Written statements

E1 proves Lead 7, including all multiple and singular fibres: effective divisors
are vertical by restricting their zero real Chern class to a Kähler regular
fibre and integrating. The exact field isomorphism is pullback along g;
meromorphic extension of the descended function uses the proper graph image.

E2 proves CDP20 Theorem 2.1 by the graph method of LRS. The graph is the
hypersurface av−bu=0 in Y×P1; its projection has Rπ_*O=O. Relative dimension
at most one and the ideal sequence give R1π_*O_T=0 for every closed subscheme
T. E17 now also supplies a direct proof of the printed assertion for the
specific exceptional divisor of a resolved pencil: its pulled-back Euler
sequence gives R2 sigma_*O(-tE)=0, hence R1 and R2 sigma_*O_tE=0. An
arbitrary exceptional divisor does not have this property, as the explicit
elliptic-curve blowup example shows. Full fibres are Cartier divisors in the original smooth Y;
the proof writes their multiplicity filtration and weighted component
induction. Neither the CDP monodromy count nor the cotangent-section step is
used. The top-degree base-change statement used here survives the failure of
CDP98 Lemma 1.5.

E3 proves b2>0 for a positive-dimensional Moishezon manifold and excludes a=2,
a=3 and nonholomorphic algebraic reduction on S6. The supplied CDP98 source
numbers the Moishezon result Lemma 1.4, not the prompt's Corollary 1.2.

E4 proves R1g_*O locally free for a proper map from a smooth manifold to a
curve with connected fibres. It rewrites the comb paper's theorem `raynaud`:
resolve the central divisor, perform cyclic base change, normalize, and use
the finite quotient of a polydisc local model. Reduced central fibres give
torsion-free R1; cyclic averaging and the Leray injection transfer this to
the original map. Possible gcd components are included in the normalization
comparison.

E5 proves the Leray sequence and smooth-fibre boundary. For
κ=u1⊗η1+u2⊗η2, cup product sends aη1+bη2 to
(bu1−au2)⊗η1∧η2, whose determinant is detκ. At singular fibres dg has
Jacobian-ideal image; the text gives the multiple, double and triple models.
The argument uses the locally free R1 source; it does not assume
R2g_*T_Y/C is locally free at a singular fibre.

E6 proves full extension over every analytic base germ, including nonreduced
germs, for C=P1 and rankκ=2 somewhere. Embedded regular tori lift through
every small Artin extension because Def(F) is smooth and
H1(TF)→H1(TY|F) is onto. Local Cartier equations show every map obstruction
restricts to zero on all rank-two regular fibres; Leray and torsion-freeness
then kill it. Relative Douady graph representability and analytic smoothness
produce a holomorphic local section. Stein factorization proves connectedness
using one persisting regular torus. Smooth general fibres remain tori, and
E1 gives a=1 when b2=0. Parent independently stress-tested this proof.

E7 checks the rank hypothesis for every named family from its rank-two cusp:
periods I,(log q)/(2πi)B+H(q), detB nonzero. Finite logarithmic transforms
and affine translation changes preserve that cusp. Comb smoothing fixes the
limiting Hodge plane in a transverse graph chart, so the logarithmic rank-two
period form persists. This answers the fibration-retention question in the
comb paper §10(1). E15 subsequently determines the full Kuranishi germ.

E8 computes the theta determinant exactly. For the stated theta
linearization, the general formula is
det Ωτ=−(μ′−i(θz/θ)/(2π))²−wp(μ)/(4π²).
The square-only formula requires wp(μ)=0. For the original input this holds
and det Ωτ=−g2²/(36π²g3). The root rank-one locus consists exactly of the
order-three point, with determinant order two. The order-four apparent pole
cancels the squared coordinate derivative; the logarithmic cusp matrix is
invertible. Arbitrary Engel sections do not come with the relation wp(P)=0.

E9 checks the used R1–R3 steps independently: E=G=O⊕O(−1), the invariant
class has no zero at the hexagon, log-tangent cohomology is (1,1,0,0), and
the normal quotient is K_dP6. The nonzero period KS and h1=1 kill the full
Kuranishi ideal, including nilpotents. This already occurs in DGKX version
one. Version two omits the statements; no reason for this is inferred.

E10 refutes the unrestricted fixed-positive-genus-target version, even with
rank-two KS. Two Hesse elliptic surfaces with explicitly disjoint critical
sets have smooth fibre product; pull it back by a varying genus-two curve
whose six branch values are explicit. Its nonzero base KS injects through
Leray, so no extension to the fixed central target exists. This does not
contradict E6, whose target is P1.

E11 computes h(T)=(1,1,1,0), with a smooth reduced miniversal scale line,
for coprime higher multiplicities (3k,4l) and original affine twists p≠0.
The explicit comparison P(3k,4l)→P(3,4) pulls Oold(1) to Onew(kl).
Finite invariant pushforward gives the needed acyclic root lines. The
h3 vanishing is the nonexistence of nonnegative solutions to
3k(a+2)+4l(b+2)=kl, not a sign guess about orbifold degree. The topology
used for χT=1 is the supplied S6 theorem for admissible higher multiplicities
and E19's independently checked rational-homology calculation for p≠0.
The latter is unnecessary for the p≠0 tangent-cohomology calculation:
all its horizontal root Leray lines are acyclic, so the exact tangent
sequence directly gives (1,1,1,0). It is used for the a=1 conclusion.

E12 refutes CDP98 Lemma 1.5 by an explicit Poincaré-bundle example on
A×A×P1 mapping to the second elliptic curve A, with bundle P⊠O(−2).
R0=R1=0, R2=C_0 of length one; global h=(0,0,1,0), generic-fibre
cohomology zero, central-fibre h=(0,1,1). The correct exact formula is
0→Rq/tRq→Hq(fibre)→Rq+1[t]→0. Top-degree base change remains true;
generic vanishing can leave torsion. Source occurrences of Lemma 1.5:
Proposition 2.5, Theorem 3.1, Lemma 5.4, Theorem 5.6, Proposition 5.7.

E13 computes h(T)=(1,2,2,0) and a smooth miniversal bidisc for the
two-parameter family. The third-kind connection
α=((y+b)/(x+μ)) dx/(2y), b²=1−μ³,
splits the Lie bundle and extends over the order-four cover. The inverse
pairing associated with the invariant type-(1,1) symplectic class identifies
G with E. At the two rank-one nodes the dual residue rows are
(1,−b/(e_i+μ)), whose determinant is nonzero. The two actual parameter KS
classes are independent by cross-ratio and elliptic-double-curve variation.
The special-fibre pairing comparison has been independently stress-tested.

## Computations run

`code/E_checks.py` and `.out`: exact symbolic boundary determinant, theta
heat-equation identity, original order-three constants, elliptic 3P
calculation, 489 coprime multiplicity pairs k,l≤40, Hesse critical/branch
sets, two-node residue determinant, finite-cover connection comparison, and
the exact cusp jet determinant used in the completed LR computation.

The suspected S6_01 inconsistency is absent. Its ν2²=9F²/512,
τ1=iπF²/2, b3=7i/(32π) give 24ν2²−3τ1b3=3F²/4 and joint coefficient
123ik/(64π), exactly. Independently x(3P)(0)=512/81.

`code/E_theta_numeric.py` and `.out`: 70-digit evaluations by implicit
theta differentiation and by independent Eisenstein divisor-sum Fourier
series. At τ=1.7i discrepancy rounds to zero; at τ=0.2+2i it is
4.53e−72. These numbers support but do not prove E8; the proof is symbolic.

## Primary sources and literature status

Horikawa II, publisher PDF: §4 (4.3)–(4.5), §6 Theorem 6.1 read. The
degree-two injectivity in that theorem is not silently assumed; E6 replaces
the source obstruction by the explicit smooth torus deformation functor.
Douady, Numdam PDF: §9 Theorems 1–2 and Appendix §2 Theorem 1 read.
Buchdahl 1999 primary PDF: Theorem 11 read. Catanese 2004 author PDF:
Theorem 2.1, Remark 4.1, Proposition 4.2, Theorem 4.4 read. Its boundary
is the one in E5; its smoothness criterion assumes H0(T_C⊗R1f_*O)=0,
whereas the present P1 examples have a nonzero such group. Its principal
bundle result permits the target to deform.

Both web engines searched on 15 November 2026 for combinations of torus
fibration, deformation, rank two, maximal rank, Kodaira–Spencer, Horikawa,
and separately arXiv 2610.10451, 2610.39102, 2610.00250. Recent searches
used a 60-day filter. Actual DGKX arXiv v2 record opened and matched against
the supplied source; independently indexed Viaclovsky records retrieved.
No theorem with E6's exact statement was located. This is a record of the
search, not a priority claim. BibTeX is in `records/E_references.bib`.

The LR source's lines 1733–1890 are in a commented-out block explicitly
labelled unchecked AI working notes. Their canonical and direct-image
claims are not used as proved results. The current LR argument computes
the relevant bundles and local model independently.

## Completed extensions and source audit

LR computation is now E14, Proved in the paper. The explicit elliptic
family y²=x³+tx+t+ε has LR central member and smooth total family. Critical
base Γ is ε=x²(3+2x), t=−3x². Its critical locus is an elliptic family over
Γ. G≅E extends over the isolated cuspidal point of the two-dimensional
(t,ε)-base by Hartogs on the matrix and its inverse, using local freeness
from the independently computed canonical bundle and fibre cohomology.
Restriction to the critical locus is exactly the holomorphic row
(1,−b/(1+x)); the target scalar is a unit by surjectivity onto the reduced
elliptic singular curve. Its central A=C[x]/x² map is
(a,d)↦a+d(−i+ix), determinant i. Thus Qcusp=J has h=(0,1,1), logT has
h=(1,1,0,0), and full tangent h=(1,2,2,0). The ε-KS has local Jacobian
class −1+x, whose x coefficient cannot arise from a global base vector
field. Together with the independent scale variation it proves a smooth
miniversal surface. This also supplies a concrete deformation from LR to
the configuration of the two-parameter construction.

The comb tangent/Kuranishi calculation is now E15, Proved. Both coarse
Lie and cohomology bundles have degree 2m−1 and nowhere-zero sections
coming from invariant real homology δ and cohomology γ. Their splittings
are therefore nonnegative for m>0. Multiplication of invariant sections
ρV⊗ρG→ρ(VG) has length-one cokernel at the order-three point, none at
the order-four point. This computes H0=8m+1 and H1=0 without knowledge
of the individual splitting summands. Analogous exact comparisons give
vertical cohomology (2m+1,8m+1,6m,0) and horizontal cohomology
(0,2m,2m,0). Cup-product injectivity gives log tangent
(2m+1,8m+1,6m,0), and the hexagonal normal quotient adds one to h2.
All nearby root-period sections form a smooth germ of dimension 8m+1.
Finite-equivariant periods and varying cusp gluing units admit the same
free proper fillings and affine attachment classes. The actual KS is
injective because three fixed critical values kill base automorphisms
and constant torus Dolbeault tensors cannot be exact. It is therefore
an isomorphism and kills the Kuranishi ideal. This completes the
specified family computations in E.3.

E16 (root-authored fragment `part_E_rank.tex`) computes the exact rank
divisor in all remaining families. On P(1,4), degree exhaustion yields
the two simple rank-one nodal zeros and the root order-four zero in the
two-parameter case; the LR central member has only that root order-four
zero. For a specified comb section the determinant is
y^2 P_sigma(x^4,y^3), where P_sigma has degree 4m and is computed by the
Gauss-Manin Wronskian of the actual Hodge section. All four entries test
rank zero exactly. The unspecified construction does not determine
numerical roots independently of its chosen section.

E17 refutes the printed generality of CDP98 Proposition 1.1 using the
square-zero space O_Z=O_P1 plus C_p and divisor q distinct from p.
The full twisting cohomology is h0=max(1-k,0)+1, h1=max(k-1,0).
It proves the exact replacement: the stable descending section space
consists of sections whose coherent support avoids the Cartier divisor.
No-embedded-component spaces with every component met therefore satisfy
the vanishing. All full fibres in E2 are Cohen-Macaulay and qualify.
The detailed CDP20 audit checks its only earlier dependencies, Corollary
1.3 and Proposition 1.1, and proves the specific exceptional-divisor
higher-image assertion through the pulled-back Euler sequence. No failed
cotangent or monodromy assertion is invoked. The LRS graph proof is
rewritten with full multiplicities; its adjunction sign misprint is corrected.

E18 refutes the universal local square theta identity by mu=1/2 on a
small disc about tau=i, with v=(i/pi)log(theta1(1/2,tau)/eta(tau))+i.
The proper torus family is explicitly an elliptic line-bundle quotient
with a contracting linearization. The index-six isogeny to its symmetric
period lattice is written out. The proposed square is zero, whereas
the determinant is -(theta3(i)^4+theta4(i)^4)/12, strictly negative.
All fibre O/T cohomology, all Rq O and Rq T, and the corresponding
total-space groups over the Stein disc are specified. This refutes the
advertised local identity; it is not labelled a compact S6 counterexample.
E8 supplies the exact corrected theta identity.

E19 extends the primary logarithmic-transformation homology calculation
to every original admissible affine twist. The exact lattice comparison
R=Q^-1 P_Engel has determinant -1 and sends positive affine translations
by -R. Choosing the zero cusp reference changes n0=r1, n1=r2-4l0;
the gluing determinant is 4n0+3n1=-p. The degree-one Mayer-Vietoris map
is injective because it is between free rank-nine groups with finite
cokernel; simple connectedness is not required. The remaining 4x4
matrix has Smith form (1,1,1,|p|). Thus H2=Z/|p|, and duality with
Euler number two gives H1,H2,H3,H4=Z/|p| and H5=0. This verifies b2=0
for every |p|>1 family before applying E1.

Additional programs run: `E_counterexamples.py` checks the square-zero
local algebra, all E17 twisting dimensions, E10 full O/obstruction/vertical
cohomology, and E18 by two independent methods at 70 digits (difference
2.2639198e-72). `E_topology.py` checks both exact marking intertwining
identities, the primitive exterior/edge lattices, all normal-circle norm
identities, the symbolic gluing determinant, and 336 admissible Smith forms.
`E_update_records.py` synchronizes all nineteen Part E metadata rows.

Fresh external metadata verification on 15 November 2026 opened the two
DGKX arXiv version records, the two-parameter record, and the LR record
(v2 revised 9 October). Direct opens for the comb and logarithmic records
returned DisabledError; independently retrieved arXiv-indexed search
results give their titles, authors, identifiers and dates (7 and 29 October).
Only the supplied primary source files are used for their mathematics.
Recent searches for the comb title with Kuranishi/smooth/8m+1 and for
the two-parameter and LR titles with tangent cohomology located no earlier
full E13-E15 computation. The paper records this and claims no priority.

## Critical-curve extensions completed after Part E

A.5.5 is proved in `sections/part_A6_critical_curves.tex`, with all equation
tags in the separate `A.J.*` namespace. For a reduced lci critical image
curve, the exact conormal bundle on its normalization has determinant
degree 2g−2+c, where c is the conductor length. The rank-one Hessian has
quotient line Q of nonpositive degree. Its radical cubic is constructed
by multiplying by d², with a=q_XX an actual coefficient in O_D and d,dh
in the conductor; the cancellation descends through the locally free
graded conormal module. The cubic poles are bounded by 2Ξ, forcing g=1
and c=0 in positive genus. This includes genuine meromorphic cubic jets;
the example with D=(z²−x³,w) has a radical cubic pole of order two.

The same statement now includes A3 tacnodes. Write G=d²f−aP², and divide
its cubic class by the monic normalized linear factor: [G]₃=ℓ C₂. Lift
d C₂ to H and form K=d²G−PH∈I⁴. The exact square identity gives
Δ=(a K_R−C₂,R²/4)/d⁴. Thus Δ has poles bounded by 4Ξ. Its corrected
bundle degree is −8g+8+2deg Q, so positive genus first gives g=1 and
deg Q=0. The Hessian is then nowhere zero, a is a unit already in O_D,
and h descends to O_D. Repeating with d=1 removes every pole and forces
c=0. The ordinary-triple case follows from the exact binary cubic
discriminant section M⁴(det N)⁻⁶. All three types are constant along the
resulting smooth elliptic curve. The fragment does not infer that an
arbitrary critical image curve is lci.

A.5.7 proves a separate local result without the image-lci assumption.
A Gorenstein surface whose normalization is smooth and whose conductor
is exactly twice a smooth divisor has a smooth conductor image wherever
the generic transversal is A2. The exact quotient Q=normalization/O_S
is the canonical module of the reduced conductor ring A. In the split
normalization ribbon B[ε]/ε², A is the graph of δ=u d/ds. The actual
A-linear map b+cε↦c−u b′ identifies Q with the fractional B-ideal B+uB.
Canonical-module biduality gives End_A(Q)=A, whereas the displayed
fractional ideal has endomorphism ring B. Hence A=B, and an explicit
coordinate change gives O_S=C{s,z²,z³}. The argument works branchwise
and excludes multiple branches of the local conductor image. Extra
vertical conductor and singular normalization are not eliminated by
this local statement.

`E_singular_curve.py` was run after both additions. It checks the local
cubic pole identity, the exact fourth-order square completion, the
quartic change-of-normal-coordinate invariant, its degree arithmetic,
the determinant weight of the binary cubic discriminant, and the
derivation-graph quotient's A-linearity. Metadata for A.5.5 and A.5.7 is
in `records/E_critical_results.csv`; the Part E record updater does not
overwrite this separate file.

Primary literature comparison: Kim, arXiv:2603.02347, was opened directly
on arXiv (abstract and 81-page PDF). Definition 2.0.1 assumes a flat
projective morphism with abelian-variety-torsor generic fibre; Theorem
1.0.1 also assumes minimality and delta-regularity. Its Section 3 uses an
extended translation-group action to make conductor images abelian
orbits. The required projective morphism and extended action have not
been constructed for the general CDP map, so that theorem has not been
used as a classification here. No categorical separation is asserted.
Niu–Ulrich's primary paper `A note on Mather–Jacobian multiplier ideals`
was also opened at the authors' Purdue PDF. Proposition 3.2 proves
the normalized Jacobian-minus-ramification divisor dominates the
conductor; Theorem 1.3 characterizes equality by the lci property. This
verifies favorable determinant positivity in the non-lci curve case,
but a matching symbolic-power jet-clearing estimate is not proved here.

The primary publisher PDF of Reid, `Nonnormal del Pezzo Surfaces`,
Publ. RIMS 30 (1994), 695–727, was opened and Sections 2–4 read;
J-STAGE independently verifies DOI 10.2977/prims/1195165581.
Sections 3.9 and 4.4–4.8 contain the rational-derivation description
of doubled conductors and the characteristic-zero obstruction to poles.
Their local single-branch argument recovers the cusp case of A.5.7.
Our proof gives the exact canonical-module endomorphism comparison;
it is recorded with this literature relationship and no novelty claim.
Section 4.6 also treats disjoint smooth doubles whose reductions map
birationally to the common image normalization. The present remaining
case may have vertical conductor, singular normalization or ramified
conductor covers; no extension over those defects is inferred from that
statement. The del Pezzo classification itself is not invoked here.

A.5.8 sharpens the remaining ruled-normalization instance. When every
exceptional curve of its resolution is vertical, the ruling descends
holomorphically to the normal surface by the equality π_*O=O, using
properness to keep a coordinate disc around each exceptional fibre.
The exact Leray arrows
0→R¹p̃_*O→R¹p_*O→p̃_*R¹π_*O→R²p̃_*O
have zero second and fourth terms: a blown-up P¹-bundle has R¹p_*O=0,
and p̃ has one-dimensional fibres. Thus the finite-support sheaf
R¹π_*O is zero. All normalization singularities in that remaining case
are rational, with h(O)=(1,g(B),0). This conclusion does not require
the conductor-image curve to be lci and does not remove vertical
conductor. Its full proof and metadata are in the same A6 fragment and
E_critical_results.csv.

A.5.10 handles the horizontal-cusp case when the normalization is already
a smooth minimal irrational ruled surface, including initially nonreduced
vertical conductor-image schemes. One preliminary attempt identified the
cusp kernel with the ruling tangent. That identification is not automatic:
the exact local map (u,s)↦(u²,u³,s+a u) has nonvanishing ruling derivative
at the cusp when a≠0. The written proof retains both possibilities.

Put ε=1 or 0 according to whether the ruling derivative vanishes along
the horizontal cusp section. Its actual saturated image is
L=T_{Z/B}(εC). Finiteness of normalization excludes vertical divisorial
zeros of that derivative. The induced base derivative in the reflexive
rank-two quotient has saturated image M=p*TB((1−ε)C+R). At a vertical
branch of multiplicity m, its normal differential order is m−1, while
the plane-branch conductor exponent is at least 2(m−1). Thus 2degR≤degV.
The two typed quotient sequences and c1=c2(h*TY)=0 give
L²+LM+M²=length(E**/E)+length(W). For ε1 this is
3(4−4g−v+r), forcing g1,v0. For ε0 it is
12−12g−2v+4r≤12−12g, forcing g1 and both lengths zero.
Then L is a subbundle; dh on TC gives an actual nonzero map
TC→L|C=N_C of Hom degree−v, forcing v0. A.5.7 yields a smooth elliptic
cusp image. This proof is in `sections/part_A6_cusp_chern.tex`, input by
the A6 fragment. It does not claim the same argument applies unchanged
to a nonminimal or singular normalization.

`E_cusp_chern.py` was run. It checks both local derivative orientations,
the common order of their minors, the two intersection polynomials,
the degree in the equality-case line morphism, and vertical branch
differentials for multiplicities 2 through 30. Metadata is in the
separate E_critical_results.csv. The root and A-agent were asked to
independently audit the full geometric argument.

The final A.5.10 statement has been strengthened to every smooth
irrational ruled normalization; minimality is a conclusion. Put D_p
for the divisorial common zero of dp, W=V+D_p, B_v=R−D_p. The actual
vertical tangent line is K_Z^-1 p*KB(D_p); the base derivative starts
from I_Ξ p*TB(−D_p) and extends to that line hull in E** by Hartogs.
Thus L=(2+ε)C+W+(2g−2)F and
M=(1−ε)C+B_v−(2g−2)F numerically. Since C is a section, D_p.C=0.
The previous Chern identities gain only
q_v=W²+WB_v+B_v²=(W+B_v/2)²+3B_v²/4≤0, by the negative semidefinite
vertical intersection form. Their equality cases force v=0 and q_v=0;
W effective with W²=W.C=0 is zero. Hence V=D_p=R=0. The remaining
identity K_Z+2C≡0 forbids a (-1)-curve by the integer equality
−1+2C.E=0, proving minimality. The extended intersection arithmetic was
added to E_cusp_chern.py and run successfully.

This result is now preserved as independent geometry. A-agent's A.5.12
provides the broader cohomological argument needed for B.3: local torsion
of ω_S, conductor duality and the nonconstant Picard differential force
every positive-genus conductor-image component to be smooth elliptic,
even with nonreduced conductor. I independently checked all of those
maps and inequalities and sent the verification to the root. Extending
the Chern proof over singular normalizations is therefore not needed
for that closure; no such extension is asserted here.

A.5.14 records the unconditional conductor arithmetic-genus bound for the
remaining C.2 sign problem. The initial canonical and duality arguments
of A.5.12 give h0(Q)≤1+e without Picard persistence, so every reduced
conductor component has p_a≤2. Positive normalization genus then gives
total delta≤1. The proof explicitly identifies each delta-one analytic
ring as a node or cusp and constructs its lci ideal in the actual smooth
threefold. A.5.5 therefore applies to every positive-genus coefficient-two
horizontal conductor image, even with constant ambient Picard image.
The still unresolved sign configurations are rational conductor images
and horizontal exceptional curves on normalization resolutions, as well
as the remaining non-Kähler normalization analysis. No Euler sign is
inferred merely from the genus bound.

A.5.15 supplies an exact local torus-degeneration obstruction, independently
of b2(Y). The actual full-fibre equation u(x,y,z)(x^a-y^b z^c)^m is changed
to h^m by the displayed weighted holomorphic coordinate map. For gcd(a,b,c)=1,
Nemethi's arbitrary-germ join theorem gives a wedge of spherical two-cells
and circles. Michel-Pichon-Weber's primary boundary computation gives
b1(boundary)=2(a-1)(gcd(b,c)-1), hence the rational Milnor intersection form
has rank a-1. All its H2 classes map to zero in the aspherical torus, whereas
the codimension-zero inclusion preserves intersection numbers. This is a
contradiction. It includes every ramified tacnode monomial x2-y4 z^(2r+1),
not only the simple branching model. Both primary PDFs were opened and
the exact theorem statements checked; no priority claim is made.
A general analytic ramification germ has not been reduced to this monomial
class, and the remaining ordinary-triple and singular-image cases are not
asserted to follow from it.

A.5.15 was strengthened from irreducible monomials to all exponents.
The explicit map from a cylinder collapsed at both ends to x^a-y^b z^c=1
is spherical. A parallel-arc isotopy makes its comparison cycle homologous;
the two endpoint links are parallel (c/d,-b/d) curves on Clifford tori,
with local linking -bc/d² at each end. Its square is therefore -2bc/d².
Weighted homotheties put the compact cycle in an actual local fibre.
The prior join/Seifert calculation remains an independent irreducible check.

A.5.17 extends the obstruction to every actual suspension x^a-g(y,z).
The proof retains the multiplicities of the distinct plane factors in a
deformation; on the fixed Milnor boundary these give the same product
transversal germs. Uniform boundary submersions on both faces and their
corner give an Ehresmann bundle over the complement of the proper
complex critical-value discriminant. The root audit sharpened the final
comparison: its central compact fibre lies directly in the actual torus
Y_(epsilon^m), so no extra identification with a standard Milnor fibre is
needed. Distinct plane factors give a transverse monomial intersection;
a singular single reduced factor has a generic nonzero Morse critical
value, giving an isolated A-type suspension. Both produce forbidden
spherical intersection. The reduced plane factor must therefore be
smooth. The exact algebraic morsification and weighted linking arithmetic
were checked in E_suspension.py. The root has reviewed the boundary
argument; zero-Hessian germs and non-suspension germs remain under attack.

A.5.17 now also excludes every isolated hypersurface singularity of the
reduced support when the actual map is u h^m. The exact root H=u^(1/m)h
preserves the isolated critical locus and gives f=H^m. A small linear
morsification has nonempty Morse critical locus by the positive local
degree of its gradient. On a fixed ball the boundary submersion persists
over the parameter/regular-value complement; the resulting Ehresmann
transport embeds a local Morse Milnor fibre directly in an actual global
torus fibre. Its real vanishing sphere has square −2, contradicting
asphericity. No suspension form of the initial isolated germ is needed.
Milnor's primary monograph, Lemma 6.1 and Appendix B, was opened and the
exact boundary and morsification assertions checked independently.

Two exact zero-Hessian models prevent a blanket extension of the local
obstruction. For f=v(y²+zv), every affine regular fibre has the explicit
biholomorphism (v,y)↦(v,y,(t−vy²)/v²) from C*×C. Its generic transversal
along v=y=0 is A3, but the Hessian vanishes at the origin; the conductor
double cover is locally unramified. For f=v(U²−Zv²), the map
(v,U)↦(v,U,U²/v²−t/v³) likewise identifies every affine regular fibre
with C*×C. Here the generic ordinary-triple conductor has a ramified
two-sheet part, parametrized by (u,v)↦(uv,v,u²), and a one-sheet plane
part. Thus ramification of a pair in the ordinary-triple case alone
does not provide the spherical-intersection contradiction. These are
local affine calculations, not examples of compact b2=0 fibrations.
The proposed unrestricted zero-Hessian or ramification exclusions are
not asserted. The narrower A3 branch-divisor inequalities are under
separate audit.

A.5.18 now proves exclusion of every lci rational image of a horizontal
tacnodal conductor on an irrational ruled resolution. The actual map
psi=phi ptilde:T→D descends after collapsing an embedded finite tree
in the actual singular curve D. Its restriction to D is that same
quotient, so the local torus group maps onto pi1(D). For rational D
this is a free group of rank beta=sum(branches−1), and metabelianity
forces beta≤1. Together with delta≤2 this gives at most three
normalization points above the singular image locus.

On Sigma=P1 the lci normal bundle has degree−2+2delta. The Hessian
quotient Q of degreeq carries the quadratic section with zero degree−2q;
the quartic invariant Delta has a holomorphic conductor-cleared section
of the square line L²(4Xi), of degree8+2q. The actual conductor cover
is obtained by adjoining sqrt(−Delta), so its branch divisor is the
odd part of that section's zero divisor. Away from singular D, A5.17
makes every branch point a Hessian zero. The two degree bounds force
the covering genus1 and q∈{−2,−1}.

At a smooth branch point with simple Delta zero, a must vanish simply
and the radical quartic coefficient is a unit. In exact coordinates,
X=x+(b/2a)y² removes the xy² term. Writing the result modulo X² as
y⁴C1+Xy³B1, the actual coordinate Y=yC1^(1/4)+XB1/(4C1^(3/4)) makes
f−Y⁴ divisible by X². The remaining quotient H has dz derivative a'(0)
nonzero, so Z=H gives exactly Y⁴+X²Z, excluded by A5.15. Thus every
smooth branch point costs at least three zeros of the cleared Delta.
For q−2 the degree4 is already too small. For q−1 the degree6 forces
precisely a node and a cusp on D, with all three singular preimages
branched and one smooth branch. If the Hessian coefficient is nonzero
on every branch at a singular image point, an actual diagonal entry
of its lci matrix is a unit in O_D; the square factor and monic division
therefore descend, and the A5.5 construction reruns with d=1. The cusp
then forces one Hessian zero, exhausting the degree2 together with
the smooth branch; both node branches have unit Hessian, which forces
at least five discriminant zeros at each, exceeding degree6.

The proof is in part_A6_tacnode_bounds.tex, with independent metadata.
E_tacnode_bounds.py checks the exact line-degree arithmetic, integer
cases, and the two coordinate divisibilities on eight polynomial
families. It was run successfully. The non-lci rational-image cases
and contracted-horizontal case remain outside A5.18. This is a proved
restriction, not an assertion of the remaining full Euler sign.

The lci restriction in A.5.18 has now been removed. The actual-D quotient
gives beta≤1 independently of lci. A complete local analytic classification
at delta≤2 then leaves only the space cusp C{t³,t⁴,t⁵} or the fibre product
of a plane cusp with a smooth transverse line. The proof constructs these
as actual ambient coordinate models, rather than only abstract rings.
For the space cusp, I^(2)=I²+(F) is proved through a finite C{x}-module:
the candidate quotient has generic rank9 and residue dimension9, hence
is x-torsion-free; three explicit identities give mF⊂I². A unit coefficient
of F would produce a rank-two Hessian with a noncancellable pole4, so the
generic rank-one hypothesis forces f∈I². The cusp-plus-line case has the
equally explicit I^(2)=I²+(z(y²−x³)), with its defect killed by m; its
quadratic determinant gives the same conclusion.

The actual normalized conormal image K⊂nu*OmegaY, and N=K*, have determinant
degree4 on P1 in both cases, by the displayed Jacobian-minus-tangent
correction6. The punctured affine chart for the space cusp is
(u,v,t)↦(t³,t⁴+v/(3t⁵),t⁵−u/t³+2v/(3t⁴)). Differentiation in u,v is
therefore an actual normal Taylor calculation, with t held fixed. For
f∈I² the mixed cubic poles are≤10, and quartic poles≤20. The quartic
invariant lies in a square line of degree−16+2q and has pole≤20, giving
branch degree≤4+2q. All smooth branch points are Hessian zeros, giving
the other bound≤−2q+1. Their sum≤5 contradicts twice the branch degree≥8.
For the cusp-plus-line charts, cubic/quartic poles are6/12 and2/4, so
the cleared quartic has degree2q≤0 and cannot define the required branched
double cover. Weighted-order substitution verifies the transition law
of the quartic invariant under the actual coordinate changes.

E_low_delta_tacnode.py ran successfully and saves exact generator
expansions, both symbolic Hessians, determinant corrections and the pole
bounds. A-agent independently supplied the space-cusp saturation and dual
lifts; root independently supplied the mF identities and requested the
affine-chart comparison now included. The strengthened A5.18 has been
sent to root for final independent audit. The ordinary-triple horizontal
case and contracted horizontal section remain the ruled tasks.

The root completed an independent audit of strengthened A5.18 and accepted
its lci/non-lci arguments. Its final geometry now identifies T as a smooth
minimal ruled surface over the elliptic curve and gives e(S)=0. The proof
first factors an arbitrary resolution through the minimal one, explicitly
descending the ruling and pushing forward the conductor. C2d supplies
C²=0 and disjointness from all other conductor and exceptional curves on
that minimal resolution. The exact blowdown coefficient d−1 then removes
all vertical conductor and all ruling blowups. Every remaining resolution
exceptional curve would lie in a square-zero fibre of the minimal bundle,
which is impossible. Normalization additivity gives e(S)=e(T)−e(C)+e(D)=0.
Keeping the factorization is necessary: an arbitrary chosen resolution
can contain artificial blowups along C, even though T itself is minimal.

A.5.19 proves that every ordinary-triple conductor image has arithmetic
genus at most one and is lci. All three non-lci delta-two rings are
treated: the space cusp, cusp plus line, and spatial triple axes. Their
symbolic cubes are exactly I³+FI for the respective symbolic-square
generators. The 345 identity is proved by generic/residue DVR lengths18;
the other two identities are proved directly. The initial cubic has
poles of total order at most3 in the actual conormal charts, so its
discriminant pole correction≤12 cannot overcome the degree−24 of its
line. The lci delta-two case has ordinary discriminant degree−12.

For a delta-one rational image, the lci cubic discriminant is nowhere
zero. Its projective tangent-root scheme is therefore finite etale of
degree3 over P1. The generic normalization branches have exactly the
same function-field algebra; integral closure gives an actual
identification of the finite normal covers. Every component is thus P1
of degree1. A positive-genus horizontal conductor cannot occur in that
case. The remaining irrational-ruled ordinary-triple branch has smooth
rational image and horizontal degree2 or3. Elliptic image has constant
type and the same exact minimality/Euler-zero conclusion as A5.18.

The local nodal-image example f=x(yz)(x−yz) is retained with explicit
inverse biholomorphisms between its regular affine fibre and
{xv(x−v)=t}×C*. It has an extra ordinary-double critical line. Smoothing
yz would alter that line's boundary type, so it cannot be used in the
boundary comparison of A5.17. No unjustified local exclusion of the
delta-one image is made. E_triple_images.py/out contains exact symbolic
cube saturations, cubic pole bounds, the discriminant degrees and the
product fibre map; all checks passed. A-agent independently reproduced
the three symbolic saturations in A_low_delta_cusp.py/out.

A.5.20 completes the noncontracted horizontal-cusp case even when the
normalization was initially singular. The one generic branch gives
degree1 C→Dnu and hence positive image genus. A5.14/A5.5 give smooth
elliptic D of constant cusp type without Picard persistence. C2d gives
normal degree0; the exact minimal-resolution and ruling-blowdown maps
already used in A5.18 then identify T as smooth minimal elliptic ruled
with conductor2C and e(S)=0. The only remaining noncontracted
irrational-ruled coefficient-two case is the smooth rational D4 image.

A.5.21 extends the spherical-cycle obstruction to reduced homogeneous
binary products P(x,yz), with P(1,0) nonzero. The projective map from
{P(x,v)=1} to P1 minus the d simple roots is a connected degree-d cover,
because a loop about one root acts by a full d-cycle. The d simple zeros
of v provide an arc sphere whose two endpoint links both have slope(1,−1)
and linking−1. Positive weighted homothety and the exact weighted unit
coordinate map put its square−2 class into an actual torus fibre.

The same statement now includes variable coefficients in the specified
ideal (x,yz)^d. The exact analytic family
h_s=sum a_i(s²x,sy,sz)x^(d−i)(yz)^i compares the original germ with its
constant initial form. Its distinct root functions give d smooth factors
with every pair ideal exactly(x,yz), so the boundary critical links are
unchanged. The proof supplies quantitative boundary estimates:
normal gradient>=c||normal||^(d−1), curve derivative<=C||normal||^d.
Solving one real curve coordinate for the boundary shows the required
boundary submersion survives uniformly. Proper discriminant-complement
transport then carries the explicit sphere to the original germ through
the actual weighted scaling map. No arbitrary coefficient replacement
or unverified boundary equivalence is used. E_binary_products.py/out
checks homogeneity, simple zeros, square and exact family identity.

The root independently accepted A5.19 and A5.20. The latter's normal-line
paragraph was corrected to refer first to C_T in the smooth part of T;
after factorization through the minimal resolution, C_min has that same
normal line and square0. This avoids attributing the degree-zero normal
line to an arbitrary artificially blown-up section.


The root independently audited A5.21, including the variable-coefficient
compact-boundary argument, and accepted it. Two exact common-cubic-zero
models are now appended. The germ xy[z(x-y)+xy] has an actual chart
v=x-y, Z=y(y+v)z+y²(2y+v), in which h=vZ+y⁴ on xy!=0; matching circles
chosen with |v|<|y|/2 give a sphere of square -2 that shrinks by ordinary
homothety. By contrast xz(y²-x²z), after u=y/x, has regular fibre a finite
etale triple cover of E={z(u²-z)!=0}. E has the explicit double cover
C*×(C minus {±1}), (s,v)↦(s²,sv), so the affine fibre is aspherical.
Its normalization conductor supports are SNC pairs, with coefficients
(2,2), (2,1), and (1,2). This is not a compact example.

The earlier suggestion that a degree-one vertical conductor component
over the rational D4 image must directly meet the horizontal section was
corrected: a connected positive-boundary path in the ruling fibre is
all that is forced. Exceptional subchains can contract and strict
intermediate curves can create further conductor images. No conclusion
was based on an unproved direct intersection.

C.2.D4.2 is now proved in part_C2_cubic_double.tex and sent for independent
root/A-agent audit. It excludes every positive-genus degree-two branch
cover over a smooth rational ordinary-triple image. It uses the root's
actual compact normal-cone embedding and its exact compact intersection
comparison. The finite cyclic cover is identified by evaluation w(v)=1
on a tautological line. Relative duality gives R1 p_*O(-2xi)=det N, hence
H1 of the cyclic structure algebra vanishes for every splitting of N.
All boundary class relations are counted, including disconnected branch
divisors; b1(U)=b1(X)+epsilon and the pairing formula retains b0(boundary).

The common cubic divisor has degree at most2. In the balanced normal
bundle this follows from the bidegree and genus of the residual quadratic
root curve; in nonnegative splitting it follows from the nonzero leading
quadratic coefficient of degree2-a-v. With no common zero, total branch
delta is5-g<=4; with one simple common zero it is6-g<=5. The verified
C.2.RAT.6 table gives total local pg<=1 and exceptional b1<=2, leading
to b1(U)<=3 and strictly positive intersection rank in both cases.

Common degree2 forces N=O+O(-2), and the global bundle square completion
gives P=a y(x²-b y²), a in H0O2, b in H0O4. Positive genus makes the
quadratic root curve smooth elliptic and b have four simple zeros; the
root section is disjoint from it. Two distinct common zeros yield only
A1/A3 plane branch singularities, so the cyclic resolution has q=0.
For a double common zero, the normalized cyclic algebra is exactly
O+L^-1+L^-2(F). Its H1 vanishes because R1p_*L^-2(F)=O(-1). At a
weight-(2,1) contact-k pair s=0 and s-u^k=0, repeated point blowups
subtract each new exceptional divisor from the root line and from the
strict weight-two divisor. Both nontrivial eigensheaves gain precisely
O(E), whose R1 vanishes. After k steps the branch is smooth and disjoint,
so this proves rationality of the normalized cyclic singularity for all
k>=1, with every finite and birational Leray arrow specified. The final
intersection ranks are2nu-4 for two common points and2nu for one double
common point, while b1(U) is2 or1 respectively. E_cubic_double.py/out
retains exact arithmetic and the normalized blowup coordinate identities.

Together with C.2.D4.1 and A5.19 this closes every noncontracted
coefficient-two ordinary-triple case on an irrational ruled resolution:
the image is smooth elliptic, the cover is unramified of degree3, the
normalization is smooth minimal elliptic ruled, and e(S)=0.

Root independently read and accepted the full C.2.D4.2 proof, including the splitting bounds, disconnected-boundary homology, all common-zero cases, and exact R1=0 normalized-cover ladder. A subsequent notation correction writes p*A, rather than A itself, when naming fibre divisors on P(N); no algebra changed. I independently audited the parent C.2.D4.3 rational triple-cover Euler proof and accepted all cases, including its canonical-duality refinement q=max(P-1,0).

## Final Euler comparison audits and reducible-fibre investigation

I independently audited C.2.UN.1--2. The relative Poincare-duality rank
identity, skew middle intersection form, Wang dimensions, and even rank
of G-I for G in SO(3,3) prove evenness of the Euler number of every
torus-degeneration support. The successive genus-two curve blowups and
point blowups give exactly e=2(m-k), with the stated Betti additions.
At each curve step the retained horizontal surface maps isomorphically
to its predecessor because its blowup centre is Cartier; the differential
of the original base map supplies the required normal splitting.

I independently audited the complete local-system, support-duality,
normalization, and numerical half of C.2.MH.2. The global transgression
section is first turned into an actual class on a small tube by the
integral Leray edge isomorphism over a disc. A sufficiently large prime
gives an augmentation local system whose characters are all nontrivial
on the nearby torus. The torus Koszul contraction and punctured-disc
Leray sequence give acyclicity. Compact support/Alexander duality uses
ordinary homology on S because S is compact. The exceptional-curve
Gysin map with fibrewise constant coefficients is onto by the negative
definite matrix. These are the actual maps proving e(S)=2 for rational
normalization and e(S)=2-2g for a ruled normalization. The independent
MH1 audits were carried out by the root and A-agent and accepted.

The proposed further strengthening that every reducible support has
Euler number zero has not been established by the Picard argument.
The precise extra step would be a tube class alpha in H1(U,Z) whose
restriction to every normalized component is nonzero. The nonconstant
complex restriction in INT.1 does not itself produce that real class.
This logical issue has the following explicit compact SNC test, which
is not asserted to satisfy the torus-degeneration or global CDP hypotheses.

Take the scalar Hopf surface H=(C2 minus {0})/<q Id>, q=exp(-2pi),
and its axis elliptic curve E=C/(Z+iZ). In coordinates u=z1/z2 and
w=[z2], a neighbourhood of E is E times a disc. Glue two copies of H
along E by z maps to i z. The quotient carries the analytic structure
O_H1 fiber-product_{O_E} O_H2; its local chart is C{z,x,y}/(xy), so
the two normalization maps are specified. The topological normalization
sequence maps H1(H1,R)+H1(H2,R) to H1(E,R) by
(u,v) maps to u dy-v dx. This is an isomorphism and gives H1(S,R)=0.
The coherent normalization sequence instead maps C2 onto C with two
nonzero coefficients, hence H1(S,O)=C, restricting nontrivially to both
Hopf normalizations. Thus the complex Picard restrictions cannot be
converted into local integral restrictions without using further
torus-smoothing information. The root was advised to retain the exact
INT.3 equality criterion rather than infer automatic zero from INT.1.

Primary literature checked during this final comparison: Doi--Yotsutani,
arXiv:2203.09304v2, Theorem 1.3 and Remark 1.4, constructs differential-
geometric smoothings of SNC compact complex surfaces with trivial
canonical bundle. The theorem explicitly provides a smooth real total
space and a smooth map; the comparison paragraphs do not identify it
with a holomorphic degeneration. Kamenova's Degenerations of
2-dimensional tori assumes a semistable Kahler degeneration with trivial
total canonical bundle. These are related proved constructions, but no
unproved map from the present arbitrary nonordinary holomorphic tubes
to either setting has been used.

C.2.UN.4 is now written in part_C2_vertical_refinements.tex. Every fixed
proper holomorphic torus filling admits, by actual smooth vertical
blowups, every even reduced-fibre Euler number. The universal comparison
is e(pi^-1 S)-e(S)=(r-1)e(Z) for a smooth centre Z of ambient codimension
r; it follows from the exact decomposition off Z and the projective
normal bundle over Z, so it retains singular support and multiplicities.
The -2 operation blows up a fresh smooth point (+2) and then a Fermat
plane quartic of genus3 in the exceptional P2 (-4). Its four transverse
intersections with the old component have exact chart t=(uvw)^m after
the curve blowup. The three components all retain multiplicity m.
The integral blowup map is explicitly pullback plus exceptional Gysin
classes, giving increments (2,6,2) in degrees (2,3,4) for this operation.
UN1 parity then supplies all targets from every initial filling. After
reaching zero, one +2 operation and one -2 operation add three central
components while preserving Euler zero; this gives arbitrarily many
components above each filling. The exact algebra and arithmetic checks
are retained in E_vertical_refinements.py/out. No comparison between
unrelated birational fillings is asserted: cofinality is stated using
the precise smooth vertical blowdown domination maps.

Root and A-agent independently read and accepted UN4, including all
inverse-image Euler comparisons, arbitrary multiplicities, triple
charts, and the integral pullback-plus-Gysin cohomology map. I then
independently accepted the strengthened UN3 O(nR) construction:
H1(P_n)=Z^3+Z/n and H1(Q_n)=Z+Z/n, with exact fundamental-group
presentations and degree-one strict-component comparisons after finite
base change. Those torsion invariants prove the asserted pairwise
non-bimeromorphism.

UN6 supplies an additional essential type, with a complete direct
construction in part_C2_elliptic_roots.tex. For V=Bl(E times disc),
L=O(R) and its canonical section sigma, the actual smooth hypersurface
W_m={sigma=a^m ell} in L^times times C has the free proper action
(ell,a) maps to(q^m ell,q^-1 a). Its quotient is locally
(Delta_z times E_q times Delta_y)/mu_m, with the free action
(z,[w],y) maps to(zeta z,[zeta w],y). The exact map is x=z^m,
b=w^m,a=z/w; it proves properness and smoothness without invoking
root-stack existence. The off-R isomorphism is
(v,[c]) maps to[(v,sigma(v)c^m,c^-1)], so the punctured product is
fixed for every m.

The central full fibre is P_m+mQ_m. Q_m is primary Hopf with multiplier
q^m. The surface P_m has elliptic base E and one multiple fibre mJ.
The global canonical form is p*omega_E wedge dlog(w); in the cyclic
chart its coefficient is m z^(m-1), proving K_Pm=(m-1)J exactly.
Every section of O(kJ) descends along compact elliptic fibres, and its
Laurent series has only powers divisible by m. Consequently its
pushforward is O_E(floor(k/m)[0]); the exact plurigenus slope is
1-1/m, positive and different for every m>=2. This gives kappa=1
and pairwise birational distinction. A smooth norm-level decomposition
P_m=M_m times S1 and the solid-torus gluing meridian m delta+h give
H1(P_m)=Z^3, hence the surface is non-Kahler. Both components contain
no rational curves and therefore survive bimeromorphic comparisons by
the inverse-map resolution of UN3. At a generic point of P_m the
base map is a submersion, so every finite base change retains a
degree-one component birational to P_m. No assertion about the other
base-changed components is needed. The model compactifies by replacing
the base disc by P1. E_elliptic_roots.py/out verifies the exact quotient,
canonical, homology, and plurigenus calculations.

This construction belongs to the established generalized logarithmic-
transformation setting, and no priority claim is made. I opened and
read Fujimoto, Logarithmic Transformations on Elliptic Fiber Spaces II,
Hokkaido University Technical Report Series in Mathematics 16 (1990),
pp.81--102, in https://eprints.lib.hokudai.ac.jp/repo/huscap/all/5450/16.pdf.
Definition1.1 gives the exact logarithmic cocycle surgery; Remark1.4
explicitly cites Ueno, On non-Kahler degenerations of complex tori,
Recent Trends in Mathematics, Teubner-Texte zur Mathematik 50 (1983).
The latter source is being retrieved for its precise scope. The new
UN6 section does not infer a universal exhaustion theorem from either
source and supplies its own complete quotient construction.

UN6 was independently accepted by root and A-agent, including proper
quotient charts, canonical gluing, the norm-level splitting and the
integral meridian computation. The literature search then located the
primary Fujimoto 1988 article, J. Math. Kyoto Univ.28(1),91--110,
https://scispace.com/pdf/logarithmic-transformations-on-elliptic-fiber-spaces-1uinrvp8jj.pdf.
Its Example3.4(1), printedp99, explicitly gives an abelian-surface
degeneration with a kappa1 component; this is now cited as prior
occurrence. Its Theorem2.8 and Corollary2.10, printedpp96--97, assert
that a multiple-fibre multiplicity m along a compact smooth base curve
must divide its self-intersection and forbid a multiple line in P2.
The article's exact definition on pp91--92 imposes only properness,
smooth total and base, connected fibres, and smooth elliptic general
fibre. No Kahler or multisection hypothesis appears.

The apparent conflict with UN6 is resolved by an explicit independent
counterexample, now fully written in C.ER.17--18: the diagonal Hopf
threefold H_m=(C3 minus0)/<(a,b,c)->(qa,q^m b,q^m c)> maps properly
to P2 by [a,b,c]->[a^m:b:c]. Off the line X0 its fibre has parameter
a and quotient multiplier q; on the line its parameter has multiplier
q^m. Every fibre is connected elliptic, the line pullback has exact
multiplicity m, its self-intersection is1, and the complement P2 minus
line is simply connected. A-agent independently found and verified
the same example. Thus the printed assertion has an actual
counterexample, not just an incomplete proof. The precise failed step
is also recorded: the alleged cyclic cover xi^m=s_E^m splits globally
into graphs xi=zeta s_E and normalizes to m disjoint copies; it does
not produce the claimed irreducible base cover. The Hopf map is
exactly the W_m construction for O_P2(1), via the unique vector v with
ell(v)=1. The script now verifies its projective equivariance and
both fibre parametrizations. The citation is in E_references.bib as
Fujimoto1988Log. No other statements of that article are invalidated
by this audit, and UN6 uses its own construction throughout.

UN8 was independently audited in full: the diagonal and CM graph
give exactly the two stated global Weil-ideal blowups, all three
charts are smooth and glue with the two-P1 exceptional chain, and
the support quotient S/E is exactly S2 times S2. The integral LES,
fundamental-group quotient, canonical Hartogs extension, monodromy
meridian killing, generic Picard restriction and MW rank8 all pass.
Root added the requested explicit sextic-root generic-elliptic-curve
comparison underlying NS rank4. The primary Rossi2017 source was
opened independently: arXiv1211.6329v3, Proposition4 and Remark5,
which gives the same Namikawa construction and Hodge numbers21,3.

UN9 and UN10 were independently audited. The rank-one Hessian
perturbation with simple determinant zero gives the exact pinch
normal form, and the parameter Morse charts retain a vector along
the critical curve tangent to all perturbed levels and transverse
to the fixed boundary. This justifies both Ehresmann transports.
UN10's unrestricted canonical evaluation, torsion twists and
chi0 reproduce all inputs to the precise CR2 duality argument;
the node/cusp conclusion excludes contracted genus2. No remaining
ambient Picard or Betti input was found. The same replacement
audit passed for all noncontracted irrational A2/A3/D4 arguments.

UN11's complete19-row companion-matrix and exterior-power code was
executed independently and passed. The direct SNC nearby-cycle
proof of quasi-unipotence and alternating trace needs no Kahler
ambient. The minimum-multiplicity resolution comparison was checked;
D incorporated the clarification that a centre not generically
contained in an existing exceptional divisor is still over an
unresolved original singular point and has order at least2m0.
The strong consequence m>1 implies e(S_reg)=0 is correct. UN12's
classVII complement isomorphism and exact zero-Euler curve patterns
were independently accepted, as was its ruled degree table2,1,2,3.

UN13 is written in part_C2_kummer_filling.tex, with script/output
E_kummer_filling.py/out. It starts from (A times P1_s)/(-1,-s),
t=s2, and blows up its32 isolated1/2(1,1,1) quotient points.
The exact invariant chart is (a,b,s)=(r,ru,rv), R=r2;
the six invariant quadrics become R(1,u,v,u2,uv,v2), and
t=R v2. Thus the total space is smooth, exceptionalP2 has
normalO(-2), and each special divisor is2P+sum16E_i,
P the KummerK3 and P capE_i a line of square-2 onP.
Its reduced Euler is24+48-32=40. Both special supports
become SNC Euler0 by20 UN4 negative-two operations each,
always centred away fromP. Each has57 components and an
unchanged minimal K3 component. The finite quotient trace gives
rational Betti(1,0,7,0,7,0,1), and exact exceptional Gysin
restrictions -2h,-2h2 add32 classes in degrees2and4.
Thus W has Betti(1,0,39,0,39,0,1). The40 balancing blocks
give Y Betti(1,0,119,240,119,0,1), Euler0. Formal-functions
vanishing from O_P2(2r) proves coherent cohomology(1,0,1,0)
for both. Non-uniruledness follows from the K3 two-form and
UN3 inverse-map resolution preserves its divisor birationally.
Quadratic base change is separately identified: the finite
map (a,s)->([a,s],s) is the normalization of the original
base change, so that normalization is exactly A times P1.
No persistence of K3 type under that change is asserted.
Classical Kummer construction was read directly in Huybrechts,
author-hosted K3Global.pdf Chapter1 Example1.3(iii),pp8--9;
the bibliography key HuybrechtsK3Draft was added. No priority
claim is made for this quotient construction.

UN13 now also records the complete rational and coherent cohomology of
the reduced special supports. Mayer--Vietoris for the Kummer surface
and sixteen planes gives Betti ranks (1,0,22,0,17) and coherent
dimensions (1,0,1). For every balancing blowup the actual quotient
homeomorphism S'/E = S/C identifies relative cohomology; restricting
the ambient exceptional Gysin classes splits the positive
projective-bundle summands with self-intersection sign minus xi.
This gives the same additive blowup summands on the support as on
the ambient space, including the quartic's four boundary crossings.
Twenty blocks give support ranks (1,0,62,120,57). The chosen centres
have generic reduced-support order one, so sigma^*S_red=S'_red;
projection formula for the Cartier-divisor sequence gives
R sigma_* O_S'=O_S. Hence the coherent support dimensions remain
(1,0,1). The exact arithmetic script was rerun and passed.

D's UN11 geometric realization upgrade was independently audited:
all fifteen elliptic-product rows, the genus-two Jacobian Phi5/Phi10
rows, the explicit Gaussian matrices Phi8/Phi12, and the actual
quotient monodromy g^{-1} give all nineteen characteristic rows.
The resolution and positive/negative-two balancing preserve the
punctured family; the recorded point/quartic charts preserve SNC.
No gap was found in this realization argument.

The unrestricted general-type component attack first gave an exact
canonical-ratio constraint. Write the full fibre as sum m_i S_i and
the divisor of the relative canonical evaluation as sum a_i S_i.
For the minimal normalization resolution h_i:Z_i->S_i, let D_i be
the intrinsic effective resolution conductor and E_ij=h_i^*S_j
for j different from i. Adjunction and the principal full fibre give
m_i(K_Zi+D_i)=sum_j (m_i a_j-m_j(a_i+1))E_ij. This is an actual
line-bundle identity, obtained by raising adjunction to the m_i-th
power and cancelling h_i^*O(S_i) via the full-fibre identity.
After the minimal-model blowdown, a general-type component forces
the positive part supported on interfaces with
a_j/m_j>(a_i+1)/m_i to be big: it equals m_i K_min plus an
effective divisor. Such interfaces cannot form a negative-definite
configuration or only fibres of a map. A curve-free minimal model
would instead have K_min^{m_i}=O, excluding curve-free class VII.
I did not prove propagation of the big ascending boundary through
the neighboring ruled components. No exhaustion was inferred from
this constraint. Kollár's primary arXiv2102.02614, Conjecture4,
was read directly; the 2026v2 primary arXiv2506.12670 was checked
and its specialization results retain local Moishezon assumptions.

D's subsequent semicomplete-field route removes the general-type
obstruction directly. I independently opened Guillot2019
arXiv1603.02288v2 Main Theorem and the author-hosted 2024 survey
guillot-singularities.pdf, Theorem3.3, and checked the exact
rescaling and closure applications. A targeted root cover makes
the chosen component multiplicity one and maps it generically
finitely to the original component; Jacobian adjunction on a graph
resolution preserves general type. On the new smooth family,
f_*T_rel is coherent torsion-free rank2, hence free over the disc.
For a nonzero global relative field v, dividing by the base
coordinate to its generic order along the chosen component gives
a generically nonzero meromorphic field w. On each nearby compact
torus its scalar is constant, so w is complete. Theorem3.3 applies
on the total holomorphic locus, then restriction to the invariant
component and a second application on its resolved holomorphic
locus give a semicomplete meromorphic surface field. This second
application also covers cancellation of ambient poles on the
component. Dense solutions are covered by Guillot2019. When all
leaves are algebraic, the uncountable invariant-curve family in a
countable Chow space gives a fibration after the incidence graph
resolution. Its general fibre has a nonzero semicomplete
meromorphic vector field. A pole of order p yields a time-form
primitive of order p+1 and a nonclosed path of zero time, which
contradicts semicompleteness. The fibre field is therefore
holomorphic and its genus is at most one, excluding general type.
These checks were sent to root and D for the UN15 proof.

Root assigned the independent canonical argument C.2.UN.17. It is
now written in part_C2_canonical_components.tex, C.CA.1--11, and
recorded with code E_canonical_support.py/out. The actual canonical
section, full-fibre normal-line cancellation, minimal-resolution
conductor and pushforward of a meromorphic pluricanonical section
give K_min^m=O(B) with B supported on finitely many actual curves.
For a positive-b2 minimal class VII model, write its canonical real
class in those curves. Their matrix is negative semidefinite and
K has nonnegative intersection with every curve by minimal
adjunction. Negative-definite connected blocks have nonpositive
canonical coefficients. In a singular block, the absolute value of
a nonzero kernel vector is a kernel vector and is strictly positive
by connectedness. Pairing with K-intersections makes all of them
zero, and the canonical contribution of that block is a zero class
by ambient negative definiteness. Negating the other coefficients
therefore constructs an effective rational anticanonical divisor.
Clearing denominators and integral torsion gives a topologically
trivial twist; H1(C)->H1(O) is an isomorphism and the exponential
diagram realizes that twist by a complex-flat character. The
primary Dloussky2006 Theorem0.2 now gives GSS. For b2=0, nonempty
curve support and Dloussky--Teleman2012 Remark2.7 give Hopf; a
curve-free model would have a trivial positive canonical power.
Both sources were reopened and the precise hypotheses checked.
The construction gives a flat twist, not necessarily a torsion
twist, and does not assert occurrence of every allowed GSS model.

Root proposed the opposite-sign logarithmic construction, assigned
C.2.UN.18. It is written in part_C2_projective_elliptic.tex,
C.PE.1--21, with exact code/output E_projective_elliptic.py/out.
On Bl_2(E times disc), take D=R_+-R_-, L=O(D) and its canonical
meromorphic section. The two actual equations are sigma=a^m ell
and sigma^-1=(a')^m ell', glued by a'=a^-1, ell'=ell^-1.
Their q-actions have opposite exponents and give the same proper
free local finite-quotient charts as UN6. Full central fibre is
P_m+mQ_++mQ_-, with two disjoint primary Hopf components.
The difference p_+-p_- is chosen torsion. A torsion mth-root N
of O_E(p_+-p_-) gives the connected genus-m cyclic curve y^m=sigma.
After an etale base cover killing N, the exact product map
(z,[u])->[ell=u^m n(z)^m,a=y0(z)/u] is finite and etale:
at the two branch types the Jacobians are m*u^(m-2) and
-m*u^(-m). Thus P_m is projective and has no rational curves.
The global form omega_E wedge dlog ell has zero divisor
(m-1)(J_++J_-), giving plurigenera degree
2 floor(r(m-1)/m), and different m give different canonical
growth slopes. The multiplicity-one component persists with
degree one after every finite base change.

UN18 includes all ambient/support/component cohomology. The two
Seifert meridians are m delta_++h and m delta_--h, so H1(P)=Z4.
For the compact total space the norm slice is M5 with exterior
Q times S1, Q=(E times P1) minus two balls. Each filling is
S3 times D2, with actual attachments
(w,e^itheta)->(e^(imtheta)w,e^(+/-itheta)).
Every relevant integral MV image has primitive Smith entries1;
M5 ranks are (1,2,5,5,2,1), and Y=M5 times S1 has free ranks
(1,3,7,10,7,3,1). The support MV maps have primitive ranks3
on H1 and1 on H2, giving free ranks (1,3,6,7,3).
Coherent local finite-quotient direct images are O,R1O=O;
the constant deck cocycle provides the global R1 frame.
Thus hO(Y)=(1,2,1,0), hO(P)=hO(S)=(1,2,1), and Hopf
hO=(1,1,0). All exact Jacobian, relation and Smith checks passed.

UN19 was independently audited in full after UN18 was written.
The stabilizer of the actual cyclic component cover gives the
proper quotient comparison to the original normalization. Its
equivariant minimal model is torus or Hopf by UN16. Torus
quotients have even b1 after resolving cyclic quotient chains,
so cannot have class VII normalization. On a Hopf surface the
derivative-determinant character of its deck group is nonzero
and preserved by conjugation, proving identity on H1 for every
automorphism. Poincare duality gives Lefschetz number0; fixed
curves are elliptic by adjunction, so finite-order automorphisms
have no isolated fixed points. Cyclic stabilizers are therefore
pseudoreflections and their quotient is smooth. Invariant
cohomology gives b1=1,b2=0, Jacobian pullback kills all
plurigenera, and the actual image of a Hopf elliptic curve
gives the Hopf case of DT Remark2.7. This checks the descent
to the original minimal model, not just the covering model.
UN17 now explicitly records that UN19 excludes its positive-b2
NAC alternative; the canonical argument remains independently
proved and makes no occurrence claim for that alternative.

## C.2.UN.21: secondary Kodaira component, 2026-11-15 19:12 UTC

The complete construction is in part_C2_secondary_kodaira.tex.
Start with the n=1 compact UN3 model over Bl(E x P1) and use
the canonical order-two lift of (p,t)->(-p,-t) on O(R).
Multiplication by q^(1/2) makes the induced involution free:
at any fixed base point its line eigenvalue is +/-1, neither
of which times q^(1/2) lies in q^Z. The quotient map is finite
etale, and its map T=t² has exact full special fibres
2P+2Q and 2B. Here P is secondary Kodaira with canonical
line of exact order2, Q is the primary Hopf quotient by
-q^(1/2), and B is bielliptic. Both reduced supports have
Euler0, and the absence of rational curves proves essentiality
through the already established inverse-map resolution.

The actual real norm splitting makes the quotient the mapping
torus of the lifted involution of M5, the unit circle bundle
over Bl(E x P1). The integral H2 basis consists of two lifted
base surfaces and two circle tori over the elliptic loops;
the involution acts (+,+,-,-). Oriented duality gives the
same H3 action; H1/H4 have action -I2. All base and circle
Gysin maps are primitive. Thus compact Y has rational ranks
(1,1,2,4,2,1,1), and integral cohomological torsion (Z/2)^2
in degrees2,3,4,5. The corresponding M3 mapping torus gives
P rational ranks (1,1,0,1,1), with integral torsion (Z/2)^2
in cohomology degrees2 and3. Only rational cohomology is
claimed for the union S: (1,1,1,3,2), by restriction ranks
one in degree1 and zero in degree2.

The global R1(O) logarithmic deck frame is invariant;
the base H1(O) is negative. This gives hO(Y)=(1,1,0,0),
and hO(P)=hO(S)=hO(B)=(1,1,0). The full doubled fibre is
checked separately, not identified with its reduction:
the direct-image bundles upstairs have ranks(1,2,1), and
each equivariant C[t]/t² summand has exactly one invariant
vector, e or te according to its central sign. Consequently
both full scheme fibres have hO=(1,2,1). The quadratic
base-change normalization is the actual map
y -> (pi(y),f(y)); it recovers the primary Kodaira cover.
No persistence of the secondary type under this base change
is asserted. E_secondary_kodaira.py and .out save exact
Smith normal forms, Wang ranks, support restrictions, and
coherent invariants. All checks pass. Root and A were asked
to audit the full fragment.

Root and A independently accepted the full UN21 proof. The remaining
integral support map was then resolved explicitly: the normalized
canonical section over the punctured elliptic base joins to the
core fibre through (r,theta)->(r exp(i theta),exp(i theta)).
The involution shifts theta by pi, preserving orientation, so
the mapping torus of this Seifert surface bounds J in P.
Consequently H2(J,Z)->H2(P,Z) is zero even on torsion.
Integral H_*(S)=(Z,Z+T2,Z+T2,Z3,Z2), while
H^*(S)=(Z,Z,Z+T2,Z3+T2,Z2), T2=(Z/2)^2.
Every radial torsion lift gives Smith diagonal(1,2,2);
the code checks all four choices. The bielliptic component
has H^*(B)=(Z,Z2,Z2+T2,Z2+T2,Z), by the explicit product
of a circle with the mapping torus of inversion on E.
All component, support and ambient integral groups are now
specified. The full schemes retain the separately computed
coherent dimensions.

UN20 was independently audited in full, together with the finite
saturation and exact restriction maps of UN16 on which it depends.
The G representation on L/sL, actual Mobius transformation of h,
equivariant Stein factor, connected generic fibre F/K, local
pseudoreflection smoothness, and cyclic-stabilizer quotient
comparison to the original normalization all pass.

## C.2.UN.23: cyclic torus quotient restriction

The exact proof is in part_C2_cyclic_torus.tex. Pull back every
pluricanonical section through an actual resolution A'->Z,
then push it across A'->A by Hartogs. Its image is a constant
multiple of the global torus volume form. Any divisorial
ramification forces a zero of that constant form, so kills
all positive plurigenera.

For a generator with no invariant tangent direction,
I-L is an isogeny and conjugates the affine action to a
linear action with a fixed point. With no branch curves,
the local action is 1/n(1,r), gcd(r,n)=1. The exact toric
cocharacter lattice is Z²+Z(1/n,r/n). The invariant
m-canonical form has order m((1+r)/n-1) on that primitive
ray, strictly negative unless r=n-1. This excludes every
non-SL case. In the SL case, the height-one fan is crepant.
The fundamental group is computed through the quotient:
every (lambda,L) in Lambda semidirect <L> has a fixed point,
and the local stabilizers kill all these elements, hence
the entire group. Replacing the quotient points by their
simply connected rational-chain plumbings gives the same
relations. The resolution is therefore K3, with trivial
canonical line and pi1=0.

One invariant direction yields either a branch curve and
vanishing plurigenera, or a free quotient. The addition
isogeny ker(L-I)^0 times im(L-I) -> A gives the actual
finite free product-elliptic presentation of the latter,
which is bielliptic. A translation group gives a torus.
This is a complete restriction for every cyclic torus
quotient. Equivariant minimal contraction and its actual
quotient identify the torus-minimal branch of UN16 with
this situation, excluding Enriques in that branch.

The separate rank-one first-integral branch of UN20
does not imply a torus cover. Enriques occurrence there
is not decided by UN23 and remains an explicit remaining
instance of the unrestricted component problem.
E_cyclic_torus.py checks the invariant character, negative
ray order, lattice membership and unimodular height-one
fans exactly. Its first run caught a reversed lattice
membership test in the code; the test was corrected to
y-(n-1)x integral, matching the already stated lattice.
The corrected run passes all effective weights for n<=40.
Root and A were asked to audit the full proof.

Root and A independently audited UN23 and accepted every step.
A primary-literature follow-up located and read Hisao Yoshihara,
Quotients of Abelian Surfaces, Publ. RIMS31(1995)135--143,
Theorem2.1, Example2.3 and Lemmas3.4--3.6. Its projective
classification includes only Klein-four or dihedral-order8
Enriques holonomy, so confirms the cyclic exclusion there.
The source is cited for that prior projective classification.
The independent proof of UN23 includes nonprojective tori and
the component-cover descent. Search terms involving Enriques
components of torus degenerations did not locate a construction;
that search failure is not an exclusion theorem.

## C.2.UN.25: explicit Enriques occurrence

Root supplied the decisive construction, now proved in
part_C2_enriques_filling.tex. An explicit rational elliptic
Weierstrass base has f=T4-3,g=T6+T+2; the exact discriminant
has degree12, leading31, derivative108 at0 and gcd with its
derivative1. The actual node coordinates in C.EN.4 give XY=T.
Quadratic base change and the chart(X,Y,t)=(u,uv²,uv) produce
an I2 fibre with R0 fixed pointwise and R1 coordinate z sent
to-z. Blow up z=1,2,-1,-2 and use the signed divisor
D1+D2-D-1-D-2 with root order2. Dualization conjugates the
q action to its inverse and gives an actual involution
covering t->-t.

The component over R1 is the bielliptic quotient of
C x E, C:Y²=(z²-1)(z²-4), by eta=(j,translation by-1).
The second involution is k=(z->-z,Y unchanged,u->1/u).
eta and eta*k are free; k has16 fixed points paired by eta.
The resulting eight A1 points resolve to an Enriques
surface. The intermediate Kummer resolution and free eta
quotient give the exact canonical K3 double cover.
The ambient fixed curves are four copies of R0; the
quotient charts AC=B²,T=u²A resolve as T=u²r and
T=u²r's'². Their restriction gives precisely the eight
surface A1 resolutions, so the Enriques surface really
is an embedded central component.

Full central fibre: 2M+2A+4Q1+4Q2+sum(E_i), with M
Enriques, A=P1xP1, Q_j Hopf, E_i=F2. Its complete
incidence data give e=32-28+8=12. Six UN4 negative-two
blocks on fresh points of E_i, away from M, give an SNC
zero-Euler support and leave M itself unchanged.
The compact infinity fixed curves are elliptic and
contribute only Euler-zero components; all other nodal
base fibres are nodal curves times E. General fibres
are actual product tori, and the quotient Stein factor
has degree1. The exact code E_enriques_filling.py/.out
checks the discriminant, cover identities, both quotient
resolution charts and all Euler terms. Root, A and D
independently audited the construction. A is adding the
support rational/coherent cohomology as a separate input
fragment; the occurrence theorem is complete independently
of that additional calculation.

A's exact UN25 support fragment was independently audited and
input into the proof. Its ten rational Enriques curves form two
affineD4 blocks with exactly the common-fibre relation. The
elliptic attaching curves are half-fibres of that same map.
The resulting degree2 restriction rank14, Hopf degree1 rank2
and incidence ranks7,8 give b(S)=(1,1,8,4,8), hO=(1,1,0).
Six balancing blocks give (1,1,20,40,20), with hO unchanged.
Root accepted the full UN25 source and support proof.

## C.2.UN.27: properly elliptic chi(O)=1 components

The exact UN25 construction extends with no new gluing:
blow up ±1,...,±r on R1 and use the signed divisor of
the r positive minus r negative exceptional curves.
The product cover is C_r x E with
C_r:Y²=prod(z²-j²), genus r-1.
eta=(j,translation-1), while k=(z->-z,Y->(-1)^rY,u->1/u).
For even r, k_C has4 fixed points and jk_C none;
for odd r each has2. The product fixed-point total
is always16, paired to eight A1 points. All actual
ambient quotient charts and multiplicities are unchanged.

The invariant meromorphic form dz wedge du/u has exact
divisor sum J_j-F_infinity after the crepant A1 resolution.
At branch points dz has a simple zero; at either infinity
it has a double pole. The two toric charts convert that
pole to precisely the full I0* multiplicity divisor.
Thus K=sum J_j-F, 2K=(r-2)F, and the actual connected-fibre
pushforward is O_P1(-m+r floor(m/2)). This proves
P_m=max(0,1-m+r floor(m/2)) and minimality. Every r>=3
is projective properly elliptic, chiO1, q=pg0,e12;
r2 recovers Enriques. This extends the occurrence
classes beyond UN18's chiO0 properly elliptic components.

A generalized and executed the exact support matrix:
H0 incidence ranks r+5,8; Hopf H1 restriction rank r;
H2 restriction rank14, with r-dimensional kernel from
r-1 half-fibre differences and one affineD4 relation.
Therefore b(S)=(1,1,r+6,2r,r+6), and after six blocks
b=(1,1,r+18,2r+36,r+18), with hO(1,1,0) in both.
The fragment elliptic_root_support.inc.tex is input by
part_C2_elliptic_chi_one.tex. E_elliptic_chi_one.py/.out
checks both parity patterns and independently counts
all plurigenera as invariant hyperelliptic forms.
The punctured family is literally the same product
coordinate c=a^-1 with h:c->c^-1 for every r.
Distinct canonical slopes r/2-1 distinguish the
essential component and hence each filling.

## C.2.UN.30: properly elliptic chi(O)=2 components

The exact construction is in part_C2_elliptic_chi_two.tex.
Use the square elliptic base E0 and blow up paired torsion
points ±p_j on E0 x {0}, with p_j=j/N and odd prime N>2r.
The signed root divisor and order2 quotient are those of
UN18; the base involution(-p,-t) lifts by fibre dualization.
Its off-central product coordinate c=a^-1 is independent
of r, so every filling has the same actual punctured
Kummer family with monodromy(-1,-1).

The main surface B_r has an actual finite etale product
cover C' x E, where C->E0 is the branched square root of
the torsion line L|E0 and C' kills its torsion square root.
The two exact Jacobians2 and-2/u² prove etaleness at roots.
Thus B_r and its quotient resolution M_r are projective.
The involution has16 isolated A1 points on B_r, lying
over the four two-torsion base values. M_r has fourI0*
fibres andr double smooth fibres. The invariant actual
form omega_E0 wedge dlog(ell) has one zero on each root
fibre and no other zero or pole, so on M_r its divisor
is sumJ_i. Consequently K=sumJ_i,2K=rF and
p_*mK=O(sum floor(m/2)b_i), giving P_m=1+r floor(m/2).
This proves minimality, kappa1 and distinct slopes r/2.

Finite quotient Euler gives eM=24; K²0 and RR givechiO2.
P1=1 then givesq0. Projectivity gives rational ranks
(1,0,22,0,1). In the threefold the fixed points have
representation(-1,-1,-1); the exact UN13 blowup chart
T=Ru² resolves them and restricts to the actual surface
A1 resolution. Fullcentral2M+4sumQ+16P2 has e40.
Infinity is the original product-Kummer support e40.
Twenty negative-two blocks on each fibre, away from M
and the infinity K3, give two zero-Euler supports.

The central support is a star with16 rational andr
elliptic edges. The plane edge block has rank16 and
the common nonzero half-fibre adds one, so H² restriction
rank17. Hopf H1 has rankr. Hence support before/after
balancing has ranks(1,0,21+r,2r-1,17+r) and
(1,0,61+r,2r+119,57+r), withhO(1,0,1) in both.
A independently checked these rows. Exact matrices,
torsion-centre choices and chart Jacobians are executed
in E_elliptic_chi_two.py/.out. All checks pass.

## C.2.UN.32: complete K3 occurrence criterion

The new exact proof is in part_C2_k3_exact.tex. UN28 gives
pg(E)=1 for the actual component cover over a K3 component;
UN22/29 make its non-torus case a constant-Jacobian smooth
multiple elliptic fibration over an elliptic curve.
The cyclic action preserves the actual fibration by the
rank-one quotient construction, the a1 function field,
or the Iitaka field. Factor H, the base-action kernel,
first. Its generic fibre action is translation (otherwise
the quotient would be ruled); at a multiple fibre every
fixed-point stabilizer is a normal reflection. Thus E/H
is smooth and again has only smooth multiple fibres.

The normalized root chart is explicitly
(F x Delta_u)/delta, delta(u,z)=(zeta_m u,z+tau),
with tau of exact orderm. A finite weighted-sum gauge
removes every u-dependent translation term. The unique
holomorphic two-form is locally
m c(u^m)u^(m-1)du wedge dz. Invariance of the pullback
K3 form gives lambda*beta=1 for the faithful cyclic
base action and its fibre character.

At a base stabilizer of orders>1, a root lift has
u->rho u, rho^m=lambda, and fibre beta z+a(u).
Commuting with the root deck generator gives beta*tau=tau.
Since sum beta^j=0, this forces m|s. The induced affine
automorphism of the reduced elliptic fibre has a fixed
point. Choose a root lift fixing a point above it; its
sth power is a deck transformation fixing that point,
so isidentity. Thusrho^s1 andrho^m hasexactorders,
forcinggcd(m,s)1. Hencem1. At a free base orbit,
multiplicity persists on an elliptic image curve, whose
canonical zero orderm-1 cannot occur in the pullback
of the nowhere-zero K3 form: that curve is nonexceptional
under every surface birational comparison.

The resulting E1 is a smooth principal elliptic bundle
over an elliptic curve. Its actual Cech Chern vector
c in H²(B,Lambda_F) satisfies c=beta*c; beta-I has
no real kernel, so c0. The sheaf exact sequence
0Lambda->O->F->0 lifts the torsor class toH1(O).
Represent it by a constant (0,1)-form on B=C/Gamma.
The actual deck translations are(z,w)->(z+gamma,
w+a bar(gamma)) and(z,w)->(z,w+lambda); they form
a discrete rank-four lattice. Cech coboundary fibre
translations give the actual isomorphism to E1.
Thus E1 is a torus, and the residual cyclic quotient
is exactly the UN23 symplectic K3 case.

UN24 gives every converse occurrence with its compact
diagonal quotient and zero-Euler balancing. This proves
the K3 criterion in all algebraic dimensions, beyond the
prior a0 equivalence. Exact order2/3/4/6 lattice matrices,
translation-fixed exponents, Chern kernels and the root
gauge identity are executed in E_k3_quotient_descent.py/.out.
Root, A and D were asked to audit the full proof.

## Audit updates: UN30 and UN32

Root and A independently audited the complete UN32 source and passed the exact root gauge, fibre-translation quotient, fixed-point lift, free-orbit canonical divisor comparison, Chern-vector identity, and additive lattice presentation. D completed a full independent UN30 audit with no correction: the two finite product-cover Jacobians, invariant canonical form, all plurigenera, Euler/coherent groups, and support restriction ranks passed.

## C.2.UN.35: exact equivariant occurrence and the exhaustive quotient criterion

Complete source is part_C2_equivariant_occurrence.tex, tags C.EO.1--16, with A's independent equivariant_torus_h1.inc.tex (C.EO.H1--H7) input exactly once. The given smooth-multiple elliptic surface is its actual principal fixed-F torsor over the root curve, including inertia translations of exact order m. The canonical Lie-group sequence 0->C->(Lambda tensor C)/Lambda->F->0 is equivariant for the integral lattice action; its additive kernel has character beta^-1. Coherent H2 on the finite quotient orbicurve vanishes by averaging and curve dimension, so the full equivariant torsor lifts to T=(C*)² with an actual cocycle, not merely a Picard-class lift.

For faithful base action its generic torsor descends to the twisted algebraic torus over C(B/Q). Steinberg1965 Theorem1.9, printed page51, was independently opened/read at https://www.numdam.org/item/PMIHES_1965__25__49_0.pdf (webref turn617view0). It applies to all connected linear algebraic groups. A gives a complete independent proof for the actual cyclic rank-two lattice orders1,2,3,4,6: Riemann--Roch C1 calculation, exact norm surjectivity, norm-one/induced character lattices, and explicit restriction/corestriction for order6. The reduced-norm argument also checks the precise division-algebra formulation of Steinberg's field hypothesis.

The resulting generic rational point pulls back to an exactly invariant meromorphic T-frame. For every character it defines a divisor; these divisors form an additive equivariant functor. Blow up its finite support in complete group orbits and replace each point by the new vertical exceptional curve, retaining fractional coefficients in the original root orders. Canonical divisor sections give exact monomial group actions, with no residual scalar two-cocycle. Restriction of each section/divisor agrees and therefore gives the actual original equivariant torsor. Local root lifts differ by the identified inertia translation on F, so their maps on the coarse total space satisfy the exact group law.

For elliptic B use B times P1 with a faithful disc character. For rational B use one blowup of A times P1 at(o,0), with action identity on A and the disc character; exceptional coordinate x/t has its inverse character and realizes any faithful cyclic P1 action. A root/divisor mark at its old node is allowed: x=uv,y=v gives strict B:u0, exceptional:v0, and the exact restriction O(exceptional)|B=O(p). Rooting the disjoint new exceptional divisors leaves the covering total smooth because every nontrivial inertia element translates F nontrivially. Off zero all divisor frames are holomorphic units, yielding an actual product of two elliptic curves. The ambient finite cyclic quotient over T=t^n and a proper resolution retain the distinguished component E/Q; UN4 balances the support to Euler zero through explicit proper birational maps.

For exhaustion, UN31 supplies the actual cyclic cover. The non-torus fibration is intrinsic by Iitaka or algebraic reduction; for a projective bielliptic cover use the Aut0 orbit pencil. Its finite free product cover makes Aut0 the first elliptic translation factor, so every automorphism preserves that pencil, whose root transitions are translations. Factor the generic base kernel using UN33's exact translation/reflection charts, leaving the faithful input just constructed. Cyclic torus quotients give the complementary class. This is an exact necessary-and-sufficient occurrence criterion, with all quotient data specified.

Executed E_equivariant_occurrence.py/.out: 233 exact orbit-divisor intertwining cases, 2375 faithful root-translation charts, all blowup/root monomial multiplicity and character identities, the rational auxiliary action, and the paired root-lift/deck ambiguity. A_equivariant_torus.py/.out independently checks the norm-torus lattices and additive-kernel characters. Root/A/D were asked to audit the full UN35 source.

## C.2.UN.38: exact Hopf boundary obstruction

Complete source part_C2_hopf_boundary.tex, tags C.HB.1--9. Relative canonical evaluation supplies an actual section with vertical divisor sum k_i S_i. On a neighborhood meeting only the smooth component S of multiplicity m, the original fibre function trivializes O(mS), so adjunction gives K_S^m trivial on that entire neighborhood. For a compact elliptic C there, a second adjunction gives N_C/S^m trivial. This proof removes the need for a relative Douady theorem. The independently checked Douady route would work after normalized root base change and upper semicontinuity of h0 of the normal line, but is not needed or cited.

For diagonal Hopf H(alpha,beta), the normal of the alpha axis has automorphy beta. A trivial nth power gives a Laurent eigenfunction a(alpha z)=beta^n a(z), hence beta^n=alpha^j and a nonconstant invariant w^n/z^j. Thus both normals are non-torsion when a0. For nonlinear F(z,w)=(beta^r z+w^r,beta w), the ordinary normal is torsion of order r, so it gives no exclusion. Instead dz wedge dw /w^(r+1) is invariant and K=-(r+1)C. Neighborhood K^m trivial would produce an invariant holomorphic function vanishing on C. Its first term must c z^-k w^(rk). At order r(k+1), the Laurent eigenoperator annihilates z^(-k-1), but the required coefficient is k c beta^-r, nonzero. This proves the higher-neighborhood obstruction exactly. Root independently audited the algebra.

The statement is restricted to an actual smooth minimal Hopf normalization, or an actual unchanged minimal Hopf neighborhood; it does not silently pass through blowups on the axis. On such a normalization the boundary is a curve divisor. Only the two diagonal axes or the one nonlinear axis occur: the proof extends any invariant curve across the origin, removes the unit cocycle by a convergent contraction product, and analyzes the resulting eigenfunction. Hence an axis omitted by the boundary is disjoint from it and contradicts the canonical neighborhood obstruction. Finite unramified primary coverings retain the neighborhood trivialization and give the secondary Hopf assertion.

Primary sources independently opened: Khaled arXiv2310.05265v2, normal forms at pp3--5 (turn630view0), and Nakamura's 2008 author survey section1.1 (turn630view1), using only their established normal-form/finite-cover facts. Existing bibliography keys are reused. E_hopf_boundary.py/.out executes the invariant canonical form and all 72 resonant jet identities for r1..8,k1..9. No occurrence or full a0 exclusion is inferred.

UN35 full audits by root and A pass after the explicit inverse-character choice for the rational auxiliary surface. The final C.EQ references match the current UN33 source.


## C.2.UN.41: compact occurrence of every diagonal primary Hopf surface

Full source is part_C2_diagonal_hopf_occurrence.tex, tags C.DH.1--16 (with explicit Tate sublabels14a--b). Two copies of the prescribed H(alpha,beta) are joined along each axis by inversion. The exact normal-line quotients have mutually inverse multipliers. The necks xy=t are glued to finite Hopf cores using r<R and delta<r². Closed-overlap boundary checks give a Hausdorff smooth threefold, and compact interior cores plus closed subneck bundles prove properness. The two transitions are(1/z,t/w) and(t/z,1/w); their discrepancy is precisely(t,t^-1). The nearby torus lattice has nonzero real determinant -(A+B)L. The actual maps from all four charts form a proper local biholomorphism; the height-zero fibre has one preimage, hence the map is an isomorphism.

Compact globalization uses a cubic pencil through the origin and prescribed alpha point of a nodal cubic. After nine blowups, K=-F and the minimal graph argument extends translation by the section to a global automorphism. The compact suspension(C* times J)/(u,y)~(alpha beta u,T_P y) has the required punctured family. The Tate parameter has a simple zero, and the central chart x=u/(1-u)²,y=u²/(1-u)³ maps by X=4x,Y=8y+4x to the chosen nodal cubic, with exact multiplicative coordinate u. This fixes the sign/inversion in the section limit. The coordinate z=y,w=u/y identifies both lattice generators. Replace the local suspension by the proved proper plumbing through this actual family isomorphism. Properness is local on the compact base, so the resulting smooth total space is compact. All other supports remain elliptic-base bundles and have Euler zero.

The integral normalization maps are H0=[[1,-1],[1,-1]] and H1 rows(1,1),(0,0),(1,1),(0,0); both have primitive rank one. They give support cohomology ranks(1,2,3,4,2), with no torsion, and coherent dimensions(1,2,1). E_diagonal_hopf_occurrence.py/.out checks every plumbing/deck coordinate, the lattice determinant, nodal coordinate and Tate expansions, and the Smith forms. A independently read and passed the full written proof. Root supplied an independent period derivation and verified the section-translation primary source. I independently opened Schuett--Shioda arXiv0907.0298v3 (turn644view0), section7.6 printed pages33--34, and retained our own graph proof. No priority claim is made.


UN41 full written audits by root and A both pass, including the added explicit Tate comparison and both cohomology tables. Code/output and metadata are complete.

## C.2.UN.42: compact occurrence of every nonlinear primary Hopf surface

Full source part_C2_nonlinear_hopf_occurrence.tex, tags C.NH.1--18. The explicit smooth curve v²=t^(6r)-t^(2r)+1 maps to the elliptic cubic v²=u³-u+1 by u=t^(2r). Its two infinity points map to the origin with exact order r, are exchanged by the hyperelliptic involution, and admit coordinates with 2psi=s^r. Weight-(r,1) blowups at the paired points of B times C give a compact smooth orbifold surface. The tautological O(R_++R_-) has weight-minus-one fibre; its nonzero total space is actually smooth, with coordinates(z,w,x), p=x^r z,s=xw. The canonical lift of translation2psi is z->z+w^r. Multiplication by beta yields g=(beta^r(z+w^r),beta w,beta^-1x), and rescaling z gives exactly the prescribed Hopf contraction.

Global properness is proved by the actual canonical-section norm. Near each centre its norm is comparable to (d_B(p,0)²+|s|^(2r))^(1/(2r)); translation by 2npsi gives two-sided ratios bounded by C(1+|n|)^(1/r). The line-norm ratios extend over the exceptional divisor. Hence beta^n dominates uniformly, giving a free properly discontinuous action for every prescribed 0<|beta|<1. A high iterate contracts all norms, and its compact norm annulus meets every orbit. This proves compactness rather than assuming it from local charts. Off the distinguished fibres, the exact additive rank-four translation lattice gives a compact two-torus.

The half-translation and hyperelliptic base involution commute, with their exact canonical line lifts. G=beta^(1/2) A_half h satisfies G²=g. A fixed point modulo g must lie over a hyperelliptic branch value, where psi is two-torsion and no blowup centre occurs. In the canonical frame G has line multiplier beta^(1/2), whereas g^n has beta^n; absolute values exclude equality. The free quotient has base P1 and exchanges the two Hopf copies, preserving either one unchanged. The other special supports are free torus quotients and have Euler zero.

The central full fibre is reduced xy=0, with H and P joined along E_(beta^r). On P the exact chart p=x^r z,(z,x)~(beta^r z,beta^-1x) and the outer frame ell=x^-1 identify it with the one-fibre logarithmic model already computed in UN6, now including r1. The canonical form has divisor(r-1)J. Its Seifert meridian r delta+h kills the core longitude and yields H1(M)=Z². P=M timesS1 has free ranks(1,3,4,3,1); J angular class is zero and radial class primitive, so its H2 class vanishes integrally. The exact normalization maps give free support ranks(1,3,5,5,2), coherent(1,2,1). E_nonlinear_hopf_occurrence.py/.out verifies the compact-curve squarefreeness, weighted quotient/gauge maps, seven iterates for r1..10, canonical form, exact G² relation, and Smith restriction forms. Root/A/D were asked to independently audit the full source. D supplied the half-period compact globalization and is writing the secondary quotient extension UN43.

UN42 full independent audit by D passes all maps, global norm bounds, rational-base quotient, exact component comparison and integral/coherent support groups. D confirmed that the product model P=M_r timesS1 preserves J as core-circle timesS1, proving integral nullhomology. Three typesetting repairs were applied; no mathematics changed. E independently read and passed UN43 in full, including the actual abelian deck splitting, unramified selected torsion-cover sheet, compact suspension finite action, both neck maps, and nonlinear scalar action modulo the infinite deck and half-period involution.

Root independently read all UN42 source and output and passed. The norm comparison now explicitly covers the whole B times small c-disc, including iterates moving p outside the local chart. The actual holomorphic canonical evaluation form x^r dz wedge dw wedge dx has invariant multiplier one and orders(k_H,k_P)=(r,0); the earlier message pair(0,-r) was only a meromorphic full-fibre shift, and no holomorphic-generator claim uses it. All literal TeX repairs are applied.

A independently read and passed all UN42, including the polynomial distortion, annular compactness, free half-period quotient, and all support groups. The actual pair identification(P,J)=(M_r timesS1,core timesS1) is now explicit, using the core-preserving circle isotopy; this justifies integral nullhomology through a concrete product map. Thus root, A and D full audits all pass.


## C.2.UN.49: exact whole-support nonlinear Hopf star criterion

Full source part_C2_nonlinear_stars.tex, tags C.NS.1--20, and executed E_nonlinear_star_criterion.py/.out. This is a necessary-and-sufficient criterion for the specified reduced SNC star P plus nonlinear primary Hopf leaves, with P a fixed-Jacobian identity-monodromy elliptic quasi-bundle. It retains all component moduli, full torsor transitions, and actual axis gluings. The exact inverse-log chart is p=x^r z,w=x^-1; it replaces each marked multiple fibre by the actual product F timesdisc. The integral boundary columns in(delta,e,h) are a=(1,0,0), b=(0,0,1), mu_P=(r,-1,0). Smoothing mu_H=-mu_P identifies the Hopf regular-fibre cycles with(e,h), while its complementary solid torus kills a=delta. Hence the smoothed four-manifold is exactly the inverse-log principal bundle T0 and every transported Hopf core is the same integral fibre class. The Chern vector retains all global boundary windings; it is not replaced by the multiplicities alone.

Canonical evaluation gives k_Hi-k_P=r_i and K_P=sum(r_i-1)J_i. Exact quasi-bundle canonical pushforward gives g(B)>=1, and the remaining effective canonical divisor forces B elliptic and no unmarked multiple fibres. The rescaled canonical form on H_i minusJ_i is c_i dz wedge dw/w^(r_i+1). In U=z/w^r and W=logw its period determinant is nonzero 2pi i beta^-r. All these are the same global torus period, so every r_i equals one common r, even with independent primitive angular directions. Fundamental-group comparison then forces c(T0)=0. The actual Cech class lifts to H1(O_B), whose constant Dolbeault representative gives a rank-four translation lattice and an isomorphism T0 with a complex torus.

For sufficiency the compact twistor family is written explicitly as O(1)^2 modulo lattice sections v=(p,z)->(p+t barz,z-t barp). Real invertibility has denominator1+|t|². Every oriented fibre-lattice basis has the same nonzero wedge times t. After t=s^r, deleting one generator produces the actual flat-line semi-torus M_i,s^times with deck(p+delta_i(s),beta_i ell), where delta_i has exact orderr and the prescribed beta_i is retained. Weighted insertion tensors by O(R_i), giving exactly the nonlinear Hopf chart. Unitary flat metrics reduce the varying flat-line norm to an exponential factor still less than one, so the polynomial weighted distortion gives a proper local quotient. Off the inserted Hopf there is an actual isomorphism to the original twistor tube minus its marked elliptic curve. The estimate p-p_i=O(|x|^r+|s|^r|log|x||) proves every cluster point is on that curve; this supplies Hausdorff and proper simultaneous replacement at disjoint curves. The central main component is exactly the original P, and all gluing translations are retained through actual Hopf automorphisms. Every other fibre remains a smooth torus.

Code verifies the determinant-one boundary matrix, the rational/integral Chern correction, ten exact nonlinear period Jacobians, all small SL2(Z) fibre bases, the twistor inverse, and commuting flat-line deck maps. Root/A/D full source audits were requested. Checkpoint09 is instructed to include this complete source beyond its clean PDF cutoff throughUN48, honestly marking the independent audits pending.


### UN49 complete independent audit closure after checkpoint09

Root, A and D each independently read the entire UN49 source and passed every major step. Their audits cover the exact inverse logarithmic torsor and primitive boundary matrix, the actual same integral core cycle despite distinct angular slopes, the nonzero canonical period and common resonance, the full Chern-zero torus comparison, both charts of the compact twistor lattice quotient, the varying-flat-line weighted insertion, and the logarithmic cluster estimate used in simultaneous Hausdorff/proper replacement. No mathematical correction was requested. Checkpoint09 correctly listed audits pending at its earlier cutoff; all three passes arrived after it closed.

E independently read all of D's UN46 and UN48 and passed: the affine logarithmic maps from actual entire line bundles; injected semidirect fundamental group of any actual SNC smoothing; closed coframe and transitive entire flows; complete four-period lattice; two-component inversion comparison; common rank-three lattice and nonzero signed normal-period sum; primitive elliptic quotient; prescribed nodal section and I_d resolution charts; variable Hopf and finite torsion lattices; two normal-product constants; punctured suspension isomorphism; and final compact annular replacement. No correction was requested. These audits were sent during the checkpoint freeze and are now recorded.


## C.2.UN.50: complete nonlinear primary and secondary star criterion

The audited UN49 remains unchanged. New part_C2_secondary_nonlinear_stars.tex gives every exact change for H_r(beta)/mu_n, gcd(r,n)=1. The actual coarse coordinates are u=z^n and X=x z^k with rk-nl=1. They give p=X^r u^-l and deck(u,X)=(gamma^r u,gamma^l X), gamma=beta^n. The normal root cover u=y^r,X=s y^l has primitive-normal generator translating F by n/r, so the torsion character is retained as well as its order. The inverse product coordinate is W=X^-n u^k=x^-n; its inverse is u=p^n W^r,X=p^k W^l.

The primitive boundary matrix has columns(-l,k,0),(0,0,1),(r,-n,0), determinant1. Hence mu_P=r delta-n e, delta=n a+k mu_P, e=r a+l mu_P. On the Hopf side the invariant normal is Y=w z^-k; its complementary meridian is n a-k mu_H and its fibre cycle r a-l mu_H. With mu_H=-mu_P these become exactly delta,e, so all core cycles still agree integrally. The global Chern correction adds the full n_i e_i/r_i, not merely the residue of n_i modulo r_i. The secondary canonical core period is 2pi i beta^-r/n, nonzero, so UN49's equal-resonance necessity persists.

For compact realization the twistor semi-torus deck scalar is gamma_i=beta_i^n_i. Tensor the flat line after the weight-(r,1) blowup by O(n_iR_i). Its smooth nonzero coarse chart is the free finite quotient with weights(r,1,-1) modulo n_i. Lifting the infinite deck by the prescribed beta_i gives exactly the required secondary Hopf component. The outer flat coordinate is x^-n_i, so both the original torsor and the full integer Seifert framing are restored. Polynomial norm distortion exponent n_i/r is still dominated by the contraction, and the same logarithmic cluster estimate allows simultaneous compact replacement. The other fibres are unchanged tori.

E_secondary_star_criterion.py/.out passes255 coprime(r,n) examples with exact Bezout, inverse monomials, determinant-one boundary maps, normal-root character, infinite deck weights and nonzero period formula. Full independent root/A/D audits requested.


UN50 complete root audit passes. Root independently checked the reciprocal Hopf base and fibre monomials, the killed meridian and primitive core, the full n-dependent character and Chern correction, the free O(nR) coarse quotient, and every contraction/cluster estimate.

### Independent check for root's forthcoming full mixed-Hopf-star reduction

The canonical relation K_H=-aJ pulls back to a central weighted diagonal primary cover F=(gamma^p z,gamma^q w), gcd(p,q)=1. A generic elliptic curve lifts to z^q=c w^p of weighted degree pq, and an orbit of m such curves has degree mpq. The character equation a m p q=p+q excludes every generic curve unless p=q=m=1. For p=r>1,q1 it also excludes the weight-r axis; only the weight-one axis remains, with a=r+1. The finite affine action on z/w^r has a fixed point by averaging, giving an actual diagonalizing coordinate change. Exact determinant/normal character equality forces every deck matrix to have diagonal characters(C^r,C); finite weights therefore are(r,1).

For a central scalar cover, the preimage is m distinct lines and a m=2. If m1, the determinant character equals the square of the marked normal character. Both diagonal characters coincide, and the unipotent additive parameter vanishes because a scalar central contraction has finite index; the full group is scalar and its torsion is cyclic. If m2, some element exchanges the lines and acts by -1 on dz/z wedge dw/w, so the required log-canonical trivialization cannot descend. A nonzero unit cannot repair this character, since it and its inverse extend across0 and its value there is nonzero. This independently closes the apparent nonabelian-secondary one-boundary case. For a nonlinear leaf the previous actual cyclic normal form already applies. The resulting mixed-star rule is exactly: one common period order R for nonlinear leaves; each diagonal weighted resonance must be strictly smaller, because its leading core two-form period vanishes. Root owns that extension as UN53.


UN50 full independent A audit passes every coarse exponent, normal character, boundary matrix, killed meridian, primitive core, O(nR) quotient and analytic compactness comparison. Root and A full audits now pass; D has checked the exponent algebra while completing UN52.

### Independent full audit of root UN53

E read the complete part_C2_all_hopf_stars.tex and passed all steps: full primary/secondary pair classification including the nonabelian scalar-cover orbit and its log-form sign; the exact degree-one strict cover for the multiplicity-one central P; effective-canonical minimality; verticality of the marked curves through the actual elliptic quotient or Chern pullback; exact normal-order/multiplicity comparison; the common primitive period and diagonal strict inequality; and every mixed weighted chart, finite action, norm bound and cluster-set compact replacement. No correction requested.

## C.2.UN.54: coherent incidence and the entire reduced a0 Hopf support branch

The complete source is part_C2_hopf_graph_reduction.tex, tags C.HR.1--8, with E_hopf_graph_reduction.py/.out. On every primary Hopf surface the nonzero constant additive deck cocycle restricts nontrivially to every elliptic curve: the actual lifted parametrization has contraction u->lambda u, and the constant Laurent coefficient prevents b(lambda u)-b(u)=1. Finite unramified trace and restriction maps prove the same on every secondary surface.

The actual normalization sequence for a reduced all-Hopf SNC support has H1 map equal to a weighted graph incidence matrix with every endpoint coefficient nonzero. A tree has a surjective matrix and h2O0, which flat upper semicontinuity excludes. UN44 makes the graph group an abelian quotient of the nearby Z4, so there is at most one cycle. The graph is therefore unicyclic and its sole remaining matrix row must vanish on the spanning-tree kernel. This is exactly product-one holonomy for the actual restriction ratios, yielding hO(1,2,1).

Serre duality identifies the transpose matrix with the component residue obstruction maps. Leaf elimination kills every residue on an attached tree, while the cycle residues are all nonzero. H0K_H=0 means the unique global dualizing form vanishes exactly on the off-cycle components. Dividing the canonical evaluation by the minimum full-fibre power and using the actual xy=t adjunction formula proves that its minimum vertical order is attained exactly by the cycle components.

If all Hopf components have algebraic dimension zero, their exact curve lists give degree at most two. A connected unicyclic graph with this bound has every degree two. All components are therefore diagonal and there are no attached trees or nonlinear components. The actual normal maps and integral product of UN46, followed by the compact realization of UN48, classify the entire reduced all-a0-Hopf support branch, retaining all component and gluing data. This is a proved reduction to a complete existing occurrence criterion; the all-a1 attached-tree branch is not asserted to be classified. Code passed35 exact cycle/tail/tree maps, a symbolic two-vertex determinant and a branched transpose-kernel calculation. Independent root/A audits requested.


UN50 full independent D written audit now passes. The wording for Y=w z^(-k) now says normal-line multiplier gamma^(-l); the nonlinear full coordinate has higher terms, already handled by the explicit diagonal-reference smooth-pair comparison. Root/A/D full audits all pass.

E read all UN52 and independently passed the weighted core/neck construction, finite normalizations and inertia, actual R=I argument through the nontorsion elliptic line, integral period descent, constant-integer transport and rational left-kernel comparison, independent edge-orbit normal constants, invariant ring and full multiplicities, punctured marked-torus torsor trivialization, compact base gluing and both unequal-multiplicity examples. No correction requested.

UN54 precision from both root and A applied: a primary curve can lift to several branches permuted by F. Passing to F^d fixes a branch and yields the actual finite elliptic cover C-star/<F^d> of the curve. The pulled constant cocycle is d, not1; the same Laurent constant-term contradiction proves nonvanishing. All residue and incidence conclusions are unchanged.


UN54 root full audit passes after the F^d correction.

## C.2.UN.58: exact geometry, canonical heights and period heights of Hopf trees

Full source part_C2_hopf_tree_reduction.tex, tags C.HT.1--12. Normal duality first separates any diagonal a0 component from all torsion-normal Hopfs, so its whole connected support is the previously classified diagonal cycle. In the remaining branch all internal/cycle vertices are a1 Hopfs and the only a0 vertices are nonlinear leaves.

The actual normalized multiple-fibre cover is F timesdisc with free translation inertia. The explicit averaging gauge b(s)=-(1/m)sum j A(zeta^j s) makes this translation constant. Its normal line has exact order m, and duality identifies the connected regular-fibre covers across every edge. Fixed identity-monodromy charts give a globally well-defined meromorphic two-form q*theta wedge dz even though dz alone need not be an absolute global form. Ratios of vertical-divisor forms descend as actual meromorphic functions on P1, including in the root chart. The exact order formula is m ord(theta)+m−1.

Canonical evaluation gives divisor sum(k_neighbor−k_v−1)J. The root congruence excludes every unmarked multiple fibre, makes (k_neighbor−k_v)/m an integer, and degree(theta)=-2 gives sum d=valence−2. Every terminal edge has outward d1. Backward leaf induction forces d1 on every tree edge, so the canonical height is the sum of normal orders along its path from the cycle. The precise base differentials are c dz/z at cycle vertices and c dz at tree vertices with parent point infinity.

The actual finite-root cohomology square identifies UN54 coherent holonomy with the linear action of the lifted elliptic maps, so its cycle product is a translation and all Jacobians identify. Normal-product xy=t takes x^m=c to y^m=t^m/c on the same connected root cover. Together with the product-preserving tubular comparison and UN50 nonlinear-core map, this proves equality of the integral core classes in the actual nearby torus. Its canonical period has order greater than every elliptic vertex height and exactly each nonlinear leaf height, with nonzero leading coefficient 2pi i c beta^(-r)/n. Thus all nonlinear leaves have one common weighted height. No nonvanishing period is asserted when there is no nonlinear leaf, and no existence inference from the necessary equations is made.

E_hopf_tree_heights.py/.out passes the branched weighted harmonic system, its unique heights and rational differential orders, unequal-height obstruction, unmarked-multiple congruence, actual collar monomials, and19 general finite-orbit gauge identities. An initial unnecessary symbolic trigonometric implementation was interrupted for speed and replaced by the stronger formal cyclic-vector identity; the final exact output is complete. Root/A full source audits requested.


UN58 full root source audit PASS through C.HT.12. Root checked the exact translation gauge and primitive normal character, invariant wedge and vertical-ratio descent, divisor congruences and unmarked-multiple exclusion, tree induction, actual coherent Jacobian comparison, collar root-cover isotopy and nonzero nonlinear periods. Code and metadata were already complete.

E independently read all UN56 and passed the ruled normal-line decomposition and local flat pullback, m|(a+b) and equal ramification, actual elliptic lattice cover and projective-bundle power map, index decomposition, common root inertia, one-original-Hopf contradiction, nontorsion ruled-line condition, translated marked Pic0 families and finite compact quotient. No correction requested.


UN58 full independent A and D written audits also pass; root/A/D complete audits all pass.

## C.2.UN.60: complete all-Hopf pruning/reinsertion criterion

Complete proof draft is sections/hopf_tree_occurrence_draft.inc.tex, deliberately unassembled during checkpoint10 preparation. All exact code is saved and passed in E_hopf_tree_pruning.py/.out. Root/A/D received the full proof for independent audit. D independently checked every one-/two-mark root-torsor map; A independently checked the exact two-axis/ruled core descriptions and all period/order identities.

The criterion consists of the actual unicyclic graph and dual normal maps, no unmarked multiples on elliptic vertices, the common nonlinear weighted height with strict smaller elliptic heights, and M=I on the exact pruned core. The full analytic pruning record is retained. On a one-point root P1, the exact additive-kernel sequence identifies F torsors with two integer line degrees; zero forces the product ruled cap, while a nonzero vector−n e gives O(−n)^times/gamma^Z and the specified weighted secondary Hopf pair. Two marked points are handled by the explicit degree-gcd cyclic etale root-stack cover and coprime weighted projective line, yielding an actual marked diagonal Hopf quotient or P(O plus L) via a finite translation/rotation quotient of F timesP1.

Each inverse Hopf operation uses the full Bezout chart p=X^m u^(-l), W=X^(-n)u^k; this retains the complete integer and torsor transition, not just normal torsion. Disjoint operations commute by their literal atlases. For necessity the compact leaf boundary Z3→Z2 kills the same primitive delta as F timesD2, so actual van Kampen pushout diagrams preserve the nearby fundamental group on the exterior. The final core group is therefore Z4, forcing its injected semidirect product M to be identity. No analytic contraction of the original smoothing is asserted.

Sufficiency uses the compact UN57 period family with V_(t^R) and unchanged logt, whose positive determinant is explicit. The primitive compact elliptic period is exactly 2i Im(c)||lambda||² t^R. A local fibre-basis change gives the exact semi-torus deck (p+delta(t),gamma(t)w). Weight-m insertion with O(nE) has the explicit child U=Z/W^m translationdelta/t^m. The product ruled cap is the ordinary blowup(p,t); delta order at least2 makes its normal projective action identity and its child translationdelta/t. Hence every recorded height determines its actual central diagonal or nonlinear type and its remaining period order.

The affine base is treated directly: rho=(|p|²+|t|^(2m))^(1/(2m)) gives uniform polynomial norm distortion, dominated by the line contraction. For old images in a compact annular chart the new p satisfies a linear-versus-logarithm bound and remains bounded. At x0 the old p displacement is O(|x|^m+|t|^ell log|x|), so every cluster point lies on the one removed compact elliptic curve. This proves the actual Hausdorff/proper finite replacement and its compact gluing, even without a compact auxiliary base. Reverse induction through the recorded transition maps restores every original surface, torsor, base point and gluing translation.

The output certifies120 primitive basis changes,400 two-mark Picard relation lattices,215 complete weighted maps and finite characters,19 ordinary-cap drops, and a full nested record. Full source audits are pending at this write time; checkpoint10 should keep its existing fully audited PDF cutoff honest.


UN60 complete root and D written source audits PASS through all C.PR.1--18 and restoration. Root requested the bounded-iterate precision C|delta|(1+|log rho|), now explicit; the existing B absorbs it and every compactness/cluster limit is unchanged. A full source audit remains pending at this cutoff. The complete source stays unassembled through checkpoint10 by root instruction.


UN60 all three independent full-source audits now PASS: root, A and D. A checked every root-torsor quotient, primitive period direction, commuting inverse atlas, exact van Kampen pushout, V_(t^R) determinant, arbitrary fibre-basis change, nested weighted/cap maps, freeness, affine norm bounds, cluster gluing and reverse-record retention. Root also checked the complete executed output. The .inc remains deliberately unassembled for checkpoint10, whose compiled cutoff is212 statements/402 pages throughUN59; the complete UN60 proof/code/metadata is an additional audited source result.


After checkpoint10 current-tree freeze at22:36:08 was released, the fully audited UN60 was copied byte-for-byte to assembled sections/part_C2_hopf_tree_occurrence.tex. The earlier .inc draft remains unchanged. Metadata now points to the assembled source; the frozen checkpoint correctly retains its earlier PDF cutoff through59.

E independently read every block of UN59 and passed the finite linear/eigenvalue restriction, target-frame V transport, exact real-rational logarithm correction, Reynolds character coordinates retaining uv=s^h and s, smooth invariant quotient, conjugate infinity action and all nontrivial finite-linear examples. No correction requested.


E independently read the full extended UN61 and UN62 sources and passed both. UN61 retains arbitrary smooth root P and supplied genus-zero quasi-bundles through its actual incidence pivots, root fibration, integral Chern commutator and compact reconstruction. UN62 retains every original properly elliptic torsor. Its four-triple-fibre example has W=y/s exactly, positive root line O(sumD_i), 3K=q*O(2), and P_(3b)=2b+1.

## C.2.UN.63: complete weighted elliptic-tree/root criterion

Complete source is sections/weighted_elliptic_trees_draft.inc.tex, deliberately unassembled pending full audits. The exact code E_weighted_elliptic_trees.py/.out passed all cases. The criterion retains weighted component lines, sections, finite normalizations, actual elliptic boundary maps and the literal compressed uv=s^h necks. It does not reconstruct arbitrary ruled chains and then assume that they contract.

A cyclic root of an elliptic quasi-bundle has fixed finite-index fibre lattice, an actual connected-fibre Stein base and translation transitions, by the isogeny derivative identity. Its local finite quotient remains smooth-multiple, so pg is the base genus. UN28 bounds the total by one. Nonlinear Hopf roots are given by w=v^q and the exact resonance qr contraction. Thus the reduced root is a genus-zero unicyclic branch or a unique genus-one rooted branch, with the other strict components allowed to be properly elliptic quasi-bundles.

The compressed canonical frame du/u wedge dz gives order difference h(d+1), hence tree increments h*m. Actual collars identify the same integral core period. The finite character of the minimum form is detD; a nonzero nonlinear leading period forces zeta_N^R=detD. The exact inverse torsor maps preserve the full secondary integer and primitive fibre basis. Their boundary pushouts preserve the nearby Z4, forcing M=I or integral Chern zero.

Reflected root cycles are treated by epsilon=minus1, image edge sigma(j+1), and the signed affine equation. Its sum is (D-epsilonI)b-epsilon*u/N inLambda. R=D is diag(rho,epsilon). The exact unitary identity gives finite-equivariant V_(s^R); target-frame affine constants and the explicit cut-chart map C.WT.23a yield an actual global finite action. No finite graph inversion across an edge is allowed because its two endpoints lie over distinct original components.

The finite surgery stabilizer uses its own order d0. Its lift may have d0th power the kth infinite period. The coefficient equation removes only nonresonant lower jets and forces resonant lower jets to vanish, retaining the exact terminal fractional translation k*c/d0. The actual compressed insertion p=x^mZ,xW=s^h adds d(s)s^(ell-hm)W^m and has child displacement delta/s^(hm). The pulled old O(nE) has coefficient nh on the new divisor; replacing it by O(nE_new) would be wrong and is explicitly excluded. The same construction handles a product cap by normalized blowup(p,s^h).

The norm rho=(|p|²+|s|^(2hm))^(1/2m), rho>=|s|^h, gives polynomial distortion dominated by deck contraction. The bounded annulus and logarithmic cluster estimates prove actual proper Hausdorff replacement on affine bases. The final quotient has exact invariant ring C{z,u^B,v^A} and original function x^a y^b. The full conjugate pruning record is also restored at infinity, so that quotient end is smooth by the same charts. All components, maps, multiplicities and root torsors are retained. Root/A/D full audits requested; D independently passed the finite-action blocks and supplied the explicit global middle-map precision now included.


E independently read the complete mathematical proof of UN65 and passed all C.CZ.1--14. The actual triple-point normal line identity, coherent/Euler incidence sums, reduced anticanonical classification, residue/trace bisection obstruction, injected collar groups and extending converse volume form are exact. No correction requested.


UN63 full root written-source and code audit PASS. D also completed a full independent read of C.WT.1--43, including C.WT.23a, and independently executed the entire exact program, all PASS. Root authorized promotion on that final D pass. The complete draft was copied byte-for-byte to sections/part_C2_weighted_elliptic_trees.tex; SHA256 equality was checked and the draft retained. A full-source audit is still in progress. No mathematical changes were made during promotion.


## C.2.UN.67: exact exclusion of the nonminimal rational/Hopf interface

Source part_C2_rational_hopf_interface.tex is complete with C.RH.1--10; code E_rational_hopf_interface.py/.out passed. This closes the parent-assigned rational elliptic-surface obstruction, not merely its minimal case. A rational component P and smooth elliptic boundary J of exact torsion-normal order m give the actual sequences0→O((k−1)J)→O(kJ)→N_J^k→0. For k<m both curve groups vanish; at m the second section is nonzero all along J. Thus |mJ| is an actual basepoint-free pencil. Its Stein degree d would give connected fibre(m/d)J and violate exact normal order, so it is connected; adjunction gives genus one. Disjointness from the other boundary curves makes all of them vertical.

The actual multiplicity-one saturated fields have poles only on those boundaries. The finite-path continuation argument excludes poles of their projected curve fields. A transverse/vertical commuting pair preserves marked periods, or the rank-one return-germ identity gives the same single-valued periods. Thus the actual elliptic pencil has identity integral monodromy. Relatively minimizing it contracts only vertical(-1) curves, leaves that monodromy and coherent Euler unchanged, and permits the precise Kodaira table application. At a full multiple fibre t=u h^a, normalization w^a=u,s=wh is étale; a new vertical(-1) curve would map étale/isomorphically to one below, so relative minimality is retained. The only primitive identity-monodromy Kodaira fibre is I0. The local translation invariant frame gives R1qO=O over the full base, hence chi0, contradicting rational chi1. This is an obstruction on the actual surface and field maps; no analytic contraction of a Hopf leaf or ambient extension of the pencil has been asserted.

All Hopf curves are disjoint. Hence an interface with an elliptic or nonlinear Hopf has no triple point and its actual normal-product map makes the rational-side normal torsion. The new exclusion therefore covers every such Hopf interface, and in particular all Hopf leaves, even with rational double curves and triple points elsewhere. Root and A independently checked the proof before writing; full source sent to root/A/D. The existing primary bibliography key Kodaira1963II is used. I independently opened the publisher record and the original scan text at https://it.scribd.com/document/480913137/kodaira1963-II, reading Theorem6.2 and TableI (primary scan refs turn689view0/turn690view0/turn690view1); the publisher record alone had no readable paper content.


UN67 root full-source audit requested one exact repair to the relative-minimality paragraph, now applied. The earlier inference that an etale image of a rational(-1) curve must be embedded/isomorphic is not used: a nodal or immersed image was not excluded. The replacement proves K.C>=0 on every component of a relatively minimal elliptic fibre using F.C=0 and adjunction; the exceptional square-zero rational alternative contradicts K.F=0. Since the positive sum is zero, every K.C=0. Under the etale root cover K_up=pi*K_down, and cycle pushforward gives K_up.E=deg(E/C)K_down.C=0, contradicting the upstairs(-1) adjunction. Root passes the complete source with this exact replacement.


UN67 corrected complete source has full root/A/D independent written passes. Root independently executed the saved exact code, all passed. The earlier image-embedding inference remains explicitly recorded as repaired by canonical cycle intersection.

## C.2.UN.70: the full nonminimal parent alignment

Complete draft sections/nonminimal_parent_alignment_draft.inc.tex, tags C.NP.1--9, with exact executed code E_nonminimal_parent_alignment.py/.out. The hypothesis is an isolated torsion-normal elliptic boundary J with nonnegative coefficient in the actual canonical section; every parent of a higher Hopf leaf has coefficient m−1. Rational P is now excluded by67. In kappa>=0, the explicit UN31 canonical base line has nonnegative degree, so 0=K_P.J=K_Z.J0+sum positive a_E E.J forces all blowdowns off J. On a Hopf minimal model, all curves have square0, so the square-drop formula forces the same neighbourhood preservation. A nonlinear Hopf model would leave only J after pushing the canonical divisor and contradict its negative canonical axis coefficient.

For the elliptic-ruled case the actual finite-etale base pullback along J makes its lifts disjoint square-zero sections. The rational-fibre identity sum m_i(2+E_i²)=2 forces a vertical(-1) curve away from a chosen section. Contracting such curves preserves it. The final image of every other lifted section has square>=0 by the blowdown formula and <=0 by Hodge index against the preserved nef isotropic section. Equality proves that every contracted curve also missed every lifted section. Thus the survivor in each fibre is precisely the intrinsic component meeting all sections; the exceptional locus and proper contraction are group invariant. The free base action gives the actual smooth ruled quotient. This proves the required descent, without choosing an unproved equivariant elementary transform.

The pushed canonical section forces a second surviving boundary. The actual extension0→O→V→L→0 splits: H1(L^-1)=0 for nontrivial torsion L, or a compact second boundary and finite trace kill the additive torsor when L=O. A finite etale torsion-killing base cover gives E'×P1, whose deck PGL2 map is constant. Its actual quotient is the fixed-Jacobian smooth-multiple elliptic map. Every boundary is vertical, including contracted ones. The original saturated fields on P align the map and kill any remaining linear monodromy; no field pushforward through a contraction is presumed. The retained surface blowups are all vertical and every rational boundary is exceptional. No ambient blowdown is claimed.

Root independently read the entire UN70 draft and passed all maps, signs, equivariance and the precise scope. The code verifies2584 rational-fibre blowup states, positive discrepancies and marked-section square identities; its saved output gives the exact counts. A/D full audits requested. The draft remains unassembled until A pass and root promotion authorization.


## UN70 promotion — 2026-11-15 23:33 UTC

A completed a full independent written-source audit and passed the canonical group-equivariant ruled contraction, Hodge-index equality preserving every lifted section, free-base quotient, split/trace map, original-field alignment, and all retained vertical data. Root had already passed the complete proof and authorized promotion after A and the executed code. The exact output records 2584 rational-fibre blowup states, 210 discrepancy checks, and 90 marked-section square comparisons, all passing. The assembled source is `sections/part_C2_nonminimal_parent_alignment.tex`; the full earlier draft is retained byte-for-byte in `sections/nonminimal_parent_alignment_draft.inc.tex`. This is a surface morphism result: no ambient contraction of the parent is asserted. D full-source audit remains pending.


## Independent UN68 audit — 2026-11-15 23:33 UTC

Read the complete `sections/part_C2_flat_toric.tex` source, C.TC.1–12. Full audit PASS: both actual boundary blowdown maps preserve an anticanonical nodal rational cycle; the minimal ruled/Hopf curve argument and connected rational boundary propagate rationality. The SNC coherent restriction complex is the cellular complex of the actual closed dual surface; Gorenstein duality and chi0 give its oriented torus type. The elementary charge inequality is exact on P2 and F_b, and equality reverses only recorded node blowups, yielding an actual torus action on each original component pair. The global HRR/adjunction count gives zero total charge, so every pair is toric, with r=3v, t=2v and e(S)=2v. No sufficiency for arbitrary toric gluing is asserted. Full PASS sent to root and D.


## UN70 third full audit — 2026-11-15 23:35 UTC

D independently read the entire promoted source and passed every block, including the canonical and square comparisons, the intrinsic fibre survivor and deck-equivariant contraction, finite-trace splitting, exact elliptic quotient, original-field alignment and retained vertical point-blowup record. Root/A/D complete source audits now all pass. No ambient contraction is inferred.


## Independent UN71 full source and code audit — 2026-11-15 23:40 UTC

Read every C.TG.1–15 block and independently opened the original Gross–Siebert arXiv math/0309070v3 PDF. Checked Definition4.3, the full units-to-residues/colimit proof of4.14, Theorems5.2/5.4 and Remark5.6. The last explicitly gives simplicity when the discriminant is empty. Actual angular injection, affine chart transitions, marked constant log-gluing comparison, smooth cone fan, commuting shear maps, free/proper quotient, barycentric unit-polydisc compactness and invariant volume all pass. Independent execution of `code/D_toric_gluing.py` passed every check (240 cone charts,300 shears,20 Cech products,9 holonomies,1800 indices). Exact local-disc and central-log-space scope is retained, without full-germ or compact-base inference.

The separate UN73 proposed compact-middle determinant was independently proved and executed in `code/E_toric_compact_period_audit.py` and `.out`: arbitrary symmetric S plus skew aJ gives the stated four-term determinant, positive for S positive definite since (1−|t|^(2k))(-log|t|)>=0. Both actual exponential-frame limits were also checked: near0 B=I+t^kJ gives b-prime; near infinity B=s^kI+J with reversed Gamma generators gives minus conjugate(b-prime), hence exactly conjugate gluing constants. Full UN73 written-source audit will follow when its file is ready.


## Independent full audits UN69, UN72 and UN73 — 2026-11-15 23:44 UTC

UN69 full written audit PASS: positive-square rationality is compared through the actual minimal map; the exact blowup pencil makes all disjoint boundaries rational; the coefficient/intersection argument excludes every (-1) curve on a strict maximum, and actual surface blowdowns preserve coefficient-one elliptic boundaries. The ruled rational centre would transport a sphere of square -2 into the nearby torus, so it is excluded. Strict rational-edge ascent terminates at an actual plane-line leaf, preserving every other boundary and removing precisely one rational edge per point contraction.

UN72 full written audit PASS: an unequal-height elliptic exit on a component already carrying a higher-genus boundary gives exactly the torsion normal and nonnegative coefficient of UN70. The actual birational elliptic map makes that higher-genus boundary impossible, so ascent stays higher-genus and reaches the actual UN64 section-leaf contraction. After nonelliptic removal, the reduced SNC nearby-cycle formula gives sum e(T_v)=0. The explicit minimal-model Euler terms then force genuinely minimal components before UN66 is used. Every ordinary neighbourhood reversal, the normal extension with df, compact version and intrinsic point/genus balance are exact.

UN73 full written audit PASS: read all C.TX.1–14. Checked the finite angular enlargement, exact real period matrix, four-term positive determinant, proper middle torus family, both exponential quotient maps, variable-constant cone fillings and their volume forms. The base coordinates u=kappa*t and v=kappa/t undo the imaginary period shift exactly. Dividing the vector frame by t^k and reversing both nonangular generators gives minus conjugate(b-prime), hence exactly the conjugate gluing constants. Compact gluing is proper over P1 with no other singular values, and e(Y)=4d. The independent determinant certificate is code/E_toric_compact_period_audit.py and .out. No arbitrary full-germ identification is inferred. All three full PASS reports sent to root and the responsible author.


## Independent UN74 and UN75 audits — 2026-11-16 00:10 UTC

UN74 full written audit PASS. The actual Cartier pullback pi*P-prime=P+T forces a nonzero first normal term, so the marked section gives a smooth parent. The distinct reduced fibre marks give simple zeros for each neighbouring Q-prime, hence the exact transverse charts p=xy,r=x,q=z and f=x^m y^m z^n. The normal extension, the M^m equation, the L canonical equation, and the reduced-maximum splitting have the stated signs. Compact actual contraction and Euler/triple changes also check. PASS sent to A and root.

Independently reread the exact Kulikov1977 restoration passages4.10.8–9 and4.14.5, and Kulikov1981 sections2,8–11. The restored overlap is the restriction of the same finite sigma composite. Its proper graph therefore glues to the identity graph on the unchanged chart, with properness local on each target. This gives an actual global bimeromorphic comparison over the disc and its punctured-family isomorphism; it does not give a single global ordinary-blowup factorization. The primary source imposes no projectivity. Literal VII0 terminology is avoided by the stronger precise Hopf-minimal-model hypothesis in UN75.

UN75 complete written audit PASS. The strengthened Hopf-survival paragraph uses complete exceptional P1 fibres and the actual proper preceding graph; at a generic surviving point the map is nonconstant. A compact projective point fibre has closed generic-degree-one image equal to the original compact component. Hartogs gives the actual canonical-direct-image comparison. The finite level induction terminates, and the retained subanalytic subdivision makes all normal-cone Euler terms and restored-overlap cancellations legitimate. Independently executed code/D_kulikov_records.py: every exact check passed. Full PASS sent to D and root.

Independently executed code/D_compact_toric_gluing.py for UN73: symbolic determinant,588 positivity cases,936 finite angular comparisons, both exact base-scale recoveries and all other checks passed.


## C.2.UN.76 completed and promoted — 2026-11-16 00:19 UTC

Complete source `sections/part_C2_weighted_flat_toric.tex`, retained byte-identical draft `sections/weighted_flat_toric_draft.inc.tex`, tags C.WF.1–28; SHA256 b50eb2ba9012cf1b08d51ada6761cb5096ba30a15ba81e2f909485123c5a9e15. Full written audits by root, A and D pass. The three requested precisions are included: actual tangent-dependent unit transitions glue via normalized blowups of monomial ideals; original component/stratum ray labels make the semistable boundary globally embedded SNC; the double-stratum Euler proof selects a boundary curve dominating the original curve, not an exceptional boundary over a triple point.

The exact root cocharacter lattice is sum m_i v_i=M h. Its old rays have height1; successive height-one stars yield a unimodular toric semistable resolution. Formula sum(k_i+1)v_i−1 gives the same M lambda−1 on every new ray. Primitive canonical evaluation only gives 0<lambda<=1 in a weighted fibre, not min k_i=0. The latter tempting inference was explicitly rejected and replaced by divisibility of Omega/t. The relative central residue gives exp(−2pi i lambda)=detA, so lambda=1 or1/2, and all weights are even in the latter case. Finite etale old-component and dominating-double-curve covers give e=0 on all positive-dimensional original open strata; hence the original support Euler number is its positive triple count.

The central marked log action propagates from the actual compact toric-pair maps and normal-product sections to (z,s)→(a s^b z^A,zeta s). The developed lift has g^M=g_gamma0, not finite order on that cover. Exact period equations retain that extension. The compact period shift changes a0 to a0+iR*d as well as B to B+iRI. Real-linearity is used only for real j/M terms; complex log s stays outside V. At infinity the linear vector frame is det(D)D, the affine vertex is Ap−b and the constant is conjugate(a)^−1. The reflected coarse fan, actual torus inversion and gamma→−gamma recover the conjugate original finite action.

Descent uses finite point stabilizers only. Original Kummer inertia is identity on the tangent stratum and fixes each normal ray; finite order makes its monomial lattice map identity. The constructed unit coefficients depend solely on the root base. Characterwise logarithmic averaging fixes s and recovers the exact old coarse smooth invariant ring. This proves compact occurrence of the marked reduced log support and all full weights. The actual original morphism recovers the original nonreduced analytic fibre, but the new compact period units were not matched to its higher jets; no whole-germ or arbitrary thickening identification is claimed.

Executed `code/E_weighted_flat_toric.py` and `.out` passed all checks. One initial verification run was interrupted because unsimplified iterative symbolic matrices expanded exponentially; the exact recurrence was expanded at each step and rerun successfully. This changed no identity. The code checks648 rays,1851 points,1923 unimodular cones,1974 canonical valuations,3084 character cosets,3172 primitive ratios,420 finite averaging jets and42 exact finite-action iterations, plus the full determinant and both central base corrections.

Independent full UN78 written audit PASS was sent to D. Its root valuations and affine minimum, finite birational action retained through inverse-before-quotient reconstruction, d_I*nu_I stratum degree and Bezout volume, signed Euler formula and compact root record all check. Requested the same monomial-ideal and globally labelled-ray precision and corrected a literal TeX left token; code rerun follows when saved.


UN76 root independently reran the complete exact program and passed all checks; its output is retained at build/root_UN76_code_rerun.out. Full source remains accepted with the three precision additions now in the promoted source.

UN78 independent execution completed on2026-11-16 at00:21UTC. code/D_rooted_kulikov.py passed3330 Bezout/simplex volumes,3330 cyclic stratum-cover averages,216 Pick triangulations,49977 canonical ray/minimum comparisons,100 chain Euler computations,1120 positive toric examples and6426 root/resolution/core balances. The corrected source now contains normalized monomial blowup gluing, global component/stratum labels and the repaired left delimiter. Complete written and executed audits both PASS.


## Independent intrinsic UN78 and full UN77 audits — 2026-11-16 00:29 UTC

UN78 added C.RK.18–22 full PASS. The root cover is defined by the actual local normal-line powers and unit transition maps, so no nonexistent global meromorphic frame is required on a nonalgebraic surface. The ratio w=s^(N/n)/g_j is integral by the displayed monic equation and extends on the normal root; its strict component gives the actual birational resolution of the fixed finite normal cover. GAGA algebraizes finite coherent algebras over projective exceptional surfaces, ruling out any new Hopf root covers. Proper change of variables for |f|^(−2c)|Omega|² gives exactly min(k_i+1)/m_i and logarithmic divergence at equality, making the condition intrinsic. Only two typography commas were corrected.

Read the complete promoted UN77, including C.HM.10, and reopened Kulikov1977 sections4.11.2,4.14,4.16.2 and Kulikov1981 section8 from the primary PDFs. Full audit PASS after the explicit diagnostic-resolution precision: Lemma4.14's old smooth ruled surface is on an auxiliary resolution used only to check its hypotheses. No diagnostic divisor enters the actual modification record, card labels or canonical-order bound. The corrected1981 maximal-old-order clause gives connected boundary and no inserted links directly. The last-descendant argument supplies condition(e), and the proper sigma-record is the actual4.14.5 restoration.

The effective anticanonical point-map induction, coefficient-one isolation/leaf assertions, rational self-double sum−1 contradiction, typeI/typeII receiving-degree comparison, positive-order ruled third case, and block-level lexicographic termination all check. Independently executed code/A_maximal_hopf.py:4298 states,4753 transitions,41 normal-degree checks,900 self-double contradictions,1275 positive-level identities and5832 block potential comparisons all pass. Full written+executed PASS sent to A and root.

## The zero-coefficient boundary obstruction and its exact resolution — 2026-11-16 00:57 UTC

The first proposed aligned-parent argument incorrectly identified actual boundary with the nonzero support of its canonical divisor. Root caught the zero-coefficient case. The exact local countermodel is Tot(O_P1(-1)_a plus O_P1(-2)_b), with homogeneous base coordinates[U:V] and actual function f=bUV. The zero section E lies generically only in P=(b=0), meets the two other boundary surfaces once each, and has normal(-1,-2). K is the pullback O(1), so an actual canonical section has orders(0,0,1). Its regular local fibre is C times C-star. This is an actual obstruction to that local inference; it was not called a compact torus counterexample until D constructed and verified UN79.

There is an exact arbitrary-neighbourhood modification of this local configuration: the split normal extension gives F1 after Bl_E, and P∩F is its negative section with ambient normal(-1,-1). The type-II flop blows E down on P and makes F into P2 with normal O(-2) and two boundary lines. Both receivers are point-blown-up twice, first by Bl_E and then by the flop. The initial count of only one receiving blowup was corrected after A's independent toric chamber calculation. No smooth point contraction of this O(-2) plane was asserted. This move is retained as an exact local calculation, but is not needed in UN81.

A's UN80 supplies the required global torus input. A constant combination of the actual saturated ambient fields descends to the nowhere-zero invariant translation field on the UN70 minimal quasi-bundle. Rank one uses lambda_i=d_i−c_iH; rank two uses commuting projected fields and preserved time periods. The actual translation multiple-root charts extend it without zero. At every exceptional valuation, D(w)=0 forces tangency while D(z)=1 forbids it, so every point-exceptional prime must be a polar divisor, hence actual boundary. This conclusion concerns the specified point map; D's compact UN79 curve is horizontal for that map.

Full UN80 source and independent code audit PASS (final labels C.EP.1–11). Full UN79 written and independently executed audit PASS: the cubic root of the nodal elliptic surface, its exact two A2 charts, the global rational-curve blowup, generator orders, the explicit genus-three balancing curve and all transverse intersections check. Its complete target neighbourhood is untouched by the later centres; the final six components have Euler numbers0,4,4,6,6,−8, double-curve Euler24 and12 triples, giving support Euler0. The actual horizontal degree-one map is part of the statement.

## C.2.UN.81 complete draft and executed certificates

The complete proof is in sections/aligned_parent_reduction_draft.inc.tex, C.AP.1–14, pending full independent audits. It concerns only actual torsion-normal interfaces with strictly higher maximal minimal Hopfs; it does not assume that an equal-order diagonal-a0 plateau supplies such an interface. UN70 and UN80 apply to the actual normalization with every boundary branch retained. All full fibre graphs have rational valence at most b+1 and elliptic-root valence at most b, where square is minus b. A last node flop has opposite receiving square at least0 (at least1 for an elliptic root), so neither receiver can be another designated aligned parent. The total designated point defect strictly drops.

For a zero-triple last point, the other square is+1 and the exact linear system |E| gives Q→P2, retaining E as a line. Its other actual boundary equals the positive discrepancy divisor, so all exceptions are boundary and every receiving order is strictly higher. The plane subprocedure stops at its FIRST whole-component removal, then completes the already checked finite sigma cleanup. Before that removal, plane type-II steps strictly decrease total surface b2 by increasing canonical order, and zero-triple calls raise the order by2. This is a finite progress block; it does not claim that its initial plane marking survives an arbitrary later global cleanup. One-triple cases use the actual ruled-removal block directly.

The outer potential is(c1,...,cM,h_aligned). Whole removals reduce its card part and may reset h; direct aligned flops reduce h and preserve cards. Maximal Hopf neighbourhoods are untouched because a removed ruled component's section parent has order q−1<M and every other boundary is rational. No such component meets a minimal Hopf of order M. The designated parent primes therefore survive, their markings persist, and at the endpoint their defect is zero. Rational self-incidences cannot remain on their minimal vertical models, while the actual moves introduce no elliptic self-incidence.

Code E_aligned_parent_reduction.py/.out passed79032 full-fibre vertex identities,22928 last-point boundary cases,17002 exact opposite-square comparisons,300 plane defect comparisons,110 outer direct decreases and4059 whole-removal lexicographic checks. The analytic contractions are proved in the text and the cited actual diagrams; the program does not infer them from graphs. Root/A/D full reads requested. A requested that rationality of a +1 receiver be proved without assuming it is a maximum; the direct minimal-canonical/ruled/Hopf comparison is now explicitly included.


UN81 full written audits by root, A and D all PASS. D independently executed the complete exact program, all checks passing. The input now explicitly permits the retained NC endpoint of UN77, with its labelled normalization branches. The plane divisor comparison explicitly takes the ratio with the pullback of the form of divisor minus three times the marked line: its exceptional-only divisor pushes to zero on P2, so the ratio is constant. This certifies the actual discrepancy identity. Promoted byte-for-byte to sections/part_C2_aligned_parent_reduction.tex, with the complete draft retained.


## Independent complete UN82--84 audits — 2026-11-16 01:18 UTC

UN82 full written and independently executed audit PASS. The maximal effective-anticanonical divisor containing one isolated coefficient-one elliptic curve is entirely reduced and elliptic on the rational, irrational-ruled and Hopf normalization cases, using the actual point-map and residue comparisons. Its propagation forces the entire connected support to have the same canonical order, hence order zero by primitive evaluation. Therefore a positive maximal minimal Hopf is a terminal torsion-normal leaf. The exact script passed1207 weight identities,627 triangular cases,728 quadratic cases,29 nonlinear cases,3009 point-map states and3160 height comparisons.

UN83 full written and independently executed audit PASS. The sign-free isolated torsion interface has an actual point map to a fixed-Jacobian smooth-multiple elliptic model, a nonlinear Hopf with its preserved axis, or a one-section elliptic ruled bundle with its actual extension class. The degree-at-least-two ruled case uses an actual finite etale base cover, disjoint sections, Pic0 and trace to construct the elliptic pencil; it does not assume an equivariant elementary transformation. The degree-one case retains the full extension. Exact code passed443 fibre graphs,100 normal-divisibility comparisons and1500 height identities.

UN84 full written and independently executed audit PASS. I reopened Kulikov1981 section7 and section8 from the four-page primary PDF and checked the exact current-maximum hypothesis: the candidate search uses ruledness only at the current maximum. While that order exceeds the largest Hopf order, adjunction supplies that ruledness. The candidate removed may have lower positive order, so the full positive card vector is retained. Actual missing-fibre insertions have order q+1, no additions occur at the current maximum, and the protected Hopf primes and canonical orders survive the proper comparison maps. Finite cleanup produces the recorded NC input to77. Exact code passed728 updates,2667 records/10644 steps and10000 self-branch comparisons.

## C.2.UN.85 global reduction — complete proof and executed checks

Draft source sections/global_torus_reduction_draft.inc.tex, tags C.GP.1--10. The positive-Hopf branch starts with84 and82 and protects one actual maximal minimal Hopf neighbourhood. A component is recognized only after recording the actual point model of83, its entrance curve and all normalization branches. The recognized models have negative-square rational boundary and nonpositive-square elliptic boundary. The fixed potential is(c1,...,cM,u,d), where u counts unrecognized global primes and d sums exact point-map defects. Direct type-II changes preserve all recorded models and lower d, a new recorded comparison lowers u before any finite defect increase, and whole positive component-removal blocks lower the card vector and may reset every recognition except the protected Hopf. Thus no assertion about future numerical eligibility is required.

At an NC stage the complete fibre canonical coefficients include unmarked coefficient-zero vertices. Their shifted adjacent coefficients are primitive under the actual consecutive/sum blowup rules. This excludes the nodal image of a chosen last exceptional curve and the three-source branch case. A single-source image node would already be a node of the smooth exceptional P1. A rational self-double cover splits; the actual branch labels therefore give the two smooth local surface germs and the (-1,-1) normal neighbourhood. If both source germs belong to one global recognized prime, its point map factors through both disjoint normalized contractions and its defect drops two, with the prime counted once.

One attempted stronger discrepancy-tree inequality n<=b-1 was rejected before promotion. Blow up an off-boundary point, a point on its exceptional, and then their node: the last exceptional has square-1, valence2 and discrepancy4. The exact invariant is n<=b+1, which gives receiving square b+1-t>=0 and is fully sufficient to exclude already recognized receivers. This correction affects no promoted theorem. A withdrew the stronger suggestion, and the explicit counterexample is retained in the new program.

The endpoint has no rational boundary, hence no new rational NC self-incidence; the actual one-horizontal-section comparison excludes new elliptic self-incidences. It is embedded SNC with no triples. Quasi-bundle edges retain their common Jacobian through the actual inverse normal-root maps; nonlinear leaves retain their UN50 period covers. UN28 permits at most one genus-one base. UN47 gives component-to-support surjectivity and kills that component in the actual support-to-graph fundamental-group quotient, forcing a tree in the genus-one case. The actual support data then lie precisely in61/62. Every endpoint component and double curve has Euler zero.

The all-minimum-Hopf branch uses75 and the canonical-flat65/68/71 cores. The full inverse record reconstructs the original family from its ACTUAL endpoint germ. Compact occurrence of the classified central spaces is supplied separately by57/61/62/73; no identification of arbitrary higher analytic jets and no transfer of an inverse record to a different smoothing is asserted.

Executed code/E_global_torus_reduction.py and .out passed16090 positive-discrepancy vertices,2744 actual transitions,1852 receivers,26750 complete-fibre canonical states,129925 shifted-edge checks,101 same-global double-source comparisons,8470 direct defect decreases,30976 recognition comparisons,248040 whole-card resets,60 finite adversarial records with39441 steps, and771 incidence graphs with3035 frontier steps. I also independently executed A_nc_interface_branches.py:43870 states,43829 transitions,213077 shifted-edge checks and every rational NC image comparison PASS. Root full written audit PASS; A/D complete-draft audits have passed and final precision confirmations are pending at this note's timestamp.


UN85 final full written audits by root, A and D all PASS. Root and D independently executed the complete program with every check passing. The final source includes the full-fibre coefficient-zero convention, all three NC triple-source patterns, split rational double cover and actual surface germs, the same-global-prime double contraction, exact graph fundamental-group comparison and separate nonlinear leaf period cover. Promoted byte-for-byte to sections/part_C2_global_torus_reduction.tex with draft retained. SHA256 c410b0cc646c02a22c8cb134a6c8b0a44ddded03773f6eea6da2d301f97b3b44. Metadata records F16 and the exact actual-endpoint/higher-jet scope. The only final layout adjustment split the two definitions in C.GP.6 into gathered rows.


Final source audit repaired the UN21 equation namespace: all28 C.SK occurrences in part_C2_secondary_kodaira.tex were renamed C.SKD to remove the collision with the independent C.3 exclusion. The entire pre-rename source is retained at records/versions/UN21_before_SKD_tag_rename_20261116.tex. No algebra or assertion changed. E_references.bib now explicitly marks its four previously checked sources verified. Schuett--Shioda Section7.6, printed33--34, was independently reopened from arXiv0907.0298v3 and checked: section translations extend over singular fibres. Its verified note records that exact scope; the manuscript also proves the actual extension graph separately. The original bibliography is retained at records/versions/E_references_before_verification_markers_20261116.bib.


## Complete unrestricted generation UN86 — final independent audit, 2026-11-16 01:29 UTC

Read the entire written source sections/part_C2_complete_rooted_generation.tex, C.AR.1--16. Full audit PASS. The admissible input consists of an actual classified core atlas and punctured torus comparison, explicit inverse sigma charts with restored overlaps, the regular cyclic action after reversal, labelled root coarsening and smooth invariant rings, and ordinary smooth target maps. These are checks on supplied analytic maps and do not assume an additional original family. The quotient of the freely permuted nonzero root fibres is biholomorphic to any one fibre. Properness, flatness and connectedness follow from the retained proper maps and the explicit smooth target function. The inverse record is applied before quotienting; all higher jets remain in its actual source atlas.

The normalized root-stratum Euler is exactly d_I times the simplex volume nu_I. Combining it with the ordinary blowup and forward sigma changes gives e_original=e_core-Delta_sigma-R_N-Delta_pi with every sign fixed by actual arrows. The zero-Euler subfamily is consequently selected within an exhaustive geometric construction, not merely by a numerical assertion detached from existence. The fixed original normal covers, projectivity of all exceptional finite covers, and the density threshold give h=N(H-tau), independent of embedded resolution and divisible root exponent.

The initial compact paragraph allowed the global root to acquire singularities at other bad fibres. Root and I independently identified this precision. The final written correction uses the exact restriction sequence for O_B(dp-2c-sum other critical values), with its H1 vanishing by Serre duality, to prescribe a=t+O(t²) at c and a=1 at all other critical values. Its pole p is regular. Thus the cyclic cover is etale over other critical fibres and ramifies elsewhere only over smooth fibres. Its normalized total space is smooth away from the selected root tube. The exact local comparison for a=t*u(t) is s'=s/u(t)^(1/N), choosing the analytic root with value1 at zero; it respects the cyclic action and all retained charts. The old paragraph is preserved by root before editing.

Independently executed code/D_complete_rooted_generation.py:24486 primitive canonical/descent checks,166782 intrinsic normal-cover/root-scaling cases,61930 invariant monoid comparisons,258 stratum volume/sheet averages, the symbolic four-space signed Euler identity and6336 zero-balance reconstructions all PASS. Final written compact addition reread and passed. Completion judgment sent to root: UN85/86 provide exhaustive finite geometric generation for unrestricted C.2, including an exact zero-Euler subfamily and actual reconstruction of every supplied family; no uniqueness of reduction record or unproved identification of endpoint transverse jets is asserted.
