# The unchanged native magnetic vector and its open-face spectral measure

8 September 2026. This note proves an all-volume spectral-probability limit
for the actual native magnetic leading face vector. The full finite-volume
amplitude, the original coordinate-dependent coefficients, every open boundary,
and the affine map to the first physical excitation coefficient are retained.
The calculation concerns a sequence of finite Taylor-coefficient matrices;
the coupling-dependent spectral transport is a separate calculation.

## 1. Original finite objects and the exact physical coefficient map

Fix an integer \(L\ge2\), put \(m=2L\), and use the original vertices
\(\{-L,\ldots,L\}^3\). A positively directed physical edge
\(e=(n,i)\) exists when both \(n\) and \(n+\mathbf e_i\) lie in this
set. A face \(p=(n;i,j)\), \(i<j\), has oriented edge word
\[
(n,i)^+(n+\mathbf e_i,j)^+(n+\mathbf e_j,i)^-(n,j)^-.
\tag{1.1}
\]
Thus its two plane base coordinates belong to \([-L,L-1]\cap\mathbb Z\),
and its normal base coordinate belongs to \([-L,L]\cap\mathbb Z\).
All \(M_L=3m^2(m+1)\) such faces are included. Distinct faces are adjacent
exactly when they share a physical edge. Write \(\mathsf A_L\) for the
unsigned adjacency matrix, \(d_p\) for its degrees, and
\[
\mathsf Q_L=\operatorname{diag}(d_p)+\mathsf A_L
  :\mathbb C^{\mathsf P_L}\longrightarrow\mathbb C^{\mathsf P_L}.
\tag{1.2}
\]
The inner product is counting measure, conjugate-linear in its first
argument. In particular no orientation sign is inserted in (1.2).

Each lattice edge belongs to at most four faces, and two distinct elementary
faces share at most one edge, so \(d_p\le12\). Directly expanding squares
gives
\[
\begin{split}
\langle x,\mathsf Q_Lx\rangle
 &=\sum_{\{p,q\}\text{ adjacent}}|x_p+x_q|^2,\\
\langle x,(24I-\mathsf Q_L)x\rangle
 &=\sum_{\{p,q\}\text{ adjacent}}|x_p-x_q|^2
   +2\sum_p(12-d_p)|x_p|^2.
\end{split}
\tag{1.3}
\]
Hence \(\operatorname{spec}(\mathsf Q_L)\subset[0,24]\). This proof
uses the unchanged open graph, including its degree-deficient faces.

For the original link variables \(U_e\in SU(2)\), retain
\[
\begin{gathered}
W_{n;ij}(U)=\operatorname{tr}
 \bigl(U_i(n)U_j(n+\mathbf e_i)
 U_i(n+\mathbf e_j)^{-1}U_j(n)^{-1}\bigr),\\
T_a=-i\sigma_a/2,\qquad
X_{e,a}f=\left.\frac{d}{dt}f(\ldots,e^{tT_a}U_e,\ldots)\right|_{t=0},
\qquad E_e=-\sum_{a=1}^3X_{e,a}^2,\\
H=\kappa H_0+b\sum_p(2-W_p)=\kappa K_\xi+2bM_LI,
\quad H_0=\sum_eE_e,\quad K_\xi=H_0-\xi\sum_pW_p,\\
\kappa=\frac{2g_{\rm YM}^2}{a},\qquad
b=\frac{1}{2g_{\rm YM}^2a},\qquad
\xi=\frac{b}{\kappa}=\frac1{4g_{\rm YM}^4},\qquad a>0,\ g_{\rm YM}>0.
\end{gathered}
\tag{1.4}
\]
Here \(a\) without a face subscript is the physical lattice spacing;
the face coefficient vector below is denoted \(\boldsymbol a_L\).
The original Lie metric has \(-\Delta_e^c=4E_e\). No factor in (1.4)
is changed. The gauge-invariant physical space is the invariant closed
subspace of product-Haar \(L^2(SU(2)^N)\). The operator and form domains
are its intersections with \(H^2\) and \(H^1\), respectively.

Define the linear face-to-state map
\[
\mathcal W_L:\mathbb C^{\mathsf P_L}\longrightarrow\mathcal H_{\rm phys},
\qquad \mathcal W_Lx=\sum_px_pW_p.
\tag{1.5}
\]
It is an isometry onto the free energy-three face space: for unequal faces
a link appearing in only one face changes the sign of the integrand under
\(U_e\mapsto-U_e\), proving orthogonality; for equal faces their holonomy
is Haar distributed and the fundamental character has squared Haar norm one.
Every face trace has fundamental Casimir \(3/4\) on its four links, giving
\(H_0\mathcal W_L=3\mathcal W_L\).

