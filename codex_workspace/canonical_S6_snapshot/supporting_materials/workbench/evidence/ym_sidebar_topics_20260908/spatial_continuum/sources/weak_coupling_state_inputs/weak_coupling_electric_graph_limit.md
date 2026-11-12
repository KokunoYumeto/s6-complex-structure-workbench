# Full-vacuum potential moments and the electric-state graph limit

8 September 2026. All statements through Section 6 concern a fixed original
open box L>=2 and fixed spacing a>0, at small positive g. The nonlinear
Wilson operator, actual vacuum, full gauge action, raw state norms and
all physical factors are retained. We derive the missing derivative-state
map from the vacuum equation, not from strong vacuum convergence alone.

## 1. Exact original operator and potential-gradient inequality

Use the finite-box definitions and exact coordinate maps of the companion
manuscripts *The original finite-box SU(2) Hamiltonian at small positive
coupling* and *Actual weak-coupling vacuum, observable and spectral maps*.
In particular
\[
 H=\kappa H_0+bW,\quad H_0=\sum_eE_e,
 \quad \kappa=2g^2/a,\quad b=1/(2g^2a),
 \quad W=\sum_p w_p,\quad w_p=2-\operatorname{tr}U_p,
 \quad E_e=-\sum_{\alpha=1}^3X_{e,\alpha}^2.                 \tag{1}
\]
The anti-Hermitian generators are \(T_\alpha=-i\sigma_\alpha/2\).
All positive contained links and all contained faces are included. The
strictly positive unit vacuum is \(\psi\), with actual energy
\(\mathcal E\), so \(H\psi=\mathcal E\psi\). The scalar
\(2b|P|\) is part of bW and is not removed in this equation.

For any face p and any of its four links e,
\[
 \sum_\alpha|X_{e,\alpha}w_p|^2=w_p-w_p^2/4\le w_p.       \tag{2}
\]
To check every factor, hold the other links fixed. Its oriented face word
is a Haar translate of U_e or U_e^{-1}; conjugations rotate the three
generators orthogonally. Write the resulting SU(2) element as
\(u_0I+i\boldsymbol u\cdot\boldsymbol\sigma\), with
\(u_0^2+|\boldsymbol u|^2=1\). Its trace is 2u_0, and
\(\operatorname{tr}(T_\alpha U)=u_\alpha\).
The three squared derivatives sum to \(|\boldsymbol u|^2\).
Since \(w_p=2-2u_0\), this is exactly (2). The inverse-link case
has the same sum by inversion and bi-invariance, not a changed orientation.

Let \(r_e\) be the actual number of faces incident to e; on this open
box \(r_e\le4\), including every boundary edge. Cauchy--Schwarz in
that finite incident set, followed by summation in e, gives
\[
 \sum_{e,\alpha}|X_{e,\alpha}W|^2
  \le\sum_e r_e\sum_{p\ni e}\sum_\alpha|X_{e,\alpha}w_p|^2
  \le16W.                                                   \tag{3}
\]
Thus the constant 16 is independent of the box; W itself still contains
every face. In particular this is not a local replacement potential.

## 2. All potential moments from the actual vacuum equation

Write \(M_k=\int W^k\psi^2\,dU\), with \(M_0=1\).
For every integer k>=1,
\[
 \boxed{bM_{k+1}\le\mathcal E M_k+4\kappa k^2M_{k-1},
 \qquad M_1\le\mathcal E/b.}                              \tag{4}
\]
Here is a proof that retains the derivative terms. The exact ground-state
identity for a real smooth f is
\[
 q_H[f\psi]-\mathcal E\|f\psi\|^2
   =\kappa\int\psi^2\sum_{e,\alpha}|X_{e,\alpha}f|^2dU.
                                                               \tag{5}
\]
It follows by differentiating the product twice in (1), integrating with
the original Haar measure, and substituting the full eigen-equation.
The kinetic term of \(q_H[f\psi]\) is nonnegative. For k>=2 take
\(f=W^{k/2}\), or its smooth positive regularization if needed.
Equation (3) bounds the right side by
\(4\kappa k^2M_{k-1}\); the left side is at least
\(bM_{k+1}-\mathcal E M_k\), proving (4).
For k=1 use \(f=(W+\epsilon)^{1/2}\). Its squared gradient is
at most \(4W/(W+\epsilon)\le4\). In (5) the lower bound is
\(b(M_2+\epsilon M_1)-\mathcal E(M_1+\epsilon)\).
Letting epsilon decrease to zero proves the same formula for k=1.
For higher odd k the identical regularization and dominated convergence
on the compact group justify all powers. The bound for M1 follows
directly from \(bW\le H\) in quadratic forms on \(\psi\).

