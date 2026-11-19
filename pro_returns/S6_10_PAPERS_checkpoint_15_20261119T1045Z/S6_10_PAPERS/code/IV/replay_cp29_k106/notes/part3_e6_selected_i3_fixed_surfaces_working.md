# Selected-I3: complete compact surface and interior-corner normal ledger

The source and closing data are SI3, for M6,b=1,m=2,n=1 and the
scalar root s^2 r0. This note uses the executed common and three
corner atlases, with the full c0=(p-1)^4c dictionary. It evaluates the
closed compact fixed components contained in those atlases. The four
lower source/reference doubles and the selected moving normal cap
retain their separate boundary constructions.

## FSI.1. Actual faces, periods and the three completed ends

In a regular chart with ray matrix N, the physical circle acts with
weights N^-1 delta. The nonzero-weight coordinates must all vanish
on its fixed set. The corresponding ray face is therefore the
minimal fixed face, and its coordinate complement gives the actual
fixed-component chart. All normal characters here are read from these
same coordinate maps.

The finite period identification is exact. For the common fan use
M=[[7,2],[1,2]]; for a face of total upper height h, its two fibre
coordinate sums transform by hM times the period vector. Apply the
componentwise floor of (hM)^-1 to that sum. This returns its unique
canonical period translate, with the recovered integral vector
retained. At the zero corner use rI+h[[3,-1],[6,2]], at infinity use
[[7h,2h],[h,r+2h]], and at one use
[[3r,-r],[0,4(r+h)]]. These are the actual matrices of SI3.26--27
and I3P.11, not substitute lattices.

The rank-two matrices are invertible on each relevant positive-base
face. On the rank-one lower infinity or one boundary, the second
coordinate fixes the second period and the first period is retained
as its kernel. Thus the canonicalization records both all face
orbits and the exact stabilizer. The compact generic surfaces and
the interior strata below have zero period stabilizer.

The resulting count in the constructed charts is 421 generic
surface orbits and 3422 generic curve orbits. The zero corner has
98 additional interior points and two additional interior curves;
infinity has 28 additional points and two additional curves. The
one corner has its four lower surfaces, and zero has its selected
moving surface. Those last five surfaces are outside this compact
ledger. The face output records every chart, normal weight, period
word, canonical ray and complete normal coefficient vector.

For each common cone the protected-face index gives its final zero
and infinity owner, original parent K,J word, actual native period
to that owner and the vertex permutation. The one owner is the
unique upper-star reference in I3P. The lower joins of I3P have their
own two-dimensional upper-face references; they are not substituted
for these three-dimensional protected facets. The initial failed
reference selection that included those joins is preserved under
records/attempts/e6_selected_i3_first_face_reference_selection.

## FSI.2. The full section and normal arrows

The three dense normal maps are written explicitly in I3C.1--4.
Here they are independently constructed by composing actual maps
before taking any degree. In the zero order (Z,V_pt,p,P), the
initial point map to (V_reg,Z,R,p) is the matrix
\[
 C_0=\begin{pmatrix}
 -3&1&-6&6\\1&0&0&0\\0&0&1&1\\0&0&1&0
 \end{pmatrix},
 \tag{FSI.1}
\]
with the full factor U6 in the first character. Its K^rJ^s period
map is
\[
 K_{r,s}=\begin{pmatrix}
 1&0&7r+2s&-4(2r+s)\\
 0&1&r+2s&-s\\0&0&1&0\\0&0&0&1
 \end{pmatrix},
 \tag{FSI.2}
\]
with factor (p-1)^(4(2r+s)) c^(2r+s) in its first character.
The recorded owner period is undone by the literal SI3.26 matrix
and the factor c0^-b in V_pt. Thus the full unit left in that
character is c0^(2r+s-b)U6. This composition retains R=pP and
all of its nonzero p powers.

At one the initial matrix is
\[
 C_1=\begin{pmatrix}-1&1&0&0\\1&0&0&0\\
 0&0&1&0\\0&0&0&1\end{pmatrix}.
 \tag{FSI.3}
\]
Compose it with the actual K,J matrix having first-row additions
(7r+2s,8r+4s) in the P,v columns, and second-row addition r+2s in
the P column. Its complete unit vector is
p^(-6-r-2s,r+s,1,0)c^(2r+s,0,0). At infinity the common coordinates
are V_reg,Z,R; apply the actual inverse owner period of SI3.27,
including its f^(-2a-b), then project to those three coordinates.

