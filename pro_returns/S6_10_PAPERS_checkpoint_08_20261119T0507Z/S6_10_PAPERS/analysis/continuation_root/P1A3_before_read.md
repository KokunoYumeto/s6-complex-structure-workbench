# P1A.3: tangent cohomology and actual Kodaira--Spencer class

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.
This derivation is written from `P1A3_statement_input_packet.md` before
opening the P1A.3 proof. It uses P1A.1, the explicit connection and cusp
charts, and the already opened analytic Serre/Douady theorems. No
critical-ideal or tangent-computation program has been opened.

## 1. An exact dual description of the tangent cohomology

The wedge pairing gives a pointwise perfect pairing
T_M tensor (Omega^1_M tensor K_M) -> K_M, by contraction of a vector
with the one-form factor. Analytic Serre duality therefore identifies

    H^q(T_M)^dual = H^(4-q)(Omega^1_M tensor K_M).

Here K_M=h*L^-6 by P1A.1. This is the explicit bundle pairing and
cohomological morphism that permits the computation below.

The logarithmic cotangent sequence derived directly from the toric
charts in the preceding P1A.2 prereading proof, tensored by h*L^-6, is

    0 -> h*L^5 -> Omega^1_M(log D) tensor h*L^-6
      -> h*(F tensor L^-6) -> 0.                         (T)

It uses K_B(a)=L^11, whose actual meromorphic-frame identification
was computed there: kappa=d lambda/(lambda-a) equals lambda^9 times
the canonical L^11 frame. This sequence remains exact on finite root
charts because they descend through the specified free group action.

## 2. Cohomology of the two end terms

P1A.1 and projection formula give the direct images after tensoring
with wedge^j G. For an L^n summand the coarse degree is
d(n)=floor(4n/5)+floor(-3n/4).

For h*L^5 the weights in the four relative degrees are

    j=0: 5;
    j=1: 5,4,3;
    j=2: 4,3,2;
    j=3: 2.

The weights4,5 have coarse degree0;2,3 have degree-1. Thus the only
nonzero base cohomology is H0, and the absolute dimensions are
(1,2,1,0,0).

For F tensor L^-6, the three weights are -4,-5,-6. After tensoring
with wedge^j G all resulting weights lie between -9 and -4. The
weights-4 through-8 have degree-1, while d(-9)=-2. Weight-9 occurs
once in j=2, from the weight0 direction of F and the G weights-1,-2,
and once in j=3, from the same F direction and all three G factors.
There is no H0, and each of those two degree-2 line bundles contributes
one H1. The absolute dimensions are consequently(0,0,0,1,1).
The Leray sequence has only two base columns, so no further differential
can change either calculation.

The nonzero end-term cohomology groups of (T) occupy disjoint degrees,
and every possible connecting map has a zero target. Therefore

    h^q(Omega^1_M(log D) tensor K_M)=(1,2,1,1,1).

## 3. Removing the logarithmic pole by its actual residue

Tensor the branch-normalization residue sequence with K_M:

    0 -> Omega^1_M tensor K_M
      -> Omega^1_M(log D) tensor K_M
      -> nu_* O_Y tensor K_M|D -> 0.

The last twist is a constant one-dimensional fibre because K_M is
pulled back from the base and D lies over the single point a. The
smooth complete toric normalization Y has H0(O_Y)=C and no positive
cohomology by the opened zero-divisor form of Demazure vanishing.

The sole global section of the logarithmic middle term comes from
h*L^5. In the fixed frames it is

                  lambda^-5 kappa tensor (L^-6 frame).

Indeed the unique L^5 generator is lambda^4, and kappa contributes
lambda^9. Its residue at lambda=a is a^-5 times the nonzero L^-6
frame. Thus H0 of the middle term maps isomorphically to the residue
C. The long exact sequence gives

    h^q(Omega^1_M tensor K_M)=(0,2,1,1,1).

Applying the exact duality of step1, with indices reversed, proves

                      h^q(T_M)=(1,1,1,2,0).

Every group here is determined by a displayed line-weight calculation,
the actual nonzero residue, and a specified perfect pairing. Neither
an Euler-characteristic fit nor a vanishing of H2(T_M) is used.

## 4. Nonzero class of the actual parameter family

Take the smooth fibre A over lambda=1. The base parameter and the
complex family parameter xi give two actual period-plane derivatives.
In the supplied frame, the family plane has columns
w2,w1,w0+(625 pi i/96)xi e. Differentiating in xi and projecting
to H/F gives the rank-one nonzero map P:F -> G sending only the
weight0 generator to (625 pi i/96)e.

The base derivative is obtained by projecting Gamma6, as in the
preceding derivation. For c=-i xi, r=625 pi c/96, its logarithmic
matrix at lambda=1 is

    Q_1=(1/3125) [ A B 0; 120 0 125/2; 0 120 50 ],
    A=-78125/6+300r, B=-390625/48-375r.

Direct expansion gives det(Q_1)=3/625. The derivative with respect
to lambda rather than kappa has the nonzero scalar factor
1/(1-a), so its rank is3 for every parameter.

These are precisely the torus deformation classes: differentiating
the lattice-translation gluing on the universal cover gives its
translation-valued Cech1-cocycle. Contracting it with a relative
one-form is the projected derivative of that form in H/F. This
identifies H1(T_A) with Hom(F,G) and sends the xi and base cocycles
to P and Q_1/(1-a), with the same sign convention on both maps.

The normal tangent sequence on this actual smooth fibre is

    0 -> T_A -> T_M|A -> O_A tensor T_(B,1) -> 0.

Since H0(O_A)=C, the kernel of H1(T_A)->H1(T_M|A) is exactly the
line spanned by the base Kodaira--Spencer class. The rank-one
nonzero matrix P is not on the line spanned by the invertible
matrix Q_1/(1-a): every nonzero scalar multiple of that matrix
has nonzero determinant, whereas det(P)=0, and P itself is nonzero.
Thus the image of P in H1(T_M|A) is nonzero. The restriction of the
global parameter Kodaira--Spencer class is this image, because its
lattice gluing cocycle restricts to the same torus cocycle. Its
global class in H1(T_M) is therefore nonzero.

The local compact family used here is the one actually specified by
the packet: the finite affine numerators remain fixed, and the toric
deck multipliers exp(2 pi i C(q,xi)nu) vary holomorphically with xi.
On a small parameter neighbourhood, the same finite fan charts and
uniformly bounded holomorphic C give the given proper filling. These
chart maps define the deformation; no unrelated abstract tangent
direction is substituted for its Kodaira--Spencer class.

## 5. The miniversal germ, including possible nilpotents

The opened Douady existence and semiuniversality theorem gives a
miniversal analytic germ R with tangent space H1(T_M)=C. Therefore
its local ring has a minimal presentation C{u}/I with I contained
in(u)^2. The actual parameter family induces a classifying map from
a disc with coordinate s to R. Its tangent map is nonzero by step4.
On rings it sends u to g(s), with g'(0) nonzero.

Substitution C{u}->C{s}, u->g(s), is an isomorphism by the holomorphic
inverse-function theorem. Since it factors through C{u}/I, its kernel
contains I; its kernel is zero, so I=0. Thus R is the smooth
one-dimensional germ and the classifying map is a local isomorphism.
This proves that the supplied family is miniversal at every member.
The ring argument also excludes a hidden nonreduced obstruction ideal.

## Next checks

The complete derivation is now written before the P1A.3 target proof
is opened. A fresh exact program will enumerate the line weights,
check the unique nonzero residue exponent and verify the determinant
and rank comparison, then the printed proof will be compared.