The companion finite-box eigenvalue theorem gives a finite K such that
\(\mathcal E\le K\) for sufficiently small positive g, with L,a fixed.
No uniformity in L is assumed. Substituting the original coefficients
into (4) gives the exact scaled recursion
\[
 \frac{M_{k+1}}{g^{2k+2}}
 \le 2aK\frac{M_k}{g^{2k}}+
                 16k^2\frac{M_{k-1}}{g^{2k-2}}.             \tag{6}
\]
Define explicitly \(B_0=1\), \(B_1=2aK\), and
\(B_{k+1}=2aK B_k+16k^2 B_{k-1}\). Induction proves
\(M_k\le B_k g^{2k}\) for every fixed k. The recursion keeps the
full vacuum energy estimate and every original g,a factor. For example,
\(B_2=(2aK)^2+16\) and
\(B_3=(2aK)^3+80(2aK)\). Only fixed-box boundedness of K is used.

## 3. Potential-weighted strong convergence and the total electric graph

Retain the exact full-measure map \(\mathcal B_g\), matrices T,G,C,
and Gaussian \(\Phi_0\) from the state companion. Put
\[
 V_2(x)=\tfrac14\sum_\alpha\|Cx^\alpha\|^2,
 \qquad D=-\sum_{\alpha,c,d}G_{cd}
                         \partial_{x_c^\alpha}\partial_{x_d^\alpha}.
                                                               \tag{7}
\]
The companion proves \(\mathcal B_g\psi\to\Phi_0\) strongly.
We strengthen it to
\[
 \mathcal B_g\bigl((W/g^2)\psi\bigr)\to V_2\Phi_0,
 \qquad
 \mathcal B_g(g^2H_0\psi)\to D\Phi_0
                \quad\hbox{strongly in }L^2.                \tag{8}
\]
The first convergence is local by the exact Taylor limit W(gx)/g²→V2
and the strong vacuum convergence. To prove that no weighted tail is
lost, choose the same fixed radius rho as in the companion: W(y)>=c|y|²
inside it and W>=c_rho outside it. On the subset |x|>R with
|gx|<rho, the variable t=W/g² is at least cR². Outside the rho
neighborhood it is at least c_rho/g². Therefore (6) at k=3 gives
\[
 \int_{|x|>R}|\mathcal B_g((W/g^2)\psi)|^2dx
  \le \frac{B_3}{cR^2}+\frac{g^2B_3}{c_\rho}.             \tag{9}
\]
The limiting polynomial times Gaussian has an integrable squared tail.
Let R tend to infinity after the local convergence to obtain the first
part of (8).

For the second, the actual eigen-equation gives the exact identity
\[
 g^2H_0\psi=\frac{a\mathcal E}{2}\psi-\frac{W}{4g^2}\psi.
                                                               \tag{10}
\]
The first limit in (8) and \(\mathcal E\to\mu_0\) show that its
image tends to \((a\mu_0/2-V_2/4)\Phi_0\). The exact oscillator
equation \([(2/a)D+V_2/(2a)]\Phi_0=\mu_0\Phi_0\) identifies
this as DΦ0. This proves (8) from full potential moments, not merely
from convergence in L2 of the vacuum.

## 4. Every retained electric weight and its graph limit

For any fixed real edge weights w define
\[
 \Gamma_w=\sum_e w_eE_e,\qquad
 G_w=T\operatorname{diag}(w)T^*,\qquad
 D_w=-\sum_{\alpha,c,d}(G_w)_{cd}
                        \partial_{x_c^\alpha}\partial_{x_d^\alpha}.
                                                               \tag{11}
\]
No positivity of w is needed. The electric operators on distinct links
strongly commute by their product-group spectral decomposition. Their
eigenvalues are nonnegative, so on \(\operatorname{Dom}H_0\)
\[
 \|\Gamma_w F\|\le\|w\|_\infty\|H_0F\|.                \tag{12}
\]
Their individual Casimir spectra and all signs of w remain in this
inequality. Restriction to the physical space is valid because every
E_e commutes with the full vertex gauge projection.

