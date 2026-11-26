"""Give the conormal calculation and triple-conductor algebra single owners."""
from S6_SERIES_PUBLISH_c3_edit import *

def block(text,label):
    i=text.index(r'\label{'+label+'}')
    a=text.rfind(r'\begin{proposition}',0,i)
    b=text.index(r'\end{proof}',i)+len(r'\end{proof}')
    return text[a:b]
def items(text):
    a=text.index(r'\begin{enumerate}')
    a=text.index(r'\item',a)
    b=text.index(r'\end{enumerate}',a)
    return [r'\item'+v for v in text[a:b].split(r'\item')[1:]]

s=SOURCE.read_text()
old30=block(s,'night:P4.30');old31=block(s,'night:P4.31');old34=block(s,'night:P4.34')
parts34=items(old34);assert len(parts34)==9
generic=old31[old31.index('At a generic ordinary triple point'):old31.index(r'\item Consequently')].strip()
assert generic.endswith('The conductor is exactly $(x,y)^2$.')

conormal=r'''\begin{lemma}[Conormal defects of compact curves]\hypertarget{tag-P254}{}\label{lem:II:rational-conormal-defects}
\StatementRecord{lem:II:rational-conormal-defects}{proved}{P254}{\cref{lem:II:plane-branch-conductor}}
Let $C$ be a compact irreducible reduced curve in a smooth complex threefold $Y$, with normalization $\nu_C:E\to C$, inclusion $i:C\hookrightarrow Y$ and $j=i\nu_C$. Let $g$ be the genus of $E$, and suppose $\deg j^*\Omega_Y=0$. Write $P$ for the ideal of $C$ and $P^{(2)}$ for the functions vanishing to order at least two along every local generic branch. Put
\[
 K=\ker(j^*\Omega_Y\to\Omega_E),\qquad
 \operatorname{im}(dj)=\Omega_E(-R),\qquad Q=P/P^{(2)}.
\]
Differentiation embeds $Q$ in $j_*K$. At $p\in C$ let $\tau_p$ be the length of $j_*K/Q$, let $r_p$ be the sum of the coefficients of $R$ above $p$, and put $d_p=\delta(C,p)+\tau_p-r_p$. Then
\[
 \chi(\mathcal O_Y/P^{(2)})=5(1-g)-\sum_p d_p.
\]
At a smooth point $d_p=0$. At a planar point $d_p=5\delta(C,p)$, so an ordinary node has $d_p=5$. At a nonplanar point with at most two analytic branches, $d_p\ge7$.
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Dividing the derivative row on $E$ by its common zeros gives a surjection onto the line bundle $\Omega_E(-R)$. Its kernel $K$ is locally free of rank two and is a direct summand in a local frame of $j^*\Omega_Y$. The degree hypothesis gives
\[
 \deg K=2-2g+\deg R.
\]
Differentiation of a defining function gives its normal derivative along each generic smooth branch of $C$. Its kernel in $P$ is exactly $P^{(2)}$. A section of $Q$ killed away from finitely many points has zero generic derivative on every branch and is therefore zero. Thus the resulting map $Q\to j_*K$ is injective, and its cokernel has finite length $\tau=\sum_p\tau_p$. Riemann--Roch on $E$ gives
\[
 \chi(Q)=4(1-g)+\deg R-\tau.
\]
The normalization sequence gives $\chi(\mathcal O_C)=1-g-\sum_p\delta(C,p)$. Applying Euler additivity to
\[
 0\longrightarrow Q\longrightarrow\mathcal O_Y/P^{(2)}
   \longrightarrow\mathcal O_C\longrightarrow0
\]
proves the formula. For $E=\mathbb P^1$ it reads $5-\sum_p d_p$; for an elliptic $E$ its constant term is zero.

\item On each normalized branch choose a parameter $t$ and ambient coordinates vanishing at its image. If $m=\min_i\operatorname{ord}_t x_i(t)$, the common order of the derivative entries is $m-1$. This is the coefficient of $R$. A generator of $\bigwedge^2K$ has a unit Pl\"ucker coordinate because $K$ is saturated in the free ambient rank-three module. Let $L$ be the $\mathbb C\{t\}$-span of the differentiated defining equations. The elementary-divisor decomposition of this rank-two lattice gives
\[
 \operatorname{length}(K/L)=
 \min\operatorname{ord}_t\{	ext{two-by-two gradient minors}\}.
\]
Over all branches above $p$, the inclusions are
$Q\subset(\nu_C)_*L\subset j_*K$. Their finite quotient lengths are complex dimensions, so $\tau_p$ is at least the sum of these branchwise lattice lengths. At an embedding-dimension-three point every defining equation has no linear term. Each gradient entry then has order at least $m$ on this branch, and its two-by-two minors have order at least $2m$.
At a smooth point $m=1$, differentiation identifies the free conormal module with $K$, giving $R=0$, $\tau_p=0$ and $d_p=0$.

'''+parts34[3]+parts34[4].replace('As in \cref{night:P4.30},','By the gradient-lattice calculation above,')+parts34[5]+parts34[6]+r'''
\end{enumerate}
\end{proof}

'''

