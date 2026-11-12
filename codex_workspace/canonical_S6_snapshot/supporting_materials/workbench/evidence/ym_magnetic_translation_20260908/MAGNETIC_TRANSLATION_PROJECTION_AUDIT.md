# Gauge-projected translations of the actual finite-lattice vacuum

8 September 2026. Independent bounded calculation. The proposed first-
and second-derivative averages are correct with source vertices for the
specified left multiplication. This note proves their domains, centering,
norm and energy coefficients, resolves the possible zero vector, and
checks the additional specified open-box flux. All assertions concern a
fixed finite regulator. No continuum or novelty claim is made.

## 1. Objects, signs, domains and the gauge action

Let \((\mathsf V,\mathsf E)\) be a finite graph without self-loops, with
fixed physical edge orientations and source/target maps \(s,r\).
Reverse traversal means \(U_e^{-1}\), not a second independent edge.
Let \(\lambda\) be probability product Haar measure on
\(\mathcal Q=SU(2)^{\mathsf E}\), and retain the full Wilson Hamiltonian

\[
H=-\kappa\sum_{e,a}X_{e,a}^2+V,\qquad
V=b\sum_p(2-\operatorname{tr}U_p),\qquad \kappa,b>0,
\]

with every specified plaquette word and its original coefficient.
The basis and derivatives are

\[
T_a=-i\sigma_a/2,\qquad
X_{e,a}f(U)=\left.\frac d{du}\right|_0f(\ldots,e^{uT_a}U_e,\ldots).
\]

These derivatives generate left multiplication of the variable. As
vector fields they are right-invariant; in particular
\([T_a,T_b]=\epsilon_{abc}T_c\), but on functions
\([X_{e,a},X_{e,b}]=-\epsilon_{abc}X_{e,c}\).
One checks the latter on a matrix-coordinate function:
\(X_aX_bU=T_bT_aU\). Derivatives on distinct edges commute.
Haar integration by parts gives \(X_{e,a}^*=-X_{e,a}\).
With \(c=-\operatorname{tr}/2\), \(X^c=2X\) and
\(\Delta^c=4\Delta^T\), so the original physical coefficient remains
\(\kappa=2g_{\rm YM}^2/a\), equivalently \(\kappa/4\) with \(\Delta^c\).

Write \(H\psi=E\psi\), \(\|\psi\|_\lambda=1\), for the actual smooth
strictly positive gauge-invariant ground state. The bounded smooth
potential and compact elliptic kinetic operator give \(D(H)=H^2\),
form domain \(H^1\), and \(\psi\in C^\infty\). Put

\[
q_0(u,v)=\langle(H-E)^{1/2}u,(H-E)^{1/2}v\rangle .
\]

This is a nonnegative form, and its kernel is \(\mathbb C\psi\).
Uniqueness follows directly by dividing a second ground vector by
\(\psi\) in the ground-state Dirichlet identity proved below.

Use the vertex gauge maps and unitary pullbacks

\[
(\beta_gU)_e=g_{s(e)}U_eg_{r(e)}^{-1},\qquad
(\mathcal G_gf)(U)=f(\beta_gU),\qquad
\Pi=\int_{SU(2)^{\mathsf V}}\mathcal G_g\,dg .
\]

These pullbacks compose in reverse order, which has no effect on the
Haar projection: Haar multiplication proves \(\Pi^2=\Pi\), and Haar
inversion proves \(\Pi^*=\Pi\). Its range is exactly the invariant
subspace. The other convention \(h_s^{-1}U_eh_r\) gives exactly this
same projection under \(g_v=h_v^{-1}\).

Each gauge map is a product of left/right group isometries. Thus it
commutes with the free product Laplacian, preserves every \(H^k\),
and commutes with the full \(H\), since the plaquette traces are
invariant. The Haar average has the same properties. Hence \(\Pi\)
commutes with \(H\), its spectral calculus and its closed form.

Fix real vectors \(\alpha_e\in\mathbb R^3\), set

\[
A_e=\sum_a\alpha_{ea}T_a,\qquad
D=\sum_{e,a}\alpha_{ea}X_{e,a},\qquad
(T_tf)(U)=f((e^{-tA_e}U_e)_e).
\]

The notation \(T_t\) is the requested translation, distinct from the
three basis matrices \(T_a\). It is the unitary group \(e^{-tD}\).
Its generator is the skew-adjoint closure of the displayed derivative
on smooth functions, obtained directly from this complete compact
group flow. It preserves all Sobolev spaces and commutes with the
electric kinetic operator, not generally with \(V\).

For every fixed \(k,m\), the smooth vector has the Sobolev Taylor formula

\[
T_t\psi=\sum_{j=0}^m\frac{(-t)^j}{j!}D^j\psi
+O_{H^k}(|t|^{m+1}).
\]

Indeed the integral remainder is bounded by
\(|t|^{m+1}\|D^{m+1}\psi\|_{H^k}/(m+1)!\), since translations are
isometries for the Sobolev norms defined by the free Laplacian.
Applying the bounded \(\Pi\) or the smooth ground-state rank-one
projection preserves these estimates. All differentiations and
energy expansions below are consequently valid in the actual form
domain, and even in each fixed higher Sobolev norm.

## 2. Exact derivative intertwining and Haar moments

For any fixed \(A\in\mathfrak{su}(2)\), direct substitution gives the
operator identity on smooth functions

\[
\mathcal G_gX_{e,A}\mathcal G_g^{-1}
=X_{e,\operatorname{Ad}_{g_{s(e)}^{-1}}A}.
\tag{2.1}
\]

