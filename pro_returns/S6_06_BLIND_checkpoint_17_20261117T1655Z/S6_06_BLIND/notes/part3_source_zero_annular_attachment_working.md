# Source-zero E-annulus: the exact component and normal deck

Working attachment record, 17 November 2026. The statements below concern
the actual E annulus and its chain charts. They supply boundary data; they
do not assert that the collision quotient and the cap have been attached
over the central collision point.

## EA.1. The component permutation and its full-cycle representative

Use the notation and actual theta/Cartier maps of K39 Sections 19–22 and
27. Thus (N=km), (n=\pm1), (c=nk), and the changed ordinary line
coordinate is (V_\eta). The positive (q_1)-deck, as an arrow on the
logarithmic base cover, is
\[
 S:(q_1\text{-sheet},V_\eta)\longmapsto
       (q_1\text{-sheet}+1,v^{-c}V_\eta).
\]
On the actual node charts
\[
 X_j=V_\eta/v^j,\qquad Y_j=v^{j+1}/V_\eta,
 \qquad X_jY_j=v,
\]
this is literally
\[
             S:(j,X_j,Y_j)\longmapsto(j-c,X_j,Y_j).       \tag{EA.1}
\]
Both normal coordinates are unchanged after the displayed index change.
This proves that the node components modulo the scalar period (N)
have (k) cycles of length (m), with the sign of (n) retained.

Write the full scalar period as
\[
 g:(Z,V_\eta)\longmapsto(g_ZZ,v^N g_0V_\eta).
\]
It sends chart (j) to chart (j+N), with

\[
        (Z,X_j,Y_j)\longmapsto(g_ZZ,g_0X_j,g_0^{-1}Y_j).
\]
After (m) positive (q_1)-deck arrows the index is (j-nN).
Returning to representative (j) by the *actual* period (g^n)
therefore gives the full-cycle arrow
\[
 C=g^nS^m:(Z,X,Y)\longmapsto
       (g_Z^nZ,g_0^nX,g_0^{-n}Y).                         \tag{EA.2}
\]
This is a forward-deck arrow on the chosen sheet. The
endpoint-to-initial closing in the associated mapping torus is its
inverse. No component reindexing has been discarded.

## EA.2. The central source and normal maps

On (v=0), (0<|T|<\epsilon), the exact central identities already
proved from the chord and Cartier maps are
\[
 P^2Q=1,\qquad h=(Q,P^a),\qquad
 g_Z=P^{-b},\qquad g_0=2(-1)^{b+1}\lambda_0P.             \tag{EA.3}
\]
Here the factor (v^N) has been removed only in writing the node-chart
unit (g_0). The scalar in the actual suspension remains

\[
                         \lambda=v^N\lambda_0.
\]
For (a=1,b=2), (EA.2) has source multiplier (P^{-2n}=Q^n).
Dividing by the literal source period (h^n), whose line multiplier
is (P^n), gives
\[
 C_{\mathrm{good}}:(Z,X,Y)\longmapsto
       (Z,(-2\lambda_0)^nX,(-2\lambda_0)^{-n}Y).          \tag{EA.4}
\]
For (a=2,b=1), the actual central line is trivial on this punctured
annulus in the frame (ZV_\eta): its factor under (h) is

\[
                            QP^2=1.
\]
Accordingly put (\widehat X=ZX),

\[
 \widehat Y=Z^{-1}Y,\qquad \widehat X\widehat Y=v.
\]
Then the same arrow is
\[
 C_{\mathrm{red}}:(Z,\widehat X,\widehat Y)\longmapsto
       (P^{-n}Z,(2\lambda_0)^n\widehat X,
                         (2\lambda_0)^{-n}\widehat Y).   \tag{EA.5}
\]
The source multiplier (P^{-n}) is the marked nonzero two-torsion
translation. Its square is (P^{-2n}=Q^n), an actual source period.
It is not itself a source period: the already established asymptotics

