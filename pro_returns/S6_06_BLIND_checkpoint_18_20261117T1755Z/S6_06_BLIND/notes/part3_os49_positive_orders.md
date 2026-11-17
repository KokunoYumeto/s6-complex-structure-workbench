# P3F.32. All sphere orders of the positive-diagonal OS49 filling

**Proved.** Use the positive-diagonal fan of P3F.31, the cap
order \(m=3k\), \(k>0\), and the vector
\[
 \ell=n(1,-1,0,0)^t+d\delta,\qquad n\in\{1,-1\},\quad d\in\mathbb Z.
\]
The exact construction below extends the positive-fan page and
angular origins to every such order and twist. Every resulting
sphere family has zero positive-loop return index and a product
mapping torus. P3K.65 gives the corrected negative-diagonal sphere class \(-3k\) for this positive \(r\)-loop, or \(-k\) for the shorter \(w\)-loop, for both norm signs and every fixed delta character.

## 1. The actual closing map and its origins

Put \(\lambda=r^m\), \(v=\log r/(2\pi i)\) and
\(s=\log q/(2\pi i)\). The periods are
\[
 u=(2s,s)^t+U(q),\qquad
 \gamma=(-3s,-s+mv)^t+C(q),\qquad D=3U+2C,
\]
so
\[
 H=-u-\gamma,\qquad K=3u+2\gamma=D+(s+2mv)\delta.
\]
The invariant cap covector evaluates to \(n\) on \(\ell\).
When \(v\) increases by one, its affine logarithmic origin changes
by \(n\log t\,\delta/(2\pi i)\). The fixed extra displacement
\(d\delta/m\) has no parameter difference. Consequently
multiplication of the ordinary line coordinate by \(t^n\) closes
the family. It is a unit at the type-II value and is \(q^{-n}\)
at the cusp. Its toric map is the integral vertical translation
by \(n\), which preserves the positive-diagonal fan.

On \(q=Q^{2m}\), choose the two extending origins
\[
 \begin{aligned}
 \sigma(s,v)&=nvD+nmv(v-1)\delta,\\
 o(s,v)&=-\frac{nsD}{2m}
          -\frac{ns^2}{4m}\delta-nsv\delta.
 \end{aligned}
\]
The first is bounded in the cusp charts; the second has parameter
difference \(-ns\delta\), exactly the logarithm of the closing
map at the cusp. Their difference is
\[
 F(s,v)=\frac{nD(s+2mv)}{2m}
       +\left(\frac{n(s+2mv)^2}{4m}-nmv\right)\delta,
\]
and direct subtraction gives
\[
 \begin{aligned}
 F(s,v+\theta)-F(s,v)
    &=n\theta K+nm\theta(\theta-1)\delta,\\
 F(s+2m,v)-F(s,v)&=nK+nm\delta.
 \end{aligned}
\]
The cyclic descent is therefore by an integral period. Its line
gauge has winding \(2mn\), while the displayed real angular gauge
has zero values at both endpoints. The actual positive \(r\)-loop
has \(n\) turns of the primitive \(K\)-circle. For \(n=-1\) the
parametrized rotating trace is reversed; the index changes sign
by P3F.11.

## 2. The page, including the finite-cap line

The finite cap is the actual free affine quotient of P3F.29.
Its gamma displacement is \(n/m\). For \(n=\pm1\) its circle
base is the weighted Hopf three-sphere with one exceptional orbit
of order \(m\), with the gamma orientation reversed in the
negative case. The regular-binding page maps to the complex
elliptic base with degree \(m\), with full branching at the
finite logarithmic value and at the regular binding value. It is
the explicit cyclic cover obtained by taking an \(m\)-th root
of a rational coordinate whose zero and pole are those two
values. The genus of its compact base is zero.

Here the cap hypothesis is verified by the actual root charts:
its linear part has order three and fixes \(\ell\), and its
\(j\)-th power has gamma displacement \(jn/m\). For
\(0<j<m\) this displacement is nonintegral because
\(\gcd(n,m)=1\). It is therefore free. No nonidentity
delta rotation compensates such a displacement. Thus the
delta action is free on these cap charts as well, exactly
as required in the trace construction.

