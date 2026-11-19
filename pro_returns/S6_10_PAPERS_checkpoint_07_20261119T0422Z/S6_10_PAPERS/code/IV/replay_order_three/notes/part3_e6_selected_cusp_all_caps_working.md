# E6 selected cusp with both complete cap progressions

The complete source/root/normal proof has passed the root and two
independent peer audits. The preceding audit drafts and the
relative-level expansion are preserved in the attempt records.

## Statement

On the source
\[
 y^2=x^3+r x^2+t x+t^2,\qquad G=(0,t),\qquad
 r=\frac{3-2w^2}{(w^2-3)^2},
\]
take the selected zero at
\(t_c=(w^2-1)/(w^2-3)^3\), the actual point line
\(M_a=\mathcal O(aG-O)\), and the whole source/line suspension
over translation by \(-bG\). Retain the exact finite cap and
complete ordinary-to-cap reference map in either row
\[
 (a,b;m)=(6,1;3l+2),\quad l\ge0,\qquad
 (a,b;m)=(2,3;3l),\quad l\ge1 .
 \tag{EG.1}
\]
In both rows \(ab=6\), the primitive norm is \(n=\pm1\), and the scalar
\(\lambda=R_\lambda^m\ne0\), including its chosen root and
phase, is fixed and sufficiently small for the actual compact
contraction shells. Every finite character and integral annular
reference column is retained. The positive ordered \(w\)-loop
defines the completed sphere family and its actual return.

On the initial vertical fan the physical characteristic pair is
\((k_M,\ell_M)=(-6,0)\), its native free pair is \((0,-6)\),
and its clutched sphere has class \(-1\) in \(\Theta_7\cong
\mathbb Z/28\). On every vertical fan \(T_j\), \(j\in\mathbb Z\),
the exact values are
\[
 \begin{split}
 (k_M,\ell_M)&=(-6-18j(j-1),0),\\
 (m_{\rm native},n_{\rm native})&=(0,-6-18j(j-1)),\\
 [\Sigma_j]&=-1-3j(j-1)\pmod {28}.
 \end{split}
\]
For every selected lattice-basis fan, the full actual return is
given by the proved K71 fan algorithm, with these vertical seeds
and the complete coefficient and Cox maps (EG.45)--(EG.46).
This is a comparison of the actual completed families, including
their physical circle, both normal caps, source/Cartier maps and
finite-root closing. The ordered loop has local degree four over
the original \(r=1/3\) puncture; the statement assigns no shorter
source endpoint.

## EG.1. The full source and the two actual point-line maps

Retain
\[
 \begin{gathered}
 v=w^2-1,\quad D=w^2-3,\quad A=3-2w^2,\quad
 \\
 Y^2=X^3+AX^2+DTX+T^2,\qquad G=(0,T),\quad q=T-v .
 \end{gathered}
 \tag{EG.2}
\]
The source map to the original family is
\((x,y,t)=(D^{-2}X,D^{-3}Y,D^{-3}T)\), with
\(r=A/D^2\). Set \(s_0=v(w^2+3)/4\) and
\[
 U=Y-T-DX/2,\qquad
 f_2=\frac{U}{X-s_0},\qquad {\cal T}(p)=p-G .
 \tag{EG.3}
\]
The two inverse chord maps are
\[
 k_\pm=(Y\mp T)/X,\quad
 X_\pm=k_\pm^2-A-X,\quad Y_\pm=\mp T-k_\pm X_\pm .
 \tag{EG.4}
\]
Their denominators are units at the selected cusp
\((w,X,Y,T)=(0,-1,0,-1)\). Thus all four translations
\({\cal T}^j\), \(0\le j\le3\), used below extend on a common
source neighbourhood and keep the full \(q,w\).

Write \(M_a=\mathcal O(aG-O)\). For \(a=2\), the actual
point-to-tensor map is \(r_2=f_2^{-1}:M_2\to M_1^{\otimes2}\).
For \(a=6\), it is \(r_6=f_6^{-1}:M_6\to M_1^{\otimes6}\), where
\[
 f_3=\frac{s_0XU}{s_0(Y+T+DX/2)-(Ds_0+2T)X},
 \qquad f_6=f_3^2 f_{2,3G}.
 \tag{EG.5}
\]
Here \(f_{2,3G}\) is the whole tangent-over-vertical function.
Its section and tangent coordinates are explicitly
\[
 \begin{split}
 x_3&=4T^2/s_0^2+2DT/s_0,\\
 y_3&=T(8T^2+6Ds_0T+D^2s_0^2-s_0^3)/s_0^3,\\
 \ell_3&=(3x_3^2+2Ax_3+DT)/(2y_3),\qquad
 x_6=\ell_3^2-A-2x_3,\\
 f_{2,3G}&=\frac{Y-y_3-\ell_3(X-x_3)}{X-x_6}.
 \end{split}
 \tag{EG.6}
\]
Every source and target factor is retained in the two suspension
coefficients
\[
 \begin{split}
 B_{6,1}(p)&=f_2(p)^6\,\frac{f_6({\cal T}p)}{f_6(p)},\\
 B_{2,3}(p)&=f_2(p)f_2({\cal T}^3p)
                     f_2({\cal T}p)^2f_2({\cal T}^2p)^2,\\
 B_{\rm sel}^{(a,b)}(p)&=\frac q{T^3}B_{a,b}(p).
 \end{split}
 \tag{EG.7}
\]
Indeed the \(M_1^{\otimes a}\) lift over \({\cal T}^b\)
has coefficient \(\prod_{j=0}^{b-1}f_2({\cal T}^jp)^a\).
Multiplying it by \(r_a(p)/r_a({\cal T}^bp)\) gives precisely
(EG.7), including the uncancelled \(f_2({\cal T}^3p)\) in the
second row. Thus the source translations are exactly \(-G\)
and \(-3G\), respectively.

