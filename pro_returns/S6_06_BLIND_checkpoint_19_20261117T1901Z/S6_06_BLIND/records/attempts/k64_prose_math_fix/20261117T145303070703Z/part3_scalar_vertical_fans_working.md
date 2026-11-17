# Exact scalar returns on the physical-vertical-edge fans

Proved as P3K.64 after full root and checks audits, 17 November 2026.
This extends the
actual first-star calculation K62 by its literal integral
shear maps. It does not use the simultaneous equivariant
product or rank-one initial data previously invoked in K29.
The arbitrary-fan formula remains outside this calculation.

## SV.1. The actual shear, periods and closing

Retain one of K62's actual fixed-source scalar families,
with its protected whole-zero nodal cusp and full periods
\[
 h:(Z,V)\mapsto(\kappa qZ,\alpha V),\qquad
 B:(Z,V)\mapsto(gZ,q\eta V),\qquad \eta=\lambda\beta.
\]
All of \(\kappa,\alpha,g,\beta\) are independent of the
scalar parameter. Write \(J\in\mathbb Z\) for its actual
scalar winding. The forward ordinary closing, with its
already constructed cap arrow, is \(q^e\) times its
specified bounded source-independent unit. The canonical
scalar loops of K26/K28/K32 retain exactly these arrows.

For each integer \(n\), use the physical-vertical-edge
fan \(T_n\) with directions
\[
             e_2,\quad (1,n),\quad(1,n-1).
\]
On its torus the literal coordinate and period maps are
\[
 Z_n=Z,\quad V_n=Z^{-n}V,\qquad h_n=hB^n,\quad B_n=B.
                                                        \tag{SV.1}
\]
They preserve the physical circle and the original height
\(q\). In these actual coordinates the full periods are
\[
 \begin{split}
 h_n:(Z_n,V_n)&\mapsto(\kappa_n qZ_n,\alpha_n V_n),\\
 B_n:(Z_n,V_n)&\mapsto(g_nZ_n,q\eta_nV_n),\\
 \kappa_n&=\kappa g^n,\qquad
 \alpha_n=\alpha\eta^n\kappa^{-n}g^{-n^2},\\
 g_n&=g,\qquad \eta_n=\eta g^{-n}.
 \end{split}                                          \tag{SV.2}
\]
These identities follow by substituting (SV.1) in each
original period, including its line coordinate. The
integer labels of \(h_n,B_n\) are the standard two basis
vectors in the new characters, so their period orbit
still has one vertex and no stabilizer of a chosen
star representative.

The actual winding vector is consequently
\[
 \bigl(\operatorname{wind}\kappa_n,
       \operatorname{wind}\alpha_n,
       \operatorname{wind}g_n,
       \operatorname{wind}\eta_n\bigr)
                    =(0,nJ,0,J).                    \tag{SV.3}
\]
There is no assertion that the new source line is an
unmarked replacement for the old one. Its actual
character map is \(V_n=Z^{-n}V\).

The ordinary closing remains \(q^e\) in these characters.
Reindexing by \(B_n^{-e}\) gives the full bounded
endpoint \(E_n=(g^{-e},\eta_n^{-e})\), with the retained
bounded closing unit included in its second factor.
On the cut parameter interval take its actual
logarithms and use
\[
 C_\tau:(Z_n,V_n)\mapsto(AZ_n,DV_n),\quad
 A=\exp(e\chi\log g),\quad
 D=\exp(e\chi\log\eta_n)                              \tag{SV.4}
\]
and the inverse logarithm of that bounded closing
unit in \(D\). The cutoff is zero on the first collar
and one on the last. Thus \(C_{\rm end}E_n=1\)
with every derivative. It commutes with all actual
periods and the physical circle. The two vertex
chart expressions are exactly
\[
 (a,b,c)\mapsto((AD)^{-1}a,Ab,Dc),\qquad
 (u,v,w)\mapsto(ADu,D^{-1}v,A^{-1}w).
                                                        \tag{SV.5}
\]
They preserve every transition row with the full units
\(\kappa_n,\alpha_n,g_n,\eta_n\).
Use on the degree-two parameter cover the literal
pullback
\[
          C^{(2)}_{j+\tau}=C_\tau E_n^{-j},\quad j=0,1.
                                                        \tag{SV.6}
\]
This retains the original ordinary and cap endpoint
squares and gives \(E_n^{-1},E_n^{-2}\) at its two
successive collars. No new seam is selected for the
doubled return.