The finite-value root is a multiple of three, so the supplied
order-three good reduction extends over that root as a smooth
elliptic surface. The line on this root is the pulled-back
degree-zero section line. The extra \(d\delta/m\) in the affine
deck multiplies its circle coordinate by a constant root of
unity. It acts as the identity on the elliptic source coordinate.
Thus its change of gluing is a scalar transition on the base:
on a cut annulus it is the constant character
\(\exp(2\pi i d/m)\). After the page has gone around all \(m\)
sheets its total character is \(\exp(2\pi i d)=1\).
Choosing the scalar transitions on the individual sheet overlaps
gives a line pulled back from the base page. This describes the
actual additional gauge; it does not change the Picard class on
an elliptic fibre. A different cap trivialization can change the
compact extension only by an integral fibre class.

At the cusp choose \(m\) norm shells in the actual \(M^\times\)
subfan, with radii \(R_1<\cdots<R_m\) satisfying \(cR_m<R_1\).
The exact height defects and no-reentry proof in P3F.31 apply to
every one of these shells. Its explicit positive-multiplier
annular lift glues them to the \(m\) outer page sheets. At the
type-II values use the original line-complement map. This is an
embedded page \(V_m\subset Y\setminus F\) carrying the actual
delta line \(M\), up to the base line just described.

Its regular compact cap has \(m\) type-II and \(m\) type-\(I_2\)
fibres. The section and zero section remain disjoint under the
base cover and its good-reduction extension. More explicitly,
the degree-\(3k\) rational coordinate power factors through
the degree-three cover of P3F.31; the further degree-\(k\)
cover branches only at its smooth good-reduction fibre and
at the regular binding fibre. It pulls back two already
disjoint sections, so it introduces no section intersection.
Hence
\[
 \chi(\mathcal O)=k,\qquad \sigma=-8k,\qquad
 M_{\mathrm{rel}}^2=-2k,\qquad p_{\mathrm{rel}}=-24k.
\]
These identities are unaffected by an integral fibre-class
change: the section line has degree zero on a fibre, and the
fibre has square zero.

## 3. The actual graph line and return

Use the \(K\)-compression and its exact inverse boundary angle.
The annular lift above leaves the binding base coordinate
unchanged. The boundary phase now winds \(m\) times, so the
normal pushoff equation of P3F.31 confines its intersections
with the unrotated compression to \(m\) proper boundary arcs.
The page misses the fixed sphere through its actual line subfan;
therefore all remaining intersections are over a compact regular
base interval. Enlarge the \(m\) lifts to disjoint half-disc
bands. Each pair is
\[
 (T^2\times D_i,\ T^2\times A_i),
 \qquad H^2(T^2\times D_i,T^2\times A_i;\mathbb Z)=0.
\]
The exact radial homotopy on the complement, followed by this
restriction injectivity, identifies the graph-normal meridian
line with the actual page line on all of \(V_m\).

The cap marking still has
\((u,\gamma)=(2H+K,-3H-K)\). Its determinant is one, and its
vanishing primitive cycle is \(w\). The two marked caps and
their line restrictions are precisely those in P3F.31. Thus
the actual sphere-bundle bordism has
\[
 b^2=-8k,\qquad p_1(T\bar X)=-24k,
\]
and one primitive \(K\)-turn has
\[
 A_K=\frac{3(-8k)-(-24k)}{24}=0.
\]
The explicitly computed positive parameter loop has \(n\)
turns and the endpoint-zero angular delta gauge, so its index
is \(nA_K=0\). The topology of the positive-fan filling follows
from P3F.29 and the actual common blowup of P3F.31, which adds
the same primitive cohomology summands to both fillings. It is
the standard smooth six-sphere. The Hopf transfer P3F.22 gives
oriented return class zero, and P3F.24 gives the product mapping
torus for every \(k,d\) and both signs of \(n\).
