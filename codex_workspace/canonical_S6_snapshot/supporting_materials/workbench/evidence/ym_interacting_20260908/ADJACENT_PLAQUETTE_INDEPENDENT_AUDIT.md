# Independent audit: adjacent-plaquette quantum correction

8 September 2026, 11:26 UTC. Verdict: PASS for the stated finite seven-link,
small-positive-ξ calculation. No mathematical error was found. This is not
a continuum Yang-Mills theorem or a mass-gap conclusion.

The complete source `adjacent_plaquette_quantum_correction.md` was read and
its calculation independently derived. Audited source SHA-256:
`6065f6473efdbbd7700f0bf79d4ce29cc3429600a8f46ae5621adfe787be2fc5`.
The audit preserves the original two plaquettes, all seven links, the
opposite common-edge orientations, probability Haar measures, the metric
and both Hamiltonian coefficients. No mathematical source, PDF, canonical
artifact or remote content was edited by this audit.

## 1. Actual vacuum and its controlled first derivative

Write \(F=W_P+W_Q\), with \(P=U_eA\), \(Q=U_e^{-1}B\), and retain

\[
H=\kappa(H_0-\xi F)+4bI,
\qquad H_0=-\sum_{f=1}^{7}\Delta_f^T,
\qquad \xi=b/\kappa,
\qquad T_a=i\sigma_a/2.
\]

Direct Pauli multiplication gives \(\sum_aT_a^2=-3I/4\). The
product Peter-Weyl basis therefore gives the simple constant eigenvector
at zero and the first nonzero full-space eigenvalue \(3/4\). Each
four-link fundamental trace has \(H_0W_P=3W_P\) and
\(H_0W_Q=3W_Q\). No gauge fixing or omission of an outer edge is used.
The original metric has orthonormal basis \(2T_a\), hence

\[
\Delta^c=4\Delta^T,\qquad
\kappa=2g_{\rm YM}^2/a,\qquad b=1/(2g_{\rm YM}^2a),\qquad
\xi=1/(4g_{\rm YM}^4).
\]

On \(|z|=3/8\), the unperturbed resolvent norm is at most \(8/3\).
Since \(\|F\|_\infty\leq4\), its perturbation series converges for
\(|\xi|<3/32\). The resulting contour projection has rank one by
continuity from \(\xi=0\). For real \(\xi\) in this interval the
lowest eigenvalue of \(H_0-\xi F\) lies in
\([-4|\xi|,4|\xi|]\), while every eigenvalue above it is at least
\(3/4-4|\xi|>3/8\), by the min-max principle and the bounded
multiplication perturbation. Thus this branch is the actual ground branch,
not an assumed reference state. Positivity improvement and compact
elliptic regularity give its unique positive smooth representative.

Choose the analytic representative \(\int\phi_\xi d\lambda=1\),
and denote the eigenvalue of \(H_0-\xi F\) by \(e_\xi\).
Differentiating gives

\[
H_0\phi'_0-F=e'_0,\qquad
e'_0=-\int Fd\lambda=0,\qquad
\phi'_0=F/3.
\]

The zero-mean condition removes the constant in the last solution. The
normalization used for the physical state is explicitly
\(\psi_\xi=\phi_\xi/Z_\xi^{1/2}\),
\(Z_\xi=\int\phi_\xi^2d\lambda\), not a change to \(H\).
For fixed \(U_e\), the two outer products are independent Haar variables,
so \(\int W_P^2=\int W_Q^2=1\) and \(\int W_PW_Q=0\).
All higher Taylor coefficients of \(\phi_\xi\) have zero mean.
Consequently

\[
Z_\xi=1+\frac{2\xi^2}{9}+O(\xi^3),\qquad
\log\rho_\xi=\frac{2\xi}{3}F+O(\xi^2),\qquad
\rho_\xi=\psi_\xi^2.
\]

The asserted smooth remainders are justified directly: if the Riesz
vector is analytic in \(H^s\), the eigen-equation rewritten as

