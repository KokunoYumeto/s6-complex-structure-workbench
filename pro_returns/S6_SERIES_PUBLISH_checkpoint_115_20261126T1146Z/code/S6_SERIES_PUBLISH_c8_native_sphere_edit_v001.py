"""Complete publication editing of the wholly read native sphere remainder."""
import csv
import hashlib
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation

root=Path(__file__).resolve().parent.parent
folder=root/'agents/continuation8_iii_integration/units/root'
lane=root/'agents/continuation8_iii_weighted_units'
path=folder/'full_sphere_nullity.tex'
original=path.read_text()
assert hashlib.sha256(path.read_bytes()).hexdigest()=='421291a22537ab77d85ea4940036b1682c9e7be00eb8350506191e5b88282cff'
text=original
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
rows=[]
edits=0
owner='wb:cusp-s12-one-copy-invariant'
def edit(old,new,kinds,reason,label=None):
    global text,edits
    assert old and text.count(old)==1,(old[:100],text.count(old))
    line=text.count('\n',0,text.index(old))+1
    text=text.replace(old,new,1);edits+=1
    for kind in kinds:
        rows.append([f'III-C8-NATIVE-SPHERE-PUB-{edits:03}-{kind}',kind,label or owner,f'full_sphere_nullity.tex sequential line {line}','pending page concordance','root/full_sphere_nullity.tex','pending final build',old,new,reason,'whole repaired/original/receiving/comparison read; full candidate readback pending; global gates open'])

old=text[:text.index(r'\begin{corollary}[The two-copy sphere carrier]')]
new=r'''\subsection{Coefficients and framed fibres of the sphere carriers}
\hypertarget{tag-038U}{}\label{wb:cusp-s12-carrier-homotopy}

\begin{definition}[The native sphere carriers]\hypertarget{tag-Q256}{}\label{wb:def:native-sphere-carriers}
{\normalfont\scriptsize tag Q256}\par
Use the original sphere member, cusp neighbourhood, ordered period
marking, skeleton collapse $c:\overline T^2\to Z_2$ and map $g$
of Definition~\ref{wb:def:marked-cusp-nullbordism-data}. Put
\[
 K=S^1\times\overline T^2,\qquad
 \mathcal A=([0,\epsilon]\times K)/
 (\{0\}\times K=v_0,\ \{\epsilon\}\times K=v_1),\qquad
 B=\Sigma_{\mathrm{red},\epsilon}Z_2.
\]
The two poles of $\mathcal A$ are distinct; its basepoint is $v_0$.
The map $q_2$ of \cref{wb:cusp-cone-S12-route} is
\[
 q_2(x)=[r,e^{i\varphi},\overline\pi_f(x)]
 \quad(t(f(x))=re^{i\varphi},\ 0<r<\epsilon),\qquad
 q_2(W)=v_0,\quad
 q_2(X\setminus\operatorname{int}N_0)=v_1.
\]
The continuous based postcomposition
\[
 p=\widehat p_2:\mathcal A\to B,\qquad
 [r,z,a]\longmapsto[r,c(a)]
\]
sends both poles to the reduced-suspension basepoint, and $g=pq_2$
by its defining formula on the interior and both collapsed ends.
This is the continuous surjective based quotient $\widehat q_3$
of \cref{wb:cusp-cone-angle-forgotten-sphere-carriers}.

Let $d:C_6\to(X,x_0)$ be the fixed based source homeomorphism.
The target homeomorphism $\phi:B\to C_3$ and its inverse are
\[
 \phi[r,c(u_1,u_2)]=[r/\epsilon,u_1,u_2],\qquad
 \phi^{-1}[s,u_1,u_2]=[\epsilon s,c([u_1,u_2])]
\]
on the open cells, where $0<u_i<1$; both send the basepoint to the
basepoint. The source quotient relations and the cube boundary
are identical under these formulas, proving their inverse identities
and continuity. Set $g_C=\phi gd$; the inverse transport is
$g=\phi^{-1}g_Cd^{-1}$. In homotopy groups $[g]$ denotes $[g_C]$.
All smash coordinates use Definition~\ref{wb:def:ordered-cube-spheres}.
In particular, define
\[
 Q=(q_2\wedge q_2)(d\wedge d)\mu_{6,6}^{-1}:C_{12}\to\mathcal A\wedge\mathcal A,
 \qquad
 P=\mu_{3,3}(\phi\wedge\phi)(p\wedge p):\mathcal A\wedge\mathcal A\to C_6.
\]
\end{definition}

'''
edit(old,new,['D02','D05','D12','D13','D16','D20','D22','D26'],
     'Replace the unnumbered defensive setup with the exact native input. The shared marked cusp data remain in Q257; q2,p,g,d,phi,Q,P are specified here with the actual source/target quotients and every homeomorphism inverse. Preserve038U at the subsection.',
     'wb:def:native-sphere-carriers')
