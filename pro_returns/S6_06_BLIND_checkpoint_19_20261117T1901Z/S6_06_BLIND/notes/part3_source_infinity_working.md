# The second boundary of the marked E7 source curve

We retain the actual marked source of SM.7 and the chord-normalized
linearization of the K39 working calculation. The following are exact
maps on a punctured parameter disc. They do not assign the completed
threefold return.

Put v=zeta^(-2). The holomorphic coordinate isomorphism on each nonzero
parameter fibre is
\[
 X=\zeta^{-2}X_\infty,\qquad
 Y=\zeta^{-3}Y_\infty,\qquad
 T=\zeta^{-4}T_\infty.
\]
It sends the source equation and marked section to
\[
 Y_\infty^2=X_\infty^3+(\zeta^2-2)X_\infty^2
              +T_\infty X_\infty+\zeta^2,
 \qquad G_\infty=(0,\zeta).
\]
All coefficients extend across zeta=0. The selected value becomes
\(T_{\infty,0}=1-2\zeta^2\), and its cubic factors literally as
\[
 (X_\infty-1)^2(X_\infty+\zeta^2).
\]
Its normalization is
\[
 X_\infty=s^2-\zeta^2,\qquad
 Y_\infty=s(s^2-\zeta^2-1).
\]
The double preimages are \(s=\pm\sqrt{1+\zeta^2}\). They remain
disjoint across the central parameter. The normalization map is an
immersion there: its s derivative has first component 2s, and at s=0
its second component is \(-(1+\zeta^2)\), a unit. The zero section
gives its smooth infinity point. Thus this selected normalization
surface is the literal product \(\mathbf P^1\times D_\zeta\).

At zeta=0 the source cubic discriminant is
\(4T_\infty^2(1-T_\infty)\). The unselected double discriminant
value is at T_inf=0 and the selected simple value remains T_inf=1.
The local simultaneous source resolution at the former is the same
rank-one matrix construction as in K39, through the exact coordinates
\[
 A=Y_\infty-\zeta,\quad B=Y_\infty+\zeta,\quad C=X_\infty,
 \quad D=T_\infty+X_\infty^2+(\zeta^2-2)X_\infty,
 \qquad AB=CD.
\]
The marked small resolution is A=Dz, C=Bz. Its projection to zeta is
the submersion \(\zeta=(B-Dz)/2\). The selected node lies in the
complementary chart, at A=-zeta, C=1, w=zeta, and hence misses this
exceptional curve.

The actual Hom factors are also retained. Define
\[
 F_{21,\infty}
  =\frac{Y_\infty+\zeta+(T_\infty/(2\zeta))X_\infty}{X_\infty},
 \qquad
 F_{12,\infty}
  =\frac{Y_\infty-\zeta-(T_\infty/(2\zeta))X_\infty}{X_\infty}.
\]
The previous factors obey \(F_{ab}=\zeta^{-1}F_{ab,\infty}\).
Since \(q=\zeta^{-4}q_\infty\), the actual linearization becomes
\[
 \phi_{ab}=\frac{q}{vF_{ab}}
       =\frac{\zeta^{-1}q_\infty}{F_{ab,\infty}}.
\]
At the selected node its factors are respectively
\(1/(2\zeta)\) and \(-1/(2\zeta)\). Hence
\(\phi_{21}/q_\infty=2\) and
\(\phi_{12}/q_\infty=-2\), with zero parameter winding. The leading
selected Tate coefficient is
\[
 \frac{q_T}{q_\infty}
   =-\frac1{64(1+\zeta^2)^3}+O(q_\infty).
\]
It is a nonvanishing unit on the parameter disc. The III-star Hom
limits are likewise 2 and -2, obtained directly from the displayed
T_inf-leading terms. These comparisons retain the original scalar.

The remaining morphism is the actual periodic suspension through the
unselected I2 component flop. An extending selected normalization and
its units do not supply that exterior suspension map. Its fixed data,
marked line and finite-cap boundaries remain part of this calculation.

The common suspension formula also has an exact comparison on the
punctured parameter disc. Identify the pullback of each actual source
Cartier line with its infinity-chart line by sending the canonical
meromorphic divisor section to the same section. Translation by the
marked G commutes with the displayed source coordinate isomorphism.
Since the primitive lift U_a has target multiplier X(p-G)^{-a}, this
line comparison gives
\[
 I_\zeta U_{a,\mathrm{old}}I_\zeta^{-1}
       =\zeta^{2a}U_{a,\infty}.
\]
The actual degree-two Cartier multiplier satisfies
r_old=\zeta^{-2}r_inf; its equal source and target factors cancel
when conjugating B. Hence the identity ab=2 gives the literal map
\[
 I_\zeta B_{a,b,\mathrm{old}}I_\zeta^{-1}
 =2(-1)^{b+1}\lambda q_\infty U_{a,\infty}^{,b}.
\]
The exponent is 2ab-4=0, so this comparison retains the original
scalar. Near the unselected I2 point q_inf is a unit with value -1.
The finite-cap root maps remain required: the source base coordinate
changes by T_old=\zeta^{-4}T_inf, so a root coordinate of order m
has the actual comparison z_old^m=\zeta^4 z_inf^m. The displayed
source-line map alone does not choose or close this root comparison.

The program code/part3_root/source_infinity_chart.py checks all the
displayed substitutions and leading coefficients exactly; its output
does not encode a sphere-return value.

The initial program compared factored symbolic expressions structurally;
its equivalent opposite-factor forms failed that check. The preserved
attempt is under code/part3_root/attempts/source_infinity_structural_comparison.
The corrected assertion checks their expanded polynomial difference.
