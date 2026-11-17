# The one-missing-coefficient ordinary-axis conductor

Current-run full audit draft, 2026-11-17. The setting is an ordinary
three-axis critical curve, uniform generic A3, and total local defect
nine. P4.48 gives d=(2,2,2), b=(1,1,1), q=1. The quartic square has
exactly one missing coefficient; rescale to quadratic conductor
x(y+z). Every coordinate map below is an actual analytic isomorphism.

## 1. Exact two-form classification of the conductor ideal

The normalized rank-one image has a two-dimensional value space W,
with one linear relation involving precisely the y- and z-branches.
Its colength one makes it W plus all positive-order branch functions.
The source generators, multiplied by axis coordinates, generate these
positive-order functions separately. Therefore the leading kernel
vector lifts to g in I with quadratic part x(y+z).

Write g=x(alpha*y+beta*z)+yz*gamma, where alpha,beta are units and
gamma(0)=0. Replacing y,z by alpha*y,beta*z is an invertible analytic
coordinate change and preserves the axis curve. Put k=y+z,h=yz.
Then g=xk-hc, c(0)=0. Since xyz lies in P^(2) and P^2 lies in I,

    I0=(g,xh,h^2) is contained in I.

Its Hilbert--Burch matrix is

    [[h,0],[-k,h],[c,-x]].

The three maximal minors are g,xh,h^2, up to signs. The ideal has
radical P and codimension two, is Cohen--Macaulay, and agrees with
the actual A3 conductor at each generic axis point. As in P4.47,
P/I0 is torsionfree; its finite-length kernel under P/I0 -> P/I
vanishes. Thus I=I0 exactly.

There are only two analytic forms for this ideal. The quotient
O/(x,k,h) is C{y}/(y^2), so analytic division gives

    c=lambda*y+xA+kB+hC,

with a scalar lambda. Replace g by g+xhA+h^2C, then set x'=x-hB.
The ideal becomes exactly

    (x'k-lambda*yh, x'h, h^2).

The coordinate map has derivative one in x at the origin. If lambda
is zero this is I_std=(xk,xh,h^2). If lambda is nonzero, rescale
x'=lambda*X and obtain I_mis=(xk-yh,xh,h^2). This explains precisely
the earlier jet-matching obstruction; higher coefficients do not
survive the ideal (x,k,h), because y^2 is zero in its quotient.

## 2. The standard form

For I_std, append (a,b,c) to the Hilbert--Burch matrix
[[h,0],[-k,h],[0,-x]]. The determinant is a*xk+b*xh+c*h^2.
Membership of all adjugate entries in I gives exactly

    f=A x^2k^2+B x^2kh+C xh^2+D h^4,
    A(0) nonzero.

The colon identities are I:h=(x,h), I:x=(k,h), and I:k=(x,h^2).
They give a in (xk,h), c in (x,h^2), and the cancellation of the
remaining hk coefficient. These are the actual conductor ring
conditions of de Jong--van Straten, Theorem1.12, already verified
in P4.41.

Complete the square in k, absorb sqrt(A) in x, and replace y by
y*(1+gamma*z) to make k+gamma*h the new y+z. These are invertible
analytic coordinate maps and replace h by a unit times h. Absorbing
that unit into the coefficients gives exactly

    f=x^2k^2+xh^2 C+h^4D.                         (S)

If C(0) is nonzero, substitute x=h^2v and divide by h^4. The finite
root in v is simple, so f has a smooth factor x-h^2v(y,z). Its
quotient is xk^2+h^2U with U a unit. The coordinate X=x/U puts this
factor into Xk^2+h^2. Its finite birational normalization is

    u=h/k, X=-u^2, u(y+z)=yz.

This last equation is an A1 quadric. The first factor is smooth,
and the second has rational normalization.

Suppose instead C(0)=0. Perturb D by a small constant and the linear
part of C generically, keeping C(0)=0. These changes retain every
boundary A3 germ. Now replace C by C-epsilon and scale

    x=epsilon^3 X, y=epsilon Y, z=epsilon Z.

