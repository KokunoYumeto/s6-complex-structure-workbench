"""Publish the full cusp nullbordism and retain its complete comparison scope."""
import csv
import hashlib
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation
root=Path(__file__).resolve().parent.parent
folder=root/'agents/continuation8_iii_integration/units/root'
lane=root/'agents/continuation8_iii_weighted_units'
path=folder/'cusp_nullbordism.tex'
original=path.read_text();text=original
assert hashlib.sha256(path.read_bytes()).hexdigest()=='538ee1aadbee5736af333a67ae25b6226faf93d8f4da33b39a36cf4028f328ef'
native=folder/'full_sphere_nullity.tex'
native_old=native.read_text();native_text=native_old
assert hashlib.sha256(native.read_bytes()).hexdigest()=='d2217e8f7f3e05940c33c8452391abe84708a1e733b3b734975e28c729f6efdd'
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
rows=[];count=0
def edit(old,new,kinds,why,owner='wb:cusp-null:thm'):
    global text,count
    assert text.count(old)==1,(old[:100],text.count(old))
    line=text.count('\n',0,text.index(old))+1
    text=text.replace(old,new,1);count+=1
    for kind in kinds:
        rows.append([f'III-C8-CUSP-PUB-{count:03}-{kind}',kind,owner,f'cusp_nullbordism.tex sequential line {line}','pending page concordance','root/cusp_nullbordism.tex','pending final build',old,new,why,'whole repaired/original/receiving/comparison read; candidate readback pending; global gates open'])

old=text[:text.index(r'\begin{theorem}[A framed nullbordism of the cusp fibre]')]
new=r'''\subsection{A framed nullbordism of the cusp fibre}

\begin{definition}[Marked cusp data]\hypertarget{tag-Q258}{}\label{wb:def:marked-cusp-nullbordism-data}
{\normalfont\scriptsize tag Q258}\par
Use the original smooth sphere member and its intrinsic closed cusp
neighbourhood $N_0$ from Definition~\ref{mapsIII:def:cusp-suspension-maps}.
Write $f:X\to B_{\mathrm{base}}$ for its map to the base, $t$ for
the specified cusp coordinate, $W=f^{-1}(0)$, and choose $x_0\in W$.
The ordered quotient basis is induced by
$(\widehat\gamma,\widehat u)$ and the kernel lattice is
$\mathbb Z\langle\widehat w,\widehat\delta\rangle$.
The coefficient map and its inverse identify the quotient torus
with $\overline T^2=\mathbb R^2/\mathbb Z^2$.
Write $h_{\mathrm{per}}$ for the same period function denoted $h$
in that definition. The actual periods are
\begin{equation}
 Z(s)=sB_0+C(t),\qquad e^{2\pi i s}=t,\qquad
 B_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 C(t)=\begin{pmatrix}6\mu(t)&h_{\mathrm{per}}(t)\\
 b(t)-h_{\mathrm{per}}(t)&\mu(t)\end{pmatrix}.
 \hypertarget{tag-038N}{}\label{wb:cusp-null:eq:periods}
\end{equation}
Every entry of $C$ is holomorphic at $t=0$. On the dense torus
$(x_1,x_2,t)$, with $x=\exp(2\pi i\zeta)$, the residual period
action is
\begin{equation}
 \Psi_\lambda(x,t)=
 \bigl(t^{B_0\lambda}\exp(2\pi iC(t)\lambda)x,t\bigr),
 \qquad \lambda\in\mathbb Z^2.
 \hypertarget{tag-038E}{}\label{wb:cusp-null:eq:action}
\end{equation}
Its inverse is $\Psi_{-\lambda}$, as direct multiplication of the
two componentwise factors shows. It is the free properly
discontinuous action on the unimodular filling of
\SeriesRef{mapsI:src:A.1.2}; its quotient projection is a local
biholomorphism at every toric fixed point. The explicit injective
chart needed below is proved in \cref{wb:h24:ret:chart-lemma}.

Put
\[
 K^{(1)}=((\mathbb R/\mathbb Z)\times\{0\})
          \cup(\{0\}\times(\mathbb R/\mathbb Z)),\qquad
 Z_2=\overline T^2/K^{(1)},\qquad
 c:\overline T^2\to Z_2.
\]
The open two-cell gives $Z_2$ its orientation, so $c$ has degree
one. Give it the ordered smooth open-cell coordinates $(c_1,c_2)$.
The reduced-suspension target and the native map are
\[
 B=\Sigma_{\mathrm{red},\epsilon}Z_2
 =\frac{[0,\epsilon]\times Z_2}
 {(\{0,\epsilon\}\times Z_2)\cup([0,\epsilon]\times\{*\})},
\]
\begin{equation}
 g(x)=[|t|,c(\overline\pi_f(x))]\quad(0<|t|<\epsilon),\qquad
 g(W)=g(X\setminus\operatorname{int}N_0)=*.
 \hypertarget{tag-038J}{}\label{wb:cusp-null:eq:g}
\end{equation}
The cube target map and its inverse are
\[
 \phi[r,c(u_1,u_2)]=[r/\epsilon,u_1,u_2],\qquad
 \phi^{-1}[s,u_1,u_2]=[\epsilon s,c([u_1,u_2])]
\]
on the open cells; both send the basepoint to the basepoint.
The same collapsed faces give both inverse identities and continuous
quotient descent. Thus $\phi:B\to C_3$ is a based homeomorphism.
The round target is $h_3\phi:B\to S^3$, with inverse
$\phi^{-1}h_3^{-1}$ from Definition~\ref{wb:def:ordered-cube-spheres}.
For the fixed based diffeomorphism $d_S:S^6\to X$, put
$d=d_Sh_6:C_6\to X$, with inverse $h_6^{-1}d_S^{-1}$.
In homotopy groups, $[g]$ denotes the class of $g_C=\phi gd$;
the inverse coordinate transport is $g=\phi^{-1}g_Cd^{-1}$.
\end{definition}

'''
edit(old,new,['D04','D05','D06','D10','D13','D16','D18','D20','D22','D26'],
     'Number the full actual cusp input, retain every period/action/map identity, replace the unavailable reconstructed-page locator by its permanent construction owner, give deck inverse and exact source/target coordinate maps. The original member, lattice, periods, action, local quotient scope and whole collapsed map remain unchanged.',
     'wb:def:marked-cusp-nullbordism-data')
