# Source-zero returns on every physical vertical-edge fan

Working proof for independent audit, 17 November 2026, prospective K82.
The actual source, Cartier maps, root caps and parameter closing are those
of K49, K60, K69 and the completed reduced attachment K80. Retain
(a,b,m)=(1,2,4p) or (2,1,4p-1), p positive, signed cap norm nu=+/-1,
every finite character and the complete annular cochain. The source is
Y²=X³+(1-2v)X²+TX+v², G=(0,v), and q=q1=T-(v²-2v).
The scalar is lambda=v^N lambda0 with N=km. The case k=0 denotes
the actual fixed-scalar loop obtained by RT.12 on a sufficiently small
compact parameter annulus; its scalar is chosen after that annulus.

For every integer j let T_j have basis P_j=((1,0),(j,1)), with the
negative-square convention of K71. Let Z_j be its actual positive-v
return in the physical K68 presentation Theta7=Z/28. The exact relative
formula proved below is

\[
 Z_j-Z_0=
 2b\binom{j+1}{3}+(3-b)\binom{j+1}{2}
                         -N\binom j2\pmod {28}.       \tag{ZV.1}
\]

Here each binomial is its integer-valued falling-factorial polynomial,
including at negative integers. In the reduced a=2,b=1 branch, K80 gives
Z0=k(3p-1), so the completely evaluated return is

\[
 Z_j=k(3p-1)+2\binom{j+2}{3}
                    -k(4p-1)\binom j2\pmod {28}.       \tag{ZV.2}
\]

The good branch retains its independently determined Z0 in (ZV.1).
This proof assigns no good-branch absolute value. It also assigns no
nonvertical fan value: the fixed-star free entries needed for that
extension have not been recovered from a residue.

## ZV.1. Actual vertical characters, full periods and their seam

Write the full periods on the protected selected-cusp neighbourhood as

\[
 h(Z,V,q)=(\kappa qZ,\alpha V,q),\qquad
 B(Z,V,q)=(gZ,q\eta V,q).
\]

Every coefficient is the full nowhere-zero function of q and the cut
source parameter. The exact SZ.44 calculation gives the single-loop
winding matrix

\[
 W=\begin{pmatrix}1&b\\-a&N-2\end{pmatrix}.
\]

Make the literal character map (Z,V,q) to (Z_j,V_j,q)=(Z,Z^-j V,q),
and take the actual period generators h_j=hB^j and B_j=B. Their
complete coefficients are

\[
 \kappa_j=\kappa g^j,\quad g_j=g,\quad
 \alpha_j=\alpha\eta^j\kappa^{-j}g^{-j^2},\quad
 \eta_j=\eta g^{-j}.                                  \tag{ZV.3}
\]

The character matrix and its inverse are integral. On every absolute
matched cone they give inverse maps of its character semigroup with
the stated full units. They therefore identify T_j with its standard
vertical marking as an actual holomorphic toric neighbourhood. The
inverse maps attach its unchanged common exterior, source line and
finite root charts. Its full multiplier winding matrix is exactly
P_j^-1 W P_j. No q-height or annular cochain is discarded.

Put L0=nu k. The actual forward ordinary closing is (Z,V) to
(Z,q^L0 V). After the actual B^-L0 reindex, its bounded chart arrow is
(g_j^-L0 Z_j,eta_j^-L0 V_j). On the cut parameter interval take
logarithms G_j=log(g_j), H_j=log(eta_j), and a cutoff chi that is zero
on the initial collar and one on the terminal collar. The coordinate
map has multipliers A=exp(L0 chi G_j), D=exp(L0 chi H_j).
It has the explicit inverse with negative exponents and cancels the
bounded closing on the entire terminal collar with all derivatives.
All its multipliers depend only on the unchanged q and v, so it
commutes with both full periods and the physical circle. Its vertex
maps are exactly

\[
 (a_0,b_0,c_0)\mapsto((AD)^{-1}a_0,Ab_0,Dc_0),
 \quad(u_0,v_0,w_0)\mapsto(ADu_0,D^{-1}v_0,A^{-1}w_0).
                                                        \tag{ZV.4}
\]

The products in both charts remain q. The three period rows are
DZ.8 with the full coefficients (ZV.3). Thus these are closed charts
of the actual family. The doubled seam is its literal pullback:
on lap ell=0,1 use C_tau E_tau^-ell. The two formulas agree on the
middle collar and cancel E² at the last collar, just as DZ.8a.
The full cap square and every finite character remain the same.

## ZV.2. The complete doubled product and its integral nonfixed entries

On the literal double parameter cover, set

\[
 \mathcal B_j=2P_j^{-1}WP_j,
 \quad t=N-1,
 \quad l=(\mathcal B_{22}-\mathcal B_{21},
          \mathcal B_{11}-\mathcal B_{12},\mathcal B_{22}).
                                                        \tag{ZV.5}
\]

In particular

\[
 l_0=2\{N+a-2+(3-N-b)j+bj^2\},\quad
 l_1=2\{1+b(j-1)\},\quad l_2=2(N-2-bj).
                                                        \tag{ZV.6}
\]

Their normal transition matrices are the actual DZ.10 matrices
diag(eta_j/alpha_j,kappa_j alpha_j),
diag(kappa_j/g_j,g_j eta_j), and diag(eta_j,kappa_j).
Their determinant winding is 2t. Each based coefficient equals its
angular factor times the exponential of its actual periodic logarithm.
Use precisely the based quaternion maps H_d of DZ.12, with integral
d, and the normal map H_t Q H_(l_i-t), multiplied by those full
logarithmic units with a protected radial cutoff. Its second radial
endpoint is exactly the original diagonal matrix, not its valuation.
The same normal-rescaling isotopy and cutoff velocity as DZ.14
restore all higher terms and keep both vertex collars fixed. This
constructs an ordinary product of the entire doubled three-curve
plumbing and its rounded boundary.