## SV.2. The closed ordinary product and exact trace

The three native normal transitions are the ones of
K47/K62 with the full units (SV.2). In the second
vertex product \((u,\eta_n v,\kappa_n w)\), their
based double-loop normal matrices are
\[
 \begin{split}
 K_0&=\operatorname{diag}
       (e^{2iJ(1-n)\theta},e^{2inJ\theta}),\\
 K_1&=\operatorname{diag}(1,e^{2iJ\theta}),\\
 K_2&=\operatorname{diag}(e^{2iJ\theta},1).
 \end{split}                                          \tag{SV.7}
\]
For example their first coordinate factors before
reference division are \(\eta_n/\alpha_n\),
\(\kappa_n/g_n\), and \(\eta_n\), respectively.
Their second coordinate factors are
\(\kappa_n\alpha_n\), \(g_n\eta_n\), and
\(\kappa_n\). This proves (SV.7) from the actual
native coordinate arrows. The determinant is
\(e^{2iJ\theta}\) in every row.

Use the explicit quaternion contractions of DZ.12
with
\[
 t=J,\qquad
 l=\bigl(2J(1-n),0,2J\bigr),\qquad
                 Q\mapsto H_t QH_{l_i-t}.            \tag{SV.8}
\]
The equality of the determinant loops makes the
first vertex product common to all three stars.
Each remaining determinant-one normal loop is
contracted by that displayed \(H\) map. The actual
normal-rescaling and cutoff-flow construction of
DZ.2 carries the higher derivatives and retains
the full nonzero unit germs. The scalar factors
with nonzero winding are the exact powers in
(SV.7); every other based unit has its fixed
logarithm. Thus this is a closed ordinary product
of the doubled marked plumbing. It is not claimed
to intertwine the physical circle.

The physical tangent and normal weights in these
characters remain
\[
                  w=(0,1,-1),\qquad d=(-2,-1,-1).
\]
Use the literal orbit map DZ.16 and its derivative
in the covering group of stable \(GL^+\). Their
degrees are
\[
 \begin{split}
 I_i&=t w_i+d_i(l_i-t),&
 I&=(-2J+4nJ,\,2J,\,-2J),\\
 W_i&=t w_i-d_i(l_i-t),&
 W&=(2J-4nJ,\,0,\,0).
 \end{split}                                          \tag{SV.9}
\]
The same generic vertex paths and rank-one endpoint
caps as in DZ.3 close these exact traces. The
parameter-dependent vertices are (SV.5), so they
commute with the diagonal physical action and
their endpoint traces remain independent of the
parameter. No extra vertex meridian is inserted.
The coordinate-frame changes extend over the
annulus times its normal four-disc, exactly as
in the proved stable-trace comparison.

The integral prism identities now give
\[
 \begin{array}{c|cc|cc}
 &V_{ii}&\delta_i&m_i^{\rm ord}&n_i^{\rm ord}\\ \hline
 C_1&2J&-2J+4nJ&-2nJ&2J(n-1)\\
 C_2&2J& 2J-4nJ&2J(n-1)&-2nJ .
 \end{array}                                          \tag{SV.10}
\]
Here \(2n_i^{\rm ord}=\delta_i-V_{ii}\) uses only
the actual local ambient-to-single-star frame map,
not the earlier scalar initial-variation assertion.

## SV.3. The native pairs, exact flops and recurrence

