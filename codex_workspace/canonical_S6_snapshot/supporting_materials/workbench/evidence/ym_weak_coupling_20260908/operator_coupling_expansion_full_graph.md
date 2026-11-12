# The first two coupling coefficients of the full tree-coordinate Hamiltonian

8 September 2026.

This note computes the terms of orders g and g squared after the exact
maximal-tree, Haar-density, and dilation map of the original finite-box
SU(2) Hamiltonian. Every original edge and face remains in the formulas.
The coefficients are finite differential expressions in all chord
coordinates. No spatial mode, Wilson word, density term, or scalar
energy has been removed. A quantitative remainder estimate is proved
on compact chart cores. This is a fixed-box operator calculation; it
does not assert a uniform-volume perturbation expansion or an
interacting continuum construction.

## 1. Original operator, weights, and graph data

Fix an integer L>=2 and physical spacing a>0. The vertices are
\(\{-L,\ldots,L\}^3\). Let E be every positively oriented contained
nearest-neighbor edge and P every contained positively oriented
elementary face. Keep

\[
 T_\alpha=-\frac i2\sigma_\alpha,\qquad
 [T_\alpha,T_\beta]=\epsilon_{\alpha\beta\gamma}T_\gamma,
 \qquad E_e=-\sum_{\alpha=1}^3X_{e,\alpha}^2,
\]

and the full operator

\[
 H_g=\frac{2g^2}{a}\sum_{e\in E}E_e
       +\frac1{2g^2a}\sum_{p\in P}(2-\operatorname{tr}U_p),
 \qquad g>0.                                                   \tag{1}
\]

The measure is product Haar probability, and the physical subspace is
the invariant subspace for all vertex gauge transformations. In
particular the coefficients remain \(\kappa=2g^2/a\),
\(b=1/(2g^2a)\), and \(\xi=1/(4g^4)\), with the full scalar
Wilson contribution \(2b|P|\) included in (1).

For fixed real edge weights h_e retain the original face average and
weighted operator

\[
 h_p=\frac14\sum_{e\in\partial p}h_e,\qquad
 D_{h,g}=\frac{2g^2}{a}\sum_eh_eE_e
       +\frac1{2g^2a}\sum_ph_p(2-\operatorname{tr}U_p).          \tag{2}
\]

For a physical profile h one may take h_e=h(am(e)), with the original
edge midpoint m(e). The weights and a are fixed throughout this
coupling expansion; their derivatives with respect to g are zero.
The calculations allow signed weights. All operator identities below
are first stated on smooth compact chart functions, which lie in the
original weighted operators' domains.

Use the fixed maximal tree rooted at o=(-L,-L,-L), with parent obtained
by decreasing the first coordinate in the order 1,2,3 that exceeds -L.
Let \(\mathcal T\) be its tree edges and \(\mathcal C\) its chords,
with \(r=|\mathcal C|=2(2L)^3+3(2L)^2\). If t_v(U) is the
ordered root-to-v tree holonomy, the exact chord is

\[
 Z_c=t_{s(c)}U_ct_{t(c)}^{-1}.                              \tag{3}
\]

The inverse retains the tree links and sets U_c=t_s^{-1}Z_ct_t.
Independent left and right Haar translations in each chord preserve
the full product measure. Based gauge averaging removes the tree
variables; residual physical invariance is simultaneous conjugation
of every chord, not separate conjugation in each chord.

For every original edge e and chord c define two signed coefficients
\(\ell_{ec},r_{ec}\) by

\[
 (\ell_{ec},r_{ec})=
 \begin{cases}
 (\mathbf1_{\{c=e\}},0),&e\in\mathcal C,\\
 (\epsilon(s(c),e),-\epsilon(t(c),e)),&e\in\mathcal T,
 \end{cases}                                                \tag{4}
\]

where epsilon(v,e) is one when the original tree edge e lies on
the specified root-to-v path and zero otherwise. Put

\[
 t_{ec}=\ell_{ec}+r_{ec},\qquad
 s_{ec}=\ell_{ec}-r_{ec}.                                  \tag{5}
\]

