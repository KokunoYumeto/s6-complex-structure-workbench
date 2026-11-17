# Signed commutator plumbing for the fixed-edge flop

Working orientation calculation for independent audit, 17 November 2026.
The explicit charts below determine a sign which is left adjustable in
the last paragraph of Krylov's Theorem2. This note is not yet promoted
to a numbered statement.

Use H with ordered real basis (1,i,j,k), and its boundary orientation
on the unit S3. Write

    A(s,t)=(t s t^-1,t), B(s,t)=(s,s t s^-1), C=[A,B].

For a boundary map f, let Sigma_f be D4_s times S3_t glued to
S3_s times D4_t by the identification right=f(left), with the
orientations inherited from the standard boundary of D4_s times D4_t.
Here A extends the left piece and B extends the right piece. Thus
left composition by a B power and right composition by an A power
do not change the oriented diffeomorphism type of Sigma_f.

Take three products D_i=D4_s times D4_t with signs +,-,+. Glue
the S3_s times D4_t face of D_1 to that of D_2 by

    s2=s1, t2=s1 t1 s1^-1,

and the D4_s times S3_t face of D_2 to that of D_3 by

    s3=t2^-1 s2 t2, t3=t2.

These maps reverse the induced oriented boundaries because the
adjacent eight-ball signs differ. Round the common corners. The two
unattached outer faces are the standard oriented left face
D4_s times S3_t of D_1 and right face S3_s times D4_t of D_3.
Following a point across the intermediate corner gives the boundary
word g=A^-1 B. Composing on the right by the extending A and on the
left by the extending B^-1 gives

    B^-1 g A = B^-1 A^-1 B A.

In the mapping class group the commutator C is central, so the last
word is C^-1. Hence the oriented boundary of this plumbing is
Sigma_(C^-1).

There are two zero-section four-spheres. Orient the first by ds on
its D_1 hemisphere and -ds on its D_2 hemisphere. Orient the second
by dt on its D_2 hemisphere and -dt on its D_3 hemisphere. At their
single intersection in D_2, their concatenated tangent orientation
is -ds dt, exactly the orientation of D_2. Their intersection is +1.
Each normal clutch fixes a real line, so each self-intersection is
zero. The exact intersection matrix is therefore

    Q=[[0,1],[1,0]], signature(Q)=0.

On the first sphere the normal transition from its first hemisphere
to its second is Ad_s. On the second it is Ad_t^-1. The normal
orientations on the two hemispheres of the first sphere are both dt;
those on the second sphere are both -ds. Thus the two Pontryagin
numbers have opposite signs and absolute value four. Their product
is -16, independently of the convention for the sign of the SU2
clutch generator. Tangent TS4 has p1=0, so these are also the two
evaluations of p1(TW).

The handle description has no homology in degrees1,2,3 and a free
rank-two group in degree4. In particular W is spin. Since Q is
unimodular, its relative Pontryagin square is

    (p,-p) Q^-1 (p,-p)^t = -32, |p|=4.

The spin Eells--Kuiper formula gives

    mu(Sigma_(C^-1))=(-32-4*0)/896=-1/28,
    mu(Sigma_C)=+1/28.

The last equality uses the central disc-supported sphere subgroup
and the extension-by-identity identification with the double, with
the orientations just specified. The remaining comparison to the
complex six-sphere is explicit as follows. In the Cox products
u=a0+j a1, v=c0+j conjugate(c1), q=uv, h=u i u^-1,
h reverses the complex CP1 orientation and q preserves the original
complex normal orientation when H has the ordered basis above.
The complex orientation on the exterior D3_h times S3_q is therefore
the product orientation. It is the negative of the boundary
orientation of D3_h times D4_q on that face. The doubled exterior
S3_h times S3_q has the product orientation, so the central
disc-supported class C has the same positive Eells--Kuiper sign in
the complex exterior marking.

Together with the independently audited coefficient n=-6A in
notes/part3_flop_relative_group.md, this computation fixes the proposed
fixed-edge correction as +n in the positive Theta_7 generator. The
actual chart/product and boundary-word comparisons above are retained
for independent audit before any new return value is exported.
