"""Define the actual retained-coordinate maps and present their three proofs."""
from datetime import datetime, timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
path=u.WORK/'root/quotient_maps.tex'
before=path.read_text(encoding='utf-8');after=before
df,rows=r.table(r.DEFECTS);changes=[]
def edit(key,kind,label,old,new,reason):
 global after
 assert after.count(old)==1,(key,after.count(old))
 after=after.replace(old,new,1)
 ident='III-C8-QUOTIENT-MAPS-'+key
 assert not any(x['change_id']==ident for x in rows)
 changes.append(dict(change_id=ident,type=kind,statement_id=label,old_location='retained-coordinate quotient subsection before publication pass',old_page='pending page concordance',new_location='Retained-coordinate quotient maps',new_page='pending final PDF',old_text=old,new_text=new,reason=reason,review_status='applied; whole readback and final PDF pending'))
intro=after[:after.index(r'\begin{theorem}')]
new_intro=r'''\subsection{Retained-coordinate quotient maps}

\begin{definition}[Suspension quotients of the cusp]
\hypertarget{tag-Q011}{}\label{mapsIII:def:cusp-suspension-maps}
{\normalfont\scriptsize tag Q011}\par
Use the intrinsic closed cusp neighbourhood $N_0$ in the original
sphere member, or in one of the defined admissible $|p|=1$ members.
Write $q=t_c=re^{i\phi}$, $0\le r\le\epsilon$, and
$q=e^{2\pi i s}$. In Definition~\ref{mapsIII:def:radial-cusp-data} put
\[
 B_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 C(q)=\begin{pmatrix}6\mu(q)&h(q)\\b(q)-h(q)&\mu(q)\end{pmatrix},
 \qquad Z=sB_0+C(q).
\]
Let $\overline\Lambda=\Lambda/
\mathbb Z\langle\widehat w,\widehat\delta\rangle$ and
$\overline T=\overline\Lambda_{\mathbb R}/\overline\Lambda$.
The ordered basis $([\widehat\gamma],[\widehat u])$ identifies
$\overline T$ with $\mathbb R^2/\mathbb Z^2$ by its two coefficients;
the inverse sends $(a_1,a_2)$ to
$a_1[\widehat\gamma]+a_2[\widehat u]$ modulo the lattice.
For a period lift $\zeta=Z(s)u_{\rm long}+v$, with real
$u_{\rm long},v$, define $\overline\pi=[u_{\rm long}]$.
The real period basis gives the unique coefficients, and period
translations change $u_{\rm long}$ by its integral deck vector.

Give every circle its zero-cell at the identity and use the product
cell structures on $\overline T=T^2$ and $S^1\times\overline T=T^3$.
The map $q_2$ sends $x\in N_0\setminus W$ to
$[r,e^{i\phi},\overline\pi(x)]$ in the unreduced suspension
$\Sigma^u T^3$. It sends $W$ to the lower vertex and the
exterior to the upper vertex. Collapsing $T^{3,(2)}$ and the
basepoint arc gives
\[
 H:X\longrightarrow\Sigma(T^3/T^{3,(2)})=S^4.
\]
Forgetting $e^{i\phi}$ and then collapsing $T^{2,(1)}$ and the
basepoint arc gives $\widehat q_3:X\to\Sigma(T^2/T^{2,(1)})=S^3$.
Forgetting $e^{i\phi}$ and applying the first-coordinate character
$[u_{\rm long}]\mapsto e^{2\pi i(u_{\rm long})_1}$ gives
$\widehat q_\gamma:X\to\Sigma S^1=S^2$.
The reduced maps are the quotients of the corresponding unreduced
suspension maps by their specified basepoint arcs.
\end{definition}

'''.replace('u_{\\rm long}','u_{\\rm long}')
edit('NUMBERED-MAPS','D13','mapsIII:def:cusp-suspension-maps',intro,new_intro,'Move all shared quotient maps, exact period coordinates, coefficient inverses and product-cell/suspension conventions into a numbered definition before use. The same intrinsic cusp maps and admitted sphere scope are retained.')
titles={
 '02J7':('maps:src:B.3.1','The retained-angle homotopy class'),
 '02J8':('maps:src:B.3.2','Null-homotopies after forgetting the angle'),
 '02J9':('maps:src:B.3.3','The cusp-core collapse class')
}
for tag,(label,title) in titles.items():
 edit(tag+'-TITLE','D16',label,r'\begin{theorem}\hypertarget{tag-'+tag+'}',r'\begin{theorem}['+title+r']\hypertarget{tag-'+tag+'}','Supply the precise mathematical title without changing the conclusion.')
 start=after.index(r'\StatementRecord{'+label+'}')
 end=after.index('\n',start)
 edit(tag+'-TAG','D10',label,after[start:end],r'{\normalfont\scriptsize tag '+tag+r'}\par','Print only the retained small tag; all old label/target multiplicities remain.')
