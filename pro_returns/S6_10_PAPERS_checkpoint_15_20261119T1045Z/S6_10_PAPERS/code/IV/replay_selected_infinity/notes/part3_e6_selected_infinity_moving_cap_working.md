# The moving selected fixed surface and its full reference cap

This calculation concerns the original E6 data \((a,b;m)=(6,1;2)\),
norm number \(n=1\), the retained finite character and scalar, the
initial negative-square fan of EI.70, and the positively oriented
full \(\epsilon=w^{-1}\) circle. We use the actual source, Cartier,
period and finite-cap arrows of EI, FO, FL and K68. The expression
computed here belongs to the single moving face \(\langle Q_0,Q_1\rangle\)
of FL.1 together with its specified reference cap. The other fixed
components retain their individual ledgers. In particular no total
return or free integral pair is assigned by this calculation.

## MC.1. The actual fixed surface and both blowdown maps

Let \(d=1-3\epsilon^2\),
\(\rho=\epsilon/\sqrt d\), \(\alpha=\epsilon/d\), and
\(u=\alpha/\rho=1/\sqrt d\), with the square root whose value is
one. These are the actual functions in EI.42--50. Their inverses
on the chosen discs are
\[
 \epsilon=\frac{\rho}{\sqrt{1+3\rho^2}},\quad
 d=\frac1{1+3\rho^2},\quad
 u=\sqrt{1+3\rho^2},\quad \alpha=\rho u.       \tag{MC.1}
\]
All disc sizes below are chosen inside these inverse domains.
On one selected collar the fourth-root source coordinate is the
actual inverse \(\chi=\chi(\sigma,H)\) of EI.65. On its fixed
surface \(H=q=0\),
\(\epsilon=\chi(\sigma,0)\sigma\) and
\(\rho/\sigma=\chi/\sqrt d\) are nonzero analytic units. We
retain these entire functions. The other three selected collars
are their images under the free fourth-root permutation of EI.71;
their quotient has this one representative, with no stabilizer
on the moving fixed surface.

The normalization coordinate is
\[
 Z=\frac{s-1}{s+1},\qquad z_1=u s,\qquad S=\alpha s=\rho z_1.
                                                        \tag{MC.2}
\]
The ideals at O and T are exactly \((Z-1,\sigma)\) and
\((Z+1,\sigma)\), with the full generator changes EI.79.
Near O put \(v=z_1^{-1}\); then
\(Z-1=-2uv/(1+uv)\). Near T one has
\(Z+1=2z_1/(u+z_1)\). Thus their ideals are literally
\((v,\rho)\) and \((z_1,\rho)\), by invertible two-by-two
diagonal generator maps whose coefficients have just been
displayed. The centres are distinct points of the central
\(\mathbf P^1_{z_1}\).

The q-factor chart of EI.69 has, on its y-factor representative,
\[
 y=s_Nt_N,\quad U=\sigma^4s_N,\quad V=t_Nx,
 \quad q=x s_Nt_N.                                    \tag{MC.3}
\]
Its fixed locus is \(s_N=t_N=0\), with coordinates \((\sigma,x)\).
At a source section graph \(\sigma=\eta v\), the last chart of
the nine-factor resolution has
\[
 U=\eta^4v^4s_N,\quad V=t_N,\quad q=s_Nt_N.             \tag{MC.4}
\]
Its fixed coordinates are exactly \((\eta,v)\). FO.26 leaves
this cone unchanged. All other common-refinement cones meet it
on its proper boundary faces, so they introduce no additional
modification of this fixed surface. Equations MC.3--4 and the
two source graph charts therefore identify this particular
fixed surface, as a complex surface over the parameter disc, with
\[
 F=\operatorname{Bl}_{(O,0),(T,0)}
                  (\mathbf P^1_{z_1}\times D_\rho).     \tag{MC.5}
\]
The charts at O are \(\rho=vS\) and \(v=\rho R\); the
charts at T are \(z_1=\rho z\) and \(\rho=z_1\zeta\).
On each overlap the inverse divides by the specified nonzero
coordinate. They are the ordinary blowup charts, including
their original parameter functions. The factors in EI.71
carry their full normal maps. The dense source-chart equalities
extend on these charts because both sides are the displayed
holomorphic maps, with identical Cartier generators.