Thus a tree edge has t_ec=epsilon(s(c),e)-epsilon(t(c),e) and
s_ec=epsilon(s(c),e)+epsilon(t(c),e). A chord edge has t_ec=s_ec
=delta_ec. These signs are fixed by the inverse terminal holonomy
in (3). The additive tree map has matrix T_{ce}=t_ec; consequently

\[
 G_{cd}=\sum_e t_{ec}t_{ed},\qquad
 (G_h)_{cd}=\sum_eh_e t_{ec}t_{ed}.                         \tag{6}
\]

The original oriented face curl composed with zero-tree chord insertion
is denoted C, as in the fixed-box companion. No metric on the chords
has been substituted for G.

## 2. Exact left and right fields, with their logarithmic signs

Write \(Z_c=\exp(y_c^\alpha T_\alpha)\), \(|y_c|<2\pi\).
For one chord use \(A_yv=y\times v\), which is exactly the
coefficient vector of \([y^\alpha T_\alpha,v^\beta T_\beta]\).
Left and right multiplication give coordinate vector fields

\[
 L_\alpha=\left(I-\frac12A_y+b(|y|)A_y^2\right)e_\alpha
                      \mathbin{\cdot}\nabla_y,
 \qquad
 R_\alpha=\left(I+\frac12A_y+b(|y|)A_y^2\right)e_\alpha
                      \mathbin{\cdot}\nabla_y,               \tag{7}
\]

where e_alpha is the standard color basis vector and

\[
 b(u)=\frac1{u^2}-\frac{\cot(u/2)}{2u}\quad(0<u<2\pi),
 \qquad b(0)=\frac1{12}.                                   \tag{8}
\]

Here b(u) is a scalar analytic function, distinct from the original
Hamiltonian coefficient b=1/(2g^2a).

To prove (7) and its signs, differentiate the exponential:

\[
 (d\exp)_y(v)\exp(-y)=\int_0^1e^{sA_y}v\,ds.
\]

For exp(t e_alpha) exp(y), its left-translated derivative is e_alpha;
the logarithmic derivative is therefore
\(A_y(e^{A_y}-I)^{-1}e_\alpha\), with the analytic value on the
kernel of A_y. On the line spanned by y this is the identity. On
the perpendicular plane A_y^2=-|y|^2 I, and direct inversion of

\[
 \frac{\sin |y|}{|y|}I+
           \frac{1-\cos |y|}{|y|^2}A_y
\]

gives \((|y|/2)\cot(|y|/2)I-A_y/2\). This is exactly the
first expression in (7). For exp(y) exp(t e_alpha), the same
left-translated derivative is exp(A_y)e_alpha; multiplying by
that factor changes the sign of A_y/2 and gives the right field.
Thus the left sign is negative and the right sign positive in the
original T_alpha convention.

Taylor division of cosine by sine gives

\[
 b(u)=\frac1{12}+\frac{u^2}{720}+O(u^4).                    \tag{9}
\]

In particular the first logarithmic coefficients are
I minus or plus A_y/2 plus A_y^2/12, and there is no cubic
coefficient in an individual left or right vector field.

The exact quotient fields of the original kinetic operator are

\[
 \mathcal X_{e,\alpha}
 =\sum_c\{\ell_{ec}L_{c,\alpha}+r_{ec}R_{c,\alpha}\}.
                                                                  \tag{10}
\]

Each displayed field is divergence-free for product Haar measure.
The exact quotient kinetic operator is
\(-(2g^2/a)\sum_{e,\alpha}\mathcal X_{e,\alpha}^2\);
the weighted version inserts h_e in the same original-edge sum.
This follows edge by edge from the invariance of the sum over the
three generators under the adjoint rotations induced by changing
the tree representative. It does not require the weights to be
constant across edges.

## 3. The exact Haar/dilation map and its density contribution

Retain the complete density and isometry

