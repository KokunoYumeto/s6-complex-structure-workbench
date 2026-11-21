"""Guarded exact-value and local-expansion editing, after analytic batch A."""
from pathlib import Path
import re,json,hashlib,datetime
B=Path(__file__).parent
base=B/'S6_SERIES_PUBLISH_I_editorial_batch_a_preview.tex'
original=base.read_text();s=original;guards=[];removed=[]
def patch(old,new,reason,ids=()):
 global s
 assert s.count(old)==1,(reason,s.count(old),old[:100])
 guards.append(dict(id=f'IA-B-{len(guards)+1:02}',old=old,new=new,
   expected_count=1,reason=reason,statement_ids=list(ids)))
 s=s.replace(old,new,1)
def block(label,proof=True):
 i=s.index(r'\label{'+label+'}')
 a,env=max((s.rfind(r'\begin{'+e+'}',0,i),e)for e in
 ['proposition','theorem','lemma','cited','remark','corollary'])
 z=s.index(r'\end{'+env+'}',i)+len(r'\end{'+env+'}')
 if proof:
  p=s.find(r'\begin{proof}',z)
  n=re.search(r'\\begin\{(?:proposition|theorem|lemma|cited|remark|corollary)\}',s[z:])
  if p>=0 and (not n or p<z+n.start()):
   z=s.index(r'\end{proof}',p)+len(r'\end{proof}')
 return s[a:z]
def preserve(name,old,reason):
 removed.append(dict(name=name,reason=reason,original=old,sha256=hashlib.sha256(old.encode()).hexdigest()))

# Restore only the operative application of the known Siegel theorem.
old=r'''The expanded source derivation is retained in the proof compendium, Paper~I, label \nolinkurl{ari:C.4.1}.




The Siegel-function identities are those of \citet[Remark~2.2 and Proposition~2.3]{Shin2015}, with the local-height normalization proved explicitly. A complete re-derivation is given in \CompendiumRef{I}{app:rederive:ari-C.4.1}.'''
new=r'''\begin{proof}
Dividing the defining products gives
$g_a=i e^{\pi ia_1v}\vartheta_1(v,\tau)/\eta(\tau)$.
Since $\Im v=a_1\Im\tau$, its absolute value is exactly $N(v,\tau)$.
For a nonintegral rational pair of denominator $n\ge2$,
\cite[Remark~2.2, p.~3, and Proposition~2.3, pp.~3--4]{Shin2015}
gives the modular-unit assertion. Its product has coefficients in
$\mathbb Q(\zeta_n)$ after taking the indicated power; the exponent
$6nB_2(r/n)$ belongs to $n^{-1}\mathbb Z$.

By \cref{ari:C.1.1}, $-\log N$ has mean zero, the logarithmic pole
at $O$, and the Laplacian of the normalized Green function of $(O)$.
The difference of two functions with these properties is harmonic
on the compact torus, and its mean makes the constant zero.
In the Weierstrass coordinate the normalization is
\[
 -\log N(z)-\frac12\log|x(z)|
       \longrightarrow-\frac1{12}\log|\Delta|.
\]
Under the exact homothety
$(\Lambda,z,x,\Delta)\mapsto(c\Lambda,cz,c^{-2}x,c^{-12}\Delta)$,
$N$ is unchanged and both sides of the last comparison change by
$\log|c|$. This proves the stated model transport and the formula
for $D_{\rm part}$.
\end{proof}'''
patch(old,new,'Restore the precise cited modular-unit application and exact local-height normalization; remove dangling compendium pointers.',('ari:C.4.1',))

old=r'''Let $\psi_m$ be the standard division polynomial of a smooth
Weierstrass model, normalized by $\psi_1=1$, $\psi_2=2y$.'''
new=r'''Let $\psi_m$ be the standard division polynomial of a smooth
short Weierstrass model, normalized by $\psi_1=1$, $\psi_2=2y$.
On a general equation
$y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6$, the exact change
$Y=y+(a_1x+a_3)/2$, followed by
$X=x+(a_2+a_1^2/4)/3$, gives a short equation and
$\psi_2=2Y=2y+a_1x+a_3$.
The division functions below are transported by this isomorphism.'''
patch(old,new,'Specify the exact general-model division-function transport used later at 2 and 3.',('ari:C.4.2',))

