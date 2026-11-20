# Independent complete derivation of P1.8

## Provenance and scope

Authoring agent: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited reasoning effort; no numeric effort setting is exposed. This derivation was made from exactly `audit_root/P18_fresh_inputs_09/statements_only.tex` and `audit_root/P18_fresh_inputs_09/raw_marked_inputs.md`, together with the fresh computations authored in this directory. P1.1, P1.4, P1.5, and P1.7 are the permitted proved inputs. The printed P1.15 and P1.18 statements are excluded from the proof. No existing P1.8 proof, producer, receiving result, Library, Space, or prior chat was opened. No online literature was needed.

The proof below constructs the lift, identifies all of its scalar freedom, defines the real transversality function, proves its exact global parameter domain, derives the cusp graph and its bounded correction, and supplies the finite-root descent morphism. It does not compute a numerical minimum for any later algebraic splitting.

## 1. Conventions, exact maps, and the compact base

Write

\[
\mathfrak B_8=\sqrt[8]{(\mathbb P^1,0)}\times_{\mathbb P^1}\sqrt[5]{(\mathbb P^1,\infty)},
\qquad
\mathfrak B=\sqrt[4]{(\mathbb P^1,0)}\times_{\mathbb P^1}\sqrt[5]{(\mathbb P^1,\infty)}.
\]

There is an explicit morphism \(d:\mathfrak B_8\to\mathfrak B\): on the zero chart it sends the order-eight coordinate \(s\) to the order-four coordinate \(t=s^2\), and at infinity it is the identity on the order-five chart. The cusp \(b_*\) lies over \(\lambda_*=-256/3125\) and has no stack stabilizer. The base on which real transversality is required is

\[
X=\mathfrak B\setminus\{b_*\}.
\]

It contains the two finite-root points. Its underlying topological space is connected, and its complement in the compact underlying sphere consists of one point.

Let \(E\) denote the rank-four cohomology bundle with its nilpotent canonical extension at the cusp and its good-reduction extensions on \(\mathfrak B_8\). The supplied polarization contraction is the alternating matrix

\[
J=\begin{pmatrix}
0&1&-1&1\\-1&0&1&-1\\1&-1&0&1\\-1&1&-1&0
\end{pmatrix},
\qquad \operatorname{contr}(u\wedge v)=u^tJv.
\]

In lexicographic exterior coordinates the supplied bivector is \(\omega=(1,1,1,1,1,1)^t\). Its alternating matrix \(\Omega\), with every upper-triangular entry equal to one, satisfies \(J\Omega=-I_4\). In particular \(\omega\) is nondegenerate. The actual quotient map is

\[
\pi=\begin{pmatrix}
-1&1&0&0&0&0\\
-1&0&1&0&0&0\\
-1&0&0&1&0&0\\
-1&0&0&0&1&0\\
-1&0&0&0&0&1
\end{pmatrix}.
\]

The fresh matrix computation verifies that

\[
A_{1:5,1:5}=\bigl(Q^{-1}(\wedge^2 C_f^{-1})Q\bigr)_{1:5,1:5},
\quad
B_{1:5,1:5}=\bigl(Q^{-1}(\wedge^2 C_g)Q\bigr)_{1:5,1:5}.
\]

Here the indices \(1:5\) are the last five indices in zero-based indexing. Thus the identification of the five-dimensional quotient with \(W=\wedge^2E/\mathbb C\omega\) is the displayed integral map \(\pi\), not an unspecified representation equivalence. The rank-six system gives the exact sequence

\[
0\longrightarrow\mathcal O e\longrightarrow V\xrightarrow{p_V}W\longrightarrow0,
\qquad e=(1,0,0,0,0,0)^t.
\tag{1}
\]

The exact sequence also holds in the chosen boundary extensions. At the cusp the relation $p_VN_V=N_Wp_V$ gives $p_V\exp(s_qN_V)=\exp(s_qN_W)p_V$, while $N_Ve=0$; in nilpotent frames the map and its kernel are therefore the same constant projection and line as away from the cusp. Finite-root exactness is exactness of the finite representations, with invariant local lifts supplied by averaging.

All occurrences of complex conjugation below refer to the real local systems specified by the integer matrices in the packet.

## 2. The Hodge extension at the cusp and the filtration of P

The Hodge bundle supplied by P1.4 is

\[
H=T^3\oplus T,\qquad \ell=T^3,
\qquad T=\mathcal O\bigl((2/5)[\infty]-(3/8)[0]\bigr).
\tag{2}
\]

