# Every lattice-basis fan of the actual selected-cusp source loop

Working proof for P3K.71, 17 November 2026. The parameter family is exactly
F54/F56, with the complete finite cap, fixed sufficiently small scalar,
positive rho loop and physical orientation of K68. This note computes that
return on every two-triangle periodic fan T(P), det P=+1 or -1. It does not
assign a source-zero return or a different source-parameter loop.

## AF.1. Literal identical-fan arrows and the canonical representative

For columns v,w of P, T(P) consists of all triangles

    {n,n+v,n+w}, {n+v,n+w,n+v+w}, n in Z².

Put R=[[-1,-1],[1,0]], so PR has columns w-v,-v and R³=I.
The first PR triangle is the first P triangle translated by -v; the second
is the second P triangle translated by -2v. For -P, its first triangle is
the second P triangle translated by -(v+w), and its second is the first
P triangle with the same translation. Swapping the columns merely
interchanges the two named vertices in each triangle. These are exact
equalities of the complete infinite fans.

Use the identity on the absolute dense-torus characters (Z,V,q). Each
matched absolute cone has the same semigroup of characters, so this
identity extends to the identity on its affine toric chart. On overlaps
it is that same character map. It commutes with the full original period
maps h,B, including their bounded units; the inverse changes of period
basis are integral. Therefore it descends to a holomorphic family
isomorphism, equal to the identity on the overlap with the original
source and every finite cap. It carries the physical delta action and
the complete closing arrow. No orientation or circle character changes.

For det P=-1 first swap its columns. Among the six matrices
P,PR,PR²,-P,-PR,-PR² there is exactly one representative of one of the
following forms:

    T_n = [[1,0],[n,1]], n in Z;
    C = [[p,-r],[q,s]], p,r>0, ps+rq=1.

Here is the complete geometric selection. The star at the lattice origin
has rays ±v, ±w, ±(v-w), with its six actual unimodular triangles. When
the physical vector delta=(0,1) is a ray, that primitive ray is delta
itself. The unique adjacent triangle with positive first-coordinate
edge and positive orientation gives T_n. Otherwise delta is in the
interior of exactly one of those six cones. Its boundary vectors, ordered
from positive to negative first coordinate, give C. Their determinant
is one, and the coefficients of delta are (r,p)>0. The six candidates
are precisely the six oriented triangles already identified above.
This proves existence and uniqueness, with the family map just given.

## AF.2. A terminating exact factorization using only C0/C1 flops

Set Q0=[[1,-1],[0,1]], Q1=[[1,0],[-1,1]], Q2=Q0^-1.
Starting with C=[[p,-r],[q,s]], perform the following finite integer
algorithm. For r>=p replace C by C Q2 and record0. For p>r replace C
by C Q1^-1 and record1. Before termination the new positive pair is
(p,r-p) or (p-r,r); its sum strictly decreases. The determinant implies
gcd(p,r)=1. Equality p=r therefore means p=r=1; the next replacement
is [[1,0],[q,1]]=T_q. The process terminates. Reverse the recorded
list. Literal matrix multiplication then gives

    C = T_n Q_{i1} ... Q_{ik}, with every i_j in {0,1}.

Every intermediate matrix after the initial T_n again has positive
first entry and negative second entry. Its three physical tangent
weights (r,p,-r-p) are consequently all nonzero. There is no step
requiring an uncomputed, separately retained fixed curve.

The arithmetic factorization specifies the construction; the actual
forward maps are these full Cox maps. C0 uses new basis(v,w-v), dense
characters(ZV,V), and first triangle(a/c,bc,c). C1 uses new basis(v-w,w),
dense characters(Z,ZV), and first triangle(a/b,b,bc). In the old native
chart(z,n0,n1), the two other-ruling charts are

    (n0/n1, z n1, n1), (n1/n0, z n0, n0).

For C1 the two normal coordinates are interchanged. This interchange
has the explicit constant path

    S_t = 1/2 [[1+exp(pi i t),1-exp(pi i t)],
               [1-exp(pi i t),1+exp(pi i t)]], 0<=t<=1.

It is unitary, commutes with the scalar native normal transition zI,
and preserves the oriented real four-plane. The two chart products
are exactly q=z n0 n1. Their common rank-one matrix is
[[n0,n1],[z n0,z n1]]. These are the actual other ruling of the
same conifold, with its full link map.

For a complete multiplier matrix A=(A_hj), the new multiplier is

    A'_ik = product_h,j A_hj^((Q^-1)_ih Q_jk).

Here i,k are the new row and column indices; h,j are the old ones. This is literal substitution in the characters and
period generators, with q unchanged. All coefficients retain their
full q and rho dependence. The old and new second native charts give
z'=1/z, n'=zn, as in GF.11. Thus every forward step is the actual
periodic family flop, with the original source, line, cap, finite
character and closing arrow on its exterior.

## AF.3. The complete vertical seed

