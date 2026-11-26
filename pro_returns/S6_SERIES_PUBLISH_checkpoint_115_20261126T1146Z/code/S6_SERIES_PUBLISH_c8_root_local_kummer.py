"""Present the full local/global Kummer arguments and their exact source maps."""
from datetime import datetime,timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
df,ds=r.table(r.DEFECTS);changes=[]
p=u.WORK/'root/local_kummer.tex';before=p.read_text();after=before
def edit(suffix,kind,label,old,new,reason):
 global after
 assert after.count(old)==1,(suffix,after.count(old))
 after=after.replace(old,new,1)
 ident='III-C8-KUMMER-'+suffix
 assert not any(x['change_id']==ident for x in ds)
 changes.append(dict(change_id=ident,type=kind,statement_id=label,old_location='local_kummer before full publication comparison',old_page='pending page concordance',new_location='local_kummer after exact map expansion',new_page='pending final PDF',old_text=old,new_text=new,reason=reason,review_status='exact edit applied; whole edited unit reading pending'))
old=r'''We distinguish a finite holomorphic map with smooth source from a finite
map with normal, possibly singular, source. A branched cover of compact
complex manifolds has the former meaning in this section. Write
$V_{\rm tor}=\Z\langle\widehat w,\widehat\delta\rangle$.'''
new=r'''\begin{definition}[The marked cusp and its root covers]
\hypertarget{tag-Q017}{}\label{mapsIII:def:kummer-data}
{\normalfont\scriptsize tag Q017}\par
Use the original family of Definition~\ref{mapsIII:def:marked-family}
and put $V_{\rm tor}=\mathbb Z\langle\widehat w,\widehat\delta\rangle$.
The cusp period matrix, in the ordered bases
$(\widehat\gamma,\widehat u)$ and $(\widehat w,\widehat\delta)$, is
\[
 Z(s)=sB_0+C(q),\qquad q=e^{2\pi i s},\qquad
 B_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]
with the holomorphic correction and prescribed $A_2$ fan of
Definition~\ref{mapsIII:def:cusp-suspension-maps}.
For $N\ge1$, the base root is $q=v^N$ and the source correction is
$C_N(v)=C(v^N)/N$. The source period cover uses that same fan.
In group presentations, $a_1,a_2$ denote the clockwise based loops
whose conjugation matrices are $A_1,A_2$, and
$a_0=(a_1a_2)^{-1}$. Their inverse loops and point-return maps are
those of Definition~\ref{mapsIII:def:three-filling-datum}.
\end{definition}'''
edit('INPUT','D13','mapsIII:def:kummer-data',old,new,'Replace the introductory category distinction with the exact shared marked data, roots, fan and map-specific loop convention in a numbered definition.')
edit('K2-TITLE','D16','maps:src:C.1.1','[Local Kummer theorem]','[The local Kummer construction]','Name the actual finite maps and source construction.')
edit('K2-INPUT','D05','maps:src:C.1.1',r'''Let $N\geq1$. On the cusp toric cover with period correction $C(q)$,
put $q=v^N$ and $C_N(v)=C(v^N)/N$. The map''',r'''For $N\geq1$ and the data of
Definition~\ref{mapsIII:def:kummer-data}, the map''','Bind the unchanged full positive-integer scope to its numbered input.')
edit('SPECIFIED-ROOT','D02','maps:src:C.1.1',r'''There is no root-selection ambiguity: the logarithm being divided by $N$
is the specified holomorphic function $2\pi iC(v^N)\lambda$.''',r'''The specified holomorphic function $2\pi iC(v^N)\lambda/N$
defines the exponential factor on the whole root disc.''','State the actual single-valued function and domain positively while preserving the full-disc action.')
titles={
 '02K3':('lemma','maps:src:C.1.2','smoothness of a cover of the entire fan','Smooth covers of the entire cusp fan'),
 '02K4':('theorem','maps:src:C.1.3','no smooth global Kummer extension','The lattice obstruction to a smooth global extension'),
 '02K5':('proposition','maps:src:C.1.4','a separate degree obstruction','The monodromy-orbit degree obstruction'),
 '02K6':('theorem','maps:src:C.1.5','normal singular globalizations','Normal global Kummer covers')}