The original native translation has
\[
\Gamma=\sum_{e=(n,1)}n_2^2E_e,
\qquad h_1(n)=\exp(-\theta n_2H_c),\quad h_2=h_3=I,
\qquad H_c=i\sigma_3=-2T_3,
\tag{1.6}
\]
with \(\theta=2\pi a^2/D\),
\(D=L_Tq_T+6m_T^2>0\),
\(L_T=\operatorname{Im}\tau_T\),
\(q_T=-\operatorname{Im}\beta_T\), and
\(m_T=\operatorname{Im}\mu_T\). These are the same physical coordinates
and magnetic scale as in magnetic_translation_true_vacuum.md.
In first_physical_excitation_band.md the positive unit vacuum is proved to
satisfy \(\psi_\xi=1+\xi\sum_pW_p/3+O_{H^2,L}(\xi^2)\).
Applying the specified \(\Gamma:H^2\to L^2\), at fixed \(L\), gives
\[
\Gamma\psi_\xi=\xi\mathcal W_L\boldsymbol a_L+O_{L^2,L}(\xi^2),
\quad
\boxed{
a_{12}(n)=\frac{n_2^2+(n_2+1)^2}{4},\qquad
a_{13}(n)=\frac{n_2^2}{2},\qquad a_{23}(n)=0.}
\tag{1.7}
\]
Indeed a 12-face has direction-1 edge bases at heights \(n_2,n_2+1\),
a 13-face has two at height \(n_2\), and a 23-face has none; multiplying
the sum of squared heights by \((3/4)/3\) gives exactly (1.7).
The centered vector \((\Gamma-\langle\psi_\xi,\Gamma\psi_\xi\rangle)
\psi_\xi\) has the same leading coefficient because
\(\langle1,\mathcal W_L\boldsymbol a_L\rangle=0\) and its
centering scalar is \(O_L(\xi^2)\).

The same band source proves the true-vacuum second-order matrix
\[
\mathsf F_L=\frac7{15}I-\frac1{21}\mathsf Q_L.
\tag{1.8}
\]
That derivation retains the whole interaction, the shared-edge spin-zero
and spin-one virtual channels, and the vacuum subtraction. This note
calculates the spectral measure of (1.8) on precisely (1.7).

## 2. The unscaled spectral measure and the complete native amplitude

For a Borel set \(B\subset\mathbb R\), define
\[
\sigma_L(B)=\langle\boldsymbol a_L,
 \mathbf1_B(\mathsf Q_L)\boldsymbol a_L\rangle,
\qquad A_L=\sigma_L(\mathbb R)=\|\boldsymbol a_L\|^2,
\qquad \mu_L=\frac{\sigma_L}{A_L}.
\tag{2.1}
\]
The finite-dimensional spectral theorem defines the indicated orthogonal
projections. No unit-amplitude replacement of the native state occurs:
\(\sigma_L\) is kept, and only its explicitly named probability
\(\mu_L\) is divided by its actual nonzero mass.

Write \(I_L=[-L,L-1]\cap\mathbb Z\), and set
\[
s_r=\sum_{t\in I_L}t^r,
\qquad f(t)=\frac{t^2+(t+1)^2}{4}
 =\frac{t^2}{2}+\frac t2+\frac14.
\tag{2.2}
\]
Both displayed expressions define the same original coefficient. The exact
finite sums needed below are
\[
\begin{gathered}
s_0=2L,\quad s_1=-L,\quad s_2=\frac{L(2L^2+1)}3,
\quad s_3=-L^3,\quad
s_4=\frac{L(6L^4+10L^2-1)}{15},\\
\sum_{t\in I_L}f(t)^2=\frac{L(4L^4+1)}{40},\qquad
\sum_{t\in I_L}\left(\frac t2+\frac14\right)^2
 =\frac{L(4L^2-1)}{24}.
\end{gathered}
\tag{2.3}
\]
Here is an elementary verification of all sums. The odd sums pair \(t\)
with \(-t\) except for \(-L\), giving \(s_1,s_3\). For the even sums,
\(s_{2r}=L^{2r}+2\sum_{t=1}^{L-1}t^{2r}\). The polynomials
\(P_2(z)=z(z+1)(2z+1)/6\) and
\(P_4(z)=z(z+1)(2z+1)(3z^2+3z-1)/30\) obey
\(P_2(0)=P_4(0)=0\) and
\(P_r(z)-P_r(z-1)=z^r\) for \(r=2,4\), by multiplication.
Telescoping proves the two even sums. Expanding the retained polynomial
\(f^2=t^4/4+t^3/2+t^2/2+t/4+1/16\) and the last square in (2.3),
then substituting \(s_0,\ldots,s_4\), proves the remaining identities.

