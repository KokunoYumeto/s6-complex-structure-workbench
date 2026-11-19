# The complete integer pair on source-zero vertical fans

Reconstructed by checks from the complete audited conversation after the
execution-environment loss, 17 November 2026. The original working proof
passed root and fourfold, including all coupled-loop edge maps. This is
a reconstruction with fresh formatting and a fresh certificate; it does
not claim the lost file's byte hash.

## VZ.1. Actual source, period and normal maps

Retain the two actual source-zero families and all their realized cap
characters. The source parameter is \(v\), its positive angle is
\(\theta\), and \(q\) is the selected cusp coordinate. The fixed-scalar
periods, with every analytic unit retained, are
\[
 h:(Z,V)\longmapsto(\kappa qZ,\alpha V),\qquad
 B:(Z,V)\longmapsto(gZ,q\eta V),\qquad
 \operatorname{wind}(\kappa,\alpha,g,\eta)=(1,-a,b,-2),
\]
where \((a,b)=(1,2)\) or \((2,1)\), so \(ab=2\) and \(a+b=3\).
The columns are \(h,B\); in particular \(\operatorname{wind}g=b\).

For the literal vertical fan \(T_j\), use \(V_j=Z^{-j}V\) and
\(h_j=hB^j\). The full period characters are
\[
 Q_j=\kappa qg^j,\quad
 \alpha_j=\alpha\eta^j\kappa^{-j}g^{-j^2},\quad
 g_j=g,\quad \eta_j=\eta g^{-j}.                       \tag{VZ.1}
\]
Consequently
\[
 W_j=
 \begin{pmatrix}1+bj&b\\-a-3j-bj^2&-2-bj\end{pmatrix}
 =\binom1{-a-j}(1+bj,\ b).                            \tag{VZ.2}
\]
No periodic logarithm of \(g\) is used.

