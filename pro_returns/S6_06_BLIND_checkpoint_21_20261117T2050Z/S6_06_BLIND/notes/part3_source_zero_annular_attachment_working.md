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

## EA.9. The actual cyclic graph reset and its charged-chart continuation

The common graph identity of EA.4 does not identify consecutive graph
coordinates. Here is the missing reset, with its line map. Use the
marked source-resolution coordinates
\[
 A=Dz_s,\quad C=Bz_s,\quad
 v=(B-Dz_s)/2,\quad X=Bz_s,
\]
and set
\[
 F_2=1-Bz_s^3-(1-2v)z_s^2.
\]
The next negative-G translation has the exact source coordinates
\[
 X'=F_2/z_s^2,\quad A'=-F_2/z_s^3,\quad
 B'=B-Dz_s-F_2/z_s^3,\quad D'=-B'/z_s.
 \tag{EA.18}
\]
They satisfy \(A'B'=X'D'\), preserve \(v\), and preserve the full
source base coordinate
\(T=D-X^2-(1-2v)X\). In the next common Cox gauge take
\[
 (\widetilde t_0,\widetilde t_1)=(1,-z_s),\qquad
 (\widetilde s_0,\widetilde s_1)=(A',D').
 \tag{EA.19}
\]
In the current target gauge \((s_0,s_1)=(z_s,1)\), the meromorphic
line coefficient is \(\xi/z_s^a\). In the next domain gauge it is
\(\widetilde\xi(-z_s)^a\). Therefore the exact coefficient arrow is
\[
            \widetilde\xi=(-1)^a z_s^{-2a}\xi.
 \tag{EA.20}
\]
For the actual reduced line, this reads
\(\widetilde\xi=\xi/z_s^4\), after the retained Cartier map
\(r\) at both ends. Equations (EA.18)--(EA.20) give the reset,
rather than replacing it by the bare projective ruling.

Its effect on the associated-node chart is already nontrivial on the
central proper component. Write
\[
 X=s^2-1,\quad Y=s(s^2-1),\quad z_s=1/s,\quad
 B=s(s^2-1),\quad D=s^2(s^2-1).
\]
Near its \(s=-1\) node, the analytic square root in RT.2 is
\(\sigma=-s\). Substitution in the literal functions
\[
 F_+=\frac{(\sigma+1)(s_1-s_0)
                -s_0^2(t_0+t_1)/(\sigma+1)}2,
\]
\[
 F_-=\frac{(\sigma+1)(t_0+t_1)
                -t_1^2(s_1-s_0)/(\sigma+1)}2
\]
gives \(F_+=2,F_-=0\). Thus the finite associated coordinate
\(z_n=\xi/F_+\) is nonzero. At the next target, (EA.18) has
\(\widetilde s_0=\widetilde s_1=0\), whereas
\(\widetilde\xi=\xi s^4\ne0\). Its analytic square root has
value one, and
\[
             \widetilde F_+=0,\qquad
             \widetilde F_-=1-1/s.
\]
Consequently \(z_n\) goes to infinity. The reset enters the
complementary \(U\ne0\) charge-a chart. It does not close inside
the finite nonzero charge-\((a-1)\) chart. This is the exact reason
the Euler sequence \(2M\oplus2M^{-1}\) from that chart alone has
not been descended over the entire cyclic end.

There is nevertheless a literal continuation from the resulting
charged chart. Use the complementary small-resolution equations
\[
                  S_0=Uw,\qquad V=wT_0.
\]
In its \(U=1\) gauge the remaining coordinates are
\((w,S_1,T_1,T_0)\), and the full source functions from RT.2 are
\[
 q=wT_0,\qquad
 v=S_1T_1+\frac{T_1w-S_1T_0}{2\sqrt{1+S_1T_1}}.
 \tag{EA.21}
\]
The primary \(V=1\) chart has coordinates
\((S_0,S_1,T_1,z_n)\). Its source functions are exactly (EA.21)
under
\[
                (S_0,S_1,T_1,z_n)=(w,S_1,T_1,T_0).
 \tag{EA.22}
\]
This map has a specific chain meaning. On \(U_j\ne0\), the
actual adjacent node overlap is
\[
 U_{j-1}=c_\lambda qU_j,\qquad
 V_{j-1}=(c_\lambda U_j)^{-1},\qquad c_\lambda=2\lambda.
 \tag{EA.23}
\]
At \((U_j,V_j)=(1,q)\), apply the retained source-fibre scalar
normalization \((U,V)\mapsto(c_\lambda^{-1}U,c_\lambda V)\).
The result is \((q,1)\), precisely (EA.22). Thus this is a node
chart overlap with index \(j\mapsto j-1\), not an additional
cap or an extra charged point. In a forward B cut its index cancels
the preceding \(j\mapsto j+1\) in (EA.11). In particular the
charged origin in these two descriptions is one point, and must
not be counted twice.

Both gauges retain the same effective physical weights, in the
ordered coordinates of (EA.22),
\[
                   (-1,-1,+1,+1)/a,
\]
and the same residual \(\mu_a\) action. The displayed coordinate
arrow is complex linear on these charged coordinates and preserves
their real eight-dimensional orientation. Conjugating its two
negative physical-weight coordinates gives the same positive Hopf
projection at both ends. Its physical line is \(O(-a)\), with
the outward-meridian dual \(O(a)\). A charged ball is carried by
(EA.22), with this full normalization retained; its transported
truncation is used if the original radii differ. This fixes the
boundary orientation against the local charged model of RT.10.

The source functions \(q,v\) in (EA.21) are unchanged throughout.
On the finite cap, (EA.7)--(EA.10) carry the same primitive map,
including \(q=q_\infty^{-1}h\), the actual \(z_\infty^m\)
factor in the reduced line, and its trivial commutator with
\(A_0\). The physical normalization in (EA.23) commutes
with this full root/line square. Both norm signs and every retained
finite character remain.

This supplies the cyclic chart transition and its local charged
orientation. The compact radial-to-product-radius cobordism and its
complete global attachment are still being constructed. No individual
source-zero return is assigned by counting the charts in this section.
The exact source, line, and charged-chart identities are executed in
\path{code/part3_fourfold/source_zero_associated_reset.py}.

## EA.10. The retained scalar winding in the adjacent-node arrow

The finite-cut construction in EA.5 starts at fixed nonzero
\(\lambda\). For the original rescaled source loop, the exact same
overlap has
\[
 c_\lambda(v)=2\lambda_0v^{km},\qquad
 (U,V)\longmapsto(c_\lambda(v)^{-1}U,c_\lambda(v)V).
 \tag{EA.24}
\]
Thus its two characters have source-parameter windings \(-km\)
and \(+km\). This map is not asserted to extend at \(v=0\) in
those old coordinates. Its full collar derivative is retained: it is
the diagonal character map followed by a rank-one factor
\(I-\eta\otimes d\log c_\lambda\), where \(\eta\) is the
physical complex orbit field and
\(d\log c_\lambda(\eta)=0\). The latter factor is invertible
through the explicit homotopy
\(I-t\eta\otimes d\log c_\lambda\); the diagonal character and
its winding are not removed by this homotopy.

The comparison with a fixed-scalar boundary uses the actual two-parameter
family, not an extension of (EA.24). Write \(\lambda=r^m\). Its
cap generator is \(A(v,r)=r^nA_0(v)\), and the ordinary-to-cap
map on the logarithmic r cover is
\[
 F(v,\nu)=F_0(v)+n\nu s_\infty\delta,\qquad
 \nu=\log r/(2\pi i).
\]
Here \(F_0(v)\) is the complete extending annular map of RCZ.5--7,
with its integral cochain fixed at the reference fibre. The positive
r deck has the full arrows \(q_1^n\) and \(h^n\), since
\(q_1=q_\infty^{-1}h\), and
\[
          F(v,\nu+1)\,q_1^n=h^n F(v,\nu).
 \tag{EA.25}
\]
The equation retains both norm signs, the fixed finite character,
and every source/line unit. The same source and line Cartier maps
are used over both parameter directions; the base-only physical
scalars commute with them. The cap division and \(F_0\) have their
stated holomorphic source-parameter extensions, so their source-loop
endpoint is retained literally.

On the boundary, \(r=v^k r_0\). In this actual product-parameter
family the diagonal loop is homotopic to the source loop at fixed r
followed by k scalar-root loops at the comparison source. The based
homotopy carries all the endpoint squares (EA.25). Hence its return
class is the fixed-scalar source return plus the actual
\(kA_{\rm scalar}\) term, in the same transported fan. This is
the geometric parameter-loop relation already used in K58; no
class in \(\Theta_7\) is divided. The still-missing compact
fixed-scalar source attachment has not been supplied by this
boundary comparison.

