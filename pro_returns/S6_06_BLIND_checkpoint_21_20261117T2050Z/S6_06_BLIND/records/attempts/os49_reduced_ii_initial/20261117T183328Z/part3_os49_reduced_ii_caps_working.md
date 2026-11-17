# OS49 reduced-II caps: actual source, line and integral joint topology

Working proof for independent audit. Keep the exact fixed OS49 source,
M=O(G-O), Q=3G and the original component-supported selected cusp. Put
m=3k for the IV-star cap, h=6l+1 for a reduced-II cap, with k,l positive.
The full cap vectors are n_A ell_0+d_A delta at IV-star and
n_B gamma+d_B delta at II. This note constructs the roots and records
all integral specialization and fundamental maps. It assigns no return.

## RI.1. Exact reduced root, marked section and Cartier diagram

Write q=t-1. The original equation and its actual marked section are
\[
 y^2=x^3-3(1+q)^3q x+(1+q)^4q(1+2q),\qquad
                         G=((1+q)^2,(1+q)^2).
\]
On q=z^h, x=z^(2l)X, y=z^(3l)Y, the relatively minimal equation is
\[
 Y^2=X^3-3(1+z^h)^3z^{2l+1}X
                 +z(1+z^h)^4(1+2z^h).                  \tag{RI.1}
\]
It has a reduced II fibre and smooth total surface, since the last
term has derivative one in z at the cusp. Its actual deck and section
satisfy
\[
 D(z,X,Y)=(\zeta_hz,\zeta_h^{-2l}X,\zeta_h^{-3l}Y),
 \quad \tau'(G')=-X(G')/Y(G')=-z^l,\quad \tau'(O)=0.    \tag{RI.2}
\]
On the normalized central cusp X=s^2,Y=s^3, D acts by
s to zeta_h^(-l)s. Its order is h because gcd(l,6l+1)=1.
Both G' and Q'=3G' tend to O in the smooth additive group.

Here is the actual line map, retaining the marked source coordinates.
At the original smooth O and G the coordinate tau=-x/y has values
0 and -1. The source change gives tau'=z^l tau exactly. Resolve its
indeterminacy at the new O by the successive charts
\[
 \tau'=z^j u_j\quad(1\le j\le l),\qquad
                 \tau=u_l,\quad q=z^h.                \tag{RI.3}
\]
These are the consecutive point blowups in the graph of the rational
source map. Before the last blowup both marked sections pass through
the same centre; on the last chart they are u_l=0 and u_l=-1. At every
intermediate exceptional curve the two pulled-back section divisors
have the same coefficient j. Their difference therefore has coefficient
zero. The remaining graph resolution is over the original cusp, away
from G and O, where their divisor line has its original nonzero frame.
Consequently the two actual graph projections beta to the root and pi
to the original source give the exact Cartier equality
\[
         \beta^*N=\pi^*M,\qquad N=\mathcal O(G'-O').     \tag{RI.4}
\]
On (RI.3) its local ratio is (u_j+z^(l-j))/u_j and on the last chart
it is (u_l+1)/u_l; all vertical powers have literally cancelled.
The formula uses these functions only in their marked-section charts;
the other source points where the rational function tau+1 vanishes
are not inserted into the divisor. The original Cartier frames are
used on their complement. On the chart (RI.3), D sends u_j to
zeta_h^(l-j)u_j, so both numerator and denominator have the same
character. Thus the diagram and the line map commute with D. The
central line N|II is trivial with the resulting D weight zero.

