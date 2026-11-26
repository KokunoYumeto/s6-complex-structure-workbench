#!/usr/bin/env python3
"""Assemble one LP theorem/proof from its released text and completed proofs.

All changes are confined to the receiving lane. Original and frozen input
files are read-only. This is a source assembly, not a mathematical execution.
"""
from pathlib import Path
from hashlib import sha256
import re

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'agents/continuation7_iii_weighted_cups_root'
STAGE = ROOT / 'agents/continuation7_iii_weighted_cups_receiving'
P = 'S6_SERIES_PUBLISH_III_02LP'


def sha(s):
    return sha256(s if isinstance(s, bytes) else s.encode()).hexdigest()


statement = (SOURCE / f'{P}_released_statement.tex').read_text()
statement = statement[statement.index(r'\begin{theorem}'):].strip()
original = (SOURCE / f'{P}_released_proof.tex').read_text()
original = original[original.index(r'\begin{proof}'):].strip()
assert sha(original) == '576e201fe7ec50fc93f3a9844c7e48d8a7dee5ff4c15b1f15911a8af33b0a5b8'
blocks = re.findall(r'\\begin\{proof\}(?:\[[^]]*\])?([\s\S]*?)\\end\{proof\}', original)
assert len(blocks) == 2
items = []
for b in blocks:
    q = re.split(r'\\item\s+', b)[1:]
    q[-1] = q[-1][:q[-1].rfind(r'\end{enumerate}')].rstrip()
    items.append(q)
first, second = items
assert len(first) == 11 and len(second) == 18
statement = re.sub(r'^\\StatementRecord.*$', r'\\textnormal{\\small tag 02LP.}',
                   statement, flags=re.M)
statement = statement.replace('for any $d>0$', 'for any positive integer $d$')
statement = re.sub(r'\n{3,}', '\n\n', statement)

marking = r"""
\emph{The marked groups and primitive component classes.}
Use the physical lattice $(\delta,a,b,\gamma)$ and the alternating form
$\xi=a^*\wedge b^*+6d\gamma^*\wedge\delta^*$.
Put $s=[a\wedge b]$. The full normal maps of
\ref{maps:src:D.2.34} give, in coordinates $(s,t,t'_0,t'_1)$,
the six relation columns
\[
\begin{split}
C_{01}&=(-2dn_0,-k,0,0),&
C_{02}&=(-6dr_0,0,m_0,0),&
C_{03}&=(0,r_0,n_0,0),\\
C_{11}&=(-3dn_1,2\ell,0,0),&
C_{12}&=(-6dr_1,0,0,m_1),&
C_{13}&=(0,-r_1,0,n_1).
\end{split}
\]
Every common divisor of $m_i,n_i$ or of $m_0,m_1$ divides $P$.
Thus these pairs are coprime and $\gcd(k,2\ell)=1$.
The surviving Seifert relation matrix and its integral inverse are
\[
 R=\begin{pmatrix}-n_0&m_0\\-n_1&-m_1\end{pmatrix},
 \qquad R^{-1}=P\begin{pmatrix}-m_1&-m_0\\n_1&-n_0\end{pmatrix}.
\]
They eliminate every loop, proving simple connectivity.

Let $B$ be the six-column normal matrix and $e_{ij}$ its source basis.
The following formulas give the full inverse quotient marking.
Set $R_d=-P(2\ell e_{01}+k e_{11})$, so $BR_d=ds$.
Choose $A,B_0$ with $-kA+2\ell B_0=1$, and put
$q=2An_0+3B_0n_1$ and $R_t=Ae_{01}+B_0e_{11}+qR_d$.
Then $BR_t=t$. Choose $\alpha_i m_i+\eta_i n_i=1$ and put
$C_i'=\alpha_i e_{i2}+\eta_i e_{i3}$. The remaining inverse columns are
\[
 R_{t_0}=C_0'+6r_0\alpha_0R_d-r_0\eta_0R_t,\qquad
 R_{t_1}=C_1'+6r_1\alpha_1R_d+r_1\eta_1R_t,
\]
with images $t'_0,t'_1$. Since every first coordinate of $B$ is
divisible by $d$, the quotient and its inverse are
\[
 \operatorname{coker}B\longrightarrow\mathbb Z/d,\quad
 [(z_s,z_t,z_0,z_1)]\longmapsto[z_s],
 \qquad [j]\longmapsto[js].
\]
For a kernel vector the exact preimage is
$(z_s/d)R_d+z_tR_t+z_0R_{t_0}+z_1R_{t_1}$.

Let $E$ be the exterior after filling the two finite caps and before
adjoining the cusp. Its first homology is
\[
 \langle\gamma,x'_0,x'_1\mid m_0x'_0=n_0\gamma,\
                                  m_1x'_1=n_1\gamma\rangle.
\]
The quotient map sends $(z_\gamma,z_0,z_1)$ to
$m_0m_1z_\gamma+n_0m_1z_0+m_0n_1z_1$.
Its inverse sends $1$ to $P(x'_0+x'_1)$: the two relation columns
together with this vector have determinant $P^2=1$.
Thus the cusp meridian $x'_0+x'_1$ has primitive value $P$.
The actual normal-disc differences in the cusp give a section of
the relative augmentation map $\mathbb Z^d\to\mathbb Z$.
Together with the quotient above they give
\[
 H_2(X)=\mathbb Z^{d-1}\oplus(\mathbb Z/d)\langle s\rangle,
 \quad H_3(X)=\mathbb Z/d,\quad H_1=H_5=0,\quad b_3=0.
\]
The maps retain all cusp boundary torsion and hold for every
$k,\ell,n_i,r_i$ in \eqref{maps:eq:D.WI1}.

The dual relative Thom map is therefore
\[
 H^1(E)\longrightarrow H^2(X,E)=\mathbb Z^d,\qquad
                   1\longmapsto\pm(1,\ldots,1).
 \tag{D.WI4}\hypertarget{tag-027I}{}\label{maps:eq:D.WI4}
\]
Its cokernel injects into $H^2(X)$ with rank-zero quotient inside
the torsion-free group $H^2(E)$. Hence it is all of $H^2(X)$.
The classes are the actual Cartier divisors $x_i=\operatorname{PD}(D_i)$;
at a self-identification the local equation is the product of the
branch coordinates. The inverse reads evaluation on the normal-disc
differences. Their sole relation is $\sum_i x_i=0$, so
$f_X^*[\mathrm{point}]=0$. Each reduced finite multiple-fibre divisor
also has zero class, since its positive multiple is this fibre class
and $H^2(X;\mathbb Z)$ is free.
"""

