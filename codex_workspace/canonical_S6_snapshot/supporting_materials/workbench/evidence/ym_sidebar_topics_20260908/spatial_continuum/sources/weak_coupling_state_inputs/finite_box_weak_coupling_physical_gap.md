# The original finite-box SU(2) Hamiltonian at small positive coupling

8 September 2026. This note retains the full nonlinear Wilson Hamiltonian
and proves a limit of its actual physical eigenvalues at each fixed open
box. The maximal-tree map, Haar density, kinetic tensor, residual gauge
action, and harmonic comparison are all specified. The resulting
fixed-volume theorem does not identify an interacting continuum limit.

## 1. The unchanged operator and its physical space

Fix L at least 2, set m=2L, and use vertices n in {-L,...,L} cubed, all
positive contained nearest-neighbor edges, and all contained elementary
faces. Write V,E,P for these sets, with
\[
 |V|=(m+1)^3,\quad |E|=3m(m+1)^2,\quad |P|=3m^2(m+1).
\]
On the product Haar probability space of SU(2) link variables, use
\(T_a=-i\sigma_a/2\), left derivatives X_{e,a}, and
\(E_e=-\sum_aX_{e,a}^2\). Reverse traversal uses the inverse of the
same link. The trace W_p is the fundamental trace of the original
oriented four-edge word. With physical spacing a>0 and coupling g>0,
\[
 H_g=\frac{2g^2}{a}\sum_e E_e
       +\frac1{2g^2a}\sum_p(2-W_p).
\tag{1}
\]
Thus \(\kappa=2g^2/a\), \(b=1/(2g^2a)\), and
\(\xi=1/(4g^4)\) remain the previous parameters. In the original
metric \(c(A,B)=-\operatorname{tr}(AB)/2\),
\(-\Delta_e^c=4E_e\); (1) includes that factor. The scalar 2b|P|
is contained in its displayed potential and is not discarded.

Vertex gauge transformations act by \(U_e\mapsto h_sU_eh_t^{-1}\).
Their Haar average is an orthogonal projection. Its range is the
physical Hilbert space. The operator and form domains are the invariant
parts of H^2 and H^1 on the compact product group. Bounded smooth
multiplication by the potential preserves self-adjointness, compact
resolvent and these domains. The positive unit ground state is unique:
the modulus inequality gives a nonnegative minimizer; elliptic
regularity and the maximum principle make it smooth and positive; and
integration by parts gives
\[
 q_{H_g-\mathcal E_g}(\psi_g f)
       =\frac{2g^2}{a}\sum_{e,a}\int\psi_g^2|X_{e,a}f|^2.
\tag{2}
\]
Dividing a second ground state by the positive smooth first one in
(2) proves uniqueness. Gauge transformations therefore fix this actual
vacuum. Let \(\mathcal E_0(g)\le\mathcal E_1(g)\le\cdots\)
be the physical eigenvalues, with multiplicity and index zero for the
ground state, and let \(\Delta_L(g,a)=\mathcal E_1(g)-\mathcal E_0(g)\).

## 2. Exact nonlinear maximal-tree coordinates, including measure

Root the graph at o=(-L,-L,-L). For each other vertex choose its parent
by decreasing the first coordinate, in the order 1,2,3, which exceeds
-L. These positively oriented parent edges form a tree \(\mathcal T\):
the sum of the three coordinate offsets strictly decreases toward o,
and every other vertex has one parent. There are |V|-1 tree edges.
Denote the remaining chords by \(\mathcal C\), of cardinality
\[
 r=|E|-|V|+1=2m^3+3m^2.
\tag{3}
\]
Let t_v(U) be the ordered holonomy on the tree path from o to v, with
t_o=I. Define, for every chord c from s to t,
\[
 Z_c=t_s(U)U_ct_t(U)^{-1}.
\tag{4}
\]
The coordinate map U -> ((U_e)_{e in tree},(Z_c)_{c in chords}) is a
smooth global bijection of product compact groups. Its inverse retains
the specified tree links, computes their same t_v, and sets
\(U_c=t_s^{-1}Z_ct_t\). For each fixed tree configuration the chord
changes are independent left and right translations of Haar measure.
Fubini therefore proves exact preservation of the full product Haar
probability measure by this bijection.

