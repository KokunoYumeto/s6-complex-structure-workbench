# The order-three source generator with every reduced E6 cap

We keep the original source
\(y^2=x^3+r x^2+tx+t^2\), the section \(G=(0,t)\),
the point line \(M_6=\mathcal O(6G-O)\), translation by
\(-G\), and the ordered selected node of K99, with
\(\rho\) near \(+1/2\). The source parameter is
\(s=1/4-r\). Its positive circle is the unselected
order-three source generator of E87 and K99. The scalar
is fixed, with the actual finite character and the full
reference annular map retained. We construct here its
cap comparison for
\[
 m=3l+2,\quad l\ge0,\quad n=\pm1,\quad d\in\mathbb Z/m.
                                                        \tag{OC.1}
\]
The line remains M6 and the source translation remains
\(-G\). No change to the M2 line or its \(-3G\)
translation is made in this comparison.

## OC.1. The full root source over the order-three disc

Put \(k=2l+1\). The exact source/root map is
\[
 q_\infty=z^m,\quad x_0=z^{2k}X,\quad y_0=z^{3k}Y,
 \qquad
 Y^2=X^3+r z^{2l+2}X^2+z^{l+2}X+z^2,\quad G'=(0,z).
                                                        \tag{OC.2}
\]
Its original affine coordinates are
\(t=z^{-m},x=z^{-2(l+1)}X,y=z^{-3(l+1)}Y\).
These are morphisms on their stated punctured domains,
and the displayed Weierstrass projective maps retain
the zero and marked section.

Let \(b_0=z^l,c_0=r z^{2l}\) and
\(c=(1+b_0X+c_0X^2)^{1/2}\), with value one at the
origin. The exact source coordinates
\(U=Y-zc,V=Y+zc\) satisfy \(UV=X^3\). Conversely
\(2zc=V-U\) has a unique analytic inverse for z
jointly with s near the origin: its z derivative
there is two. Its three resolution charts are
\[
\begin{array}{c|ccc}
 &X&U&V\\\hline
 \text{middle}&ab&a^2b&ab^2\\
 \text{U-end}&ab&a&a^2b^3\\
 \text{V-end}&ab&a^2b^3&a.
\end{array}                                             \tag{OC.3}
\]
For example the first overlap has
\(a_{\rm middle}=b_{\rm U}^{-1}\),
\(b_{\rm middle}=a_{\rm U}b_{\rm U}^2\).
Each map carries the same analytic inverse z,
hence the original function \(q_\infty=z^m\).
Together with the smooth group charts these give
the full resolved root family, smooth over the
entire s disc including zero.