ruling = r"""
\emph{The actual ruling and the divisor products.}
In short coordinates $(a,\delta)$ and long coordinates $(b,\gamma)$,
the valuation sends $b$ to $e_1$ and $\gamma$ to $de_2$.
The prescribed rays
$e_1,e_2,e_2-e_1,-e_1,-e_2,e_1-e_2$ have boundary curves
\[
 H-E_A-E_C,\quad E_A,\quad H-E_A-E_B,\quad
 E_B,\quad H-E_B-E_C,\quad E_C.
\]
The notation in the statement is
$E_1=E_B,E_2=E_C,E_3=E_A$, with inverse
$E_A=E_3,E_B=E_1,E_C=E_2$.
In the toric chain construction of \ref{maps:src:D.1.9}, substitute
$(\widehat u,\widehat w,\widehat\delta,\widehat\gamma)
=(b,a,\delta,-\gamma_1)$, with inverse
$(a,b,\delta,\gamma_1)
=(\widehat w,\widehat u,\widehat\delta,-\widehat\gamma)$.
Apply its normal-disc and period-cylinder maps to the current
holomorphic period functions, retaining their units.
The ruling has relative vector $n_{2e}-2n_e+n_0$, and the diagonal
has $n_{e_1+e_2}-n_{e_1}-n_{e_2}+n_0$.
Injectivity into the toric relative group, followed by cancellation
of translated normal discs, gives the actual chains
\[
 E_A+E_C=-T(b,a)=T(a,b),\quad
 E_B+E_C=T(-\gamma_1,\delta)=T(\delta,\gamma_1),\quad
 E_C=-T(b,\delta).
\]
In particular the positive ruling $f=H-E_B$ has in the period
quotient the same image as $E_A+E_C$, and maps to $s$, with sign fixed by
$T(b,a)=-T(a,b)$. Its $\xi$ value is one; $E_C$ has value zero.
The inverse marking reads the same short and long coordinates.
This is a unit-period chain comparison and applies in every
$\gamma$ component of the degree-$d$ period cover.

The two branch curves at each neighbouring component intersection
sum to $f$. The two directed incidences remain distinct when $d=2$.
Multiplying $\sum_i x_i=0$ by $x_j$ fixes the diagonal coefficient,
giving \eqref{maps:eq:D.WI3}. At $d=1$ the only class is zero;
at $d=2$ both off-diagonal coefficients are two and $2\kappa=0$.
Every integral cubic is zero, since its degree-four product is
torsion and $H^6(X;\mathbb Z)=\mathbb Z$.
"""

chern = first[2].replace(
    'The differential and its literal critical cycle.',
    'The tangent classes and normalized components.')
kernel = first[3].replace('Its\ncorrected target', 'Its\ntarget')
kernel = kernel.replace(
    'at a triple point they are $(x,-y,0)$ and $(x,0,-z)$.',
    r"""at a triple point they are $(x,-y,0)$ and $(x,0,-z)$.
Indeed $yzA+xzB+xyC=0$ implies $A=xA'$, $B=yB'$, $C=zC'$
by reduction modulo each coordinate in the convergent power-series
domain, and then $A'+B'+C'=0$. These are exactly the two displayed
columns, with inverse coefficient extraction. The node calculation
is the same divisibility argument. A Hermitian complement to
$\delta$ and a unit section give a global frame $(\delta,v_2)$ of $V$.
Outside the critical cycle, a unit frame of $L$ lifts through
$df^*/\|df\|^2$; kernel projection and $df$ give its inverse.""")
critical = first[4] + '\n\n' + first[5]
critical = critical.replace(r'\ref{maps:src:D.2.44}--\ref{maps:src:D.2.45}',
                            r'\ref{maps:src:D.2.44}')
critical = critical.replace('Only a local covering is used to compute $[C]$.',
                            'The cusp period covering computes $[C]$.')
critical = critical.replace('No covering of either finite logarithmic cap is assumed.', '')
critical = critical.replace(
    "the weight-one cusp's literal\nthree-curve sum has regular-fibre preimage",
    "the three chain equalities above identify the weight-one cusp's\nthree-curve sum with")

