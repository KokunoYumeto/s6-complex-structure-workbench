# Independent fixed-edge derivative and orientation audit

17 November 2026. This note audits the actual-family coefficient in the
relative group used in notes/part3_flop_relative_group.md. Section 5
also independently checks the oriented Eells--Kuiper sign of its
commutator \(C\). It makes no assertion about a flop at a curve which
is not a semifree fixed edge.
The exact local matrix checks are in
`code/part3_fourfold/fixed_edge_signs.py` and its JSON certificate.

## 1. The two quaternion products retain the complex orientation

Use the orientation ((1,i,j,k)) of (mathbb H), and write

\[
 u=a_0+j a_1,\qquad v=c_0+j\overline{c_1},\qquad
 q=uv,\qquad h=u i u^{-1},\qquad k=v^{-1} i v.
\]

At the first north pole, (a_1=x+iy) gives the derivatives

\[
 (\partial_xh,\partial_yh)=(-2k,-2j).
\]

The matrix in the positively oriented tangent plane ((j,k)) has
determinant (-4). Thus the quaternion (h)-sphere has the opposite
orientation from the complex first exceptional curve. At (u=1),

\[
 q=(\Re c_0)+i(\Im c_0)+j(\Re c_1)+k(\Im c_1),
\]

so the (q)-normal orientation is the original complex normal
orientation. The first complex normal neighbourhood consequently has
orientation (-[S^2_h]\,[D^4_q]). Its complement has boundary orientation

\[
 [\partial E]=[S^2_h]\,[S^3_q],
 \qquad [E]=[D^3_y]\,[S^3_q].                    \tag{FE.1}
\]

This last orientation is opposite to the orientation induced on

\(D^3\times S^3\subset\partial(D^3\times D^4)\).
Indeed its outward (q)-radial vector must cross the three (y)-vectors.

For the second resolution, (c_1=x+iy) gives

\[
 (\partial_xk,\partial_yk)=(2k,-2j).
\]

This has determinant (+4); its base coordinate preserves the complex
orientation. Its normal coordinate (q=u=a_0+j a_1) reverses the complex
normal orientation. The second complex normal neighbourhood is therefore
again (-[S^2_k]\,[D^4_q]). The actual common exterior retains (FE.1).
In particular the map ((y,q)\mapsto(q^{-1}yq,q)) preserves its oriented
product marking.

## 2. The physical Hopf action and the variation sign

At the first exceptional curve the physical circle weights are

\((-1,+1)\) on the two complex normal coordinates. In the above real
normal product its action is exactly

\[
 q\longmapsto q e^{-i\theta}.
\]

The Hopf quotient is (z=q i q^{-1}\in S^2\subset\operatorname{Im}\mathbb H).
At (q=1), its derivatives in the (j,k) directions are (-2k,2j),
which preserve the sphere orientation. The physical circle vector is

\(-i\), so

\[
 [S^3_q]=-[S^1_\delta]\,[S^2_z].
\]

Moving this circle vector past the three exterior (y)-vectors gives

\[
 [E]=[S^1_\delta]\,[D^3_y]\,[S^2_z].             \tag{FE.2}
\]

Thus the quotient exterior and its closed conifold filling have the
product orientation (D^3_y\times S^2_z) and (S^3_y\times S^2_z),
respectively. This is the order (S^2\times S^3) as well, since (2\cdot3)
is even.

Let (t) be the relative variation in the marking (D^3_y\times S^3_q).
For the physical mapping torus, a relative (D^3\times[0,1]) gives

\[
 [S^2_h\times S^1_\theta]=t[S^3_q]
\]

because its oriented boundary is

\(S^2_h\times[0,1]-D^3\times\{1\}+D^3\times\{0\}\).
The integral Gysin--Stokes calculation in
`notes/part3_exterior_variation.md` gives the boundary cohomology slope

\(k_{\rm Jin}\) when the base sphere is given the complex curve
orientation. The first paragraph proves that the (h)-orientation is
its negative. Hence, in the exact quaternion product used here,

\[
                         t=-k_{\rm Jin}.         \tag{FE.3}
\]

This is also verified directly by the generator below, without changing
the circle orientation or the mapping-torus convention.

## 3. The universal Jin clutch has (p_1=-4\deg g)

Choose the degree-one map

\[
 \zeta(y)=\cos\phi(|y|)-\sin\phi(|y|)\frac{y}{|y|},
\]

where (\phi) decreases from (\pi) to (0), is flat near the boundary,
and has the smooth odd radial expansion at zero. Its degree is (+1):
the decreasing radial coordinate and the antipodal map on (S^2) each
reverse orientation. Define

\[
 L(y,q)=(y,\zeta(y)q),\qquad
 R(y,q)=(y,q\zeta(y)),\qquad
 B=LR^{-1}.
\]

