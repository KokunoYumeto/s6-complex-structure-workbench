# The original M2 branch at selected infinity

Working proof for the actual datum \((M_a,b;m,n)=(M_2,3;3,1)\),
with its prescribed finite character, scalar root and complete annular
reference. The original scalar is fixed in a common strict-contraction
range for the compact charts below. The loop is one positive full
\(\epsilon=w^{-1}\) turn; the original selected height is retained.
This proof starts with the actual M2 source and line maps. The auxiliary
cube morphism CB.1--16 is retained separately and supplies no covering
division of a return.

## MB.1. The complete ordinary source and point-line map

Put \(d=1-3\epsilon^2\), \(\zeta=\epsilon^2\). The full source map is
\[
\begin{gathered}
 y^2=x^3+(3\epsilon^2-2)x^2+dt x+\epsilon^2t^2,
 \qquad G=(0,\epsilon t),\\
 x_o=\epsilon^2d^{-2}x,\quad y_o=\epsilon^3d^{-3}y,
 \quad t_o=\epsilon^4d^{-3}t,
 \quad r=\epsilon^2(3\epsilon^2-2)d^{-2},\\
 t_c=\epsilon^4(1-\epsilon^2)d^{-3},\quad
 q_o=t_o-t_c=\epsilon^4d^{-3}\bigl(t-(1-\epsilon^2)\bigr).
\end{gathered}                                                   \tag{MB.1}
\]
It carries the cubic, O, G and both ordered selected node branches.
On the original source set
\[
 s_0=1/4-r,\quad f_2(p)=\frac{y_o-t_o-x_o/2}{x_o-s_0},\qquad
 T(p)=p-G,
\]
\[
 k=(y_o+t_o)/x_o,\quad x'_o=k^2-r-x_o,\quad
 y'_o=t_o-kx'_o .                                             \tag{MB.2}
\]
The inverse uses the chord to \(+G\):
\(k_+=(y_o-t_o)/x_o\), \(x_o^+=k_+^2-r-x_o\),
\(y_o^+=-t_o-k_+x_o^+\). Substituting either composition and
the full cubic gives the identity. Both directions extend through
the two original source resolution charts of
\((y_o-t_o-x_o/2)(y_o+t_o+x_o/2)=x_o^2(x_o-s_0)\).
Here \(s_0\) is a unit. The full source arrow in this datum is
\(T^3\), the three chronological compositions of MB.2. Its actual
point-line coefficient and selected suspension are
\[
 B_{2,3}(p)=f_2(p)f_2(T^3p)f_2(Tp)^2f_2(T^2p)^2,
 \qquad B_o=\lambda\frac{q_o}{t_o^3}B_{2,3}.
                                                               \tag{MB.3}
\]
This is EX.1--2 derived from the typed tensor map
\(f_2^{-1}:M_2\to M_1^{\otimes2}\). The six factors and all
their source targets are part of MB.3. The finite I2 component
orders are three and three; the indicated selected factor cancels
that whole fibre, leaving exactly the selected whole zero.

On the complementary ordinary cover
\[
 \epsilon=\chi\sigma,\quad
 \bar Y^2=\bar X^3+a_2\bar X^2+d\bar X+\sigma^2,
 \quad a_2=(3\epsilon^2-2)\chi^2,
 \quad (x_o,y_o,t_o)=(\sigma^2d^{-2}\bar X,
       \sigma^3d^{-3}\bar Y,\sigma^4d^{-3}),
 \quad H=1-\chi^4(1-\epsilon^2).
                                                               \tag{MB.4}
\]
Write \(\bar T\) for MB.2 in this curve and put
\(\rho_{2,p}=(\tau-\tau(2G))/\tau\) at O, with the canonical
point section on its complement. The genuine coefficient is
\[
 \mathcal B_2^{\rm pt}(p)
  =\sigma^{-6}\bar B_{2,3}(p)
        \frac{\rho_{2,\bar T^3p}}{\rho_{2,p}},\qquad
 B_o^{\rm pt}=\lambda H\sigma^4\mathcal B_2^{\rm pt}.
                                                               \tag{MB.5}
\]
The complete divisor of \(\bar f_2\) is
\(2[G]-[2G]-[O]+[\sigma=0]\). Translating all four factors
in MB.3 with multiplicities \(1,1,2,2\) gives
\([2G]+[3G]-[5G]-[O]+6[\sigma=0]\).
The source/target genuine-frame ratio in MB.5 cancels the four
horizontal terms. Dividing by \(\sigma^6\) cancels the vertical
term. Thus MB.5 and its inverse extend as nonzero maps on both
point-section charts, including their intersections with the
central divisor. The exact central tangent limits give coefficient
64. This is a line-module statement, not a claim that the raw
meromorphic coefficient is a unit at its point divisors.