edit('J7-DEFINED-MAP','D06','maps:src:B.3.1','For the exact retained-angle map just defined,',r'For the retained-angle map of Definition~\ref{mapsIII:def:cusp-suspension-maps},','Point to the numbered complete input.')
edit('J7-FRAME-OWNER','D06','maps:src:B.3.1','The sphere identifications for the original member and the defined\nadmissible $|p|=1$ members are established in the proof of\n\\cref{maps:src:B.1.2}; take the outward stable framing of each.','The sphere identifications for the original member and the defined\nadmissible $|p|=1$ members are established by\n\\cref{maps:src:B.1.1}; take the outward stable framing of each.','The complete sphere/framing proof was moved into the preceding full-scope J4 lemma; the Hopf-circle citation to J5 remains at its actual separate use.')
old=r'''It preserves the product $q$.  The full inverse image is'''
new=r'''Its inverse is
$z_0=w_0h_1(q)h_2(q)$, $z_1=w_1/h_1(q)$ and $z_2=w_2/h_2(q)$.
The factors are holomorphic and nonzero, and both maps preserve
$q=z_0z_1z_2=w_0w_1w_2$. The full inverse image is'''
edit('J7-CHART-INVERSE','D20','maps:src:B.3.1',old,new,'Print the exact inverse from the complete admitted comparison at the coordinate change used in the proof.')
old=r'''The inequality holds for small $r_0$
because $A_0$ is joined to $\ell_0B_0$ through
$\ell_0B_0+sR(q_0)$, all of which are invertible.'''
new=r'''Put $\ell_0=\log r_0$. The matrix $R(q)$ is bounded near zero,
so choose $r_0$ with $\|B_0^{-1}R(q_0)\|<|\ell_0|$.
For $0\le t\le1$ the factorization
\[
 \ell_0B_0+tR(q_0)
 =\ell_0B_0\bigl(I+(t/\ell_0)B_0^{-1}R(q_0)\bigr)
\]
has inverse obtained by the convergent geometric series for its
second factor. Thus its determinant has the positive sign of
$\det(\ell_0B_0)=\ell_0^2$, proving the inequality.'''
edit('J7-DETERMINANT','D22','maps:src:B.3.1',old,new,'Give the exact small-radius bound and inverse that justify the unchanged positive determinant, as already proved in the whole comparison.')
edit('J7-FREUDENTHAL','D18','maps:src:B.3.1',r'$\pi_6(S^4)\to\pi_2^{\mathrm S}$ is an isomorphism by Freudenthal.',r'$\pi_6(S^4)\to\pi_2^{\mathrm S}$ is an isomorphism by'+ '\n'+r'\cite[Corollary~4.24, pp.~360--361]{Hatcher2002}.','Use the exact primary locator read in this continuation for the stated stabilization range.')
edit('J8-NAME','D08','maps:src:B.3.2','The angle-forgetting workbench maps satisfy','The two angle-forgetting maps of Definition~\\ref{mapsIII:def:cusp-suspension-maps} satisfy','Name the maps by their mathematical retained coordinates and numbered definition.')
j9start=after.index(r'\begin{theorem}[The cusp-core')
definition=r'''\begin{definition}[The cusp-core collapse]
\hypertarget{tag-Q012}{}\label{mapsIII:def:core-collapse}
{\normalfont\scriptsize tag Q012}\par
For the original sphere quotient write
$Q=M\cup_\beta T$, where $T=D_R^2\times S^1$ is the designated
cusp solid torus and $K=\{0\}\times S^1$ is its core.
The boundary identification in retained quotient coordinates is
$\beta(Re^{i\phi},\theta)=(e^{i\phi},\theta)$.
Set $C=M\cup\operatorname{Cone}(\partial M)$, with cone vertex $c_0$.
The map $q_1:X\to C$ is the prescribed Seifert quotient on the
exterior. On the punctured cusp it is
$x\mapsto[r(x),\beta(Re^{i\phi(x)},\theta_\gamma(x))]$,
and it sends $W$ to $c_0$. The two formulas agree on the outer boundary.
\end{definition}

'''
opening=after[j9start:after.index('\n',j9start)]
edit('CORE-INPUT','D13','mapsIII:def:core-collapse',opening,definition+opening,'Give the original-member target, fixed boundary map, core and actual quotient formula one numbered owner before use.')
old=r'''Let $C=M\cup\operatorname{Cone}(\partial M)$ and let
$q_1:X\to C$ be the workbench map retaining the
Seifert quotient away from the cusp and collapsing
$W$ to the cone point.  Under the cofiber splitting
$C\simeq S^3\vee S^2$ determined by the cusp core,'''
new=r'''For the map $q_1$ of Definition~\ref{mapsIII:def:core-collapse},
the core cofiber splitting $C\simeq S^3\vee S^2$ constructed below gives'''
edit('J9-INPUT-OWNER','D11','maps:src:B.3.3',old,new,'The complete geometric input now occurs once in the preceding definition; the full cofiber and class conclusion remains.')
old=r'''\item Write $Q=M\cup_\beta T$, where $T=D_R^2\times S^1$ is the
designated cusp solid torus, $K=\{0\}\times S^1$ is its core, and
$\beta(Re^{i\phi},\theta)=(e^{i\phi},\theta)$ is the fixed boundary
identification in the retained quotient coordinates. Define $\kappa:Q\to C$'''
new=r'''\item In the notation of Definition~\ref{mapsIII:def:core-collapse},
define $\kappa:Q\to C$'''
edit('J9-REPEATED-INPUT','D11','maps:src:B.3.3',old,new,'Use the same already defined fixed boundary map and core; retain the entire quotient, inverse and homotopy proof.')
edit('J9-REPLACEMENT','D08','maps:src:B.3.3','Choose the repaired quotient $e$','Choose the quotient replacement $e$','Use the mathematical construction name.')
old=r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'
for tag,(label,_) in titles.items():
 start=after.index(r'\hypertarget{tag-'+tag+'}')
 pos=after.index(old,start)
 end=after.index(r'\end{proof}',start)
 assert pos<end
 segment=after[start:end]
 newsegment=segment.replace(old,r'\begin{enumerate}[label=\arabic*.,leftmargin=*]',1)
 edit(tag+'-ENUMERATION','D23',label,segment,newsegment,'Replace this result’s machine enumeration by a normal numbered proof; retain all steps and delimiters.')
