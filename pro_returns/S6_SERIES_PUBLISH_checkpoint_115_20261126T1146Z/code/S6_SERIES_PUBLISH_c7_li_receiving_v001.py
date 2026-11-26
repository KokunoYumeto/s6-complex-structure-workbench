"""Prepare the complete LI receiver, preserving every permanent identity.

The original has been read after the frozen fresh derivation.  This writes
only the receiving lane; the canonical manuscript is read-only.
"""
from pathlib import Path
from hashlib import sha256
import csv
import io
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'agents/continuation7_iii_all_parity_receiving'
OUT.mkdir(exist_ok=True)
canonical = ROOT/'S6_SERIES_PUBLISH_III.tex'
raw = canonical.read_bytes()
assert sha256(raw).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
text = raw.decode()
start = text.index(r'\begin{theorem}[every positive weight by integral bar chains]')
end_statement = text.index(r'\end{theorem}',start)+len(r'\end{theorem}')
start_proof = text.index(r'\begin{proof}',end_statement)
end_proof = text.index(r'\end{proof}',start_proof)+len(r'\end{proof}')
end_auxiliary = text.index('homology.',end_proof)+len('homology.')
old_statement = text[start:end_statement]
old_proof = text[start_proof:end_proof]
old_with_auxiliary = text[start_proof:end_auxiliary]
assert sha256(old_proof.encode()).hexdigest() == 'cbd98b486a018aa7d461b3c941b2b40590b8730ecc9f15adfe24c9ef4cfc38b8'

statement = old_statement.replace('[every positive weight by integral bar chains]',
                                  '[Integral homology at every positive weight]',1)
statement = '\n'.join(line for line in statement.splitlines()
                      if not line.startswith(r'\StatementRecord'))
intro_start = statement.index('The restriction on')
intro_end = statement.index('Index the boundary',intro_start)
statement = statement[:intro_start]+r'''Let $d$ be any positive integer. Every iterate $Q\mapsto dQ$ of
the $172$ natural initial rows has the following integral homology
presentation, for every free finite-good affine logarithm, every finite
list of regular logarithms and every integer clutch. There are $495$
cap patterns when finite-good caps are allowed at $\mathrm{III}^*$ and
$\mathrm{IV}^*$, and $459$ in the subset with every star cap original.
The formula applies to both sets. Their inclusion $j$ and the map $\pi$
which replaces each finite-good $\mathrm{III}^*$ or $\mathrm{IV}^*$ cap
by its original cap satisfy $\pi j=1$; $j\pi$ performs exactly those
replacements. The Seifert group and free ranks are
\eqref{maps:eq:D.WP8}--\eqref{maps:eq:D.WP9}.

The full presentation \eqref{maps:eq:D.OW2}--\eqref{maps:eq:D.OW4}
has the following integral coordinates.
''' + statement[intro_end:]
statement = statement.replace('Replace the five\nfinite or regular logarithmic normal columns by',
                              'Use the five\nfinite or regular logarithmic normal columns')
statement = statement.replace('If $A_i$ has order $h\\mid m$, the sum in',
                              'For $A_i$ of order $h\\mid m$, the sum in')
statement = statement.replace('the actual weighted matrices','the weighted matrices')