old=r'''The recursion and all coefficients are checked over $\mathbb Q[t]$
by \path{Cspecial_division.py}. The same program computes
$\gcd(F_n,F_n')=1$ and excludes common factors for proper orders.
Thus no point or multiplicity is omitted.'''
new=r'''The recurrence below gives these identities over $\mathbb Q[t]$.
The Euclidean algorithm gives $\gcd(F_n,F_n')=1$ and excludes
common factors with the polynomials for proper orders. Thus the
listed factors give every point, with its exact order and multiplicity.'''
patch(old,new,'State the exact polynomial algorithm and result in mathematical terms.',('ari:C.4.4',))
patch(r'''product is $11$. The substitution is checked in
\path{Cspecial_relations.py}. The order-four value follows from''',
r'''product is $11$. The order-four value follows from''',
'Remove duplicate program narration; the exact substitution is displayed.',('ari:C.4.4',))
old=r'''Its initial values at $P$ are $\psi_0=0,\psi_1=1,\psi_2=2y$,
$\psi_3=-A^2$, $\psi_4=4y(-8B^2-A^3)$. No approximate algebra
enters this calculation. The same code records $\psi_9$, and the
separate file \texttt{Cspecial\_psi16.out} records the factored
$\psi_{16}$ for the duplication ladder. A rational polynomial
relation for the nonreal order-seven values is explicitly computed
by \path{Cspecial_relations.py}, by the resultant prescription
of \ref{ari:C.4.3}.'''
new=r'''Its initial values at $P$ are $\psi_0=0,\psi_1=1,\psi_2=2y$,
$\psi_3=-A^2$, $\psi_4=4y(-8B^2-A^3)$.
The resultant prescription of \cref{ari:C.4.3} gives a rational
polynomial relation for the nonreal order-seven values.'''
patch(old,new,'Keep the exact recurrence and resultant prescription; move unused higher-step outputs to records.',('ari:C.4.4',))
oldcount=block('ari:C.4.5')
preserve('ari_C4_5_numerical_check',oldcount,'Independent numerical verification of the exact torsion polynomials.')
newcount=r'''\begin{corollary}[The small-order torsion parameters]
\hypertarget{tag-000T}{}\label{ari:C.4.5}
\StatementRecord{ari:C.4.5}{proved}{000T}{\cref{ari:C.4.4}}
The numbers of smooth parameters of exact orders
$2,3,4,5,6,7,8$ are respectively
$0,0,1,2,2,4,4$. Thus there are thirteen parameters in total,
including the two nonreal conjugate parameters of order seven.
\end{corollary}
\begin{proof}
The polynomials in \cref{ari:C.4.4} are squarefree and their
roots have the indicated exact orders. Their degrees give the count.
\end{proof}'''
patch(oldcount,newcount,'Keep the exact counting consequence; archive numerical agreement as verification.',('ari:C.4.5',))

# The derivative identities precede the local expansions which use them.
oldder=block('ari:C.8.11')
newder=oldder.replace('On an ordinary modulus chart put',
 r'On an ordinary modulus chart write $L(\tau)=\log N(\mu(\tau),\tau)$ and put')
