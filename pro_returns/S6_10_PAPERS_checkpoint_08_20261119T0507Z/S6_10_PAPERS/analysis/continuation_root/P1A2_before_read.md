# P1A.2: Hodge-table derivation before reading the target proof

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.
The target statement and construction-input packet supplied by the Paper V
owner were read. No P1A.2 proof or producing program has been opened.
Earlier progress messages had exposed that two determinant tests have
exceptional value c=5/(3 pi); the matrices and their derivation below
were independently obtained from Gamma6 and the chart definitions.

## 1. Base line bundles and the actual logarithmic extension

Put a=-256/3125 and kappa=d lambda/(lambda-a). On the root base of
orders4 at zero and5 at infinity, L=O(4D_infinity-3D_zero).
The divisor of kappa as a logarithmic differential is
3D_zero-D_infinity. Since div(lambda)=4D_zero-5D_infinity,
the identification K_B(a)=L^11 sends kappa to lambda^9 times the
specified meromorphic L^11 frame. This fixes the scalar and monomial
convention, rather than only the rational degree.

The supplied F is L^2+L+O and G=O+L^-1+L^-2. Write r=625 pi c/96.
In the ordered flat frame (e,w2,w1,w0,w-1,w-2), F has columns
w2,w1,w0-r e. The quotient H/F has coordinates
(x_e+r x_w0,x_w-1,x_w-2), with precisely the G line weights.
Projecting the derivative of these three columns through Gamma6 gives
the logarithmic Kodaira--Spencer map K:F -> K_B(a) tensor G.
Relative to kappa and the stated meromorphic frames, its matrix is

    (1/3125) [ A/lambda^2   B/lambda      0
               120/lambda^3   0        125/(2lambda)
                0         120/lambda^3  50/lambda^2 ],

where A=-78125/6+300r and B=-390625/48-375r.
For example the first coefficient is b(w2)+r Gamma_W(w0,w2),
and the first quotient coordinate formula gives every other entry.

The chart identity q=z0 z1 z2 z3 gives the exact sequence

    0 -> h* K_B(a) -> Omega^1_M(log D) -> h* F -> 0.

Indeed the injection sends dq/q to sum dz_i/z_i; the quotient has
the three logarithmic torus characters. The finite root charts are
smooth after their prescribed free action, so the same sequence descends
there. On overlaps the period translation changes a lifted relative
one-form by its differentiated period times the base differential;
its extension class is therefore the actual projected matrix K above.
Exterior powers give, for p=1,2,3,

    0 -> h*(K_B(a) tensor wedge^(p-1)F)
      -> Omega^p_M(log D) -> h*(wedge^p F) -> 0.       (L_p)

In a local split frame, replacing one factor f_i by its base-valued
transition adds (-1)^i K(f_i) wedged with the remaining factors.
After cup product with a class in wedge^q G this is the connecting
map, with insertion into the G wedge and its ordinary exterior sign.
Thus the global maps used below have been derived from the actual
transition sequence, not inferred from the desired Hodge dimensions.

## 2. Global connecting maps and their ranks

For L^n, the coarse divisor is
floor(4n/5)[infinity]+floor(-3n/4)[zero]. A meromorphic section
lambda^k times the fixed frame is holomorphic exactly for
ceil(3n/4)<=k<=floor(4n/5). All relevant coarse degrees are either
-1 or0, so their H1 is zero. In weights -3 through3 the sole H0
weight is0; in weights8 through14 the sole missing H0 weight is11.
This uses the exact root-frame multiplication, with invariant
pushforward exact over characteristic zero.

By the supplied P1A.1 and projection formula,
R^q h_* h*V=V tensor wedge^q G for the sums of line bundles here.
The Leray sequence has only two base columns, and the H1 column
just computed is zero. Hence the cohomology and connecting maps of
(L_p) are the global-section exterior maps of K. All monomial factors
match: kappa corresponds to lambda^9; a nonzero K entry of total
line weight n is the unique generator lambda^ceil(3n/4). Therefore
the global exterior-map constants are exactly

    K0=(1/3125) [ A B 0; 120 0 125/2; 0 120 50 ].

The fresh program `code/continuation_root/P1A2_hodge_fresh.py` constructs
the bases by their line weights and contracts/wedges K0 with their
actual exterior signs. It enumerates all maximal minors, records their
common zeros, and computes the following dimensions and ranks. The
indices in each vector are q=0,1,2,3.

    p=1: A_p=(0,2,3,1), B_p=(1,3,2,0), delta=(1,3,1,0).
    p=2: A_p=(2,6,7,3), B_p=(0,2,3,1), delta=(0,2,3,0).

The only exceptional real parameter for the relevant full minors is
pi c=5/3. It lies outside the family: the separately supplied,
independently certified P1.16 point value has h_b(1)<-1, while P1.8
gives c>-h_min and h_min<=h_b(1). Thus c>1, pi c>3.
The P1.16 certificate is the Paper V owner's fresh 276-step
Taylor/Gronwall period-ball program; this derivation uses its certified
point inequality and does not require the unresolved full global-minimum
cover. The target proof has not been opened to obtain this exclusion.

The long exact sequences of (L_p) now give

    H^q(Omega^1(log D))=(0,1,1,0,0),
    H^q(Omega^2(log D))=(2,6,5,1,0).

In detail dim H^q(log)=dim A_q-rank(delta_(q-1))
                              +dim B_q-rank(delta_q).