For clarity, the properties of its canonical extension needed here can be checked directly at the node. Put \(r=64/625\). The central polynomial factors exactly as

\[
x^5+\lambda_*^3x+\lambda_*^4
=(x-r)^2g(x),\qquad
 g(x)=x^3+2rx^2+3r^2x+4r^3,
\tag{3}
\]

and \(g(r)=10r^3\ne0\). The normalization map of the nodal curve is the explicit map

\[
\nu:\{z^2=g(x)\}\longrightarrow C_{\lambda_*},
\qquad (x,z)\longmapsto(x,(x-r)z).
\tag{4}
\]

The two preimages of the node are \((r,\pm\sqrt{10r^3})\). The pullback of \(dx/y\) is

\[
\frac{dx}{(x-r)z},
\]

with nonzero residues \(\pm(10r^3)^{-1/2}\). The pullback of \((x-r)dx/y\) is \(dx/z\), a nonzero holomorphic differential on the smooth genus-one normalization. These give two independent limiting Hodge classes: the first has nonzero residue and the second comes from the normalization. The logarithmic period calculation in Section 7 proves directly that they give holomorphic classes in the nilpotent canonical extension.

The polarization extends nondegenerately to that extension. Indeed its matrix in the nilpotent exponential frame is still \(J\), because the monodromy logarithm is infinitesimally symplectic. The rank-two Hodge bundle is isotropic on the smooth fibers and therefore, by holomorphic continuation, on the extended fiber too. Its rank remains two by the preceding residue and normalization classes. Consequently the following map is an isomorphism on every fiber, including the cusp:

\[
E/H\longrightarrow H^\vee,
\qquad [v]\longmapsto\bigl(h\longmapsto\operatorname{contr}(h\wedge v)\bigr).
\tag{5}
\]

The map has kernel zero because \(H=H^\perp\), and both sides have rank two. This proves the exact Hodge sequence needed below without an assertion of an unexamined cusp extension.

The wedge map

\[
\ell\otimes(E/\ell)\longrightarrow W,
\qquad u\otimes[v]\longmapsto\pi(u\wedge v)
\tag{6}
\]

is fiberwise injective. Its wedge map before projection has kernel zero on \(E/\ell\). A bivector \(u\wedge v\) has square zero, while \(\omega\wedge\omega\ne0\); thus the image of that wedge map has zero intersection with \(\mathbb C\omega\). This verifies the actual injection at the boundary as well as the permitted input P1.5. We identify its image with \(P\).

The contraction defines a surjection

\[
\alpha:P\longrightarrow\mathcal O,
\qquad \alpha\bigl(\pi(u\wedge v)\bigr)=u^tJv.
\tag{7}
\]

Its value is defined using the unique representative in \(u\wedge E\), so no contraction is being applied ambiguously to a class modulo \(\omega\). Nondegeneracy of \(J\) gives surjectivity for every nonzero \(u\). Set \(K=\ker\alpha\). The exact maps in (5) give

\[
0\longrightarrow\ell\otimes(H/\ell)\longrightarrow K
\longrightarrow\ell\otimes(H/\ell)^\vee\longrightarrow0.
\tag{8}
\]

The last map is induced by (5), restricted to \(\ell^\perp/H\); its image is the annihilator of \(\ell\) in \(H^\vee\), which equals \((H/\ell)^\vee\). With (2), (8) is

\[
0\longrightarrow T^4\longrightarrow K\longrightarrow T^2\longrightarrow0,
\qquad
0\longrightarrow K\longrightarrow P\xrightarrow{\alpha}\mathcal O\longrightarrow0.
\tag{9}
\]

These are actual bundle maps; they fix the relevant line-bundle identifications.

## 3. Descent of the bundles and the needed cohomology

Put

\[
L=\mathcal O\bigl((4/5)[\infty]-(3/4)[0]\bigr)
\quad\hbox{on }\mathfrak B.
\tag{10}
\]

Then \(d^*L=T^2\). The kernel \(\mu_2\) of the zero-chart map \(\mu_8\to\mu_4\) acts as \(-I\) on \(E\), as proved from the explicit root-chart action in Section 10. It acts as the identity on \(\wedge^2E\), \(W\), and \(P\). Accordingly their descent along \(d\) is the invariant descent through this explicit kernel. The rank-six system already has the order-four zero-chart action \(B\), so (1) and (7) descend to \(\mathfrak B\). On that base (9) reads

