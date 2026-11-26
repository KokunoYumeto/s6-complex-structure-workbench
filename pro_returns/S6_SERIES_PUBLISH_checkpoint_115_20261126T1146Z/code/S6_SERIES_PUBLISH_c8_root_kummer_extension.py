"""Consolidate the identical Kummer proof and retain its conductor/deck refinements."""
from datetime import datetime,timezone
from collections import Counter
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
df,ds=r.table(r.DEFECTS);changes=[]
path=u.WORK/'root/kummer_extension.tex';before=path.read_text();after=before
def edit(suffix,kind,label,old,new,reason):
 global after
 assert after.count(old)==1,(suffix,after.count(old))
 after=after.replace(old,new,1)
 ident='III-C8-KUMMER-EXT-'+suffix;assert not any(x['change_id']==ident for x in ds)
 changes.append(dict(change_id=ident,type=kind,statement_id=label,old_location='kummer_extension before complete publication comparison',old_page='pending page concordance',new_location='kummer_extension with exact shared proof map',new_page='pending final PDF',old_text=old,new_text=new,reason=reason,review_status='exact edit applied; complete edited-unit reading pending'))
old=r'''This section determines exactly what is true in the assertion that the
degree-$N^2$ cover of the regular fibres extends by a toric power map.  The
answer is positive for the completed \emph{local} cusp family, but the source
action has to be changed, and two different degrees must not be conflated.

Retain the cusp data'''
new=r'''\begin{definition}[Completed cusp root data]
\hypertarget{tag-Q019}{}\label{mapsIII:def:completed-cusp-root-data}
{\normalfont\scriptsize tag Q019}\par
Use the completed target cusp and period correction of
Definition~\ref{mapsIII:def:kummer-data}. Write $t=q$, with inverse
$q=t$, for its base coordinate. In these coordinates the data are'''
edit('INPUT','D13','mapsIII:def:completed-cusp-root-data',old,new,'Put all complete target/source data in a numbered definition. The target is the already constructed cusp; the exact t=q coordinate map and inverse identify its scope with K2.')
old=r'''Fix an integer $N\geq1$.  Let $v$ be a coordinate on a second disc and
make the base change'''
new=r'''Fix an integer $N\geq1$. For a sufficiently small $r>0$, take
\[
 \Delta_v=\{|v|<r\},\qquad \Delta_t=\{|t|<r^N\},\qquad
 \Delta_v=\rho_N^{-1}(\Delta_t),
\]
and restrict the target cusp to $\Delta_t$. The germ $C$ is represented
on a disc containing $\{|z|<r\}$. Let $v$ be the root coordinate and set'''
edit('COMPATIBLE-DOMAINS','D05','mapsIII:def:completed-cusp-root-data',old,new,'Move the full compatible-disc convention before the source action and its use; retain every N>=1 and both actual target/source restrictions.')
old=r'''\begin{theorem}[Kummer extension through the cusp]
\hypertarget{tag-037X}{}\label{wb:cusp-cover-extension-theorem}
Fix $N\geq1$.  For a sufficiently small $r>0$, take the compatible
disc representatives
\[
 \Delta_v=\{|v|<r\},\qquad \Delta_t=\{|t|<r^N\},\qquad
 \Delta_v=\rho_N^{-1}(\Delta_t),
\]
and restrict the target cusp family to $\Delta_t$.  The holomorphic
germ $C$ is represented on a disc containing $\{|z|<r\}$.
With the actions \eqref{wb:cusp-cover-target-action} and
\eqref{wb:cusp-cover-source-action}, the following statements hold.'''
new=r'''Also write
\[
 \Psi^{\rm un}_{\bar\lambda}(\xi,v)
 =\bigl(c_{\bar\lambda}(v)v^{B_0\bar\lambda}\xi,v\bigr)
\]
for the action with the unrooted correction at $v$.
\end{definition}

\begin{theorem}[Central fibres and deck transformations of the Kummer map]
\hypertarget{tag-037X}{}\label{wb:cusp-cover-extension-theorem}
{\normalfont\scriptsize tag 037X}\par
For the data of Definition~\ref{mapsIII:def:completed-cusp-root-data},
the local Kummer maps of Theorem~\ref{maps:src:C.1.1} have the
following central-fibre and whole-family descriptions.'''
edit('THEOREM-INPUT','D11','wb:cusp-cover-extension-theorem',old,new,'Name the earlier common construction and the additional central-fibre/whole-family conclusions, with the complete input already defined and the original six clauses retained.')
oldproof=after[after.index('\\begin{proof}') : after.index('\\end{proof}')+len('\\end{proof}')]
newproof=r'''\begin{proof}
The data agree with Theorem~\ref{maps:src:C.1.1} through the maps
\[
 (x,t)\longmapsto(x,q=t),\qquad
 (\xi,v)\longmapsto(\xi,v),\qquad
 \bar\lambda\longmapsto\lambda
\]
in the fixed ordered bases. Their inverses are $(x,q)\mapsto(x,t=q)$,
the identity on $(\xi,v)$, and the inverse basis identification.
Every cone and every character coordinate is fixed. The holomorphic
correction is the same $C$, and both source actions use
$C(v^N)/N$. Thus these maps extend through every toric chart, commute
with the period actions and the power maps, and induce inverse maps
on their quotients and fibre products. The radius identification
$r=\epsilon_N$, with inverse $\epsilon_N=r$, gives the full
inverse-image discs of that same construction.

Under these identifications, the earlier theorem proves the free and
properly discontinuous source action, proper smooth quotient, both
finite degrees, finite flatness of $\kappa_N$, normality of $N_0[N]$,
and the precise relative non-\'etale and nonflat loci. Its complete
chart and invariant-ring proof applies to these identical maps. In
particular its maximal-chart formula is
\begin{equation}
 \mathbb C\{z_0,z_1,z_2\}\longrightarrow
 \mathbb C\{w_0,w_1,w_2\},\qquad z_i\longmapsto w_i^N.
 \hypertarget{tag-0380}{}\label{wb:cusp-cover-maximal-chart-map}
\end{equation}
The equality of the two coordinate descriptions of equivariance is
\begin{align}
 P_N\Psi^{(N)}_{\bar\lambda}(\xi,v)
 &=\bigl((c^{(N)}_{\bar\lambda}(v))^N
             v^{NB_0\bar\lambda}\xi^N,v^N\bigr)\\
 &=\bigl(c_{\bar\lambda}(v^N)
             (v^N)^{B_0\bar\lambda}\xi^N,v^N\bigr)
 =\Psi_{\bar\lambda}P_N(\xi,v).
 \hypertarget{tag-037W}{}\label{wb:cusp-cover-equivariance-computation}
\end{align}
It uses the same identity $NC_N(v)=C(v^N)$ on the whole root disc.

We describe the normalization and conductor maps explicitly.
The local equation $v=w_0w_1w_2$ makes $W_N$ reduced. Before the
lattice quotient its components are the toric divisors $D_p$,
$p\in\mathbb Z^2$, and the action sends $D_p$ to
$D_{p+B_0\bar\lambda}$. The equality $B_0\bar\Lambda=\mathbb Z^2$
gives one component orbit with trivial component stabilizer, as in
the earlier construction. The branch-separating map is the injection
\[
 \frac{\mathbb C\{w_0,w_1,w_2\}}{(w_0\cdots w_{k-1})}
 \longrightarrow
 \prod_{i=0}^{k-1}\frac{\mathbb C\{w_0,w_1,w_2\}}{(w_i)},
 \qquad 1\le k\le3.
\]
Its kernel is zero because $\bigcap_{i<k}(w_i)=(w_0\cdots w_{k-1})$.
It is finite, has the same total ring of fractions, and has normal
target, so it is the integral closure. These maps glue; the quotient
of the separated components is $D_0$. The identity of the star fans
identifies this $D_0$ with the target normalization $E\simeq\mathrm{dP}_6$,
with inverse the same fan map. The two branches at an open double
stratum prove that $W_N$ is nonnormal. The ramification formula of
Theorem~\ref{maps:src:C.1.1} gives index $N$ on each central component.
Each maps onto its target component. Hence the branch support is all
of $W$ for $N>1$ and empty for $N=1$.

The relative map has the same local-ring homomorphism as
\eqref{maps:eq:C.1.2}, now written
\begin{equation}
 \begin{gathered}
 A_N:=\frac{\mathbb C\{z_0,z_1,z_2,v\}}{(z_0z_1z_2-v^N)},
 \qquad B:=\mathbb C\{w_0,w_1,w_2\},\\
 A_N\longrightarrow B,\qquad z_i\longmapsto w_i^N,
 \qquad v\longmapsto w_0w_1w_2.
 \end{gathered}
 \hypertarget{tag-037S}{}\label{wb:cusp-cover-basechange-local-ring}
\end{equation}
Write
\[
 \mathcal D_N=\{(\varepsilon_0,\varepsilon_1,\varepsilon_2)\in\mu_N^3:
                   \varepsilon_0\varepsilon_1\varepsilon_2=1\}.
\]
The identity on the three diagonal multipliers identifies this with
the group in that earlier proof, and the invariant-ring map gives
\begin{equation}
 A_N=B^{\mathcal D_N}.
 \hypertarget{tag-037Z}{}\label{wb:cusp-cover-invariant-ring}
\end{equation}
The inverse on an invariant monomial takes its common exponent residue
$r$ modulo $N$ and writes it uniquely as
$(w_0w_1w_2)^r\prod_i(w_i^N)^{b_i}$, $0\le r<N$.
The finite residue grouping is the convergent-series inverse proved
there. On the dense torus the group is the phase action
\[
 (\eta_1,\eta_2)(\xi_1,\xi_2,v)
       =(\eta_1\xi_1,\eta_2\xi_2,v),\qquad (\eta_1,\eta_2)\in\mu_N^2.
\]
Its first-chart identification is
$(\eta_1,\eta_2)\mapsto((\eta_1\eta_2)^{-1},\eta_1,\eta_2)$,
with inverse $(\varepsilon_0,\varepsilon_1,\varepsilon_2)
\mapsto(\varepsilon_1,\varepsilon_2)$.
It extends torically and commutes with every period action. The chart
invariant-ring isomorphisms therefore glue to identify its whole
quotient with $N_0[N]$.

The closed-fibre computations in the earlier proof give, at a triple point,
\begin{align}
 \dim_{\mathbb C}
 \frac{\mathbb C\{w_0,w_1,w_2\}}
      {(w_0^N,w_1^N,w_2^N,w_0w_1w_2)}
 &=N^3-(N-1)^3\\
 &=3N^2-3N+1.
 \hypertarget{tag-038A}{}\label{wb:cusp-cover-triple-fibre-length}
\end{align}
At a double stratum, the $N$ roots of the nonzero transverse coordinate
separate $N$ local branches. Each has generic degree $N$ and the
two-variable map $z_i=w_i^N$, $v=w_0w_1$, with closed-fibre length
\begin{equation}
 \dim_{\mathbb C}
 \frac{\mathbb C\{w_0,w_1\}}{(w_0^N,w_1^N,w_0w_1)}=2N-1.
 \hypertarget{tag-037V}{}\label{wb:cusp-cover-double-fibre-length}
\end{equation}
Thus the $N$ branches have total generic degree $N^2$.
For $N>1$ the excesses over the respective local generic ranks are
$(N-1)(2N-1)$ and $N-1$, exactly as in the earlier nonflatness proof.
At $N=1$ both excesses vanish and both maps are identities.

For the regular fibres use $v=e^{2\pi i s_v}$, so $t=e^{2\pi iNs_v}$.
The log coordinate $s_v$ is the coordinate $r$ of the earlier period
calculation, with inverse renaming, and
\[
 Z_N(s_v)=s_vB_0+\frac1N C(v^N),\qquad
 Z(Ns_v)=NZ_N(s_v),\qquad
 N\Pi_{\rm source}=\Pi_{\rm target}S_N.
\]
The same isomorphism $[\zeta]\mapsto[N\zeta]$, with inverse
$[\widetilde\zeta]\mapsto[\widetilde\zeta/N]$, puts the fibre map in the form
\begin{equation}
 \frac{\mathbb C^2}{N\mathbb Z^2+Z(Ns_v)\mathbb Z^2}
 \longrightarrow
 \frac{\mathbb C^2}{\mathbb Z^2+Z(Ns_v)\mathbb Z^2},\qquad
 [\widetilde\zeta]\longmapsto[\widetilde\zeta].
 \hypertarget{tag-037P}{}\label{wb:cusp-cover-additive-fibre-map}
\end{equation}
It has the same image lattice of index $\det S_N=N^2$.
In source coordinates its deck maps are
$\zeta\mapsto\zeta+(a,b)/N$, with inverse translation by $-(a,b)/N$;
their exponentials are the phase maps above.

For the clockwise cusp generator the pulled-back clutch is $M_0^N$.
Write $M_0=I+R$, where $R(a,b,c,d)=(0,0,b,-a)$ and $R^2=0$.
Then $M_0^N=I+NR$ and $M_0^NS_N=S_NM_0$.
Both affine clutches fix zero, represented by $(1,1)$ after
exponentiation, and $\zeta\mapsto N\zeta$ preserves it. Thus this
identity intertwines the affine clutches as well. Their action on
$\Lambda/S_N\Lambda$ is trivial because every change under $M_0^N$
is $N$ times a short period. The deck group therefore acts on the
whole punctured relative family.

Finally, $P_N$ preserves every ray and sends $D_p$ to $D_p$.
On $D_0$ its induced cocharacter map on $N'/\mathbb Z(0,0,1)$
is multiplication by $N$. This is $[N]:E_N\to E$, of degree $N^2$.
Its boundary charts are $(a,b)\mapsto(a^N,b^N)$, giving index $N$
on each of the six boundary curves. The normalization maps are the
inclusions of $D_0$ followed by the period quotient maps.
Equation~\eqref{wb:cusp-cover-equivariance-computation} makes the
normalization square commute pointwise. Every source conductor gluing
by $\bar\lambda$ maps to the target gluing by the same $\bar\lambda$,
including its holomorphic unit factors. Each of the two translation
orbits of maximal triangles is preserved; these are the two
triple-point classes. The generic isomorphisms of the normalizations
give degree $N^2$ on the reduced central fibres.

At $N=1$ the actions coincide, $P_1$ is the coordinate identity,
and $\kappa_1$ is its quotient. The projection $N_0[1]\to N_0$ has
inverse $y\mapsto(y,f_0(y))$, identifying $Q_1$ with the identity.
All ramification and branch supports are empty and $S_1=I$.
\end{proof}'''
edit('COMMON-PROOF','D12','wb:cusp-cover-extension-theorem',oldproof,newproof,'Assign the identical full action/flatness/invariant-ring/local-length argument to K2 after printing every input, chart, period and group identification with inverse. Retain the complete additional branch normalization, conductor square, N double branches, whole-family deck action and all endpoints. All old equation anchors remain at their formulas.')
old=r'''On the compatible discs of Theorem~\ref{wb:cusp-cover-extension-theorem},
let $\Psi^{\mathrm{un}}_{\bar\lambda}$ be the source action obtained
from \eqref{wb:cusp-cover-target-action} by replacing $t$ with $v$.
Direct substitution gives'''
new=r'''{\normalfont\scriptsize tag 0382}\par
The two action formulas of
Definition~\ref{mapsIII:def:completed-cusp-root-data} have the following
comparison for every holomorphic matrix $C$ on the compatible discs.
Direct substitution gives'''
edit('ACTION-REMARK-SCOPE','D26','wb:cusp-cover-naive-action-failure',old,new,'Keep the analytic comparison for every holomorphic C, separately from the constructed target-cusp input of 037X; the whole equality proof remains.')
old=r'''Here $m_\eta(\xi,v)=(\eta\xi,v)$, and the multiplier lies in the
deck group $\mu_N^2$ of the relative toric power map.'''
new=r'''Here $m_\eta(\xi,v)=(\eta\xi,v)$ has inverse
$m_{\eta^{-1}}$, and the multiplier lies in the deck group
$\mu_N^2$ of the relative toric power map.'''
edit('MULTIPLIER-INVERSE','D20','wb:cusp-cover-naive-action-failure',old,new,'Print the inverse of the equality-case deck multiplier while keeping every exceptional equality case and N=1.')
start=after.index('The maps of Theorem~\\ref{wb:cusp-cover-extension-theorem} have targets')
end=after.index('For $N>1$, the connected regular-fibre cover',start)
edit('GLOBAL-REMARK-OWNER','D12','wb:cusp-cover-global-scope',after[start:end],r'''{\normalfont\scriptsize tag 037Y}\par
Use the maps and compatible discs of
Definition~\ref{mapsIII:def:completed-cusp-root-data} and
Theorem~\ref{wb:cusp-cover-extension-theorem}.

''','Use the preceding proved factorization/normalization/endpoint maps by their exact owners instead of proving those same clauses again. The full original-base lattice obstruction remains.')
edit('BASE-LOOP','D20','wb:cusp-cover-global-scope',r'''through both finite fillings.  Indeed, the monodromy matrix $A_1$
satisfies''',r'''through both finite fillings. The counterclockwise based loop
$a_1^{-1}$ has point-return matrix $A_1$ by
Definition~\ref{mapsIII:def:three-filling-datum}, and
$A_1$ satisfies''','Name the actual inverse based loop realizing the displayed fibre transport, preserving the exact original-base subgroup obstruction.')
edit('Y-TITLE','D16','wb:cusp-cover-global-scope','[The cusp cover and the original base]','[Monodromy of the marked fibre subgroup]','Name the actual integral-local-system conclusion.')
kp=u.WORK/'root/local_kummer.tex';kb=kp.read_text()
ko=r'''For $N\ge1$, the base root is $q=v^N$ and the source correction is
$C_N(v)=C(v^N)/N$. The source period cover uses that same fan.'''
kn=r'''For $N\ge1$, the base root is $q=v^N$ and the source correction is
$C_N(v)=C(v^N)/N$. Choose a sufficiently small root radius $\epsilon_N>0$
and represent the germ on the compatible discs $|v|<\epsilon_N$ and
$|q|<\epsilon_N^N$;
the source disc is the full inverse image of the target disc.
The source period cover uses that same fan.'''
assert kb.count(ko)==1
ka=kb.replace(ko,kn,1)
changes.append(dict(change_id='III-C8-KUMMER-COMPATIBLE-DISCS',type='D26',statement_id='mapsIII:def:kummer-data',old_location='Q017 root-cover input',old_page='pending page concordance',new_location='Q017 compatible root/target representatives',new_page='pending final PDF',old_text=ko,new_text=kn,reason='Print the exact compatible disc representatives used by the local finite map and the later identical construction. Every N>=1 remains; the complete source is the full inverse image of the chosen target.',review_status='bounded input follow-up; whole shared-proof comparison pending admission'))
cp=u.ROOT/'S6_SERIES_PUBLISH_III.tex';canonical=cp.read_text()
assert canonical.count(before)==1 and canonical.count(kb)==1
replacement=canonical.replace(before,after,1).replace(kb,ka,1)
for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}']:
 oldids=Counter(re.findall(pattern,canonical));newids=Counter(re.findall(pattern,replacement))
 assert not(oldids-newids),(pattern,oldids-newids)
 extra=newids-oldids
 expected=Counter({'mapsIII:def:completed-cusp-root-data':1}) if 'label' in pattern else Counter({'tag-Q019':1})
 assert extra==expected,(pattern,extra)
assert not any(x['change_id']==changes[-1]['change_id'] for x in ds)
path.write_text(after,newline='\n');kp.write_text(ka,newline='\n');cp.write_text(replacement,newline='\n')
r.write_table(r.DEFECTS,df,ds+changes)
print('UTC',datetime.now(timezone.utc).isoformat());print('EXACT_EDIT_ROWS',len(changes),'EXTENSION_LINES_BEFORE',len(before.splitlines()),'AFTER',len(after.splitlines()));print('ALL_OLD_IDENTITIES_AND_UNSELECTED_BYTES_PRESERVED; ONLY_Q019_NEW; NO_CRITERION_CREDIT')