There are \(m(m+1)\) 12-faces at each permitted \(n_2\), and \(m^2\)
13-faces at each height from \(-L\) through \(L\), inclusive. Therefore
\[
\begin{split}
A_L
 &=m(m+1)\sum_{t=-L}^{L-1}
       \left(\frac{t^2+(t+1)^2}{4}\right)^2
   +\frac{m^2}{4}\sum_{t=-L}^{L}t^4\\
 &=\boxed{\frac45L^7+\frac65L^6+\frac23L^5
                  +\frac1{30}L^3+\frac1{20}L^2}.
\end{split}
\tag{2.4}
\]
In particular \(A_L>0\), \(A_L\ge4L^7/5\), and
\(A_L/L^7\longrightarrow4/5\). The boundary heights \(n_2=L\) and
\(n_3=L\) have been included in this mass.

## 3. Exact comparison in the same finite Hilbert space

Introduce a comparison vector solely for estimating (2.1). On the common
base cube \(C_L=I_L^3\), put
\[
g_L(n)=\mathbf1_{C_L}(n)\frac{n_2^2}{2},
\quad
\boldsymbol b_L(n;12)=g_L(n),\quad
\boldsymbol b_L(n;13)=g_L(n),\quad
\boldsymbol b_L(n;23)=0.
\tag{3.1}
\]
This defines an entry on every original face; it is zero on the remaining
faces. Set \(\boldsymbol r_L=\boldsymbol a_L-\boldsymbol b_L\).
Its complete nonzero-entry list is
\[
\begin{array}{c|c}
\text{original face and base}&r_L(n;ij)\\ \hline
n\in C_L,\ ij=12&n_2/2+1/4\\
ij=12,\ n_3=L,\ n_1,n_2\in I_L&f(n_2)\\
ij=13,\ n_2=L,\ n_1,n_3\in I_L&L^2/2.
\end{array}
\tag{3.2}
\]
Every other entry is zero. The three displayed sets are disjoint. No term
in (3.2) is deleted from the native vector or its measure.

Using (2.3) on these exact supports gives
\[
\begin{split}
B_L:=\|\boldsymbol b_L\|^2
 &=\frac{m^2s_4}{2}
   =\frac45L^7+\frac43L^5-\frac2{15}L^3,\\
R_L:=\|\boldsymbol r_L\|^2
 &=m^2\frac{L(4L^2-1)}{24}
   +m\frac{L(4L^4+1)}{40}+\frac{m^2L^4}{4}\\
 &=\frac65L^6+\frac23L^5-\frac16L^3+\frac1{20}L^2,\\
C_L^{\rm cross}:=\langle\boldsymbol b_L,\boldsymbol r_L\rangle
 &=m^2\left(\frac{s_3}{4}+\frac{s_2}{8}\right)
   =-\frac23L^5+\frac16L^3,\\
A_L&=B_L+2C_L^{\rm cross}+R_L.
\end{split}
\tag{3.3}
\]
The negative cross term is retained. These formulas give
\(B_L/A_L\to1\) and \(R_L/A_L\to0\). They follow from a literal
decomposition in \(\mathbb C^{\mathsf P_L}\), not a change of
coordinates, of face sets, or of physical background.

In the order \((12,13,23)\), use the two real plane vectors
\[
v_{24}=\left(\frac23,\frac23,\frac23\right),\qquad
v_{12}=\left(\frac13,\frac13,-\frac23\right),\qquad
(1,1,0)=v_{24}+v_{12}.
\tag{3.4}
\]
Their dot product is zero, and their squared lengths are \(4/3\) and
\(2/3\). Let \(\boldsymbol u_{\lambda,L}(n;\alpha)
=g_L(n)(v_\lambda)_\alpha\) on every original face. All three face
types exist on \(C_L\), so this is a literal orthogonal decomposition:
\[
\boldsymbol b_L=\boldsymbol u_{24,L}+\boldsymbol u_{12,L},\qquad
\langle\boldsymbol u_{24,L},\boldsymbol u_{12,L}\rangle=0,
\qquad
\|\boldsymbol u_{24,L}\|^2=\frac23B_L,\quad
\|\boldsymbol u_{12,L}\|^2=\frac13B_L.
\tag{3.5}
\]
These are not asserted to be finite-open-graph eigenvectors. The next
section bounds their exact eigen-equation errors.

## 4. Every shift and the finite-difference/open-boundary estimates