edit(r'''Let $d:C_6\to(X,x_0)$ and $\phi:\Sigma_r S^2\to C_3$ be the fixed
based identifications in
\cref{wb:cusp-cone-angle-forgotten-sphere-carriers}, and set
$g_C=\phi\widehat q_3d$. The displayed two-copy quotient, in those
coordinates, is exactly
''',r'''Use $d,\phi,g_C$ of Definition~\ref{wb:def:native-sphere-carriers}.
The displayed two-copy quotient is exactly
''',['D12','D20'],
     'Use the same now-numbered input maps, retaining the complete native application and its inverse transport. No coordinate or geometric scope is changed.',
     'wb:cusp-s12-native-smash-null')

start=text.index(r'\paragraph{The one-copy coefficient and the framed fibre.}')
end=text.index('The suspension calculation in',start)
old=text[start:end]
new=r'''\begin{proposition}[The coefficient and framed fibre]\hypertarget{tag-038X}{}\label{wb:cusp-s12-one-copy-invariant}
{\normalfont\scriptsize tag 038X}\par
The sixfold suspension identifies $\pi_6(S^3)$ with the even subgroup
of $\pi_{12}(S^9)\cong\mathbb Z/24$. For every chosen generator
$\nu_9$, the map
\[
 \operatorname{coef}_{\nu_9}:\pi_6(S^3)\longrightarrow\mathbb Z/12,
 \qquad E^6x=2\operatorname{coef}_{\nu_9}(x)\nu_9,
\]
is an isomorphism. Its inverse is $[a]_{12}\mapsto a\gamma$, where
$E^6\gamma=2\nu_9$. The native $g$ of
Definition~\ref{wb:def:native-sphere-carriers} has coefficient zero.

For every $0<r_0<\epsilon$ and every
$u_0\in\overline T^2\setminus K^{(1)}$, the value
$y_0=[r_0,c(u_0)]$ is regular. Its entire inverse image is an
embedded three-torus with the ordered normal framing induced by
$(r,c_1,c_2)$. That framed fibre represents $[g]$, and its sixfold
framed product represents $E^6[g]$, so the framing determines the
displayed coefficient.

For the particular embedded torus $N$ of \cref{wb:cusp-null:thm},
there are based smooth surjective quotient maps
$F_0,F_1:X\to S^3_{\mathbb H}$, where $S^3_{\mathbb H}$ is the
unit quaternion sphere based at $1$, and one based homeomorphism
$b:C_3\to S^3_{\mathbb H}$, such that
\[
 F_0^{-1}(-1)=F_1^{-1}(-1)=N,\qquad
 \operatorname{coef}_{\nu_9}[b^{-1}F_0d]=0,\quad
 \operatorname{coef}_{\nu_9}[b^{-1}F_1d]=1.
\]
The two maps have the same unframed embedded regular fibre and the
same maps on ordinary integral homology: all positive-degree maps
are zero, and both degree-zero maps are the identity.
\end{proposition}

\begin{proof}
\emph{1. Suspension coordinates.}
Use the exact cube representative $g_C=\phi gd$ of
Definition~\ref{wb:def:native-sphere-carriers}. In the following
suspension formulas, $g$ denotes $g_C$; their inverse geometric
transport is $g=\phi^{-1}g_Cd^{-1}$ as specified there.
'''
edit(old,new,['D01','D02','D10','D12','D13','D16','D20','D26'],
     'Give the whole038X scope as one proposition and one proof: full integral suspension and coefficient isomorphism, every original radius/open-cell regular value, native zero, and actual fixed-generator framing witnesses. Move the repeated native coordinate setup to Q256, with exact inverse notation transport retained.')
