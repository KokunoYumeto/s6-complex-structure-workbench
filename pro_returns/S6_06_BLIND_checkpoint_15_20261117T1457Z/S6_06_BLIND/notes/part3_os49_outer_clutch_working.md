# OS49: the exact outer C2 clutch in the primitive H/K marking

Working scope, 17 November 2026. This note computes the actual outer
transition in the specified primitive H/K six-chart marking. It does
not identify that native edge with the diagonal used by P3K.17, and
assigns no corrected OS49 fan return or characteristic residue.

## OH.1. The retained periods

The actual periods of P3K.34, OC.3, before any proposed whole-plumbing
product, are
\[
 u=(2s,s)^t+U(q),\qquad
 \gamma=(-3s,-s+mv)^t+C(q),\qquad \lambda=r^m,
\]
where \(v=\log r/(2\pi i)\). The primitive periods are literally
\[
 H=-u-\gamma=(s,-mv)^t-U-C,\qquad
 K=3u+2\gamma=(0,s+2mv)^t+3U+2C.
\]
Thus in the same physical \((Z,V)\) characters the complete maps have
the form
\[
 h:(Z,V,q)\mapsto(\kappa qZ,\alpha V,q),\qquad
 B:(Z,V,q)\mapsto(gZ,\eta qV,q),
\]
with scalar windings, on one positive physical \(r\)-loop,
\[
 (\operatorname{wind}\kappa,\operatorname{wind}\alpha,
   \operatorname{wind}g,\operatorname{wind}\eta)
                       =(0,-m,0,2m).                    \tag{OH.1}
\]
The retained source and cap units do not vary with \(r\). The finite
\(d\delta\) character is fixed. This computation does not replace the
actual endpoint-to-initial cap closing by its forward inverse.

## OH.2. The exact outer normal map

In the standard six-chart marking the native fixed-curve second
vertex has base \(\kappa w\), negative normal \(\alpha v\), and
positive normal \((\kappa\alpha)^{-1}u\). The native C2 product has
base \(w\) and normals \((v,u)\). Hence their actual comparison is
\[
 z_2=\kappa^{-1}z_0,\qquad
 (N_{2,-},N_{2,+})
   =(\alpha^{-1}N_{0,-},\kappa\alpha N_{0,+}).       \tag{OH.2}
\]
After conjugating the negative-weight line, its positive-weight
normal determinant is
\[
       \det_+\Gamma=\kappa\frac{\alpha}{\bar\alpha},\qquad
       \operatorname{wind}\det_+\Gamma=-2m.           \tag{OH.3}
\]
The other outer branch map is the identity. A nonvanishing determinant
homotopy on the fixed annulus has equal parameter winding at its two
ends. The two maps just displayed therefore cannot be replaced by
a parameter-independent determinant interpolation. Equal inner
charged-cap gauges do not supply that missing interpolation: (OH.2)
is their required outer overlap, and its winding is retained.

This is the precise test which prevents transferring P3K.62's narrow
whole-I1 comparison to these OS49 period labels. For that whole-I1
comparison both \(\kappa\) and \(\alpha\) are scalar-independent;
equation (OH.1) explicitly computes their different values here.

## OH.3. The local trace arithmetic, with the geometric endpoint still open

For the literal doubled H/K scalar loop the ordinary normal matrices
have determinant winding \(2t\) and first-entry windings \(l_i\), with
\[
                 t=2m,\qquad l=(6m,0,4m).
\]
In the circle-trace computation the C2 ordinary pair is
\((-l_0,l_0-l_2)\); the actual native-to-ordinary boundary map has
pure-left degree \(2t\). Thus the doubled native free pair is
\[
                  (2t-l_0,l_0-l_2)=(-2m,2m).          \tag{OH.4}
\]
The unique half of this pair in the free integer lattice is
\((-m,m)\). Identifying the doubled product with the literal pullback
of the actual single native product remains part of the geometric
comparison below. This arithmetic performs no division in
\(\Theta_7\), and is not assigned to a single physical return here.

