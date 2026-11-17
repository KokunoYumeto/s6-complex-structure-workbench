# The literal primitive-scalar C1 native arrow

Unpromoted consistency calculation, 17 November 2026. This note
uses a concrete primitive scalar family of P3K.22 (for example
P3K.10's OS45 family), not the source-zero family of P3K.60.
It records the complete local arrow which must be compared with
P3K.25's characteristic bordism and P3K.29's initial product.
No earlier proved status is changed by this working note.

## SCN.1. The actual primitive scalar seam

Keep the physical line character \(V\) and the original positive
\(\lambda\)-loop of K22/K25. The full periods are
\[
 h:(Z,V,q)\mapsto(\kappa(q)qZ,\alpha(q)V,q),\qquad
 B:(Z,V,q)\mapsto(g(q)Z,q\lambda\beta(q)V,q),
\]
where all displayed units are independent of the scalar parameter.
Put \(\eta=\lambda\beta\). The primitive cap-to-ordinary gluing of
K10/K22 has the literal forward parameter arrow
\[
                  R_{\rm ord}:(Z,V,q)\mapsto(Z,q^{-1}V,q).
                                                        \tag{SCN.1}
\]
Its cap arrow is the holomorphic unit recorded in K10; the exact
overlap square there is retained unchanged. Reindexing the shifted
cone by the actual period \(B\) gives
\[
                    E_\lambda:(Z,V)\mapsto(gZ,\eta V).
                                                        \tag{SCN.2}
\]
This is the K25.6 endpoint in global torus coordinates; in its
local square coordinates \((Z_{\rm loc},V_{\rm loc})=(Z,ZV)\)
it is \((gZ_{\rm loc},g\eta V_{\rm loc})\).

On a cut scalar interval \(\tau\in[0,1]\), let
\(\lambda=\lambda_*e^{2\pi i\tau}\). Retain the actual logarithms
of \(g,\eta\) on the \(q\)-disc times this interval, and take a
cutoff \(\chi=0\) near the first end, \(\chi=1\) near the last.
Use
\[
 C^{(1)}_\tau:(Z,V)\mapsto(AZ,DV),\qquad
 A=e^{-\chi\log g},\quad D=e^{-\chi\log\eta}.         \tag{SCN.3}
\]
On the terminal collar \(C^{(1)}=E_\lambda^{-1}\), so the
entire seam identity \(C_{\rm end}^{(1)}E_\lambda=1\) holds
with every derivative. These maps preserve \(q\), commute with
both periods and the physical circle, and have the two actual
chart expressions
\[
 (a,b,c)\mapsto((AD)^{-1}a,Ab,Dc),\qquad
 (u,v,w)\mapsto(ADu,D^{-1}v,A^{-1}w).
                                                        \tag{SCN.4}
\]
Substitution in each of DZ.8's three transition rows preserves
every coefficient. Thus these are actual closed vertex charts,
with the original units and forward \(q^{-1}\) arrow.

The doubled seam is specified as the literal pullback
\[
 C^{(2)}_{j+\tau}=C^{(1)}_\tau E_{\lambda(\tau)}^{-j},
                       \qquad j=0,1.                \tag{SCN.5}
\]
Its middle and terminal collar identities are respectively
\(E^{-1}\) and \(E^{-2}\). It has not been independently chosen
from the doubled endpoint.

## SCN.2. The complete native C1 product and Cox lift

In these closed charts the horizontal native star is given by
\[
 (z,n_0,n_1)=(c,a,b),\qquad
 (z',n'_0,n'_1)=(\eta v,g w,(g\eta)^{-1}u).
                                                        \tag{SCN.6}
\]
The full \(C_1\) transition row is
\[
              (u,v,w)=(g\eta bc,\eta^{-1}c^{-1},g^{-1}ac).
\]
Hence (SCN.6) satisfies exactly
\[
                         z'=z^{-1},\qquad n'_i=zn_i.
                                                        \tag{SCN.7}
\]
This is a single native star product with all parameter units
included. On its first chart (SCN.4) acts by
\[
                 (z,n_0,n_1)\mapsto
                    (Dz,(AD)^{-1}n_0,An_1).
                                                        \tag{SCN.8}
\]
On the second it is
\((z',n'_0,n'_1)\mapsto(D^{-1}z',A^{-1}n'_0,ADn'_1)\);
the equality (SCN.7) is retained literally.

For Cox coordinates with auxiliary weights \((1,1,-1,-1)\),
put \(z=a_1/a_0,n_i=a_0c_i\). The lift of (SCN.8) is
\[
 (a_0,a_1,c_0,c_1)\mapsto
       (a_0,D a_1,(AD)^{-1}c_0,Ac_1).                \tag{SCN.9}
\]
It preserves \(q=a_0a_1c_0c_1\), so its inverse has the same
\(q\) and inverse multipliers even for the full \(q\)-dependent
units. It extends through both small resolutions. In this order
the physical circle weights are \((0,1,-1,0)\). The angular
factor of (SCN.9) is the corresponding physical-circle factor;
the inverse direction from K25.7 is retained by (SCN.3).
The native product pulled back under the double parameter cover
is exactly the one using (SCN.5), including (SCN.6).

## SCN.3. The doubled ordinary normal maps and trace degrees

The raw period-unit winding is
\(\left(\begin{smallmatrix}0&0\\0&1\end{smallmatrix}\right)\)
for one positive primitive loop. For two turns, with
\(\lambda=\lambda_*e^{2i\theta}\), the actual based normal
ratios in the second-vertex product
\((u,\eta v,\kappa w)\) are exactly
\[
 K_0=K_2=\operatorname{diag}(e^{2i\theta},1),
 \qquad K_1=\operatorname{diag}(1,e^{2i\theta}).       \tag{SCN.10}
\]
All other units cancel against their identical reference values.
The original higher normal terms are carried by the same
normal-rescaling and cutoff-flow construction as DZ.2. Thus the
closed ordinary product uses
\[
 t=1,\qquad l=(2,0,2),\qquad
 T_i(Q)=H_1 QH_{l_i-1}.
\]
The physical weights remain \(w=(0,1,-1)\),
\(d=(-2,-1,-1)\). Substitution in the literal orbit map DZ.16
and its closed stable derivative gives
\[
                  I=(-2,2,-2),\qquad W=(2,0,0).
                                                        \tag{SCN.11}
\]
The actual capped graph-loop prism and the ambient-frame
comparison then give on \(C_1\)
\[
 V_{11}=2,\qquad\delta_1=-2,\qquad
       2n_1=\delta_1-V_{11}=-4,\qquad m_1=0.
                                                        \tag{SCN.12}
\]
The native-to-ordinary boundary arrow in this star is
\[
                    q_H\mapsto
                   (U H_1U^{-1})q_H H_{-1}.
                                                        \tag{SCN.13}
\]
Its Hopf-oriented left degree is \(+2\), and its right degree
is zero. Extending its inverse by OR.2's actual cylinder map
gives the pure-left endpoint \(L^{-2}\). The doubled native
pair obtained from (SCN.12) is therefore \((2,-2)\).

The product (SCN.5)--(SCN.7) is the literal pullback of the
single native product, so the same fixed-boundary connection
argument of DZ.4 identifies its relative return with \(f^2\).
Its two free coordinates consequently give the single native
pair
\[
                               (m(f),n(f))=(1,-1).
                                                        \tag{SCN.14}
\]
This uses the free coordinates of the actual relative square;
it does not divide a seven-sphere class.

## SCN.4. The exact comparison still to be audited

The local square in K25 is the horizontal star of (SCN.6):
its original edge joins \((0,0)\) to \((1,0)\), and its other
vertices are \((1,-1),(0,1)\). Its characters are precisely
\((Z_{\rm loc},V_{\rm loc})=(Z,ZV)\), as in SCN.1.
Thus (SCN.2), (SCN.8) and (SCN.9) provide the full native
closing dictionary for the stated K25 parameter family.

The relative Cox conjugation used in K23 would attach central
change \(-1\) to (SCN.14), whereas the K25 characteristic
bordism records zero. The map or relative-boundary term
responsible for this difference has not yet been identified.
The two concrete derivations are preserved for root audit.
In particular, K29's passage from K27's fixed-star cusp
product to a delta-equivariant product of the entire
three-curve union must be checked as an actual map; the
fixed-star normal product alone is not that missing map.

This working note is not exported as a theorem. It does not
alter the exact source-zero \(C_2\) comparison of K60, whose
same scalar test gives zero \(C_2\) right coordinate.
