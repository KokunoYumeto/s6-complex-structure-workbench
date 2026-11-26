"""Consolidate the smooth class-VII special case into the proved resolution theorem."""
from S6_SERIES_PUBLISH_c3_edit import *

s = SOURCE.read_text()
def block(label, kind='proposition'):
    i=s.index('\\label{'+label+'}',s.index('\\begin{document}'))
    a=s.rfind('\\begin{'+kind+'}',0,i)
    b=s.index('\\end{proof}',i)+len('\\end{proof}')
    return s[a:b]

p23=block('night:P4.23'); p37=block('night:P4.37')
p26=block('night:P4.26'); p21=block('night:P4.21')
p37new=p37
old=r'''\StatementRecord{night:P4.37}{proved}{02XA}{}'''
new=r'''\StatementRecord{night:P4.37}{proved}{02XA}{\cref{cdp:st:C.2.VII.1,night:P4R.6,night:P4.25,night:P4.15,night:P4.36}}
\hypertarget{tag-02WV}{}\label{night:P4.23}\label{stmt:P4.23}
\StatementRecord{night:P4.23}{proved}{02WV}{}'''
assert p37new.count(old)==1; p37new=p37new.replace(old,new,1)
a=p37new.index('The numerically anticanonical classification used in the proofs of')
b=p37new.index('\\item Favre',a)
oldfirst=p37new[a:b]
newfirst=r'''Let $\beta:T\to T_0$ be the minimal-model contraction, and let $D_T$ be the effective integral divisor of \cref{night:P4R.6} for this same $\nu$ and $\sigma$. Its support is $\rho^{-1}(\operatorname{Sing}S)_{\rm red}$ and $K_T+D_T$ is torsion. Apply \cref{cdp:st:C.2.VII.1} to $(Z,D,\sigma)=(T,D_T,\beta)$. It gives the nonzero divisor $D_0=\beta_*D_T$ and the three positive-Betti minimal-model alternatives.

On the Inoue--Hirzebruch and parabolic Inoue alternatives, that proposition makes $D_0$ reduced nodal. At each reverse point blowup, \cref{lem:II:canonical-boundary-blowup}, applied to the successive pushforwards of this same $D_T$, gives exceptional coefficient $\mu-1$ and preserves a reduced normal-crossing boundary. Thus $D_T$ is reduced normal crossing. Its defining residue identity is precisely the one in \cref{night:P4.25}; that proposition gives normal crossings on $S$ and a smooth $N$. The minimal resolution $\sigma$ is therefore an isomorphism. On every normal-crossing chart, $N\to S\hookrightarrow Y$ includes a smooth coordinate plane, so the maximal-minor ideal is the unit ideal. Apply \cref{night:P4.15} to this map, with $\ell=0$, to get $e(T)=K_T^2$.

For the class-VII surface $T$, \cref{lem:II:negative-kodaira-models}\textup{(ii)}, invariance of $\chi(\mathcal O)$ under point blowup, and Noether's formula give
\[
 e(T)=b_2(T)>0,\qquad K_T^2=-b_2(T).
\]
This contradicts the preceding equality. Hence the remaining positive-Betti model $T_0$ is intermediate Kato. Write $n=b_2(T_0)>0$ and let $A_0$ be its maximal reduced curve divisor. Proposition~\ref{cdp:st:C.2.VII.1} identifies $\operatorname{Supp}D_0=A_0$, and $K_{T_0}+D_0$ is torsion.

'''
p37new=p37new[:a]+newfirst+p37new[b:]
old=r'''Blowing up a regular point or one of these saddles
again gives only regular points and saddles with
opposite-sign nonzero eigenvalues. Thus every
blowup centre has the same two possibilities
$\varepsilon=0,1$ as in \cref{night:P4.36}, with the same formulas.'''
new=r'''At a regular point use the two charts of \cref{lem:II:hopf-foliation-blowups}. At a saddle substitute $a=\alpha$, $b=\beta$ into its coordinate calculation. The charts $x=u,y=uv$ and $x=uv,y=v$ give, respectively,
\[
 \beta u\partial_u-(\alpha+\beta)v\partial_v,
 \qquad (\alpha+\beta)u\partial_u-\alpha v\partial_v.
\]
These equalities follow by applying the differential of each displayed blowdown map to its vector field; they hold for the positive real weights here. Every new zero is a saddle with nonzero opposite-sign eigenvalues. The transverse-form orders in those same charts therefore give $\varepsilon=0$ at a regular centre and $\varepsilon=1$ at a saddle, with the canonical and saturation formulas stated below.'''
assert p37new.count(old)==1;p37new=p37new.replace(old,new,1)
old=r'''\item All class-VII cases with positive second Betti
number have now been excluded. The zero-Betti
Inoue case has no conductor curves and was
excluded in the proof of \cref{night:P4.26}.
Proposition~\ref{night:P4.36} treats the remaining
Hopf case and proves the final assertion.'''
new=r'''\item All class-VII cases with positive second Betti number have been excluded. For $b_2(T_0)=0$, the same $D_0$ is a nonzero effective divisor. Apply \cref{lem:II:negative-kodaira-models}\textup{(iii)} to this minimal $T_0$ and its curve $\operatorname{Supp}D_0$; it makes $T_0$ Hopf. Proposition~\ref{night:P4.36}, with the original maps $\nu:N\to S$ and $\sigma:T\to N$, proves that both $\sigma$ and $\beta$ are isomorphisms and gives Euler number zero.'''
assert p37new.count(old)==1;p37new=p37new.replace(old,new,1)
# The identities retain their stable labels but use the paper's equation counter.
for tag,label in [('P4.37.1','eq:class-vii-chern'),('P4.37.2','eq:class-vii-completion')]:
    i=p37new.index('\\tag{'+tag+'}')
    a=p37new.rfind('\\[',0,i);b=p37new.index('\\]',i)+2
    oldeq=p37new[a:b]
    neweq=oldeq.replace('\\[','\\begin{equation}',1).replace('\\]','\\end{equation}',1).replace('\\tag{'+tag+'}','')
    p37new=p37new[:a]+neweq+p37new[b:]