The gauge transformation h_v=t_v makes every tree link I and makes
each chord precisely Z_c. Under an arbitrary original gauge transformation
k, tree holonomies become \(t_v\mapsto k_ot_vk_v^{-1}\), so
\(Z_c\mapsto k_oZ_ck_o^{-1}\) simultaneously for all c. Consequently
\[
 \mathcal U:F\longmapsto F((Z_c(U))_c)
\tag{5}
\]
is an isometry from \(L^2(SU(2)^r,dZ)\) onto the subspace invariant
under based gauge transformations (k_o=I). To establish surjectivity on
L^2, first average a smooth function over the compact based gauge group.
In tree/chord variables its average is independent of the tree variables:
that group acts transitively on each tree-variable fibre and leaves Z
fixed. Smooth functions are dense and Haar averaging is an orthogonal
projection, so this equality extends by continuity to the entire invariant
L^2 subspace. No evaluation of an L^2 class on a measure-zero slice is
needed. The full physical
space corresponds exactly to simultaneous-conjugation-invariant F.
No quotient measure or residual gauge condition is omitted.

The exact transformed potential is
\(W(Z)=\sum_p(2-\operatorname{tr}U_p(Z))\), where tree links in
the original face word are I and chord links are Z_c or Z_c^{-1} with
their original orientation. For an edge e and generator T_a, define
the vector field \(\mathcal X_{e,a}\) on the chord manifold by varying
that single original edge through \(e^{tT_a}U_e\), starting from the
tree-I representative, recomputing (4), and differentiating at t=0.
This is an explicit smooth vector field: its coefficients are obtained
by the finite products and inverses (4), not a retained-loop approximation.
Here is its complete expression. Let \(\epsilon(v,e)\) be one when the
tree edge e lies on the root-to-v tree path, and zero otherwise. Write
\(L_{c,\alpha}F(Z)=\left.\frac d{dt}F(\ldots,e^{tT_\alpha}Z_c,\ldots)
\right|_{t=0}\) and
\(R_{c,\alpha}F(Z)=\left.\frac d{dt}F(\ldots,Z_ce^{tT_\alpha},\ldots)
\right|_{t=0}\). Then
\[
 \mathcal X_{e,\alpha}=
 \begin{cases}
 L_{e,\alpha},&e\in\mathcal C,\\
 \displaystyle\sum_{c\in\mathcal C}
 [\epsilon(s(c),e)L_{c,\alpha}-\epsilon(t(c),e)R_{c,\alpha}],
       &e\in\mathcal T.
 \end{cases}
\tag{5a}
\]
Indeed a varied tree edge changes each downstream t_v to
\(e^{tT_\alpha}\) at the tree-I representative; differentiating (4)
gives the stated left and right fields with the minus sign from the
inverse t_t. Each displayed field is divergence-free for product Haar.
Thus the exact transformed kinetic operator on smooth functions is
\(-(2g^2/a)\sum_{e,\alpha}\mathcal X_{e,\alpha}^{,2}\).
Gauge invariance of the original sum of squared derivatives shows that
the exact based-invariant Dirichlet form is
\[
 q_g[F]=\frac{2g^2}{a}\int\sum_{e,a}|\mathcal X_{e,a}F|^2dZ
                   +\frac1{2g^2a}\int W(Z)|F|^2dZ.
\tag{6}
\]
Indeed differentiation of (5) gives these fields at the representative;
changing tree representative rotates the three generator components at
each edge by an orthogonal adjoint matrix, preserving their summed squares.
The product-Haar identity just proved then integrates that pointwise
identity. Chord-edge variations alone supply a full tangent frame, since
they vary their own Z_c by left multiplication while leaving all other
chords fixed. Thus the form is elliptic on the compact chord manifold.
Its domain is H^1, its represented operator has domain H^2, and (5)
intertwines both closed forms and their self-adjoint operators. Restriction
to the residual invariant subspace preserves these statements.