for tag,label in [('038S','wb:cusp-null:thm'),('03A6','wb:cusp_s12_carrier_homotopy:L567')]:
    old='\\hypertarget{tag-'+tag+'}{}\\label{'+label+'}\n'
    edit(old,old+'{\\normalfont\\scriptsize tag '+tag+'}\\par\n',['D10'],
         'Show the existing permanent statement tag in a small header while preserving its target and label.',label)
edit(r'''For the framed inverse image, set
''',r'''\emph{1. The complete inverse image.}
Set
''',['D13'], 'Give the actual inverse-image construction its proof stage after the exact based-nullity application.')
edit(r'''Use the injective chart of \cref{wb:h24:ret:chart-lemma}, whose
toric coordinates are
''',r'''Use the injective neighbourhood constructed in the proof of
\cref{wb:h24:ret:chart-lemma}. Its toric coordinates are
''',['D20','D22'],
     'Use the entire uniform chart construction, whose domain covers all base angles; the current argument independently identifies the complete three-torus, retaining the extra angular variable.')
edit(r'''Conversely these moduli give $A(t)(u-u^0)=0$ and hence the same
quotient value. Its angular coordinates and their inverse are
\phantomsection\hypertarget{tag-033Q}{}\label{qa:III:layout:1}
\[
 (\varphi,a,b)\longmapsto(\varphi-a-b,a,b),\qquad
 (\theta_0,a,b)\longmapsto(\theta_0+a+b,a,b)
 \quad\pmod{2\pi}.
\]
''',r'''Conversely these moduli give $A(t)(u-u^0)=0$ and hence the same
quotient value. Its angular coordinates and their inverse are
\begin{equation}
 (\varphi,a,b)\longmapsto(\varphi-a-b,a,b),\qquad
 (\theta_0,a,b)\longmapsto(\theta_0+a+b,a,b)
 \quad\pmod{2\pi}.
 \hypertarget{tag-033Q}{}\label{qa:III:layout:1}
\end{equation}
''',['D19','D20'],
     'Attach existing033Q and its exact old label to the retained inverse angular identity in an automatically numbered equation. No new formal result or equation identity is created.')