The original source comparison is also explicit. Before the
T blowup, the O blowup resolves \(S=\rho z_1\): in its first
O chart \((v,S)\), the original coordinates are
\((S,\rho)=(S,vS)\); in its second O chart \((\rho,R)\),
\(S=R^{-1}\), interpreted in the inverse chart at \(S=\infty\).
Away from O the map is \((z_1,\rho)\mapsto(\rho z_1,\rho)\).
These are exactly the two charts of the blowup of
\((S,\rho)=(0,0)\) in \(\mathbf P^1_S\times D_\rho\),
together with its unchanged complement. The inverse in the
first original blowup chart is \(z_1=S/\rho\); in the other
it is \(v=\rho/S\). Those formulas are coordinates of the
respective blowup charts and hence extend at the exceptional
curves. This proves the actual elementary-transform isomorphism.

The T centre then becomes \((z_1,\rho)=(0,0)\) on that first
exceptional curve. Its two charts give
\[
 S=\rho^2z,
 \qquad (h,k,\rho)=(-\zeta,-z_1^2\zeta,z_1\zeta),       \tag{MC.6}
\]
which is the complete EI.49 map to \(hk=\rho^2\). Inserting
it into EI.46 or EI.48 retains the original resolved source
map and both moving node branches. The total-transform
exceptional basis \((e_1,e_2)\) has intersection matrix
\(\operatorname{diag}(-1,-1)\); the first strict exceptional
curve is \(e_1-e_2\), with square \(-2\). The native exceptional
curves in MC.5 become \(-e_1,e_2\) after the reference cap is
attached, and the native central strict curve becomes
\(e_1-e_2\). Their complete chain has squares
\((-1,-2,-1)\) and adjacent intersections one. Thus both
descriptions retain the contracted curve and the two actual
ordinary blowups.

## MC.2. The point and tensor arrows on the entire normalization

Write \(b=P^a\), where
\(P=-(1+\epsilon)/(1-\epsilon)\). We record the identities
for the two admitted line exponents \(a=2,6\); the surface
contribution in this note uses \(a=6\). The chosen nodal
theta ratio is
\[
 f_b(Z)=\frac{1-Z/b}{1-Z}
       =-\frac{1-b}{2b}(s-s_a),\quad
 s_a=\frac{1+b}{1-b},\quad S_a=\alpha s_a.               \tag{MC.7}
\]
This is a literal rational identity, including its zero and
pole divisors. EI.50 gives \(S_a(0)=-1/a\). The point line
on the original normalization has the globally nonzero
Cartier frame
\[
 e_M=\frac{\sigma_a}{S-S_a}.                            \tag{MC.8}
\]
Here the numerator is the canonical meromorphic section of
divisor \([aG]-[O]\), and \(S-S_a\) has that same divisor;
the quotient is the stated line-module isomorphism, including
the inverse chart at infinity. Neither marked divisor meets
the original graph centre \(S=\rho=0\). Pulling MC.8 through
both blowups therefore leaves a nowhere-zero frame on F.

Let \(u_M\) be its coefficient. The coefficient in the
canonical meromorphic point frame is
\(v_M=u_M/(S-S_a)\). Combining this equality with MC.7 and
the actual definition \(V_{\rm pt}=f_bv_M\) gives
\[
 V_{\rm pt}=\phi_a(\epsilon)u_M,
 \quad \phi_a=-\frac{d(1-P^a)}{2P^a\epsilon}.            \tag{MC.9}
\]
For both admitted a this is a holomorphic unit with value a
at zero. The apparent zero and pole have cancelled as the
two explicitly equal Cartier divisors in MC.8--9; no point
divisor or normal factor has been discarded.

The full normalized Miller function remains
\[
 f_{a,o}=\frac{(S+\rho^2)^a}{S-S_a}.                    \tag{MC.10}
\]
Its exceptional factors are
\(\rho^a(z_1+\rho)^a\) in the first chart and
\(\rho^{2a}(z+1)^a\) in the second. Its orders along the
two exceptional valuations are a and 2a, respectively.
Define \(C_2=2\) and \(C_6=6+20\epsilon^2+6\epsilon^4\).
The complete tensor-to-point coefficient on the selected
normalization is
\[
 H_o=\frac{\epsilon^{-a}d^{a-1}}{C_a(\epsilon)},
 \quad V_{{\rm tensor},o}=H_o V_{\rm pt},
 \quad H_o\phi_a=
       \left(\frac{d}{\epsilon(1+\epsilon)}\right)^a.     \tag{MC.11}
\]
These follow directly by substituting EI.26--27 and
\(\alpha^{1-a}\); the last equality is an exact rational
identity. Equations MC.9--11 retain the marked G numerator
and its two exceptional orders. Off the fixed surface the
coefficient is still the full smooth-fibre Cartier/theta
ratio EI.20 and EI.77. The normal derivative on the fixed
surface uses precisely its restriction MC.9--11, because
\(q=x s_Nt_N\) has zero first normal derivative there.
The original full functions and their higher derivatives
remain in the chart maps EI.69--71.