On the selected fibre put
\[
 X=S^2-1,\quad Y=S(S^2-w^2),\quad
 Z=\frac{S-w}{S+w},\quad P=\frac{1+w}{1-w}.
 \tag{EG.8}
\]
The section \(G\) is \(S=-1\), and \(O\) is \(S=\infty\).
For \(a=2,6\) the actual point \(aG\), divisor equation and
normalizing unit are
\[
 S_a=w\frac{1+P^a}{1-P^a},\qquad c_a=w-S_a,\qquad
 S-S_a=c_a\,\frac{1-Z/P^a}{1-Z}.
 \tag{EG.9}
\]
They extend holomorphically over \(w=0\), with
\(S_a(0)=-1/a\), \(c_a(0)=1/a\). In particular
\[
 \begin{aligned}
 S_2&=-(1+w^2)/2,&c_2&=(1+w)^2/2,\\
 c_6&=(1+w)^6/(6+20w^2+6w^4),&
 f_a|_{q=0}&=(S+1)^a/(S-S_a).
 \end{aligned}
 \tag{EG.10}
\]
The identities use the actual Miller functions (EG.3)--(EG.6):
their divisors and their coefficient \(S^{a-1}\) at infinity
agree. For \(a=2\) it also follows by direct substitution in
(EG.3). This retains the whole point-divisor-to-theta coefficient,
not just the point \(P^a\).

Let \(f_P(Z)=\Theta_Q(Z/P)/\Theta_Q(Z)\) be the actual rigidified
theta section of \(M_1\), with \(f_P(QZ)=P f_P(Z)\).
Here and below \(P=P_G(q,w)\) is the full marked Tate lift;
(EG.8)--(EG.10) are its restriction to \(q=0\).
The two actual point-line theta coefficients are
\[
 V_a=f_P(Z)^a r_a(p)\,v_a .
 \tag{EG.11}
\]
On the selected normalization their comparison with the strict
point theta factor is the full even unit
\[
 f_P^a/f_a=\frac{c_a}{(1+w)^a}
                   \frac{1-Z/P^a}{1-Z},\qquad
 \frac{c_2}{(1+w)^2}=\frac12,\quad
 \frac{c_6}{(1+w)^6}=\frac1{6+20w^2+6w^4}.
 \tag{EG.12}
\]

The exact constant of the \(M_1\) translation is
\[
 \eta_1=f_2(p)\frac{f_P(P^{-1}Z)}{f_P(Z)} .
 \tag{EG.13}
\]
Its divisor is zero on the compact smooth elliptic fibre, so it
is independent of \(p\). Substitution of (EG.7) into (EG.11)
then telescopes literally, giving in both rows
\[
 H:(Z,V_a)\mapsto(\kappa q Z,P^aV_a),\qquad
 B:(Z,V_a)\mapsto(P^{-b}Z,q\eta V_a),\qquad
 \eta=\lambda\,\eta_1^6/T^3 .
 \tag{EG.14}
\]
This is an equality of the full coefficients: \(ab=6\) is used
only after the actual tensor/point maps in (EG.7) and (EG.11).
Both selected node branches have \(f_2=2\). They are fixed by
every \({\cal T}^j\), and therefore
\[
 \eta_1|_{q=0}=2,\qquad
 B_{a,b}|_{\rm node}=64,\qquad
 B_{\rm sel}^{(a,b)}/q=64/v^3 .
 \tag{EG.15}
\]
The coefficient at the central cusp is the retained \(-64\).

The weighted node coordinates
\(\xi=X-v=w^2\widetilde X,\ Y=w^3\widetilde Y,\
q=w^6Q_c\) give the full equation
\[
 \widetilde Y^2=\widetilde X^2(\widetilde X+1)
       +Q_c(v^2+Dw^2\widetilde X)+w^6Q_c^2 .
 \tag{EG.16}
\]
The inverse \(j\)-series gives
\(\kappa=w^{-6}\widehat\kappa(Q_c,w)\),
\(\widehat\kappa(0,w)=-v^2/64\).
The actual \(G\) has formal parameter
\(wv/(v+w^6Q_c)\). Thus \(P\), \(P^{-b}\), \(P^a\), and
\(\eta/\lambda\) have extending nonzero logarithms on this
weighted bidisc, with their specified constant values. The only
parameter winding in (EG.14) is the full \(-6\) in \(\kappa\).