\[
 \mathcal J(y)=(16\pi^2)^{-r}
   \prod_c\left[\frac{\sin(|y_c|/2)}{|y_c|/2}\right]^2,
 \qquad
 (\mathcal B_gF)(x)=g^{3r/2}\mathcal J(gx)^{1/2}F(\exp(gx))
                                                               \tag{11}
\]

on \(\Omega_g=\{x:|x_c|<2\pi/g\}\), with zero extension outside.
Its adjoint includes the reciprocal density. Compactly supported
x-functions whose support lies inside Omega_g pull back to smooth
functions in the original operator domain. The factor (16pi^2)^-r
and the dilation power in (11) remain in this exact map.

Put \(l_g(x)=\log\mathcal J(gx)\). Its first terms are

\[
 l_g(x)=-r\log(16\pi^2)
   -\frac{g^2}{12}\sum_c|x_c|^2
   -\frac{g^4}{1440}\sum_c|x_c|^4+O(g^6)
                                                               \tag{12}
\]

on fixed compact x-sets. The constants follow by expanding
2 log(sin(u/2)/(u/2)); the remainder and its derivatives are
bounded on each smaller chart.

For each e,alpha define the exact first-order transformed field
\(\mathcal Q_{e,\alpha}(g)=\mathcal B_g(g\mathcal X_{e,\alpha})
\mathcal B_g^*\) on these compact cores. The chain and product
rules give the vector part from (7), followed by subtraction of
one half of its derivative of l_g. Because
\(x\cdot(x\times e_\alpha)=0\) and
\(x\cdot[x\times(x\times e_\alpha)]=0\), the exact result is

\[
 \boxed{\begin{split}
 \mathcal Q_{e,\alpha}(g)
 ={}&\sum_c t_{ec}\partial_{c,\alpha}
   -\frac g2\sum_c s_{ec}(x_c\times e_\alpha)\cdot\nabla_c\\
 &+g^2\sum_c t_{ec}b(g|x_c|)
       \left([x_c\times(x_c\times e_\alpha)]\cdot\nabla_c
                           +x_c^\alpha\right).
 \end{split}}                                                \tag{13}
\]

The last x_c^alpha is multiplication, with a positive sign. In
fact the radial derivative of l_g is
\([g\cot(g|x_c|/2)/|x_c|-2/|x_c|^2]x_c\); multiplication by
-1/2 and the radial part t_ec e_alpha gives exactly
g^2 t_ec b(g|x_c|)x_c^alpha. Thus (13) includes the full density
term, not only its leading approximation.

Write its first three evaluated differential coefficients as

\[
 \begin{split}
 Q^{(0)}_{e\alpha}&=\sum_ct_{ec}\partial_{c,\alpha},\\
 Q^{(1)}_{e\alpha}&=-\frac12\sum_cs_{ec}
                         (x_c\times e_\alpha)\cdot\nabla_c,\\
 Q^{(2)}_{e\alpha}&=\frac1{12}\sum_ct_{ec}
       \left((x_c x_c^\alpha-|x_c|^2e_\alpha)\cdot\nabla_c
                           +x_c^\alpha\right).
 \end{split}                                                \tag{14}
\]

Then Q(g)=Q^(0)+gQ^(1)+g^2Q^(2)+O(g^4) in the coefficient
C1 norm on compact sets. Each coefficient is formally
skew-adjoint in dx: Q^(0) and Q^(1) have divergence zero;
the vector part of Q^(2) has divergence
\(\sum_ct_{ec}x_c^\alpha/6\), and its multiplication term
is one half of that divergence. This independently checks the
sign of the half-density term.

## 4. Evaluated kinetic tensors and the retained scalar

Let composite indices be (c,beta), with beta=1,2,3, and sum
repeated color components explicitly or by their stated finite
ranges. The exact principal tensor is the sum of the outer
products of the vector coefficients of (13), excluding its
multiplication term. Its first coefficients are

\[
 A_0^{c\beta,d\gamma}=G_{cd}\delta_{\beta\gamma},           \tag{15}
\]

