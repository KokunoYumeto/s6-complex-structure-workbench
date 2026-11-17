# P3F.34. The integral homology of every free affine OS49 cap

**Proved; correction to the general-n CSV value.**
Use the exact free sector of P3F.33, and put
\[
 m=3k,\qquad g=\gcd(m,n,3d).
\]
The calculation below gives, for \(n\ne0\),
\[
 \begin{aligned}
 H_1(X)&=H_4(X)=\mathbb Z/|n|,\\
 H_2(X)&=H_3(X)=\mathbb Z/|n|\oplus\mathbb Z/g,\\
 H_5(X)&=0,\qquad H_0(X)=H_6(X)=\mathbb Z.
 \end{aligned}                                      \tag{P3F.34.1}
\]
In the free sector \(g\) is one or three. The free example
\((m,n,d)=(9,3,1)\) therefore has
\(H_2=H_3=(\mathbb Z/3)^2\). This is not the general-n
value stated in CSV row D.2.11. The complete integral
Gysin and exterior-restriction calculation was independently
audited before this comparison was marked final.

For \(n=0\), the free criterion forces \(3\mid k\) and
\(\gcd(k,d)=1\). The same calculation gives
\[
 H_1=H_5=\mathbb Z,\quad
 H_2=H_3=\mathbb Z^2\oplus\mathbb Z/3,\quad
 H_4=\mathbb Z^2,\quad H_0=H_6=\mathbb Z.             \tag{P3F.34.2}
\]

## 1. The fixed exterior and the actual boundary circle

Remove a closed finite-cap neighbourhood. Its exterior \(V\)
does not depend on \(m,n,d\): fix the same scalar \(\lambda\)
and use the same ordinary, type-II and cusp charts. Its
boundary \(E\) is the marked mapping torus of the order-three
linear monodromy \(A\). The affine part of a torus mapping
torus is removed by an explicit translation isotopy on its
base interval. For the convention
\((x,1)\sim(Ax+a,0)\), the map to the linear mapping torus
is
\[
                    (x,t)\longmapsto(x+tA^{-1}a,t).
\]
At the two ends, \(a=A(A^{-1}a)\) verifies that this map
descends. Choose the marked base loop by the lifted path
\(x(t)=-tA^{-1}a\); its image is the zero-section base
loop, and every fibre period is unchanged. The translation
lift is the one supplied by the root gluing, so no integral
period is inserted in this comparison. This
is the same boundary trivialization used in P3F.26--29.
In particular every pair \((V,E)\) below is this one
fixed marked pair. Only the finite-cap logarithmic gluing
changes with \((k,n,d)\); the displayed isotopy uses its
chosen translation lift and adds no integral period.
Thus the exterior restriction lattice used in Section 3
is independent of all three cap integers.

Write \(\alpha\) for its base-loop generator, and let
\(\eta\in H^1(E;\mathbb Z)\) take value one on \(\alpha\)
and zero on the fibre lattice. The other integral generators
of \(H^1(E)\) are
\[
 \psi,\qquad h=-w+3\delta.
\]
The root-cap construction makes \(E\to B_{m,n,d}\) a
principal normal circle bundle. Its positively marked
circle, up to the common orientation convention, is the
actual loop
\[
             \beta_{m,n,d}=m\alpha-\ell.             \tag{P3F.34.3}
\]
It goes once around the normal root disc while its image in
the ordinary base winds \(m\) times. The compensating fibre
translation is \(-\ell\), exactly as in the root gluing.
Its values under \((\psi,h,\eta)\) are
\[
                         (-n,-3d,m).
\]
The free action criterion ensures that this is a free
geometric circle action, even when its abelianized homology
class is not primitive.

