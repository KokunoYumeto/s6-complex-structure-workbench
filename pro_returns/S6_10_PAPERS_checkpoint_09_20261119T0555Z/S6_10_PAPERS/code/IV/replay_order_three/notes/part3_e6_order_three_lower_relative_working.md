# The exact relative normal calculation for the four lower surfaces

This working proof continues LS.1--4 and E104--106. It compares each
executed lower surface with its actual fixed-source scalar-chain
reference, using the full point-line boundary map. The outer selected
tube and Jin transfer remain in the separate exterior ledger. No total
source return is assigned here.

## LR.1. The marked source domain and its boundary maps

Let \(E\) denote the minimal \(I_3\) source domain of LS.7,
with its finite boundary \(|t|=\eta\). The executed lower
surface \(\widetilde E\) has the specified proper map
\(b:\widetilde E\to E\) given by the 12 source charts
LS.7a, comprising nine ordinary blowups. The map is the
identity on the outer boundary. Every physical normal
coordinate is the pullback of its parent coordinate,
by all 48 saved parent matrices.

The actual source family in E105.1 is smooth over the
source parameter: the equation
\(s=S_0T_0-S_1T_1\) has nonzero \(T_0\) or \(T_1\)
derivative, and its other source chart has \(s\) as
an independent coordinate. Over the compact source
domain it is a proper family with the specified
outer boundary. Keep the E105 boundary vector field
and extend it over the interior using a partition
of unity on source charts. Each local field has
parameter component one; the weighted sum does too.
Prescribe its tangent value on the actual section
\(O\), and use a section tubular neighbourhood
before taking that partition. Its complete flow
identifies \(E\) with the reference source domain
\(E_*\), including the marked section and the
displayed boundary source map. This construction
also gives the tangent cobordism between them;
the reference tangent comparison has relative
Pontryagin number zero before the nine blowups.

The actual point line is a complex line bundle on
this same smooth source family. A Hermitian
connection and parallel transport along the
just specified source field give a complex-linear
line isomorphism on the interval. On the boundary
its coefficient is retained and is composed with
the exact LS.13a arrow
\[
 H=P^{-6}U_6^{-1}Z^3,\qquad
 U_k^{\rm pt}=P^{-3-l}u_s^lU_6^{-1}Z_*^2
 (\lambda_0qK P^{-3})^j a_{\rm ref}.
 \tag{LR.1}
\]
Thus this transport does not prescribe that the
boundary line gauge is the identity. Its inverse
is the inverse parallel transport and the full
reciprocal of LR.1.

## LR.2. Integral boundary gauges and the actual fibre clutch

The three node charts \(x_Iy_I=P\) have the same
primitive vanishing circle \(a\). To obtain the
source handle presentation, cut the base disc along
three distinct radial paths after a small deformation
of its three nodes. The complement is the actual
smooth torus bundle; each local \(xy=t\) chart
attaches one vanishing disc with boundary \(a\).
The charts identify these circles by the literal
source overlap of LS.7. Returning the three critical
values to the central value preserves this handle
presentation. Consequently
\[
 H_1(E;\mathbb Z)=\mathbb Z\langle b\rangle.
 \tag{LR.2}
\]
The boundary is the actual torus mapping torus of
\(Q=P^3\). If \(\alpha\) is its positive base
circle, its fundamental group has the presentation
\[
 [a,b]=1,\quad \alpha a\alpha^{-1}=a,\quad
 \alpha b\alpha^{-1}=a^3b.
 \tag{LR.3}
\]
These relations follow by continuing the actual
logarithm of \(Q=P^3\) once around \(P=0\).
They give
\[
 H_1(\partial E;\mathbb Z)
 =\mathbb Z\langle b,\alpha\rangle
   \oplus\mathbb Z/3\langle a\rangle.
 \tag{LR.4}
\]
The inclusion kills \(a\) by the displayed
vanishing discs, kills \(\alpha\) by the section
\(O\)'s base disc, and sends \(b\) to the source
generator. The blowups leave these first-homology
maps unchanged. In particular
\[
 H^1(\partial E;\mathbb Z)/
 \operatorname{im}H^1(\widetilde E;\mathbb Z)
 =\mathbb Z\langle\alpha^*\rangle.
 \tag{LR.5}
\]