# Expose a conclusion already proved in full in the smooth rational owner.
old=r'''$\nu:T\to S$ be its smooth rational normalization. Then $e(S)>0$.'''
new=r'''$\nu:T\to S$ be its smooth rational normalization. Then $e(S)>0$. A normal-crossing such support has $e(S)=2$.'''
assert p21.count(old)==1;p21new=p21.replace(old,new,1)

# Keep every assertion of P4.26 and apply the consolidated stronger result.
a=p26.index('\\begin{proof}');b=p26.index('\\end{proof}')+len('\\end{proof}')
p26new=p26[:a]+r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item For an irreducible singular support use its normalization $\nu:N\to S$, minimal resolution $\sigma:T\to N$, and composite $\rho=\nu\circ\sigma$. Put
\[
 A=\rho^{-1}(\operatorname{Sing}S)_{\rm red},\qquad
 C=\operatorname{Sing}(S)_{\rm red}.
\]
Proposition~\ref{night:P4R.6} gives an effective integral divisor $D$ with support $A$ and $K_T+D$ torsion. Proposition~\ref{night:P4.12} gives $\kappa(T)=-\infty$. Apply \cref{lem:II:negative-kodaira-models} to a minimal model $T_0$ of this same $T$.

\item First let $T$ be rational. Push $D$ along a chosen minimal-model contraction $\beta:T\to T_0$ to $D_0$. A rational surface has torsion-free Picard group, by the common-resolution pullback in the proof of \cref{night:P4.21}; thus $D_0\sim-K_{T_0}$. Apply the plane-cubic and ruled degree-two enumeration in \eqref{cdp:eq:A.RT.13}--\eqref{cdp:eq:A.RT.16} to this identical pair $(T_0,D_0)$. The incidence argument in the proof of \cref{night:P4.21} uses only these boundary configurations. It gives a connected support: either its fundamental group is trivial and all its normalized components are rational, or $D_0$ is reduced normal crossing.

At each reverse blowup, apply \cref{lem:II:canonical-boundary-blowup,lem:II:boundary-blowup-groups} to the successive pushforwards of this same $D$. The first gives exceptional coefficient $\mu-1$ and preserves the reduced normal-crossing alternative. The second identifies the boundary groups through the actual blowdown and preserves connectedness. Every nonexceptional normalized component is the strict transform of its predecessor, and every added exceptional component is rational. Hence the two alternatives hold for $D$ on $T$.

\item In the reduced normal-crossing alternative, \cref{night:P4.25}, with the residue divisor $D$ just constructed, makes $S$ normal crossing and $N$ smooth. Its minimal resolution is the identity. Proposition~\ref{night:P4.21}, applied to the same smooth rational normalization $\nu:T=N\to S$, gives $e(S)=2$.

