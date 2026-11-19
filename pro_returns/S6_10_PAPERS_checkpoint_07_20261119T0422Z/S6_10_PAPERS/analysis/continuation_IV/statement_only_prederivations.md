# Statement-only derivations for checkpoint36 K109–K119

Written 19 November 2026 by GPT-6 Astra (OpenAI), ChatGPT Pro mode,
effort Pro, S6_10_PAPERS continuation. The input at this stage is solely
the eleven statements and dependency IDs in the verified checkpoint36
results CSV. None of their eleven named proof files or producer programs
has been opened. These are mathematical substeps, not whole-proof checks.

## K109, K110, K113 and K114: endpoints

For y²=x³+rx²+tx+t², the Weierstrass cubic discriminant is
t²[-27t²+(18r−4)t+r²−4r³]. Thus the finite simple-node quadratic
is 27t²+(4−18r)t+r²(4r−1). Its discriminant is
16(1−3r)³. For r≠0,1/4,1/3 both roots are distinct and nonzero.
At r=0 the remaining selected root is −4/27, as in K114.

The tangent to G=(0,t) has slope 1/2, so the third intersection of
y=t+x/2 with the cubic has x-coordinate s=1/4−r. Therefore 2G
has coordinates (s,−t−s/2), and
f₂=(y−t−x/2)/(x−s) has divisor 2[G]−[2G]−[O]. The translated
products in the statements must be checked with their actual arguments;
the divisor identity alone does not establish all cap coefficients.

The endpoint quotient requires an affine source lift, its inverse,
preservation of the integral period lattice, and extension across all
completed charts. A statement that the physical scalar action extends
does not by itself prove surjectivity onto the whole automorphism group.
The intended comparison is a map from that C* to Aut_hol(X); its kernel
and every other automorphism must both be computed. These obligations
will be compared to the printed proofs, with no group equality assumed.

For the M2 primitive endpoint write E_R=(R^(−l)S)^n. At the three
successive root values R,ζ₃R,ζ₃²R, the product of scalar factors is
R^(−3ln)ζ₃^(−3ln)=λ^(−n), since m=3l and n=±1. The remaining
chronological source-line product is S³ or its actual inverse; the
claimed q B₀^(−1) must be established as a full coefficient identity.
For n=−1 the coefficient has to be evaluated at the inverse source point.

## K111 and K112: selected-I3 characteristic arithmetic

K111's numerical pair gives (4·71−(−4))/24=12 and
(μ,ν)=(ℓ/4,k−ℓ/4)=(−1,72). This validates the conversion,
not the geometric calculation of k=71 and ℓ=−4.

In K112 the displayed polynomial k_j=11−6j³+24j²−30j, ℓ_j=−4
gives (4k_j−ℓ_j)/24=2−j³+4j²−5j. At j=−1 the values are
k=71, S=12; at j=0 they are k=11, S=2. The stated native-arrow
increment (15,−10) must therefore carry index −10 in the stated
orientation. The whole 28-class fan conclusion needs the complete
paths with their integer prism sums, not only the vertical polynomial.
The polynomial is periodic modulo28 after replacing j by j+28;
enumerating exactly one period is therefore exhaustive for the vertical
image. New code will compute that image before the proof is opened.

## K115: marked-node parametrization and scalar-return arithmetic

Substituting r=(1−ω²)/3 and t_c=(ω−1)²(2ω+1)/27 in the finite
node quadratic must give zero identically. The omitted ω values account
for the double-root/collision cases; the remaining r=0 lift is ω=−1,
with selected t_c=−4/27, while ω=1 is omitted.

For M6, m=3l+2 and (k,ℓ)=(18m−3m j(j−1),24(l+1)) gives
S=3m−(l+1)−m j(j−1)/2=8l+5−m j(j−1)/2. The integer
j(j−1) is even. For M2, (k,ℓ)=(2l−3l j(j−1),8l) gives
S=−l j(j−1)/2. Thus the M2 T₂ integer is −l, so its covers
produce the subgroup lZ/28; inclusion for every other fan still requires
the full integer fan recurrence.

For M6 T₀ gives 8l+5, always odd and prime to7 unless l=2 mod7.
At those l, T₄ gives −10l−7, still odd and congruent1 mod7. These
are units modulo28. Their powers therefore produce every residue, once
the prescribed actual endpoint is established for that fan.

## K116 and K119: OS45 polynomial loci

