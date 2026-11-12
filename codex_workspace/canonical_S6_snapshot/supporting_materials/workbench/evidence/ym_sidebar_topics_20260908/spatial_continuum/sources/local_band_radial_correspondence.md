## 23. Exact correspondence between local energy and radial vacuum images

The complete [local-energy first-band proof](sources/local_band_inputs/LOCAL_ENERGY_BAND_TRANSFER.md)
is retained together with its [preceding definitions and proofs](sources/local_band_inputs/extensive_quantum_blocking.md). Its equation numbers are explicitly
called local-band source numbers below; the numbered equations of
this manuscript continue from (318). That source proves the actual
fixed-box local-energy graph limit, the seven-dimensional spectral
frame, and the local spatial Riemann limits. Section 22 supplies
the phase-square weighted limits. We now prove their exact common
operator and state maps, including a common positive-coupling
sequence and every displayed raw amplitude.

### 23.1. One original finite-regulator space

Fix \(L\ge2\), \(a>0\), and \(g>0\). Retain the entire open box, every edge and
face, and the physical invariant Haar Hilbert space. Put
\[
 H=\kappa\sum_e E_e+b\sum_p(2-\operatorname{tr}U_p),\qquad
 E_e=-\sum_{\alpha=1}^3X_{e,\alpha}^2,\qquad
 \kappa=\frac{2g^2}{a},\quad b=\frac1{2g^2a}.
\]
Let \(\psi\) be the actual positive unit vacuum, with energy \(\mathcal E\), and
\(A=H-\mathcal E\). Write \(d\mu=\psi^2dU\). For real edge weights \(f_e\) set
\[
 f_p=\frac14\sum_{e\in\partial p}f_e,\qquad
 D_f=\kappa\sum_e f_eE_e+b\sum_p f_p(2-\operatorname{tr}U_p),
 \quad C_f=D_f-\langle\psi,D_f\psi\rangle,\quad \Xi_f=C_f\psi.
 \tag{319}
\]
The signed electric sum has its Peter--Weyl self-adjoint domain: in the
joint Casimir expansion, the sum of the squared absolute weighted
eigenvalues times the squared coefficients must be finite. The
bounded self-adjoint magnetic perturbation makes \(D_f\) self-adjoint on
that same domain; no invariance of the domain under the multiplier
is asserted or needed. All identities below
initially use smooth physical functions; \(\psi\) and every finite spectral
eigenvector are smooth. Thus all displayed products on those vectors are
defined, including when unbounded operators occur.

Let \(Q=g^{-2}F\) be the globally smooth real invariant function of Section 22, with its original cutoff. Put
\[
 B_s=e^{isQ},\qquad
 R_g=\kappa\sum_{e,\alpha}(X_{e,\alpha}Q)^2,\qquad
 z_g=(R_g-\langle R_g\rangle_\psi)\psi.
 \tag{320}
\]
At every fixed regulator \(R_g\) is a bounded smooth nonnegative multiplier.
It is not the local weighted differential operator \(D_f\).

There is nevertheless an exact common-operator relation. Define
\[
 R_{g,f}^{Q}=\kappa\sum_{e,\alpha}f_e(X_{e,\alpha}Q)^2,\qquad
 J_f^Q=i[D_f,Q].
\]
Applying each \(X\) twice to \(B_s v\) gives
\[
 B_s^*D_fB_s=D_f+sJ_f^Q+s^2R_{g,f}^{Q},\qquad
 R_{g,f}^{Q}=\tfrac12[Q,[D_f,Q]],
 \tag{321}
\]
where
\[
 J_f^Q=-i\kappa\sum_{e,\alpha}f_e
 \{2(X_{e,\alpha}Q)X_{e,\alpha}+X_{e,\alpha}^2Q\}.
\]
The face multiplication and its entire scalar commute with \(Q\) and \(B_s\);
this is why they contribute no commutator, not a deletion from \(D_f\).
For \(s\ne0\), (321) also proves
\[
 R_{g,f}^{Q}
 =\frac{B_s^*D_fB_s+B_{-s}^*D_fB_{-s}-2D_f}{2s^2}.
 \tag{322}
\]
For \(0\le f_e\le M\),
\[
 0\le R_{g,f}^{Q}\le M R_g
\]
pointwise. For arbitrary real weights its absolute value is at most
\(\|f\|_\infty R_g\). These follow term by term from the nonnegative squares.
When \(f_e=1\), \(D_f=H\) and \(R_{g,f}^{Q}=R_g\) exactly.

The additional exact commutator is
\[
 [D_f,R_g]=-\kappa\sum_{e,\alpha}f_e
 \{(X_{e,\alpha}^2R_g)+2(X_{e,\alpha}R_g)X_{e,\alpha}\}.
 \tag{323}
\]
It follows by the same product rule and again retains the full \(D_f\).
Equations (321)--(323) are concrete finite-regulator operator maps between
the two constructions, before any oscillator comparison.

