# Moving regular order-one sites with the actual annular maps

Complete working proof submitted for the independent audit of P3K.43.
The source is the fixed marked rational elliptic source of P3K.41,
with its actual line, translation \(Q=bG\), selected whole-zero
\(I_1\), effective additive caps, and transported index-one fan.
Only ordinary order-one logarithmic sites move, in the regular-source
locus away from those fixed sites and the selected cusp. Every signed
norm, elliptic period coefficient, delta coefficient, finite character,
and annular map is retained. The parameter transitions have the linear
source/lattice marking of P3K.41. A closed loop means an actual closed
family with that marking; the proof does not close a nonclosed braid by
an unspecified endpoint automorphism.

The result is that these motions introduce no additional sphere return.
With fixed scalar their physical return is zero. With scalar winding
\(\ell\), the same exact condition and return as P3K.41 hold:
\(\ell=N M/b\), and the return is the \(N\)-th power of the actual
shorter scalar return. The proof constructs the isomorphism that makes
this statement, including its inverse endpoint arrow.

## MS.1. The full regular-disc logarithmic map

Fix a simply connected regular-source disc \(D\) and a smaller disc
containing the moving site \(p\). The local suspension is the actual
compact complex two-torus family
\[
 \mathcal X_D=N_D^\times/\langle B_\lambda\rangle
       =V_D/\Pi(t)\mathbb Z^4.                         \tag{MS.1}
\]
The first presentation retains the source degree-zero line and its
contracting lift. In the second presentation a holomorphic marking of
the full period lattice is chosen on \(D\), including the source-line
characters. Its period map \(\Pi(t)\) takes values in the actual Lie
bundle \(V\) of P3K.41. It is not a projection to just the gamma
coordinate. On a small scalar-parameter disc the same marking is
holomorphic in that parameter as well.

Let \(v\in\mathbb Z^4\) be the complete marked period of the
order-one clutch. With the ordinary-to-cap direction fixed, its map is
\[
 \Phi_p(t)=\operatorname{trans}\left(
       \Pi(t)v\,\frac{\log(t-p)}{2\pi i}\right).        \tag{MS.2}
\]
The gamma coefficient of \(v\) is \(-n\) for the norm \(n\).
This sign is the literal equation
\(h=\gamma-n\arg(t-p)/(2\pi)\) of P3K.32, not a change to its
inverse arrow. The remaining entries of \(v\) are the specified
elliptic and delta coefficients. A branch change of the logarithm adds
\(\Pi(t)v\), an actual full period in (MS.1). Thus (MS.2) is a
single-valued holomorphic translation on the punctured disc, including
its line automorphy. Any prescribed extending unit or translation is
also retained; its independent variation is the actual cap/line
comparison already proved in P3K.41.

There is a literal local model on the whole common disc \(D\).
For order one the norm identity is \(A_p=B_\lambda^n\), hence
\[
 N_D^\times/\langle A_p,B_\lambda\rangle
              =N_D^\times/\langle B_\lambda\rangle .    \tag{MS.3}
\]
Inside the original small cap disc use this quotient. On its overlap
with \(D\setminus\{p\}\), use (MS.2) to carry the exterior
coordinate into that same quotient. These maps agree by the original
cap gluing. They identify the entire piece over \(D\) with the
fixed model (MS.1), using the actual source line and suspension, while
its outer annular transition remains exactly \(\Phi_p\). This
constructs the enlarged chart; it does not presume a lift of a
circle-valued base phase or move the source coordinate \(t\).

The resulting charts form an actual holomorphic family as \(p\)
varies locally. Their interior models and root/cusp models are fixed,
and their outer annular maps are holomorphic in \(t,p\). A finite
compact cover by these local proper pieces gives the same compact
fibres and proper family over a smaller parameter disc.

## MS.2. The exact Lie logarithm on a fixed outer annulus