We claim the actual graph limit
\[
 \boxed{\mathcal B_g(g^2\Gamma_w\psi)\longrightarrow D_w\Phi_0.}
                                                               \tag{13}
\]
For a smooth invariant compactly supported u(x), its reciprocal map
\(\mathcal B_g^*u\) is a smooth physical function supported in the
logarithm chart for all sufficiently small g. Differentiating the exact
tree fields and density gives
\[
 \mathcal B_g(g^2H_0\mathcal B_g^*u)\to Du,
 \qquad
 \mathcal B_g(g^2\Gamma_w\mathcal B_g^*u)\to D_wu          \tag{14}
\]
strongly, since every coefficient and derivative converges uniformly on
the fixed compact support. In detail the principal coefficients of gX_e
are its derivative columns of T at y=0; derivatives of these coefficients
and of the Haar density each carry an extra factor g. Summing their
exact squared fields gives G and Gw. The lower-order terms tend to zero
on this compact support, not by deletion from the original operator.

Choose smooth invariant radial cutoffs u_R=χ_RΦ0. Their Gaussian decay
gives \(u_R\to\Phi_0\) in the graph norms of both constant-coefficient
operators D and Dw. The first limit in (14), combined with (8), shows
\[
 \lim_{g\to0}\|g^2H_0(\psi-\mathcal B_g^*u_R)\|
        =\|D(\Phi_0-u_R)\|.                                \tag{15}
\]
Apply (12) to the difference, then use the second limit in (14).
The limsup error in (13) is at most
\(\|w\|_\infty\|D(\Phi_0-u_R)\|+
\|D_w(u_R-\Phi_0)\|\), which tends to zero as R grows. This proves
(13). Every limit here fixes L,a,w before g tends to zero.

Inner products with the strongly converging unit vacua now prove
\[
 g^2\langle\Gamma_w\rangle_\psi\to
          \langle\Phi_0,D_w\Phi_0\rangle,
\quad
 \mathcal B_g\bigl(g^2(\Gamma_w-\langle\Gamma_w\rangle)\psi\bigr)
     \to V_w:=(D_w-\langle D_w\rangle)\Phi_0.              \tag{16}
\]
This is the raw actual covariance-state map whose derivative control
was not supplied by (12) of the state companion alone.

## 5. Explicit complete limiting covariance spectral measure

In the mode coordinates (4) of the state companion write
\[
 \Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_r),
 \quad A_w=O^TG^{-1/2}G_wG^{-1/2}O,
 \quad J_w=\Sigma^{1/2}A_w\Sigma^{1/2}.                    \tag{17}
\]
These are exact finite real matrices with the original weights. Let
\(a_{\nu,\alpha}^{\dagger}\) be the oscillator creation operators
fixed by
\(z_{\nu,\alpha}=\sqrt{2/\sigma_\nu}
(a_{\nu,\alpha}+a_{\nu,\alpha}^{\dagger})\), with
\([a_{\nu,\alpha},a_{\eta,\beta}^{\dagger}]
=\delta_{\nu\eta}\delta_{\alpha\beta}\). In particular each real
coordinate has vacuum variance 2/σν. Differentiating the full Gaussian
of the companion gives
\[
 \langle D_w\rangle=\frac38\operatorname{tr}(A_w\Sigma),
 \qquad
 V_w=-\frac18\sum_{\nu,\eta}(J_w)_{\nu\eta}
                \sum_{\alpha=1}^3
                   a_{\nu,\alpha}^{\dagger}a_{\eta,\alpha}^{\dagger}\Phi_0.
                                                               \tag{18}
\]
For a direct check before passing to creation operators, put
\(S=G^{-1/2}B^{1/2}G^{-1/2}\). Ordinary differentiation gives
\[
 D_w\Phi_0=
 \left[\frac34\operatorname{tr}(G_wS)
  -\frac1{16}\sum_\alpha(x^\alpha)^TSG_wSx^\alpha\right]\Phi_0.
                                                               \tag{19}
\]
Gaussian covariance 2S^-1 subtracts exactly half of its constant term.
Then (17) and the stated coordinate/creation relation give (18), with no
omitted constant or color multiplicity.

The diagonal two-quantum vector
\(\sum_\alpha(a_{\nu,\alpha}^{\dagger})^2\Phi_0\) has squared
norm 6; the off-diagonal vector
\(\sum_\alpha a_{\nu,\alpha}^{\dagger}a_{\eta,\alpha}^{\dagger}\Phi_0\)
for ν<η has squared norm 3. These follow by commuting the two annihilators
through the two creators; different unordered mode pairs are orthogonal.
The exact limiting raw excitation measure is consequently
\[
 \boxed{\nu_{w,0}=
 \frac3{32}\sum_\nu (J_w)_{\nu\nu}^2\delta_{2\sigma_\nu/a}
 +\frac3{16}\sum_{\nu<\eta}(J_w)_{\nu\eta}^2
                          \delta_{(\sigma_\nu+\sigma_\eta)/a}.}
                                                               \tag{20}
\]
Repeated energies add their positive masses. The total is
\(3\operatorname{tr}(J_w^2)/32\); its first moment is
\(3\operatorname{tr}(\Sigma J_w^2)/(16a)\).
These are moments of the displayed limiting finite measure; convergence
of an unbounded first-moment test for finite-g measures is not inferred
merely from weak convergence.