For a regular compact fluid profile \(u(s,x)\), the retained local-band source uses exactly
\(h_s(x)=\lambda_{\rm fl}^2|\operatorname{curl}u(s,x)|^2\), with calibration \(\lambda_{\rm fl}\).
The edge weights are \(f_e=h_s(a\,m(e))\), with the original face averages.
They are nonnegative. Equations (319)--(323) apply to those very weights.
The fluid parameter \(s\) has not been identified with the phase parameter,
the quantum heat time, or the coupling regulator.

### 23.2. Exact finite-frame overlap, with the Gram tensor retained

Use the retained local-band source's actual spectral projection
\[
 P_g=\mathbf1_{(\Delta/2,\,11\Delta/10)}(H-\mathcal E),\qquad
 \Pi_g=|\psi\rangle\langle\psi|+P_g,\qquad
 \Delta=2\sigma/a .
\]

For sufficiently small \(g>0\) at a fixed box, \(P_g\) has rank six
and \(\Pi_g\) has rank seven. Retain
\[
 {\cal K}=\mathbb C\oplus\operatorname{Sym}_3(\mathbb C),\qquad
 \langle(c,B),(d,E)\rangle_{\cal K}=\bar c d+6\operatorname{tr}(B^*E),
\]
the exact frame \(M_g\), \(G_g=M_g^*M_g\), and inverse \(G_g^{-1}M_g^*\) on the
range, as in local-band source (133). Set \(e_{\rm vac}=(1,0)\), and define
\[
 x_g=M_g^{-1}P_g z_g,\qquad
 y_{g,f}=M_g^{-1}P_g\Xi_f.
\]
Since \(M_ge_{\rm vac}=\psi\), \(C_f\) has zero vacuum expectation, and \(\Pi_g\) projects
onto the frame,
\[
 y_{g,f}={\cal D}_{g,f}e_{\rm vac},\qquad
 \langle z_g,P_g\Xi_f\rangle
       =\langle x_g,G_g y_{g,f}\rangle_{\cal K}.
 \tag{324}
\]
This is exact, because the part of \(z_g\) orthogonal to the band has zero
inner product with \(P_g\Xi_f\), and \(M_g^*M_g=G_g\). Likewise
\[
 \|P_g z_g\|^2=\langle x_g,G_gx_g\rangle_{\cal K},\qquad
 \|z_g\|^2=\|P_gz_g\|^2+\|(I-\Pi_g)z_g\|^2.
 \tag{325}
\]
The last equality uses \(\langle\psi,z_g\rangle=0\), which follows from its actual
expectation subtraction. No vector is divided by its norm.

One can also write the complete unprojected raw overlap in the original
vacuum measure. Since \(\psi\) is strictly positive and smooth on a compact
space, \(d_f=(D_f\psi)/\psi\) is a smooth real physical function. Then
\[
 \langle z_g,\Xi_f\rangle
 =\int (R_g-\mu(R_g))(d_f-\mu(d_f))\,d\mu.
 \tag{326}
\]
This gives its exact covariance; it does not replace \(d_f\) by the classical
fluid configuration or by a sampled classical energy.

### 23.3. Exact identification of the selected oscillator direction

The two sources retain the same tree linear map \(T\), \(G=TT^*\),
\(C=d_1\jmath\), and \(B=G^{1/2}C^*CG^{1/2}\). To avoid a conflict with the
phase-square \(R_g\), call the edge-space isometry
\[
 {\cal R}=T^*G^{-1/2}.
\]
Direct multiplication gives \({\cal R}^*{\cal R}=I\). Its range is
\((\ker T)^\perp=(\operatorname{im}d_0)^\perp\), the original transverse edge space.
The exact identity \(d_1T^*G^{-1}=C\) gives
\(d_1{\cal R}=CG^{1/2}\), hence
\[
 {\cal R}^*d_1^*d_1{\cal R}=B.
 \tag{327}
\]
For the selected lowest eigenmode \(\nu\) of Section 22, its original edge
vector is \(v_\nu=\mathcal R Oe_\nu\). Thus it belongs to the same lowest
three-dimensional eigenspace spanned by the retained local-band source's explicit
orthonormal edge cochains \(V_1,V_2,V_3\). Define
\[
 n_i=\langle V_i,v_\nu\rangle,\qquad
 n\in\mathbb R^3,\quad n^{\mathsf T}n=1,\qquad P_n=nn^{\mathsf T}.
 \tag{328}
\]
Equations (327)--(328) prove the mode alignment without replacing an
unspecified orthogonal basis by an invented one. On each of the three
color copies, \(a_{\nu,\alpha}^\dagger=\sum_i n_i a_{i,\alpha}^\dagger\).
Orthogonality of this mode change preserves the oscillator measure and
creation commutators.