Independently define the infinite graph on
\(\mathbb Z^3\times\{12,13,23\}\) by the same physical-edge sharing
rule. Its operator on counting-measure
\(\ell^2(\mathbb Z^3;\mathbb C^3)\) is
\(\mathsf Q_\infty=12I+\mathsf A_\infty\). Within plane \(ij\),
the neighbors have bases \(n\pm\mathbf e_i,n\pm\mathbf e_j\).
For the distinct planes, the entire list is
\[
\begin{array}{c|c|c}
\text{source}&\text{target}&\text{target base, }a,b\in\{0,1\}\\ \hline
12&13&n+a\mathbf e_2-b\mathbf e_3\\
12&23&n+a\mathbf e_1-b\mathbf e_3\\
13&23&n+a\mathbf e_1-b\mathbf e_2.
\end{array}
\tag{4.1}
\]
The reverse list has the negative offsets. To prove this directly, two
faces sharing direction \(i\) have their two direction-\(i\) edges at
their respective base and base plus their other plane direction. Equating
these two possible physical-edge bases gives exactly the four offsets
in each row. The inverse traversals in (1.1) change no physical-edge
equality. There are four coplanar neighbors and eight cross-plane
neighbors, all distinct, yielding degree twelve.

Let \(J_L\) extend a face vector by zero to this infinite counting
space. Since the original graph is its induced subgraph,
\[
J_L^*\mathsf Q_\infty J_L=12I+\mathsf A_L,
\qquad
\boxed{\mathsf Q_L=J_L^*\mathsf Q_\infty J_L-\mathsf D_L},
\quad \mathsf D_L=\operatorname{diag}(12-d_p).
\tag{4.2}
\]
Both maps in (4.2) have the displayed original domains, and \(J_L\)
is an isometry. The nonzero boundary matrix \(\mathsf D_L\) is kept.

For the zero-extended scalar \(g_L\) in (3.1) define
\[
\mathcal D_{i,L}=\sum_{n\in\mathbb Z^3}
 |g_L(n+\mathbf e_i)-g_L(n)|^2.
\tag{4.3}
\]
Separation of the three finite coordinate sums gives exactly
\[
\begin{split}
\mathcal D_{1,L}=\mathcal D_{3,L}&=\frac m2s_4,\\
\mathcal D_{2,L}
 &=m^2\left[\frac{L^4+(L-1)^4}{4}
       +\sum_{t=-L}^{L-2}\left(t+\frac12\right)^2\right],\\
\sum_{t=-L}^{L-2}\left(t+\frac12\right)^2
 &=\frac{8L^3-12L^2+10L-3}{12},\\
\mathcal D_L^{\rm sum}
 :=\mathcal D_{1,L}+\mathcal D_{2,L}+\mathcal D_{3,L}
 &=\frac{14}{5}L^6-\frac43L^5+\frac{10}{3}L^4
                         -\frac23L^3-\frac2{15}L^2.
\end{split}
\tag{4.4}
\]
For directions 1 and 3 the only changes are the two boundary planes,
each contributing \(ms_4/4\). In direction 2 the lower and upper jumps
contribute \(L^4/4\) and \((L-1)^4/4\); each internal difference is
\(((t+1)^2-t^2)/2=t+1/2\). Expanding the last finite sum using (2.3)
with its upper endpoint removed proves its displayed polynomial and
then the last line. Thus the jump terms have not been replaced by
interior derivatives.

For a constant plane vector \(v\in\mathbb C^3\) and any eigenpair
\[
(12I+4\mathbf1\mathbf1^T)v=\lambda v,
\tag{4.5}
\]
the residual of \(g_Lv\) in the infinite graph has, in component
\(\alpha\) and at base \(n\), precisely
\[
\bigl((\mathsf Q_\infty-\lambda)(g_Lv)\bigr)_\alpha(n)
 =\sum_{\beta,\delta\in\mathsf T_{\alpha\beta}}
 v_\beta\bigl(g_L(n+\delta)-g_L(n)\bigr).
\tag{4.6}
\]
There are twelve terms, with \(\mathsf T_{\alpha\alpha}\) the four
coplanar shifts and other sets given by (4.1). Indeed the removed
zero-shift matrix is diagonal 16 and off-diagonal 4, precisely the
matrix in (4.5). The two vectors (3.4) satisfy (4.5) at 24 and 12:
their component sums are 2 and 0, respectively.

Translation invariance of counting norm and
\(\|x+y\|^2\le2\|x\|^2+2\|y\|^2\) imply
\[
\sum_n|g_L(n+\mathbf e_i-\mathbf e_j)-g_L(n)|^2
 \le2(\mathcal D_{i,L}+\mathcal D_{j,L}).
\tag{4.7}
\]
Split the change into its two successive coordinate shifts to prove
this, and use translation isometry for each summand. The same bound
holds with either sign or with the entire offset reversed.

