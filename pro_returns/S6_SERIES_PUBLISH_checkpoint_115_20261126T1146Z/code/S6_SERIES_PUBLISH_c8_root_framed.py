"""Give the full-scope framing comparison one proof before the sphere class."""
from __future__ import annotations
from datetime import datetime, timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

path=u.WORK/'root/framed_class.tex'
before=path.read_text(encoding='utf-8')
fields,rows=r.table(r.DEFECTS)
changes=[]

def record(key,kind,statement,old,new,reason):
 ident='III-C8-FRAMED-'+key
 assert not any(x['change_id']==ident for x in rows)
 changes.append(dict(change_id=ident,type=kind,statement_id=statement,old_location='framed-class unit before consolidation',old_page='pending page concordance',new_location='Framings and the quotient homotopy class',new_page='pending final PDF',old_text=old,new_text=new,reason=reason,review_status='source applied; whole readback and final PDF reading pending'))

theorem_start=before.index(r'\begin{theorem}\hypertarget{tag-02J5}')
old_initial=before[:theorem_start]
theorem=before[theorem_start:]
sphere_start=theorem.index(r'Put $d=|p|=1$.')
sphere_end=theorem.index('  The target of',sphere_start)
sphere_argument=theorem[sphere_start:sphere_end]
transport_start=theorem.index('The global stable framing is')
transport_end=theorem.index('This proves the stable-framing comparison on every coset')
transport_end=theorem.index('for the present member.',transport_end)+len('for the present member.')
old_transport=theorem[transport_start:transport_end]

