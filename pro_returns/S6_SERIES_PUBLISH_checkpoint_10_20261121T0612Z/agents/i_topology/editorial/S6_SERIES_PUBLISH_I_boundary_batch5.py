from pathlib import Path
import re,json,hashlib,datetime
P=Path(__file__).resolve().parent
initial=Path('work/S6_SERIES_PUBLISH_I.tex').read_text();s=initial;patches=[];archive=[]
def patch(old,new,reason,ids):
 global s
 ident='I-topology5-%02d'%(len(patches)+1)
 assert s.count(old)==1,(ident,s.count(old),old[:120])
 patches.append(dict(id=ident,old=old,new=new,reason=reason,statement_ids=ids));s=s.replace(old,new,1)
def span(label,next_marker):
 i=s.index('\\label{'+label+'}');a=s.rfind('\\begin{',0,i);b=s.index(next_marker,i);return s[a:b]
old=span('push:src:C.3.5','\\begin{figure}')
archive.append(dict(statement_id='push:src:C.3.5',original_block=old))
statement=old[:old.index('\\end{cited}')+len('\\end{cited}')]
statement=statement.replace('\\begin{cited}', '\\begin{proposition}').replace('\\end{cited}','\\end{proposition}')
statement=statement.replace(r'''with $w=e^{-\pi i c}$ and positive loops in the $w$-plane. This computes the closing
cocycle, not the mapping class of its composition with parallel
transport. In particular it does not imply \(6[\Phi]=0\).''',r'''with $w=e^{-\pi i c}$ and positive loops in the $w$-plane. For parallel transport $P:X_{c_0}\to X_{c_0-12}$ along this lifted path, the resulting six-loop diffeomorphism is $\widetilde F_{12,c_0-12}\circ P$.''')
j=json.loads((P.parent/'S6_SERIES_PUBLISH_I_actual_rederivations_first_open.json').read_text())
proof=j['extracts']['app:rederive:push-src-C.3.5'];proof=proof[proof.index('\\begin{proof}'):].strip()
a=proof.index('The raw formula');b=proof.index('The global roots')
proof=proof[:a]+r'''The even-shift translation and its quadratic correction are those of \citet[Proposition~7.8, pp.~91--92, and Proposition~C.2, p.~102]{DuEtAl2026v1}. Their representatives in the fixed root and cusp charts are as follows.
'''+proof[b:]
proof=proof.replace('Thus no real\ninterpolation of a multivalued period has been used.','')
proof=proof.replace(r'''Any difference from the fixed even-shift choice of Proposition~\ref{fam:src:A.3.1} is a scalar automorphism,
which lies in its connected $\mathbb C^*$ by Proposition~\ref{fam:src:B.4.1}. The choice therefore
has the same smooth monodromy class.''',r'''Composing this even-shift map with the inverse of the fixed choice in Proposition~\ref{fam:src:A.3.1} gives an automorphism over the identity of the base. The full automorphism theorem, Theorem~\ref{night:P5.5}, identifies it with a scalar in $\mathbb C^*$. A path from that scalar to $1$ supplies an isotopy, so the two closing choices define the same smooth monodromy class.''')
proof=proof.replace(r'''They need not be
replaced by one.''','')
proof=proof.replace(r'''In particular the scalar representative's pole is not
an obstruction to the holomorphic map itself: its unit
representative already extends.''',r'''The extending map is represented by $U_{12,c}$, and the displayed deck multiplier identifies it with the scalar representative on the punctured chart.''')
a=proof.index('Finally \\(w=e^{-\\pi i c}');proof=proof[:a]+r'''Finally \(w=e^{-\pi i c}\) makes six positive loops the path
\(c(r)=c_0-12r\); its endpoint is closed by the positive shift
\(h=12\). For parallel transport $P$ along that path the closed diffeomorphism is therefore $\widetilde F_{12,c_0-12}\circ P$. The overlap difference between the scalar logarithm and the two-coordinate unit logarithm is exactly $\Pi_c\widehat\gamma$. Scaling both logarithms by a real number $a$ changes this difference to $a\Pi_c\widehat\gamma$. For $0<a<1$, this vector is not a period: the real period map is an isomorphism and $a\widehat\gamma\notin\Lambda$. Thus the separately scaled chart maps fail the overlap equation at precisely this fractional period.
\end{proof}'''
patch(old,statement+'\n\n'+proof+'\n\n','Restore the complete canonical closing application from the attached full derivation, retaining every finite/cusp comparison and giving the exact parallel-transport composition; remove dead compendium navigation.',['push:src:C.3.5'])
old=span('push:src:B.4.3','\\begin{theorem}[The obstruction on normalization components]')
archive.append(dict(statement_id='push:src:B.4.3',original_block=old))
statement=old[:old.index('\\end{cited}')+len('\\end{cited}')]
statement=statement.replace('\\begin{cited}[consequences with explicit derivation]','\\begin{theorem}[The Hodge obstruction to normal-crossing limits]').replace('\\end{cited}','\\end{theorem}')
proof=r'''\begin{proof}
Proposition~\ref{push:src:B.4.2} gives a surjection from the fundamental group of a nearby fibre onto $\pi_1(D)$. Since that fibre is diffeomorphic to $S^6$, it follows that $\pi_1(D)=1$ and $H^1(D;\mathbb C)=0$.

For a compact complex threefold $X$ diffeomorphic to $S^6$, the groups $H^2(X;\mathbb Z)$ and $H^4(X;\mathbb Z)$ vanish, so $c_1(X)=c_2(X)=0$. The analytic Riemann--Roch formula, obtained from \citet[Theorem~4.3, pp.~564--565]{AtiyahSinger1968IIIE}, gives
\[
 \chi(X,\mathcal O_X)=\frac1{24}\langle c_1(X)c_2(X),[X]\rangle=0.
\]
Every holomorphic three-form $\Omega$ is closed and is exact because $H^3(X;\mathbb C)=0$. Stokes' theorem gives $\int_X i\Omega\wedge\overline\Omega=0$. The integrand is pointwise nonnegative for the complex orientation, so $\Omega=0$. Serre duality therefore gives $h^3(X,\mathcal O_X)=0$, and connectedness gives $h^0(X,\mathcal O_X)=1$. Hence
\[
 h^1(X,\mathcal O_X)=1+h^2(X,\mathcal O_X)\geq1.
\]
Locally along the reduced normal-crossing divisor, $g$ has the form $s=z_1\cdots z_k$ after absorbing a holomorphic unit. This makes $\mathcal O_{\mathcal Z}$ torsion-free over the local discrete valuation ring of the disc and hence flat over it. Upper semicontinuity for the proper flat map gives $h^1(D,\mathcal O_D)\geq1$; see \citet[\S7, Satz~5, pp.~63--64]{Grauert1960D}.

For a proper complex algebraic variety with Du Bois singularities, the canonical map from singular cohomology to coherent cohomology is surjective in every degree; see \citet[\S1.D, p.~120]{GrafKovacs2014Root}. Normal-crossing singularities are Du Bois, including self-intersections of a global component. Thus algebraicity and properness of $D$ would make $H^1(D;\mathbb C)\to H^1(D,\mathcal O_D)$ surjective, contradicting the two groups just computed.

Now suppose $D$ is simple normal crossing and each nonempty closed stratum satisfies the $\partial\bar\partial$-lemma. These are exactly the strata in condition (K1) of \citet[Definition~2.3, p.~9]{Chen2026HodgeRoot}. For a proper semistable degeneration with smooth total space and this condition, \citet[Theorem~2.4(4), p.~10]{Chen2026HodgeRoot} gives $E_1$ degeneration of the Hodge--de Rham spectral sequence on a nearby fibre. In total degree one this yields
\[
 0=b_1(X_s)=h^0(X_s,\Omega^1_{X_s})+h^1(X_s,\mathcal O_{X_s})\geq1,
\]
a contradiction.

A closed smooth submanifold of a compact K\"ahler manifold is K\"ahler. A closed stratum of a Moishezon component is also Moishezon: choose a projective modification, take a component of the inverse image dominating the stratum, and intersect with general relative hyperplanes until the induced proper map is generically finite. This gives a generically finite projective cover and hence maximal algebraic dimension for the stratum. Smooth Moishezon manifolds satisfy the $\partial\bar\partial$-lemma, as recalled in \citet[\S2.1, p.~8]{Chen2026HodgeRoot}. Either stated hypothesis on the irreducible components therefore gives condition (K1), proving the last assertion. A finite parameter cover preserves the biholomorphism type of every nonzero fibre, so the argument applies for every $N\geq1$.
\end{proof}
'''
patch(old,statement+'\n\n'+proof+'\n','Restore the full RR/Stokes, semicontinuity, Du Bois and closed-stratum application; use already verified exact primary locators; consolidate duplicate root-image lower bound and misplaced marked-map scope paragraphs.',['push:src:B.4.3'])
old=span('push:src:D.4.6','\\begin{proposition}[Nonvanishing near the elliptic points and cusp]')
archive.append(dict(statement_id='push:src:D.4.6',original_block=old))
new=r'''\begin{remark}[The Green-function pullback along the moving zero]\hypertarget{tag-032O}{}\label{push:src:D.4.6}
\StatementRecord{push:src:D.4.6}{proved}{032O}{\SeriesRef{push:src:D.4.4}, \SeriesRef{push:src:D.4.5}, \SeriesRef{push:src:D.4.7}, \SeriesRef{push:src:D.4.8}; \citet[equation~(1.1), p.~912, and Lemma~2.3, p.~919]{LinWang2010}}
For a fixed modulus $\tau$, let
\[
 G_\tau(z)=-\frac1{2\pi}\log\mathcal N(z,\tau),\qquad
 Z(z,\tau)=\partial_z\log\vartheta_1(z,\tau)
                 +2\pi i\frac{\operatorname{Im}z}{\operatorname{Im}\tau}.
\]
The normalization proved in Proposition~\ref{push:src:D.4.5} gives the zero-mean Green function, and differentiation gives
\[
 \partial_zG_\tau(z)=-\frac{Z(z,\tau)}{4\pi}.
\]
This is the critical equation of \citet[equation~(1.1), p.~912, and Lemma~2.3, p.~919]{LinWang2010}. The section of the universal elliptic curve used here is
$\iota(\tau)=(\mu(\tau),\tau)$, with $\wp_\tau(\mu(\tau))=0$, and its exact pullback is
\[
 D_{\rm part}(\tau)=-12G_\tau(\mu(\tau))
                  -\frac6\pi\log(2\sqrt3).
\]
Along this section, Proposition~\ref{push:src:D.4.4} computes the full derivative, including the variation of $\tau$:
\[
 \partial_\tau D_{\rm part}
   =\frac{iZ}{4\pi^2P}(3ZP-2g_2),\qquad P=\wp'_\tau(\mu).
\]
Thus the two factors controlling the level curves on ordinary charts are the pullback of the fixed-modulus critical factor $Z$ and the additional factor $3ZP-2g_2$. Propositions~\ref{push:src:D.4.7} and~\ref{push:src:D.4.8} supply their nonvanishing and boundary estimates; Proposition~\ref{push:src:D.4.5} gives the coarse equianharmonic crossing.
\end{remark}

'''
patch(old,new,'Replace the literature/process contrast by the exact Green normalization, section map, pullback and full moving-modulus derivative; preserve tag032O and remove dead navigation.',['push:src:D.4.6'])
patch('and the nearby value $h^1(\\mathcal O)=1$ in \\ref{push:src:B.4.3}', 'and the nearby lower bound $h^1(\\mathcal O)\\geq1$ in \\ref{push:src:B.4.3}', 'Use the exact sufficient RR lower bound furnished by the restored B4.3 proof; the full value one remains in the structure-sheaf and Hodge-table calculations.', ['push:src:B.4.6'])
# Every old anchor must remain with exactly the same multiplicity.
pat=r'\\(?:label|hypertarget)\{([^}]+)\}'
from collections import Counter
oldanchors=Counter(re.findall(pat,initial));newanchors=Counter(re.findall(pat,s));lost={k:(v,newanchors[k]) for k,v in oldanchors.items() if newanchors[k]!=v}
assert not lost,lost
result={'input_sha256':hashlib.sha256(initial.encode()).hexdigest(),'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'patches':patches,'anchor_check':{'old_anchor_count':sum(oldanchors.values()),'all_preserved':True},'size_change_characters':len(s)-len(initial)}
(P/'S6_SERIES_PUBLISH_I_boundary_batch5_guarded.json').write_text(json.dumps(result,indent=2)+'\n')
(P/'S6_SERIES_PUBLISH_I_boundary_batch5_preview.tex').write_text(s)
(P/'S6_SERIES_PUBLISH_I_boundary_batch5_archived_proofs.json').write_text(json.dumps(archive,indent=2)+'\n')
print('guards',len(patches),'added characters',len(s)-len(initial),'input',result['input_sha256'])