\[
 \boxed{A_1^{c\beta,d\gamma}
 =\frac12\sum_{e,\eta}\epsilon_{\eta\beta\gamma}
       (s_{ec}t_{ed}x_c^\eta-t_{ec}s_{ed}x_d^\eta),}          \tag{16}
\]

and

\[
 \boxed{\begin{split}
 A_2^{c\beta,d\gamma}=\sum_e\Big\{
 &\frac{s_{ec}s_{ed}}4
       [\delta_{\beta\gamma}(x_c\cdot x_d)
                                      -x_d^\beta x_c^\gamma]\\
 &+\frac{t_{ec}t_{ed}}{12}
       [x_c^\beta x_c^\gamma+x_d^\beta x_d^\gamma
          -( |x_c|^2+|x_d|^2)\delta_{\beta\gamma}]
                       \Big\} .
 \end{split}}                                                \tag{17}
\]

Every original edge appears, with its exact t and s coefficients.
For weighted operators define A_{n,h} by inserting h_e into
each edge sum in (15)--(17); A_{0,h}=G_h tensor I_3.
The tensors are real and symmetric in the two composite indices.

For a direct derivation, write the vector coefficients of (14)
as a_0,a_1,a_2. The order-one tensor is
sum(a_0 a_1^T+a_1 a_0^T), giving (16). The order-two tensor is
sum(a_1 a_1^T+a_0 a_2^T+a_2 a_0^T). The color contraction

\[
 \sum_\alpha (x_c\times e_\alpha)^\beta
                 (x_d\times e_\alpha)^\gamma
 =\delta_{\beta\gamma}(x_c\cdot x_d)-x_d^\beta x_c^\gamma
\]

gives the first line of (17); inserting
x_c times x_c^alpha minus |x_c|^2 e_alpha gives its second line.

The exact divergence-form kinetic operator after (11) is

\[
 \frac2a\left[-\partial_i A^{ij}(gx)\partial_j
   +\frac12\partial_i(A^{ij}(gx)\partial_j l_g)
   +\frac14(\partial_i l_g)A^{ij}(gx)(\partial_j l_g)\right].
                                                               \tag{18}
\]

In the first term the derivatives act on the function to their
right as well as on A. The next two terms are multiplication
operators. Formula (18) follows by conjugating
-J^-1 partial_i(J A^{ij} partial_j) with J^1/2 and expanding
both derivatives. It is equivalently -(2/a) sum Q_ealpha(g)^2.

Since partial_j l_g=-g^2 x_j/6+O(g^4), the order-two density
scalar in the bracket is
-g^2 trace(A_0)/12=-g^2 trace(G)/4. Therefore the kinetic
coefficients are exactly

\[
 \begin{split}
 K_0&=-\frac2a\partial_i A_0^{ij}\partial_j,\\
 K_1&=-\frac2a\partial_i A_1^{ij}\partial_j,\\
 K_2&=-\frac2a\partial_i A_2^{ij}\partial_j
                       -\frac{\operatorname{tr}G}{2a}I.
 \end{split}                                                \tag{19}
\]

The corresponding weighted scalar is -trace(G_h)/(2a). It has
not been absorbed into a changed vacuum energy. Notice also
that partial_i A_1^{ij}=0: for each e,alpha, its constant vector
field differentiates the linear field only in the same alpha
direction, and partial_alpha(x times e_alpha)=0, while the
linear field has divergence zero. Thus K_1 has no hidden
first-order drift. The divergence notation in K_2 retains all
the quadratic metric's first-order derivatives.

As a check for one chord and one left Casimir, t=s=1 gives
A_1=0 and A_2=(|x|^2 I-xx^T)/12. Its order-two kinetic
coefficient is
\(-\Delta_{S^2}/(6a)-1/(2a)\), using
\(\Delta_{S^2}=|x|^2\Delta-(x\cdot\nabla)^2-x\cdot\nabla\).
This follows from (17)--(19) without changing the group radius
or the original factor 2/a.

## 5. All ordered Wilson coefficients through degree four