The physical weights are w=(0,1,-1) and d=(-2,-1,-1). They remain
these actual weights because P_j^-1 e2=e2. The same explicit Hopf
trace and full stable derivative of DZ.16--18 give

\[
 I_i=t w_i+d_i(l_i-t),\qquad
 W_i=t w_i-d_i(l_i-t).                              \tag{ZV.7}
\]

The parameter-independent vertex caps, generic normal sections and
ambient-frame homotopy are those in DZ.3, transported by (ZV.3)--(ZV.4).
Consequently the two literal action/derivative prism identities are

\[
 V(w_i e_i-w_0e_0)=I_i e_i-I_0e_0,\qquad
 w_i\delta_i-w_0\delta_0=W_i-W_0.                  \tag{ZV.8}
\]

For the nonfixed C1 curve, w0=0 and w1=1. These determine its complete
selected entries without any fixed-star entry:

\[
 V_{11}=I_1=2t-l_1,\qquad
 \delta_1=W_1-W_0=l_1-2l_0+2t.                     \tag{ZV.9}
\]

## ZV.3. The actual single native C1 product and oriented flop

The native chart is explicit. In the first vertex use
(z,n0,n1)=(c0,a0,b0); in the second use

\[
 (z',n'_0,n'_1)=(\eta_jv_0,\ g_jw_0,\ u_0/(g_j\eta_j)).
                                                        \tag{ZV.10}
\]

The full C1 row of DZ.8 gives z'=z^-1 and n'=z n. Both products
are q. These functions are nonzero and periodic on the closed
single-loop chart; their integer winding has not been replaced by a
logarithm. Thus (ZV.10) is a literal native product of this one star.
The normal-order interchange needed for its Q1 flop is the constant
unitary path of K71.6. It conjugates both Spin factors by fixed
orientation-preserving lifts and preserves their third degrees.

On the doubled cover the native-to-ordinary boundary coefficient map
is (U H_t U^-1) q_H H_(l1-t), with the same full unit homotopy as above.
The left degree is 2t; the right factor has third degree zero because
it has only the radial and parameter variables. The actual inverse
cylinder extension has endpoint degrees (-2t,0) and extends over the
normal D4. Therefore the native right free integer equals the ordinary
right free integer. The ambient-to-star frame map of K31, carried by
(ZV.10), gives that doubled integer as (delta1-V11)/2.

The doubled native product is the literal pullback of (ZV.10) with
the doubled seam in ZV.1. Choose a complete global connection having
this boundary product and pull it back to the two-sheeted parameter
cover. The relative return is the square of the actual single return.
The right free coordinate is a homomorphism to Z, so the single
native right integer is exactly

\[
 r_j=\frac{\delta_1-V_{11}}4
       =\frac{l_1-l_0}{2}
       =-N+(N+2b-3)j-bj^2.                         \tag{ZV.11}
\]

This uses division in a proved integral free coordinate of an actual
square. Every l_i is even, and the displayed polynomial is integral.
No Theta7 class or arbitrary integer lift has been divided.

The full seam extends to the common Cox chart of this C1 star.
With z=a1/a0 and n_i=a0 c_i, the actual lift of (ZV.4) is

\[
 (a_0,a_1,c_0,c_1)\mapsto
       (a_0,Da_1,(AD)^{-1}c_0,Ac_1).                \tag{ZV.12}
\]

It preserves q=a0 a1 c0 c1 and both the auxiliary and physical circle
actions. Since q is unchanged, its inverse uses the reciprocal full
functions at that same q. It therefore extends through both small
resolutions. The other-ruling charts are the actual maps
(n0/n1,z n1,n1) and (n1/n0,z n0,n0), with the stated constant
normal interchange. They retain the common rank-one matrix and all
full period multipliers. Their cone bases are P_j Q1=P_(j-1),
Q1=((1,0),(-1,1)). On the common link the Hopf arrow is
(h,q_H) to (q_H^-1 h q_H,q_H), with K68 physical orientation.
The exact Cox conjugation consequently changes the central sphere
class by the actual right integer r_j. Thus

\[
                         Z_{j-1}-Z_j=r_j.          \tag{ZV.13}
\]

All maps are the identity on the matched common exterior after their
inverse character identification. Hence the original source, finite
cap, signed norm and full annular closing are still the same data.
The common blowup and both primitive exceptional rulings preserve
the proved integral sphere topology, as in F35.

## ZV.4. Summation and evaluation

The integer polynomial

\[
 F(j)=2b\binom{j+1}{3}+(3-b)\binom{j+1}{2}
                                          -N\binom j2
\]

satisfies F(0)=0 and F(j-1)-F(j)=r_j as exact identities for every
integer j. The inverse of the actual flop supplies the negative steps
as well. Induction in either direction proves (ZV.1). For a=2,b=1,
Pascal's exact polynomial identity gives F(j)=2 binom(j+2,3)-N binom(j,2).
Substitution of the audited reduced attachment and RT.12 gives (ZV.2).
In particular j=1 is the already marked opposite-diagonal fan and
has Z1-Z0=a in both branches, agreeing with the independent K60
single native diagonal map. The new recurrence extends that
calculation to every integer vertical fan without assigning any
unknown fixed-star free coordinate from a finite-group residue.

The independent exact program
`code/part3_root/source_zero_vertical_fans.py` executes the full
matrix conjugation, primitive prism entries, native-chart products,
Cox seam, recurrence and integer-valued formulas. Its bounded examples
are checks of the symbolic proof, not its arbitrary-integer argument.
