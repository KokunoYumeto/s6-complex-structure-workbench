# A closed formula and the complete image of the marked infinity return

Proved as P3K.93 after full root and independent symbolic audits. This
evaluates the actual return
algorithm of P3K.92. The proof retains the two source-zero algorithms,
the selected-cusp algorithm, and their exact reflected word.

## Statement

Retain all source, Cartier, cap, root, scalar and endpoint markings of
P3K.92. For any unimodular fan basis \(P\), put
\[
 (x,y)^t=P^{-1}(0,1)^t,\qquad S=x^2+xy+y^2.
\]
Then its actual fixed-scalar positive infinity return is
\[
 \boxed{\displaystyle
 I_a(P)=f_a(S):=
 1-a-3(a-1)(S-1)-\frac{2a+1}{4}(S-1)(S-3)
 \pmod {28}.}                                      \tag{IC.1}
\]
Here \(a=1\) is the good \(m=4p\) branch and \(a=2\) the reduced
\(m=4p-1\) branch, for every \(p\ge1\), either norm sign and every
fixed admissible finite character and integral annular cochain. The
integer \(S\) is odd, so the displayed expression is integral.

The complete images over all lattice-basis fans are
\[
 \begin{array}{c|l}
 a=1&\{0,6,8,10,14,20,22,24\}\\
 a=2&\{5,7,9,13,19,21,23,27\}.
 \end{array}                                       \tag{IC.2}
\]
The proof below evaluates the sphere class in the actual P3K.92
family. It assigns no infinity characteristic pair or free relative
coordinate from that class.

## IC.1. Canonical fans, their norm, and the reflected word

Use the literal identical-fan arrows of P3K.71 and P3K.90: a column
swap, multiplication on the right by
\(R=\left(\begin{smallmatrix}-1&-1\\1&0\end{smallmatrix}\right)\),
and central negation match the actual translated triangles. The
identity on their absolute character semigroups is the family map;
it carries all full period coefficients, original source/Cartier
charts, finite caps and endpoint closings. On \((x,y)\) these
operations are respectively
\[
 (y,x),\qquad (y,-x-y),\qquad(-x,-y).
\]
Each preserves \(x^2+xy+y^2\) by direct expansion. Thus \(S\) is a
function of the actual fan.

The canonical representative is either
\(T_j=\left(\begin{smallmatrix}1&0\\j&1\end{smallmatrix}\right)\),
or
\[
 P=\begin{pmatrix}u&-r\\s&z\end{pmatrix},\qquad
 r,u>0,\quad uz+rs=1.                              \tag{IC.3}
\]
In the second case \((x,y)=(r,u)\). Its actual construction is the
finite word from a vertical seed using
\[
 Q_0=\begin{pmatrix}1&-1\\0&1\end{pmatrix},\qquad
 Q_1=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
\]
The first step is \(Q_0\). The subsequent Euclidean word is the one
proved in P3K.90; all its three physical weights are nonzero.

Let \(J=\operatorname{diag}(-1,1)\) and
\(E=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\).
For nonvertical \(P\), the canonical reflected basis is literally
\[
 P^*=JPE=\begin{pmatrix}r&-u\\z&s\end{pmatrix}.
\]
The column swap is an identical-fan map, while \(J\) is exactly the
source/Cartier reflection with full height translate proved in
P3K.92. Thus the second source-zero class in that theorem is
\(Z_a(P^*)\). Exact matrix multiplication gives
\[
 (PQ_0)^*=P^*Q_1,\qquad (PQ_1)^*=P^*Q_0,             \tag{IC.4}
\]
and at the first step
\[
 (T_jQ_0)^*=T_{1-j}Q_0.                             \tag{IC.5}
\]
Both reflected algorithms therefore start with the actual common
\(Q_0\) step, and thereafter interchange the two generators. These
are identities of full period-basis/character maps; their coefficient
substitution is the same integral monomial formula as in P3K.92.
No new normal identification is introduced in evaluating the arrays
below.

## IC.2. The full paired prism equations