\[
0\longrightarrow L^2\longrightarrow K\longrightarrow L\longrightarrow0,
\qquad
0\longrightarrow K\longrightarrow P\xrightarrow{\alpha}\mathcal O\longrightarrow0.
\tag{11}
\]

Let \(\rho:\mathfrak B\to\mathbb P^1\) be the coarse map. Directly taking invariant Laurent monomials on a root chart gives

\[
\rho_*L^k
=\mathcal O_{\mathbb P^1}\left(
\left\lfloor\frac{4k}{5}\right\rfloor[\infty]
+\left\lfloor-\frac{3k}{4}\right\rfloor[0]\right).
\tag{12}
\]

For example, on a chart \(z=t^m\), a line with divisor coefficient \(a/m\) has generator \(t^{-a}\). Invariant sections have coefficients with powers congruent to \(a\pmod m\); their smallest nonnegative power leaves the coarse generator \(z^{-\lfloor a/m\rfloor}\). This is the precise local map underlying (12). Taking invariants of a finite group is exact by averaging, so the same invariant-chart Čech calculation computes the cohomology of \(L^k\) from the right side of (12).

The required values are

| \(k\) | \(\lfloor4k/5\rfloor\) | \(\lfloor-3k/4\rfloor\) | coarse degree |
|---:|---:|---:|---:|
| \(-2\) | \(-2\) | \(1\) | \(-1\) |
| \(-1\) | \(-1\) | \(0\) | \(-1\) |
| \(0\) | \(0\) | \(0\) | \(0\) |
| \(1\) | \(0\) | \(-1\) | \(-1\) |
| \(2\) | \(1\) | \(-2\) | \(-1\) |

Thus

\[
H^0(L^{\pm1})=H^0(L^{\pm2})=0,
\quad
H^1(L^{\pm1})=H^1(L^{\pm2})=0,
\quad H^1(\mathcal O)=0,
\quad H^0(\mathcal O)=\mathbb C.
\tag{13}
\]

Here the sphere cohomology assertion has an explicit additive Cousin construction. For a coarse line of degree \(d=-1\) or \(0\), choose frames with transition \(e_\infty=\lambda^d e_0\). An overlap cocycle \(g(\lambda)=\sum_{n\in\mathbb Z}a_n\lambda^n\) decomposes as

\[
g_0(\lambda)=\sum_{n\ge0}a_n\lambda^n,
\qquad
 g_\infty(1/\lambda)=-\lambda^{-d}\sum_{n<0}a_n\lambda^n,
\qquad g=g_0-\lambda^dg_\infty.
\tag{14}
\]

Both functions are holomorphic on their respective charts, with convergence inherited from the Laurent expansion. This constructs the vanishing of \(H^1\). The transition convention follows from the exact map \(f\mapsto\lambda^bf\) taking \(\mathcal O(a[\infty]+b[0])\) to \(\mathcal O((a+b)[\infty])\). A global section of a degree-minus-one line has no allowable Laurent monomial, which proves its \(H^0\) vanishing.

The first extension in (11) has class in \(H^1(L)=0\). Its splitting is unique because the space of differences is \(H^0(L)=0\). Hence \(K=L^2\oplus L\), with the first summand and the quotient maps fixed by (11). The second extension splits because \(H^1(K)=0\), and its splitting is unique because \(H^0(K)=0\). We obtain an isomorphism respecting the filtration and the contraction:

\[
P\simeq L^2\oplus L\oplus\mathcal O,
\qquad \alpha=(0,0,1).
\tag{15}
\]

In particular

\[
H^1(P^\vee)=0,
\qquad H^0(P^\vee)=\mathbb C\alpha.
\tag{16}
\]

## 4. Actual holomorphic lifting and its complete scalar freedom

Take the pullback of (1) along the inclusion \(P\hookrightarrow W\):

\[
V_P=\{(v,p)\in V\oplus P:p_V(v)=p\},
\qquad
0\longrightarrow\mathcal Oe\longrightarrow V_P\longrightarrow P\longrightarrow0.
\tag{17}
\]

Local bundle splittings exist because the displayed map is a surjection of locally free sheaves. On finite quotient charts they can be made equivariant by the explicit averaging map

\[
\sigma_{\rm av}(p)=\frac1{|G|}\sum_{g\in G}g^{-1}\sigma_{\rm loc}(gp).
\tag{18}
\]

Projection to \(W\) of each summand is \(p\), so (18) remains a lift. On overlaps their differences form a \(P^\vee\)-valued Čech cocycle multiplying \(e\). Use (15), the invariant-chart map (12), and the Laurent formula (14) separately on its \(L^{-2}\), \(L^{-1}\), and \(\mathcal O\) components. Subtracting the resulting local zero-cochains gives local lifts which agree on overlaps. This constructs a global holomorphic map