The cap retracts to the compact flat four-manifold
\(B_{m,n,d}=T^4/\langle\alpha\rangle\). Its rational
cohomology is the \(A\)-invariant exterior algebra, so
its Betti numbers are \(1,2,2,2,1\) and its Euler
characteristic is zero. Abelianizing its exact deck
presentation gives
\[
 H_1(B_{m,n,d})=\mathbb Z^3/\langle(-n,-3d,m)\rangle
               =\mathbb Z^2\oplus\mathbb Z/g.
\]
In particular
\[
 H^1(B_{m,n,d})=
 L_{m,n,d}:=\ker\bigl[(-n,-3d,m):\mathbb Z^3\to\mathbb Z\bigr].
                                                               \tag{P3F.34.4}
\]

## 2. An integral basis of the boundary two-cohomology

Keep the fibre forms
\[
 u_2=\psi h,\qquad v_2=(\psi+u)w
\]
of P3F.29, and put
\[
                 p=\eta\psi,\qquad q=\eta h/3.
\]
The four classes \(u_2,v_2,p,q\) form an integral basis
of \(H^2(E;\mathbb Z)\). The division by three in the last
class must be retained; replacing \(q\) by \(\eta h\)
would lose the torsion in (P3F.34.1).

Here is a proof using the already constructed cap
\((m,n,d)=(3,1,0)\). Denote its projection by \(\pi_0\).
The normal circle is \(3\alpha-\ell_0\), and the integral
class \(-\psi\) evaluates to one on it. Its Euler class
therefore vanishes by the integral Gysin sequence, and
this circle bundle is topologically trivial. The exact
first-cohomology pullback from this cap has basis
\[
                      h,\qquad 3\psi+\eta.
\]
P3F.29 proves that the cap's integral two-cohomology
restricts to the full fibre invariant lattice with basis
\(u_2,v_2\). Fibre integration, or direct contraction
by \(3\alpha-\ell_0\), identifies its actual boundary
pullback as
\[
                    u_2+q,\qquad v_2.
\]
Indeed these invariant forms are horizontal; the invariant
forms on the finite torus cover compute all rational
cohomology by averaging. The kernel of restriction is
spanned rationally by \(p,q\), and horizontality forces
the displayed correction uniquely. The product splitting
with the class \(-\psi\) then supplies the other two
integral classes
\[
 (-\psi)h=-u_2,\qquad
 (-\psi)(3\psi+\eta)=p.
\]
Thus \(v_2,u_2+q,u_2,p\) is an integral basis, equivalently
\(u_2,v_2,p,q\).

## 3. Determine the exterior restriction without guessing a splitting

Fill \(V\) by the \((3,1,0)\) cap. The resulting manifold
is the proved sphere of P3F.26. Its integral Mayer--Vietoris
sequence shows that \(H^2(V)\cong\mathbb Z^2\) and that
restriction identifies it with a direct summand of
\(H^2(E)\). Its complement is the cap pullback just
computed. The homology sequence similarly gives
\[
 H_1(V)=\mathbb Z,\qquad H_2(V)=\mathbb Z^2.
\]
The generator of \(H_1(V)\) is gamma, as in the exact
van Kampen calculation of P3F.26.

Let two basis vectors of the exterior restriction have
coordinates in the basis \(u_2,v_2,p,q\), and project
them modulo \(v_2\) to vectors \(U_1,U_2\in\mathbb Z^3\)
in the ordered basis \(u_2,p,q\). Write
\[
                       W=U_1\times U_2.
\]
No component of this integral vector is assumed in advance.
For the circle (P3F.34.3), integration of the invariant
forms gives the exact one-classes
\[
 \begin{aligned}
 (\pi_\beta)_*u_2&=3d\psi-nh,\\
 (\pi_\beta)_*v_2&=0,\\
 (\pi_\beta)_*p&=m\psi+n\eta,\\
 (\pi_\beta)_*q&=kh+d\eta.
 \end{aligned}                                      \tag{P3F.34.5}
\]
The circle has period one, so these are integral
fibre-integration maps, not unnormalized contractions.

