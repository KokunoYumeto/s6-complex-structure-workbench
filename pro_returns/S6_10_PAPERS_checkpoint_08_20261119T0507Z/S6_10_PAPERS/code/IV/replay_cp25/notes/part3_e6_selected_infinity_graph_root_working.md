# Exact root graph chart at the E6 selected-infinity boundary

Retain the actual source rescaling EI.1–8, epsilon=1/w and
d0=1-3epsilon^2. The ordinary infinity coordinates satisfy

\[
 q_{\rm orig}=d_0^3\epsilon^{-4}q_{\rm new},\qquad
 q_{\rm new}=z_{\rm new}^m,
 \quad z_{\rm orig}=d_0^{3/m}\epsilon^{-4/m}z_{\rm new}.
\]

The roots of d0 are fixed on its nonzero disc. The closure of this
base-coordinate graph is the normalized blowup graph of the ideal
(epsilon^4,z_new^m). Its distinguished valuation ray is
(m/g,4/g), g=gcd(m,4). The cover

\[
 \epsilon=\eta^m,\qquad z_{\rm new}=\eta^4\zeta
\]

maps holomorphically to its normalized graph chart and carries the
original root coordinate to z_orig=d0^(3/m) zeta. The inverse on
eta nonzero is the displayed division by eta^4; the full finite
eta-root action is retained at eta=0.

For m=3l, l>=1, the good-root coordinates are
X_new=z_new^(2l)x_new, Y_new=z_new^(3l)y_new. The literal map is

\[
 X_{\rm orig}=\epsilon^{-2/3}X_{\rm new},\quad
 Y_{\rm orig}=\epsilon^{-1}Y_{\rm new},\qquad
 X_{\rm new}=\eta^{2l}U,\quad Y_{\rm new}=\eta^{3l}V,
 \quad (X_{\rm orig},Y_{\rm orig})=(U,V).
\]

For m=3l+2, l>=0, the reduced-root coordinates use exponents
2l+2 and3l+3. The map is

\[
 \begin{split}
 X_{\rm orig}&=d_0^{2/m}\epsilon^{-2(l+2)/m}X_{\rm new},\\
 Y_{\rm orig}&=d_0^{3/m}\epsilon^{-3(l+2)/m}Y_{\rm new},\\
 X_{\rm new}&=d_0^{-2/m}\eta^{2(l+2)}U,\qquad
 Y_{\rm new}=d_0^{-3/m}\eta^{3(l+2)}V.
 \end{split}
\]

Thus (U,V,z_orig) are precisely the original K96 root coordinates
on this graph chart, over r=epsilon^2(3epsilon^2-2)/d0^2. This
statement concerns the displayed graph chart. The complementary
zeta-infinity corner, the Cartier graph and the complete cap groupoid
remain to be constructed.

For xi^m=1, the complete deck action is eta -> xi eta,
zeta -> xi^(-4) zeta, with (U,V) weights (-2l,-3l) in the good
case and (-2(l+2),-3(l+2)) in the reduced case. The original root
weights give exactly D^(-4): the exponent differences are integer
multiples of m, as checked by the literal formulas in
code/part3_root/e6_selected_infinity_graph.py. At a generic point
of eta=0, the retained inertia has order g; no division by this
finite group is omitted. The finite eta cover and the primitive
graph ray are related by these actual coordinate and deck maps.

The fixed original root disc |z_orig|<delta has the exact pulled-back
domain |z_new|<delta |epsilon|^(4/m)|d0|^(-3/m). It supplies that
shrinking collar. A fixed native bidisc at the joint origin requires
the remaining graph charts and cap arrows recorded above.