proof = r'''\begin{proof}
\emph{The integral comparison.}
Use the bar chains of $\Lambda$ with trivial coefficients and with
degenerate simplices factored out. Their low-dimensional boundaries are
\[
 \partial[u]=0,\qquad
 \partial[u|v]=[v]-[u+v]+[u].
                                                        \tag{D.BC6}\hypertarget{tag-01Y2}{}\label{maps:eq:D.BC6}
\]
The standard resolution and its contracting homotopy give this
functorial model of $B\Lambda$; the contraction preserves the
degenerate subcomplex
\cite[Chapter I, Section 5, pp.~18--19]{manBrown82}.
Put
\[
             p_1([u])=u,\qquad p_2([u|v])=p(u,v).
                                                        \tag{D.BC7}\hypertarget{tag-01Y3}{}\label{maps:eq:D.BC7}
\]
The first map kills two-boundaries. Bilinearity of $p$ makes
$p_2\partial[u|v|w]=0$. The cycle $[u|v]-[v|u]$ maps to
$u\wedge v$. In particular the six cycles
$[e_\alpha|e_\beta]-[e_\beta|e_\alpha]$, $\alpha<\beta$,
are the coordinate two-tori, and give the inverse on
$H_2(T^4;\mathbb Z)=\Lambda^2\Lambda$.

Antisymmetrizing \eqref{maps:eq:D.BC1} gives zero, proving the
symmetry of $D_A$. The binomial identity, valid for every pair
of integers, gives
\[
 f_A(u)+f_A(v)-f_A(u+v)
             =p(Au,Av)-(\Lambda^2A)p(u,v).
                                                        \tag{D.BC8}\hypertarget{tag-01Y4}{}\label{maps:eq:D.BC8}
\]
Extend $f_A$ linearly on bar one-chains. Then
$f_A\partial=p_2A-(\Lambda^2A)p_2$ on two-chains.

The marked period maps identify the exterior with the torus bundle
over the based graph obtained by cutting along the chosen stems.
At weight $d$ their lattice map is
$S_d=\operatorname{diag}(1,1,1,d)$ and their monodromies are
$A_i(d)=S_d^{-1}A_i(1)S_d$. The period-subgroup cover sends
$[x]_{\psi^d}$ to $[x]_\psi$; on an open fundamental strip its
inverse sheets are $x,\psi x,\ldots,\psi^{d-1}x$.
The line map is the product of the original line maps on these
sheets, and its positive roof is the sum of their positive roofs.
Division by that roof and multiplication by it give the inverse
period parametrizations. Thus the graph and peripheral maps carry
the same line units and the origin sections.

With fibre-first orientation the integral mapping-cone complex is
\[
 {\cal C}_n=B_n(\Lambda)\oplus
                   \bigoplus_{i<r}B_{n-1}(\Lambda),
 \qquad
 \partial(c;g_i)=
 \left(\partial c+\sum_{i<r}(A_i-I)g_i;
                                     -\partial g_i\right).
                                                        \tag{D.BC9}\hypertarget{tag-01Y5}{}\label{maps:eq:D.BC9}
\]
For the convention $(x,1)\sim(A_i^{-1}x,0)$, a cylinder labelled
by its terminal chain $g$ starts at $A_i g$, giving the displayed
sign. The universal cover is real four-space over a tree and is
contractible. The graph of bar models has the same marked
$\Lambda\rtimes F_r$ group; the period maps induce the indicated
maps on each vertex and cylinder, hence on each peripheral torus.

On two-cycles define
\[
 P_2(c;g_i)=
 \left(p_2c+\sum_{i<r}f_{A_i}(g_i);
                                  (p_1g_i)_{i<r}\right).
                                                        \tag{D.BC10}\hypertarget{tag-01XS}{}\label{maps:eq:D.BC10}
\]
The target coordinates are
\[
 C\oplus K,\qquad
 C=\Lambda^2\Lambda/
          \sum_{i<r}(\Lambda^2A_i-I)\Lambda^2\Lambda,
 \quad
 K=\ker[A_0-I\ \cdots\ A_{r-1}-I].
                                                        \tag{D.BC11}\hypertarget{tag-01XT}{}\label{maps:eq:D.BC11}
\]
The entire relation lattice in $C$ is retained. On a three-boundary
the fibre coordinate of \eqref{maps:eq:D.BC10} is
\[
 \sum_{i<r}\bigl(p_2(A_i-I)h_i-f_{A_i}\partial h_i\bigr)
       =\sum_{i<r}(\Lambda^2A_i-I)p_2h_i .
                                                        \tag{D.BC12}\hypertarget{tag-01XU}{}\label{maps:eq:D.BC12}
\]
Here $p_2\partial c_3=0$. Its differential to degree one also
agrees, by \eqref{maps:eq:D.BC8}, so $P_2$ induces a homomorphism.

We specify its inverse. For $k=(u_0,\ldots,u_{r-1})\in K$,
list $v_1=A_0u_0,v_2=-u_0,\ldots,v_{2r}=-u_{r-1}$ and put
$s_j=\sum_{h\le j}v_h$, with $s_0=s_{2r}=0$. Set
\[
 T(k)=\sum_{j=1}^{2r}[s_{j-1}|v_j]
                           -\sum_{i<r}[u_i|-u_i],
 \qquad Z(k)=(-T(k);[u_i]_{i<r}).
\]
The boundary of $T(k)$ is $\sum_i([A_iu_i]-[u_i])$, so $Z(k)$
is a cycle of graph coordinate $k$. Its fibre coordinate is
\[
 z(k)=\sum_i f_{A_i}(u_i)-\sum_jp(s_{j-1},v_j)
                                      +\sum_i p(u_i,-u_i)\quad\text{in }C.
\]
Choose an integer basis $k_j$ of $K$, with its inverse coordinate
matrix. For a bivector $x=\sum x_{\alpha\beta}e_\alpha\wedge
e_\beta$ let
$F(x)=\sum x_{\alpha\beta}([e_\alpha|e_\beta]
-[e_\beta|e_\alpha])$ in the fibre. Define
$s(k_j)=[Z(k_j)]-[F(z(k_j))]$ and extend linearly.
Changing the representative of $z(k_j)$ changes $F$ by the
fibre relation bounding in the corresponding mapping cylinder.
Thus
\[
 (c,k)\longmapsto [F(c)]+s(k)
\]
is well-defined. Its composite with $P_2$ is the identity.
Conversely, subtract $s$ of the graph coordinate from a two-cycle.
The mapping-cone exact sequence puts the remainder in the fibre;
$p_2$ and $F$ are inverse there. This proves the other composite
and the integral isomorphism in \eqref{maps:eq:D.BC11}.

\emph{Peripheral and logarithmic tori.}
At an independent boundary a fixed vector $A_iv=v$ gives the
cycle with $g_i=[v]$ and every other component zero. Its coordinates
are $(f_{A_i}(v),J_iv)$. For $A_i^m\lambda=\lambda$, the torus
in the $m$-fold mapping-torus cover has edge chain
\[
                        \sum_{\nu=0}^{m-1}[A_i^\nu\lambda].
                                                        \tag{D.BC13}\hypertarget{tag-01XV}{}\label{maps:eq:D.BC13}
\]
Its endpoints telescope. The graph coordinate is $J_iN_m\lambda$
and its fibre coordinate is the sum in \eqref{maps:eq:D.BC4}.

The last loop is $t_r=t_{r-1}^{-1}\cdots t_0^{-1}$.
The inverse cylinders carry its local one-chain $[u]$ to
\[
         -[A_{j+1}\cdots A_{r-1}A_ru],
                            \qquad 0\le j<r .
                                                        \tag{D.BC14}\hypertarget{tag-01XW}{}\label{maps:eq:D.BC14}
\]
Applying $\sum(A_j-I)$ gives $[A_ru]-[u]$ by telescoping.
There is no residual fibre chain. For a fixed vector this is
$J_rv$; applying $P_2$ gives $c_r(v)$. Applying the same map to
each summand of \eqref{maps:eq:D.BC13} gives its full norm sum.
This proves both lines of \eqref{maps:eq:D.BC3} with their
ordered suffixes.

The positive normal meridian of a logarithmic cap is
$\mu=t_i^m v^{-1}$, where $A_i^m=I$ and $A_iv=v$.
The commuting fibre and normal loops give
\[
              [\lambda,\mu]=[\lambda,t_i^m]-[\lambda,v].
                                                        \tag{D.BC15}\hypertarget{tag-01XX}{}\label{maps:eq:D.BC15}
\]
The last term is the fibre bivector $\lambda\wedge v$.
The root pair gives $[t_i,\mu]=[v,t_i]$, and hence the fifth
column $(c_i(v),J_iv)$. These signs are fixed by the boundary map
\[
 (y,\tau)\longmapsto
       \bigl(y+(\tau/m)v,\exp(2\pi i\tau/m)\bigr).
\]
Its inverse chooses a root sheet and subtracts $(\tau/m)v$;
changing the sheet is the deck identification. The positive normal
circle is $(y-sv,\tau+ms)$.

The core group in degree one is generated by its four fibre loops
and its root, with relations $(A_i-I)\lambda$ and $m\,\mathrm{root}-v$.
The five displayed columns respect these relations: the cyclic
sum vanishes on $(A_i-I)\lambda$, the remaining wedge term is a
column of $(\Lambda^2A_i-I)$, and the root relation reads
$\sum_{\nu<m}c_i(A_i^\nu v)=mc_i(v)$.
The normal line pulls back to the trivial normal line on the
finite cover, so its Chern class is torsion. Its integer evaluation
on each integral two-cycle is zero. The Thom sequence therefore
identifies the full boundary kernel with this whole core $H_1$
image. This proves all five columns, including every torsion
relation in the normal-line case, as in
\ref{maps:src:D.2.29}--\ref{maps:src:D.2.30}.
Writing $\nu=qh+j$, $0\le j<h$, proves the stated period
compression of the sum and $N_m=(m/h)N_h$ over the integers.

The affine freeness criterion is \eqref{maps:eq:D.WP5} at the
weighted matrix. Let $F$ be a primitive
fixed basis and $H$ a basis of the image lattice of $F^{-1}N_h$.
Then $P\Lambda=F(H/h)\mathbb Z^2$, where $P=N_h/h$; an integer
right inverse of $H^{-1}F^{-1}N_h$ gives every lattice preimage.
Write $v=Fz$, $w=hH^{-1}z$ and $t=\gcd(m,w_1,w_2)$.
The fixed-plane condition for the $j$th power is $m/t\mid j$.
On a nonidentity moving plane, $(A_i^j-I)^{-1}$ gives the fixed
point once that condition holds. On an identity moving plane,
the condition is $jv/m\in\Lambda$. Consequently freeness is
exactly
\[
 \gcd(m,v_1,v_2,v_3,v_4)=1,\qquad h\mid m/t.
\]
The first failed condition gives the fixed power
$j=m/\gcd(m,v_1,v_2,v_3,v_4)$; the second gives $j=m/t$.
For an affine lift $Ax+\eta$ with $P\eta=v/m$, put
$y=(I-A_i)^{-1}(\eta-v/m)$ on the moving plane.
The coordinate change $x'=x-y$, with inverse $x=x'+y$,
carries it to $A_ix'+v/m$.
On the root family the same change is analytic: for its root
operator $R$ and norm-zero moving section $b_0$, use
$y_0=-m^{-1}\sum_{j=0}^{m-1}jR^jb_0$.
Telescoping gives $(I-R)y_0=b_0$; the inverse adds $y_0$.
The finite sum carries the original translation and line units.

The integral marking is also explicit under a change
$t_i'=(\lambda,t_i)$. On $\Lambda\times C$ use
\[
 (x,z)(y,w)=(x+y,z+w+p(x,y)),\qquad
 (x,z)^{-1}=(-x,-z+p(x,x)).
\]
The lift of $A_i$ is $(x,z)\mapsto(A_ix,z-c_i(x))$;
\eqref{maps:eq:D.BC8} proves multiplicativity in $C$.
Conjugation gives
$c_i'(u)=c_i(u)+(A_iu)\wedge\lambda$ and
$v'=v+N_m\lambda$. Commuting $t_i'$ with its $m$th power gives
\[
 \sum_{\nu<m}c_i(A_i^\nu\lambda)
       =c_i(N_m\lambda)+(N_m\lambda)\wedge\lambda.
\]
Substitution shows that the four norm columns are fixed and the
new root column is the old root plus the old $\lambda$ norm column.
The column change and its inverse are
$\left(\begin{smallmatrix}I_4&\lambda\\0&1\end{smallmatrix}\right)$
and the same matrix with $-\lambda$.
On core groups the map sends the new root to
$\mathrm{root}+\lambda$ and fixes the fibre, with inverse
subtraction. It respects the power relations because
\[
 mI-N_m=(I-A_i)\sum_{j=0}^{m-1}(m-1-j)A_i^j.
\]
In the central lift the inverse generator change retains
$(-\lambda,p(\lambda,\lambda))$. All these maps are integral
also on the even part of $C$.

At a regular site $A_i=I$ and $h=1$; the same five columns
apply. An added identity edge adds a direct $\Lambda$ block to
$K$, with inverse given by reading that block and projecting to
the others. The signed clutch $e$ is an order-one regular site
of power $-e\gamma$. Its coordinate shear and inverse are
$(y,\theta)\mapsto(y+\theta e\gamma,\theta)$ and subtraction.
Deleting its root $c_*=\gamma^{-e}$ gives the asserted product
relation. Replacing a chosen independent base loop by the inverse
of the ordered product gives the change to any last boundary;
the original product relation gives its inverse.

\emph{Unchanged caps.}
The local component, line and plumbing maps of
\ref{maps:src:D.2.40} identify the cap $H_2$ groups as free
abelian groups at every positive weight. These local maps retain
the $d$th component permutation and the full norm of the line
units. Their fibre-kernel transport can be proved integrally as
follows. Put $W_d=\Lambda^2S_d$ and let
$f_d:\Lambda^2\Lambda\to H_2(U_d)$ be the fibre map.
The cover and simplex transfer satisfy
\[
 p_*f_d=f_1W_d,\qquad
 \operatorname{tr}_U f_1=f_d\,dW_d^{-1}.
\]
The transfer matrix is integral: it multiplies nongamma wedges
by $d$ and gamma wedges by one. On the fibre image the composite
$\operatorname{tr}_Up_*$ is multiplication by $d$, since a deck
translation of a fibre is homotopic to the identity. Freeness of
$H_2(U_d)$ gives the two containments in
\[
 \ker f_d=(\Lambda^2\Lambda)\cap
          W_d^{-1}(\ker f_1\otimes\mathbb Q).
\]
Choose primitive quotient rows $Q_1$ and a section $\sigma_1$
for the weight-one fibre kernel. A unimodular Smith decomposition
of $Q_1W_d$ gives a kernel basis $K_d$, inverse kernel rows $L_d$,
quotient rows $Q_d$ and section $\sigma_d$, satisfying
\[
 Q_d\sigma_d=I,\quad L_dK_d=I,\quad
 K_dL_d+\sigma_dQ_d=I.
\]
The cover and transfer in these coordinates are
$Q_1W_d\sigma_d$ and $Q_d dW_d^{-1}\sigma_1$.
Both composites are multiplication by $d$. These identities
give every saturated kernel and its inverse coordinates in
\eqref{maps:eq:D.OW4}.

The boundary Wang sequence has fibre term
$\operatorname{coker}(\Lambda^2A_i-I)$ and graph term
$\operatorname{Fix}A_i$. The fixed normal tori constructed in the
local cap maps bound their node thimbles or original cap discs.
Subtracting those literal tori from a boundary class leaves a
fibre class. The latter bounds precisely on the kernel just
computed. Their images under $P_2$ are the full columns
\eqref{maps:eq:D.BC5}. The possible multiplicative rim term
$\delta\wedge u_2$ vanishes by the integral unit elliptic
preimages in \eqref{maps:eq:D.OW7}; those preimages are polynomial
in $d$. Hence every cap kernel, with its torsion, is represented
by the stated fibre and fixed-normal columns.
The narrow multiplicative original and Mumford patterns are
identified by those same marked local maps. The finite choices
at $\mathrm{III}^*$ and $\mathrm{IV}^*$ account for the extra
$36$ patterns. Sitewise inclusion and replacement give the
maps $j,\pi$ stated above and their two displayed composites.

\emph{The complete gluing and homology.}
Let $\mathcal B$ be the full relation matrix with target
$\Lambda^2\Lambda\oplus K$: include all fibre relations,
all primitive unchanged-cap fibre kernels and all the normal
columns just proved. Put $\mathcal C=\operatorname{coker}\mathcal B$.
In a Smith decomposition $U\mathcal B V=\Delta$, the quotient
generator for a diagonal entry $d_j$ is $U^{-1}e_j$, and its
bounding chain is $Ve_j$, since
$\mathcal B Ve_j=d_jU^{-1}e_j$. This supplies the cyclic
coordinates and their inverse representatives.

Fill the finite and regular logarithms first and leave the
selected cusp unfilled; call the result $E$. With
$g=\gcd(a,d)$, the exterior degree-one group is
\[
 \mathbb Z\gamma\oplus(\mathbb Z/g)\delta
                   \oplus\bigoplus_{i\ne *}\mathbb Z x_i.
\]
The logarithmic root discs have boundaries
$m_ix_i-v_{i,\gamma}\gamma-v_{i,\delta}\delta$.
Their distinct nonzero base coefficients prove injectivity
of the disc boundary map, with inverse obtained by reading
and dividing those coefficients by $m_i$.
Use a free lift of this group and let $P$ contain these columns
and $g\delta$. The same argument proves that $P$ is injective.

For each remaining component use its positive normal disc;
its boundary is $\mu_Cx_i+\rho_C\delta$, where $\mu_C$ is its
multiplicity and $\rho_C$ is the integer winding read from its
marked period and line transitions. Exponentiating the period
logarithm recovers the path. At the selected cusp the $d$
discs have boundaries $x_*+jC_{22}\delta$, $0\le j<d$,
in its actual short-period matrix. Let $M$ contain all these
boundaries. The kernel $\ker\Gamma$ of their map to $H_1(E)$
is computed by the integer equation $Mz=Pz'$.
Injectivity of $P$ makes $z'$ unique. A Hermite basis of the
projected $z$-lattice and its inverse coordinates give exactly
this kernel, including its index in the component-disc lattice.

The relative sequence \eqref{maps:eq:D.WP11} is therefore
\[
 0\longrightarrow\mathcal C\longrightarrow H_2(X)
        \longrightarrow\ker\Gamma\longrightarrow0.
\]
For a kernel basis vector take its component discs, subtract
the logarithmic power discs given by $z'$, and close the remaining
boundary by the exterior monodromy chains. The coefficient of
$g\delta$ is bounded by the B\'ezout combination of the
$a\delta$ and $d\delta$ monodromy chains. Reading the component
coordinates and subtracting these closed cycles is the inverse
splitting. Thus $H_2(X)=\mathcal C\oplus\ker\Gamma$,
and the free group $\ker\Gamma$ adds no torsion. Its actual
integral construction retains every common even factor in
$T=\operatorname{Tor}\mathcal C$.

The nongamma vanishing words are unchanged by $S_d$.
The determinant-one elliptic pairs kill both elliptic generators;
in the two $\mathrm{OS}46/\mathrm{II}$ cases the original
$I_3^*$ discs give $2e_1+\delta$ for $a=1$ and
$e_1+2\delta$ for $a=4$, together with $3e_1=-u-v$.
The selected cusp kills $\delta$. These relations kill the
elliptic lattice in those cases as well. Reading the remaining
period exponent and representing it by the return path are
inverse maps onto $\mathbb Z\gamma$.
The actual logarithmic root paths then give the Seifert presentation
in \eqref{maps:eq:D.WP8}: their powers are
$c_i^{m_i}=\gamma^{\mu_i}$ and their product is $\gamma^e$.
Conversely the return and root paths satisfy exactly these
vanishing, power and product relations; the maps fix every
generator on composition.

For free ranks, the rational inverse of $S_d$ carries the graph
and fixed-normal diagrams to weight one. Equivalently, let
$\rho=P_2$ on the fibre coordinate and let $\tau$ be evaluation
of the alternating cocycle $x\wedge A_wy$. On the fibre
$\tau=2\rho$, so $2\rho-\tau=h\circ\operatorname{graph}$.
On the basis above,
$h(k_j)=2z(k_j)+\sum_t s_{t-1}\wedge v_t$.
The maps $(c,k)\mapsto(c-h(k)/2,k)$ and addition of the same
term are inverse over $\mathbb Q$. They send fixed-normal
coordinates to zero and norm coordinates to
$-\lambda\wedge v$, giving the free-rank calculation of
\eqref{maps:eq:D.WP9}. At odd $g$ these maps are also integral:
the free coordinate of $\tau$ is even under the weight-one
cover, and multiplication by two is invertible on $\mathbb Z/g$.
At every $g$, the finite factors remain those of $\mathcal B$.

In detail, write $r_1=\operatorname{rank}H_1(X)$, let $L$
count the nonzero-Chern originals and let $\beta$ be the sum
of the component contributions in \eqref{maps:eq:D.WP9}.
The component-disc group has rank $d+(u-1)+\beta+L$ for
$u$ unchanged caps, and $\operatorname{rank}\Gamma=u-r_1$.
The rational cokernel $\mathcal C$ has rank $r_1$ at $L=0$
and zero at $L>0$. Hence
\[
 b_2=\begin{cases}d-1+\beta+2r_1,&L=0,\\
                  d-1+\beta+L+r_1,&L>0.
       \end{cases}
\]
The local component complexes give $\chi(X)=2d$, and duality
gives $b_3=2\beta+2r_1$ at $L=0$ and $2\beta+2L$ at $L>0$.
For each cyclic Smith factor use its two-term resolution
$\mathbb Z\xrightarrow{d_j}\mathbb Z$. The dual unit cochain
represents its Ext generator modulo $d_j$, with inverse the
same residue; cap product with the oriented fundamental class
gives the corresponding $H_3$ and $H_4$ coordinates.
This proves the complete integral table \eqref{maps:eq:D.WP9}.

All operations use integer polynomial identities, integer kernels,
the finite period sum of length $h$, and Smith or Hermite
decompositions of the full stated matrices. They apply to every
positive $d$, every permitted affine power, every finite list of
regular logarithms and every integer clutch on the natural rows.
\end{proof}'''