definition=r"""\subsection{Framings and the quotient homotopy class}
\begin{definition}[The character kernel and stable generators]
\hypertarget{tag-Q010}{}\label{mapsIII:def:framing-conventions}
{\normalfont\scriptsize tag Q010}\par
Let $(\gamma,u,w,\delta)$ be the basis dual to
$(\widehat\gamma,\widehat u,\widehat w,\widehat\delta)$, and put
\[
 L=\ker\gamma=\mathbb Z\langle\widehat u,\widehat w,
                                    \widehat\delta\rangle,
 \qquad T_L=L_{\mathbb R}/L\subset\Lambda_{\mathbb R}/\Lambda.
\]
We write $\pi_3^{\rm S}=\mathbb Z/24\langle\nu\rangle$, with
$e_{\mathbb R}(\nu)=1/24$, and
$\pi_6(S^3)=\mathbb Z/12\langle\nu'\rangle$ in the convention
of \cite[Theorem~4.1 and Corollaries~4.2--4.3, pp.~76--77]{mapsToda52}.
The map $\eta_n:S^{n+1}\to S^n$ is the $(n-2)$-fold suspension
of the complex Hopf map, for $n\ge2$.
We use outward stabilization, with the normal frame before the
tangential frame and a constant orientation-preserving adjustment
of any permutation of those fields.
\end{definition}

\begin{lemma}[Framing on the character kernel]
\hypertarget{tag-02J4}{}\label{maps:src:B.1.1}
{\normalfont\scriptsize tag 02J4}\par
For every admissible member with $|p|=1$, the manifold $X_p$ is
an oriented smooth six-sphere. Let $F$ be a regular fibre.
Compare its bounding stable framing with the frame on $TX_p|_F$
formed by four translation-invariant vertical fields and an
oriented lifted base frame. The restriction of their stable
difference to every coset of $T_L\subset F$ is null-homotopic.
\end{lemma}

\begin{proof}
"""
new_transport=r"""
The global stable framing is
$\tau_x(v,t)=d\chi_x(v)+t\chi(x)$.
Two oriented stable trivializations differ by a map $S^6\to\mathrm{SO}$.
The equality $\pi_6(\mathrm{SO})=0$
\cite[Corollary to Theorem~II and the table on p.~315]{mapsBott59}
makes its stable homotopy class independent of $\chi$.

The affine return maps have the form $h_j(x)=A_jx+a_j$.
Choose a constant change $C$ of the four vertical fields
so that, together with an oriented lifted base frame and the
positive stabilizing vector, they form an oriented frame.
Let $D:F\to GL^+(7,\mathbb R)$ compare that frame with $\tau$.
The transported-frame homotopy has endpoint
\[
 D_1(x)=D_0(h_jx)\operatorname{diag}(C^{-1}A_jC,I_3).
\]
The constant last factor is connected to the identity.
Polar decomposition gives $g\simeq g\circ h_j$ for
$g:F\to SO(7)$. The isotopy $x\mapsto A_jx+t a_j$
identifies the cohomology action with $A_j^t=T_j^{-1}$.

Use the matrices of Definition~\ref{mapsIII:def:lifted-fibre} at $d=1$.
For a mod-two covector $a\gamma+bu+cw+f\delta$,
$A_1$-invariance gives $b=0$, $f=c$; $A_2$-invariance gives
$f=0$, $c=b$. Conversely those equations make both matrix
differences vanish. Thus the common invariant group is
$(\mathbb Z/2)\gamma$.
The integral fixed-vector equations give, in both directions,
\[
 \begin{aligned}
 \ker(A_1-I)&=\mathbb Z\langle\widehat\gamma+2\widehat u-4\widehat w,
                                      \widehat\delta\rangle,\\
 \ker(A_2-I)&=\mathbb Z\langle\widehat\gamma+3\widehat u-3\widehat w,
                                      \widehat\delta\rangle.
 \end{aligned}
\]
Their intersection is $\mathbb Z\widehat\delta$.
For $\Omega=\gamma\wedge u\wedge w\wedge\delta$, the map
$\operatorname{PD}(v)=\iota_v\Omega$ has inverse determined
by its four coefficients. Since $\det A_j=1$,
evaluation on three vectors gives
\[
 (\textstyle\bigwedge^3 A_j^t)\operatorname{PD}(v)
       =\operatorname{PD}(A_j^{-1}v),
 \qquad \operatorname{PD}(\widehat\delta)=-\gamma\wedge u\wedge w.
\]
Indeed both evaluations equal
$\Omega(v,A_jv_1,A_jv_2,A_jv_3)
 =\Omega(A_j^{-1}v,v_1,v_2,v_3)$.
It follows that
\[
 H^1(F;\mathbb Z/2)^{h_1^*,h_2^*}=(\mathbb Z/2)\gamma,
 \qquad
 H^3(F;\mathbb Q)^{h_1^*,h_2^*}=\mathbb Q\,\gamma u w.
\]
For the coset inclusion $j_a(y)=a+y$, one has $j_a^*\gamma=0$.
Thus $g j_a$ lifts to $\ell_a:T_L\to\operatorname{Spin}(7)$.
Let $c:\operatorname{Spin}(7)\to SO(7)$ be the double cover
and let $u_3$ generate its integral third cohomology.
Transfer gives $\beta=\frac12\operatorname{tr}(u_3)$ with
$c^*\beta=u_3\otimes1$, since the deck translation is homotopic
to the identity. Hence
\[
 (\ell_a^*u_3)\otimes1=j_a^*g^*\beta=0.
\]
The group $H^3(T_L;\mathbb Z)=\mathbb Z$ is torsion free, so
this class vanishes integrally. Spin$(7)$ is two-connected;
the lifted map can be made constant on the two-skeleton and
then factors through $T_L/T_L^{(2)}=S^3$.
Its remaining class is zero by the degree-three Hurewicz isomorphism.
The two lifts differ by multiplication by the central element $-1$,
which is homotopic to the identity along a path in Spin$(7)$.
This proves the framing assertion for every coset.
\end{proof}

"""
new_initial=definition+sphere_argument+'\n'+new_transport
record('SINGLE-FRAME-PROOF','D12','maps:src:B.1.1; maps:src:B.1.2',old_initial,new_initial,
 'Move the already proved all-admissible-|p|=1 sphere identification and affine/Spin comparison from J5 into J4, with its full hypotheses. The original-member doubling proof remains in the checking record as the replaced proof. The canonical result has one transfer proof; the complete unit before rewriting and both prior comparisons were read.')
record('FULL-SCOPE-OWNER','D26','maps:src:B.1.1',
 'Let F be a regular fibre of the original fibration.',
 'For every admissible member with |p|=1, X_p is an oriented smooth six-sphere; the stable comparison is null on every character-kernel coset.',
 'This is relocation of the exact broader statement already proved inside J5, not a new parameter extension or a narrowing of J5. The complete d=1 homology/Hurewicz/Kervaire–Milnor and affine-transport argument now precedes its use.')
record('EXPLICIT-INVARIANTS','D22','maps:src:B.1.1',
 'The exhaustive calculation in maps_exact.py gives the invariant subgroups.',
 new_transport[new_transport.index('Use the matrices'):new_transport.index('For the coset inclusion')],
 'Replace the program-only justification by the actual mod-two equations, both integral fixed lattices and the determinant-one Poincare-duality map, including its inverse coordinate description. The same invariant groups and gamma-kernel restriction are proved.')
record('NUMBERED-CONVENTIONS','D13','mapsIII:def:framing-conventions',
 old_initial[old_initial.index('We use'):old_initial.index(r'\begin{lemma}')],definition,
 'Move the shared stable/unstable generators, character kernel and framing order into numbered Definition Q010. The independence of the sphere identification is proved once inside the following lemma.')