For every \(k>0\) and \(d\in\mathbb Z\), the cap with
\(n=1\) gives the already proved sphere of P3F.29.
The pair sequence for attaching its disc bundle shows
that its map
\[
 H_1(B_{3k,1,d})\longrightarrow H_2(V)
\]
is an integral isomorphism. Its dual is precisely
(P3F.34.5) restricted to \(H^2(V)\). Taking cross
products of its two images gives determinant
\[
                 \pm\bigl(W_1 k-W_2d+W_3\bigr).
\]
It has absolute value one for every positive \(k\) and
every integer \(d\). Therefore
\[
                   W_1=W_2=0,\qquad W_3=\pm1.
\]
This proves integrally that the exterior image projects
isomorphically onto \(\mathbb Z u_2\oplus\mathbb Z p\)
and has no \(q\)-component. Its possible \(v_2\)-terms
vanish under (P3F.34.5), so they do not affect any map
being computed. This argument uses actual proved
sphere fillings to determine the exact restriction
lattice; it does not assume a boundary normalization.

## 4. The two Smith invariants and every homology group

After an integral change of basis in \(H^2(V)\), the
dual transfer map has the two columns
\[
       v_1=(3d,-n,0),\qquad v_2=(m,0,n)
                 \quad\text{in }L_{m,n,d}.            \tag{P3F.34.6}
\]
Their cross product is
\[
              v_1\times v_2=n(-n,-3d,m).
\]
The primitive normal of \(L_{m,n,d}\) is
\((-n,-3d,m)/g\), so their index in this rank-two
lattice is \(g|n|\). The gcd of all their entries is
\(g\). Because \(L_{m,n,d}\) is primitive in
\(\mathbb Z^3\), divisibility of a vector in it is
the same as divisibility in the ambient lattice.
Thus the first Smith invariant is \(g\), and the
second is \(|n|\). Freeness implies \(g\mid n\):
all primes other than three are excluded by
\(\gcd(k,n,d)=1\), and a nontrivial factor three
occurs exactly in the already classified \(3\mid n\)
case. In fact \(g\in\{1,3\}\).

Use the pair sequence of \(X=V\cup N(B)\), with the
Thom identification \(H_j(N(B),E)=H_{j-2}(B)\).
Its degree-two portion is
\[
 H_1(B)\longrightarrow H_2(V)\longrightarrow H_2(X)
 \longrightarrow H_0(B)\xrightarrow{\ n\ }H_1(V).
\]
For \(n\ne0\), the last arrow is injective. Torsion
in \(H_1(B)\) maps to zero in the free group \(H_2(V)\).
The transpose of the free transfer has the Smith
invariants just computed, and therefore
\[
                   H_2(X)=\mathbb Z/g\oplus\mathbb Z/|n|.
\]
P3F.33 already gives \(H_1(X)=\mathbb Z/|n|\).
Euler additivity gives \(\chi(X)=2\), because \(V\)
and \(E\) are fixed, every flat cap has Euler zero,
and the reference filling is \(S^6\). The rational
groups in degrees one and two vanish. Poincare
duality and Euler characteristic then force every
middle rational group to vanish. Integral duality
and the universal coefficient theorem give
\[
 H_3(X)\cong\operatorname{Ext}(H_2(X),\mathbb Z),\quad
 H_4(X)\cong\operatorname{Ext}(H_1(X),\mathbb Z),\quad
 H_5(X)=0.
\]
This proves all groups in (P3F.34.1).

For \(n=0\), the two vectors in (P3F.34.6) generate
\(3\mathbb Z\psi\) in the lattice
\(\mathbb Z\psi\oplus\mathbb Z(kh+d\eta)\).
The pair sequence therefore has cokernel
\(\mathbb Z\oplus\mathbb Z/3\), followed by a free
\(\mathbb Z\) kernel of the now-zero last arrow.
It gives \(H_2=\mathbb Z^2\oplus\mathbb Z/3\).
Duality and Euler characteristic give (P3F.34.2).

The executable check builds a primitive integral basis
of (P3F.34.4), expresses (P3F.34.6) in that basis,
and computes its Smith form for all sampled free triples.
The arbitrary-integer proof is the cross-product and
divisibility argument above.