\[
\sigma:P\longrightarrow V,
\qquad p_V\sigma=\operatorname{id}_P.
\tag{19}
\]

The same construction applies at the cusp in the nilpotent canonical extensions, so (19) is holomorphic there in canonical frames, not merely on a punctured neighborhood. Equivalently, (16) kills the extension class of (17); (14) specifies the cochain operation realizing that statement.

Here global holomorphic lifting is on the compact orbifold with the canonical extension at the cusp; its restriction map gives the lifts being used on $X$. Every second lift on that compact extension has the form

\[
\sigma'=\sigma+a\alpha e,\qquad a\in\mathbb C,
\tag{20}
\]

because its difference from \(\sigma\) has image in \(\mathcal Oe\), and (16) identifies the full space of such differences. Conversely every map in (20) is a lift. This proves the complete scalar freedom.

A concrete prescribed lift can be selected without leaving an unassigned extension class: fix a smooth base point, a flat marking there, and a vector \(p_0\in P\) with \(\alpha(p_0)=1\). For the lift constructed above, let \(a_0\) be the first coordinate of \(\sigma(p_0)\) in the supplied \((e,W)\) coordinates. The map

\[
\sigma_* =\sigma-a_0\alpha e
\tag{21}
\]

is the unique global holomorphic lift for which that first coordinate is zero. Formula (20) proves independence of the preliminary choices in the construction of (21). The subsequent statements hold for every specified \(\sigma\), including (21).

For each real number \(c\), define

\[
F_c=(\sigma+ic\alpha e)(P)\subset V|_X.
\tag{22}
\]

Projection to \(W\) restricts to the identity on \(P\), so the map in (22) is injective and its image is a holomorphic rank-three subbundle. The formula also gives a holomorphic family in the complex parameter replacing \(ic\).

## 5. The common line of P and its conjugate

At a point of \(X\), choose a nonzero Hodge generator \(u\in\ell\). Set

\[
\beta=u^tJ\bar u,
\qquad p=\pi(u\wedge\bar u).
\tag{23}
\]

The prescribed polarization convention gives \(i\beta>0\). Consequently \(\beta\ne0\), \(\bar\beta=-\beta\), and \(u,\bar u\) span a nondegenerate symplectic two-plane \(U\). There is the actual symplectic direct-sum map \(U\oplus U^\perp\to E\), given by addition, which is an isomorphism since \(U\cap U^\perp=0\) and the dimensions add to four. Because \(J\Omega=-I\), the bivector \(\omega\) decomposes in this sum as a nonzero bivector on \(U\) plus a nonzero bivector on \(U^\perp\).

An equality of quotient classes

\[
\pi(u\wedge v)=\pi(\bar u\wedge w)
\]

means \(u\wedge v-\bar u\wedge w=t\omega\). Its left side has zero component in \(\wedge^2U^\perp\); the right side has a nonzero such component multiplied by \(t\). Thus \(t=0\). The direct decomposition

\[
\wedge^2 E=\wedge^2U\oplus(U\wedge U^\perp)\oplus\wedge^2U^\perp
\]

then forces the common vector to be a multiple of \(u\wedge\bar u\). This proves

\[
P\cap\bar P=\mathbb C p.
\tag{24}
\]

Define

\[
j=\frac{p}{\beta}.
\tag{25}
\]

Both numerator and denominator change sign under conjugation; hence \(j\) is real. The injection (6) and (7) give \(\alpha(j)=1\). Replacing \(u\) by \(fu\) multiplies both numerator and denominator by \(|f|^2\), so \(j\) is independent of the generator. It is a globally defined nonzero real analytic section of the real line in (24), with the indicated contraction value.

## 6. The exact transversality function

Since \(j\) is real and the quotient map is real, \(\sigma(j)-\overline{\sigma(j)}\) lies in \(\mathbb Ce\) and is purely imaginary. Define the real analytic function \(h\) on \(X\) by the exact identity

\[
\sigma(j)-\overline{\sigma(j)}=2i h e.
\tag{26}
\]

This is single valued: all its constituents are equivariant for the given real monodromies and \(e\) is their fixed real vector. It is also real analytic at the finite-root points, as checked in Section 10.

Every vector in \(F_c\cap\overline{F_c}\) projects to the line (24). The image of \(F_c\) contains no nonzero multiple of \(e\), because projection is injective there. The lift of \(j\) from \(F_c\) is \(\sigma(j)+ic e\); the lift from \(\bar F_c\) is \(\overline{\sigma(j)}-ic e\). Their difference is exactly