For a face p=(n;i,j), i<j, retain its original four ordered slots

\[
 ((n,i),+),\quad ((n+e_i,j),+),\quad
 ((n+e_j,i),-),\quad ((n,j),-).                            \tag{20}
\]

In slot m put v_{p,m}=epsilon_m x_c if its edge is chord c,
and v_{p,m}=0 if it is a tree edge. Thus tree slots remain in
the ordered list with their exact identity factor. The face
word in the tree-I representative is exactly

\[
 U_p(gx)=\prod_{m=1}^4\exp(g v_{p,m}^\alpha T_\alpha),
                                                               \tag{21}
\]

in the order (20). In particular inverse traversal is represented
by the negative vector in that same slot; no factors are
commuted or reordered. For this section fix p and write v_m for
its four vectors, r_m^2=v_m dot v_m, and d_mn=v_m dot v_n.

The Pauli multiplication rule in the retained convention gives

\[
 \begin{split}
 \operatorname{tr}(vT\,wT)&=-\tfrac12 v\cdot w,\\
 \operatorname{tr}(vT\,wT\,zT)&=-\tfrac14 v\cdot(w\times z),\\
 \operatorname{tr}(vT\,wT\,zT\,uT)
 &=\tfrac18[(v\cdot w)(z\cdot u)-(v\cdot z)(w\cdot u)
                                      +(v\cdot u)(w\cdot z)],
 \end{split}                                                \tag{22}
\]

where vT=v^alpha T_alpha. These identities follow by applying
T_alpha T_beta=-(delta_alpha_beta/4)I+(epsilon_alpha_beta_gamma/2)
T_gamma and taking the trace. In particular (vT)^2=-|v|^2I/4.

Define w_{n,p} by expanding the exact expression
2-tr U_p(gx). Its constant and linear terms vanish, and the
next coefficients are

\[
 \boxed{w_{2,p}=\frac14\left|\sum_{m=1}^4v_m\right|^2,
 \qquad
 w_{3,p}=\frac14\sum_{m<n<l}v_m\cdot(v_n\times v_l).}       \tag{23}
\]

The complete quartic coefficient is

\[
 \boxed{\begin{split}
 w_{4,p}=-\Bigg[\,
 &\sum_m\frac{r_m^4}{192}
 +\sum_{m<n}\left\{\frac{(r_m^2+r_n^2)d_{mn}}{48}
                                  +\frac{r_m^2r_n^2}{32}\right\}\\
 &+\sum_{m<n<l}
       \frac{r_m^2d_{nl}+r_n^2d_{ml}+r_l^2d_{mn}}{16}\\
 &+\sum_{m<n<l<q}
       \frac{d_{mn}d_{lq}-d_{ml}d_{nq}+d_{mq}d_{nl}}8
                                                        \Bigg].
 \end{split}}                                                \tag{24}
\]

All sums use the retained slot order. There is at most one
four-distinct-slot term, but it is left in the displayed
ordered form so every position and inverse sign is explicit.

To verify completeness, the degree-n coefficient of the product
in (21) is the finite sum

\[
 \sum_{a_1+\cdots+a_4=n}
 \frac{(v_1T)^{a_1}(v_2T)^{a_2}
       (v_3T)^{a_3}(v_4T)^{a_4}}{a_1!a_2!a_3!a_4!}.
\]

At degree three, the patterns (3) and (2,1) have zero trace;
only the three-distinct-slot trace in (22) survives, with the
positive sign in w_3 because W=2-tr U. At degree four the
patterns (4), (3,1), (2,2), (2,1,1), and (1,1,1,1) give
respectively the five displayed types in (24), with the
negative sign from W. This proves that none of the quartic
word contributions is missing.

For a single nonzero slot, (23)--(24) give r^2/4 and -r^4/192,
the direct expansion of 2-2 cos(g r/2). For the four-slot test
(v,w,-v,-w), (23) has zero quadratic and cubic terms and (24)
gives \(|v\times w|^2/4\). This agrees with the commutator word's
leading logarithm g^2[vT,wT]. This check does not replace the
independent original face letters in (20). In particular w_4
need not have one sign for arbitrary noncommuting letters.

