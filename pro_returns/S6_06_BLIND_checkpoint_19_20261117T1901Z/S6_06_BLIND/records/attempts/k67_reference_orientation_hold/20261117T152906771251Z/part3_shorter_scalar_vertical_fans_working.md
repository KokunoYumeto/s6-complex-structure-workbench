# Shorter scalar endpoints and the actual vertical-fan comparisons

Working proof, 17 November 2026. This note retains the actual source,
line, cap, and endpoint maps in K35.2--5 and K33.1--3. It does not use
their withdrawn simultaneous equivariant product of the entire cusp
plumbing or the former K31 fan formula. K64 remains unchanged. The
reference-fan integer index is used, but no individual characteristic
pair on a changed fan is assigned here.

## SE.1. The actual shorter family and its finite-cap square

Fix a whole-zero I1 source and marked line from the canonical catalogue.
Write the contracting source translation as \(-bG\), the line as
\(\mathcal M=\mathcal O(aG-O+D)\), and the scalar family as
\(\lambda=r^M\). Here \(b\mid M\). The nontrivial root orders and the
actual order-one charts have exponents
\[
 P_i=Mn_i/m_i,\qquad \sum_iP_i=\varepsilon\in\{1,-1\},
 \quad A_{i,r}=r^{P_i}A_{i,0},\quad B_\lambda=r^MB_0.
 \tag{SE.1}
\]
The sum includes the actual framing-chart exponent \(-Mb_0\) in K32.
The finite cyclic equations are \(A_{i,0}^{m_i}=B_0^{n_i}\) and
\([A_{i,0},B_0]=1\), with every prescribed affine and line character.

Use the actual rational lift \(U\) of \(+G\), obtained from the chord
divisor in K35.6. Its norm is the rational base function
\[
 \rho=B_0^{-1}/U^b.
 \tag{SE.2}
\]
On root chart \(i\) its exact comparison to an extending lift is
\[
 U=z^{e_i}h_i(z)L_i,\quad L_i^b=B_0^{-1},\quad
 D_iL_iD_i^{-1}=\chi_iL_i,\quad
 \chi_i=\zeta_{m_i}^{e_i}=\zeta_b^{z_i},\quad
 h_i(\zeta_{m_i}z)=h_i(z).
 \tag{SE.3}
\]
These are maps of the actual corrected root line. In particular the
quadratic I1* line retains the two node scalars \((1,-1)\) and
\(\chi_i=-1\). The good III/III* roots have \(\chi_i=-1\), the good
IV/IV* roots have \(\chi_i=\rho_i^{-a}\), and the reduced partners
whose component class is killed by \(a\) have \(\chi_i=1\). The finite
averaging of a norm-one unit in K35.3 is performed before (SE.3); no
nonconstant unit is discarded as a character.

Let \(h_0=e^{2\pi iH}\) be the actual one-gamma **forward** ordinary
closing, including its bounded constant and all order-one charts.
The orders of \(h_0\rho^\varepsilon\) are divisible by \(b\).
At a root chart the required integer congruence is
\(P_i+\varepsilon z_i=0\pmod b\); at the selected I1 the simple
zero cancels the pole of \(B_0^{-1}\). Retain the specified rational
root \(g_0^b=h_0\rho^\varepsilon\). The actual forward arrow is
\[
 D_r=r^{-\varepsilon M/b}g_0U^\varepsilon:
 X_r\longrightarrow X_{\zeta_b r}.
 \tag{SE.4}
\]
At cap \(i\), the ordinary-to-cap cochain changes by
\(+Mn_i\log z\,\delta/(2\pi ib)\), cancelling the literal ordinary
power \(z^{-Mn_i/b}\). Its remaining map is an invariant unit times
\(L_i^\varepsilon\), and
\[
 L_i^\varepsilon A_{i,r}L_i^{-\varepsilon}
   =\chi_i^{-\varepsilon}A_{i,r}
   =\zeta_b^{P_i}A_{i,r}=A_{i,\zeta_b r}.
 \tag{SE.5}
\]
It commutes with \(B_\lambda\). Thus this is the actual cap square,
not a fibrewise identification without an endpoint. The integral
annular/source-period cochain is retained as
\[
 \frac{P_i\delta-\varepsilon(A_i-I)e_\gamma}{b}
 =(0,-\varepsilon k_{i,2},\varepsilon k_{i,1},
                    (P_i+\varepsilon z_i)/b)^t.
 \tag{SE.6}
\]
This supplies every finite group arrow as well as the ordinary overlap.