Multiplication by h has a unique formal-group inverse at O. Applied
to Q' it gives the extending D-invariant section R, hR=Q', R(0)=O.
There is no other extending h-torsion section: the root's elliptic
monodromy is the actual B matrix of F26, since h=1 modulo six, and
B-I is unimodular. An invariant torsion point is therefore zero.
The source map t_(-n_B R)D is consequently the actual reduced-root
norm source map; its hth power is t_(-n_B Q').

Lift t_(-R) on N through (RI.4). Its commutator with D is a base unit.
At the central fibre the source lift is the identity and the line is
trivial, so its finite commutator character is one. The exact finite
average of the zero-constant unit logarithm makes the lift F commute
with D; this is a conjugation through extending line units, not an
average of the lattice cochain. Write B_0=beta(q)F^h. The base unit
beta is D-invariant. Choose its actual analytic root with the prescribed
reference value and put
\[
 A_0=\beta(q)^{n_B/h}F^{n_B}D,\qquad A_0^h=B_0^{n_B}.
                                                               \tag{RI.5}
\]
Multiplication by the retained character zeta_h^(d_B) and the scalar
norm factor gives the full actual cap. Its ordinary-to-cap arrow
retains these source and line lifts and has normal relation
h alpha_B-n_B gamma-d_B delta. No integer period has been inserted.

## RI.2. Central bundle, freeness and every specialization map

Write y=(gamma,delta) in the two actual suspension/physical period
coordinates. The central fibre is the quotient
\[
 (\mathbb P^1_s\times T^2_y)/\langle
       (s,y)\longmapsto(\zeta_h^{-l}s,
                        y+(n_B,d_B)/h)\rangle.          \tag{RI.6}
\]
Normalization of the cuspidal source is a homeomorphism, so this gives
its actual topological central fibre. The two source points s=0,infinity
are fixed by every deck power. The cap action is free exactly when
gcd(h,n_B,d_B)=1. Its physical circle is free exactly when gcd(h,n_B)=1:
a nonintegral gamma shift prevents isotropy, while a power with integral
gamma shift fixes s=0 and can be cancelled by a physical-delta rotation.
These conclusions include the retained line character d_B.

The sphere sector below has gcd(h,n_B)=1. More generally, for every
free (RI.6), choose integers a,b with a n_B+b d_B=1 modulo h. The map
\[
 (s,\gamma,\delta)\longmapsto
 \left(e^{2\pi i l(a\gamma+b\delta)}s,
              [\gamma,\delta]\right)                  \tag{RI.7}
\]
identifies (RI.6) with S^2 times the enlarged torus
R^2/(Z^2+Z(n_B,d_B)/h). Its equivariance follows by substituting the
literal generator in (RI.6). It fixes both marked source sections.
The physical circle action is carried by the displayed map, including
the induced rotation of its first coordinate. Integral cohomology is
therefore free; this is not only a rational invariant calculation.

The source two-class eta is normalized to integrate one on the oriented
source sphere and zero on the O torus. The root formal translation flow
of Q' gives an actual generic torus section: at suspension coordinate
gamma it is the source point -gamma Q', with its rigidified line lift.
Changing gamma by one is exactly B, and changing it by n_B/h is exactly
the source/line part of A. It extends to the central O torus because
Q'(0)=O. In these literal coordinates its source forms u,w restrict to
zero. The source collapse has degree one on its oriented two-cell and
kills its two one-cycles. Thus specialization of eta is precisely uw,
with no additional psi delta term. This is the marked-section arrow
that fixes the possible integral cross term.

At II the original invariant lattices have bases
\[
 \begin{array}{c|c}
 1&(\psi,\delta)\\
 2&(uw,\psi\delta)\\
 3&(\psi uw,uw\delta)\\
 4&\nu.
 \end{array}                                             \tag{RI.8}
\]
The actual specialization images are, respectively,
\[
 \begin{array}{c|c|c}
 q&\text{image}&\text{quotient map}\\\hline
 1&\{a\psi+b\delta:n_Ba+d_Bb=0\bmod h\}&n_Ba+d_Bb\bmod h\\
 2&\mathbb Z(uw)+\mathbb Z(h\psi\delta)&[\psi\delta]\bmod h\\
 3&uw\{a\psi+b\delta:n_Ba+d_Bb=0\bmod h\}&n_Ba+d_Bb\bmod h\\
 4&h\mathbb Z\nu&[\nu]\bmod h .
 \end{array}                                             \tag{RI.9}
\]
These are the torus covering pullbacks in (RI.7), the actual source
class just identified, and their cup products. Every quotient is Z/h.
There is no specialization kernel.

## RI.3. The retained IV-star cap maps in the joint sphere sector

The actual base/fibre relations already imply that any sphere datum
must satisfy
\[
 D=h n_A+m n_B=\pm1.                                    \tag{RI.10}
\]
In particular gcd(m,h)=gcd(m,n_A)=gcd(h,n_B)=1. Thus every such IV-star
cap satisfies F33's freeness criterion for all d_A, and its flat central
surface has torsion-free cohomology by F34.

Retain F34's boundary basis (u_2,v_2,p,q), where
u_2=psi(-w+3delta), v_2=(psi+u)w, p=eta_boundary psi,
q=eta_boundary(-w+3delta)/3. The actual normal-circle integration map
in F34 is
\[
 u_2\mapsto3d_A\psi-n_Ah_1,\quad v_2\mapsto0,
 \quad p\mapsto m\psi+n_A\eta_{\partial},\quad
 q\mapsto k h_1+d_A\eta_{\partial},\qquad h_1=-w+3\delta.
                                                               \tag{RI.11}
\]
Its integral kernel is generated by
v_2 and k u_2-d_A p+n_A q. Hence the degree-two fibre image is exactly
Z v_2+Z(k u_2); its quotient is Z/k and omega=u_2+v_2 maps to one.
The degree-one fibre image, in basis (psi,h_1), is
n_A a+3d_A b=0 modulo m. Its quotient is Z/m.

For completeness put phi=psi uw and rho=(psi+u)w delta. The oriented
pairing of the full degree-one and degree-three invariant lattices is
\[
 \begin{pmatrix}0&1\\-3&0\end{pmatrix}
 \quad\text{in }(\psi,h_1)\text{ and }(\phi,\rho).
                                                               \tag{RI.12}
\]
The actual covering T4 to the cap has degree m, so its pullbacks pair
as m times the unimodular downstairs pairing. Therefore the complete
third image is exactly
\[
 \{c\phi+e\rho:n_Ac+d_Ae=0\bmod k\}.                  \tag{RI.13}
\]
Indeed an integer inverse of n_A modulo m gives the first-image basis
(m,0),(-3d_A n_A^{-1},1); substituting in (RI.12) gives (RI.13).
The determinant of that lattice is k, and the perfect downstairs
pairing proves there is no omitted sublattice. The degree-four image
is mZ nu by the actual covering degree. All d_A and normal-circle
boundary terms remain in (RI.11)--(RI.13).

## RI.4. Complete global MV and differential calculation

The linear tuple is exactly F26/OT.5: the reduced root construction
changes the affine filling, not its marked ordinary monodromy. Its
integral parabolic H1 vanishes and its global invariants/coinvariants
are OT.7. The only finite specialization quotients are the ones in
(RI.9),(RI.11)--(RI.13). In degrees one through four their full global
cokernel presentations are
\[
 \begin{array}{c|c}
 1&\begin{pmatrix}m&0&n_A\\0&h&n_B\end{pmatrix}\\[2pt]
 2&\begin{pmatrix}k&0&1\\0&h&3\end{pmatrix}\\[2pt]
 3&\begin{pmatrix}k&0&n_A\\0&h&n_B\end{pmatrix}\\[2pt]
 4&\begin{pmatrix}m&0&1\\0&h&1\end{pmatrix}.
 \end{array}                                             \tag{RI.14}
\]
Under (RI.10) all four have unit Smith factors. Their primitive global
kernels are generated by
\[
        1,\quad mh\psi,\quad kh\omega,
                        \quad kh\phi,\quad mh\nu.       \tag{RI.15}
\]
The second column remains the free coinvariant column OT.7 and the
middle column is zero.

The auxiliary linear-root fillings and the original cusp admit the
actual origin inversion, so their rational intrinsic d2 is zero by
its (-1)^q action. The actual cap boundary paths, repeated m and h
respectively, close to their full integral norm vectors. Their exact
translation-prism differential is
\[
 d_2=\frac1m\iota_{n_A\ell_0+d_A\delta}
               +\frac1h\iota_{n_B\gamma+d_B\delta}.     \tag{RI.16}
\]
Apply the unchanged coinvariant projections to the four primitive
classes (RI.15). Each value is precisely D=h n_A+m n_B. The d_A,d_B
contractions are retained before projection and vanish in the specified
coinvariant component; they are not discarded from the cap maps.
Thus for D=+1 or -1 the four maps are integral units. There is no
higher differential and only H0=H6=Z remains.

## RI.5. Full fundamental group and constructed sphere members

The reduced-II filling kills the two elliptic one-cycles by its actual
source collapse; its boundary onto the group of (RI.6) retains the two
torus directions and the root meridian. Along with the selected cusp
this gives exactly the primitive fibre relation lattice generated by
(H_B-I,H_C-I) in F26, leaving gamma. The two surviving base meridians
have the full relations
\[
 m\alpha_A-n_A\gamma=0,\qquad
 h\alpha_B-n_B\gamma=0,\qquad \alpha_A+\alpha_B=0.       \tag{RI.17}
\]
All generators now commute: the remaining fibre generator is invariant
and the base has one generator after the last relation. The full group
is cyclic of order |D| for D nonzero and infinite cyclic for D zero.
Thus D=+1 or -1 is necessary and, by RI.4, sufficient for the actual
constructed manifold to be a simply connected integral homology S6.
The same Hurewicz/Whitehead and Theta6 identification used in F26 gives
the standard smooth S6. The full group and homology are carried to every
allowed fan by the actual relative common blowups of F35.

These constructions exist exactly for gcd(3k,6l+1)=1 in this two-cap
sphere sector. Bezout gives every pair (n_A,n_B) in (RI.10); the root
norm and retained characters above construct each one. The smallest
case is
\[
 (m,h,n_A,n_B,d_A,d_B)=(3,7,1,-2,0,0),\qquad D=1.        \tag{RI.18}
\]
All full source/line and finite-character maps remain in the proof.
Additional ordinary order-one clutches, moving sites, parameter closing
and return classes have not been assigned by this note.