edit('Put $L_j=\\log|w_j|$ and use the real lift $u$ near $u^0$.',
     '\\emph{2. The ordered differential and its frame homotopy.}\nPut $L_j=\\log|w_j|$ and use the real lift $u$ near $u^0$.',
     ['D13'], 'Separate the full actual differential calculation as the second proof stage; retain every derivative and determinant identity.')
old=r'''normal vector to its class modulo the tangent bundle.

For $0\leq\sigma\leq1$, let
'''
new=r'''normal vector to its class modulo the tangent bundle.

For its Pontryagin--Thom interpretation, apply
Lemma~\ref{mapsIII:based-regular-fibre-smoothing} to the actual map
$h_3\phi g:X\to S^3$, source basepoint $x_0$ and value
$h_3\phi(y_0)$. The full inverse image is $T_{r_0}$, disjoint from
$x_0$ because $|t|=r_0>0$ there. The displayed differential proves
smoothness and rank three near it. The ordered target chart is
$(r,c_1,c_2)\phi^{-1}h_3^{-1}$, with inverse
$h_3\phi(r,c_1,c_2)^{-1}$, so its composite with $h_3\phi g$
is exactly $(r,c_1,c_2)g$. The lemma preserves this entire inverse
image and its actual frame. Postcomposition of its homotopy by
$\phi^{-1}h_3^{-1}$ returns to $B$ and fixes its basepoint.

For $0\leq\sigma\leq1$, let
'''
edit(old,new,['D12','D14','D20','D22','D26'],
     'Apply the sole complete smoothing owner Q255 with the exact round-target map/inverse, whole T_r0, verified rank and ordered target chart. This retains the original based PT/frame scope without reprinting a second generic smoothing proof.')
edit('For the cap use a new time coordinate $v\\in[0,1]$ and define',
     '\\emph{3. The collared framed cap.}\nUse a new time coordinate $v\\in[0,1]$ and define',
     ['D13'], 'Give the complete cap and basepoint-exclusion construction its third proof stage.')
edit(r'''Time recovers $|z|$ and the $w_0$ phase recovers its angle.
Thus this is an embedding onto the disk factor, giving
''',r'''The inverse is
\[
 z=\sqrt{1-2v}\,\frac{w_0}{|w_0|}\quad(w_0\ne0),\qquad
 z=0\quad(w_0=0).
\]
It is smooth at the centre by the inverse-function theorem applied
to the derivative $f(0)I_2$; away from the centre the displayed
formula is smooth. Thus this is an embedding onto the disk factor, giving
''',['D20','D22'],
     'Print the exact inverse of the retained disk parametrization and its centre smoothness, preserving the actual q-profile, collar and frame extension.')
start=text.index('Under the fixed based identification $X\\cong S^6$,')
end=text.index('The homomorphism\n',start)
edit(text[start:end],r'''Under the fixed based coordinates of
Definition~\ref{wb:def:marked-cusp-nullbordism-data},
\[
 [g]=0\in\pi_6(S^3)\cong\mathbb Z/12,\qquad
 [E^6g_C]=0\in\pi_{12}(S^9)\cong\mathbb Z/24.
\]
For a chosen generator $\nu_9$ of the target group, define its
even-coordinate map and inverse by
\[
 \delta:\mathbb Z/12\longrightarrow2\langle\nu_9\rangle,
 \quad[a]_{12}\longmapsto2a\nu_9,\qquad
 \delta^{-1}(2a\nu_9)=[a]_{12}.
\]
The native coefficient is
$a=\delta^{-1}([E^6g_C])=0\pmod{12}$.
''',['D12','D14','D20','D22','D26'],
     'Define the actual native coefficient only after the proved zero map and zero suspension, through the complete even-coordinate isomorphism and inverse. This removes dependence on later038X while preserving exactly the original coefficient convention and all zero values.',
     'wb:cusp_s12_carrier_homotopy:L567')
