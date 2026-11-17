# Actual signed returns for the one-cap additive families

P3K.26: completed actual source, line, parameter and signed Thom proof.
The root audit passed the corrected integral coinvariant argument,
and fourfold independently checked both norm signs. This applies to
the actual constructions of P3F.37 and the complementary starred,
ordinary III/IV and II caps of F41--43. Their sole logarithmic
norm is \(n=1\) or \(n=-1\). The actual parameter is
\(\lambda=r^m\), with one positive loop in the punctured
\(r\)-disc. Both norm signs have the same oriented return
integer in the table below. The proof retains the arrows, source
line diagrams, and normal Thom orientation for each sign.

## AR.1. Physical characters and the complete parameter square

Move the capped source value to infinity and denote the selected
scalar-zero nodal value by \(t_c\). Near that cusp write
\(q=t-t_c\), \(s=\log q/(2\pi i)\), and
\(v=\log r/(2\pi i)\). In physical characters the source
Abel coordinate is \(a=\zeta_1\) and the scalar line coordinate
is \(V=e^{2\pi i\zeta_2}\). Let \(g\) be the marked Abel
logarithm of \(Q=bG\). The actual suspension map is
\[
 B_\lambda(a,V)=(a-g,e^{2\pi iC}qr^mV),\qquad
 \gamma_{\rm out}=(g,-C-s-mv),\qquad \delta=(0,1).
                                                        \tag{AR.1}
\]
Thus \(B_\lambda\) is translation by \(-\gamma_{\rm out}\),
and \(\gamma_{\rm out}=B_\lambda^{-1}\) is exactly the
outward loop used in the cap meridian. Delta is positive physical
line rotation. The functions \(g,C\) have bounded holomorphic
characters in the specified nodal chart; their constants and
any fixed line character are retained.

The annular arrow is \(F_c:\text{ordinary}\to\text{cap}\),
where \(c=\log\lambda/(2\pi i)\). Its scalar variation is
\(n(c-c_0)s_\infty\delta/m\), as follows directly from
the positive \(A_r\) root cut. At \(c\mapsto c+m\) the
cap is identical. The inverse closing \(c+m\to c\) is
\(F_c^{-1}F_{c+m}\), whose global multiplier is
\((t-t_c)^{-n}\). Its positive deck is consequently
\[
              (v,\zeta)\longmapsto(v+1,\zeta+n s\delta).
                                                        \tag{AR.2}
\]
This is fixed by the actual ordinary-to-cap arrow, including its
base unit; it is not deduced from a later orientation convention.

On the auxiliary cusp cover \(q=Q_0^{2m}\), use the two
extending origins
\[
\begin{split}
 o_n(s,v)&=n\bigl(-gs/m,\ Cs/m+s^2/(2m)+sv\bigr),\\
 \sigma_n(s,v)&=n\bigl(gv,\ -Cv-m(v^2-v)/2\bigr).
\end{split}                                             \tag{AR.3}
\]
They satisfy the exact identities
\[
\begin{split}
 o_n(s,v+1)-o_n(s,v)&=n s\delta,\\
 \sigma_n(s,v+1)-\sigma_n(s,v)&=n s\delta+n\gamma_{\rm out},\\
 o_n(s+2m,v)-o_n(s,v)&=-2n\gamma_{\rm out}+2mn\delta,\\
 \sigma_n(s+2m,v)-\sigma_n(s,v)&=0.
\end{split}                                             \tag{AR.4}
\]
The characters of \(\sigma_n\) are bounded units for either
sign, so they extend in the actual Mumford charts. The ordinary
origin removes (AR.2). On their common punctured collar their
difference is the explicit translation
\[
 F_n=\sigma_n-o_n
 =n\left(g(s/m+v),-C(s/m+v)-\frac{(s+mv)^2}{2m}+\frac{mv}{2}\right).
\]
Its angular change is
\[
 F_n(s,v+\theta)-F_n(s,v)
   =n\theta\gamma_{\rm out}
                   -\frac{nm}{2}\theta(\theta-1)\delta.  \tag{AR.5}
\]
The quadratic line gauge vanishes at both endpoints. The whole
displayed difference changes under \(s\mapsto s+2m\) by
\(-2mn\theta\delta\), an integral retained line winding.
On the orbit the actual positive \(r\)-loop is therefore
\(n\gamma_{\rm out}\). The auxiliary root is in the cusp
base and does not replace this loop by a parameter cover.