line = r"""
\emph{One integral auxiliary line and all period maps.}
Let $W$ consist of the regular core and the cusp, leaving both finite
discs unfilled. Its group is $\pi_1(W)=\mathbb Z\langle\gamma,x\rangle$.
For the actual core monodromies in the basis $(\delta,a,b,\gamma)$,
\[
A_0=\begin{pmatrix}1&-1&0&2d\\0&-1&-1&6d\\0&1&0&0\\0&0&0&1\end{pmatrix},
\quad
A_1=\begin{pmatrix}1&0&1&-3d\\0&0&1&0\\0&-1&0&6d\\0&0&0&1\end{pmatrix},
\quad A_\infty=I+E_{23}+dE_{14},
\]
the quadratic refinement $q(\lambda)=\lambda_a\lambda_b+
\lambda_a+\lambda_b\bmod2$ is invariant. Its polarization is
$\xi\bmod2$; direct substitution in both displayed matrices proves
invariance, with every additional term even as an integer-valued
polynomial. Consequently
\[
 J_\lambda(x,z)=
 (x+\lambda,(-1)^{q(\lambda)}e^{\pi i\xi(\lambda,x)}z)
\]
satisfies the exact lattice cocycle identity.
The connection $d-\pi i\xi(x,dx)$ has Chern class $\xi$.
The scalar-one lifts $(x,z)\mapsto(A_ix,z)$ preserve it and have
inverse $A_i^{-1}$. They fix the origin frame, so all marked
fixed-loop sweep values are zero. This constructs the integral
core class at every weight.

For the cusp write the real coordinates as $x=(a,\delta)U+
(b,\gamma)V$ and the complex coordinates as $Z=U+\Omega V$, with
\[
 K=\operatorname{diag}(1,-6d),\qquad
 \Omega=\frac{\log q_{\rm base}}{2\pi i}\operatorname{diag}(1,d)
                  +B(q_{\rm base}),\qquad K\Omega=(K\Omega)^t.
\]
The holomorphic units are included in $B$.
Multiply the line coordinate by
\[
 G(U,V)=
 \exp\bigl(-\pi i(U^tKV+V^tK\Omega V)+\pi iZ_1\bigr);
\]
its reciprocal is the inverse. Short factors become trivial, and
the long $b,\gamma$ factors are
\[
 -z_1^{-1},\qquad
 \exp\bigl(\pi i(6d\Omega_{22}+\Omega_{12})\bigr)z_2^{6d}.
\]
The second has base order $3d^2$ and a nonzero holomorphic unit.
The relation $\Omega_{12}=-6d\Omega_{21}$ verifies commutation.
Replacing $\Omega$ by $\Omega+\operatorname{diag}(1,d)$ and
$U$ by $U+\operatorname{diag}(1,d)V$ gives the same Gaussian
comparison, proving the actual base return and its inverse.

Use $\phi(r,s)=-r(r-1)/2+3s^2$. Its period differences are
$\phi(r+1,s)-\phi(r,s)=-r$ and
$\phi(r,s+d)-\phi(r,s)=6ds+3d^2$, exactly the two factor valuations.
Interpolate on the given unimodular triangles. The Cartier monomials
and their reciprocals give regular local frames and inverse maps;
the holomorphic period unit is kept in the long identification.
The equivalent support used below is
\[
 \psi(r,s)=-\frac{r(r-1)}2+3s(s-1)=\phi(r,s)-3s.
 \tag{D.WI17}\hypertarget{tag-027A}{}\label{maps:eq:D.WI17}
\]
The exact line map is $\zeta_\psi=z_2^{-3}\zeta_\phi$, with inverse
$\zeta_\phi=z_2^3\zeta_\psi$. If a period multiplies $z_2$ by
$q_{\rm base}^{\lambda_s}u_\lambda(q_{\rm base})$, the line factor
changes by $q_{\rm base}^{-3\lambda_s}u_\lambda^{-3}$.
For Cartier slopes $m_\psi=m_\phi-3e_2$, this map is the identity
between the regular frames $\chi^{-m_\phi}\zeta_\phi$ and
$\chi^{-m_\psi}\zeta_\psi$. It therefore extends through every chart
and collar, including every period unit.

The weight-$d$ core and cusp are the literal period cover
$\gamma_d=d\gamma_1$. Pullback preserves the first three core graph
generators and multiplies the two fixed long sweeps by $d$.
The weight-one core class has fibre value $\xi_1$ and zero on all
five graph generators, and its cusp boundary class is the line just
constructed: the two angular Wang sweeps bound in the cusp and
$H_1$ of that boundary is free. Pullback therefore identifies the
whole integral boundary line at weight $d$, including its torsion
cohomology class. This also identifies the direct weight-$d$ cocycle
construction above with that pullback. The cover is used on these
core and cusp pieces.
"""

cap = second[3]
cap = cap.replace(
    'Only the core and cusp were covered; neither finite fill was\nassumed to be a cover of a weight-one fill.',
    r"""For an exact global extension map, the two relative degree-two
columns into $H_1(W)$ are the Seifert matrix $R$ above, whose inverse
is integral. Hence $H_2(W)\to H_2(X)$ is onto and its kernel is the
complete normal Thom image. The functional given by the line modulo
$d$ annihilates it by \eqref{maps:eq:D.WI19}; it therefore descends
uniquely. The universal-coefficient isomorphism for $H_1(X)=0$
identifies this functional with the same glued class $u$.""")
component = second[4] + r"""
The six wall differences for $\phi$ are $(-6,1,0,-6,1,0)$.
In the $(H,E_A,E_B,E_C)$ marking they give degrees $(-5,1,-6,0)$,
so the displayed $\eta$ is exactly $-5H-E_A+6E_B$.
The inverse of the adjusted homology splitting reads the evaluations
of $x_0,\ldots,x_{d-2}$ and then $u$. Changing an integer representative
of a $u$-value changes the adjustment by $ds=0$, so both maps are
well defined and mutually inverse.
"""
mixed = second[5].replace(
    'reducing the ordinary square merely modulo $d$ would lose\nprecisely the extra order-two information.',
    'the target retains its order-two kernel under reduction modulo $d$.')

