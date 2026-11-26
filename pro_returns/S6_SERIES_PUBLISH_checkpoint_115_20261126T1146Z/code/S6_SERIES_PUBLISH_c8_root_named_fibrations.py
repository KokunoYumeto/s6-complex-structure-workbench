"""Present the three actual fibration inputs and reuse exact common homotopies."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
path=u.WORK/'root/named_fibrations.tex';before=path.read_text(encoding='utf-8');after=before
df,rows=r.table(r.DEFECTS);changes=[]
def edit(key,kind,label,old,new,reason):
 global after
 assert after.count(old)==1,(key,after.count(old))
 after=after.replace(old,new,1)
 ident='III-C8-NAMED-'+key;assert not any(x['change_id']==ident for x in rows)
 changes.append(dict(change_id=ident,type=kind,statement_id=label,old_location='named-fibration unit before publication comparison',old_page='pending page concordance',new_location='Quotient maps in three sphere-fibration families',new_page='pending final PDF',old_text=old,new_text=new,reason=reason,review_status='applied; complete rewritten-proof reading and final PDF pending'))
start=before.index('The primitive characters and cusp vanishing lattices are')
end=before.index('\n\\item For the two-parameter family',start)
character_block=before[start:end]
table_end=character_block.index(r'\end{array}')+len(r'\end{array}')
table_end=character_block.index(r'\]',table_end)+2
character_table=character_block[:table_end]
param_start=before.index('For the third family put')
param_end=before.index('In particular $N_i$ is relatively prime to $m_i$.',param_start)
parameter_block=before[param_start:param_end]
definition=r'''\subsection{Quotient maps in three sphere-fibration families}

\begin{definition}[The three marked sphere families]
\hypertarget{tag-Q014}{}\label{mapsIII:def:three-sphere-families}
{\normalfont\scriptsize tag Q014}\par
Use the sphere members of Viaclovsky's two-parameter family,
the Liu--Rollenske family, and the sphere members $X_{3k,4l}$
with $k,l\ge1$ and $\gcd(3k,4l)=1$, with the sections,
integral logarithmic collar lifts, twists and cusp markings of
those constructions. Their marked lattices, primitive characters
and cusp vanishing lattices are the following.
'''+character_table[character_table.index(r'\['):]+r'''
Put $L=\ker\chi$. For the logarithmic family use its constructed
integral lifts and write
'''+parameter_block[parameter_block.index(r'\['):]+r'''\end{definition}

'''
heading=after[:after.index(r'\begin{theorem}')]
edit('NUMBERED-DATA','D13','mapsIII:def:three-sphere-families',heading,definition,'State all three actual family/marking inputs, the exact primitive-character table and positive logarithmic sphere condition before use; the parameters and source constructions are unchanged.')
edit('MOVED-CHARACTERS','D11','maps:src:B.4.1',character_block,'','The full character/vanishing-lattice data now have the preceding numbered owner; the connected character kernel is verified in the proof.')
edit('MOVED-PARAMETERS','D11','maps:src:B.4.1',parameter_block,'','The original logarithmic parameter formulas and signed sphere equation now occur once in the input definition.')
old="For the sphere members of Viaclovsky's two-parameter family,\nthe Liu--Rollenske family, and the sphere members $X_{3k,4l}$\nwith $k,l\\geq1$ and $\\gcd(3k,4l)=1$, use the sections,\nintegral logarithmic collar lifts and cusp markings of their\nconstructions. The primitive invariant-circle quotient extends"
new=r'For the data of Definition~\ref{mapsIII:def:three-sphere-families},'+'\n'+'the primitive invariant-circle quotient extends'
edit('STATEMENT-INPUT','D05','maps:src:B.4.1',old,new,'The statement uses the identical complete family input through its numbered definition, without a parameter enlargement.')
edit('SMALL-TAG','D10','maps:src:B.4.1',r'\label{maps:src:B.4.1}',r'\label{maps:src:B.4.1}'+'\n'+r'{\normalfont\scriptsize tag 02JA}\par','Print the existing permanent tag in the common small form.')
edit('DUPLICATE-CONCLUSION','D11','maps:src:B.4.1','The quotient class therefore takes the same\nvalue on these fibrations.','','The statement already gives 6nu-prime for every specified member; the concrete two-parameter consequence has its own numbered remark.')
old='In particular $N_i$ is relatively prime to $m_i$.'
new=r'''Reducing $m_1N_0+m_0N_1=\pm1$ modulo $m_i$ proves
$\gcd(N_i,m_i)=1$ for each logarithmic filling.
In the three rows of the input table the bases of $L$ are,
respectively, $(\widehat u,\widehat w,\widehat\delta)$,
$(e_1,e_2,e_3)$ and $(\delta,a,b)$.
Their coefficient maps $L\to\mathbb Z^3$ have inverse the
corresponding integral linear combinations. The complementary
vectors $\widehat\psi,e_4,d$ have character value one.
Thus the quotient $[x]\mapsto\chi(x)\bmod\mathbb Z$
has connected kernel $T_L=L_{\mathbb R}/L$.'''
edit('KERNEL-COORDINATES','D20','maps:src:B.4.1',old,new,'Write the exact split lattice and both coordinate maps in every family, together with the unchanged primitive finite-translation argument.')
old=r'The torus isomorphism is $[x]\mapsto[P_Vx]$.'
new=r'''The torus isomorphism is $[x]\mapsto[P_Vx]$, with inverse
$[y]\mapsto[P_V^{-1}y]$, where
\[
 P_V^{-1}=\begin{pmatrix}
 0&0&0&-1\\0&0&-1&0\\0&-1&0&6\\1&0&1&-2
 \end{pmatrix}.
\]
The two matrix products are the identity.'''
edit('PV-INVERSE','D20','maps:src:B.4.1',old,new,'Print the complete inverse of the existing determinant-minus-one marking matrix; preserve its finite-matrix and translation identifications.')
old=r'''$e_4=f_2+f_4$, hence $\delta=f_3$ and $\xi=f_4^*$.'''
new=r'''$e_4=f_2+f_4$. The inverse basis equations are
$f_1=e_1-e_3$, $f_2=e_2$, $f_3=2e_3-e_1$ and $f_4=e_4-e_2$.
Thus $\delta=f_3$ and $\xi=f_4^*$.'''
edit('LR-INVERSE','D20','maps:src:B.4.1',old,new,'Give the inverse of the actual local Liu–Rollenske basis map, preserving both geometric circle factors.')
old=r'''identify this quotient with $D^2\times S^1$; the $m$ choices
of $\theta$ for a fixed $v$ are permuted transitively by the
deck generator. Its base map is $q=z^mv^a$.'''
new=r'''identify this quotient with $D^2\times S^1$.
For the inverse choose a solution of $e^{2\pi im\theta}=v$ and put
$s=z e^{2\pi ia\theta}$. The $m$ choices of $\theta$ are permuted
transitively by the deck generator, since $\gcd(N,m)=1$;
$aN+cm=1$ makes the corresponding $s$ values deck equivalent.
Substitution gives both inverse composites on the quotient.
Its base map is $q=z^mv^a$.'''
edit('FINITE-TORUS-INVERSE','D20','maps:src:B.4.1',old,new,'Write the actual inverse on quotient points and the integer identity that makes its choice independent.')
old=r'''The modulus ratio is strictly increasing as a function of
$|z_1|\in(0,1)$; a regular value with both entries nonzero
has $m_0m_1$ phase preimages, all with positive local degree.
Thus $\deg F_{m_0,m_1}=m_0m_1$.'''
new=r'''For $t=|z_1|^2$ the first squared radius is
\[
 R(t)=\frac{t^{m_0}}{t^{m_0}+(1-t)^{m_1}},\qquad
 R'(t)=\frac{t^{m_0-1}(1-t)^{m_1-1}
                (m_0(1-t)+m_1t)}
               {(t^{m_0}+(1-t)^{m_1})^2}>0\quad(0<t<1).
\]
It runs from zero to one. A regular value with both entries nonzero
has exactly $m_0m_1$ phase preimages, each with positive local degree.
Thus $\deg F_{m_0,m_1}=m_0m_1$.'''
edit('ALL-ORDER-RADII','D22','maps:src:B.4.1',old,new,'Supply the exact positive derivative for every existing positive multiplicity pair; retain the full weighted projection and degree conclusion.')
old=r''' P_2=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.'''
new=r''' P_2=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},
 \qquad
 P_2^{-1}=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.'''
edit('P2-INVERSE','D20','maps:src:B.4.1',old,new,'Print the full inverse of the actual native/marked period map.')
old=r''' P_{\log}=\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\0&6&-1&0\\1&-2&0&1\end{pmatrix}.'''
new=r''' P_{\log}=\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\0&6&-1&0\\1&-2&0&1\end{pmatrix},
 \qquad
 P_{\log}^{-1}=\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\-6&0&-1&0\\-2&1&0&1\end{pmatrix}.'''
edit('PLOG-INVERSE','D20','maps:src:B.4.1',old,new,'Keep every toric shear entry and display the inverse coordinate map.')
old=r'''These are maps of tori $[t]\mapsto[Pt]$, including their
toric shear entries.'''
new=r'''These are maps of tori $[t]\mapsto[Pt]$, with inverses
$[v]\mapsto[P^{-1}v]$; multiplying each displayed pair gives the identity.
They include all toric shear entries.'''
edit('PERIOD-COMPOSITES','D20','maps:src:B.4.1',old,new,'Tie the new inverse matrices to both torus quotient maps explicitly.')
old=r'The retained three-torus map is $(\phi,t)\mapsto(\phi,Jt)$.'
new=r'''Here $J_2^{-1}=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$,
$J_{\mathrm{LR}}^{-1}=J_{\mathrm{LR}}$ and $J_{\log}^{-1}=J_{\log}$.
The retained three-torus map is $(\phi,t)\mapsto(\phi,Jt)$,
with inverse $(\phi,v)\mapsto(\phi,J^{-1}v)$.'''
edit('LONG-INVERSES','D20','maps:src:B.4.1',old,new,'Display each inverse long marking before its exact degree and suspended-map use.')
old=r'''It factors into the $(1,2)$ and $(1,3)$ diagonal $SU(2)$
loops. Each contracts through
\[
 \begin{pmatrix}
 r e^{-it}&-\sqrt{1-r^2}\\
 \sqrt{1-r^2}&r e^{it}
 \end{pmatrix},\qquad 0\leq r\leq1,
\]
followed by a constant real rotation to the identity.'''
new=r'''This is the identical matrix $D(a,b)$ in the proof of
Theorem~\ref{maps:src:B.3.1}, under the identity map on the two
angular coordinates and a constant frame change. Its two displayed
$K_s$ factors therefore give the same periodic contraction here;
the inverse coordinate identification is again $(a,b)\mapsto(a,b)$.'''
edit('ONE-SU3-CONTRACTION','D12','maps:src:B.4.1',old,new,'The complete native gauges, both diagonal charts, exact inverse image and differential frame remain. Reuse only the literally identical two-angle matrix contraction, after identifying every variable and frame change.')
as_=after.index('\\item The cusp boundary map already proved shows')
ae=after.index('\nFinally, \\SeriesRef{push:src:E.5.3}',as_)
old=after[as_:ae]
new=r'''\item Take the closed cusp neighbourhood $N$ with its product
outer collar. The boundary-to-neighbourhood map proved above is the
long-period projection to $\Lambda/K=\mathbb Z^2$.
The equivariant-cover construction in the proof of
Theorem~\ref{maps:src:B.3.2}, on this actual free period cover,
gives $h_0:N\to T^2$ inducing that projection, with $h_0(x_0)=0$.
The native long-period map $\alpha$ induces the same homomorphism;
hence $\alpha=h_0+[\ell]$ for a real lift $\ell$ on $N\setminus W$.
Using a radial cut-off $b$ equal to zero near $W$ and one on the
outer collar, put
\[
 h=h_0+[b\ell],\qquad L=(1-b)\ell.
\]
Then $h(x_0)=0$, $h=\alpha$ on the outer collar and
$\alpha=h+[L]$. These are the same operations as the cited construction
with the identity on its real native deck coordinates; the inverse
coordinate map is the identity.

Apply Lemma~\ref{mapsIII:carrier-extension-lemma} with $r=|q|$,
this $\alpha,h,L$, and the based target maps
$c_3=\operatorname{collapse}\circ J:T^2\to S^2$ and
$c_\gamma=\operatorname{character}\circ J:T^2\to S^1$.
The matrices $J$ and their displayed inverses carry these formulas
exactly to the two prescribed marked angle-forgetting maps.
The punctured cusp is a torus bundle with connected fibre over a
punctured disc, so it is connected and locally path connected;
its product collar gives the required frontier equality.
All compactness and basepoint hypotheses of the lemma hold.
Its two explicit homotopies therefore give the claimed based
null-homotopies, including their fixed exterior and basepoint.
'''
edit('ONE-SUSPENSION-HOMOTOPY','D12','maps:src:B.4.1',old,new,'Reuse the sole Q8 two-stage proof after matching its actual period cover, native deck coordinates, lifted difference, cut-off, basepoint, collar, frontier and the two c composed with J maps. Keep each family’s boundary-group proof and all inverse markings; no lemma is applied outside its defined data.')
tail=r'''Finally, \SeriesRef{push:src:E.5.3} supplies distinct
two-parameter members with different sufficiently small
$\mu$; their quotient classes are both $6\nu'$.'''
edit('CONSEQUENCE-OWNER','D13','mapsIII:rem:three-family-quotient-class',tail,'','Move the complete concrete two-parameter consequence into its own numbered remark after the theorem proof; the exact Paper II input and conclusion are preserved.')
remark=r'''
\begin{remark}[Two-parameter quotient classes]
\hypertarget{tag-Q015}{}\label{mapsIII:rem:three-family-quotient-class}
{\normalfont\scriptsize tag Q015}\par
\SeriesRef{push:src:E.5.3} supplies distinct two-parameter members
with different sufficiently small $\mu$.
Theorem~\ref{maps:src:B.4.1} gives quotient class $6\nu'$ for both.
\end{remark}

'''
after=after.rstrip()+'\n'+remark
ident='III-C8-NAMED-NUMBERED-CONSEQUENCE';assert not any(x['change_id']==ident for x in rows)
changes.append(dict(change_id=ident,type='D13',statement_id='mapsIII:rem:three-family-quotient-class',old_location='last sentence inside JA proof',old_page='pending page concordance',new_location='numbered remark after JA',new_page='pending final PDF',old_text=tail,new_text=remark,reason='Keep the exact mathematical consequence and source as one numbered remark.',review_status='applied; whole readback pending'))
source=u.repairs.SOURCE.read_text(encoding='utf-8');assert source.count(before)==1
candidate=source.replace(before,after,1)
newlabels=['mapsIII:def:three-sphere-families','mapsIII:rem:three-family-quotient-class'];newtargets=['tag-Q014','tag-Q015']
u.check_permanent_identifiers(source,candidate,newlabels,newtargets)
path.write_text(after,encoding='utf-8',newline='\n');u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n');r.write_table(r.DEFECTS,df,rows+changes)
print('UTC',datetime.now(timezone.utc).isoformat())
print('EXACT_DEFECT_ROWS',len(changes),'LINES',len(before.splitlines()),len(after.splitlines()))
print('Q014_Q015_CREATED; ALL_OLD_IDENTITIES_PRESERVED; NO_READING_CREDIT')