For a common matrix N, final end matrix Ne and directed common map
Le, the exact coordinate map is N^-1 Le Ne, with every unit exponent
multiplied by N^-1. The protected-face columns are exactly the three
appropriate unit coordinate columns; the other column has base order
one. If its three entries are o_ei, the coefficient arrow is
\[
 z_i^{\rm common}=q_e^{o_{ei}}u_{ei}z_i^{\rm end},
 \qquad(q_0,q_1,q_\infty)=(p,p-1,p^{-1}).
 \tag{FSI.4}
\]
The saved u functions are the full powers just specified. They and
their inverses extend on the stated end discs. Consequently the
section with common coefficient one has divisor -sum_e o_ei,
which fixes the degree sign without a frame convention choice.

These maps are computed for all4264 common cones, including those
with a zero physical weight. The resulting degrees and full unit
vectors agree independently with every one of the3422 I3C curve
records. For every cone the identity sum_i h_i d_i=-1 also holds,
with the complete original canonical orders 2h_i-1 retained.

## FSI.3. The 421 actual surfaces and their integral line classes

A surface face has two actual normal rays with weights w_minus<0
and w_plus>0. Its quotient generic fan has two opposite tangent
rays. The two charts therefore supply its entire P1 fibre over the
punctured p-base. Their actual normal overlap is determined by
\[
 v_0+v_1+d_- n_-+d_+n_+=0.
 \tag{FSI.5}
\]
Here n_minus,n_plus are the saturated normal rays and v0,v1 the
two aligned tangent rays. Expressing this relation in the actual
unimodular basis gives the two integral fibre degrees d_minus,d_plus.
The signs agree with the coordinate overlap of O(-1), whose
coefficients multiply by the inverse projective base coordinate.

At each end align every surface chart by its stored actual period.
Quotient its four-dimensional lattice by the two normal rays. The
remaining two-dimensional fan is a full half-plane with opposite
boundary rays and base-order-one middle rays. At zero and one every
surface has exactly two such charts. At infinity409 surfaces have
two charts and12 have three. In each three-chart case the extra ray
is exactly the sum of the adjacent old ray and one boundary ray.
Its two explicit monomial charts are therefore the ordinary blowup
\[
 (x,y)=(a,ab),\qquad(x,y)=(cd,d).
 \tag{FSI.6}
\]
Every other cone and every full period/unit map remains in the
displayed end fan. These are twelve actual point blowups of the
specified split P1 bundles, with their centres on the specified
sections. The split bundle itself is given by the fibre transition
z_common=q_e^o u_e z_end from FSI.4 and its reciprocal; its
homogeneous arrow is [u:v] mapped to [q_e^o u_e u:v].

The two fixed sections have self-intersections s0,s1 and normal
degrees q0_minus,q0_plus and q1_minus,q1_plus obtained from FSI.4.
Their sum s0+s1 is zero in the unblown case and -1 in the blown
case. For the latter, the exact exceptional wall relation in the
four-dimensional lattice gives its normal line degrees e_minus,
e_plus and self-intersection -1. Its two chart incidences with the
sections are i0,i1, with i0+i1=1. These are saved individually.

The integral intersection matrix in the basis (S0,fibre), or
(S0,fibre,E), is
\[
 I=\begin{pmatrix}s0&1\\1&0\end{pmatrix},\qquad
 I=\begin{pmatrix}s0&1&i0\\1&0&0\\i0&0&-1\end{pmatrix}.
 \tag{FSI.7}
\]
Its determinant has absolute value one. The ordinary two-section
bundle gives its free rank-two lattice, and the explicit blowup
adds the independent integral exceptional class. For each normal
line the complete Chern vector is the solution of
\[
 I x_\pm=(q0_\pm,d_\pm)^t,
 \qquad
 I x_\pm=(q0_\pm,d_\pm,e_\pm)^t
 \tag{FSI.8}
\]
in the respective cases. Every solution is integral. The opposite
section supplies an independent check: its class is I^-1(0,1), or
I^-1(0,1,i1); it has exactly the stored self-intersection and both
stored normal degrees. Thus no normal Chern number is selected from
a residue or from an unspecified boundary gauge.