Apply Cauchy--Schwarz to the twelve terms in (4.6), sum over \(n,\alpha\),
and collect each fixed target type \(\beta=ij\), with normal direction
\(k\). The four same-plane shifts contribute exactly
\(2(\mathcal D_i+\mathcal D_j)\). The four shifts to one other plane
contribute at most \(3(\mathcal D_i+\mathcal D_k)\) and those to the
remaining plane at most \(3(\mathcal D_j+\mathcal D_k)\): their terms
are a zero shift, two single shifts, and one double shift bounded by
(4.7). Consequently the coefficient for \(|v_\beta|^2\) is at most
\[
12[5(\mathcal D_i+\mathcal D_j)+6\mathcal D_k]
 \le72\mathcal D_L^{\rm sum}.
\]
We have proved the explicit infinite residual estimate
\[
\| (\mathsf Q_\infty-\lambda)(g_Lv)\|^2
 \le72\|v\|^2\mathcal D_L^{\rm sum}.
\tag{4.8}
\]

Here is the complete boundary correction on the original support. Define
\(\beta_L(t)=\mathbf1_{\{t=-L\}}+\mathbf1_{\{t=L-1\}}\) for
\(t\in I_L\). A face \(ij\) of base \(n\in C_L\) and normal
direction \(k\) has
\[
12-d_{n;ij}=\beta_L(n_i)+\beta_L(n_j)+4\mathbf1_{\{n_k=-L\}}.
\tag{4.9}
\]
For proof, each of its four edges has two transverse extension
directions, each with two incident faces except that a transverse
coordinate equal to \(-L\) or \(L\) permits only one. Summing the
three other incident faces over the four edges gives degree twelve,
minus one for either extreme plane base and minus four when the normal
coordinate is an outer boundary. On the common cube the only outer
normal boundary is \(-L\), giving (4.9). On the rest of the original
face set the same formula uses
\(4\mathbf1_{\{n_k\in\{-L,L\}\}}\); our comparison vector is zero
there, while its native residual is already retained in (3.2).

For any \(v\), the exact squared norm of this boundary error is
\[
\mathcal E_L(v):=\|\mathsf D_L(g_Lv)\|^2
 =\sum_{ij}|v_{ij}|^2\sum_{n\in C_L}\frac{n_2^4}{4}
  [\beta_L(n_i)+\beta_L(n_j)+4\mathbf1_{\{n_k=-L\}}]^2.
\tag{4.10}
\]
In each plane type the nonzero summands lie in at most five coordinate
planes of \(m^2\) points each. The bracket is at most 6 and
\(n_2^4/4\le L^4/4\). Counting overlaps more than once is an upper
bound, so
\[
\mathcal E_L(v)\le45m^2L^4\|v\|^2.
\tag{4.11}
\]
Equations (4.2), (4.8), and the triangle inequality, with every quantity
in the same original counting norm, prove
\[
\begin{gathered}
\varepsilon_{\lambda,L}
 :=\| (\mathsf Q_L-\lambda I)\boldsymbol u_{\lambda,L}\|,\\
\boxed{
\varepsilon_{\lambda,L}
 \le\sqrt{72\|v_\lambda\|^2\mathcal D_L^{\rm sum}}
          +\sqrt{\mathcal E_L(v_\lambda)}
 \le\|v_\lambda\|\mathcal K_L,}\qquad
\mathcal K_L=\sqrt{72\mathcal D_L^{\rm sum}}+\sqrt{45m^2L^4},\\
\varepsilon_{24,L}+\varepsilon_{12,L}
 \le\frac{2+\sqrt2}{\sqrt3}\mathcal K_L.
\end{gathered}
\tag{4.12}
\]
Since (4.4) gives \(\mathcal D_L^{\rm sum}=O(L^6)\), all these
residual bounds are \(O(L^3)\); their squared norms are small relative
to \(A_L\), which has order \(L^7\). The explicit formulas, rather
than this order notation, are the finite-volume estimates used below.

## 5. Quantitative spectral probability limit for the actual native vector

For a complex Lipschitz function \(h:[0,24]\to\mathbb C\), write
\(\|h\|_\infty\) and \(\operatorname{Lip}(h)\) for its supremum
norm and Lipschitz constant. Define the explicit finite numbers
\[
\begin{split}
\mathcal N_L
 &=\frac{(\sqrt{A_L}+\sqrt{B_L})\sqrt{R_L}+|B_L-A_L|}{A_L},\\
\mathcal T_L
 &=\frac{\sqrt{B_L}}{A_L}\,
           \frac{2+\sqrt2}{\sqrt3}\mathcal K_L.
\end{split}
\tag{5.1}
\]
All symbols on the right sides were calculated above without asymptotic
replacement. We claim, for every \(L\ge2\),
\[
\boxed{
\left|\int h(q)\,d\mu_L(q)
       -\frac23h(24)-\frac13h(12)\right|
 \le\mathcal N_L\|h\|_\infty
       +\mathcal T_L\operatorname{Lip}(h).}
\tag{5.2}
\]