For the actual full-model measures the precise conclusion is
\[
 g^4\langle v_w,\mathbf1_{\bullet}(H-\mathcal E)v_w\rangle
       \Longrightarrow\nu_{w,0},\quad
 v_w=(\Gamma_w-\langle\Gamma_w\rangle)\psi,
 \qquad
 g^4\|v_w\|^2\to\frac3{32}\operatorname{tr}(J_w^2).        \tag{21}
\]
This follows from the proved strong vector map (16), actual finite
spectral projections of the state companion, and its tightness argument
for raw measures. It holds against bounded continuous tests, with total
mass convergence. The factor g4 is explicitly retained; the original
norm and original positive-g spectrum are not declared equal to the limit.

## 6. Native weights and the actual state, without a fictitious vacuum

For the original native electric weight,
\(w_{(n,1)}=n_2^2\) and all other w_e=0. Then
\[
 G_{\rm nat}=\sum_{e=(n,1)}n_2^2\,t_et_e^T,
 \qquad t_e\text{ is column e of }T.                       \tag{22}
\]
It is positive semidefinite and nonzero. For example take a direction-1
edge at transverse coordinate n2=L and choose an adjacent contained
face. That edge participates in a chord loop, and its column of T is
nonzero: otherwise d1=CT would have zero column there, contradicting the
nonzero coefficient of that face in the original oriented curl. Its
weight L² is positive. Thus (22) is nonzero, and all invertible
congruences in (17) preserve that property. Hence
\[
 \lim_{g\downarrow0}g^4\|v_{\rm nat}\|^2
              =\frac3{32}\operatorname{tr}(J_{\rm nat}^2)>0.\tag{23}
\]
This resolves the fixed-box derivative/norm question for the actual
native Γ state. Equation (20) supplies all its limiting mode-pair masses,
including their original physical energies. It does not establish a
volume-uniform error in (21) or spectral tightness along g=g_j,L=L_j.
The exact finite matrices (22),(17) provide the next explicit spatial
objects to compute, rather than an assumption that the missing joint
limit has already been proved.

Equations (13)--(23) concern the actual electric derivative state. They
do not identify a finite-angle translated state with that derivative
state. In particular no small-angle or simultaneous volume/coupling
remainder has been imported into (21) without its own estimate.

## 7. Finite-energy mass of the native comparison measure as the box grows

The matrices in (17),(22) also permit a boundary-sensitive estimate of
the limiting native measure, without diagonalizing a large box numerically.
Let \(R=T^*G^{-1/2}\), an isometry onto \(\ker d_0^*\), and
\(P_T=RR^*\). Then
\[
 A_{\rm nat}=O^TR^*\operatorname{diag}(w)RO,\quad
 0\le A_{\rm nat}\le L^2I,\quad
 \operatorname{tr}A_{\rm nat}=\sum_e w_e(P_T)_{ee}.         \tag{24}
\]
Every original edge belongs to a contained elementary face, including
boundary edges. The oriented circulation around that face, divided by
2, is a unit vector in \(\ker d_0^*\) with edge component of absolute
value 1/2. The variational formula for the norm of an orthogonal
projection therefore gives \((P_T)_{ee}\ge1/4\).
For the original native weights the exact sum is
\[
 S_1:=\sum_e w_e
   =(2L)(2L+1)\sum_{n_2=-L}^L n_2^2
   =\frac23L^2(L+1)(2L+1)^2.                               \tag{25}
\]
The least frequency obeys
\(\sigma_{\min}=\sqrt8\sin(\pi/(4L+2))
\ge\sqrt8/(2L+1)\), using \(\sin x\ge2x/\pi\) on
\([0,\pi/2]\). Positivity and the trace Cauchy--Schwarz inequality,
with \(r=4L^2(4L+3)\), imply
\[
 \begin{split}
 \operatorname{tr}(J_{\rm nat}^2)
 &\ge\frac{(\operatorname{tr}J_{\rm nat})^2}{r}
 \ge\frac{\sigma_{\min}^2 S_1^2}{16r}\\
 &\ge\frac{L^2(L+1)^2(2L+1)^2}{18(4L+3)}
 \ge\frac{L^5}{27}.                                      \tag{26}
 \end{split}
\]
The last, deliberately explicit lower estimate uses \(4L+3\le6L\)
for L>=2; neither the earlier exact expression nor its boundary factors
is replaced in the definition of the state.