finite = r"""
\emph{The finite lift and the common fixed-point characters.}
For every $N\mid6d$ the magnetic translation by $\delta/N$ is
\[
 (x,z)\longmapsto
 (x+\delta/N,e^{\pi i\xi(\delta/N,x)}z).
\]
Its commutator with $J_\lambda$ is
$\exp(-2\pi i\,6d\lambda_\gamma/N)=1$, and its $N$th power is
$J_\delta$. It commutes with all return lifts, since they fix
$\delta$ and preserve $\xi$. In the $\phi$ Gaussian coordinate
it acts by $(z_1,z_2,\zeta)\mapsto(z_1,e^{2\pi i/N}z_2,\zeta)$.
In the $\psi$ coordinate the dense line character is $-3$.
Thus the global finite class is represented on each component by
\[
 j_i^*u=\rho_d(-5H+6E_1-E_3),\qquad
 \psi(r,s)=\phi(r,s)-3s.
 \tag{D.TP1}\hypertarget{tag-025R}{}\label{maps:eq:D.TP1}
\]
The degree on every vertical fixed curve is one.
The $\phi$ slope on the edge $(0,j)$ to $(0,j+1)$ is $6j+3$,
so the actual regular line character is $-6j-3$.
The period $j\mapsto j+d$ changes it by $-6d$, zero modulo $N$.
The reciprocal gauges give the inverse identifications.
This proves finite lifts for $N=d,2d,3d$ whenever those groups
are used.
"""
semifree = second[7].replace('The scalar circle action is semifree.',
                            'The scalar circle action is semifree.')
semifree += r"""
On the given cusp fan every nonvertical edge has determinant one
with $\delta$; the vertical edges give exactly the $d$ curves.
The adjacent charts have overlap $(x',y',w')=(wx,wy,w^{-1})$,
with inverse $(x,y,w)=(w'x',w'y',(w')^{-1})$.
It gives the two $\mathcal O(-1)$ normal transitions and weights
$1,-1$. Thus every nonidentity subgroup element has precisely
these fixed curves and a free complement.
At $d=1$, the groups $H_2,H_3$ and all coefficient coordinates
under consideration are zero directly. Subsequent finite
localization is used for nontrivial groups.
"""
characters = r"""
Since $H_1(X;\mathbb Z/d)=0$ and $H^3(BS^1;\mathbb Z/d)=0$,
the degree-two Serre sequence gives a full-circle Borel lift
$\widehat u$ of $u$. Its restriction is
\[
 \widehat u|_{C_j}=x+\lambda_j t,\qquad
 \lambda_j=h-6j-3\quad\text{in }\mathbb Z/d,
 \quad \langle x,[C_j]\rangle=1.
 \tag{D.TP2}\hypertarget{tag-025S}{}\label{maps:eq:D.TP2}
\]
Here the same $h$ occurs on every component. To prove this, restrict
to $C_N$, $d\mid N\mid6d$, and compare with the constructed finite
line. The fixed-point section and the scalar isotopy give
$\pi_1(W_{C_N})=\mathbb Z^2\times C_N$.
Every fixed-point section has zero map into $\mathbb Z^2$, since
multiplication by $N$ is injective there. The universal-cover
degree-two sequence places the difference of the two classes in
group cohomology. Restriction along these identical finite subgroups
therefore gives one common character. Each fixed curve has no
degree-one mixed term. The map
$H^2(BS^1;\mathbb Z/d)\to H^2(BC_N;\mathbb Z/d)$ sends the
character-one generator to that generator and is an isomorphism;
the inverse does the reverse assignment. This proves the full-circle
formula as well.

In the $\psi$ support convention,
\[
 \psi(0,j+1)-\psi(0,j)=6j.
 \tag{D.TP3}\hypertarget{tag-025T}{}\label{maps:eq:D.TP3}
\]
Its usual dense-character-zero linearization differs from the
transported one by the common character $3$.
Thus, on putting $\lambda_0=h-3$ and taking $\epsilon=-1$,
\[
 \lambda_j=\lambda_0+6\epsilon j\quad\text{in }\mathbb Z/d.
 \tag{D.TP4}\hypertarget{tag-025U}{}\label{maps:eq:D.TP4}
\]
Reversing the scalar generator reverses all weights and characters,
giving $\epsilon=1$. This is the precise comparison of the two
support conventions, and is compatible with $j\mapsto j+d$.
"""
thomas = second[9]
localization = second[10]
localization = localization.replace(
    'Apply equivariant localization with coefficients\n$\\mathbb Z/(3d)$ to $\\mathcal P_3(\\widehat u)$.\nNo field assumption is needed here: the complement\nis scalar-free, and each normal Euler class becomes\na unit after inverting $t$.',
    r"""Restrict to $C_N$ with $N=3d$ and apply equivariant localization
with coefficients $\mathbb Z/(3d)$ to $\mathcal P_3(\widehat u)$.
The finite line lift exists by $N\mid6d$. The complement is free
and has finite-dimensional quotient, so its cohomology is killed
by a sufficiently high power of $t$. The inverse of restriction
after localization is $\sum_j i_{j*}(z/e_j)$, by the Thom
self-intersection formula on each fixed curve.""")
localization = localization.replace(
    'The base cohomology polynomial ring injects\ninto its localization at $t$, so the degree-zero\nidentity is an identity in the original coefficient\nring, not just a localized statement.',
    r"""Since $N=3d$, multiplication by $t$ sends
$H^0(BC_N;\mathbb Z/(3d))$ isomorphically to $H^2$, and the
positive even powers have the same coefficient group. Thus
localization preserves the constant coefficient in this formula.""")
sum_formula = second[11]
sum_formula = sum_formula.replace(
    'For $3\\nmid d$ the same\nlocalization calculation with the ordinary cube gives\nzero modulo $d$.',
    r"""For $3\nmid d$ take $N=d$ and use the ordinary cube to obtain
zero modulo $d$. At $d=1$ this value lies in the zero coefficient group.""")
sum_formula = sum_formula.replace(
    'Mixed coordinates are separate from\nthis calculation; in particular it does not discard\nthe order-$2d$ mixed Pontryagin-square terms when $d$\nis even.',
    'The mixed coordinates retain the full modulus $D_2$ proved above.')

