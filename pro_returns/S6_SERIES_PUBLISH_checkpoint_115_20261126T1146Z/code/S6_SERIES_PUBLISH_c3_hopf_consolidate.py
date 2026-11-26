from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text()
def block(label,kind='proposition'):
 p=s.index('\\label{'+label+'}',s.index('\\begin{document}'))
 a=s.rfind('\\begin{'+kind+'}',0,p)
 z=s.index('\\end{proof}',p)+len('\\end{proof}')
 return s[a:z]
r5=block('night:P4R.5');strong=block('night:P4.24');r8=block('night:P4R.8')
curve=r'''\begin{lemma}[Curves on a Hopf surface]\hypertarget{tag-P248}{}\label{lem:II:hopf-curves}
\StatementRecord{lem:II:hopf-curves}{proved}{P248}{}
Every irreducible compact curve on a Hopf surface is smooth elliptic and has self-intersection zero. Distinct such curves are disjoint.
\end{lemma}
\begin{proof}
Let $T_0$ be the Hopf surface and $E$ one of its irreducible compact curves. Since $b_2(T_0)=0$, one has $E^2=K_{T_0}\cdot E=0$. Adjunction gives $p_a(E)=1$. A rational normalization would define a nonconstant map $\mathbb P^1\to T_0$. It lifts to the universal cover $\mathbb C^2\setminus\{0\}$, where its two coordinate functions are constant. Thus the normalization genus is one and the sum of the local delta invariants is zero, so $E$ is smooth elliptic. Distinct curves have intersection number zero, whereas each local intersection of two distinct complex curves is positive. They are therefore disjoint.
\end{proof}

\begin{lemma}[A single conductor branch under finite normalization]\hypertarget{tag-P249}{}\label{lem:II:single-conductor-branch}
\StatementRecord{lem:II:single-conductor-branch}{proved}{P249}{}
Let $S$ be a reduced hypersurface in a smooth complex threefold and $\nu:N\to S$ its finite normalization. Suppose that $C=\operatorname{Sing}(S)_{\rm red}$ is a curve and that $A=(\nu^{-1}C)_{\rm red}$ has exactly one local analytic curve branch at each of its points. Then $C$ has exactly one local analytic branch at each point; its distinct irreducible components are disjoint.
\end{lemma}
\begin{proof}
Fix $p\in C$ and two irreducible curve germs $C_1,C_2$ of $C$ at $p$. Choose normalization preimages whose germs of $A$ map onto these two germs. If the preimages coincide, the unique irreducible germ of $A$ there has one irreducible image, giving $C_1=C_2$. Otherwise the two preimages correspond to distinct irreducible analytic surface branches $S_1,S_2$ of $S$ at $p$. In the regular three-dimensional local ring of the ambient manifold, their nonassociate irreducible equations generate an ideal of height two. Their intersection consequently contains a curve germ through $p$. That intersection lies in the conductor image of each surface branch. Its inverse image on each normalization branch is contained in the unique germ of $A$ there, so its image is both $C_1$ and $C_2$. Again $C_1=C_2$. This proves local unibranchness and excludes intersections of distinct global irreducible components.
\end{proof}

'''
newhead=r'''\begin{proposition}[Smooth Hopf normalizations]\hypertarget{tag-02WW}{}\label{night:P4.24}\label{stmt:P4.24}
\StatementRecord{night:P4.24}{proved}{02WW}{\cref{lem:II:hopf-curves,lem:II:single-conductor-branch,lem:II:canonical-boundary-blowup,night:P4.12}}
\hypertarget{tag-02YH}{}\label{night:P4R.5}\label{stmt:P4R.5}
\StatementRecord{night:P4R.5}{proved}{02YH}{\cref{night:P4.24}}
Let $f:Y\to B$ be a proper surjective holomorphic map with connected fibres from a smooth compact complex threefold with $b_1(Y)=b_2(Y)=0$ to a smooth compact curve, with smooth general fibre a complex two-torus. Let $mS$ be a fibre with irreducible, reduced, singular support and smooth normalization $\nu:T\to S$. Suppose that the minimal model of $T$ is Hopf. Then $T$ is already minimal. The reduced conductor on $T$ and its reduced image $C=\operatorname{Sing}(S)_{\rm red}$ are disjoint unions of smooth elliptic curves. Each map between their components is a finite unramified covering, and
\[
 e(S_{\rm reg})=e(C)=e(S)=0.
\]
In particular, the number $k$ of point blowups from the minimal model and the number $v$ of exceptional curves in the conductor are both zero, and the identities $e(S_{\rm reg})=k-v$ and $e(S)=k-v+e(C)$ hold.
\end{proposition}
'''
proof=strong[strong.index('\\begin{proof}'):]
a=r'''Applied to this same minimal
Hopf surface $T_0$, the first step of
\cref{night:P4R.5} proves that its compact irreducible curves
are smooth elliptic and that distinct such curves are disjoint.'''
b=r'''Lemma~\ref{lem:II:hopf-curves}, applied to this same $T_0$, makes every compact irreducible curve smooth elliptic and distinct such curves disjoint.'''
assert a in proof;proof=proof.replace(a,b,1)
a=r'''Apply the
hypersurface-branch argument in the proof of \cref{night:P4R.5}
to the finite normalization $\nu:T\to S\subset Y$: its domain
has exactly one reduced conductor germ at each point, and the
two surface branches over a putative pair of image germs
intersect in a curve germ contained in both images. That
argument identifies the two image germs.'''
b=r'''Apply \cref{lem:II:single-conductor-branch} to the finite normalization $\nu:T\to S\subset Y$. Its inverse image of $C$ is the reduced conductor, which has exactly one smooth germ at each point. The lemma identifies every pair of image germs.'''
assert a in proof;proof=proof.replace(a,b,1)
a=r''' e(S)=e(T)-e(D_{\mathrm{red}})
                 +e(\operatorname{Sing}S)=0.'''