\[
2i(h+c)e.
\tag{27}
\]

Therefore, at each point of \(X\),

\[
F_c\cap\overline{F_c}=0\quad\Longleftrightarrow\quad h+c\ne0.
\tag{28}
\]

A change of splitting (20) changes the function by

\[
h_{\sigma+a\alpha e}=h_\sigma+\operatorname{Im}a.
\tag{29}
\]

Thus the function and its minimum are tied to the specified lift, with their transformation completely identified.

## 7. Explicit plumbing and the actual logarithmic periods of the Hodge line

Write \(f(x,\lambda)=x^5+\lambda^3x+\lambda^4\). Near \(\lambda_*\), choose the analytic branch

\[
x_c(\lambda)=r(\lambda/\lambda_*)^{3/4},
\qquad 5x_c(\lambda)^4+\lambda^3=0.
\]

Define

\[
G(x,\lambda)=x^3+2x_cx^2+3x_c^2x+4x_c^3,
\quad z=(x-x_c)\sqrt{G(x,\lambda)},
\]

with either analytic square-root branch near the node. The exact polynomial identity

\[
f(x,\lambda)=f(x_c,\lambda)+(x-x_c)^2G(x,\lambda)
\]

gives the local analytic coordinate morphism

\[
u=y-z,\qquad v=y+z,
\qquad uv=q(\lambda):=f(x_c,\lambda)=\lambda^4-4x_c^5.
\tag{30}
\]

The derivative of \(z\) with respect to \(x\) at the node is \(\sqrt{10r^3}\ne0\), so \((u,v)\) are analytic plumbing coordinates. Moreover

\[
q'(\lambda_*)=\partial_\lambda f(r,\lambda_*)
=\lambda_*^2(3r+4\lambda_*)=-\frac{r\lambda_*^2}{5}\ne0.
\tag{31}
\]

Thus \(q\) is a genuine local base coordinate. Along a fiber, \(v=q/u\), \(z=(v-u)/2\), and \(y=(u+v)/2\). Direct differentiation gives

\[
\frac{dx}{y}=-x_z\,\frac{du}{u}=F(u,v)\frac{du}{u},
\qquad F(0,0)=-\frac1{\sqrt{10r^3}}\ne0,
\tag{32}
\]

where \(F\) is holomorphic after expressing \(\lambda\) as a holomorphic function of \(uv\). Expand

\[
F(u,v)=\sum_{m,n\ge0}f_{mn}u^mv^n.
\]

On the annulus \(uv=q\), its Laurent constant is

\[
R(q)=\sum_{n\ge0}f_{nn}q^n.
\tag{33}
\]

The vanishing-circle period is \(a(q)=2\pi iR(q)\), up to the orientation of that circle, and \(a(0)\ne0\). For a crossing path from \(u=\varepsilon\) to \(u=q/\varepsilon\), the terms with \(m=n\) contribute \(R(q)\log q\) plus a holomorphic term. Each term with \(m\ne n\) contributes

\[
\frac{f_{mn}}{m-n}\left(q^m\varepsilon^{n-m}-q^n\varepsilon^{m-n}\right).
\tag{34}
\]

This is holomorphic in \(q\). The series converges normally after choosing a smaller plumbing bidisc. Integrals over the remaining parts of a transported cycle are holomorphic: away from the plumbing annulus, finitely many smooth relative coordinate charts give holomorphic primitives, and the path integrals are differences of those primitives at holomorphically moving endpoints. Thus crossing periods equal their indicated logarithmic part plus a holomorphic function at \(q=0\). This proves, rather than presupposes, the bounded holomorphic remainder.

For the supplied marking,

\[
C_fC_g^{-1}=I_4+N_H,
\qquad
N_H=\begin{pmatrix}0&0&0&0\\1&0&0&0\\1&0&0&0\\1&0&0&0\end{pmatrix}
=d_0e_0^t,
\quad d_0=(0,1,1,1)^t.
\tag{35}
\]

The equality \(Jd_0=e_0\) identifies the monodromy transvection functional with the vanishing period. The primitive vanishing class has the marking \(\pm d_0\); the orientation makes the associated period functional \(e_0^t\), with the simultaneous sign change of the dual class leaving (35) unchanged. In particular the first coordinate of the Hodge vector is its nonzero vanishing period, up to that harmless simultaneous orientation choice.