detectors = r"""
\emph{The complete integral target and inverse detectors.}
Put $B_d=K(\mathbb Z/d,2)$. Its marked low-degree homology is
\[
 H_2(B_d;\mathbb Z)=\mathbb Z/d,\quad
 H_4(B_d;\mathbb Z)=\mathbb Z/D_2,\quad
 H_6(B_d;\mathbb Z)=\mathbb Z/D_3 .
 \tag{D.WI22}\hypertarget{tag-027G}{}\label{maps:eq:D.WI22}
\]
Here the positive reductions of $\mathbb{CP}^j$ give the generators
$\gamma_j(g)$, with $g$ the Hurewicz image of $1\bmod d$.
In Cartan's integral model for $d=p^f$ the basic pair is
$\Gamma(x_2)\otimes\Lambda(y_3)$ with $dy=p^fx$.
The differential on $y\gamma_{j-1}(x)$ is
$jp^f\gamma_j(x)$. Its $p$-primary homology in degree $2j$ has
order $p^{f+v_p(j)}$. The first further pair has degrees
$2p+1,2p+2$ and differential $dt=pz$.
For $p=2$ it contributes $\mathbb Z/2$ in degree five and
zero in degree six; for $p\ge3$ it starts above degree six.
Its products and torsion products with the basic positive classes
start in higher degrees. These are the complete low-degree groups
of the integral model
\cite[Expos\'e 11, Theorems 1 and 4, pp.11-09--11-13; Appendix 1, pp.11-22--11-23]{manCartan1955EML}.
Distinct prime components have relatively prime positive homology
orders, so their tensor and torsion products vanish. The Chinese
remainder isomorphism gives \eqref{maps:eq:D.WI22} for all $d$.

The quadratic generator has relations $d^2q(1)=2dq(1)=0$.
Conversely $q(j)=j^2\bmod D_2$ is well defined and quadratic,
giving the inverse detector and proving these are its complete
relations. For the degree-six generator $z$, the maps with
integral classes $dh$ on $\mathbb{CP}^3$ and $dx+y$ on
$\mathbb{CP}^1\times\mathbb{CP}^2$ push forward to $d^3z$ and
$3dz$. Their reductions factor through a point or
$\mathbb{CP}^2$, respectively, so both images vanish.
Thus its order divides $\gcd(d^3,3d)=D_3$.
The ordinary cube or Thomas operation evaluates to one on the
positive reduced hyperplane class, giving the opposite bound
\cite[equations (2.8), (3.4), pp.267--268]{ffThomas56}.
Divided-power functoriality identifies
$\gamma_j(g)$ with the positive $\mathbb{CP}^j$ pushforward:
addition on $\mathbb{CP}^\infty$ gives
$[\mathbb{CP}^i]*[\mathbb{CP}^j]=\binom{i+j}{i}[\mathbb{CP}^{i+j}]$,
and its free homology permits cancellation of $j!$ before applying
integer reduction. The detector and inverse are therefore
$n\gamma_j(g)\mapsto n$ and $n\mapsto n\gamma_j(g)$.

The free factor in
$K(\mathbb Z^{d-1}\oplus\mathbb Z/d,2)
=(\mathbb{CP}^\infty)^{d-1}\times B_d$
has free even homology and no odd homology. K\"unneth gives
\eqref{maps:eq:D.WI14}, with inverse coordinate map
\[
 (C_\alpha,J_\beta,K_i,L)\longmapsto
 \sum C_\alpha\gamma_\alpha(e)+
 \sum J_\beta\gamma_\beta(e)g+
 \sum K_i e_i\gamma_2(g)+L\gamma_3(g).
\]
The forward evaluations are respectively the free cubic monomials,
$x^\beta u$, $x_i\mathcal Q_2(u)$ and $\mathcal Q_3(u)$.
They pair to one with their own displayed generator and to zero
with the others. The possible degree-six cohomology
$\operatorname{Ext}$ ambiguity from $H_5(B_d)$ pairs to zero
with integral six-cycles. Consequently \eqref{maps:eq:D.WI15}
is the full fundamental-class invariant, with its precise
two- and three-primary coordinates.
"""