Keep \(\lambda_{\rm osc}=2\sigma/a\) and \(k=3/2\);
\(\lambda_{\rm osc}\) is an energy, not \(\lambda_{\rm fl}\).
With \(q=\sigma|z_\nu|^2/4\) and
\(z_{\nu,\alpha}=\sqrt{2/\sigma}(a_{\nu,\alpha}+a_{\nu,\alpha}^\dagger)\), direct expansion gives
\[
 q=\tfrac12\sum_\alpha
 \{a_{\nu,\alpha}^2+(a_{\nu,\alpha}^\dagger)^2
                    +2a_{\nu,\alpha}^\dagger a_{\nu,\alpha}+1\}.
\]
Therefore, with the retained local-band source's creation-vector map \(\Phi\),
\[
 (q-k)\Phi_0=\tfrac12\Phi(P_n),\qquad
 \|\tfrac12\Phi(P_n)\|^2=\tfrac64\operatorname{tr}(P_n^2)=\tfrac32.
 \tag{329}
\]
The source's factor six is retained, including all three colors. This
exact identity is the relation between the radial Gamma vacuum-image
direction and the local first band. The phase direction is one
rank-one matrix in that six-dimensional symmetric-matrix band.

At fixed \(L,a\), the two source vector limits and projection convergence give
\[
 x_g\longrightarrow (0,\tfrac{\lambda_{\rm osc}}2P_n),\qquad
 y_{g,f}\longrightarrow(0,\tfrac1{4a}{\mathsf R}_f^{\min}),\qquad
 \|(I-\Pi_g)z_g\|\longrightarrow0.
 \tag{330}
\]
The last assertion follows by applying the converging band projection to
the strong vector limit \(\lambda_{\rm osc}(q-k)\Phi_0\), which is entirely in
that band by (329).

Using the original inner product in (324) now proves
\[
 \langle z_g,P_g\Xi_f\rangle
 \longrightarrow\frac{3\lambda_{\rm osc}}{4a}
                  n^{\mathsf T}{\mathsf R}_f^{\min}n,\qquad
 \|z_g\|^2\longrightarrow\tfrac32\lambda_{\rm osc}^2.
 \tag{331}
\]
The unprojected overlap has the same limit: \(\Xi_f\) has a bounded fixed-box
norm by its proved strong graph limit, and the omitted part of \(z_g\)
tends strongly to zero. This controls the missing cross term by
Cauchy--Schwarz; it does not declare all local-energy leakage zero.

### 23.4. The phase-square operator on the whole finite spectral frame

A further fixed-box result follows from the retained local-band source's excited-vector
moment identity (131). Let \(u_g\) be an eigenvector in the bounded finite
spectral range, with bounded norm and \(H\)-eigenvalue \(e_g\).
For \(U_g=W/g^2\), positivity of the electric part gives the initial
moment bound below. Division of the moment recursion by \(g^{2n+2}\)
gives the subsequent bounds for integers \(n\ge1\):
\[
 \begin{aligned}
 \int U_g|u_g|^2&\le2ae_g\|u_g\|^2,\\
 \int U_g^{n+1}|u_g|^2
 &\le2ae_g\int U_g^n|u_g|^2+
       16n^2\int U_g^{n-1}|u_g|^2,\qquad n\ge1.
 \end{aligned}
 \tag{332}
\]
Consequently every fixed moment is bounded at the fixed box, uniformly
over the bounded eigenvalue range. The global inequality
\(0\le R_g\le D_SU_g\) from Section 22 is pointwise and does not
depend on positivity of \(u_g\). For any fixed integer \(m\ge1\),
it therefore gives exactly the same squared
tail estimate as (294), with its vacuum moment \(B_{2m+1}\)
replaced by the eigenvector moment bound in (332):
\[
 \int_{|x|>R}|{\cal B}_g(R_g^m u_g)|^2
 \le D_S^{2m}B^{\rm eig}_{2m+1}
       \left(\frac1{c_*R^2}+\frac{g^2}{c_\rho}\right).
 \tag{333}
\]
Indeed, in the inner chart \(U_g\ge c_*R^2\); outside it,
\(U_g\ge c_\rho/g^2\). On each region, \(R_g^{2m}\) is bounded by
\(D_S^{2m}U_g^{2m}\). One extra power of \(U_g\) proves (333).