## SE.2. The bounded forward endpoint and a literal pullback product

Use the actual logarithmic cusp characters, with exponential
\((z_1,z_2)\mapsto(Z,V)=(e^{2\pi iz_1},e^{2\pi iz_2})\).
The marked outward gamma and forward ordinary logarithm are
\[
 \gamma=(\Gamma,C-s-Mv),\quad
 H=\varepsilon s+U_0(q),\quad v=\log r/(2\pi i).
\]
Here \(\Gamma=b\mu_G\) is the fixed bounded Tate lift of \(+bG\);
\(U_0\) denotes a bounded base logarithm and is distinct from the
rational source lift \(U\). The bounded displacement of (SE.4) is
\[
 \tau(v)=\frac{H\delta+\varepsilon\gamma}{b}
   =\left(\frac{\varepsilon\Gamma}{b},
           \frac{U_0+\varepsilon C-\varepsilon Mv}{b}\right).
 \tag{SE.7}
\]
Every entry is holomorphic on the whole cusp disc. Put
\[
 \alpha=\frac{\varepsilon M(b-1)}{2b^2},\qquad
 d(v)=\tau(v)+\alpha\delta,
 \quad \widetilde D_r=e^{2\pi i\alpha}D_r.
 \tag{SE.8}
\]
The added factor is the actual global physical-circle action. It
changes neither (SE.5) nor any finite affine vector. The exact norm is
\[
 \sum_{j=0}^{b-1}d(v+j/b)=b\tau(v)
                         =H\delta+\varepsilon\gamma.
 \tag{SE.9}
\]
On the ordinary charts the same equality follows from (SE.2), including
the scalar factor of (SE.4). Consequently the b-th iterate is the
specified one-gamma r-closing, and the quotient is the actual proper
family over \(w=r^b\). Its scalar winding is
\[
                         J=M/b.
 \tag{SE.10}
\]

The bounded vector
\[
 \sigma(v)=\left(\varepsilon\Gamma v,
   v(U_0+\varepsilon C)-\frac{\varepsilon M}{2}(v^2-v)\right)
 \tag{SE.11}
\]
satisfies \(\sigma(v+1/b)-\sigma(v)=d(v)\) exactly, including
the constant in (SE.8). Since (SE.4) is **forward**, the closed native
coordinates are \(\xi=z-\sigma(v)\). This arrow differs from the
endpoint-to-initial OS49 closing, whose closed coordinates use a plus
sign. All formulas here use the forward convention (SE.4).

For a cut shorter parameter interval beginning at \(v\), set
\[
 C_s(v)=\exp\bigl(\sigma(v)-\sigma(v+s)\bigr),
      \qquad 0\le s\le1/b.
 \tag{SE.12}
\]
The exponential acts on the two torus characters. It is a holomorphic
nonzero unit on the full cusp disc, smooth in the path variable. Its
inverse has the negative exponent. It commutes with the actual torus
periods and with physical delta. Its terminal value is precisely
\(\widetilde D_v^{-1}\). The functional identity in (SE.11) holds
on a whole parameter neighborhood, so the first and last collars
match with all derivatives, rather than only at their endpoints.

Retain the b successive factors
\[
 \begin{split}
 P_j(v)&=\exp\bigl(\sigma(v)-\sigma(v+j/b)\bigr),\\
 \log P_j/(2\pi i)
   &=-j\tau(v)-j\alpha\delta
           +\frac{\varepsilon Mj(j-1)}{2b^2}\delta.
 \end{split}
 \tag{SE.13}
\]
The logarithm is the displayed vector on the fixed logarithmic cover.
For every sheet, including both collars,
\[
 C_s(v+j/b)P_j(v)=C_{j/b+s}(v),\qquad
 P_b(v)=\exp(-H\delta-\varepsilon\gamma).
 \tag{SE.14}
\]
Thus the r-product is the **literal b-fold pullback** of the shorter
native product. Every cap chart is pulled back by (SE.5), and the
full lattice cochain (SE.6) accompanies it. No new covered boundary
product is chosen.

