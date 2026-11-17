# OS49 native C2 trace and directed comparison

Working calculation for audit, 17 November 2026. The full
source, line, seam, ruling and Cox arrows are also retained in
fourfold's notes/part3_os49_outer_clutch_working.md, OH.4.
No numerical mapping or manuscript statement is promoted here.

## OCN.1. The exact input and actual relative square

K34's physical periods are
\[
 u=(2s,s)+U,\qquad \gamma=(-3s,-s+mv)+C,\qquad\lambda=r^m,
\]
where \(m=3k>0\). Their primitive basis is
\[
 H=-u-\gamma=(s,-mv)-U-C,\qquad
 K=3u+2\gamma=(0,s+2mv)+3U+2C.
\]
Thus, in the literal H/K characters,
\[
 H:(Z,V)\mapsto(\kappa qZ,\alpha V),\qquad
 K:(Z,V)\mapsto(gZ,q\eta V),
\]
with actual positive-r windings
\[
              (\operatorname{wind}\kappa,\operatorname{wind}\alpha,
                \operatorname{wind}g,\operatorname{wind}\eta)
                         =(0,-m,0,2m).
\]
K37 specifies \(q^{-n}\), \(n=\pm1\), as the closing
endpoint-to-initial arrow. The forward arrow is \(q^n\).
Reindexing by \(K^{-n}\) leaves
\(E_r=(g^{-n}Z,\eta^{-n}V)\). The cut seam
\[
 C_\tau=(AZ,DV),\qquad
 A=e^{n\chi\log g},\qquad D=e^{n\chi\log\eta}
\]
satisfies \(C_{\rm end}E_r=1\) with all derivatives.
It commutes with every actual period and physical delta.
Its two vertex-chart maps are
\[
 (a,b,c)\mapsto((AD)^{-1}a,Ab,Dc),\qquad
 (u,v,w)\mapsto(ADu,D^{-1}v,A^{-1}w).
\]
The fixed extra delta character commutes and is retained.
The double seam is the literal pullback
\(C^{(2)}_{j+\tau}=C_\tau E_r^{-j}\), \(j=0,1\).

The native diagonal star is exactly
\[
 (z,n_0,n_1)=(a,b,c),\quad
 (z',n'_0,n'_1)=(u,v,w),\quad z'=z^{-1},\quad n'_i=zn_i.
\]
On the doubled parameter loop, the actual normal ratios in
the second vertex product \((u,\eta v,\kappa w)\) give
\[
 t=2m,\quad l=(6m,0,4m),\quad
 w=(0,1,-1),\quad d=(-2,-1,-1).
\]
The closed ordinary product \(Q\mapsto H_tQH_{l_i-t}\),
with the complete unit and higher-normal rescaling,
therefore has the exact orbit/derivative degrees
\[
 I=(-8m,4m,-4m),\qquad W=(8m,0,0).
\]
The actual prisms give \(V_{22}=4m,\delta_2=8m\).
Hence its ordinary C2 pair is \((-6m,2m)\).
The native-to-ordinary boundary map
\[
           q_H\mapsto(UH_{2m}U^{-1})q_HH_{2m}
\]
has left degree \(4m\), right degree zero. Its inverse
cylinder extension has endpoint \(L^{-4m}\). The native
doubled pair is consequently \((-2m,2m)\).

Because the product and seam above are literally pulled
back from the single native product, this is the free
pair of the actual relative square. The single pair is
\[
                              (-m,m).
\]
This uses only injectivity of doubling in the two free
integer coordinates, not division in \(\Theta_7\).

## OCN.2. Ruling and orientation of the actual flop

In K17's order \((z_0,z_4,z_1,z_2)\), the positive
auxiliary moment is the first ruling on \([z_0:z_4]\),
explicitly the negative-diagonal fan with common edge
\(u_1u_2\). Its chart \(z_4=1\) has
\((a,b,c)=(z_0,z_1,z_2)\); the chart \(z_0=1\) has
\((a^{-1},ab,ac)\). This is the native C2 star above
with its original complex orientations. The second
ruling, the negative moment, is the positive-diagonal
fan with edge \(u_0u_4\).

The literal full Cox seam is
\[
 (z_0,z_4,z_1,z_2)\mapsto
       ((AD)^{-1}z_0,z_4,Az_1,Dz_2).
\]
It fixes \(q=z_0z_4z_1z_2\), has its displayed inverse
at the same q, and extends through both rulings.
Transporting the metric and positively normalizing
the radius retain the bounded moduli. The unrestricted
four-weight identity gives the actual common-link and
oriented exterior maps, in the negative-to-positive
direction,
\[
 \tau(h,q_H)=(q_H^{-1}h q_H,q_H),\qquad
 T(y,q_H)=(q_H^{-1}yq_H,q_H).
\]
All source/cap maps outside the star are unchanged.
The first-resolution complex-normal reset preserves
the central coordinate. Therefore the actual
conjugation is
\[
 T(L^\mu R^\nu\mathcal C^s)T^{-1}
       =L^{-\nu}R^{\mu+2\nu}\mathcal C^{s+\nu}.
\]
The directed comparison from the computed native pair
is
\[
                  s_{\rm positive}-s_{\rm negative}=m.
\]
Together with the independently constructed positive-
diagonal zero index, this records the working negative-
diagonal class \(-m\bmod28\), pending root audit.
Both norm signs use the same positive-r unit winding.
No other-fan or shorter-loop value is assigned.

The old zero-correction step also fails its actual
outer marking test. The second C0-to-C2 arrow is
base \(\kappa^{-1}\), normal
\(\operatorname{diag}(\alpha^{-1},\kappa\alpha)\).
Its positive-Hopf determinant has winding
\(\operatorname{wind}\kappa+2\operatorname{wind}\alpha=-2m\).
Thus K62's scalar-independent outer comparison does
not apply to this OS49 H/K input.