Changing the root of the norm unit by \(\zeta_m^d\) adds a
fixed delta character to the cap. Its actual graph line is still
the norm sphere of \(N\); that character is retained in the
sheet identifications. It is independent of \(v\), so it cancels
in (AR.2)--(AR.5). The affine and line conjugations of F44 are
also independent of \(r\), preserve \(B_0\), and transport
the annular map. Thus the same identities apply after those
exact local comparisons, without dropping their boundary gauges.

## AR.2. The signed Seifert map and the actual complex page

Use the actual root coordinate \(q_\infty=z^m\) and the
cap norm coordinate
\[
 u=m\gamma_{\rm out}-n\frac{\arg q_\infty}{2\pi}.
\]
Its quotient relation is
\((z,u)\sim(\zeta_mz,u-n)\), with \(u\) of period \(m\).
For both signs let \(R>0\) solve
\(R^2+|z|^2R^{2/m}=1\). The actual map is
\[
 (z,u)\longmapsto(z_1,z_2)=
 \left(zR^{1/m}e^{2\pi i n u/m},R e^{2\pi i n u}\right).
                                                        \tag{AR.6}
\]
It is invariant under the quotient relation because \(n^2=1\).
The positive derivative of the radial equation and the inverse
\(R=|z_2|\), followed by a lift of its argument and
\(z=z_1R^{-1/m}e^{-2\pi inu/m}\), prove that it is a smooth
marked solid-torus diffeomorphism. Changing the lift is exactly
a power of the original root action. Its base projection is
\[
 t=z_2/z_1^m=q_\infty^{-1}.
\]
On the ordinary base disc the same map is
\(z_1=\rho e^{2\pi in\gamma_{\rm out}}\),
\(z_2=t z_1^m\), with the unique positive \(\rho\) satisfying
\(\rho^2+|t|^2\rho^{2m}=1\). The two displayed maps agree
on the overlap by the exact equation for \(u\). They identify
the actual three-dimensional orbit-base gluing with \(S^3\),
not merely its abstract Seifert invariants.

The positive weighted Hopf coordinate is
\[
                         \beta=n\gamma_{\rm out}.       \tag{AR.7}
\]
Choose a regular binding value \(\tau\). The affine complex
page \(\eta-\tau\xi^m=1\) embeds in this sphere by
\((\xi,\eta)\mapsto(\rho\xi,\rho^m\eta)\), where \(\rho>0\)
puts it on the sphere. Its projection is
\[
                         t=\tau+\xi^{-m}.                \tag{AR.8}
\]
The compactified page base is \(\mathbb P^1_\xi\). It is
ramified to order \(m\) at the additive cap and at the
regular binding, and it is unramified at the selected nodal
cusp and at every other source singular fibre. In particular
the selected cusp contributes \(m\) separate \(I_1\) fibres.

The root-chart page equation is
\[
 n u+\frac{\arg(1-\tau z^m)}{2\pi}=\frac\phi{2\pi}
                                  \pmod{\mathbb Z}.     \tag{AR.9}
\]
Its \(m\) sheets are cyclically permuted by the actual
\(A_r\), which decreases the sheet index by one for either
norm sign. Choosing sheet zero gives the exact source-root
slice. For phase zero the page coordinates satisfy
\[
 \xi^m=\frac{z^m}{1-\tau z^m},\qquad
 \eta=\frac1{1-\tau z^m}.                                 \tag{AR.10}
\]
These are holomorphic, independent of \(n\). Thus the page
inherits the actual complex source orientation for both signs.

## AR.3. The actual root line, finite-base torsor, and square

On the cap, the sheet-zero map is
\(p\mapsto[p,u_0(z(p))]\) on the complete resolved root
surface, including its exceptional components and tangencies.
Every root sheet has a unique representative in this one. Indeed
a relation taking the same norm level to itself has
\(nk+mh=0\), hence \(k=mj,h=-nj\); the actual identity
\(A_r^{mj}B_\lambda^{-nj}=1\) then proves uniqueness.
No residual finite stabilizer quotient remains. On the circle line,
normalize a nonzero vector in \(N_p\) to have the indicated
norm coordinate. This is an explicit equivariant map from the
norm sphere of \(N\) to the actual delta bundle on the page.
It uses the resolved line identities of F41--43, including the
good-starred toric corrections, the good III/IV exceptional
differences, and the cancelling II correction. It therefore
identifies the actual line, not only its generic Picard point.