The native \(C_1\) coordinates are
\[
 (c,a,b),\qquad
       (\eta_n v,g_nw,(g_n\eta_n)^{-1}u),
\]
and the native \(C_2\) coordinates are
\((a,b,c),(u,v,w)\). Their exact transitions are
\(z'=z^{-1},n'_i=zn_i\). On each star the change
to (SV.8) is
\[
                q_H\mapsto
                   (UH_JU^{-1})q_HH_{l_i-J}.         \tag{SV.11}
\]
Its left degree is \(2J\), and its right degree
is zero. The inverse cylinder extension has
endpoint \(L^{-2J}\), with coefficient maps
extending over \(D^3\times D^4\). Thus the native
doubled pairs are obtained from (SV.10) by adding
\(2J\) to the left coordinate:
\[
 C_1:\ (2J(1-n),2J(n-1)),\qquad
 C_2:\ (2nJ,-2nJ).                                   \tag{SV.12}
\]

The boundary products and seams (SV.6) are literal
pullbacks of the single native products. Pull back
a connection with those exact boundary products.
Its return is the actual relative square. Any
connection used in (SV.8)--(SV.11) with the same
boundary product interpolates to that one relative
to the boundary. The free-coordinate map to
\(\mathbb Z^2\) therefore gives the actual single
pairs
\[
 C_1:\ (J(1-n),J(n-1)),\qquad
 C_2:\ (nJ,-nJ).                                     \tag{SV.13}
\]
This is injectivity of multiplication by two in
the free relative group, not division of a
seven-sphere class.

The full Cox lifts of (SV.5) are
\[
 \begin{split}
 C_1:\ &(a_0,a_1,c_0,c_1)
       \mapsto(a_0,Da_1,(AD)^{-1}c_0,Ac_1),\\
 C_2:\ &(a_0,a_1,c_0,c_1)
       \mapsto(a_0,(AD)^{-1}a_1,Ac_0,Dc_1).
 \end{split}                                          \tag{SV.14}
\]
Each preserves the actual height monomial and
extends through both resolutions. Transport the
metric by the full unit map and use its positive
radial normalization on the link. The unrestricted
four-weight common-link identity then gives the
literal \(T(y,q_H)=(q_H^{-1}yq_H,q_H)\) extension,
with the same fixed complex-normal reset as K62.
Equivariance under \(h_n,B_n\) carries one chosen
free star representative to the whole periodic
orbit. The outside source, line and finite-cap
maps are unchanged.

In the actual lattice marking, flipping \(C_2\)
replaces direction \((1,n-1)\) by \((1,n+1)\);
the new fan is \(T_{n+1}\). Flipping \(C_1\)
replaces \((1,n)\) by \((1,n-2)\), giving
\(T_{n-1}\). These are the literal two diagonal
replacements in the periodic squares, with the
same period group and positive height.
The actual Cox conjugation changes the central
coordinate by the right native integer. Hence
\[
 A_{n+1}-A_n=-nJ,\qquad
 A_{n-1}-A_n=(n-1)J.                                \tag{SV.15}
\]
The two are inverse statements for the same
oriented elementary comparison. Their exact
telescoping, with the independently computed
initial fixed-star value \(A_0\), gives
\[
                   A_n=A_0-J\,\frac{n(n-1)}2
                          \quad\text{in }\mathbb Z/28.
                                                        \tag{SV.16}
\]
The integer \(n(n-1)/2\) is integral for every
positive, zero or negative \(n\). At \(n=0\)
the two first comparisons agree with K62.
This computation covers the displayed vertical
line of fans only. It makes no assertion about
the arbitrary-fan recurrence quarantined after
the scalar determinant obstruction.


The exact certificate is code/part3/scalar_vertical_fans.py, with its
JSON and captured output. It verifies 14 symbolic identities and 425
signed instances. The actual maps and relative comparison were independently
audited by root and checks before promotion. The scope retains canonical
ordinary closing by q^e times the specified source-independent bounded unit;
shorter endpoints with an additional source translation are not included.