## MB.2. The actual three-step section graph and both normal charts

At O use \(\eta=-\bar X/\bar Y\), \(U=\eta^2\bar X\), with
\[
 1=U+a_2\eta^2+d\eta^4/U+\sigma^2\eta^6/U^2,\qquad U(0)=1.
\]
The two graph charts are \(\eta=\sigma p\) and \(\sigma=\eta v\),
with \(p=v^{-1}\). Their original source arrows are EI.58. At T,
the identity
\((\bar X,\sigma\bar Y,\sigma^2)=(\bar Y,\sigma)^2\)
gives the actual quadratic-Veronese graph; use
\(\bar Y=\sigma z,\bar X=\sigma^2A\) and its reciprocal chart.
Their equation is
\(z^2=\sigma^4A^3+a_2\sigma^2A^2+dA+1\).

The one-step chord lift is exactly EI.62. In particular it sends
O:p to T:\(p-1\), and T:z to O:\(z-1\) at \(\sigma=0\).
Composing its full analytic formulas three times gives
\[
 O:p\longmapsto T:p-3,\qquad T:z\longmapsto O:z-3.
                                                               \tag{MB.6}
\]
On the reciprocal graph overlap write its complete coefficient as
\[
 (\eta,v)\longmapsto(\eta c_3,v/c_3),\qquad
 c_3=c_1(p)c_1(\bar Tp)c_1(\bar T^2p),
 \qquad c_3|_{\eta=0}=1-3v.                              \tag{MB.7}
\]
Each factor is evaluated at its actual intermediate point. On
the dense reciprocal overlap the three central factors are
\(1-v,(1-2v)/(1-v),(1-3v)/(1-2v)\). Their product is
\(1-3v\); the p-chart MB.6 gives the extension at every omitted
intermediate point. The inverse is the three reverse source
chords. These are source maps, not three suspension periods:
MB.3 contributes the selected factor only once.

The actual point frame on this graph is
\[
 e_{2,p}=\sigma_2/\rho_{2,p},\qquad
 \rho_{2,p}=(p-c_2)/p=1-c_2v,
 \quad c_2=\tau(2G)/\sigma,
 \quad c_2|_{\sigma=0}=2.                                \tag{MB.8}
\]
Its inverse Cartier generator is retained through \(p=0,c_2\).
In these frames MB.5 has coefficient64 on the complete central
graph. In canonical meromorphic coefficients it is instead
\(64(p-2)/p\) on O and \(64(z-3)/(z-5)\) on T. These exact
ratios specify the two horizontal endpoint arrows.

The ordinary line chain is
\[
 X_jY_j=\sigma,\quad V=\sigma^jX_j,
 \quad B:(p,j,X_j,Y_j)\mapsto
 (\bar T^3p,j+4,\mathcal C X_j,\mathcal C^{-1}Y_j),
 \quad\mathcal C=\lambda H\mathcal B_2^{\rm pt}.
                                                               \tag{MB.9}
\]
The residual quarter action is
\((\chi,\sigma,X_j,Y_j)\mapsto
(i\chi,-i\sigma,i^jX_j,i^{-j-1}Y_j)\), with the actual
source action \((\bar X,\bar Y)\mapsto(-\bar X,-i\bar Y)\).
It fixes MB.8 and commutes with MB.9. The two source copies remain
distinct: \((C,j)\mapsto(\operatorname{other}C,j+4)\) has two
orbits for each residue \(j\bmod4\).