On every fixed ball the transported multiplier tends uniformly to
\(\lambda_{\rm osc}q\). Strong eigenvector convergence, multiplication by
these locally bounded coefficients, (333), and the polynomial Gaussian
tail of the comparison eigenvector give
\[
 {\cal B}_g(R_g^m u_g)\longrightarrow
             (\lambda_{\rm osc}q)^m u_0 .
 \tag{334}
\]
For the entire finite frame, choose an eigenbasis along a subsequence,
use the bounded finite rank and projection convergence to extract
convergent basis vectors, and apply (334) to each. The computed limiting
matrix is independent of this extraction; otherwise a sequence failing
matrix convergence would have a subsequence with the computed limit,
a contradiction. This proves finite-frame matrix convergence, with
all constants still depending on the fixed box. It is not a
uniform-volume theorem.

Write \(Z_g=R_g-\langle R_g\rangle_\psi\) and compress by the exact frame.
The resulting comparison operator on \(\mathcal K\) is
\[
 {\cal Z}_0(c,B)=\lambda_{\rm osc}
 \left(3\operatorname{tr}(P_nB),
       \tfrac c2P_n+P_nB+BP_n\right).
 \tag{335}
\]
Pair annihilation gives \(6\operatorname{tr}(P_nB)\), multiplied by
\(\lambda_{\rm osc}/2\). Pair creation of the vacuum gives
\(c\lambda_{\rm osc}P_n/2\). The number term has commutator
\(\Phi(P_nB+BP_n)\). These computations prove
(335), including its self-adjointness for the factor-six metric.

The compression has nonzero leakage. For any band vector \(\Phi(B)\),
\[
 (I-\Pi_0)\lambda_{\rm osc}(q-k)\Phi(B)
 =\tfrac{\lambda_{\rm osc}}2\,{\cal S}_{P_n}{\cal S}_B\Phi_0,
 \tag{336}
\]
where \(\mathcal S_B\) is the pair-creation polynomial defined in the retained local-band source.
The pair-annihilation and number terms stay in \(\Pi_0\) and there are no
higher spatial modes from \(P_n\). For \(B=P_n\), this is nonzero:
with three color oscillators,
\[
 \left\|\left(\sum_\alpha a_\alpha^{\dagger2}\right)^2\Phi_0\right\|^2
 =4^2\,2!\,(3/2)_2=120.
\]
For verification, its three terms \((a_\alpha^\dagger)^4\Phi_0\)
have total squared norm \(3\cdot4!=72\), and its three terms
\(2(a_\alpha^\dagger)^2(a_\beta^\dagger)^2\Phi_0\), \(\alpha<\beta\),
have total squared norm \(3\cdot4\cdot2!\cdot2!=48\).
Different occupation vectors are orthogonal. The leakage squared norm in (336) is thus
\(30\lambda_{\rm osc}^2\) for \(B=P_n\).

At finite regulator, inserting \(I=\Pi_g+(I-\Pi_g)\) gives
\[
 \Pi_g Z_g C_f\Pi_g
 =\Pi_g Z_g\Pi_g C_f\Pi_g+
 ((I-\Pi_g)Z_g\Pi_g)^*((I-\Pi_g)C_f\Pi_g).
 \tag{337}
\]
All range vectors are smooth, \(Z_g\) is a bounded smooth multiplier, and \(C_f\)
preserves smoothness, so every displayed product is defined.
The graph limits (334) and local-band source (132) identify each fixed-box
leakage matrix element by inner products of their full limiting
vectors. Thus neither compressed multiplication nor a comparison
of its matrices discards the term in (337).

### 23.5. Ordered local-profile limit: one-third overlap and its constants

Now use exactly
\[
 L_j=j^2,\qquad a_j=\frac1{100j},\qquad
 \ell_j=a_j(2j^2+1),\qquad \lambda_j=\frac{2\sigma_j}{a_j},
 \qquad c_j=j\lambda_j\longrightarrow c_\Gamma=100\sqrt2\pi.
\]
For a fixed real \(h\in C_c(\mathbb R^3)\), set
\(H_h=\int_{\mathbb R^3}h(x)\,dx\) and \(a_h=\sqrt2\pi H_h\).
The retained local-band source's proved matrix limit is
\[
 \frac{\ell_j^4}{a_j}{\mathsf R}_{h,j}^{\min}
       \longrightarrow 4\sqrt2\pi H_h I_3.
 \tag{338}
\]
Thus the two comparison frame vectors, with their displayed raw
scale factors, are
\[
 jz_{0,j}=(0,\tfrac{c_j}{2}P_{n_j}),\qquad
 \ell_j^4v_{h,0,j}=(0,\tfrac{\ell_j^4}{4a_j}
                      {\mathsf R}_{h,j}^{\min})
                 =(0,a_h I_3+o(1)).
 \tag{339}
\]
The unit vector \(n_j\) need not converge:
\(\operatorname{tr}(P_{n_j})=\operatorname{tr}(P_{n_j}^2)=1\)
for every \(j\), so all the following scalar conclusions are independent
of that basis freedom. Direct factor-six contractions give
\[
 \begin{split}
 \|jz_{0,j}\|^2&\longrightarrow\tfrac32c_\Gamma^2
                         =30000\pi^2,\\
 \|\ell_j^4v_{h,0,j}\|^2&\longrightarrow36\pi^2H_h^2,\\
 \langle jz_{0,j},\ell_j^4v_{h,0,j}\rangle
                  &\longrightarrow3c_\Gamma a_h
                         =600\pi^2H_h.
 \end{split}
 \tag{340}
\]
For \(H_h\ne0\), the squared cosine of their angle therefore tends to \(1/3\).
This is a computed fraction of raw Gram entries, not a replacement
of either original state by a unit vector.