b=r''' e(S_{\rm reg})=e(T)-e(D_{\rm red})=0,
 \qquad e(C)=0,\qquad e(S)=e(S_{\rm reg})+e(C)=0.'''
assert a in proof;proof=proof.replace(a,b,1)
newstrong=curve+newhead+proof
# Preserve the entire stronger proof, transferring only its two repeated prerequisites.
replacement='\\subsection{Smooth Hopf normalizations}\\label{subsec:II:smooth-hopf-normalizations}\n\n'+newstrong
oldunit='\\subsection{Hopf normalizations and the conductor graph}\n\n'+r5
oldstrongunit='\\subsection{Minimality of a smooth Hopf normalization}\n\n'+strong
assert s.count(oldunit)==s.count(oldstrongunit)==1
newsource=s.replace(oldstrongunit,'',1).replace(oldunit,replacement,1)

# The resolved normalization retains the full old rooted-boundary and free-quotient argument.
r8new=r8
a=r'''The Hopf-curve and blowup calculations
in the proof of \cref{night:P4R.5} therefore apply: $A$ has $r\ge1$ connected
components, each a smooth elliptic root
with rational trees attached. Each of its
$v$ rational components came from one of
the $k$ blowups; $e(A)=v$, $e(T)=k$, and
$\rho$ is an isomorphism off $A$. This
proves the displayed formula for the
regular locus.'''
b=r'''Lemma~\ref{lem:II:hopf-curves} makes $(D_0)_{\rm red}$ a union of $r\ge1$ disjoint smooth elliptic curves. At each point blowup, apply \cref{lem:II:canonical-boundary-blowup} to the effective boundary and its pushforward. A centre of multiplicity $\mu$ has exceptional coefficient $\mu-1$. A smooth centre adds a rational leaf precisely when $\mu\ge2$; a node subdivides the corresponding edge. Hence $A$ has $r$ connected components, each a smooth elliptic root with a rational tree attached. Its $v$ rational components have exactly $v$ double points, so $e(A)=v$. Each was created by one of the $k$ point blowups. Since $e(T)=k$ and $\rho$ is an isomorphism off $A$, this proves $e(S_{\rm reg})=k-v\ge0$.'''
assert a in r8new;r8new=r8new.replace(a,b,1)
a=r'''A root which
maps to a point gives the zero
homomorphism on its fundamental group;
a noncontracted root maps through the
normalization of one component of $C$.
Every rational tree is simply connected.
Consequently killing $\pi_1(T)$ and
the normalized component groups of $C$
in the disconnected van Kampen
presentation leaves the free quotient
$F_{b+r-s}$, as in the proof of \cref{night:P4R.5}. Virtual
abelianness gives $b+r-s\le1$, hence'''
b=r'''The associated connected graph has one vertex for $T$ and one for each of the $s$ connected components of $C$, with $r$ edges supplied by the connected components of $A$. Its van Kampen presentation has $r-s$ stable letters in addition to the vertex groups. Each component of $A$ has the group of its elliptic root, since its attached rational tree is simply connected. A contracted root gives the zero homomorphism; a noncontracted root maps through the smooth normalization of one image component. Kill $\pi_1(T)$ and the normal subgroups generated by all normalized component groups of $C$. Every edge-group relation disappears. The normalization graph of $C$ contributes its $b$ free generators, so the remaining quotient is exactly $F_{b+r-s}$. Proposition~\ref{night:P4R.1} makes $\pi_1(S)$ virtually abelian, hence $b+r-s\le1$. Thus'''
assert a in r8new;r8new=r8new.replace(a,b,1)
a=r'''\item Apply the hypersurface-branch argument in the proof of
\cref{night:P4R.5} to the finite normalization $\nu:N\to S\subset Y$.
The preceding step gives its required single conductor germ at
each normalization point, including points under the exceptional
fibres. That argument identifies any two image germs through the
intersection of their surface branches.'''
b=r'''\item Apply \cref{lem:II:single-conductor-branch} to the finite normalization $\nu:N\to S\subset Y$. The preceding step gives its single conductor germ at each normalization point, including those under the exceptional fibres. The lemma identifies every pair of image germs.'''
assert a in r8new;r8new=r8new.replace(a,b,1)
r8new=r8new.replace(r'\SeriesRef{night:P4R.5}, \SeriesRef{night:P4R.6}',r'\SeriesRef{lem:II:hopf-curves}, \SeriesRef{lem:II:single-conductor-branch}, \SeriesRef{night:P4R.6}',1)
assert newsource.count(r8)==1;newsource=newsource.replace(r8,r8new,1)
# The later class-VII application needs only the curve lemma, with no torus-fibre hypotheses.
a=r'Every curve on the minimal Hopf surface $Z$ has square zero, as proved in \cref{night:P4R.5}.'
b=r'Lemma~\ref{lem:II:hopf-curves} gives square zero for every curve on this minimal Hopf surface $Z$.'
assert newsource.count(a)==1;newsource=newsource.replace(a,b,1)
# One further-results entry for the now single result, retaining its two permanent statement identities.
olditem=r'\item \SeriesRef{night:P4R.5}\quad Euler number of a smooth Hopf normalization.'
assert newsource.count(olditem)==1;newsource=newsource.replace(olditem+'\n','',1)
newsource=newsource.replace(r'\item \SeriesRef{night:P4.24}\quad Smooth Hopf normalizations.',r'\item \SeriesRef{night:P4.24}\quad Minimality, conductor coverings and zero Euler number for smooth Hopf normalizations.',1)
preserve_identifiers(s,newsource)
for old,new in zip(identifiers(s),identifiers(newsource)):
 for name,count in old.items():assert new[name]==count,name