edit(r'''More precisely, the coefficient homomorphism
\[
 \operatorname{coef}_{\nu_9}:\pi_6(S^3)\longrightarrow\mathbb Z/12,
 \qquad x\longmapsto a\quad\text{where }E^6x=2a\nu_9,
\]
has inverse $[a]_{12}\mapsto a\gamma$.  The two inverse identities
follow by applying the injective $E^6$ and the inverse on its even
image.  Consequently $[g]=0$ precisely when $[E^6g]=0$ and precisely
when $a=0$.  For the native map these values are zero by
\cref{wb:cusp-null:thm}.
''',r'''The coefficient map in the statement has inverse
$[a]_{12}\mapsto a\gamma$: apply the injective $E^6$ and the
inverse on its even image to verify both composites. Consequently
$[g]=0$ precisely when $[E^6g]=0$ and precisely when $a=0$.
For the native map these values are zero by \cref{wb:cusp-null:thm}.
''',['D12','D22'],
     'Retain the exact coefficient map once in the statement and prove both inverse identities here. Equation038Z remains at the original native suspension equality.')
edit('For $0<r_0<\\epsilon$ and\n$u_0\\in\\overline T^2\\setminus K^{(1)}$, put $y_0=[r_0,c(u_0)]$.',
     '\\emph{2. The entire framed inverse image.}\nFor $0<r_0<\\epsilon$ and\n$u_0\\in\\overline T^2\\setminus K^{(1)}$, put $y_0=[r_0,c(u_0)]$.',
     ['D13'], 'Give the full arbitrary regular-value argument its proof stage, retaining the entire original parameter domain.')
old=r'''The inverse differential of the ordered coordinates $(r,c_1,c_2)$
gives its normal three-framing.  A complement to the tangent bundle
makes this inverse literal; changing the complement changes its
lifts by tangential vectors and gives a homotopy of framed normal
bundles.  A smaller closed tubular neighbourhood has compact
complement whose image misses $y_0$.  Relative smooth approximation
within half this positive image distance, fixed near the fibre and
the basepoint, therefore preserves the entire regular fibre and its
frame.  The based Pontryagin--Thom construction identifies this
framed fibre with $[g]$
\cite[\S7, Theorem~B and Lemma~4, pp.~43, 48--50]{CuspNullMilnor1965}.
'''
new=r'''The inverse differential of the ordered coordinates $(r,c_1,c_2)$
gives its normal three-framing. A complement to the tangent bundle
makes this inverse literal. Two choices of lifts differ by tangent
vectors; their affine interpolation still maps to the same three
target coordinate vectors and gives the framing homotopy.

Apply Lemma~\ref{mapsIII:based-regular-fibre-smoothing} with source
$X$, basepoint $x_0$, map $h_3\phi g:X\to S^3$, and value
$h_3\phi(y_0)$. Its entire inverse image is the torus just proved,
and the displayed local coordinates prove smoothness and rank three
near it. The target chart is
$(r,c_1,c_2)\circ\phi^{-1}h_3^{-1}$, whose inverse is
$h_3\phi\circ(r,c_1,c_2)^{-1}$ on the chosen open cell.
Thus its composite with $h_3\phi g$ is exactly the original ordered
coordinate map. The lemma first makes the map constant near $x_0$
and then supplies the relative smoothing with the same full fibre
and differential. Composing its homotopy with $\phi^{-1}h_3^{-1}$
gives the corresponding based homotopy in $B$.
Its framed Pontryagin--Thom class is therefore exactly $[g]$.
'''
edit(old,new,['D12','D14','D20','D22','D26'],
     'Apply complete earlyQ255 with the actual h3 phi target transport and inverse chart; verify the full inverse image, smooth local rank and exact unchanged differential. The based bump stage supplies the necessary smooth neighbourhood of x0 before relative approximation. No new coefficient or framing assertion is introduced.')
