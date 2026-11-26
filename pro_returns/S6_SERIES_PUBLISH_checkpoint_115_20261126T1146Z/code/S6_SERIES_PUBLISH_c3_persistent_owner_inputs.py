from S6_SERIES_PUBLISH_c3_edit import *
s=SOURCE.read_text();after=s
old=r'''We record the comparison through each ruling blowdown $\sigma:Z\to Z'$ used below. Put $D'=\sigma_*D_Z$, let $a$ be the coefficient of its exceptional curve $E$ in $D_Z$, and put $d=\operatorname{mult}_{\sigma(E)}D'$. Then
\begin{equation}
 K_Z+D_Z=\sigma^*(K_{Z'}+D')+(1+a-d)E.
 \hypertarget{tag-0093}{}\label{cdp:eq:C.22b}
\end{equation}
Intersection with $E$, using $c_1(K_Z+D_Z)=0$ and $E^2=-1$, gives $a=d-1$. Thus the log-canonical divisor is the exact pullback of $K_{Z'}+D'$, and the latter again has zero rational Chern class.'''
new=r'''For each ruling blowdown $\sigma:Z\to Z'$, apply \cref{lem:II:canonical-boundary-blowup} with $Z_1=Z$, $Z_2=Z'$, $D_1=D_Z$, $D_2=D'=\sigma_*D_Z$, and its multiplicity $m=d=\operatorname{mult}_{\sigma(E)}D'$. Its coefficient $a$ is the coefficient of the same exceptional curve $E$ in $D_Z$. Formula~\eqref{cdp:eq:C.22b} gives $a=d-1$ and identifies $K_Z+D_Z$ with the pullback of $K_{Z'}+D'$, which again has zero rational Chern class.'''
assert after.count(old)==1;after=after.replace(old,new,1)
oldalias=r'\hypertarget{tag-0080}{}\hypertarget{tag-0073}{}\SsixEquationAliases{\label{cdp:eq:A.T.22}\label{cdp:eq:A.RT.11}}'
newalias=r'\hypertarget{tag-0080}{}\hypertarget{tag-0073}{}\hypertarget{tag-0093}{}\SsixEquationAliases{\label{cdp:eq:A.T.22}\label{cdp:eq:A.RT.11}\label{cdp:eq:C.22b}}'
assert after.count(oldalias)==1;after=after.replace(oldalias,newalias,1)
oldcurve=r'''Write its equation as $f=\prod_i f_i$ in the smooth-plane local ring and let $R_i$ and $B_i$ be a branch ring and its normalization. The elements of $R=\OO/(f)$ supported only on branch $i$ form
\[
 \left(\prod_{j\ne i}f_j\right)\bigg|_{f_i}\,R_i.
\]
This equality follows from
$\bigcap_{j\ne i}(f_j)=(\prod_{j\ne i}f_j)$ in that unique
factorization domain. Multiplying by arbitrary elements of
$B_i$ therefore shows that the conductor exponent on branch $i$
is its intrinsic exponent plus $\sum_{j\ne i}I(f_i,f_j)$.
A singular branch has intrinsic exponent at least two:
exponent one would imply $\C+t\C\{t\}=\C\{t\}\subset R_i$.'''
newcurve=r'''Write its reduced equation as $f=\prod_i f_i$, with branch ring $R_i$ and normalization $B_i$. Apply \cref{lem:II:plane-branch-conductor} to this same equation, with its unit equal to one. It gives the conductor exponent $2\delta(f_i)+\sum_{j\ne i}I(f_i,f_j)$ on branch $i$. A singular branch has $\delta(f_i)\ge1$, so its intrinsic exponent is at least two.'''
assert after.count(oldcurve)==1;after=after.replace(oldcurve,newcurve,1)
oldvii=r'''The
Hopf alternative has only smooth elliptic curves, which
are pairwise disjoint. This follows as well from the
explicit contraction description used in \cref{cdp:st:C.3.8} and its
finite unramified quotient: the preimages of two distinct
curves are disjoint elliptic curves, and the quotient
is locally biholomorphic. All assertions are then
immediate on that model.'''
newvii=r'''Lemma~\ref{lem:II:hopf-curves}, applied to this minimal surface $Z_0$, makes its compact curves smooth elliptic and pairwise disjoint. Thus every connected component of $(D_0)_{\rm red}$ has arithmetic genus one and Euler number zero, and there are no rational components on that model.'''
assert after.count(oldvii)==1;after=after.replace(oldvii,newvii,1)
preserve_identifiers(s,after)
for previous,current in zip(identifiers(s),identifiers(after)):
 for label,count in previous.items():assert current[label]==count,label
SOURCE.write_text(after,newline='\n')
for key,statement,prior,receiving,reason in [
 ('BLOWUP','lem:II:persistent-normalization-pullback',old+'\n'+oldalias,new+'\n'+newalias,'The same blowdown, exceptional curve and effective numerically anticanonical divisor satisfy P232. Transfer the exact repeated equation C.22b to its owner with the existing label/target as an alias and give every variable identification in P263.'),
 ('CURVE','lem:II:persistent-normalization-pullback',oldcurve,newcurve,'The same reduced transverse plane equation satisfies the earlier P282. Apply its intrinsic-delta-plus-intersection formula; retain the complete exponent-two cusp ring, tacnode and triple-point classification and all following global arguments.'),
 ('HOPF','cdp:st:C.2.VII.1',oldvii,newvii,'The same Hopf minimal model satisfies P248. Replace the repeated curve comparison by that exact application and explicitly derive the genus/Euler/rational-count conclusions.')]:
 rows=[]
 for i,kind in enumerate(['D12','D14'],1):rows.append(dict(change_id=f'II-C3-PERSISTENT-INPUT-{key}-{i:02}',type=kind,statement_id=statement,old_location='Persistent-normalization and class-VII proofs',old_page='source; final concordance pending',new_location='Earlier common owners and exact applications',new_page='integrated build pending',old_text=prior,new_text=receiving,reason=reason,review_status='Complete original proof read; complete receiving rereading follows; exposed comparison.'))
 print(key,append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))
set_unit_status('lem:II:persistent-normalization-pullback','D12','open','The P232 canonical-boundary and P282 conductor calculations were repeated here. Exact identities have now transferred to their earlier owners; full receiving-unit rereading remains pending.','code/S6_SERIES_PUBLISH_c3_persistent_owner_inputs.py')
add_event('lem:II:persistent-normalization-pullback; cdp:st:C.2.VII.1','II-C3-PERSISTENT-INPUT-TRANSFER','used and rechecked in this run',
 'Root read the complete old P263 and VII.1 proofs before this bounded transfer. The exact point blowdown data identify C.22b with P232 A.RC.5; its original label/tag move once as equation aliases. The identical reduced transverse plane equation applies P282, retaining the singularity classification and all subsequent steps. VII.1 applies P248 to its actual minimal model. P263 D12 reopens for the identified repeated proof until the full receiving unit has been read; no final placement/page gate closes.',
 'S6_SERIES_PUBLISH_II.tex: P263 and VII.1',source='code/S6_SERIES_PUBLISH_c3_persistent_owner_inputs.py')