For specificity the actual \(+G'\) map in the
middle chart is the complete map of EX.7:
\[
\begin{split}
 K&=1+\frac{b(b-a)(b_0+c_0ab)}{2c(c+1)},\\
 F&=1-\frac{ab(b_0+c_0ab)(K+1)}{2c(c+1)}
              -\frac{c_0ab^2(a-b)}{4c^2},\\
 X'&=a(a-b)F,\qquad c'=(1+b_0X'+c_0X'^2)^{1/2},\\
 H&=K+\frac{b(a-b)(b_0+c_0X')}{2c(1+c')},\\
 (a',b')&=((b-a)F/H,-aH).
\end{split}                                             \tag{OC.4}
\]
Every denominator is a unit on the same sufficiently
small root chart; \(K=F=H=1\) at its triple point.
The inverse is the actual opposite chord, obtained
also by \(Y\mapsto-Y\). It preserves z through the
inverse in OC.3. These equalities are uniform in r;
in particular there is no denominator s in this
source translation map.

The root deck is
\[
 D(z,X,Y)=(\zeta_mz,\zeta_m^{-2k}X,\zeta_m^{-3k}Y).
                                                        \tag{OC.5}
\]
The identities \(l-2k=-m\), \(3k=2m-1\) and
\(3(l+1)=m+1\) give the exact invariant c, the
weight \(\zeta_m\) of U,V, and the common weight
\(\zeta_m^{l+1}\) of a,b. Thus OC.4 commutes with
this entire deck, including its base coordinate.

The identity-component invariant field is the
actual field
\[
 a\left(2b-a-\frac{z(b_0+2c_0ab)}c\right)\partial_a+
 b\left(2a-b+\frac{z(b_0+2c_0ab)}c\right)\partial_b.
                                                        \tag{OC.6}
\]
It is holomorphic and vanishes at the triple point;
its flow agrees with the group translation on the
smooth locus by its Weierstrass differential.
Consequently the formal division in
\[
 R=2G'-[m]^{-1}((2m-1)G'),\qquad mR=G'                 \tag{OC.7}
\]
defines the full analytic source translation on
the resolved root. Its formal inverse has derivative
\(1/m\). Since \(2m-1=3(2l+1)\), its argument is
in the identity formal group. The exact identity
\(mR=2mG'-(2m-1)G'=G'\) uses that same division.
Uniqueness and OC.5 make R deck invariant. At
s zero, the actual section G' has order three,
so the formal argument is zero and R equals
\(2G'\) there. Its extension does not require
the section \(3G'\) to be nonzero.

## OC.2. The actual coincident-section Cartier map

Let \(\tau_0=-x_0/y_0\) and \(\tau'=-X/Y\).
The exact coordinate arrow is
\(\tau'=z^k\tau_0\). The original threefold
section calculation gives
\[
 \tau_0(3G)=
 -\frac{2s(2+s q_\infty)}
         {8+6s q_\infty+(s^2-s^3)q_\infty^2}.
                                                        \tag{OC.8}
\]
The denominator is a unit jointly in \((s,q_\infty)\).
Apply the actual formal doubling to this section.
It gives the full analytic function L with
\[
 \tau'(6G')=z^kL(s,z^m),\quad L(s,0)=-s,
 \quad L(s,q_\infty)=s\ell(s,q_\infty),
 \quad\ell(0,0)=-1.                                   \tag{OC.9}
\]
The factorization by s follows from the literal
order-three identity at s zero. Shrinking the
joint chart makes \(\ell\) an analytic unit.
Equation OC.9 is retained with its full function;
it is not replaced by its leading coefficient.
For an explicit rational definition of that entire function,
in the original affine chart put
\[
\begin{split}
 x_3&=2t(2t+s)/s^2,\\
 y_3&=t(8t^2+6st+s^2-s^3)/s^3,\\
 a_6&=(3x_3^2+2rx_3+t)/(2y_3),\\
 x_6&=a_6^2-r-2x_3,\qquad
 y_6=-y_3+a_6(x_3-x_6),\\
 L(s,q_\infty)&=-x_6/(q_\infty y_6),\qquad
 t=q_\infty^{-1},\quad r=1/4-s.
\end{split}                                             \tag{OC.9a}
\]
The first two coordinates are the actual addition
\(2G+G\), and the next three are the actual tangent
doubling of \(3G\). Substitution and cancellation
in OC.9a write \(L/s\) as a quotient of polynomials
in \((s,q_\infty)\), whose numerator and denominator
at the origin are respectively \(-1024\) and \(1024\).
The exact polynomials are retained in the certificate
of OC.6. Thus OC.9a also proves directly the joint
unit statement and specifies every coefficient of L.

Use the normalized graph of \(u=\tau'/z^k\), with
its morphisms \(\beta\) to the root and \(\pi\)
to the original minimal regular source. Its
actual ideal is \((\tau',z^k)\); resolve the
remaining cyclic chart by the primitive rays
\((j,1)\), \(j=0,\ldots,k\), and \((1,0)\).
Every adjacent determinant is one. On a chart
between adjacent rays, original monomials are
the integer characters of those rays, so the
map retains both \(\tau'\) and z exactly.
This is the same proper graph as EX.10--12.

The two original section equations are
\(\tau'\) and \(\tau'-z^k s\ell\). On the
graph their exact Cartier coefficient is
\[
 \frac{\tau'}{\tau'-z^ks\ell(s,z^m)}
  =\frac{u}{u-s\ell(s,q_\infty)}.                       \tag{OC.10}
\]
In the other chart \(\tau'v=z^k\) it is
\(1/(1-vs\ell(s,z^m))\), with \(uv=1\)
on the common open set. These are coefficient
arrows of the two specified Cartier line
modules; their inverses are the reciprocal
arrows between the reversed source and target.
At s zero their sections coincide. The equations
\(u\) and \(u-s\ell\) remain their separate
total-family Cartier generators, including
the intersection \(u=s=0\).

Along an exceptional divisor of ray \((j,1)\),
the two generic orders are both j. On the
equality ray j=k the strict equations are
exactly the two equations in OC.10, including
their coincident point. Its extra intersection
at s zero has codimension two in the total
graph and introduces no new divisor. This
proves on the complete graph the actual
equality of line-module maps
\[
                   \beta^*N_6=\pi^*M_6,
 \qquad N_6=\mathcal O(6G'-O).                         \tag{OC.11}
\]
The other root/source cyclic resolution
centres contain neither marked section and
carry their canonical section frames. Their
invariant monomial maps therefore add no
coefficient to OC.11. Translations and their
inverses carry the original source/root
graph to itself. Its normalized closure,
followed by the specified common regular
refinements, carries their actual lifted
maps. Thus OC.11 is an equivariant equality
with the complete point-section coefficient,
including at the order-three coincidence.

## OC.3. The extending Hom map and its full norm root

All original Miller factors and their chronological
translation arguments are retained. Their weights
under OC.2 give exactly
\[
 B_{{\rm sel}}'=h z^{-2}B'_6,
 \qquad h=1-t_{\rm selected}(s)z^m.                    \tag{OC.12}
\]
The selected node stays near \(1/54\), so h
and its inverse are holomorphic on this
small infinity cap. On the open s nonzero,
EX.13 gives order two for \(B'_6\) on
each reduced central root component, with
central coefficient \(4h\) after division.
On s zero the exact original formula is
\(B_{6,\rm old}=4t^2\). Since
\(B_{6,\rm old}=z^{-6(l+1)}B'_6\) and
\(2m=6l+4\), this gives
\[
 B'_6=4z^2,\qquad B_{{\rm sel}}'=4h\quad(s=0).
                                                        \tag{OC.13}
\]
These are equalities in the genuine point-line
frames carried by OC.11. Horizontal factors
are their exact Cartier Hom divisors. Therefore
both the actual Hom map OC.12 and its inverse
have order zero at every codimension-one
prime of the full smooth root charts:
the horizontal ones cancel as line maps,
the central component orders are those just
specified, and the s-divisor order is zero
by OC.13. The intersection of the height-one
valuation rings in each normal chart then
extends the two rational maps, with their
product one, through \(s=z=0\). This proves
the joint extending unit as a line morphism.

There is also a full starting lift of translation
by \(-R\) which remains regular as the marked
point \(P=6G'\) becomes O. Let \(\tau=\tau'(P)\)
and write its actual Weierstrass coordinates as
\(X_P=A/\tau^2,Y_P=-A/\tau^3\), where A
is the analytic formal-group function with
\(A(0,z,s)=1\). In the affine Weierstrass
chart of R, the literal chord gives
\[
 \tau\ell_{P,R}(X,Y)=
 \tau(Y-Y_R)+
 \frac{A+\tau^3Y_R}{A-\tau^2X_R}(X-X_R).
                                                        \tag{OC.14}
\]
The denominator is a unit near the full root
central section. Define the actual Hom
coefficient
\[
 F=\frac{\tau\ell_{P,R}(X,Y)}{X-X_{P+R}}.              \tag{OC.15}
\]
Its divisor is the specified
\([P]+[R]-[P+R]-[O]\), so it covers
\(p\mapsto p-R\) on N6. In the limit
\(\tau=0\), OC.14 has numerator
\(X-X_R\); the denominator is the same
function because P+R=R. Thus its coefficient
in the actual coincident Cartier modules
is one. This is an equality of the two
typed generators, not evaluation of an
uncancelled zero over zero.

At a generic point of the identity root
component this also gives the full central
coefficient one as z tends to zero.
The central line N6 has degree zero on
each component, and its translated line
has the same degrees. Hence the vertical
divisor of this Hom section lies in the
kernel of the full central intersection
matrix, namely the fibre multiplicity
vector. The generic identity-component
value fixes its coefficient at zero.
The horizontal divisors have just been
matched, and OC.14 fixes the s-divisor
order. The same normal-chart argument
therefore extends F and its inverse
over the whole joint disc. In particular
the factor \(\tau=z^ks\ell\) was kept
in OC.14; the proof uses its exact
pole cancellation at s zero.

The chord-over-vertical ratio has deck
weight \(\zeta_m^{-k}\), and \(\tau\)
has weight \(\zeta_m^k\). Their product
F thus commutes with D as an actual
line map. The ratio
\(\beta=B_{{\rm sel}}'/F^m\), where
\(F^m\) is composition of the m
successive translated maps, is an
invertible base function. Indeed both
maps cover the same translation by
\(-G'\); their quotient is a
holomorphic function on each connected
compact source fibre and hence a base
function. It has value four at z zero
and is deck invariant. Its actual
analytic m-th root is fixed by the
reference value. Uniqueness makes that
root deck invariant as well. Put
\[
 \widetilde F=\beta^{1/m}F,\quad
 A_0=\zeta_m^d\widetilde F^{\,n}D,
 \quad A_0^m=(B_{{\rm sel}}')^n,
 \quad[A_0,B_{{\rm sel}}']=1.                          \tag{OC.16}
\]
The prescribed finite character remains
the literal factor \(\zeta_m^d\).
For the prescribed scalar root
\(R_\lambda^m=\lambda\), independent
of s, set \(B_\lambda=\lambda
B_{{\rm sel}}'\) and
\(A_\lambda=R_\lambda^n A_0\).
The exact identity is
\(A_\lambda^m=B_\lambda^n\).

## OC.4. The full annular reference and cap product

The ordinary-to-cap map retains the entire
reference cochain. On the actual annular
sectors put
\[
 s_\alpha=\frac{\log_\alpha q_\infty}{2\pi i},\quad
 z_\alpha=e^{2\pi i s_\alpha/m},\quad
 c_\lambda=\frac{n\log R_\lambda}{2\pi i}+\frac dm,
 \quad f_\alpha=\operatorname{Log}_\alpha\widetilde F.
\]
Here \(s_\alpha\) is the sector logarithm,
distinct from the source parameter s.
The complete map is
\[
 \Phi_\alpha=\operatorname{Exp}
 (n s_\alpha f_\alpha+s_\alpha c_\lambda\delta
                  +h_\alpha)I_{z_\alpha}.              \tag{OC.17}
\]
Its overlap data, in the original Lie
frame and with the reference integers,
are
\[
\begin{split}
 s_\beta&=s_\alpha+j_0,
 \quad f_\beta=D_*^{j_0}f_\alpha+\Pi_{\alpha\beta},\\
 h_\beta-D_*^{j_0}h_\alpha
   &=-n s_\alpha\Pi_{\alpha\beta}
        +j_{\alpha\beta}\operatorname{Log}_\beta B_\lambda
        +\Lambda_{\alpha\beta}.
\end{split}                                             \tag{OC.18}
\]
The reference-zero Cauchy construction in
EX.18 applies to the extending functions
OC.2--16 on this actual source disc:
extend the reference cochains, form
their overlap residual E, put
\(k_\alpha=-\sum\chi_\beta E_{\alpha\beta}\),
and subtract the common Cauchy transform
of \(\bar\partial k_\alpha\) on the fixed
annulus. The residual vanishes at the
reference source parameter. The fixed
partition and contours preserve analytic
dependence on s, and the constructed
cochains retain exactly that reference
value. The integer period and suspension
columns in OC.18 have not been changed.
Substitution gives the full arrows
\[
 \Phi_\beta=A_\lambda^{j_0}
           B_\lambda^{j_{\alpha\beta}}\Phi_\alpha,
 \qquad \Phi_\alpha B_\lambda=B_\lambda\Phi_\alpha.
                                                        \tag{OC.19}
\]
The inverse uses the reversed sector
arrow, its inverse root map and the
negative Lie displacement. Thus these
are actual inverse gluings of the
original ordinary annulus to the
cap, retaining every finite character,
normal derivative and reference integer.

All these cap charts and maps extend
over the s disc. The original line
period has uniformly bounded coefficient
on its compact source cut. Fix the
original scalar in the common strict
contraction range for this cap and the
quadratic reference cap. For both norm
signs the primitive generator
\(H=A_\lambda^n\) satisfies \(H^m=B_\lambda\).
Choose a number \(\rho_0<1\) with
\(\|B_\lambda v\|\le\rho_0^m\|v\|\)
uniformly in the chosen Hermitian
source-line atlas. The actual weighted Hermitian norm is
\[
 \|v\|'^2=\sum_{j=0}^{m-1}\rho_0^{-2j}\|H^jv\|^2.
\]
It is equivalent to the original norm on the compact
source cut. Its exact transformation is
\[
 \|Hv\|'^2=\rho_0^2\bigl(\|v\|'^2-\|v\|^2
                +\rho_0^{-2m}\|B_\lambda v\|^2\bigr)
          \le\rho_0^2\|v\|'^2.
\]
Its compact norm shell and the finite
source/root charts prove properness
and freeness of the cyclic quotient.
The actual maps preserve s and their
smooth coordinate charts retain its
nonzero derivative. The quotient cap
therefore forms a proper smooth family
of six-dimensional manifolds with
boundary over the full source disc.
Its physical circle is free; a
nonzero power of the contracting
primitive generator cannot equal a
unit-modulus physical scalar on a
nonzero vector.

Prescribe a product of the ordinary
annulus over the source disc. The
derivative of OC.17 carries its
horizontal lifts to the cap collar.
A relative partition of unity and
circle averaging extend those lifts
over each compact cap, preserving
that precise boundary product.
Integrating them radially over the
disc gives its complete product with
that same prescribed boundary map.
The full line and tangent derivatives
are transported in this construction.
There is no source-parameter endpoint
deck: all functions and cochains just
constructed are single valued on the
disc. The full root and sector word
OC.19 is nevertheless retained on
every annular overlap.

## OC.5. Integral comparison with the quadratic reference

Compare the actual fixed-scalar boundary
family for OC.1 with the quadratic
norm-one family of K99, on the same
original ordinary source, line,
selected fan and parameter circle.
Cut both along the same small original
infinity annulus. Their exteriors are
literally the same family; the complete
Cartier arrows are the identity there.
Their two cap pieces are the products
constructed in OC.4, with the same
ordinary boundary product. The physical
circle quotients of those cap pieces
are five-dimensional manifolds with
boundary, and their parameter families
are their products with the same circle.

Choose on each cap quotient its line
and tangent connections pulled back
from that five-dimensional body, with
the common prescribed collar connection.
The forms \(x^3\) and \(p_1x\) vanish
on each such product because all their
coefficients are pulled back from a
five-dimensional manifold. On the
common six-dimensional mapping-torus
exterior use the identical connections.
The actual derivative and line maps
OC.17--19 make these connections agree
on the two glued collars. Thus the
completed cubic and Pontryagin-linear
integrals agree individually, including
their boundary transgressions.

The selected tube and its K68 Hopf
cap are disjoint from this infinity
replacement and have the identical
complete maps in both families.
The physical Euler line and the
literal first-to-second Jin clutch
therefore have the same orientation
and generator. K99 and the exact K68/Cox
product of OF.1--3 give for every cap
OC.1 the exact initial-fan pair
\[
 (k_M,\ell_M)=(-27,-12),\quad
 (m_{\rm native},n_{\rm native})=(-3,-24),\quad A=-4.
                                                        \tag{OC.20}
\]
The same argument applies to every
vertical fan: its selected products
are precisely the ordinary products
of OF.1--3, independent of the
infinity cap. Hence its full native
array is \(V=\operatorname{diag}(27,0,0)\),
\(\delta=(-21,0,0)\), with the same
integer A. These values come from
the matched full connections and
the actual quaternion product; no
integer is chosen from a residue.

Finally the directed fan replacements
of OF.4 take place in the selected
source neighbourhood. Their full
common-link maps, normal resets,
prism chains and physical-circle
products are unchanged on replacing
the disjoint infinity cap. Starting
with OC.20, every exact induction
step in OF.4--5 consequently has
the same free data. For every
\(P\in\mathrm{GL}_2(\mathbb Z)\),
put \((x,y)^t=P^{-1}e_2\) and
\(S=x^2+xy+y^2\). The actual
integer obtained by those directed
steps and its physical sphere class
are
\[
 A(P)=-4+\frac32(S-1)-\frac{27}{8}(S^2-1),
 \qquad [\Phi_P]=A(P)\pmod{28}.                        \tag{OC.21}
\]
The complete image and its explicit
primitive fan witnesses are therefore
the sixteen values proved in OF.5.
The maps OC.2--19 provide the missing
comparison from every cap in OC.1
to those already proved fan values.

The entire statement here uses the
chosen common fixed-scalar contraction
range and the full positive source
loop, with its prescribed reference
marking. The M2 progression, other
selected generators and any shorter
endpoint loop remain separate tasks.
The exact certificate and independent
geometric audit are recorded separately
before this working proof is promoted.

## OC.6. Exact record and proof scope

The exact program is
`code/part3_root/e6_order_three_all_caps.py`.
Its JSON preserves the entire rational function OC.9a,
the numerator and denominator of \(\ell\), both
coincident-section graph arrows, the full normalized
chord identity OC.14, the universal root and deck
exponents, both norm signs, the finite character,
the complete sector square and the weighted-norm
identity. It passes 1,087 exact checks. The universal
equations are symbolic in l; the additional regular
graph checks for \(0\le l\le30\) record their primitive
ray matrices without substituting those samples for
the symbolic determinant proof. OC.4--5 supply the
geometric cap product and matched-connection argument;
the certificate does not assert those conclusions
from its finite algebra alone.