\[
\phi_\xi=(H_0+I)^{-1}[(1+e_\xi+\xi F)\phi_\xi]
\]

shows analyticity in \(H^{s+2}\). Smooth multiplication is bounded on each
fixed Sobolev space. Starting at \(s=0\), induction and Sobolev embedding
give every fixed \(C^k\) remainder. For sufficiently small real ξ,
uniform closeness to 1 permits the same estimates for logarithms. The
constant \(4bI\) remains in the original energy \(E_\xi=4b+\kappa e_\xi\)
and cancels only in the explicitly ground-subtracted operator.

## 2. Conditional score and its covariance

Eliminate exactly one outer edge \(S\) of \(P\), not an edge of \(Q\).
For each fixed retained configuration \(r\), integration over this edge
makes \(P\) Haar and leaves \(Q\) fixed. Thus

\[
\rho_{R,\xi}=1+\frac{2\xi}{3}W_Q+O(\xi^2),\qquad
X\log\rho_\xi-X\log\rho_{R,\xi}
=\frac{2\xi}{3}XW_P+O(\xi^2)
\]

for every retained derivative \(X\). Differentiation commutes with the
compact marginal integral. Its exact, interacting form is

\[
J_\xi^*(X\log\rho_\xi)=X\log\rho_{R,\xi},\qquad
J_\xi^*u=\rho_{R,\xi}^{-1}\int u\rho_\xi d\lambda_S.
\]

Expanding the divergence operator, its retained second derivatives cancel
in \(L_\xi J-JA_\xi\), giving exactly the printed negative score
contraction. Centering the retained observable changes none of its
derivatives; explicitly \(\mu_\xi(W_Q)=2\xi/3+O(\xi^2)\).
The only common derivative support of \(W_P,W_Q\) is \(e\). Hence

\[
B_\xi f_\xi=-\frac{2b}{3}G+O(b\xi),\qquad
G=\sum_a(X_{e,a}W_P)(X_{e,a}W_Q),\qquad
J_\xi^*B_\xi f_\xi=0.
\]