## MC.3. The actual normal bundle and its determinant

Order the normal coefficients as \((a_N,c_N)\), with physical
weights \((-1,+1)\). In the ordinary native fixed-edge chart
\(q=Za_Nc_N\) and \(V_{\rm pt}=c_N\). The ordinary two
source charts have the exact common normal transition
\[
 Z'=Z^{-1},\qquad a_N'=Za_N,\qquad c_N'=Zc_N.            \tag{MC.12}
\]
Thus each ordinary normal line is the indicated
\(\mathcal O_{\mathbf P^1_Z}(-1)\), with this coefficient
convention. The actual q-factor map MC.3 to it is
\[
 a_N=\sigma^{-4}t_N,
 \qquad c_N=\sigma^4s_N.                               \tag{MC.13}
\]
In the q-factor corner MC.4 the exact map instead is
\(a_N=Z^{-1}\sigma^{-4}t_N\), \(c_N=\sigma^4s_N\),
with \(\sigma=\eta v\). The full overlap is
\(t_y=Z^{-1}t_q\), \(s_y=s_q\); it changes the height
from \(q=s_qt_q\) to \(q=Zs_yt_y\) identically.
The factor Z and its inverse are nonzero on these O/T
neighbourhoods and are retained, including their source
derivatives. The normal factors of EI.71 for the
source unit \((\eta,v)\mapsto(\eta c_b,v/c_b)\) multiply
to one in MC.13. They retain every derivative of \(c_b\).
The point-frame unit is exactly MC.9 on F. Its multiplication
on the positive normal and reciprocal multiplication on the
negative normal agree with EI.78. No further exceptional
normal divisor appears, since FO.26 leaves this normal
chart unchanged and MC.9 is nonzero on every chart of F.

Let \(B\) denote the pullback of the line in MC.12 and
let \(F_0=\operatorname{div}_F(\sigma)\) be the complete
central fibre, including all its components with their
actual multiplicities. MC.13 is the meromorphic bundle map
\[
 N_-=B\otimes\mathcal O(4F_0),
 \qquad N_+=B\otimes\mathcal O(-4F_0).                  \tag{MC.14}
\]
The specified generators of these two divisor lines are
\(\sigma^{-4}\) and \(\sigma^4\). They prove that both
divisor lines are trivial as line bundles because \(F_0\)
is the divisor of the global parameter function. The maps
in MC.13 have the stated zeroes and poles as morphisms to
the ordinary ambient charts; those zeroes and poles have
not been replaced by bounded units.

The positive-weight spinor bundle is
\(E=\overline{N_-}\oplus N_+\). Complex conjugation is
the actual anti-equivariant map on the negative normal
coefficient; its weight becomes positive. Writing
\(h=c_1(\pi_Z^*\mathcal O(1))\), MC.12--14 give the
integral equality
\[
 c_1(N_-)=c_1(N_+)=-h,
 \qquad c_1(E)=-c_1(N_-)+c_1(N_+)=0\quad\text{in }H^2(F;\mathbb Z).
                                                        \tag{MC.15}
\]
For example the actual determinant transition over the
two native charts is \(\overline Z Z=|Z|^2\), a positive
function. Its positive-Hermitian normalization is one.
The whole spinor transition, including its SU2 factor,
remains part of the bundle.

On the outer parameter annulus the full new-to-original
normal map is the one in EI.23,
\[
 (a_N,c_N)\longmapsto
 (\epsilon^4d^{-3}\chi_L^{-1}a_N,\chi_Lc_N),
 \qquad\chi_L=(\epsilon/d)^{1-a}.                       \tag{MC.16}
\]
Its positive-weight arrow is the conjugate first factor
and the unchanged second factor. The two phase windings
are \(-(a+3)\) and \(1-a\), giving determinant winding
\(-2a-2\). Equivalently the original tensor-to-point
arrow MC.11 has determinant phase \(H_o/\overline H_o\)
of winding \(-2a\), the native tensor-to-point arrow
has winding \(-2\), and the original-height arrow has
winding \(-4\); their directed composite is
\(-4-2a-(-2)=-2a-2\). These are retained integers of
the actual maps. The conclusion MC.15 did not set any
of these boundary phases to one.