## 3. The unique minimum and its exact linear coordinate maps

Each summand of W is nonnegative. For SU(2), trace equal to 2 forces
the group element to be I. If W=0, every face holonomy is I. Any
monotone path from the minimum corner o to a vertex consists of positive
coordinate steps; any two such words differ by interchanges of adjacent
steps in different directions. Each interchange is an actual contained
elementary square. Flatness therefore makes their holonomies identical.
For every positive edge s->t, append it to a monotone path to s and
compare with a monotone path to t. This gives t_s U_e=t_t, in particular
Z_c=I for all chords. Conversely those identities make every face I.
The potential has exactly one zero on the chord manifold, the identity
configuration. This proof uses the original open box, not a torus.

Use real edge and face cochains with their original counting inner
products. Define
\[
 (d_0 f)(e)=f(t)-f(s),\qquad
 (d_1 x)(n;i,j)=x_i(n)+x_j(n+e_i)-x_i(n+e_j)-x_j(n).
\tag{7}
\]
The target of d_0 is \(\mathbb R^E\), and that of d_1 is
\(\mathbb R^P\). Substitution proves d_1d_0=0. The same monotone
path interchange argument, now with additive real edge integrals,
proves \(\ker d_1=\operatorname{im}d_0\).

Let p_v(x) be the additive integral along the specified tree path, and
define \(T:\mathbb R^E\to\mathbb R^{\mathcal C}\) by
\[
 (Tx)_c=p_s(x)+x_c-p_t(x).
\tag{8}
\]
This is precisely the derivative of (4) in each of the three Lie-algebra
components. Let j insert chord coordinates into the full edge vector
with zero tree entries. Then Tj=I, and
\(\ker T=\operatorname{im}d_0\): one implication follows by
telescoping, and in the other the potentials p_v give x=d_0p when
all the chord identities (8) vanish. Put
\[
 G=TT^*,\quad R=T^*G^{-1/2},\quad K=\ker d_0^*,\quad C=d_1j.
\tag{9}
\]
G is strictly positive because T is surjective. The displayed R is an
isometry onto K: R^*R=I, its image is perpendicular to ker T, and the
dimensions agree. The map \(J=T^*G^{-1}\) is the inverse of T on K.
Since TJ=I=Tj, their difference is a gradient, giving
\[
 d_1J=C,\qquad d_1R=CG^{1/2},\qquad
 R^*d_1^*d_1R=G^{1/2}C^*CG^{1/2}.
\tag{10}
\]
These identities prove the metric relation between tree coordinates and
transverse edge cochains. In particular neither a tree metric nor a
Euclidean chord metric is silently substituted for the original kinetic
tensor. C is injective by ker d_1=im d_0 and the zero tree entries of j.

In the exponential chart \(Z_c=\exp(y_c^aT_a)\), the principal kinetic
matrix in (6) at zero is \(G\otimes I_3\), by differentiating (4).
The Taylor expansion of each original face word, using
\(\operatorname{tr}(T_aT_b)=-\delta_{ab}/2\), gives
\[
 W(y)=\frac14\sum_{a=1}^3\|Cy^a\|^2+O_L(|y|^3).
\tag{11}
\]
One can check the coefficient without choosing a logarithm of the whole
word: its first derivative is the signed sum of its edge generators,
its trace derivative is zero, and the second trace derivative is the
trace of that sum squared. The commutator terms have trace zero. Thus
the quadratic term of 2-tr is one quarter the squared signed sum.
All higher word terms remain in W. Their fixed-chart bound follows from
Taylor's integral remainder for the finite smooth word, not their removal.
Injectivity of C proves nondegeneracy of this unique minimum.