Set

\[
 W_n(x)=\sum_{p\in P}w_{n,p}(x),\qquad
 W_{n,h}(x)=\sum_{p\in P}h_p w_{n,p}(x),\qquad n=2,3,4.
                                                               \tag{25}
\]

The signed sum in w_2 is the original curl (Cx)_p, so
W_2=one quarter sum_alpha ||Cx^alpha||^2. The expansion of the
full Wilson multiplication term is therefore

\[
 \frac{W(gx)}{2g^2a}
 =\frac1{2a}\{W_2+gW_3+g^2W_4\}+O(g^3),                 \tag{26}
\]

with the weighted version using W_{n,h}. This is an expansion
of the full face terms 2-tr U_p: their constant at the identity
cancels inside each original expression. It is not deletion of
the original scalar 2b|P| from the operator.

## 6. The full coefficients and the weighted observable

On compact chart cores define \(\widetilde H_g=\mathcal B_gH_g
\mathcal B_g^*\), including the exact tree quotient already
specified. The evaluated coefficients are

\[
 \boxed{\begin{split}
 H_0&=-\frac2a\partial_i A_0^{ij}\partial_j+\frac{W_2}{2a},\\
 H_1&=-\frac2a\partial_i A_1^{ij}\partial_j+\frac{W_3}{2a},\\
 H_2&=-\frac2a\partial_i A_2^{ij}\partial_j
                     -\frac{\operatorname{tr}G}{2a}I
                     +\frac{W_4}{2a}.
 \end{split}}                                                \tag{27}
\]

Here A_0,A_1,A_2 are exactly (15)--(17), and W_2,W_3,W_4
are the explicit four-letter polynomials (23)--(25). Thus

\[
 \widetilde H_g f=H_0f+gH_1f+g^2H_2f+\mathcal R_g f.
                                                               \tag{28}
\]

The leading coefficient is precisely the complete companion
oscillator in the original chord coordinates:

\[
 H_0=\frac1a\left[-2\sum_{\alpha,c,d}G_{cd}
          \partial_{c,\alpha}\partial_{d,\alpha}
                 +\frac18\sum_\alpha\|Cx^\alpha\|^2\right].
\]

No diagonalization or selection of oscillator modes was used to
obtain either higher coefficient.

Likewise \(\widetilde D_{h,g}=\mathcal B_gD_{h,g}\mathcal B_g^*\)
has coefficients

\[
 \boxed{\begin{split}
 D_{h,0}&=-\frac2a\partial_i A_{0,h}^{ij}\partial_j
                                    +\frac{W_{2,h}}{2a},\\
 D_{h,1}&=-\frac2a\partial_i A_{1,h}^{ij}\partial_j
                                    +\frac{W_{3,h}}{2a},\\
 D_{h,2}&=-\frac2a\partial_i A_{2,h}^{ij}\partial_j
                     -\frac{\operatorname{tr}G_h}{2a}I
                                    +\frac{W_{4,h}}{2a}.
 \end{split}}                                                \tag{29}
\]

The constant profile gives D_{1,n}=H_n for each n=0,1,2,
as required by the original identity D_{1,g}=H_g. These are
operator coefficients, before subtraction of the moving actual
vacuum energy or weighted vacuum expectation. Centering and
vacuum-response derivatives remain the exact operations in the
coupling-response companion; they are not silently incorporated
into H_2 or D_{h,2}.

## 7. A quantitative compact-core remainder estimate

This section makes the remainder in (28) an actual norm bound.
Put N=3r and take R>=1. Assume f is smooth and compactly
supported in the Euclidean ball |x|<R, and
\(0<g\le\min(1,R^{-1})\). Then every g|x_c|<=1<2pi,
so the support is strictly inside the exact logarithm chart.
Define

\[
 \|f\|_{2,\Sigma}=\sum_{|\alpha|\le2}\|\partial^\alpha f\|_2,
 \quad C_N=(N+1)(2N+1),
\]

