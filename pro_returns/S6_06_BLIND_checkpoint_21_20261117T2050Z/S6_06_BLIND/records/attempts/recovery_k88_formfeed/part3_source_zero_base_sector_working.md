# The fixed-scalar source-zero return in the T0 sector

Recovered mathematical text for P3K.88. The original working source was
lost with the execution environment after checkpoint19. Its audited initial
integers, full maps, recurrence, witness construction and orientation are
retained here; this file does not claim the old source hash.

## ZB.1. The specified family and its initial integer pair

We retain the actual source
\[
Y^2=X^3+(1-2v)X^2+TX+v^2,\qquad G=(0,v),\qquad
q=T-(v^2-2v).
\]
The positive source loop is a small counterclockwise circle about
\(v=0\). Its scalar is fixed in the compact admissible annulus. The
marked datum is \((a,b)=(1,2)\), with good cap order \(4p\), or
\((a,b)=(2,1)\), with reduced cap order \(4p-1\), \(p\ge1\).
Both cap norm signs, every finite character and the full annular cochain
are retained. The orientation and physical line \(M\) are those of K68.

K80 and K83 identify the actual initial return with physical integer
zero. K86 computes the complete relative normal correction over the
horizontal normalization, the removed four-ball and their common
boundary. It gives \(\Gamma=0\), including both full Cartier factors.
Consequently its initial physical pair is \((1,4)\) for \(a=1\) and
\((0,0)\) for \(a=2\). Write \(\mu=2-a\). The initial native free
coordinates are \((\mu,0)\); these are integers supplied by the full
normal comparison. They are the inputs to the computation below.

## ZB.2. The full source, period and flop arrows

The actual marked periods have the form
\[
h=(\kappa qZ,\alpha V),\qquad B=(gZ,q\eta V),
\qquad
\operatorname{wind}_v(\kappa,\alpha,g,\eta)=(1,-a,b,-2).
\]
All four functions are the original nonzero holomorphic units. In
particular their bounded dependence on \(q\) is retained. Their winding
matrix is
\[
W=\begin{pmatrix}1&b\\-a&-2\end{pmatrix}.
\]
For a basis change \(Q\in SL_2(\mathbb Z)\), character substitution
and the inverse period basis give the complete multiplier formula
\[
U'_{is}=\prod_{h,j}U_{hj}^{(Q^{-1})_{ih}Q_{js}}.             \tag{ZB.1}
\]
This equality holds for the units themselves. Its valuation part leaves
the \(q\)-valuation matrix equal to the identity.

Put
\[
Q_0=\begin{pmatrix}1&-1\\0&1\end{pmatrix},\qquad
Q_1=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
\]
We start with \(T_0\), take \(Q_0\) first, and then use any finite
word in these two matrices. In a native source chart
\((z,n_0,n_1)\), the two other-ruling charts are
\[
(n_0/n_1,zn_1,n_1),\qquad(n_1/n_0,zn_0,n_0).              \tag{ZB.2}
\]
They have the same rank-one matrix and the same function
\(q=zn_0n_1\). The second type also interchanges the two normals by
the actual unitary path
\[
\frac12\begin{pmatrix}
1+e^{\pi is}&1-e^{\pi is}\\1-e^{\pi is}&1+e^{\pi is}
\end{pmatrix},\qquad 0\le s\le1.                         \tag{ZB.3}
\]
This path commutes with the scalar normal transition \(zI\).
For full multipliers \((A,D)\), the Cox lift is
\[
(a_0,a_1,c_0,c_1)\longmapsto
(a_0,Aa_1,(AD)^{-1}c_0,Dc_1).                            \tag{ZB.4}
\]
The quotient is the required holomorphic change on each stable chart.
On its exterior it is the same inverse character substitution as
(ZB.1). Thus the actual Cartier line, all finite roots and characters,
and the prescribed closing arrow commute with the comparison there.
The source and finite cap maps are unchanged on that common exterior.

The based logarithms of the full unit ratios extend through a radial
collar. Multiplying those logarithms by the fixed collar cutoff gives
the explicit unit homotopy relative to its two boundary ends. The
remaining winding factors act on the native quaternion by
\(H_{-1}q_HH_{\ell_i+1}\). The Hopf comparison has left degree
\(-2\) and right degree zero; its inverse cylinder has left degree
\(+2\). This identifies the ordinary double used below with the
same full normal framing as K86 on each selected star.

## ZB.3. The full integer prism seed and target solution