triple=r'''\begin{lemma}[Primary ordinary-triple conductor schemes]\hypertarget{tag-P256}{}\label{lem:II:triple-conductor-symbolic-square}
\StatementRecord{lem:II:triple-conductor-symbolic-square}{proved}{P256}{\cref{lem:II:conductor-duality}}
Let $S$ be a reduced hypersurface in a smooth complex threefold $Y$, with finite normalization $\nu:N\to S$. Let $C$ be an irreducible curve component of its reduced image conductor, and suppose that its generic transverse germ is the ordinary triple point $xy(x-y)=0$. Write $P\subset\mathcal O_Y$ for the reduced ideal of $C$. The ambient ideal of the primary image conductor component supported on $C$ is $P^{(2)}$, taking order two on every local analytic branch of $C$. This also identifies the full image conductor scheme when $C$ is its whole reduced support.
\end{lemma}
\begin{proof}
Apply \cref{lem:II:conductor-duality} to this finite normalization. The image conductor is Cohen--Macaulay of pure dimension one. Its primary component along $C$ is obtained by intersecting the isolated primary ideals belonging to all local minimal primes of $C$. These ideals glue by their unique localization-and-contraction characterization. The quotient by their intersection injects into the direct sum of their primary quotients. Its associated primes are therefore among these one-dimensional minimal primes; it has no finite-support submodule and has depth one. Write $J$ for this ambient component ideal.

'''+generic+r'''

Consequently $J_{\mathfrak p}=P_{\mathfrak p}^{,2}$ at every local minimal prime $\mathfrak p$ of $C$. This gives $J\subset P^{(2)}$. A section of $P^{(2)}/J$ vanishes at all these generic points and hence has finite support. Depth one of $\mathcal O_Y/J$ makes that submodule zero. Thus $J=P^{(2)}$ at every point, including multibranch self-identifications of the global curve $C$.
\end{proof}

'''

# The local plane calculation also records the primitive-gradient estimate
# formerly used separately in the elliptic special case.
needle='Write $r_i$ for the coefficient of $R$ on that branch.'
assert conormal.count(needle)==1
conormal=conormal.replace(needle,needle+r''' The primitive plane kernel has a unit coefficient. At a singular unibranch point of multiplicity $m$, both entries of $dh$ have order at least $m$, so $v_i\ge m$; its conormal lattice quotient has at least that length. This is the same branchwise normal-derivative map used above.''')
new30=old30[:old30.index(r'\begin{proof}')]+r'''\begin{proof}
Apply \cref{lem:II:rational-conormal-defects} with this same $Y,C,E$ and $j=i\nu$. The normalization has genus one, and $b_2(Y)=0$ gives $\deg j^*\Omega_Y=0$. Its formula is
\[
 \chi(\mathcal O_Y/P^{(2)})=-\sum_p d_p.
\]
Every point is unibranch. A singular planar point has $d_p=5\delta(C,p)>0$, and a nonplanar point has $d_p\ge7$; smooth points have $d_p=0$. The sum is therefore nonpositive, with equality precisely when every normalization defect vanishes. Then $\nu:E\to C$ is an isomorphism and $C$ is smooth.
\end{proof}'''
apply_edit(old30,conormal+triple+new30,
 'II-C3-CONORMAL-SINGLE-OWNERS',['D12','D14','D20','D22'],
 'lem:II:rational-conormal-defects; lem:II:triple-conductor-symbolic-square; night:P4.30; night:P4.34',
 'Conormal calculation before the elliptic and triple equality applications',
 'Transfer the full derivative/lattice and local defect proofs into one genus-g calculation. The explicit substitution g=1 proves the unchanged elliptic statement, and g=0 preserves every rational formula. Transfer the full generic triple-vector and depth proof into its primary-component owner.',
 'Complete original P4.30/P4.31/P4.34 proofs read by root; receiving full proof comparison follows admission. No independent credit.')

parts31=items(old31);assert len(parts31)==7
new31=old31[:old31.index(r'\begin{proof}')]+r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
'''+parts31[0]+r'''\item Let $C_{\rm sch}$ be the image conductor scheme and $P\subset\mathcal O_Y$ the reduced ideal of $C$. Apply \cref{lem:II:triple-conductor-symbolic-square} to this same finite normalization $\nu:N\to S$. The common reduction has made $C$ the whole irreducible image support, and its generic transverse germ is the stated ordinary triple point. Thus
\[
 \mathcal O_{C_{\rm sch}}=\mathcal O_Y/P^{(2)}.
\]
The equality includes all special points of $C$.