for suffix in range(1,6):
 marker=r'\tag{B.3.'+str(suffix)+'}'
 pos=after.index(marker);start=after.rfind(r'\[',0,pos);end=after.index(r'\]',pos)+2
 old=after[start:end];new=r'\begin{equation}'+old[2:-2].replace(marker,'')+r'\end{equation}'
 edit('EQUATION-'+str(suffix),'D19','maps:eq:B.3.'+str(suffix),old,new,'Convert exactly this inherited manual number to an automatic section equation with its old formula, label and target retained.')
newlabels=['mapsIII:def:cusp-suspension-maps','mapsIII:def:core-collapse'];newtargets=['tag-Q011','tag-Q012']
u.check_permanent_identifiers(before,after,newlabels,newtargets)
source=u.repairs.SOURCE.read_text(encoding='utf-8');assert source.count(before)==1
candidate=source.replace(before,after,1)
u.check_permanent_identifiers(source,candidate,newlabels,newtargets)
path.write_text(after,encoding='utf-8',newline='\n');u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,rows+changes)
print('UTC',datetime.now(timezone.utc).isoformat())
print('EXACT_DEFECT_ROWS',len(changes),'LINES',len(before.splitlines()),len(after.splitlines()))
print('Q011_Q012_CREATED; ALL_OLD_IDENTITIES_PRESERVED; NO_READING_CREDIT')