## MB.3. The complete selected and finite-quotient atlas

At the selected source collar take the full Tate coordinate
\(q=Q=\kappa H\), the chosen lift P of G and the point-theta
coordinate \(V_\theta=f_{P^2}v_M\). Its exact periods are
\[
 h:(Z,V_\theta)\mapsto(qZ,P^2V_\theta),\qquad
 B:(Z,V_\theta)\mapsto(P^{-3}Z,
       \lambda\sigma^4H\beta_2 V_\theta),
\]
\[
 \psi_2=f_{P^2}/\rho_{2,p},\qquad
 \beta_2=\mathcal B_2^{\rm pt}\frac{\psi_2(\bar T^3p)}{\psi_2(p)}.
                                                               \tag{MB.10}
\]
This keeps the full theta functions. In particular the two normal
products are \(UV=\sigma^4xy\), \(xy=q\), and in a section graph
\(UV=\eta^4v^4q\). Use all six and nine ordered-factor charts,
and the actual 38-cone common refinement of the grouped and
alternating orders. It gives 238 ordinary quotient charts and
39 selected charts. For any regular cone matrix N their physical
weights are exactly \(N^{-1}(0,0,0,1)^t\).

Here is the full coefficient map, which specifies this atlas for
the M2 datum. In the ordinary quotient characters
\((\chi^4,\chi\eta,v,V)\), the period ray map is
\[
 T_B=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\-1&4&4&1\end{pmatrix}.
                                                               \tag{MB.11}
\]
From a source cone N to a target cone \(N'\), its full character
matrix is \((N')^{-1}T_BN\). Its two unit columns are
\((N')^{-1}(0,1,-1,0)^t\) for the full \(c_3\), and
\((N')^{-1}(0,0,0,1)^t\) for the full \(\mathcal C\).
In the selected coordinates \((\eta,v,q,V)\), the period is
\(V\mapsto V+4\eta+4v+q\). Its full source unit vector is
\((1,-1,0,0)^t\), since the source arrow is
\((\eta,v)\mapsto(c_3\eta,c_3^{-1}v)\); the Hom coefficient
is \(\lambda\beta_2/\kappa\). Multiplication by \((N')^{-1}\)
gives both selected chart unit columns. The exact interface is
\[
 k=4j+r-1,\qquad
 X_k=\psi_2^{-1}q^j s_r,\qquad Y_k=\psi_2q^{-j}t_r.
                                                               \tag{MB.12}
\]
Every \(q^j\) remains a monomial through q zero. These equations
and MB.10 prove the complete period square on every parent face.
The projective factor ratios give the proper common refinement;
the two inverse cone-character maps carry all higher unit terms
and their normal derivatives. Thus this construction uses the
actual M2 chart maps, not a substitution in a residue table.

On the central selected disc P is the unit two-torsion branch
with limit \(-1\). Since \(P^2=Q^h\), its zero valuation gives
\(h=0\) and hence \(P=-1\). Thus \(P^2=1\) without an integral
source reindex. On the O graph write \(\tau=\sigma p\),
\(\tau(2G)=\sigma c_2\), and \(Z-1=\tau u(\tau)\).
The full ratio \(f_{P^2}/\rho_2\) is the product of the divided
difference \((Z(\tau)-Z(\tau(2G)))/(\tau-\tau(2G))\),
\(\tau/(Z(\tau)-1)\), and the remaining theta product divided
by \(P^2\). At \(\sigma=0\) the first two units cancel and
the last is one. This proves \(\psi_2=1\) through both point
charts; no 0/0 substitution is used.

The native finite source graph is IA's actual I2 resolution,
with \(\eta_e=\chi\eta\), \(\epsilon=\chi\sigma\), and the full
chain map
\[
 X_j=\chi^jA_j,\qquad Y_j=\chi^{-j-1}B_j,
 \qquad A_jB_j=\epsilon.                                \tag{MB.13}
\]
The two point Cartier ratios coincide because their numerator
and denominator both multiply by \(\chi\). The full source
translation here is again the composition of three IA chord
arrows, with all target charts retained.

At the remaining two central two-torsion points the single chord
has the full triangular source map ASI.2. Its threefold composite
preserves the same actual odd fixed ideal, as does its inverse.
If its complete ideal matrix is M, the blowup/quotient arrow is
\(\rho'=\rho(Mz)_\beta^2\),
\(z'_\gamma=(Mz)_\gamma/(Mz)_\beta\), with the entire neutral
line coefficient. This is the actual M2 lift through the two
\(\mu_2\) quotient resolutions. Its residual period is
\(\gamma^{-1}B\). The two odd chain pairs are still 1/2 and 3/4;
no second copy of those four nodes is introduced.

## MB.4. The complete fixed normal bundles

On a fixed component, differentiating a unit in MB.11 multiplies
a vanishing normal coordinate. Thus its normal coefficient is
exactly the displayed unit and tangent monomial, with no omitted
normal derivative. The only new central source unit is
\(c_3=1-3v\). Its full base arrow is the projective map
\[
 [p:1]\longmapsto[p-3:1],\qquad
 A_3=\begin{pmatrix}1&-3\\0&1\end{pmatrix}.             \tag{MB.14}
\]
The canonical homogeneous lift of this matrix on \(\mathcal O(-k)\)
has coefficient \((1-3v)^k\) in the reciprocal chart and the
corresponding p-chart coefficient one. These are precisely the
integer powers in MB.11. They extend at \(p=0,1,2,3,\infty\)
through the displayed intermediate p-charts. This proves their
normal line-bundle transitions and their degree; the zero of
\(1-3v\) is retained in the change of base chart.

The other central Hom unit is \(64\lambda H\), with H retained
in the selected q charts. MB.12 has period block zero on the
four strict and fourteen compact surface representatives; the
internal chain label \(j=0,1,2,3\) is distinct from that block.
Together with the exact \(\psi_2=1\), this gives the finite-base
normal clutch, including the Q0 extension, on all those stars.

For clarity the resulting global bundles can be read directly.
The strict source is the actual quotient of
\(\bar Y^2=\bar X^3-2\chi^2\bar X^2+\bar X\), with source map
\(t_e=\chi^{-4},x_e=\chi^{-2}\bar X,y_e=\chi^{-3}\bar Y\).
Let \(L^4=\mathcal O(F)\) be the line whose frame transition is
\(e_\infty=\chi^{-1}e_{\rm fin}\). The source normals at O,T
have coefficient \(\chi^{-1}\); hence
\[
 O^2=T^2=-1/4,\quad OT=0,\quad LO=LT=1/4,\quad L^2=0.
\]
The raw strict normal map and its common-refinement map are
\[
 s=\chi^{j+1}s_e,\quad t=\chi^{-j-1}t_e,
 \qquad s_{\rm raw}=a^{3-j}n_+,\quad t_{\rm raw}=n_-.
\]
They give the actual normal lines
\[
 N_{+,j}=\mathcal I_{O+T}^{4-j}\otimes L^j,
 \qquad N_{-,j}=L^{-j-1}.                               \tag{MB.15}
\]
The two characters are \(\chi^4,\chi^{-j-1}\). The A3 chains
and the A1 point corrections therefore have the same integral
degree vectors read by the full SS/FP wall relations. The sign
map is retained: the section \(\chi\) of character one meets
the last A3 exceptional curve, so its boundary Chern class is
\(-1\) in the chosen \(\mathbb Z/4\) generator. The relative
rational lift is the actual inverse intersection matrix applied
to each integral degree vector. The preserved source-volume
map supplies \(p_1=-24\) on the minimal source and the exact
crepant A3/A1 comparisons.

Every exceptional/refinement star uses the same source character
\(p=1/v\), native map \((t_e,\eta_e,v,V)
=(T_0^{-1},T_1,T_2,T_3)\), and the unit powers MB.11.
For the four exceptional products the negative line has the
explicit coefficient \(v^{j+1}\) and hence is
\(\mathcal O(-1,-j-1)\); the positive line is trivial.
For the remaining ten stars and twelve p-curves, the complete
normal matrices are the inverse cone matrices of MB.11--13.
The accompanying certificate recomputes these actual matrices,
all weights and their full normal rows; it retains their M2 unit
columns. The exact degrees and both characteristic summands are
then evaluated from those normal bundles.

## MB.5. The selected moving surface and its actual cap clutch

The unchanged q-factor cone is
\(U=\eta^4v^4s_N,V=t_N,q=s_Nt_N\).
The source ideals \((Z-1,\sigma)\), \((Z+1,\sigma)\) are
the two exact O/T ideals of EI.79. Their generator maps identify
the moving surface with
\(F=\operatorname{Bl}_{(O,0),(T,0)}(\mathbf P^1\times D)\),
including the two original-coordinate blowdown maps MC.1--6.
These equations do not involve a or b. Their full M2 point arrow
does: with \(P=-(1+\epsilon)/(1-\epsilon)\),
\[
 \phi_2=\frac{2d}{(1+\epsilon)^2},\qquad
 H_o=\frac{\epsilon^{-2}d}{2},\qquad
 V_{\rm pt}=\phi_2u_M,
 \quad V_{{\rm tensor},o}=H_oV_{\rm pt}.                \tag{MB.16}
\]
Here \(V_{\rm pt}\) is precisely the selected Tate point
coefficient \(V_\theta=f_{P^2}v_M\) of MB.10. Writing
\(V_{\rm gen}=\rho_2v_M\) for the ordinary genuine coefficient,
the full directed square is
\[
 V_{\rm gen}\ \xmapsto{\ \psi_2\ }\ V_\theta
      =\phi_2u_M\ \xmapsto{\ H_o\ }\ V_{{\rm tensor},o},
 \qquad \psi_2=f_{P^2}/\rho_2.
                                                               \tag{MB.16a}
\]
Thus the q-factor normal below is taken after the complete
MB.12 point-to-theta arrow, and \(\phi_2\) is the entire
module-frame arrow to \(u_M\). The two point-frame coefficients
are related by this stated morphism on both point charts.
This follows from the actual divisor \(S-S_2\) and
\(f_{2,o}=(S+\rho^2)^2/(S-S_2)\). Its exceptional orders
are two and four, and neither is discarded.

The signed normals are
\(a_N=\sigma^{-4}t_N,c_N=\sigma^4s_N\), with the additional
\(Z^{-1}\) on the first coefficient in the q-factor chart.
The source reset MB.7 cancels in their product. The complete
positive-spinor boundary arrow is
\[
 D_{\rm full}=\operatorname{diag}(\overline t/\overline r,r),
 \quad t=\epsilon^4d^{-3},\quad r=H_o\sigma^4.
                                                               \tag{MB.17}
\]
Its two phase windings are \((-2,+2)\). The exact polar identity
\(\operatorname{diag}(\overline r^{-1},r)
=(r/|r|)\operatorname{diag}(|r|^{-1},|r|)\)
retains the common phase of winding two. It extends along the
S1 factor of the actual cap \(C_0=-D^3\times S^1\); the remaining
zero-period factors extend by their explicit collar logarithms.
The positive factors deform by their real logarithms. The
remaining non-scalar arrow is exactly
\(\operatorname{diag}(e^{-4i\theta},1)\).

The full native product is the literal Cox quaternion product.
Its positive frame is
\[
 G_0(Z)=\begin{pmatrix}1&-Z\\\overline Z&1\end{pmatrix},
 \quad G_1(Z^{-1})\operatorname{diag}(\overline Z,Z)=G_0(Z).
\]
The actual completed-to-cap clutch is therefore
\[
 v_{\rm cap}=G_0\operatorname{diag}(e^{-4i\theta},1)G_0^{-1}v_F.
                                                               \tag{MB.18}
\]
The factor \(\operatorname{diag}(\overline Z^{-1},1)\) commutes
with the diagonal phase and is retained on the q chart. The
source Möbius cap map is the full Hermitian-ball map MC.17,
holding this transported Cox quaternion fixed and using the
physical Hopf phase; it is not a tangent derivative lift.

The bundle bordism MC2.3 uses exactly this first-to-second arrow.
Its parameter reversal is
\(\eta=\overline\xi/\epsilon_0^2\), with determinant
\(-\epsilon_0^{-4}\) and boundary \(\eta=1/\epsilon\).
Keeping both original windings gives the two capped roots
\(h+2u,-h-2u\), where \(h^2=u^2=0\), \(\int hu=1\).
Their product is \(-4\). Thus the actual moving bundle has
\(\kappa_c=-4\). The same normal map gives its primitive native
product; no value of \(\kappa_c\) has been selected from a residue.

## MB.6. The actual cubic good cap and its entire annular reference

The original infinity cap has
\[
 q_{\infty,o}=z^3,\quad
 (x_o,y_o,t_o)=(z^{-2}X,z^{-3}Y,z^{-3}),\quad
 Y^2=X^3+rz^2X^2+zX+1,
 \quad G'=(0,1),\quad D(z,X,Y)=(\omega z,\omega^2X,Y).
                                                               \tag{MB.19}
\]
The actual \(2G'=(s_0z^2,-1-(s_0/2)z^3)\) is retained.
At it and at O the quotient weights are \((2,1)\), and the
two resolution rays are \((2/3,1/3),(1/3,2/3)\).
The section support functions give the coefficient correction
\(\min(v_w,2v_z)\) and the full line-module equality
\(\beta^*N_2=\pi^*M_2+E_P-E_O\), with both monomial
Cartier generators retained. This is EX.14 in this actual cap.

The section \(Q'=3G'\) has \(\tau(Q')=-s_0z^2/2+O(z^5)\).
Let \(R=[3]^{-1}Q'\), the actual small formal-group division.
Its translation and inverse preserve the ideals \((w,z^j)\),
\((z,w^j)\), \(j=1,2\), and hence their common normalized graph.
For \(P=2G'\) the full starting lift is
\[
 F=\tau(R)\frac{\ell_{P,R}}{X-X(P+R)}.
                                                               \tag{MB.20}
\]
The chord-over-vertical divisor is
\((P)+(R)-(P+R)-(O)=D_P-t_{-R}^*D_P\); hence MB.20
is the coefficient of the actual line map covering \(p\mapsto p-R\).
All powers of this lift below are chronological compositions,
with each coefficient evaluated at its actual source point.
The chord has deck weight \(\omega\) and \(\tau(R)\) has
weight \(\omega^2\), so this exact product commutes with D.
Its central coefficient is one; its horizontal divisor and the
two correction divisors above give the extending map and inverse.
The six Miller factors have original weight \(z^{-6}\), while
the selected factor is \(z^6h_{\rm sel}\). Consequently
\[
 B'_{\rm sel}=h_{\rm sel}B'_{2,3},\quad
 h_{\rm sel}=1-t_cz^3,
 \quad B'_{2,3}|_{z=0}=4.                                \tag{MB.21}
\]
The last equality is the literal central norm of
\((Y-1)/X\), whose three values multiply to \(-2\); its square
is four. Compared with the retained K96 reference height,
the full unit is \(h_{\rm sel}/h_{\rm ref}\), with its unique
logarithm zero at z zero and its prescribed cube root.
Set \(\widetilde F=(B'_{\rm sel}/F^3)^{1/3}F\), retaining that
root and all its Cartier factors. For the given scalar root and
character,
\[
 R_\lambda^3=\lambda,\qquad
 A=R_\lambda\omega^{d_0}\widetilde F D,
 \qquad A^3=B=\lambda B'_{\rm sel},\quad[A,B]=1.
                                                               \tag{MB.22}
\]

The complete sector map is
\[
 \Phi_\alpha=\operatorname{Exp}
   (s_\alpha f_\alpha+s_\alpha c_\lambda\delta+h_\alpha)I_{z_\alpha},
 \quad s_\alpha=\log_\alpha q_{\infty,o}/(2\pi i),
 \quad z_\alpha=e^{2\pi i s_\alpha/3},
\]
\[
 f_\beta=D_*^kf_\alpha+\Pi_{\alpha\beta},\quad
 h_\beta-D_*^kh_\alpha=-s_\alpha\Pi_{\alpha\beta}
             +j_{\alpha\beta}\log_\beta B+\Lambda_{\alpha\beta}.
                                                               \tag{MB.23}
\]
Here \(c_\lambda=\log R_\lambda/(2\pi i)+d_0/3\).
Perform the full reference-zero Cauchy construction of EX.18
first on the \(\zeta\)-disc: extend the entire reference cochain,
form its residual E, put \(k_\alpha=-\sum\chi_\beta E_{\alpha\beta}\),
take the common \(\bar\partial k_\alpha\), and subtract its
fixed-contour Cauchy transform. The result retains every period,
integer j and reference value. It gives exactly
\(\Phi_\beta=A^kB^{j_{\alpha\beta}}\Phi_\alpha\), with inverse
\(I_z^{-1}\) after the inverse Lie displacement.

On the actual old-cap overlap
\(q_{\infty,o}=d^3/\sigma^4\),
\(|\sigma|>|d|^{3/4}\delta^{-1/4}\), a quarter-turn sends
\(s_o=3\log d/(2\pi i)-4\log\sigma/(2\pi i)\) to \(s_o+1\).
Its full root word is \(AB^{j_\gamma}\); four such arrows give
\[
 A^4B^J=R_\lambda^4\omega^{4d_0}\widetilde F^4D^4B^J,
 \qquad J=\sum_{i=0}^3j_{\gamma,i}.
                                                               \tag{MB.24}
\]
The endpoint-to-initial arrow is its full inverse. No scalar or
integer has been removed. The continued native-root map is
\(z_o=\epsilon^{-4/3}dz_e\),
\(X_o=\epsilon^{-2/3}X_e\), \(Y_o=\epsilon^{-1}Y_e\),
with endpoint \(D_o^{-4}\). On the complementary root cover
the quotient of \(\widetilde D^4\) fixes the genuine point
coefficient and gives exactly the ordinary residual quarter
action MB.9. The cap remains on its large-sigma domain; no
division point is introduced at sigma zero.

The exact weighted norm
\(\|v\|'^2=\sum_{j=0}^2\rho_0^{-2j}\|A^jv\|^2\), with
\(\|Bv\|\le\rho_0^3\|v\|\), makes A strictly contracting.
It gives the proper free cap quotient and free physical circle.
Push the chosen ordinary horizontal fields through the full
derivative of MB.23, extend by a relative partition of unity,
average over the physical circle and integrate radially over
the \(\zeta\)-disc. This is a product with exactly the prescribed
boundary derivative and line map. The quotient cap body has
dimension five; its product connections give zero for both
\(x^3\) and \(p_1x\) on its parameter-circle product. Pulling
back by \(\zeta=\epsilon^2\) retains this exact cap product and
the entire word MB.24.

## MB.7. Compact attachment and the physical transfer

Glue the actual finite domains MB.4, MB.9--13, the native I2
source and the cap MB.19--24. Their face equations retain the
full point-module ratios, original source functions and inverse
character maps. The selected real norm matrix is
\[
 \begin{pmatrix}L_q&-3L_P\\2L_P&4L_\sigma+L_q+L_C\end{pmatrix},
 \quad\det=L_q(4L_\sigma+L_q+L_C)+6L_P^2>0.
\]
The two period coefficients in \([0,1]\) bound all four
source/line node coordinates, as in the explicit IA parallelogram
calculation. The projective ratio graphs are proper over those
bounded boxes. The ordinary chain uses four consecutive labels
with MB.9, including its full projective p charts; the original
cap uses its compact contraction shell. These regions cover the
compact source-base graph. Their period face maps are exactly
MB.11--13 and MB.24, and a compact chart meets only finitely many
translates by their source/line index shifts. Thus every artificial
face is paired and the glued cut is compact and Hausdorff, with
only the actual outer epsilon family as boundary.

After the actual selected Hopf-cap insertion MB.17--18, the
fixed-inner normal ledger is evaluated from MB.11--15. Its U
pairs are the following separately computed characteristic pairs.

| Components | Multiplicity | U pair |
|---|---:|---:|
| Four strict-source surfaces | one set | (42,108) |
| Four remaining two-torsion points | one set | (-2,-14) |
| Interior points and curves | two O/T copies | (-18,-126) per copy |
| Four exceptional-source surfaces | two O/T copies | (-20,-20) per copy |
| Ten refinement surfaces | two O/T copies | (18,126) per copy |
| Twelve p-chart curves | two O/T copies | (0,-18) per copy |
| Ten finite-base interface curves | two O/T copies | (0,0) per copy |
| Moving capped surface | one | (-4,-10) |

All normal rows and multiplicities here are those proved for
the actual M2 period in MB.6--15. Their sum is \((-4,8)\).
The physical nonzero-vector line is \(M=U^*\) by the actual K68
Hopf map, so both odd characteristic terms change sign on each
fixed link. Finite-chart averaging and Stokes retain the inverse
stabilizer orders and the transported tangent splitting. For
\(\operatorname{or}W=d\phi_\delta\wedge\operatorname{or}Y
\wedge dr\wedge d\theta\), the outer boundary is
\(-\operatorname{or}Y\wedge d\theta\); the Jin interval reverses
the parameter. These are the same two explicit orientation arrows
as OT.17--20, giving physical Jin pair \((-4,8)\).

The orbit hypotheses are supplied by the actual M2 reference
sphere of F41/K96/K98, with cap relation matrix
\(\left(\begin{smallmatrix}3&1\\1&0\end{smallmatrix}\right)\)
and inverse \(\left(\begin{smallmatrix}0&1\\1&-3\end{smallmatrix}\right)\).
The unchanged physical Hopf boundary has Euler restriction
\((0,-1)\). Gysin and the primitive boundary H3 map give
\(H^2(P)=\mathbb Ze\), \(H^3(P)=H^4(P)=0\). The original fixed
filling has difference matrix
\(\left(\begin{smallmatrix}0&-1\\-1&0\end{smallmatrix}\right)\)
and gives the orbit S5 with its unknotted fixed sphere. The
separate conifold cap has matrix
\(\left(\begin{smallmatrix}0&0\\-1&-1\end{smallmatrix}\right)\),
primitive kernel \((1,-1)\) and primitive cokernel. Its actual
unknotted Hopf replacement is \(S^2\times S^3\), with physical
Euler line \((e,-b_{\rm mer})\).

Use the circle-averaged connection that is product on this same
selected tube and the actual cap product MB.23. It selects the
actual return and its physical lift, preserves H2 by the Euler
class and H3 by orientation, and uses the identical Hopf extension
on the selected tube. K68's piece/inverse map is
\(\lambda_M(f)=-\Sigma(f^{-1})=\Sigma(f)\). Hence the actual
initial integer is \((4(-4)-8)/24=-1\). The held-Cox normal
product MB.18 is also the one giving
\(k_M=\mu+\nu\), \(\ell_M=4\mu\), so its native free pair is
\((2,-6)\) before central reduction.

The full original point-frame period winding matrix is
\(\left(\begin{smallmatrix}-4&0\\0&0\end{smallmatrix}\right)\):
\(\kappa_o=\epsilon^{-4}d^3\kappa_e\), while \(P^2,P^{-3}\)
and the complete point Hom divided by \(q_o\) are extending
units. All coefficient shears, native Cox maps and ordinary
products of IF.1--7 apply to these literal functions, with their
inverse character map the identity on MB.23. The full reference
was constructed on zeta first; theta inversion and the target
source period give exactly \((Z,V,q_o)\mapsto(Q/Z,V,q_o)\).
Thus the two vertical endpoints retain the same actual cap and
normal products. The complete K102 integer algorithm follows
from the same initial native pair and full directed prism maps,
with each M2 unit retained. This final all-fan application is to
the constructed M2 family, not to the cubic-cover map CB.5.