In particular the complete map from the completed
point-theta y-chart normals to the original tensor
normals is the diagonal map
\[
 (\overline{t_N},s_N)\longmapsto
 \left(\overline{\epsilon^4d^{-3}H_o^{-1}\sigma^{-4}}
                  \overline{t_N},\ H_o\sigma^4s_N\right).
                                                        \tag{MC.16a}
\]
In the q-factor chart its first coefficient also has
the full factor \(\overline Z^{-1}\). Thus MC.16a
retains the ordinary height, the point/tensor scalar,
the q-factor powers and the source-chart unit in one
arrow. Its two parameter windings on the y-chart
are \(-a\) and \(4-a\), and its determinant winding
is \(4-2a\). The additional actual Hopf and source
projective maps are those in MC.17 and PL.4--6 below.

## MC.4. The full reference cap and the integral gluing map

The reference cap of K68 is \(C_0=D^3\times S^1\), attached
to \(\partial F=S^2\times S^1\) with the specified physical
Hopf map and inverse-clutch direction PL.1--6. We use its
orientation opposite the product orientation on
\(D^3\times S^1\); this glues to the complex orientation
of \(\mathbf P^1\times D\). The base change MC.2 on
the boundary is a full parameter-dependent Möbius map.
It extends over this cap by an explicit map, rather
than by choosing a null-homotopy of that loop.

Realize the closed three-ball as the positive semidefinite
Hermitian two-by-two matrices Y of trace one. Its boundary
consists of rank-one matrices, so the map from its boundary
to \(\mathbf P^1\) is \([v]\mapsto vv^*/(v^*v)\). For
the actual matrix \(A(\epsilon)=\operatorname{diag}(\alpha,1)\)
in MC.2, set
\[
 \Psi_A(Y,\epsilon)=
 \left(\frac{A(\epsilon)YA(\epsilon)^*}
                   {\operatorname{tr}(A(\epsilon)YA(\epsilon)^*)},
       \epsilon\right).                               \tag{MC.17}
\]
On the boundary this is exactly \(s\mapsto S=\alpha s\).
Its inverse is the same formula with \(A^{-1}\). Its
denominator is positive on the entire closed ball, and
its differential is nonsingular by that inverse. The
positive-Hermitian lift carries the full physical spinor
and the phase on the boundary. The constant fractional
linear changes between Z and s are carried by the same
formula using their actual matrices. Matrix multiplication
commutes with MC.17, so the full composed boundary map
and its inverse extend to \(C_0\). Its orientation is
positive, as follows by a path in \(\mathrm{GL}_2(\mathbb C)\)
from each fixed A to the identity and the nonvanishing
Jacobian of its inverse; this uses no disc extension of
the parameter loop.

Use the entire K68 normal bundle clutch, including MC.11,
MC.13, MC.16 and the retained physical scalar and finite
character. PL.4's exact map
\(Q(a,c)=(\overline c,-\overline a)\), considered as
a complex-linear map to the conjugate spinor bundle,
carries the opposite circle and its associated line.
Its projective map is the actual antipodal map on the
traceless Hermitian three-ball. Its inverse and the
physical parameter reversal remain those of PL.6.
These arrows give the prescribed rank-two positive
complex bundle \(E_c\) on
\(F_c=F\cup C_0\), with its whole U2 clutch. No SU2
clutch degree is assigned or removed here.
Here MC.17 extends the map of the fixed-sphere base;
the projectivization in PL.4 acts on the normal Hopf
sphere. The resulting normal-sphere-bundle map covers
MC.17, with PL.4 as its stated fibre map.

The determinant computation on this closed base is an
integral Mayer--Vietoris computation. With the circle
oriented by positive \(\arg\epsilon\), the relevant
groups and maps are
\[
 H^1(F)\oplus H^1(C_0)=0\oplus\mathbb Z
  \ \xrightarrow{\ (0,-1)\ }\ H^1(\partial F)=\mathbb Z,
                                                        \tag{MC.18}
\]
and
\[
 H^2(F)\oplus H^2(C_0)=
 \mathbb Z\langle h,e_O,e_T\rangle\oplus0
 \ \xrightarrow{\ (1,0,0)\ }\
 H^2(\partial F)=\mathbb Z.                             \tag{MC.19}
\]
The first map is restriction from the literal product
cap with the Mayer--Vietoris difference sign. The second
map has degree one on the native sphere and zero on
the two interior exceptional divisors. These maps also
follow directly from the two blowup charts in MC.5:
they are the identity on the outer boundary. Exactness
therefore gives
\[
 H^2(F_c;\mathbb Z)\hookrightarrow H^2(F;\mathbb Z),
 \qquad\operatorname{image}=\mathbb Z\langle e_O,e_T\rangle.
                                                        \tag{MC.20}
\]
In particular every actual determinant phase on the
boundary has zero connecting class. At the level of
maps, any such phase g on \(S^2\times S^1\) can be
written \(g=e^{in\theta}e^f\) after dividing out its
actual integer degree n; the remaining zero-period
logarithm f exists by lifting to the universal cover
of \(\mathbb C^*\). Extend f over the ball using a
smooth collar extension and a cutoff that is constant
near the ball centre; the factor \(e^{in\theta}\)
already extends over \(D^3\times S^1\). This explicitly
extends the retained determinant map, including the
integer \(-2a-2\) in MC.16. It is not an extension over
the parameter disc and imposes no zero-winding assertion.
Since MC.15 is zero and \(H^2(C_0)=0\), the injective
map MC.20 proves
\[
 c_1(E_c)=0\quad\text{in }H^2(F_c;\mathbb Z).            \tag{MC.21}
\]
The full SU2 and parameter-dependent parts of the
clutch still determine \(c_2(E_c)\); that integer
remains unassigned in this note.