record('J4-TITLE','D16','maps:src:B.1.1',r'\begin{lemma}',r'\begin{lemma}[Framing on the character kernel]',
 'Supply the mathematical title of the complete stable comparison.')
record('J4-TAG','D10','maps:src:B.1.1',
 r'\StatementRecord{maps:src:B.1.1}{proved}{02J4}{the definitions and constructions stated in the proof}',
 r'{\normalfont\scriptsize tag 02J4}\par',
 'Print only the existing tag and preserve its permanent anchor and label.')
record('PROGRAM-PROSE','D09','maps:src:B.1.1',r'\texttt{maps\_exact.py}',
 'The explicit mod-two equations, fixed-vector equations and Poincare-duality map in the proof.',
 'The body computation is now fully given by its inputs, linear equations and exact outputs. The historical program attribution remains in checking records; its eventual program-table disposition is part of the global program gate.')

old_prefix=theorem[theorem.index(r'\item Put $d=|p|=1$.'):transport_end]
new_prefix=r"""\item By Lemma~\ref{maps:src:B.1.1}, choose an oriented diffeomorphism
$\chi:X_p\to S^6$ and its bounding stable framing $\tau$.
The target of \SeriesRef{mapsI:src:A.1.3} is an oriented three-sphere.
Choose an oriented diffeomorphism $\psi:Q\to S^3$ and write
$e=\psi\circ e_{\rm q}\circ\chi^{-1}$.
"""
assert theorem.count(old_prefix)==1
theorem=theorem.replace(old_prefix,new_prefix,1)
record('USE-PRECEDING-LEMMA','D12','maps:src:B.1.2',old_prefix,new_prefix,
 'The exact sphere/frame construction is now the preceding full-scope lemma. Keep the target/source maps and all remaining regular-fibre, Hopf-product, APS and Toda arguments in the sole theorem proof.')
edits=[
 ('J5-TITLE','D16',r'\begin{theorem}\hypertarget{tag-02J5}',r'\begin{theorem}[The quotient homotopy class]\hypertarget{tag-02J5}'),
 ('J5-TAG','D10',r'\StatementRecord{maps:src:B.1.2}{proved}{02J5}{\SeriesRef{maps:src:B.1.1}; \cite[Theorem (4.14), p.~423]{mapsAPS2}; \cite[Theorem 4.1 and Corollaries 4.2--4.3]{mapsToda52}}',r'{\normalfont\scriptsize tag 02J5}\par'),
 ('QUOTIENT-NAME','D08','For the repaired quotient of','For the quotient replacement of'),
 ('ENUMERATION','D23',r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',r'\begin{enumerate}[label=\arabic*.,leftmargin=*]'),
 ('COMPARISON-LOCATOR','D04','The comparison just proved identifies the induced stable\ntangent framing with the Lie framing of $T^3$.',r'Lemma~\ref{maps:src:B.1.1} identifies the induced stable'+'\n'+r'tangent framing with the Lie framing of $T^3$.'),
]
for key,kind,old,new in edits:
 assert theorem.count(old)==1,key
 theorem=theorem.replace(old,new,1)
 record(key,kind,'maps:src:B.1.2',old,new,'Exact publication edit after consolidation; mathematical scope and all permanent identities remain.')
for suffix in ['1','2','3']:
 marker=r'\tag{B.1.'+suffix+'}'
 pos=theorem.index(marker)
 start=theorem.rfind(r'\[',0,pos)
 end=theorem.index(r'\]',pos)+2
 old=theorem[start:end]
 new=r'\begin{equation}'+old[2:-2].replace(marker,'')+r'\end{equation}'
 theorem=theorem[:start]+new+theorem[end:]
 record('EQUATION-'+suffix,'D19','maps:src:B.1.2',old,new,'Replace this single inherited manual tag by automatic section numbering; preserve the mathematical display, old target and equation label.')
after=new_initial+theorem
u.check_permanent_identifiers(before,after,['mapsIII:def:framing-conventions'],['tag-Q010'])
source=u.repairs.SOURCE.read_text(encoding='utf-8')
assert source.count(before)==1,'Current canonical framing block'
candidate=source.replace(before,after,1)
u.check_permanent_identifiers(source,candidate,['mapsIII:def:framing-conventions'],['tag-Q010'])
path.write_text(after,encoding='utf-8',newline='\n')
u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,fields,rows+changes)
print('UTC',datetime.now(timezone.utc).isoformat())
print('EXACT_DEFECT_ROWS',len(changes))
print('NEW_ID Q010 mapsIII:def:framing-conventions')
print('ONE_FULL_SCOPE_FRAMING_PROOF_PRECEDES_J5; ALL_OLD_IDENTITIES_PRESERVED')
print('NO_READING_OR_CRITERION_CREDIT_ASSIGNED')