edit(r'''Here is a framing comparison that proves what the unframed data
determine.  Take the particular embedded torus $N$ and bounding
derivative framing $\tau_0$ of \cref{wb:cusp-null:thm}.  We construct
two maps with this same embedded regular fibre and coefficients
$0$ and $1$, retaining the fixed $\nu_9$.  For this comparison,
$y_0$ denotes the particular regular value used in that theorem.
''',r'''\emph{3. Two framings on the same embedded fibre.}
Take the particular embedded torus $N$ and bounding derivative
framing $\tau_0$ of \cref{wb:cusp-null:thm}. Keep the chosen
$\nu_9$ fixed, and use that theorem's regular value $y_0$.
''',['D02','D12','D13'],
     'State the actual shared torus, derivative frame and fixed generator directly, before the complete unchanged quaternion/J construction.')
edit(r'''Their coefficients $0$ and $1$ prove the
asserted failure of those data to determine $a$.  For the native
$g$, the specific derivative framing remains $\tau_0$ and its
coefficient is the already proved value $0$.
''',r'''The two coefficients are $0$ and $1$ with the same unframed
fibre and homology maps. For the native $g$, the derivative framing
is $\tau_0$ and its coefficient is $0$.
\end{proof}
''',['D02','D11','D13'],
     'Close the one complete038X proof with the actual coefficient comparison and native value. The full target map, collapse, Ad/J convention, inverse-unit degree and all homology checks are retained.')

owner='wb:cusp-s12-nullity-scope'
start=text.index(r'\paragraph{The postcomposition and its scope.}')
end=text.index('Thus $Q:C_{12}',start)
old=text[start:end]
new=r'''\begin{proposition}[The postcomposition kernel and metric slices]\hypertarget{tag-038W}{}\label{wb:cusp-s12-nullity-scope}
{\normalfont\scriptsize tag 038W}\par
For $P,Q$ of Definition~\ref{wb:def:native-sphere-carriers}, the
postcomposition homomorphism
\[
 P_*:\pi_{12}(\mathcal A\wedge\mathcal A,*)\longrightarrow\pi_{12}(C_6,*)
\]
satisfies $P_*[Q]=0$ and has a nonzero kernel. More precisely, there
are based maps $J:C_6\to\mathcal A\wedge\mathcal A$ and
$R:\mathcal A\wedge\mathcal A\to C_6$ with
$RJ\simeq\mathrm{id}_{C_6}$ through based maps and $PJ=*$.
For a generator $[h]\in\pi_{12}(C_6)\cong\mathbb Z/2$, the class
$\beta=[Jh]$ is nonzero, with $R_*\beta=[h]$ and $P_*\beta=0$.

The initial quotient maps $\widehat q_3^{\wedge2}$ and
$\widehat q_\gamma^{\wedge4}$ of
\cref{wb:cusp-cone-angle-forgotten-sphere-carriers} are based
null-homotopic and have the specified moving embedded four-spheres.
Their intrinsic radius-$R$ basepoint balls are exactly Euclidean
at the respective thresholds $T-C>4R$ and $\ell_T>4R$ on the
stated radial tail. The same initial maps therefore have the
pointed $\mathbb R^4$ limits proved there.
\end{proposition}

\begin{proof}
\emph{1. The actual postcomposition and its kernel.}
Use $P,Q,d,\phi,p$ and the ordered $\mu$ of
Definition~\ref{wb:def:native-sphere-carriers}.
'''
edit(old,new,['D02','D10','D12','D13','D16','D20','D26'],
     'Give the whole038W assertion one proposition and one proof: exact native kernel membership, explicit nonzero kernel detected by a retract, and both original metric-family/initial-homotopy assertions. The repeated definitions move identically to Q256 with all maps and inverse coordinate choices.')