Set \(s_q=\log q/(2\pi i)\). The calculation (33)--(34), with the continuation law (35), gives the exact frame relation

\[
u(q)=(I_4+s_qN_H)\widehat u(q),
\qquad \widehat u(q)\text{ holomorphic at }0,
\qquad \widehat u_0(0)\ne0.
\tag{36}
\]

The three coordinates with logarithmic terms have the same coefficient prescribed by (35); the preceding direct period calculation shows that removing those terms leaves holomorphic functions. This also supplies the cusp Hodge-extension assertion used in Section 2.

## 8. The rank-three cusp graph, with an explicit invertible projection

Fresh multiplication of the supplied rank-six matrices gives

\[
T_V=(BA)^{-1}=I_6+N_V,
\quad
N_V=\begin{pmatrix}
0&0&0&-1&1&-1\\
0&0&0&0&0&0\\
0&0&0&0&0&0\\
0&1&0&0&0&0\\
0&0&1&0&0&0\\
0&-1&1&0&0&0
\end{pmatrix}.
\tag{37}
\]

It satisfies \(N_V^2=0\) and has rank three. The correct cohomology coordinate morphism associated with the supplied homology basis matrix \(S\) is

\[
y_{\rm new}=S^t y_{\rm old}.
\]

The exact identities are

\[
S^t T_VS^{-t}=\begin{pmatrix}I_3&0\\I_3&I_3\end{pmatrix},
\qquad
S^te=(0,0,0,1,0,0)^t.
\tag{38}
\]

Use coordinates \((x,y)\in\mathbb C^3\oplus\mathbb C^3\) in (38). Thus \(N_V(x,y)=(0,x)\), and the invariant vector \(e\) is the first vector of the lower block.

For an arbitrary four-vector \(u=(u_0,u_1,u_2,u_3)^t\), form the five-by-four matrix whose columns are \(\pi(u\wedge e_j)\). It is

\[
U(u)=\begin{pmatrix}
u_1-u_2&-u_0&u_0&0\\
u_1-u_3&-u_0&0&u_0\\
u_1&-u_0-u_2&u_1&0\\
u_1&-u_0-u_3&0&u_1\\
u_1&-u_0&-u_3&u_2
\end{pmatrix}.
\tag{39}
\]

Apply \(S^t\) to the literal rank-six lifts \((0,U(u))^t\) and retain the first three rows. The resulting exact matrix is

\[
X_4(u)=\begin{pmatrix}
-u_1&u_0+u_2-u_3&-u_1+u_3&u_1-u_2\\
u_1-u_2&-u_0&u_0&0\\
u_1-u_3&-u_0&0&u_0
\end{pmatrix}.
\tag{40}
\]

Let \(X(u)\) be its columns numbered \(1,2,3\) in zero-based indexing. Direct determinant expansion gives

\[
\det X(u)=u_0^3.
\tag{41}
\]

Adding any multiple of \(e\) to a lift does not change these top three rows. Equations (36) and (41) therefore show that, in canonical extension frames, the projection of \(F_c\) to the first three coordinates is an isomorphism all the way to the cusp.

Choose the local frame of \(P\) given by the columns

\[
p_j(q)=\pi(\widehat u(q)\wedge e_j),\qquad j=1,2,3.
\]

They are independent by (41). Its canonical lifted frame under \(\sigma+ic\alpha e\), in (38) coordinates, has the actual block form

\[
\widehat M_c(q)=\begin{pmatrix}X(\widehat u(q))\\D_c(q)\end{pmatrix},
\tag{42}
\]

with both blocks holomorphic. The upper block is exactly (40), because the central coordinate of a lift is absent from it. Passing to flat frames applies the explicitly given nilpotent exponential:

\[
M_c(q)=\begin{pmatrix}I_3&0\\s_q I_3&I_3\end{pmatrix}
\widehat M_c(q)
=\begin{pmatrix}X\\s_qX+D_c\end{pmatrix}.
\]

Right multiplication by the specific invertible holomorphic matrix \(X^{-1}\) gives the frame

\[
\begin{pmatrix}I_3\\Z_c(q)\end{pmatrix},
\qquad
Z_c(q)=\frac{\log q}{2\pi i}I_3+C_c(q),
\qquad C_c(q)=D_c(q)X(\widehat u(q))^{-1}.
\tag{43}
\]