SOURCE.write_text(newsource,newline='\n')

edits=[('OWNER',['D12','D14'], 'night:P4R.5; night:P4.24',oldunit+'\n\n'+oldstrongunit,replacement,
 'The identity on (f,Y,B,mS,nu,T) matches the two hypotheses. P4.24 makes k=v=0 and the image elliptic, proving every R5 conclusion. Retain both permanent labels/tags on one complete stronger statement; preserve the full stronger proof, moving its two shared prerequisites to P248/P249. The old graph proof transfers to the proper-resolution setting below.'),
 ('RESOLVED',['D12','D14'],'night:P4R.8',r8,r8new,
 'Transfer the complete rooted-boundary and disconnected van Kampen arguments from R5 to the proper-resolution result that uses them with contracted curves. Apply the exact finite normalization N→S to P249 and the exact minimal Hopf surface to P248. All original R8 conclusions and its exceptional-fibre argument remain.'),
 ('CURVE-USE',['D04','D12'],'cdp:st:C.2.VII.4',a,b,
 'Use the precise general Hopf-curve owner with the identical minimal surface Z, without importing the torus-family hypotheses of the merged stronger result.'),
 ('FURTHER',['D12','D24'],'night:P4.24',olditem+'\n'+r'\item \SeriesRef{night:P4.24}\quad Smooth Hopf normalizations.',r'\item \SeriesRef{night:P4.24}\quad Minimality, conductor coverings and zero Euler number for smooth Hopf normalizations.',
 'The two permanent identities now name the same theorem, so the navigational list describes it once.')]
