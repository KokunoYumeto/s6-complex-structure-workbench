# The exact boundary twist for a simple flop

Working proof, 17 November 2026. The quaternionic boundary map and the
explicit relative generators below are calculated here. The actual-family
stable derivative and the oriented identification with the run's Theta_7
generator still require the checks stated at the end. No arbitrary-fan
return value is assigned by this note.

## 1. The two actual normal products

Write the conifold link as

    K=(S^3_a times S^3_c)/S^1,
    (a,c) ~ (e^{i phi}a,e^{-i phi}c)

in complex coordinates. With the quaternion convention already used in
the Cox calculation put

    u=a0+j a1,   v=c0+j conjugate(c1),
    (u,v) ~ (u e^{i phi},e^{-i phi}v),
    q=uv,       h=u i u^{-1},       k=v^{-1} i v.

The first resolution has base h and real normal coordinate q; the
second has base k and the same real normal coordinate q. These are actual
products: choose a unit representative u of h and set v=u^{-1}q in the
first case; choose a unit representative v of k and set u=qv^{-1} in the
second. A different representative changes only the displayed auxiliary
S^1 orbit. Both inverse constructions are smooth in the quotient charts.

The exact boundary map is therefore

    tau(h,q)=(q^{-1} h q,q).                              (FG.1)

It extends over D^3 times S^3 by

    T(y,q)=(q^{-1} y q,q),   y in Im(H), |y|<=1.          (FG.2)

The map is smooth at y=0, and its inverse is
(y,q) -> (q y q^{-1},q). It preserves the product orientation.
Complex orientations must be compared in these same products; changing
the quaternion convention in only one normal product would change the
displayed signs.

## 2. Explicit relative generators and an exact conjugation

Choose an SO(3)-equivariant smooth degree-one map

    zeta:(D^3,S^2)->(S^3,1)

constant on a boundary collar. One explicit choice is
zeta(y)=cos(phi(r))-sin(phi(r)) y/r, with phi decreasing from pi to
zero, linear to first order at the centre and flat near the boundary;
the odd Taylor conditions at the centre make the formula smooth.
It commutes with y and satisfies
zeta(q y q^{-1})=q zeta(y)q^{-1}. Define actual relative maps

    L(y,q)=(y,zeta(y)q),     R(y,q)=(y,q zeta(y)).         (FG.3)

They commute and extend over D^3 times D^4 by the same quaternionic
multiplications. Thus their extensions to the boundary S^6 of that
seven-disc are isotopically trivial in the standard sphere filling.
Their integer powers and products have the same explicit extensions.

Substitution, with no isotopy, gives

    T L T^{-1}=R.                                        (FG.4)

The calculation uses both equivariance of zeta and the commutation of
zeta(y) with y. The localized maps double to the usual quaternion maps
on S^3 times S^3, up to isotopy through degree-one choices of zeta.

## 3. The central relation and its orientation limitation

The primary paper of Krylov, arXiv:math/0107005, defines
A(s,t)=(tst^{-1},t), B(s,t)=(s,sts^{-1}), Y(s,t)=(s,st).
Its Theorems 2--3 give the central commutator C=[A,B], of order 28,
and the relation AY=YAB. The proof establishes that C generates Theta_7;
its last orientation choice on printed p12 is explicitly adjustable.
Consequently this note defines C by that commutator and does not silently
equate it with the oriented generator used elsewhere in this run.

Our T=A^{-1}, L=Y and R=YB^{-1}. Hence, in the doubled mapping class
group, direct use of those relations gives

    T R T^{-1}=L^{-1}R^2 C,
    T(L^m R^n C^s)T^{-1}=L^{-n}R^{m+2n}C^{s+n}.          (FG.5)

The first relative map in (FG.5) is fixed on the boundary because it is
a conjugate of a relative map. The extension-by-identity injection of
relative pseudo-isotopy classes into the double is Krylov,
arXiv:math/0409342, Proposition1. Its Lemma3 identifies the relative
group in this dimension as Theta_7 plus two infinite cyclic factors.
Here those factors are represented by (FG.3): their evaluation on the
relative D^3 cycle gives the sum m+n, and their normal derivative
difference generates the kernel of that evaluation. The central
disc-supported classes are unchanged by conjugation with T.

## 4. The stable derivative detects the second coefficient

Use the Cartesian frame on D^3 and the left-invariant quaternion frame
on S^3. Along L, the derivative matrix has diagonal blocks I_3,I_3
and a lower off-diagonal block. Scaling that lower block to zero is a
homotopy through invertible matrices, fixed at the boundary. Thus its
relative stable derivative is zero.

Along R, the same matrix has diagonal blocks I_3,Ad(zeta^{-1}); its
off-diagonal block is removed by the same explicit homotopy. The
stabilization of Ad:S^3->SO(3) represents twice a generator of pi_3(SO).
This factor follows from the adjoint rank-three bundle: for an SU(2)
bundle with Chern roots x,-x, the complexified adjoint has roots
2x,0,-2x, so p1(ad)=-4c2 whereas the quaternionic real four-plane has
p1=-2c2. Choose the stable generator by the latter convention.

The relative stable derivative of L^m R^n is therefore -2n. This
calculation is in the fixed product framing. A change of the boundary
framing can change its relation with the variation integer; it cannot
be discarded before identifying the actual Cox products.

## 5. The actual remaining comparison

The exact flop map (FG.1) replaces the previously uncomputed local
boundary identification by an explicit conjugation. For the actual
family, the remaining tasks are to extend that product marking to its
exterior and evaluate the relative stable derivative there, with all
finite caps and the period reindexing retained. The ordinary torus
tangent matrices are triangular and the nodal maps in
notes/part3_nodal_frames.md remove their parameter dependence on the
punctured overlaps. The still required step is their global gluing to
the boundary framing in (FG.1). Absolute vanishing of p1 does not supply
that relative comparison.

The other orientation check is the sign of C relative to the run's
positive Eells--Kuiper generator. No sign is needed to recognize the
zero coefficient, but a nonzero coefficient requires this check. The
manuscript does not assign a general-fan value before these tasks are
completed.
