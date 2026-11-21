from pathlib import Path
import re,json,datetime
from S6_SERIES_PUBLISH_editing import Editor,block
r=Path(__file__).resolve().parents[1];ed=Editor('I')
body=block(ed.text,'fam:src:B.4.1');night=block(ed.text,'night:P5.5')
a=ed.text.index(r'\subsection{Re-derivation of Proposition~\ref{fam:src:B.4.1}}')
b=ed.text.index(r'\section',a+3);oldappendix=ed.text[a:b]
new=night.replace(r'\begin{theorem}\hypertarget{tag-02YQ}{}',
 r'\begin{theorem}[The full automorphism group]\hypertarget{tag-01QF}{}\label{fam:src:B.4.1}\label{fam:st:B.4.1}\hypertarget{tag-02YQ}{}',1)
new=new.replace('The parameter $a\\bmod\\mathbb Z$ acts by translation by $a\\widehat\\delta$.',
 'The parameter $a\\bmod\\mathbb Z$ acts by $\\zeta\\mapsto\\zeta+ae$,\nwhere $e=\\Pi_c\\widehat\\delta$. The exponential group isomorphism\nis $a\\bmod\\mathbb Z\\mapsto e^{2\\pi ia}$.')
i=new.index(r'\item Taking determinants');j=new.index(r'\item A holomorphic',i)
new=new[:i]+r'''\item Proposition~\ref{fam:src:A.1.1} identifies the complete
anticanonical pencil with $f$ and proves that every automorphism
induces the identity on its base.

'''+new[j:]
i=new.index(r'\item A holomorphic');j=new.index(r'\item The linear part',i)
new=new[:i]+r'''\item On each ordinary torus, a lifted holomorphic automorphism
has lattice-periodic derivative, hence constant derivative by
compactness. Thus it is affine. Its integral linear part commutes
with $A_1,A_2$, and \cref{fam:src:A.2.1} gives
$P=aI+bE_{41}$ with $a,b\in\mathbb Z$ and $a=\pm1$.
The identity period columns in $H\Pi=\Pi P$ give $H=aI$;
the first column then gives $b=0$.

'''+new[j:]
old=r'''  The integral mapping-cone calculation in
\path{code/current_audits/audit_paper_i/code/priority_rows_exact.py}
constructs every differential from the cyclic resolutions and the
three overlap restrictions, then checks the same vanishing by Smith
decomposition with unimodular basis changes. All differential,
integral-kernel and image matrices are saved in
\path{priority_rows_exact.output.json}.'''
assert old in new
new=new.replace(old,'')
new=new.replace('On the finite root charts\nordinary logarithms prove the same exact sequence with their finite\nequivariance retained.',
 'On a finite root disc, a holomorphic lift has lattice defect in\n$\\ker N_j=(I-A_j)\\Lambda$, by the saturated-image calculation\nof \\cref{fam:src:A.1.2}. Subtracting a period kills the defect\nand preserves holomorphy. This gives the same exact sequence\nwith its finite equivariance.')
new=new.replace('Here is the integral lattice calculation, including torsion. Put','For the integral lattice cohomology, put')
ed.replace(body,'','D12','Place the full automorphism statement once in its credited appendix, with the exact exponential isomorphism.','fam:src:B.4.1')
ed.replace(oldappendix,'','D12','Archive the second integral cocycle proof. Its coefficient lattice is mapped explicitly to the retained proof by K*T=Q and Q*L=-C, with both determinant signs and integral inverses verified. The finite holomorphic-lift step is incorporated in the retained proof.','app:rederive:fam-src-B.4.1')
newheading=r'\subsection{The full automorphism group}\hypertarget{tag-000E}{}\label{app:rederive:fam-src-B.4.1}'
ed.replace(r'\subsection{All automorphisms and the integral parameter period}',newheading,
 'D14','Locate the credited proof anchor at the unique full automorphism proof.','app:rederive:fam-src-B.4.1:heading')
ed.replace(night,new,'D12','Preserve the full admissible-twist scope, integral translation sheaf, cusp extension, full cocycle lattice and all connected components. Cite the already proved pencil and centralizer instead of repeating their proofs.',
 'night:P5.5')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_automorphism_comparison.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'read_scope':'Complete body statement, full B4.1 credited proof and all six steps of night:P5.5 read before consolidation.',
 'exact_integral_comparison':'records/S6_SERIES_PUBLISH_I_aut_lattice_transport.json',
 'scope':'One full proof with its broader admissible-twist scope; alternate proof retained in exact edit records. This integration claims no independent preread proof.'},indent=2)+'\n')