The exact comparison projection of \(v_{h,0,j}\) onto \(z_{0,j}\) has
coefficient
\[
 \frac{n_j^{\mathsf T}{\mathsf R}_{h,j}^{\min}n_j}
               {2a_j\lambda_j};
\]
for the scaled vectors in (339) that coefficient tends to \(H_h/50\).
Consequently
\[
 \|\ell_j^4v_{h,0,j}-(H_h/50)jz_{0,j}\|^2
                   \longrightarrow24\pi^2H_h^2.
 \tag{341}
\]
Equations (340)--(341) also hold as the ordered actual limits
\(\lim_{j\to\infty}\lim_{g\downarrow0}\), by (330)--(331) at every fixed \(j\).
They have not been asserted along either independently selected
coupling sequence in the two sources.

For the actual regular NS profile, substitute
\(H_h=\lambda_{\rm fl}^2\|\operatorname{curl}u(s)\|_2^2\). This is positive for a nonzero
compact smooth incompressible profile: the compact divergence/curl
identity makes zero curl imply zero gradient, hence \(u=0\).
The leading local curvature state thus has a nonzero overlap with
the phase direction, and has the positive residual in (341).
This is an actual proved relation, rather than an inference of
nonrelation from the different presentations.

The residual has a concrete completion within the same lowest modes.
Define three phase quadratics using each of the original \(V_i\), with
the same admissible cutoff, and write \(z_g^{(i)}\) for their centered
phase-square vacuum vectors. Their fixed-box comparison matrices
are \((\lambda_{\rm osc}/2)e_i e_i^{\mathsf T}\). Their three pair vectors are orthogonal.
Summing them gives \((\lambda_{\rm osc}/2)I_3\). At comparison level,
\[
 \ell_j^4v_{h,0,j}-(H_h/50)\sum_{i=1}^3jz_{0,j}^{(i)}
                         \longrightarrow0.
 \tag{342}
\]
No new spatial-locality identification is involved: these are
three global selected-mode phases. The same complete compressed
operator relation holds in the ordered comparison:
\(\sum_i j\mathcal Z_{0,j}^{(i)}\) acts as
\(c_j(3\operatorname{tr}B,cI_3/2+2B)\).
Multiplication by \(H_h/50\) makes its limit exactly the retained
local-band source's
\[
 \mathcal T_h(c,B)=\sqrt2\pi H_h
                 (6\operatorname{tr}B,cI_3+4B).
\]
The proof is substitution into (335), with \(\sum_iP_i=I_3\).
This relates the entire seven-dimensional compressed operators,
not merely their vacuum columns. The leakage (337) remains present.

### 23.6. Exact nonidentity and the joint state errors

For nonnegative local \(h\) with at least one positive sampled edge
weight, \(C_f\) is not any scalar multiple of the bounded multiplier
\(Z_g\) as an operator on the smooth physical core. Choose a plaquette
\(p\) incident to an edge \(e\) with \(f_e>0\), and set
\(\phi=\operatorname{tr}U_p\). There are configurations with
\(X_{e,\alpha}\phi\ne0\), as follows by varying that edge with all
other plaquette links fixed to the identity. The smooth function
\(\phi\) is gauge invariant. Applying \(D_f\) to \(e^{it\phi}\) and
dividing by that nonzero multiplier gives a polynomial in \(t\)
whose quadratic coefficient is
\(\kappa\sum_{e,\alpha}f_e(X_{e,\alpha}\phi)^2\),
strictly positive somewhere. A fixed multiplication operator has
no \(t\)-dependence. Equality on every \(e^{it\phi}\) is therefore
impossible. The same argument applies after subtracting the vacuum scalar.

This establishes the specific full-operator nonidentity while
(321)--(342) prove the strongest explicit relations derived here.
The three-phase completion does not remove the full-operator
nonidentity or the leakage, and does not identify a local field.

