from pathlib import Path
import json
BASE=Path(__file__).resolve().parent
src=BASE.parents[2]/'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15/S6_10_PAPERS_V.tex'
s=src.read_text();label=s.index(r'\label{night:P1.18}');start=s.index(r'\begin{proof}',label);end=s.index(r'\end{proof}',start)+len(r'\end{proof}')
old=s[start:end];p=old

def replace_once(a,b):
 global p
 assert p.count(a)==1,(a[:100],p.count(a));p=p.replace(a,b)
def section(a,b,new):
 global p
 i=p.index(a);j=p.index(b,i);p=p[:i]+new+'\n\n'+p[j:]

insert=r'''\paragraph{Fresh normalization from the two finite roots.}
The executable certificate uses the rational matrix $\Gamma_6$ of
\cref{night:P1.16}, the integral matrices $A,B$ of
\cref{night:P1.15}, and the normalization $H(1)=I$, $Xe_0=e_0$.
It derives the two gauged connections by exact rational substitution:
\[
 \lambda=u^4,\quad D_0=\operatorname{diag}(1,u^6,u^3,1,u^{-3},u^{-6}),
 \qquad
 \lambda=u^{-5},\quad D_\infty=
 \operatorname{diag}(1,u^{-8},u^{-4},1,u^4,u^8).
\]
Write $U_0(0)=U_\infty(0)=I$ for their regular fundamental
solutions.  For a positive local root rotation $\zeta$ with gauge
exponents $d_i$, the character is $T=\operatorname{diag}(\zeta^{d_i})$.
Uniqueness of the regular right ODE gives
$U(\zeta u)=T^{-1}U(u)T$ and
$(UD^{-1})(\zeta u)=T^{-1}(UD^{-1})(u)$.
Since $D(1)=I$, the two based matrices are exactly
\[
 H_0=U_0(1)^{-1}T_0^{-1}U_0(1),\qquad
 H_\infty^{\rm mon}=U_\infty(1)^{-1}T_\infty^{-1}U_\infty(1).
\]
The equations solved are $XH_0=BX$, $XH_\infty^{\rm mon}=AX$,
$Xe_0=e_0$.  The exact geometric existence and normalized uniqueness
are supplied by \cref{night:P1.15}; a certified invertible square
subsystem encloses that exact solution.  Every omitted equation is
also checked against its enclosure.  Residual containment is used
as a consistency check; existence is the cited geometric input.
The limiting frames are
$F_0=XU_0(1)^{-1}$ and $F_\infty=XU_\infty(1)^{-1}$.

The zero-root transport starts at $u=1/4$, with a series radius
$2/5$, and then uses the exact positive real steps
$\delta=\min(u/32,1-u)$, of radius $u/8$, until $u=1$.
The infinity root is evaluated directly at $u=1$ with radius $5/4$.
For any shifted rational connection $P(t)/Q(t)$, the actual
certificate first verifies
\[
 d=|Q_0|-\sum_{j\ge1}|Q_j|R^j>0,\qquad
 M=\frac{\sum_j\|P_j\|_wR^j}{d}.
\]
The degree-$N$ transition error is then bounded by
$e^{MR}(r/R)^{N+1}/(1-r/R)$ for $r<R$, by the integral equation
and the coefficient integral below.  Each step records its
rational centre, radius, order, positive denominator bound and
full propagated ball error.  No saved historical coefficient
array or historical subdivision tree is an input.
'''
replace_once(r'\paragraph{The analytic enclosures and their actual matrix maps.}',insert+'\n'+r'\paragraph{The analytic enclosures and their actual matrix maps.}')
replace_once('The current root computations use $N=3000$, $R=0.999$ and each\nrectangle\'s actual maximum radius. Every coefficient and point\nrounding radius remains in the corresponding ball calculation.',r'''The fresh computation stores coefficients through $N=3000$ and
uses $R=999/1000$.  A shorter prefix may be evaluated at a centre;
its own degree and actual modulus are used in the same tail formula.
On the central squares the whole-square modulus is used.
Every coefficient and evaluation radius is retained. Polynomial
evaluation is grouped into blocks of32 coefficients; this is the
identity $p(z)=\sum_j z^{32j}p_j(z)$, with no change of polynomial
or of its error bound.''')
section(r'\paragraph{Collar continuation.}',r'\paragraph{The real implicit system and Hessian.}',r'''\paragraph{Fresh collar continuation.}
At a centre $z_c$ put $t=z-z_c$ and expand
\[
 1+(z_c+t)^5=\sum_{j=0}^5q_jt^j,\qquad
 \widetilde B_j=\sum_{k=j}^4\binom kjB_kz_c^{k-j}.
\]
The right transition $T(0)=I$ has the coefficients
\[
 T_{n+1}=\frac{\displaystyle
 \sum_{j=0}^{\min(4,n)}T_{n-j}\widetilde B_j
 -\sum_{j=1}^{\min(5,n)}q_j(n-j+1)T_{n-j+1}}
 {(n+1)q_0}.
\]
Starting with $R=1/8$, the program halves $R$ until
$d=|q_0|-\sum_{j=1}^5|q_j|R^j>0$.
It sets $M=\sum_j\|\widetilde B_j\|_wR^j/d$, takes a step
$|\delta|\le R/2$, and increases $N$ from32 in increments of16
until the certified error
\[
 e^{MR}\frac{(|\delta|/R)^{N+1}}{1-|\delta|/R}<10^{-45}.
\]
Every coefficient, centre and step is an enclosed complex number;
the strict denominator and tail tests are ball comparisons.
The map is exactly $Y(z_c+\delta)=Y(z_c)T_{z_c}(\delta)$.
At a collar centre of modulus at least $0.99$, continuation starts
at $(49/50)z_c/r_c$, where $r_c$ is the outward upper endpoint
of $|z_c|$. This point has modulus at most $49/50$, its value is
enclosed by the root series, and the continuation follows the
radial segment to the centre.  The resulting
whole-rectangle enclosure uses the matrix-exponential estimate above.
There are412 executed complex Taylor transitions in the completed
cover.  Their individual tails are propagated before every right
matrix multiplication.''')
replace_once('The certified determinant enclosure excludes\nzero on the entire central square and on its sixteen subsquares;\nthe matrix inverse is therefore the actual one there.', 'On each of the four closed central subsquares the certified\nmatrix inverse exists throughout the square, so it is the actual\ninverse there. Their union is the whole central square.')
section(r'\item \textbf{The infinity value and its strict local minimum.}',r'\item \textbf{The closed covers and their strict lower bounds.}',r'''\item \textbf{The infinity value and its strict local minimum.}
Set $a=256/3125$ and use the exact scaled root coordinates
\[
 w=a^{1/5}u,\quad\lambda=aw^{-5},\qquad
 v=a^{-1/4}u_0,\quad\lambda=av^4.
\]
The infinity regular frame is
$\widetilde Y(u)=XH(u^{-5})D_\infty(u)$.
Its third indexed column, the $w_0$ column, is unchanged by the
root gauge.  The real four-row system and its certified inverse
extend the uniquely normalized coefficient pair to zero; its
fifth reality equation extends there by continuity.
For $\zeta=e^{2\pi i/5}$ the exact deck formula is
\[
 \widetilde Y(\zeta u)=A\widetilde Y(u)T_\zeta,
 \qquad T_\zeta=\operatorname{diag}(1,\zeta^{-8},\zeta^{-4},1,
                                     \zeta^4,\zeta^8).
\]
At zero this changes the unique coefficient pair to
$(\zeta^8v_2,\zeta^4v_1)$ and preserves the $-i$ coefficient.
Thus both variables vanish and
\[
 h_b(\infty)=-c_0\operatorname{Re}(F_\infty)_{03}
 =-\frac{96}{625\pi}\operatorname{Re}(XH_\infty)_{03}.
\]
The same deck map gives $h_b(\zeta u)=h_b(u)$, so the real
gradient at zero vanishes.  The four closed quadrants of
$Q=[-1/10,1/10]^2$ are the central certificate.  On each, the
implicit derivative formulas give
\[
 \min(h_{xx},h_{yy})-|h_{xy}|>\frac14.
\]
Every real vector therefore satisfies
$t^tD^2h_b\,t\ge|t|^2/4$ throughout $Q$.  Integration along
the segment from zero, which remains in the convex square, gives
\[
 h_b(aw^{-5})-h_b(\infty)\ge\frac18|w|^2.
 \tag{1.18.5}
\]
The centre is the unique minimum on this square.

The fresh normalized root calculation gives the outward enclosure
\[
 h_b(\infty)=
 -1.094540250311402780116268263054945703725533269405330897770522063712646972012
 \quad(\text{radius}<4\cdot10^{-76}).
\]
In particular the following exact terminating-decimal bounds hold:
\[
 -1.094540250311402780116268263054945703726
 <h_b(\infty)
 <-1.094540250311402780116268263054945703725.
 \tag{1.18.4}
\]
The complete complex matrices, normalized equations and outward
balls are retained in
\path{code/paper_v/output/fresh_frobenius.json}.''')
section(r'\item \textbf{The closed covers and their strict lower bounds.}',r'\item \textbf{The actual cusp graph and the inner disc.}',r'''\item \textbf{The new closed covers and their strict lower bounds.}
Put $R=49/50$ and $S=103/100$.  The first-quadrant $w$ disc
$|w|\le R$ contains the sector $0\le\arg w\le2\pi/5$;
under $\lambda=aw^{-5}$ this covers $|\lambda|\ge aR^{-5}$.
Its intersection with $[0,1/10]^2$ is covered by the central
Hessian certificate.  The first-quadrant $v$ disc $|v|\le R$
maps by $\lambda=av^4$ onto $|\lambda|\le aR^4$.
The respective finite deck maps are the real integral matrices
$A,B$, which fix $e_0$ and preserve the height.

The collar uses $R\le|w|\le S$ in the first quadrant.
Its image contains every argument and every radius between
$aS^{-5}$ and $aR^{-5}$.  The exact rational inequality
$R^4\ge S^{-5}$ proves overlap with the zero-root disc.
The exact cusp coordinate is
$q=\lambda/\lambda_*-1=-w^{-5}-1$.
Boxes contained in $|q|\le1/4$ are covered by the cusp certificate.
For that disc the seed rectangle is
$[-1/4,1/4]\times[0,1/4]$ in the $q$ plane; the exact marked
conjugation map in item2 gives its lower-half counterpart.
The inner subdisc $|q|\le1/100$ is treated in item6.
All boundaries are retained.  These maps and the rational overlap
prove coverage of the full punctured base, including its two
finite-root points.

The three first-quadrant seed rectangles are $[0,R]^2$ for
each root and $[0,S]^2$ for the collar.  Each subdivision is into
four closed rational rectangles with disjoint interiors.
For each leaf the program either proves the strict inequality
on the whole rectangle or records a checked geometric reason:
outside the required radius, inside the central Hessian square,
inside the inner cusp disc, or inside the cusp disc already
covered in its own coordinate.  A new real preconditioner of
item1 may be applied at each centre.  Its exact formula fixes
$e_0$ and preserves the height; the whole-box ODE bound is then
applied to that same constant real change of coordinates.

All strict comparisons use the exact rational decimal
\[
 U=-1.0945402503114027801162682630549457037>h_b(\infty).
\]
The fresh complete partition has the following counts. The last
column is an exact terminating decimal strictly below every
accepted lower endpoint in that row, and strictly above $U$:
\[
\begin{array}{lrrrr}
 \text{region}&\text{strict}&\text{geometric}&\text{total}
     &\text{uniform lower bound}\\\hline
 \text{infinity root}&335&89&424&-1.094216\\
 \text{zero root}&200&77&277&-1.083056\\
 \text{cusp annulus}&113&8&121&-1.083777\\
 \text{collar}&440&338&778&-1.030556
\end{array}
\]
Thus there are1088 strict and512 geometric leaves,1600 in total,
in addition to the four central Hessian squares.
The root normalization uses120-decimal-digit Arb arithmetic;
the complete outer cover uses80 digits, with all input radii
retained.  The maximum subdivision depth is8.

Each output leaf records its full quadtree address, exact rational
rectangle, geometric reason or outward height endpoints, and
selected real minor.  A second program reconstructs every rectangle
from its address, checks prefix freeness and
$\sum4^{-\mathrm{depth}}=1$, and checks the exact areas
$2401/2500,2401/2500,1/8,10609/10000$ of the four seeds.
It separately rechecks all geometric exclusions and all serialized
strict endpoint comparisons.  These finite checks prove that no
required box or boundary is omitted.  They check the saved finite
certificate; the interval ODE program supplies its height bounds.''')
section(r'\item \textbf{The actual cusp graph and the inner disc.}',r'\item \textbf{The parameter domain and the full splitting translation.}',r'''\item \textbf{The actual cusp graph and the inner disc.}
The exact cusp substitution and gauge are
\[
 \lambda=\lambda_*(1+q),\qquad
 D_\lambda=\operatorname{diag}(1,\lambda^2,\lambda,1,
                                  \lambda^{-1},\lambda^{-2}),
 \qquad YD_\lambda=H_c(I+R_c\log q)P(q).
\]
The rational matrices $R_c,A_0$ are obtained by substituting in
$D_\lambda^{-1}\Gamma_6D_\lambda+D_\lambda^{-1}D_\lambda'$;
they are saved exactly in
\path{code/paper_v/output/fresh_local_domains.json}.
For the fresh anchor take
\[
 q_a=1/4,\quad\lambda_a=-\tfrac54a,\quad
 w_a=(4/5)^{1/5}e^{\pi i/5},\quad u_a=a^{-1/5}w_a.
\]
The actual right connection map is
\[
 H_c=Y_{\rm root,\infty}(w_a)
       D_\infty(u_a)^{-1}D_{\lambda_a}
       P(1/4)^{-1}(I-R_c\log(1/4)).
\]
It fixes the continuation branch and every gauge factor.
The resulting logarithmic monodromy and an explicit unimodular
marking are
\[
 N=\begin{pmatrix}
 0&1&1&-1&0&0\\0&0&0&0&-1&1\\0&0&1&0&-1&0\\
 0&0&1&0&-2&1\\0&0&1&0&-1&0\\0&0&1&0&-1&0
 \end{pmatrix},\qquad
 J=\begin{pmatrix}
 1&1&0&0&0&0\\0&0&-1&1&0&0\\0&1&-1&0&1&0\\
 0&1&-2&0&0&0\\0&1&-1&0&0&1\\0&1&-1&0&0&0
 \end{pmatrix}.
\]
The enclosure of $2\pi iH_cR_cH_c^{-1}$ contains this unique
integer matrix. Exact multiplication gives
\[
 N=B^{-1}A^{-1}-I,quad N^2=0,quad\det J=\pm1,quad
 J^{-1}NJ=\begin{pmatrix}0&I_3\\0&0\end{pmatrix},\quad
 e_J=J^{-1}e_0=(1,0,0,0,0,0)^t.
\]
This anchor's marking is related explicitly to the former cusp
marking $N_{\rm old}=A^{-1}B^{-1}-I$ by
$N=AN_{\rm old}A^{-1}$.
The actual left map is $z\mapsto Az$; its top coordinate changes
by $z_3-z_4+z_5$, which is real on the normalized intersection
vector.  It fixes $e_0$ and preserves $h_b$.
For the former marking
\[
 J_{\rm old}=\begin{pmatrix}
 -1&0&0&0&0&0\\0&0&0&0&1&0\\0&0&0&0&0&1\\
 0&1&0&1&0&0\\0&0&1&0&0&0\\0&-1&1&0&0&0
 \end{pmatrix},
\]
the exact matrix
\[
 J^{-1}AJ_{\rm old}=
 \begin{pmatrix}
 -1&0&1&2&0&-3\\0&0&-1&-1&0&3\\0&1&-1&0&-1&2\\
 0&0&0&-1&0&1\\0&0&0&0&0&-1\\0&0&0&0&1&-1
 \end{pmatrix}
\]
has block form $\left(\begin{smallmatrix}D&E\\0&D\end{smallmatrix}\right)$.
It changes a graph $Z$ to $DZD^{-1}+ED^{-1}$, so its imaginary
part changes by the real similarity $B\mapsto DBD^{-1}$.
This supplies the full graph-coordinate comparison.

Set $c_*=-h_b(\infty)$, $s=kc_*$ and $V=J^{-1}H_cP(q)$.
The actual shifted columns are $V_1,V_2,V_3-se_J$.
Their upper and lower blocks are $U_0,L$; the right scaling
from the algebraic columns is
$\operatorname{diag}(\lambda^2,\lambda,1)$, preserving their
span and the third-column shift.
The coefficient absolute sums through degree600 and the proved
cusp tail enclose $P(q)$ on the entire closed disc $|q|\le1/100$.
The certified inverse of $L$ exists throughout this disc.
Since $Ne_0=0$, the logarithmic factor gives exactly
\[
 Z(q)=\frac{\log q}{2\pi i}I_3+C(q),\qquad C=U_0L^{-1}.
\]
Put $B=\operatorname{Im}C$ and $y=-\log|q|/(2\pi)$. Then
\[
 \det\operatorname{Im}Z
 =y^3+\operatorname{tr}(B)y^2
  +\sum_{i<j}(B_{ii}B_{jj}-B_{ij}B_{ji})y+\det B.
 \tag{1.18.6}
\]
Set $y_0=\log100/(2\pi)$ and $t=y-y_0\ge0$.
The coefficients of
$\det(tI_3+y_0I_3+B(q))$, in increasing degree, have the
uniform certified lower bounds
\[
 \frac32,\qquad\frac92,\qquad\frac{15}4,\qquad1,
\]
with the last coefficient exactly one.
Indeed the stored lower endpoints are strictly greater than $1.7115,4.6510,3.8702$ in the first
three positions; the last is exactly one.
Thus the determinant is positive throughout the punctured disc.
A graph vector $(Zv,v)$ is real exactly when $v$ is real and
$(\operatorname{Im}Z)v=0$, proving transversality of the
$c_*$ plane. Item1 therefore gives
$h_b-h_b(\infty)\ne0$ there. The punctured disc is connected;
the anchor $q=1/100$ has
$h_b=-0.4504422009074128681790612984233345084\ldots>h_b(\infty)$.
Hence $h_b>h_b(\infty)$ on the whole punctured inner disc.

These maps also prove the cusp limit.  The lower block of $e_J$
is zero, so $L$ is independent of a real parameter $c$, and
$C_c$ is holomorphic at zero and affine in $c$.
For every fixed real $M$, it is uniformly bounded on a smaller
closed disc and the compact interval between $c_*$ and $-M$.
As $y\to\infty$, the Neumann inverse makes
$yI+\operatorname{Im}C_c$ invertible uniformly on that interval.
The real quantity $h_b+c$ cannot cross zero along it; its sign
at $c_*$ is positive, so $h_b-M>0$ at the other endpoint.
Thus $h_b\to+\infty$ at the cusp. The closed covers and the
central strict estimate prove the global minimum and uniqueness.''')
section(r'\item \textbf{The parameter domain and the full splitting translation.}',r'\end{enumerate}',r'''\item \textbf{The parameter domain and the full splitting translation.}
Item1 and \cref{night:P1.8} give
$c>-h_b(\infty)$ and $\operatorname{Im}\xi>-h_b(\infty)$
on the completed base. The enclosure gives
$-h_b(\infty)<1.095<10$.
For the upper-half-plane polygon specified in the statement,
$g=(96/(625\pi i))w_0$ has $\alpha(g)=1$, and
\[
 a_{\rm split}=\frac{96}{625\pi i}Y_{03}(\lambda_*/2).
\]
The fresh evaluation is at
$v=2^{-1/4}e^{\pi i/4}$ in the zero-root coordinate
$\lambda=av^4$.  Its continuation from the positive real axis
lies in the upper half-plane and is homotopic there, relative
endpoints, to the stated polygon. The root gauge has third
indexed diagonal entry one, so the displayed top coordinate is
unchanged. This proves the precise path and gauge comparison.
Both components of $a_{\rm split}$ have outward radius less than
$8\cdot10^{-76}$ in
\path{code/paper_v/output/fresh_local_domains.json}.

The defining equality
$\sigma_{\rm original}=\sigma_b-a_{\rm split}\alpha e$
gives the exact plane equality
\[
 (\sigma_{\rm original}+\xi_{\rm original}\alpha e)(P)
 =(\sigma_b+(\xi_{\rm original}-a_{\rm split})\alpha e)(P).
\]
Hence $\xi_b=\xi_{\rm original}-a_{\rm split}$ and
$h_{\rm original}=h_b-\operatorname{Im}a_{\rm split}$ pointwise.
The resulting minimum is
\[
 -0.181138544374987443901945340672108376803615204418668779889361825660830413266
 \quad(\text{radius}<8\cdot10^{-76}),
\]
attained at the same base point.
The original real line $\xi_{\rm original}=ic$ maps exactly to
$\xi_b=-\operatorname{Re}a_{\rm split}
       +i(c-\operatorname{Im}a_{\rm split})$;
its criterion is $c>-h_{{\rm original},\min}$.

The newly executed programs are
\path{code/paper_v/fresh_frobenius.py},
\path{fresh_local_domains.py},
\path{fresh_global_cover.py}, and
\path{verify_saved_certificate.py} in the same directory.
The exact rational connection data, complete new quadtree leaves,
local inverses, coefficient bounds, outward endpoints and independent
saved-certificate validation are retained under
\path{code/paper_v/output/}; the four leaf files are
\path{fresh_cover_infinity.jsonl},
\path{fresh_cover_zero.jsonl},
\path{fresh_cover_cusp.jsonl}, and
\path{fresh_cover_collar.jsonl}.
The dependency versions and commands are in
\path{code/paper_v/README.md}.
These are fresh computations after reading the printed proof.
The historical12911-leaf calculation remains a separate recorded
check; no absent historical program or leaf file is claimed to
have been executed by this certificate.''')
# Avoid an overlong display line: use a split decimal in the two enclosures.
p=p.replace('-1.094540250311402780116268263054945703725533269405330897770522063712646972012\n \\quad', '-1.0945402503114027801162682630549457037255332694053308977705\\ldots\n \\quad')
p=p.replace('-0.181138544374987443901945340672108376803615204418668779889361825660830413266\n \\quad','-0.1811385443749874439019453406721083768036152044186687798893\\ldots\n \\quad')
# The radius belongs to the full stored midpoint, not the truncated display.
p=p.replace('\\quad(\\text{radius}<4\\cdot10^{-76})','\\quad(\\text{stored midpoint radius}<4\\cdot10^{-76})')
p=p.replace('\\quad(\\text{radius}<8\\cdot10^{-76})','\\quad(\\text{stored midpoint radius}<8\\cdot10^{-76})')
(BASE/'P1_18_replacement_proof.tex').write_text(p+'\n')
oldstatement='A certified enclosure has radius $4.04\\cdot10^{-56}$ about the\n56-digit midpoint retained in\n\\path{code/part1/minimum_certificate_summary.json}.'
assert s.count(oldstatement)==1
newstatement='A fresh certified enclosure has radius less than $4\\cdot10^{-76}$\nabout the full stored midpoint in\n\\path{code/paper_v/output/fresh_frobenius.json}.'
patches=[{'id':'V-P118-fresh-enclosure','statement_id':'night:P1.18','operation':'replace_exact','old':oldstatement,'new':newstatement,'reason':'Replace an unavailable historical summary locator by the newly executed certificate and its actual outward radius.'},{'id':'V-P118-fresh-full-cover','statement_id':'night:P1.18','operation':'replace_exact','old':old,'new':p,'reason':'Install the complete newly executed 1600-leaf cover, four-square Hessian, explicit A-conjugate cusp marking, rigorous majorants, normalized finite-root transport and saved-certificate verification; preserve the exact geometric and parameter maps.'}]
(BASE/'patches_P1_18.json').write_text(json.dumps(patches,indent=2)+'\n')
print('replacement proof',len(p.split()),'words;',len(p),'bytes; patches',len(patches))