receiver = statement.rstrip()+'\n\n'+proof.rstrip()+'\n'
patterns = (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}')
for old,new in [(old_statement,statement),(old_with_auxiliary,proof)]:
    assert text.count(old)==1
    for pattern in patterns:
        assert sorted(re.findall(pattern,old))==sorted(re.findall(pattern,new))
target = OUT/'S6_SERIES_PUBLISH_III_02LI_receiving.tex'
assert not target.exists()
target.write_text(receiver,newline='\n')
buffer=io.StringIO(newline='')
writer=csv.DictWriter(buffer,['statement_id','old_text','new_text','reason'],delimiter='\t',lineterminator='\n')
writer.writeheader()
writer.writerow(dict(statement_id='maps:src:D.2.41',old_text=old_statement,new_text=statement,
                    reason='D26: state the495 broad and459 all-star-original pattern sets with their inclusion/retraction; retain all-parity scope and exact formulas. D10: remove production header.'))
writer.writerow(dict(statement_id='maps:src:D.2.41',old_text=old_with_auxiliary,new_text=proof,
                    reason='Retain the single integral bar proof and every BC identity; supply its cycle inverse, full Thom/shear maps, all-weight free-cap transport, indexed gluing and marked homology. Move the following executable prose to the check/program records.'))
(OUT/'S6_SERIES_PUBLISH_III_02LI_replacements.tsv').write_text(buffer.getvalue(),newline='\n')
assert canonical.read_bytes()==raw
print('Receiver lines',len(receiver.splitlines()),'bytes',len(receiver.encode()),'SHA256',sha256(receiver.encode()).hexdigest())
print('Two exact guards; identities',*[len(re.findall(p,receiver)) for p in patterns])
print('One statement, one proof; canonical unchanged; final comparison and admission pending.')
