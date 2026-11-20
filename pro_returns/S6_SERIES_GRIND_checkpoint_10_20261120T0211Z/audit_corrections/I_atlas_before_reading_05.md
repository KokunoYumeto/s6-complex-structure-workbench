# Independent construction of the Paper I coefficient atlas

## Exposure boundary and scope

Written on 2026-11-19 by GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root and not separately exposed, branch `S6_SERIES_GRIND/corrections_audit`. The isolated statement was opened at 21:51:46 UTC. This derivation was completed before opening the receiving proof of `inv:C3.8` or any file under `audit_paper_i/open_atlas`.

Permitted earlier inputs read in full are retained in the nine `I_permitted_*.tex` files beside this report: `fam:src:A.1.2`, `wb:thm:retained-period-deformation`, `inv:A2.1`, `inv:A3.2`, `inv:C3.1`, `inv:C3.2`, `inv:C3.7`, and the original compendium statements/proofs `wb:lem:toric-chart-control` and `wb:thm:candidate-cusp-geometry`. I also opened DGKX v1 source lines 605–715 (the original matrices and period laws) and 9690–9825 (the scalar deformation cocycle). The latter is a permitted primary source, and supplies the scalar cocycle independently of the receiving Q construction. Prior messages had disclosed that an atlas was being constructed and that its scalar convention was being compared with minus the DGKX cocycle; they disclosed no Q formula. This is therefore a statement-first reconstruction using the explicitly permitted earlier results, not an assertion that the period/cusp existence theorems were rediscovered here.

The fresh program `code/independent_I_atlas_before_reading_05.py` verifies 39 exact algebraic identities. Its output is `code/independent_I_atlas_before_reading_05.json`, PASS, 0.428218 seconds, script SHA256 `26e77480693460c070572eb546b9bd1ace2d259b4d7deed9d2f0280b65557fe0`. It checks the two complete period transports, the original finite vectors, the primitive and its lattice difference, and the full symbolic cusp residue and fan-coordinate identities. Analytic properness and the determinant divisor are the explicitly read earlier inputs; the program does not claim to prove those facts.

## 1. Conventions and the scalar cocycle

Use the homological order `(gamma,u,w,delta)`, with dual real flat coordinates denoted by the same letters when there is no ambiguity. Put

\[
Z=\begin{pmatrix}6\mu&\tau\\\beta&\mu\end{pmatrix},\quad
\Pi=(Z\mid I_2),\qquad \beta=\beta^{\rm part}+c.
\]

An arrow from chart i to chart j is written `F_ij`. All target tensors/functions are pulled back to chart i when added. Thus a cocycle satisfies
\(h_{ik}=h_{ij}+F_{ij}^*h_{jk}\), and a potential has difference
\(H_j-H_i=h_{ij}\). This convention fixes the later partition signs.

On ordinary charts the parameter derivative field is \(V=\partial_{\zeta_2}\). In the cusp exponent coordinates it is \(V_0=2\pi i x_2\partial_{x_2}\). For each actual generating arrow define a scalar h by the following evaluated table:

| Original arrow | Scalar h |
|---|---|
| lattice translation \(\zeta\mapsto\zeta+\Pi\lambda\) | \(\lambda_\gamma\) |
| ordinary deck map \((z,\zeta)\mapsto(gz,R_g\zeta)\) | 0 |
| finite affine generator r1 | 1/3 |
| finite affine generator r2 | −1/4 |
| finite connector \(\zeta\mapsto\zeta+(\log s_j)/(2\pi i)\,\Pi v_j\) | \(\gamma(v_j)\log s_j/(2\pi i)\) |
| cusp deck \(\Psi_\lambda\) | \(\lambda_1\) |
| exponent connector and toric chart changes | 0 |

The two finite values use exactly \(v_1=(1,2,-4,0)^t\), \(v_2=(-1,-3,3,0)^t\); no vector is replaced by a congruent representative. The displayed generators have \(R_ge_2=e_2\). Differentiating their full c-dependent formulas gives \(\partial_cF=hV\) in target coordinates. Differentiating a composite proves the stated cocycle law. A relation among words gives zero scalar on the dense ordinary locus, hence gives zero holomorphic scalar throughout its domain. In particular the construction never divides by the vector field at its toric zeros. The finite connectors retain their chosen logarithm on each small annular source chart; changing it by an integer is exactly the corresponding original lattice arrow.