for tag,(kind,label,oldtitle,newtitle) in titles.items():
 edit(tag+'-TITLE','D16',label,'['+oldtitle+']','['+newtitle+']','Use a descriptive mathematical title with the original result scope.')
 pattern=re.compile(r'^\\StatementRecord\{'+re.escape(label)+r'\}[^\n]*\n',re.M)
 old=pattern.search(after).group()
 edit(tag+'-HEADER','D07',label,old,r'{\normalfont\scriptsize tag '+tag+r'}\par'+'\n','Replace the machine header by the small original permanent tag; the operative input is explicit in the statement/proof.')
for i in range(5):
 old=r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'
 pos=after.index(old);context=after[pos:after.index('\n',after.index(r'\item',pos))+1]
 edit('PROOF-LIST-'+str(i+1),'D08','maps:src:C.1.'+str(i+1),context,context.replace(old,r'\begin{enumerate}[leftmargin=*]'),'Use ordinary mathematical proof-step numbering, preserving every complete proof item.')
old=r'''\item The assertion is about the entire cusp fan. A cover can be smooth in
one triangle and singular in its neighbour, so testing one triple point
cannot replace this argument.'''
new=r'''\item The local role of the neighbouring cones has an explicit example.
In the displayed initial basis take
$K=\mathbb Zr_0+\mathbb Zr_1+\mathbb Z(2r_2)
=\{(x,y,z):y\in2\mathbb Z\}$.
Its torus map is $(s_1,s_2,q)\mapsto(s_1,s_2^2,q)$.
The initial source chart has primitive basis $r_0,r_1,2r_2$
and map $(z_0,z_1,z_2)\mapsto(z_0,z_1,z_2^2)$.
Across the edge $(r_1,r_2)$, the target basis is
$r_3=(1,1,1),r_1,r_2$, with dual basis
\[
 e'_0=(1,1,-1),\quad e'_1=(0,-1,1),\quad e'_2=(-1,0,1).
\]
Since $(0,1/2,0)=(e'_0+e'_2)/2$, the corresponding normal
source chart has ring
\[
 \mathbb C\{x_0,x_1,x_2,B\}/(B^2-x_0x_2),
 \qquad B=\chi^{(e'_0+e'_2)/2},
\]
and its finite map forgets $B$. It is free of rank two over
the target ring, with basis $1,B$. At its origin the cotangent
space has dimension four while the chart has dimension three.
Equivalently, the primitive source rays $2r_3,r_1,2r_2$ span
an index-two sublattice of $K$. Thus the same entire-fan cover
has the displayed smooth chart and singular adjacent chart.'''
edit('K3-NEIGHBOUR-MAPS','D22','maps:src:C.1.2',old,new,'Retain the old one-chart/adjacent-chart example with its full admitted monomial-ring map, now in the actual e1-e2 fan coordinates. Both dual bases and the index/cotangent obstruction are explicit; no auxiliary scope is discarded.')
edit('K4-STEIN-SOURCE','D18','maps:src:C.1.3',r'''of the proper map $fF$, with connected fibres $g:Y\to C'$ and finite map
$h:C'\to B$.''',r'''of the proper map $fF$, with connected fibres $g:Y\to C'$ and finite map
$h:C'\to B$ \cite[\S1, p.~458]{mapsLi1995Cycles}.''','Give the exact already-read analytic Stein-factor formulation used by the complete admitted comparison.')
edit('K4-TRANSPORT-LOOP','D20','maps:src:C.1.3',r'''\item Follow a based meridian of the second finite fibre, choosing it to avoid
the additional deleted points, and then return to the same small''',r'''\item Follow the counterclockwise based meridian $a_2^{-1}$,
whose point-return map is $A_2$ by
Definition~\ref{mapsIII:def:three-filling-datum}, choosing it to avoid
the additional deleted points, and then return to the same small''','Name the exact inverse loop realizing the displayed forward transport. The full reverse-loop intersection and involution already in the proof remain unchanged.')
old=r'''A base covering supporting one fibre
lattice must have at least as many sheets as its monodromy orbit.
The unique prescribed cusp has local connected-fibre parameter $v$
with $q=v^N$ and is the entire preimage, so the base degree would be
$N$. This contradicts $N^2>N$.'''
new=r'''Here is the full base-degree argument for the stated normal-source
scope. Let $F:Z\to X$ be such an extension and take the connected
normal component containing the prescribed cusp source. Its finite
image contains the cusp neighbourhood and hence is all of $X$.
The proper map $fF$ has Stein factorization
\[
 Z\xrightarrow{g}C'\xrightarrow{h}B
\]
with connected fibres and finite $h$
\cite[\S1, p.~458]{mapsLi1995Cycles}.
The whole prescribed cusp preimage has base coordinate $q=v^N$;
over a small nonzero $q$ it has exactly $N$ connected torus fibres.
Thus $\deg h=N$.

The closed analytic set
$E=Z_{\rm sing}\cup\operatorname{Supp}\Omega_{Z/X}$ misses
the entire preimage of the punctured cusp disc. Its image under
the proper map $fF$ is a proper analytic subset of $B$, hence finite
\cite[Chapter~II, Theorem~8.8, p.~118]{mapsDemailly2012CADG}.
Delete that image, the three original exceptional values and the
finitely many branch values of $h$. Over the remaining base,
$F$ is a finite cover of torus bundles. A loop can be perturbed
away from the additional deleted points through a homotopy in the
original ordinary base, preserving its original monodromy.

For a sheet $y\in C'$ over the chosen base point put
$\mathcal L_y=(F|_{g^{-1}(y)})_*\pi_1(g^{-1}(y))\subset\Lambda$.
Fibre basepoint changes act trivially on this subgroup because
$\Lambda$ is abelian. For an actual bundle transport $H$ and its
lift $\widetilde H$, the equality
\[
 (F|_{g^{-1}(y')})_*\widetilde H_*
 =H_*(F|_{g^{-1}(y)})_*
\]
gives $\mathcal L_{y'}=H_*\mathcal L_y$.
The two inverse based meridians have point-return matrices
$A_1,A_2$. Replacing generators by their inverses leaves the
same generated subgroup, since each original generator is the
inverse of its replacement. Therefore the whole monodromy orbit
of $L_N$ is the image of the $N$ sheets under $y\mapsto\mathcal L_y$.
The already proved $N^2$ distinct lattices give $N^2\le N$,
contradicting $N>1$.'''
edit('K5-NORMAL-SOURCE-DEGREE','D22','maps:src:C.1.4',old,new,'Incorporate the entire already admitted normal-source bad-locus, Stein-degree and actual transport-square argument. It retains every source/branch/sheet allowance and uses no extra hypothesis or fresh independent derivation.')
old=r'''\item The exact orbit enumeration for $2\leq N\leq8$ is supplied in
\texttt{code/kummer\_orbits.py}; it gives respectively
$12,36,96,150,432,392,768$ elements. These finite computations check the
formulas in small cases. The preceding argument proves the required
lower bound for every $N$ and does not infer it from a finite search.
'''
edit('K5-FINITE-VALUES','D09','maps:src:C.1.4',old,'','Move the complete finite orbit values to the numbered joint calculation remark; exact historical/current paths and actual execution limits belong in the final program table.')
edit('K6-FREE-BASIS-MAP','D20','maps:src:C.1.5',r'''cusp loop is a free factor in the fundamental group of the punctured
sphere; equivalently, extend the given section along a relative graph
retraction.''',r'''cusp loop is a free factor in the fundamental group of the punctured
sphere. Explicitly the free-basis map
$(a_1,a_2)\mapsto(a_0,a_1)$ has inverse
$a_2=a_1^{-1}a_0^{-1}$. A pair-of-pants spine containing the
cusp loop gives the relative graph retraction, along which the
specified section extends.''','Print the actual free-group basis map and inverse underlying the existing relative degree-two obstruction assertion.')
edit('K6-COVER-COSSETS','D20','maps:src:C.1.5',r'''image of $U_N$. Its degree is $|K_N|/|U_N|=N^2|G_N|$.''',r'''image $H_N$ of $U_N$. If $\varphi:\pi_1(X^*)\to K_N$ is
the displayed epimorphism, the coset bijection is
\[
 H_N\backslash\pi_1(X^*)\longrightarrow U_N\backslash K_N,
 \qquad H_N\gamma\longmapsto U_N\varphi(\gamma).
\]
Its inverse chooses any lift of a representative in $K_N$;
the relation $H_N=\varphi^{-1}(U_N)$ makes that inverse
independent of the lift. Thus the degree is
$|K_N|/|U_N|=N^2|G_N|$.''','Supply the exact covering-sheet bijection and its inverse from the complete admitted comparison.')
edit('K6-CUSP-MORPHISM','D20','maps:src:C.1.5',r'''The power map of \ref{maps:src:C.1.1} has
this subgroup, using the zero-section lift of the base loop.''',r'''On universal logarithmic coordinates the power map of
Theorem~\ref{maps:src:C.1.1} is
$(s_v,\zeta_v)\mapsto(Ns_v,N\zeta_v)$.
The identity $NZ_N(s_v)=Z(Ns_v)$ sends the first two period
generators to themselves, the last two to their $N$-multiples,
and the zero-section base lift to $a_0^N$.
Thus it has exactly the displayed subgroup.''','Give the actual logarithmic covering map and all generator images before invoking covering classification; no equality-of-degree substitute is used.')
edit('K6-LOCAL-ALGEBRA','D02','maps:src:C.1.5',r'''the integral closure in the finite covering's local sheaf of meromorphic
functions; we do not use the field of global meromorphic functions on
the compact nonalgebraic space.
Integral closure is unique, so these local extensions glue on all
overlaps, including the self-identifications of $W$.''',r'''the integral closure in the finite covering's local sheaf of meromorphic
functions. On each overlap the isomorphism of the unramified covers
and its inverse extend by
\cite[Expos\'e~XII, Proposition~5.3, pp.~254--255]{SGA1Recomposed2004}.
Uniqueness makes their composites the identity and gives the cocycle
equation. The local extensions therefore glue on all overlaps,
including the self-identifications of $W$.''','Keep the precise local analytic algebra and replace the defensive global-field aside by the exact inverse extension/cocycle maps already proved in the admitted comparison.')
edit('K6-REGULAR-RING-INVERSE','D20','maps:src:C.1.5',r'''to $z^h$ and fixing $x_2,x_3$ identifies it with a convergent
three-variable power-series ring.''',r'''to $z^h$ and fixing $x_2,x_3$ identifies it with a convergent
three-variable power-series ring; the inverse sends the unique series
$\sum_{k\ge0}a_k(x_2,x_3)z^{hk}$ to
$\sum_{k\ge0}a_k(x_2,x_3)t^k$.''','Print the inverse of the already used analytic regular-ring isomorphism.')
edit('K6-COUNTS','D09','maps:src:C.1.5',r''' Exact enumeration gives
$|G_2|=48$, $|G_3|=216$, $|G_4|=3072$; the accompanying program
checks these finite examples, while the construction proves the
statement for arbitrary $N$.''','', 'Move the same three group orders into the numbered calculation remark; preserve the full unrestricted construction and singularity argument.')
old=r'''The local cover constructions have the two different degrees just computed. Non-invariance of its fibre sublattice alone
does not prohibit a further base cover. The entire-fan argument excludes
smooth global sources; the finite quotient in \ref{maps:src:C.1.5} gives the different
answer for normal singular sources with additional cusp sheets.'''
new=r'''\begin{remark}[Small congruence orbits and groups]
\hypertarget{tag-Q018}{}\label{mapsIII:rem:kummer-finite-values}
{\normalfont\scriptsize tag Q018}\par
For the marked matrices and $L_N$ above, the full monodromy orbit
has the following cardinalities:
\[
 \begin{array}{c|rrrrrrr}
 N&2&3&4&5&6&7&8\\\hline
 |\langle A_1,A_2\rangle L_N|&12&36&96&150&432&392&768.
 \end{array}
\]
For the exact matrix--phase groups in \eqref{maps:eq:C.1.4},
\[
 |G_2|=48,\qquad |G_3|=216,\qquad |G_4|=3072.
\]
These are finite congruence computations. The all-$N$ orbit bound
is the integral lattice argument of Proposition~\ref{maps:src:C.1.4},
and the all-$N$ finite cover is constructed in
Theorem~\ref{maps:src:C.1.5}.
\end{remark}'''
edit('NUMBERED-CALCULATIONS','D13','mapsIII:rem:kummer-finite-values',old,new,'Give all retained finite values one numbered home. The old repeated degree/scope summary is already proved with the actual lattice, base-cover and inverse extension maps in the five results.')
for n in range(1,5):
 old=r'\tag{C.1.'+str(n)+'}'
 edit('EQUATION-'+str(n),'D19','maps:eq:C.1.'+str(n),old,'','Use the section equation counter while retaining the exact existing label, permanent target and formula.')