The two retained constructions choose different finite lists for
their least dyadic exponent. Fixed-box convergence alone does not
prove that either existing least exponent satisfies the other's
new scaled tests. The concrete joint state errors, which Section 23.8
controls on its defined refined sequence, are in the common
comparison coordinates
\[
 \|{\cal B}_{g_j}(jz_{g_j,j})
                 -(c_j/2)\Phi(P_{n_j})\|\to0,\qquad
 \|\ell_j^4{\cal B}_{g_j}P_{g_j}\Xi_{f_{h,j}}
                 -\Phi(a_hI_3)\|\to0,
 \tag{343}
\]
together with the already retained frame Gram/projection control.
These are the precise errors whose product estimates by
Cauchy--Schwarz would promote (340) to a single actual diagonal.
Each test is attainable at every fixed box by the preceding proofs,
so their finite union can be imposed in a newly defined refined
dyadic selection. Section 23.8 below defines that additional sequence
and proves the common state map on it. Neither preexisting sequence
is declared unchanged by this refinement, and no uniform-volume
bound is inferred.

For products without intermediate projection one additionally needs
the joint scaled limit of the exact leakage in (337), including
the retained local-band source's higher spatial modes and four-creation terms.
Their fixed-box maps are explicit here and in local-band source (147)--(148);
their simultaneous volume limit is not supplied by the two source
diagonals. None of the calculations above assumes it.

### 23.7. Unchanged bounded cylinders on the weighted phase core

This additional estimate uses the already selected sequence of Section 22; it
requires no local-energy-band error estimate. Let \(F_j\) be
the pullback of one fixed continuous gauge-invariant coarse cylinder,
let \(\Delta F_j=F_j-F(I)\), and retain (317):
\(\|\Delta F_j\psi_j\|\to0\). Its uniform bound is
\(|\Delta F_j|\le2\|F\|_\infty\). Therefore
\[
 \int|\Delta F_j|^4\psi_j^2
 \le4\|F\|_\infty^2\|\Delta F_j\psi_j\|^2\longrightarrow0.
 \tag{344}
\]
For each fixed nonnegative integer \(m\), (303) with power \(2m\)
gives a uniform bound on \(\|(jR_g)^{2m}\psi_j\|\); for \(m=0\),
use the unit vacuum norm instead. Write \(h_j\) for an actual carrier
time-orbit vector. Equation (300) gives \(|h_j|\le2\psi_j\). All the
multipliers commute, so Cauchy--Schwarz in the original measure gives
\[
 \begin{split}
 \|\Delta F_j(jR_g)^m h_j\|^2
 &\le4\int|\Delta F_j|^2(jR_g)^{2m}\psi_j^2\\
 &\le4\left(\int|\Delta F_j|^4\psi_j^2\right)^{1/2}
               \|(jR_g)^{2m}\psi_j\|\\
 &\le8\|F\|_\infty\|\Delta F_j\psi_j\|\,
               \|(jR_g)^{2m}\psi_j\|\longrightarrow0.
 \end{split}
 \tag{345}
\]
For a finite carrier combination, the bound
\(|h_j|\le2(\sum_\ell|a_\ell|)\psi_j\) replaces the factor four by
\(4(\sum_\ell|a_\ell|)^2\). For a weighted vacuum vector, the same
proof starts with factor one. Since \(j\langle R_g\rangle_\psi\)
is bounded by (303), it also proves the scalar action on
\(j(R_g-\langle R_g\rangle_\psi)\psi_j\) after subtracting its
bounded multiple of \(\psi_j\).

Thus the unchanged bounded cylinder \(F\) acts by exactly \(F(I)\) in all
the retained polynomial phase-square vector limits. This is a
proved extension of the scalar cylinder representation to those
polynomial cores, with the actual moment bounds used in (345).
It is compatible with (340)--(342): the local operator \(D_f\) is a
differential operator with coefficients \(\kappa f_e\) and the magnetic
term \(bf_p\), and its scaled first-band action is not a fixed bounded
configuration cylinder. The unbounded coefficient and projection
operations cannot be replaced by the scalar action in (345).
Equations (321), (335), and (337) give the exact relationships to
that different operator class.

### 23.8. A defined common dyadic sequence for every fixed local profile

Define one common sequence using the
finite union of the two source requirements and the additional
state tests below. It does not identify the numerical least
dyadic of either preexisting sequence with this new one.