edit(r'''Let $d:(S^6,*)\to(X,x_0)$ be the fixed based identification and
$H_g$ the based null-homotopy of \cref{wb:cusp-null:thm}.
The formula $H(u,s)=H_g(d(u),s)$ has initial map $g\circ d$,
constant terminal map and fixed basepoint, so $[g]=0$.
''',r'''Use $d:C_6\to(X,x_0)$ and $\phi:B\to C_3$ from
Definition~\ref{wb:def:marked-cusp-nullbordism-data}, and let
$H_g$ be the based null-homotopy of \cref{wb:cusp-null:thm}.
The formula $H(u,s)=\phi H_g(d(u),s)$ has initial map $g_C$,
constant terminal map and fixed basepoint, so $[g]=0$.
The inverse coordinate changes are $d^{-1}$ and $\phi^{-1}$.
''',['D20','D22'],
     'Apply the same fixed source/target homeomorphisms, with inverse changes, to the actual based null-homotopy; all endpoint values remain literal.',
     'wb:cusp_s12_carrier_homotopy:L567')
edit(r'''therefore gives $[E^6g]=0$ in either placement convention.
By the definition $[E^6g]=2a\nu_9$, where $\nu_9$ has order $24$,
we have $24\mid2a$, hence $12\mid a$.
Equivalently, $[a]_{12}\mapsto2a\nu_9$ is injective, with
inverse $2a\nu_9\mapsto[a]_{12}$ on its image.
''',r'''therefore gives $[E^6g_C]=0$ in either placement convention.
For the displayed $\delta$, adding $12$ to $a$ changes the image
by $24\nu_9=0$, and
$2a\nu_9=2b\nu_9$ is equivalent to $24\mid2(a-b)$, hence to
$12\mid(a-b)$. Thus $\delta$ is an isomorphism onto the even
subgroup, with the stated well-defined inverse. The zero class is
in this image, so its actual coefficient exists and is
$\delta^{-1}(0)=0$. This establishes the coefficient here, before
any computation for arbitrary one-copy classes.
''',['D14','D20','D22'],
     'Prove descent, injectivity, surjectivity onto the specified subgroup and the inverse, then apply it to the already established zero class. No stabilization injectivity is assumed for this native zero argument.',
     'wb:cusp_s12_carrier_homotopy:L567')

closing=text[text.index(r'\paragraph{Exact scope.}'):]
edit(closing,'',['D02','D11','D12','D13','D14','D26'],
     'Move the complete mathematical postcomposition comparison to numbered Q257 after both frame calculations. There the same q2,p3,hat p2, H/g values, actual framed tori and Hopf-smash map/value are supplied; complete038W owns the point-set/metric initial-map assertions. Root also moves the overlapping retained paragraph to this same owner.')

# Keep the removed Hopf-smash conclusion in the actual later comparison owner.
needle=r'''proved in \cref{wb:cusp-s12-nullity-scope}.
\end{remark}
'''
hopf=r'''proved in \cref{wb:cusp-s12-nullity-scope}.

The Hopf smash has an explicit representative in the same models.
Let $\eta_2$ be the complex Hopf map of
Definition~\ref{mapsIII:def:framing-conventions} and put
$\eta_{2,C}=h_2^{-1}\eta_2h_3:C_3\to C_2$.
On the retained target use
\[
 \phi_4[r,c_3(e^{i\varphi},[u_1,u_2])]
      =[r/\epsilon,\varphi/(2\pi),u_1,u_2],\qquad
 \phi_4^{-1}[s,a,u_1,u_2]
      =[\epsilon s,c_3(e^{2\pi ia},[u_1,u_2])]
\]
on the open cells and the basepoint elsewhere. Both maps respect
exactly the collapsed faces and are inverse. Composing $\phi_4$
with $h_4$ gives the same ordered cotangent-coordinate sphere
identification as \eqref{wb:h24:ret:eq:four-cell}, since
$\tan(\pi(a-1/2))=-\cot(\pi a)$. Hence the actual smash is
\[
 \mu_{4,2}\bigl((\phi_4Hd)\wedge\eta_{2,C}\bigr)
             \mu_{6,3}^{-1}:C_9\longrightarrow C_6.
\]
Its stable class is $\eta^2\eta=\eta^3=12\nu$ by the product
framed-collapse convention and \eqref{maps:eq:B.1.2}.
Suspension from $\pi_9(S^6)$ is an isomorphism at every subsequent
stage: $9+k<2(6+k)-1$ for every $k\geq0$
\cite[Corollary~4.24]{Hatcher2002}. Let $\nu_6$ be the inverse
image of the fixed stable generator $\nu$ under this isomorphism.
In cyclic coordinates its inverse sends $a\nu$ to $a\nu_6$ modulo
$24$. The displayed Hopf smash therefore represents
$12\nu_6\ne0$ in $\pi_9(S^6)$, as asserted for the retained map.
\end{remark}
'''
assert native_text.count(needle)==1
native_text=native_text.replace(needle,hopf)
old_frame=r'''The latter is the derivative frame $\mathfrak n$ of
\eqref{wb:cusp-null:eq:actual-frame}, extended over the explicit
framed cap by \eqref{wb:cusp-null:eq:extended-frame}.
'''
new_frame=r'''The latter is the derivative frame $\mathfrak n$ of
\eqref{wb:cusp-null:eq:actual-frame}. Its proved frame homotopy
joins it to $NP$; the cap frame
\eqref{wb:cusp-null:eq:extended-frame} extends $NP$.
The cylinder followed by that cap is its framed nullbordism.
'''
assert native_text.count(old_frame)==1
native_text=native_text.replace(old_frame,new_frame)
native_table=lane/'S6_SERIES_PUBLISH_NATIVE_SPHERE_publication_defects.tsv'
with native_table.open(newline='') as f:
    rr=csv.DictReader(f,delimiter='\t');native_rows=list(rr);assert rr.fieldnames==fields