Write \(b=3-a\) and
\[
 W=\begin{pmatrix}1&b\\-a&-2\end{pmatrix}.
\]
For the source-zero algorithm at \(P\), the full winding matrix is
\(B_Z=2P^{-1}WP\), with product trace \(t_Z=-1\). For the
selected-cusp algorithm it is
\(B_C=-6P^{-1}E_{11}P\), with \(t_C=-3\). These are the actual
integer data of P3K.90 and P3K.71, whose complete coefficient maps
and native products are retained in P3K.92.

For any such \((B,t)\), their common prism notation is
\[
 \begin{split}
 \ell&=(B_{22}-B_{21},B_{11}-B_{12},B_{22}),\\
 w&=(r,u,-r-u),\qquad d=(-r-2u,-2r-u,r-u),\\
 I_i&=t w_i+d_i(\ell_i-t),\qquad
 J_i=t w_i-d_i(\ell_i-t).
 \end{split}                                      \tag{IC.6}
\]
The source-zero and selected-cusp variation/derivative arrays satisfy
\[
 V(w_i e_i-w_0e_0)=I_i e_i-I_0e_0,\qquad
 w_i\delta_i-w_0\delta_0=J_i-J_0,\quad i=1,2.        \tag{IC.7}
\]
Let \(K\) exchange indices 0 and 1 and fix index 2. Form the following
explicit algebraic sums of the already computed arrays:
\[
 \mathcal V=V_Z(P)+K V_Z(P^*)K+2V_C(P),\qquad
 \mathcal D=\delta_Z(P)+K\delta_Z(P^*)+2\delta_C(P).
                                                               \tag{IC.8}
\]
Their role is to evaluate the right-hand side of P3K.92's formula.

The full winding matrices obey
\[
 B_Z+E B_Z(P^*)E+2B_C
   =2P^{-1}(W+JWJ)P-12P^{-1}E_{11}P=-8\operatorname{Id}.
                                                               \tag{IC.9}
\]
The traces in (IC.6) add to \(-1-1+2(-3)=-8\). For indices 0,1,
reflection interchanges \(w,d,\ell\) in their displayed order.
For index 2 it changes the sign of \(d_2\); the corresponding
\(\ell_2-t\) also changes sign because
\(\operatorname{tr}B_Z=-2=2t_Z\). Consequently the full combined
prism right-hand sides are exactly
\[
 \mathcal I_i=\mathcal J_i=-8w_i.                   \tag{IC.10}
\]
This includes index 2; no unlabelled permutation of its sign is used.

All three weights are nonzero after the first step. The complete
symmetric solution of (IC.7) with right-hand side (IC.10) is
\[
 \mathcal V_{ij}=-8\delta_{ij}+
                \frac{\mathfrak c}{w_iw_j},\qquad
 \mathcal D_i=-8+\frac{\mathfrak e}{w_i}.            \tag{IC.11}
\]
Indeed \(\mathcal V+8\operatorname{Id}\) annihilates the plane
spanned by \(w_i e_i-w_0e_0\). A symmetric matrix annihilating that
plane is a scalar multiple of the outer product of
\((1/w_0,1/w_1,1/w_2)\). The derivative equations similarly give
one scalar. Thus their selected diagonal and selected derivative
entries determine \(\mathfrak c,\mathfrak e\) uniquely.

## IC.3. The complete common first-step seed

Put
\[
 P_b(j)=2b\binom{j+1}{3}+(3-b)\binom{j+1}{2},\qquad
 \mu=2-a,\qquad \nu_j=6P_b(j).
\]
P3K.89 and P3K.90 give the actual source-zero fixed ordinary entries
on \(T_j\)
\[
 c_Z(j)=-2-2\mu-2\nu_j,\qquad
 e_Z(j)=-2-2\mu+2\nu_j.
\]
P3K.71 gives the selected-cusp entries
\[
 c_C(j)=18j(j-1),\qquad e_C(j)=-12-18j(j-1).
\]
The actual \(Q_0\) Cox arrow and complex-meridian reset send each
selected old pair \((c,e)\) to target entries \((c,2c-e)\) on
\(C_2\). This is the same typed two-ruling map in all three
algorithms. The source-zero class increment is \((e-c)/4\), and
the selected-cusp increment is \((e-c)/2\), exactly as proved by
their respective actual doubled products.

