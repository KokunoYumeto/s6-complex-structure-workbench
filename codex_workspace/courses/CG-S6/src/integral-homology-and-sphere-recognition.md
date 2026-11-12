# Integral homology and recognition of the six-sphere {#cg-s6-07}

CG-S6 · Lesson 7

This chapter proves the full integral homology, the original degree-one homotopy equivalence and its smooth recognition. The included companions supply the complete receiving topology, stable-group, framing and sphere-twist arguments. Four exercises have complete solutions. These are author-written and self-checked proofs; no independent review or exhaustive literature audit is claimed.

We retain the compact threefold \(f:X\to B=\mathbb P^1\) of lesson 5, with its original periods, affine translations and cusp action. Lesson 6 proves \(\pi_1(X)=1\). Here we calculate integral cohomology through the actual specialization maps. In particular, a rational rank calculation will not stand in for an integral lattice calculation.

Write \(p_0=\infty,p_1=0,p_2=1\), \(B^\circ=B\setminus\{p_0,p_1,p_2\}\), and \(j:B^\circ\hookrightarrow B\). On a marked smooth fibre \(F\), use

\[
V=H^1(F;\mathbb Z)=\mathbb Z\langle\gamma,u,w,\delta\rangle,\qquad
q=uw+6\gamma\delta,\qquad
\operatorname{vol}=\gamma uw\delta .
\tag{0.1}
\]

Products of covectors denote exterior products in the displayed order. The original lattice is \(\Lambda=\mathbb Z\langle\widehat\gamma,\widehat u,\widehat w,\widehat\delta\rangle\). The deck matrices \(A_j\), cohomological matrices \(T_j=(A_j^{-1})^{\mathsf t}\), cusp matrices \(M_0=(A_1A_2)^{-1}\), \(T_0=(T_1T_2)^{-1}\), and based meridians remain precisely those of lesson 6.

The included [integral duality companion](integral-duality-and-the-specialization-lattices.md) proves compact-support Poincaré duality, finite generation, the full integral pairing and the exact covering comparison. Its singular-chain prerequisites are included as well. These are the integral foundations used in Sections 1–2 and 7 below.

## 1. Integral cohomology of the two finite central surfaces {#finite-cohomology}

Put

\[
\begin{gathered}
m_1=3,\quad m_2=4,\qquad
v_1=(1,2,-4,0)^{\mathsf t},\quad
v_2=(-1,-3,3,0)^{\mathsf t},\\
\eta_1=2u+w+3\delta,\qquad \eta_2=u+w+2\delta.
\end{gathered}
\tag{1.1}
\]

The central reduced surface is \(S_j=(\mathbb R^4/\Lambda)/\langle g_j\rangle\), with \(g_j[x]=[A_jx+v_j/m_j]\), and the covering \(\pi_j:F_j\to S_j\) has degree \(m_j\). Lessons 1–3 prove freeness, holomorphicity, the full normal boundary and the comparison with the varying family.

**Proposition 1.1.** Both central surfaces have torsion-free integral homology and cohomology, with ranks

\[
(b_0,b_1,b_2,b_3,b_4)=(1,2,2,2,1).
\tag{1.2}
\]

**Proof.** Their universal cover is \(\mathbb R^4\). The deck group has the exact presentation

\[
\Gamma_j=\left\langle t_\lambda,g\ \middle|\
t_\lambda t_\mu=t_{\lambda+\mu},\
g t_\lambda g^{-1}=t_{A_j\lambda},\
g^{m_j}=t_{v_j}\right\rangle.
\tag{1.3}
\]

Its abelianization is

\[
H_1(S_j;\mathbb Z)=
\frac{\Lambda/(A_j-I)\Lambda\ \oplus\ \mathbb Z g}
{\mathbb Z([v_j],-m_j)}.
\tag{1.4}
\]

Lesson 1, Proposition 2.1, gives the entire image lattices. More explicitly, the two surjective maps

\[
\begin{aligned}
\Lambda&\longrightarrow\mathbb Z^2,&
(a,b,c,d)&\longmapsto(a,2b+c+3d),\\
\Lambda&\longrightarrow\mathbb Z^2,&
(a,b,c,d)&\longmapsto(a,b+c+2d)
\end{aligned}
\tag{1.5}
\]

have kernels \((A_1-I)\Lambda\) and \((A_2-I)\Lambda\), respectively. Surjectivity follows by taking \((a,b,c,d)=(a,0,e,0)\). Under these maps \(v_1\) has image \((1,0)\), and \(v_2\) has image \((-1,0)\). Thus the sole relation in the free rank-three group in (1.4) has coefficient \(+1\) or \(-1\) on its first coordinate. Eliminating that coordinate proves \(H_1(S_j)=\mathbb Z^2\), with no finite summand.

The affine quotient is a closed oriented real four-manifold, since \(\det A_j=1\). Its Euler characteristic is zero: a finite covering of degree \(m_j\) multiplies the alternating cell count by \(m_j\), and a four-torus has Euler characteristic \((1-1)^4=0\). Integral Poincaré duality gives \(H_3(S_j)=H^1(S_j)=\mathbb Z^2\) and \(H^3(S_j)=H_1(S_j)=\mathbb Z^2\). In the universal-coefficient sequence

\[
0\longrightarrow\operatorname{Ext}(H_2(S_j),\mathbb Z)
\longrightarrow H^3(S_j;\mathbb Z)
\longrightarrow\operatorname{Hom}(H_3(S_j),\mathbb Z)
\longrightarrow0,
\tag{1.6}
\]

the first group is finite and the middle group is free. Hence the first group is zero. For a finitely generated abelian group, this removes every torsion summand of \(H_2\). The Euler characteristic now gives
\(0=1-2+b_2-2+1=b_2-2\), so \(H_2(S_j)=\mathbb Z^2\). The remaining groups and cohomology follow from connectedness, orientation and universal coefficients. ∎

The absence of torsion is needed before using transfer to infer injectivity. Transfer alone gives \(m_j\alpha=0\) when \(\pi_j^*\alpha=0\); it does not remove torsion by itself.

## 2. Every finite specialization index {#finite-specialization}

For \(0\leq r\leq4\), define
\(L_j^r=\pi_j^*H^r(S_j;\mathbb Z)\subseteq(\bigwedge^rV)^{T_j}\).
The target invariance follows from the deck action. Summing a cochain over the sheets gives transfer with
\(\operatorname{tr}\pi_j^*=m_j\); Proposition 1.1 therefore proves injectivity in every degree.

**Theorem 2.1.** The indices of these exact images are

\[
\begin{array}{c|ccccc}
&r=0&r=1&r=2&r=3&r=4\\ \hline
j=1&1&3&1&1&3\\
j=2&1&4&2&2&4 .
\end{array}
\tag{2.1}
\]

In degrees one and two the full images are

\[
\begin{aligned}
L_1^1&=\langle3\gamma,\eta_1\rangle,&
L_2^1&=\langle4\gamma,\eta_2\rangle,\\
L_1^2&=(\bigwedge^2V)^{T_1}
      =\langle\gamma\eta_1,q\rangle,&
L_2^2&=\{a\gamma\eta_2+bq:a\equiv b\pmod2\}.
\end{aligned}
\tag{2.2}
\]

The nonzero degree-three cokernel at \(p_2\) is generated by the image of \(\gamma uw\).

**Proof in degree one.** A homomorphism \(\Gamma_j\to\mathbb Z\) restricts to a covector \(\alpha\in V\). Relation (1.3) says exactly
\(\alpha A_j=\alpha\) and \(m_j h(g)=\alpha(v_j)\). Conversely these two conditions define a homomorphism on all generators of (1.3), so they are sufficient as well. The original matrices give

\[
V^{T_j}=\langle\gamma,\eta_j\rangle,\qquad
\gamma(v_1)=1,\quad\gamma(v_2)=-1,\quad
\eta_1(v_1)=\eta_2(v_2)=0.
\tag{2.3}
\]

Consequently \(a\gamma+b\eta_j\) extends precisely when \(m_j\mid a\). This proves both degree-one image lattices.

**The degree-two invariant lattices.** Use the ordered coordinates
\((\gamma u,\gamma w,\gamma\delta,uw,u\delta,w\delta)\).
Writing a two-form as \((a,b,c,d,e,f)\), its invariance equations reduce integrally to

\[
\begin{array}{c|ccc}
T_1&e=f=0&a=2b&c=3b+6d\\
T_2&e=f=0&a=b&c=2b+6d .
\end{array}
\tag{2.4}
\]

These equations follow by applying the exterior square of the original matrix to each of the six basis vectors and equating coefficients. They also show sufficiency: the resulting vector is \(b\gamma\eta_j+dq\), with arbitrary integers \(b,d\). Thus there is no additional finite-index over-lattice.

With evaluation on the original orientation class \(\operatorname{vol}\), the intersection matrices of these bases are

\[
B_1=\begin{pmatrix}0&3\\3&12\end{pmatrix},
\qquad
B_2=\begin{pmatrix}0&2\\2&12\end{pmatrix}.
\tag{2.5}
\]

Indeed \((\gamma\eta_j)^2=0\),
\(\gamma\eta_1q=3\operatorname{vol}\),
\(\gamma\eta_2q=2\operatorname{vol}\), and
\(q^2=12\operatorname{vol}\).
The middle integral intersection form on \(S_j\) is unimodular by Proposition 1.1 and Poincaré duality. Pullback multiplies it by \(m_j\). If \(k_j=[(\bigwedge^2V)^{T_j}:L_j^2]\), taking absolute determinants therefore gives

\[
9k_1^2=3^2,\qquad4k_2^2=4^2.
\tag{2.6}
\]

Thus \(k_1=1\) and \(k_2=2\). Determining the second image, rather than only its index, requires the next two calculations.

**The missing coset at order four.** The cyclic extension (1.3) has extension cocycle

\[
e(a,b)=
\begin{cases}0,&a+b<4,\\v_2,&a+b\geq4,\end{cases}
\qquad 0\leq a,b\leq3,
\tag{2.7}
\]

using the representatives \(1,g,g^2,g^3\). Indeed multiplication of the two representatives crosses \(g^4=t_{v_2}\) exactly in the second case, and \(A_2v_2=v_2\). The cyclic resolution has alternating differentials \(T_2-I\) and \(N_2=I+T_2+T_2^2+T_2^3\). Hence

\[
H^2(C_4;V)=V^{T_2}/N_2V
=\langle\gamma,\eta_2\rangle/
  \langle4\gamma,2\eta_2\rangle.
\tag{2.8}
\]

This resolution is exact before applying coefficients: in the group ring, the kernel of multiplication by \(g-1\) consists of the constant coefficient sums, the multiples of \(1+g+g^2+g^3\); the kernel of that sum consists of coefficient vectors whose sum is zero, which are exactly the multiples of \(g-1\).

The cochain obstruction to extending an invariant one-form through the quotient is its evaluation on (2.7). Thus the degree-two transgression of \(\gamma\) is \(\gamma(v_2)=-1\pmod4\), whereas that of \(\eta_2\) is zero. To see the convention directly, extend a fibre homomorphism to the chosen representatives by value zero. The failure of its value on a product to equal the sum of its values is precisely its value on the inserted translation \(e(a,b)\). This is the representing two-cocycle. With this convention the cochain product rule yields

\[
d_2(\gamma\eta_2)=-[\eta_2]\ne0
\quad\hbox{in }H^2(C_4;V).
\tag{2.9}
\]

