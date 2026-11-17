# Uniform A3 at three coordinate axes: exact minimal-defect subcases

Current-run working proof, 2026-11-17. This file records the exact scope
and the abandoned deformation as well as the replacement argument.

## A. The boundary condition that must be retained

The reduced critical curve is the union of the three coordinate axes,
with ideal P=(xy,xz,yz), delta=2. Put h=xyz. Its symbolic square is
P^(2)=P^2+(h). In the generic A3 setting the actual conductor image ideal
I contains P^(2). The normalized rank-one nilradical has branchwise
projection colength at least one and Hessian order at least two.
When all three orders are exactly two and the projection colengths are
one, its leading quotient values have rank at most two. Thus its
additional descent defect is at least one, and the total local defect
is at least 2+3*(2/2+1)+1=9.

The former proposed deformation G -> G-epsilon with h fixed is NOT a
valid exclusion. On a boundary near the x-axis it replaces the tacnode
by two transverse A1 points: (G-epsilon,h)=0 has two separate points in
the normal slice. It therefore fails the boundary A3 hypothesis needed
for transport. The argument below replaces it by a deformation of U
in the exact equation G^2+h^2 U; it keeps the three axes fixed.

## B. The full quartic tensor

Write the quartic part as a quadratic form in (xy,xz,yz), with symmetric
matrix having diagonal entries A,C,E and off-diagonal entries B,D,F.
The leading rank-one Hessian along each axis gives

    AC=B^2, AE=D^2, CE=F^2.

If a diagonal entry is zero, its adjacent off-diagonal entries vanish,
and the remaining 2-by-2 block has rank one. If all three diagonal
entries are nonzero, the vanishing null cubic on the x-axis gives
F=BD/A. Hence in either case the full quartic is a square

    (a xy+b xz+c yz)^2.

The null-cubic assertion concerns the coefficient linear in x of the
normal cubic. Higher total-degree terms contribute higher powers of x
and cannot cancel it. The complete germ has the same conclusion for
its leading coefficient. All three branch Hessians are nonzero only
if at least two of a,b,c are nonzero.

## C. The case abc != 0: exact conductor and rational normalization

Assume the total defect is nine, all three branch Hessian orders are
two, and abc is nonzero. The normalized quotient values have one
linear relation involving all three branches. Since the residual
descent defect is one, their entire module consists of that
two-dimensional space of values together with all positive-order
branch functions. Multiplying a source generator that is a unit on a
given normalized branch by its axis coordinate generates the positive
orders on that branch alone. Consequently the leading kernel vector
lifts to an actual g in I with quadratic part a xy+b xz+c yz.

We already have h in I. The ideal I0=(g,h) has radical P: on each
coordinate plane, g is the product of its two coordinate functions
times a unit. Moreover P^2 is contained in I0. For example
g*(xy)=a(x,y,z)(xy)^2 modulo h, and a is a unit; the other squares
follow in the same way and all mixed products are multiples of h.
At the generic point of each axis, I0 is the A3 conductor ideal
(normal coordinate, square of the null coordinate). Thus I0 and I
agree generically. Since I0 is a codimension-two complete intersection,
O/I0 is Cohen--Macaulay and P/I0 is torsionfree on the reduced curve.
The map P/I0 -> P/I has finite-length kernel, which must vanish.
Therefore the equality I=(g,h) is exact.

The actual conductor ring condition (de Jong--van Straten1990,
Theorem1.12, already opened and used in P4.41) gives f in I^2. Write

    f=A g^2+B gh+C h^2,  A(0) != 0.

Completing the square and absorbing sqrt(A) into its first factor gives
the exact equation

    f=G^2+h^2 U,

where G has nondegenerate quadratic part a'xy+b'xz+c'yz with all three
coefficients nonzero. The ideal remains (G,h).

If U(0) is nonzero, extract sqrt(-U) and factor

    f=(G+h sqrt(-U))(G-h sqrt(-U)).

Each factor has nondegenerate quadratic Hessian, so it is an ordinary
A1 surface singularity. In particular both normalization branches are
normal rational surface germs. The local normalization has no
positive-genus exceptional component.

## D. The case U(0)=0: a boundary-preserving Morse exclusion

First add an arbitrarily small generic linear form to U. On the fixed
boundary the original generic A3 coefficient is a unit, so this change
preserves the transverse A3 germs. We can choose the resulting linear
part L in the open set specified below. Now replace U by U-epsilon.
The critical axes and their boundary A3 germs remain unchanged.