For a regular fibre, the local real coordinate gamma has lattice difference \(\lambda_\gamma\). Therefore the scalar class restricts to \(\gamma^{0,1}\). The injectivity in `inv:C3.1` identifies the resulting class with exactly \(g_\gamma\), including its scale and sign.

## 2. An explicit quadratic tensor for the one-form cocycle

The relative one-form cocycle needed for Q can be lifted explicitly using a symmetric quadratic tensor. This is the step that supplies coefficients beyond the existence result `inv:A3.2`.

On a regular base coordinate t set

\[
J=\begin{pmatrix}0&1\\6&0\end{pmatrix},\qquad
S_t=JZ_t^{-1}
=\frac1{6\mu_t^2-\tau_t\beta_t}
 \begin{pmatrix}-\beta_t&6\mu_t\\6\mu_t&-6\tau_t\end{pmatrix}.
\]

This is symmetric, and \(S_tZ_t=J\). Define the absolute quadratic lift

\[
\mathscr T^{\rm raw}_t=\tfrac12(d\zeta)^tS_t(d\zeta)\otimes\partial_t
\quad\hbox{in }\operatorname{Sym}^2\Omega_X^1\otimes f^*T_B.
\]

Products in this formula are symmetric tensor products, not exterior products. Under a change of base coordinate t=t(z), \(S_z=S_t/t_z\) and \(\partial_z=t_z\partial_t\), so the displayed tensor is identical. The derivative determinant has no zero on the ordinary part by `inv:A2.1`.

Here is an exact check of the relative deck transport. In a common coarse coordinate t the two period transformations are

\[
(\tau,\mu,\beta)\mapsto
((\tau-1)/\tau,(1-\mu)/\tau,\beta+2-6(1-\mu)^2/\tau),
\]
\[
(\tau,\mu,\beta)\mapsto
(-1/\tau,1+\mu/\tau,\beta-3-6\mu^2/\tau),
\]

with

\[
R_1=\begin{pmatrix}-1/\tau&0\\(1-\mu)/\tau&1\end{pmatrix},\qquad
R_2=\begin{pmatrix}1/\tau&0\\-\mu/\tau&1\end{pmatrix}.
\]