newder=newder.replace(r'''These computations independently verify the differential formula used in Proposition~\ref{ari:C.3.2};
its apparent singularity at a half-period is
handled by the root chart rather than division by zero.''',
r'''The formulas involving $1/\wp'(\mu)$ apply where $\wp'(\mu)\ne0$.
The half-period case is treated in the root coordinate of
\cref{ari:C.3.1}.''')
patch(oldder,'','Move the common first-derivative identities before their use in the local expansions.',('ari:C.8.11',))
start=s.index(r'\subsection{The next local terms}')
end=s.index(r'\subsection{CM and torsion}',start)
oldlocal=s[start:end]
newlocal=oldlocal.replace(r'\subsection{The next local terms}',
 r'''\section{Local expansions of the norm}

\subsection{Differential identities}
'''+newder+r'''

\subsection{The square and equianharmonic points}''',1)
newlocal=newlocal.replace(r'''The fresh exact differential-polynomial calculation in
\path{code/continuation_root/ari_C2_C3_fresh.py}
checks all these coefficients and the real quartic polynomial.
Its exact output is retained beside the program; the earlier theta
evaluation diagnostics remain in the computation record.''','')
newlocal=newlocal.replace(r'''\item We rederive the differentiation in Proposition~\ref{push:src:D.4.4}: put
$\ell=\partial_z\log\vartheta_1(\mu,\tau)$,
$a=\operatorname{Im}\mu/T$, $Z=\ell+2\pi ia$, and
$R=\mu'-a$. The theta heat equation and
$\wp=-\partial_z\ell-E$ give on the zero locus
\[
 \mu'=\frac{i\ell}{2\pi}-\frac{ig_2}{6\pi\wp'},\qquad
 R=\frac{iZ}{2\pi}-\frac{ig_2}{6\pi\wp'},\qquad
 \partial_\tau\log N=\frac{Z}{8\pi i}(Z+4\pi iR).
\]
These equations give the factored formula of Proposition~\ref{push:src:D.4.4}
with its stated normalizations. At $\rho$ the unit endomorphism fixing the''',
r'''\item Use the notation of \cref{ari:C.8.11}, with
$\ell=\partial_z\log\vartheta_1(\mu,\tau)$ and $Z=W$.
The differential identities proved there apply to the zero locus.
At $\rho$ the unit endomorphism fixing the''')
newlocal=newlocal.replace(r'''\begin{proposition}[the equianharmonic point is neither an extremum]''',
r'''\begin{proposition}[The equianharmonic expansion]''')
patch(oldlocal,'','Move local expansions before the local-maximum and division-ladder arguments.',('ari:C.3.1','ari:C.3.2'))
anchor=r'\section{An analytic proof of the elliptic maximum}'
patch(anchor,newlocal+'\n'+anchor,'Insert derivative identities and local expansions in dependency order.',('ari:C.8.11','ari:C.3.1','ari:C.3.2'))

# Remove obsolete computational narration from the unchanged exact ladder.
old=r'''All operations are rational polynomial operations;
\path{code/C_ladder_algebra.py} reproduces them and records
the next two steps as well. The general identity is \ref{ari:C.4.2}.'''
new=r'''These are rational polynomial operations using the recurrence in
\cref{ari:C.4.4}. The general identity is \cref{ari:C.4.2}.'''
patch(old,new,'Retain the full ladder algorithm without file and output narration.',('ari:C.8.4',))
patch(r'''Thus the decimal diagnostics
in the accompanying programs are dispensable.''','',
'Remove diagnostic discussion from the scalar-bound proof.',('ari:C.8.1',))
patch(r'''For the cusp we check directly the analytic step of supplied K6.''',
r'''For the cusp use the Fourier expansion of $\wp$.''',
'Remove unresolved run/item reference.',('ari:C.8.1',))
patch(r'''without using any certificate from K6.''',r'''on the whole cusp region.''',
'State the mathematical scope.',('ari:C.8.1',))
patch(r'''This is a rational inequality on one disc,
not a subdivision or a root search.''',r'''The bound holds on the whole disc.''',
'Remove comparison with verification methods.',('ari:C.8.4',))

out=dict(source_path=str(base),source_sha256=hashlib.sha256(original.encode()).hexdigest(),
 generated_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 requires_batch='S6_SERIES_PUBLISH_I_editorial_batch_a_guards.json',guards=guards)
(B/'S6_SERIES_PUBLISH_I_editorial_batch_b_guards.json').write_text(json.dumps(out,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_b_removed.json').write_text(json.dumps(removed,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_b_preview.tex').write_text(s)
print(json.dumps({'guards':len(guards),'removed_blocks':len(removed),'preview_sha256':hashlib.sha256(s.encode()).hexdigest()},indent=2))
