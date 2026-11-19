# E6: the complete marked-node coordinate and actual source rescaling

Working coordinate proof. The exact source, branch, line-weight and
selected-height maps below are recorded before the remaining source
attachments are assigned returns. The original family is
\[
 y^2=x^3+rx^2+tx+t^2,\qquad G=(0,t).
\]
Its two nonzero finite discriminant roots are marked by
\[
 \rho^2=1-3r,\qquad
 t_+(\rho)=\frac{1-3\rho^2+2\rho^3}{27}.
\]
The selected double root and its normalization constant are
\[
 u=\frac{2\rho^2-\rho-1}{9},\qquad
 b=\frac{(\rho-1)^2}{9},\qquad
 u+b=\frac{\rho(\rho-1)}3.
\]
Indeed the selected cubic is \((x-u)^2(x+b)\). With
\(x=s^2-b\), \(y=s(s^2-u-b)\), the section has
\(s(G)=(1-\rho)/3\). Thus the ordered nodal branches use the
actual square root of \(\rho(\rho-1)/3\).

## EN.1. A rational parameter for the ordered branch cover

Put
\[
 D=w^2-3,\qquad \rho=\frac{w^2}{D},\qquad
 r=\frac{3-2w^2}{D^2},\qquad
 t_+=\frac{w^2-1}{D^3}.
\]
The inverse branch relation is \(w^2=3\rho/(\rho-1)\).
The chosen normalization square root is exactly \(w/D\).
This gives the rational parametrization of the twofold ordered-node
cover, with its two signs retained by \(w\mapsto-w\).

On \(D\ne0\) use the actual source and base coordinate map
\[
 X=D^2x,\qquad Y=D^3y,\qquad T=D^3t.
\]
Its inverse divides by these same nonzero powers. Substitution gives
\[
 E_w:\quad
 Y^2=X^3+(3-2w^2)X^2+(w^2-3)TX+T^2,
 \qquad G=(0,T).
\]
The selected height is
\[
 q=T-(w^2-1),\qquad t-t_+=D^{-3}q.
\]
Writing \(v=w^2-1\), its selected normalization is literally
\[
 X=S^2-1,\qquad Y=S(S^2-w^2),\qquad
 Z=\frac{S-w}{S+w},\qquad P_G=\frac{1+w}{1-w}.
\]
Here the section is \(S(G)=-1\). The zero section has \(Z(O)=1\).
The chosen fourth root of the selected \(c_4\) is \(2w\), so
the branch marking is single valued on the punctured \(w\)-plane.
The full Tate period has the actual-height leading coefficient
\[
 Q=q\kappa,\qquad
 \kappa(0,w)=-\frac{(w^2-1)^2}{64w^6}.
\]
This follows from \(c_4|_{q=0}=16w^4\) and the derivative of the
full discriminant, so the powers of the selected height have been
retained. The higher terms are the actual inverse \(j\)-series.

## EN.2. Every finite source boundary in this parameter

The complete discriminant factorization is
\[
 \Delta=-432T^2(T-v)(T-T_-),\qquad
 T_-=-\frac{(3-2w^2)^2(w^2+3)}{27},
 \qquad v-T_- =\frac{4w^6}{27}.
\]
The following table records these exact parameter preimages. The
collision names refer to the source configurations analyzed in the
E6 collision notes; the displayed equations supply their locations.

| Parameter | Original marked value | Exact collision or coordinate boundary |
|---|---|---|
| \(w=0\) | \(\rho=0,r=1/3\) | The two selected-node branches meet the cusp; \(T_+=-1\), and their separation has order six. |
| \(w=\pm1\) | \(\rho=-1/2,r=1/4\) | The selected \(I_1\) joins the \(T=0\) fibre; \(T_+=0\). |
| \(w^2=-3\) | \(\rho=1/2,r=1/4\) | The unselected \(I_1\) joins the \(T=0\) fibre. |
| \(w^2=3/2\) | \(\rho=-1,r=0\) | The unselected III collision. |
| \(w^2=3\) | The original \(r\)-parameter is infinite | The displayed polynomial source is \(Y^2=X^3-3X^2+T^2\); its selected value is \(T=2\). |
| \(w=\infty\) | \(\rho=1,r=0\) | The selected III boundary on the ordered branch cover. |