A diagonal linear change makes the quadratic part of G equal to
G2=xy+xz+yz and changes h only by a nonzero constant, absorbed in U.
Write (x,y,z)=epsilon*(X,Y,Z). Then

    f_epsilon/epsilon^4
       = G_epsilon(X,Y,Z)^2
           + epsilon^3 h3(X,Y,Z)^2
                         (L(X,Y,Z)-1+O(epsilon)),

where G_epsilon=G2+O(epsilon), and h3=XYZ. Near a nonzero point of the
smooth cone G2=0, use G_epsilon as the normal coordinate. Its parameter
Morse centre is O(epsilon^3). Substituting that centre leaves the
effective tangential function

    epsilon^3*(Phi+O(epsilon)),
    Phi=h3^2*(L-1) restricted to G2=0.

We exhibit nondegenerate critical points of Phi with nonzero value.
The projective conic G2=0 has parametrization

    [x:y:z]=[t(t+1):t+1:-t].

For L=x+y+z this gives H(t)=-t^2(t+1)^2 and
l(t)=t^2+t+1. In radial coordinate r,

    Phi(r,t)=r^6 H(t)^2 (r*l(t)-1).

Radial criticality is r=6/(7*l(t)). After this substitution the critical
value function is -6^6/7^7*(H/l^3)^2. Its derivative is controlled by

    d(H/l^3)/dt
       = t(t-1)(t+1)(t+2)(2t+1)/(t^2+t+1)^4.

The three additional critical points t=1,-2,-1/2 avoid every zero and
pole and are simple. Their radial coordinates are 2/7,2/7,8/7. At
each point the value is -1024/823543 and the two-by-two Hessian
determinant is 4718592/1977326743, both nonzero. Thus Phi is Morse.
The corresponding property is Zariski open in the coefficients of L;
the explicit example proves that the open set is nonempty, so an
arbitrarily small generic linear perturbation of any initial U is
available. Equivalently, h3/l^3 is a degree-six map of the conic with
three further simple ramification points beyond its forced zeros and
poles.

Divide the two tangential critical equations by epsilon^3 after the
normal Morse elimination. They are analytic in epsilon, with invertible
Jacobian at each exhibited critical point. The implicit-function theorem
therefore gives full nondegenerate three-variable critical points of
f_epsilon for sufficiently small nonzero epsilon. Their critical values
have leading term epsilon^7 times the displayed nonzero value.
They tend to the original critical point as epsilon tends to zero.

This deformation retains boundary A3. Nested boundary transport embeds
its local Morse vanishing sphere, of square -2, into a nearby global
torus fibre, which is impossible. Hence U(0)=0 is excluded in the
actual torus degeneration. Together with C, the full-quartic,
minimal-defect conductor case has rational normalization.

## E. A missing quartic coefficient: the exact ring condition

When exactly one coefficient is zero, the minimal model for the
conductor is I=(xk,xh,h^2), k=y+z,h=yz. It cannot be replaced by
(xk,xyz), whose zero set contains a plane. Its Hilbert--Burch matrix is

    [[h,0],[-k,h],[0,-x]].

Appending a column (a,b,c) gives determinant a*xk+b*xh+c*h^2. The
adjugate membership conditions are

    ax,ah,ck,ch,bx+ch,ak+bh in I.

The exact colon ideals give
a in (xk,h), c in (x,h^2), b in (k,h), with cancellation of the hk
terms. Consequently the full equation has the form

    f=A x^2 k^2+B x^2 kh+C xh^2+D h^4.

If A(0) != 0, complete the square in k and apply actual coordinate
changes preserving h up to a unit. This gives

    f=x^2(y+z)^2+x y^2 z^2 C+y^4 z^4 D.

When C(0) != 0, substitute x=h^2 v and divide by h^4. The resulting
equation has a simple finite root in v, giving a smooth factor
x-h^2 v(y,z). Division leaves xk^2+h^2 U with U a unit. The actual
coordinate X=x/U makes it Xk^2+h^2. Its finite birational normalization
is given by

    u=h/k, X=-u^2, u(y+z)=yz.

The last equation is an A1 quadric; the extension is finite because
u^2=-X, and birational because u=h/k off k=0. Both branches therefore
have rational normalization. The case C(0)=0 and the remaining
nonminimal-Hessian or nonordinary three-branch conductor cases are
not concluded here.

## Executed algebra

`code/part4/a3_three_axes.py` records all minors, the conic derivative,
its exact Morse values/Hessians, and the A1 normalization equation.
Its output is separate from this proof.