First, by (3.2), functional calculus, and Cauchy--Schwarz,
\[
\left|\langle\boldsymbol a_L,h(\mathsf Q_L)\boldsymbol a_L\rangle
       -\langle\boldsymbol b_L,h(\mathsf Q_L)\boldsymbol b_L\rangle\right|
 \le\|h\|_\infty(\sqrt{A_L}+\sqrt{B_L})\sqrt{R_L}.
\tag{5.3}
\]
For example expand the difference as
\(\langle\boldsymbol r_L,h(\mathsf Q_L)\boldsymbol a_L\rangle
+\langle\boldsymbol b_L,h(\mathsf Q_L)\boldsymbol r_L\rangle\),
and apply the operator-norm bound \(\|h(\mathsf Q_L)\|\le\|h\|_\infty\).
Second, the finite spectral theorem and the scalar Lipschitz inequality
give, for either \(\lambda=24,12\),
\[
\|[h(\mathsf Q_L)-h(\lambda)I]\boldsymbol u_{\lambda,L}\|^2
 =\int|h(q)-h(\lambda)|^2
       d\langle\boldsymbol u_{\lambda,L},
         \mathbf1_{dq}(\mathsf Q_L)\boldsymbol u_{\lambda,L}\rangle
 \le\operatorname{Lip}(h)^2\varepsilon_{\lambda,L}^2.
\tag{5.4}
\]
Use \(\boldsymbol b_L=\boldsymbol u_{24,L}+\boldsymbol u_{12,L}\)
and their exact orthogonality to obtain
\[
\begin{split}
&\left|\langle\boldsymbol b_L,h(\mathsf Q_L)\boldsymbol b_L\rangle
       -B_L\left[\frac23h(24)+\frac13h(12)\right]\right|\\
&\hspace{15mm}\le\sqrt{B_L}\operatorname{Lip}(h)
   (\varepsilon_{24,L}+\varepsilon_{12,L}).
\end{split}
\tag{5.5}
\]
Indeed the difference equals the inner product of \(\boldsymbol b_L\)
with the sum of the two error vectors in (5.4). This step bounds the
actual spectral cross terms; it does not assume that distinct approximate
eigenvectors have orthogonal spectral projections. Combine (5.3), (5.5),
(4.12), and \(|\frac23h(24)+\frac13h(12)|\le\|h\|_\infty\),
then divide by the actual \(A_L\), proving (5.2).

Equations (2.4), (3.3), and (4.4) show directly
\(\mathcal N_L=O(L^{-1/2})\) and \(\mathcal T_L=O(L^{-1/2})\).
In particular the right side of (5.2) tends to zero for each Lipschitz
\(h\). To pass to all continuous \(h\), partition the compact interval
\([0,24]\) into sufficiently short intervals and use linear interpolation
of its endpoint values. Uniform continuity makes the resulting Lipschitz
function \(h_\eta\) satisfy \(\|h-h_\eta\|_\infty\le\eta\).
Both measures in (5.2) have total mass one, so the substitution error is
at most \(2\eta\). First let \(L\to\infty\), then \(\eta\to0\).
This proves
\[
\boxed{\mu_L\ \Longrightarrow\ \frac23\delta_{24}+\frac13\delta_{12}.}
\tag{5.6}
\]
The unscaled statement is simultaneously retained: (5.3)--(5.5) prove
\[
\begin{split}
\left|\int h\,d\sigma_L
       -A_L\left[\frac23h(24)+\frac13h(12)\right]\right|
 &\le A_L\bigl(\mathcal N_L\|h\|_\infty
                +\mathcal T_L\operatorname{Lip}(h)\bigr),\\
\boxed{L^{-7}\sigma_L\ \Longrightarrow\
              \frac8{15}\delta_{24}+\frac4{15}\delta_{12}.}
\end{split}
\tag{5.7}
\]
The second convergence is of finite measures, whose total masses tend
to \(4/5\); it follows by multiplying (5.6) by \(A_L/L^7\).
The original \(\sigma_L\) itself has diverging total mass \(A_L\),
which remains exactly (2.4).