The identity
\(P_b(j)+P_b(1-j)=3j(j-1)+a\) now gives the selected combined
entries after this common first step:
\[
 \begin{split}
 \mathcal V_{22}
   &=c_Z(j)+c_Z(1-j)+2c_C(j)=-4(2a+3),\\
 \mathcal D_2
   &=(2c_Z-e_Z)(j)+(2c_Z-e_Z)(1-j)
                    +2(2c_C-e_C)(j)=-4(8a-3).
 \end{split}                                      \tag{IC.12}
\]
The target weights are \((1,1,-2)\). Substitution into the unique
full prism solution (IC.11) gives the complete arrays
\[
 \mathcal V=
 \begin{pmatrix}
 -8(4a+3)&-16(2a+1)&8(2a+1)\\
 -16(2a+1)&-8(4a+3)&8(2a+1)\\
 8(2a+1)&8(2a+1)&-4(2a+3)
 \end{pmatrix},\qquad
 \mathcal D=
 \begin{pmatrix}16(4a-3)\\16(4a-3)\\-4(8a-3)\end{pmatrix}.
                                                               \tag{IC.13}
\]
In particular this is a full common seed, independent of \(j\),
obtained from the actual three target systems.

The vertical groupoid class is \(1-a\) by P3K.92. The total of the
three finite increments at the first step is
\[
 \nu_j+\nu_{1-j}+\frac{e_C(j)-c_C(j)}2=6(a-1).
\]
Therefore the actual infinity class after this step is represented
by \(7(1-a)\). This agrees with \(f_a(3)\); the vertical seed agrees
with \(f_a(1)\).

## IC.4. Both generator identities and the complete induction

For positive \(r,u\) define
\[
 D=ru(r+u),\qquad S=r^2+ru+u^2,
\]
and set
\[
 \mathfrak c=-4(2a+1)D^2,\qquad
 \mathfrak e=4D\bigl((2a+1)S+2a-8\bigr).            \tag{IC.14}
\]
At \((r,u)=(1,1)\), these give exactly (IC.13).

The two actual forward generators change the weights as follows:
\[
 \begin{array}{c|c|c|c}
 i&(r',u')&w_i&w'_2\\\hline
 0&(r+u,u)&r&-r-2u\\
 1&(r,r+u)&u&-2r-u.
 \end{array}
\]
Direct multiplication gives both identities
\[
 S'=S+\frac{2D}{w_i},\qquad
 \frac{D'}{w'_2}=-\frac{D}{w_i}.                   \tag{IC.15}
\]
By (IC.4) the reflected source-zero step uses the other generator,
while the selected-cusp step uses the original one. Each has the
same actual selected-entry reset. Hence the algebraic sums obey
\[
 \mathcal V'_{22}=\mathcal V_{ii},\qquad
 \mathcal D'_2=2\mathcal V_{ii}-\mathcal D_i.         \tag{IC.16}
\]
The target full prism equations remain (IC.10).

Substitute (IC.14--15) into (IC.11) at the target. Its selected
variation is
\[
 -8-4(2a+1)\frac{D'^2}{(w'_2)^2}
   =-8-4(2a+1)\frac{D^2}{w_i^2}=\mathcal V_{ii}.
\]
Its selected derivative is
\[
 -8-\frac{4D}{w_i}
       \left((2a+1)\left(S+\frac{2D}{w_i}\right)+2a-8\right)
   =2\mathcal V_{ii}-\mathcal D_i.
\]
The uniqueness proved in IC.2 therefore gives the entire target
arrays, with (IC.14), for either generator. This proves their formula
along every finite Euclidean word.