## EA.11. Chamber ownership of the two charged descriptions

The coordinate identification (EA.22) is retained together with its two
auxiliary chambers. For the primary resolution
\(U=S_0z,T_0=zV\), the auxiliary and physical weights on
\((S_0,S_1,T_1,z,V)\) are respectively
\[
 (1,1,-1,a-1,-a),\qquad(0,0,0,1,-1).
\]
For the complementary resolution \(S_0=Uw,V=wT_0\), the weights
on \((U,w,S_1,T_1,T_0)\) are
\[
 (a,1-a,1,-1,-1),\qquad(1,-1,0,0,0).
\]
Thus, for a=2, the primary positive chamber is the actual
\(\operatorname{Tot}(O(-1)\oplus O(-2)\to\mathbb P^2)\)
of RT.9. Its z=1 origin has charge one. The primary V=1 origin
instead lies in the negative auxiliary chamber and has charge two.
The complementary U=1 origin lies in its positive chamber and also
has charge two. Equation (EA.22) identifies the last two charts;
it does not place a charge-two origin in the primary positive chamber.

In either charged gauge, maintaining U=1 or V=1 under the physical
circle uses the auxiliary factor of exponent \(-1/a\). The ordered
remaining coordinates therefore have the same physical weights
\((-1,-1,+1,+1)/a\). Their residual auxiliary \(\mu_a\)
characters agree modulo a. The map (EA.22) is complex linear in
those coordinates, preserves their real eight-dimensional orientation,
and carries the physical line \(M=O(-a)\) literally.