There is also a direct concentration estimate that does not merely
test fixed functions. Put
\(p(q)=(q-12)(q-24)\). On \([0,24]\),
\(|q-12|\le12\), \(|q-24|\le24\), and \(|p(q)|\le288\)
(the quadratic has its interior extremum \(-36\) at 18 and endpoint
values 288 and 0). By the decomposition (3.2),(3.5),
\[
\|p(\mathsf Q_L)\boldsymbol a_L\|
 \le12\varepsilon_{24,L}+24\varepsilon_{12,L}+288\sqrt{R_L}.
\tag{5.8}
\]
For \(0<\delta\le6\), any point of \([0,24]\) at distance at least
\(\delta\) from both 12 and 24 has
\(|p(q)|\ge\delta(12-\delta)\): below 12 the lower bound is the
larger \(\delta(12+\delta)\), and between the two roots the product
\((q-12)(24-q)\) attains its minimum on the permitted interval at
either endpoint. Spectral integration of (5.8) therefore yields
\[
\boxed{
\mu_L\{q:\min(|q-12|,|q-24|)\ge\delta\}
 \le\frac{[12\varepsilon_{24,L}+24\varepsilon_{12,L}
                    +288\sqrt{R_L}]^2}
             {A_L\delta^2(12-\delta)^2}.}
\tag{5.9}
\]
The residuals on the right may be replaced by their explicit bounds
(4.12). For fixed \(\delta\), the displayed upper bound is \(O(L^{-1})\).
The limit weights follow from (5.2), not from concentration alone.

## 6. Exact pushforward to the band coefficient and original energy units

Let \(\phi(q)=7/15-q/21\). Since (1.8) is exactly the affine functional
calculus of (1.2), their spectral projections obey
\[
\mathbf1_B(\mathsf F_L)=\mathbf1_{\phi^{-1}(B)}(\mathsf Q_L).
\tag{6.1}
\]
One proof is to choose an orthonormal eigenbasis of the real symmetric
\(\mathsf Q_L\); each vector with eigenvalue \(q\) has the same vector
with eigenvalue \(\phi(q)\) for \(\mathsf F_L\). The two indicator
operators therefore agree on a basis. The exact unscaled and probability
measures of \(\mathsf F_L\) on the unchanged \(\boldsymbol a_L\) are
\[
\sigma_L^F=\phi_*\sigma_L,\qquad
\mu_L^F=\phi_*\mu_L,\qquad \sigma_L^F(\mathbb R)=A_L.
\tag{6.2}
\]
In particular
\[
\boxed{\begin{split}
\mu_L^F&\Longrightarrow
 \frac23\delta_{-71/105}+\frac13\delta_{-11/105},\\
L^{-7}\sigma_L^F&\Longrightarrow
 \frac8{15}\delta_{-71/105}+\frac4{15}\delta_{-11/105}.
\end{split}}
\tag{6.3}
\]
For a Lipschitz test function on \([-71/105,7/15]\), (5.2) applies
to its composition with \(\phi\), with Lipschitz constant divided
by 21. Thus (6.3) includes an explicit finite-volume error bound.

The support bound (1.3) permits polynomial test functions, giving
\[
\begin{gathered}
\lim_L\frac{\langle\boldsymbol a_L,\mathsf Q_L\boldsymbol a_L\rangle}{A_L}
 =\frac23\,24+\frac13\,12=20,\\
\lim_L\frac{\|\mathsf Q_L\boldsymbol a_L\|^2}{A_L}
 =\frac23\,24^2+\frac13\,12^2=432,\\
\lim_L\operatorname{Var}_{\mu_L}(q)=432-20^2=32,\\
\lim_L\frac{\langle\boldsymbol a_L,\mathsf F_L\boldsymbol a_L\rangle}{A_L}
 =\frac7{15}-\frac{20}{21}=-\frac{17}{35},\qquad
\lim_L\operatorname{Var}_{\mu_L^F}(F)=\frac{32}{441}.
\end{gathered}
\tag{6.4}
\]
The nonzero limiting variance proves that the native vector's coefficient
measure does not concentrate at the lowest coefficient alone.

