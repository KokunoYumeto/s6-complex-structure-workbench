"""Present the actual three-filling datum and its complete cellular comparison."""
from datetime import datetime,timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
df,rows=r.table(r.DEFECTS)
changes=[];prepared={}
def transform(key):
 path=u.WORK/'root'/(key+'.tex');before=path.read_text(encoding='utf-8');after=before
 def edit(suffix,kind,label,old,new,reason):
  nonlocal after
  assert after.count(old)==1,(key,suffix,after.count(old))
  after=after.replace(old,new,1)
  ident='III-C8-CELL-'+suffix
  assert not any(x['change_id']==ident for x in rows)
  changes.append(dict(change_id=ident,type=kind,statement_id=label,old_location=key+' before complete publication rewrite',old_page='pending page concordance',new_location=key+' after exact map comparison',new_page='pending final PDF',old_text=old,new_text=new,reason=reason,review_status='exact edit applied; whole edited proof reading pending'))
 if key=='common_conventions':
  edit('DECK-MATRICES','D20','mapsIII:def:marked-family',
   'The homology transport matrices are $A_1,A_2,M_0$, with',
   'The fibre-linear matrices of the analytic deck generators are\\n$A_1,A_2,M_0$, with'.replace('\\n','\n'),
   'Specify the actual map represented by each existing matrix. The exact roof reversal, conjugation and point-return maps are printed in the cell datum; the map-specific dual formula in Q001 is unchanged.')
 else:
  heading=after[:after.index(r'\begin{theorem}')]
  oldroof=heading[heading.index('For a matrix $A$'):heading.index('The positive interval')]
  newheading=r'''\subsection{A cell presentation from the three fillings}

\begin{definition}[The marked three-filling datum]
\hypertarget{tag-Q016}{}\label{mapsIII:def:three-filling-datum}
{\normalfont\scriptsize tag Q016}\par
Use Definition~\ref{mapsIII:def:marked-family} with $p=-1$,
\[
 (g,u,w,d)=(\widehat\gamma,\widehat u,\widehat w,\widehat\delta),
 \qquad (m_1,m_2)=(3,4),
\]
where the inverse naming map sends each unhatted basis vector
to its displayed hatted vector. Thus
$v_1=g+2u-4w$, $v_2=-g-3u+3w$, and the cusp translation drift is zero.
The fibre is $F=\mathbb R^4/\Lambda$.
'''+oldroof+r'''The positive interval loop $\rho$ satisfies
$\rho t_\lambda\rho^{-1}=t_{A\lambda}$.
In the finite boundary chart below its base coordinate is
$q=e^{-2\pi i\theta}$, so this interval runs clockwise.
The counterclockwise loop is $\eta=\rho^{-1}$; it satisfies
$\eta t_\lambda\eta^{-1}=t_{A^{-1}\lambda}$.
The point-return map read from the endpoint relation is
$A^{-1}$ along $\rho$ and $A$ along $\eta$.
The reversal of roof coordinates and its inverse are
\[
 M_A\longrightarrow M_{A^{-1}},\quad
 [x,t]\longmapsto[A^{-1}x,1-t],
 \qquad [y,s]\longmapsto[Ay,1-s].
\]
At the endpoints the quotient relations make both composites
the identity and fix the marked fibre over the base point.
\end{definition}

'''
  edit('NUMBERED-DATUM','D13','mapsIII:def:three-filling-datum',heading,newheading,'Collect the unchanged p=-1 inputs in one numbered definition and print both exact loop/roof reversals. The original cell-versus-handle disclaimer is replaced by the precise homeomorphism and homotopy-equivalence claims in the theorem/proof.')
  edit('JB-TITLE','D16','maps:src:B.5.1',
   r'\begin{theorem}\hypertarget{tag-02JB}{}\label{maps:src:B.5.1}',
   r'\begin{theorem}[The three-filling mapping-cylinder model]\hypertarget{tag-02JB}{}\label{maps:src:B.5.1}'+'\n'+r'{\normalfont\scriptsize tag 02JB}\par',
   'Give the theorem a mathematical title and print its existing permanent tag in the small form.')
  record=re.search(r'^\\StatementRecord[^\n]+\n',after,re.M).group()
  edit('JB-HEADER','D07','maps:src:B.5.1',record,'','Remove the machine header; every operative geometric construction and source citation remains in the proof.')
  edit('JB-INPUT','D05','maps:src:B.5.1',
   'The underlying topological manifold of $X$ is obtained from',
   'For Definition~\\ref{mapsIII:def:three-filling-datum}, the underlying\\ntopological manifold of $X$ is obtained from'.replace('\\n','\n'),
   'Bind the theorem to precisely the original marked three-filling scope.')
  old=r'''In particular this is a statement about
the underlying smooth neighbourhood and does not replace
the scheme-theoretic fibre $m_jS_j$ by a reduced fibre in
the holomorphic map.'''
  new=r'''The bundle projection is $[x,s]\mapsto[x]\in S_j$,
while the holomorphic base coordinate is $q=s^{m_j}$.
Thus this smooth normal-disc model has scheme-theoretic
fibre $m_jS_j$ for the original holomorphic map.'''
  edit('NORMAL-DISC-MAP','D20','maps:src:B.5.1',old,new,'Retain both the associated normal-disc quotient and the multiplicity by their exact projection/base-coordinate formulas, with no categorical separation or unstated replacement.')
  old=r'''linear
interpolation of this lift straightens it on a collar.
Thus the actual gluing is identified with \eqref{maps:eq:B.5.3}, without
discarding a loop of translations of nonzero lattice drift.
This also corrects the first paragraph on page 42 of
\cite{mapsAC26}: multiplicity does not prevent this
neighbourhood from being a smooth normal disc bundle.
We make no assertion of a holomorphic tubular projection.
The meridian relation proved in that paragraph remains
valid; its meridian is the normal circle winding $m_j$
times around the base, rather than a once-around base
loop.'''
  new=r'''writing this periodic lift as $\ell$,
the collar isotopy is $x\mapsto x-t\ell$, with inverse
$x\mapsto x+t\ell$, for $0\le t\le1$.
It identifies the gluing with \eqref{maps:eq:B.5.3} after the
displayed nonzero drift has been kept.
The normal-circle meridian winds $m_j$ times around the base;
this is the kernel meridian in \cite[Lemma~7.1, proof, p.~42]{mapsAC26}.'''
  edit('COLLAR-MERIDIAN','D01','maps:src:B.5.1',old,new,'Keep the exact drift, its inverse collar translation and normal-meridian degree; move the historical correction/defensive discussion to the publication record. The primary p42 paragraph was opened and read.')
  old=r'''The constant phase cocycle is removed by the linear phase
gauge coming from $\operatorname{Re}C(0)a$.'''
  new=r'''On the universal phase coordinates $\phi=\arg(x)/(2\pi)$,
the constant phase gauge is $b=\phi-\operatorname{Re}C(0)a$,
with inverse $\phi=b+\operatorname{Re}C(0)a$.
It conjugates the constant phase cocycle to the quotient just defined.'''
  edit('PHASE-INVERSE','D20','maps:src:B.5.1',old,new,'Print the existing linear phase gauge and its inverse on the specified universal coordinates.')
  old=r'''Writing $\xi=Z_qa+b$ proves that this sends $Z_qa+b$ to
$Z_q^0a+b$, fixes the real lattice, and conjugates the
period actions.'''
  new=r'''Writing $\xi=Z_qa+b$ proves that this sends $Z_qa+b$ to
$Z_q^0a+b$, fixes the real lattice, and conjugates the
period actions. Its inverse is
\[
 \xi^0\longmapsto
 \xi^0+(C(q)-C_0)(\operatorname{Im}Z_q^0)^{-1}
                             \operatorname{Im}\xi^0.
\]
Indeed the two imaginary-part formulas recover the identical
real coefficient $a$, and both composites fix $a,b$.'''
  edit('FROZEN-INVERSE','D20','maps:src:B.5.1',old,new,'Supply the inverse of the existing frozen-period homeomorphism by the exact same real coefficient, preserving its full extension proof.')
  old=r'''$T^2\times(0,\eta)$, using $a=(B_\rho^+)^{-1}y$.'''
  new=r'''$T^2\times(0,\eta)$, using $a=(B_\rho^+)^{-1}y$;
the inverse is $y=B_\rho^+a$ on the universal positive coordinates.'''
  edit('POSITIVE-INVERSE','D20','maps:src:B.5.1',old,new,'Print the inverse already determined by the full positive-period coordinate formula.')
  old=r'''$b'=b-\theta B_0a$.  In these coordinates its expression'''
  new=r'''$b'=b-\theta B_0a$, with inverse $b=b'+\theta B_0a$.
In these coordinates its expression'''
  edit('PL-PHASE-INVERSE','D20','maps:src:B.5.1',old,new,'Give the exact phase-coordinate inverse before its finite piecewise-affine use.')
  old=r'''This does not require a finite
triangulation invariant under the infinite monodromy
group.'''
  edit('TRIANGULATION-SCOPE','D02','maps:src:B.5.1',old,'Each occurrence uses its stated subdivision and the common\\nsubdivision on the adjoining cylinder.'.replace('\\n','\n'),'State the finite construction positively while preserving the exact independent triangulations and common-subdivision maps.')
  old=r'''This changes
the double mapping cylinder by homotopy equivalence;
equivalently use \cite[Propositions 4G.1--4G.2]{mapsHatcher02}.'''
  new=r'''Use \cite[Theorem~4.8, p.~349]{mapsHatcher02}
for the cellular approximations. Write $b_j^c,r_j^c$ for them,
with homotopies $F_j(x,s)$ from $b_j$ to $b_j^c$ and
$G_j(x,s)$ from $r_j$ to $r_j^c$.
The map to the new double mapping cylinder is the identity on
$U_*,W,S_1,S_2$ and on its $j$th prism is
\[
 [x,t]\longmapsto
 \begin{cases}
 F_j(x,3t),&0\le t\le1/3,\\
 [x,3t-1],&1/3\le t\le2/3,\\
 G_j(x,3-3t),&2/3\le t\le1.
 \end{cases}
\]
The endpoint equations give a continuous quotient map.
The inverse up to homotopy is the same formula with
$F_j(x,1-s)$ and $G_j(x,1-s)$.
In either composite the extra paths are a homotopy followed
by its reverse. Put $\lambda(v)=\min(2v,2-2v)$.
The paths $F_j(x,(1-r)\lambda(v))$ and
$F_j(x,1-(1-r)\lambda(v))$ contract the two possible
retracings for $0\le r\le1$; the identical formulas apply to
$G_j$. Linear reparametrization of the remaining prism interval
then gives the identity, with its endpoints fixed.
These maps on the three prisms agree with the identity maps
on their common target pieces and prove the asserted homotopy equivalence.'''
  edit('CELLULAR-HOMOTOPY-MAPS','D20','maps:src:B.5.1',old,new,'Give the actual three-prism comparison, reverse map and both composite homotopies. The exact primary 4G.1/4G.2 readings showed that 4G.2 concerns open covers; use the directly operative cellular-approximation theorem and the complete maps here.')
  edit('FINITE-COUNTS-CONVENTION','D02','maps:src:B.5.1',
   '$B_j=A_j|_L$ (an inverse convention gives the same\\ncounts).'.replace('\\n','\n'),
   '$B_j=A_j|_L$, in the roof convention of\\nDefinition~\\ref{mapsIII:def:three-filling-datum}.'.replace('\\n','\n'),
   'Use the declared roof and its printed inverse convention map instead of an unsupported alternate-convention aside.')
  edit('JC-TAG','D10','maps:src:B.5.2',r'\hypertarget{tag-02JC}{}\label{maps:src:B.5.2}',r'\hypertarget{tag-02JC}{}\label{maps:src:B.5.2}'+'\n'+r'{\normalfont\scriptsize tag 02JC}\par','Print the existing permanent tag in the common small form.')
  for i in range(2):
   needle=r'\cref{maps:src:B.1.2}'
   pos=after.index(needle,after.index(r'\begin{theorem}[Homology'))
   old=after[pos:pos+len(needle)]
   # Two occurrences are deliberately handled by context-specific exact guards.
   context=after[max(0,pos-48):pos+len(needle)+2]
   replacement=context.replace(needle,r'Theorem~\ref{maps:src:B.1.1}')
   edit('FRAMING-OWNER-'+str(i+1),'D04','maps:src:B.5.2',context,replacement,'Point the unchanged explicit normal torus and identity chart to J4, now the sole earlier framing proof owner.')
  old=r''' D_1=\begin{pmatrix}1&0&0\\0&1&0\\-12&0&1\end{pmatrix}.'''
  new=r''' D_1=\begin{pmatrix}1&0&0\\0&1&0\\-12&0&1\end{pmatrix},
 \qquad
 D_1^{-1}=\begin{pmatrix}1&0&0\\0&1&0\\12&0&1\end{pmatrix}.'''
  edit('DEGREE-ONE-INVERSE','D20','maps:src:B.5.2',old,new,'Print both integral coordinate maps of the exact cusp degree-one attachment.')
  old=r'''Using the decomposition
$H_2(M_0)=\sigma H_2(W)\oplus K_2$ and the
bases in \eqref{maps:eq:B.5.18}, the map'''
  new=r'''The decomposition map and inverse are
\[
 (v,k)\longmapsto\sigma(v)+k,\qquad
 x\longmapsto(r_{0*}x,x-\sigma(r_{0*}x)).
\]
Using $H_2(M_0)=\sigma H_2(W)\oplus K_2$ and the
bases in \eqref{maps:eq:B.5.18}, the map'''
  edit('KERNEL-SPLITTING-INVERSE','D20','maps:src:B.5.2',old,new,'Print the exact inverse decomposition through the chosen integral section, with no rational saturation.')
  old=r'''carries
this map to $I_4\oplus I_2$. Thus both attachment'''
  new=r'''is its own inverse and carries
this map to $I_4\oplus I_2$. Thus both attachment'''
  edit('DEGREE-TWO-INVERSE','D20','maps:src:B.5.2',old,new,'Record the explicit target automorphism inverse: its square fixes both v and h.')
  tags=list(re.finditer(r'\\tag\{B\.5\.(\d+)\}',after))
  assert len(tags)==8
  for token in [m.group() for m in tags]:
   pos=after.index(token);start=after.rfind(r'\[',0,pos);end=after.index(r'\]',pos)+2
   old=after[start:end];new=old.replace(r'\[',r'\begin{equation}',1)
   new=new[:new.rfind(r'\]')]+r'\end{equation}'+new[new.rfind(r'\]')+2:]
   new=new.replace(token,'')
   n=re.search(r'B\.5\.(\d+)',token)[1]
   edit('AUTO-EQUATION-'+n,'D19','maps:eq:B.5.'+n,old,new,'Replace the manual display number with the section equation counter, preserving the complete body and every permanent label/target.')
 prepared[key]=(path,before,after)
transform('common_conventions');transform('cell_presentation')
source=u.repairs.SOURCE.read_text(encoding='utf-8');candidate=source
for key,(path,before,after) in prepared.items():
 assert candidate.count(before)==1,key
 candidate=candidate.replace(before,after,1)
u.check_permanent_identifiers(source,candidate,['mapsIII:def:three-filling-datum'],['tag-Q016'])
for path,before,after in prepared.values():path.write_text(after,encoding='utf-8',newline='\n')
u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,rows+changes)
print('UTC',datetime.now(timezone.utc).isoformat())
print('EXACT_DEFECT_ROWS',len(changes))
print('CELL_LINES',len(prepared['cell_presentation'][1].splitlines()),len(prepared['cell_presentation'][2].splitlines()))
print('Q016_CREATED; ALL_OLD_IDENTITIES_PRESERVED; WHOLE_EDITED_READING_PENDING')