The variation of (L) is (+1), from the degree of the graph

\(q=\zeta(y)\). It commutes with the physical right circle. Its quotient
is ((y,z)\mapsto(y,\operatorname{Ad}_{\zeta(y)}z)\).

For Jin's mapping-torus identification

\((v,0)\sim(g(y)v,1)\), the connection in the product frame can be chosen

\[
 A_\theta=-\theta\,dg\,g^{-1},\qquad 0\leq\theta\leq1.
\]

The endpoint transformation is correct because

\(A_1=gA_0g^{-1}-dg\,g^{-1}\).
For the right Maurer--Cartan form (\omega=dg\,g^{-1}),

\[
 d\omega=\omega^2,\qquad
 F=-d\theta\wedge\omega+(\theta^2-\theta)\omega^2.
\]

Use the product orientation (S^3_y\times S^1_\theta). Then

\[
 \int\operatorname{tr}(F^2)
 =2\!\int_0^1(\theta^2-\theta)\,d\theta
       \int_{S^3}\operatorname{tr}(\omega^3).
\]

In the standard quaternion matrix representation,

\(\operatorname{tr}(ijk)=-2\), so the right Maurer form on the
positively oriented unit quaternion sphere has

\(\int\operatorname{tr}(\omega^3)=-24\pi^2\deg g\).
Consequently

\[
 \langle c_2,[S^3\times S^1]\rangle
 =\frac{1}{8\pi^2}\int\operatorname{tr}(F^2)=\deg g,
 \qquad
 \langle p_1(\operatorname{ad}g),[S^3\times S^1]\rangle
 =-4\deg g.                                      \tag{FE.4}
\]

For (L), this adjoint three-plane bundle has the quotient sphere
bundle as its unit sphere bundle. The base (S^3\times S^1) is
parallelizable and has (H^2=0). The vertical Euler class is (2x),
where (x) is the actual meridian-one circle class, so its square is
the pullback of (p_1=-4[y\theta]). Therefore

\[
                    (k_L,\ell_L)=(-1,-4).         \tag{FE.5}
\]

This agrees with (FE.3) and its variation (+1). Composing an actual
equivariant return of variation (t) with (L^{-t}) consequently changes
its quotient characteristic pair to

\[
 k_0=0,\qquad \ell_0=\ell-4k.                    \tag{FE.6}
\]

The characteristic assignments are homomorphisms on the relevant
homologically trivial mapping classes; their mapping-torus
pair-of-pants bordism carries the actual circle line and proves
additivity. No independent choice of quotient line is made in (FE.6).

## 4. Integral Gysin detection of the second relative coefficient

The actual exterior return, after killing variation as above, has
relative class

\[
                           B^b C^s.
\]

Double the exterior by its fixed product cap. This gives the actual
principal circle bundle over the closed conifold quotient and, in each
fibre, the oriented manifold (S^3_y\times S^3_q). On its Jin mapping
torus, the total tangent bundle is the pullback of the quotient tangent
bundle plus the trivial vertical line. Thus the first Pontryagin class
is the pullback of the quotient class.

The closed quotient mapping torus has (H^2=\mathbb Zx) and

\(H^4=\mathbb Z[y\theta]\). Equation (FE.6) says (x^2=0).
The integral Gysin sequence therefore makes

\[
 H^4(\text{quotient mapping torus};\mathbb Z)
 \longrightarrow
 H^4(\text{circle total mapping torus};\mathbb Z)
\]

injective: its kernel is precisely (x\,H^2=0).

Represent the relative class by (B^b C^s), with the disc supporting

\(C^s\) chosen away from (S^3_y\times\{q=1\}\). The representative
fixes this three-sphere pointwise. Its normal clutch on the resulting
four-cycle (S^3_y\times S^1_\theta) is exactly

\[
                       \operatorname{Ad}_{\zeta(y)^b}.
\]

Its first Pontryagin number is (-4b) by (FE.4). The pulled-back class

\([y\theta]\) evaluates (1) on this cycle. To see that this statement
retains the actual marking, restrict to one fibre: the class is the

\(y\)-sphere generator. The possible (x\theta\) ambiguity of a
quotient (H^3) lift pulls back to zero, and the total fibre has

\(H^2(S^3\times S^3)=0\). An isotopy between representatives gives a
mapping-torus diffeomorphism which is the identity on the chosen
initial fibre; it therefore retains this cohomology marking.

It follows that

\[
 \ell-4k=\ell_0=-4b.
\]

With the run's index convention (A=(4k-\ell)/24\), the exact result is

\[
                    b=6A,\qquad n=-b=-6A,        \tag{FE.7}
\]

where (n) is the exponent of (R) after rewriting in commuting

\(L,R\) generators. In the fixed Cartesian/left-quaternion frame the
stable derivative is (2b=12A\), agreeing with the direct derivatives

