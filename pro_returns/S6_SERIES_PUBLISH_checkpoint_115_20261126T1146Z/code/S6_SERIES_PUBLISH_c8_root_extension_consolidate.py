"""Put the suspension homotopy before its exact two applications, once."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
cp=u.WORK/'root/carrier_extension.tex';qp=u.WORK/'root/quotient_maps.tex';ep=u.WORK/'root/extension_homotopy.tex'
carrier=cp.read_text(encoding='utf-8');quotient=qp.read_text(encoding='utf-8')
assert not ep.exists()
df,rows=r.table(r.DEFECTS);changes=[]
def log(key,kind,label,old,new,reason):
 ident='III-C8-EXTENSION-'+key;assert not any(x['change_id']==ident for x in rows)
 changes.append(dict(change_id=ident,type=kind,statement_id=label,old_location='carrier-extension and retained-coordinate units before consolidation',old_page='pending page concordance',new_location='Suspension homotopies; retained-coordinate maps; smash powers',new_page='pending final PDF',old_text=old,new_text=new,reason=reason,review_status='applied; whole affected proof readback and final PDF pending'))
ls=carrier.index(r'\begin{lemma}');ps=carrier.index(r'\begin{proof}',ls);pe=carrier.index(r'\end{proof}',ps)+len(r'\end{proof}')
oldlemma=carrier[ls:ps];oldproof=carrier[ps:pe]
definition=r'''\subsection{Suspension homotopies from torus extensions}

\begin{definition}[Torus extension data]
\hypertarget{tag-Q013}{}\label{mapsIII:def:torus-extension-data}
{\normalfont\scriptsize tag Q013}\par
A torus extension datum consists of a compact Hausdorff space $X$,
a compact manifold with boundary $N\subset X$ which is a closed
neighbourhood with $\operatorname{int}_X(N)=N\setminus\partial N$,
and a continuous $r:N\to[0,\epsilon]$ such that
$W=r^{-1}(0)$, $\partial N=r^{-1}(\epsilon)$ and
$U=N\setminus W$ is connected and locally path connected.
It also contains continuous maps
$\alpha:U\to T^d=\mathbb R^d/\mathbb Z^d$ and $h:N\to T^d$
inducing the same homomorphism on $\pi_1(U)$, a point $x_0\in W$
with $h(x_0)=0$, and a based continuous map
$c:(T^d,0)\to(Z,z_0)$ to a compact Hausdorff based space.
\end{definition}

'''
body=oldlemma[oldlemma.index(r'\['):]
body=body.replace('Then $G:X\\to\\Sigma_rZ$ is based nullhomotopic, by a homotopy','The map $G:X\\to\\Sigma_rZ$ is based null-homotopic, by a homotopy',1)
lemma=r'''\begin{lemma}[Suspension of a torus extension]
\hypertarget{tag-02Q8}{}\label{mapsIII:carrier-extension-lemma}
{\normalfont\scriptsize tag 02Q8}\par
For the data of Definition~\ref{mapsIII:def:torus-extension-data}, set
'''+body
proof=oldproof.replace(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',r'\begin{enumerate}[label=\arabic*.,leftmargin=*]',1)
proof=proof.replace('The lifting criterion for the covering\n$\\mathbb R^d\\to T^d$ therefore supplies a continuous function',r'The lifting criterion for the covering'+'\n'+r'$\mathbb R^d\to T^d$'+ '\n'+r'\cite[Proposition~1.33, pp.~61--62]{Hatcher2002} supplies a continuous function',1)
extension=definition+lemma+'\n'+proof+'\n\n'
log('NUMBERED-DATA','D13','mapsIII:def:torus-extension-data',oldlemma[:oldlemma.index(r'\[')],definition,'Collect exactly the existing hypotheses as numbered data: no compactness, frontier, connectivity, pi1, basepoint or target condition is added or removed.')
log('SINGLE-HOMOTOPY-OWNER','D14','mapsIII:carrier-extension-lemma',carrier[ls:pe],extension,'Move the complete general lemma and its two-stage proof before the two-coordinate application. The new actual subsection is a source placement; it alone earns no criterion credit.')
log('LIFTING-LOCATOR','D18','mapsIII:carrier-extension-lemma','The lifting criterion for the covering R^d to T^d.','Hatcher Proposition 1.33, pp.61–62.','Add the exact primary locus already read in the complete c4 comparison.')
log('LEMMA-TITLE-TAG','D10','mapsIII:carrier-extension-lemma',r'\StatementRecord{mapsIII:carrier-extension-lemma}{proved}{02Q8}{the definitions and constructions stated in the proof}',r'{\normalfont\scriptsize tag 02Q8}\par','Keep the old label and target with its small visible tag; the result has one short mathematical title.')
q7start=carrier.index(r'\begin{proposition}')
smashstart=carrier.index('For either resulting based homotopy $H$')
smashend=carrier.index(r'\end{proof}',smashstart)+len(r'\end{proof}')
smash=carrier[smashstart:smashend].replace('For either resulting based homotopy $H$, and each integer',r'Use either based null-homotopy $H$ from Theorem~\ref{maps:src:B.3.2}.'+'\n'+'For each integer',1)
newcarrier=r'''\subsection{Smash powers of the angle-forgetting maps}
\hypertarget{tag-02Q9}{}\label{mapsIII:carrier-extension-section}

\begin{proposition}[Smash powers of cusp quotient maps]
\hypertarget{tag-02Q7}{}\label{mapsIII:angle-forgotten-one-copy-null}
{\normalfont\scriptsize tag 02Q7}\par
For the original sphere member and $x_0\in W$, every positive
smash power of either map $\widehat q_3$ or $\widehat q_\gamma$
of Definition~\ref{mapsIII:def:cusp-suspension-maps} is based null-homotopic.
\end{proposition}

\begin{proof}
'''+smash+'\n\n'
log('SMASH-SINGLE-PROOF','D12','mapsIII:angle-forgotten-one-copy-null',carrier[q7start:smashend],newcarrier,'The original qhat3 and qhatgamma, basepoint, radial coordinate q=t_c and reduced quotient are exactly Q011/J8. Reuse its full based null-homotopies; retain the entire positive-power formula and compact-Hausdorff descent. The a=1 conclusion and all positive powers are unchanged. The alternate CW construction and cusp-group route remain in the whole old proof and admitted comparison.')
log('REMOVE-PROCESS-INTRO','D07','mapsIII:carrier-extension-section',carrier[:ls],r'\subsection{Smash powers of the angle-forgetting maps}', 'Remove working-edition and second-proof history; the actual nonextension result remains with its own proof, and the quotient maps are defined explicitly.')
tail=carrier[carrier.index(r'\paragraph{Scope and preservation of the other proof.}'):]
log('REMOVE-DUPLICATE-TAIL','D12','mapsIII:angle-forgotten-one-copy-null',tail,'The positive-power proposition ends at its proof.','Remove the duplicate-proof preservation instruction and orphan process/scope paragraph; the distinct embedded-nullbordism construction retains its own result and will receive its own unit review.')
js=quotient.index(r'\begin{proof}',quotient.index(r'\hypertarget{tag-02J8}'))
je=quotient.index(r'\end{proof}',js)+len(r'\end{proof}')
oldj8=quotient[js:je]
cut=oldj8.index('Thus $\\pi\'+[(1-t)\\ell\']$')
newj8=oldj8[:cut]+r'''

\item Apply Lemma~\ref{mapsIII:carrier-extension-lemma} with
$N=N_0$, $r=|q|$, $\alpha=\overline\pi$, $h=\pi'$ and
$L=\ell'$. These are literal identifications of the maps just
constructed, with their inverse notation changes. The neighbourhood
has its product outer collar, and its punctured part is a torus
bundle with connected fibre over the punctured disc; hence the
frontier, connectedness and local path-connectedness conditions hold.
Also $\pi'(x_0)=0$, and
$\overline\pi=\pi'+[\ell']$ verifies the required equality on
fundamental groups. For the three-sphere target take the based
collapse $c_3:T^2\to T^2/T^{2,(1)}=S^2$. For the two-sphere
target take the first-coordinate character $c_\gamma:T^2\to S^1$.
Their suspended formulas are exactly those of
Definition~\ref{mapsIII:def:cusp-suspension-maps}.
The lemma therefore supplies both based null-homotopies, stationary
at $x_0$ and on the exterior.

Before collapsing the basepoint arc, the same two homotopy formulas
in that lemma give the corresponding unreduced homotopies. Their
continuity at both vertices uses the compact torus and is uniform
in the homotopy parameter; $\ell'=0$ fixes the outer collar in the
first stage. In the sphere coordinates
\[
 [r,v]\longmapsto
 (\sin(\pi r/\epsilon)\beta(v),\cos(\pi r/\epsilon)),
 \qquad\beta(0)=e_1,
\]
the second stage moves $x_0$ along
$(\sin(\pi s)e_1,\cos(\pi s))$.
Postcompose by the rotation
\[
 \begin{pmatrix}\cos\pi s&-\sin\pi s\\
                 \sin\pi s&\cos\pi s\end{pmatrix}
\]
on the first and last coordinate plane, fixing the other coordinates.
Matrix multiplication takes that path and the terminal constant to
the lower vertex. This gives the based unreduced null-homotopy.
In the reduced suspension the same arc is already collapsed.
\end{enumerate}
\end{proof}'''
newquotient=quotient[:js]+newj8+quotient[je:]
log('J8-EXACT-APPLICATION','D12','maps:src:B.3.2',oldj8,newj8,'Reuse the preceding sole two-stage suspension proof after matching every input: N0, |q|, alpha, pi-prime, ell-prime, frontier, connected punctured torus bundle, basepoint, pi1 and the two exact based quotient maps. Keep the complete cover/partition/collar construction and unreduced target rotation. No new scope or conclusion.')
source=u.repairs.SOURCE.read_text(encoding='utf-8');assert source.count(carrier)==1 and source.count(quotient)==1
candidate=source.replace(carrier,newcarrier,1).replace(quotient,extension+newquotient,1)
u.check_permanent_identifiers(source,candidate,['mapsIII:def:torus-extension-data'],['tag-Q013'])
cp.write_text(newcarrier,encoding='utf-8',newline='\n');qp.write_text(newquotient,encoding='utf-8',newline='\n');ep.write_text(extension,encoding='utf-8',newline='\n');u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n');r.write_table(r.DEFECTS,df,rows+changes)
print('UTC',datetime.now(timezone.utc).isoformat())
print('DEFECT_ROWS',len(changes),'EXTENSION_LINES',len(extension.splitlines()),'SMASH_LINES',len(newcarrier.splitlines()),'J8_LINES',len(newj8.splitlines()))
print('Q013_CREATED; Q8_PRECEDES_J8; ALL_OLD_IDENTITIES_PRESERVED; NO_READING_CREDIT')