## SE.3. Each actual native star and its full unit maps

For the fan \(T_n\), use the same literal shear as K64,
\[
 Z_n=Z,\quad V_n=Z^{-n}V,\quad h_n=hB^n,\quad B_n=B.
\]
Its full unit coefficients are
\[
 \kappa_n=\kappa g^n,\quad
 \alpha_n=\alpha_0\eta^n\kappa^{-n}g^{-n^2},\quad
 g_n=g,\quad\eta_n=\eta g^{-n},\qquad \eta=\lambda\beta.
 \tag{SE.15}
\]
Here \(\alpha_0\) is the original period multiplier, not the constant
in (SE.8). Its shorter-loop winding vector is exactly
\((0,nJ,0,J)\). The source factor \(U^\varepsilon\) in the endpoint
has not been removed: it is the first component of (SE.7).

Apply the same shear to \(\sigma\):
\(\sigma_n=(\sigma_1,\sigma_2-n\sigma_1)\). If (SE.12) has
character multipliers \((A,D)\) in these coordinates, its two vertex
maps are literally
\[
 (a,b_1,c)\mapsto((AD)^{-1}a,Ab_1,Dc),\qquad
 (u,v_1,w_1)\mapsto(ADu,D^{-1}v_1,A^{-1}w_1).
 \tag{SE.16}
\]
The complete transitions, before suppressing any unit, are
\[
\begin{array}{c|ccc}
 &u&v_1&w_1\\ \hline
 C_0&\kappa_n\alpha_n b_1c&\alpha_n^{-1}ab_1&\kappa_n^{-1}b_1^{-1}\\
 C_1&g_n\eta_n b_1c&\eta_n^{-1}c^{-1}&g_n^{-1}ac\\
 C_2&a^{-1}&ab_1&ac.
\end{array}
 \tag{SE.17}
\]
Substitution of (SE.16) gives the same factors on every row. The
native C1 coordinates are
\((c,a,b_1)\) and \((\eta_nv_1,g_nw_1,(g_n\eta_n)^{-1}u)\);
the native C2 coordinates are \((a,b_1,c)\) and \((u,v_1,w_1)\).
Each has the literal transition
\(z'=z^{-1},\ n'_i=zn_i\). On C1 the factors are
\((D,(AD)^{-1},A)\) and \((D^{-1},A^{-1},AD)\); on C2 they are
\(((AD)^{-1},A,D)\) and \((AD,D^{-1},A^{-1})\).
These are exact automorphisms of the individual
\(\mathcal O(-1)\oplus\mathcal O(-1)\) models. They prove closed
native products on those stars. They do not supply a simultaneous
physical-circle-equivariant product of the three-curve plumbing.
The physical height is \(q=ab_1c\). Along any open curve axis it
vanishes to second order in the two normal coordinates, and at a
vertex it has order three. Thus the normal derivatives of the full
source factors \(A(q,v),D(q,v)\) are their values at \(q=0\), constant
along that curve; their remaining terms are precisely higher normal
jets carried by the normal-rescaling isotopy below. This retains the
q-dependence instead of treating the source factor as a constant map.

The Cox lifts, in the native orders, are
\[
 \begin{split}
 C_1:&\ (a_0,a_1,c_0,c_1)
       \mapsto(a_0,Da_1,(AD)^{-1}c_0,Ac_1),\\
 C_2:&\ (a_0,a_1,c_0,c_1)
       \mapsto(a_0,(AD)^{-1}a_1,Ac_0,Dc_1).
 \end{split}
 \tag{SE.18}
\]
They preserve q and extend to both resolutions. In particular the
extra bounded source factor of the shorter endpoint is present in
both Cox rulings. The free period action transports a representative
to its orbit with the same maps. Outside those neighborhoods the
source, line, and every finite-cap arrow remain (SE.4)--(SE.6).

## SE.4. The ordinary double product and the actual relative square