\(dL=0\), (dR=-2\).

Equations (FE.1)--(FE.7) do not choose the orientation of the
disc-supported class \(C=[A,B]\). The separate boundary construction
below supplies that sign.

## 5. Independent audit of the signed commutator plumbing

The explicit construction in notes/part3_flop_commutator_orientation.md
uses three products \(D_i=D^4_s\times D^4_t\), oriented with signs
\(+,-,+\). The first gluing is on the right face and is
\((s,t)\mapsto(s,sts^{-1})=B(s,t)\).
The second is on the left face and is
\((s,t)\mapsto(t^{-1}st,t)=A^{-1}(s,t)\).
Each coordinate map preserves the product face orientation, whereas
the ambient eight-ball signs on its two sides are opposite; thus
these are the required orientation-reversing boundary identifications.
The remaining left face belongs to \(D_1\), and the remaining right
face belongs to \(D_3\). Following a point through the two identified
corners gives \(g=A^{-1}B\), from left to right.

The map \(A\) extends the left face \(D^4_s\times S^3_t\), and
\(B^{-1}\) extends the right face \(S^3_s\times D^4_t\).
These orientation-preserving extensions identify the boundary with
the gluing defined by
\[
 B^{-1}gA=B^{-1}A^{-1}BA=C^{-1}.
\]
The last equality uses the already established centrality of the
specific commutator, and does not change its sign by choosing a new
generator. Here \(\Sigma_f\) always means right coordinate
\(=f(\text{left coordinate})\), with the orientations of
\(\partial(D^4_s\times D^4_t)\).

The first zero-section sphere is oriented by \(ds\) in \(D_1\) and
\(-ds\) in \(D_2\). The second is oriented by \(dt\) in \(D_2\)
and \(-dt\) in \(D_3\). Their only intersection is in \(D_2\),
where their concatenated orientation is \(-ds\,dt\), precisely
the orientation of \(D_2\). Both normal clutches fix a real line.
The intersection form is therefore
\[
 Q=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
The first normal clutch is \(\operatorname{Ad}_s\); the second is
\(\operatorname{Ad}_{t^{-1}}\). The two first normal frames have
orientation \(dt\), and the two second normal frames have orientation
\(-ds\). This latter reversal introduces no extra Pontryagin sign:
quaternionic conjugation reverses the four-plane orientation and
commutes with every adjoint action. The base hemisphere conventions
are identical for the two clutches, while the clutch maps have
opposite degrees. Their Pontryagin evaluations are consequently
\((p,-p)\), with \(|p|=4\). This establishes the relative sign
without requiring a convention for the individual SU(2) clutch.

The handle presentation has two four-handles and no homology in
degrees one through three. It is spin and has signature zero. The
unimodular matrix \(Q\) gives
\[
 \langle p_1^2,[W,\partial W]\rangle
 =(p,-p)Q^{-1}(p,-p)^{\mathsf T}=-32.
\]
The spin Eells--Kuiper formula therefore gives
\[
 \mu(\Sigma_{C^{-1}})=-\frac1{28},\qquad
 \mu(\Sigma_C)=+\frac1{28}.                         \tag{FE.8}
\]

For completeness, the comparison with the actual Hopf transfer
P3F.22 has two explicit reversals. Its positively oriented Hopf
sphere \(u\) has orientation \(-q\), by (FE.2). Its ordered factors
are \((u,y)\), whereas the plumbing factors are \((y,q)\).
Thus
\[
 D^4_u\times S^3_y
       \longleftrightarrow -(S^3_y\times D^4_q),\qquad
 S^3_u\times D^4_y
       \longleftrightarrow -(D^4_y\times S^3_q).
\]
The two pieces exchange, and each has the opposite orientation.
The literal left-to-right gluing map is consequently inverted:
\[
                         \lambda(F)=-\Sigma_{F^{-1}}.
\]
For a disc-supported class the sphere-gluing map is the homomorphism
to oriented homotopy spheres, so
\(\Sigma_{F^{-1}}=-\Sigma_F\). One can see this directly by putting
the supporting disc in the common boundary and cancelling the two
opposite product collars. Hence \(\lambda(C)=\Sigma_C\), and the
positive sign in (FE.8) is the run's positive Eells--Kuiper sign.

The exact boundary flop conjugation from the parent note shifts the
central exponent by \(n\). Equations (FE.7)--(FE.8) therefore give the
signed fixed-edge formula
\[
                          A_{\rm after}=-5A_{\rm before}
                                  \pmod {28}.       \tag{FE.9}
\]
This statement concerns the actual change across a semifree fixed
edge with the specified common exterior and complex orientations.
It does not assign the relative derivative or the correction for a
flop at another toric edge.

The exact matrix arithmetic and central-word check are exported in
code/part3_fourfold/commutator_orientation.py and its JSON output.