At fixed \(j\), retain the original finite edge set \(E_j\) and let
\(e^{(r)}\) be the edge weight that is one at \(r\) and zero elsewhere, always
with the prescribed quarter-face averages. Define the actual
comparison error map
\[
 {\cal T}_{g,j}f
  ={\cal B}_gP_g C_{g,f}\psi_g
          -\Phi({\mathsf R}_{f,j}^{\min}/(4a_j)).
 \tag{346}
\]
Here both terms are in the same full comparison Hilbert space,
including the original constant-Jacobian kinetic coordinate
isometry used to express \(\Phi\). The map is linear in the finite
real weight vector \(f\): \(D_f\) is linear, its expectation is linear,
and \(P_g,\psi_g\) do not depend on \(f\). The oscillator matrix is
also linear. The source graph and projection convergence imply
\(\|\mathcal T_{g,j}e^{(r)}\|\to0\) for every \(r\). Thus
\[
 \sup_{\|f\|_\infty\le j}\|{\cal T}_{g,j}f\|
 \le j\sum_{r\in E_j}\|{\cal T}_{g,j}e^{(r)}\|
 \longrightarrow0\quad(g\downarrow0,\ j\hbox{ fixed}).
 \tag{347}
\]
Every sum in (347) is finite. This proves the required uniformity
over the entire finite weight cube without assuming uniformity
as its dimension grows.

At each fixed \(j\), let \(\nu_1,\nu_2,\nu_3\) be the three original
lowest column indices of \(O\), in their existing order. They include
the original selected \(\nu_j\) of Section 22. Put
\[
 n_{i,j}=V^*{\cal R}Oe_{\nu_i},\qquad
 P_{i,j}=n_{i,j}n_{i,j}^{\mathsf T},\qquad
 n_{i,j}^{\mathsf T}n_{r,j}=\delta_{ir},\qquad
 \sum_{i=1}^3P_{i,j}=I_3.
\]
The identities follow from (327), the orthonormality of both
lowest-mode bases, and their equal three-dimensional ranges.
For each \(i=1,2,3\), use the same original cutoff and the quadratic
\(\sigma_j|z_{\nu_i}|^2/4\) for that original \(O\)-column to define
\(Q_g^{(i)}\), \(R_g^{(i)}\), and
\(z_g^{(i)}=(R_g^{(i)}-\langle R_g^{(i)}\rangle)\psi_g\).
These constructions preserve the original tree and Gram metric:
\(O\) is not changed. Its exact comparison in the \(V\)-basis is
(327)--(328), acting identically on all three colors.
The proof of their fixed-box weighted vacuum limits uses the
same established steps, with this selected quadratic: it and
its first differential vanish at the unique minimum, its
derivative square \(S_i\) is bounded by a fixed-box constant times
\(W\), and its local quadratic coefficient is \(\lambda_jq_i\).
The source moment recursion and tail proof then give
\[
 {\cal B}_g(jz_g^{(i)})
             \longrightarrow(c_j/2)\Phi(P_{i,j}).
 \tag{348}
\]
This is a proved application to three explicitly specified
quadratics; it is not an assumption of new weighted convergence.
One is exactly the original selected-mode quadratic, so its
phase-square direction has not been replaced. The earlier
sum in the \(V\)-basis in (342) has this same comparison because both
sums of the three rank-one projectors are \(I_3\).

At stage \(j\) choose the least positive integer \(n_j^\dagger\) for which
\(g_j^\dagger=2^{-n_j^\dagger}<j^{-5}\) satisfies all original stage-\(j\)
tests in both sources and, in addition,
\[
 \begin{split}
 \ell_j^4 j\sum_{r\in E_j}
       \|{\cal T}_{g_j^\dagger,j}e^{(r)}\|&<1/j,\\
 \|{\cal B}_{g_j^\dagger}(jz_{g_j^\dagger}^{(i)})
            -(c_j/2)\Phi(P_{i,j})\|&<1/j
                 \quad(i=1,2,3),\\
 j\|{\cal Z}_{g_j^\dagger}^{(i)}
                -{\cal Z}_{0,j}^{(i)}\|_{\mathcal K}&<1/j
                 \quad(i=1,2,3),\\
 \|(I-P_{g_j^\dagger})jz_{g_j^\dagger}^{(i)}\|&<1/j
                 \quad(i=1,2,3).
 \end{split}
 \tag{349}
\]
The original source compact-family tests are functions of \(g\) that
tend to zero at fixed \(j\), as proved there; the number of powers,
edge basis vectors, and additional quadratics is finite at that
\(j\). Here
\[
 {\cal Z}_g^{(i)}
 =G_g^{-1}M_g^*\Pi_g
       (R_g^{(i)}-\langle R_g^{(i)}\rangle)\Pi_gM_g,
\]
and \({\cal Z}_{0,j}^{(i)}\) is (335) with \(P_n=P_{i,j}\).
Equations (334)--(335) prove the finite-frame test tends to zero.
Equations (347)--(348) prove the vector tests tend to zero.
For the last test, (348)'s limit lies wholly in the comparison
first band, and the transported actual band projection converges
in operator norm at fixed \(j\). Applying the two projections
to the strongly converging vector proves that its omitted norm
tends to zero. Thus the last test is attainable as well. Their finite union therefore holds for every
sufficiently small positive \(g\). The dyadics tend to zero, so the
set of admissible positive exponents is nonempty and has a
least element. This proves existence of the sequence just
defined. No uniform-volume estimate has been assumed.
Its coefficients are precisely
\(\kappa_j=200j(g_j^\dagger)^2\) and \(b_j=50j/(g_j^\dagger)^2\),
including every face and the original Wilson scalar.