\[
               P\sim16/T,\qquad Q\sim T^2/256
\]
give the half-period valuation. Thus the reduced full-cycle arrow retains
an actual source translation, even though its displayed normal units
are constant.

Equations (EA.4) and (EA.5) retain the full central units, not only their
winding numbers. In particular the positive-weight normal determinant
gets the unit (c/\bar c) for the displayed constant (c), after
conjugating the negative-weight coordinate. This statement does not
choose a logarithm across (T=0).

## EA.3. The Cartier class and the remaining cap comparison

The flat frame (ZV_\eta) in (EA.5) is used only on the punctured
annulus. The source calculation of K39 Section 2 identifies the full
central Cartier line for (a=2) with (O(C_0)), and for (a=1)
with (O(G_0-O)), whose component degrees on ((C_0,C_1)) are

\[
                          (-1,+1).
\]
Consequently the punctured trivialization in (EA.5) is not declared to
extend as a nowhere-zero section across the (I_2) fibre. The vertical
Cartier divisor remains part of the attachment.

The finite cap has the actual generator

\[
 A=v^{kn}r_0^nA_0,\qquad A_0^m=B_0^n,
\]
and the ordinary-to-cap map is the full (F_0) fixed in RCZ.5–7,
after the explicitly displayed changed origins. It identifies the
forward (q_1)-deck with the inverse cap-root arrow, including the
source translation and the line character. It therefore transports
(EA.2) to the cap frame with its full source/line cocycle. No assertion
that this transported frame extends across (T=0) follows from the
constant normal units in (EA.4)–(EA.5).

For the good branch, the chosen division representative

\[
 R=(QP^2)^{1/m}
\]
and the identity-component representative (R_I=P^{2/m}) on a strict
I chart differ by (Q^{1/m}). Their (m)-norms differ by the source
period (Q), including its actual line factor (P). The alternative
strict-I representative has no component translation there, but using
it in the cap requires an actual affine source conjugacy and its line
lift, with the integral annular cochain carried. The finite-cap
equation to solve is the explicit one from AE.1–4:

\[
                       (1-D)T=Z,
\]
where (Z) is the exact difference of the two affine translation
terms and has zero *cyclic* norm. A pointwise (m)-division identity
alone does not establish that cyclic-norm condition. This is the next
comparison being computed, and no global filling or numerical return
is assigned in this record.

The finite exact certificate is
\path{code/part3_fourfold/source_zero_e_annular_deck.py}; it checks both
signs, the component cycles, the full-period reindexing and the two
central normal-unit cancellations.

## EA.4. The primitive chamber map on the actual finite cap

Here the primitive map is the *negative* source translation of SZ.7:

\[
 U_1:(p,w)\longmapsto(p-G,w/X(p-G)).
\]
For (a=2), retain the actual Cartier map

\[
 r(p)=X(p-G),\qquad
 r:O(2G-O)\longrightarrow O(G-O)^{\otimes2}.
\]
The primitive map in the original line is therefore

\[
 U_2^{\rm Cartier}=r_{\rm target}^{-1}
              U_2^{\rm tensor}r_{\rm source}.            \tag{EA.6}
\]
It is (EA.6), rather than an unlabelled tensor-power frame, that is
carried to the cap. In the common Cox coordinates of SZ.14–15 every

\[
                         U_a: \text{t-ruling}\longrightarrow
                                      \text{s-ruling}
\]
is the identity on the common nonzero coordinate (V). This is the
inverse direction to K23's s-ruling-to-t-ruling map

\[
                 \tau(h,q_H)=(q_H^{-1}h q_H,q_H).
\]
The degree-two case retains the actual residual (\mu_2) and line
charge two.

Write (q_\infty=z^m) on the cap and

\[
 q=q_\infty^{-1}h,\qquad h=1-T_0(v)q_\infty.
\]
There is the following literal normalization of the primitive lift:

