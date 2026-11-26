#!/usr/bin/env python3
"""Prepare the full marked-cycle consolidation; drafts stay outside central source."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import csv,re,hashlib

root=Path(__file__).resolve().parents[1]
out=root/'agents/continuation3_conductor';stem='S6_SERIES_PUBLISH_c3_conductor_15'
reference=(out/'S6_SERIES_PUBLISH_c3_conductor_sec10_initial_reference.tex').read_text()
def statement(n):
    p=reference.index(r'\label{cdp:st:C.2.UN.'+str(n)+'}')
    a=reference.rfind(r'\begin{proposition}',0,p);b=reference.index(r'\end{proof}',p)+len(r'\end{proof}')
    return reference[a:b]
original={n:statement(n) for n in [46,48,51,55,57]}
for n,s in original.items():
    p=out/(stem+f'_UN{n}_input.tex')
    if p.exists():assert p.read_text()==s
    else:p.write_text(s,newline='\n')
with (root/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    established={r['old_tag']:r['target_label'] for r in csv.DictReader(f,delimiter='\t') if r['old_tag']}
all_old='\n'.join(original.values())
current=(root/'S6_SERIES_PUBLISH_II.tex').read_text()
p=current.index(r'\label{lem:II:normal-product-collars}')
a=current.rfind(r'\begin{lemma}',0,p);b=current.index(r'\end{proof}',p)+len(r'\end{proof}')
p326old=current[a:b]
frozen326=out/(stem+'_P326_input.tex')
if frozen326.exists():assert frozen326.read_text()==p326old
else:frozen326.write_text(p326old,newline='\n')
p326new=p326old
needle='These collars can be chosen simultaneously on all double curves.'
extension=r'''The same conclusions hold for a full reduced normal crossing fibre without triple points whose normalization $\nu:\coprod_i V_i\to S$ has smooth components and whose inverse image of each connected double curve $C$ is the disjoint union of two curves, each mapped isomorphically to $C$. These two curves label the local branches; they may lie on the same normalization component. The two normal lines in the conclusions are then the normal lines of these curves in their normalization components, transported to $C$ by the two specified isomorphisms.

These collars can be chosen simultaneously on all double curves.'''
assert p326new.count(needle)==1
p326new=p326new.replace(needle,extension,1)
p326new=p326new.replace(r'with an annulus bundle in $N_{C/V_2}^{\times}$',r'with an annulus bundle in $N_{C/B_2}^{\times}$')
needle=r'Near $C$ write $L_i=\OO_X(V_i)$ and let $s_i$ be its canonical divisor section.'
extension=r'''In the simple normal crossing case the two branch germs along $C$ are the restrictions of its two smooth components. In the normalization case, their two specified inverse curves label these germs globally along $C$. The labels agree on overlaps because each inverse curve maps isomorphically to $C$. The labelled branch germs therefore glue, after shrinking around the compact curve, to two smooth Cartier divisors $B_1,B_2$ in a neighbourhood $N$ of $C$, with $S\cap N=B_1\cup B_2$. The normalization map restricted near either inverse curve is biholomorphic onto this smooth branch. Its derivative identifies the corresponding normal line with $N_{C/B_i}$. This construction applies when the two inverse curves belong to one normalization component as well.

Near $C$ write $L_i=\OO_N(B_i)$ and let $s_i$ be its canonical divisor section.'''
assert p326new.count(needle)==1
p326new=p326new.replace(needle,extension,1)
p326new=p326new.replace('$L_1|_C=N_{C/V_2}$ and $L_2|_C=N_{C/V_1}$.','$L_1|_C=N_{C/B_2}$ and $L_2|_C=N_{C/B_1}$.',1)
needle='On a compact core in a component, $f$ is a submersion because that component has multiplicity one.'
extension=r'''Remove small open normal discs about the inverse double curves from every normalization component. Each resulting compact core maps biholomorphically onto its image in the regular part of $S$: normalization is an isomorphism there. Thus the cores are embedded in $X$, including when two boundary circles come from one self-identified normalization. On each such core, $f$ is a submersion because its branch has multiplicity one.'''
assert p326new.count(needle)==1
p326new=p326new.replace(needle,extension,1)
equations={}
for m in re.finditer(r'\\\[.*?\\\]',all_old,re.S):
    tags=re.findall(r'\\tag\{([^}]+)\}',m.group())
    if tags:assert len(tags)==1;equations[tags[0]]=m.group()
used=[];alias_maps=[]
def eq(key,aliases=(),map_text='Identity variables and maps.'):
    key='C.'+key if not key.startswith('C.') else key
    s=equations[key];tag=re.search(r'\\hypertarget\{(tag-[^}]+)\}',s).group(1)
    lab=re.search(r'\\label\{([^}]+)\}',s).group(1);assert established[key]==lab
    s=s.replace(r'\[',r'\begin{equation}',1);s=s[:-2]+r'\end{equation}';s=s.replace(r'\tag{'+key+'}','')
    used.append(key)
    hooks=[]
    for alias in aliases:
        alias='C.'+alias if not alias.startswith('C.') else alias
        d=equations[alias];atag=re.search(r'\\hypertarget\{([^}]+)\}',d).group(1);alab=re.search(r'\\label\{([^}]+)\}',d).group(1)
        hooks.append(r'\hypertarget{'+atag+r'}{}\SsixEquationAliases{\label{'+alab+'}}')
        alias_maps.append(dict(old_tag=alias,target_label=alab,owner_tag=key,map=map_text));used.append(alias)
    if hooks:s=s.replace(r'\end{equation}','\n'+'\n'.join(hooks)+'\n'+r'\end{equation}')
    return re.sub(r'\n[ \t]*\n+', '\n',s)

definition=r'''\subsection{Marked cycles and their integral lattices}\label{subsec:II:marked-cycle-lattices}

\begin{definition}[Marked normal cycles]\hypertarget{tag-P329}{}\label{def:II:marked-normal-cycle}
\StatementRecord{def:II:marked-normal-cycle}{proved}{P329}{\cite[arXiv v1, \S2.2.7--\S2.2.9, p.~5]{AbashevaDeev2024AB}}
A marked normal cycle consists of an oriented cyclic list of $N\ge1$ compact smooth surfaces $V_1,\ldots,V_N$. Each $V_i$ is either a diagonal primary or secondary Hopf surface, with its two distinct coordinate-axis curves, or a ruled surface
'''+eq('MX.1').replace('L_i',r'\mathcal L_i')+r'''
with its zero and infinity sections. We use the lines convention for $\PP$. The orientation orders these curves as incoming $C_i^-$ and outgoing $C_i^+$. Hopf surfaces of every algebraic dimension are allowed. For each edge the data include
'''+eq('HC.3').replace('H_i','V_i').replace('H_{i+1}','V_{i+1}')+r'''
The normal crossing surface $S$ is obtained by these elliptic identifications. For $N=1$, this means identifying the two distinct marked curves of the single normalization. The two inverse images of each double curve map isomorphically to it and label its two local branches. Every double curve is disjoint from the others.

The complement of the two marked curves has the logarithmic presentation
'''+eq('HC.1').replace('G_i=H_i','G_i=V_i')+r'''
For $t\ne0$, the edge map $\Phi_i(t):G_i\to G_{i+1}$ sends the elliptic base by $\phi_i$ and sends a nonzero normal vector to its $\theta_i$-dual vector with product $t$. Let $L_i$ be the complex linear part of a logarithmic lift, and let $M_i:\Lambda_i\to\Lambda_{i+1}$ be its restriction. Set
'''+eq('HC.6').replace(r'\ell','N')+r'''
The integral product $M$ is defined up to conjugacy. Its identity condition is independent of the logarithms and of multiplying any $\theta_i$ by a nonzero constant, and it is equivalent to $L=I$.
\end{definition}
\begin{proof}
For a diagonal Hopf surface with contraction $(z,w)\mapsto(\alpha z,\beta w)$, the complement of the incoming axis is the entire normal line bundle of the outgoing axis:
'''+eq('HC.4')+r'''
The specified free finite diagonal quotient gives the secondary case. Its action on the nonzero axis is free: an element with trivial character there would fix its nonzero points in the Hopf cover. Hence the quotient remains a line bundle on the quotient elliptic curve. Coordinatewise exponentiation identifies $\Lambda_i$ with the inverse image of the full diagonal deck group. It contains the two angular periods $2\pi i\Z^2$ and one contracting logarithm, with a finite angular enlargement. These three real periods are independent, since the contracting logarithm has nonzero real part; they form a lattice of rank three. The angular periods span $\C^2$ over $\C$.

For a ruled surface, the chart $v\mapsto[1:v]$ identifies the complement of the infinity section with $\operatorname{Tot}(\mathcal L_i)$; removing the zero section gives $\mathcal L_i^\times$. The other chart uses the inverse fibre coordinate and the dual line. A degree-zero line on an elliptic curve has constant factors of automorphy \cite[arXiv v1, \S2.2.7--\S2.2.9, p.~5]{AbashevaDeev2024AB}. With an oriented base-period basis $\gamma_1,\gamma_2$ and a chosen factor character $\chi_i$, its logarithmic presentation is
'''+eq('MX.3').replace('L_i',r'\mathcal L_i')+r'''
The two projected base periods are real-linearly independent, and the vertical angular period is nonzero. This proves the rank, discreteness and complex spanning assertions. The two positive normal meridians are opposite primitive lattice elements. At a Hopf vertex each angular meridian is primitive as well: a proper fractional angular period would give a nonidentity finite deck element fixing the other nonzero axis.

Each edge is a biholomorphism of the two complements. On universal covers its elliptic base map is affine. The logarithm $h$ of its nowhere-zero normal multiplier has constant increments under both base periods, because the normal lines have constant factors. Thus $h'$ descends to a holomorphic function on the compact elliptic base and is constant. The whole logarithmic lift is affine. In the ordered Hopf coordinates, where $C_i^-$ has coordinate $z_i$ and $C_i^+$ has coordinate $w_i$, it is
'''+eq('HC.5')+r'''
The ruled charts use the same affine construction in their base and line coordinates. In each case $L_i\Lambda_i=\Lambda_{i+1}$, since the lifted map descends to the specified biholomorphism. A change of logarithm adds a lattice translation; a scalar change in $\theta_i$ adds a constant in its normal direction. Neither changes $L_i$. Changing the initial integral basis conjugates $M$. Finally $\Lambda_1$ spans $\C^2$, so $M=I$ holds exactly when $L=I$.
\end{proof}

'''

period=r'''\subsection{Logarithmic period families}\label{subsec:II:logarithmic-period-families}

\begin{lemma}[A logarithmic family of two-tori]\hypertarget{tag-P331}{}\label{lem:II:logarithmic-period-family}
\StatementRecord{lem:II:logarithmic-period-family}{proved}{P331}{}
Let $\Lambda\subset\C^2$ have the integral basis
'''+eq('TL.1',aliases=['AD.5'],map_text='The common cycle coordinate map sends W to C times R and its primitive p to (0,1); w_j=(a_j,c_j). Thus Lambda=Z w1+Z w2+Z p, exactly the AD5 lattice.')+r'''
Let $N$ be a positive integer, and put
'''+eq('TL.2')+r'''
Here $\sigma\in\C$. For a fixed vector $w=(w^{(1)},w^{(2)})$, define
'''+eq('TL.3')+r'''
On any branch of $\log z$ in $\C^*$, let
'''+eq('TL.4',aliases=['AD.6'],map_text='Apply with N=d, Lambda(z)=V_z Lambda, B(z)=P4(z) and T_z=C^2/(Z P1+Z P2+Z P3+Z P4). This is exactly the full AD6 period quotient, with the same coordinate identity.')+r'''
Then $T_z=\C^2/\langle P_1(z),P_2(z),P_3(z),P_4(z)\rangle_{\Z}$ is a smooth proper family of connected complex two-tori over $\C^*$. Changing $\log z$ by $2\pi i$ sends $P_4$ to $P_4+NP_3$. Put $r=|z|$. Its real determinant, in the coordinate order $(\operatorname{Re}w^{(1)},\operatorname{Im}w^{(1)},\operatorname{Re}w^{(2)},\operatorname{Im}w^{(2)})$, is
'''+eq('TL.6',aliases=['AD.7'],map_text='Set N=d and r=|z| in the same positive determinant. No lattice scaling or omitted positive factor occurs.')+r'''
Writing $s=z^{-1}$ and changing the vector frame by $\eta_\infty=\eta/z$ gives
'''+eq('TL.7',aliases=['AD.9'],map_text='W_s(w)=V_s^infinity(w)=J conjugate(w)+s w, with J=[[0,1],[-1,0]]. These are the same vector-frame sections.')+r'''
and the four periods
'''+eq('TL.8',aliases=['AD.10'],map_text='N=d and W_s=V_s^infinity. The fourth displayed vector is precisely AD10; the first three span its unchanged rank-three lattice.')+r'''
In particular $V_0^\infty(w)=J\overline w$, where $J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.
\end{lemma}
\begin{proof}
For fixed $w$, $V_z(w)$ is holomorphic in $z$. The identity $\langle w,J\overline w\rangle=0$ gives $\|V_z(w)\|^2=(1+|z|^2)\|w\|^2$. Thus $V_z$ is an invertible real-linear map with determinant $(1+|z|^2)^2$; its orientation is positive by continuity from $V_0=I$. Its inverse is $v\mapsto(v-zJ\overline v)/(1+|z|^2)$. For $p=(0,1)$, this gives
'''+eq('TL.5')+r'''
The first three original periods span $\C\times\R$, and their real determinant with a fourth vector $v$ is $C\operatorname{Im}v^{(2)}$. Put $r=|z|$ and $\tau=N\log z/(2\pi i)$. The contribution $\operatorname{Re}\tau\,V_z(p)$ does not change the determinant. The imaginary contribution uses \eqref{cdp:eq:C.TL.5}, together with $\operatorname{Im}\tau=-N\log r/(2\pi)$ and $\operatorname{Im}b^{(2)}=1$. Multiplication by the real determinant of $V_z$ gives exactly \eqref{cdp:eq:C.TL.6}. It is positive because $(r^2-1)\log r\ge0$.

On a simply connected base chart the four holomorphic periods act by translations on $\C^2$. Their real matrices and inverses are uniformly bounded over every compact base subset. Only finitely many integral translation vectors can move one prescribed compact subset into another, so the action is properly discontinuous. The continuously varying closed real parallelepipeds give properness of the quotient over that base subset. The integral change $P_4\mapsto P_4+NP_3$ identifies these quotients on changes of logarithm, constructing the stated family on all of $\C^*$.

Division of each period by $z$ gives \eqref{cdp:eq:C.TL.7}. Since $\log z=-\log s$ up to $2\pi i\Z$, the fourth period becomes the fourth vector in \eqref{cdp:eq:C.TL.8}, with precisely its negative logarithmic coefficient. Its branch changes again add an integral period. This proves the full frame and period comparison at infinity.
\end{proof}

'''

moving=r'''\subsection{Proper normal products and moving lattices}\label{subsec:II:moving-marked-cycles}

\begin{lemma}[Moving marked cycles and their normal products]\hypertarget{tag-P333}{}\label{lem:II:moving-marked-cycle}
\StatementRecord{lem:II:moving-marked-cycle}{proved}{P333}{\cref{def:II:marked-normal-cycle,lem:II:normal-product-collars}}
For the data of \cref{def:II:marked-normal-cycle}, the prescribed normal-product maps give a smooth proper threefold $\mathcal Y\to\Delta$ whose full central fibre is the marked reduced normal crossing surface $S$. A nearby fibre $Y_t$ has
'''+eq('HC.7',aliases=['MX.4','AD.1'],map_text='The nearby fibre is Y_t=f^{-1}(t), called F_t in AD1. The common lattice Lambda in AD1 is Lambda1. All three formulas use the same core loops and oriented cycle generator in the same van Kampen presentation.')+r'''
The same presentation holds for every smooth-total smoothing with this full central fibre and its given branch and normal-product maps, including a single normalization with its two marked curves identified.

When $M=I$, identify the complements with $\C^2/\Lambda_1$ by their complex linear edge maps. If their full affine composite is
'''+eq('HC.9').replace(r'\ell','N')+r'''
then the integration of the common logarithmic coframe gives
'''+eq('HC.8').replace(r'\Lambda(t)',r'\widehat\Lambda(t)')+r'''
with the exact period lattice
'''+eq('HC.10',aliases=['MX.2'],map_text='Lambda in MX2 is Lambda1, and its b0,v0 are the same full affine cycle constants. The full rank-four period lattice is denoted widehat-Lambda(t), reserving Lambda(t) for the moving rank-three core lattice. The coordinate map is the identity.').replace(r'\Lambda(t)',r'\widehat\Lambda(t)')+r'''

This construction also permits holomorphic motion of the marked components. Choose a basis $\lambda_1,\lambda_2,\lambda_3$ of the common lattice $\Lambda$, and holomorphic vectors $\lambda_j(t)$ with $\lambda_j(0)=\lambda_j$. Transport each lattice vector by its fixed integer coordinates, and write $n_i(t)$ for the transported outgoing normal meridians. Choose holomorphic common affine edge constants $\mathbf b_i(t)\in\C^2$ with the prescribed central values. After shrinking $\Delta$, these data give smooth proper families of the marked Hopf or ruled components and their normal-product filling. Every central component, finite diagonal character, elliptic gluing map and normal-product constant is the prescribed one. Its complete punctured family is the quotient by
\begin{equation}\label{eq:II:moving-cycle-periods}
 \Lambda(t)+\Z\left(b(t)+\frac{\log t}{2\pi i}u(t)\right),
 \qquad b(t)=\sum_i\mathbf b_i(t),\qquad u(t)=-\sum_i n_i(t).
\end{equation}
Here $\Lambda(t)=\sum_j\Z\lambda_j(t)$, and all integral relations are transported with the same integer coefficients. The assertion about moving data assumes $M=I$ at the central value.
\end{lemma}
\begin{proof}
Each marked curve has an entire normal-line chart by \cref{def:II:marked-normal-cycle}. Give its degree-zero normal line a flat Hermitian metric. For an elliptic presentation with periods $\gamma_1,\gamma_2$ and factors $\chi(\gamma_j)$, the real-linear function $h$ determined by $h(\gamma_j)=\log|\chi(\gamma_j)|$ makes $|v|e^{-h(z)}$ invariant. This gives the flat metric explicitly. Choose the metric on its dual at the next component through $\theta_i$, so the product of the two normal norms is $|t|$ on $xy=t$. The two marked curves in every component are disjoint, so their small normal discs can be chosen disjoint.

Fix $0<r_0<R_0$, with $R_0$ small enough for these disjoint charts, and take $|t|<r_0^2$. At each edge use the open subset $\|x\|,\|y\|<R_0$ of the two dual lines with the holomorphic equation $xy=t$. Attach its $x$-end where $\|x\|>r_0$ and its $y$-end where $\|y\|>r_0$ to the respective component charts; the inverse inserts $t/x$ or $t/y$. Both ends cannot overlap because $\|x\|\|y\|<r_0^2$. The two ends attached to the same component remain disjoint even for a single self-identified normalization.

These maps glue the component cores times the disc and the finitely many necks by biholomorphisms. Each equivalence class meets at most one core piece and one neck piece. At either end of an attaching annulus, one of those open pieces omits its limiting point, so the gluing graph is closed relative to the product of the pieces. The finite quotient is therefore Hausdorff.

Choose $r_0<r_1<R_1<R_0$ and a closed base subdisc $|t|\le\delta<r_0^2$. Take in each component the closed core on which both marked normal norms are at least $r_1$, and take the closed neck sets on which both norms are at most $R_1$. These are compact over the compact components or elliptic bases. A point of an open core outside its closed core has one normal norm between $r_0$ and $r_1$; its dual neck coordinate has norm at most $\delta/r_0<r_0$, so the point lies in a closed neck set. A neck point with one norm greater than $R_1$ lies in its corresponding component core; the other marked normal norm there is at least $R_0$ because the two radius-$R_0$ charts are disjoint. It therefore lies in a closed core. These compact sets cover the full inverse image of the closed subdisc and prove properness. The core products are smooth and the neck equation $xy=t$ is smooth, with central branches of multiplicity one. Thus the central fibre is exactly the specified marked surface.

On a ruled complement, the logarithm of the flat norm is a linear height on its logarithmic cover, with compact three-torus levels. For a primary Hopf complement one may take
$h=\log|z|-(\log|\alpha|/\log|\beta|)\log|w|$.
The other normal height is $-(\log|\beta|/\log|\alpha|)h$, so small discs around the two axes bound a compact height interval. These heights are invariant under the finite diagonal group as well. Consequently each core and each annular neck retracts onto a three-torus. They are connected, every attaching annulus is connected, and their incidence cycle is connected, so the nearby fibre is connected. Their collar maps induce exactly the lattice isomorphisms $M_i$. Van Kampen along a spanning tree of the cycle, followed by its last edge, gives \eqref{cdp:eq:C.HC.7}, with the lattice injected. Choose the cycle generator so that conjugation transports the core loops through the oriented edge maps and acts by $M$.

For a given smoothing, apply \cref{lem:II:normal-product-collars} to its full reduced central fibre. Its normalization has the given smooth components, and the two marked curves over each double curve map isomorphically to that curve, so the branch-labelled clause applies also in the self-identification case. The lemma identifies the smooth collars with these same normal circle bundles and product maps, and transports the compact normalization cores compatibly with their boundaries. It therefore supplies exactly the same van Kampen homomorphisms and the same presentation.

Suppose $M=I$. Since the lattices span their complex vector spaces, the complex cycle product is the identity. With $P_1=I$ and $\Lambda=\Lambda_1$, choose constant matrices identifying the complements by
'''+eq('HG.2')+r'''
The common logarithmic differentials $P_i\,d\log(z_i,w_i)$ on Hopf charts, and the corresponding base and logarithmic line differentials on ruled charts, glue across every neck to a closed holomorphic coframe on each nearby compact fibre. The dual fields commute because the forms are closed. They have complete complex-time flows: compactness gives a uniform local existence interval, which can be iterated. Their action of $\C^2$ has open orbits, hence one orbit on the connected fibre, and a discrete cocompact stabilizer. The orbit map proves \eqref{cdp:eq:C.HC.8}.

Integration on the core loops gives exactly $\Lambda_1$, while the oriented cycle loop gives the translation in \eqref{cdp:eq:C.HC.9}. These are all the fundamental-group generators in \eqref{cdp:eq:C.HC.7}; thus the stabilizer is exactly \eqref{cdp:eq:C.HC.10}. A turn of $\log t$ changes its last period by $2\pi i v_0\in\Lambda_1$, because each edge map is single-valued. This proves the full fixed-data period comparison.

For the moving construction, real independence of $\lambda_j(t)$ and complex spanning persist near zero. The incoming normal meridian at vertex $i$ is $-n_{i-1}(t)$. At a Hopf vertex, $n_i(0)$ and $n_{i-1}(0)$ are complex-linearly independent. At a ruled vertex they are equal; extend the primitive $n_i$ to an integral basis $n_i,\lambda_i,c_i$ of the common lattice. The images of $\lambda_i,c_i$ in the elliptic quotient are real-linearly independent, so $\lambda_i$ and $n_i$ are a complex basis. Transport all three by their fixed integer coefficients. The inverse of the complex frame $(\lambda_i(t)/(2\pi i),n_i(t)/(2\pi i))$ then gives the exact ruled presentation
'''+eq('MX.10')+r'''
The projected periods remain real-linearly independent near zero. They define the moving elliptic base, and the factor $\exp b_i(t)$ in this displayed lattice defines its degree-zero line. Its projective completion is a smooth proper family of the original marked ruled surface.

With these ruled frames and the Hopf frames, the common-coordinate identities are
'''+eq('HG.12',aliases=['AD.8'],map_text='For the twistor application, n_i(z)=V_z(n_i) and Lambda(z)=V_z Lambda. The Hopf part of HG12 is exactly AD8 under t=z, with the same two angular vectors and full finite angular enlargement. At ruled vertices the separate MX10 frame is used instead.')+r'''
where the formula for the two displayed columns of $P_i(t)$ is used at Hopf vertices. A Hopf lattice contains its two fixed angular periods. Its quotient by that angular sublattice has the same abstract integral relations as at zero. A chosen contracting generator has holomorphic logarithms $P_i(t)^{-1}c_i(t)$ with negative real parts on a smaller disc. Every finite generator still has the relation $m v=A(2\pi i,0)+B(0,2\pi i)$ with the same integers. Thus its two finite characters and their freeness conditions are unchanged. Exponentiation gives the marked primary or secondary Hopf family. Uniform contraction gives a compact annulus meeting every orbit over a closed smaller base disc, proving properness of this family.

For every edge, $L_i(t)$ maps its entire lattice to the next one and its outgoing normal to minus the next incoming normal. Hence it induces the elliptic base isomorphism and the reciprocal normal-line map. Adding the chosen common vector $\mathbf b_i(t)$ gives their affine constants, holomorphic in $t$, with the prescribed central maps. The ruled and Hopf cases both extend over their marked curves through their entire line-bundle charts. The component metrics just constructed vary smoothly with $t$: the real-linear equations defining $h_t$ have an invertible base-period matrix. Disjoint cores, flat norms and radii can therefore be chosen uniformly on a smaller disc. The same finite gluing and compact-core argument gives the moving proper filling, still with $xy=t$ and multiplicity one on every central branch.

In common coordinates the logarithmic term on edge $i$ is $-n_i(t)\log t/(2\pi i)$. Summing all edge constants and terms gives \eqref{eq:II:moving-cycle-periods}. On successive cores use their logarithmic maps to the common vector space and subtract the accumulated affine edge constants. Use those same maps on the necks. They agree on overlaps modulo $\Lambda(t)$; the last overlap adds exactly the displayed cycle period. A change of logarithm adds the integral vector $u(t)$. These maps define a holomorphic map of the entire punctured family to the displayed period quotient. On each fibre it is the coframe isomorphism already proved. Its vertical differential is invertible and it is the identity on the base; hence it is locally biholomorphic, and its fibrewise inverses glue holomorphically. This proves the complete moving-family comparison.
\end{proof}

'''

criterion=r'''\subsection{The marked-cycle criterion}\label{subsec:II:marked-cycle-criterion}

\begin{proposition}[Marked cycles with torus smoothings]
\hypertarget{tag-01E2}{}\label{cdp:st:C.2.UN.57}
\StatementRecord{cdp:st:C.2.UN.57}{proved}{01E2}{\cref{def:II:marked-normal-cycle,lem:II:moving-marked-cycle,lem:II:logarithmic-period-family,cdp:st:C.2.UN.40,lem:II:central-primary-hopf-cover}; \cite[arXiv v1, \S2.2.6, p.~5]{AbashevaDeev2024AB}}
\hypertarget{tag-01DQ}{}\label{cdp:st:C.2.UN.46}
\StatementRecord{cdp:st:C.2.UN.46}{proved}{01DQ}{}
\hypertarget{tag-01DW}{}\label{cdp:st:C.2.UN.51}
\StatementRecord{cdp:st:C.2.UN.51}{proved}{01DW}{}
\hypertarget{tag-01E0}{}\label{cdp:st:C.2.UN.55}
\StatementRecord{cdp:st:C.2.UN.55}{proved}{01E0}{}
For a marked normal cycle in \cref{def:II:marked-normal-cycle}, its proper normal-product plumbing satisfies
'''+eq('HC.2')+r'''
Every smooth-total two-torus smoothing with this full reduced central fibre has $M=I$. This identity is also equivalent to occurrence of the specified support as a full reduced fibre of a smooth compact complex threefold over $\PP^1$ with connected two-torus general fibre. The compact construction preserves every marked component and every elliptic gluing map and chooses the normal-product constants. Its only other singular fibre is the complex conjugate marked support. Every reduced fibre support has Euler characteristic zero.

A compatible cycle containing a Hopf component contains at least two Hopf components. For an all-ruled cycle, including the two-section identification of one ruled normalization, the projection of $b_0$ in \eqref{cdp:eq:C.HC.10} to the common elliptic quotient is the full elliptic translation around the cycle. The compact construction preserves that translation.

Every full reduced SNC fibre in a smooth-total two-torus degeneration whose components are unblown diagonal Hopf surfaces of algebraic dimension zero is such a cycle, with no triple points and with both axes of every component in its boundary. For two components, the Hopf surfaces are isomorphic, and a diagonal automorphism of one copy makes both gluing maps inversion. Thus the support is two copies of the same primary or secondary diagonal Hopf surface joined by the two inversion maps. Every such support has the compact realization above. The two normal-product constants remain the parameters of the local quotient \eqref{cdp:eq:C.HC.9}--\eqref{cdp:eq:C.HC.10}.

The identification of the two distinct axes of a single diagonal Hopf surface has $M\ne I$ and admits no smooth-total two-torus smoothing.
\end{proposition}
\begin{proof}
Apply \cref{lem:II:moving-marked-cycle} to the specified components, elliptic identifications and dual-normal maps. It supplies the proper plumbing. For a given smoothing the transverse bilinear term of its defining function gives a dual-normal trivialization on each double curve. Its ratio with the specified trivialization is a nowhere-zero holomorphic function on that compact elliptic curve, hence a constant. By \cref{def:II:marked-normal-cycle} this leaves $M$ unchanged. The lemma therefore gives the same presentation \eqref{cdp:eq:C.HC.7} for the given smoothing, including the branch-labelled self-identification. The injected subgroup $\Lambda_1$ and the cycle generator commute precisely when $M=I$. A two-torus has abelian fundamental group, giving necessity. For $M=I$ the lemma's closed coframe and orbit map give the biholomorphism \eqref{cdp:eq:C.HC.8} with the full lattice \eqref{cdp:eq:C.HC.10}. This proves \eqref{cdp:eq:C.HC.2} with all affine constants retained.

Assume $M=I$ and use the common logarithmic coordinates \eqref{cdp:eq:C.HG.2}. Let $n_i\in\Lambda$ be the positive outgoing normal meridian. The incoming one at vertex $i$ is $-n_{i-1}$. At every ruled vertex the two meridians are opposite, giving
'''+eq('MX.5')+r'''
At a Hopf vertex the two complex normal lines are independent. The frames at those vertices and the total normal period of the cycle are
'''+eq('HG.3',aliases=['AD.2'],map_text='The first formula is the identical Hopf frame P_i=(n_i/(2pi i),-n_(i-1)/(2pi i)) of AD2. The second formula records the sum of the same oriented edge logarithmic coefficients; the ruled vertices use their separate MX10 frame.')+r'''
The sum follows from the edge coefficient $-n_i/(2\pi i)$ in \eqref{eq:II:moving-cycle-periods}. A cycle with one Hopf vertex would force $n_i=n_{i-1}$ there by following \eqref{cdp:eq:C.MX.5} through all the other vertices, contradicting that independence. In particular a single Hopf self-identification is impossible when $M=I$. Equivalently, its sole matrix in \eqref{cdp:eq:C.HC.5} has upper-left entry zero and cannot be the identity.

Put $W=\operatorname{span}_{\R}\Lambda$ and choose a nonzero real linear functional $\ell$ with kernel $W$. A Hopf contraction with logarithms $(\log\alpha_i,\log\beta_i)$ gives the common lattice vector $P_i(\log\alpha_i,\log\beta_i)$. Applying $\ell$ to this vector and using \eqref{cdp:eq:C.HG.3} gives
'''+eq('HG.4',aliases=['MX.6','AD.3'],map_text='Identical common lattice, oriented outgoing n_i, incoming -n_(i-1), functional ell with kernel W, and the same Hopf contraction alpha_i,beta_i. All three real coefficient identities coincide.')+r'''
Both logarithms are negative. If one transverse value vanished, both would vanish, placing the two independent complex normal lines in the real three-plane $W$. Thus both values are nonzero and have the same sign. Equation \eqref{cdp:eq:C.MX.5} propagates that sign through every ruled vertex. In the all-ruled case, their common normal $n$ has $\C n\cap W=\R n$: projection along $\C n$ gives the rank-two lattice of its elliptic base. Hence the common transverse value is again nonzero. In every case
'''+eq('HG.5',aliases=['MX.7'],map_text='Here u=2pi i v0=-sum n_i is the identical vector already displayed in HG3. The HG5 formula proves its nonzero transverse value. Together these give both clauses of MX7, with the alias placed at the nonvanishing conclusion.')+r'''
It follows that $u\ne0$ and $\C u\cap W=\R u$. Write $u=d p$ with $p$ primitive in $\Lambda$ and $d>0$. The common affine edge constants $\mathbf b_i$ have sum $b$, and the fourth period is
'''+eq('AD.4')+r'''

The real quotient $W/\R p\to\C^2/\C p$ is an isomorphism. Put $K=W\cap iW$, a complex line. Since $ip\notin W$, one has $W=K\oplus\R p$, and a nonzero vector of $K$ together with $p$ is a complex basis of $\C^2$. Send $K$ to the first coordinate line and $p$ to $(0,1)$; this complex linear isomorphism sends $W$ to $\C\times\R$. Extend $p$ to an integral basis and orient its two remaining projected periods so that the lattice has exactly the form \eqref{cdp:eq:C.TL.1}. Every $n_i$ has nonzero second coordinate, by the preceding transverse calculation. Changing one normal-product constant adds an arbitrary complex multiple of this $n_i$ to its edge translation, so choose it to make $b=(\sigma,i)$ as in \eqref{cdp:eq:C.TL.2}. The elliptic gluing map is unchanged because this direction is its normal line. In the all-ruled case $p=-n$ and $u=Np$. Every adjustable direction lies in $\C p$, so the projection of $b$ to $\C^2/(\C p+\Lambda)$, including its full horizontal translation $\sigma$, remains unchanged.

Apply \cref{lem:II:logarithmic-period-family} to this exact lattice, this $b$ and the positive integer $d$ in place of its $N$. Its periods \eqref{cdp:eq:C.TL.4}, with $\Lambda(z)=V_z\Lambda$ and fourth period $B(z)$, are the quotient in \eqref{cdp:eq:C.AD.6}; its determinant \eqref{cdp:eq:C.TL.6} gives \eqref{cdp:eq:C.AD.7}. This constructs the smooth proper family of two-tori on all of $\C^*$.

At zero apply the moving clause of \cref{lem:II:moving-marked-cycle} with $\lambda_j(z)=V_z(\lambda_j)$ and $\mathbf b_i(z)=V_z(\mathbf b_i)$. Every integer coordinate of every normal meridian and finite character is unchanged. Its Hopf frames \eqref{cdp:eq:C.HG.12} are precisely \eqref{cdp:eq:C.AD.8}, while ruled vertices use \eqref{cdp:eq:C.MX.10}. The central components and elliptic maps are the specified ones. The sum of the affine constants is $V_z(b)$, and the normal sum is $dV_z(p)$, so \eqref{eq:II:moving-cycle-periods} is exactly the fourth period of \eqref{cdp:eq:C.AD.6}. The lemma's piecewise logarithmic maps and their holomorphic inverses identify the entire punctured filling with that period family.

At infinity put $s=z^{-1}$ and use the frame $\eta_\infty=\eta/z$ of \cref{lem:II:logarithmic-period-family}. Write $W_s=V_s^\infty$ in \eqref{cdp:eq:C.TL.7}; this is the map \eqref{cdp:eq:C.AD.9}. Choose outgoing normals $n_i^\infty(s)=-W_s(n_i)$ and affine constants $\mathbf b_i^\infty(s)=W_s(\mathbf b_i)$. Their total normal period is $-dW_s(p)$ and their constant sum is $W_s(b)$, giving exactly \eqref{cdp:eq:C.AD.10}.

For a Hopf vertex the frame at $s=0$ satisfies
'''+eq('AD.11')+r'''
Indeed $\overline{2\pi i}=-2\pi i$, so the two columns built from $n_i^\infty(0),-n_{i-1}^\infty(0)$ are $J\overline{P_i}$. Applying its inverse to $W_0\Lambda=J\overline\Lambda$ gives the second identity. Thus the contracting logarithms and finite angular characters are exactly their complex conjugates, still contracting and free.

At a ruled vertex take the separate frame $(\lambda_i/(2\pi i),n_i/(2\pi i))$ used in \eqref{cdp:eq:C.MX.10}. At infinity choose the lattice lift $\lambda_i^\infty(0)=-W_0(\lambda_i)$ as well as $n_i^\infty(0)=-W_0(n_i)$. Its frame is again $J$ times the conjugate original frame, and its component lattice is the conjugate lattice. Exponentiation therefore identifies its elliptic base, degree-zero line and marked projective completion with their complex conjugates. In either component type the coordinate expression of an edge constant is also conjugated:
\[
 (J\overline{P_i})^{-1}J\overline{\mathbf b}
       =\overline{P_i^{-1}\mathbf b}.
\]
Consequently the elliptic gluing maps are precisely the conjugate specified maps. Apply \cref{lem:II:moving-marked-cycle} to these central conjugate data, with moving lattice $W_s\Lambda$, the indicated outgoing normals and the constants $W_s(\mathbf b_i)$. Its full period quotient is \eqref{cdp:eq:C.AD.10}, and its equation $xy=s$ gives a smooth proper filling whose full central fibre is the conjugate marked support.

Glue the two fillings to the period family on $\C^*$ by these punctured-family biholomorphisms and the frame change $\eta_\infty=\eta/z$. Choose disjoint small discs at zero and infinity and a middle annulus. Over every base point the gluing identifies all pieces with one Hausdorff proper local model. A finite closed refinement of the three base charts has compact inverse images, proving that the total space is Hausdorff and proper over $\PP^1$, hence compact. Its charts are smooth. All middle fibres are the connected two-tori of the period family. Each Hopf component has Euler number zero by \cref{lem:II:hopf-curves} and its sphere-bundle calculation; each ruled elliptic component has $e(\PP^1)e(E)=0$. Each double curve is elliptic, and there are no triple points. The normalization and double-curve decomposition therefore gives Euler number zero for both singular supports, including a single ruled self-identification.

For the asserted SNC Hopf branch, apply \cref{cdp:st:C.2.UN.40} to the given smooth unblown components. Both axes lie in the boundary. On a primary diagonal Hopf surface of algebraic dimension zero they are the only curves by \cite[arXiv v1, \S2.2.6, p.~5]{AbashevaDeev2024AB}: a nonzero integer relation between its multipliers would give a nonconstant invariant meromorphic monomial. For a secondary component, \cref{lem:II:central-primary-hopf-cover} preserves algebraic dimension under its finite primary cover. The inverse image of every curve is therefore a union of those axes; the diagonal deck group preserves each axis and their images remain distinct. Thus each component has exactly its two disjoint boundary curves. The SNC equation supplies exactly one other branch at each. The connected incidence graph has degree two at every vertex and is a cycle, with two parallel edges allowed. Its normal-product maps come from the transverse bilinear term of its full reduced fibre equation.

For two Hopf components multiply their edge matrices:
'''+eq('HC.11')+r'''
The product is the identity exactly when $c_1=c_2=-1$ and $k_1=k_2=0$. Hence $L_1=L_2=-S_0$, where $S_0$ exchanges the two coordinates, and $\Lambda_2=-S_0\Lambda_1$. Coordinatewise exponentiation gives $\Gamma_2=(S_0\Gamma_1)^{-1}=S_0\Gamma_1$. Thus $(z,w)\mapsto(w,z)$ descends to a biholomorphism of the two Hopf surfaces, including their finite diagonal subgroups. Under this map their elliptic identifications have the form $z\mapsto a/z$ and $w\mapsto b/w$. The diagonal automorphism $(Z,W)\mapsto(a^{-1}Z,b^{-1}W)$ commutes with the complete deck group and turns both maps into inversion. The compact construction already proved applies to this same reduced support; \eqref{cdp:eq:C.HC.9}--\eqref{cdp:eq:C.HC.10} preserve each specified local normal-product constant.
\end{proof}

'''

suspension=r'''\subsection{Elliptic suspensions realizing marked cycles}\label{subsec:II:cycle-elliptic-suspensions}

\begin{proposition}[Elliptic suspensions realizing marked cycles]\hypertarget{tag-01DS}{}\label{cdp:st:C.2.UN.48}
\StatementRecord{cdp:st:C.2.UN.48}{proved}{01DS}{\cref{cdp:st:C.2.UN.57,lem:II:moving-marked-cycle,cdp:st:C.2.UN.41,lem:II:central-primary-hopf-cover}; \cite[arXiv v3, Definition~3.1, p.~7; \S7.6, pp.~33--34]{SchuttShioda2010}}
Let $S$ be a marked normal cycle with $M=I$, containing a Hopf component, and suppose that every Hopf component has algebraic dimension zero. The other components may be the marked ruled surfaces of \cref{def:II:marked-normal-cycle}. There is a holomorphic map $f:Y\to\PP^1$ from a smooth compact complex threefold with connected two-torus general fibre and full reduced SNC central fibre isomorphic to the specified $S$. Every reduced fibre support has Euler characteristic zero.

This realization is obtained by replacing a neighbourhood of one fibre in the compact elliptic suspension \eqref{cdp:eq:C.HG.10}. Its punctured periods are \eqref{cdp:eq:C.HG.11}, with the affine matching \eqref{cdp:eq:C.HG.13}--\eqref{cdp:eq:C.HG.14}. It preserves every component, every finite secondary character and every elliptic gluing map, and chooses the normal-product constants. In particular it realizes every compatible all-Hopf cycle of arbitrary length in the stated algebraic-dimension-zero class.
\end{proposition}
\begin{proof}
Use the common lattice $\Lambda$ and vector $u=d p$ from the proof of \cref{cdp:st:C.2.UN.57}, where $p$ is primitive and $d>0$. The nonvanishing \eqref{cdp:eq:C.HG.5} makes $W/\R p\to\C^2/\C p$ an isomorphism of real planes. Extend $p$ to an integral basis $p,\lambda,c$ of $\Lambda$. Choose a complex linear quotient coordinate $X$ with $X(\lambda)=2\pi i$; the two projected periods are real-linearly independent, so $\operatorname{Re}X(c)\ne0$. Reverse $c$ to make this real part negative. Choose the second complex linear coordinate $Z$ by $Z(p)=2\pi i$ and $Z(\lambda)=0$. The vectors $p,\lambda$ are complex-linearly independent, so this determines a complex linear isomorphism and gives
'''+eq('HG.6',aliases=['MX.8'],map_text='The common linear map (X,Z) sends p to (0,2pi i), lambda to (2pi i,0), and c to (log q0,log a). The mixed-cycle MX8 lattice is this same lattice, with the same u=d(0,2pi i), and the stronger displayed 0<|q0|<1 includes its stated bound.')+r'''
The logarithms are these chosen coordinates of $c$.

One has $a\ne1$. Otherwise subtract an integral multiple of $(0,2\pi i)$ from $c$ so that its second coordinate is zero. Then
'''+eq('HG.7')+r'''
is well defined and injective: equality of its images forces the coefficient of $(0,2\pi i)$ to vanish, leaving exactly the two periods in its source. Its derivative is injective; compactness makes it an embedded elliptic curve in $G$. This is impossible in the complement of the two axes of one of the Hopf components. For a primary component the nonresonant diagonal curve list in \cite[arXiv v1, \S2.2.6, p.~5]{AbashevaDeev2024AB} gives only those axes. For a secondary component, apply \cref{lem:II:central-primary-hopf-cover} to preserve algebraic dimension on its finite primary cover; the inverse image of any curve is a union of its axes, so again there is no curve in the complement.

The nodal cubic and its prescribed smooth point are
'''+eq('HG.8')+r'''
in the affine chart $z=1$. Substitution gives the cubic equation, and its smooth group coordinate $\zeta=(y/x-1)/(y/x+1)$ has value $a$. Since $a\in\C^*\setminus\{1\}$, this point is distinct from $O$ and from the node. Apply the nodal-cubic pencil construction in the proof of \cref{cdp:st:C.2.UN.41} to this pair $O,P_0$. Its restriction and first-jet argument uses exactly these two distinct smooth points: it gives a second cubic transverse at nine distinct smooth base points and missing the node. Blowing up those points yields the smooth compact rational elliptic surface with sections $O,P$ and this selected $I_1$ fibre.

Make the global base change $\PP^1_s\to\PP^1$ given by $s\mapsto s^d$ at the selected value. Normalize, resolve and take its smooth relatively minimal elliptic model $J\to\PP^1_s$. The equation at the selected node before resolution is $xy=s^d$. Its resolution has charts $(u_j,v_j)$, $0\le j<d$, with
\[
 x=u_j^{j+1}v_j^j,\qquad
 y=u_j^{d-j-1}v_j^{d-j},\qquad s=u_jv_j,
\]
and adjacent gluing $u_{j+1}=v_j^{-1}$, $v_{j+1}=u_jv_j^2$. These maps are isomorphisms off the node and insert the chain of $d-1$ projective lines between its two branches. Their central equations are $u_jv_j=0$, so together with the original component they give the $I_d$ fibre. The two sections avoid the node and retain their values in its identity component. The other operations are proper vertical modifications of the projective base change. The resulting $J$ is smooth, projective and relatively minimal over $\PP^1_s$. Apply \cite[arXiv v3, Definition~3.1, p.~7; \S7.6, pp.~33--34]{SchuttShioda2010} to this $J$ and the section $P$: translation by $P$ extends to an automorphism over the base, with inverse translation by $-P$.

Pull back the exact nodal Tate comparison in the proof of \cref{cdp:st:C.2.UN.41} along the same $s\mapsto s^d$. Its parameter $Q_1$ has a simple zero, so $Q(s)=Q_1(s^d)$ has order $d$. Its smooth central group-coordinate comparison is the coordinate $a$ above; the inverse function theorem at this point gives the section lift in
'''+eq('HG.9')+r'''
Choose a holomorphic $d$th root of the unit $Q(s)/s^d$ and put $t=s(Q(s)/s^d)^{1/d}$. This coordinate has nonzero derivative at zero and gives $Q=t^d$ exactly. Write the section lift as $a(t)$ and choose its holomorphic logarithm with value $\log a$.

Form the suspension
'''+eq('HG.10')+r'''
The action is free and properly discontinuous because its first coordinate is multiplied by $q_0$, with $0<|q_0|<1$. A closed annulus in $\C^*$ times the compact $J$ meets every orbit, so the quotient is compact and smooth. Its general fibre is a connected two-torus: in additive coordinates the elliptic-fibre lattice and a logarithm of its section translation give a rank-four lattice, whose remaining real direction is supplied by $\log|q_0|\ne0$. At the distinguished value its punctured periods are exactly
'''+eq('HG.11',aliases=['MX.9'],map_text='The mixed realization uses the identical t with Q=t^d, the identical section lift a(t) with a(0)=a, and the same q0. MX9 is this complete period lattice in the same (log b,log y) coordinates.')+r'''
The map from this additive quotient to the suspension sends $[(X,Z)]$ to $[(e^X,[e^Z])]$. The two angular periods exponentiate to the identity, $(\log q_0,\log a(t))$ is its suspension generator, and $(0,d\log t)$ is the elliptic-fibre generator. Local logarithms give its inverse modulo these same generators.

Transport every $n_i$ and every chosen contracting period by its fixed integer coefficients in the three generators of \eqref{cdp:eq:C.HG.6}, replacing that basis by the basis of $\Lambda(t)$ in \eqref{cdp:eq:C.HG.11}. In particular $\sum_i n_i(t)=-d(0,2\pi i)$. Apply the moving clause of \cref{lem:II:moving-marked-cycle} to this lattice. Its Hopf frames are \eqref{cdp:eq:C.HG.12}, with all finite angular relations unchanged; its ruled frames are \eqref{cdp:eq:C.MX.10}. Thus both sorts of marked component have their prescribed central surfaces.

Choose the affine edge lifts holomorphically, preserving the constants of each central elliptic gluing map. In the all-Hopf case write those fixed constants as $d_i$ and the adjustable normal-product logarithms as $e_i(t)$. Their sum is
'''+eq('HG.13')+r'''
For a ruled edge use the base and line frame \eqref{cdp:eq:C.MX.10}; its adjustable normal constant has the same common coefficient $-n_i(t)/(2\pi i)$. Thus in the mixed case the full sum is likewise $b_0(t)+(0,d\log t)$. Choose a Hopf vertex $i+1$. The coefficients $-n_i(t)/(2\pi i)$ and $-n_{i+1}(t)/(2\pi i)$ of its two adjacent normal-product logarithms are complex-linearly independent near zero. Fix the other constants and solve this invertible two-by-two holomorphic linear system to obtain
'''+eq('HG.14')+r'''
These changes lie in the normal directions and preserve all elliptic gluing maps.

Now apply \cref{lem:II:moving-marked-cycle} with these adjusted affine constants. Its full period formula has constant sum zero and normal sum $d(0,2\pi i)$, so it is exactly \eqref{cdp:eq:C.HG.11}. Its maps send each core logarithm to the common vector space and subtract the accumulated edge constants; on the last overlap the difference is $(0,d\log t)$, and logarithm changes give $\Lambda(t)$. Composing the lemma's punctured-family biholomorphism with the exponential map above identifies the entire local filling with \eqref{cdp:eq:C.HG.10} over the punctured disc, including every affine parameter. Its full central divisor is the prescribed reduced cycle.

Replace the distinguished tube in $Y^{\rm std}$ by this filling. Remove a closed smaller base disc from the suspension and use the filling over a larger disc; glue by the displayed isomorphism on the intervening annulus. At either annular boundary only one piece contains the limiting base point, giving a Hausdorff gluing. Closed smaller pieces in the two proper families cover the result and are compact. This proves compactness, while the same charts preserve smoothness and the holomorphic map to $\PP^1_s$. All fibres are connected.

Every component of the new central support, and every double elliptic curve, has Euler number zero, so its support does also. At any other value the support is unchanged from the suspension. Its projection to $\C^*/q_0^{\Z}$ is a locally trivial bundle with fibre $J_s^{\rm red}$ and transition the automorphism induced by $P$. Its finite cellular complex with these local coefficients has Euler number $e(\C^*/q_0^{\Z})e(J_s^{\rm red})=0$. This gives the asserted Euler number at every value.
\end{proof}

'''

examples=r'''\subsection{Explicit Hopf and ruled cycles}\label{subsec:II:explicit-marked-cycles}

\begin{example}[Three Hopf components and ruled insertions]\hypertarget{tag-P332}{}\label{ex:II:three-hopf-cycle}
\StatementRecord{ex:II:three-hopf-cycle}{proved}{P332}{\cref{cdp:st:C.2.UN.48,cdp:st:C.2.UN.57,cdp:st:C.2.UN.41}}
There is a compact realization with the three primary Hopf contractions and edge matrices
'''+eq('HG.1')+r'''
The matrix product is the identity, and the full multiplicative cycle period is $(t^{-2},t^2)$. The construction also gives a secondary three-cycle with the finite weights $(1,2),(3,2),(2,4)$ modulo $5$ on these respective components. In both cases the positive divisor of the total normal period in the common lattice is $2$.

For a repeated two-component inversion cycle of length $2k$ with free finite weights $(a,b)$ modulo $n$, so that $\gcd(a,n)=\gcd(b,n)=1$, the positive normal-period divisor is
'''+eq('HG.17')+r'''
In particular the weights $(1,4)$ modulo $5$ give divisor $5$ for two components.

For every pair of integers $a,b\ge1$ there is also a marked cycle with two Hopf components and $a+b-2$ ruled components. Its positive normal-period divisor is $\gcd(a,b)$. These cycles have the compact realizations of \cref{cdp:st:C.2.UN.48}.
\end{example}
\begin{proof}
For the three-component example use the common lattice generated by $2\pi i\Z^2$ and the following $c$, with outgoing meridians
'''+eq('HG.15')+r'''
The frames \eqref{cdp:eq:C.HG.3} give the contracting logarithms $P_1^{-1}c$, $-P_2^{-1}c$ and $-P_3^{-1}c$, which are exactly the three pairs in \eqref{cdp:eq:C.HG.1}. Their ratios are irrational, hence their multipliers are multiplicatively independent; the curve calculation in \cref{cdp:st:C.2.UN.41} gives algebraic dimension zero. Matrix multiplication gives $L_3L_2L_1=I$. The corresponding multiplicative maps, with normal-product constants one, are
'''+eq('HG.16')+r'''
Their composite is $(z,w)\mapsto(t^{-2}z,t^2w)$. Thus $u=2\pi i(-2,2)$, whose divisor in the angular lattice is $2$. A nonzero multiple of $c$ has nonzero real part, so it does not enlarge the lattice on this angular line. The marked-cycle criterion and \cref{cdp:st:C.2.UN.48} give its compact realization.

For the finite repeated cycle, in units of $2\pi i$ the angular lattice is $\Z^2+\Z(a,b)/n$ and its total normal period is $k(-1,1)$. A representative $j(a,b)/n$ lies on this line modulo $\Z^2$ precisely when $n\mid j(a+b)$. Put $g=\gcd(n,a+b)$. Then $j$ is a multiple of $n/g$, and the fractions in the first coordinate are the multiples of $a/g$ modulo integers. Since $\gcd(a,g)=1$, they give every multiple of $1/g$. Hence the intersection with the line is $\Z(-1,1)/g$, proving \eqref{cdp:eq:C.HG.17}. The sign follows from the outgoing vectors $(1,0)$ and $(0,-1)$.

In the three-component example enlarge the common angular lattice by $(1,2)/5$. Applying the three inverse frames gives weights $(1,2),(3,2),(2,4)$ modulo $5$. Each coordinate is coprime to $5$, so each finite action is free on both nonzero axes and on their complement. The preceding line calculation has $g=\gcd(5,1+2)=1$ and leaves the divisor of $(-2,2)$ equal to $2$. The same period and normal-product construction therefore gives the asserted secondary compact cycle.

For the mixed examples choose real numbers $A,B<0$ with irrational ratio and use the common lattice
\[
 \Lambda=\langle 2\pi i(1,0),2\pi i(0,1),(A,B)\rangle_{\Z}.
\]
Take the cyclic list of outgoing normal vectors to be $a$ copies of $2\pi i(1,0)$ followed by $b$ copies of $2\pi i(0,-1)$. At each of its two changes, the frame with columns $n_i/(2\pi i),-n_{i-1}/(2\pi i)$ gives a Hopf component; choose the contracting generator $(A,B)$ at the first change and its negative at the second. Their contracting logarithms are $(A,B)$ and $(B,A)$, respectively, so both have algebraic dimension zero. Each repeated normal gives the ruled component constructed from the quotient along its normal line and the lattice of \eqref{cdp:eq:C.MX.10}. The remaining projected real period is nonzero because $A,B<0$, so that quotient is elliptic. This defines all $a+b$ marked components and their normal lines.

Choose the angular frames unimodularly and take each edge linear map to be $P_{i+1}^{-1}P_i$, with affine constants zero. The product telescopes to the identity and identifies each outgoing normal with minus the next incoming normal. Exponentiation gives the elliptic identifications and dual-normal maps of the defined marked cycle. Its normal sum is $u=2\pi i(-a,b)$ and its primitive divisor is $\gcd(a,b)$; the real period $(A,B)$ cannot contribute to a purely angular vector.

For $0<|t|<1$, put $\ell_t=\log|t|$. In the real coordinate order
$(\operatorname{Im}z/(2\pi),\operatorname{Im}w/(2\pi),\operatorname{Re}z,\operatorname{Re}w)$,
the first two angular periods are the first two unit vectors. The determinant of the four periods is therefore exactly
\[
 \det\begin{pmatrix}A&-a\ell_t\\ B&b\ell_t\end{pmatrix}
       =\ell_t(bA+aB)>0.
\]
The normalization of these real coordinates accounts for the two factors $2\pi$ in the angular periods. The constant cycle translation is zero in this example. In an all-ruled cycle, changing normal-product constants adds only vectors in the common normal line, so the projection of the cycle translation to its elliptic quotient remains the prescribed one, as proved in \cref{cdp:st:C.2.UN.57}. The compact realization of every mixed example follows from \cref{cdp:st:C.2.UN.48} with these same components and edge maps.
\end{proof}

'''

for suffix,s in [('_P326_replacement.tex',p326new),('_P329.tex',definition),('_P331.tex',period),('_P333.tex',moving),('_criterion.tex',criterion),('_UN48_replacement.tex',suspension),('_P332.tex',examples)]:
    assert Counter(re.findall(r'\\begin\{([^}]+)\}',s))==Counter(re.findall(r'\\end\{([^}]+)\}',s))
    (out/(stem+suffix)).write_text(s,newline='\n')
with (out/(stem+'_draft_aliases.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['old_tag','target_label','owner_tag','map'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(alias_maps)
REVIEWED=True
if not REVIEWED:
    print('15 DRAFT: receiving texts written; complete comparison and records remain pending.')
    raise SystemExit

# Exact main and remote guards.  The early owners and all five old statements
# must be admitted together, since equation identities move between them.
heading=r'\subsection{Marked cycle and tree constructions}\label{subsec:II:marked-cycle-tree-constructions}'
a=current.index(heading)
b=current.index(original[48],a)+len(original[48])
mainold=current[a:b]
assert mainold.count(original[46])==1 and mainold.count(original[48])==1
assert not re.search(r'\\begin\{proposition\}',mainold.replace(original[46],'').replace(original[48],''))
period=period.replace(r'\label{subsec:II:logarithmic-period-families}',r'\label{subsec:II:logarithmic-period-families}\label{subsec:II:marked-cycle-tree-constructions}',1)
nextheading=r'\subsection{Stars and weighted component constructions}\label{subsec:II:star-weighted-constructions}'+'\n\n'
mainnew=period+criterion+suspension+examples+nextheading
earlynew=p326new+'\n\n'+definition+moving
remotes=[dict(statement_id='lem:II:normal-product-collars',old_text=p326old,new_text=earlynew,reason='Full P326 branch-labelled extension, followed immediately by complete P329/P333. Both new owners precede UN41 and all later cycle consumers. Admit with the main fragment and the three removals to move each original equation target exactly once.')]
for n in [51,55,57]:
    assert current.count(original[n])==1
    remotes.append(dict(statement_id=f'cdp:st:C.2.UN.{n}',old_text=original[n],new_text='',reason='The full statement identity, all hypotheses/conclusions and every formula target are transferred to the common owners, the consolidated criterion, UN48 or P332 in this same atomic package. The separate repeated proof is removed.'))
before=mainold+p326old+''.join(original[n] for n in [51,55,57])
after=mainnew+earlynew
assert Counter(used)==Counter(equations.keys()), (Counter(used)-Counter(equations.keys()),Counter(equations.keys())-Counter(used))
for k in ['label','hypertarget']:
    pat=r'\\'+k+r'\{([^}]+)\}'
    x=Counter(re.findall(pat,before));y=Counter(re.findall(pat,after))
    assert all(y[key]==count for key,count in x.items()),[(key,x[key],y[key]) for key in x if x[key]!=y[key]]
    assert max(y.values())==1
for s in [mainnew,earlynew]:
    assert Counter(re.findall(r'\\begin\{([^}]+)\}',s))==Counter(re.findall(r'\\end\{([^}]+)\}',s))
    assert not re.search(r'\\tag\{|\(C\.[A-Z]+\.|\\path\{|\.py\b|\r|night:P4R\.13|night:P4\.40',s)
    assert not any(re.search(r'\n[ \t]*\n',m.group()) for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',s,re.S))
assert current.count(mainold)==1 and current.count(p326old)==1

newdisplays={lab:m.group() for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',after,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
alias_lookup={r['old_tag']:r for r in alias_maps}
def math_payload(s):
    s=re.sub(r'\\SsixEquationAliases\{\\label\{[^}]+\}\}','',s)
    s=re.sub(r'\\tag\{[^}]+\}|\\hypertarget\{[^}]+\}\{\}|\\label\{[^}]+\}','',s)
    for word in [r'\[',r'\]',r'\begin{equation}',r'\end{equation}']:s=s.replace(word,'')
    return re.sub(r'\s+','',s)
payloads=[]
for key,old_eq in equations.items():
    label=established[key];receiving=newdisplays[label]
    if key in alias_lookup:
        payloads.append(dict(old_tag=key,target_label=label,result='Exact scope-preserving formula alias',map=alias_lookup[key]['map']))
        continue
    comparison=receiving
    if key=='C.HC.1':comparison=comparison.replace('G_i=V_i','G_i=H_i')
    if key=='C.HC.3':comparison=comparison.replace('V_i','H_i').replace('V_{i+1}','H_{i+1}')
    if key in ['C.HC.6','C.HC.9']:comparison=comparison.replace('_N',r'_\ell')
    if key in ['C.HC.8','C.HC.10']:comparison=comparison.replace(r'\widehat\Lambda(t)',r'\Lambda(t)')
    if key in ['C.MX.1','C.MX.3']:comparison=comparison.replace(r'\mathcal L_i','L_i')
    assert math_payload(old_eq)==math_payload(comparison),key
    payloads.append(dict(old_tag=key,target_label=label,result='Formula payload preserved under declared variable identity',map='Identity formula; H_i=V_i on Hopf vertices, old cycle length ell=N, old ruled line L_i=mathcal L_i, and old full rank-four Lambda(t)=widehat-Lambda(t) where applicable.'))

def part(s,start,end=None):
    i=s.index(start);j=s.index(end,i) if end else len(s)
    return s[i:j]
def proof(s):return part(s,r'\begin{proof}')
dest_by_n={46:definition+moving+criterion,48:criterion+suspension+examples,51:definition+moving+criterion+suspension+examples,55:period+criterion,57:definition+moving+period+criterion}
destloc={46:'P329/P333 and subsec:II:marked-cycle-criterion',48:'Marked-cycle criterion, elliptic-suspension subsection and P332',51:'P329/P333, marked-cycle criterion, UN48 and P332',55:'Logarithmic-period and marked-cycle-criterion subsections',57:'P329/P333, logarithmic-period and marked-cycle-criterion subsections'}
rows=[]
def log(kind,owner,oldtext,newtext,reason,where='',newwhere=''):
    rows.append(dict(change_id=f'II-C3-CYCLES15-{len(rows)+1:04d}',type=kind,statement_id=owner,old_location=where or owner+' complete original source',old_page='Exact source span supplied; previous PDF page omitted',new_location=newwhere or 'Early P326/P329/P333 and section10 cycle units',new_page='Pending integrated final PDF',old_text=oldtext,new_text=newtext,reason=reason,review_status='Complete original and receiving proofs read and compared; exposed editorial rereading. No independent proof or computational execution credit; final PDF open.'))

for n in [46,51,55,57]:
    log('D12',f'cdp:st:C.2.UN.{n}',original[n][:original[n].index(r'\begin{proof}')],criterion[:criterion.index(r'\begin{proof}')],'Consolidates the four complete cycle criteria in the strongest proved scope. Keeps every original permanent tag and statement label as a simultaneous owner identity. Preserves the all-ruled full translation and one-normalization case, the a=0 actual-fibre cycle conclusion, the exact one/two-Hopfs exclusions and inversion maps, all secondary groups, and the compact conjugate-fibre realization. The separate elliptic-suspension construction remains at UN48.',newwhere='subsec:II:marked-cycle-criterion')
log('D12','cdp:st:C.2.UN.48',original[48][:original[48].index(r'\begin{proof}')],suspension[:suspension.index(r'\begin{proof}')],'Retains the distinct elliptic-suspension realization and includes the already proved mixed Hopf/ruled specialization from UN51. Every Hopf component still has algebraic dimension zero, at least one is present, M=I, and all marked component/elliptic maps remain. The explicit examples move to their numbered owner P332.',newwhere='subsec:II:cycle-elliptic-suspensions')

# Map each original mathematical proof block to its complete receiving owner.
blockmap={
46:[definition+part(criterion,'For the asserted SNC Hopf branch'),part(definition,'Each edge is a biholomorphism'),part(moving,'Each marked curve', 'On a ruled complement'),part(moving,'On a ruled complement','Suppose $M=I$'),part(moving,'Suppose $M=I$','For the moving construction'),part(criterion,'For two Hopf components')],
48:[part(criterion,'Assume $M=I$','Apply \\cref{lem:II:logarithmic-period-family}')+part(suspension,'Use the common lattice','The nodal cubic'),part(suspension,'The nodal cubic','Transport every $n_i$'),part(moving,'For the moving construction')+part(suspension,'Transport every $n_i$','Replace the distinguished tube'),part(suspension,'Replace the distinguished tube')+examples],
51:[definition+part(moving,r'\begin{proof}','For the moving construction'),part(criterion,'Assume $M=I$','Apply \\cref{lem:II:logarithmic-period-family}'),part(moving,'For the moving construction')+suspension,part(criterion,'The real quotient','Apply \\cref{lem:II:logarithmic-period-family}')+part(examples,'For the mixed examples')],
55:[part(criterion,'The real quotient','Apply \\cref{lem:II:logarithmic-period-family}'),period,part(criterion,'At zero apply','At infinity put'),part(criterion,'At infinity put','Glue the two fillings'),part(criterion,'Glue the two fillings','For the asserted SNC Hopf branch')],
57:[definition+part(moving,r'\begin{proof}','For the moving construction'),part(criterion,'Assume $M=I$','Apply \\cref{lem:II:logarithmic-period-family}'),period,part(moving,'For the moving construction')+part(criterion,'At zero apply','At infinity put'),part(criterion,'At infinity put','For the asserted SNC Hopf branch')]
}
block_titles={}
for n,s in original.items():
    matches=list(re.finditer(r'\\par\\medskip\\noindent\\textbf\{([^}]+)\}',s))
    assert len(matches)==len(blockmap[n]),(n,len(matches),len(blockmap[n]))
    spans=[]
    for i,m in enumerate(matches):
        a=m.start();b=matches[i+1].start() if i+1<len(matches) else s.index(r'\end{proof}',a)
        source=s[a:b];dest=blockmap[n][i];spans.append((a,b,dest,m.group(1)))
        log('D12',f'cdp:st:C.2.UN.{n}',source,dest,'Transfers this complete mathematical block to the indicated general owner or its exact map application. The original and receiving block were both read in full. All hypotheses, maps, lattice generators and conclusions are compared in the owner-transfer table; construction-only specializations retain their own full realization proof.',where=f'UN{n} proof: {m.group(1)}',newwhere=destloc[n])
    block_titles[n]=spans
    for idx,m in enumerate(re.finditer(r'\S[\s\S]*?(?=\n\s*\n|\Z)',s)):
        p=m.group();pos=m.start()
        if p.startswith(r'\StatementRecord'):continue
        found=next((v for lo,hi,v,title in spans if lo<=pos<hi),dest_by_n[n][:dest_by_n[n].index(r'\begin{proof}')])
        if re.search(r'\bactual\b|\bretained?\b|\bsaved\b|\bcertified\b|\bchecks?\s+\d',p,re.I):
            log('D08',f'cdp:st:C.2.UN.{n}',p,found,'States the named surface, inclusion, lattice or gluing map directly at its mathematical owner. Marking-preservation assertions remain precise morphism statements; program/run vocabulary is removed.',where=f'UN{n} original paragraph {idx+1}',newwhere=destloc[n])
        if re.search(r'rather than|not merely|not just|without (?:discarding|suppressing|asserting)|does not replace|no holomorphic|no restriction on|no elliptic quotient|no inequality|not only its leading',p,re.I):
            log('D02',f'cdp:st:C.2.UN.{n}',p,found,'Replaces defensive contrasts by the proved domain and explicit coordinate/period comparison. The general algebraic-dimension scope is stated once positively in P329; the complete family maps and affine translations remain proved.',where=f'UN{n} original paragraph {idx+1}',newwhere=destloc[n])
        if re.search(r'\(C\.[A-Z]+\.[0-9]+\)',p):
            log('D04',f'cdp:st:C.2.UN.{n}',p,found,'Replaces the printed inherited equation identifiers by numbered equation or common-owner references. Every former equation target is preserved and listed in the old-tag map, including exact aliases.',where=f'UN{n} original paragraph {idx+1}',newwhere=destloc[n])
        if r'\path{' in p or re.search(r'12,180|1,376|169 mixed cycles',p):
            log('D09',f'cdp:st:C.2.UN.{n}',p,found,'Moves the program citation to the exact plain-path appendix rows in provenance addition162. The input matrices, normal-vector list, finite weights, determinant, gcd and family maps remain in numbered mathematical owners; saved-output and sample-count claims are removed. No execution is credited.',where=f'UN{n} program paragraph {idx+1}',newwhere='Appendix addition162; P331, P332, UN48 and UN57 mathematical scopes')

for key,oldeq in equations.items():
    label=established[key];new_eq=newdisplays[label]
    reason='Uses the section equation counter with the same permanent target and label. '
    reason+=alias_lookup[key]['map'] if key in alias_lookup else 'The complete formula payload is unchanged under the explicitly recorded identities H_i=V_i, ell=N, ruled L_i=mathcal L_i or full rank-four Lambda(t)=widehat-Lambda(t), where applicable.'
    log('D19',label,oldeq,new_eq,reason,where='Inherited display '+key,newwhere='Receiving owner of '+label)
log('D13','def:II:marked-normal-cycle',original[51][:original[51].index(r'\end{proposition}')],definition,'Places the complete common data in one numbered Definition, with its proof of the rank-three lattices, primitive normal periods, entire line charts and affine edge lifts. The identity map V_i=H_i in the Hopf case and V_i=R_i in the ruled case identifies every earlier domain.')
log('D13','ex:II:three-hopf-cycle',part(original[48],'For example there is a three-component',r'\end{proposition}'),examples,'Extracts the explicit three-cycle, secondary divisibility and mixed normal-vector families as one numbered example with every calculation and map. The generic realization theorem no longer carries an example in its statement.')
log('D14','sec:II:10',mainold,mainnew,'Orders the section10 receiving units as logarithmic periods, the complete criterion, the distinct elliptic suspension and explicit examples. Keeps the old marked-cycle-tree boundary label as an alias on the period subsection and creates a following open stars/weighted unit. The enclosing section remains open on the remaining statements.')
log('D14','subsec:II:marked-cycle-lattices','',definition+moving,'Places P329/P333 immediately after the earlier P326, before the first UN41 application. Their only internal premises are P326 and P329; no section10 criterion or later occurrence theorem is used. This resolves the common construction before all consumers.')
log('D25','lem:II:normal-product-collars',p326old,p326new,'The previous owner states only simple normal crossings, while the cycle criteria also include identifying two sections of one ruled normalization. Adds exactly the normal-crossing domain with two globally labelled inverse curves mapping isomorphically to each double curve. Those labels glue the local branch germs to smooth Cartier divisors on a neighbourhood; normalization identifies their normal lines and the compact regular cores. The original SNC statement and all collar/product/transport conclusions remain unchanged.')
log('D12','lem:II:normal-product-collars',part(original[46],'\\item For an arbitrary actual smoothing',r'\item If the given'),part(moving,'For a given smoothing','Suppose $M=I$'),'The full smooth retraction/divisor-section argument already belongs to P326. P333 applies its original SNC clause or its proved labelled-branch clause to exactly the given double curves and normalization cores; the same van Kampen homomorphisms result.')
log('D25','cdp:st:C.2.UN.57',part(original[57],'For an arbitrary specified smoothing','\\item Conversely'),part(criterion,r'\begin{proof}','Assume $M=I$'),'Makes the given-smoothing comparison explicit: the induced normal-product trivialization divided by the specified one is a holomorphic unit on a compact elliptic curve, hence a scalar. P329 proves that this scalar does not change M. Thus the necessary criterion applies to the specified support without identifying distinct trivializations.')
log('D20','def:II:marked-normal-cycle',equations['C.MX.1']+equations['C.MX.3'],newdisplays['cdp:eq:C.MX.1']+newdisplays['cdp:eq:C.MX.3'],'Uses mathcal L_i for the same ruled line bundle and L_i for the edge linear map. The isomorphism is the identity on the original line bundle, its total space and projective completion.')
log('D20','lem:II:moving-marked-cycle',equations['C.HC.8']+equations['C.HC.10']+equations['C.HG.11'],newdisplays['cdp:eq:C.HC.8']+newdisplays['cdp:eq:C.HC.10']+newdisplays['cdp:eq:C.HG.11'],'Uses widehat-Lambda(t) for the same full rank-four nearby torus lattice and Lambda(t) for the same moving rank-three core lattice. Their inclusion and added cycle generator are exactly HC10/HG11; no coordinate or subgroup is changed.')
log('D20','lem:II:moving-marked-cycle',part(original[55],'Choose logarithmic',r'\par\medskip') if 'Choose logarithmic' in original[55] else equations['C.TL.2'],part(moving,'This construction also permits',r'\end{lemma}'),'Uses bold b_i for common vector edge constants, leaving scalar b_i(t) as the ruled line-factor logarithm of MX10. The edge sum b(t)=sum bold b_i(t) and exponent exp b_i(t) identify the two quantities explicitly.')
log('D17','cdp:st:C.2.UN.48',part(original[48],'The section translation by','\\item  The analytic Tate'),part(suspension,'The resulting $J$ is smooth','Pull back the exact nodal Tate'),'Replaces the obsolete reference to repeated minimal-graph extension proofs by the freshly opened primary theorem in Schutt–Shioda arXiv v3 Definition3.1 p7 and section7.6 pp33–34. The receiving J is the same smooth projective relatively minimal elliptic model and P the same section, so the published extension gives exactly its translation and inverse.')
log('D18','cdp:st:C.2.UN.48',next(l for l in original[48].splitlines() if l.startswith(r'\StatementRecord')),next(l for l in suspension.splitlines() if l.startswith(r'\StatementRecord')),'Records the exact opened arXiv v3 version, definition and section/page scope for the translation application. The central bibliography already pins this version; source-wide review remains open.')
log('D22','ex:II:three-hopf-cycle',part(original[51],'The exact examples and moving-frame comparisons',r'\end{enumerate}'),part(examples,'For the mixed examples'),'Supplies all previously implicit mixed-family inputs: a copies of the first angular normal and b copies of the negative second, A,B<0 with irrational ratio, the two changing Hopf frames, all repeated ruled frames, edge product, normal sum and primitive gcd.')
log('D25','ex:II:three-hopf-cycle',part(original[51],'Their primitive cycle divisor is','The same calculation'),part(examples,'For $0<|t|<1$'),'Makes the determinant convention exact: the full four-period determinant has this value in coordinates (Im z/(2pi), Im w/(2pi), Re z, Re w). The two angular periods become unit vectors, leaving the displayed two-by-two determinant ell_t(bA+aB). This states the missing coordinate normalization and preserves the original scalar formula with A=log|alpha|, B=log|beta|.')
log('D11','cdp:st:C.2.UN.46',part(original[46],'The constants in $\\theta_i$','\\end{enumerate}'),criterion[:criterion.index(r'\begin{proof}')],'States the distinction between the prescribed local normal-product constants and the compact construction choices once in the theorem: local HC9/HC10 keeps them all, while the compact construction preserves components/gluing and chooses those constants. Removes the closing repeated scope paragraph.')

def tsv(suffix,fields,data):
    with (out/(stem+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
for suffix,s in [('_input.tex',mainold),('_replacement.tex',mainnew),('_early_replacement.tex',earlynew),('_P331.tex',period)]:
    (out/(stem+suffix)).write_text(s,newline='\n')
with (root/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',fields,rows)
tsv('_remote_repairs.tsv',['statement_id','old_text','new_text','reason'],remotes)
tsv('_equations.tsv',['old_tag','target_label','statement_id'],[dict(old_tag=key,target_label=established[key],statement_id='Receiving owner recorded in formula map') for key in equations])
tsv('_formula_comparisons.tsv',['old_tag','target_label','result','map'],payloads)

maps=[
('UN46/UN51/UN57 complement and affine-edge definitions','P329','One marked normal cycle, including primary/secondary Hopf and ruled components, and its integral M.','Vi=Hi or Ri; mathcal Li is the same former ruled Li. The logarithmic exponentials, constant line factors, phi_i and theta_i are unchanged. Hopf incoming/outgoing axes and ruled zero/infinity sections give the same primitive meridians; ell=N only renames cycle length.'),
('UN46/UN51/UN55/UN57 full finite plumbing and pi1 arguments','P333 before UN41','Proper smooth normal-product filling, same given-smoothing pi1, closed coframe, full affine period quotient.','The same normal lines/phi/theta, disjoint cores, xy=t necks and r0<R0 overlaps give the same quotient. Expanded r1/R1/closed-subdisc cover proves properness. P326 maps the given smoothing to these same branch-labelled collars. Core loops and the cycle generator give Lambda semidirect M Z; the coframe orbit map gives the full rank-four lattice, now widehat-Lambda.'),
('P326 original simple-normal-crossing scope','P326 original clause plus labelled normalization clause','The same smooth product collar and core maps for a single ruled normalization with its two sections identified.','The two inverse curves each map isomorphically to C, so label the branch germs and glue them to smooth Cartier divisors B1,B2 on a neighbourhood N. nu is biholomorphic near each inverse branch and away from double curves, identifying both normal lines and the compact cores. The same Psi=(r,s1,s2) derivative and horizontal transport apply.'),
('UN48/UN51/UN55/UN57 moving lattices and punctured comparisons','P333 moving clause','Holomorphic families preserving every central marked component and finite character, with the complete period b(t)+(log t)/(2pi i)u(t).','Transport every lattice vector by its fixed integer coefficients. Hopf frames are (n_i/(2pi i),-n_(i-1)/(2pi i)); ruled frames instead use a transverse integral lift and n_i. Finite angular relations stay identical. Bold b_i denotes the common vector edge constant; scalar b_i in MX10 remains its line factor. Piecewise logarithmic maps subtract the same accumulated constants and have holomorphic fibrewise inverses.'),
('UN55 period proof and UN57 repeated determinant/frame application','P331','Smooth proper C* family with all full periods, determinant and frame at infinity.','The same V_z(w)=w+zJ conjugate(w), inverse, N>0, Lambda basis and b=(sigma,i). The determinant is in (Re w1,Im w1,Re w2,Im w2), with no rescaling. UN57 uses N=d; old W_s is exactly V_s^infinity. All-ruled d=N follows from the primitive n and u=-Nn.'),
('UN46/UN51/UN55/UN57 complete theorem statements','Consolidated UN57 with all four tags','Necessary and sufficient local and compact marked-cycle criterion; all class-specific conclusions retained.','All hypotheses are the union already proved by UN57 plus UN46/UN51 special conclusions: M=I, arbitrary algebraic dimension, secondary groups, full elliptic translation, one ruled self-identification, at least two Hopf vertices, actual a=0 SNC fibres form cycles, and exact two-copy inversion. The sole Hopf self-gluing has nonidentity HC5. Scalar normal-dual ratios on compact elliptic curves leave M unchanged.'),
('UN48/UN51 common normal sign calculation','UN57 normal-period paragraphs','u=-sum n_i is transverse to W, has primitive divisor d>0 and gives an elliptic quotient.','At Hopf vertices apply ell to the identical contracting logarithm P_i(log alpha_i,log beta_i); both negative real logs imply one nonzero sign. Ruled ni=ni-1 propagates it, and the all-ruled elliptic quotient excludes vanishing. HG3/HG5 together give every clause of former MX7.'),
('UN55/UN57 compact period fillings at zero and infinity','UN57 applications of P331/P333','Specified marked support at zero and its conjugate support at infinity, preserving full elliptic maps.','At zero use lambda_j(z)=V_z lambda_j and bold b_i(z)=V_z bold b_i. At infinity use W_s=J conjugation+s identity, lattice W_s Lambda, outgoing -W_s n_i and constants W_s bold b_i. Hopf frames satisfy AD11; ruled transverse lifts are also negated, giving the same J-conjugate frame. Edge-coordinate constants conjugate by (J bar P)^-1 J bar b=bar(P^-1b). The exact eta/z frame glues the two punctured families.'),
('UN48 all-Hopf and UN51 mixed elliptic suspension','UN48 full mixed receiving realization','A distinct compact realization by replacing one tube in (C* times J)/<(b,y)->(q0b,y+P)>.','Same primitive p, linear coordinates X,Z, q0 and a. The HG7 embedded elliptic curve proves a!=1. Apply UN41 pencil/Tate construction to the exact nodal point HG8, pull back along s^d, retain every xy=s^d resolution chart and set t=s(Q/s^d)^(1/d). Fresh SS v3 applies to that same projective relatively minimal J/P. Fixed integer lattice transport and two independent adjacent normal constants solve b0=0. The exponential map [(X,Z)]->[(exp X,[exp Z])] identifies exactly HG11 with the suspension; P333 supplies the complete punctured map.'),
('UN46 two-component matrix and quotient proof','UN57 final paragraph','Exact isomorphism of the two Hopf surfaces and simultaneous inversion gluing.','HC11=I gives both Li=-S0, Lambda2=-S0 Lambda1, Gamma2=S0 Gamma1. Coordinate exchange descends including the finite group; the commuting diagonal automorphism (a^-1 Z,b^-1 W) sends a/z,b/w to inversion. All local theta constants remain in HC9/HC10.'),
('UN48 examples and UN51 program-paragraph mathematics','P332','Three primary/secondary Hopf cycle, finite divisor k gcd(n,a+b), and all two-Hopf/ruled-insertion families.','Retains all HG1/HG15/HG16 matrices, contractions, finite weights and composite (t^-2,t^2). Angular line intersection uses n|j(a+b) and gcd(a,n)=1. The mixed input is a copies of (1,0), b copies of (0,-1), with common real contraction (A,B); the two changes are Hopf and repeats ruled. The full determinant is computed in the stated normalized angular coordinates, with ell_t(bA+aB)>0.'),
]
tsv('_owner_transfers.tsv',['old_owner','new_owner','conclusion','map'],[dict(zip(['old_owner','new_owner','conclusion','map'],r)) for r in maps])
deps=[
('P329','Opened Abasheva–Deev v1 section2.2.7–2.2.9 p5','Same degree-zero elliptic line and exact constant factors; no body construction premise.','Ready; placed immediately after P326.'),
('P333','P326 and P329','The full reduced fibre has two labelled inverse curves over every double curve; all entire normal charts and integral affine maps come from P329.','Ready; both inputs precede P333. UN41 can apply it without a forward premise.'),
('UN41','P329/P333','Two Hopf copies, second ordered (W,Z), edge matrix -swap twice; composite (-log t,log t) generates the same DH10 cycle subgroup. The second-core maps differ by (t,t^-1); moving case pulls back by the inverse of tau=Q(t).','Provenance owns the complete UN41 receiving guard and has read the settled owners. This remote consumer integration remains a separate D12 gate until admitted.'),
('UN57 merged criterion','P329/P333, P331, UN40, P327/P248','Same marked data; actual normal-product ratios are constant. P331 is used with N=d; P333 with V_z and with W_s at infinity.','Local ordering complete: the common owners are early, P331 immediately precedes the criterion, and UN40 precedes the cycle unit.'),
('UN48','UN57, P333, UN41 pencil/Tate construction, opened Schutt–Shioda v3','Same lattice and marked components, exact HG8 smooth nodal point and s^d pullback; same J/P for translation extension.','Local order complete. UN41 already precedes section10; provenance publication pass is coordinated independently.'),
('P332','UN57 and UN48','The exact normal vectors, matrices, finite groups and affine constants meet those two complete realization statements.','Local order complete; all formula inputs and resulting determinants are displayed.'),
('Section10 remaining stars/weighted/trees','The current UN49 onward, with cycle duplicates removed and admitted UN54/P337 and UN61/P330 deltas preserved','Following stable subsection label subsec:II:star-weighted-constructions.','Open; no all-class completion or final full-section placement claim.'),
]
tsv('_dependencies.tsv',['consumer','input','map','status'],[dict(zip(['consumer','input','map','status'],r)) for r in deps])

now=datetime.now(timezone.utc).isoformat()
event_defs=[
('cdp:st:C.2.UN.46','UN46','_criterion.tex','Read the entire original and receiving statement/proof. Compared its cycle formation, affine edge maps, finite secondary groups, finite proper plumbing, full given-smoothing collar argument, injected semidirect product, coframe/flow quotient, exact affine periods and one/two-component calculations. All old identities survive at P329/P333/UN57. The coordinate exchange and diagonal automorphism are retained explicitly.'),
('cdp:st:C.2.UN.48','UN48','_UN48_replacement.tex','Read the entire original and receiving statement/proof and the full current proposed UN41 input. Preserved all HG6–14 maps: primitive-lattice coordinates, HG7 embedded curve, exact nodal point, every xy=s^d resolution chart and overlap, identity-component section, Q=t^d root coordinate, compact suspension, same four periods, both sorts of moving frames, the two independent normal-constant equations, entire punctured-family map/inverse, nested-annulus replacement and every support Euler calculation. Added the explicit exponential quotient map. Freshly opened SS v3 Definition3.1 p7 and complete section7.6 pp33–34 before its exact J/P translation application.'),
('cdp:st:C.2.UN.51','UN51','_criterion.tex','Read the entire original mixed-cycle statement/proof and all receiving owners. The ruled whole-line charts, opposite primitive meridians, mixed local criterion, ni=ni-1, exclusion of exactly one Hopf vertex, sign propagation, primitive quotient, a!=1 and mixed elliptic-suspension realization all retain their exact maps. The separate ruled moving frame is preserved at P333, avoiding the dependent Hopf columns. Full all-ruled translation and one-section-pair identification remain. The program-paragraph mixed inputs and determinant now have their complete P332 proof.'),
('cdp:st:C.2.UN.55','UN55','_criterion.tex','Read the entire original all-ruled statement/proof and all receiving P331/P333/UN57 text. The actual lattice coordinate isomorphism, primitive p=-n, arbitrary horizontal sigma, V_z inverse and positive determinant, all four periods, exact zero and infinity frame maps, both proper fillings and compact finite closed refinement are preserved. N=number of ruled vertices equals d; the general conjugate filling gives the required second N-component ruled cycle. The one-normalization case uses the proved P326 labelled-branch clause.'),
('cdp:st:C.2.UN.57','UN57','_criterion.tex','Read the entire original and consolidated receiving statement/proof. Preserved every primary/secondary marked component, arbitrary algebraic dimension, all affine/finite data and the compact conjugate-support conclusion. Verified the common normal sign, exact W=C times R coordinate map, permitted normal-constant change, N=d period application, integer transport at zero, both Hopf and ruled conjugate frames at infinity, conjugation of each affine edge map, complete punctured isomorphisms and proper compact gluing. All four previous statement tags/labels now belong to this same complete criterion.'),
('lem:II:normal-product-collars','P326','_P326_replacement.tex','Read the complete original and receiving P326. The SNC statement is unchanged. The added domain has exactly two globally labelled inverse curves over each double curve. Their germs glue to smooth Cartier divisors B1/B2 on a neighbourhood, and normalization gives biholomorphic branch neighbourhoods and normal-line derivatives. The same Psi=(r,s1,s2) has identity tangential and invertible transverse derivative, preserves f=xy, and gives the circle reversal. Normalization is an isomorphism on the compact regular cores, where the same horizontal right inverses and radial flows give mutually inverse transports.'),
('def:II:marked-normal-cycle','P329','_P329.tex','Read the full receiving definition/proof against all five originals. Verified entire Hopf/ruled normal-line charts, free finite diagonal quotient, full rank-three lattice, primitive angular normals, constant-factor line presentation, affine elliptic lift and periodic derivative, theta scalar independence and equivalence M=I iff L=I. Freshly read the complete primary page5 of Abasheva–Deev v1, including sections2.2.6–2.2.9, for the used exact forms. Ruled mathcal L_i and edge L_i now denote different objects explicitly.'),
('lem:II:logarithmic-period-family','P331','_P331.tex','Read the complete receiving statement/proof against full UN55/UN57. Checked the Hermitian norm identity and real determinant, inverse V_z, exact fourth-vector determinant in the stated real coordinate order, positivity for every r>0, uniformly bounded lattice matrices and closed parallelepipeds, monodromy P4->P4+NP3 and the eta/z frame at infinity. All old TL/AD targets are unchanged or explicitly aliased with N=d and W_s=V_s^infinity.'),
('lem:II:moving-marked-cycle','P333','_P333.tex','Read the complete receiving statement/proof against the full original plumbing, coframe and moving-family arguments. Checked the flat norm, disjoint open ends, closed gluing graphs, expanded r0<r1<R1<R0 compact-cover proof, connectedness, injected lattice semidirect product, exact P326 application, complete commuting flows and all period generators. For moving data, both lattice frame types, finite integer characters, contraction openness, uniform properness and entire punctured maps/inverses are proved. Bold edge vectors, scalar line-factor logarithms and rank-three/rank-four lattices are distinguished. Provenance separately read this owner for its UN41 specialization; no independent proof credit is asserted.'),
('ex:II:three-hopf-cycle','P332','_P332.tex','Read the complete receiving example/proof against full UN48 and the UN51 final computational paragraph. Compared all three frames/contractions/matrices, composite (t^-2,t^2), finite weights modulo5, line-intersection gcd and repeated-cycle divisor. Read the entire pinned A_mixed_cycles.py source without executing it; its a/b normal list, two changes, repeated ruled vertices, common period and exact two-by-two determinant are now stated with the corresponding normalized four-dimensional coordinate order. Program counts and body paths are removed to appendix162.'),
]
events=[]
for statement,key,suffix,text in event_defs:
    events.append(dict(statement_id=statement,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',outcome=text+' Exposed editorial comparison only; no independent proof or computational execution credit. No refined P4R.13/P4.40 use occurs. Final integrated PDF pages remain unread.',event_id='publish:c3:conductor15:'+key,phase='publication editorial comparison',source_file='agents/continuation3_conductor/'+stem+suffix,source_row='',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor15:marked-cycles',publish_input_file='',publish_input_row='',date_utc=now,where='Complete original/receiving cycle units and bounded early-owner transfer'))
tsv('_CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where'],events)

units=[('subsec:II:normal-product-collars','Smooth normal-product collars'),('subsec:II:marked-cycle-lattices','Marked cycles and their integral lattices'),('subsec:II:moving-marked-cycles','Proper normal products and moving lattices'),('subsec:II:logarithmic-period-families','Logarithmic period families; preserves marked-cycle-tree-constructions label'),('subsec:II:marked-cycle-criterion','The marked-cycle criterion'),('subsec:II:cycle-elliptic-suspensions','Elliptic suspensions realizing marked cycles'),('subsec:II:explicit-marked-cycles','Explicit Hopf and ruled cycles'),('subsec:II:star-weighted-constructions','Stars and weighted component constructions')]
statuses=[]
for unit,title in units:
    for c in [f'D{i:02}' for i in range(1,26)]+['structure']:
        state='done';reason='Complete original and receiving unit compared across all25 classes; every local instance found is repaired in the exact per-instance rows and owner maps.'
        if c in ['D10','D16']:reason='Prior done status preserved; every old tag and label remains and all new owners have mathematical titles.'
        elif unit=='subsec:II:star-weighted-constructions':state='open';reason='Following UN49-onward star/weighted/tree work remains open. The cycle duplicates have moved; admitted UN54/P337 and UN61/P330 changes remain untouched.'
        elif c in ['D14','structure']:reason='Local ordering and actual subsection structure complete. P329/P333 immediately follow P326 before UN41; P331 precedes the criterion, then UN48 and P332. The remaining section10 unit and whole-paper final order remain separately open.'
        elif c=='D12' and unit in ['subsec:II:marked-cycle-lattices','subsec:II:moving-marked-cycles']:state='open';reason='The five local cycle proofs are consolidated completely. The full earlier UN41 application is prepared by provenance and remains an external admission gate; no global duplicate-proof closure is claimed until it is integrated.'
        elif c=='D18':state='open';reason='Exact primary versions/loci were freshly read and recorded; source-wide bibliography review remains a separate gate.'
        elif c=='D23':state='open';reason='Source environments and equation-alias paragraph breaks are checked; final integrated PDF page inspection remains open.'
        elif c=='D24':state='open';reason='The body owner/heading changes are complete, but the whole-paper results list and organization must be reconciled by root with the final integrated structure.'
        elif c=='D19':reason='All57 inherited displays use the section counter with every label/target preserved. Exact formula identities and aliases, including renamed notation, are listed in the equation/comparison maps.'
        elif c=='D25':reason='Complete inference comparison performed. The one-normalization collar domain, induced-versus-chosen normal-product scalar map, separate ruled moving frame and full determinant-coordinate convention are explicit.'
        statuses.append(dict(unit=unit,title=title,criterion=c,status=state,reason=reason))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],statuses)

sources=[]
for key,url,version,locus,path,paraphrase in [
('AbashevaDeev-v1-cycle-lines','https://arxiv.org/pdf/2303.10764v1','arXiv:2303.10764v1,19March2023','Complete printed p5; sections2.2.6 and2.2.7–2.2.9','/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/AbashevaDeev2023_v1.pdf','Nonresonant diagonal Hopf curves are its axes; every degree-zero elliptic line has constant factors, and the two explicit line-coordinate descriptions are isomorphic. Used at P329 and the exact a=0 curve applications.'),
('SchuttShioda-v3-translation','https://arxiv.org/pdf/0907.0298v3','arXiv:0907.0298v3,9July2010','Definition3.1 printedp7; complete section7.6 printedpp33–34','/workspace/scratch/9fcd229a9ed4/tmp/c3_provenance_primary/SchuttShioda2010_arxiv_v3.pdf','The source defines smooth projective relatively minimal elliptic surfaces and states that translation by any section extends over singular fibres as an automorphism preserving the fibration. Applied to the exact resolved base-changed J and P in UN48.')]:
    data=Path(path).read_bytes()
    sources.append(dict(source_id=key,url=url,version=version,exact_locus=locus,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),own_paraphrase=paraphrase,reader='continuation3 conductor; exposed editorial source reading',date_utc=now,storage='Primary PDF read from temporary source cache; no PDF or extract added to checkpoint artifacts.'))
tsv('_primary_sources.tsv',['source_id','url','version','exact_locus','sha256','bytes','own_paraphrase','reader','date_utc','storage'],sources)

comparison='''# Package15 — marked-cycle consolidation

## Atomic admission and complete reading

The main replacement starts at the current marked-cycle-tree-constructions heading and replaces complete UN46 and UN48. The remote repair table replaces the complete P326 owner by its compared extension followed by P329/P333, and removes the full old UN51, UN55 and UN57 blocks. Admit all five guards atomically because57 equation identities move among the owners. All original labels and permanent targets have exactly the same multiplicities in the combined receiving text. No central file has been edited.

All five original statements and every complete proof were read, and all receiving P326/P329/P331/P333/UN57/UN48/P332 statements and proofs were read in full. The current proposed UN41 statement/proof was also read in full for its pencil/Tate input and common construction scope. The records credit exposed editorial comparison only. No mathematical program was executed and no independent check credit is claimed.

## Common construction and order

P329 owns the full marked data, line charts, rank-three lattices and affine edge derivation. It allows the one-normalization operation explicitly, preserves all finite angular characters and proves M=I equivalent to the complex product identity. Ruled line bundles are mathcal L_i; edge matrices are L_i, with the identity map between every former line-bundle notation and its receiving object.

P326 retains its original SNC statement and adds exactly the full reduced normal-crossing domain whose two inverse curves over each double curve map isomorphically to it. These maps label branch germs globally and glue them to two Cartier divisors on a neighbourhood. Normalization is biholomorphic near each branch and on the regular cores. Its derivatives give the same normal lines; the existing retraction/divisor-section map and horizontal transport then prove the product collars and all inclusion homomorphisms in this precise domain. This closes the domain needed for a single ruled normalization with its two sections identified.

P333 gives the complete fixed and moving construction. Its flat metrics, disjoint open ends, closed gluing graphs and expanded r0<r1<R1<R0 compact-cover argument prove a Hausdorff proper smooth total space. Connected cores and necks prove connectedness. The same lattice collar maps give an injected Lambda in the semidirect presentation. A closed coframe gives complete commuting flows and the exact orbit quotient; all core generators and the cycle generator give the entire lattice. The full rank-four lattice is now widehat-Lambda(t), with Lambda(t) reserved for the rank-three moving core lattice.

For moving data, every lattice vector keeps its fixed integer coefficients. Hopf vertices use the two independent angular normal vectors, including every finite relation and character. Ruled vertices use a transverse integral lift with their primitive normal; the dependent pair of opposite section normals is never used as a complex basis. The entire family of elliptic bases and degree-zero lines, and its projective completion, is constructed. Vector edge constants are bold b_i; scalar b_i(t) in MX10 remains the line-factor logarithm. Uniform metrics/cores prove properness. The logarithmic maps subtract accumulated edge constants, differ by the complete cycle period on the last overlap, and have holomorphic inverses on the entire punctured family.

P329/P333 stand immediately after P326, before UN41. Their only body prerequisites are P326 and P329. Provenance has read the settled common owners and prepares the complete UN41 specialization: use (z,w) on the first copy, (W,Z) on the second, and -swap on both edges. The composite period (-log t,log t) generates the same subgroup as DH10. The common second-core map (t/Z,1/W) differs from the retained old map (1/Z,t/W) by (t,t^-1), so they define the identical quotient map. Its moving case pulls back by the explicit inverse of tau=Q(t). That remote application remains an external D12 admission gate.

## Complete criterion and period realization

The four old theorem tags UN46/UN51/UN55/UN57 now belong to one complete criterion. Their full union of conclusions remains: arbitrary diagonal Hopf algebraic dimension and secondary groups, ruled vertices, the full elliptic translation, one ruled self-identification, necessity for every given smoothing, compact realization with precisely the conjugate marked fibre as its only other singular fibre, all support Euler numbers zero, at least two Hopf vertices, the a=0 unblown SNC fibre cycle classification, and the exact one/two-Hopfs cases. For a given smoothing its induced theta divided by the prescribed theta is a holomorphic unit on a compact elliptic curve and hence a scalar; P329 proves M is unchanged. This supplies the precise map from the given smoothing to the specified criterion.

The sign proof is owned once. Hopf contractions give HG4; ruled vertices give n_i=n_(i-1). The signs are nonzero, and u=-sum n_i is transverse to W. The primitive p gives W=(W intersect iW) direct-sum R p. The displayed complex linear map sends W to C times R and p to(0,1). A normal-product change fixes b's second coordinate at i while preserving the elliptic map. In the all-ruled case d=N and the horizontal sigma is unchanged.

P331 owns the full V_z family, its inverse, the exact real determinant, positive rank for every z in C*, the bounded-matrix proper quotient, monodromy and the eta/z frame at infinity. The criterion applies it with N=d. P333 at zero uses V_z on each fixed lattice vector and edge constant. At infinity it uses W_s=J conjugation+s identity, outgoing -W_s n_i and constants W_s b_i. The Hopf frames satisfy AD11. The ruled transverse lattice lift is also negated, giving the same J-conjugate frame. The explicit equation (J bar P)^-1 J bar b=bar(P^-1b) proves the conjugate elliptic gluing maps. The exact period maps then glue both proper fillings to the C* family over P1.

For two Hopf components HC11=I gives L1=L2=-swap and Lambda2=-swap Lambda1. Exponentiation, coordinate exchange and the commuting diagonal automorphism are retained verbatim as maps, including finite groups and both inversion gluings. The sole Hopf self-gluing has a transition with upper-left entry zero and cannot have identity product.

## Distinct elliptic suspension and exact examples

UN48 keeps the different elliptic-suspension realization and incorporates its full mixed specialization from UN51. The X,Z coordinate change sends the same primitive p and integral basis to HG6. The embedded elliptic curve HG7 proves a is not1 in the a=0 Hopf complement. HG8 gives the exact smooth nodal point; the full earlier UN41 pencil and Tate construction applies through that point and its group coordinate. Every xy=s^d resolution chart and overlap remains, as does the holomorphic root t=s(Q/s^d)^(1/d). Schutt–Shioda arXiv v3 Definition3.1 p7 and complete section7.6 pp33–34 were freshly opened before applying translation extension to the same smooth projective relatively minimal J/P.

The suspension quotient, compact annulus, all four periods and fixed integer transport are preserved. The two adjacent independent normal constants solve b0=0 without changing an elliptic gluing map. The exponential map [(X,Z)]->[(exp X,[exp Z])] identifies exactly the receiving additive quotient with the suspension: angular periods, its q0/a(t) generator and the t^d elliptic generator match one for one. P333 gives its complete punctured-family map and inverse. The nested-annulus replacement and the elliptic-base bundle Euler calculation at every remaining value are retained.

P332 owns all explicit examples. HG1/HG15/HG16 retain the three contraction pairs, matrices, normal vectors and composite(t^-2,t^2). The finite line-intersection proof gives k gcd(n,a+b), including the weights modulo5 and their exact component transforms. The previously undefined mixed counts are now the normal list of a copies of(1,0), then b copies of(0,-1), with common real contraction(A,B). Its two changes give two Hopf vertices and repetitions give a+b-2 ruled vertices. The telescoping frame product gives M=I; the normal sum gives gcd(a,b). The determinant formula is stated in normalized angular coordinates, so its value ell_t(bA+aB) is the exact four-period determinant in that coordinate order. The pinned A_mixed_cycles.py source was read in full, without execution. The four program citations and all saved-output/count claims move to the prepared appendix162 rows; their mathematical computations remain proved here.

## Status

The actual receiving units are smooth collars, marked lattices, moving normal products, logarithmic periods, the criterion, elliptic suspensions and explicit examples. Their local ordering and restructuring are complete. The new following stars/weighted unit, and the enclosing section10 remainder, stay open. D10/D16 remain done. D18 is open for the source-wide gate, D23 for final integrated pages, and D24 for final results-list/organization reconciliation. P329/P333 D12 stays open solely for provenance's separate earlier UN41 application admission. No refined P4R.13/P4.40 use occurs. No manifest, seal, receipt, inventory difference or census refresh was made.
'''
(out/(stem+'_comparison.md')).write_text(comparison,newline='\n')
for p in out.glob(stem+'*'):
    if p.is_file():assert b'\r' not in p.read_bytes()
report=f'15 READY: {len(rows)} defects; {len(events)} exposed full-proof events; {len(maps)} exact owner maps; {len(equations)} inherited equation identities; {len(units)} actual units/{len(statuses)} criteria. Main plus4 remote guards match once. Tags P329/P331/P332/P333; no central writes.\n'
(root/'code'/'S6_SERIES_PUBLISH_c3_conductor_15.out').write_text(report,newline='\n')
print(report,end='')