For p=2, H0(log) is precisely the two sections of K_B(a) tensor F,
and H1(log) is precisely the six sections of K_B(a) tensor F tensor G:
B_2 has no H0 and its q=1 connecting map is injective.

## 3. Actual residue complex of the Kuhn cusp

The normalization of D is the smooth complete toric variety of the
star of a lattice vertex of the periodic Kuhn fan. Its boundary is
the full toric boundary, so its logarithmic one-forms are O tensor M_C,
where M_C is the three-dimensional character space. Its double
strata have seven toric normalization components, indexed by the
nonzero binary vectors v in {0,1}^3. Their complete fans imply H^i(O)=0
for i>0 by Demazure vanishing for the zero nef divisor. The same is
true for the normalization of D, and hence for its trivial logarithmic
one-form bundle. This is the bounded classical toric vanishing input.

The local residue sequence on q=z0 z1 z2 z3 descends to the normalized
global branch sequence. For p=1 its residue quotient is O_(D-normalized).
For p=2 its residue quotient is the complex

    R^0=Omega^1_(D-normalized)(log conductor)
         -> R^1=O_(normalized double strata),

placed in degrees0 and1. Local exactness follows on the coordinate
chart by expanding a two-form in dz_i/z_i: its iterated residues are
the coefficients of pairs, and the two orders of residue cancel.
Taking the sum over the two branches gives the displayed differential.

For an edge orbit v the two preimages of its double stratum have
normal vectors v and -v. A character m has residues m(v) and -m(v),
whose sum vanishes. Thus the induced global differential C^3 -> C^7
is exactly zero. The residue hypercohomology is consequently
H0(R)=C^3 and H1(R)=C^7, with no higher terms. In degree1 the
residue quotient has only H0=C.

## 4. The two residue maps for two-forms

The map H0(Omega^2(log D))->C^3 is evaluation at the cusp of the two
global sections of K_B(a) tensor F. They occupy the distinct w2 and
w1 fibre directions and have nonzero monomial coefficients at a.
It therefore has rank2.

The H1 map is computed on the actual deck cocycles. Identify G(a)
with characters of the period-deck lattice. A class represented by
g(nu) times a toric logarithmic one-form m has a primitive on the
component labelled by v equal to g(v)m. Along the common edge,
its boundary residue is, up to the single common convention sign,

                         v -> m(v)g(v).                 (R)

This comes from subtracting the primitives on the components labelled
0 and v and contracting with the two opposite normals. The displayed
deck multipliers are holomorphic constants on the central torus;
their logarithmic derivatives along a fibre are zero and introduce
no additional term in (R).

The residue of the connection at lambda=a maps F(a) to G(a).
In the given frames it is the matrix Q obtained from K above by
putting lambda=a. This is the actual identification in (R): on the
uniformizing model Z(q)=log(q)/(2 pi i) I+C(q), the logarithmic
residue of a relative character form and the connecting period-deck
character have the same coefficients. This verifies the normalization
directly, and the supplied marking changes both sides by its same
invertible lattice maps. The fresh exact program gives

    det Q=4470348358154296875/281474976710656 != 0.

The six global sections of K_B(a) tensor F tensor G have the form
lambda^(ceil(3n/4)-9) f_i tensor g_j, where
n=11+weight(f_i)+weight(g_j) has coarse degree0. Write T for their
3 by3 coefficient matrix at a. Under the identification by Q, (R)
is evaluation of the quadratic form with matrix T Q^(-transpose).
Thus its rank is the rank of the symmetrization map followed by
quadratic evaluation on the seven binary edge vectors.

The program independently forms all six T matrices. In the coefficient
basis (x1^2,x2^2,x3^2,x1x2,x1x3,x2x3), its determinant is

    -4722366482869645213696 (3 pi c-5)
      /9822542779147624969482421875.

It is nonzero for c>1. Evaluation of those six monomials on
e1,e2,e3,e1+e2,e1+e3,e2+e3,e1+e2+e3 has rank6; the first three
values recover the squares, and the next three recover the mixed
coefficients. This proves that the H1 residue map has rank6, with
the full actual map and its one-dimensional cokernel specified.

## 5. Ordinary cohomology and the full table

The degree1 residue sequence now gives
H^q(Omega^1_M)=(0,2,1,0,0): its quotient has only H0=C,
and the logarithmic sheaf has H0=0. The degree2 residue complex,
with hypercohomology dimensions(3,7) and residue-map ranks(2,6),
gives H^q(Omega^2_M)=(0,1,6,1,0). Explicitly the long exact
sequence has the maps C^2 -> C^3 of rank2 and C^6 -> C^7 of rank6;
its next logarithmic group has dimension5 and its next one dimension1.

P1A.1 supplies H^q(O_M)=(1,1,0,0,0). Serre duality for a compact
complex fourfold identifies the dual of H^q(Omega^p_M) with
H^(4-q)(Omega^(4-p)_M), using the actual wedge pairing into K_M
and its trace. It gives the remaining rows without a Kähler assumption.
The resulting rows are exactly

    (1,1,0,0,0), (0,2,1,0,0), (0,1,6,1,0),
    (0,0,1,2,0), (0,0,0,1,1).

The program derives the ordinary dimensions from the two long exact
sequences and their ranks, then checks their alternating sum is6.
No Euler-characteristic fit was used to choose an individual entry.

## Remaining checks before reading the target proof

The complete new mathematical derivation and exact program above are
finished and written before the target proof is opened. The classical
source locators for toric vanishing and Serre duality are being reopened;
the Paper V owner has separately completed the required main-result
credit comparison. Comparison with the printed target is the next step.