The Haar density in this chart is exactly
\[
 dZ=\mathcal J(y)\,dy,\qquad
 \mathcal J(y)=(16\pi^2)^{-r}
       \prod_{c\in\mathcal C}
       \left[\frac{\sin(|y_c|/2)}{|y_c|/2}\right]^2,
       \quad |y_c|<2\pi.
\tag{12}
\]
The continuous value at zero is used. Indeed unit-quaternion polar
coordinates have Haar measure \(\sin^2(r/2)dr,d\Omega/(4\pi^2)\);
division by the Cartesian polar Jacobian r^2 gives (12) for one factor.
Its integral over the radius-2pi chart is one. This retains the full
density and its factor 16pi squared for every original chord.

## 4. Exact open-box transverse frequencies

Set \(\lambda_j=4\sin^2(\pi j/[2(m+1)])\), j=0,...,m.
The complete positive squared singular values of d_1 on K are
\[
 \lambda_{j_1}+\lambda_{j_2}+\lambda_{j_3},
 \quad j_i\in\{0,\ldots,m\},\quad
 k=\#\{i:j_i>0\}\ge2,
 \quad\hbox{multiplicity }k-1.
\tag{13}
\]
We prove the boundary-sensitive formula. On the one-dimensional interval
with vertices l=0,...,m and edges l=0,...,m-1, let
\(Df(l)=f(l+1)-f(l)\). The vectors
\[
 v_0(l)=(m+1)^{-1/2},\qquad
 v_j(l)=\sqrt{\frac2{m+1}}\cos\frac{\pi j(l+1/2)}{m+1},
\]
\[
 w_j(l)=-\sqrt{\frac2{m+1}}\sin\frac{\pi j(l+1)}{m+1},
       \quad 1\le j\le m,
\tag{14}
\]
are orthonormal bases in their respective counting spaces. The geometric
sum formula for roots of unity, followed by the cosine and sine product
identities, proves their inner products; their counts equal the dimensions.
The difference-of-cosines formula gives
\(Dv_j=\sqrt{\lambda_j}w_j\), and taking the adjoint gives
\(D^*w_j=\sqrt{\lambda_j}v_j\). Here l=n_i+L is an explicit index
map, not a change of physical coordinates: edge midpoints remain
\(a(n+e_i/2)\).

Tensor these bases in the three coordinate directions. At a fixed triple
j, one-cochains have one basis vector in each direction i with j_i>0:
use w_{j_i} in that direction and v_{j_h} in the other two. These k
vectors are orthonormal. The gradient of the vertex tensor is the vector
with components \(s_i=\sqrt{\lambda_{j_i}}\). The oriented curl in
(7) has components \(s_i x_h-s_h x_i\). Expanding their squares gives
\[
 \sum_{i<h}|s_i x_h-s_h x_i|^2
  =\left(\sum_i s_i^2\right)\sum_i|x_i|^2
                  -\left|\sum_i s_i x_i\right|^2.
\tag{15}
\]
Consequently the orthogonal complement of the gradient has dimension k-1
and squared curl value \(\sum\lambda_{j_i}\). For k=1 it is zero
dimensional. This proves (13) on a complete tensor basis, with all open
boundaries included. Its total multiplicity is \(3m^2+2m^3=r\),
agreeing with (3), not an extra polarization count.

Since sine is strictly increasing on the relevant half interval, the
smallest frequency is
\[
 \sigma_{\min}=\sqrt8\sin\frac{\pi}{2(m+1)}.
\tag{16}
\]
It occurs exactly at triples (1,1,0),(1,0,1),(0,1,1), each with one
transverse component, hence has multiplicity three.

## 5. The comparison operator and the residual gauge constraint