The curve v²=4u³+3 has a nonsingular projective completion of genus1:
the cubic has three distinct roots and odd degree, so its two-sheeted
map to the u-line has four simple branch points. Riemann–Hurwitz gives
2g−2=−4+4=0. Removing N distinct points gives the familiar one-relator
surface presentation with two handle generators and N based meridians;
the exact list of 48 points, disjointness and base paths remain to check.

The proposed unselected-II polynomial has degree6 in u. With z=u³,
16z²+120z+243 has two nonzero, distinct roots. Neither equals −3/4,
because the value there is162. Each z therefore gives three distinct u
and each u gives two distinct v: exactly twelve ordered points.

At t=0 the OS45 cubic discriminant is proportional to 16a³+3.
Substitute a=−u(u³+3)/9: its zero locus is
2187−16u³(u³+3)³=0. The displayed factorization in K119 can be
verified directly. In z=u³, the factors 2z−3 and
8z³+84z²+342z+729 have total degree4. Their roots must be distinct,
nonzero, and different from −3/4. This gives twelve u and twenty-four
ordered v points. t_c=(3−2u³)/(6u) vanishes exactly at z=3/2,
giving three u and six v points; eighteen remain with nonzero selected
height. Differentiating the nodal discriminant equation at t=0 gives
dt_n/da=−2a when 16a³+3=0. The new exact program will verify these
identities and nonvanishing using polynomial gcds and remainders.

The zero-return conclusions need an actual extending family and its
endpoint comparison. Algebraic root counts alone do not establish them.
For the K119 displayed arrows, F₁E_XF₀^(−1)=C E_Y implies
E_X^(−1)F₁^(−1)=F₀^(−1)E_Y^(−1)C^(−1); composition with P_YF₀
gives exactly the stated conjugacy identity. An extending C* action has
the path exp(θ log C), for any chosen logarithm of the constant C.

## K117: exact target-prism solution

All weights w_i are assumed nonzero only in the displayed nonzero-weight
formula. The proposed symmetric matrix
V_rs=(I_r/w_r)δ_rs+C/(w_rw_s) satisfies
V(w_i e_i−w₀e₀)=I_i e_i−I₀e₀, because its rank-one term cancels.
Likewise δ_r=(J_r+E)/w_r gives
w_iδ_i−w₀δ₀=J_i−J₀. The prescribed entries V₂₂=a and
δ₂=2a−b then force C=w₂²a−w₂I₂ and E=w₂(2a−b)−J₂.
Uniqueness follows because a symmetric matrix vanishing on both
w_i e_i−w₀e₀ is a multiple of (1/w_r)(1/w_s), while the remaining
diagonal condition fixes that multiple; the analogous one-dimensional
argument determines δ. Integrality and the geometric identification of
these data remain separate checks of the actual fan maps.

The claimed vertical pair gives (4k−ℓ)/24=−1−3j(j−1), and the
native relation k=μ+ν, ℓ=4μ gives (0,k). For the ordered cover,
u³=(v²−3)/4. Near v=0 the first derivative of a(u) vanishes at
u³=−3/4, while the second derivative is nonzero. Since u−u₀ has
leading order v², a−a₀ has order v⁴; a positive v-loop has four
positive a-turns. Exact leading coefficients are left to new code.

## K118: two-cap integrality and table conversions

Use the actual Bezout equation h n∞+m n₀=ε, ε=±1. It entails
gcd(m,h)=1. On the four displayed domains J₀=mh/b equals respectively
2kl, l(4k+1), 2k(3l+2), and (3l+2)(4k+1), all integers.
For b=6 or2, the parity of the Bezout equation gives m n₀=ε mod2;
therefore (3ε−m n₀)/b is integral after the explicit factor3 when
b=6. For b=3 the factor3 is explicit; for b=1 it is immediate.
The exponent J₀(b−1)/2 is respectively 5kl, l(4k+1),
k(3l+2), and0, again integral.

Substitute every displayed (k_phys,ℓ_phys) into (4k−ℓ)/24 and
compare it symbolically with its S₀. Substituting the vertical variation
Δk=−3J₀j(j−1), Δℓ=0 gives ΔS=−J₀j(j−1)/2. The stated
whole-fan image still needs the actual fan recurrence and endpoints.
The sphere and mapping-torus identifications need the given orientation
morphisms; the table arithmetic alone is not their proof.

## Evidence boundary

This file records independently obtained substeps and open proof
obligations before the printed proofs were read. It does not certify any
of the eleven whole statements. Source status Proved remains historical;
receiving status stays open until the relevant full proof is checked.