There is also a direct conditional-covariance check. Put
\(P=p_0I+i\boldsymbol p\cdot\boldsymbol\sigma\) and
\(Q'=BU_e^{-1}=q_0I+i\boldsymbol q\cdot\boldsymbol\sigma\).
At fixed \(r\), \(p\) is uniform on \(S^3\), and \(q\) is fixed. The
derivatives are \(X_{e,a}W_P=-p_a\), \(X_{e,a}W_Q=q_a\).
Therefore the common-edge score covariance is

\[
J_\xi^*(\sigma_a\sigma_c)
=\frac{\xi^2}{9}\delta_{ac}+O(\xi^3),\qquad
J_0^*(G^2)=\frac{|\boldsymbol q|^2}{4}
=\frac{4-W_Q^2}{16}.
\]

Here \(\sigma_a=X_{e,a}\log\rho_\xi-X_{e,a}\log\rho_{R,\xi}\).
The density and score errors are uniform; the calculation uses Haar only
for the Taylor coefficient at zero. It follows independently that

\[
J_\xi^*(|B_\xi f_\xi|^2)
=\frac{b^2}{36}(4-W_Q^2)+O(b^3/\kappa),\qquad
\|B_\xi f_\xi\|_{\mu_\xi}^2
=\frac{b^2}{12}+O(b^3/\kappa).
\]

Thus no product-Haar vacuum is assumed at positive \(b\).

## 3. Signs, Haar norms and both eliminated Casimir channels

The opposite traversal of \(e\) in \(Q\) gives

\[
X_{e,a}W_Q=-\operatorname{tr}(T_aBU_e^{-1}),\qquad
\sum_a\operatorname{tr}(T_aC)\operatorname{tr}(T_aD)
=-\frac12\operatorname{tr}(CD)
+\frac14\operatorname{tr}C\operatorname{tr}D.
\]

Since \(\operatorname{tr}(PQ')=\operatorname{tr}(AB)\), this proves

\[
G=\frac12R_0-\frac14D_0
=\frac38R_0-\frac14D_1,
\qquad D_1=D_0-R_0/2.
\]

For fixed \(U_e\), \(p,q\) are independent uniform \(S^3\) variables.
Rotational invariance and \(\sum_{\alpha=0}^3p_\alpha^2=1\) give
\(\mathbb E p_\alpha p_\beta=\delta_{\alpha\beta}/4\).
With \(s=\sum_{a=1}^3p_aq_a\),

\[
R_0=2(p_0q_0-s),\qquad D_1=3p_0q_0+s,\qquad G=-s.
\]

Each of the four products \(p_\alpha q_\alpha\) has second moment
\(1/16\), and distinct such products are orthogonal. The resulting exact
moments are

\[
\|R_0\|^2=4(1+3)/16=1,\quad
\|D_1\|^2=(9+3)/16=3/4,\quad
\langle R_0,D_1\rangle=2(3-3)/16=0,\quad
\|G\|^2=3/16.
\]

Every outer edge occurs once in each term defining \(R_0,D_1\), so
its Laplacian contributes \(-3/4\). The common edge has

\[
\Delta_e^TD_0=-\frac32D_0+2G=R_0-2D_0=-2D_1,
\qquad \Delta_e^TR_0=0.
\]

There are six outer edges. Thus the two full free eigenvalues are exactly
\(9\kappa/2\) and \(13\kappa/2\). Integration over \(S\) kills
both \(R_0,D_1\); the free product Laplacian commutes with that integration.
They are therefore eigenvectors of the eliminated form operator \(C_0\)
with those same eigenvalues, rather than merely eigenvectors of a formal
compression. Finally,

\[
B_\xi f_\xi=b\left(-\frac14R_0+\frac16D_1\right)+O(b\xi),
\qquad \frac1{16}+\frac{3}{4}\frac1{36}=\frac1{12}.
\]

## 4. Exact moving-subspace transport and controlled form resolvent

All Hilbert spaces can be compared with \(L^2(\lambda)\), using the
uniformly equivalent smooth positive densities near zero. The projections
need not be orthogonal in this fixed reference inner product, but their
algebraic ranges are exactly the same retained-function space. This gives
the stronger exact identities

\[
P_\xi P_0=P_0,\quad P_0P_\xi=P_\xi,\quad
Q_0Q_\xi=Q_0,\quad Q_\xi Q_0=Q_\xi.
\]

Consequently

\[
T_\xi=Q_\xi|_{\ker P_0}:\ker P_0\longrightarrow\ker P_\xi,
\qquad T_\xi^{-1}=Q_0|_{\ker P_\xi}.
\]

These are exact inverses, not approximate ones. The Neumann/residual
argument in the audited source is valid as well; here its compressed
operator \(Q_0Q_\xi Q_0\) is in fact already the identity on
\(\ker P_0\). The conditional density formula and its first derivatives
give \(P_\xi-P_0=O(\xi)\) on both \(L^2\) and \(H^1\), so the exact
inverses also identify their \(H^1\) subspaces and are locally bounded.

Let \(V_0=H^1\cap\ker P_0\). On this fixed space pull back the full form
and the mass form by \(T_\xi\):

\[
\widetilde c_\xi(h,k)
=\kappa\int\sum_{f,a}\overline{X_{f,a}T_\xi h}
 X_{f,a}T_\xi k\,\rho_\xi d\lambda,\qquad
\widetilde m_\xi(h,k)=\int\overline{T_\xi h}T_\xi k\,\rho_\xi d\lambda.
\]

Uniform density bounds and bounded inverses give uniform \(H^1\)
coercivity of \(\widetilde c_\xi+z\widetilde m_\xi\) at fixed
\(\kappa,z>0\). Its difference from the zero form has norm \(O(\xi)\)
as a map \(V_0\to V_0^*\). The resolvent equation for
\(v_\xi=T_\xi^{-1}w_{\xi,z}\) is precisely

\[
(\widetilde c_\xi+z\widetilde m_\xi)(h,v_\xi)
=\langle T_\xi h,B_\xi f_\xi\rangle_{\mu_\xi}\quad(h\in V_0).
\]

The right side is \(b\langle h,-R_0/4+D_1/6\rangle_\lambda+O(b\xi)\)
in \(V_0^*\). Subtracting the equation for its free solution and testing
the difference with itself proves an \(O(b\xi)\) error in \(H^1\), with
constants allowed to depend on fixed positive \(\kappa,z\). Transporting
back changes it by the same order. Thus

\[
w_{\xi,z}=-\frac{bR_0}{4(9\kappa/2+z)}
+\frac{bD_1}{6(13\kappa/2+z)}+O(\xi^2)
\]

in \(H^1\) at fixed \(\kappa,z>0\), as stated. For \(z=\kappa\), divide
the full equation by κ: its free coercive form and mass coefficient are
then independent of κ, the forcing is \(\xi[-R_0/4+D_1/6]+O(\xi^2)\),
and the error is \(O(\xi^2)\). This also proves the displayed separate
\(b,\kappa\) remainder scales for \(I,J\). No spectrum of the moving
operator was assumed to have a termwise expansion.

## 5. True-vacuum orthogonality, exact energy decrease and coefficient

The conditional projection, retained lift and forms intertwine the vertex
gauge action by Haar substitution and invariance of the actual density.
Their uniquely defined resolvent does as well. Thus \(w_{\xi,z}\) and
\(u_{\xi,z}=\psi_\xi(Jf_\xi-w_{\xi,z})\) are invariant. The latter
is orthogonal to the actual vacuum because \(f_\xi\) is centered and
\(J_\xi^*w_{\xi,z}=0\). It is a nonzero form-domain vector, since

\[
\|Jf_\xi-w_{\xi,z}\|_{\mu_\xi}^2=d_\xi+J_{\xi,z}>0.
\]

The resolvent identity tested with \(w\) gives
\(c_\xi(w,w)=I_{\xi,z}-zJ_{\xi,z}\), and the cross form is
\(q_\xi(Jf,w)=\langle B_\xi f,w\rangle=I_{\xi,z}\). The minus sign
in the corrected vector therefore gives

\[
\mathcal R_{\rm full}(z)=\frac{a_\xi-I_{\xi,z}-zJ_{\xi,z}}
 {d_\xi+J_{\xi,z}},\qquad
\mathcal R_{\rm retained}-\mathcal R_{\rm full}(z)
=\frac{I_{\xi,z}+(z+a_\xi/d_\xi)J_{\xi,z}}{d_\xi+J_{\xi,z}}.
\]

The positive resolvent has strictly positive quadratic form on every
nonzero vector, so this is strictly positive when \(B_\xi f_\xi\ne0\).
The coupling norm expansion proves this nonvanishing for all sufficiently
small positive ξ. At zero, \(d_0=\int W_Q^2=1\) and
\(a_0=\kappa\langle W_Q,H_0W_Q\rangle=3\kappa\). Analytic densities
give the stated \(O(\xi)\) relative bounds for these quantities.

At \(z=\kappa\), orthogonality of the two free channels gives

\[
I_{\xi,\kappa}=\frac{b^2}{\kappa}
 \left(\frac1{88}+\frac1{360}\right)+O(b^3/\kappa^2)
=\frac{7b^2}{495\kappa}+O(b^3/\kappa^2),
\]

\[
J_{\xi,\kappa}=\frac{b^2}{\kappa^2}
 \left(\frac1{484}+\frac1{2700}\right)+O(b^3/\kappa^3)
=\frac{199b^2}{81675\kappa^2}+O(b^3/\kappa^3).
\]

Substitution into the exact decrease gives

\[
\frac7{495}+4\frac{199}{81675}
=\frac{1155+796}{81675}=\frac{1951}{81675},
\]

and therefore precisely

\[
\boxed{\mathcal R_{\rm retained}-\mathcal R_{\rm full}(\kappa)
=\frac{1951}{81675}\frac{b^2}{\kappa}+O(b^3/\kappa^2).}
\]

Since \(b^2/\kappa=1/(8g_{\rm YM}^6a)\) and
\(b^3/\kappa^2=1/(32g_{\rm YM}^{10}a)\), the original-variable
coefficient is \(1951/(653400g_{\rm YM}^6a)\), with exactly the stated
strong-coupling remainder order. Both trial Rayleigh values remain near
\(3\kappa\); the decrease is not an assertion of a small continuum energy.

## 6. Independent exact-arithmetic replay

Separate from the root's checker, a bounded SymPy/rational replay verified
all 16 Pauli entrywise Fierz identities, the fundamental Casimir, the
quaternion contraction identity, all four Haar moments, the coupling norm,
both resolvent coefficients, the decrease coefficient and its original
coupling conversion. All passed. The analytic, conditional-domain and
form-resolvent arguments are proved above and are not inferred from those
finite arithmetic tests. No repair to the audited source is required.

## 7. Addendum: the actual retained and corrected excitation values

8 September 2026. The additional second-order calculation was independently
derived and passed a separate exact-rational replay. Its coefficients are
correct, not merely the previously checked decrease.

Keep \(F=W_P+W_Q\), \(W=W_Q\), the mean-one analytic representative and
the original full Hamiltonian:

\[
\phi_\xi=1+\xi\phi_1+\xi^2\phi_2+O(\xi^3),\qquad
\phi_1=F/3,\qquad \int\phi_2\,d\lambda=0,\qquad
H=\kappa(H_0-\xi F)+4bI.
\]

Writing the eigenvalue of \(H_0-\xi F\) as
\(e_\xi=e_1\xi+e_2\xi^2+O(\xi^3)\), integration of the first and second
coefficient equations gives

\[
e_1=0,\qquad e_2=-\int F\phi_1\,d\lambda=-2/3,\qquad
H_0\phi_2=F^2/3-2/3.
\]

This retains the scalar ground energy; it does not replace the physical
vacuum by its first-order approximation. The analytic Sobolev control in
Section 1 justifies all coefficient integrations and \(O(\xi^3)\) density
remainders used here.

For one edge of the simple four-edge loop, the fundamental trace obeys
\(\Delta_e^TW=-3W/4\) and
\(\sum_a|X_{e,a}W|^2=1-W^2/4\). The product rule therefore gives

\[
\Delta_e^T(W^2-1)
=-\frac32W^2+2(1-W^2/4)=-2(W^2-1).
\]

Summing its four distinct edges proves
\(H_0\chi_{\rm ad}(Q)=8\chi_{\rm ad}(Q)\), where
\(\chi_{\rm ad}(Q)=W^2-1\). The equality with the adjoint character also
follows from the two eigenvalues \(e^{\pm i\theta}\) of \(Q\):
\(W^2-1=1+2\cos(2\theta)\).

For a Haar quaternion \(q\), \(\mathbb E q_0^2=1/4\) and
\(\mathbb E q_0^4=1/8\). To check the fourth moment explicitly, invariance
under a rotation taking \(q_0\) to \((q_0+q_1)/\sqrt2\) gives
\(\mathbb E q_0^4=3\mathbb E q_0^2q_1^2\); expanding
\(\mathbb E(\sum_{\alpha=0}^3q_\alpha^2)^2=1\) then gives
\(4\mathbb E q_0^4+12\mathbb E q_0^2q_1^2=1\).
Thus \(\int W^2=1\), \(\int W^4=2\), and the odd trace moments vanish
by Haar invariance under \(Q\mapsto-Q\).

The two traces are independent under product Haar, as proved above.
Consequently

\[
\int F^2\chi_{\rm ad}(Q)\,d\lambda
=\int W^2(W^2-1)\,d\lambda=1,\qquad
\int F^2W^2\,d\lambda=1+2=3.
\]

Self-adjointness of \(H_0\), with its exact eigenvalue 8 on this
character, now gives

\[
\int\phi_2W^2\,d\lambda
=\int\phi_2\chi_{\rm ad}(Q)\,d\lambda
=\frac18\int H_0\phi_2\,\chi_{\rm ad}(Q)\,d\lambda
=\frac1{24}.
\]

Retaining the state-normalization factor \(Z_\xi=1+2\xi^2/9+O(\xi^3)\),
the actual density is

\[
\rho_\xi
=1+\frac{2\xi}{3}F
+\xi^2\left(\frac{F^2}{9}+2\phi_2-\frac29\right)+O(\xi^3).
\]

The linear term in its \(W^2\) moment vanishes by the Haar moments.
The second-order terms therefore give precisely

\[
r_\xi:=\mu_\xi(W^2)
=1+\left(\frac39+\frac2{24}-\frac29\right)\xi^2+O(\xi^3)
=1+\frac7{36}\xi^2+O(\xi^3).
\]

Likewise \(m_\xi:=\mu_\xi(W)=2\xi/3+O(\xi^2)\), and hence

\[
d_\xi=\operatorname{Var}_{\mu_\xi}(W)
=r_\xi-m_\xi^2
=1+\left(\frac7{36}-\frac49\right)\xi^2+O(\xi^3)
=1-\frac14\xi^2+O(\xi^3).
\]

All four edges of \(Q\) are retained. Centering changes none of their
derivatives, and the one-edge gradient identity above proves the exact
pointwise numerator identity

\[
\sum_{e\in Q,a}|X_{e,a}W|^2=4-W^2,\qquad
a_\xi=\kappa(4-r_\xi).
\]

Dividing by the actual variance, with its positive zeroth-order value,
yields the retained excitation quotient

\[
\begin{aligned}
\mathcal R_{\rm retained}
&=\kappa\,
\frac{3-7\xi^2/36+O(\xi^3)}
 {1-\xi^2/4+O(\xi^3)}\\
&=3\kappa+
\left(\frac34-\frac7{36}\right)\kappa\xi^2+O(\kappa\xi^3)\\
&=\boxed{3\kappa+\frac59\frac{b^2}{\kappa}
+O(b^3/\kappa^2)}.
\end{aligned}
\]

Subtracting the independently proved decrease at \(z=\kappa\) gives

\[
\frac59-\frac{1951}{81675}
=\frac{45375-1951}{81675}=\frac{43424}{81675},
\]

and therefore the actual corrected excitation value is

\[
\boxed{\mathcal R_{\rm full}(\kappa)
=3\kappa+\frac{43424}{81675}\frac{b^2}{\kappa}
+O(b^3/\kappa^2).}
\]

Both displayed values are Rayleigh quotients of \(H-E_\xi\) for the
specified actual-vacuum trial states. They are not claims of exact
excited eigenvalues. They establish the energy level of the trials as
well as their strictly positive difference.

For completeness the unsubtracted original-\(H\) energy origin is also
fixed by the same second coefficient equation:

\[
E_\xi=4b-\frac23\frac{b^2}{\kappa}+O(b^3/\kappa^2).
\]

Adding this exact ground-energy shift to each excitation quotient gives

\[
\frac{\langle u_{\rm retained},H u_{\rm retained}\rangle}
 {\|u_{\rm retained}\|^2}
=3\kappa+4b-\frac19\frac{b^2}{\kappa}+O(b^3/\kappa^2),
\]

\[
\frac{\mathfrak h[u_{\xi,\kappa}]}{\|u_{\xi,\kappa}\|^2}
=3\kappa+4b-\frac{11026}{81675}\frac{b^2}{\kappa}
+O(b^3/\kappa^2),
\]

where \(\mathfrak h\) is the original-\(H\) closed form. This last form
notation does not require additional operator-domain regularity of the
resolvent-corrected vector. The finite strong-coupling scope is unchanged.