## EG.2. The complete exterior and both finite-root families

On the ordinary exterior the actual source maps (EG.4) and
their compositions extend over the unselected \(I_2\), using
the two A1 charts of
\[
 (y-t-x/2)(y+t+x/2)=x^2(x-s),\qquad s=1/4-r .
 \tag{EG.17}
\]
Here \(s\) stays near \(-1/12\) and is a unit. The line
divisor is \(3F_0-2F_\infty\) in both rows: in the second
row this follows from the six retained \(f_2\) factors of
(EG.7), with component orders \(0,1\) and the actual odd
translation exchanging the two \(I_2\) components. Thus
\(q/T^3\) leaves exactly the selected whole zero. The maps
and their inverses have zero order along the source-parameter
divisor, as evaluated on an ordinary section avoiding the
horizontal divisors. Normality extends the typed Hom map
through the remaining codimension-two source locus.

We now use the complete K96 root maps, with the following
literal substitutions and units. For the reduced branch put
\(m=3l+2,\ k=2l+1\). In the original source coordinate the root is
\[
 q_\infty=z^m,\quad x_0=z^{2k}X',\quad y_0=z^{3k}Y',
 \qquad
 Y'^2=X'^3+r z^{2l+2}X'^2+z^{l+2}X'+z^2 .
 \tag{EG.18}
\]
With \(c=\sqrt{1+z^lX'+r z^{2l}X'^2}\),
\(U'=Y'-zc,\ V'=Y'+zc\), its equation is \(U'V'=X'^3\).
The inverse of \(2zc=V'-U'\) and all three A2 charts retain
the actual \(z\). In the middle chart \(X'=ab,\ U'=a^2b,\
V'=ab^2\), use \(b_0=z^l,c_0=r z^{2l}\) and the full functions
\[
 \begin{split}
 K&=1+\frac{b(b-a)(b_0+c_0ab)}{2c(c+1)},\\
 F&=1-\frac{ab(b_0+c_0ab)(K+1)}{2c(c+1)}
             -\frac{c_0ab^2(a-b)}{4c^2},\\
 X''&=a(a-b)F,\quad c'=\sqrt{1+b_0X''+c_0X''^2},\\
 H_c&=K+\frac{b(a-b)(b_0+c_0X'')}{2c(1+c')}.
 \end{split}
 \tag{EG.19}
\]
The actual \(+G'\) arrow is
\((a,b)\mapsto((b-a)F/H_c,-aH_c)\); its inverse is the
actual negative chord. It preserves the same \(z\) and
commutes with
\[
 {\mathfrak D}(z,X',Y')
   =(\zeta_mz,\zeta_m^{-2k}X',\zeta_m^{-3k}Y').
 \tag{EG.20}
\]
The exact division is
\(R=2G'-[m]^{-1}((2m-1)G')\), with \(mR=G'\).
The small inverse is taken only on the identity formal
group; \(2m-1=3k\). The nonidentity central component of
\(R\) is two and is retained.

The root line graph is the actual ideal \((\tau',z^k)\),
where \(\tau'=-X'/Y'=z^k\tau_0\). The two section equations
are \(\tau'\) and \(\tau'-z^kL(s,z^m)\), \(L(s,0)=-s\ne0\).
Its normalized graph has the ray \((k,1)\), and its regular
subdivision retains every ray \((j,1)\), \(1\le j\le k\).
Both exceptional orders are \(j\); at \(j=k\) the graph
coordinate retains the distinct directions \(0,L\). The
literal coefficient maps on its two charts are
\[
 \frac{\tau'}{\tau'-z^kL}=\frac{u}{u-L},\qquad
 \frac1{1-v_{\rm gr}L},\qquad uv_{\rm gr}=1 .
 \tag{EG.21}
\]
The other quotient centres carry neither marked divisor.
The deck-commuting source translation and its inverse lift
to the quotient resolution and then to the normalized
product graph, with these same coefficient maps. This
gives the full equality \(\beta^*N_6=\pi^*M_6\).
The root selected coefficient is exactly
\[
 B'_0=h_\infty z^{-2}B'_6,\qquad
 h_\infty=1-t_c(r)z^m,\qquad (B'_6/z^2)|_{\rm central}=4 .
 \tag{EG.22}
\]

For the good branch \(m=3l\), the actual root is
\[
 q_\infty=z^{3l},\quad x_0=z^{4l}X',\quad y_0=z^{6l}Y',
 \qquad
 Y'^2=X'^3+r z^{2l}X'^2+z^lX'+1 .
 \tag{EG.23}
\]
Its source point is \(G'=(0,1)\), and the small formal
division is \(R=[m]^{-1}(3G')\), with \(mR=3G'\).
Put \(u=z^l\). The quotient first retains its \(\mu_l\)
kernel and then the \(\mu_3\) action of weights \((2,1)\)
on each marked chart \((w_P,u)\). At \(2G'\) take
\(w_P=X'-su^2\); at \(O\), take \(w_O=-X'/Y'\).
The resolution rays are \((2/3,1/3),(1/3,2/3)\).
The strict-section support function
\(\max(v_w-2v_u,0)\) gives the full correction
\[
 \beta^*N_2=\pi^*M_2+E_P-E_O,\qquad
 \operatorname{coeff}_{(v_w,v_z)}E_*=\min(v_w,2l v_z).
 \tag{EG.24}
\]
Every arrow is the quotient of its actual monomial
Cartier generators. The translations have the exact
form \(w\mapsto w\varepsilon+u^2a\) and preserve the
ideals \((w,u^j),(u,w^j)\), \(j=1,2\), together with
their inverses. They therefore lift to this full graph
and carry both correction divisors. The complete root
Hom coefficient is
\[
 B'_0=h_\infty B'_{2,3},\qquad
 B'_{2,3}|_{\rm central}=4 .
 \tag{EG.25}
\]
The last constant is the square of the exact norm \(-2\)
of \(f=(Y'-1)/X'\) under the three central translations,
not a discarded base factor.

For both roots use the literal chord-over-vertical function
\(g_{P_*,R}=\ell_{P_*,R}/(x-x(P_*+R))\).
Its divisor is \(D_{P_*}-t_{-R}^*D_{P_*}\).
The actual starting line lift is
\[
 F_{\rm line}=
 \begin{cases}
 \tau(6G')\,g_{6G',R},& a=6,\\
 \tau(R)\,g_{2G',R},& a=2 .
 \end{cases}
 \tag{EG.26}
\]
The formal factor and chord have opposite deck weights.
Their product commutes with \(\mathfrak D\) and has
central coefficient one. In the reduced case the zero
Hom multidegrees and the primitive whole-fibre kernel
carry this limit to every component. The exact ratio
\(\beta=B'_0/F_{\rm line}^m\) is an invariant base unit,
central four. Its analytic \(m\)-th root is fixed by the
complete reference map. Put
\[
 \widetilde F=\beta^{1/m}F_{\rm line},\quad
 A_0=\zeta_m^d\widetilde F^{\,n}\mathfrak D,\quad
 B=\lambda B'_0,\quad A=R_\lambda^nA_0 .
 \tag{EG.27}
\]
Then \(\widetilde F^m=B'_0\), \(A_0^m=(B'_0)^n\),
\(A^m=B^n\), and all source, correction, character and
line arrows commute literally as specified.

## EG.3. The root rescaling and the whole annular reference

All preceding formulas can be written directly in the
current \(T\) coordinate. Choose the analytic unit
\(L_D=D^{1/m}\) on the source disc. The exact new-to-old
root maps are
\[
 \begin{array}{c|ccc}
 &z_{\rm old}&X'_{\rm old}&Y'_{\rm old}\\ \hline
 a=6&L_D^3 z_{\rm new}&L_D^2X'_{\rm new}&L_D^3Y'_{\rm new}\\
 a=2&L_D^3 z_{\rm new}&X'_{\rm new}&Y'_{\rm new}.
 \end{array}
 \tag{EG.28}
\]
Their inverse divides by the same nonzero units. The
new reduced equation has coefficients
\(A z^{2l+2}X'^2+D z^{l+2}X'+z^2\);
the new good equation has
\(A z^{2l}X'^2+D z^lX'+1\).
Substitution uses \(L_D^m=D\) and gives these full
equations, not just their central fibres. In both rows
\(q_{\infty,\rm old}=D^3 q_{\infty,\rm new}\) and
\[
 h_{\infty,\rm old}=1-vz_{\rm new}^m .
 \tag{EG.29}
\]

On the reduced graph,
\(\tau'_{\rm old}=L_D^{-1}\tau'_{\rm new}\) and
\(\tau_{0,\rm old}=D^{-2}\tau_{0,\rm new}\);
its \(u=\tau'/z^k\) coordinate changes by \(D^{-2}\).
Both numerator and denominator of (EG.21) are carried.
The root tangent factor has weight \(L_D\), so
\(B'_{6,\rm old}=L_D^6 B'_{6,\rm new}\).
The \(z^{-2}\) factor contributes \(L_D^{-6}\);
the complete root \(B'_0\) is unchanged.
In (EG.26) the formal coordinate has weight
\(L_D^{-1}\) and the full chord has weight \(L_D\);
their product is unchanged as well.

In the good graph \(u_{\rm old}=D u_{\rm new}\),
while \(w_P,w_O\) are unchanged. On every correction
cone the actual monomial \(w^r u^s\) consequently carries
the full factor \(D^s\); this is the line arrow in
(EG.24). The root source coordinates and chord functions
are unchanged by (EG.28), including their \(D z^l\)
tangent coefficient. Thus the complete \(B'_0\) and
\(F_{\rm line}\) are again unchanged. In both rows the
reference-fixed norm root and the actual finite
character in (EG.27) are carried by that same map.

The ordinary full Miller product has weight \(D^{-6}\)
in both rows of (EG.7). The old factor
\((t-t_c)/t^3\) has weight \(D^6\), so the entire
ordinary suspension scalar is unchanged. All of
(EG.28)--(EG.29), including their fractional unit roots,
are holomorphic on the disc \(\zeta=w^2\), with their
values fixed once at the full reference parameter.

The canonical point frame and the tensor-reference frame have the
following directed comparison. With the same canonical meromorphic
section coefficient \(v_M\), they are
\[
 V_{\rm pt}=f_{P^a}v_M,\qquad
 V_{\rm tensor}=f_P^a f_a^{-1}v_M.
 \tag{EG.29a}
\]
The source map carries the canonical section literally and preserves
the full \(Q,P,Z\), so \(V_{{\rm pt},{\rm old}}=V_{{\rm pt},{\rm new}}\).
The whole Miller function has weight
\(f_{a,{\rm old}}=D^{1-a}f_{a,{\rm new}}\). Consequently
\[
 V_{{\rm tensor},{\rm old}}=D^{a-1}V_{{\rm tensor},{\rm new}},\qquad
 q_{\rm old}^{h}Z_{\rm old}^{u}V_{{\rm tensor},{\rm old}}^{j}
 =D^{-3h+(a-1)j}q_{\rm new}^{h}Z_{\rm new}^{u}
                     V_{{\rm tensor},{\rm new}}^{j}.
 \tag{EG.29b}
\]
These exact units enter the annular map below. On this selected-cusp
disc \(D\) is nonzero and its fixed logarithm is holomorphic in
\(\zeta=w^2\); thus its full parameter phase, as well as its norm,
is retained. The root point-line coefficient in the good row is
unchanged, while its graph monomials retain the \(D^s\) just displayed
above. This specifies both sides of each Cartier arrow.

Here is the whole annular square. First work over the
\(\zeta\)-disc. Retain the actual source, root and Cartier map
\(I_z\) from (EG.18)--(EG.29). On the fixed angular sectors put
\[
 s_\alpha=\frac{\log_\alpha q_\infty}{2\pi i},\quad
 z_\alpha=e^{2\pi i s_\alpha/m},\quad
 c_\lambda=\frac{n\log R_\lambda}{2\pi i}+\frac dm,\quad
 f_\alpha=\operatorname{Log}_\alpha\widetilde F .
 \tag{EG.30}
\]
Use the actual extension-group Lie coordinates: the
source component is the Abel integral of \(-R\), and
the line component contains (EG.21) or (EG.24), the
full \(h_\infty\), and the norm root. On an overlap
\(s_\beta=s_\alpha+k\), write
\(f_\beta=\mathfrak D_*^k f_\alpha+\Pi_{\alpha\beta}\).
Retain the entire reference period columns, suspension
integers \(j_{\alpha\beta}\), and integral vectors
\(\Lambda_{\alpha\beta}\). Then
\[
 \begin{split}
 \Phi_\alpha&=\operatorname{Exp}
     (n s_\alpha f_\alpha+s_\alpha c_\lambda\delta
                              +h_\alpha)I_{z_\alpha},\\
 h_\beta-\mathfrak D_*^k h_\alpha
   &=-n s_\alpha\Pi_{\alpha\beta}
              +j_{\alpha\beta}b_\beta+\Lambda_{\alpha\beta},
 \qquad b_\beta=\operatorname{Log}_\beta B .
 \end{split}
 \tag{EG.31}
\]
The period functions are transported over the disc,
with their original integer coefficients. In particular
the nonidentity reduced division branch is retained in
these periods; no small logarithm replaces it.

Use the invariant differential and rigidified-line
frame to express the vectors on the ordinary annulus.
Extend the whole reference \(h_\alpha\) to \(h_\alpha^0\).
For the residual additive cocycle \(E_{\alpha\beta}\),
zero at the reference, put
\[
 k_\alpha=-\sum_\beta\chi_\beta E_{\alpha\beta},\quad
 \omega=\bar\partial k_\alpha,\quad
 v_{\rm CG}(q,\zeta)=\frac1\pi\int
                   \frac{\omega(t,\zeta)}{q-t}\,dA(t),\quad
 h_\alpha=h_\alpha^0+k_\alpha-v_{\rm CG}.
 \tag{EG.32}
\]
The fixed larger-annulus cutoff and contours are those
of the actual EX construction. This solves (EG.31)
holomorphically in \(\zeta\), with the entire prescribed
reference value. Finite averaging applies only to the
vector cochains. Subtracting the target-sheet
\(knf_\beta+kc_\lambda\delta\) leaves exactly
\(j_{\alpha\beta}b_\beta+\Lambda_{\alpha\beta}\), hence
\[
 \Phi_\beta=A^k B^{j_{\alpha\beta}}\Phi_\alpha,\qquad
 \Phi_\alpha B=B\Phi_\alpha .
 \tag{EG.33}
\]
The inverse is \(I_z^{-1}\) followed by the negative
Lie argument. Pull this whole construction back by
\(\zeta=w^2\). It is literally even in \(w\), includes
both signed norms and all finite characters, and has
identity source, line, root and annular closing.

## EG.4. Actual orbit topology, fixed trace and both normal caps

For each fixed row and root order, choose the fixed
scalar below the common bounds on the finite exterior
and root charts. The actual cap generator \(H=A^n\)
satisfies \(H^m=B\), \(H^n=A\), and has scalar factor
\(R_\lambda\). Its strictly contracting norm gives
the compact shell and excludes an additional physical
circle stabilizer. Together with the protected
selected-fan regions these are the proper outside
products over the source disc.

The reference sphere is the corresponding F41 datum.
Its application to the present source uses the
contractible marked arc from the present
\(\rho=w^2/(w^2-3)\) to \(\rho=-1\), avoiding all
other collisions in its interior. The full K96
unselected-III disc attachment at the endpoint is
the actual E6-B model. The source/line/root maps
and their inverses above give the completed
family on a tube about that arc, with the same
reference and character. Proper interval
transport therefore supplies the F41 sphere here.

On the standard selected fan the only fixed set
is the vertical \(\mathbf P^1\), whose chart is
\[
 c_i'=Zc_i,\quad Z'=Z^{-1},\quad
 q=Zc_0c_1=Z'c_0'c_1',\qquad
 \operatorname{wt}_\delta(c_0,c_1)=(-1,+1).
 \tag{EG.34}
\]
Every other edge has determinant \(\pm1\) with
the physical cocharacter. On the free complement
\(E\) of its normal tube, the F41 sphere gives
the integral homology of \(S^3\) and \(\pi_1E=0\).
Conjugating the negative line gives
\(\mathcal O(1)\oplus\mathcal O(-1)\); its SU(2)
clutch \(\operatorname{diag}(Z,Z^{-1})\) bounds
the explicit disc \((r e^{i\theta},\sqrt{1-r^2})\).
Thus the boundary is the product Hopf map
\(S^2\times S^3\to S^2\times S^2\).
The primitive normal \(H_3(\partial E)\to H_3(E)\)
map and natural Gysin integration give
\(H^2(E/S^1)=\mathbb Z e\), \(H^3=H^4=0\).
The orbit union with \(S^2\times D^3\) has
degree-two MV matrix \(\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\).
It is simply connected and has the homology
of \(S^5\); the already verified F7--8
classification identifies its fixed pair with
\((S^5,\text{unknotted }S^2)\). The boundary
Hopf gauges match by their global logarithm
on \(S^2\times S^2\).

The full local height is unchanged from K95:
with \(\xi=X-v\),
\[
 Y^2-\xi^2(\xi+w^2)=q(q+v^2+D\xi),\qquad
 q=\frac{2\{Y^2-\xi^2(\xi+w^2)\}}
 {v^2+D\xi+\sqrt{(v^2+D\xi)^2+
                    4\{Y^2-\xi^2(\xi+w^2)\}}}.
 \tag{EG.35}
\]
The square root has value one at the cusp.
Its ordered normalization is
\(f(S,w)=(S^2-w^2,S(S^2-w^2),w)\).
Put \(x=S-w,y=S+w\) and
\[
 n_f=(3S^2-w^2)d\xi-2S\,dY+2w(S^2-w^2)dw .
 \]
The actual native normal arrows are
\[
 dq=-xy\,n_f/(v^2+Dxy),\quad
 d(c_0c_1)=-y^2n_f/(v^2+Dxy),\quad
 d(c'_0c'_1)=-x^2n_f/(v^2+Dxy).
 \tag{EG.36}
\]
The common denominator is an extending unit.
The source translation \(-bG\) and its line
lift are untwisted by their actual extension-group
logarithms on this source neighbourhood. Their
normalization action is
\[
 S\longmapsto
 \frac{(1+g_t)S+(1-g_t)w}{((1-g_t)/w)S+(1+g_t)},
 \qquad g_t=\exp(t\log P^{-b}).
 \tag{EG.37}
\]
Writing \(g_t=1+wh_t\), its difference from
\(S\) is \(h_t(S^2-w^2)/(2+h_t(w-S))\).
Its full derivative is uniformly \(I+O(|S|+|w|)\).
Together with the exact increasing F9 orbit
coordinate this gives the same actual ordered
embedded trace: \(S=-w\) is lower, \(S=w\)
upper. The exterior/root extension (EG.33)
gives its unchanged outer product. Interpolation
on the common real gamma lift gives the literal
height \(\operatorname{Re}(S\overline w)/
\sqrt{|S|^2+|w|^2}\), preserving the branch order.

The point-line arrow on this trace is also
explicit. Let \(\sigma_a\) be its canonical
rational section, with divisor \(aG-O\).
The map \(\sigma_a\mapsto S-S_a\) is a
nonzero holomorphic trivialization on
\(\mathbf P^1\times D_w\): at \(aG\) the
two zeros cancel, and at \(O\) their simple
poles cancel. Equivalently the actual
comparison to the \(a=6\) trace line sends
\[
 \sigma_a\longmapsto
       \frac{S-S_a}{S-S_6}\,\sigma_6 .
 \tag{EG.38}
\]
It is a Cartier line isomorphism, including
both marked points, and is holomorphic on
the \(\zeta=w^2\) disc.
For a local coefficient \(g\) of this map,
the normal variables are carried by
\((U,V)\mapsto(g^{-1}U,gV)\). The actual
positive-spinor coefficients consequently
change by \((\overline g^{-1},g)\).
Their phases agree and all full positive
norms are retained. The scalar logarithms
extend on the inner source ball and,
after a collar cutoff, on the outer
\(D^3\times S^1\) cap. This gives an
actual line/normal comparison, not an
identification from degree zero alone.

The remaining coefficient map is precisely
the K68 anti-linear map
\[
 (a_+,a_-)\longmapsto
 \frac1{\sqrt{|x|^2+|y|^2}}
 \begin{pmatrix}y&-\overline x\\x&\overline y\end{pmatrix}
 \overline{(a_+,a_-)} .
 \tag{EG.39}
\]
The outer cap is
\((P,q_H,w)\mapsto(A_wPA_w^*/\operatorname{tr}(A_wPA_w^*),
q_H,w)\), \(A_w=\left(\begin{smallmatrix}1&-w\\1&w\end{smallmatrix}\right)\).
It keeps the actual quaternion \(q_H\).
The inner cap is the same projection-normal
four-ball, with the extending factor in
(EG.36). The inverse line \(U=M^{-1}\)
and physical line \(M\) are carried over
both caps. The orbit calculation above
gives the actual integral Thom extension
and the same \(S^4\) normal-sphere boundary.
Thus the complete K95/F56 excision,
with relative second Chern number \(-1\),
has \(U\)-pair \((6,0)\) and physical
\(M\)-pair \((-6,0)\) in both rows.
The delta-averaged product connection
selects the return equal to the identity
on the fixed tube. Its literal K68
Hopf lift satisfies
\(\lambda_M(F)=-\Sigma_{F^{-1}}=\Sigma_F\).
This identifies the actual reference
native triple \((0,-6,-1)\).

## EG.5. Every vertical seed and every selected fan

Keep all coefficients (EG.14). On the
vertical fan \(T_j\) the full characters
and periods are
\[
 V_j=Z^{-j}V,\quad H_j=HB^j,\quad
 Q_j=\kappa qg^j,\quad
 \alpha_j=\alpha\eta^j\kappa^{-j}g^{-j^2},\quad
 \eta_j=\eta g^{-j}.
 \tag{EG.40}
\]
Here \(g=P^{-b}\), \(\alpha=P^a\).
The source interpolation
\(Q_t=Q\exp(tj\log g)\) has the exact
nodal vector field
\(\partial_t+j\log g\,y\partial_y\).
It is joined to the actual marked
period flow on the outside by a
vertical partition of unity, fixed
on the two protected collars.
Its Cartier arrow is \(Z^j\),
carrying the two generators
\(x^{-j-1}y^j,x^{-j}y^{j+1}\)
to \(1/x,y\). It retains (EG.38)
and both caps.

In the full real coefficient frame,
the q-deck is
\((u,d)\mapsto(u-b_{\rm ang},d-\gamma)\)
and the \(w\)-deck is
\((u,d)\mapsto(u+6b_{\rm ang},d)\).
All remaining unit logarithms occur
in these coefficients. The exact
relative connection difference is
\[
 A_j-A_0=-j\{du+(\alpha_q-6\theta)
                                     db_{\rm ang}\}.
 \tag{EG.41}
\]
The dual-line tensor has curvature
\(6j\,d\theta\wedge db_{\rm ang}\),
whose square is zero. Its relative
isomorphism is fixed by the actual
disc
\((q/Z_*,Z_*,1)\mapsto(qZ_*^{j-1},Z_*,Z_*^{-j})\)
with \(Z_*\) near \(-1\), away
from both marked point divisors.
After the integral cochain is
removed, its real Cech logarithm,
the extending \(\theta,b_{\rm ang},
\gamma\) characters and the
boundary logarithm give exactly
the specified outer line map.
The actual source/graph tangent
matrix is upper triangular in
the K63 frame order; its entire
comparison collar has zero
\(\operatorname{tr}(F^2)\).
For the relative \(p_1\) pairing use the actual level
cobordism of K63. Choose \(U_1\Subset U_2\Subset U_3\)
around the fixed tube, with all surgery and connection changes
in \(U_1\), and take the real lift \(\widetilde b\) of the
original source-product circle map \(b_{\rm ang}\) on \(U_3\).
For a cutoff \(\chi=1\) on \(U_2\), supported in \(U_3\),
and a fixed real constant \(c\), define the full relative homotopy
\[
 b_t=b_{\rm ang}
       \exp\!\bigl(2\pi i\,t\chi(c-\widetilde b)\bigr),
 \qquad 0\le t\le1.
 \tag{EG.41a}
\]
Outside \(U_3\) it is literally \(b_{\rm ang}\); at \(t=1\)
it is constant on \(U_2\). Choose a common regular value different
from \(\exp(2\pi i c)\). Its preimage under
\((x,t)\mapsto b_t(x)\) is the relative level cobordism, fixed on
the outer boundary. The terminal level misses \(U_1\), so it is
the identical cycle before and after surgery. The original level
is the actual source three-level times \(S^1_\gamma\); its
source-pulled \(p_1\) integral is zero. Stokes on the displayed
cobordism, with the retained zero outer \(p_1\) comparison and
transgression, gives zero on the terminal level. This proves the
required relative pairing without identifying the terminal level
itself with a product.
The outward Euler collar from
(EG.41) contributes \(-18j^2\);
the interior term is affine in
\(j\).

Both linear-endpoint values are
fixed by a literal family arrow.
From (EG.9)--(EG.12),
\[
 S_a(-w)=S_a(w),\quad
 c_a(-w)=P^{-a}c_a(w),\quad
 f_\theta(Z^{-1},P^{-a})
                  =P^a f_\theta(Z,P^a).
 \tag{EG.42}
\]
The last identity is the full
theta inversion at the same
\(Q\), with the actual lift
\(P=P_G(q,w)\). Thus the actual
source/line identity can also be checked directly on the full smooth
fibre. The source is the identity in \((X,Y,T)\); every coefficient
of the actual Miller functions (EG.3)--(EG.6) is holomorphic in
\(\zeta=w^2\). The canonical point-section coefficient is unchanged.
Since
\(\Theta_Q(Z^{-1})=-Z^{-1}\Theta_Q(Z)\), the exact tensor-coordinate
map is
\[
 \begin{split}
 V_a(-w)
 &=f_{P^{-1}}(Z^{-1})^a f_a(X,Y,T,-w)^{-1}v_a\\
 &=P^a f_P(Z)^a f_a(X,Y,T,w)^{-1}v_a
  =P^a V_a(w).
 \end{split}
 \tag{EG.42a}
\]
This gives the full source/line map
\((Z,V)\mapsto(Z^{-1},P^aV)\).
The target source period has
coefficient \(P^{-a}\); composing
it gives precisely
\[
 (Z,V)\longmapsto(Q/Z,V).
 \tag{EG.43}
\]
It carries every full root and
annular map because those were
constructed on the \(\zeta\)
disc before pullback. Its height
translation is one, so it sends
\(T_0\) to \(T_1\) with the
same physical characteristic
pair. Equations (EG.39)--(EG.43)
therefore give, for every integer
\(j\),
\[
 \begin{aligned}
 (k_M,\ell_M)&=(-6-18j(j-1),0),\\
 A_M&=-1-3j(j-1),\\
 (m_{\rm native},n_{\rm native})&=(0,-6-18j(j-1)).
 \end{aligned}
 \tag{EG.44}
\]

For an arbitrary selected lattice
basis \(P_{\rm bas}\), put
\(R_{\rm bas}=P_{\rm bas}^{-1}\).
In the following display \(P_{ij}\) and \(R_{ij}\) denote the
entries of these two matrices.
The actual character powers are
its two rows and its new period
powers are the two columns of
\(P_{\rm bas}\). Their complete
unit matrix is
\[
 A_{ij}=
 (\kappa^{P_{1j}}g^{P_{2j}})^{R_{i1}}
 (\alpha^{P_{1j}}\eta^{P_{2j}})^{R_{i2}},
 \qquad
 B_P=-6P_{\rm bas}^{-1}e_1e_1^tP_{\rm bas}.
 \tag{EG.45}
\]
The q-exponents are \(RP=I\).
The three full Cox edge rows are
\[
 \begin{gathered}
 (A_{11}A_{21}bc,A_{21}^{-1}ab,A_{11}^{-1}b^{-1}),\\
 (A_{12}A_{22}bc,A_{22}^{-1}c^{-1},A_{12}^{-1}ac),\\
 (a^{-1},ab,ac).
 \end{gathered}
 \tag{EG.46}
\]
Their normal determinants have
winding \(-6\), with first
windings
\((B_{22}-B_{21},B_{11}-B_{12},B_{22})\).
The actual based quaternion
contractions \(H_{-3}\) and
\(H_{l_i+3}\), together with the
full extending logarithms of
(EG.14), satisfy the exact
two-vertex tube identity
\(zD_{i,*}K_i=zD_i\).
Normal rescaling and the cutoff
flow of its velocity carry all
higher normal jets. Hence the
ordinary/native cylinder has
left degree \(-6\), right zero,
and inverse correction \(L^6\),
with the same odd Spin
endpoints and nine integral
prism equations as K71.

Each Euclidean fan step uses
the literal rank-one Cox ruling
map, common link
\((h,q_H)\mapsto(q_H^{-1}hq_H,q_H)\),
and its actual native reset.
They commute with every
coefficient in (EG.45).
The inverse character map on
the common exterior is the
identity in the original
source/Cartier coordinates,
so (EG.33) and its full finite
characters remain the same
at every step. The two compact
ruling charts, the unchanged
compact exterior and their
blowup/Gysin/primitive period
maps carry the sphere topology.
This identifies the entire
actual fanwise return algorithm
with K71, starting from all
the proved vertical seeds
(EG.44), for both full
progressions (EG.1).

The original parameter equation
\(r-1/3=-w^4/[3(w^2-3)^2]\)
is retained. This comparison
concerns the specified ordered
\(w\)-loop with fixed scalar.
No shorter source endpoint or
other E6 boundary is assigned
by these maps.