# The remaining original finite-cap auxiliaries and the independent
# characteristic bordism are appended below before the final recognition.
finite_detector = first[6]
finite_detector = finite_detector.replace(
    'A primitive generator has the root-loop exponent inverse to\n$n_1$ modulo $m_1$, hence odd modulo four.',
    r"""Choose $A,K$ with $Am_1+Kn_1=1$ and put $t=Aq+Kh$.
Then $q=m_1t$, $h=n_1t$, so the inverse base coordinates are
$\eta=B\beta+m_1t$, $g=C\beta+n_1t$.
The root-loop exponent is $K=n_1^{-1}\bmod m_1$, odd modulo four.""")
finite_detector = finite_detector.replace(
    'Its Wang sequence gives',
    r"""An affine translation in this return is conjugated away by
translation through $(I-A)^{-1}$ of that vector, with the opposite
translation as inverse. For $A=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$,
the matrices
$U=\left(\begin{smallmatrix}-1&0\\1&-1\end{smallmatrix}\right)$,
$V=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$ satisfy
$U(A-I)V=\operatorname{diag}(1,2)$.
For $A^{-1}$ use
$U=\left(\begin{smallmatrix}-1&0\\-1&-1\end{smallmatrix}\right)$ and
$V=\left(\begin{smallmatrix}1&-1\\0&1\end{smallmatrix}\right)$.
Every determinant is one and each adjugate is its integer inverse.
The Wang sequence therefore gives""")
finite_detector += r"""
The inverse of projection along $\delta$ adds the unique $\delta$
multiple making a vector have zero character value.
The resulting ambient change is a triangular shear, homotopic
through invertible shears to the identity; it identifies the
reference stable framing with this actual tangent parallelization.
"""
parity = r"""
\emph{The actual tangent-parallelization parity.}
Let a closed oriented three-manifold $N$ have a tangent
parallelization. Kaplan's prescribed almost-framing construction
gives a framed four-manifold with one zero-handle and $h$
two-handles, preserving its spin structure
\cite[Definition 1.7, Remark 1.8, Theorem 3.1, pp.239--240,243--246]{mapsKaplan79}.
The difference between its tangent framing and
$(\text{outward normal},TN)$ lifts to
$\operatorname{Spin}(4)=SU(2)_L\times SU(2)_R$.
The two factors are two-connected; on $N$ their homotopy classes
have integer degrees $A,B$, with inverse representatives supported
in a positive three-ball. The quaternion action
$(q_L,q_R)v=q_Lvq_R^{-1}$ sends its first column to
$q_Lq_R^{-1}$, of degree $A-B=\chi(W)$ by the relative Euler
obstruction. Stabilization sends $(A,B)$ to $A+B$ up to a common
generator sign: its two half-spin summands have equal stable
Pontryagin magnitude and opposite Euler contributions.
The quaternionic generator has stable framed coefficient one.
Thus the induced framed coefficient modulo two is
$A+B\equiv\chi(W)=1+h$.
The spin intersection matrix is even and becomes alternating
modulo two. Splitting nonzero pairings into hyperbolic blocks
proves its rank is even. Its handle sequence gives
$\dim H_1(N;\mathbb F_2)=h-\operatorname{rank}(Q\bmod2)$.
Hence every such actual parallelization has parity
$1+\dim H_1(N;\mathbb F_2)$, for its specified spin structure.
For \eqref{maps:eq:D.WI9} that dimension is two, so
\[
 \epsilon=[N]_\rho=1\pmod2.
 \tag{D.WI10}\hypertarget{tag-0273}{}\label{maps:eq:D.WI10}
\]
"""
link = first[8].replace(
    'Retain the actual Thom chains, not only their matrix classes.',
    'The following normal columns are realized by their actual Thom chains.')
transgression = r"""
\emph{The admissible sphere and relative transgression.}
An odd multiple of $N$ kills its odd-primary homology component;
join parallel copies by tubes in $X\setminus C$.
Its induced stable parity and critical-link parity stay odd.
Use Kaplan's filling for its prescribed almost framing, delete
the zero-handle, and reverse the resulting two-handle cobordism.
Deleting the real-codimension-four critical cycle preserves simple
connectivity. Each attaching circle therefore bounds an embedded
disc in $X\setminus C$. General position makes these discs mutually
disjoint and disjoint from the current three-manifold in their
interiors, since $2+2<6$ and $2+3<6$.
The first normal gives the boundary collar. The four remaining
directions extend over each disc precisely when their
$\pi_1SO(4)=\mathbb Z/2$ spin obstruction vanishes; it does by
the prescribed handle spin structure. Thickening gives actual
ambient surgeries to an embedded torsion $S^3$, preserving its
integral class and induced framing parity.

For $q=a+xi+yj+zk$ and $t_1=qi,t_2=qj,t_3=qk$, the frame
\[
 (-a e_3-x t_1-y t_2-z t_3,e_1,e_2)
\]
is the nontrivial class relative to the tangent sphere frame,
and extends over the four-handle. Its coefficient map has degree
one on $S^3$ and maps onto $\pi_3V_{6,3}=\mathbb Z/2$.
This fixes the convention in Zhubr's proved three-frame criterion
\cite[Theorem 1 and Section 5, pp.6,8--9]{ffZhubr13}.
The adjoint $SU(2)$ bundle has $p_1=-4c_2$, whereas its real
quaternion bundle has $p_1=-2c_2$. Hence
$\pi_3\operatorname{Spin}(3)\to\pi_3\operatorname{Spin}(6)$
is multiplication by two. The tangent quaternion sphere frame
is odd, while the extending admissible class has even induced
stable coefficient.

Choose the admissible three-frame of that theorem; its spin
rank-three complement has obstruction $\operatorname{PD}P_{\rm ref}$.
Trivialize the complement on the detector. Its choices change
the stable degree by even integers, and extension over the
reversed two-handle trace preserves that parity.
The resulting full frame $\sigma$ has even detector parity.
Thus $\sigma/\rho$ has an integral $\operatorname{Spin}(6)$
degree $q_0\equiv\epsilon\bmod2$.
If $B_4$ bounds $\operatorname{ord}(N)$ copies of $N$, the relative
four-cell obstruction and the index-two inclusion just computed give
\[
 -B_4\cdot C=2q+\operatorname{ord}(N)q_0.
\]
Here $q$ is the complementary obstruction cochain evaluated with
its $\sigma$ boundary trivialization. Division by
$2\operatorname{ord}(N)$ yields the exact formula
\[
 \operatorname{lk}(N,\operatorname{PD}P_{\rm ref})
 =-\frac{\ell(N,C)}2-\frac{\epsilon}2\quad\text{in }\mathbb Q/\mathbb Z.
 \tag{D.WI13}\hypertarget{tag-0276}{}\label{maps:eq:D.WI13}
\]
Changing $q_0$ by an even integer changes the right side by an
integer. Multiplication by the chosen odd number is invertible
on the order-two values, so the formula also holds for the
initial detector. The free part vanishes from
$2P_{\rm ref}=\operatorname{PD}\lambda=0$.
Equations \eqref{maps:eq:D.WI10} and \eqref{maps:eq:D.WI12}
make the two odd halves cancel. The linking is primitive on the
two-primary summand, and multiplication by two is invertible on
the odd summand. This proves $P_{\rm ref}=0$ with this marked detector.
"""

