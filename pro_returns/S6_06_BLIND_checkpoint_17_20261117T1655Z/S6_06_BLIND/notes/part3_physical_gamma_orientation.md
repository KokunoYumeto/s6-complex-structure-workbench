# Physical gamma and the orientation of the source page

Independent orientation audit, 17 November 2026.

Use physical source complex coordinates, and write the line
character as \(V=r e^{i\phi}\). The complex threefold orientation is
\[
 \operatorname{or}(X)=\operatorname{or}(S)\,dr\,d\phi .
\]
The physical delta circle is positive \(d\phi\). Moving its vector
past the four source vectors and the one radial vector gives
\[
 \operatorname{or}(Y)
                  =-\operatorname{or}(S)\,d\log r .   \tag{GO.1}
\]
Equivalently, if \(V=e^{2\pi i\zeta_2}\) and
\(\zeta_2=x+iy\), delta is the positive \(x\)-direction and the
orbit orientation is \(\operatorname{or}(S)\,dy\).

For the actual contracting suspension
\[
 B(a,V)=(a-g,\ e^{2\pi iC}q r_0^m V),
\]
where \(r_0\) now denotes the family parameter, the inward period
is
\[
 \gamma_{\rm in}=(-g,C+s+mv),\qquad
 s=\frac{\log q}{2\pi i},\quad
 v=\frac{\log r_0}{2\pi i}.
\]
Its positive direction decreases the physical line radius.
Thus (GO.1) is source-page-first followed by
\(\gamma_{\rm in}\). For the inverse period
\(\gamma_{\rm out}=-\gamma_{\rm in}\), it is the negative of
source-page-first followed by \(\gamma_{\rm out}\).
This is an orientation calculation in the physical coordinates;
it is not a relabeling of a chosen generator.

For OS45 the cap map is explicitly cap-to-ordinary:
\[
 \Psi_v(\zeta,t)=\zeta+
             \frac{\log t}{2\pi i}\gamma_{\rm in}(v).
\]
A positive cap meridian becomes the ordinary base meridian plus
\(\gamma_{\rm in}\). The ordinary and cap parameter decks are
\[
 D_{\rm ord}=-\frac{\log((t-t_c)/t)}{2\pi i}\delta,\qquad
 D_{\rm cap}=-\frac{\log(t-t_c)}{2\pi i}\delta.
\]
Since \(\gamma_{\rm in}(v+1)-\gamma_{\rm in}(v)=\delta\),
they satisfy the literal square
\[
 D_{\rm ord}\Psi_v=\Psi_{v+1}D_{\rm cap}.
\]
Near the cusp this is the deck \(-s\delta\) in P3K.10.
Its two extending origins have differences
\(\Delta o=-s\delta\) and
\(\Delta\sigma=-s\delta+\gamma_{\rm in}\).
Because the local coordinates are \(\zeta-o\) and
\(\zeta-\sigma\), their cusp-to-ordinary transition is
\(\sigma-o\), with positive angular increment
\(\gamma_{\rm in}\). The actual positive scalar loop therefore
has the positive source-page orientation required in P3K.7.
The OS45 index \(-3\) and the primitive-source signs of P3K.22
are unchanged.

For the corrected reduced-III construction, the declared
ordinary-to-cap map instead gives cusp deck \(+s\delta\), and
the corrected origin difference is a positive turn of
\(\gamma_{\rm out}=B^{-1}\). Its weighted-S3 map sends that
outward period to the positive Hopf circle. Equation (GO.1)
then says that the product of its complex source page with that
Hopf orientation is opposite the actual orbit orientation.
This observation alone does not determine the return sign.
The following normal-sphere calculation retains the actual
boundary and meridian orientations and completes the comparison.

## The signed boundary-degree version of P3K.7

Orient the graph page by its complex source orientation. Define
\(\kappa\in\{1,-1\}\) by the actual boundary parametrization
\[
                  \partial V=\kappa\,E\times S^1_\theta ,
\]
where \(\theta\) is the positive physical parameter direction
of the angular trace. Orient the compression by
\(\partial W=F-E\). Its product with the parameter circle
must then be attached with orientation \(\kappa\); hence
\[
                         \partial X=\kappa F\times S^1_\theta .
\]

The fixed-circle quotient orientation is the one already
calculated in P3K.7:
\[
 \operatorname{or}(Y)=
       \operatorname{or}(F)\operatorname{or}(\nu_{\rm Hopf}).
\]
On the outer radial collar of \(Z=Y\times D^2\), this is
\[
 \operatorname{or}(Z)=
       \operatorname{or}(F)\operatorname{or}(\nu_{\rm Hopf})
                   \,dr\,d\theta .
\]
The trace has orientation
\(\kappa\,\operatorname{or}(F)\,dr\,d\theta\).
Moving the three normal vectors past the two radial/parameter
vectors introduces no sign. Consequently the induced oriented
normal three-plane is \(\kappa\nu_{\rm Hopf}\).
The actual Euler line \(x\) therefore has
\[
                         \pi_*x=\kappa
\]
on the oriented normal sphere bundle, not an automatically
positive fibre integral.

Put \(\widehat x=\kappa x\), so \(\pi_*\widehat x=1\), and define
\(b\) by \(e_v=2\widehat x-\pi^*b\).
The graph section has zero vertical Euler class, so
\(b|_V=2\kappa c_1(M)\). Its square is \(4M_{\rm rel}^2\),
independent of \(\kappa\). The two bordism-boundary reversals
and Jin's inverse mapping-torus convention remain exactly as
in P3K.7. Fibre integration therefore gives
\[
 \begin{aligned}
 A_{\rm Jin}
  &=\frac{4\int_Bx^3-\int_Bp_1(TB)x}{24}\\
  &=\kappa\,
      \frac{3\int_{\bar X}b^2-\int_{\bar X}p_1(T\bar X)}{24}.
                                                        \tag{GO.2}
 \end{aligned}
\]
This calculation identifies the sign with the actual boundary
degree \(\kappa\); an ambient/product-orientation comparison
without the normal meridian does not supply it.

For the corrected reduced-III weighted page,
\(t=t_*+a^{-m}\). Its compact affine page has complex boundary
given by positive \(\arg a\) at large \(|a|\).
In the explicit embedding
\((a,b)\mapsto(\rho a,\rho^m b)\), \(b-t_*a^m=1\),
the positive Hopf parameter \(\gamma_{\rm out}\) is precisely
that positive \(\arg a\) direction at the binding.
The corrected origin computation makes the positive
parameter turn \(+\gamma_{\rm out}\). Thus \(\kappa=+1\).
Equation (GO.2) retains the negative value
\[
                    A=-(3m-1)/4
\]
for that construction. The OS45 cap-to-ordinary construction
likewise has \(\kappa=+1\), with its inward gamma.
The earlier suggestion that the ambient reversal by itself
would invert the reduced-III index was incomplete; the
explicit meridian calculation above supplies the full sign.