This is the asserted graph and its actual basis-change morphism. In the convention where the rows of a period matrix evaluate the three form vectors on the ordered homology basis given by $S$, the period matrix is $(I_3,Z_c^t)$; transposition therefore gives the same displayed logarithmic formula with correction $C_c^t$. Since \(\widehat u_0(0)\ne0\), the inverse matrix and \(D_c\) are holomorphic on a full disc; \(C_c\) is holomorphic there and bounded on a smaller closed disc.

The contraction in these graph coordinates can also be computed exactly from (39)--(40):

\[
\alpha(x)=a(q)x,
\qquad
a(q)=\left(1,
-1+\frac{2(\widehat u_1-\widehat u_3)}{\widehat u_0},
1-\frac{2(\widehat u_1-\widehat u_2)}{\widehat u_0}\right).
\tag{44}
\]

The differences and the first coordinate are unchanged by \(I+s_qN_H\), so this is also the formula in the flat Hodge coordinates. It is holomorphic and bounded at the cusp. The exact dependence of the correction on the real parameter is

\[
C_c(q)=C_0(q)+ic\,e_1a(q),
\tag{45}
\]

where \(e_1=(1,0,0)^t\) is the first vector of the lower three-dimensional block. This checks explicitly that the scalar modification preserves the bounded holomorphic correction.

## 9. The actual asymptotic of h and its attained global minimum

Write

\[
t=\operatorname{Im}s_q=-\frac{\log|q|}{2\pi}\longrightarrow+\infty,
\qquad w=\widehat u(q),\qquad a=w_0.
\]

The symbol \(a\) in this paragraph is the first coordinate, not the splitting constant in (20). From (35)--(36),

\[
u=w+s_q a d_0,
\quad
\beta=u^tJ\bar u=w^tJ\bar w-2it|a|^2.
\tag{46}
\]

The last equality follows directly from \(Jd_0=e_0\), \(d_0^tJ=-e_0^t\), and \(d_0^tJd_0=0\). It has the positive polarization sign \(i\beta=2t|a|^2+O(1)\). Since \(a(0)\ne0\), the denominator has magnitude bounded below by a positive constant times \(t\) for all sufficiently small \(|q|\), uniformly in its argument.

Let \(b_{ij}=u_i\bar u_j-u_j\bar u_i\). The top projection in (38) of \(\pi(u\wedge\bar u)\) is exactly

\[
\chi=(b_{01}-b_{12}+b_{13}-b_{23},\ b_{02}-b_{01},\ b_{03}-b_{01})^t.
\tag{47}
\]

Substitution of \(u=w+s_q a d_0\) gives

\[
\chi_1=\chi_1(w,\bar w)-2it|a|^2,
\qquad
\chi_2=\chi_2(w,\bar w),\qquad
\chi_3=\chi_3(w,\bar w).
\tag{48}
\]

The cancellation of the logarithmic terms in the last two components is literal subtraction of \(b_{0j}\); their cancellation in \(-b_{12}+b_{13}-b_{23}\) is the identity
\(-(w_2-w_1)+(w_3-w_1)-(w_3-w_2)=0\), together with its conjugate. All the terms involving only \(w\) are bounded.

The top three coordinates of \(j\) are therefore the real vector

\[
x(q)=\chi/\beta,
\qquad
x_1=1+O(t^{-1}),\qquad x_2=O(t^{-1}),\qquad x_3=O(t^{-1}).
\tag{49}
\]

Reality follows either by (25) or by the fact that every numerator and the denominator in these ratios is purely imaginary. All estimates are uniform around the cusp.

For the specified splitting \(\sigma\), its lift of \(j\) is the graph vector

\[
\sigma(j)=(x,(s_qI_3+C_0(q))x).
\]

By (26) and the position of \(e\) in (38), \(h\) is exactly the imaginary part of its first lower coordinate. The vector \(x\) is real, so (49) yields

\[
h=t x_1+\operatorname{Im}(C_0(q)x)_1
=-\frac{\log|q|}{2\pi}+O(1).
\tag{50}
\]

This proves both the direction and the coefficient of the cusp divergence. It uses the actual rank-three graph, the specific central vector, and the specified contraction. A generic assertion that some determinant diverges would not give (50).

The function \(h\) is continuous at every point of \(X\), including the finite-root points, and (50) tends uniformly to \(+\infty\) at its only missing point. Choose any point of \(X\) and then a small cusp disc on whose punctured part \(h\) exceeds its value at that point by one. The complement of this disc is compact and contains a point where the global minimum is attained. Thus

\[
h_{\min}=\min_X h\in\mathbb R.
\tag{51}
\]