# Source bibliography additions are part of the manuscript text, not a derived inventory.
bp=u.WORK/'root/bibliography.tex';bb=bp.read_text();ba=bb
entries=r'''
\bibitem{mapsDemailly2012CADG}
Jean-Pierre Demailly, \emph{Complex Analytic and Differential Geometry},
version of 21 June 2012. Chapter~II, Theorem~8.8, pp.~117--119.
\url{https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf}.

\bibitem{mapsLi1995Cycles}
Yingchen Li, Analytic cycles and generically finite holomorphic maps,
\emph{Bulletin of the Australian Mathematical Society} 52 (1995), 457--460.
The analytic Stein factorization is stated in \S1, p.~458.
\url{https://doi.org/10.1017/S0004972700014933}.

'''
assert 'mapsDemailly2012CADG' not in bb and 'mapsLi1995Cycles' not in bb
marker=r'\end{thebibliography}';assert bb.count(marker)==1
ba=bb.replace(marker,entries+marker,1)
changes.append(dict(change_id='III-C8-KUMMER-STEIN-BIB',type='D18',statement_id='mapsDemailly2012CADG; mapsLi1995Cycles',old_location='embedded bibliography',old_page='pending page concordance',new_location='embedded bibliography',new_page='pending final PDF',old_text=marker,new_text=entries+marker,reason='Add the exact primary editions and statement/page loci already read in the full admitted K5 comparison for the now explicit K4/K5 analytic argument.',review_status='exact source bibliography addition; final common bibliography/page gates pending'))
source=u.repairs.SOURCE.read_text();assert source.count(before)==1 and source.count(bb)==1
candidate=source.replace(before,after,1).replace(bb,ba,1)
u.check_permanent_identifiers(source,candidate,{'mapsIII:def:kummer-data','mapsIII:rem:kummer-finite-values'},{'tag-Q017','tag-Q018'})
p.write_text(after,encoding='utf-8',newline='\n');bp.write_text(ba,encoding='utf-8',newline='\n');u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n');r.write_table(r.DEFECTS,df,ds+changes)
print('UTC',datetime.now(timezone.utc).isoformat());print('EXACT_DEFECT_ROWS',len(changes));print('KUMMER_LINES',len(before.splitlines()),len(after.splitlines()));print('Q017_Q018_CREATED; ALL_OLD_IDENTITIES_PRESERVED; WHOLE_EDITED_READING_PENDING')