The ungauged continuation, on the complementary chart U nonzero,
is the explicit map
\[
 (U,w,S_1,T_1,T_0)\longmapsto
 (S'_0,S'_1,T'_1,z',V')=(Uw,S_1,T_1,UT_0,U^{-1}).
 \tag{EA.26}
\]
Its inverse is \(U=(V')^{-1},w=S'_0V',T_0=z'V'\), with
S1,T1 unchanged. It preserves the auxiliary action and the physical
circle separately. It also preserves q and the full v in (EA.21).
At U=1 it is exactly (EA.22). It is the adjacent-node arrow with
the full scalar normalization already specified, not the naive
exchange of U and V on the ungauged associated-node space. A
radial defining function on either charged quotient chart can be
transported by (EA.26), with its entire derivative. Choosing the
retained or excised side of that transported function remains part
of the compact-cut construction.

Chamber names alone do not determine the boundary normal. On the
normalized charged gauges the two actual moment functions are
\[
 \mu_{\rm comp}=a+(1-a)|w|^2+|S_1|^2-|T_1|^2-|T_0|^2,
\]
\[
 \mu_{\rm prim}=|w|^2+|S_1|^2-|T_1|^2
                         +(a-1)|T_0|^2-a.
\]
Their sum is
\[
 (2-a)|w|^2+2|S_1|^2-2|T_1|^2+(a-2)|T_0|^2,
\]
and is not identically zero. The sign of a charged boundary in a
compact bordism must therefore be taken from the explicitly retained
or excised ball, with its outward radial normal. It is not obtained
by negating one moment function. These weight and moment identities
are checked in \path{code/part3_fourfold/source_zero_chamber_ledger.py}.

## EA.12. The fixed-scalar exterior and the remaining boundary equations

The scalar split uses the actual basepoint from RT.12:
\(r_{\rm base}=v_*^k r_0\), \(r_0^m=\lambda_0\).
The fixed-scalar piece is studied at \(r=r_{\rm base}\), and the
additional k canonical scalar turns are retained by the explicit
based homotopy in RT.12. A subsequent zero-winding radial change of
the scalar is a separate path in the common contracting range.

Here is the proper exterior available before the inner attachment.
Choose a source-base disc \(|T|<\epsilon\) containing both fibres
which collide at \((T,v)=(0,0)\), and shrink the source-parameter
disc so that their closures stay inside it. On its compact complement,
the resolved marked source, the section G, and the actual Cartier line
are smooth families through v=0. The selected factor q is nonzero
there. Consequently the actual nonzero-line lift B0 is an invertible
line map on this complement. A Hermitian metric on the compact
source complement bounds its norm by one finite constant C. Taking
\(|r_{\rm base}|^m C<1\) makes B a uniform contraction. Its
nonzero-line quotient has a compact fundamental annulus: the region
between a unit norm hypersurface and its B-image. This construction
retains the source boundary \(|T|=\epsilon\), the physical circle,
and the actual B endpoint; no quotient at the colliding source point
is used.

At the finite root cap retain \(A=r_{\rm base}^n A_0\),
\(B=r_{\rm base}^mB_0\), and \(A_0^m=B_0^n\).
Choose integers u,w with \(nu+mw=1\). The literal common generator
\(H=A^uB^w=r_{\rm base}H_0\) satisfies \(H^m=B\) and
\(H^n=A\). Its norm is bounded on the compact resolved root source,
so a further decrease within the same scalar range gives the same
compact fundamental-annulus construction. This applies to both
norm signs. The actual finite character and corrected root line are
carried by H0, not replaced by an unmarked root. The ordinary/cap
overlap is the full F0 of RCZ.5--7. Its lifted source/line maps commute
with B0 and physical scalars, so they identify the two actual quotient
boundaries. This gives a proper smooth exterior over the full v-disc,
with its only new source-base boundary \(|T|=\epsilon\).

For the inner finite strip, write \(J_j\) for the actual associated
node chart at chain label j. The following maps and equations are
already fixed:

1. The forward suspension is the actual map
   \(B_j:J_j\to J_{j+1}\), carrying the source by \(-G\) in
   the reduced branch and the line by its Cartier coefficient. In
   the common graph frame its node coordinates satisfy (EA.11).
2. Between consecutive source graphs the reset is (EA.18)--(EA.20),
   including \(\widetilde\xi=\xi/z_s^4\). This enters the
   complementary positive U=1 chart; it does not remain in the
   primary charge-one chart.
3. The adjacent-node arrow \(J_{j+1}\to J_j\) is (EA.23).
   Its physical normalization at fixed scalar is
   \((U,V)\mapsto((2\lambda)^{-1}U,2\lambda V)\).
   In the charged gauges this is (EA.22), with the chambers in EA.11.
   Thus the U=1 and V=1 descriptions are one charge-a boundary point.
4. The full ordinary-to-cap square on each chosen root sheet is
   \[
      F_0 U_a^{\rm Cartier}
         =z_\infty^{ma/2}U_{\rm cap}F_0,
      \qquad
      F_0B=2(-1)^{b+1}\lambda h\,U_{\rm cap}^{b}F_0.
   \]
   The root character and the good-branch sign cancel as in EA.4;
   the reduced branch commutes. These are equations of actual line
   maps, with \(q=q_\infty^{-1}h\), not merely source-point equations.
5. The full node-to-Tate map being recorded independently carries the
   actual h reindex, \(P=q_2^{-1}u_P\), the theta units and the
   degree-two Cartier map. Its positive associated square is the
   current Tate fan T0. It must be used on the \(|T|=\epsilon\)
   collar rather than the earlier normalization-stratum formula EA.8.

The fixed boundary of the horizontal blowup trace is one S3, with
the precise frame (EA.14)--(EA.15). It is capped once by the stated
\(D^4\times D^4\) handle. The primary positive chamber's charge-one
point and the complementary-positive/primary-negative charge-a point
are distinct strata. The latter has two chart descriptions but one
ownership in the strip. The remaining compact construction must give
the retained and excised sides of these strata explicitly.

In particular, the required final collar equations are the following.
The map from the inner compact cut to the exterior on
\(|T|=\epsilon\) must be the complete node-to-Tate map, commute
with the literal B/adjacent-node composition above, and satisfy the
displayed F0 root square. On the inner fixed collar it must equal
(EA.14)--(EA.15). On the charged collar it must equal (EA.22) with
its full scalar normalization, while carrying an explicitly chosen
radial defining function to a positive multiple of the target radial
defining function. The last condition fixes the boundary normal and
therefore the sign of that component in Stokes' formula.

The compact region between the actual product-radius cut and the
disk-bundle radial cut, together with these collar maps, is still the
remaining global attachment. The local surgery number of RT.10 and
the charge-a Hopf number are not added or subtracted until that
region and its oriented boundary components have been supplied.

## EA.13. Canonical complex spin-c and the explicit determinant lifts

The lower charged arm carries the canonical complex spin-c structure,
with its actual physical associated line. It is not assigned a spin
structure by its rational characteristic classes. In particular, the
two possible lifts over the fundamental group of an RP3 collar are
kept distinct until the actual chart maps have been carried.

There are explicit determinant arrows for those maps. In the source
reset (EA.18), use source coordinates \((B,D,z_s)\) on the first
small-resolution chart, and \((A',D',w')\), \(w'=-z_s\), on
the second. Direct differentiation gives
\[
 \det\frac{\partial(A',D',w')}{\partial(B,D,z_s)}=-1.
\]
Including the exact coefficient (EA.20), with the Cartier r map at
both ends for a=2, the four-dimensional complex Jacobians are
\[
  J_1=z_s^{-2},\qquad J_2=-z_s^{-4}.
 \tag{EA.27}
\]
The determinant square roots used to transport the spin reduction
in these coordinate trivializations are the literal functions
\(z_s^{-1}\) and \(i z_s^{-2}\), respectively. Their inverses
are used on the reverse arrow. These functions retain the full
source winding; no choice of a small logarithm of z_s is made.

For (EA.26), in the displayed ordered five coordinates the complex
Jacobian is the constant -1. The map intertwines the auxiliary
Euler vector field, so contraction of the five-form with that
field gives the same constant -1 on the quotient canonical
four-form. The fixed square root i carries its spin reduction.
On the normalized charged covers, the four-coordinate arrow is
the identity; its residual mu-a character is the one in EA.11.
These two descriptions agree by the actual auxiliary gauge and
its determinant. They do not permit an additional sign character
of the RP3 fundamental group.

More explicitly, on the lower arm the normal bundle is
\((S^3\times\mathbb C^2)/\{\pm1\}\), with the indicated
minus action on both normal coefficients. Its complex determinant
is trivialized by their ordered wedge. The canonical complex
spin-c lift selects a specific spin lift with respect to that
trivialization. With Clifford convention \(e_i^2=-1\), follow
\(\operatorname{diag}(e^{it},e^{it})\), \(0\le t\le\pi\).
Its canonical spin-c endpoint is
\[
 [e_1e_2e_3e_4,-1]=[-e_1e_2e_3e_4,1].
 \tag{EA.27a}
\]
Thus the normal mu2 lift is the specified \(-\omega_4\), not an
arbitrary choice between \(\omega_4\) and \(-\omega_4\).
The other complex two-plane block has the same canonical lift;
their product is \(+\omega_8\), in agreement with the full
charged-cover computation below. Equation (EA.22) is the identity
on these ordered cover blocks. The reset carries their embedded
collars and normal derivative by (EA.27), so this local lift is
transported together with the physical line.

The physical normalization is also carried at the level of its
lift. At a=2, along a chosen path of nonzero scalars d from one
to its actual value, the charged-cover derivative has diagonal
characters
\[
 (d^{-1/2},d^{-1/2},d^{1/2},d^{1/2}).
 \tag{EA.28}
\]
The square roots here are continued along that very path. A full
positive phase turn gives the endpoint -I4. Its canonical complex
spin-c action on \(\Lambda^{0,*}\mathbb C^4\) is
\((-1)^{\deg}\). The determinant-one path in (EA.28), whose
four angles are \((-\pi,-\pi,\pi,\pi)\), has exactly that
spin endpoint: on an occupation vector \((n_1,n_2,n_3,n_4)\)
its sign is
\[
 (-1)^{-n_1-n_2+n_3+n_4}=(-1)^{n_1+n_2+n_3+n_4}.
\]
It therefore closes through the specified canonical residual mu2
action. Replacing the root by its other branch is this same deck
map with this specified lift, not an unrecorded alternative spin
structure. The physical line remains M, not its dual; its charged
Hopf class is \(O(-a)\).

For a nonconstant scalar the full derivative also contains the
rank-one factor in EA.10. Its displayed homotopy is based at the
actual diagonal arrow and carries the chosen lift. The theta and
Morse units in TL.1--2 have extending logarithms on the complete
bidisc; their determinant and line maps are carried by those
logarithms. The actual h period and the Cartier r factors precede
this unit homotopy, so their integral characters are not removed.
On the finite cap the canonical complex spin-c maps are those of
the full root/line F0 square in EA.12; its finite character remains
part of the map.

The exact determinant computations and the sixteen spinor endpoint
checks are in \path{code/part3_fourfold/source_zero_spin_chart.py}.
This fixes the local lift data for the compact attachment. It does
not assert that the still-unassembled compact cut already carries
a global spin filling or select an individual source-zero class.

## EA.14. A full charged shape matching the lower arm

The actual compact comparison region is RT.20, with its two arms
retained. In its lower arm use the primary V=1 gauge and write
\(x=(S_0,S_1,z)\),
\[
 H=\|x\|^2,\quad b=H|T_1|^2,\quad c=H^2,
 \quad u=\frac b{b+c},\quad
 \sigma^2=\|x\|^2+|T_1|^2.
\]
The actual disk-bundle defining function satisfies the exact identity
\[
                  \rho=\sigma^2\sqrt{1-u}.
 \tag{EA.29}
\]
Indeed its square is \(b+c\), and
\(\sigma^4(1-u)=H(H+|T_1|^2)=b+c\).
On the lower small-R arm, u is at most the chosen ratio
\(\varepsilon^2/r_0^2<1/4\). Choose a smooth invariant angular
cutoff chi equal to one on a neighbourhood of that closed arm and
supported in \(u<1/2\). Set
\[
             f=1-\chi(1-\sqrt{1-u})>0.
\]
Then the full charged hypersurface \(\sigma^2f=\rho_0\)
agrees literally with \(\rho=\rho_0\) near the arm. It is a
complete smooth star-shaped hypersurface on the charged cover,
invariant under the residual mu2 and the physical circle. The
normal equality on that neighbourhood is an equality of defining
functions, including their derivatives, not only an equality of
zero sets.

Use the positive-width compact annulus
\[
 \mathcal A_f={\rho_0/2\le\sigma^2\le\rho_0/f\}/\mu_2.
 \tag{EA.30}
\]
It is a smooth interval bundle with disjoint boundary faces. Its
inner boundary is a round charged link; its outer boundary is the
full transported shape. All q and v functions, the physical line,
and the canonical complex spin-c structure are their restrictions
from the actual charged chart. No radial map is asserted to
preserve q or v. The physical circle is free on this annulus:
its nonzero coordinate weights are all plus or minus one after
the retained residual mu2 is accounted for. Product connections
on its collars therefore show that the outer shape and round
charged link have equal physical characteristic integrals.

Equation (EA.26) pulls the entire outer defining function to the
complementary U chart. It transports the outward radial normal
and the retained/excised side exactly, and it carries the lifts
in EA.13. The earlier coincident-face proposal with inner radius
rho0 is not used: (EA.30) uses rho0/2 everywhere, including where
f=1.

This shape comparison still respects the chamber distinction.
The lower arm itself lies in the common stable overlap with the
primary positive chamber. The charge-two origin filling the full
shape belongs to the primary negative chamber. The compact strip
must specify where the complement of the lower arm in this full
shape lies among its boundary faces. The charged shape is not
glued as an additional positive GIT chart. Thus (EA.29)--(EA.30)
fix the radial normal and its spin-c/line data without silently
closing the remaining period-strip boundary.

## EA.15. The native finite-strip quaternion and the charged seam

The native ruling coordinates are taken after the actual analytic
Morse-Cox map of RT.2 and the full two-node refinement in EA.17 below.
To make the first arrow explicit, write its old
pairs as s=(s0,s1), t=(t0,t1), and put
\[
       S=(F_+,s_0),\qquad T=(F_-,t_1).
 \tag{EA.31}
\]
This is an auxiliary-equivariant analytic isomorphism with the
inverse already displayed in RT.2. It preserves both ruling
ideals. Indeed, writing \(d=(\sigma+1)/2\),
\[
 F_+=d s_1+s_0\left(-d-
                  \frac{s_0(t_0+t_1)}{2(\sigma+1)}\right),
\]
\[
 F_-=d t_0+t_1\left(d-
                  \frac{t_1(s_1-s_0)}{2(\sigma+1)}\right).
\]
The two coefficient determinants are -d and d, both units.
Consequently (F+,s0)=(s0,s1) and (F-,t1)=(t0,t1) as ideals,
so the map lifts both projective rulings. It keeps the common
line coefficient xi, with the actual r maps in the degree-two
sector. Its full complex Jacobian is -sigma, an extending unit.
The source functions are exactly those of RT.2, expressed in
these coordinates. This is the first source-preserving chart arrow,
not a substitution based only on matching weights. Its displayed
pairs are intermediate selected-node coordinates. EA.17 carries
them to the full two-node pairs; the S,T in the norm and quaternion
formulas below denote those final pairs. The extra source/line
units and their inverses are kept in every reset and cap composition.

Use the divisor metrics transported by (EA.31) for the finite
end. In these metrics the exact EA.12 ratio is
\(N_T=R^aN_S\), \(R=\|S\|\|T\|\). On the stable collar
the old and transported metrics have a bounded positive ratio;
its actual real logarithm, and its transported cap average, give
the metric interpolation. No phase or period map is changed.
The positive scaling in EA.13 leaves the unit directions of S
and T unchanged.

Set, in these actual pairs,
\[
 u=S_0+jS_1,\qquad c=T_0+j\overline{T_1},\qquad
 \widehat u=u/\|S\|,\quad\widehat c=c/\|T\|,
\]
\[
 q_H=\widehat u\widehat c,\qquad
 h=\widehat u i\widehat u^{-1},\qquad
 k=\widehat c^{-1}i\widehat c.
 \tag{EA.32}
\]
Thus the actual t-ruling to s-ruling map is
\(h=q_H k q_H^{-1}\), with its full normal coordinate qH.

In the primary V=1 charged chart, T0=z. Conjugate the two
negative physical-weight coordinates and choose the explicit
constant unitary target coordinates
\[
 p=\overline{S_0}+j\overline{S_1}=j u j^{-1},\qquad
 q_{\rm alt}=z-jT_1=j\overline c j^{-1}.
\]
Both have the same positive right physical-circle action, with
the retained common mu-a quotient. The exact projective ratio is
\[
 w_{\rm alt}=p q_{\rm alt}^{-1}
       =\frac{j(u c)j^{-1}}{\|T\|^2},\qquad
 g_{\rm alt}=\frac{w_{\rm alt}}{|w_{\rm alt}|}
       =j q_H j^{-1}.
 \tag{EA.33}
\]
Its two Hopf base coordinates are
\[
 h_{\rm alt}=-j k j^{-1},\qquad
 h'_{\rm alt}=-j h j^{-1}.
 \tag{EA.34}
\]
Therefore \(h'_{\rm alt}=g_{\rm alt}h_{\rm alt}
g_{\rm alt}^{-1}\) is precisely the native inverse ruling
map with the stated constant arrows. Each minus in (EA.34)
is the antipodal map of S2, of degree -1; neither is discarded.
The exact Hopf lift is
\[
       g_{\rm alt}\frac{q_{\rm alt}}{|q_{\rm alt}|}
                           =\frac p{|p|}.
 \tag{EA.35}
\]

The root audit RE.9 uses instead
\(q_{\rm root}=T_1+jz=j q_{\rm alt}\).
This is the literal constant complex-linear map
\((z,-T_1)\mapsto(T_1,z)\), with complex determinant one.
In that exact coordinate choice the dictionary becomes
\[
 g_{\rm root}=-j q_H,\qquad h_{\rm root}=-k,
 \qquad h'_{\rm root}=-j h j^{-1},
 \qquad
 g_{\rm root}\frac{q_{\rm root}}{|q_{\rm root}|}
                               =\frac p{|p|}.
 \tag{EA.36}
\]
This records the comparison in the root's written atlas as well
as in the convenient conjugated atlas. The other quaternion
hemisphere always retains \(w'=w^{-1}\), including its actual
four-dimensional base orientation. The identity reconstructing
the same charged point is
\((p,q)=(rwu,ru)=(r'u',r'w'u')\), with \(r'=|w|r\),
and the positive radius is the actual solution on the transported
shape of EA.14. Hence every q-source and v function is literally
unchanged on the overlap. The inverse of (EA.31) carries that
statement back to the original Weierstrass/Cox chart.

For a=2 the associated physical line map is
\([u,z]\mapsto z u^{\otimes2}\) into O(-2); the Hopf arrow
(EA.35) intertwines it and its normal coefficient frame. The
canonical spin-c and determinant lifts are those of EA.13;
the analytic Morse unit -sigma has its extending logarithm
after its fixed constant sign is retained. The full F0 cap
square and the scalar factor in EA.23 accompany this seam.
The exact quaternion and ideal identities are executed in
\path{code/part3_fourfold/source_zero_native_charged_seam.py}.

This supplies the charged/native seam map. Its hemisphere
inversion and both S2 antipodal arrows still have to be combined
with the actual retained/excised boundary sides in the complete
finite strip. No sign of a global characteristic sum is inferred
from the quaternion formula alone.

## EA.16. Entire finite faces and the retained line coefficient

The norm inequalities are first imposed on the complementary
charged chart, after the literal chain-index change and the source
reset. Its common line coefficient is \(\xi=U_j\). Fixing
\(U_j=1\) gives the residual mu-a cover with actual source pairs
\[
                 S=(w,S_1),\qquad T=(T_0,T_1).
\]
The invariant norm functions in this gauge are exactly
\[
                  N_t=\|T\|^a,\qquad
                  N_s=\|S\|^{-a},\qquad R=\|S\|\|T\|.
 \tag{EA.37}
\]
This gauge is taken only after the actual node reindex; it is not
an assertion that the primary line coordinate U equals one.
Indeed (EA.26) sends it to the primary chart V'=1, with the same
ordered pairs \(S'=(w,S_1)\), \(T'=(T_0,T_1)\). Before that
gauge the transported common coefficient is
\[
                         \xi=(V')^{-1},
 \tag{EA.38}
\]
whereas the primary node coefficient is \(U'=q/(V')\).
Consequently the transported norms there are
\(|V'|^{-1}\|T'\|^a\) and
\(|V'|^{-1}/\|S'\|^a\). This retains the q-factor and is the
exact reason the bare inequalities in (EA.37) apply after the
specified arrow. The source-fibre constant c-lambda, its phase,
and the index j to j-1 are those in (EA.23); they precede (EA.38).

Choose a sufficiently small charged radius r. The two entire
closed finite faces are
\[
 H_t(r)=\{N_t=r^a,\ R\le r^2\}
       =(D^4_S(r)\times S^3_T(r))/\mu_a,
\]
\[
 H_s(r)=\{N_s=r^{-a},\ R\le r^2\}
       =(S^3_S(r)\times D^4_T(r))/\mu_a.
 \tag{EA.39}
\]
In the positive charged quaternion coordinates of EA.15 these
are respectively \(|p|\le|q|=r\) and
\(|q|\le|p|=r\). Their common face is
\(|p|=|q|=r\), with the exact quaternion and Hopf-line
transition (EA.33)--(EA.36). Thus the comparison specifies the
full two orbit charts, not only their unit-quaternion seam.
Rounding the product-ball corner uses its two actual norm defining
functions. Its charged shape is then compared with the prescribed
lower radial arm by EA.14, by ambient inclusion with q,v retained.

On R positive the end normalization from Ht to Hs is
\[
             d=(R/r^2)^a,\qquad
             (S,T)\longmapsto(d^{-1/a}S,d^{1/a}T).
 \tag{EA.40}
\]
It sends \((\|S\|,\|T\|)=(s,r)\) to \((r,s)\),
preserves all source auxiliary invariants and hence q,v, and is
the actual positive physical scaling of the common line before
refixing its gauge. It leaves the unit directions used in qH
unchanged. At a positive inner cut R=epsilon the factor is a
single positive constant. No extension of (EA.40) at R=0 is
claimed: the two cores remain the distinct full-face boundary
pieces in (EA.39).

The oriented side follows from the actual contracting direction.
Let eta denote the positive physical real-orbit field on this
charged cover, up to its positive factor 1/a:
\[
                       \eta=-S\partial_S+T\partial_T.
\]
The forward suspension is contracting in its physical line, so
its normalized real direction is -eta. The retained constant
phase acts tangentially and carries the lift in EA.13. On Ht,
-eta differentiates \(\|T\|^2-r^2\) to \(-2r^2\): it
enters the product ball. On Hs it differentiates
\(\|S\|^2-r^2\) to \(+2r^2\): it exits. If each end is
oriented by contraction with the forward direction, the target
minus source end chain therefore equals the positively oriented
boundary of
\[
                       (D^4_S(r)\times D^4_T(r))/\mu_a.
 \tag{EA.41}
\]
This comparison uses the full real eight-dimensional coordinate
arrow. The two negative complex conjugations preserve that
orientation; the S2 antipodal maps and the hemisphere inversion
in EA.15 are retained within it. Thus no side is selected merely
from the name of a ruling or an auxiliary chamber.

All maps on these faces are the node-chart maps in EA.9, followed
by the source/Cartier map of TL and the full F0 cap square of
EA.12. The physical associated line and its canonical spin-c
lift are transported by those same maps. The exact finite-face
norm and side computations are in
\path{code/part3_fourfold/source_zero_full_faces.py}.
The global construction must still insert these faces into the
compact period strip and account for its horizontal fixed cap;
(EA.41) records their local oriented ownership without assigning
the resulting absolute source-zero return.

## EA.17. Full two-node refinement of the Morse-Cox pairs

The parameter formula in the exact two-node chart is
\(\widetilde v=q_1-q_2=v u_v(v)\). To retain it together with
the primitive Cartier frame, use the actual analytic source
functions from SZ.20--21 and TL.4. Explicitly, put
\[
 A_0=1-2v,\qquad x_c=\frac{-A_0+\sqrt{A_0^2-3T}}3,
\]
\[
 R_c=(X-x_c)\sqrt{A_0+2x_c+X},\quad
 \upsilon=\frac{v^2-A_0x_c^2-2x_c^3}{q_1q_2},
\]
where both square roots and the extending unit upsilon are the
specified analytic branches. Define
\[
 A_M=(Y-R_c)/\upsilon,\quad B_M=Y+R_c,\quad
 a_G=A_M(G)/q_2,
\]
\[
             \alpha=-A_M/(2a_G),\qquad
             \beta=-2a_GB_M.
 \tag{EA.42}
\]
They satisfy \(\alpha\beta=q_1q_2\),
\(\alpha(G)=-q_2/2\), and \(\beta(G)=-2q_1\).
All functions are pulled back through the actual Cartesian source
map of SZ.19; no linear approximation is used in (EA.42).

Keep the exact selected factors F+,F- of RT.2 and define
\[
 S_0=F_+,\qquad T_0=F_-,\qquad
 S_1=-\frac{\beta}{2F_-},\qquad
 T_1=-\frac{2\alpha}{F_+}.
 \tag{EA.43}
\]
The quotients extend holomorphically. For example F+=0 is an
irreducible coordinate hypersurface of the RT.2 chart. The
restriction of beta to it is not identically zero, as its leading
term is \(-2(s_0+s_1)(t_0+t_1)\). Since alpha beta vanishes
there, alpha vanishes identically there and is divisible by F+.
The analogous argument gives divisibility of beta by F-. The
leading maps are exactly
\[
 (S_0,S_1)=(s_1-s_0,s_0+s_1)+O(\|(s,t)\|^3),
\]
\[
 (T_0,T_1)=(t_0+t_1,t_0-t_1)+O(\|(s,t)\|^3).
\]
Their complex Jacobian at the origin is 4. Thus (EA.43) is an
actual auxiliary-equivariant analytic isomorphism on a small
neighbourhood. It has
\[
                 q_1=S_0T_0,\qquad q_2=S_1T_1,
                 \widetilde v=S_0T_0-S_1T_1
 \tag{EA.44}
\]
as literal equations. It preserves the two ruling ideals and
therefore lifts both small resolutions, with their actual source
coordinate maps. This is the full higher-normal comparison behind
the linear display SZ.26.

The marked section is retained as well. On the old divisor s0=0,
the exact evaluations in (EA.42) give S1=S0. Hence
\[
                \kappa=\frac{S_1-S_0}{2s_0}
 \tag{EA.45}
\]
is holomorphic; its value at the origin is one, so it is a unit.
The actual line coefficient is carried by
\[
                    \xi_{\rm node}=\kappa^a\xi_{\rm Cartier}.
 \tag{EA.46}
\]
This follows by equating the meromorphic coefficients with
denominators \(s_0^a\) and \(((S_1-S_0)/2)^a\).
The source and target r maps are applied before and after this
formula when a=2. The full reset is consequently conjugated by
the actual kappa factors at its two ends; they are not replaced
by their value on the exceptional curve. The same conjugation
is made in the F0 root square.

The unit kappa and the normalized Jacobian of (EA.43) have
extending logarithms. Their exact logarithms carry the line and
canonical spin-c determinant lifts, while the nonunit
\((-1)^a z_s^{-2a}\) reset and its explicit root in EA.27
remain. Thus (EA.43)--(EA.46) connect the full finite-face proof
to the bilinear source map in RT.13--15 and to TL's actual Tate
label. They do not identify the intermediate nonlinear v formula
with the bilinear formula without this morphism.

## EA.18. Finite cut-and-paste ledger for the reduced branch

This section is the full reduced-branch attachment draft for audit.
It uses a=2,b=1. It does not copy the different a=1 moment picture.
All scalar windings have first been separated by the actual based
homotopy RT.12, so the scalar in this construction is the fixed
nonzero value at r_base. The unscaled infinite central quotient of
SZ.29 is not used.

Take the actual compact source translation graph. Its domain and
target maps outside the central curve are the literal addition
formula and the Cartier line map of SZ.7 and SZ.14--17. At that
curve use both projective charts of the common Cox graph: the
domain t-ruling includes its t1=0 chart at the zero section, and
the target s-ruling includes both divisor charts of G. Thus the
whole proper central component and the whole exceptional component
are retained, not only their affine node points. On a small graph
neighbourhood use the analytic node map (EA.42)--(EA.46). Outside
it the actual source/line map is an isomorphism between the two
graph projections; choose the ordinary norm cut and transport its
target face by that map. The finite-root source/line map is the
actual U_cap of EA.4, with F0 on its annulus. Compactness of the
remaining source and root pieces gives one common contracting
scalar range.

Cut before taking the period quotient. On the compact complement
of the graph neighbourhood this is the ordinary fundamental
annulus between a norm hypersurface and its actual B-image. On
the stable graph collar use the finite region between Ht and Hs
from EA.39, with R bounded below by a positive epsilon. The
actual end scalar and its phase are retained before the positive
normalization EA.40. The change of norm cut is an explicit
monotone interpolation of the two logarithmic norm coordinates,
fixed at their transported endpoints; on the node charts its
extension is the positive diagonal map in EA.13. Thus no raw
logarithm of q is extended through q=0. The q factor is absorbed
by the literal j to j+1 node arrow, and the actual cyclic graph
reset and j to j-1 overlap are EA.18--26.

The selected node is completed in the primary positive associated
chart. TL.1--4 identifies its boundary, through the full theta,
Cartier and h-period map, with current Tate T0. On the positive
moment piece use the compact region RT.20 and its invariant
corner rounding. Its defining functions are the actual R and
rho, and q,v are retained by ambient inclusion. The lower arm
is the transported shape EA.29--30. Its full two faces are
EA.39, with their actual source/target line coefficient EA.38;
their full orbit transition is EA.33--36. The upper arm stays
in the primary positive piece. It is not relabelled as a
charge-two arm or silently capped by a second copy of the
lower chart.

The following face pairings are the ledger for this finite
construction. They specify maps, not merely a cancellation of
numbers.

* Ordinary source and target norm faces are paired by the actual
  B map, with its Cartier coefficient. Their boundary normals
  are opposite. On the graph collar this is the same pairing
  after the explicit positive norm interpolation just described.
* Every finite-root face is paired by the literal H or A map of
  EA.12. The F0 square identifies it with the ordinary B pairing;
  both norm signs, all finite characters, and the root-component
  translations remain. There is no residual cap face from replacing
  a finite root by its generic source point.
* The inner source collar and the ordinary source exterior are
  glued by TL's full source/line map. On every node chart its
  monomial factors and units are the actual ones, including the
  h reindex. The two source-base normals are opposite. The
  source functions and their parameter arrow agree literally.
* In the chosen finite B strip the complementary U and primary
  V descriptions are one charged end. They are related by EA.26,
  not added as two positive GIT charts. After all other period
  faces have been paired, the target-minus-source finite face
  cycle is the single positive charged boundary Sigma_a of
  EA.41. The q reindex, scalar phase and determinant root are
  retained. In particular the lower charged origin is not
  quotiented by its infinite central stabilizer.
* The fixed surface is the entire
  F=Bl(P1 times D), including its exceptional disk. Its annular
  part in RT.20 carries the same two normal frames on both
  sides. It is capped only by the actual outside cap C0=D3
  times S1. No separate local D4 cap from RT.10 is inserted.

Every gluing is between disjoint closed collar faces by the
specified diffeomorphism. The construction is finite: it uses a
compact norm interval, both charts of each projective ruling,
the finite root atlas and the two compact corner arms. Thus the
resulting glued space is compact and Hausdorff; it is not obtained
by gluing two open GIT quotients with distinct limits. Invariant
rounding of the stated regular boundary functions gives its smooth
collars. On the outer nonzero v circle the cuts are simply cuts
of the original proper family: choose epsilon so small that the
R-epsilon region lies strictly inside that parameter circle.
The full TL and F0 maps therefore identify the completed outside
boundary with that actual parameter return.

The spin-c and physical-line identifications on these face
pairings are the actual coefficient and derivative maps. The
ordinary and finite-cap maps are holomorphic. The norm
interpolations have the explicit positive and rank-one derivative
homotopies in EA.10 and RT.15. The graph reset has the exact
determinant root i*z_s^(-2), conjugated by the full extending
kappa units; the charged overlap has its constant root i.
The mu2 endpoint is the canonical +omega8 in EA.13/RT.15.
These are composed in the same order as the actual face maps.
On an ordinary triple overlap their composition is the
canonical complex spin-c lift of the actual coordinate identity;
on a root overlap it is the specified finite-character action.
No additional sign character is inserted at the RP3 face.

Here is the resulting oriented boundary equation to be audited
against the full construction, before assigning a return value.
Let N7 be the actual free-circle total boundary obtained by the
outside conifold/Hopf completion, and let N6=N7/S1. Delete the
entire capped fixed tube and the primary positive chart's
charge-one ball. Replace the fixed cap C0 by C=P1 times D2
with the actual normal-map triangle of RT.17. Give C and C0
the same boundary orientation as partial F. Then
\[
 [F-C_0]=[F-C]+[C-C_0],\qquad C-C_0=S^4.
\]
Write B_F and B_4 for their actual projectivized normal sphere
bundles, with physical tautological line. The finite free
circle quotient has boundary cycle
\[
       -N_6-\mathbb P^3_a-B_F-B_4+\mathbb P^3_1.
 \tag{EA.47}
\]
Here P3_a denotes the charged boundary with M=O(-a), not a
discarded residual quotient; P3_1 is the primary positive
isolated-point boundary. The sign of P3_a is fixed by the
positive total-space end chain EA.41 and the circle-first
boundary reversal. The deleted fixed tube contributes -B_F
and -B_4 by the literal cap identity. The two negative normal
conjugations at the isolated point give +P3_1, as in RT.13.
The exceptional disk belongs to F once and never to a separate
local fixed-S3 handle.

The physical line and stable tangent bundle on this cycle are
the ones carried by the actual free circle action. The S4
normal clutch is retained; no value of its c2 is imposed.
RT.16--17 computes its index and the full fixed-surface term
with both actual parameter windings. The geometric global
attachment and (EA.47) are kept in this audit draft until the
complete outside and cyclic endpoint comparison has passed.
No individual source-zero return is assigned in this note.

## EA.19. Explicit upper-arm filling in the retained positive chamber

The region RT.20 alone excludes the primary charge-one point.
The finite construction uses the following additional actual
domain in the same positive quotient W. Choose
\(2\varepsilon<r_1<\rho_0\) and put
\[
 \mathcal D=\{\rho\le r_1\}\ \cup\
 \{r_1\le\rho\le\rho_0,\ R\ge\varepsilon\}\ \cup\
 \{r_1\le\rho\le\rho_0,\ A\ge1/2\},
 \qquad A=|z|^2/H.
 \tag{EA.48}
\]
This is a compact subset of the actual disk bundle W. On A=1/2,
RT.21 gives \(R^2/\rho^2\ge1/4\). For rho at least r1 the
artificial A boundary therefore lies strictly in R>epsilon,
already retained by the middle piece. It supplies no additional
boundary face. Below rho=r1 the entire disk bundle is retained.
All intersections are identity intersections in the same smooth
positive quotient, not identifications of different GIT limits.

The added upper portion is in the literal z=1 chart. There
\(A\ge1/2\) means \(|S_0|^2+|S_1|^2\le1\), and
\[
 \rho^2=(1+\|S\|^2)|T_1|^2
                 +(1+\|S\|^2)^2|V|^2,
 \qquad R^2=\|S\|^2(|T_1|^2+|V|^2),
\]
\[
             q_1=S_0V,\qquad
             \widetilde v=S_0V-S_1T_1.
 \tag{EA.49}
\]
Thus the full upper fibre S=0 with rho at most rho0 is present,
including its unique charge-one origin. A sufficiently small
round ball around that origin lies entirely in rho<r1 and in
this single chart; it is the one ball deleted in EA.47. Its
physical weights and canonical spin-c maps are exactly those of
RT.15. No second origin is introduced by an overlap.

The entire zero section, and hence the exceptional disk of the
fixed surface, also lies in rho<r1. On the fixed surface z=V=0
one has R=rho. Its part above r1 therefore belongs to the
R>=epsilon piece; the whole fixed surface inside rho<=rho0
is retained. It is attached to the rest of F and capped only by
the global C0 construction. There is no separate RT.10 handle.

The sole removed horn of (EA.48) is
\(r_1<\rho\le\rho_0,\ A<1/2,\ R<\varepsilon\).
At every rho in this interval it is the lower arm, since
\(\varepsilon^2/\rho^2<1/4\). Its boundary consists of the
two specified rho cuts and the actual R=epsilon side. The
charged defining-function and full-face maps EA.29--41 are
applied to those cuts and this side, with their transported
functions. They retain q,v, the physical line and the stated
spin lift. Invariant rounding uses only these regular defining
functions, with the A-boundary absent as just proved.

Finally the outside separation is quantitative in the final
two-node pairs:
\[
 |q_1|+|q_2|=|S_0T_0|+|S_1T_1|
                       \le\|S\|\|T\|=R.
\]
Since \(q_1-q_2=v u_v(v)\) is the actual base-coordinate
change, on the chosen fixed bidisc
\(|v|\le C R\) and \(|T|\le C'R\).
The R<=epsilon modification can consequently be chosen disjoint
from both the prescribed outer source-parameter circle and the
outer source-base boundary. Their actual family maps remain
unchanged. This supplies the upper-domain ownership omitted
from the first EA.18 draft; the full boundary ledger remains
under audit.

## EA.20. The complete lower-horn boundary chain

Let H be the closure of the lower horn removed in EA.48. Its
three seven-dimensional faces are the outer rim Hr at rho=rho0,
the floor Hf at rho=r1, and the side Hs at R=epsilon. Orient H
by the ambient complex orientation. With positive rho and R
coordinate conventions its boundary chain is
\[
                       \partial H=H_r-H_f+H_s.
 \tag{EA.50}
\]
The retained domain D consequently has
\[
              \partial D=\Sigma_{\rho_0}-H_r+H_f-H_s.
 \tag{EA.51}
\]
The rim is removed from its outer radial face; the floor and
side are actual remaining boundary faces, not extra copies of
the charged end. The artificial A=1/2 face is absent by EA.19.

The entire horn has V nonzero, since its lower-arm parameter
u is at most \((\varepsilon/r_1)^2<1/4\). Apply the actual
EA.26 charged map, retaining the c-lambda normalization, to all
of H. Choose the angular cutoff to be one for
\(u\le(\varepsilon/r_1)^2\) and supported in u<1/2.
Then the full outer shape of EA.14 has sigma squared times f
equal to rho on the entire horn, not only on its rim. Take the
inner round charged link with squared radius r1/2. It is
strictly below H because sigma squared is at least rho, hence
at least r1 there.
The resulting full charged annulus A_f contains the whole H,
and its outer boundary meets H exactly along the prescribed
rim. The same explicit positive shape function applies.
No radial map is used to identify source functions.

Put \(C=\mathcal A_f\setminus\operatorname{int}H\).
It is a compact free-circle domain with its inherited source
functions and physical line. Its complete boundary is
\[
           \partial C=Y_f-Y_{\rm round}-H_r+H_f-H_s.
 \tag{EA.52}
\]
Glue D to the oppositely oriented C along their floor and side
faces, using EA.26 and the exact defining functions, line maps
and spin-c lifts already specified. Their identical face
orientations before reversal are precisely why C is reversed.
The two common faces cancel. The remaining outer face is
\[
 (\Sigma_{\rho_0}\setminus\operatorname{int}H_r)
       \cup_{\partial H_r}
       -(Y_f\setminus\operatorname{int}H_r),
\]
and the only additional full face is the positively oriented
\(Y_{\rm round}\). The latter is a single charge-a link.
This is an equality of cut manifolds with their actual collars,
not a subtraction of local characteristic numbers.

The charged free portions of this outer face use the full
source and target maps in EA.39, with transition EA.33--36
and transported coefficient V inverse from EA.38. The outer
face also contains its fixed S3 tube and its upper z=1 arm.
Those pieces must be retained in their own actual charts:
EA.39 is not an identification of this entire mixed face.
The exact fixed-tube and upper-chart maps are recorded in
EA.21 below. The finite-period comparison is complete only
after these maps agree with its ordinary and root faces through
the actual B and F0 arrows.

All fixed strata lie in D. C and its glued faces are free.
The exceptional disk remains in the whole F, and the one
primary charge-one point remains in the upper domain of EA.19.
Thus this construction neither adds a second fixed cap nor
counts the two U/V descriptions of the charge-a end twice.

The gluing uses product collars obtained from the specified
invariant boundary functions and an averaged connection on
the actual line. Source functions agree on every glued face.
For a smooth real map after collar gluing, use the common face
value on a smaller product collar and interpolate to each
ambient function with an even cutoff flat at the gluing face.
This is the explicit real collar extension; it is not asserted
to be a holomorphic radial normalization. It is supported in
the inner source neighbourhood, disjoint from the actual
outer parameter family and the finite-cap annulus by EA.19.
The physical line and its derivative lift are glued by the
actual face map, constant in this product collar. The opposite
orientation on C uses the opposite spin-c collar obtained by
reflection in its specified outward real normal. That normal
is a global collar vector, so this reflection is a fixed map
and inserts no sign character on the RP3 fundamental group.
The resulting endpoint is therefore the one already carried
in EA.13, not an independently chosen RP3 lift.

The chain (EA.50)--(EA.52) supplies the lower-face counting
and the sign of the full residual charged boundary in EA.47.
The complete finite-strip and outside comparison remains an
audit draft; no individual source-zero return is entered here.

## EA.21. The fixed tube and free parts of the mixed outer face

The earlier wording of EA.20 is preserved in
\path{records/attempts/source_zero_outer_face/pre_mixed_face_decomposition.md}.
A point z=V=0 on the outer radial sphere has full physical
circle stabilizer. The charged product faces of EA.39 are free.
The following chart decomposition retains the fixed part in
the normal bundle of the whole surface F.

On an invariant neighbourhood of its fixed S3, use the unique
positive auxiliary gauge ||S||=1 and write T1=t exp(i phi),
with t positive. Put
\[
 p=e^{i\phi}S,\qquad \zeta=e^{i\phi}z,\qquad
 \nu=e^{2i\phi}\overline V,\qquad \|p\|=1 .
 \tag{EA.53}
\]
These are invariant under the remaining auxiliary circle.
On rho=rho0 the exact inverse is obtained from
\[
 t^2={\rho_0^2\over1+|\zeta|^2}
                  -(1+|\zeta|^2)|\nu|^2 ,
 \tag{EA.54}
\]
followed by any Hopf representative phi; changing that
representative is exactly the auxiliary identification.
For a sufficiently small normal disk the right side is positive.
Thus (EA.53) is a literal product of the fixed S3 with its
small real normal disk, including the zero vector. Its source
functions are
\[
 q_1=p_0\zeta\overline\nu,\qquad q_2=p_1t,\qquad
 \widetilde v=q_1-q_2 .
 \tag{EA.55}
\]
The compact physical circle multiplies both zeta and nu by
the same phase. They are precisely the positive-weight
spinor coefficients in EA.15; the second coefficient retains
the conjugation of the negative original normal. The
original complex normal and this positive spinor are related
by that displayed real-linear arrow, with the orientation
and physical tautological line of K68.

The radius on this tube satisfies
\[
 R^2={\rho_0^2\over1+|\zeta|^2}-|\nu|^2 .
 \tag{EA.56}
\]
Choose its normal radius so that R>rho0/2>epsilon throughout.
Its punctured part consequently meets the R>0 free norm
strip. On that overlap the physical positive end map is
the same coefficient map
(U,V) -> (d U,d^{-1}V), with d=(R/r^2)^a.
In the primary chart it is
(z,V) -> (d z,d^{-1}V); it extends over z=V=0,
fixes the source invariants, and has the stated positive
diagonal derivative there. Its full variable derivative is
the base-preserving rank-one extension from EA.10. This
specifies the overlap of the fixed-tube arrow and the free
norm arrow; no independent normal framing is selected.

The local fixed S3 first glues to the rest of the horizontal
normalization surface by the actual RT.1 source immersion,
the two-node map EA.42--46 and the retained Cartier r map.
It receives no local D4 cap. At the global boundary
S2 times S1, the entire resulting normal tube is carried
by the actual Cox quaternion product RT.33a and its ball
extension RT.33b to the single outside cap C0.
The normal clutch on its comparison with C is retained in
RT.29--34. In particular the local S3 and the global
S2 times S1 are connected by this actual trace, not
identified as boundary manifolds.

The upper arm has its own chart. In z nonzero take z=1 and
write
\[
 s_i=S_i/z,\qquad t=zT_1,\qquad w=z^2V .
 \tag{EA.57}
\]
The physical weights are (-1,-1,+1,+1) on
(s0,s1,t,w), and
\[
 q_1=s_0w,\qquad q_2=s_1t,\qquad
 \rho^2=(1+\|s\|^2)|t|^2+(1+\|s\|^2)^2|w|^2 .
 \tag{EA.58}
\]
These are the literal upper chart of the same positive
quotient, including s=0. Its origin belongs once to D;
the deleted charge-one ball and its source functions are
those of EA.19.

On the overlap w nonzero the complete map to the primary
charged V=1 chart is
\[
 (s_0,s_1,t,w)\longmapsto
 (\sqrt w\,s_0,\sqrt w\,s_1,\ t/\sqrt w,\ \sqrt w)
 \tag{EA.59}
\]
in the ordered coordinates (S0,S1,T1,z). The two roots
differ by the actual residual mu2 action. This map preserves
q1 and q2, is equivariant for the same physical circle,
and carries its canonical complex spin-c map through the
specified auxiliary gauge. Its full determinant and line
characters, including this residual action, are retained.
It is the overlap of the upper chart and the lower charged
chart, not a map between their origins.

At w=0,t nonzero the upper chart is still free and has R=0
when s=0. The following actual T1 chart and Tate-period map
retain this endpoint without using an R>0 flow.

On T1 nonzero take the auxiliary gauge T1=1, with coordinates
\[
 (A,B,C,D)=(T_1S_0,T_1S_1,T_1z,T_1^{-2}V).
 \tag{EA.60}
\]
Its physical weights are (0,0,+1,-1), and
q1=A C D, q2=B. The upper-chart arrow is
\[
 (s_0,s_1,t,w)\longmapsto
                   (ts_0,ts_1,t,w/t^2).
 \tag{EA.61}
\]
Thus it includes the entire w=0,t nonzero core.
The radial face rho=rho0 is covered by this chart and V
nonzero, since rho>0 implies (T1,V) is not (0,0).
On their overlap choose h with h squared equal to D. The
map to the ordered V=1 cover coordinates is
\[
 (S_0,S_1,T_1,z)=(hA,hB,h^{-1},hC).
 \tag{EA.62}
\]
Both choices of h give the same point of the specified mu2
quotient. The determinant of this four-coordinate map,
in the ordered variables (A,B,C,D), is +1/2. Consequently
the actual charged contraction volume
-2 dS0 wedge dS1 wedge dT1 wedge dz pulls back to
-dA wedge dB wedge dC wedge dD, which is the contraction
volume in the T1=1 chart. This is the full canonical
spin-c overlap, including its root deck, rather than an
orientation assigned from the coordinate names.

Here is the exact additional free-line chart. On the dense
overlap used by TL take its source coordinate S=s0/s1
and its tensor-Cartier coefficient \(\xi=s_0/s_1^2\).
The latter denominator is required by auxiliary weight two.
The full TL formulas give
\[
 W_0=s_0t/u_P,\quad Z_0=u_Gs_1w,\quad
 V_0=E_+^2s_0/s_1^2,\quad
 Q=q_1q_2u_Q,\quad P=u_P/q_2,\quad u_G=u_Qu_P .
 \tag{EA.63}
\]
Apply the actual inverse period h inverse to all coordinates,
then the indicated integral toric character map:
\[
 (Z_0,V_0)\longmapsto(Z_0/Q,V_0/P^2)=(1/W_0,V_0/P^2),
 \qquad (Z,V)\longmapsto(Z^{-1},ZV).
 \tag{EA.64}
\]
The resulting coordinates extend as
\[
 Z_t=s_0t/u_P,\qquad T_t=u_Pw/t,\qquad
 L_t=E_+^2t/u_P,\qquad q_2=s_1t .
 \tag{EA.65}
\]
In particular q1=Zt Tt and Lt is nonzero when t is nonzero.
Every theta and Cartier unit in E+ is retained in (EA.65).
The full inverse is
\[
 t=u_PL_t/E_+^2,\qquad w=T_tL_t/E_+^2,\qquad
 s_0=E_+^2Z_t/L_t,\qquad
 s_1=E_+^2q_2/(u_PL_t).
 \tag{EA.66}
\]
Here uP and E+ are evaluated on the recovered full source
chart (Zt,Tt,q2). They are independent of Lt. For example,
S=P Zt and Q/S=Tt q2 squared uQ/uP in the full theta
product, while S/P=Zt and Q/Zt=Tt q2 uQ. All factors
after the extracted 1-S have extending unit logarithms on
the chosen t-dominant collar. Thus (EA.65)--(EA.66) give
a holomorphic free-line chart through w=0,t nonzero, not
only formulas on the dense source torus.

The character map in (EA.64) has the literal lattice matrix
\[
 J=\begin{pmatrix}-1&0\\1&1\end{pmatrix},\qquad
 \widehat J(x,y,h)=(-x,x+y,h).
 \tag{EA.67}
\]
For the actual negative-square T0 fan, J sends
{0,e1,e2} to {e1,e2,e1+e2}-e1, and sends the latter
triangle to {0,e1,e2}-e1+e2. The full integral height
translations are retained in these statements. The preceding
inverse h period in (EA.64) is the actual period (Q,P squared),
not just its valuation. All period maps on this new chart are
its literal conjugates through (EA.64).

The source marking in this chart is explicit:
\[
 W_0=Z_t,\qquad Z_0=u_Q q_2 T_t,\qquad q_1=Z_tT_t .
 \tag{EA.68}
\]
It is the (Z0,q2) small-resolution chart. TL's original
chart used (W0,q2). The two source projections are the two
projections of the actual common translation graph, and
their comparison must use the source -G map and its
Cartier reset EA.18--20. This resolution arrow, with the
full r map, is retained in the endpoint audit. It is not
replaced by an identification of central Picard classes.
No individual source-zero return is assigned from this
chart calculation alone.

## EA.22. The actual upper closing arrow and the indexed ordinary end

The opposite-resolution arrow in EA.68 is supplied by the
literal inverse suspension. Retain the fixed nonzero scalar
\(c_\lambda=2\lambda\), \(c_X=q_2u_X\), and the full
SZ.43 Cartier-normalized primitive. In the original torus
coordinates the forward map and its inverse are
\[
 B:(Z,V)\longmapsto
       (P^{-1}Z,c_\lambda q_1c_X^{-2}V),\qquad
 B^{-1}:(Z,V)\longmapsto
       (PZ,c_X^2V/(c_\lambda q_1)).
 \tag{EA.69}
\]
This is the reduced a=2,b=1 map. The cX square in the
inverse is the actual source/target r-conjugated line
map proved in SZ.41--43; it is not an inferred action
on generic Picard classes.

Write (W,T,L) for (Zt,Tt,Lt). Before the inverse
suspension, the full target torus coefficients recovered
from EA.63--66 are
\[
 Z_0=q_2u_QT,\qquad V_0=P^2WL
                  ={u_P^2\over q_2^2}WL .
 \tag{EA.70}
\]
Applying EA.69 gives the exact expressions
\[
 Z_{\rm pre}=u_GT,\qquad
 W_{\rm pre}=Q/Z_{\rm pre}=q_2W/u_P,\qquad
 V_{\rm pre}={u_P^2u_X^2\over c_\lambda T}\,L.
 \tag{EA.71}
\]
The source is now precisely the marked TL resolution:
its coordinate S=P Wpre is W and its other node
coordinate is T. Thus the source part of B inverse,
which is the actual +G map, carries the opposite
(Z0,q2) resolution of EA.68 to the prescribed
(Wpre,q2) resolution. This is also the actual inverse
of the graph formulas SZ.14 and EA.18. Both projections
retain the same q1,q2 and the chosen v coordinate.

The last expression of EA.71 is read in its actual
toric edge chart. The edge is
\[
 \{(0,0,1),(1,-1,1)\}
       =\{(1,0,1),(0,1,1)\}-(0,1,0).
 \tag{EA.72}
\]
It is the negative diagonal of the square translated
by (0,-1). Its coordinates are
\[
 x=Z_{\rm pre},\qquad y=q_1/Z_{\rm pre},\qquad
 L_{\rm pre}=Z_{\rm pre}V_{\rm pre},
 \qquad xy=q_1,\quad L_{\rm pre}\ne0.
 \tag{EA.73}
\]
The invertible character on this indexed edge is ZV.
On the unshifted edge it would be ZV/q1. The actual
height translate in EA.72 therefore retains precisely
the adjacent-node j to j-1 change in the inverse
suspension; it is not applied a second time.

In the marked source coordinates (W,T,q2), the
complete upper closing map is now
\[
 (W,T,q_2,L)\longmapsto
           (W,T,q_2,F(WT,q_2)L),\qquad
 F={u_Gu_P^2u_X^2\over c_\lambda}.
 \tag{EA.74}
\]
Every factor is the full extending unit from SZ.39--43.
The retained constants uQ(0)=1/256, uP(0)=16 and
uX(0)=-1/4 give F(0)=1/c_lambda. The quotient
F/F(0) has an extending logarithm on the source
bidisc. The actual fixed scalar and its chosen phase
remain in F(0). Equation EA.74 is invertible, with
complex determinant F. It extends through T=0 and
W=0 and includes the entire t-dominant upper core.
Its inverse is the forward finite-face pairing.
The line is the physical weight-one line in both
charts. In particular no dual circle is introduced
by the source inversion in EA.64.

Here is the complete pairwise collar comparison.
The radial face has the open cover V nonzero and
T1 nonzero, since rho is positive. On the T1 chart
the free locus is C nonzero or D nonzero. The part
D nonzero is the V-chart overlap EA.62. The part
C nonzero is the upper z=1 chart with t=C nonzero,
and is carried by EA.65--74 to the actual indexed
next end. The remaining set C=D=0 is exactly the
fixed-tube locus. Thus these named charts cover
the entire mixed face, including its R=0 free
points and its fixed S3.

On the fixed-tube chart EA.53 the map to EA.60 is
the literal formula
\[
 (A,B,C,D)=(t p_0,t p_1,t\zeta,\overline\nu/t^2).
 \tag{EA.75}
\]
It gives q1=p0 zeta conjugate(nu), q2=t p1.
Its normal map is the actual positive spinor
with the retained negative-coordinate conjugation.
On z nonzero EA.61 is its inverse change to the
upper chart; on V nonzero EA.62 is its change
to the charged chart. Therefore the fixed tube,
upper free chart and charged chart agree on all
their pairwise and triple overlaps by the displayed
coefficient maps. The source functions agree
literally. The original r and kappa maps precede
these formulas; their full coefficients enter E+
and the cX square in EA.69.

The R>0 finite norm strips are attached with their
actual transported norms from EA.37--41. Their
overlap with the upper and fixed charts can be
chosen inside R>=epsilon. On that overlap the
same positive scalar d=(R/r^2)^a is used on both
maps. To define the cut on the upper chart down
to R=0, take
\[
 \widetilde d(R)=
 \exp\!\left(\chi(R)\,a\log(R/r^2)\right),
 \tag{EA.76}
\]
where chi is one for R>=epsilon and zero on a
neighbourhood of R<=epsilon/2. Set dtilde=1 on
that neighbourhood. This is a positive smooth
coefficient, applied only to transport the cut.
It preserves q1,q2 because R is invariant along
the physical real orbit. It agrees with the
specified finite norm map on its entire attachment
collar and with the exact upper endpoint near its
core. The full charged cores in EA.39 remain their
own source/target faces; EA.76 is not an extension
of the interchange EA.40 across those cores.

The finite-cap compatibility follows from the
same actual inverse arrow:
\[
 F_0 B^{-1}=(c_\lambda h)^{-1}
                         U_{\rm cap}^{-1}F_0,
 \qquad q_1=q_\infty^{-1}h .
 \tag{EA.77}
\]
This is obtained by inverting the full square in
EA.12, with its root source, r correction, norm sign,
and finite character retained. The h period in
EA.64 is carried as its full lattice arrow through
F0. The positive cut functions are transported
through F0 on its overlap and averaged over its
actual finite group, as in EA.5. The small-R
modification is disjoint from that annulus by
EA.19, so it introduces no new cap face.

For the spin-c comparison, the upper map is the
canonical complex map EA.69 followed by the
actual toric chart EA.73. Its extending unit in
EA.74 has the specified fixed scalar and the
extending logarithm of F/F(0). On the V overlap
the two square roots in EA.62 differ by precisely
the canonical residual mu2 action of EA.13/RT.15.
On the fixed tube EA.75 uses the actual original
complex normal and its written real positive
spinor map. Thus the maps on a triple overlap
are lifts of the same actual composite, with
the determinant factors already fixed in EA.27,
EA.62 and EA.74. There is no additional choice
of an RP3 sign character. The local fixed tube
joins the rest of F before the single global
C0 cap of RT.33a--b is attached.

This supplies the upper endpoint and the mixed-face
overlaps required by the finite ledger EA.47.
The full reduced attachment is submitted for
independent audit with these maps; no numerical
source-zero return is entered before that audit.