rows=[]
for key,types,statement,old,new,reason in edits:
 for index,kind in enumerate(types,1):
  rows.append(dict(change_id=f'II-C3-HOPF-CONSOLIDATE-{key}-{index:02}',type=kind,statement_id=statement,old_location='Hopf normalization units',old_page='working source; final concordance pending',new_location='Smooth Hopf normalizations and resolved normalizations',new_page='integrated build pending',old_text=old,new_text=new,reason=reason,review_status='Root complete old proofs read; complete receiving comparison follows. No independent proof credit.'))
print('Defect rows',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))
add_event('night:P4R.5; night:P4.24; night:P4R.8; lem:II:hopf-curves; lem:II:single-conductor-branch','II-C3-HOPF-CONSOLIDATE-TRANSFER','used and rechecked in this run',
 'Read every line of the complete old R5,R8 and P4.24 statements/proofs. The data identity and k=v=0 implication are explicit; both legacy statement tags/labels survive once on the stronger theorem. P248 owns the old curve argument; P249 owns the finite-normalization local-branch argument. The full rooted-tree and free-quotient arguments now stand in R8. The stronger foliation/Chern proof otherwise remains unchanged. Every original label/target multiplicity is preserved. Root receiving comparison remains the next step; no unit or final PDF gate closes here.',
 'S6_SERIES_PUBLISH_II.tex: smooth and resolved Hopf normalization units',source='code/S6_SERIES_PUBLISH_c3_hopf_consolidate.py')
# Both old units migrate to the actual receiving subsection, with open inherited work retained.
path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,progress=read_tsv(path)
oldunits={'night:P4R.5','night:P4.24'}
selected=[x for x in progress if x['paper']=='II' and x['unit_id'] in oldunits]
assert len(selected)==52
progress=[x for x in progress if not(x['paper']=='II' and x['unit_id'] in oldunits)]
for criterion in ['D'+str(i).zfill(2) for i in range(1,26)]+['structure']:
 candidates=[x for x in selected if (x['defect_type'] or x['row_kind'])==criterion];assert len(candidates)==2
 status='done' if all(x['status']=='done' for x in candidates) else 'open'
 progress.append(dict(paper='II',unit_id='subsec:II:smooth-hopf-normalizations',unit_title='Smooth Hopf normalizations',row_kind='structure' if criterion=='structure' else 'defect',defect_type='' if criterion=='structure' else criterion,status=status,date_utc=now(),evidence='code/S6_SERIES_PUBLISH_c3_hopf_consolidate.py',detail='Two original units merged under the identical data and preserved full statements. Receiving review remains pending; this migration supplies no movement credit.'))
write_tsv(path,fields,progress)
print('Merged exact smooth-Hopf scopes; transferred general arguments; receiving read pending.')