Write \(\sigma_1,\ldots,\sigma_r\) for the positive square roots
in (13), with multiplicity. In the original chord coordinates rescaled
by the explicit map y=g x, the comparison form is the operator
\[
 H_{\rm osc}=\frac1a\left[-2\sum_{\alpha=1}^3\sum_{c,d\in\mathcal C}
                     G_{cd}\partial_{x_c^\alpha}\partial_{x_d^\alpha}
              +\frac18\sum_{a=1}^3\|Cx^a\|^2\right].
\tag{17}
\]
The kinetic term in (17) is written with ordinary coordinate derivatives;
its quadratic form is positive because G is positive definite. The exact
local Hilbert map is
\[
 F(\exp(gx))=g^{-3r/2}\mathcal J(gx)^{-1/2}f(x),
\tag{18}
\]
for functions supported inside this chart. By (12) this preserves their
norm exactly. In particular the rescaling has retained both its volume
power and its nonconstant Haar factor.

Let A^{ij}(y) be the full smooth principal matrix of the kinetic form
in (6), with A(0)=G tensor I_3. Under (18) the exact kinetic form is
\[
 \frac2a\int A^{ij}(gx)
 \left(\partial_i f-\frac g2(\partial_i\log\mathcal J)(gx)f\right)^*
 \left(\partial_j f-\frac g2(\partial_j\log\mathcal J)(gx)f\right)dx,
\tag{19}
\]
and its exact potential is multiplication by \(W(gx)/(2g^2a)\).
Equation (19) follows by differentiating the displayed density in (18)
inside (6). Every metric coefficient and density derivative remains in it.
On bounded x domains these forms converge to (17) by smoothness and (11).

The linear change x=G^{1/2}z in each color component uses the constant
Jacobian \(\det(G)^{3/2}\); multiplication by its square root is
part of the unitary change of L^2 coordinates. Diagonalize the positive
matrix \(G^{1/2}C^*CG^{1/2}\) by an orthogonal matrix. By (10) its
eigenvalues are exactly (13). Thus (17) is unitarily equivalent to
\[
 \sum_{\nu=1}^r\left[-\frac2a\Delta_{z_\nu}
                    +\frac{\sigma_\nu^2}{8a}|z_\nu|^2\right],
                  \quad z_\nu\in\mathbb R^3.
\tag{20}
\]
All the linear matrices act on spatial/chord indices only. Residual SU(2)
conjugation therefore remains simultaneous adjoint rotation of the r
three-component vectors, not r independently removed color rotations.

For a single real oscillator in (20), factorization with
\(\partial_z+\sigma z/4\) and its adjoint gives energy
\(\sigma/(2a)+n\sigma/a\), n=0,1,... . The Gaussian vacuum and
successive Hermite polynomials give a complete eigenbasis (equivalently,
their generating functions are complete in the Gaussian L^2 space).
Consequently the oscillator ground energy is
\[
 \mu_0=\frac3{2a}\sum_{\nu=1}^r\sigma_\nu.
\tag{21}
\]
It is a simultaneous-rotation singlet. Every one-quantum state transforms
as an adjoint vector, which has no invariant vector: invariance under all
three coordinate-axis rotations forces its components to vanish. Every
state with at least two quanta has excitation energy at least
\(2\sigma_{\min}/a\). This value is achieved by the invariant
quadratic \(\sum_a a^\dagger_{\nu,a}a^\dagger_{\nu,a}\) on a lowest
mode. There are six independent invariant quadratics among the three
lowest spatial modes: the contractions indexed by \(\nu\le\eta\).
For each ordered pair of vector indices, invariance of a bilinear tensor
under rotations forces it to be a scalar multiple of the identity
(first use the sign-changing half-turns to remove off-diagonal entries,
then quarter-turns to equate diagonal entries). Symmetry of creation
operators therefore gives precisely those six, with no additional
invariants at that energy. Thus the first physical oscillator excitation
has energy \(2\sigma_{\min}/a\) and multiplicity six.

## 6. Limit of actual physical eigenvalues, not a substitution of operators