'''+''.join(parts31[3:])+r'''\end{enumerate}
\end{proof}'''
apply_edit(old31,new31,'II-C3-TRIPLE-EQUALITY-COMMON-SCHEME',['D12','D22'],
 'night:P4.31','Full ordinary-triple equality proof',
 'The complete generic branch-vector and depth-one calculation is now P256. Apply it to the identical finite normalization and whole conductor curve; all subsequent Euler, branch, regularity and coordinate arguments remain.',
 'Complete original proof read; every transferred formula is retained in P256; remaining proof items are byte-identical.')

oldheading=r'\subsection{The value one in the rational ordinary-triple sector}'
anchor=r'\StatementRecord{night:P4.35}{proved}{02X8}{}'
alias=anchor+'\n'+r'\hypertarget{tag-02X7}{}\label{night:P4.34}\label{stmt:P4.34}'+'\n'+r'\StatementRecord{night:P4.34}{proved}{02X7}{}'
current=SOURCE.read_text()
a=current.index(oldheading);b=current.index(anchor,a)+len(anchor)
combined=current[a:b]
assert combined.count(oldheading+'\n\n'+old34)==1
receiving=combined.replace(oldheading+'\n\n'+old34,'',1).replace(anchor,alias,1)
apply_edit(combined,receiving,'II-C3-TRIPLE-RATIONAL-ALIAS',['D12','D14'],
 'night:P4.34; night:P4.35','Rational ordinary-triple special case and stronger Euler owner',
 'The full special-case Euler conclusion follows from P4.35 by the identity map on f,Y,mS,nu and its rational resolution. Its full conormal derivation is retained in P254 and its conductor scheme calculation in P256. Keep the original P4.34 permanent tag and labels on the unchanged stronger theorem. The superseded complete special-case proof remains verbatim in this defect record, with no independent credit.',
 'Complete original P4.34 and stronger P4.35 proofs read; exact identity-domain implication checked. Every old identifier is retained in this single guarded move.')
apply_edit(r'\item \SeriesRef{night:P4.34}\quad Rational supports with ordinary triple curves.'+'\n','',
 'II-C3-TRIPLE-FURTHER-RESULT-ALIAS',['D12','D24'],'night:P4.34','Further results',
 'Remove the duplicated special-case listing; P4.35 is the single stronger Euler owner.',
 'Both statement scopes and the exact identity-data inclusion read.')
anchor=r'\item \SeriesRef{night:P4.30}\quad Symbolic double of a unibranch elliptic curve.'
new=r'\item \cref{lem:II:rational-conormal-defects}\quad Conormal defects of compact curves.'+'\n'+r'\item \cref{lem:II:triple-conductor-symbolic-square}\quad Primary ordinary-triple conductor schemes.'+'\n'+anchor
apply_edit(anchor,new,'II-C3-CONORMAL-FURTHER-RESULTS',['D24'],
 'lem:II:rational-conormal-defects; lem:II:triple-conductor-symbolic-square','Further results',
 'List the two common mathematical owners at their actual conclusions.',
 'New proved statements and their receiving applications compared.')
for old,new in [
 (r'Triple conductor and rational conormal Euler identity (\cref{night:P4.34})',r'Triple conductor and rational conormal Euler identity (\cref{lem:II:triple-conductor-symbolic-square,lem:II:rational-conormal-defects})'),
 (r'Local conductor defects and gradient minors (\cref{night:P4.34})',r'Local conductor defects and gradient minors (\cref{lem:II:rational-conormal-defects})')]:
    apply_edit(old,new,'II-C3-CONORMAL-PROGRAM-OWNER-'+str(1 if 'Euler' in old else 2),['D24'],
      'night:P4.34; lem:II:rational-conormal-defects','Programs table',
      'The unchanged program paths now point to the owners of their full printed calculations.',
      'Complete original and receiving mathematical calculations and appendix context read.')
for unit in ['night:P4.30','night:P4.35']:
    set_unit_status(unit,'D12','open','Single-owner transfer admitted; full receiving comparison is pending.','code/S6_SERIES_PUBLISH_c3_conormal_owners.py')
path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv'
fields,rows=read_tsv(path)
removed=[r for r in rows if r['paper']=='II' and r['unit_id']=='night:P4.34']
assert len(removed)==26
rows=[r for r in rows if r not in removed]
for row in rows:
    if row['paper']=='II' and row['unit_id']=='night:P4.30':
        row['detail']+=' The former P4.34 conormal material is now in this subsection through P254/P256; its Euler subcase is an alias of P4.35. Unit migration gives no movement credit.'
write_tsv(path,fields,rows)
for old,new in zip(identifiers(s),identifiers(SOURCE.read_text())):
    for name,count in old.items():assert new[name]==count,name
print('P254/P256 and the exact Euler alias admitted; receiving comparisons and remaining owner-reference transfers are pending.')