Here the spectral sequence is the one obtained by filtering the group cochains of (1.3) by quotient degree; its zero-column edge map is restriction to \(\Lambda\), namely the covering pullback. An element in this edge image survives every differential. Equation (2.9) therefore proves \(\gamma\eta_2\notin L_2^2\).

Because the index is two, the remaining possibilities are
\[
L_2^2=\langle2\gamma\eta_2,\ a\gamma\eta_2+q\rangle,
\qquad a\in\{0,1\}.
\tag{2.10}
\]

<span id="finite-descent-parity"></span>
**The exact affine descent condition.** The [integral line-bundle companion](integral-line-bundle-descent-for-the-affine-fillings.md#affine-descent-criterion) constructs a smooth line bundle on the original torus for every invariant class \(r\gamma\eta_2+s q\), retaining all its integer transition factors. It proves that descent through the actual action \(x\mapsto A_2x+v_2/4\) requires an integer row whose fourth coordinate is
\[
\ell_3=-\frac{r+3s}{2}.
\tag{2.10a}
\]
This is necessary for every smooth lift: any two lifts differ by a unit-circle function on the original torus, and its winding row must solve the full norm equation. It is also sufficient. The companion constructs the entire lifted action with row \((9s,0,0,-(r+3s)/2)\) and constant phase \(27s/32\), and verifies its exact fourth-power identity with the original translation \(v_2\). For the candidate class \(a\gamma\eta_2+q\) in (2.10), set \(r=a,s=1\). Condition (2.10a) forces \(a+3\) even, hence \(a=1\). This supplies the parity step directly from the original affine maps.

Pulling the basis (2.10) back and dividing its pairings by the covering degree four gives the downstairs matrix

\[
\begin{pmatrix}0&1\\1&a+3\end{pmatrix}.
\tag{2.11}
\]

The proved value \(a=1\) makes this matrix \(\begin{pmatrix}0&1\\1&4\end{pmatrix}\). Its evenness is now a consequence of the direct descent calculation. The same companion explicitly constructs every invariant class at order three and every parity-compatible class at order four, proving the entire degree-two image in (2.2) in both directions.

**Degrees three and four.** Direct exterior multiplication of the original \(T_j\) gives the complete invariant bases

\[
\begin{aligned}
(\bigwedge^3V)^{T_1}
 &=\langle b,c_1\rangle,&
b&=\gamma uw,&
c_1&=uw\delta-4\gamma u\delta-2\gamma w\delta,\\
(\bigwedge^3V)^{T_2}
 &=\langle b,c_2\rangle,&
c_2&=uw\delta-3\gamma u\delta-3\gamma w\delta.
\end{aligned}
\tag{2.12}
\]

For completeness, solving the invariance equations in the coordinates
\((\gamma uw,\gamma u\delta,\gamma w\delta,uw\delta)\)
leaves the first and last coefficients arbitrary; the two middle coefficients are respectively \((-4d,-2d)\) and \((-3d,-3d)\). This proves that the displayed integer bases exhaust the kernels.

Pairing \((\gamma,\eta_j)\) against \((b,c_j)\) gives

\[
D_1=\begin{pmatrix}0&1\\-3&0\end{pmatrix},
\qquad
D_2=\begin{pmatrix}0&1\\-2&0\end{pmatrix}.
\tag{2.13}
\]

The downstairs \(H^1\)-\(H^3\) pairing is unimodular, and pullback multiplies every entry by \(m_j\). If \(r_j\) is the degree-three index, its determinant therefore satisfies

\[
3\cdot3r_1=3^2,\qquad2\cdot4r_2=4^2.
\tag{2.14}
\]

Thus \(r_1=1,r_2=2\). The class \(\eta_2\) descends by (2.2), whereas
\(\eta_2 b=-2\operatorname{vol}\) is not divisible by four. If \(b\) descended too, its pairing with \(\eta_2\) upstairs would be divisible by the covering degree. Therefore \(b\) generates the nonzero cokernel at order four.

<span id="full-degree-three-lattice"></span>
The full image can now be specified. The [duality companion](integral-duality-and-the-specialization-lattices.md#duality-covering), equations (4.2)–(4.10), proves that an invariant integral class descends exactly when its pairing with every descended complementary class is divisible by the actual covering degree. For \(x=rb+sc_j\), its pairings with \(m_j\gamma,\eta_j\) are \((3s,-3r)\) at order three and \((4s,-2r)\) at order four. Thus

\[
L_1^3=\mathbb Z b\oplus\mathbb Z c_1,\qquad
L_2^3=\mathbb Z(2b)\oplus\mathbb Z c_2.
\tag{2.14a}
\]

This proves sufficiency for both displayed degree-three generators, as well as the index and the missing coset. Pullback scales their downstairs pairing matrices by \(3\) and \(4\), respectively, exactly as in (2.14).

 Finally pullback of the top orientation class is multiplication by \(m_j\), giving the degree-four column of (2.1). Degree zero is the identity since both spaces are connected. ∎

These are the actual specialization maps of \(f\). The equivariant radial trivialization in lesson 3 retracts the full finite filling onto \(S_j\). Its restriction from a punctured fibre is the precise covering \(\pi_j\), under the fixed marking. Thus no additional identification of an abstract lattice with a geometric stalk is being assumed.

## 3. Cohomology of the non-normal cusp fibre {#cusp-cohomology}

Let \(W=f^{-1}(p_0)_{\mathrm{red}}\). Lesson 5 identifies its normalization with the degree-six del Pezzo surface \(D\), obtained by blowing up the three coordinate points of \(\mathbb P^2\). Its boundary hexagon is paired along opposite curves. Write the three resulting double curves as \(\bar C_1,\bar C_2,\bar C_3\), and the two triple points as \(P,Q\).

Let \(\nu:D\to W\) be the normalization and \(i_k:\bar C_k\to W\) the closed maps. The branch labels in lesson 5 give the exact resolution

\[
0\longrightarrow\mathbb Z_W
\longrightarrow\nu_*\mathbb Z_D
\longrightarrow\bigoplus_{k=1}^3 i_{k*}\mathbb Z_{\bar C_k}
\longrightarrow\mathbb Z_P\oplus\mathbb Z_Q
\longrightarrow0.
\tag{3.1}
\]

We verify its signs and its exactness before taking cohomology. At a smooth point the first map is the identity. At a double point its nonzero stalk complex is
\(0\to\mathbb Z\to\mathbb Z^2\to\mathbb Z\to0\),
with diagonal first map and difference second map. At \(P\), the last two maps are

\[
\begin{aligned}
d_P(x_0,x_1,x_2)&=(x_0-x_1,x_0-x_2,x_1-x_2),\\
s(n_1,n_2,n_3)&=n_1-n_2+n_3.
\end{aligned}
\tag{3.2}
\]

At \(Q\) the first is
\(d_Q(x_0,x_1,x_2)=(x_2-x_1,x_0-x_1,x_0-x_2)\),
and the second is the same \(s\). Each difference map has diagonal kernel. Every vector with \(s(n)=0\) lies in its image: at \(P\) take \((x_0,x_1,x_2)=(n_2,n_3,0)\); at \(Q\) take \((x_0,x_1,x_2)=(n_2,0,n_1)\). The map \(s\) is onto. This proves exactness at both triple points and hence exactness of the sheaf resolution.

All smooth strata have torsion-free cohomology in even degrees. For \(D\), its blow-up decomposition gives
\[
H^0(D)=H^4(D)=\mathbb Z,\qquad
H^2(D)=\mathbb Z\langle H,E_1,E_2,E_3\rangle,
\tag{3.3}
\]
with intersection matrix \(\operatorname{diag}(1,-1,-1,-1)\).
These groups can be obtained by removing three disjoint small balls from \(\mathbb P^2\) and inserting the disc bundles of degree \(-1\) over the three exceptional spheres. The common boundaries are \(S^3\); Mayer–Vietoris adds one independent degree-two generator for each insertion and does not change degrees one or three. A line avoiding the balls has square \(1\), each exceptional zero-section has its normal Euler number \(-1\), and the distinct representatives are disjoint. This proves both the additive groups and the form in (3.3).

Order the boundary curves as
\[
E_1,\quad H-E_1-E_2,\quad E_2,\quad
H-E_2-E_3,\quad E_3,\quad H-E_1-E_3.
\tag{3.4}
\]
The degree-two restriction-difference map in (3.1) is
\[
d(L)=(L C_k-L C_{k+3})_{k=1}^3.
\tag{3.5}
\]
For \(L=aH-b_1E_1-b_2E_2-b_3E_3\), the six individual intersections are
\[
b_1,\ a-b_1-b_2,\ b_2,\ a-b_2-b_3,\ b_3,\ a-b_1-b_3.
\tag{3.6}
\]
Their three differences give
\[
d(L)=(s,-s,s),\qquad s=b_1+b_2+b_3-a.
\tag{3.7}
\]
Thus the image is the primitive subgroup \(\mathbb Z(1,-1,1)\), its kernel is free of rank three, and its cokernel is free of rank two.

In degree zero, the complex of global sections of the three nonzero terms of (3.1) is
\[
\mathbb Z\xrightarrow{0}\mathbb Z^3
\xrightarrow{(n_1,n_2,n_3)\mapsto(s,s)}\mathbb Z^2.
\tag{3.8}
\]
Its cohomology is \(\mathbb Z,\mathbb Z^2,\mathbb Z\). Both the image \(\mathbb Z(1,1)\) and the kernel of \(s\) are primitive. The degree-two row has the kernel and cokernel in (3.7); the degree-four row has the single group \(\mathbb Z\).

Filtering the cochain resolution (3.1) by its three columns gives no further differential. Indeed a differential of length two would run from an even row to an odd row, which is zero; every longer differential leaves the three-column range. The resulting filtration quotients are free, so their extensions split as abelian groups. We conclude

\[
H^r(W;\mathbb Z)=
\begin{cases}
\mathbb Z,&r=0,4,\\
\mathbb Z^2,&r=1,3,\\
\mathbb Z^4,&r=2,\\
0,&r>4.
\end{cases}
\tag{3.9}
\]

In particular \(\chi(W)=1-2+4-2+1=2\). The splitting of the degree-two filtration is not asserted to be canonical; the specialization map, which matters for the global calculation, is determined next.

## 4. The integral cusp specialization map {#cusp-specialization}

**Theorem 4.1.** For every \(0\leq r\leq4\), specialization is injective and identifies the cusp cohomology with the entire monodromy-invariant lattice:

\[
\operatorname{sp}^r:H^r(W;\mathbb Z)
\xrightarrow{\ \sim\ }H^r(F;\mathbb Z)^{T_0}.
\tag{4.1}
\]

The proof will exhibit a primitive degree-three image first. That geometric information resolves a differential which the ranks alone leave undetermined.

### 4.1. Local nearby cochains and their global filtration

Let \(\widetilde\Delta^*\to\Delta^*\) be the universal covering, let
\(\widetilde N_0^*=N_0\times_\Delta\widetilde\Delta^*\), and write
\(k:\widetilde N_0^*\to N_0\) and \(i:W\to N_0\) for the natural maps.
The complex of nearby cochains is

\[
\psi=i^{-1}Rk_*\mathbb Z_{\widetilde N_0^*}.
\tag{4.2}
\]

Here \(Rk_*\) means: take an acyclic sheaf resolution of the constant coefficients upstairs, apply ordinary direct image degree by degree, and retain the resulting cochain complex. Its stalk cohomology at \(w\) is the cohomology of the lifted punctured neighbourhoods of \(w\), in the limit over shrinking neighbourhoods. The unit map \(\mathbb Z_W\to\psi\) sends a locally constant function to its pullback.

Properness of \(f_0\) identifies global nearby cohomology with the marked smooth fibre:
\(\mathbb H^n(W;\psi)=H^n(F;\mathbb Z)\).
The map induced by that unit is \(\operatorname{sp}^n\). Equivalently it is restriction from shrinking complete neighbourhoods of \(W\) to a fibre on one fixed radial ray. These descriptions use the actual unit and restriction maps; they do not select an arbitrary isomorphism of two groups of equal rank.

For the local equation \(t=z_0\cdots z_k\), with \(k=0,1,2\), write each nonzero coordinate as \(r_\ell e^{i\theta_\ell}\). On a nearby fibre,
\(\sum\log r_\ell=\log|t|\) and
\(\sum\theta_\ell=\arg t\bmod2\pi\).
The allowed logarithmic radii form a nonempty convex region in an affine hyperplane; their phase space is the kernel of the sum map
\((S^1)^{k+1}\to S^1\), hence a \(k\)-torus. Contracting the radii gives the local cohomology groups of that torus, integrally. Thus

\[
\mathcal H^0\psi=\mathbb Z_W,\qquad
\mathcal H^1\psi=\mathscr V,\qquad
\mathcal H^2\psi=\mathbb Z_P\oplus\mathbb Z_Q,\qquad
\mathcal H^b\psi=0\ (b\geq3).
\tag{4.3}
\]

The sheaf \(\mathscr V\) records the vanishing circles along the double curves. At \(P\), restrictions of a triple-point one-class to the three double branches evaluate it on
\(e_0-e_1,e_0-e_2,e_1-e_2\).
At \(Q\) the corresponding ordered circles are
\(e_2-e_1,e_0-e_1,e_0-e_2\).
In both lists the first minus the second plus the third is zero. Hence there is an exact sequence

\[
0\longrightarrow\mathscr V
\longrightarrow\bigoplus_{k=1}^3i_{k*}\mathbb Z_{\bar C_k}
\xrightarrow{s}\mathbb Z_P\oplus\mathbb Z_Q
\longrightarrow0,
\tag{4.4}
\]

whose global degree-zero map is \(n\mapsto(s(n),s(n))\). Exactness follows at generic double points from the single circle, at triple points from these two independent circle coordinates, and elsewhere from zero stalks. Its cohomology gives

\[
H^a(W;\mathscr V)=
\begin{cases}
\mathbb Z^2,&a=0,\\
\mathbb Z,&a=1,\\
\mathbb Z^3,&a=2,\\
0,&a>2.
\end{cases}
\tag{4.5}
\]

The middle group is the quotient \(\mathbb Z^2/\mathbb Z(1,1)\), not a finite cyclic group.

Resolve (4.2) by an acyclic double complex and filter by its cohomology-sheaf degree. Taking vertical cohomology and then global cohomology gives

\[
E_2^{a,b}=H^a(W;\mathcal H^b\psi)
\Longrightarrow H^{a+b}(F;\mathbb Z),\qquad
d_r:E_r^{a,b}\to E_r^{a+r,b-r+1}.
\tag{4.6}
\]

All its \(E_2\)-groups are free, with the ranks

\[
\begin{array}{c|ccccc}
b=2&2&0&0&0&0\\
b=1&2&1&3&0&0\\
b=0&1&2&4&2&1\\ \hline
&a=0&a=1&a=2&a=3&a=4.
\end{array}
\tag{4.7}
\]

The finite filtration converges without a limiting ambiguity. The unit from \(\mathbb Z_W\) is the identity on the bottom row; therefore its image in \(H^r(F)\) is the bottom-row edge filtration step, with precisely the differentials entering that row accounted for.

### 4.2. What rank comparison does and does not determine

Denote the ranks of the possibly nonzero differentials by

\[
\begin{gathered}
\alpha=\operatorname{rk}d_2^{0,1},\quad
\beta=\operatorname{rk}d_2^{1,1},\quad
c=\operatorname{rk}d_2^{2,1},\\
d=\operatorname{rk}d_2^{0,2},\qquad
e=\operatorname{rk}d_3^{0,2}.
\end{gathered}
\tag{4.8}
\]

The smooth fibre is the original four-torus, with Betti numbers \(1,4,6,4,1\). In total degree one, (4.7) starts with rank \(2+2=4\), and only \(\alpha\) can decrease it. Thus \(\alpha=0\). In degree four the sole term has rank one, so \(c=0\). In total degree two the initial rank is \(4+1+2=7\); the remaining possible losses are exactly \(\beta+d+e\). Consequently

\[
\alpha=c=0,\qquad\beta+d+e=1.
\tag{4.9}
\]

These equations do not decide which of the latter three maps has rank one. We now determine that from an actual family of supported cycles.

### 4.3. Transporting a torus in the smooth stratum

The compact real torus
\[
T_f=(\Lambda_{\mathrm{tor}}\otimes\mathbb R)/\Lambda_{\mathrm{tor}},
\qquad
\Lambda_{\mathrm{tor}}=
\mathbb Z\widehat w\oplus\mathbb Z\widehat\delta
\tag{4.10}
\]
acts on the cusp charts by the original torus rotations. It commutes with the unit-dependent quotient action from lesson 5. Choose one compact orbit \(K\) in the smooth stratum \(W^\circ=(\mathbb C^*)^2\). It is a two-torus.

Near \(K\), \(f_0\) is a submersion. Average a metric over the compact group \(T_f\); its orthogonal complement to the vertical tangent bundle gives \(T_f\)-invariant horizontal lifts \(h_1,h_2\) of the two real coordinate vector fields of the base. For \(t\in\mathbb C\), flow for time one along
\[
h_t=(\operatorname{Re}t)h_1+(\operatorname{Im}t)h_2.
\tag{4.11}
\]
Compactness gives a common sufficiently small base disc and a relatively compact invariant neighbourhood \(K'\) of \(K\) on which all these flows exist. The map
\[
\Theta:K'\times\Delta_\epsilon\to N_0,\qquad
\Theta(w,t)=\Phi^{h_t}_1(w)
\tag{4.12}
\]
has \(f_0\Theta(w,t)=t\), \(\Theta(w,0)=w\), and is \(T_f\)-equivariant.
Its differential is invertible on \(t=0\). Shrinking the two neighbourhoods preserves invertibility. It is injective: equality of two images first gives equal \(t\) by applying \(f_0\), and then equal \(w\) by uniqueness of the inverse time-one flow. Thus it is an open embedding.

For \(0<r<\epsilon\), let
\[
A_r=f_0^{-1}(\Delta_r),\qquad
Z_r=\Theta(K\times\Delta_r),\qquad
K_t=\Theta(K\times\{t\}).
\tag{4.13}
\]
The set \(Z_r\) is closed in \(A_r\): if a sequence in it converges in \(A_r\), compactness of \(K\) supplies a convergent subsequence of its first coordinates, and its second coordinates converge to the image of the limit under \(f_0\), still in \(\Delta_r\). Continuity of \(\Theta\) identifies that limit with a point of \(Z_r\).

The two restrictions from supported cohomology give commuting diagrams

\[
\begin{array}{ccc}
H^3(A_r,A_r\setminus Z_r)&\longrightarrow&H^3(A_r)\\
\downarrow&&\downarrow\\
H^3(W,W\setminus K)&\longrightarrow&H^3(W)
\end{array}
\qquad
\begin{array}{ccc}
H^3(A_r,A_r\setminus Z_r)&\longrightarrow&H^3(A_r)\\
\downarrow&&\downarrow\\
H^3(F_t,F_t\setminus K_t)&\longrightarrow&H^3(F_t).
\end{array}
\tag{4.14}
\]

Excision and (4.12) identify the two left restrictions with restrictions to slices of the single product pair
\((K'\times\Delta_r,(K'\setminus K)\times\Delta_r)\).
Contracting the disc makes both restrictions isomorphisms. Passing to shrinking \(r\), proper base change identifies
\(\varinjlim_rH^3(A_r)\) with \(H^3(W)\), and the right restriction to \(F_t\), identified along the fixed radial ray, is specialization. Therefore (4.14) proves that

\[
H^3(W,W\setminus K)\longrightarrow H^3(W)
\xrightarrow{\operatorname{sp}^3}H^3(F)
\tag{4.15}
\]

is the Gysin image of the transported supported class at \(K_t\).

The subgroup \(\Lambda_{\mathrm{tor}}\) is a direct summand of the original lattice. Thus, as an oriented real torus,
\(F=T_f\times T_B\), where \(T_B\) is the complementary two-torus with lattice
\(\mathbb Z\widehat\gamma\oplus\mathbb Z\widehat u\).
The \(T_f\)-equivariant image \(K_t\) is a translate of its \(T_f\) factor.
Both \(K\subset W^\circ\) and \(K_t\subset F_t\) have trivial oriented rank-two normal bundle. The relative cohomology of a normal disc and its punctured disc is \(\mathbb Z\) in degree two. Applying the product cochain calculation gives the Thom isomorphisms and the absolute map

\[
H^3(F_t,F_t\setminus K_t)=H^1(T_f),\qquad
a\longmapsto a\otimes[T_B]^\vee
\ \in H^1(T_f)\otimes H^2(T_B)\subset H^3(F_t).
\tag{4.16}
\]

This image is a primitive rank-two direct summand. In the original exterior coordinates it is
\(\mathbb Z\langle\gamma uw,\gamma u\delta\rangle\), with normal orientation chosen so \([T_B]^\vee=\gamma u\); commuting a degree-one factor past the two normal factors introduces the sign \(+1\).
The domain of (4.15) is also free of rank two, by the same local product calculation on \(W^\circ\simeq T_f\times\mathbb R^2\). Hence specialization has rank at least two in degree three. Since (3.9) gives rank exactly two for \(H^3(W)\), it is injective there, and its image is exactly this primitive summand. Indeed a larger rank-two subgroup containing a primitive summand in the same rational span must coincide with it.

### 4.4. All integral images, including the exceptional filtration step

The maps of ranks \(\beta,e\) enter \(H^3(W)=E_2^{3,0}\). They must be zero because the specialization just proved is injective. Thus (4.9) gives
\[
\beta=e=0,\qquad d=1.
\tag{4.17}
\]
In degrees one and two no differential enters the bottom row. It follows that
\[
H^r(W)\xrightarrow{\sim}E_\infty^{r,0}
=F^rH^r(F)\subset H^r(F),\qquad r=1,2.
\tag{4.18}
\]
The quotient by this subgroup is free. In degree one its only other filtration quotient is the free group \(E_\infty^{0,1}\). In degree two the other quotients are \(E_\infty^{1,1}=\mathbb Z\) and
\(E_\infty^{0,2}=\ker d_2^{0,2}\), a subgroup of the free group \(\mathbb Z^2\). Successive extensions of free abelian groups split, so these statements prove primitivity of both images, with no appeal to rational coefficients.

In degree four the only total-degree-four filtration step is \(E_\infty^{4,0}\). The sole possibly entering map has rank \(c=0\) between free groups, so is zero. Thus specialization in degree four is an isomorphism. Degree zero is the identity on connected components.

Every specialization class is invariant under monodromy: in the neighbourhood description it comes from one class defined over the complete disc, and continuing its restriction around a loop returns the same class. Lesson 6 computes the invariant ranks
\((1,2,4,2,1)\), exactly those in (3.9). Each invariant group is the kernel of an integer endomorphism of the free exterior lattice, and is therefore primitive. The images just proved are primitive, have the same ranks, and lie in those invariant groups. Two primitive subgroups with the same rational span are both the intersection of that rational span with the ambient integer lattice. They consequently coincide. This proves Theorem 4.1 in every degree. ∎

## 5. The cohomology sheaves on the whole base {#base-cohomology}

Set \(R^r=R^rf_*\mathbb Z_X\) and \(\mathcal L^r=j^{-1}R^r\). The latter local system has fibre \(\bigwedge^rV\). Proper base change identifies each special stalk with the cohomology of the corresponding fibre. The stalk map to \(j_*\mathcal L^r\) is the actual specialization. Theorems 2.1 and 4.1 consequently give exact sequences

\[
0\longrightarrow R^r\longrightarrow j_*\mathcal L^r
\longrightarrow Q^r\longrightarrow0
\tag{5.1}
\]

with

\[
\begin{aligned}
Q^0&=0,\\
Q^1&=(\mathbb Z/3)_{p_1}\oplus(\mathbb Z/4)_{p_2},\\
Q^2&=Q^3=(\mathbb Z/2)_{p_2},\\
Q^4&=(\mathbb Z/3)_{p_1}\oplus(\mathbb Z/4)_{p_2}.
\end{aligned}
\tag{5.2}
\]

A group with subscript \(p\) denotes the sheaf with that stalk at \(p\) and zero other stalks. Every restriction of its sections is surjective, so this sheaf is flabby and has no positive cohomology. The same holds for each finite direct sum in (5.2).

**Proposition 5.1.** The required base cohomology groups are

\[
\begin{gathered}
H^0(B,R^1)=\mathbb Z(12\gamma),\quad
H^0(B,R^2)=\mathbb Z(2q),\quad
H^0(B,R^3)=\mathbb Z(2\gamma uw),\\
H^1(B,R^1)=H^1(B,R^2)=0,
\end{gathered}
\tag{5.3}
\]

and

\[
\begin{aligned}
H^2(B,R^0)&=\mathbb Z\omega,&
H^2(B,R^1)&=\mathbb Z\omega[\delta],\\
H^2(B,R^2)&=\mathbb Z\omega[\gamma\delta],&
H^2(B,R^4)&=\mathbb Z\omega[\operatorname{vol}].
\end{aligned}
\tag{5.4}
\]

Here \(\omega\) is the base generator with the orientation fixed in Section 6. Their coefficient product maps are induced by the original exterior products; in particular \([q]=12[\gamma\delta]\).

**Degree zero.** Restriction embeds a global section into the global invariant lattice on \(B^\circ\). Lesson 6 gives \(\mathbb Z\gamma,\mathbb Zq,\mathbb Z\gamma uw\) in degrees one, two and three. There is no additional cusp condition by Theorem 4.1. The finite conditions are divisibility by three and four in degree one, and divisibility by two at \(p_2\) in each of degrees two and three. These are exactly the first line of (5.3).

They also show that the invariant sections surject onto \(H^0(B,Q^r)\) for \(r=1,2,3\). In degree one the map is
\[
\mathbb Z\longrightarrow\mathbb Z/3\oplus\mathbb Z/4,\qquad
n\longmapsto(n\bmod3,n\bmod4).
\tag{5.5}
\]
The integer \(4a-3b\) maps to the prescribed pair of residues \(a,b\). The other two maps are reduction modulo two.

**Degree two.** For any of the free local systems \(\mathcal L\) with stalk \(M\), the quotient \(j_*\mathcal L/j_!\mathcal L\) is supported at the punctures. Hence
\[
H^2(B,j_*\mathcal L)
=H_c^2(B^\circ;\mathcal L)
=M_{\langle T_1,T_2\rangle}.
\tag{5.6}
\]
The last equality can be computed on an oriented triangulation of a compact pair of pants, relative to its boundary. Give each face its copy of \(M\), using chosen transport arcs. In the top cochain quotient, an interior-edge coboundary identifies the coefficients of adjacent faces by parallel transport. A spanning tree of the dual graph identifies them all with one marked copy of \(M\). The remaining dual edges impose exactly \(m=T_gm\) for their loops \(g\). This is the full coinvariant quotient. A different spanning tree changes transports by monodromy, already identified in that quotient. Compact-support cohomology of the open surface is the relative cohomology of this pair of pants and its boundary, giving (5.6).

This construction is natural for coefficient products: multiplication by an invariant flat section commutes with each parallel-transport identification. The quotient by \(Q^r\) in (5.1) does not change degree-two cohomology. The integral coinvariants proved in lesson 6 now give all of (5.4). For degree four the action is trivial since both original matrices have determinant one. Reversing the base orientation changes the sign of the common top generator and no coefficient relation.

**Degree one.** A local-system one-cocycle on \(B^\circ\), which retracts to the two meridians, is determined by
\[
x=c(\rho_1),\quad y=c(\rho_2),\qquad
c(gh)=c(g)+T_g c(h).
\tag{5.7}
\]
At a puncture its local circle class lies in \(M/(T_i-I)M\). The exact restriction sequence for the punctured base and its three discs identifies \(H^1(B,j_*\mathcal L)\) with the kernel of all three local class maps. In a local cochain model this says that each annular cocycle can be made zero by subtracting a local coboundary.

The second local condition is \(y=(T_2-I)m\). Subtract the global coboundary of \(m\), giving \(y=0\). The remaining changes that preserve this value have \(m\in M^{T_2}\). Since \(a_0=(\rho_1\rho_2)^{-1}\), the cocycle identity now gives \(c(a_0)=-T_0x\). The image \((T_0-I)M\) is \(T_0\)-stable. The other two local conditions therefore produce the exact quotient
\[
H^1(B,j_*\mathcal L)=
\frac{(T_1-I)M\cap(T_0-I)M}
{(T_1-I)M^{T_2}}.
\tag{5.8}
\]

For \(M=V\), direct multiplication gives the full spans
\[
(T_1-I)V=\langle2\gamma+u+w,\ 2\gamma-u\rangle,\qquad
(T_0-I)V=\langle\gamma,u\rangle.
\tag{5.9}
\]
The \(w\)-coefficient forces an element of their intersection to be a multiple of \(2\gamma-u\). Conversely every such multiple belongs to both. The denominator is the same subgroup: \(V^{T_2}=\langle\gamma,\eta_2\rangle\),
\((T_1-I)\gamma=0\), and \((T_1-I)\eta_2=-2\gamma+u\).
Thus (5.8) vanishes.

For \(M=\bigwedge^2V\), the full integer image spans are
\[
\begin{aligned}
(\bigwedge^2T_1-I)M
=\langle&\gamma u,\gamma w,2u\delta+w\delta,\\
&uw+u\delta-w\delta-6\gamma\delta\rangle,\\
(\bigwedge^2T_0-I)M
=\langle&\gamma u,\gamma w+u\delta\rangle.
\end{aligned}
\tag{5.10}
\]
They can be checked column by column against the exterior matrices in lesson 6. In an element of their intersection, the \(uw\)-coefficient kills the fourth generator of the first span, and the \(w\delta\)-coefficient kills its third. Comparing \(u\delta\) then kills the second generator of the second span. The intersection is exactly \(\mathbb Z\gamma u\). The full \(T_2\)-invariant basis is \((\gamma\eta_2,q)\), and its two images under \(\bigwedge^2T_1-I\) are \(\gamma u,0\). Thus the denominator is again the entire numerator.

Finally the long exact sequence of (5.1), together with the proved surjectivity onto \(H^0(Q^r)\), injects \(H^1(B,R^r)\) into the just-vanishing \(H^1(B,j_*\mathcal L^r)\) for \(r=1,2\). This proves all assertions. ∎

## 6. Three transgressions with their full signs {#transgressions}

The Leray filtration of the actual map is
\[
E_2^{p,r}=H^p(B,R^r)\Longrightarrow H^{p+r}(X;\mathbb Z).
\tag{6.1}
\]
Its differential \(d_2\) has bidegree \((2,-1)\). There are no columns beyond two, since the base has cohomological dimension two. A filtered multiplicative cochain resolution gives the product rule
\(d(\alpha\beta)=d\alpha\cdot\beta+(-1)^{|\alpha|}\alpha\cdot d\beta\),
where \(|\alpha|\) is the total degree. All products below use that sign.

**Theorem 6.1.** With the base generator fixed by the clockwise annular sum below,
\[
d_2(12\gamma)=\omega,\qquad
d_2(2q)=\omega[\delta],\qquad
d_2(2\gamma uw)=\omega[\gamma\delta].
\tag{6.2}
\]

### 6.1. The primitive first differential

Choose small disjoint discs \(D_i\) and a slightly enlarged pair of pants \(U\). The section \(\theta=12\gamma\) has cohomological lifts on all four inverse images. We can construct them directly from the already proved groups. On \(\Lambda\rtimes F(\rho_1,\rho_2)\), send \(t_\lambda\) to \(12\gamma(\lambda)\) and assign arbitrary integers \(\alpha_1,\alpha_2\) to the two meridians. Invariance of \(\gamma\) respects every conjugation relation. At the finite fillings, their exact power relations force
\[
\Theta_1(\rho_1)=\frac{12\gamma(v_1)}3=4,\qquad
\Theta_2(\rho_2)=\frac{12\gamma(v_2)}4=-3.
\tag{6.3}
\]
On the cusp, \(12\gamma\) factors through \(\Lambda/\Lambda_{\mathrm{tor}}\), and the actual meridian has value zero. It bounds the explicit coordinate disc from lesson 6. The equality \(H^1(Y;\mathbb Z)=\operatorname{Hom}(\pi_1Y,\mathbb Z)\) turns these homomorphisms into all the asserted lifts, with their original fibre restrictions.

The differences on the three annular overlaps have clockwise meridian values
\[
4-\alpha_1,\qquad -3-\alpha_2,\qquad \alpha_1+\alpha_2.
\tag{6.4}
\]
The last uses the exact based relation \(\rho_1\rho_2a_0=1\). Their sum is \(1\).

On the base, the overlap cohomology is \(\mathbb Z^3\). The image of \(H^1(U)\) is exactly
\(\{(a,b,-a-b):a,b\in\mathbb Z\}\), by the boundary-loop relation and the two freely assignable meridian values. Its quotient is \(\mathbb Z\) by the sum map. The Mayer–Vietoris connecting homomorphism identifies this quotient with \(H^2(B;\mathbb Z)\). We define \(\omega\) as the image of a triple whose sum is \(1\). This specifies the orientation rather than deleting a sign from (6.4).

To identify the resulting class with \(d_2\), retain the first two cohomology degrees of the pushed-forward cochain complex. Its truncation triangle is
\[
R^0\longrightarrow\tau_{\leq1}Rf_*\mathbb Z_X
\longrightarrow R^1[-1]\longrightarrow R^0[1].
\tag{6.5}
\]
In a double resolution, lift a global first-cohomology-sheaf section to local degree-one cochains. On overlaps their differences lie in the degree-one cohomology of \(R^0\); the connecting base cochain of degree two is the obstruction to gluing. This is exactly the representative definition of \(d_2^{0,1}\). For the chosen cover those differences are (6.4), and their connecting class is the sum quotient just computed. Consequently \(d_2(12\gamma)=\omega\), with coefficient \(+1\).

### 6.2. The two remaining coefficients

Put
\[
\theta=12\gamma,\qquad a=2q,\qquad b=2\gamma uw.
\tag{6.6}
\]
By Proposition 5.1, write \(d_2a=r\omega[\delta]\) and
\(d_2b=s\omega[\gamma\delta]\), for integers \(r,s\).
The original exterior products give
\[
\theta a=12b,\qquad ab=0,\qquad [q]=12[\gamma\delta].
\tag{6.7}
\]
Since \(|\theta|=1\),
\[
12d_2b=d_2(\theta a)=d_2\theta\cdot a-\theta\cdot d_2a.
\tag{6.8}
\]
Its right side is
\(24\omega[\gamma\delta]-12r\omega[\gamma\delta]\), so \(s=2-r\).
Since \(|a|=2\), the second identity instead gives
\[
0=d_2(ab)=d_2a\cdot b+a\cdot d_2b.
\tag{6.9}
\]
Here every exterior sign is explicit:
\[
\delta\wedge2\gamma uw=-2\operatorname{vol},\qquad
2q\wedge\gamma\delta=2\operatorname{vol}.
\tag{6.10}
\]
The target is the free group \(\mathbb Z\omega[\operatorname{vol}]\), so
\(-2r+2s=0\), giving \(r=s\). Together these equations force \(r=s=1\), which completes (6.2). ∎

## 7. The entire integral homology {#integral-homology}

**Theorem 7.1.** The original compact threefold has
\[
H^k(X;\mathbb Z)=H_k(X;\mathbb Z)=
\begin{cases}
\mathbb Z,&k=0,6,\\
0,&1\leq k\leq5.
\end{cases}
\tag{7.1}
\]

**Proof.** In total degree one the pieces are \(E_2^{1,0}=H^1(B;\mathbb Z)=0\) and \(E_2^{0,1}=\mathbb Z(12\gamma)\). The latter has injective differential by Theorem 6.1, so \(H^1(X)=0\).

In total degree two, the full list is
\[
E_2^{2,0}=\mathbb Z\omega,\qquad
E_2^{1,1}=0,\qquad
E_2^{0,2}=\mathbb Z(2q).
\tag{7.2}
\]
The first is the entire image of \(d_2(12\gamma)\), and the last has injective differential with value \(\omega[\delta]\). All stable pieces vanish, so \(H^2(X)=0\).

In total degree three, \(E_2^{2,1}=\mathbb Z\omega[\delta]\) is the entire image of \(d_2(2q)\), \(E_2^{1,2}=0\), and
\(E_2^{0,3}=\mathbb Z(2\gamma uw)\) maps injectively to
\(\mathbb Z\omega[\gamma\delta]\). Hence \(H^3(X)=0\).
No later differential can meet these terms, since its base-degree change leaves the three-column range. A finite filtered group with all successive quotients zero is zero; no extension ambiguity remains.

Lesson 6 proves \(\pi_1(X)=1\), so \(H_1(X)=0\). Compact smoothness gives finite generation. The degree-two universal-coefficient sequence gives
\(\operatorname{Hom}(H_2(X),\mathbb Z)=0\); the next gives an injection
\(\operatorname{Ext}(H_2(X),\mathbb Z)\hookrightarrow H^3(X)=0\).
For a finite cyclic group, applying \(\operatorname{Hom}(-,\mathbb Z)\) to
\(\mathbb Z\xrightarrow{n}\mathbb Z\) yields
\(\operatorname{Ext}(\mathbb Z/n,\mathbb Z)=\mathbb Z/n\).
Thus the first vanishing removes all free summands of \(H_2\), and the second removes all finite summands. Consequently \(H_2(X)=0\).

The complex structure orients the real six-manifold. Integral Poincaré duality gives
\[
H_3(X)=H^3(X)=0,\qquad
H_4(X)=H^2(X)=0,\qquad
H_5(X)=H^1(X)=0.
\tag{7.3}
\]
Connectedness and orientation give \(H_0(X)=H_6(X)=\mathbb Z\). Applying universal coefficients to the fully determined homology groups gives the remaining cohomology groups in (7.1). ∎

This proof eliminates torsion in degree two using both cohomology degrees two and three. As a geometric check, \(\chi(X)=2\) agrees with \(\chi(W)=2\): all smooth torus fibres and both finite reduced fibres have Euler characteristic zero.

## 8. Comparing the complete cohomology markings {#cohomology-dictionary}

The integral matrix \(P\) of lesson 6 maps Engel's homology coordinates to the original programme coordinates. On one-cohomology it therefore acts by \(P^{\mathsf t}\), and on degree \(r\) by \(\bigwedge^rP^{\mathsf t}\). Retain the source notation

\[
\begin{gathered}
\psi=e_4^*,\qquad k=e_1^*-e_2^*,\qquad
\nu=e_1^*e_2^*e_3^*e_4^*,\\
\xi=3e_1^*e_2^*+e_1^*e_3^*
-2e_2^*e_3^*-2e_3^*e_4^*,\qquad
\theta_E=\xi\psi .
\end{gathered}
\tag{8.1}
\]

Every coefficient is preserved. Matrix multiplication and exterior multiplication give

\[
\begin{aligned}
P^{\mathsf t}\gamma&=\psi,&
P^{\mathsf t}\delta&=-k,\\
(\bigwedge^2P^{\mathsf t})q&=\xi,&
(\bigwedge^2P^{\mathsf t})(\gamma\delta)&=k\psi,\\
(\bigwedge^3P^{\mathsf t})(\gamma uw)&=\theta_E,&
(\bigwedge^4P^{\mathsf t})\operatorname{vol}&=-\nu .
\end{aligned}
\tag{8.2}
\]

For example the coordinates of \(q\) in the original two-form basis are
\((0,0,6,1,0,0)\); their image is exactly
\((3,1,0,-2,0,-2)\).
The minus sign in the last equation is \(\det P=-1\). The sign in the second equation and the wedge-order reversal in the fourth are both needed.

Lesson 6's full translation dictionary has source sphere parameter \(p_E=-1\). Its meridians are oppositely oriented to ours. Consequently its base orientation class is related by \(\omega=-\omega_E\). Transporting the complete formulas (6.2) now gives

\[
\begin{aligned}
d_2(12\psi)&=-\omega_E=p_E\omega_E,\\
d_2(2\xi)&=\omega_E[k]=-p_E\omega_E[k],\\
d_2(2\theta_E)&=-\omega_E[k\psi]
=p_E\omega_E[k\psi].
\end{aligned}
\tag{8.3}
\]

These are the source's three signed transgressions. In particular the apparent change of the middle sign is exactly the product of the base-orientation sign and the map \(P^{\mathsf t}\delta=-k\). No original exterior form or base generator has been replaced by a rescaled one.

## 9. An actual homotopy equivalence with the sphere {#homotopy-sphere}

We now apply the topological inputs to \(X\), retaining the distinction between a homotopy equivalence and the later smooth identification. The first Hurewicz theorem used here says: if a path-connected space \(Y\) has \(\pi_i(Y)=0\) for \(1\leq i<n\), \(n\geq2\), then its map
\[
h_n:\pi_n(Y)\longrightarrow H_n(Y;\mathbb Z),\qquad
[a]\longmapsto a_*[S^n]
\tag{9.1}
\]
is an isomorphism and its lower reduced integral homology vanishes. The complete coherent-simplex proof, including both inverse maps, is in the included [CW and Hurewicz companion](cw-models-and-the-first-hurewicz-map.md#hurewicz-theorem), Theorem 4.1. Its source comparison and exact checked version are recorded there. Its hypotheses concern the actual homotopy groups, not a rational substitute.

**Theorem 9.1.** There is a degree-one map \(g:S^6\to X\) which is a homotopy equivalence.

**Proof.** Lesson 6 starts the induction with \(\pi_1(X)=0\). If \(2\leq n\leq5\) and all earlier groups vanish, (9.1) identifies \(\pi_n(X)\) with \(H_n(X;\mathbb Z)=0\), by Theorem 7.1. Induction gives \(\pi_i(X)=0\) for \(1\leq i\leq5\). Apply Hurewicz once more in degree six and choose
\([g]\in\pi_6(X)\) which maps to the positive orientation generator \([X]\). Thus
\[
g_*[S^6]=[X].
\tag{9.2}
\]
The map induces homology isomorphisms in degrees zero and six and in all other degrees, where both groups are zero.

Here is a direct argument upgrading this homology equivalence. Replace \(g\) by its path fibration
\[
E_g=\{(s,\lambda):s\in S^6,\ \lambda(0)=g(s)\},
\qquad
p(s,\lambda)=\lambda(1).
\tag{9.3}
\]
Contracting a path towards its initial point retracts \(E_g\) onto \(S^6\); under this retraction \(p\) represents \(g\). The included [path-fibre companion](path-fibres-and-integral-homotopy-equivalences.md#path-lifting), Section 1, proves the lifting formula and exact homotopy sequence.

For the cellular filtration we use the actual CW comparison from the [CW companion](cw-models-and-the-first-hurewicz-map.md#cw-manifolds):
\(\alpha:T_X\to X\), \(\beta:X\to T_X\), with \(\alpha\beta=1_X\) and \(\beta\alpha\simeq1_{T_X}\). Keep (9.3), and define the comparison

\[
\begin{aligned}
\bar g&=\beta g:S^6\to T_X,&
\bar E&=E_{\bar g},&
\bar p(s,\lambda)&=\lambda(1),\\
J:\bar E&\longrightarrow E_g,&
J(s,\lambda)&=(s,\alpha\circ\lambda),&
pJ&=\alpha\bar p.
\end{aligned}
\tag{9.3a}
\]

The path starts at \(\bar g(s)\), so its image starts at \(\alpha\beta g(s)=g(s)\), exactly as required. Both total spaces retract onto the same \(S^6\), and \(J\) commutes with these retractions. The base \(T_X\) is now an actual simply connected CW complex; \(\pi_2(T_X)=0\), and \(\bar p\) is an integral homology isomorphism in every degree because \(\bar g=\beta g\) is. Let \(K=\bar p^{-1}(t_*)\) over a vertex \(t_*\). The exact sequence and the explicit path-component argument of the path-fibre companion, Theorem 5.1, show that \(K\) is path connected and simply connected.

Suppose a positive homotopy group of \(K\) were nonzero and let \(n\geq2\) be its first degree. Hurewicz would give
\(H_i(K)=0\) for \(0<i<n\) and \(H_n(K)\ne0\).
In the integral Serre homology spectral sequence of the fibration over \(T_X\) in (9.3a), the base is simply connected, so its coefficient systems are constant. In total degree \(n\), the only possibly nonzero terms are
\[
E_2^{0,n}=H_n(K),\qquad E_2^{n,0}=H_n(T_X).
\tag{9.4}
\]
The only differential which could enter the first is
\(d_{n+1}:E_{n+1}^{n+1,0}\to E_{n+1}^{0,n}\);
earlier sources involve the vanishing groups \(H_i(K)\), \(0<i<n\).
Surjectivity of
\(\bar p_*:H_{n+1}(\bar E)\to H_{n+1}(T_X)\), already proved from (9.2) and (9.3a), makes this transgression zero. Indeed the edge image lies in its kernel, and the edge image is the whole bottom-row group. No differential leaves column zero.

Thus \(H_n(K)\) survives as the first filtration subgroup of \(H_n(\bar E)\). The homology edge map \(\bar p_*:H_n(\bar E)\to H_n(T_X)\) kills that subgroup, since the map to the base factors through the bottom row. But \(\bar p_*\) is injective, also by (9.2) and (9.3a). Hence \(H_n(K)=0\), a contradiction. All homotopy groups of \(K\) therefore vanish. The homotopy sequence of (9.3a) makes \(\bar g\) an isomorphism on every homotopy group; composition with \(\alpha\) gives the same statement for the original \(g\). The full filtered-chain proof and both actual homology edges used here are in the included [path-fibre companion](path-fibres-and-integral-homotopy-equivalences.md#serre-homology), Sections 2–3.

The same companion's [CW compression argument](path-fibres-and-integral-homotopy-equivalences.md#cw-inverses), Section 4, now gives an actual inverse \(\bar h:T_X\to S^6\) to \(\bar g\). It proves surjectivity and injectivity on homotopy classes from every CW domain by relative disk compression, then uses the domains \(T_X\) and \(S^6\) to construct both inverse homotopies. Thus the original inverse is

\[
h_X=\bar h\beta:X\to S^6,\qquad
h_Xg\simeq1_{S^6},\qquad gh_X\simeq1_X.
\tag{9.5}
\]

The second identity uses \(g=\alpha\bar g\), then \(\bar g\bar h\simeq1_{T_X}\), then the exact identity \(\alpha\beta=1_X\). The first uses \(\bar h\bar g\simeq1_{S^6}\). This completes both required comparisons. ∎

This construction specifies the morphism to be recognized: \(g\) represents the orientation generator under the actual degree-six Hurewicz isomorphism. Its existence follows after the full integral and fundamental-group calculations, rather than being presumed from a matching Euler characteristic.



## 10. The actual smooth recognition {#smooth-recognition}

The homotopy equivalence of Section 9 identifies a smooth homotopy six-sphere. The smooth statement uses two classical results: the simply connected smooth \(h\)-cobordism theorem and the vanishing of the group \(\Theta_6\) of oriented smooth homotopy six-spheres. The [sphere-twist and smooth-recognition proof](sphere-twists-and-the-original-smooth-six-sphere-comparison.md#twist-original-smooth-map) now constructs the new interior gluing with its full frame defect, cancels every actual handle and gives the orientation-preserving diffeomorphism to the original six-sphere, homotopic to its original degree-one map. We first construct the precise cobordism to which the smooth theorem applies.

An \(h\)-cobordism from a closed manifold \(M_0\) to \(M_1\) is a compact smooth manifold \(C\) with \(\partial C=M_0\amalg M_1\) for which both inclusions \(M_i\hookrightarrow C\) are homotopy equivalences. It comes with its actual boundary inclusions.

**Proposition 10.1.** Choose two disjoint orientation-preserving coordinate closed discs \(D_0,D_1\subset X\). Then
\[
C=X\setminus(\operatorname{int}D_0\cup\operatorname{int}D_1)
\tag{10.1}
\]
is a simply connected smooth six-dimensional \(h\)-cobordism between its two boundary five-spheres.

**Proof.** Coordinate discs have collars, so (10.1) is a compact smooth manifold with the indicated boundary. It is connected: any path between points outside the discs can be perturbed to meet the boundary spheres transversely in finitely many points, and each portion passing through a disc can be replaced by a path in its connected boundary sphere. Van Kampen, applied when adding the two discs back along collars of \(S^5\), identifies \(\pi_1(C)\) with \(\pi_1(X)\). The discs and the collar spheres are simply connected. Thus \(\pi_1(C)=0\).

Excision gives
\[
H_k(X,C;\mathbb Z)=
H_k(D_0,\partial D_0;\mathbb Z)\oplus
H_k(D_1,\partial D_1;\mathbb Z)
=
\begin{cases}\mathbb Z^2,&k=6,\\0,&k\ne6.\end{cases}
\tag{10.2}
\]
Here each summand is computed by the relative cell of the disc; its positive generator is its local orientation class. The fundamental class of \(X\) maps to \((1,1)\), since both chosen coordinate discs preserve the orientation. The long exact sequence of the pair and Theorem 7.1 consequently give
\[
H_6(C)=0,\qquad
H_5(C)=\mathbb Z^2/\mathbb Z(1,1)\simeq\mathbb Z,
\qquad H_k(C)=0\quad(1\leq k\leq4).
\tag{10.3}
\]
The relative boundary homomorphism sends the first and second standard generators in (10.2) to their actual boundary sphere classes in \(C\). In the quotient in (10.3) these are opposite generators. Thus each inclusion \(\partial D_i\hookrightarrow C\) induces an isomorphism on \(H_5\), and also on \(H_0\); all other homology groups on both sides vanish.

Both spaces are simply connected. The included [CW companion](cw-models-and-the-first-hurewicz-map.md#cw-manifolds) proves their CW homotopy type: its formula (2.6) treats the actual punctured cobordism, keeping the original disk radii. The included [path-fibre companion](path-fibres-and-integral-homotopy-equivalences.md#integral-comparison), Theorem 5.1, turns these homology isomorphisms into homotopy equivalences. Surjectivity of the degree-\(n+1\) edge first kills the only possible incoming transgression; injectivity in degree \(n\) then excludes a first nonzero fibre group. Its equation (5.12) constructs both original inverse maps through the specified CW comparison of \(C\), retaining the opposite signs of the two boundary generators. Hence both actual boundary inclusions are homotopy equivalences, proving the assertion. ∎

Section 6 of the [actual Morse realization and middle-cancellation companion](realizing-framed-handles-and-middle-cancellation.md#middle-six-seven-reduction) proves the required smooth product theorem in dimensions six and seven. Its exact map (6.8) identifies this \(C\) with \(\partial D_0\times[0,a_+-a_-]\), relative to its incoming boundary. Here \(a_-,a_+\) are the retained endpoint values of the resulting function. The original coordinate parametrization \(j_0:S^5\to\partial D_0\) and the map \((z,t)\mapsto(j_0(z),(a_+-a_-)t)\) compare this product with \(S^5\times[0,1]\); the inverse divides the second coordinate by the same positive factor and applies \(j_0^{-1}\). The full derivative retains \(Dj_0\) and the factor \(a_+-a_-\). Adding the two original coordinate discs then describes \(X\) as
\[
D^6\cup_\phi D^6
\tag{10.4}
\]
for a particular smooth gluing diffeomorphism \(\phi:S^5\to S^5\). The smooth map on the remaining boundary is part of the data in (10.4); a product description of the complement does not itself extend \(\phi\) across a disc.

The classical group \(\Theta_6\) uses oriented homotopy spheres modulo oriented \(h\)-cobordism, with connected sum as its operation. The [sphere-twist and smooth-recognition proof](sphere-twists-and-the-original-smooth-six-sphere-comparison.md#twist-original-smooth-map) gives the complete receiving proof that every oriented smooth homotopy six-sphere is orientation-preservingly diffeomorphic to the standard sphere. Its proof constructs a suitable seven-dimensional product with the specified original boundary, and thus proves the group equality as well. The full application to the original map of Section 9 is given below.

The [relative Morse and original-handle companion](relative-morse-functions-and-original-handles.md#relative-morse-attachment) now constructs the actual starting decomposition of this original cobordism. It fixes the original incoming and outgoing collars, retains every Hessian coefficient in its exact coordinate map, and inserts each framed handle with both original parameter radii. Its Sections 4.2–4.4 specify the transverse seam, outward corner smoothing and complete variable-time collar map, including both extreme indices and the final outgoing boundary identification. This proves the finite handle decomposition used below. The [original handle-index arrangement](rearranging-the-original-framed-handles.md#arrangement-interchange) is now proved as well. It compares the exact rounded boundary with the original surgery collars, moves complete attaching tubes through the original complement maps, interchanges the actual framed handles and retains the final boundary identification. The [ordered Morse function and descending trajectories](morse-trajectories-and-critical-value-lowering.md#trajectory-ordered-morse) supply the compatible function and the full supported critical-value change, including all original Hessian coefficients and the actual boundary maps. The [zero- and top-index removal](removing-the-original-zero-and-top-handles.md#zero-supported-cancellation) is now proved as well, retaining both original boundary collars and the entire presentation map. The [supported creation of a cancelling handle pair](creating-an-original-cancelling-handle-pair.md#pair-original-band) supplies the exact local insertion needed for stabilization, with a single transverse connecting trajectory and the full original-band comparison. Its lower attaching sphere bounds the explicitly framed disk proved in Section 6 of that companion. The [framed slides and index-one removal](framed-handle-slides-and-index-one-removal.md#slide-index-one-cancellation) now remove index one and its reversed counterpart by the actual supported belt crossing, full loop isotopy, exact common-exterior flow comparison and verified one-intersection cancellation. Section 8.1 of that companion proves the stronger surjectivity hypothesis for the boundary fundamental-group map. Only the original handles of indices two through dimension minus two remain. The [integral handle-chain companion](integral-handle-chains-and-signed-incidences.md#handle-six-seven) now proves the original filtration-to-homology map, every incidence sign, the full integer basis comparisons and the exact contractions in dimensions six and seven. The [higher-index framed-slide companion](higher-index-framed-slides-and-chain-maps.md#higher-slide-matrices) now realizes every elementary integral change with its full framed cobordism map and proves both neighbouring differentials using the singular-prism correction. The [receiving-dimension Whitney companion](whitney-moves-in-the-receiving-dimensions.md#receiving-whitney-flow) proves the full disk, adapted frame and supported move for the three required sheet-dimension pairs, with all original metric, orientation and framing maps retained. The [actual Morse realization and middle-cancellation companion](realizing-framed-handles-and-middle-cancellation.md#middle-six-seven-reduction) constructs the compatible function, proves the exact intersection-to-trajectory comparison and every escape and support hypothesis, and completes the simply connected smooth cobordism reductions in dimensions six and seven.

The [Morse cancellation companion](morse-cancellation-with-controlled-support.md) now supplies the geometric cancellation step, including the supported critical-value change and the exact product map relative to the lower boundary. Its Section 5 retains the disk radius and all derivatives of the cutoffs, and its second exercise computes the extra critical points produced by an invalid cutoff. This is the receiving cancellation argument. Sections 2–6 of the [actual Morse realization and middle-cancellation companion](realizing-framed-handles-and-middle-cancellation.md#middle-six-seven-reduction) now supply the actual function, unique trajectories, compact supports and finite cancellation order needed to apply it to every middle pair.

The [belt-complement and Whitney-disk companion](belt-sphere-complements-and-the-whitney-disk.md#whitney-boundary) now proves the complete framed disk construction for a specified simply connected index-two handle stage. Its Sections 1–3 retain the original complement diffeomorphism, both handle radii and both tangent maps. Section 5 constructs embedded fillings while preserving the entire original collar and avoiding the boundary and corner strata of the previously built collar. Sections 6–7 retain every nonorthogonal frame coefficient, the original metric and both intersection signs. They construct the actual two-corner disk and its full adapted frame. The [supported Whitney-move companion](whitney-move-with-controlled-support.md#move-receiving-attachments) now proves its receiving ambient operation. It constructs the exact corner-domain and sheet coordinates, preserves all original frame factors, removes the two intersections by a full cutoff flow, and gives the resulting diffeomorphism of attached cobordisms relative to the incoming boundary. The [receiving-dimension Whitney companion](whitney-moves-in-the-receiving-dimensions.md#receiving-whitney-flow) proves the full disk, adapted frame and supported move for the three required sheet-dimension pairs, with all original metric, orientation and framing maps retained. The [actual Morse realization and middle-cancellation companion](realizing-framed-handles-and-middle-cancellation.md#middle-six-seven-reduction) constructs the compatible function, proves the exact intersection-to-trajectory comparison and every escape and support hypothesis, and completes the simply connected smooth cobordism reductions in dimensions six and seven. The resulting product map retains the original incoming inclusion and its actual outgoing flow map.

The [six-dimensional bundle companion](spin-six-and-the-framing-comparison.md) also proves a precise tangent comparison for the actual degree-one homotopy equivalence \(g:S^6\to X\) constructed in Section 9. There is an oriented bundle isomorphism
\[
B:g^*TX\longrightarrow TS^6.
\tag{10.5}
\]
It is obtained by lifting the original tangent clutching map to \(SU(4)\), using its exterior-square real representation, and proving that the Euler number divided by two classifies oriented rank-six bundles on \(S^6\). Both bundles in (10.5) have Euler number two. The proof retains the determinant contribution before using its specified trivialization. The actual stabilization map and its inverse are
\[
\begin{aligned}
(p;v,a)&\longmapsto(p;B_pv+ap),\\
(p;w)&\longmapsto
\bigl(p;B_p^{-1}(w-\langle w,p\rangle p),\langle w,p\rangle\bigr).
\end{aligned}
\tag{10.6}
\]
Thus \(g^*TX\oplus\mathbf1_{\mathbb R}\) is trivial, and pulling back by the homotopy inverse gives a stable framing of the original \(TX\oplus\mathbf1_{\mathbb R}\). Its rank-six Euler class has not disappeared. A stable framing alone does not compute a framed bordism class or prove \(\Theta_6=0\).

The [degree-six cobar companion](the-degree-six-milnor-cobar-calculation.md#six-cobar-survival) now proves the complete degree-six cohomology calculation for the original Milnor Hopf algebra at two and its vanishing at every odd prime. Its proof retains every word length, both full correcting cochains, the source filtration comparison and every odd-prime sign. The actual coefficient comparisons and convergence to the specified arithmetic completions are proved in the subsequent linked companions. The [original integral comparison](the-original-integral-stable-group-and-its-completion-maps.md#integral-degree-six-answer) now proves finite generation of the original sphere groups, the exact suspension range and the full unit comparison with all prime completions. It proves \(\pi_6(\mathbb S)=\mathbb Z/2\mathbb Z\) and that the original 2-completion unit is an isomorphism in degree six. The [original geometric framing proof](the-original-six-dimensional-framing-invariant.md#framed-six-original-nullbordism) constructs the full quadratic invariant, proves framed bordism invariance and gives value zero for the original framed homotopy six-sphere, with an actual framed nullbordism. The [sphere-twist and smooth-recognition proof](sphere-twists-and-the-original-smooth-six-sphere-comparison.md#twist-original-smooth-map) now constructs the new interior gluing with its full frame defect, cancels every actual handle and gives the orientation-preserving diffeomorphism to the original six-sphere, homotopic to its original degree-one map. The algebraic theorem alone does not establish the smooth sphere-group calculation.

The [original-frame Pontryagin–Thom companion](framed-manifolds-and-the-pontryagin-thom-map.md#pt-bijection) now proves both geometric constructions and their exact inverse comparison. It constructs the original normal frame from the specified tangent framing, retains the full tube and Gram matrix, recovers the original frame at a regular inverse image, and proves the relative homotopy-to-bordism map. Its [suspension and original tangent-framing comparison](framed-manifolds-and-the-pontryagin-thom-map.md#pt-stabilization-and-original-framing) shows exactly how a proved zero stable class would yield a bounding manifold with the given boundary framing. The homotopy of the full comparison involution uses the original complex tangent operator. This completes the geometric correspondence. The [original geometric framing proof](the-original-six-dimensional-framing-invariant.md#framed-six-original-nullbordism) now calculates the original stable class as zero and obtains its framed nullbordism.

The [original coefficient-ring companion](coefficient-rings-and-the-original-degree-six-class.md#coefficient-original-h28) now proves the full source coefficient and grading comparisons. It calculates the entire original polynomial-coefficient cobar group in bidegree \((2,8)\), proves that this group has no coefficient torsion, and gives the exact map of its generator to the classical degree-six class. All other lengths retain an explicit bound on their coefficient torsion. These algebraic results feed the actual cooperation and integral comparisons proved in the linked companions below. The [original geometric framing proof](the-original-six-dimensional-framing-invariant.md#framed-six-original-nullbordism) now completes the geometric value calculation and supplies the framed nullbordism.

The [original Adams-tower companion](the-adams-tower-and-exact-inverse-limits.md#adams-actual-convergence) constructs the ordinary-cohomology spectrum from its full finite cocycles and cochain spaces, proves every stage group finite with its exact prime-power bound, and proves convergence to the specified homotopy limit with a complete separated filtration. Its [degree-five calculation](the-adams-tower-and-exact-inverse-limits.md#adams-degree-five-cobar) proves all-length vanishing needed by the outgoing degree-six differentials. The [actual degree-eight companion](the-actual-mod-two-cooperation-comparison-through-degree-eight.md#actual-eight-bijectivity) identifies the actual cooperation algebra through degree eight. The original geometric framing chapter proves the value zero and its framed nullbordism.

The [arithmetic-completion companion](the-original-adams-tower-and-arithmetic-completion.md#arithmetic-adams-equivalence) now constructs the unit-preserving equivalence from the original Moore-tower limit to this Adams limit. The proof covers every bounded-below spectrum and gives the exact finite transition bound \(2m(n-b+1)\). Its [homotopy-group comparison](the-original-adams-tower-and-arithmetic-completion.md#arithmetic-homotopy-groups) retains both derived terms, the original unit sign, the full torsion transitions and the complete degree-zero extension. In particular \(\pi_0C_s=\mathbb Z/p^{s+1}\), so the stage exponent is sharp. The original geometric framing chapter proves that value zero, with its complete geometric invariant.

The [actual mod-two cooperation companion](the-actual-mod-two-adams-resolution-and-cooperation-maps.md#cooperation-chain-comparison) now constructs both cross-product coordinate maps, the actual cofree Adams resolution and both chain maps and inverse homotopies comparing it with the actual cooperation cobar complex. Its [original diagonal and degree-range proof](the-actual-mod-two-adams-resolution-and-cooperation-maps.md#cooperation-original-diagonal) identifies the generator tied to the original integer two, proves every degree-two reduced coproduct zero, and shows that the degree-six calculation at every word length uses cooperation degrees through eight. The [actual degree-eight companion](the-actual-mod-two-cooperation-comparison-through-degree-eight.md#actual-eight-bijectivity) supplies the required polynomial comparison through degree eight; the [original geometric framing proof](the-original-six-dimensional-framing-invariant.md#framed-six-original-nullbordism) now supplies that value and its actual framed nullbordism.

The [full characteristic-two coordinate proof](the-exact-characteristic-two-coordinate-calculation.md#formal-two-linearization) now supplies the all-ring formal-series calculation and both inverses. The [actual projective-coordinate proof](the-original-projective-coordinate-and-actual-cooperations.md#projective-actual-coproduct) constructs the polynomial-to-cooperation morphism, proves its full coproduct and antipode comparison, and identifies its [first generator with the original integer two](the-original-projective-coordinate-and-actual-cooperations.md#projective-original-two). The [actual degree-eight companion](the-actual-mod-two-cooperation-comparison-through-degree-eight.md#actual-eight-bijectivity) now proves bijectivity of this original morphism in every cooperation degree from zero through eight. Its [bar and original-suspension proof](the-actual-mod-two-cooperation-comparison-through-degree-eight.md#actual-eight-original-suspension) determines the full graded dimensions, and its [cup-square calculation](the-actual-mod-two-cooperation-comparison-through-degree-eight.md#actual-eight-nonzero-powers) proves every power of the actual first generator nonzero. The [receiving cobar and convergence argument](the-actual-mod-two-cooperation-comparison-through-degree-eight.md#actual-eight-receiving-cobar) identifies the entire degree-six line and proves \(\pi_6(\mathbb S^{\wedge}_2)=\mathbb F_2\), with the original permanent-cycle representative. The [actual odd-prime companion](the-original-odd-prime-cooperations-and-degree-six-adams-calculation.md#odd-actual-adams) now proves the full signed bar and original suspension calculation, the actual cooperation degrees needed by stem six, and the signed comparison with the original Adams tower. It proves \(\pi_6(\mathbb S^{\wedge}_p)=0\) for every odd prime. The [original integral comparison](the-original-integral-stable-group-and-its-completion-maps.md#integral-degree-six-answer) now proves finite generation of the original sphere groups, the exact suspension range and the full unit comparison with all prime completions. It proves \(\pi_6(\mathbb S)=\mathbb Z/2\mathbb Z\) and that the original 2-completion unit is an isomorphism in degree six. The [original geometric framing proof](the-original-six-dimensional-framing-invariant.md#framed-six-original-nullbordism) constructs the full quadratic invariant, proves framed bordism invariance and gives value zero for the original framed homotopy six-sphere, with an actual framed nullbordism. The [sphere-twist and smooth-recognition proof](sphere-twists-and-the-original-smooth-six-sphere-comparison.md#twist-original-smooth-map) now constructs the new interior gluing with its full frame defect, cancels every actual handle and gives the orientation-preserving diffeomorphism to the original six-sphere, homotopic to its original degree-one map.

**Theorem 10.2.** There is an orientation-preserving smooth diffeomorphism \(d:S^6\to X\), with \(d\simeq g\) and \(d^{-1}\simeq h_X\) for the original maps of Section 9.

**Proof.** The original stable tangent frame in (10.6) enters the full Pontryagin–Thom comparison and geometric framing proof cited above. For the whole six-dimensional framed bordism group, the [general stable tangent-frame comparison](sphere-twists-and-the-original-smooth-six-sphere-comparison.md#twist-general-stable-framing) proves the complete tangent-to-normal framing homotopy without assuming a complex structure; this is an independent bundle calculation before the sphere argument. The latter's Sections 8–9 prove framed bordism invariance and identify the original sixth framed bordism group with \(\mathbb F_2\) through its quadratic invariant. The original \(H_3(X;\mathbb F_2)=0\) makes that invariant zero; injectivity therefore yields an actual framed nullbordism \(W\) with its specified boundary identification \(\iota_X:X\to\partial W\).

Remove a coordinate ball \(\chi(D^7_\rho)\) and keep its parametrization \(j(q)=\chi(\rho q)\), including \(Dj_q(v)=D\chi_{\rho q}(\rho v)\). The framed interior surgeries and exact index reduction in that geometric chapter produce a two-connected cobordism with only indices three and four. The sphere-twist companion, Section 4, proves that its actual common level \(P\) has a free unimodular alternating middle group, with two primitive integral Lagrangians: the lower belts \(b_i\) and the upper attaching classes \(a_j\). Both have the same rank \(r\). Its exact original signed matrix is
\[
 D^{\rm old}_{ij}=\sigma_i\lambda(b_i,a_j),\qquad
 H_4(C',S^6)=\ker D^{\rm old},\quad
 H_3(C',S^6)=\operatorname{coker}D^{\rm old}.
 \tag{10.7}
\]
The signs \(\sigma_i\) are those of the original ordered handle charts; no acyclicity of this old filling is presumed.

Sections 1–3 of the [sphere-twist companion](sphere-twists-and-the-original-smooth-six-sphere-comparison.md#twist-actual-cancellation) construct the complete radius-dependent tube twist, prove its signed integral action and give a terminating integral algorithm. It supplies an actual orientation-preserving diffeomorphism \(\varphi:P\to P\) carrying the upper Lagrangian onto an integral complementary one. This \(\varphi\) acts on the six-dimensional middle level and is distinct from the five-sphere gluing map \(\phi\) in (10.4). Reglue the two original seven-dimensional pieces by
\[
 C_\varphi=(C_-\sqcup C_+)/
             \bigl(i_+(p)\sim i_-(\varphi(p))\bigr).
 \tag{10.8}
\]
Its complete smooth seam is proved in Section 5 there. Both outer boundary maps remain fixed. If \(\tau_\pm\) are the original piece frames expressed in directed collar coordinates and a common stable rank \(7+k\), their exact new comparison is
\[
 A_\varphi(p)=\tau_{-,\varphi(p)}
                (D\varphi_p\oplus1\oplus I_k)\tau_{+,p}^{-1}.
 \tag{10.9}
\]
Thus the construction retains the original frames without assuming that the new gluing preserves them.

In a dual basis \(\lambda(b_i,f_j)=\delta_{ij}\), put \(F_i=\sigma_i f_i\) and write \(\varphi_*a_j=\sum_iF_iU_{ij}\). The matrix \(U\) is unimodular because both collections are bases of the same primitive subgroup. The original handle-to-intersection comparison gives the new boundary matrix \(D^\varphi=U\). The full framed slides realize \(U^{-1}\), with each orientation sign recorded as a signed comparison of the original geometric core. Supported Whitney moves in the actual dimension pair \((3,3)\) remove the opposite-sign intersections. The level before the lower stage is the simply connected incoming \(S^6\), so the proved belt-complement, disc and rank-four framing hypotheses all hold. Exactly one transverse geometric intersection remains for each matched pair. Section 6 of that companion applies the included actual Morse realization, checks escape and disjoint compact supports, and cancels all pairs.

The resulting function on \(C_\varphi\) has no critical point. With its retained endpoint values \(\ell_-<\ell_+\), let \(T=\ell_+-\ell_-\) and \(Y=V/df_{\rm end}(V)\), where the original positive field \(V\) matches both boundary collars. The full product and outgoing maps are
\[
 \begin{split}
 \Psi(q,t)&=\operatorname{Fl}^{Y}_t(j(q)),\qquad 0\le t\le T,\\
 d(q)&=\iota_X^{-1}\Psi(q,T),\\
 d^{-1}(x)&=j^{-1}\operatorname{Fl}^{Y}_{-T}(\iota_X(x)).
 \end{split}
 \tag{10.10}
\]
Their exact inverse identities, smoothness at the collars and orientation are proved there from \(df_{\rm end}(Y)=1\). In particular \(d_*[S^6]=[X]\). The original first Hurewicz isomorphism in Section 9 sends both \([d]\) and \([g]\) to \([X]\); its injectivity, with the unique basepoint change supplied by \(\pi_1X=0\), gives \(d\simeq g\). Composing with the retained inverse homotopies gives \(d^{-1}\simeq h_X\).

Finally retain the old tangent isomorphism \(B\) from (10.5). Finite projection transport along this homotopy supplies \(P:g^*TX\to d^*TX\). The exact comparison with the new derivative is
\[
 E_q=B_qP_q^{-1}Dd_q,\qquad Dd_q=P_qB_q^{-1}E_q .
 \tag{10.11}
\]
Every map is invertible; no claim \(E=1\) or nullhomotopy of \(E\) is used. This proves the theorem with both original maps, their full tangent comparison, both filling matrices and the stable-frame defect retained. ∎

The same receiving proof applies to every oriented smooth homotopy six-sphere, using the proved \(\pi_5SO(7)=0\) to obtain its original stable frame. It therefore gives \(\Theta_6=0\) without an assumption of a complex structure. The sphere-twist companion contains two additional fully solved matrix examples, including old torsion and the exact new gluing.

**Status of the classical prerequisite.** The complete receiving proofs are included and have received author self-checking and supplementary finite algebra checks. The bounded original-author Benedetti reading supplies historical context and explicitly does not supply the whole \(h\)-cobordism proof. The complete geometric arguments instead appear in the linked handle, Whitney, Morse, framing and sphere-twist companions. No independent mathematical review or exhaustive literature reading is claimed.

## 11. Four worked exercises {#solved-exercises}

### Exercise 11.1. Detecting the exact finite index rather than its rational rank

In the order-four case use the original invariant basis
\[
h=\gamma\eta_2,\qquad q=uw+6\gamma\delta,
\tag{11.1}
\]
whose pairing on the torus is \(\begin{pmatrix}0&2\\2&12\end{pmatrix}\).
Knowing that the specialization image has index two and does not contain \(h\), recover the image lattice and its pairing on \(S_2\).

**Solution.** An index-two sublattice is the kernel of a nonzero map from \(\mathbb Z h\oplus\mathbb Zq\) to \(\mathbb Z/2\). Since it does not contain \(h\), that map takes \(h\) to \(1\). Its value on \(q\) is \(a\in\{0,1\}\). Thus the sublattice has basis \(2h,ah+q\). Pairing these vectors on the torus and dividing by the degree-four covering gives
\[
\frac14
\begin{pmatrix}2&0\\a&1\end{pmatrix}
\begin{pmatrix}0&2\\2&12\end{pmatrix}
\begin{pmatrix}2&a\\0&1\end{pmatrix}
=
\begin{pmatrix}0&1\\1&a+3\end{pmatrix}.
\tag{11.2}
\]
The original affine descent calculation (2.10a) applies to the proposed class \(a h+q\): its lifted action would require the integer coefficient \(\ell_3=-(a+3)/2\). Thus \(a+3\) is even, forcing \(a=1\). The explicit lift in the companion proves existence as well as necessity, so the exact image is
\[
\mathbb Z(2\gamma\eta_2)\oplus
\mathbb Z(\gamma\eta_2+q)
=\{a'\gamma\eta_2+b'q:a'\equiv b'\pmod2\}.
\tag{11.3}
\]
Its pairing in the displayed basis is \(\begin{pmatrix}0&1\\1&4\end{pmatrix}\). This keeps the original \(q\) and does not replace it by a changed basis vector. The cokernel is generated by the class of \(\gamma\eta_2\) and is exactly \(\mathbb Z/2\).

### Exercise 11.2. Recovering the normalization groups over the integers

For the constant-sheaf normalization complex, compute the entire cohomology of its degree-zero global row
\[
\mathbb Z\xrightarrow{0}\mathbb Z^3
\xrightarrow{D}\mathbb Z^2,\qquad
D(a,b,c)=(a-b+c,a-b+c).
\tag{11.4}
\]
Do the corresponding calculation for the degree-two row of Section 3.

**Solution.** The first group survives as \(\mathbb Z\). The kernel of \(D\) has basis \((1,1,0)\), \((-1,0,1)\): the equation gives \(a=b-c\), and these two coordinates realize every solution uniquely. Thus its degree-one cohomology is \(\mathbb Z^2\). The image is the full diagonal subgroup, because \(D(1,0,0)=(1,1)\). The map \((x,y)\mapsto y-x\) identifies its cokernel with \(\mathbb Z\). All these groups are free.

In the degree-two row the map sends
\(L=aH-b_1E_1-b_2E_2-b_3E_3\) to
\[
(s,-s,s),\qquad s=b_1+b_2+b_3-a.
\tag{11.5}
\]
The scalar map \(s:\mathbb Z^4\to\mathbb Z\) is onto, since \(s(-H)=1\). Its kernel is freely parametrized by \(b_1,b_2,b_3\), with \(a=b_1+b_2+b_3\). Hence the row kernel is \(\mathbb Z^3\). The vector \((1,-1,1)\) is primitive; the quotient is explicitly \(\mathbb Z^2\) via
\[
(x,y,z)\longmapsto(x+y,z+y).
\tag{11.6}
\]
Its kernel is exactly the subgroup generated by \((1,-1,1)\), and it is onto by choosing \(y=0\). The degree-four normalization class contributes a further \(\mathbb Z\). Combining the rows with their distinct total degrees gives the ranks \(1,2,4,2,1\) of \(H^*(W;\mathbb Z)\). The spectral-sequence filtration cannot introduce torsion: each successive quotient is free, and a short exact sequence with free quotient splits by lifting a basis.

### Exercise 11.3. Reversing the base orientation without losing a sign

Retain the original classes \(\theta=12\gamma,\ a=2q,\ b=2\gamma uw\), but write the base generator as \(\omega'=-\omega\). Determine all three differentials in that basis by the product equations.

**Solution.** The first differential is \(d_2\theta=-\omega'\). Write
\(d_2a=r'\omega'[\delta]\) and
\(d_2b=s'\omega'[\gamma\delta]\).
The unchanged identity \(\theta a=12b\), with \(|\theta|=1\), gives
\[
12s'=-24-12r',\qquad s'=-2-r'.
\tag{11.7}
\]
The unchanged identity \(ab=0\) and the original exterior signs
\(\delta b=-2\operatorname{vol}\), \(a\gamma\delta=2\operatorname{vol}\)
give
\[
-2r'+2s'=0.
\tag{11.8}
\]
Thus \(r'=s'=-1\). All three coefficients change sign together. Their absolute values remain one, so all three maps remain integral isomorphisms onto their targets. This calculation also shows why reversing only the first sign while keeping the other two would violate the multiplicative spectral sequence.

### Exercise 11.4. Why the Euler characteristic does not close the calculation

Produce a closed simply connected oriented six-manifold with Euler characteristic two but with nonzero second and third integral homology. Compute those groups and compare the precise missing information with Theorem 7.1.

**Solution.** Take
\[
M=(S^2\times S^4)\mathbin{\#}(S^3\times S^3).
\tag{11.9}
\]
Each product is simply connected. Removing a coordinate disc does not change its fundamental group: adding it back uses a simply connected \(S^5\) collar, so Van Kampen identifies the two groups. Gluing the punctured products along that same simply connected collar shows \(\pi_1(M)=0\).

For \(1\leq k\leq4\), removal of a disc preserves \(H_k\) by the pair sequence and excision, whose only nonzero relative group is in degree six. The Mayer–Vietoris sequence for the connected sum has overlap \(S^5\), with zero homology in degrees one through four; its degree-zero maps also show connectedness. It follows that
\[
H_2(M)=\mathbb Z,\qquad H_3(M)=\mathbb Z^2,\qquad H_4(M)=\mathbb Z.
\tag{11.10}
\]
The product groups here follow from their product cells: \(S^2\times S^4\) has cells in degrees \(0,2,4,6\), and \(S^3\times S^3\) has cells in degrees \(0,3,3,6\), with zero cellular boundaries. Orientation and Poincaré duality give \(H_6(M)=\mathbb Z\), \(H_5(M)=H^1(M)=0\); the remaining groups are as stated. Therefore
\[
\chi(M)=1+1-2+1+1=2.
\tag{11.11}
\]
Its nonzero \(H_2\) and \(H_3\) prevent it from being a homology sphere. In the original \(X\), it is the three primitive integral transgressions, the two parabolic vanishing calculations and the universal-coefficient argument that remove those groups and their possible torsion. The matching Euler characteristic alone supplies none of these maps.