Fix a physical energy ceiling \(E_*>0\) and put \(s=aE_*\).
Only mode pairs with both \(\sigma_\nu\le s\) and
\(\sigma_\eta\le s\) can occur in (20) below that ceiling.
Let P_s be the diagonal mode projection onto these frequencies. Equations
(17),(24) give
\[
 \|P_sJ_{\rm nat}P_s\|\le sL^2,\qquad
 \nu_{{\rm nat},0}([0,E_*])
       \le\tfrac3{32}\operatorname{rank}(P_s)s^2L^4.       \tag{27}
\]
The exact open-box frequency list is
\(\sigma^2=\sum_{i=1}^3 4\sin^2(\pi j_i/[2(2L+1)])\),
\(0\le j_i\le2L\), with multiplicity k-1 when exactly k>=2
indices are positive. The same sine inequality implies
\(j_i\le(2L+1)s/2\) for every counted triple. Each multiplicity
is at most 2. Even including the extra excluded zero/one-positive
triples therefore gives the valid bound
\[
 \operatorname{rank}(P_s)
   \le2\left(1+\left\lfloor\frac{(2L+1)s}{2}\right\rfloor\right)^3.
                                                               \tag{28}
\]
Combining (26)--(28) with the exact total raw mass in (21) yields
\[
 \boxed{\nu_{{\rm nat},0}([0,E_*])
 \le \min\!\left\{1,
 \frac{54(aE_*)^2}{L}
       \left(1+\frac{(2L+1)aE_*}{2}\right)^3\right\}
                          \nu_{{\rm nat},0}([0,\infty)).} \tag{29}
\]
This retains the original raw mass; it is not an unrecorded change of
state norm. On the original spatial diagonal L_j=j²,a_j=1/(100j), its
explicit relative bound is
\[
 \frac{54E_*^2}{10^4 j^4}
          \left(1+\frac{(2j^2+1)E_*}{200j}\right)^3
                   \longrightarrow0.                     \tag{30}
\]
Thus the weak-coupling native *comparison* measures send a vanishing
fraction of their nonzero raw mass to every fixed finite physical-energy
interval along this box/spacing diagonal. This statement is fully proved
for the explicit matrix measures; it has not assumed a uniform remainder
for the actual finite-g measures in (21).

There is a corresponding precise existence statement for actual positive-g
regulators. At each fixed j, divide both sides of (21) by their explicitly
retained nonzero total mass to compare probability measures. Their weak
convergence follows from (21). For each integer k>=1 choose once a number
R_k in (k,k+1) outside the countable union, over all j>=2, of the finite
comparison spectra. At stage j, fixed-box convergence gives a positive
g_j<1/j for which the actual and comparison fractions below each R_k,
k<=j, differ by less than 1/j. Only finitely many inequalities are imposed
at that stage. For fixed E_* choose k with R_k>E_*. Eventually j>=k;
the bound (30) at the fixed ceiling R_k and the error 1/j show that the
actual fraction below E_* tends to zero. This proves existence of an actual all-positive-g
native electric-state sequence escaping every fixed finite energy interval.
It gives no specified logarithmic/fixed-kappa running-coupling estimate.

The macroscopic radial observable of the state companion and this native
electric observable therefore have different, explicitly computed spectral
limits on sufficiently weak chosen diagonals: a zero-energy atom for the
former, finite-energy escape for the latter. Their common coordinate maps,
actual vacuum and full Hamiltonian are retained. This does not prove they
are unrelated, nor rule out a further state family or spectral selection
with a useful interacting continuum limit.

## Reproducibility and references

Every operator and Hilbert-space map used here is given explicitly or in
the two complete companion proofs included with this document. The gradient
constant, moment recursion, graph limit and all spectral coefficients are
derived above. The standard ground-state transform and localization context
are cited in the companions (Kogut--Susskind, Bauer--D'Andrea--Freytsis--
Grabowska, and Simon). No interacting continuum construction or mass-gap
counterexample is asserted. In particular this is not a proof that the
original S6 completion or any claimed external counterexample exists.