The image is exactly \([h_{\min},\infty)\). It contains its minimum; (50) supplies values above every prescribed real bound; a path from a minimum point to a sufficiently near-cusp point supplies every intermediate value by continuity.

Combining this image calculation with (28) gives the exact global domain:

\[
\boxed{\;F_c\cap\overline{F_c}=0\text{ at every point of }X
\quad\Longleftrightarrow\quad c>-h_{\min}.\;}
\tag{52}
\]

At equality the failure occurs at a minimum point. For every smaller value of \(c\), the value \(-c\) belongs to the image of \(h\), and the corresponding point has a nonzero intersection. Every larger value gives \(h+c>0\) everywhere. This establishes the full domain, not only a sufficient half-line.

## 10. Finite-root extension and descent to orders five and four

At zero the supplied map is

\[
\lambda=s^8,\quad x=s^6X,\quad y=s^{15}Y,
\qquad Y^2=X^5+X+s^2.
\tag{53}
\]

The root fiber at \(s=0\) is smooth. The actual relative differential identities are

\[
s^9\frac{dx}{y}=\frac{dX}{Y},
\qquad
s^3\frac{x\,dx}{y}=\frac{X\,dX}{Y}.
\tag{54}
\]

They give nonzero holomorphic Hodge generators there. A deck generator \(\zeta=\exp(2\pi i/8)\) acts by

\[
(s,X,Y)\longmapsto(\zeta s,\zeta^{-6}X,\zeta^{-15}Y)
=(\zeta s,\zeta^2X,\zeta Y).
\tag{55}
\]

Its fourth power is \((s,X,Y)\mapsto(-s,X,-Y)\). On the central curve this is the hyperelliptic involution. It acts as \(-1\) on each of \(dX/Y\) and \(X\,dX/Y\), hence as \(-I\) on their Hodge space and its conjugate, and therefore on the entire four-dimensional cohomology. Since this finite central action is constant under equivariant good reduction, the kernel \(\mu_2\) acts as \(-I\) on the order-eight rank-four system. Its exterior square acts as the identity. The quotient maps (6)--(7) are equivariant under the same action, so \(W,P,\alpha\) descend through \(t=s^2\). The supplied rank-six action is \(B\), with \(B^4=I_6\), so the lift constructed on \(\mathfrak B\) and every \(F_c\) are already defined on the order-four chart.

At infinity the supplied map is

\[
\lambda=s^{-5},\quad x=s^{-4}X,\quad y=s^{-10}Y,
\qquad Y^2=X^5+sX+1.
\tag{56}
\]

The root fiber is smooth and

\[
s^{-6}\frac{dx}{y}=\frac{dX}{Y},
\qquad
s^{-2}\frac{x\,dx}{y}=\frac{X\,dX}{Y}.
\tag{57}
\]

For \(\zeta=\exp(2\pi i/5)\), the deck map is

\[
(s,X,Y)\longmapsto(\zeta s,\zeta^4X,Y).
\tag{58}
\]

The rank-six action is \(A\), with \(A^5=I_6\). All the maps used to construct \(F_c\) are equivariant, so the family extends holomorphically and descends on this order-five chart.

At both root centers, the smooth Hodge polarization gives \(i\beta>0\). The expressions (25)--(26) therefore remain real analytic there. Their deck invariance follows from the real integral monodromy, the equivariant lift, and the invariant real vector \(e\). Thus the root points occur in the minimum and domain arguments; no finite-root point has been silently omitted.

Finally P1.1 gives the exact orders of \(A\) and \(B\), also verified by their characteristic polynomials and powers. The rank-six system consequently descends with the stated finite orders five and four. The cusp formula (43) is the asserted period form before the subsequent toroidal filling; the cusp itself is the single point omitted from \(X\).

## 11. Conclusion and verification boundary

The constructed holomorphic maps (19) and (22), the scalar classification (20), the real analytic function (26), the actual cusp graph (43), the asymptotic (50), the attained minimum (51), the exact domain (52), and the root morphisms (53)--(58) prove every assertion in the supplied statement of P1.8. All substantive dependencies are either proved above, are literal data in the raw packet, or are the permitted P1.1/P1.4/P1.5/P1.7 inputs. P1.15 and P1.18 have not been used.

The companion quotient identities, the nilpotent rank and square, the corrected dual-coordinate conjugation, the determinant (41), and the contraction row (44) were computed freshly from the literal matrices by `fresh_matrices.py`. The first computation also preserved an initial incorrect basis-change convention as an unused printed check; its correction and nonuse are recorded in `exposure.md`. No external target proof has yet been opened at the time this derivation was written.