Let \(\mu_k\) be the sorted eigenvalues of (20) on its simultaneous-
rotation-invariant space. We claim, for every fixed L,a,k,
\[
 \lim_{g\downarrow0}\mathcal E_k(g)=\mu_k.
\tag{22}
\]
Here is a form/min--max proof retaining the nonconstant coefficients.
All localization functions used below depend only on the chart radius
\(|y|\), so are invariant under the residual simultaneous rotations.

For the upper bound choose the first k+1 invariant oscillator eigenvectors,
multiply them by a smooth cutoff equal to one on |y|<=rho and supported
in |y|<2rho, and use (18). The number rho is fixed inside the exponential
chart. In x coordinates the cutoffs tend to one. The oscillator vectors
are polynomials times a decaying Gaussian. On this fixed y chart, A,
the density derivatives, and their first derivatives are bounded; moreover
\(W(gx)/(g^2)\le c_\rho |x|^2\), because W vanishes to second order.
The cutoff derivatives in (19) have an additional g factor. Dominated
convergence therefore gives the identity matrix as their norm Gram limit
and the oscillator energy matrix as their form Gram limit. These vectors
are independent for small g, remain exactly gauge invariant, and lie in
the full original form domain. The min--max principle gives
\(\limsup\mathcal E_k(g)\le\mu_k\).

For the lower bound fix any epsilon>0. By (11), positive definiteness and
smoothness, choose rho>0 so that on |y|<2rho the principal matrix and
the quadratic potential differ from their values in (17) by relative
form errors at most epsilon. The density is positive and smooth there.
After multiplying by its square root, the kinetic derivatives are
\(\partial_i-\tfrac12\partial_i\log\mathcal J\). The elementary
inequality
\(|u-v|^2\ge(1-\epsilon)|u|^2-(\epsilon^{-1}-1)|v|^2\)
shows that these bounded density derivatives cost at most
\(C_{\rho,\epsilon}g^2\|F\|^2\) in the original form. After
reducing rho or epsilon if needed, the local form is therefore bounded
below by (1-epsilon) times the full quadratic comparison form, minus
that displayed error. The constants are finite suprema of the original
coefficients on this fixed compact chart; they need not be independent
of L and are not treated as such.

Choose smooth invariant chi_0,chi_1 with chi_0 squared plus chi_1 squared
equal to one, chi_0 supported in |y|<2rho and equal to one on |y|<=rho.
For example use the cosine and sine of a smooth radial function constant
at 0 near the inner ball and at pi/2 beyond the outer ball. The exact
product-rule localization identity for (6) is
\[
 q_g[F]=q_g[\chi_0F]+q_g[\chi_1F]
       -\frac{2g^2}{a}\int\sum_{e,a,j}|\mathcal X_{e,a}\chi_j|^2|F|^2dZ.
\tag{23}
\]
Expand each squared derivative to prove it; the mixed terms vanish by
\(\sum_j\chi_j\mathcal X\chi_j=0\). The error is bounded by
\(C_\rho g^2\|F\|^2\). On the support of chi_1 the actual W has
a positive lower bound c_rho, since its only zero is the identity and
the manifold is compact. Thus the exterior form is at least
\(c_\rho/(2g^2a)\|\chi_1F\|^2\).

Map chi_0F by the chart density and dilation into ordinary Euclidean
L^2, extending by zero. It is a bounded linear map of Hilbert spaces,
preserves its norm, and its image remains in the invariant form space.
The oscillator bound
\[
 q_{\rm osc}[u]\ge\mu_k\|u\|^2
       -\sum_{j<k}(\mu_k-\mu_j)|\langle\varphi_j,u\rangle|^2
\tag{24}
\]
follows by expansion in its complete invariant eigenbasis. Each of the
k linear functionals in (24), composed with the local map, is bounded
on the original Hilbert space. Combining (23), the local comparison,
and the exterior lower bound gives a lower bound
\((1-\epsilon)\mu_k-C_{\rho,\epsilon}g^2\) on a subspace of
codimension at most k, once g is small enough that the exterior bound
exceeds (1-epsilon)mu_k. Min--max gives that same lower bound for
\(\mathcal E_k(g)\). First send g to zero, then epsilon to zero.
This proves (22). The density maps, cutoffs, finite-rank comparisons
and domains in this argument are all for the original operator (1).