The polynomial model at \(w^2=3\) is an actual continuation of the
displayed source equation. Its completed quotient, finite root and
annular comparison are to be checked with the same line multiplier
in EN.3; a source equation alone has not assigned a sphere return.

## EN.3. The whole Cartier-Miller scalar is preserved

For the more general literal source
\[
 y^2=x^3+(d^2/4-s)x^2+dt x+t^2
\]
put
\[
 U=y-t-dx/2,\quad V=y+t+dx/2,\qquad UV=x^2(x-s).
\]
The actual sections and Miller factors are
\[
 2G=(s,-t-ds/2),\qquad f_2=\frac{U}{x-s},
\]
\[
 x(3G)=\frac{4t^2}{s^2}+\frac{2dt}{s},\quad
 y(3G)=\frac{t(8t^2+6dst+d^2s^2-s^3)}{s^3},
\]
\[
 f_3=\frac{s x U}{sV-(ds+2t)x},\qquad
 f_6=f_3^2f_{2,3G}.
\]
The full factor \(f_3\) equals the actual chord-line Miller product
\(f_2\ell_{G,2G}/(x-x(3G))\); the equality holds as a rational
function on the source, with all base factors retained.

For the coordinate map in EN.1 the transformed coefficients are
\[
 d_{\rm new}=D,\qquad
 s_{\rm new}=\frac{(w^2-1)(w^2+3)}4,
\]
and \(d_{\rm old}=D^{-1}d_{\rm new}=1\),
\(s_{\rm old}=D^{-2}s_{\rm new}=1/4-r\). Substitution into the
complete rational factors gives
\[
 f_{2,\rm old}=D^{-1}f_{2,\rm new},\qquad
 f_{3,\rm old}=D^{-2}f_{3,\rm new},\qquad
 f_{6,\rm old}=D^{-5}f_{6,\rm new}.
\]
For the last equality the tangent quotient \(f_{2,P}\) has weight
one for the actual section \(P=3G\). Its slope, doubled point and
whole tangent numerator transform by their literal Weierstrass
coordinate powers. Thus its base factor is retained as well.

The source translation is conjugated by the displayed source map.
For its actual line coefficient
\[
 B_6(p)=f_2(p)^6\frac{f_6(p-G)}{f_6(p)},
\]
the two \(D^{-5}\) factors cancel in the ratio, giving
\(B_{6,\rm old}=D^{-6}B_{6,\rm new}\). The full selected-zero
Hom coefficient consequently obeys the exact identity
\[
 \frac{t-t_+}{t^3}B_{6,\rm old}
       =\frac{q}{T^3}B_{6,\rm new}.
\]
This equality includes every integer \(D\)-power. In divisor
frames the coordinate arrow is the pullback of the actual local
divisor equations; the rational Miller arrow \(f_6^{-1}\) is carried
with its displayed factor. No independent change of the suspension
scalar has been introduced.

The associated quadratic cap equation is
\[
 Y'^2=X'^3+z^2\bigl((3-2w^2)X'^2+D X'+1\bigr),\qquad G'=(0,z).
\]
Its actual source resolution, four fixed-point blowups and identity
\(\beta^*N_6=\pi^*M_6\) are recorded in E70--71 of
`part3_e6_order_three_source_working.md`. The remaining ordinary and
annular attachment must carry this exact multiplier and those maps.

## EN.4. Exact execution and current scope

`code/part3_root/e6_marked_node_cover.py` executes the full source and
height substitution, selected normalization, discriminant factors,
inverse-\(j\) coefficient, cA2 identity, actual Miller identities,
all scaling powers and boundary preimages. Its output records the
precise checks. The source-coordinate catalogue is available for the
remaining E6 attachments; their completed sphere returns are still
being derived in the separate attachment notes.