For the original energy coefficients, a coefficient \(q\) corresponds to
\[
\kappa\bigl(3+\xi^2\phi(q)\bigr)
 =\frac{6g_{\rm YM}^2}{a}
       +\frac{\phi(q)}{8g_{\rm YM}^6a}.
\tag{6.5}
\]
This identity preserves all energy scales. Its two limiting coefficient
values insert \(-71/105\) and \(-11/105\), respectively, in (6.5).
Equation (6.5) is the Taylor polynomial, not the full interacting energy.
The band source supplies the exact transported finite matrix
\[
V_\xi^*(H-\mathcal E(\xi)I)V_\xi
 =\kappa\left(3I+\xi^2\mathsf F_L+\mathcal R_{L,\xi}\right),
\quad
\|\mathcal R_{L,\xi}\|
 \le\frac73\left(\frac{64M_L}{3}\right)^4|\xi|^4,
\quad |\xi|\le\frac3{128M_L}.
\tag{6.6}
\]
Here \(V_\xi\) is the exact isometry from the free face eigenspace to
the true interacting first cluster, and the left side acts on that free
space using (1.5). Its full vacuum energy \(\mathcal E(\xi)\) includes
the original scalar \(2bM_L\); subtracting the same scalar from both
energies explains its cancellation in (6.6). The norm and coupling
restriction in (6.6) are stated, not replaced by a volume-uniform error.
All nonlinear Wilson terms remain in \(H\) and in its exact spectral
transport; none is estimated by setting a plaquette to its classical
value. The native centered magnetic vector and its projection through
\(V_\xi\) have their own coupling-dependent dressing, treated in the
companion transport calculation.

The leading-vector amplitude also transfers exactly under (1.5):
\[
\|\xi\mathcal W_L\boldsymbol a_L\|^2=\xi^2A_L,
\qquad
\left\| -\frac23\theta^2\xi\mathcal W_L\boldsymbol a_L\right\|^2
 =\frac49\theta^4\xi^2A_L
 =\frac{4\pi^4a^8}{9D^4g_{\rm YM}^8}\,A_L.
\tag{6.7}
\]
The scalar on the right uses the original
\(\theta=2\pi a^2/D\) and \(\xi=1/(4g_{\rm YM}^4)\) without changing
either. The unscaled graph and coefficient measures of these two
specified leading vectors are respectively \(\xi^2\sigma_L\),
\(\xi^2\sigma_L^F\), and \(4\theta^4\xi^2/9\) times those original
\(\sigma_L,\sigma_L^F\). The associated probabilities, when these
scalars are nonzero, are exactly \(\mu_L,\mu_L^F\).
For the actual centered translated state, the source identity is
\(\chi_\theta=-2\theta^2
(\Gamma-\langle\psi_\xi,\Gamma\psi_\xi\rangle)\psi_\xi/3
+O_{H^1,L,\xi}(\theta^4)\). Together with (1.7) this gives
\[
\chi_\theta=-\frac23\theta^2
 [\xi\mathcal W_L\boldsymbol a_L+O_{L^2,L}(\xi^2)]
 +O_{L^2,L,\xi}(\theta^4).
\tag{6.8}
\]
The first remainder is the fixed-volume small-coupling remainder for the
centered generator vector; the second is the fixed-volume, fixed-coupling
small-angle remainder. Their dependencies are retained. Equations
(6.7)--(6.8) specify exactly which leading coefficient the measure
calculation addresses and retain the errors for the actual state.

Thus (6.1)--(6.6) give an exact map from this face-measure limit to the
specified physical band coefficient, while retaining the finite-volume
remainder. Neither (5.6) nor (6.3) takes a fixed positive coupling to
infinite volume, takes the lattice spacing to zero, or constructs the
interacting physical continuum spectral measure.

## 7. Reproducibility and calculation record

The companion check_native_magnetic_band_measure.py uses only the Python
standard library and exact integer/rational arithmetic. It independently
enumerates every original face and every physical-edge star for
\(L=2,3,4,5,6\), constructs the open adjacency, and verifies (1.7),
(2.3)--(2.4), every entry of (3.2), all norms and the negative cross term
in (3.3), the orthogonal weights (3.5), every finite difference (4.4),
the boundary identity (4.9), the exact boundary sum (4.10), and rational
squared versions of the residual bounds. It checks the native graph
moments directly and verifies the rational maps and limiting moments
in (6.3)--(6.4). Polynomial identities are additionally checked by exact
coefficient operations or by their exact finite-sum difference identities;
no floating eigenvalue calculation is used as a proof of the limit.

The checker was executed successfully with
`python agent_work/ym_gap_primary_20260908/wilson_variation/check_native_magnetic_band_measure.py`.
Its verified native amplitudes were \(201,11151/4,18708,333355/4,285129\)
for \(L=2,3,4,5,6\), respectively; the corresponding full face counts
were \(240,756,1728,3300,5616\). All polynomial, physical-edge,
finite-difference, boundary, and residual identities passed.

Task continuity: the existing root logbook and user-input provenance files
were found before writing; this owned calculation had no preexisting
native_magnetic_band_measure.md or checker to overwrite. The three source
notes named in the task were inspected, and all original native coefficients
were retained. The auxiliary common-cube vector was introduced only with
its full residual and cross term. The candidate two-atom probability was
then proved from the finite open graph, rather than assumed from its bulk
symbol. No new agent, remote write, PDF, Lean process, or spectral numerical
diagonalization is part of this bounded calculation.