The leading scaled equation f/epsilon^8 is

    F=X^2K^2+XH^2(L-1)+D0 H^4,
    K=Y+Z, H=YZ.

A nonempty open set of (L,D0) gives Morse critical points of nonzero
value away from the axes. For the exact example L=K,D0=1, use
W=Y-Z, so H=(K^2-W^2)/4. At W=0, the X-critical coordinate is

    X=-K^2(K-1)/32.

The remaining derivative is

    K^5*(12K^2+7K-3)/512.

For either root of 12K^2+7K-3, the full critical value and Hessian
determinant are

    K^6*(K+1)*(3K-1)/1024,
    -3K^10*(K+1)*(3K-1)*(28K^2+14K-5)/32768.

Both are nonzero: their numerators are relatively prime to the
critical polynomial, with resultants8748 and4923269424. Simplicity
and avoidance of the axes are algebraic open conditions, so arbitrarily
small generic coefficient perturbations are available. The analytic
implicit-function theorem lifts these critical points through the
higher weighted terms. Their values have nonzero leading term of
order epsilon^8. Boundary A3 transport then gives the forbidden
Morse sphere. Therefore C(0)=0 is impossible in the actual torus
degeneration, completing the standard form.

## 3. Exact ring-condition module for the mismatch form

Now put g=xk-yh and I=(g,xh,h^2). The matrix is
[[h,0],[-k,h],[y,-x]]. Appending (a,b,d) gives

    f=a*g+b*xh+d*h^2.

Its adjugate membership conditions are

    ax,ah,bx+dh,kd+by,dh-ay,ak+bh in I.

The exact colon ideals are

    I:h=(x,h), I:x=(xk,h,z^2), I:x^2=(k,h).

The first two conditions give a=hA modulo I. Then dh-ay gives
d=Ay+xD+hE. The condition bx+dh, followed by ak+bh, gives
b=-Ak+hB modulo I. More explicitly, the first condition permits
b=-Ak+hB+z^2B2. The condition ak+bh then gives z^2B2 in (x,h),
so B2 belongs to (x,y). Its x-part is already in I because
xz^2=h^2-xh modulo I, and its y-part is absorbed into hB.
The remaining condition is

    y(D+B)+kE in (x,h).

Write T=D+B. Modulo (x,h,k), the relation yT=0 in C{y}/(y^2)
forces T(0)=0. Write T=xW+yU+kV. Since k is a nonzerodivisor
modulo (x,h), the general solution is

    E=-yU-yV+xE1+hE2.

Substitution into the determinant cancels A and gives

    f in (p)+I^2, p=yh^2(x-h).

There are exact identities

    xh^3=y*g*h^2-y*p,
    h^4=y*g*h^2-k*p.

Thus every equation satisfying the actual ring condition has the
exact form

    f=A g^2+B gxh+Cgh^2+D(xh)^2+kappa*p,
    A(0) nonzero.                              (M)

## 4. Nonzero mismatch coefficient: rational normalization

Use the appended coefficients a=A*g+B*xh+C*h^2,
b=D*xh+kappa*yh, d=-kappa*yh. The actual conductor ring condition
identifies Hom(I,O_S) with the normalization, generated by1,n1,n2,
where n1=-a/h and n2=-(a*k+b*h)/h^2 are the adjugate fractions.
Since A is a unit, v=(n1+Bx+Ch)/A=-g/h and w=n2 give the same
actual normalization algebra. They satisfy the
following exact relations (all coefficients may be holomorphic):

    A v^2-Bxv-Chv+Dx^2+kappa*xy-kappa*yh=0,
    xw=A yv-Bxy-(kappa+C)yh,
    vw=kappa*h-Dxy,
    w^2+[(kappa+B)y+Ck]w-A*kappa*k+A*D*y^2
                     -D(kappa+C)yh-B*kappa*h=0.       (N)