Take the literal double pullback of the single native products just
constructed; (SE.13)--(SE.14) applies to its intermediate seams as
well. In the second vertex frame \((u,\eta_nv_1,\kappa_nw_1)\),
the actual based normal matrices of (SE.17) have double windings
\[
 K_0=\operatorname{diag}(e^{2iJ(1-n)\theta},e^{2inJ\theta}),\quad
 K_1=\operatorname{diag}(1,e^{2iJ\theta}),\quad
 K_2=\operatorname{diag}(e^{2iJ\theta},1).
 \tag{SE.19}
\]
Before reference division the respective factors are
\((\eta_n/\alpha_n,\kappa_n\alpha_n)\),
\((\kappa_n/g_n,g_n\eta_n)\), and \((\eta_n,\kappa_n)\).
All zero-winding based units have their logarithms on the full q-disc.
The seams (SE.16) preserve these rows. Their parameter-dependent vertex
actions commute with physical delta, so the vertex orbit maps have
no additional parameter dependence. Their stable coordinate-frame
changes extend over the vertex four-disc and the curve annulus.

Use the actual ordinary quaternion contractions of K64 with
\[
 t=J,\qquad(l_0,l_1,l_2)=(2J(1-n),0,2J),\quad
 Q\mapsto H_tQH_{l_i-t}.
 \tag{SE.20}
\]
The common determinant loop in (SE.19) makes the first vertex product
common. The remaining determinant-one loops are filled by these
literal H maps. Multiply by the exponentials of the retained bounded
unit logarithms, with radial cutoffs, and restore the full germs by
normal rescaling and its cutoff velocity. This gives the same actual
ordinary double product construction as K64 on the supplied seams.

The physical weights are \(w=(0,1,-1)\) and \(d=(-2,-1,-1)\).
The meridian and stable-derivative trace degrees of the displayed map
are therefore
\[
 I=(-2J+4nJ,2J,-2J),\qquad W=(2J-4nJ,0,0).
 \tag{SE.21}
\]
The exact vertex paths and rank-one endpoint caps in K64 close the
traces. They remain independent of the parameter under (SE.16),
including its bounded source factor. The two ordinary relative pairs
are \((-2nJ,2J(n-1))\) and \((2J(n-1),-2nJ)\).
The native comparison is
\[
 q_H\mapsto(UH_JU^{-1})q_HH_{l_i-J}.
 \tag{SE.22}
\]
It has left degree 2J and right degree zero, with the inverse cylinder
endpoint \(L^{-2J}\). Hence the actual native doubled pairs are
\[
 C_1:(2J(1-n),2J(n-1)),\qquad C_2:(2nJ,-2nJ).
 \tag{SE.23}
\]
Choose a connection on the actual compact shorter family equal to its
native product velocity on a collar; extend it by a cutoff and the
affine space of connections. Its double pullback has exactly the
boundary products in (SE.14). Interpolation relative to that boundary
compares it to (SE.20). Thus (SE.23) belongs to the actual relative
square. Multiplication by two on the free relative coordinates is
injective, giving the single pairs
\[
 C_1:(J(1-n),J(n-1)),\qquad C_2:(nJ,-nJ).
 \tag{SE.24}
\]
Equivalently its literal b-fold pullback has the K64 pairs with
\(bJ=M\); (SE.14) identifies the products in this check. There is no
division in the seven-sphere group in either calculation.

For the flop use the unrestricted four-weight common-link map with
the actual Cox lifts (SE.18). Transport the metric by the full units
and use positive radial normalization. The resulting common-link
map is \(T(y,q_H)=(q_H^{-1}yq_H,q_H)\), followed by the same fixed
complex-normal reset as K62/K64. Its action on the relative group
adds the right native coordinate to the central class. C2 replaces
\((1,n-1)\) by \((1,n+1)\), and C1 replaces \((1,n)\) by
\((1,n-2)\). Therefore the actual shorter returns satisfy
\[
 A_{n+1}-A_n=-nJ,\qquad A_{n-1}-A_n=(n-1)J,
 \quad A_n=A_0-Jn(n-1)/2\pmod {28}.
 \tag{SE.25}
\]

