# F.3.5: companion lemma and nodal transvection before reading

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.

Only the isolated companion statement packet and the supplied genus-two
node data have been read. The target F.3.5 proof remains unopened.

## 1. Rational simultaneous conjugacy, with the actual conjugating map

Let D=R-S=u*v, where u is a nonzero rational column and v a rational
row. The characteristic polynomial f of R is irreducible of degree
four. The annihilator of u under Q[T], with T acting by R, is a
nonconstant divisor of f and hence f itself. Therefore

                         B=(u,Ru,R^2u,R^3u)

is invertible over Q, and B^-1 R B=Cf. Write w=vB. In this basis
B^-1 S B=Cf-e1*w. The rank-one determinant identity gives

 g(t)-f(t)=w*adj(tI-Cf)*e1.

The adjugate column equals

 (t^3+t^2+t+1, t^2+t+1, t+1, 1)^t.

This identity follows by multiplication with tI-Cf and f(t)e1,
or directly from the characteristic relation for Cf. Since
g-f=-t^3-t^2-t, comparison of coefficients gives

                              w=(-1,0,0,1).

Thus the ordered pair in its B-basis is uniquely determined.
For the actual displayed companion pair, put
d=(Cf-Cg)e4=(0,-1,-1,-1)^t and
Bc=(d,Cf*d,Cf^2*d,Cf^3*d). Its columns are

 (0,-1,-1,-1), (1,1,0,0), (0,1,1,0), (0,0,1,1),

and det(Bc)=1. The row e4^t Bc is precisely (-1,0,0,1).
Consequently

                              P=B*Bc^-1

is the actual rational conjugating map, with R P=P Cf and
S P=P Cg. It proves the claimed simultaneous conjugacy and its
uniqueness. All maps and coefficient identities have been specified;
the separate integral marking is left to its cited input.

## 2. The supplied genus-two node and its normalization

The curve is y^2=x^5+lambda^3*x+lambda^4, and the distinguished
parameter is a=-256/3125 with double root r=64/625. At that point the
second x-derivative is 20r^3, which is nonzero. The discriminant is
lambda^15*(256+3125lambda), with a simple zero at a. Thus the local
family is a transverse one-node smoothing. Factoring the polynomial
at a as (x-r)^2 times a squarefree cubic shows that the map

                          (x,y) -> (x,y/(x-r))

is the normalization away from the node; its completion is the given
irreducible genus-one normalization. The two points over the node
are joined by the vanishing annulus in a smoothing.

## 3. Primitive nonseparating vanishing cycle and its monodromy

Remove small discs about those two points on the connected genus-one
normalization and glue in the smoothing annulus xy=t. The core
circle delta of that annulus is the vanishing cycle. Its complement
is connected because the punctured normalization is connected, so
the cycle is nonseparating. Choose an arc in that complement joining
the two boundary circles, and close it through the annulus. The
resulting integral cycle gamma meets delta once. This actual
intersection shows delta is primitive: a nontrivial multiple could
not pair to one with gamma.

The local relation y=t/x identifies the two annular boundary
coordinates. One positive turn of t changes their relative angle by
2*pi, while the exterior remains fixed. In annulus coordinates the
resulting return is theta -> theta+2*pi*rho(s), where rho is zero
at one boundary and one at the other. This is one positive Dehn
twist. Its sign can also be fixed directly by the annular period:
the normalized transverse logarithmic period is log(t)/(2*pi*i),
which increases by one on a positive loop. In the corresponding
ordered pair (delta,gamma), the return fixes delta and sends gamma
to gamma+delta; it is the identity on the cycles carried by the
complement.

The image of T-I is therefore exactly Z*delta, and (T-I)^2=0,
because delta is fixed. This proves the primitive rank-one
transvection used in the rational companion comparison. The
genus-one normalization supplies the connected complement and the
dual intersecting cycle explicitly; the primitive conclusion is not
inferred just from the numerical rank.

## Computation and next comparison

A fresh exact program will check the displayed companion column,
coefficient row, conjugating model basis, discriminant and nodal
factorization. This written derivation is complete before the target
proof and before any producing code are opened. The integral marking
and the remaining F.3.5 steps have their own reviewer scopes.
