# Irreducible type II caps in the primitive source profiles

Proved as P3F.43, with independent root and fourfold audits of the
exact six-point quotient, line identity, affine norm and integral maps.
The actual signed return is proved separately in P3K.26.

The profiles of P3K.22 with a type II fibre and a retained I1 are
I8+II+2I1 (row45), I7+I2+II+I1 (row47), and I5+I4+II+I1
(row55). Their primitive data are M=O(dG-O),Q=G with d=8,14,20.
Take the II site as the sole logarithmic cap and a retained I1
as the sole simple whole-fibre scalar zero. All other components
and the whole-fibre Hom degree one remain exactly those in K22.

## II.1. Actual roots and the section marking

Write the actual minimal II equation as

    y^2=x^3+q a(q)x+q b(q), b(0) nonzero.

For q=z^m,x=z^(2l)X,y=z^(3l)Y, the two admissible residues are

    m=6l+1: Y^2=X^3+z^(2l+1)a(z^m)X+z b(z^m),
    m=6l:   Y^2=X^3+z^(2l)a(z^m)X+b(z^m).

The first is a reduced II fibre in a smooth total surface. The
second is good, with central curve Y^2=X^3+b(0) and deck
(X,Y)->(zeta_3^(-1)X,-Y). Its order-six automorphism fixes only O:
a finite fixed point would have both X=0 and Y=0, contrary to
b(0) nonzero. Consequently every original marked section,
including Q=G and dG, has root limit O. In the exact root
coordinate w=-X/Y, its expansion is w=z^l c(z^m), since the
minimal sixth root has weight one. Thus the central good-root
norm requires nQ0=0 and is satisfied here. It is not the
nonzero-torsion norm occurring at primitive III/IV sites.

For the intermediate residue m=6l+2, k=l gives a reduced IV
root. In X=zX1,Y=zY1 the deck character on Y1 is
zeta_m^(-(3l+1))=-1. It fixes the identity component and
interchanges the other two. Q remains on the identity
component: composing this root with its cubic good root gives
the same order-six fixed point O. The affine component norm
therefore cannot generate all three labels. The actual
reflection has two component orbits, and the compact
intersection pairing of P3K.19 excludes a sphere cap.
The residues three, four and five give the nonreduced I0*,
IV* and II* fibres, excluded by their unequal multiplicities
and that same proved intersection obstruction.

## II.2. The good-root line correspondence

On the minimal sixth root, the central curve has one order-six
fixed point O, one orbit of two points with stabilizer order
three, and one orbit of three points with stabilizer order two.
At each point its stabilizer acts on the two surface coordinates
with weights (1,1). Blow up all six points. The quotient by
mu6 has central curve C of square -1 and three exceptional
curves D6,D3,D2 of squares -6,-3,-2. In the actual quotient,

    pi^*C=E_hat,
    pi^*D6=6E_O,
    pi^*D3=3(E_P1+E_P2),
    pi^*D2=2(E_R1+E_R2+E_R3).

Here E_hat has square -6 and maps with degree six. The central
fibre is 6C+D6+2D3+3D2. Contract C, then D2, then D3. Their
successive self-intersections are -1 at the moment of contraction.
After the first step the squares are -5,-2,-1 with pairwise
intersection one; after the second the remaining squares are
-4,-1 with intersection two; after the third D6 has square zero
and the cuspidal singularity specified by the invariant equation
y^2=x^3+q a(q)x+q b(q). Thus the displayed invariant map and
these contractions identify this quotient with the original
minimal II source, including its smooth total surface.