circle = r"""
\emph{The characteristic circle bordism.}
The full coefficient calculation also determines the refined class
by a compact characteristic bordism. For each $c=2^v\mid d$ let
$u_c$ be the reduction of $u$. Its Borel lift $U_c$ restricts on
the fixed curves to $x_j+r_jT$, where $r_j=h-6j-3$.
The equivariant first Chern class of $TX$ is zero: its ordinary
class is zero, and its only possible remaining character is zero
at a fixed point whose tangent weights are $0,1,-1$.

Give $X\times D^2$ the diagonal action $g(x,z)=(gx,gz)$.
Remove disjoint invariant tubes of its fixed sets $C_j\times0$.
On their normal bundle $N_{j,+}\oplus N_{j,-}\oplus\mathbb C_1$
the weights are $1,-1,1$, so the sphere action is free.
The remaining action is free everywhere. Its quotient is a
compact smooth seven-manifold $Q$; invariant tubular exponential
coordinates and their inverses give smooth collars.
The outer boundary map and inverse are
$[x,z]\mapsto z^{-1}x$ and $x\mapsto[x,1]$.
On an inner sphere conjugate the negative normal line. The orbit
of a unit vector maps to its complex line, with inverse any unit
representative modulo the scalar action. This gives
\[
 Y_j=\mathbb P(\mathcal O\oplus\mathcal O(-1)\oplus\mathcal O(1))
                     \longrightarrow C_j.
\]
For a Hermitian metric linear in its first variable the map
$\overline v\mapsto(w\mapsto h(w,v))$ identifies the conjugate
negative line with its dual; its inverse is the Riesz map.
It commutes with every normal transition and its unit.

Orient $Q$ by putting its horizontal frame before the positive
orbit vector in the complex orientation of $X\times D^2$.
On the outer collar this gives the orientation of $X$.
Conjugation of the one negative complex line reverses real
orientation; on an inner tube the quotient orientation is
$-(\operatorname{or}C_j,dr,\operatorname{or}\mathbb{CP}^2)$.
The complement has outward normal $-dr$, so every inner boundary
has its positive complex orientation. Thus
$\partial Q=X\amalg\bigsqcup_jY_j$.

The free Borel quotient is a homotopy equivalence with inverse
on cohomology. Let $U_Q$ be the descended restriction of $U_c$
and $T_Q$ the descended character-one integral line class.
Horizontal lift and the quotient differential give inverse bundle
maps in
$TQ\oplus\mathbb R=(TX\oplus\mathbb C_1)|/S^1$.
Consequently $w_2(Q)=\rho_2T_Q$ and
$\omega_Q=\rho_{2c}T_Q+i_2U_Q$ is characteristic, where
$i_2(j)=2j$ and its inverse on even residues is $2j\mapsto j$.
On the outer boundary the character line trivializes by
$[x,z,w]\mapsto(z^{-1}x,z^{-1}w)$, with inverse
$(x,a)\mapsto[x,1,a]$; hence $\omega_Q=i_2u_c$ there.
On $Y_j$, write $t_j=c_1(\ell_j^*)$. The character-one associated
line is $\ell_j^*$ by the map sending $[v,z]$ to the functional
taking $v$ to $z$; evaluation is its inverse. Thus
\[
 \omega_Q|_{Y_j}=(2r_j+1)t_j+2x_j
\]
has the displayed integral characteristic lift.

The projective-bundle sequence gives
$H^*(Y_j;\mathbb Z)=\mathbb Z[x_j,t_j]/(x_j^2,t_j^3)$ and
$\langle x_jt_j^2,[Y_j]\rangle=1$; base and fibre evaluations are
the inverse Leray--Hirsch coordinates. The tangent Euler sequence
$0\to\mathbb C\to\ell_j^*\otimes\pi^*E_j\to T_{\rm vert}Y_j\to0$
has quotient $\operatorname{Hom}(\ell_j,E_j/\ell_j)$, so
$p_1(Y_j)=3t_j^2$. It follows integrally that
\[
 \frac{\langle p_1(Y_j)((2r_j+1)t_j+2x_j)
                 -((2r_j+1)t_j+2x_j)^3,[Y_j]\rangle}{8}
             =-3r_j(r_j+1).
\]
Every endpoint is simply connected. Joining the inner components
by boundary one-handles gives their connected sum; the
characteristic classes extend over the attaching balls and their
degree-six numbers add. Zhubr's characteristic-bordism axiom
and integral normalization therefore give
\[
 \Gamma_c(X,i_2u_c)=3\sum_{j=0}^{d-1}r_j(r_j+1)=0\pmod c.
\]
Indeed with $A=h-3$ the complete sum is
$d[A(A+1)-3(2A+1)(d-1)+6(d-1)(2d-1)]$, divisible by $c$.
Changing any integer lift of a character changes its endpoint
value by a multiple of $c$.

The exact coefficient morphism is
$\Gamma_c(X,i_2u_c)=\langle u_c,P_{\rm ref}\rangle-
\langle u_c^3,[X]\rangle$.
To see its normalization, lift the marked cyclic spin-bordism class
through the free-coefficient surjection to an integral class $v$,
and kill its fundamental group by spin circle surgeries extending
the classifying map. The integral formula is
\[
 \frac{\langle p_1(2v)-(2v)^3,[Z]\rangle}{8}
   =\frac{\langle p_1v,[Z]\rangle}{4}-\langle v^3,[Z]\rangle .
\]
Coefficient naturality sends its first term to $u_c(P_{\rm ref})$
and its second to the specified cube; the inverse coordinate map
adds the cube. This uses the published characteristic-bordism axiom
with simply connected endpoints, at its inherited bordism scope
\cite[Theorem 5]{manZhubr75}\cite[pp.471--472,479]{manZhubr2010Gamma}.
The cube was proved zero, so all two-primary coordinates vanish.
The free and odd coordinates vanish from $4P_{\rm ref}=\operatorname{PD}p_1=0$;
their inverses are ordinary division on the free group and the
Bézout inverse of four on each odd cyclic factor. Chinese remainder
with its integral idempotents then gives $P_{\rm ref}=0$.
"""