The target multiplication cancels; the adjoint transformation is at
the source, not at the target. Thus on an invariant smooth \(f\),
\(\mathcal G_gD^jf=D_g^jf\), where \(D_g\) replaces every
\(A_e\) by \(\operatorname{Ad}_{g_{s(e)}^{-1}}A_e\).

Adjoint action preserves \(-2\operatorname{tr}(AB)\) and its real
coefficient vectors, and is the full rotation action on
\(\mathbb R^3\). The Haar average of a rotated vector is zero:
it is fixed by all rotations, whose only common fixed vector is zero.
For two fixed vectors \(a,b\), the averaged matrix
\(\int(Ra)(Rb)^{\mathsf T}dR\) commutes with every rotation and hence
is a scalar multiple of the identity. Its trace is \(a\cdot b\).
Therefore

\[
\int(Ra)_i\,dR=0,\qquad
\int(Ra)_i(Rb)_j\,dR=\frac{a\cdot b}{3}\delta_{ij}.
\tag{2.2}
\]

Gauge variables at distinct vertices are independent. Applying (2.2)
to (2.1) gives, for every smooth invariant \(f\),

\[
\boxed{\Pi Df=0,}
\tag{2.3}
\]

\[
\boxed{\Pi D^2f=\mathcal M f,\qquad
\mathcal M=\frac13\sum_{v\in\mathsf V}
\sum_{\substack{e,f\in\mathsf E\\s(e)=s(f)=v}}
(\alpha_e\cdot\alpha_f)\sum_{a=1}^3X_{e,a}X_{f,a}.}
\tag{2.4}
\]

The pair sum is ordered and includes \(e=f\). For a distinct-edge
pair the two ordered terms are both present; no factor two has
been suppressed. For a repeated edge the diagonal color moment
selects \(X_{e,a}^2\), so no commutator term is omitted.
Equivalently \(\Pi D\Pi=0\), \(\Pi D^2\Pi=\mathcal M\Pi\) on smooth
inputs. The operator \(\mathcal M\) is gauge invariant by its same-source
color contractions, or by its construction as the conjugated average
of \(D^2\). Its quadratic form is nonpositive: integration by parts
expresses \(-\langle f,\mathcal Mf\rangle\) as a sum with Gram matrices
\((\alpha_e\cdot\alpha_f)\), each positive semidefinite.

This projection identity is not the statement that \(D\psi=0\).
Writing \(Y_{e,a}f(U)=\left.\frac d{du}\right|_0f(U_e e^{uT_a})\),
the actual Gauss derivative at \(v\) is

\[
\sum_{s(e)=v}X_{e,a}-\sum_{r(e)=v}Y_{e,a}.
\]

It annihilates \(\psi\). A general \(D\) contains only the specified
left multiplications and is not that Gauss generator.

### Reversing an edge