In particular the actual physical finite-box gap satisfies
\[
 \boxed{\lim_{g\downarrow0}\Delta_L(g,a)
      =\frac{4\sqrt2}{a}\sin\frac{\pi}{4L+2}.}
\tag{25}
\]
The next six eigenvalues have this same limiting excitation energy.
For each fixed box this is a limit at positive couplings of the full
interacting physical spectrum. It has not been obtained by using an
unprojected one-quantum color-vector state.

## 7. What this does and does not prove about simultaneous limits

Equation (25) supplies a genuine gap-closing sequence of finite interacting
regulators. For example take L_j=j squared and a_j=1/(100j), j>=2. Its limiting
comparison gap is
\(400\sqrt2 j\sin[\pi/(4j^2+2)]\), which tends to zero.
For each fixed j, (25) proves the existence of a number g_j>0, which can
also be required to satisfy g_j<1/j, such that the actual gap differs
from this comparison value by less than 1/j. Every Hamiltonian in this
sequence has its full nonlinear potential and a strictly positive coupling.
The actual first excited eigenvectors can be chosen of unit norm and
orthogonal to their own actual vacua; their finite-regulator spectral
measures are then the atoms at those actual positive excitation energies.

This existence statement supplies neither an explicit admissible running
coupling at every cutoff nor convergence of local observables/vacua to a
nontrivial interacting four-dimensional theory. In particular convergence
of these excited spectral atoms toward zero does not identify their limits
as distinct physical continuum states, or prove nonzero continuum spectral
weight on every interval (0,epsilon). Neither identification is assumed.
The nonuniform L-dependence in the localization proof is retained, and
the next calculation must control these actual state/observable maps in
the simultaneous limit. Equation (25) is not a Yang--Mills mass-gap
counterexample.

## 8. Primary mathematical and lattice context

The Hamiltonian framework is J. Kogut and L. Susskind, *Hamiltonian
formulation of Wilson's lattice gauge theories*, Physical Review D 11
(1975), 395--408, https://doi.org/10.1103/PhysRevD.11.395.
Maximal-tree SU(2) coordinates are also treated by C. W. Bauer,
I. D'Andrea, M. Freytsis and D. M. Grabowska, *A new basis for Hamiltonian
SU(2) simulations*, https://arxiv.org/abs/2307.11829; this note derives
its own full maps (4)--(10) without any spin truncation.
The leading small-coupling comparison uses the localization/min--max
method of B. Simon, *Semiclassical analysis of low lying eigenvalues. I.
Non-degenerate minima: asymptotic expansions*, Annales de l'Institut
Henri Poincare A 38 (1983), 295--308, Sections 2,3,6,
https://www.numdam.org/item/AIHPA_1983__38_3_295_0/.
The finite-box density, kinetic tensor and residual-gauge implementation
needed here are proved explicitly above. No novelty of the general
harmonic-approximation method is claimed.

## 9. Actual-state continuation

The companion calculation *Actual weak-coupling vacuum, observable and
spectral maps* proves strong convergence of the actual vacuum under the
full-measure logarithm/Haar/dilation isometry, and operator-norm convergence
of every fixed finite spectral projection. It constructs an explicit bounded
physical radial observable whose centered raw spectral measure retains all
Laguerre weights, rather than inferring state survival from (25) alone.
For a lowest spatial mode and the stated explicit observable parameter,
the first positive limiting weight is 3/(8sqrt(2)), at the energy in (25),
and the total centered mass is 1-2^(-3/2). A particular simultaneous
very-weak-coupling macroscopic-mode diagonal instead sends this entire raw
measure to a nonzero atom at zero. These maps and that zero-energy
consequence are proved in the companion; none is identified with the
target interacting continuum. The companion is included in the same
readable source root with this manuscript.