\[
  U_{\rm cap}=z^{-ma/2}U_a^{\rm Cartier},\qquad
  B=2(-1)^{b+1}\lambda h\,U_{\rm cap}^{b},\qquad ab=2.
                                                               \tag{EA.7}
\]
The exponent (ma/2) is an integer in each admitted branch. To
verify the extending map, first take the good branch (m=4p,a=1).
The actual root coordinates have (X=z^{-2p}X'). Thus the primitive
target multiplier (1/X) is exactly (z^{2p}/X'). The root map

\[
        (p,w)\longmapsto(p-G',w/X'(p-G'))
\]
is an extending isomorphism of the actual degree-zero root line:
its horizontal divisor is the same Cartier identity as SZ.7, and at
the smooth central root fibre its generic coefficient is a nonzero
unit, so its possible whole-fibre divisor has coefficient zero.
This proves the first equality of (EA.7) in the good branch.

For the reduced branch (b=1,a=2), use (EA.6) before passing to the
actual corrected root line. The already constructed root suspension
is an everywhere invertible map (B_0); its full coefficient in
SZ.12 is retained. Since (h) is an extending nonzero unit,

\[
                        U_{\rm cap}=B_0/(2h)              \tag{EA.8}
\]
is an extending source/line map. Comparing with the exact ordinary
identity (B_0=2qU_2^{\rm Cartier}) gives

\[
                        U_{\rm cap}=z^{-m}U_2^{\rm Cartier}.
\]
This is the reduced equality in (EA.7). It incorporates the actual
Cartier correction (EA.6) and the already constructed reduced III root
line. No coefficient on an uncorrected tensor frame is used as its
extension. The earlier unused raw tensor-coefficient display is preserved
in the attempt record and is withdrawn from this comparison.
Finally (z^{mab/2}=z^m=q_\infty), so multiplying by the actual
selected factor (q) proves the second equality of (EA.7) with the
unit (h), rather than with a discarded base power.

The actual finite character is also determined. On the good root the
canonical deck sends (X'\) to (-X'), and preserves the marked
source divisor. Consequently

\[
 D U_{\rm cap}D^{-1}=-U_{\rm cap}.
\]
The translation lift in (A_0) commutes with (U_{\rm cap}) by the
literal constant-factor presentation of a degree-zero elliptic line.
The equality extends over the root line. Hence

\[
              U_{\rm cap}A_0U_{\rm cap}^{-1}=-A_0
                    \quad (a,b)=(1,2).                   \tag{EA.9}
\]
Equivalently the first primitive step carries the finite delta
character (d\) to (d+m/2); the second returns to (d).
On the reduced cap, (EA.8), the exact norm relation and the
deck-invariance of (h) instead give

\[
                 U_{\rm cap}A_0=A_0U_{\rm cap}
                    \quad (a,b)=(2,1).                   \tag{EA.10}
\]
Both statements retain (n=\pm1) and every original finite delta
character. Multiplication of (A_0) by the rescaled parameter factor

\[
                              v^{kn}r_0^n
\]
does not change either commutator.

On the chosen root sheet the full annular Cartier map carries

\[
            U_a^{\rm Cartier}\longmapsto z^{ma/2}U_{\rm cap}.
\]
Its root-deck character cancels exactly: in the good branch both

\[
                         \zeta_m^{ma/2}\quad\text{and}\quad -1
\]
are (-1), and in the reduced branch both characters are (1).
The translation part of the full (F_0) commutes with the displayed
primitive lift in the actual degree-zero-line group. Thus this is a
literal annular comparison with the full root/line map, not only a
comparison of source points. After (b) steps it is exactly the
actual suspension in (EA.7).

In particular, in the reduced branch the forward suspension retains
one t-ruling-to-s-ruling arrow; the cap inserts no second ruling
change. The inverse suspension has the opposite arrow. The
identification of this arrow with the oriented residual stable end of
the real collision bordism is still a separate map. No characteristic
number is inferred here solely from the number of primitive factors.

## EA.5. The finite stable-end metric arrow and its fixed boundary

This section works with a fixed nonzero scalar, chosen small after the
compact source-origin neighbourhood has been cut out. It does not use the
nonproper infinite central quotient from SZ.29. On the compact exterior
the actual source/line multiplier is bounded, so this scalar gives a
uniform finite contracting cut. The selected divisor is retained by its
node charts, rather than by a limit of a zero scalar in one chart.

For the reduced primitive period write the nonzero constant as
\(c_\lambda=2\lambda\). The actual arrow is
\[
 (p,w)\longmapsto(p-G,c_\lambda q\,\rho(p)w),
\]
where \(\rho\) is precisely the Cartier line arrow (EA.6). On the
logarithmic Tate chain put
\[
 U_j=\frac{w}{c_\lambda^j q^j},\qquad
 V_j=\frac{c_\lambda^j q^{j+1}}w,
 \qquad U_jV_j=q.
\]
The period sends \(j\) to \(j+1\) and
\[
 (U_j,V_j)\longmapsto(\rho U_j,\rho^{-1}V_j).
 \tag{EA.11}
\]
In the common Cartier/Cox line frame, \(\rho\) is the identity
arrow between the two source rulings. Thus its node extension is
literally the associated chart \(UV=S_0T_0\), with the weights in
SZ.28. The factor \(q\) has been removed by the stated chain-index
change, not by a limiting argument. The two finite cap arrows in
EA.4 still accompany this chart.

Here is the needed change of the finite cut hypersurfaces on the stable
locus. Let \(\xi\) be the common line coordinate of auxiliary weight
\(a\), with \(s\) of weight \(+1\) and \(t\) of weight \(-1\).
The actual Fubini--Study divisor metrics give
\[
 N_t=|\xi|\,\|t\|^a,\qquad
 N_s=\frac{|\xi|}{\|s\|^a},\qquad
 R=\|s\|\|t\|,\qquad N_t=R^aN_s.
 \tag{EA.12}
\]
These are auxiliary-invariant functions. The arrow from the domain end
\(H_t=\{N_t=1\}\) to the target end \(H_s=\{N_s=1\}\) is the
physical positive rescaling
\[
 (\xi,\xi_{\rm dual})\longmapsto
 (R^a\xi,R^{-a}\xi_{\rm dual}).
 \tag{EA.13}
\]
It preserves the product \(\xi\xi_{\rm dual}=q\), the source
coordinates and the physical circle. On \(R\ge\varepsilon>0\)
it is smooth and bounded and extends both node branches. At
\(R=\varepsilon\) its factor is the constant
\(\varepsilon^a\). Only after (EA.13) is the auxiliary positive
normalization used to choose a representative. Auxiliary normalization
alone does not change (EA.12), and was not an end-to-end map.

On the reduced moment graph of RT.8,
\(\mu_{\rm aux}+K\mu_\delta=c\), with \(K,c>0\), the derivative
along the positive auxiliary orbit has the five coefficients
\[
             1,\quad1,\quad1,\quad1+K,\quad4+2K.
\]
It is therefore strictly positive away from the origin. The unique
normalizing arrow is smooth on the displayed stable overlaps and
preserves the full functions \(q,v\), because they are auxiliary
invariants. The actual cap metric is transported by \(U_{\rm cap}\);
on the overlap it is joined to (EA.12) by the logarithm of the positive
metric ratio. Averaging that real function over the finite root group
makes the interpolation equivariant and retains its original character.

The inner boundary also meets the fixed surface. In the positive node
chart it is
\[
 z=V=0,\qquad (S_0,S_1,T_1)/\mathbb C^*,
 \qquad \text{weights }(1,1,-1).
\]
The invariant radius on this surface is
\(R=\|(S_0,S_1)\||T_1|\). Its level \(R=\varepsilon\) is the
circle bundle of \(O(-1)\), with the following literal \(S^3\)
coordinate. Use the unique positive auxiliary gauge \(\|S\|=1\),
write \(T_1=\varepsilon e^{i\phi}\), and set
\[
                  p=e^{i\phi}(S_0,S_1)\in S^3.
 \tag{EA.14}
\]
The positive-weight spinor is \((z,\overline V)\). In this same
gauge its actual boundary frame is
\[
 \left(e^{i(a-1)\phi}z,e^{ia\phi}\overline V\right).
 \tag{EA.15}
\]
Before positive normalization the first component is
\(T_1^{a-1}z/\varepsilon^{a-1}\), and the second is
\(\|S\|^{2a}T_1^a\overline V/\varepsilon^a\).
The displayed positive factor in the second component is required for
full auxiliary invariance; no phase has been suppressed.

Consequently the inner end is not identified here with the bare ruling
mapping torus. Its stable portion has the precise (EA.13) arrow and
the ruling change of EA.4, while its fixed portion has the \(S^3\)
and normal frame (EA.14)--(EA.15). The remaining construction is the
actual surgery joining those two portions, with its boundary orientation.
No individual source-zero return follows from (EA.11)--(EA.15) alone.
The certificate \path{code/part3_fourfold/source_zero_cap_end.py}
checks the admitted finite characters and the exact metric/frame weights.

## EA.6. The reduced positive moment model as an actual bundle

For \(a=2\), the positive auxiliary coordinates of the associated node
chart are \((S_0,S_1,z)\), each of weight one. The negative coordinates
\((T_1,V)\) have weights \((-1,-2)\). The strict derivative in EA.5
shows that the level \(\mu_{\rm aux}+K\mu_\delta=c>0\) meets each
positive-stable auxiliary complex orbit exactly once modulo its compact
circle. It therefore has the literal smooth quotient map to
\[
 \operatorname{Tot}\bigl(O(-1)\oplus O(-2)\longrightarrow
                         \mathbb P^2_{[S_0:S_1:z]}\bigr).
 \tag{EA.16}
\]
Its physical action is the one induced by weight one on \(z\), weight
minus one on \(V\), and weight zero on the remaining coordinates. This
keeps the fixed \(O(-1)\) surface over \(z=0\) and the isolated point
\([0:0:1]\), rather than replacing them by a putative free end.

In the exact node-adapted source coordinates, \(q_1-q_2=v u_v(v)\),
where \(u_v(0)\ne0\). The parameter change
\(\widetilde v=v u_v(v)\) is an actual biholomorphism of discs.
On (EA.16) its map is
\[
                    \widetilde v=S_0zV-S_1T_1.
 \tag{EA.17}
\]
The two coefficients of the two fibre coordinates vanish together only
at \([1:0:0]\) and \([0:0:1]\). In each corresponding affine base
chart, (EA.17) is exactly a nondegenerate four-variable form
\(xw-yz\). Thus both critical points and their actual circle actions
remain explicit. The physical fixed surface meets the first of these
points; the second is the isolated fixed point.

The compact radial link of the zero section in (EA.16) is
\(S(O(-1)\oplus O(-2))\). Its \(S^3\)-bundle Gysin sequence gives
\(H^4\cong\mathbb Z/2\), because the Euler class is \(2h^2\).
The total bundle has \(c_1=0\) and \(p_1=8h^2\), directly from
\(TP^2\oplus O(-1)\oplus O(-2)\). These are invariants of this
specified local bundle and link. The link has not been identified with
the global residual boundary of the completed source family; in
particular no choice of the remaining common order-two return is made
from these numbers.

The distinction is visible in the actual functions. On the charge-one
chart \(z=1\), the old source-product radius is
\[
 R^2=(|S_0|^2+|S_1|^2)(|V|^2+|T_1|^2),\qquad
 q=S_0V,\qquad\widetilde v=S_0V-S_1T_1.
\]
This radius vanishes along the entire fibre over \([0:0:1]\),
including its nonzero points. Its level is therefore not the radial
disk-bundle boundary in (EA.16). A separate compact charge-one
truncation and its actual end map remain to be attached; the disk-bundle
surgery calculation in RT.10 has not been substituted for that map.

## EA.7. Two exact source norm sections, with their scope retained

The following are additional source maps; they have not been supplied
with a completed nonzero-line quotient at the selected cusp. Put
\(T_0=v^2-2v\) and make the root \(q=z^{-m}\).
For the fourth root, the minimal source equation is
\[
 Y^2=X^3+(1-2v)z^2X^2+(1+T_0z^4)X+v^2z^6.
\]
With its actual source deck \(D:(X,Y,z)\mapsto(-X,-iY,iz)\),
the section
\[
                 S=(vz^2+i,iz)
\]
satisfies \(S+D S=G\) and \(D^2S=S\). Its cyclic norm is
therefore \(2G\). The identity is the literal chord addition formula:
the slope between \((vz^2+i,iz)\) and \((vz^2-i,-iz)\) is \(z\),
and their sum is \((0,vz^3)\).

For the third root the minimal equation is
\[
 Y^2=X^3+(1-2v)z^2X^2+(z+T_0z^4)X+v^2z^6.
\]
Its source deck is \(D:(X,Y,z)\mapsto(\zeta_3^2X,Y,\zeta_3z)\).
Choose the holomorphic branches
\(\rho^2=1+v,\rho(0)=1\) and \(E^3=1+\rho\). Then
\[
       S=(vz^2+E^2z,\ \rho E^2z^2+Ez)
\]
is an exact section with cyclic source norm \(G\). To verify the
norm directly, put \(A=v,t=E^3\). The three orbit points lie on
\[
 y=\frac{x^2}{tz}+\frac{t^2-3A}{2t}zx-vz^3.
\]
Substituting this parabola in the cubic gives the four intersections:
the three displayed orbit points and \(-G\). The two coefficient
identities are
\[
 A^3-vt(t^2-3A)-T_0t^2=0,
\]
\[
 t^4-6At^2-3A^2-4t^2+8vt^2-8vt=0.
\]
Both follow exactly from \(A=v\), \(t=1+\rho\),
\(\rho^2=1+v\). The exact substitutions and the norm polynomial are
executed in \path{code/part3_fourfold/global_cap_norm_sections.py}.

These maps give source affine norm data on the indicated root family.
The full invariant Cartier lift, its annular line cochain and the
protected multiplicity-one cusp have not been constructed from these
sections. The earlier multiplicity obstruction in SZ.27 applies to its
specified fractional-period quotient; it has not been asserted for an
unconstructed quotient using these new sections. No completed-family
or return conclusion is drawn here from the source norm identities.

## EA.8. A normalization-stratum unit for the remaining labelled end map

On the selected nodal stratum \(q_1=0\), with \(v\ne0\), the Tate
parameter is \(Q=0\). Use its marked lift \(P=P_G\) and put
\(\zeta=Z/P\), so the marked section is \(\zeta=1\). The exact
theta quotient restricts to
\[
       f_P(Z)=\frac{1-\zeta}{1-P\zeta}.
\]
In the divisor chart whose marked equation is \(1-\zeta\), the
actual degree-\(a\) line coefficient is consequently
\[
       \xi=(1-P\zeta)^a V,
\]
up to the fixed nonzero constant used in that divisor equation. This
is an equality of the meromorphic Cartier coefficients, since the
canonical meromorphic coefficient is \(V/f_P(Z)^a\). Near the
selected node \(\zeta=0\) this is a unit with constant value one.
The source scaling still contains the exact lift
\(P=q_2^{-1}u_P\), whose source-parameter winding is minus one.

This calculation is only on the displayed nodal normalization. The
full bidisc map to the chosen Morse coordinates must retain the
convergent Tate node map, the actual Cartier divisor image, and its
two branch charts. It is not yet an identification of the radial
model's outer family with the requested periodic fan. In particular
the selected-node value of this unit does not remove the source
scaling \(P\) from the completed cap/endpoint map.
