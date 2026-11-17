# P3K.46. The actual characteristic pair on the reflected cusp fan

Proved after complete root audit and independent RC.1--3 audit,
17 November 2026. We retain exactly
the selected-cusp family, fixed scalar, III-star cap, positive rho loop
and initial fan of P3F.54/P3F.56. Let \(T'=J(T)\) be the reflected fan
of P3K.45, obtained by flopping its nonfixed diagonal edge \(C_2\).
In the actual fixed-edge Cox products, the reflected return has
\[
 (k,\ell)=(6,0),\qquad
 (m_{C_0},n_{C_0},s)=(0,-6,1).
\]
The subscripts specify the retained fixed edge \(C_0\). We do not assign
the separate relative integers at \(C_2\), or a formula for other fans.
The proof constructs the circle-equivariant map of the completed
mapping-torus quotients; it does not infer the pair from the oriented
conjugacy class.

## RC.1. The fixed-edge chart map after the actual source period

We use the physical height coordinate \(q\), as in P3K.42. Write
\(q_T=\kappa(q,\rho)q\), retaining the actual unit \(\kappa\) and its
rho winding. In the first chart of the initial fixed edge, put
\[
 Z=z,\qquad V=c_1,\qquad q=z c_0c_1.                 \tag{RC.1}
\]
Its second chart has coordinate \(z^{-1}\) and normal coordinates
\(z c_0,z c_1\), after the actual source-period reindex and its
retained units. These are precisely the two fixed-edge products used
in P3K.40 and P3K.42.

The reflected triangles are
\((0,e_1,e_1+e_2)\) and \((0,e_2,e_1+e_2)\). Their affine toric
coordinates are, respectively,
\[
 \left(\frac qZ,\frac ZV,V\right),\qquad
 \left(\frac qV,\frac VZ,Z\right).                  \tag{RC.2}
\]
Thus the reflected fixed edge at \([0,e_2]\) has first chart
\[
 z'=Z',\qquad d_0=\frac q{V'},\qquad
 d_1=\frac{V'}{Z'},\qquad q=z'd_0d_1.              \tag{RC.3}
\]
The adjacent translate of the first triangle has tangent coordinate
\((z')^{-1}\) and normal coordinates \(z'd_0,z'd_1\).
In particular its actual normal transition is again multiplication
by its displayed fixed-curve coordinate.

The half-source family map proved in P3K.45 is
\[
 (Z,V,q_T,\rho)\longmapsto(q_T/Z,V,q_T,-\rho).
                                                               \tag{RC.4}
\]
It carries the vertical edge at \(0\) to the vertical edge at \(e_1\).
Let the target source period, in the target marking, be
\[
 h_{\rm tar}(Z',V',q)
       =(\kappa qZ',\alpha(q,\rho)V',q).             \tag{RC.5}
\]
Here \(\alpha\) means the target line multiplier, including the inverse
Picard marking produced by the half-source continuation. It is the
actual nonzero source-period unit from P3F.54. We do not replace it by
the source multiplier with its old marking. Composing (RC.4) with the
literal inverse of (RC.5) gives
\[
       (Z,V,q)\longmapsto(Z^{-1},\alpha^{-1}V,q).
                                                               \tag{RC.6}
\]
The cancellation of \(\kappa\) in (RC.6) is the equality
\((q_T/Z)/(\kappa q)=Z^{-1}\). Its winding has been retained in both
maps before this composition.

Substitution in (RC.3), using (RC.1), gives the fixed-edge arrow
\[
 z'=z^{-1},\qquad
 d_0=\alpha z c_0,\qquad d_1=\alpha^{-1}z c_1.
                                                               \tag{RC.7}
\]
In the second target chart this is
\[
 (z')^{-1}=z,\qquad z'd_0=\alpha c_0,
                   \qquad z'd_1=\alpha^{-1}c_1.       \tag{RC.8}
\]
Consequently the map extends over both endpoints of the fixed curve.
It preserves the physical height exactly:
\(z'd_0d_1=z c_0c_1\). It also preserves the physical delta action,
whose normal weights are \((-1,+1)\).

The coordinates in (RC.1) on the fixed curve agree with the ordered
normalization coordinate \(z=(s-\rho)/(s+\rho)\) of P3K.40/P3K.42:
both use the same two ordered branches and send the zero section to
\(z=1\). The target uses its continued branch order. Thus (RC.7) is
an arrow between the specified fixed-edge products, including their
source coordinate; it is not an unidentified bundle isomorphism.

## RC.2. Its literal Cox product and extension over the cap

Only the normal derivative of (RC.7) enters its normal-sphere product.
We retain the actual nonlinear unit by the explicit homotopy
\[
 \alpha_t(q,\rho)=\alpha(t^2q,\rho),\qquad 0\le t\le1.
                                                               \tag{RC.9}
\]
On a uniformly small height disc all these functions are nonzero.
Equations (RC.7)--(RC.8) with \(\alpha_t\) are invertible,
delta-equivariant and preserve \(q\); at \(t=0\) the unit is
\(a(\rho)=\alpha(0,\rho)\). We next use the exact diagonal homotopy
\(a_s=a|a|^{-s}\), \(0\le s\le1\), in those same equations.
It ends at the closed circle-valued function
\[
                         \tau(\rho)=a(\rho)/|a(\rho)|. \tag{RC.10}
\]
No logarithm or square root of this function is chosen. Any winding
is retained.

Use the homogeneous Cox coordinates \((a_0,a_1;b_0,b_1)\) with
auxiliary equivalence
\((a,b)\sim(e^{i\phi}a,e^{-i\phi}b)\). On the chart \(a_0\ne0\),
the local source coordinate is \(z=a_1/a_0\), and the local normal
coordinates are \(c_i=a_0b_i\). The unitary version of (RC.7) is
therefore exactly
\[
 (a_0,a_1;b_0,b_1)
       \longmapsto(a_1,a_0;\tau b_0,\tau^{-1}b_1).
                                                               \tag{RC.11}
\]
Indeed its target local normal coordinates are
\(a_1\tau b_0=\tau zc_0\) and
\(a_1\tau^{-1}b_1=\tau^{-1}zc_1\), as required.

Keep the same quaternion convention and the same ordered normal
coordinates as in P3K.40/P3K.42:
\[
 u=a_0+ja_1,\qquad v=b_0+j\overline{b_1},\qquad
 h=uiu^{-1},\qquad q_H=uv.
\]
Set \(r=ji\) and \(d=-i\). Literal multiplication gives
\[
 r(a_0+ja_1)d=a_1+ja_0,
 \qquad
 \tau b_0+j\overline{\tau^{-1}b_1}=v\tau.
                                                               \tag{RC.12}
\]
Hence (RC.11) acts on the actual product as
\[
 (h,q_H)\longmapsto
 \left(rhr^{-1},\;r\exp(-\pi h/2)q_H\tau(\rho)\right).
                                                               \tag{RC.13}
\]
To obtain the second entry we use the exact equality
\(udu^{-1}=\exp(-\pi h/2)\), with \(d=\exp(-\pi i/2)\).
This retains the determinant of the constant interchange of the two
Cox source coordinates. It is not replaced by a different lift of
that projective map.

Formula (RC.13) has the following explicit extension over the
actual product cap:
\[
 \begin{aligned}
 D^3\times S^3\times S^1_\rho&\longrightarrow
                  D^3\times S^3\times S^1_\rho,\\
 (y,q_H,\rho)&\longmapsto
 \left(ryr^{-1},\;r\exp(-\pi y/2)q_H\tau(\rho),\;-\rho\right).
 \end{aligned}                                               \tag{RC.14}
\]
Its inverse first takes \(y=r^{-1}y'r\), and then takes
\(q_H=\exp(\pi y/2)r^{-1}q'_H\tau(\rho)^{-1}\), with
\(\rho=-\rho'\). Thus it is a smooth diffeomorphism, including
\(y=0\). The base map is an orientation-preserving real rotation;
the fibre map is left and right multiplication by unit quaternions.
The positive rho-circle is carried to its positive half rotation.
It follows that (RC.14) preserves all the product orientations used
in the completion.

The physical Hopf action is \(q_H\mapsto q_He^{-i\theta}\).
Since \(\tau(\rho)\) is complex, (RC.14) commutes with this action
with its given orientation. It therefore descends to a map of
\(D^3\times S^2\times S^1_\rho\) and is an isomorphism of the
actual principal circle bundles above that map. In particular the
meridian Euler class is preserved, with sign \(+1\).

The homotopies (RC.9)--(RC.10) also give maps of the original
completions, not just their linear models. More explicitly, for each
homotopy of the boundary maps we take its velocity
\((\partial_tF_t)F_t^{-1}\), multiply it by a collar cutoff which is
one at the inner boundary and zero at the outer boundary, and
integrate this time-dependent vector field. It is periodic in rho
and delta-equivariant. Its flow supplies the required collar
diffeomorphism and transports the same principal circle bundle.
Thus composing (RC.14) with that flow extends the original boundary
map (RC.7), with all its units.

## RC.3. The completed quotient and its characteristic numbers

Let \(E_T\) and \(E_{T'}\) denote the complements of the fixed tubes
in the two actual families over the rho-circle. P3K.45 supplies the
literal isomorphism
\[
       E_{T,\rho}\longrightarrow E_{T',-\rho},       \tag{RC.15}
\]
including its finite cap and every ordinary annulus. It is
delta-equivariant and orientation-preserving. On the tube boundary,
(RC.15) is exactly the map calculated in RC.1. Use the collar flow
just constructed so that it matches (RC.14) on the attached cap.
We thereby obtain a map of the actual glued total spaces, not only
of a single fibre or of their homology groups.

Divide by the physical circle and attach
\(D^3\times S^2\times S^1_\rho\) in the same Cox product. Denote
this physical positive-parameter completion by \(P_T\), and denote
the corresponding reflected completion by \(P_{T'}\). The preceding
maps glue to an oriented diffeomorphism
\[
              \widehat I:P_T\longrightarrow P_{T'},
       \qquad \widehat I^*x^P_{T'}=x^P_T.            \tag{RC.16}
\]
Here \(x^P_T,x^P_{T'}\) are the Euler classes of the actual meridian
lines. The pullback identity follows from the explicitly equivariant
principal-bundle map in RC.2 and its identical map on the exterior.
Periodicity of (RC.14) is what makes (RC.16) a map of the completed
mapping-torus quotients. Equivalently, one may choose the mutually
transported connections of P3K.45; the fibre arrows then give the
same glued map with the displayed positive half rotation of the
parameter circle.

For the positive physical returns \(f_T,f_{T'}\), P3K.42 gives
\(P_T=M_{f_T^{-1}}\) and \(P_{T'}=M_{f_{T'}^{-1}}\) in Jin's
endpoint convention. In particular the proved pair of \(P_T\) is
\((-6,0)\). Naturality applied directly to (RC.16) first gives that
same physical pair on \(P_{T'}\).

Now put \(N_T=M_{f_T}\) and \(N_{T'}=M_{f_{T'}}\). These are obtained
from their respective physical completions by the same reversal of
the parameter circle, carrying the meridian line unchanged. Each
reversal changes the six-manifold orientation and both characteristic
numbers. Conjugating (RC.16) by these two actual parameter reversals
gives an orientation-preserving map \(N_T\to N_{T'}\), still with
pullback of the meridian Euler class equal to the original class.
Thus, writing those classes as \(x_T,x_{T'}\), we obtain the exact
integer equalities
\[
 \begin{aligned}
 \langle x_{T'}^3,[N_{T'}]\rangle
       &=\langle x_T^3,[N_T]\rangle,\\
 \langle p_1(N_{T'})x_{T'},[N_{T'}]\rangle
       &=\langle p_1(N_T)x_T,[N_T]\rangle.
 \end{aligned}                                               \tag{RC.17}
\]
P3K.42 evaluates the right-hand sides as \((6,0)\). This proves the
stated reflected pair. Its index is consequently \(A=(4k-\ell)/24=1\),
in agreement with the independent oriented conjugacy calculation
of P3K.45.

Finally the actual fixed-edge product is the one retained throughout
RC.1--RC.3. The exact fixed-edge identities of P3K.23/P3K.42 therefore
give
\[
        n_{C_0}=-6A=-6,\qquad
        m_{C_0}=6A-k=0,\qquad s=1\pmod {28}.         \tag{RC.18}
\]
These are the relative coordinates for \(C_0\) in the reflected fan.
No relative integer for its flopped nonfixed edge \(C_2\) is obtained
by this calculation.

The exact certificate is code/part3/source_cusp_reflected_pair.py,
with its JSON and captured output. It verifies the chart maps,
source-period cancellation, quaternion interchange, physical-circle
commutation and the stated characteristic-number arithmetic.