The change of the *actual class sum* in P3K.92 is
\[
 \begin{split}
 \Delta I_a
  &=-\frac{(e_Z-c_Z)+(e_{Z^*}-c_{Z^*})+2(e_C-c_C)}4\\
  &=-\frac{\mathcal D_i-\mathcal V_{ii}}4
    =-\frac{(2a+1)D^2}{w_i^2}
      -\frac{D\bigl((2a+1)S+2a-8\bigr)}{w_i}.
 \end{split}                                      \tag{IC.17}
\]
Every quotient by 4 here is the sum of the already proved integral
native increments. No sphere class is divided by 4. Expanding the
polynomial in (IC.1) and using (IC.15) gives exactly
\[
                 \Delta I_a=f_a(S')-f_a(S).         \tag{IC.18}
\]
The first-step and vertical seeds in IC.3 agree with \(f_a\), and
every canonical nonvertical fan is reached by the terminating word.
Thus (IC.1) follows for all canonical fans. The identical-fan arrows
and norm invariance in IC.1 give the result for every unimodular
input, including negative determinants.

## IC.5. The complete image and explicit actual fans

Unimodularity implies \(\gcd(x,y)=1\). The three nonzero parity
vectors \((1,0),(0,1),(1,1)\) all give \(x^2+xy+y^2=1\pmod2\).
Thus \(S=2t+1\) for an integer \(t\), and the two polynomials are
\[
 f_1(S)=-3t(t-1),\qquad f_2(S)=-5t^2-t-1.           \tag{IC.19}
\]
The first is even and has residues \(\{0,1,3,6\}\) modulo 7; the
second is odd and has residues \(\{0,2,5,6\}\) modulo 7. Direct
substitution for \(t\) modulo 4 gives respectively residues
\(\{0,2\}\) and \(\{1,3\}\). Equivalently, both polynomials have
period 28 modulo 28, with differences
\[
 f_1(2(t+28)+1)-f_1(2t+1)=-28(6t+81),
\]
\[
 f_2(2(t+28)+1)-f_2(2t+1)=-28(10t+141).
\]
These exact residue computations give the two eight-element upper
sets in (IC.2).

Every entry is realized by an actual primitive fan below. The notation
\([u,-r;s,z]\) denotes its full basis matrix; each determinant is 1
and its physical coordinates are \((r,u)\). The construction and all
source/cap endpoints for each such matrix are those of P3K.92.
\[
 \begin{array}{c|r|c|r|c}
 a&I_a\pmod{28}&(r,u)&S&P=[u,-r;s,z]\\\hline
 1&0 &(0,1)&1   &[1,0;0,1]\\
 1&6 &(3,4)&37  &[4,-3;-1,1]\\
 1&8 &(2,3)&19  &[3,-2;-1,1]\\
 1&10&(1,2)&7   &[2,-1;1,0]\\
 1&14&(1,5)&31  &[5,-1;1,0]\\
 1&20&(7,10)&219&[10,-7;3,-2]\\
 1&22&(1,3)&13  &[3,-1;1,0]\\
 1&24&(3,5)&49  &[5,-3;2,-1]\\\hline
 2&5 &(2,3)&19  &[3,-2;-1,1]\\
 2&7 &(1,2)&7   &[2,-1;1,0]\\
 2&9 &(1,3)&13  &[3,-1;1,0]\\
 2&13&(3,4)&37  &[4,-3;-1,1]\\
 2&19&(2,9)&103 &[9,-2;-4,1]\\
 2&21&(1,1)&3   &[1,-1;1,0]\\
 2&23&(2,5)&39  &[5,-2;-2,1]\\
 2&27&(0,1)&1   &[1,0;0,1]
 \end{array}                                       \tag{IC.20}
\]
Substituting their \(S\) values in (IC.19) verifies all entries.
The exact certificate also reexecutes both source-zero algorithms
and the selected-cusp algorithm, with their complete witness
histories, at every displayed matrix. Thus the upper sets are the
complete images of the actual infinity families.

## IC.6. Exact certificate scope

`code/part3_fourfold/source_infinity_closed_formula.py` executes the
symbolic reflected winding/prism identity, all nine unknowns in each
of the three complete first-target systems, their common seed, both
selected reset identities, both class-increment identities and norm
invariance. It checks the period 28 residue calculation and all sixteen
primitive witnesses by the original actual algorithms. A compact
additional replay covers 2,768 full algorithm evaluations, including
negative bases and different vertical seeds. The complete count is
2,885 exact checks. The formula and exhaustiveness follow from the
finite-word proof and the realized residue sets above; the replay
range supplies an additional check of that proof's implementation.