assert len(native_rows)==73
for number,olds,news,kinds,why in [
    (27,needle,hopf,['D12','D14','D20','D22','D26'],'Retain the complete Hopf-smash conclusion moved from the cusp closing paragraph in Q257, with the actual cube representative, all source/target homeomorphism inverses, the identical cotangent target convention, stable product relation and exact stabilization inverse.'),
    (28,old_frame,new_frame,['D20','D22','D26'],'State the precise two-stage framed bordism: the actual derivative frame is homotoped to NP on the cylinder, then the explicit cap extends NP. Do not identify the two boundary frame matrices without that homotopy.')]:
    for kind in kinds:
        native_rows.append(dict(zip(fields,[f'III-C8-NATIVE-SPHERE-PUB-{number:03}-{kind}',kind,'wb:remark:two-cusp-postcompositions','root/full_sphere_nullity.tex Q257','pending page concordance','root/full_sphere_nullity.tex Q257','pending final build',olds,news,why,'bounded full-scope move after whole original/receiving comparison; readback pending; global gates open'])))

units.check_permanent_identifiers(original,text,['wb:def:marked-cusp-nullbordism-data'],['tag-Q258'])
units.check_permanent_identifiers(native_old,native_text)
for candidate in [text,native_text]:
    assert '\r' not in candidate
    _,changes,issues=presentation.statement_records_to_small_tags(candidate)
    assert not changes and not issues
    _,changes,issues,aliases=presentation.remove_manual_equation_tags(candidate)
    assert not changes and not issues and not aliases
    assert not presentation.unresolved_literal_equation_references(candidate)
for target,value in [(path,text),(native,native_text)]:
    temp=target.with_suffix('.tex.tmp');temp.write_text(value,encoding='utf-8',newline='\n');temp.replace(target)
with (lane/'S6_SERIES_PUBLISH_CUSP_NULLBORDISM_publication_defects.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(fields);w.writerows(rows)
with native_table.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(native_rows)
print('CUSP_INPUT',len(original.splitlines()),hashlib.sha256(original.encode()).hexdigest())
print('CUSP_CANDIDATE',len(text.splitlines()),hashlib.sha256(text.encode()).hexdigest())
print('CUSP_EXACT_EDITS',count,'DEFECT_ROWS',len(rows),'NEW_ID','Q258')
print('NATIVE_CANDIDATE',len(native_text.splitlines()),hashlib.sha256(native_text.encode()).hexdigest(),'DEFECT_ROWS',len(native_rows))
print('ALL_OLD_IDENTITIES_PRESERVED; TWO_COMPLETE_CANDIDATE_READBACKS_REQUIRED')
print('CANONICAL_AND_SHARED_WRITES 0; NEW_INDEPENDENT_CREDIT 0')