Differentiating these three functions with respect to t and substituting in the displayed S formula gives, for each generator,
\(R_j^t S_t'R_j=S_t\). The fresh symbolic calculation verifies all four entries as rational identities in the six independent variables \(\tau,\mu,\beta,\tau_t,\mu_t,\beta_t\). Composition proves the actual relative transport for every original deck word. A translation has identity relative differential. Thus the relative image of \(\mathscr T^{\rm raw}\) is a single global relative tensor.

For an ordinary transition \(F:(t,\zeta)\mapsto(t,R(t)\zeta+b(t))\), put \(D=R_t\zeta+b_t\). Exact expansion gives

\[
F^*\mathscr T'^{\rm raw}-\mathscr T^{\rm raw}
=dt\,a_F\otimes\partial_t,
\quad
a_F=D^tS_t'R\,d\zeta+\tfrac12D^tS_t'D\,dt.
\]

For a lattice vector \(\lambda=(\lambda_\gamma,\lambda_u,\lambda_w,\lambda_\delta)^t\), this specializes to the especially useful expression

\[
a_\lambda=\lambda_u\,d\zeta_1+6\lambda_\gamma\,d\zeta_2
 +\tfrac12(\lambda_u^2d\tau+12\lambda_u\lambda_\gamma d\mu
                       +6\lambda_\gamma^2d\beta). \tag{L}
\]

Formula (L) contains holomorphic differentials of period functions, so it remains holomorphic on a finite root disc; it has no division by its ramified coarse derivative.

## 3. Finite root extension with the original affine vectors

Let t=s^m at a finite special value. The raw tensor coefficient there is
\(S_t=ms^{m-1}S_s\). At the order-three point the entries of \(S_s\) have poles of order at most two, since its denominator has exact order two and its numerator is holomorphic. Multiplication by \(3s^2\) removes them. At the order-four point the denominator of \(S_s\) is a unit, so \(4s^3S_s\) is holomorphic. Thus the raw tensor is an absolute holomorphic tensor on both root covers, including their central tori.

For completeness the original integer matrices are

\[
A_1=\begin{pmatrix}1&0&0&0\\6&0&1&0\\-6&-1&-1&0\\-2&1&0&1\end{pmatrix},\quad
A_2=\begin{pmatrix}1&0&0&0\\0&0&-1&0\\-6&1&0&0\\3&0&1&1\end{pmatrix}.
\]

Their exact identities are \(A_1^3=A_2^4=I\), \(A_jv_j=v_j\). Consequently the m-th power of the actual affine lift r is the lattice translation \(L_{v_j}\), since its accumulated real translation is
\(m^{-1}\sum_{k=0}^{m-1}A_j^kv_j=v_j\). The fresh program checks all these identities.

Use the finite holomorphic average

\[
\mathscr T^{\rm av}=\frac1m\sum_{k=0}^{m-1}(r^k)^*\mathscr T^{\rm raw}.
\]

Its relative image is the same tensor, by the just-proved exact relative transport. Telescoping gives the full central extension formula

\[
r^*\mathscr T^{\rm av}-\mathscr T^{\rm av}
=\frac1m\bigl(L_{v_j}^*\mathscr T^{\rm raw}-\mathscr T^{\rm raw}\bigr)
=dt\,\frac{a_{v_j}}m\otimes\partial_t. \tag{F}
\]

For any lattice arrow the corresponding difference of the average is

\[
dt\left[\frac1m\sum_{k=0}^{m-1}(r^k)^*a_{A_j^k\lambda}\right]\otimes\partial_t,
\]

because \(r^kL_\lambda=L_{A_j^k\lambda}r^k\). Each term is the explicit holomorphic form (L) pulled back by the displayed original affine map. These formulas give every finite-cap generator, with all affine parts retained. The free quotient is locally biholomorphic by the permitted finite filling result, so restricting to local inverse charts transfers the forms to the actual X. Finite/ordinary connectors lie in s≠0 and use the ordinary expansion above with their full logarithmic b(t); there is no singular central connector to fill.

## 4. Full cusp extension, including both triple points

Use exactly the original cusp data

\[
Z(q)=\frac{\log q}{2\pi i}B_0+C(q,c),\qquad
B_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]
\[
C(q,c)=\begin{pmatrix}6\mu(q)&h(q)\\b^{\rm part}(q)-h(q)+c&\mu(q)\end{pmatrix}.
\]

Define

\[
\widetilde S(q)=J\left(\frac{B_0}{2\pi i}+qC'(q,c)\right)^{-1},\qquad
S_q=q\widetilde S(q).
\]

The matrix in parentheses is invertible on a sufficiently small closed cusp disc, by its nonzero value at zero. Its inverse is evaluated by its two-by-two adjugate and determinant. No term of C or C′ is discarded. The matrix \(\widetilde S\) is symmetric and

\[
\widetilde S(0)=2\pi i H,\qquad H=JB_0^{-1}=\operatorname{diag}(1,-6),\quad HB_0=J.
\]

For a maximal triangle \(\sigma=(v_0,v_1,v_2)\) of the original lower/upper triangulation, the exact toric coordinates satisfy

\[
q=z_0z_1z_2,\qquad x_a=\prod_i z_i^{v_{i,a}},\qquad
d\zeta=\frac1{2\pi i}\sum_i v_i\frac{dz_i}{z_i}.
\]

Set

\[
B_{ij}(q)=\frac{v_i^t\widetilde S(q)v_j}{(2\pi i)^2},\qquad
b_\sigma=\tfrac12\sum_iB_{ii}(q)\frac{dz_i}{z_i}.
\]

Subtract this exact logarithmic expression from the raw tensor:

\[
\mathscr T_\sigma
=\mathscr T^{\rm raw}-dq\,b_\sigma\otimes\partial_q
=\sum_{i<j}\left(B_{ij}-\frac{B_{ii}+B_{jj}}2\right)
               z_k\,dz_i\,dz_j\otimes\partial_q,\quad\{i,j,k\}=\{0,1,2\}. \tag{T}
\]

Every coefficient on the right is holomorphic at every coordinate stratum, including z0=z1=z2=0. This proves the extension separately on every lower and upper triangle; these two triangle orbits give the two triple points in the actual quotient. The formula also covers every double curve. The displayed equality is one of the fresh exact symbolic checks.

For two toric charts, the one-form difference is \(b_\sigma-b_\tau\). It is holomorphic on their intersection: along a common ray the residue is the same evaluated expression \(v^t\widetilde S(q)v/(2(2\pi i)^2)\), so it cancels identically as a function of q. A coordinate corresponding to a noncommon ray is invertible on that intersection. This proves holomorphicity directly in the original toric overlap coordinates.

It remains to include the full unit multipliers in the actual cusp quotient. Let \(\lambda\in\mathbb Z^2\), \(d=B_0\lambda\), and let \(\tau=\sigma+d\). Put

\[
V_\sigma=\begin{pmatrix}v_{0,1}&v_{1,1}&v_{2,1}\\v_{0,2}&v_{1,2}&v_{2,2}\\1&1&1\end{pmatrix},
\qquad c_i^t=(\hbox{first two entries of row }i\hbox{ of }V_\sigma^{-1}).
\]

These entries are actual integers because the original triangles are unimodular. The complete original map
\(\Psi_\lambda(x,q)=(e^{2\pi iC(q,c)\lambda}q^{B_0\lambda}x,q)\)
has the exact coordinate expression

\[
z_i'=z_i\exp(2\pi i c_i^tC(q,c)\lambda). \tag{U}
\]

To verify it, use
\(V_\tau=\left(\begin{smallmatrix}1&0&d_1\\0&1&d_2\\0&0&1\end{smallmatrix}\right)V_\sigma\).
The first two columns of the inverse are unchanged, and their row sum is zero; hence the product of the three units in (U) is exactly one. The fresh check proves these identities for both symbolic lower and upper triangles at arbitrary integer translate (vx,vy), rather than for one chosen cone.

Write \(B_{ii}'=(v_i+d)^t\widetilde S(v_i+d)/(2\pi i)^2\). Applying (L) on the cusp dense torus and then (T) gives

\[
a_{\Psi_\lambda}=\lambda^tJ^t d\zeta+
\tfrac12\lambda^tZ_q^tJ\lambda\,dq+b_\sigma-\Psi_\lambda^*b_\tau.
\]

All of its coefficients can be written without logarithmic singularities. Namely define the evaluated holomorphic scalar functions

\[
R_i(q)=\frac{\lambda^tJ^tv_i}{2\pi i}
       +\frac{\lambda^tB_0^tJ\lambda}{4\pi i}
       +\frac{B_{ii}(q)-B_{ii}'(q)}2,
\]
\[
D(q)=\tfrac12\lambda^tC'(q,c)^tJ\lambda
       -\pi i\sum_i B_{ii}'(q)c_i^tC'(q,c)\lambda.
\]

The equality \(HB_0=J\) gives, for every ray v and every lambda,

\[
2\pi iR_i(0)=\lambda^tJ^tv_i+
\tfrac12\lambda^tB_0^tJ\lambda+
\tfrac12\{v_i^tHv_i-(v_i+B_0\lambda)^tH(v_i+B_0\lambda)\}=0.
\]

This cancellation is checked as a polynomial identity with all four v/lambda entries independent. Thus the evaluated divided difference
\(\widehat R_i(q)=(R_i(q)-R_i(0))/q\), with its Taylor value at zero, is holomorphic, and the complete generator form is

\[
a_{\Psi_\lambda}=\sum_i\widehat R_i(q)z_jz_k\,dz_i+D(q)\,dq,
\qquad \{i,j,k\}=\{0,1,2\}. \tag{C}
\]

Formula (C) retains the full units (U), all of C′, and the actual affine lattice indexing. It is holomorphic at all doubles and both triples. Its coefficients are evaluated by rational matrix inversion, multiplication, differentiation and a removable divided difference of the given holomorphic period functions. There is no unspecified Cousin problem or inverse Dolbeault operator in this construction.

The permitted toric control and proper/free action theorem supplies the actual quotient neighborhoods and their local finite overlap control. It is used with the same C(q,c), not with its limit. The exponent connector to the ordinary region has q≠0, where the quadratic difference and its division by dq are already holomorphic.

## 5. One holomorphic cocycle on the complete atlas

Take the raw lift on ordinary charts, the averaged lift on finite-cap source charts, and (T) on toric source charts. On each actual quotient coordinate chart choose its specified local inverse into this source atlas. For every overlap define aij by

\[
F_{ij}^*\mathscr T_j-\mathscr T_i=dt\,a_{ij}\otimes\partial_t.
\]

The preceding formulas provide holomorphic aij on all overlap types, even where dt vanishes. This is an equality of absolute tensors, and under a base coordinate change the product dt times partial_t is unchanged; hence it defines the same one-form. It is unique because the equality is unique on the dense ordinary locus and the extension is holomorphic. Telescoping the tensor differences proves exactly
\(a_{ik}=a_{ij}+F_{ij}^*a_{jk}\). Thus no unverified triple-overlap compatibility remains. On an overlap described by a finite word, evaluate aij by successive pullbacks and additions of the displayed generator formulas. Different words give the same form by the tensor identity. Proper discontinuity bounds the words occurring between any two relatively compact source charts.

The fibre class, including its sign, is determined without a Hodge existence argument. On a regular flat cover define the smooth (1,0)-form

\[
A=u\,d\zeta_1+6\gamma\,d\zeta_2
 -\tfrac12(u^2d\tau+12u\gamma d\mu+6\gamma^2d\beta).
\]

Its complete lattice difference is exactly (L). Expanding with
\(\zeta_1=6\mu\gamma+\tau u+w\), \(\zeta_2=\beta\gamma+\mu u+\delta\), gives

\[
A=u\,dw+6\gamma\,d\delta+
\tfrac12d(\tau u^2+12\mu u\gamma+6\beta\gamma^2),
\qquad dA=du\wedge dw+6d\gamma\wedge d\delta.
\]

The fresh program checks all ten exterior coefficients and the complete lattice difference. On a regular fibre, the last expression is exactly eta and has type (1,1) by `inv:C3.7`, so \(\bar\partial A=\eta\). Therefore the class of aij restricts to eta with the positive sign in the isolated target.

## 6. Specified refinement, weights and evaluated coefficients

Here is a deterministic way to specify the partition without leaving a local-finiteness assumption unresolved. Enumerate the ordinary, finite and toric source charts in the order: chart type, original generator/triangle integer indices by increasing absolute size and lexicographic order, then rational centers and positive rational radii by increasing height and lexicographic order. In each source chart retain pairs of concentric rational coordinate balls whose closed outer ball stays inside the chart and whose quotient map is injective on an open neighborhood of that closure. Use inner radius half the outer radius. These retained inner balls cover X: every point has a local inverse chart by the permitted free/proper quotient construction, and rational balls refine its neighborhoods. All retained choices are defined by the original atlas, not by an unidentified diffeomorphism.

For the fixed admissible c, X is compact. Let N be the least integer for which the first N retained inner balls cover X, after the stated enumeration. Such an integer exists by compactness. This specifies a finite, hence countable and locally finite, refinement; it applies equally to central finite tori and every cusp stratum. A number N is not numerically evaluated here, and no numerical cover size is claimed. The mathematical rule determines the chart selection and supplies coefficient formulas for each selected chart. One may instead run the same rule on an exhaustion of relatively compact parameter discs to obtain a countable locally finite family atlas; the isolated target only needs the fixed X.

On the i-th selected outer ball with coordinate z, center bi and radius ri, use the explicit cutoff

\[
\phi_i(z)=\begin{cases}
\exp[-1/(1-|z-b_i|^2/r_i^2)],& |z-b_i|<r_i,\\
0,& |z-b_i|\ge r_i.
\end{cases}
\]

Extend it by zero to X. The extension is smooth, its support lies in the closure of its injective coordinate chart, and the sum \(W=\sum_{i=1}^N\phi_i\) is positive because the inner balls cover. Put \(\rho_i=\phi_i/W\). All coefficients are given by elementary functions of the specified chart coordinates. Every derivative can be evaluated recursively: for a nonzero multiindex alpha,

\[
D^\alpha(W^{-1})=-W^{-1}
\sum_{0<\beta\le\alpha}\binom\alpha\beta
(D^\beta W)D^{\alpha-\beta}(W^{-1}),
\qquad D^0(W^{-1})=1/W.
\]

The sum is finite, so it is locally finite at all special points. The proper/free quotient bounds enter in specifying the injective charts; no convergence of an unbounded deck sum is asserted.

With the cocycle sign convention of section 1 define on Ui

\[
H_i=-\sum_j\rho_jh_{ij},\qquad B_i=-\sum_j\rho_ja_{ij},
\qquad G=\bar\partial H_i,\qquad Q=\bar\partial B_i. \tag{P}
\]

On Ui∩Uk the cocycle law and sum rho=1 give
\(H_k-H_i=h_{ik}\) and \(B_k-B_i=a_{ik}\). Their differences are holomorphic, so (P) defines global smooth forms with \(\bar\partial G=\bar\partial Q=0\).

For actual chart coordinates z1,z2,z3, write \(a_{ij}=\sum_r a_{ij,r}dz_r\). The final evaluated coefficients are

\[
G=-\sum_s\left(\sum_jh_{ij}\,\partial_{\bar z_s}\rho_j\right)d\bar z_s,
\]
\[
Q=\sum_{r,s}\left(\sum_ja_{ij,r}\,\partial_{\bar z_s}\rho_j\right)
dz_r\wedge d\bar z_s. \tag{E}
\]

The positive sign in the second formula comes from reversing \(d\bar z_s\wedge dz_r\) after applying \(\bar\partial\) to B. On a fibre, Bi−A is a global smooth (1,0)-form because its local differences vanish. Hence Q and eta differ by a global bar-partial-exact form there. Likewise Hi−gamma is globally smooth on the fibre, so G has precisely the class already identified as g_gamma.

## 7. Exponential identity and the real-representative obstruction

The original integers are \((l_0,l_1,l_2)=(0,1,-1)\). The exact retained collar formula is
\(p=12l_0-4l_1-3l_2=-1\). Equivalently the three integral clutch contributions are
\(4l_1-a_1,\ 3l_2-a_2,\ -12l_0+a_1+a_2\); their sum is 1, independent of the frame integers. With the fixed exponential convention \(z\mapsto e^{2\pi iz}\), `inv:C3.2` therefore gives

\[
\exp(12[G])=\exp(12g_\gamma)=f^*\mathcal O_{\mathbb P^1}(1).
\]

Finally, a real bar-partial-closed (1,1)-form is also partial-closed by conjugation and hence d-closed. On this X, diffeomorphic to S6 by the permitted original construction, its real de Rham class is zero, so it is d-exact. Its restriction to a regular fibre then has square integral zero by Stokes. A bar-partial class equal to eta has square integral \(\int_F\eta^2=-12\): replacing eta by eta+bar-partial(alpha) changes its square by the bar-partial of an explicit (2,1)-form, so does not change that integral. This contradicts zero. Thus the constructed Q is necessarily a complex representative and no real one has its asserted fibre class.

## Assessment before receiving the proposed proof

All required form identities and special-stratum extension gates are supplied above, relative to the explicitly permitted earlier construction/divisor inputs. No proof of `inv:C3.8` has been consulted. The remaining comparison is editorial and mathematical comparison with that receiving proof, not a missing local extension in this derivation. Numerical values for the chosen rational coordinate-ball cover are not claimed: its deterministic enumeration and least finite covering stage are specified mathematically, and the coefficient rule (E) evaluates any resulting chart. The 39-check output certifies only its listed finite identities; the full cocycle/partition/extension reasoning is this written derivation.