The remaining comparison is specific: identify the diagonal and
source/target native products in the P3K.17 actual master-space
boundary with this C2 marking, and retain the forward arrow for each
norm sign. Neither (OH.3) nor the local arithmetic (OH.4) assigns the
oriented global correction before that map is given.

The exact symbolic checks are retained in
\path{code/part3_fourfold/os49_outer_clutch_certificate.py} and its
JSON/output files. Root and blind_control were informed of (OH.1)--(OH.3)
before checkpoint15; no previous archive is altered.

## OH.4. The literal single seam and the labelled two rulings

The ordinary arrow in K34 is explicitly endpoint-to-initial closing
by \(q^{-n}\), for each \(n=\pm1\). Its forward arrow is therefore
\(q^n\). Apply the actual K-period \(B^{-n}\) to return its cell
representative to the initial one. The remaining bounded map is
\[
 E_r(Z,V,q)=(g(q,r)^{-n}Z,\eta(q,r)^{-n}V,q).
\]
On a cut parameter interval take the actual holomorphic-in-q
logarithms and a cutoff \(\chi\) constant zero and one on the initial
and terminal collars. The actual coordinate map
\[
 C_\tau(Z,V,q)=(A_\tau Z,D_\tau V,q),\qquad
 A_\tau=\exp(n\chi\log g),\quad
 D_\tau=\exp(n\chi\log\eta)
\]
satisfies \(C_{\rm end}E_r=1\) on whole collars, with all spatial
and parameter derivatives. It commutes with H, K and the physical
circle. Its vertex maps are exactly
\[
 (a,b,c)\mapsto((AD)^{-1}a,Ab,Dc),\qquad
 (u,v,w)\mapsto(ADu,D^{-1}v,A^{-1}w).
\]
Substitution in all three rows retains each full coefficient
\(\kappa,\alpha,g,\eta\). In particular the C2 row
\((u,v,w)=(a^{-1},ab,ac)\) is parameter-free. This constructs an
actual closed single native C2 product, not a whole-plumbing product.
Its double is the literal pulled-back atlas
\[
 C^{(2)}_{j+\tau}=C_\tau E_{r(\tau)}^{-j},\qquad j=0,1.
\]
Both expressions agree at the middle seam and their derivatives
agree on collars; the terminal map cancels the double forward
arrow after \(B^{-2n}\). Thus (OH.4) is the square of the actual
single native return, and its single free pair is \((-m,m)\).
There is no division of a sphere class in this step.

The source/target ruling can be read directly in K17's original
coordinate order \((z_0,z_4,z_1,z_2)\). The positive auxiliary
moment quotient has \((z_0,z_4)\ne0\) and is the negative-diagonal
fan. On its \(z_4=1\) chart put
\((a,b,c)=(z_0,z_1,z_2)\). On \(z_0=1\) the coordinates are
\((u,v,w)=(a^{-1},ab,ac)\). Consequently this is exactly the first
native C2 ruling. The lifted seam in this original coordinate order is
\[
 (z_0,z_4,z_1,z_2)\mapsto
 ((AD)^{-1}z_0,z_4,Az_1,Dz_2).
\]
It commutes with the auxiliary action and preserves the product
\(q=z_0z_4z_1z_2\). It therefore carries the same common rank-one
matrix locus and the same native boundary map to the second ruling.
The negative auxiliary moment quotient is that second ruling,
with \((z_1,z_2)\ne0\), and is the positive-diagonal fan.

In the conventions of FF.3--4 the common-link map and its oriented
exterior extension are
\[
 (h,q_H)\mapsto(q_H^{-1}h q_H,q_H),\qquad
 (y,q_H)\mapsto(q_H^{-1}y q_H,q_H).
\]
Thus the direction is negative fan to positive fan. The relative
group formula assigns central increment equal to the right free
integer, here \(+m\). The remaining root audit is the retained
K23/FF central orientation and its application to these completed
boundary families. No change has been made to an OS49 numerical
mapping row or manuscript statement in this working note.