where the multi-index alpha here ranges over all N real
coordinates. For the explicit scalar in (8) put

\[
 d(u)=\frac{b(u)-1/12}{u^2},\quad d(0)=\frac1{720},\qquad
 B_* =1+\max_{0\le u\le1}(|d(u)|+|d'(u)|).                  \tag{30}
\]

The even Taylor expansion (9) makes d smooth at zero, with
d'(0)=0; its elementary trigonometric expression is smooth
on the rest of this interval. Thus B_* is a specified finite
positive real constant, independent of the graph or regulator.
It can be evaluated from (8); it is not an unknown operator
remainder or a mathematical hypothesis.

For each edge put

\[
 T_e=\sum_c|t_{ec}|,\quad S_e=\sum_c|s_{ec}|,
 \quad M_{0,e}=T_e,\quad
 M_{1,e}=\frac{S_e(1+R)}2,\quad
 M_{2,e}=\frac{T_e(1+R)^2}{12},\quad
 M_{4,e}=10T_eB_*(1+R)^4.
                                                               \tag{31}
\]

Let q_p be the number of chord slots among the four original
slots of face p. For the weighted expansion in (29) a valid
explicit remainder constant is

\[
 \begin{split}
 \mathcal C_{h,L,a,R}={}&\frac{6C_N}{a}\sum_e|h_e|
 \left[2M_{1,e}M_{2,e}+M_{2,e}^2
  +2(M_{0,e}+M_{1,e}+M_{2,e})M_{4,e}+M_{4,e}^2\right]\\
 &+\frac1{a\,5!}\sum_p|h_p|\left(\frac{q_pR}{2}\right)^5.
                                                               \tag{32}
\end{split}
\]

Every quantity in this finite sum is now defined by the original
graph, weights, a, R, and the explicit scalar function (8).
The estimate is

\[
 \boxed{
 \|[\widetilde D_{h,g}-D_{h,0}-gD_{h,1}-g^2D_{h,2}]f\|_2
       \le g^3\mathcal C_{h,L,a,R}\|f\|_{2,\Sigma}.}
                                                               \tag{33}
\]

Taking every h_e=h_p=1 proves the same estimate for (28).

Here is the proof. For a first-order operator P, let M(P) be
the largest absolute value of a coefficient or one of its
first coordinate derivatives on |x|<=R, including its
multiplication coefficient. Expanding the composition of two
such operators produces N^2 second-order terms, N^2+2N
first-order terms, and N+1 multiplication terms. Thus

\[
 \|PQf\|_2\le C_N M(P)M(Q)\|f\|_{2,\Sigma}.              \tag{34}
\]

The explicit polynomials in (14) obey M(Q^(i)_ealpha)<=M_i,e
for i=0,1,2. For example differentiating
x^beta x^alpha-|x|^2 delta_alpha_beta costs at most 4R,
and 4R<=(1+R)^2. The multiplication coefficient in Q^(2)
is bounded by T_e R/12 with the same bound on its derivatives.

Formula (13) gives the exact field remainder

\[
 Q_{e\alpha}(g)=Q^{(0)}_{e\alpha}+gQ^{(1)}_{e\alpha}
                 +g^2Q^{(2)}_{e\alpha}+g^4F_{e\alpha,g},
\]

where

\[
 F_{e\alpha,g}=\sum_ct_{ec}|x_c|^2d(g|x_c|)
       \left([x_c\times(x_c\times e_\alpha)]\cdot\nabla_c
                                +x_c^\alpha\right).
\]

The chain rule, g<=1, and (30) bound every coefficient and
first derivative by M_4,e. The factor 10 in (31) bounds,
in particular, the derivative terms 6R^3|d|+gR^4|d'|
from the vector coefficient and 3R^2|d|+gR^3|d'| from
its multiplication coefficient. The even smooth extension
handles x_c=0 as well.

Let Q_app=Q^(0)+gQ^(1)+g^2Q^(2). Subtracting the square
through order two from the exact square leaves

\[
 g^3\{Q^{(1)},Q^{(2)}\}+g^4(Q^{(2)})^2
       +g^4\{Q_{\rm app},F_g\}+g^8F_g^2,
\]

where {P,Q}=PQ+QP. Apply (34), use g<=1, multiply by
2|h_e|/a, and sum over the three alpha values and all
original edges. This gives exactly the first line of (32).
All coefficient derivatives in the composition are retained.

For the potential let A_m=v_m^alpha T_alpha in (21).
Its operator norm is |v_m|/2. At real g each exponential
is unitary. The product rule for the fifth derivative and
the multinomial theorem therefore give

\[
 \left|\frac{d^5}{dg^5}\operatorname{tr}
                   \prod_{m=1}^4e^{gA_m}\right|
 \le2\left(\sum_m\|A_m\|\right)^5
 \le2\left(\frac{q_pR}{2}\right)^5.
\]

The integral Taylor remainder after degree four is bounded
by this number times g^5/5!. Multiplication by the original
1/(2g^2a), summation with |h_p|, and ||f||_2<=||f||_(2,Sigma)
give the second line of (32). This proves (33) without a
uniform-volume assumption or an estimate on unspecified
unbounded states outside the compact chart core.

## 8. Residual gauge invariance, parity, and exact scope

The remaining SU(2) gauge action rotates every x_c by the
same adjoint matrix in SO(3). Dot products and scalar triple
products in (23)--(24) are invariant under that action;
the epsilon and delta tensors in (16)--(17) transform
covariantly in their derivative indices. The original graph
numbers t,s and the physical weights carry no color indices.
Consequently H_n and D_{h,n} preserve the exact residual
physical subspace. The density and the compact radial cores
are invariant under the same rotations.

Let parity act only on the Lie-algebra coordinates by
\((\mathcal Pf)(x)=f(-x)\). It does not change the physical
edge positions, spacings, graph orientations, or weights.
The coefficients A_0,A_1,A_2 have degrees zero, one, and two;
W_2,W_3,W_4 have degrees two, three, and four. Since a
derivative changes sign under this parity,

\[
 \mathcal PH_0\mathcal P=H_0,\qquad
 \mathcal PH_1\mathcal P=-H_1,\qquad
 \mathcal PH_2\mathcal P=H_2,
                                                               \tag{35}
\]

and the same identities hold for D_{h,0},D_{h,1},D_{h,2}.
All these expressions are formally symmetric on the smooth
compact core; this follows also by expanding the exact
symmetric weighted operator with the norm remainder (33).

Simultaneous x->-x is not an adjoint SO(3) rotation. It
therefore does not remove the odd cubic gauge-invariant
terms. For the even full Gaussian Phi_0 of H_0,
<Phi_0,H_1 Phi_0>=0 follows exactly from (35): H_1 has
polynomial coefficients, so this Gaussian matrix element is
integrable, and changing x to -x reverses its sign. The same
is true of <Phi_0,D_{h,1}Phi_0>. These calculated matrix
elements are not an assumption of differentiable eigenvalues
or of a globally convergent perturbation series at g=0.

Equations (27)--(33) give the full requested operator and
weighted-observable coefficients with a controlled local
remainder. Using them in vacuum, spectral, or simultaneous
continuum perturbation theory requires actual estimates for
the relevant states and tails; the compact-core statement
does not replace those estimates. The original nonlinear
operator and every finite graph interaction remain the
objects from which these coefficients were computed.

## Proof dependencies

The exact maximal-tree quotient, Haar measure, and full
finite-box operator are proved in *The original finite-box
SU(2) Hamiltonian at small positive coupling*. The full-measure
dilation isometry and physical Gaussian are proved in *Actual
weak-coupling vacuum, observable and spectral maps*. The
original weighted local-energy operator and its exact
vacuum/covariance response at positive coupling are retained
in *Local-energy spacetime kernel and the exact nonlinear
coupling response*. The present note evaluates the higher
graph coefficients directly from those exact maps.