On the ordinary finite-base charts the page is the unramified
source pullback. At the selected nodal pieces the actual
circle-line/orbit charts of P3F.9 give the same source Picard
line, with the conifold Hopf charge retained in the later
compression. The page phase and the regular-binding bands in
P3K.6 and P3F.31 are chosen using (AR.7); since its positive
parameter angle is \(\beta\) for both signs, their exact
avoidance and line-carrying band maps apply unchanged. The
finite-base page is consequently a source translation torsor
with the specified line and the marked binding collar.

Here is its comparison with the sectioned compact page, relative
to that collar. The integral monodromy coinvariants of the source
lattice \(\Lambda\) are zero, for the following exact reason.
Any nonzero finitely generated coinvariant group has a quotient
\(\mathbb Z/p\) for some prime \(p\). The unimodular
symplectic pairing would give a nonzero common invariant vector
in \(\Lambda/p\). It is a nonzero monodromy-invariant
\(p\)-torsion point of the smooth elliptic family. The finite
algebraic division cover then has a degree-one component: its
single-valued branch is an algebraic section over the regular
base. Properness extends it over the missing points of the
minimal regular source. This contradicts its proved
Mordell--Weil group \(\mathbb Z\).

The capped meridian is the inverse product of the retained
singular-fibre meridians, so those retained meridians generate
the same elliptic monodromy group. Each of them lifts as a
closed based loop in one cut sector of (AR.8), since that
cover is unramified there with trivial sheet permutation.
Their actual lattice transports are the original ones.
The page monodromy coinvariants therefore vanish integrally
as well. This argument retains the actual images of
\(T-I\), including their multiplicities; it does not replace
them by primitive vanishing cycles. For the constructible
lattice of periods,
\[
 H^2(C,\partial C;j_*\Lambda)=0.                       \tag{AR.11}
\]
Indeed compact-support duality on the punctured oriented base
identifies the corresponding \(j_!\)-group with the coinvariant
lattice. The quotient \(j_*\Lambda/j_!\Lambda\) is a finite
skyscraper and has no first cohomology. This proves (AR.11)
with the actual boundary marking. The component quotient of the
extending translation sheaf is also a skyscraper and has no
relative first cohomology. After removing it, lift the remaining
translation cocycle to the smooth Lie sheaf. Its period
two-cocycle vanishes by (AR.11), and a partition of unity that
vanishes on the prescribed collar kills the remaining Lie
cocycle. Exponentiation gives the actual smooth translation
isomorphism with the sectioned page, fixed on that collar.

The line comparison under these smooth base translations is
made through the rigidified fibrewise Picard map, rather than
an unproved holomorphic divisor for a smooth total-space map.
On a local holomorphic translation chart form
\(\operatorname{Hom}(N,T^*N)\). Its restriction is trivial on
every fibre. At a smooth fibre this is the constant-factor
degree-zero uniformization. At a reduced additive fibre the
component degrees are zero; the proper direct-image generator
has vertical divisor in the whole-fibre kernel, so division by
that base monomial gives a nowhere-zero section. At a node it
is the normalization gluing unit, preserved by translation.
Thus the fibre \(h^0\) is one everywhere, and proper base
change plus evaluation gives a holomorphic line isomorphism
after pulling out a base line. Rigidify it along the zero
section, then pull back by the actual smooth translation
section. This is the desired smooth line isomorphism.

