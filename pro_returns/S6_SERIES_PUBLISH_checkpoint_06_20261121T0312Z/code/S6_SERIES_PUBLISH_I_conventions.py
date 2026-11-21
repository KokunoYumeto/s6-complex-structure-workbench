from pathlib import Path
import re,json,hashlib,sympy as S
from S6_SERIES_PUBLISH_editing import Editor,block
r=Path(__file__).resolve().parents[1]
ed=Editor('I')
A1=S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
P=S.Matrix([[0,-2,-1,-2],[2,-1,0,-1],[0,2,1,3],[-1,0,0,0]])
T0=S.Matrix([[0,-1,-1,0],[1,-1,0,0],[0,0,1,0],[0,0,0,1]])
T1=S.Matrix([[-1,1,-1,2],[-1,0,-1,1],[1,1,2,-1],[0,0,0,1]])
H=S.Matrix([[-1,0,0,0],[-6,0,-1,0],[6,-1,0,0],[2,1,1,1]])
Q=P*H
assert P.det()==-1 and H.det()==1
assert T0*P==P*A1 and T1*P==P*A2
assert T0*Q==Q*A1.inv() and T1*Q==Q*A2.inv()
(r/'records/S6_SERIES_PUBLISH_I_marking_matrices.json').write_text(json.dumps({
 'method':'Exact integer matrix multiplication against the primary common-basis matrices in Engel Theorem5.1 p13 and equation(6.1) p16.',
 'det_P':int(P.det()),'det_S':int(H.det()),'Q':str(Q),'identities':['T0 P=P A1','T1 P=P A2','T0 Q=Q A1^-1','T1 Q=Q A2^-1'],
 'primary_evidence':'agents/i_provenance/literature/S6_SERIES_PUBLISH_I_Engel_v1_p013.png and p016.png, actually read by provenance agent.'},indent=2)+'\n')