The reference-fan value uses only the actual equivariant cover.
The shorter endpoint commutes with physical delta and preserves the
complex orientation. Its b-fold parameter cover is the prescribed
r-family by (SE.9), so pullback of the Euler line and tangent bundle
multiplies the integer characteristic index by b. The previously
computed reference integer is \(\chi-H_{\rm page}/2\). Consequently
\[
 A_0=(\chi-H_{\rm page}/2)/b\in\mathbb Z,
 \qquad H_{\rm page}=Ma^2/d_{\rm source}.
 \tag{SE.26}
\]
This uses no simultaneous normal framing and assigns no separate k
or ell to a changed fan. The actual Hopf transfer then supplies its
reference sphere class, which is the input to (SE.25).

## SE.5. The original K33 endpoint with its retained constant

For the original construction use root orders \(3K,4L\),
\(\gcd(3K,4L)=1\), and \(4Ln_0+3Kn_1=\varepsilon\).
Its actual parameter is
\[
 w_h=e^{-\pi ic/(KL)},\quad u=\kappa w_h^{2KL},\quad
 w_h=r^6,\quad M=12KL.
 \tag{SE.27}
\]
The exact integral cochain and finite norms are K33.4--7:
\[
 p=(0,-\varepsilon,\varepsilon,(4Ln_0+2\varepsilon)/6)^t,
 \quad q=(0,0,\varepsilon,(3Kn_1-3\varepsilon)/6)^t.
\]
The full ordinary, root, annular, and cusp maps obey
\(x_{\rm cov}-6x=d^0(\varepsilon e_1,\varepsilon e_1,
\varepsilon e_1,0)\). Their actual one-step forward cusp vector is
\(\tau=(H\delta+\varepsilon\gamma)/6\), with no scalar correction
silently added. The canonical sigma above has
\(\Delta_{1/6}\sigma=\tau+5\varepsilon KL\delta/6\).
Retain instead the specified original endpoint product
\[
 \sigma_{\rm desc}(v)=\sigma(v)+\varepsilon KLv\delta,
 \qquad \Delta_{1/6}\sigma_{\rm desc}
                    =\tau+\varepsilon KL\delta.
 \tag{SE.28}
\]
The last term is an integral physical period, so its exponential is
one in every actual toric character and on every finite cap. Thus
\(z-\sigma_{\rm desc}(v)\) is a closed native-star coordinate for
the original forward endpoint. Its j-fold product has additive
discrepancy \(j\varepsilon KL\delta\), still an actual integral
period. Formula (SE.14) holds with sigma_desc and the same exact
original source/root cochain.

On the r-cover, subtracting the initial origin makes the difference
from the sigma product the literal global map
\[
 G_\theta:X_{r(\theta)}\longrightarrow X_{r(\theta)},
 \qquad G_\theta=\delta_{-\varepsilon KL\theta},
                         \quad0\le\theta\le1.
 \tag{SE.29}
\]
It is the physical scalar multiplication on the line. It commutes
with every period and finite affine map, and its integral toric
character action extends over all the indicated charts. Since
\(G_0=G_1=1\), it is a based periodic global gauge, not merely a
map on one normal boundary. Transporting a connection by this map
preserves its actual based relative return under the transported
native boundary products. Its intermediate right quaternion phase
is retained by (SE.18). This proves the covered product comparison
without identifying the original endpoint with another sixth root.

Alternatively (SE.19)--(SE.24) applies directly to the original
native seam (SE.28), whose actual scalar winding is \(J=2KL\).
The exact base/root arrow \(T=(t-1)/t\) in K33.14--15 identifies
the reference page with the E6 \((a,b)=(1,6)\) row and retains both
norm signs. Its cover reference index is zero. Integer index
naturality gives \(6A_0=0\) in \(\mathbb Z\), hence \(A_0=0\).
The vertical-fan result is therefore
\[
             A_n=-KL\,n(n-1)\pmod {28}.
 \tag{SE.30}
\]
For \(K=L=1\), T2 has class \(-2\), while T0 and T1 have class
zero. No arbitrary-fan formula, source-moduli return, or separate
characteristic pair is assigned by this note.

The accompanying exact certificate is
`code/part3/shorter_scalar_vertical_fans.py`. It checks the cyclic norm,
all intermediate product logarithms, the native and Cox maps, the
full-unit shear and winding trace, the original integral constant,
and both signed norm choices. These algebraic identities accompany
the actual cap and relative-product maps above.