Both marked sections dG' and O pass through the root point O.
In the blowup chart w=z u they meet E_O at the finite marked
coordinates u=c_dG(q) and u=0. The proper central elliptic
curve meets E_O at u=infinity, so both sections avoid every
contracted curve. Each section has exceptional coefficient one
at this single blowup. Subtracting their divisors therefore
cancels that coefficient exactly and gives

    beta^*O(dG'-O) = pi^*alpha^*O(dG-O).             (II.1)

This identity also holds if the two sections have further
contact: both sides are differences of their actual Cartier
divisors in the displayed (u,q) chart. No other exceptional
point lies on either section. For m=6l pull back the complete
diagram and resolve its fibre product. The actual root source
translation Q' has limit O, fixes the six centres, and lifts
through the whole diagram. Thus (II.1) carries its actual
suspension line map B0 and its deck commutation to the line
N=O(dG'-O). On the good central fibre N is the trivial Picard
class, as required by its actual marked section limit.

At a reduced II root the pullback/relative-minimal line comparison
has only one irreducible component. Its vertical difference is
therefore a whole-fibre divisor. The corresponding base monomial
retains the complete deck character and supplies the extending
B0. This is the same actual divisor comparison as at a reduced
III/IV root, with a one-component intersection kernel.

## II.3. Source norm, actual cap and the family closing

Choose gcd(m,n)=1. Multiplication by m has a unique inverse
branch at the marked central point: it acts on the additive
group at a II root, and on the elliptic group at O at a good
root. This gives a D-invariant analytic R with mR=Q'.
The source map a0=t_(-nR)D satisfies a0^m=t_(-nQ').
Lift t_(-R) to F on N using the actual chord divisor and its
whole-fibre correction. Normalize DFD^(-1)=chi F, chi^m=1.
Write B0=beta(q)F^m. Its actual deck descent makes beta
invariant. Then

    (F^n D)^m/B0^n=chi^(n m(m-1)/2) beta(q)^(-n).

Dividing by an invariant analytic mth root gives the commuting
line norm A0^m=B0^n. This retains the possible even-order
character factor. Set A_r=r^n A0,B_lambda=r^m B0. Bezout
gives H=A_r^u B_lambda^v=rH0 with H^m=B_lambda,H^n=A_r.
Strict norm contraction on a smaller compact tube constructs
the actual smooth proper cap N^times/<H> and proves delta
free. Its outward meridian maps are q->-nh,gamma->mh.
The ordinary-to-cap cochain and closing are precisely the
ones in SC.4/OA.2: scalar variation n(c-c0)s delta/m,
inverse closing (t-t_c)^(-n), lambda=r^m. They extend by
the actual scalar-zero cusp charts and by units elsewhere.

## II.4. Every integral map for one II cap

The full source/boundary cones are executed in
code/part3/ii_cap_boundary.py/.json/.out. Here the removed
component column is L=F and its intersection matrix is zero.
The source-complement complex is C4=Z -> C3=Z -> C2=NS
-> C1=Z -> C0=Z with d4=1 and d2=F^t B. The boundary
complex has one Z in each degree zero through three and
zero differentials. Its actual translation and inclusion
are obtained by the same uncancelled cones as OA.3.

The source complement is simply connected. Its fundamental
group is a quotient of the elliptic lattice because the section
kills the base loops; F^tB is surjective, so its H1 vanishes.
Its translation coinvariants are free Z, generated by the
actual relative-Wang cycle T O-O, and its invariant lattice
is ZF. One can also read this directly from the exact sequence
0 -> F-perp -> NS -> Z -> 0: in the K22 full Wang calculation
the invariant F maps to zero and the cokernel generator O
maps to one, forcing the relative-Wang column to be primitive.

Thus H1(W)=H2(W)=H3(W)=Z,H4(W)=0. The boundary E has
H1=H2=H3=Z^2,H4=Z. In the stored marked H2 basis the actual
fibre is primitive and its exterior image is zero; the other
boundary column is a unit. In both the reduced II and good
cap, H1=Zh,H2=ZC,H3=Z(C h),H4=0. For good reduction
the determinant of D-I on the elliptic lattice is one, so
there is no hidden finite cap group. The actual generic
fibre transport/specialization has degree one in either cap.

Consequently, retaining the integer collar coefficient kappa,
the full middle map is D2=[[0,1],[-1,-kappa]] after the
explicit oriented boundary choice. The other degree maps in
the actual bases (q,gamma) and (source boundary,F gamma) are
D1=D3=[[0,1],[n,-m]], while D4 is Z->0 and D0=(1,-1)^t.
The cap rows follow from u_cap=m u_ordinary-n arg(q)/(2pi);
there is no H3 source term because each cap source retracts
to its two-dimensional fibre. In the good case the actual
degree-one regular-fibre transport carries the two boundary
elliptic generators onto the cap's full normal elliptic Z^2,
which is killed in the simply connected source complement.
The reduced II cap source is already simply connected. The
remaining marked relations give pi1(Y)=Z/|n| by Van Kampen.
For n nonzero the integral homology is H0=H5=Z,
H1=H3=Z/|n|,H2=H4=0. Hence exactly n=+/-1 are spheres
in these one-cap domains. Their actual Hopf filling is the
standard S6 by the proved K22 Gysin calculation. No return
class has been assigned from this topology computation.