In the other alternative, $A$ is connected and simply connected, and $T$ is simply connected. The map $\rho$ identifies $T\setminus A$ with $S\setminus C$. A compatible analytic triangulation makes $A\subset T$ a subcomplex \cite[Theorem~2, p.~464]{Lojasiewicz1964}. Apply \cref{lem:II:proper-conductor-pushout} with $(X,Y,A,C,h)=(T,S,A,C,\rho)$. The inclusion $j:A\hookrightarrow T$ induces an isomorphism of the trivial groups, and the lemma identifies
\[
 \pi_1(S)\simeq\pi_1(C)
\]
through $C\hookrightarrow S$, with inverse on $\pi_1(T)$ given by $(\rho|_A)_*j_*^{-1}$.

Every normalized component of $C$ is rational: it is dominated by a noncontracted normalized component of $A$, and the resulting nonconstant map from $\mathbb P^1$ is finite. The image $C$ is connected. Proposition~\ref{night:P4R.1} makes $\pi_1(C)$ virtually abelian. Apply \cref{lem:II:curve-normalization-graph} to this same curve. If $b$ is its incidence-graph cycle rank and $c\ge1$ its number of components, that lemma gives $b\le1$ and
\[
 e(C)=c+1-b\ge c\ge1.
\]
Proposition~\ref{night:P4.13}, for the same full fibre $mS$, gives $e(S_{\rm reg})\ge0$. Thus $e(S)>0$.

\item For a ruled minimal model of positive base genus, apply \cref{night:P4R.7} to these same $\nu,\sigma$ and $D$ to obtain $e(S)\ge0$. For a class-VII minimal model, \cref{night:P4.37} applies to the same normalization resolution. It excludes the positive-second-Betti case altogether and makes the remaining normalization a smooth minimal Hopf surface with $e(S)=0$. In particular the positive-second-Betti case in the statement has no instance. This covers every singular irreducible support in the minimal-model list.

\item A normal irreducible support is smooth by \cref{night:P4.12}. Use the cyclic base-change map and torus deformation theorem in the final paragraph of the proof of \cref{night:P4.8}, with this full fibre $mS$. They give a finite unramified torus cover of $S$. Multiplicativity under that finite covering gives $e(S)=0$.