For any current basis \(P\), let
\[
\begin{aligned}
B_P&=2P^{-1}WP,&
\ell&=(B_{22}-B_{21},B_{11}-B_{12},B_{22}),\\
(x,y)^t&=P^{-1}e_2,& w&=(x,y,-x-y),\\
d&=(-x-2y,-2x-y,x-y),\\
I_i&=-w_i+d_i(\ell_i+1),&
J_i&=-w_i-d_i(\ell_i+1).
\end{aligned}                                           \tag{ZB.5}
\]
The doubled ordinary product has variation matrix \(V\), stable
derivative \(\delta\), and the integral prism equations
\[
\begin{aligned}
V(w_i e_i-w_0e_0)&=I_ie_i-I_0e_0,\\
w_i\delta_i-w_0\delta_0&=J_i-J_0,\qquad i=1,2.
\end{aligned}                                           \tag{ZB.6}
\]
The complete initial values, from the native pair and inverse cylinder
above, are
\[
\begin{aligned}
c&=-2\mu-2,\\
V&=\begin{pmatrix}
c&4a-6&6-4a\\4a-6&2b-4&0\\6-4a&0&-4
\end{pmatrix},\\
\delta&=(c,8-4a-2b,4a-4),\qquad S=0.
\end{aligned}                                           \tag{ZB.7}
\]
In particular the fixed entry is specified as an integer.

At a selected old curve \(i=0,1\), put
\(c=V_{ii}\), \(e=\delta_i\). Its actual single native right
coordinate is \(\rho=(e-c)/4\). The divisor four comes from
the literal doubled product and its already fixed native comparison.
The common Cox link is
\((h,q_H)\mapsto(q_H^{-1}hq_H,q_H)\). It acts by
\[
(\mu,\rho,S)\longmapsto(\mu+2\rho,-\rho,S+\rho).
                                                               \tag{ZB.8}
\]
The sign of the last coordinate is the physical K68 orientation.
After the same ordinary cylinder on both sides the target selected
curve is labelled two, and
\[
V'_{22}=c,\qquad\delta'_2=2c-e,\qquad S'=S+(e-c)/4.
                                                               \tag{ZB.9}
\]
Every target in the specified word has three nonzero weights. Use its
own \(I,J,w\), and set
\[
C=w_2^2c-w_2I_2,\qquad E=w_2(2c-e)-J_2.
\]
The complete target solution is
\[
V'_{rs}=\frac{I_r}{w_r}\delta_{rs}+rac{C}{w_rw_s},
\qquad\delta'_r=\frac{J_r+E}{w_r}.                       \tag{ZB.10}
\]
Indeed substitution verifies every prism equation and the two selected
entries. A symmetric difference annihilates the plane spanned by
\(w_i e_i-w_0e_0\), hence has the form
\(C'(1/w_r)(1/w_s)\); the selected entry makes \(C'=0\).
The derivative difference is a multiple of \((1/w_r)\), and its
selected entry also vanishes. These arguments prove uniqueness. The
actual target product constructed in ZB.2 supplies an integral
solution; therefore this rational expression equals its integral
invariants. The coordinate \(\rho\) in (ZB.8) is its actual free
integer. No finite-group residue enters this reconstruction.

## ZB.4. Every residue is exhibited by a complete actual word

We enumerate every word beginning with \(Q_0\) and having length one
through ten: 1,023 words on each branch. Their positive first row has
the form \((u,-r)\), \(u,r>0\), so all target weights are nonzero.
The reverse Euclidean construction terminates at \(T_0\) for each
word, as verified independently by its exact integer factorization.
Equations (ZB.7)--(ZB.10) evaluate every word without a residue lift.
The first two length-two examples \(Q_0^2,Q_0Q_1\) give classes
\(6,6\) for \(a=1\) and \(9,0\) for \(a=2\).

For each residue we choose a witness by the lexicographic score
consisting of maximum entry size, sum of entry sizes, word length,
and the four matrix entries. The following two tables give all 28
residues, their actual bases and their computed integer sums. A basis
entry \((u,v;x,y)\) denotes the matrix with those two rows.

\par\medskip\noindent\textbf{Good branch, \(a=1,b=2\).}
\input{notes/part3_source_zero_base_sector_witnesses_a1.tex}

\par\medskip\noindent\textbf{Reduced branch, \(a=2,b=1\).}
\input{notes/part3_source_zero_base_sector_witnesses_a2.tex}

The executable certificate is
`code/part3_root/source_zero_base_sector.py`. Its JSON gives each
full variation matrix, derivative, finite word and successive native
right increments. The original independent audit solved 282 full
target linear systems for these 56 witnesses and checked every
coefficient-conjugation equation. The recovered independent K90
Gaussian audit is separately saved with its exact deterministic
checksum. The finite witness list proves surjectivity onto
\(\Theta_7=\mathbb Z/28\) for each of these two specified
fixed-scalar source-zero fan families.
