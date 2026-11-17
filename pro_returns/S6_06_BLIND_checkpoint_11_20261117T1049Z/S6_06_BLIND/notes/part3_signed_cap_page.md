# The actual page and Thom sign for the two primitive cap twists

Independent signed calculation for the ordinary-to-cap constructions
with \(n=1\) and \(n=-1\). The source root, its actual line, and
its contractions are retained from the corresponding cap proof.
This note establishes the map and its orientation; it does not
replace a source-line correspondence by its numerical square.

## The two marked solid-torus maps

Let \(q_\infty=z^m\), and use the actual norm coordinate
\[
        u=m\gamma_{\rm out}
                   -n\,\frac{\arg q_\infty}{2\pi},
        \qquad n\in\{1,-1\}.
\]
The cap base is
\[
 (D_z\times(\mathbb R/m\mathbb Z))/
       \bigl((z,u)\sim(\zeta_m z,u-n)\bigr).
\]
The cyclic action is free, including at \(z=0\).
Let \(R>0\) be the unique solution of
\[
                      R^2+|z|^2R^{2/m}=1.
\]
The marked smooth map into the weighted solid torus in \(S^3\) is
\[
 (z,u)\longmapsto
 (z_1,z_2)=
 \bigl(zR^{1/m}e^{2\pi i n u/m},
                       R e^{2\pi i n u}\bigr).
                                                        \tag{SCP.1}
\]
It is invariant under the displayed cyclic action because
\(n^2=1\). The radial equation has positive derivative, so
the map is smooth. Its inverse is explicit: take
\(R=|z_2|\), choose any of the \(m\) lifts of
\(e^{2\pi i n u}=z_2/|z_2|\), and put
\[
                  z=z_1R^{-1/m}e^{-2\pi i n u/m}.
\]
Changing the lift of \(u\) by one applies the given cyclic
action to the resulting representative. Thus this is a
diffeomorphism onto the named solid torus, with the original
base map
\[
                      t=z_2/z_1^m=q_\infty^{-1}.
                                                        \tag{SCP.2}
\]
On the ordinary overlap, write
\(\alpha=\arg(q_\infty)/(2\pi)\). The two angular coordinates
of (SCP.1) are
\[
 \arg(z_1)/(2\pi)=\alpha/m+n u/m=n\gamma_{\rm out},
 \qquad
 \arg(z_2)/(2\pi)=n u=nm\gamma_{\rm out}-\alpha.
                                                        \tag{SCP.3}
\]
Consequently the positive weighted Hopf coordinate is
\(\beta=n\gamma_{\rm out}\). This is an equality of the
actual marked circle coordinates, not a choice of its sign.

## The complex page and its actual boundary degree

Use a regular binding value \(t_*\). The affine complex page
is the Milnor page
\[
                         b-t_*a^m=1.
\]
Its radial embedding in \(S^3\) is
\((a,b)\mapsto(\rho a,\rho^m b)\), with \(\rho>0\) uniquely
chosen to put the point on the unit sphere.
Its projection is \(t=b/a^m=t_*+a^{-m}\). On the root chart,
the exact page graph has equation
\[
       n u+\frac{\arg(1-t_*z^m)}{2\pi}
                     =\frac{\phi}{2\pi}\pmod{\mathbb Z}.
                                                        \tag{SCP.4}
\]
It has \(m\) sheets in the length-\(m\) circle. The actual
cyclic action sends their sheet number to the preceding one,
for both signs of \(n\). Choosing one sheet therefore gives
the actual source-root slice. For the displayed affine page
we take \(\phi=0\); any other fixed phase is the indicated
constant weighted-circle rotation. The corresponding complex page
coordinate is determined by
\[
                 a^m=\frac{z^m}{1-t_*z^m},
                 \qquad b=\frac1{1-t_*z^m},
                                                        \tag{SCP.5}
\]
with the marked branch. These are holomorphic coordinates,
and they are independent of the sign of \(n\). In particular
the page is oriented by that actual complex source slice.

The actual two-origin calculation for these constructions
gives the positive parameter loop as \(n\gamma_{\rm out}\),
with the retained scalar gauge. By (SCP.3) it is one positive
\(\beta\)-turn for both \(n=1\) and \(n=-1\).
The complex boundary of the page has positive \(\arg a\)
orientation, which is the positive weighted Hopf direction
at the regular binding. Thus, with \(\theta\) the physical
positive parameter coordinate,
\[
                         \partial V=+E\times S^1_\theta.
                                                        \tag{SCP.6}
\]

## The normal Thom sign

The ambient orbit orientation in source coordinates may be
opposite the one induced by (SCP.1). It cannot be inserted
as an extra sign independently of the normal orientation.
Retain the actual fixed-curve Hopf chart instead.
Orient the real compression by \(\partial W=F-E\).
Equation (SCP.6) requires the positive product orientation
on \(W\times S^1_\theta\) when attaching it to the graph
page. The resulting trace has
\[
                            \partial X=+F\times S^1_\theta.
\]
In the oriented ambient \(Z=Y\times D^2\), the local
orientation is
\[
              {\rm or}(F)\,{\rm or}(\nu_{\rm Hopf})
                                   \,dr\,d\theta .
\]
The oriented trace tangent is
\({\rm or}(F)\,dr\,d\theta\). Moving the three normal
directions past the two radial and angular directions has
positive sign. Hence the oriented normal three-plane is
the positive Hopf normal model for both signs of \(n\).
For the actual circle line \(x\),
\[
                                \pi_*x=+1.
                                                        \tag{SCP.7}
\]
This is the signed calculation GO.2 with \(\kappa=+1\);
the two ambient bordism reversals and Jin's inverse
mapping-torus convention are exactly those already retained
in K7.

For each of these actual cap constructions, after its proved
source-to-page line correspondence is used, the signed
return formula is therefore
\[
             A=\frac{12M_{\rm page}^2-p_1(TS_{\rm page})}{24}.
                                                        \tag{SCP.8}
\]
Its sign is the same for the two primitive twists.
For the whole-fibre zero families whose retained page line
has no component correction, this is
\[
                   A=\chi(\mathcal O_{S_{\rm page}})
                                      -\frac{m a^2}{2d}.
                                                        \tag{SCP.9}
\]
The actual line correspondences, including the good-root
exceptional corrections, remain part of the proof of each
family. The present normal calculation introduces no
additional sign when \(n=-1\).

The cyclic and circle-coordinate identities and the
orientation parity are executed in
code/part3_fourfold/signed_cap_page.py.