\item Normal-crossing supports have the nonnegative even Euler number given by \cref{night:P4.6}. For the final global conclusion, the degree-one Leray injection for this connected-fibre map $f:Y\to B$ in the proof of \cref{night:P4.7} gives $B=\mathbb P^1$. The Euler-additivity calculation in the proof of \cref{cdp:st:C.3.5} applies to this same $f$: the complement of the finitely many critical values is a proper smooth bundle with two-torus fibre and Euler number zero. Consequently
\[
 e(Y)=\sum_{b\in B}e\bigl((f^{-1}(b))_{\rm red}\bigr)\ge0.
\]
Apply \cref{cdp:st:C.1.1} with this $Y$ and $L=\mathcal O_Y$. Its Chern--Gauss--Bonnet and Poincar\'e-duality equalities give $c_3(Y)=e(Y)=2-b_3(Y)$, and its alternating degree-three pairing makes $b_3(Y)$ even. Thus $c_3(Y)\in\{0,2\}$ and $b_3(Y)=2-c_3(Y)$.
\end{enumerate}
\end{proof}'''+p26[b:]

after=s.replace(p23,'',1).replace(p37,'',1).replace(p21,p21new,1).replace(p26,p26new,1)
oldheading=r'\subsection{Excluding the remaining class-VII minimal models}'
assert after.count(oldheading)==1;after=after.replace(oldheading+'\n','',1)
anchor=r'\subsection{Euler numbers with an irrational ruled resolution}'
# The subsection title and theorem title differ; choose the actual next unit.
if anchor not in after:
    p=after.index('\\label{night:P4R.7}',after.index('\\begin{document}'))
    pos=after.rfind('\\subsection{',0,p)
else:
    pos=after.index(anchor)
after=after[:pos]+oldheading+'\n\n'+p37new+'\n\n'+after[pos:]
oldtitle=r'\subsection{Class-VII minimal models with positive second Betti number}'
newtitle=r'\subsection{Anticanonical supports on class VII surfaces}'
assert after.count(oldtitle)==1;after=after.replace(oldtitle,newtitle,1)
oldnav=r'\item \SeriesRef{night:P4.23}\quad Positive Euler number for class VII normalizations.'
assert after.count(oldnav)==1;after=after.replace(oldnav+'\n','',1)
oldnav37=r'\item \SeriesRef{night:P4.37}\quad Class VII minimal models with positive second Betti number.'
newnav37=r'\item \SeriesRef{night:P4.37}\quad Every class VII normalization is a smooth minimal Hopf surface.'
assert after.count(oldnav37)==1;after=after.replace(oldnav37,newnav37,1)
preserve_identifiers(s,after)
for before,current in zip(identifiers(s),identifiers(after)):
    for name,count in before.items():assert current[name]==count,name
SOURCE.write_text(after,newline='\n')

changes=[
 ('CONSOLIDATE',['D12','D14','D22'],'night:P4.23; night:P4.37',p23+'\n'+p37,p37new,
  'The old smooth case maps identically to the stronger normalization-resolution theorem by N=T and sigma=id. The stronger theorem excludes that entire positive-Betti domain and retains its complete foliation, saturated-sheaf Chern identity, integer blowup increment and strict initial quadratic bound. The class-VII alternatives are now excluded directly on the actual R6 divisor using VII.1, P232, P4.25 and P4.15, removing every backward dependency on P4.26. The final zero-Betti clause applies P244 and the unchanged full Hopf theorem on the original maps. Both permanent tags and all labels remain.'),
 ('SADDLE',['D18','D22'],'night:P4.37',oldfirst,newfirst,
  'The initial resolved-divisor application identifies every morphism and residue divisor; the saddle paragraph writes both blowdown differentials explicitly for the positive real weights of the cited foliation. No integer-weight restriction is silently transferred.'),
 ('RATIONAL-CONCLUSION',['D12','D22'],'night:P4.21',p21,p21new,
  'Expose e(S)=2 for normal-crossing supports already proved in step 4 on exactly the original smooth rational normalization data. No proof, hypothesis or existing conclusion changes.'),
 ('CONSUMERS',['D12','D14','D18','D22'],'night:P4.26',p26,p26new,
  'Retain the complete original statement. Replace repeated class-VII and boundary-pushout proofs by the stronger earlier theorem and exact common-owner applications. The rational two-case proof identifies the same boundary under every blowdown, the proper pushout maps including contracted components, and the curve normalization maps. Global Euler/index formulas use their original calculations on identical f and Y.'),
 ('NAVIGATION',['D12','D24'],'night:P4.23; night:P4.37',oldtitle+'\n'+oldnav+'\n'+oldnav37,newtitle+'\n'+newnav37,
  'Place the stronger theorem immediately after its last local input P4.25 and before R7/P4.26; leave VII.1 as its own anticanonical-support unit and one further-results entry.'),
 ('EQUATIONS',['D04','D23'],'night:P4.37',r'\tag{P4.37.1}; \tag{P4.37.2}','Section-numbered equation environments with eq:class-vii-chern and eq:class-vii-completion unchanged',
  'Remove run-coded equation numbers while retaining the exact two formulas and every reference label.')]
rows=[]
for key,kinds,stmt,old,new,reason in changes:
    for i,kind in enumerate(kinds,1):
        rows.append(dict(change_id=f'II-C3-CLASS-VII-{key}-{i:02}',type=kind,statement_id=stmt,
          old_location='Smooth and resolved class VII Euler arguments',old_page='working source; concordance at final build',
          new_location='Class VII exclusion after the reduced resolved-conductor theorem',new_page='integrated build pending',
          old_text=old,new_text=new,reason=reason,
          review_status='Complete original proofs read by root; complete receiving comparison follows; no independent credit.'))
print('Defect rows',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))
fields,rows=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
for row in rows:
    if row['paper']=='II' and row['unit_id']=='night:P4.23':row['unit_title']='Anticanonical supports on class VII surfaces'
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,rows)
for unit in ['night:P4.21','night:P4.23','night:P4.26','night:P4.37']:
    set_unit_status(unit,'D12','open','Consolidated class-VII proof and exact consumers admitted; complete receiving-unit comparison pending.','code/S6_SERIES_PUBLISH_c3_class_vii_owner.py')
add_event('night:P4.23; night:P4.37; night:P4.26; night:P4.21','II-C3-ROOT-CLASS-VII-TRANSFER','used and rechecked in this run',
 'Complete original P4.23, P4.37, P4.26 and P4.21 read. P4.37 is moved before its consumers with direct VII.1/P232/P4.25/P4.15 inputs; N=T,sigma=id gives the exact old smooth specialization. Every old label/target multiplicity is preserved. The full intermediate-Kato Chern proof remains, with explicit positive-real saddle coordinates. P4.26 keeps its original statement and exact rational/proper-pushout/global maps. Full receiving comparison remains to be recorded. No final or independent credit.',
 'S6_SERIES_PUBLISH_II.tex: anticanonical supports, class VII exclusion and irreducible Euler signs',source='code/S6_SERIES_PUBLISH_c3_class_vii_owner.py')
print('Admitted consolidated class-VII theorem; receiving readings pending.')