On the compactification its remaining base ambiguity is an
integral fibre class \(kF\). The actual line is therefore
compared, for its square, with
\[
                         M_{\rm page}=P_{aG'}-O.
\]
Here \(M_{\rm page}F=F^2=0\), so adding \(kF\) changes
neither its square nor the characteristic pairings. On the
regular binding collar the line extends over the actual
\(T^2\)-bundle over a disc and has fibre degree zero; its
boundary first Chern class is zero. The relative boundary-gauge
ambiguity consequently has zero pairing with the line and
with itself, by the exact relative product calculation P3K.5.
This retains even an odd boundary gauge.

## AR.4. The Thom sign for each physical return

By (AR.5) and (AR.7), the positive physical parameter coordinate
\(\theta\) is the positive weighted coordinate \(\beta\)
for both signs of \(n\). The complex boundary of the affine
page has positive \(\arg\xi\), hence
\[
                         \partial V=+E\times S^1_\theta.
\]
Orient the actual compression by \(\partial W=F-E\).
Attaching its rotated product gives the trace with
\(\partial X=+F\times S^1_\theta\). In the actual
fixed-sphere Hopf chart the ambient orientation is
\[
 {\rm or}(F)\,{\rm or}(\nu_{\rm Hopf})\,dr\,d\theta,
\]
whereas the trace tangent is \({\rm or}(F)\,dr\,d\theta\).
Moving the three normal directions past the two last directions
has positive sign. Thus the induced normal three-plane is the
positive Hopf model and the actual Euler line satisfies
\(\pi_*x=+1\) for each norm sign. The possible reversal of
the ambient source-product orientation in the signed \(S^3\)
identification is already included in this normal comparison;
it supplies no additional sign. This is the full signed
calculation of notes/part3_signed_cap_page.md, independently
executed in its sign certificate.

The two outer-bordism/Jin reversals are exactly those in P3K.7.
Consequently the actual positive-return invariant is
\[
 A^{\rm Jin}=\frac{12M_{\rm page}^2-p_1(TS_{\rm page})}{24}.
                                                        \tag{AR.12}
\]
Both the circle line and its orientation have now been compared
to the actual page, so this equation applies to the constructed
return rather than to a formal characteristic-number model.

## AR.5. Exact arithmetic and the oriented classes

Let \(e\) be the original capped Kodaira Euler number and
\(e'\) the resolved root Euler number. The compact Jacobian
page in (AR.8) has
\[
 \chi=\frac{m(12-e)+e'}{12},\quad
 \sigma=-8\chi,\quad p_1=-24\chi.                    \tag{AR.13}
\]
All other source fibres are unramified, and the binding is
regular, so the displayed Euler count includes every fibre.
The actual line point meets the identity component at every
retained reducible fibre and at each reduced additive root.
Good roots are irreducible. The height base-change formula
therefore gives, with \(h(G)=1/d\),
\[
 h(aG')=\frac{ma^2}{d}=2\chi+2(P_{aG'}\cdot O),
 \qquad M_{\rm page}^2=-\frac{ma^2}{d}.
\]
Combining this actual line comparison with (AR.12) yields
\[
 A^{\rm Jin}=\chi-\frac{ma^2}{2d}=-P_{aG'}\cdot O.
                                                        \tag{AR.14}
\]

| Source/capped site | Root order | Actual A, for both n=1 and n=-1 |
|---|---|---|
| E7-A or E7-B, III*, (a,b)=(2,1) | m=4l+3 | -3l-2 |
| E7-A or E7-B, III*, (1,2) | m=4l, l>=1 | 0 |
| E6-A or E6-B, IV*, (6,1) | m=3l+2 | -8l-5 |
| E6-A or E6-B, IV*, (2,3) | m=3l, l>=1 | 0 |
| OS47, III, (14,1) | m=4l+1 | -25l-6 |
| OS47, III, (7,2) | m=4l, l>=1 | -4l |
| OS56, III, (30,1) | m=4l+1 | -57l-14 |
| OS56, III, (15,2) | m=4l, l>=1 | -12l |
| OS56, IV, (30,1) | m=3l+1 | -43l-14 |
| OS56, IV, (10,3) | m=3l, l>=1 | -3l |
| OS45, II, (8,1) | m=6l+1 | -19l-3 |
| OS45, II, (8,1) | m=6l, l>=1 | -19l |
| OS47, II, (14,1) | m=6l+1 | -37l-6 |
| OS47, II, (14,1) | m=6l, l>=1 | -37l |
| OS55, II, (20,1) | m=6l+1 | -55l-9 |
| OS55, II, (20,1) | m=6l, l>=1 | -55l |

Here l>=0 in every reduced row. The E7 and E6 paired source
equations are those retained in F41. The signed physical return
class is \([\Sigma]=A^{\rm Jin}\pmod{28}\) with
\(\mu(\Sigma)=A^{\rm Jin}/28\pmod{\mathbb Z}\), by the
actual Hopf-gluing transfer P3F.22. A nonzero residue gives the
nonproduct mapping torus by P3F.24, with both spin structures
retained. The table is for the actual single positive \(r\)-loop;
no unrecorded multiple of that loop is used. Its origin, root,
Euler, height, square and residue identities are executed in
code/part3/additive_returns.py/.json/.out.