start=ed.text.index('\\section{Common conventions and the marked construction}')
end=ed.text.index('\\begin{lemma}[The exact comparison of the two Weierstrass equations]',start)
old=ed.text[start:end]
new=r'''\section{The marked family and its coordinates}
\hypertarget{tag-01TG}{}\label{inv:notation-dictionary}

\begin{definition}[Base and integral marking]
\hypertarget{tag-01O1}{}\label{def:common-conventions}
\StatementRecord{def:common-conventions}{proved}{01O1}{}
Let $B=\mathbb P^1_t$, $p_1=0$, $p_2=1$, $p_0=\infty$,
$\Sigma=\{p_0,p_1,p_2\}$, and $B^\circ=B\setminus\Sigma$.
The full fibres of the marked family are $3S_1$, $4S_2$ and $W$;
$S_1,S_2,W$ are reduced, and $D=W+S_1+S_2$.
We orient base meridians counterclockwise in holomorphic local
coordinates and use clockwise root deck generators
$s_j(g_jz)=e^{-2\pi i/m_j}s_j(z)$, where $(m_1,m_2)=(3,4)$ and
$g_1g_2g_0=1$. The lift of a positive base loop ends at the inverse
deck translate, and its endpoint identification applies $g_j$.

The integral homology lattice and its dual basis are
\[
 \Lambda=\mathbb Z\langle\widehat\gamma,\widehat u,
                     \widehat w,\widehat\delta\rangle,
 \qquad (\gamma,u,w,\delta).
\]
The period matrix in coordinates $(\zeta_1,\zeta_2)$ is
\[
 \Pi_c=\begin{pmatrix}6\mu&\tau&1&0\\
                    \beta_c&\mu&0&1\end{pmatrix},
 \qquad \beta_c=\beta^{\rm part}+c,
 \qquad (\beta^{\rm part}+\tau)(p_0)=0.
\]
Its rows are $\sigma_1=6\mu\gamma+\tau u+w$ and
$\sigma_2=\beta_c\gamma+\mu u+\delta$. The monodromy matrices are
\[
 A_1=\begin{pmatrix}1&0&0&0\\6&0&1&0\\-6&-1&-1&0\\-2&1&0&1\end{pmatrix},
 \quad A_2=\begin{pmatrix}1&0&0&0\\0&0&-1&0\\-6&1&0&0\\3&0&1&1\end{pmatrix},
 \quad A_0=(A_1A_2)^{-1}.
\]
They act on columns in the displayed integral basis. Homology has
integral coefficients unless specified, and complex manifolds carry
their complex orientations. Reversing the two additive coordinates
acts by $J=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$:
the period and Hermitian matrices become $J\Pi_c$ and
$JHJ^{\mathsf t}$, respectively.
\end{definition}

\begin{definition}[The parameter and the finite translations]
\hypertarget{tag-PI01}{}\label{I:def:family-parameter}
\StatementRecord{I:def:family-parameter}{proved}{PI01}{}
Put
\[
 D_{\rm part}=\Im\beta^{\rm part}
                  -6(\Im\mu)^2/\Im\tau,\qquad
 M=\sup D_{\rm part},\qquad
 \mathcal P=\{c\in\mathbb C:\Im c<-M\},\qquad w=e^{-\pi ic}.
\]
The scalar $w$ is the family parameter; in an exterior product,
$w$ denotes the marked covector of Definition~\ref{def:common-conventions}.
The standard affine translations are
$v_1=(1,2,-4,0)^{\mathsf t}$ and
$v_2=(-1,-3,3,0)^{\mathsf t}$, and the cusp collar is untwisted.
We write $u_{\rm Engel}=e^{-2\pi ic}=w^2$ for the multiplicative
parameter with the inverse period lift at $c=0$ as its reference.
The line-bundle identification and the effect of changing that reference
are proved in Proposition~\ref{fam:src:B.1.4}.
We use $\rho=e^{\pi i/3}$; the transformation $\tau\mapsto\tau+1$
carries the convention $e^{2\pi i/3}$ to $\rho$.
\end{definition}

\begin{proposition}[Integral changes of marking]
\hypertarget{tag-01S2}{}\label{inv:B1.0}
\StatementRecord{inv:B1.0}{proved}{01S2}{}
In Engel's common integral basis, our marked basis has column matrix
\[
 P_{\rm mark}=\begin{pmatrix}
 0&-2&-1&-2\\2&-1&0&-1\\0&2&1&3\\-1&0&0&0
 \end{pmatrix}.
\]
His base indices $(0,1,\infty)$ correspond to $(1,2,0)$ here.
The matrices satisfy $T_0P_{\rm mark}=P_{\rm mark}A_1$ and
$T_1P_{\rm mark}=P_{\rm mark}A_2$, and his distinguished circle is
$\delta_{\rm E}=P_{\rm mark}\widehat\delta$.
The positive-root affine vectors are
$a_0=-P_{\rm mark}v_1/3$ and $a_1=-P_{\rm mark}v_2/4$.
For reversed meridians the change of marking is
\[
 Q=P_{\rm mark}S,
 \quad S=\begin{pmatrix}-1&0&0&0\\-6&0&-1&0\\6&-1&0&0\\2&1&1&1\end{pmatrix},
 \quad Q=\begin{pmatrix}2&-1&0&-2\\2&-1&0&-1\\0&2&1&3\\1&0&0&0\end{pmatrix},
\]
and $T_0Q=QA_1^{-1}$, $T_1Q=QA_2^{-1}$.
\end{proposition}
\begin{proof}
The matrices in \cite[Theorem~5.1, p.~13; equation~(6.1), p.~16]{Engel2026}
in that common basis are
\[
 T_0=\begin{pmatrix}0&-1&-1&0\\1&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},
 \qquad
 T_1=\begin{pmatrix}-1&1&-1&2\\-1&0&-1&1\\1&1&2&-1\\0&0&0&1\end{pmatrix}.
\]
Multiplication gives all four intertwining identities,
$\det P_{\rm mark}=-1$ and $\det S=1$. Thus these are integral
lattice isomorphisms with the stated actions. The last column of
$P_{\rm mark}$ is $(-2,-1,3,0)^{\mathsf t}$, the distinguished
circle in that basis. Since $A_jv_j=v_j$, inversion of the affine
deck generator sends its translation $v_j/m_j$ to $-v_j/m_j$.
Applying $P_{\rm mark}$ gives the displayed affine vectors.
\end{proof}

\begin{definition}[Root bundles and logarithmic differentials]
\hypertarget{tag-PI02}{}\label{I:def:root-bundles}
\StatementRecord{I:def:root-bundles}{proved}{PI02}{}
Let $\rho:\mathcal B\to B$ be the root curve of orders $(3,4)$,
with tautological root bundles $R_1,R_2$. Put $R=R_1R_2^{-1}$ and
$\mathcal O_{\mathcal B}(n)=R^n$.
Thus $R_1=R^4$, $R_2=R^3$, $\rho^*\mathcal O_B(1)=R^{12}$ and
$K_{\mathcal B}=R^{-7}$. Here $\mathcal O_B(n)$ has coarse degree $n$;
its pullback is $\mathcal O_{\mathcal B}(12n)$.
We use
\[
 \mathcal L=\Omega_B^1(\log\Sigma),\qquad
 \mathcal A=\Omega_X^1(\log D),\qquad
 \mathcal E=\mathcal A/f^*\mathcal L.
\]
Fibres in coherent base change are the full scheme fibres.
\end{definition}
\begin{proof}
The relations $R_1^3=R_2^4=\rho^*\mathcal O_B(1)$ give
$R^4=R_1$ and $R^3=R_2$. The root canonical divisor formula gives
$K_{\mathcal B}=\rho^*K_B\otimes R_1^2\otimes R_2^3
=R^{-24+8+9}=R^{-7}$.
\end{proof}

\begin{definition}[Theta, period and height conventions]
\hypertarget{tag-PI03}{}\label{I:def:theta-height}
\StatementRecord{I:def:theta-height}{proved}{PI03}{}
The theta variable has periods $(1,\tau)$. With $q=e^{2\pi i\tau}$,
define
\[
 N(z,\tau)=\left|\frac{\vartheta_1(z,\tau)}{\eta(\tau)}\right|
                 e^{-\pi(\Im z)^2/\Im\tau},\quad
 \Delta_0=q\prod_{n\ge1}(1-q^n)^{24},\quad t=j(\tau)/1728.
\]
Then $t=E_4^3/(1728\Delta_0)$ and
$t-1=E_6^2/(1728\Delta_0)$. The arithmetic Weierstrass equation is
\[
 E_t:Y^2=X^3-\tfrac34t^3(t-1)X+\tfrac14t^4(t-1)^2,
 \qquad P_t=(0,t^2(t-1)/2),\qquad \omega=dX/(2Y).
\]
Its discriminant is $\Delta_E=27t^8(t-1)^3$.
The lattice coordinates are $X=\wp(u)$, $Y=\wp'(u)/2$;
for $\Lambda=\mathbb Z+\tau\mathbb Z$,
$g_2^3-27g_3^2=(2\pi)^{12}\eta(\tau)^{24}$.
We use the height of $(O)$,
$\widehat h_O(P)=\frac12\lim n^{-2}h(x(nP))$;
the surface self-pairing and rank-one BSD regulator are
$2\widehat h_O$. The real period is
$\Omega=\int_{E(\mathbb R)}|\omega|$, summed over both real
components when there are two. The archimedean local height is
$-\log N$. At finite places $|p|_v=p^{-1}$ and
$n_v=[K_v:\mathbb Q_p]$; complex embeddings are counted separately.

Quasi-periods satisfy $\zeta(z+\omega_j)=\zeta(z)+\eta_j$ and
$\omega_1\eta_2-\omega_2\eta_1=-2\pi i$; $\eta(u)$ denotes their
real-linear extension. In the critical-point calculation we use
$\chi=(\tau-i)/(\tau+i)$, $z=k\chi^2$, and
$\beta_{\rm cusp}=\log(5+2\sqrt6)/(2\pi)$.
\end{definition}

\begin{lemma}[The real period determinant and the fibre class]
\hypertarget{tag-PI04}{}\label{I:period-determinant}
\StatementRecord{I:period-determinant}{proved}{PI04}{}
Put $y=\Im\tau$, $m=\Im\mu$, $r=\Im\beta_c$, and
$D_c=r-6m^2/y=D_{\rm part}+\Im c$.
The real period determinant in the row order
$(\Re\zeta_1,\Im\zeta_1,\Re\zeta_2,\Im\zeta_2)$ is $yD_c$.
For $D_c<0$, the integral fibre class
$\eta_F=u\wedge w+6\gamma\wedge\delta$ satisfies
\[
 \int_{F,\operatorname{or}_{\mathbb C}}\eta_F^2=-12,
 \qquad
 \Gamma=\frac{i}{2D_c}
       \left(d\bar\zeta_2-\frac myd\bar\zeta_1\right)
       =\gamma^{0,1}.
\]
Moreover $\eta_F\wedge\Gamma\wedge d\zeta_2$ equals the marked
volume form $\gamma\wedge u\wedge w\wedge\delta$.
\end{lemma}
\begin{proof}
Writing $a=\Re\mu$, $x=\Re\tau$, $b=\Re\beta_c$, the real matrix is
\[
 \begin{pmatrix}6a&x&1&0\\6m&y&0&0\\b&a&0&1\\r&m&0&0\end{pmatrix}.
\]
Its determinant is $yr-6m^2=yD_c$. Also
$\eta_F^2=12\gamma\wedge u\wedge w\wedge\delta$.
The negative determinant reverses the marked orientation relative
to the complex orientation, giving the stated integral.
The imaginary parts of the two period rows give
$\gamma=(\Im d\zeta_2-(m/y)\Im d\zeta_1)/D_c$;
taking its $(0,1)$ part gives $\Gamma$.
Substitution of the same two rows into the exterior product gives
the final identity, whose coefficient is one.
\end{proof}

\begin{definition}[The Picard coordinate]
\hypertarget{tag-PI05}{}\label{I:def:Picard-coordinate}
\StatementRecord{I:def:Picard-coordinate}{proved}{PI05}{}
Let $\mathfrak g=g_\gamma$ be the coherent Leray class with fibre
image $\gamma^{0,1}$ and put $M_z=\exp(z\mathfrak g)$, where
$\exp$ is the sheaf map $z\mapsto e^{2\pi iz}$.
We normalize $\int_B\omega_{FS}=1$ and
$c_{1,BC}(L)=[iF_L/(2\pi)]$; the unnormalized Chern--Ricci class
is $2\pi c_{1,BC}(T_X)$.
\end{definition}

\begin{remark}[Special-fibre and Picard coordinates]
\hypertarget{tag-PI06}{}\label{I:special-coordinate-values}
\StatementRecord{I:special-coordinate-values}{proved}{PI06}{}
Propositions~\ref{ari:C.1.2}, \ref{fam:src:A.4.1} and
\ref{fam:src:B.1.4} give
\[
 \begin{array}{c|c|c|c}
 &\kappa&\text{upper-half-plane period}&\text{nome}\\\hline
 S_1&c+\frac12-\frac{3i}{2\pi}\log48&-\kappa_1&
 q_1=-w^2/48^3\\
 S_2&c+\frac32-\frac{3i}{\pi}\log6&-\kappa_2/2&
 q_2=iw/216.
 \end{array}
\]
In particular $q_1=(27/64)q_2^2$ and the full compact-family domain
is $0<|w|<216$, equivalently $0<|u_{\rm Engel}|<46656$.
Proposition~\ref{inv:C3.2} fixes the collar orientation and gives
$\exp(12g_\gamma)=f^*\mathcal O_B(-p)$, where
$p=12l_0-4l_1-3l_2$. For the standard data $p=-1$,
$\exp(12\mathfrak g)=f^*\mathcal O_B(1)$,
$\mathcal O_X(S_1-S_2)=\exp(\mathfrak g)$, and $[G_0]=12\mathfrak g$.
The prescribed Chern--Ricci form in Proposition~\ref{inv:C3.6}
is $\pi f^*\omega_{FS}$.
\end{remark}

'''
# The former inv:B1.0 proof has been compared above: its theta quotient is
# already fully proved in fam:B.1.1 and its reference scalar in fam:B.1.4.
old_dictionary=block(ed.text,'inv:B1.0')
ed.replace(old_dictionary,'','D12','Consolidate the repeated theta-quotient and reference-scalar proofs with fam:src:B.1.1 and fam:src:B.1.4; relocate the unique integral marking calculation to the numbered convention proposition with the same label/tag.','inv:B1.0')
ed.replace(old,new,'D14','Merge the two overlapping convention sections into numbered definitions, an explicit marking proposition and a determinant lemma. Preserve every coordinate map and normalization; place the exact primary monodromy matrices beside their integral intertwiners. Move the software convention and historical shared-label index to the records; all mathematical source comparisons stay in their canonical statements.','def:common-conventions')
# Restore the exact theta-period identity at its mathematical proof, already
# stated there; no second assertion is kept in a dictionary.
assert r'D_{\rm part}' in ed.text
ed.save()