## MC.5. The tangent number and the normal-link expression

Without the two interior blowups, the fixed base and
the cap are \(S^2\times D^2\) and \(D^3\times S^1\)
with the preceding boundary map. MC.17 extends that
map over the second piece. Their union is consequently
the boundary of \(D^3\times D^2\), with its corners
rounded by the radial product collars, and has stable
trivial tangent bundle. Its Pontryagin number is zero.

For each of the two actual complex blowups the local
map \((x,t)=(r,rv)\) has Jacobian r; its reciprocal
chart is \((x,t)=(uw,w)\). These maps give
\(K_{\rm new}=\pi^*K_{\rm old}+E\), and the normal
overlap on E gives \(E^2=-1\). Pullbacks pair trivially
with E. Replacing one point by \(\mathbf P^1\) increases
the relative Euler number by one. Therefore the local
changes, with their complex orientations, are
\[
 \Delta c_1^2=-1,\quad\Delta c_2=1,
 \quad\Delta p_1=\Delta(c_1^2-2c_2)=-3.                \tag{MC.22}
\]
The blowdown is the identity on the prescribed outer
boundary. The two cap-clutched tangent bundles thus
have exactly this relative change. Both native centres
are ordinary distinct interior points, and MC.6 gives
the identical count in the original source graph.
It follows that
\[
 \int_{F_c}p_1(TF_c)=-6.                                \tag{MC.23}
\]

Finally take the physical positive normal spinor
\(E_c=\overline{N_-}\oplus N_+\) with the complex
orientation on the fixed base. Conjugating the first
normal complex line reverses the original real normal
orientation. The resulting inner circle-first quotient
is therefore the negative of the ordinary complex
projective-line bundle of \(E_c\). This is the same
explicit conjugation and circle orientation as K68
PL.1--2a and the strict-surface formula SS.5. Let
\(x=c_1(\mathcal O(1))\) on that projectivization,
and write \(c_i=c_i(E_c)\). Its projective relation is
\(x^2+c_1x+c_2=0\), with fibre integral \(\pi_*x=1\).
The vertical tangent line has first Chern class
\(2x+c_1\), so its square is \(c_1^2-4c_2\).
Consequently the actual quotient numbers in the U
convention satisfy
\[
 \begin{split}
 k_U&=-\int_{F_c}(c_1^2-c_2),\\
 \ell_U&=-\int_{F_c}\{p_1(TF_c)+c_1^2-4c_2\},\\
 \frac{4k_U-\ell_U}{24}
   &=\frac1{24}\int_{F_c}\{p_1(TF_c)-3c_1^2\}
     =-\frac14.                                       \tag{MC.24}
 \end{split}
\]
This cancellation retains the actual bundle \(E_c\):
the coefficient of its unassigned second Chern number
is exactly zero. Equations MC.21 and MC.23 determine
the displayed rational contribution directly, before
any sum with the other components. The physical M
expression is its negative under the literal K68
dual-line and inverse-clutch map. Neither individual
integer \(k_U\) nor \(\ell_U\), and neither total
source return, is recovered from MC.24 alone.

## MC.6. Exact record and scope

`code/part3_root/e6_selected_infinity_moving_cap.py`
checks the full rational identities MC.1--13 for both
admitted line exponents, both graph-to-source branches,
the blowup intersections and integral basis change,
the integer maps MC.18--20, all retained winding
integers, and the characteristic cancellation MC.24.
Its JSON, stdout and stderr retain the exact output.
The construction and boundary argument above supply
the geometric content of those identities; numerical
sampling is not used. Independent review is recorded
separately. The source-moduli return still requires
the other compact normal ledgers and the complete
outer mapping-torus and finite-cap transfer.