K66 gives, on the actual T_n family, the physical class
s_n=-1-3n(n-1) modulo28 and the exact fixed native pair
(0,-6-18n(n-1)). Its complete integer proof retains both circle lines
and every collar cochain. The ordinary product of K55 differs by its
literal pure-left endpoint L^6. Consequently its fixed ordinary entries
are V00=18n(n-1), delta0=-12-18n(n-1).

For this basis the exact period winding is
B=[[-6,0],[6n,0]], the tangent weights are(0,1,-1), and the actual
circle/derivative prism equations of K55 give the other entries. Thus

    V = [[18n(n-1),6-12n,12n-6],
         [6-12n,0,0], [12n-6,0,0]],
    delta = [-12-18n(n-1),12n-12,-12n].

In particular both initial columns and the fixed entry are computed.
There is no free integer inferred from the finite-group residue.

## AF.4. Exact update and reconstruction on the target family

For any intermediate P define, in its actual marked coordinates,

    B=-6 P^-1 e1 e1^t P,
    l=(B22-B21,B11-B12,B22),
    (x,y)^t=P^-1 e2,
    w=(x,y,-x-y), d=(-x-2y,-2x-y,x-y),
    I_i=-3 w_i+d_i(l_i+3), W_i=-3 w_i-d_i(l_i+3).

These degrees are obtained from the full GF multiplier maps, not only
their winding matrix. For completeness their actual based periodic
unit logarithm is

 (P^-1)_i1(P_1j f_kappa+P_2j f_g)
 +(P^-1)_i2(P_1j f_alpha+P_2j f_eta).

Multiplication of these logarithms by the protected radial cutoff
constructs the full normal contraction. Its quaternion factors are
H_-3 Q H_(l_i+3), with the based smooth H of GF.9. The native-to-ordinary
Hopf map is (U H_-3 U^-1) q_H H_(l_i+3). Its left degree is -6 and
its right degree is zero, so its inverse-cylinder endpoint is L^6.
This is the same complete normal comparison on every intermediate
fan, including every new selected star.

Write a=V_ii and b=delta_i for the selected old curve i=0 or1.
Its native right integer is n_i=(b-a)/2. The exact Cox common-link
arrow is T(y,q_H)=(q_H^-1 y q_H,q_H), with the fixed complex normal
reset. Its action on the native relative coordinates is

    (m,n,s) -> (m+2n,-n,s+n).

The commutator generator has mu=+1/28 by the explicit orientation
calculation retained in K68. Thus the last entry is the physical
Theta7 class. The constant C1 normal interchange above conjugates
each Spin factor by a constant orientation-preserving lift and leaves
its degree unchanged. Adding the same ordinary L^6 comparison on
both sides gives, at the selected target curve C2,

    V'22=a, delta'2=2a-b, s'=s+(b-a)/2 mod28.

The actual target prism equations are

    V'(w_j e_j-w_0 e_0)=I_j e_j-I_0 e_0,
    w_j delta'_j-w_0 delta'_0=W_j-W_0, j=1,2.

Its weights are all nonzero by AF.2. Their complete symmetric solution
is

    V'jk = (I_j/w_j for j=k, else0) + c/(w_j w_k),
    delta'_j=(W_j+e)/w_j,
    c=w_2² a-w_2 I_2, e=w_2(2a-b)-W_2.

To prove uniqueness, the two vectors w_j e_j-w_0 e_0 span the
kernel of the functional with coefficients(1/w_0,1/w_1,1/w_2).
A symmetric difference annihilating that plane is c rr^t. The
derivative difference has the one analogous constant. The selected
entries determine both constants exactly. Existence is supplied by
the target family and the actual products just constructed. Their
integral invariants equal this unique rational solution, so all the
displayed values are integers, and (b-a)/2 is the actual integral
native right coordinate. No group class is divided by two.

Inductively these formulas compute the actual ordinary invariants and
physical class at every stage, and terminate at the prescribed fan.
The complete original family at that fan is identified in AF.1--2.
This proves the algorithm for every integer unimodular input, without
a bounded fan assertion or an unproved matrix-reset recurrence.

## AF.5. Executed certificate and explicit scope

code/part3_root/source_all_fans.py executes exact Fraction arithmetic.
For every unimodular matrix whose entries have absolute value at most18
it checks the exact canonical representative, decreasing factorization,
reconstruction, all integral prism equations, selected inversion and
integer right coordinates. It checks6504 inputs representing814 fans.
An independent three-edge traversal from the original seed checks439
states through depth8 against the new factorization; its four formerly
uncomputed separate-fixed transitions are not used as inputs. The
algorithm itself handles their fan targets from the K66 seed.

It also checks123 exact instances of the previously proved vertical,
horizontal and adjacent formulas, with the current physical baseline.
For example P=[[2,-1],[-1,1]] has word(0,1) from T0 and native right
increments(-6,-48), hence class -1-6-48=1 modulo28. The selected
source loop differs from the scalar OS45 loop of K70, whose original
source equation, scalar and cap are separately retained there.

The finite range includes every odd residue. No exhaustive parity or
image claim is inferred from that observation. The theorem is the
terminating exact value algorithm for each of the stated actual fans.