Choose the outer annulus once, with
\(r<|t-p_0|<R\), and restrict \(|p-p_0|<r/2\). The ratio of
the two actual maps in (MS.2) has the following honest Lie lift:
\[
 \begin{split}
 L(t,p)&=\frac{\Pi(t)v}{2\pi i}
                   \operatorname{Log}\frac{t-p}{t-p_0},\\
 \operatorname{Log}\frac{t-p}{t-p_0}
       &=-\sum_{j\geq1}\frac{(p-p_0)^j}{j(t-p_0)^j}.
 \end{split}                                             \tag{MS.4}
\]
The series converges uniformly on compact subsets of the fixed annulus
and parameter disc, and vanishes at \(p=p_0\). Its exponential is
the displayed ratio, with no residual period. In particular
\[
       \Phi_p\Phi_{p_0}^{-1}=\operatorname{trans}(L).      \tag{MS.5}
\]
All four entries of \(v\) participate in this identity. For several
distinct moving sites choose disjoint discs for this small parameter
step and use the sum of their Lie cocycles on the corresponding
annuli. The translations commute by the actual degree-zero-line group
law of P3K.41 CP.3, including the suspension scalar. Thus summing the
lifts is the actual composition of the gluing maps.

On a change of regular-source marking, \(\Pi' =\Pi C\) and
\(v'=C^{-1}v\) for the same integral monodromy matrix \(C\).
Consequently \(\Pi'v'=\Pi v\) literally. This is how (MS.4)
is transported to the next disc along a site path. No global
single-valued source period basis is assumed, even when the path
winds around a fixed singular fibre. The complete period is carried
by the actual local system; it is never reset after a turn.

## MS.3. The actual global family comparison

Use the fixed orbifold base atlas of P3K.41, adding the discs and fixed
outer annuli just constructed. Its Lie bundle has
\(H^1(B,V)=0\), proved there from the exact coarse extension of
\(\mathcal O(-1)\) by \(\mathcal O\), with all root weights
retained. Equation (MS.4) is a \(V\)-valued total Cech one-cocycle
on this atlas and groupoid. It is supported on the regular annular
overlaps and is zero on unchanged overlaps; on a refinement the
indicated bundle transition maps are included. Unlike a merely
torus-valued logarithm, it has no new integral two-cocycle. The
pre-existing finite-root group cocycle remains the one of P3K.41.

The Laurent/Cauchy solution from CP.2 gives holomorphic sections
\(L_0,L_i\), analytic in \(p\), satisfying
\[
                    L_0-L_i=L=\Psi_p-\Psi_{p_0},          \tag{MS.6}
\]
where \(\Psi\) denotes the Lie expression in (MS.2) on the
overlap. The solution is zero at \(p=p_0\). At root charts this
is the full groupoid solution; finite averaging is applied to the
complex vector sheaf, not to the integral lattice. Thus no invariant
logarithm of a nonzero fixed torsion point is being assumed.

Set \(T_0=\operatorname{trans}(L_0)\) on the ordinary chart and
\(T_i=\operatorname{trans}(L_i)\) on the cap chart. With the
ordinary-to-cap direction of (MS.2), equation (MS.6) gives
\[
                  \Phi_{p_0}T_0=T_i\Phi_p.                \tag{MS.7}
\]
Hence these maps glue to an actual isomorphism from the moving-site
family to the reference-site family. Formula (MS.7) fixes its direction;
it is not obtained by reversing a closing map informally.

Every local map is an extending translation of the sheaf used in
P3K.41. On finite roots it is the actual lifted source and line
translation commuting with \(A_i,B_\lambda\), so the finite
character and norm remain unchanged. At the selected cusp its Lie
section exponentiates, after the same integral period reindexing, to
the actual bounded toric unit map
\[
                 (Z,V,q)\longmapsto(a(q)Z,b(q)V,q),       \tag{MS.8}
\]
with both units and their inverses holomorphic. This is CP.3's
toric extension on the fixed fan. It transports the actual physical
delta action, fixed-curve tube, and Cox normal coordinates. Thus the
comparison includes the line and normal maps on the cusp collar;
there is no separate uncomputed framing change.

The same construction applies when affine cap data, line units, and
annular units vary at the same time. First use the actual local
conjugacies of P3K.41, retaining their finite kernel cocycle, then
apply (MS.4)--(MS.7). All maps are analytic on a small parameter disc
and keep the marked source itself fixed.

## MS.4. A closed braid and its exact endpoint

Cover the compact parameter interval of a site motion by finitely many
of the steps above. At each step keep its chosen outer annuli fixed.
Compose the actual isomorphisms (MS.7), always carrying the current
period marking and every annular map. This gives an interval
comparison to the reference-site family. It applies to any actual
closed braid in this marked scope. If sites are permuted, their full
cap data and the specified endpoint are carried by that permutation;
no additional endpoint identification is inserted.

For fixed scalar, both endpoint models are the same fixed compactified
suspension. Their discrepancy is a global extending translation,
because every map in the construction is such a translation and
has identity linear lattice part. P3K.41 CP.3--4 computes this group
as exactly the physical \(\mathbb C^*\) action, using the root
line orders and the selected-cusp valuation. That computation includes
all finite kernels of \(1-D_i\). In particular a braid around
a source singular value has not produced an untested finite endpoint.

Write the discrepancy as multiplication by \(c\ne0\). The
path \(c_t=\exp(t\log c)\) is a global physical delta isotopy
on all source, root, and toric charts. Composing the interval
comparison with its inverse closes it over the parameter circle.
This is a smooth isomorphism of the actual closed bundle with the
fixed bundle. Its physical return is therefore zero. The assertion
uses the actual family and endpoint; it does not infer loop
triviality merely from isomorphism of individual fibres.

## MS.5. Varying scalar and the physical return arrow

When the scalar varies, make the comparison at the same scalar on
each parameter disc. The marked period map \(\Pi(t,\lambda)\)
and (MS.4) are holomorphic there. CP.2's simultaneous Laurent splitting
therefore supplies the same actual family isomorphisms. Continuing
them yields a comparison to the fixed-site scalar/cap-data family of
P3K.41. Its exact root/cusp valuation gives
\[
                     \ell=N\frac{M}{b},\qquad N\in\mathbb Z,
                                                               \tag{MS.9}
\]
for the scalar winding of any closed marked family in this scope.
The reference endpoint is the \(N\)-fold iterate of P3K.35's
constructed shorter endpoint, for \(\lambda=w^{M/b}\).

For clarity retain the full arrows. Let \(I_t:X_t\to Y_t\)
be the moving-site to fixed-site comparison, let
\(E_X:X_0\to X_1\), \(E_Y:Y_0\to Y_1\) be the actual
forward endpoints, and let \(P_Y:Y_0\to Y_1\) be parallel
transport. Their discrepancy is a physical scalar \(C\) on
\(Y_1\), so
\[
 I_1E_XI_0^{-1}=C E_Y,\qquad
 P_X=I_1^{-1}P_YI_0.
\]
The physical return is the inverse endpoint followed by parallel
transport. Consequently
\[
 I_0(E_X^{-1}P_X)I_0^{-1}
       =E_Y^{-1}C^{-1}P_Y
       \simeq E_Y^{-1}P_Y.                                \tag{MS.10}
\]
The isotopy is the actual global delta path in MS.4. Thus the return
is precisely the \(N\)-th power of P3K.35's shorter scalar return,
with no additional contribution from the moving ordinary sites.
For the fixed transported fan coordinate \(S=p^2-pq+q^2\), the
oriented class is therefore the integer value
\[
 \frac{N}{b}\left(\chi(4-3S)+\frac{H(3S^2-7)}8\right)
            \pmod {28},\qquad H=\frac{Ma^2}{d},           \tag{MS.11}
\]
already realized by that constructed shorter family and its iterates.
No residue-class division is used.

This proves the stated extension for regular order-one sites, including
their closed braids around the fixed singular values. It retains the
fixed marked source and effective caps. Source-moduli loops,
collisions with source singular values, arbitrary nontranslation
endpoints, and the component-supported OS49 cusp are not assigned a
return by this argument.

## Audit and certificate status

The exact local annular, period-marking, quotient, and endpoint
identities are checked by `code/part3/moving_order_one_sites.py`,
with its JSON and captured output. The global geometric proof above
is submitted for root and peer audit; no result is promoted solely
from the symbolic certificate.