The exact reversal is \(U'_e=U_e^{-1}\). Under it
\((e^{-tA_e}U_e)^{-1}=U'_e e^{tA_e}\). Thus the pullback of \(D\)
on that edge is \(-Y_{e,A_e}\), and the translation becomes right
multiplication with the opposite generator sign. Right derivatives
transform by \(\operatorname{Ad}_{g_{r(e)}^{-1}}\), so their contractions
are grouped at targets. The new target is the old source, exactly
preserving (2.4). To rewrite a right derivative as a left derivative
one must use \(Y_{e,A}=X_{e,\operatorname{Ad}_{U_e}A}\), with its
configuration-dependent coefficient. Keeping the old constant
\(\alpha_e\) while swapping source and target would not be the same
translation.

## 3. Exact centering and complete leading norm

Define the requested overlap, centered state and orthogonal projection

\[
c(t)=\langle\psi,T_t\psi\rangle,\qquad
\chi_t=\Pi T_t\psi-c(t)\psi,\qquad
\mathcal P=\Pi-|\psi\rangle\langle\psi|.
\]

Since \(\Pi\psi=\psi\), \(\chi_t=\mathcal PT_t\psi\).
It is invariant, orthogonal to the actual vacuum, and belongs to
every fixed Sobolev space. No normalization of \(\chi_t\) is presumed.
Reality of \(\psi,T_t\) and unitarity give \(c(-t)=c(t)\in\mathbb R\).
Write

\[
S=\|D\psi\|_\lambda^2,\qquad m_4=\|D^2\psi\|_\lambda^2 .
\]

Skew-adjointness and (2.3) give

\[
c'(0)=0,\quad c''(0)=-S,\quad
\left.\frac d{dt}\Pi T_t\psi\right|_0=0,\quad
\left.\frac{d^2}{dt^2}\Pi T_t\psi\right|_0=\mathcal M\psi .
\]

The fourth overlap derivative is \(m_4\). In particular

\[
c(t)=1-\frac S2t^2+\frac{m_4}{24}t^4+O(t^6).
\tag{3.1}
\]

Because \(\langle\psi,\mathcal M\psi\rangle
=\langle\psi,D^2\psi\rangle=-S\), the exact centered second derivative is

\[
\eta=\chi''_0=\mathcal M\psi+S\psi,\qquad \eta\perp\psi,
\qquad
\boxed{\chi_t=\frac{t^2}{2}\eta+O_{H^k}(|t|^3).}
\tag{3.2}
\]

The complete leading squared norm is consequently

\[
\boxed{\|\chi_t\|^2
=\frac{t^4}{4}\left(\|\mathcal M\psi\|^2-S^2\right)+O(|t|^5)
=\frac{t^4}{4}\|\eta\|^2+O(|t|^5).}
\tag{3.3}
\]

To see the vacuum subtraction explicitly, the projected uncentered norm is

\[
\|\Pi T_t\psi\|^2
=1-St^2+t^4\left(\frac{\|\mathcal M\psi\|^2}{4}
+\frac{m_4}{12}\right)+O(|t|^5).
\]

The overlap square is
\(c(t)^2=1-St^2+t^4(S^2/4+m_4/12)+O(t^6)\).
Their exact difference is \(\|\chi_t\|^2\), proving all cancellations
and factors in (3.3). No general evenness of the projected vector is
used to improve the error term.

## 4. Exact energy coefficient and resolution of degeneracy

The ground-state product rule and Haar integration by parts give

\[
q_0(\psi F,\psi F)
=\kappa\sum_{e,a}\int|X_{e,a}F|^2\psi^2\,d\lambda.
\tag{4.1}
\]

The eigen-equation for the full \(V\) is what cancels its explicit
zeroth-order terms. All potential dependence remains in \(\psi\).
Since \(q_0(\psi,\cdot)=0\), centering does not change the
vacuum-subtracted form of \(\Pi T_t\psi\). Its complete leading value is

\[
\boxed{q_0(\chi_t,\chi_t)
=\frac{t^4}{4}q_0(\eta,\eta)+O(|t|^5).}
\tag{4.2}
\]

Here the coefficient is fully specified on the actual vacuum by

\[
q_0(\eta,\eta)
=\kappa\sum_{e,a}\int
\left|X_{e,a}\left(\frac{\mathcal M\psi}{\psi}\right)\right|^2
\psi^2\,d\lambda .
\tag{4.3}
\]

The \(H^1\) Taylor remainder proves (4.2) using continuity of the
closed form, not a formal multiplication by an unbounded operator.
Writing \(\ell=\log\rho=2\log\psi\) makes the coefficient function explicit:

\[
\frac{\eta}{\psi}
=S+\frac13\sum_v\sum_{s(e)=s(f)=v}
(\alpha_e\cdot\alpha_f)\sum_a
\left(\frac12X_{e,a}X_{f,a}\ell
+\frac14(X_{e,a}\ell)(X_{f,a}\ell)\right).
\tag{4.4}
\]

Its \(\rho\)-mean is zero, and (3.3) is one quarter of its actual-vacuum
variance times \(t^4\).

There is no unresolved assumption about \(\eta\ne0\). Every second
derivative in \(\mathcal M\) has Haar integral zero. Thus

\[
\eta=0\ \Longrightarrow\
0=\int\eta\,d\lambda=S\int\psi\,d\lambda
\ \Longrightarrow\ S=0\ \Longrightarrow\ D\psi=0,
\]

using strict positivity of \(\psi\). The last equality makes
\(T_t\psi=\psi\) for all \(t\), by its complete translation flow.
Conversely \(D\psi=0\) implies \(\eta=0\) and \(\chi_t=0\) identically.
We have proved the exact classification

\[
\boxed{\eta=0\ \Longleftrightarrow\ D\psi=0\
\Longleftrightarrow\ T_t\psi=\psi\ \text{for all }t\
\Longleftrightarrow\ \chi_t=0\ \text{for all }t.}
\tag{4.5}
\]

It can also be tested directly on the specified potential:
\(D\psi=0\) implies \((DV)\psi=0\) by differentiating the ground
equation, because \(D\) commutes with the electric term. Positivity
gives \(DV=0\). Conversely \(DV=0\) makes \(V\) invariant under this
flow; then \(T_t\) commutes with \(H\), and uniqueness of its normalized
positive vacuum gives \(T_t\psi=\psi\). Thus the same alternatives
are equivalent to \(DV=0\) or \(DV\ne0\), without replacing the vacuum.

In the nontrivial alternative the coefficients in (3.3) and (4.2)
are strictly positive: \(\eta\ne0\), \(\eta\perp\psi\), and (4.1)
shows that zero energy would force \(\eta/\psi\) constant and hence
\(\eta=0\). For all sufficiently small nonzero \(t\), the actual
excitation quotient is therefore

\[
\frac{q_0(\chi_t,\chi_t)}{\|\chi_t\|^2}
=\frac{q_0(\eta,\eta)}{\|\eta\|^2}+O(|t|).
\tag{4.6}
\]

In the trivial alternative both numerator and denominator vanish
identically, so there is no state to normalize. The unsubtracted
Hamiltonian form is exactly \(q_H(\chi_t)=q_0(\chi_t)+E\|\chi_t\|^2\).
No uniform lower bound or spatial-limit assertion is extracted from
these fixed finite-graph statements.

## 5. The specified native flux: exact class convolution

Now take the full open box \(\{-L,\ldots,L\}^3\), \(L\geq2\), with
all elementary faces, and the exact field

\[
h_1(n)=\exp(-\theta n_2H_c),\quad h_2(n)=h_3(n)=I,\qquad
H_c=i\sigma_3=-2T_3.
\tag{5.1}
\]

Its fixed generators in the preceding notation are
\(A_{(n,1)}=-n_2H_c=2n_2T_3\), all other \(A_e=0\).
There is at most one translated outgoing edge at each vertex.

For any invariant \(f\), applying its invariance to
\((T_hf)(\beta_gU)\) replaces \(h_e^{-1}\) by
\(g_{s(e)}^{-1}h_e^{-1}g_{s(e)}\).
Because no two nontrivially translated edges share a source, the
vertex Haar integrals separate into independent single-edge class
averages. Define their product on the entire Hilbert space by

\[
(K_\theta f)(U)
=\int\prod_{\substack{e=(n,1)}}dk_e\
f\bigl((k_e^{-1}h_e(\theta)^{-1}k_e\,U_e)_{e=(n,1)},
       (U_e)_{e\not\parallel1}\bigr).
\]

Trivial factors may be omitted. It follows exactly that

\[
\boxed{\Pi T_h\Pi=K_\theta\Pi.}
\tag{5.2}
\]

This factorization would not follow for a general packet with several
translated outgoing edges at one vertex.

On the spin-\(j\) matrix coefficients of edge \(e=(n,1)\), Schur's
lemma gives the scalar average
\(\chi_j(h_e)/(2j+1)\); its trace fixes the scalar without an omitted
multiplicity. With \(x=\theta n_2\), the eigenvalues of \(h_e\) are
\(e^{\pm ix}\), so the exact multiplier is

\[
m_j(x)=\frac{\sin((2j+1)x)}{(2j+1)\sin x}
=\frac1{2j+1}\sum_{m=-j}^{j}e^{2imx}.
\tag{5.3}
\]

The finite sum specifies the continuous values where \(\sin x=0\).
It is real, bounded in absolute value by one, and even in \(x\).
Thus \(K_\theta\) is a self-adjoint contraction, commutes with every
electric Laplacian and with \(\Pi\), and is exactly even in \(\theta\).
It is positivity preserving as an average, but its spectral
multipliers need not be nonnegative.

Since \(\sum_{m=-j}^jm^2=j(j+1)(2j+1)/3\), (5.3) gives the exact
quadratic coefficient
\(m_j(x)=1-\frac23j(j+1)x^2+O_j(x^4)\).
The fourth scalar Taylor remainder is bounded by a constant times
\(x^4[j(j+1)]^2\). On the fixed finite graph, product expansion or
the averaged-flow fourth-order remainder therefore proves

\[
K_\theta f=f-\frac23\theta^2\Gamma f+O_{H^k}(\theta^4),\qquad
\Gamma=\sum_{e=(n,1)}n_2^2(-\Delta_e^T)
\tag{5.4}
\]

for every smooth fixed \(f\). More explicitly, the remainder is bounded
as an operator \(H^{k+4}\to H^k\) by \(C_{L,k}\theta^4\).
There is no same-\(H^k\) operator-norm expansion with an unbounded
coefficient silently treated as bounded.

## 6. Native-flux norm, energy and strict variance

Let \(\gamma=\langle\psi,\Gamma\psi\rangle\) and
\(v=(\Gamma-\gamma)\psi\). Combining (5.2)--(5.4) with exact centering
gives

\[
\chi_\theta=-\frac23\theta^2v+O_{H^k}(\theta^4),
\]

\[
\boxed{\|\chi_\theta\|^2
=\frac49\theta^4\operatorname{Var}_\psi(\Gamma)+O(\theta^6),\qquad
q_0(\chi_\theta)=\frac49\theta^4q_0(v)+O(\theta^6),}
\tag{6.1}
\]

where \(\operatorname{Var}_\psi(\Gamma)=\|v\|^2\).
These error orders use the exact evenness just proved. Here
\(\mathcal M=-4\Gamma/3\), so the signs and constants also agree
directly with the general formula (3.2).

For this full box the variance is strictly positive for every \(b>0\)
and \(\kappa>0\); no strong-coupling assumption is needed. Suppose it
were zero. Then \(\Gamma\psi=\gamma\psi\). Haar integration annihilates
each Laplacian, and \(\int\psi>0\), giving \(\gamma=0\).
Integration by parts now yields

\[
0=\langle\psi,\Gamma\psi\rangle
=\sum_{e=(n,1),\,n_2\ne0}n_2^2\sum_a\|X_{e,a}\psi\|^2 .
\]

Every displayed derivative vanishes; connectedness of each edge group
makes \(\psi\) independent of all these links. The full kinetic
operator applied to \(\psi\) is independent of each such link as
well. Dividing the original eigen-equation by the positive \(\psi\)
would force the entire Wilson potential to be independent of it.

Choose the specific link \(e=((0,1,0),1)\). Both endpoints lie in the
box and it has four elementary incident faces for \(L\geq2\). With
all other links set to the identity, those four faces have trace
\(\operatorname{tr}U_e\), independently of their orientation, while
every other face has trace 2. Thus the full potential on this fiber is

\[
V=4b(2-\operatorname{tr}U_e),
\]

which is nonconstant for \(b>0\). This is the required contradiction.
Consequently both leading coefficients in (6.1) are strictly positive,
and the centered projected flux state is nonzero for sufficiently
small nonzero \(\theta\). Its finite excitation quotient is

\[
\frac{q_0(\chi_\theta)}{\|\chi_\theta\|^2}
=\frac{q_0((\Gamma-\gamma)\psi)}
       {\operatorname{Var}_\psi(\Gamma)}+O(\theta^2).
\tag{6.2}
\]

Neither its value nor a spatially uniform estimate has been presumed.
The original \(H\) quotient is (6.2) plus the retained ground energy \(E\).

## 7. Bounded primary-literature check and exact relevance

A bounded search located and inspected the following primary papers at
the indicated equations. They establish relevant projected-state
constructions; no statement of novelty or exhaustive absence is inferred.

1. T. Thiemann and O. Winkler, *Gauge Field Theory Coherent States
   (GCS): II. Peakedness Properties*, Classical and Quantum Gravity
   18 (2001), 2561-2636. Section 5, Definition 5.1, equations (5.1)--(5.2)
   explicitly average graph coherent states over vertex Haar variables;
   Lemma 5.1 gives the invariant spin-network expansion, and Lemma 5.2,
   equation (5.7), relates projected overlaps to a gauge integral.
   These are the same compact projection map \(\Phi\mapsto\Pi\Phi\).
   This note instead inserts \(\Phi=T_t\psi\), the translated actual
   interacting vacuum, and subtracts its exact vacuum component.
   [Primary preprint, Section 5](https://arxiv.org/pdf/hep-th/0005237),
   [published article](https://doi.org/10.1088/0264-9381/18/14/301).

2. B. Bahr and T. Thiemann, *Gauge-invariant coherent states for loop
   quantum gravity: II. Non-Abelian gauge groups*, Classical and Quantum
   Gravity 26 (2009), 045012. Equations (2.2)--(2.5) use
   \(L^2(SU(2)^E)\), vertex \(SU(2)^V\) gauge action and its compact Haar
   projector. Section 4.2, equation (4.6), defines the projected
   coherent states. Its displayed source/target pullback agrees with
   ours; the inverse pullback is obtained by vertex inversion in Haar
   measure. Their heat-kernel coherent
   seed is not identified with the exact Wilson ground state here;
   only the displayed projection map is shared.
   [Primary preprint, equations (2.2)--(2.5) and (4.6)](https://arxiv.org/pdf/0709.4636),
   [published article](https://doi.org/10.1088/0264-9381/26/4/045012).

3. I. I. Kogan and A. Kovner, *A variational approach to the QCD wave
   functional: Dynamical mass generation and confinement*, Physical
   Review D 52 (1995), 3719-3734. Equation (2.9) displays a Gaussian
   seed with a classical-field shift; equation (2.12) projects a
   Gaussian seed over gauge transformations and expressly specializes
   to zero classical shift. Equations (3.1)--(3.2) retain the projected
   overlap in expectation values. This is related variational
   provenance, not a proof that their continuum ansatz equals a
   translated finite-box Wilson vacuum, and none of their approximate
   dynamical conclusions is used here.
   [Primary preprint, equations (2.9), (2.12), (3.1)--(3.2)](https://arxiv.org/pdf/hep-th/9408081),
   [published article](https://doi.org/10.1103/PhysRevD.52.3719).

The exact common morphism is the bounded compact operator
\(\Phi\mapsto\Pi\Phi\), followed in this calculation by
\(\Pi\Phi\mapsto(\Pi-|\psi\rangle\langle\psi|)\Phi\).
Semiclassical peakedness, a Gaussian ansatz and continuum dynamics
are not transferred along that map without proof.

## 8. Independent arithmetic diagnostic

A separate bounded exact computation enumerated all 24 proper signed
coordinate-permutation rotations. It verified all 9 first-moment
entries and all 81 second-moment entries in (2.2). Rotational invariance
above, not the finite enumeration, proves the full Haar identities.
The same replay checked the quadratic character coefficient for
dimensions \(1,\ldots,8\), and the exact flux factor
\((1/4)(4/3)^2=4/9\). All tests passed. The operator/domain arguments
and the strictly positive interacting-vacuum variance are proved
explicitly in Sections 1--6.

## 9. Original-coordinate, reference-frame and exact-energy addendum

8 September 2026. The entire companion source
../magnetic_translation_true_vacuum.md was independently read, including
its original-coordinate subsection and equations (2.4), (4.5), and
(6.1)--(6.3). The audited source SHA-256 is
 d02615ef717ba5248ef7cdc86a220443cba9ca0ee1e8fd967e03917d0c7ebaff.
The completed source was subsequently reread after the scope/typesetting
changes and the new discrete-representation Section 7; its current
audited SHA-256 through companion Section 7 is
 d2feea08df82780497f4b58890894b290be9786c18a5575be0fcc6dfbc683de1.
Section 10 below records the additional proof.
The original period block was also checked against
../retained_cusp_nonlinear_bridge.md. The following checks preserve its
original variables, metric, reference and transport convention.

### 9.1 Exact coordinate and gauge maps

Write \(m=m_T\), \(q=q_T\), retain \(L_T\), and
\(D=L_Tq+6m^2>0\), without changing their values. In the original real
coordinate order
\((x_1,x_2,x_3,x_4)=(\operatorname{Re}z_1,\operatorname{Im}z_1,
\operatorname{Re}z_2,\operatorname{Im}z_2)\), the exact imaginary block is

\[
B=\begin{pmatrix}6m&L_T\\-q&m\end{pmatrix},\qquad
B^{-1}=\frac1D\begin{pmatrix}m&-L_T\\q&6m\end{pmatrix}.
\]

The full covered period map, in the order separating real and imaginary
coordinates, has blocks
\(\begin{psmallmatrix}A&M I\\ B&0\end{psmallmatrix}\), whose inverse is
\(\begin{psmallmatrix}0&B^{-1}\\ M^{-1}I&-M^{-1}AB^{-1}\end{psmallmatrix}\).
Consequently the compact coordinates are exactly
\((u_1,u_2)^t=B^{-1}(x_2,x_4)^t\); this conclusion neither removes the
real block \(A\) nor changes the covered real period \(M\).

The permutation
\[
(y_0,y_1,y_2,y_3)=(x_3,x_2,x_4,x_1)
\]
is orthogonal and has four inversions, hence determinant \(+1\).
In these coordinates
\[
u_1=\frac{my_1-L_Ty_2}{D},\qquad
u_2=\frac{qy_1+6my_2}{D},\qquad
du_1\wedge du_2=\frac{6m^2+L_Tq}{D^2}\,dy_1\wedge dy_2
              =D^{-1}dy_1\wedge dy_2 .
\]
In particular \(y_0\) is a Euclidean temporal coordinate and the three
displayed spatial coordinates retain their Euclidean lengths.

For \(H_c=i\sigma_3=-2T_3\), the original connection is therefore
\[
A_{\rm orig}=\frac{2\pi H_c}{D^2}
(my_1-L_Ty_2)(q\,dy_1+6m\,dy_2).
\]
Let \(\mathfrak b=2\pi/D\) and retain the full polynomial
\[
f=\frac{2\pi}{D^2}
\left(\frac{mq}{2}y_1^2-L_Tq\,y_1y_2-3mL_Ty_2^2\right).
\]
Its derivatives are
\[
\partial_1 f=\frac{2\pi}{D^2}(mqy_1-L_Tqy_2),\qquad
\partial_2 f=\frac{2\pi}{D^2}(-L_Tqy_1-6mL_Ty_2).
\]
Adding \(\mathfrak b y_1dy_2\) to \(df\) gives exactly the two components
of \(A_{\rm orig}/H_c\): the second component uses
\(D-L_Tq=6m^2\). Thus
\[
A_{\rm orig}=\mathfrak b H_c y_1dy_2+H_cdf.
\]
All values commute with \(H_c\), so the original gauge convention
\(A^g=g^{-1}Ag+g^{-1}dg\), first with \(g_1=e^{-H_cf}\) and then with
\(g_2=e^{-\mathfrak bH_cy_1y_2}\), gives
\[
A_{\rm orig}^{g_1}=\mathfrak b H_c y_1dy_2,\qquad
(A_{\rm orig}^{g_1})^{g_2}=-\mathfrak b H_c y_2dy_1.
\]
These are gauge maps of the actual connection, not discarded exact
terms in the original presentation.

On an edge from \(y=an\) to \(y+ae_1\), the last connection integrates
to \(-\mathfrak b a^2 n_2H_c\). Ordinary parallel transport for
\(d+A\) solves \(\dot P=-A(\dot y)P\); its inverse consequently has
the plus-integral exponent. Hence, with
\(\theta=\mathfrak b a^2=2\pi a^2/D\),
\[
h_1(n)=e^{-\theta n_2H_c},\qquad h_2(n)=h_3(n)=I.
\]
Its positively oriented 12-face product is
\(e^{-\theta n_2H_c}e^{+\theta(n_2+1)H_c}=e^{+\theta H_c}\);
the 13 and 23 products are \(I\). These formulas concern the specified
nonwrapping physical patch. They do not replace the periodic transition
links, which the companion source explicitly retains.

### 9.2 Reference-frame covariance, with representation conventions

Let \(M_e\) be magnetic inverse transport and \(R_e\) the flat reference
in the same endpoint frames. The background variable used for the left
translation is \(h_e=M_eR_e^{-1}\). If both change frame, direct
multiplication gives
\[
(g_sM_eg_t^{-1})(g_sR_eg_t^{-1})^{-1}
=g_sM_eR_e^{-1}g_s^{-1}=g_sh_eg_s^{-1}.
\]
The reference may be \(I\) in the final fixed frame above. It is generally
not \(I\) after a nonconstant vertex-frame change; retaining its transformed
value is essential for this identity.

The companion uses the representation
\(R_gF(U)=F(g^{-1}\!\cdot U)\), whereas Section 2 above used the
inverse pullback \(\mathcal G_gF(U)=F(g\cdot U)\).
Thus \(R_g=\mathcal G_{g^{-1}}\), with the same Haar projection.
For each configuration \(U\),
\[
(R_gT_hR_g^{-1}F)(U)
=F\bigl((g_s h_e^{-1}g_s^{-1}U_e)_e\bigr)
=(T_{h'}F)(U),\qquad h'_e=g_sh_eg_s^{-1}.
\]
Differentiating gives
\(R_gX_e(A)R_g^{-1}=X_e(\operatorname{Ad}_{g_s}A)\);
this is exactly the inverse-pullback version of Section 2, not a
contradictory adjoint sign. Its first and second Haar moments are
unchanged. This proves the stated background-to-state covariance with
the original orientation and chosen reference.

### 9.3 Exact finite energies and all-face derivative signs

Retain \(H=-\kappa\sum_e\Delta_e^T+V\), its actual normalized positive
ground state \(\psi\), its ground energy \(E\), and
\(\mathcal A=H-E\geq0\). Every translation is unitary and preserves
all Sobolev spaces. Bi-invariance of the Casimir gives
\[
T_h^*HT_h=H+V(hU)-V(U).
\]
Here the potential argument is \(hU\), not \(h^{-1}U\), because
\(T_h^*F(U)=F(hU)\). Applying this identity to \(\psi\), and using
the orthogonal form decomposition under \(\Pi\), proves
\[
0\leq \mathfrak q_{\mathcal A}[\Pi T_h\psi]
\leq\mathfrak q_{\mathcal A}[T_h\psi]
=\int\psi^2\,[V(hU)-V(U)]\,dU .
\]
This verifies companion (2.4) without substituting a Haar-independent
vacuum or a classical magnetic action for the actual vacuum expectation.

For the native flux, the bounded self-adjoint class-convolution operator
\(K=K_\theta\) preserves every Sobolev space and commutes with the
electric operator. On the smooth vector \(\psi\),
\[
[K,[H,K]]=2KHK-K^2H-HK^2.
\]
Taking the vacuum expectation and using \(H\psi=E\psi\) gives
\[
\frac12\langle\psi,[K,[H,K]]\psi\rangle
=\langle K\psi,HK\psi\rangle-E\|K\psi\|^2
=\mathfrak q_{\mathcal A}[K\psi].
\]
The electric commutator vanishes, so replacing \(H\) by \(V\) in the
double commutator is exact. This proves both equalities in companion
(4.5). Centering by the vacuum leaves this excitation form unchanged.

For \(\Gamma=\sum_{e=(n,1),a}n_2^2(-X_{e,a}^2)\), commutation with
the electric operator and the eigen-equation give
\[
(H-E)\Gamma\psi=[V,\Gamma]\psi .
\]
The product rule, retaining the minus sign inside \(\Gamma\), gives
for every smooth \(F\)
\[
[V,\Gamma]F
=\sum_{e=(n,1),a}n_2^2
\bigl((X_{e,a}^2V)F+2(X_{e,a}V)X_{e,a}F\bigr).
\]
The two displayed signs are positive. Put \(v=(\Gamma-\gamma)\psi\)
with \(\gamma=\langle\psi,\Gamma\psi\rangle\). Since
\(\langle\psi,[V,\Gamma]\psi\rangle
=\langle\psi,(H-E)\Gamma\psi\rangle=0\), one obtains
\[
\mathfrak q_{\mathcal A}[v]
=\langle\Gamma\psi,[V,\Gamma]\psi\rangle
=\frac12\langle\psi,[\Gamma,[V,\Gamma]]\psi\rangle .
\]
For the last equality expand the double commutator with \(H\) first,
use the eigen-equation, and then use \([H,\Gamma]=[V,\Gamma]\).
All products are defined: \(\psi\), \(V\psi\) and their displayed
derivatives are smooth on the compact configuration manifold.

Each elementary open-box face uses four distinct edges. If an edge
belongs to that face, its trace is a fundamental matrix coefficient in
that edge (possibly an inverse coefficient); the Casimir eigenvalue
is \(3/4\) in either orientation. With the complete face set retained,
\[
q_p=\frac34\sum_{\substack{e\in\partial p\\e=(n,1)}}n_2^2,\qquad
\Gamma W_p=q_pW_p,\qquad
\Gamma V=-b\sum_pq_pW_p,\qquad
X_{e,a}V=-b\sum_{p\ni e}X_{e,a}W_p .
\]
In particular direction-13 faces remain in these formulas even though
their chosen background curvature is the identity. This checks
companion (6.1)--(6.3) on the full interacting model.

An independent exact symbolic replay checked the determinant and inverse
of \(B\), the orientation and orthogonality of the permutation, and both
components of the polynomial gauge identity. All passed. Together with
Sections 1--8, this closes the bounded audit with no mathematical error
found. The result is a finite-regulator theorem with the stated actual
vacuum; it supplies no unproved joint-volume, continuum or spectral-limit
claim.

## 10. Exact discrete electric-channel map

8 September 2026. Companion Section 7 is correct, including the negative
double-commutator matrix sign and the mode of convergence. The full
source was reread at the final hash recorded in Section 9.

For each finite edge-spin tuple \(\boldsymbol j=(j_e)_e\), the full
product Peter--Weyl block is finite dimensional and invariant under
every vertex transformation. Let \(P_{\boldsymbol j}\) be its orthogonal
projection. Thus \(P_{\boldsymbol j}\Pi=\Pi P_{\boldsymbol j}\), and
\[
\mathcal H_{\rm phys}
=\mathop{\widehat{\bigoplus}}_{\boldsymbol j}
\Pi P_{\boldsymbol j}\mathcal H .
\]
Choose an orthonormal basis \(\Phi_s\) in each nonzero summand, retaining
its invariant multiplicity label. The map
\[
\mathcal U:\mathcal H_{\rm phys}\longrightarrow\ell^2(\{s\}),\qquad
\mathcal U F=(\langle\Phi_s,F\rangle)_s
\]
is unitary: orthogonality proves isometry on finite sums; completeness
follows because the bounded projection \(\Pi\) applied to the dense
finite Peter--Weyl sums is dense in its range. This also proves
surjectivity by completion.

The electric operator is diagonal with eigenvalues
\(\lambda_s=\kappa\sum_ej_e(j_e+1)\). The class-convolution operator is
scalar on each whole surrounding Peter--Weyl block, so it is scalar
on every invariant multiplicity component:
\[
\mathcal U K_\theta\mathcal U^{-1}
=\operatorname{diag}(k_s),\qquad
k_s=\prod_{e=(n,1)}
\frac{\sin((2j_e+1)\theta n_2)}
     {(2j_e+1)\sin(\theta n_2)} .
\]
The finite weight sum defines each factor at a vanishing denominator.
Each \(k_s\) is real and \(|k_s|\leq1\).

Put \(a_s=\langle\Phi_s,\psi\rangle\), retaining the actual interacting
ground state, so \(\sum_s|a_s|^2=1\). Unitarity and Parseval give exactly
\[
c_\theta=\sum_s|a_s|^2k_s,\qquad
\mathcal U\chi_\theta=(a_s(k_s-c_\theta))_s,\qquad
d_\theta=\sum_s|a_s|^2(k_s-c_\theta)^2 .
\]
The scalar sums converge absolutely because \(|k_s|\leq1\) and
\(|c_\theta|\leq1\). The vector converges in every Sobolev norm:
smoothness gives \(\sum_s(1+\lambda_s)^r|a_s|^2<\infty\) for each
fixed \(r\), and the extra multiplier has modulus at most 2.
In particular finite joint-spin cutoffs converge in the form domain,
with no new state or probability law substituted for the coefficients.

Retain the bounded multiplication operator \(V\), including its full
constant \(2bM\), and
\[
V_{st}=2bM\delta_{st}-b\sum_p\langle\Phi_s,W_p\Phi_t\rangle .
\]
Its double commutator \(B_\theta=[K_\theta,[V,K_\theta]]/2\) is bounded
with \(\|B_\theta\|\leq2\|V\|\), since \(K_\theta\) is a contraction.
The exact matrix entry is
\[
\langle\Phi_s,B_\theta\Phi_t\rangle
=\frac12\bigl(2k_sk_t-k_s^2-k_t^2\bigr)V_{st}
=-\frac12(k_s-k_t)^2V_{st}.
\]
For finite joint-spin cutoffs \(F_R\uparrow I\) on the physical Hilbert
space, the finite double sum is consequently
\[
-\frac12\sum_{s,t\in F_R}\overline{a_s}a_t
(k_s-k_t)^2V_{st}
=\langle F_R\psi,B_\theta F_R\psi\rangle .
\]
The difference from \(\langle\psi,B_\theta\psi\rangle\) is bounded by
\[
\|B_\theta\|\,\|F_R\psi-\psi\|
(\|F_R\psi\|+\|\psi\|),
\]
which tends to zero. By the exact energy identity already proved,
this limit equals \(n_\theta\). No absolute convergence of the
infinite double matrix sum is asserted or needed. The original scalar
constant contributes zero to this particular expression because it
is diagonal and \(k_s-k_s=0\); it remains in \(H\) and \(E\).
All off-diagonal face matrix elements remain present and need not
have individually nonnegative contributions.

Thus the continuous magnetic parameter, all discrete electric labels,
the physical projection and the exact interacting-vacuum norm/energy
are connected by the displayed unitary map, with the claimed domain
and limit properties proved. This closes the added finite-spin audit.

## 11. Finite-range energy matrix and full covariance

8 September 2026. The added companion Section 8 was read in full at
source SHA-256
a1d7e0817f153ce966b4cc4fcf149dba52521e21a587c390b88d5b322cbce198.
Its complete real-matrix identity and support assertion are correct.

Retain \(E_e=-\Delta_e^T\), the original positive ground state \(\psi\),
\(\gamma_e=\langle\psi,E_e\psi\rangle\), and
\(v_e=(E_e-\gamma_e)\psi\). Every \(v_e\) is smooth, real, invariant
and orthogonal to \(\psi\). Define
\[
C_{ef}=\langle v_e,v_f\rangle,\qquad
N_{ef}=\mathfrak q_{\mathcal A}(v_e,v_f).
\]
These are real symmetric positive-semidefinite Gram matrices. In
particular their entries need not be nonnegative.

The edge Casimirs commute for every pair, including \(e=f\). Expanding
the double commutator on the smooth vacuum gives
\[
\begin{split}
\langle\psi,[E_e,[H,E_f]]\psi\rangle
={}&\langle E_e\psi,HE_f\psi\rangle
 +\langle E_f\psi,HE_e\psi\rangle\\
 &-2E\langle E_e\psi,E_f\psi\rangle .
\end{split}
\]
Reality makes the first two scalars equal. Subtraction of the centered
vacuum components does not change the \(H-E\) form, so the expression
is exactly \(2N_{ef}\). Since every edge Casimir commutes with the
whole electric sum,
\[
N_{ef}=\frac12\langle\psi,[E_e,[V,E_f]]\psi\rangle .
\]
These are unbounded differential operators applied only to smooth
vectors; their products and integrations by parts are well-defined.

For an elementary face \(p\), if \(f\notin\partial p\), then
\([W_p,E_f]=0\). If \(f\in\partial p\), the product rule expresses
\([W_p,E_f]\) as derivatives only in the \(f\)-variable with coefficients
depending only on the four variables in \(\partial p\). For
\(e\notin\partial p\), each \(e\)-derivative therefore commutes with
every such coefficient and \(f\)-derivative. This proves
\[
[E_e,[W_p,E_f]]=0
\quad\hbox{unless }e,f\in\partial p .
\]
The constant in \(2-W_p\) has zero commutator; with its original
coefficient retained, the exact full-potential expression is
\[
N_{ef}=\frac b2\sum_{p:\,e,f\in\partial p}
\langle\psi,[E_e,[2-W_p,E_f]]\psi\rangle .
\]
This proves the stated numerator support without any vacuum
factorization. No analogous locality for \(C_{ef}\) follows or is
claimed.

For \(w_e=n_2^2\) on \(e=(n,1)\), and \(w_e=0\) otherwise,
\[
(\Gamma-\langle\Gamma\rangle)\psi=\sum_e w_ev_e,\qquad
\operatorname{Var}_\psi(\Gamma)=w^tCw,\qquad
\mathfrak q_{\mathcal A}[(\Gamma-\langle\Gamma\rangle)\psi]=w^tNw .
\]
The denominator is strictly positive for the native all-\(b>0\)
state by Section 6. Thus the finite-regulator small-angle quotient is
exactly \(w^tNw/(w^tCw)\). This establishes the precise
local-energy/full-covariance map and makes no claim about their
relative growth along a changing regulator.

## 12. Private preservation of the three primary sources

8 September 2026. Each of the three arXiv source URLs in Section 7 was
requested once and successfully downloaded into
literature_primary/Gauge_Projected_States_20260908 under the repository
root. SOURCE_PRESERVATION_RECEIPT.json records URLs, archive bytes,
SHA-256 values and the safe entry inventory. SOURCE_EXTRACTION_RECEIPT.json
records original authorship, titles, equation uses and the hashes of the
three unmodified TeX files selected after path and regular-file checks.
No figures, style files, executable entries or unrelated archive members
were extracted. No downloaded source was executed or compiled, and
nothing was included in canonical or public material.

The actual relevant source text was then read: Thiemann--Winkler lines
3029--3188 (internal labels def4.1, 4.1--4.7, la4.1--la4.2; these
labels differ from printed equation numbers), Bahr--Thiemann lines
250--314 and 878--925 (Gl:Projector and
Gl:DefinitionGaugeInvariantCoherentState), and Kogan--Kovner lines
325--509 (shifted Gaussian, projected ansatz labelled an, and the
normalized two-projection expectation). These sources verify the
specific projection/overlap statements recorded in Section 7.