Put \(Q(q,v)=\kappa(q,v)q\). The actual source-disc map is defined by
\[
 Q(q',v)=Q(q,v)g(q,v)^j,\qquad
 q'=a_j(q,v)q,\qquad a_j(0,v)=g(0,v)^j.                \tag{VZ.3}
\]
The analytic inverse function theorem, uniform shrinking over the compact
parameter annulus, and uniqueness give a single periodic holomorphic map
and its inverse. Identity on the marked Tate coordinate identifies the
source periods. For the remaining suspension translation put
\[
 c(q,v)=g(q',v)/g(q,v),\qquad
 (Z,\gamma_j)\longmapsto(c(q,v)^{\gamma_j}Z,\gamma_j).
                                                               \tag{VZ.4}
\]
The logarithm of \(c\) is the unique one zero on \(q=0\). The identity
\(c^{\gamma_j+1}g(q)=g(q')c^{\gamma_j}\) is the complete suspension
square. On the two node charts this acts by reciprocal normal units,
so it extends and is the identity on the fixed locus.

Use the marked contracting-\(B\) coefficient in the F9 proper height
coordinate on both sides. The two node-preimage lifts have the prescribed
strict decreasing order in one short real arc. The actual \(h_j^{-1}\)
identifying the second chart has zero \(B\) coefficient. Thus the
source map carries the whole fixed graph and its distinct endpoint
heights; interpolation of the two proper decreasing coordinates has
no integer-height crossing. The full line norms are carried by this
same map.

In the native fixed star, \(q=ZAB\), the source-normal map is
\[
 (Z,A,B)\longmapsto(Z,a_j(q,v)A,B).                    \tag{VZ.5}
\]
It intertwines the second chart \(A_1=ZA,B_1=ZB\) exactly; its inverse
uses the specified inverse \(q\)-map. The higher \(q\) terms have no
normal linear contribution. The character shear is the typed Cartier
tensor map, multiplication by \(Z^j\) from the new line to the old.
It preserves the adjoint normal bundle. The remaining normal coefficient
is therefore exactly \(g(0,v)^j\), of winding \(bj\).

## VZ.2. The actual Hopf boundary map

Write
\[
 u=(1+\mathbf jZ)/\sqrt{1+|Z|^2},\quad h=ui u^{-1},\quad
 Q_N=A+\mathbf j\bar B,\quad q_H=uQ_N.
\]
Carry the initial normal map into both references and remove its positive
modulus by the same positive Cox path. On a cut parameter interval write
\(g(0,v)^j/|g(0,v)^j|=e^{i\alpha}\), with \(\alpha(0)=0\) and
increment \(2\pi bj\). For \(H=e^{i\alpha/2}\), the literal map is
\[
 Q_N'=H Q_N H,\qquad
 q_H'=e^{h\alpha/2}q_H e^{i\alpha/2}.                 \tag{VZ.6}
\]
The two half-phase endpoints are both \((-1)^{bj}\); their product is
a closed physical-circle-equivariant map. Its orbit-sphere action is
\(\eta\mapsto\operatorname{Ad}(e^{h\alpha/2})\eta\).

The constant-in-\(h\) map \(C(q_H)=Hq_HH\) extends over the actual
\(D^3_h\) cap. Compose the map \(F\) of (VZ.6) on the right with
\(C^{-1}\). The resulting coordinate arrow is
\[
 q_H\longmapsto A_j(h,\theta)q_H,\qquad
 A_j=e^{h\alpha/2}e^{-i\alpha/2}.                     \tag{VZ.7}
\]
Its zero-winding factor contracts by its specified real logarithm,
retaining both endpoints. Set \(N=bj\). The resulting map is
\(e^{\pi N\theta h}e^{-\pi N\theta i}\). Its preimages of \(-1\)
have \(h=-i\) and \(\theta=(2r+1)/(2N)\). In the outward domain
basis \((j,-k,\partial_\theta)\) its differential is
\((k,j,2\pi Ni)\). The positive target basis at \(-1\) is
\((i,j,-k)\); the determinant is \(2\pi N\). Thus
\[
              \deg A_j=bj                           \tag{VZ.8}
\]
in outward \(S^2_h\) times positive parameter orientation. The complex
orientation of the source fixed curve is \(-S^2_h\). That sign is
retained in the cap computation below.

## VZ.3. The complete line comparison

Use \(u,t,d,\gamma\) for the real coefficients of the source vanishing
period, \(h\), physical delta and \(B\), respectively; \(t\) here is not
the source parameter \(v\). The two actual character maps give
\[
 u_j=u,\quad t_j=t,\quad\gamma_j=\gamma-jt,\quad d_j=d-ju.
                                                               \tag{VZ.9}
\]
For the meridian-one dual line \(U=M^*\), the integral parts of the
actual full coefficient connections are
\[
 A_0=dd+(\alpha_q-2\theta)d\gamma-a\theta\,dt,
\]
\[
 A_j=dd_j+(\alpha_q-(2+bj)\theta)d\gamma_j
                     -(a+3j+bj^2)\theta\,dt.        \tag{VZ.10}
\]
Their difference in original coefficients is
\[
 A_j-A_0=-j\{du+(\alpha_q+\theta)dt+b\theta\,d\gamma\}.
                                                               \tag{VZ.11}
\]
Including the actual unit terms, the braces are
\(du+\alpha_Qdt+\phi_gd\gamma\). The \(q\) deck changes \(u\) by
\(-t\), and the parameter deck changes it by \(-t-b\gamma\);
the invariant form retains both changes.

Under (VZ.3), the target phase is
\(\alpha_q'=\alpha_q+bj\theta\) plus its full zero-winding unit term.
In the new coefficients the target reference connection is
\[
 A_{0,q'}=dd_j+(\alpha_q+(bj-2)\theta)d\gamma_j-a\theta\,dt.
\]
Hence the two residual parameter terms are
\[
 A_j-A_{0,q'}=-(3j+bj^2)\theta\,dt-2bj\theta\,d\gamma_j
                    +\text{the full unit correction}.          \tag{VZ.12}
\]

Make the actual graph maps \(b,\gamma\), with outer values \(t,\gamma_j\),
constant near the fixed sphere using their real lifts. Use nested tubes
\(U_0\subset U_1\subset U_2\), with every surgery and connection change
inside \(U_1\) and the level maps constant on \(U_2\). They extend over
the same three-ball cap. The theta-cut coefficient arrows
\(w\mapsto e^{2\pi ib}w\) and \(w\mapsto e^{2\pi i\gamma}w\)
define lines with curvatures
\[
 \Xi=d\theta\wedge db,\qquad \Psi=d\theta\wedge d\gamma,\qquad
 \Xi^2=\Xi\Psi=\Psi^2=0.                              \tag{VZ.13}
\]
The full integral evaluations give
\[
 U_j\simeq U_{0,q'}\otimes
 T_b^{-(3j+bj^2)}\otimes T_\gamma^{-2bj}.              \tag{VZ.14}
\]

This isomorphism retains the outer gauge. After the displayed period
and meridian evaluations, the sole boundary obstruction is the \(q\)
angle: \(q\)-monodromy kills \(u\) primitively, whereas theta, \(b\)
and gamma extend. At one theta choose the actual free section disc
\(|Z_*|=1,\gamma=t=0\), avoiding the marked sections and fixed graph.
The prescribed \(Z_*^{-j}\) arrow and both tensor frames extend there,
so the boundary ratio has zero \(q\)-angle degree. In vector frames
\(e_l=e^{2\pi ir_{il}}e_i\), remove the zero integer two-cocycle;
a partition of unity gives \(r_{il}=a_l-a_i\).
Replacing \(e_i\) by \(e^{-2\pi ia_i}e_i\) trivializes the ratio.
Remove its extending theta, \(b\) and gamma characters, then extend
its remaining real boundary logarithm by a collar cutoff. The inverse
trivialization is exactly (VZ.14), with the prescribed outer arrow and
the carried inner cap (VZ.7).

## VZ.4. The exact tangent collar

Put \(\tau=\log Q/(2\pi i)\), \(G=\log g/(2\pi i)\), and
\(\delta G=\log c/(2\pi i)\). Only the last logarithm is periodic.
In the full invariant source coframe
\(\omega=du+\operatorname{Re}\tau\,dt+
\operatorname{Re}G\,d\gamma\), the actual pullback is
\[
 \omega'=\omega+\operatorname{Re}\delta G(d\gamma-jdt),\quad
 dt'=dt,\quad d\gamma'=d\gamma-jdt.                   \tag{VZ.15}
\]
The full base map is
\[
 r'=r+\log|a_j|,\quad
 \alpha'=\alpha+\arg(a_j)/(2\pi),\quad\theta'=\theta.  \tag{VZ.16}
\]
Its derivatives are single-valued and retain the winding \(bj\).
The full coframe matrix is block triangular with this base Jacobian
and the source block
\[
 \begin{pmatrix}
 1&-j\operatorname{Re}\delta G&\operatorname{Re}\delta G\\
 0&1&0\\0&-j&1
 \end{pmatrix}.                                     \tag{VZ.17}
\]
In the source order \((\omega,\gamma,t)\) it is upper triangular with
diagonal one. All base-to-source entries lie in the off-diagonal block,
so the curvature-square trace is the sum of the two diagonal-block
traces. The unipotent source trace is zero. The base interpolation lives
on the boundary variables \(\alpha,\theta\) and one collar coordinate,
so its curvature square is zero by dimension. This supplies a connection
with \(\operatorname{tr}(F^2)=0\) on the whole comparison collar, not
merely flat endpoints. The line phases stay in (VZ.10)--(VZ.14).
Use the actual image cut under (VZ.16); no radial coordinate map is
claimed to preserve the source functions.

## VZ.5. The four relative interior pairings

For the carried dual-line curvature \(F\), use
\[
 \Omega_+=dr\wedge d\alpha\wedge du\wedge dt
                  \wedge d\gamma\wedge d\theta.      \tag{VZ.18}
\]
The required pairings, with their prescribed boundary connections, are
\[
 \int F^2\Xi=1,\quad \int F^2\Psi=0,\quad
 \int p_1\Xi=0,\quad \int p_1\Psi=2.                 \tag{VZ.19}
\]

For the first pairing freeze theta. All four actual units then have
holomorphic logarithms on the protected \(q\) disc. The exact BW.2
source, graph, line and Hopf-cap flows, with the same closing exponent
and full coefficient boundary frame, give its relative calibration.
The actual SCN.9/K62 comparison has both outer normal maps and its
common inner physical gauge extending; its separate characteristic
terms vanish, and its whole collar is \(3\int F^2\Xi-3\).
Thus the pairing is one. No logarithm of \(g\) around the parameter
circle is taken. The carried boundary connection makes this slice
pairing constant.

For the Psi Euler pairing choose gamma zero outside the fixed graph's
short arc. This level is the actual \(I_1\) source neighbourhood \(E\),
disjoint from the surgery and cap. At fixed theta its boundary
connection is \(dd-a\theta\,dt\), which is closed. The \(q\) deck
changes \(d\) by minus gamma, so its \(q\) holonomy is zero. The line
has degree zero on the sole normalization sphere, exactly its integral
Chern class since \(E\) retracts to the nodal fibre.
The graph map \(b\) extends over the vanishing-cycle handle by its
constant attaching-circle lift and collar cutoff. The flat line with
graph holonomy \(e^{-2\pi ia\theta}\) has boundary connection
\(dd-a\theta\,db\). Its comparison with the actual line has zero
\(q\)-angle winding by the literal disc \(Z_*=-1,\gamma=0\), where
the Cartier frame, \(Z_*^{-j}\) arrow and complete \(q'\) map extend.
A Cech trivialization, the extending \(b\) character, and the final
real boundary logarithm make its relative boundary value exact.
Transport the flat connection through this isomorphism. Its square
vanishes, giving the second pairing. Terms containing \(d\theta\)
vanish after multiplication by Psi, so all parameter-dependent gauges
remain included.

For the Xi Pontryagin pairing, choose a regular graph level missing
\(U_2\). It is relatively cobordant to the original source-three-level
times gamma, with the source-pulled connection. The four-form integrates
to zero there; the comparison collar has zero transgression by
(VZ.15)--(VZ.17). This uses nested tubes and does not extend a product
description through the surgery.

For the last pairing keep the actual nodal source frame. In \(xy=q\),
with \(\Omega=dx\wedge dy\), put
\[
 V=(x,-y),\qquad H=(\bar y,\bar x)/R^2,\qquad R^2=|x|^2+|y|^2.
\]
Then \(dq(H)=\Omega(V,H)=1\). The fixed-\(x\) and fixed-\(y\) Tate
horizontals are literally
\[
 H_x=H-\frac{\bar y}{xR^2}V=(0,1/x),\qquad
 H_y=H+\frac{\bar x}{yR^2}V=(1/y,0).                  \tag{VZ.20}
\]
Scaling their shear coefficients gives determinant-one homotopies.
The normalized frame
\[
 (V/R,RH)=R^{-1}
 \begin{pmatrix}x&\bar y\\-y&\bar x\end{pmatrix}
                                                               \tag{VZ.21}
\]
has degree one, so the relative second Chern number is one.
The actual \(q\)-polar frame \((V,qH)\) has determinant \(q\);
its relative first Chern class is the fibre, whose square is zero
by disjoint parallel fibres. Hence the source relative \(p_1\) is
\(-2\). The real period frame differs by (VZ.20) and the positive
matrix of its marked period lattice; the polar rotation factors
through its angle circle and has no third transgression.
Finally \(\Psi=d\theta\wedge d\gamma\) reverses the last two factors
of (VZ.18), giving the asserted \(+2\).

## VZ.6. The cap and the original-boundary Euler collar

The complex fixed curve has orientation \(-S^2_h\). The physical
quotient near the fixed tube has orientation
\(-S^2_h\wedge dr\wedge S^2_\eta\); its inner boundary is
\(+S^2_h\times S^2_\eta\), so the inserted cap is
\(-D^3_h\times S^2_\eta\). With coordinate clutch
\(v_{\rm ref}=A_jv_j\), its difference base is
\[
 -(D^3_j\cup-D^3_{\rm ref})\times S^1_\theta.         \tag{VZ.22}
\]
In the positive-spinor representation,
\(\int\operatorname{tr}(A^{-1}dA)^3=-24\pi^2\deg A\).
Use the radial connection \(f(r)A^{-1}dA\) in the first frame,
equivalently \(-f(r)dA A^{-1}\) in the second. The stated clutch
and boundary direction give
\[
 c_1(E)=0,\quad c_2(E)=-bj,\quad
 p_1(\operatorname{ad}E)=4bj.                        \tag{VZ.23}
\]
The physical tautological line has fibre value minus one.
The projective relation yields positive-parameter pair
\((-bj,-4bj)\); K68's literal parameter reversal gives
\[
                 (\Delta k,\Delta\ell)_{\rm cap}=(bj,4bj).
                                                               \tag{VZ.24}
\]
The constant map \(C\), positive factors and unit logarithms extend
as already specified, so this is the cap of the actual line arrow.

In the original exterior expressed in the piece coefficients
\(\gamma=\gamma_j\), the complete integral connection and primitive are
\[
 A_{\rm ext}=dd_j+(\alpha-2\theta)d\gamma+j\,du+
                        [j\alpha-(2j+a)\theta]dt,
\]
\[
 \beta=-j\{du+[\alpha+(1+bj)\theta]dt+b\theta\,d\gamma\}.
                                                               \tag{VZ.25}
\]
The full unit terms are the derivatives of the carried coefficient
maps. Their relative Cech boundary arrow is fixed; the zero-period
factors deform together with that endpoint primitive retained.
In \(\Omega_B=d\alpha\wedge du\wedge dt\wedge d\gamma\wedge d\theta\),
direct exterior differentiation gives
\[
 3\int_0^1\beta(F_{\rm ext}+s\,d\beta)^2\,ds
          =(-6aj-9j^2-2bj^3)\Omega_B.                \tag{VZ.26}
\]
The actual outward interpolation is from piece one to exterior zero,
so its contribution is \(6aj+9j^2+2bj^3\). Its tangent transgression
is zero by VZ.4.

## VZ.7. Independent fixed-scalar integer assembly

The K68 physical/dual line map and parameter reversal give
\(k=\int_{\Omega_+}F_U^3\), \(\ell=\int_{\Omega_+}p_1F_U\)
in this comparison. Equations (VZ.13), (VZ.14) and (VZ.19) give
\[
 \Delta k_{\rm int}=-9j-3bj^2,\qquad
 \Delta\ell_{\rm int}=-4bj.                          \tag{VZ.27}
\]
Adding the actual cap and original-boundary collar yields
\[
 \Delta\ell=0,\qquad
 \Delta k=2bj^3+(9-3b)j^2+(6a-9+b)j=6P_b(j),
\]
\[
 P_b(j)=2b\binom{j+1}{3}+(3-b)\binom{j+1}{2}.        \tag{VZ.28}
\]
The final equality uses \(a+b=3\). NC/K86 supplies reference pair
\((\mu_0,4\mu_0)\), where \(\mu_0=1\) in the good branch and zero
in the reduced branch. Thus
\[
 (k_j,\ell_j)=(\mu_0+6P_b(j),4\mu_0),\quad
 (\mu_j,\nu_j)=(\mu_0,6P_b(j)),\quad A_j=P_b(j).       \tag{VZ.29}
\]
This is an integer computation before reduction modulo 28.
Explicitly \(P_2(j)=j(j+1)(4j-1)/6\) and
\(P_1(j)=j(j+1)(j+2)/3\). K82 supplies only an independent
residue check, not an integer selection.

## VZ.8. All four native phase-square edges

Use the actual RT.12 independent parameters
\(v=v_*e^{2\pi it}\), \(r=r_{\rm base}e^{2\pi i\rho}\),
where \(r_{\rm base}=v_*^c r_0\), \(r_0^m=\lambda_0\).
Retain the full RCZ map and norm
\[
 B=r^mB_0(v),\quad A=r^nA_0(v),\quad
 F=F_0(v)+n\frac{\log r}{2\pi i}s_\infty\delta,\quad A_0^m=B_0^n,
                                                               \tag{VZ.30}
\]
with either realized \(n=\pm1\). Here \(F\) is ordinary-to-cap.
Since \(q=q_\infty^{-1}h_\infty\), increasing \(\log r/(2\pi i)\)
by one gives the literal directed square
\[
 F_{\rm end}R_{\rm ord}=R_{\rm cap}F_{\rm start},\qquad
 R_{\rm ord}=q^n,\quad R_{\rm cap}=h_\infty^n.         \tag{VZ.31}
\]
Both \(s_\infty\) terms cancel. This preserves the actual finite
characters, reduced Cartier correction and complete \(F_0\).

At the selected cusp, include \(r_{\rm base}^m\) in \(\eta\), but
exclude its variable phase. On the source cut use full logarithms
\(G=\log g,H=\log\eta\), with exact jumps
\[
 G(t+1)-G(t)=2\pi ib,\qquad H(t+1)-H(t)=-4\pi i.
\]
After the forward \(q^n\) arrow and the actual \(B^{-n}\) reindex,
the scalar endpoint is \(E_r=(g^{-n},\eta^{-n})\).
The current-to-reference cut product is
\[
 C(t,\rho)=(A,D),\quad
 A=e^{n\rho G(t)},\quad
 D=e^{n\rho H(t)+\pi inm\rho(\rho-1)}.                \tag{VZ.32}
\]
It is the inverse of the K30 reference-to-current product and
\(C(t,1)E_r(t)=1\) on full collars. For \(T_j\) put
\(D_j=DA^{-j}\). Its exact native chart factors are
\[
 (z,c_0,c_1)\longmapsto
 (Az,(AD_j)^{-1}c_0,D_jc_1).                         \tag{VZ.33}
\]
The Cox lift is
\((a_0,a_1,c_0,c_1)\mapsto
(a_0,Aa_1,(AD_j)^{-1}c_0,D_jc_1)\).
The second chart factors are \((A^{-1},D_j^{-1},AD_j)\);
both preserve the physical circle and \(q\).

The four edges are explicit. At \(\rho=0\) the product is the identity,
the fixed-scalar source product. At \(t=0\) it is the exact inverse
K30 scalar product with the actual amplitude. At \(\rho=1\) it is
\((g^n,\eta^n)=E_r^{-1}\). On \(t=1\) relative to \(t=0\), its full
mismatch in these characters is
\[
 K_j(\rho)=
 (e^{2\pi inb\rho},e^{-2\pi in(2+bj)\rho}).           \tag{VZ.34}
\]
All zero-winding units have equal endpoint values; their chosen
logarithm differences are the two integers just displayed.

For native factors \((a,p,q_1)\) with \(apq_1=1\), the literal
quaternion lift has \(L^2=pq_1,\ R^2=p/q_1\).
Substitution gives
\[
 L=e^{-\pi inb\rho},\quad
 R=e^{\pi in(4+2bj-b)\rho},\quad q_H\longmapsto Lq_HR.
                                                               \tag{VZ.35}
\]
Both endpoint half-phases equal \((-1)^{nb}\); the full map closes
even in the odd case. The base \(h\) and orbit sphere \(\eta\) both
rotate by \(\operatorname{Ad}L\), so this is the literal extending
linear rotation on \(D^3_h\times S^2_\eta\), with principal lift
(VZ.35). The base and normal Spin endpoints are both \((-1)^{nb}\);
their product is one. The normal map is independent of \(h\), hence
its primary third classes vanish by its factorization through the
parameter circle. Positive moduli use the same positive Cox maps at
both references with their explicit triangular derivative homotopy.

## VZ.9. Every scalar seam and the coupled integer pair

The same formula is defined for \(0\le\rho\le c\). At integer \(\rho=c\)
the quadratic factor is one because \(c(c-1)\) is even, and
\[
 C(t,c)=(g^{nc},\eta^{nc}),\qquad C(t,c)E_r^{(c)}(t)=1.
                                                               \tag{VZ.36}
\]
Every intervening seam is the accumulated product of the actual
endpoint maps. The ordinary and cap endpoints are \(q^{nc}\) and
\(h_\infty^{nc}\), with the same \(F_0\) and finite-character square.
The two half-phases at this endpoint are \((-1)^{nbc}\).

On the coupled diagonal \(\rho=ct\), the earlier DZ product has
current-to-reference logarithm
\[
 (nctG(t),\ nctH(t)+2\pi inm c^2t^2).
\]
Its difference from (VZ.32) is precisely
\[
                  \pi inm(c^2t^2+ct)\delta.          \tag{VZ.37}
\]
Its exponential is one at both endpoints because \(c(c+1)\) is even.
It is the actual physical delta loop, with its full winding retained;
it is identity on the orbit normal three-plane and extends over the
same physical line and Hopf cap. Flatten both products on the common
endpoint collars using (VZ.36). The remaining logarithm interpolation
carries every normal jet. Thus this is the actual DZ product comparison,
not a new product chosen on the fixed tube.

Apply the RT.12 based phase homotopy from \((t,ct)\) to the broken
source-then-scalar path at the retained amplitude. The four edge maps,
(VZ.35) and (VZ.37), identify its actual native caps; their only
mismatches are the displayed cap-extending maps. Thus free relative
coordinates add in the integral K23 group, or equivalently by the
exact normal-section and derivative composition. Its central
commutator does not alter these free coordinates. The same completed
pair-of-pants carries the physical line, so both characteristic
numbers add as integers.

At fixed source the actual scalar page has \(\chi=p\) and
\(H=ma^2/2\). K72 in this same native star gives scalar free pair
\[
 (\mu_{\rm sc},\nu_{\rm sc})=
 \left(6p,\ 6\left((a-1)(3p-1)-m\binom j2\right)\right).
                                                               \tag{VZ.38}
\]
The literal cap orders are \(m=4p\) in the good branch and \(m=4p-1\)
in the reduced branch. Combining with (VZ.29), and using
\(k_M=\mu+\nu,\ell_M=4\mu,A_M=\nu/6\), gives
\[
 \begin{aligned}
 k_j&=\mu_0+6P_b(j)+c[3H-3m j(j-1)],\\
 \ell_j&=4\mu_0+24cp,\\
 \mu_j&=\mu_0+6cp,\\
 A_j&=P_b(j)+c\left((a-1)(3p-1)-m\binom j2\right).
 \end{aligned}                                       \tag{VZ.39}
\]
The original coupled source construction has \(c\ge1\). The written
phase-square maps also carry every integer winding in the retained
contracting annulus. The full data table is
\[
 \begin{array}{c|c|c|c|c|c}
 (a,b)&m&\mu_0&\chi&H&A_{\rm scalar,0}\\\hline
 (1,2)&4p&1&p&2p&0\\
 (2,1)&4p-1&0&p&8p-2&3p-1
 \end{array}.                                        \tag{VZ.40}
\]
For the actual doubled ordinary product put \(t=cm-1\).
Its native-to-ordinary left correction is \(2t\), with the existing
DZ/K82 Cox arrows, and hence
\[
 V_{00}=2t-2\mu_j-12A_j,\qquad
 \delta_0=2t-2\mu_j+12A_j.                            \tag{VZ.41}
\]
These are full integer seeds; no lift is selected from a central
residue and no new global ordinary-product recurrence is asserted.

The executed local and assembly certificate is
code/part3/source_zero_vertical_pair.py. The independent component
audits were PS.1--7 and NP.1--4 by fourfold; their complete maps are
reproduced here. Root and fourfold passed the full proof in the
conversation before the environment loss.