Adjunction gives the canonical vectors I^-1(-2-s0,-2), respectively
I^-1(-2-s0,-2,-1). Their squares are8 and7. The actual Euler numbers
are4 and5 from the P1 bundle and one point blowup. Hence p1(TF)
is0 or-3, with the complex orientation and the full source determinant
maps preserved. The executable saves every matrix, exceptional
monomial map, period word, section degree and normal Chern vector.

## FSI.4. Actual interior points and the four interior curves

The98 zero-corner points and28 infinity points have four nonzero
physical coordinate weights. Their period stabilizers vanish by
the same integral matrix calculation in FSI.1. They are distinct
chart origins in the quotient atlas; no extra multiplicity is
deduced from a determinant or from a ray height.

Each of the four additional interior curves has precisely two
charts after the actual period alignment. Its quotient tangent
rays are opposite primitive rays, so these charts glue to P1.
The complete line transition is obtained from the four-dimensional
inverse matrices. For independent verification, use each of the
two integer auxiliary cocharacters (1,11,103,1009) and
(2,17,89,701) in the aligned lattice. At the two endpoints their
tangent weights are k,-k. The normal degree is the sum of the
two ratios m_i/k. Both computations give the same integral vector
of three degrees. This is also the degree obtained by substituting
the two toric coordinate arrows directly.

Every full c0 or f coefficient in these arrows remains in the
output. On these closed corner components the source base is its
fixed origin; the nonzero units restrict to their actual constants.
Their quotient by that constant has its extending analytic logarithm
on the corresponding chart neighbourhood. Multiplication by its
exponential gives the explicit comparison with the constant
coefficient, preserving the complete original arrow. No boundary
normal factor from a different source region is used here.

## FSI.5. Weighted characteristic expressions and exact compact sum

For a surface write its two normal intersections as
x=c1(N_minus)^2, y=c1(N_minus)c1(N_plus), z=c1(N_plus)^2,
and let t=p1(TF). With physical weights w1,w2 put
\[
 B=x/w1^2+y/(w1w2)+z/w2^2.
\]
Expansion of the actual two weighted Euler factors, with the
positive hyperplane generator U, gives
\[
 k_U=B/(w1w2),\qquad
 \ell_U=\frac{t-x-z-2(w1/w2+w2/w1)y+(w1^2+w2^2)B}{w1w2}.
 \tag{FSI.9}
\]
This is the fixed-normal formula SZ.57--59/IE.4--5 applied to the
actual Chern vectors FSI.8. The physical line is M=U^*, by the
explicit K68 anti-equivariant Hopf map, so its inner pair is
(-k_U,-ell_U). The same exact formulas for a point are
k_U=1/product(w_i), ell_U=sum(w_i^2)/product(w_i). For a curve
they are I3C.8 with its three actual line degrees. Every finite
weight denominator remains in these formulas.

The421 surfaces have physical-M inner pair
\[
 \left(-\frac{292926553257191671}{5199567557184000},
 \frac{6844342706156462179}{15598702671552000}\right).
 \tag{FSI.10}
\]
The zero interior points and curves together give (-8,-182);
the infinity interior points and curves give (-8,-92).
Adding these to FSI.10 and the complete I3C.9 curve pair gives
the exact compact native subtotal
\[
 (k_M,\ell_M)_{\rm compact}=(-63,453),\qquad
 (4k_M-\ell_M)_{\rm compact}/24=-235/8.
 \tag{FSI.11}
\]
This is the sum over the closed components proved above. It includes
no lower source/reference double, moving selected cap, outer Jin
boundary transfer or completed return.

The complete code/part3/e6_selected_i3_fixed_faces.py records all
minimal faces and exact period orbits. The companion
code/part3/e6_selected_i3_fixed_surfaces.py records all normal
coefficient maps, all421 integral intersection problems, all126
points and four interior curves, together with their input hashes.
Its executed111231 checks include independent agreement with every
curve degree and all of its full unit powers. The original failed
reference selection and its exact correction remain preserved.