Here is the actual line map represented by the
remaining generator. Glue trivial frames on the
two source domains with
\[
 e_R=(t/\eta)e_L
 \quad\hbox{on } |t|=\eta.
 \tag{LR.6}
\]
The section \((t/\eta)e_L\) on the left and
\(e_R\) on the right is the same section on
the overlap. Its divisor is precisely the
left source fibre \(F\). Thus this explicit
clutch line has \(c_1=\operatorname{PD}[F]\).
Its inverse uses \(\eta/t\).

For completeness the full boundary function is
retained in the gauge comparison. Its homotopy
class in \(H^1(\partial E;\mathbb Z)\) is
\(n\alpha^*+m b^*\). A map from the source
handle presentation to the circle representing
\(b^*\) extends the \(m b^*\) term over
\(\widetilde E\). After dividing by that
extending map and by \((t/\eta)^n\), the
boundary function has a single-valued logarithm.
Extend that logarithm using its collar value and
a cutoff to zero in the interior; exponentiation
gives the reciprocal bundle isomorphism as well.
This constructs the exact line-bundle comparison
with the clutch line LR.6, keeping the integer
\(n\) and the entire original boundary function.
It does not set LR.1 to a constant.

The fibre class obeys
\[
 F^2=0,\qquad D\cdot F=0,
 \quad D=3F-C_1+C_2.
 \tag{LR.7}
\]
Indeed a regular fibre has the actual product
normal disc from the base coordinate, and can
be moved to a base value disjoint from every
central component of \(D\). The source flow
preserves this fibre class through its marked
base coordinate. Thus every integer and full
unit retained in LR.1 changes the closed line
classes only by the fibre clutch LR.6, whose
square and intersections in LR.7 vanish.

## LR.3. The two reference normal lines

On the fixed-source scalar-chain side the actual
normal coordinates are
\[
 U_k^{\rm pt}=V_{\rm pt}/s^k,\qquad
 V_k^{\rm pt}=s^{k+1}/V_{\rm pt}.
 \tag{LR.8}
\]
A change of the original point-line frame acts
on these coordinates by its coefficient and
its reciprocal. Hence their actual complex
normal bundles are \(M_6\) and \(M_6^{-1}\),
with physical weights \(+1,-1\). The original
Cartier calculation E73 gives
\[
 c_1(M_6)=D=3F-C_1+C_2,\qquad D^2=-6,
 \tag{LR.9}
\]
under the source transport LR.1. The corresponding
normal bundles on the executed collision side
are the invariant bundles of LS.8 and their
literal pullbacks through all nine blowups.

Close the collision surface with the oppositely
oriented reference surface, using the actual
boundary map of E105--106. The preceding gauge
construction identifies each closed normal line
with the reference-supported class plus an
integer multiple of the fibre clutch. Its square
and mixed pairing therefore retain the exact
values
\[
 \int L_+^2=6,\qquad
 \int L_+L_-=-6,\qquad
 \int L_-^2=6.
 \tag{LR.10}
\]
The minus sign from the reference orientation
is included here. No value of the integer
boundary winding is needed or suppressed:
LR.6--7 show explicitly why it contributes
zero to each of these three pairings.

The tangent cobordism LR.1 contributes zero
between the minimal source and its reference.
The nine actual blowups contribute LS.16:
\[
 \int p_1(TF_{\rm double})=-27.
 \tag{LR.11}
\]
All normal transitions still come from the
same point line and its inverse; the blowdown
is the identity on the outer boundary.

## LR.4. Scoped relative physical pair

Use the actual E102 normal-link orientation
and its physical line map \(M=U^*\), with
weights \((+1,-1)\). Substitution of LR.10--11
in E102.4 gives
\[
 (k_U,\ell_U)=(-18,27),\qquad
 (k_M,\ell_M)=(18,-27)
 \tag{LR.12}
\]
for each of the four lower/reference doubles.
This is the relative fixed-surface calculation
in its specified source and normal frames.
The outer selected-tube completion and the
outer-to-Jin parameter arrow are separate
parts of the full boundary ledger, so LR.12
does not assign a total source return.

The initial minimal-source prose, the nine-blowup
correction, and the complete LS.1--4 peer record
remain preserved under the two named lower-surface
attempt directories. The independent finite
calculation accompanying this note checks the
integral boundary presentation, the fibre-clutch
pairings and the signed relative normal formula.