Use daggers to distinguish all actual states on this sequence:
\[
 v_{h,j}^\dagger=P_{g_j^\dagger}\Xi_{f_{h,j}},\qquad
 w_{i,j}^\dagger=jz_{g_j^\dagger}^{(i)},\qquad
 w_{n,j}^\dagger=jz_{g_j^\dagger}.
\]
For any fixed real \(h\in C_c(\mathbb R^3)\), \(\|f_{h,j}\|_\infty\le\|h\|_\infty\)
is at most \(j\) eventually. The first test in (349) and (347)
then bound its scaled actual-to-comparison error by \(1/j\).
No finite dense list of profiles is required: the entire
finite weight cube was controlled on the same sequence.

The source's Riemann matrix limit (338), (348)--(349), and
the isometry of the common coordinate maps prove
\[
 \boxed{\left\|\ell_j^4v_{h,j}^\dagger
          -\frac{H_h}{50}\sum_{i=1}^3 w_{i,j}^\dagger
         \right\|\longrightarrow0
          \quad\hbox{for every fixed }h\in C_c(\mathbb R^3).}
 \tag{350}
\]
Explicitly its transported norm is at most
\((1+3|H_h|/50)/j\) plus the norm of
\(\Phi(\ell_j^4\mathsf R_{h,j}^{\min}/(4a_j)-H_hc_jI_3/100)\).
The last matrix tends to zero because
\(H_hc_\Gamma/100=\sqrt2\pi H_h\). The factor-six formula makes
matrix convergence equivalent to convergence of this final
creation-vector norm. This proves (350) completely.

The same actual-to-comparison estimates prove on this defined
single sequence
\[
 \begin{split}
 \|w_{n,j}^\dagger\|^2&\longrightarrow30000\pi^2,\\
 \|\ell_j^4v_{h,j}^\dagger\|^2&\longrightarrow36\pi^2H_h^2,\\
 \langle w_{n,j}^\dagger,\ell_j^4v_{h,j}^\dagger\rangle
                                  &\longrightarrow600\pi^2H_h,\\
 \|\ell_j^4v_{h,j}^\dagger-(H_h/50)w_{n,j}^\dagger\|^2
                                  &\longrightarrow24\pi^2H_h^2.
 \end{split}
 \tag{351}
\]
Indeed each comparison vector in (339) has bounded norm, so
the error in every inner product is bounded by the two
vector errors times those bounds, plus their product.
The computed constants (340)--(341) then give (351).
For \(H_h\ne0\), the squared angular fraction is \(1/3\). For \(H_h=0\),
(350) gives the vanishing scaled local vector; no division by
that norm is made.

All these statements retain the raw original local state:
it has norm of order \(\ell_j^{-4}\) when \(H_h\ne0\). The explicit
scale \(\ell_j^4\) records its comparison amplitude; it is not a
unit normalization. Each \(w_{i,j}^\dagger\) likewise retains its definition
\(j(R_g^{(i)}-\langle R_g^{(i)}\rangle)\psi_g\) and its nonzero raw limiting norm.
No equality of the fluid time and quantum time was introduced.
The original phase sequence's bounded-cylinder tests are in
the finite union, so the polynomial-core scalar action (345)
persists on this defined refined sequence. Mixed products
without \(\Pi_g\) still retain the leakage (337); (350) by itself
does not determine its simultaneous volume limit.

The added finite-frame test also promotes the ordered compressed
operator relation following (342) to this same sequence:
\[
 \left\|\ell_j^4{\cal D}_{g_j^\dagger,f_{h,j}}
       -\frac{H_h}{50}\sum_{i=1}^3
                       j{\cal Z}_{g_j^\dagger}^{(i)}
 \right\|_{\mathcal K}\longrightarrow0.
 \tag{352}
\]
The first term tends to \(\mathcal T_h\) by the retained local-band source's
edge-basis and Gram tests, which are included in (349).
For the second term its error from the comparison sum is
at most \(3|H_h|/(50j)\), by (349). Equations (335) and
\(\sum_iP_{i,j}=I\) make that comparison sum
\((H_hc_j/50)(3\operatorname{tr}B,cI_3/2+2B)\), which tends exactly to \(\mathcal T_h\)
because \(c_\Gamma=100\sqrt2\pi\). This proves (352), retaining
the full actual Gram frame. It concerns compressed operators;
the exact full-product term (337) is still present.