These follow directly from g=xk-yh and the three adjugate linear
relations; no new algebra is substituted for the actual normalization.

Assume kappa(0) is nonzero. At the origin the relations give v=w=0,
so there is one normalization point. The last equation eliminates
k analytically, and k belongs to its maximal-ideal square. Since
h=y(k-y), its quadratic initial term is -y^2.
Write a=A0,b=B0,d=D0,u=kappa0. The first three quadratic equations
are

    a v^2-bxv+dx^2+u xy=0,
    xw-a yv+bxy=0,
    vw+u y^2+dxy=0.

Set V=a v-(b/2)x, delta=a*d-b^2/4,
Y=delta*x+a*u*y, W0=w+(b/2)y, W=a*u*W0+delta*V.
These are invertible linear coordinates. The equations become

    V^2+xY=0, VW+Y^2=0, xW-YV=0.

They define the irreducible rational normal cubic cone in four-space.
The full tangent-cone ideal contains this prime ideal and has the same
dimension two, so it equals it. Blowing up the normalization point
is smooth along the exceptional rational normal cubic: in each
projective chart its two independent initial equations have independent
derivatives along that smooth projective curve. The exceptional curve
is P1 with normal bundle O(-3). The exact sequences for its thickenings
have successive terms O_P1(3n), all with H1 zero. Formal functions
therefore gives R1 rho_*O=0. The normalization singularity is rational.

## 5. Vanishing mismatch coefficient: a fixed-conductor polar exclusion

Suppose kappa(0)=0. Perturb D and the linear part of kappa by arbitrarily
small generic amounts, and replace kappa by kappa-epsilon. The equation
remains in the same ring-condition module, so the fixed axes retain
generic A3 near the fixed boundary; its previously unit quartic
coefficients stay units there.

Scale x=epsilon^2 X,y=epsilon Y,z=epsilon Z. Write K=Y+Z,H=YZ and
G=XK-YH. Dividing f by epsilon^6 gives

    A0 G^2+epsilon*(B0 G XH+C0 G H^2)
      +epsilon^2*[D0(XH)^2+p(L-1)]+higher terms,
    p=YH^2(X-H).

Near a nonzero smooth point of G=0, parameter Morse elimination in
the G coordinate leaves an effective function epsilon^2*Phi plus
higher terms. The square-completion corrections are absorbed into
D and L using the exact cone identities

    XH^3=-Yp, H^4=-Kp on G=0.

Thus the leading tangential function is

    Phi=D'(XH)^2+p(L'-1) restricted to G=0.

The generic perturbations allow D',L' in a nonempty open set. The
explicit choice D'=1,L'=-Z suffices to exhibit it. Parametrize

    K=r, Y=tr, Z=(1-t)r, X=t^2(1-t)r^2.

Then

    Phi=t^4(1-t)^4*r^7*[1+r(t^2-t+1)].

At t=1/2,r=-7/6 both derivatives vanish. The value is
-823543/573308928 and the Hessian is the diagonal matrix

    diag(117649/1990656,15647317/214990848).

Its determinant is1840891197733/427972821516288, nonzero.
The angular critical numerator factors as
(2t-1)(3t^2-3t-4), so the selected point is simple and avoids the
axes and the pole K=0. Nondegeneracy is an algebraic open condition
on the coefficients. After normal elimination, divide the tangential
critical equations by epsilon^2 and apply the analytic implicit-function
theorem. The lifted full Morse points have critical values of order
epsilon^8 with nonzero leading coefficient. They approach the origin.

The fixed boundary A3 comparison transports their square-minus-two
vanishing spheres into a nearby global torus fibre, a contradiction.
Therefore kappa(0)=0 is impossible. Together with Section4 this
completes the mismatch form and hence the one-missing-coefficient
ordinary-axis case.

## Computation

The colon ideal generators, adjugates, quadratic coordinate change,
two polar critical computations, and their nonzero determinants are
checked by code/part4/a3_missing_coefficient.py. The proof above retains
the actual conductor and every boundary transverse type throughout.