recognition = r"""
\emph{Complete marked oriented recognition.}
Let $A_d=\mathbb Z^{d-1}\oplus\mathbb Z/d$ with its displayed basis.
The isomorphism $\psi_X:A_d\to H_2(X)$ sends the free basis to the
lifts adjusted by their $u$ values and the cyclic generator to $s$.
Its inverse evaluates $x_0,\ldots,x_{d-2}$ and then $u$.
The universal-coefficient isomorphism
$H^2(X;A_d)=\operatorname{Hom}(H_2(X),A_d)$ represents this inverse
by a classifying map $f_X:X\to K(A_d,2)$.
The full marked pair is
\[
 P(f_X)=0,\qquad
 \mu_d=\sum_{0\le i\le j\le d-2}C_{ij}\gamma_{ij}(e)g
                  -12\sum_{i=0}^{d-2}e_i\gamma_2(g),
\]
where $C_{ij}$ is the incidence coefficient of
\eqref{maps:eq:D.WI3}. All free cubic and pure cyclic coordinates
are zero. The inverse detectors above fix every coefficient,
so this pair depends on $d$ alone for all allowed data.

Zhubr's Theorem 5 is injective on the marked spin-bordism group
for the finitely generated group $A_d$. The marked recognition
of Theorem 3, with its Section 4.1 construction and uniqueness
at zero free $H_3$, applies here
\cite[Theorems 3,5 and Section 4.1, pp.795--796,809--810]{manZhubr75}.
For any two members it gives an oriented diffeomorphism $F$ with
$F_*=\psi_{X'}\psi_X^{-1}$ and inverse
$(F^{-1})_*=\psi_X\psi_{X'}^{-1}$.
Thus every adjusted free generator and the positive cyclic generator
have the stipulated images in both directions.

Existence at every $d$ follows from $k=\ell=1$, $m_0=3,m_1=4$,
$n_0=1,n_1=-1,r_0=r_1=0$, whose determinant is $1$.
The coprimalities give the actual finite-cap freeness conditions
of \ref{maps:src:D.2.34}. Define $M_d$ by this member.
For $d=1$ all its positive homology below degree six is zero.
The sphere's stable tangent map
$(x;v,a)\mapsto(x;v+ax)$ has inverse
$(x;y)\mapsto(x;y-\langle y,x\rangle x,\langle y,x\rangle)$.
It gives the same zero spin-bordism data; marked recognition gives
the orientation-preserving identification $M_1=S^6$.
When $d$ is prime to six, $D_2=D_3=d$ and the marked invariants
coincide with \ref{maps:src:D.1.11}, under the same basis map and
its inverse. Finally $\chi(X)=2+2(d-1)=2d$; diffeomorphism-induced
inverse homology maps preserve this alternating sum, so distinct
positive weights have distinct types.
"""

sections = [marking, ruling, chern, kernel, critical, line, cap, component,
            mixed, finite, semifree, characters, thomas, localization,
            sum_formula, detectors, finite_detector, parity, link,
            transgression, circle, recognition]
body = '\n\n'.join(r'\item ' + s.strip() for s in sections)
new = statement + '\n\n' + r'\begin{proof}' + '\n'
new += r'\begin{enumerate}[leftmargin=*]' + '\n' + body + '\n'
new += r'\end{enumerate}' + '\n' + r'\end{proof}' + '\n'
old = statement + '\n' + original
for command in ['label', 'hypertarget', 'tag']:
    pat = r'\\' + command + r'\{([^}]+)\}'
    a, b = re.findall(pat, old), re.findall(pat, new)
    assert sorted(a) == sorted(b), (command, set(a) - set(b), set(b) - set(a))
    assert len(b) == len(set(b)), (command, 'duplicate')
    print('IDENTITIES', command, len(b), 'preserved')
triples = r'\\tag\{([^}]+)\}\s*\\hypertarget\{([^}]+)\}\{\}\s*\\label\{([^}]+)\}'
assert sorted(re.findall(triples, old)) == sorted(re.findall(triples, new))
stack = []
for kind, name in re.findall(r'\\(begin|end)\{([^}]+)\}', new):
    if kind == 'begin':
        stack.append(name)
    else:
        assert stack and stack.pop() == name, (kind, name, stack)
assert not stack
for bad in [r'\StatementRecord', r'\path{', r'\subsubsection*', 'code/', 'records/',
            'conjectural', 'proof was given', 'actual marked caps, not']:
    assert bad not in new, bad
assert new.count(r'\begin{proof}') == new.count(r'\end{proof}') == 1
assert new.count(r'\begin{theorem}') == new.count(r'\end{theorem}') == 1
path = STAGE / f'{P}_receiving.tex'
path.write_text(new, encoding='utf8', newline='\n')
print('RECEIVER', path.relative_to(ROOT), len(new.splitlines()), len(new.encode()), sha(new))
print('SCOPE one staged theorem and one proof; no frozen/canonical edit; no TeX build')