edit(r'''\qquad P_*[Q]=0
\]
by \cref{wb:cusp-s12-full-carrier-null}.''',r'''\qquad P_*[Q]=0
\]
by \cref{wb:cusp-s12-native-smash-null}.''',['D14'],
     'Cite the exact earlier native application Q254 for the same P Q, retaining the universal theorem through that proved application.')
edit(r'''For completeness, an explicit map supplies the required
four-sphere homotopy retract.''',r'''To construct the four-sphere homotopy retract,''',['D02','D15'],
     'Introduce the retained constructive proof directly; its seven-piece map and all integral homology and based-inverse arguments remain.')
edit('To construct the four-sphere homotopy retract,  Give',
     'To construct the four-sphere homotopy retract, give', ['D23'],
     'Join the introductory clause to its retained sentence with ordinary capitalization.')
old=r'''off the poles its inverse reads $s=\pi^{-1}\arccos x_3$ and the
phase of $x_1+ix_2$.
'''
new=r'''off the poles its inverse reads $s=\pi^{-1}\arccos x_3$ and the
phase of $x_1+ix_2$. Denote this sphere map by $\chi_2$.
The specified identification with $C_2$ is
$\psi_2=h_2^{-1}\chi_2$, with inverse $\chi_2^{-1}h_2$.
Thus the displayed $j_2,r_2$ formulas mean the suspension formulas
composed with $\psi_2^{-1}$ on the source and $\psi_2$ on the
target, respectively; their two strict composite identities follow
by cancellation of these inverse maps.
'''
edit(old,new,['D20','D22'],
     'Identify the unreduced circle-suspension sphere with the same Q253 cube model by the actual stereographic transport and inverse, so the retract compositions use literal C2 coordinates.')
edit(r'''This proves noninjectivity of this exact $P_*$.  The native class
$[Q]$ belongs to its kernel; the construction assigns no further
value to $[Q]$ and makes no identification of $\beta$ with $[Q]$.

The same initial maps retain the point-set and metric properties
proved in \cref{wb:cusp-cone-angle-forgotten-sphere-carriers}.
''',r'''Thus $R_*\beta=[h]\ne0$ detects a nonzero element of
$\ker P_*$, and the native $[Q]$ lies in the same kernel by the
proved equation $P_*[Q]=0$.

\emph{2. The initial maps and their intrinsic metric slices.}
Use the quotient maps and metrics of
\cref{wb:cusp-cone-angle-forgotten-sphere-carriers}.
''',['D02','D11','D13','D26'],
     'Retain exactly the proved membership and noninjectivity through the actual R detector, without an unproved identification of beta with Q. State the original metric constructions as the second full proof stage.')
old=r'''specified initial quotient maps of based null-homotopies.
'''
new=old+r'''\end{proof}
'''
edit(old,new,['D13'], 'Close the one complete038W proof after both full initial-map/metric applications.')
for p in [text]:
    assert '\r' not in p
    _,changes,issues=presentation.statement_records_to_small_tags(p)
    assert not changes and not issues
    _,changes,issues,aliases=presentation.remove_manual_equation_tags(p)
    assert not changes and not issues and not aliases
    assert not presentation.unresolved_literal_equation_references(p)
units.check_permanent_identifiers(original,text,['wb:def:native-sphere-carriers'],['tag-Q256'])
path.write_text(text,encoding='utf-8',newline='\n')
with (lane/'S6_SERIES_PUBLISH_NATIVE_SPHERE_publication_defects.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(fields);w.writerows(rows)
print('INPUT',len(original.splitlines()),hashlib.sha256(original.encode()).hexdigest())
print('CANDIDATE',len(text.splitlines()),hashlib.sha256(text.encode()).hexdigest())
print('EXACT_EDITS',edits,'DEFECT_ROWS',len(rows),'NEW_ID','Q256')
print('OLD_IDENTITIES_PRESERVED; CANDIDATE_WHOLE_READBACK_REQUIRED')
print('CANONICAL_AND_SHARED_WRITES 0; NEW_INDEPENDENT_CREDIT 0')
