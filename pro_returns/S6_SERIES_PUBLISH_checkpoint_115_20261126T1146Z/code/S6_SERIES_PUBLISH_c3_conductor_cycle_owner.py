"""Extract the exact local branch count from the complete conductor-graph proof."""
from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text();i=s.index(r'\label{night:P4.35}')
a=s.rfind(r'\begin{proposition}',0,i);b=s.index(r'\end{proof}',i)+len(r'\end{proof}')
old=s[a:b]
ea=old.index(r'\item',old.index(r'\begin{enumerate}'))
eb=old.index(r'\end{enumerate}',ea)
parts=[r'\item'+x for x in old[ea:eb].split(r'\item')[1:]]
assert len(parts)==8
lemma=r'''\begin{lemma}[Two image branches force a conductor cycle]\hypertarget{tag-P255}{}\label{lem:II:conductor-two-branch-cycle}
\StatementRecord{lem:II:conductor-two-branch-cycle}{proved}{P255}{\cref{lem:II:conductor-duality}; \cite[Tags~0AG0 and 0BBZ, Lemmas~15.123.2 and 10.60.12]{StacksProject}}
Let $\nu:N\to S$ be the finite normalization of a reduced hypersurface in a smooth complex threefold. Let $C$ be a compact irreducible component of the reduced image conductor, and let $D\subset N$ be the union, with reduced structure, of the conductor curves which dominate $C$. Put $c=b_0(D^\nu)$ and $k=b_0(D)$, and let $\beta(D)$ be the cycle rank of its normalization-incidence graph. At a point $p\in C$ with exactly two analytic branches and lying on no other image-conductor component, one has
\[
 \sum_{q\in\nu^{-1}(p)}\bigl(|\kappa^{-1}(q)|-1\bigr)\ge c,
 \qquad \beta(D)\ge k\ge1,
\]
where $\kappa:D^\nu\to D$ is normalization. In particular, a conductor with an acyclic normalization-incidence graph has no such image point.
\end{lemma}
\begin{proof}
Let $\eta:C^\nu\to C$ be normalization and $h=\nu|_D$. Integral closure gives the unique factorization
\[
 h\kappa=\eta\phi,\qquad \phi:D^\nu\to C^\nu.
\]
Each normalized component of $D$ maps nonconstantly, because $\nu$ is finite. It is compact, so its map to the connected compact curve $C^\nu$ is finite and surjective. Write $p_+,p_-$ for the preimages of $p$.

The $n$ points of $\nu^{-1}(p)$ correspond to the irreducible analytic hypersurface branches of $S$ at $p$. Every pair of distinct branches meets in a curve: their nonassociate irreducible equations in the regular local ring of dimension three have height two. The height bounds are \cite[Tags~0AG0 and 0BBZ, Lemmas~15.123.2 and 10.60.12]{StacksProject}; a common height-one prime would make the two factors associates. Their intersection is in the nonnormal locus, and hence in $C$ near $p$, since no other image component passes through $p$.

Every point over $p$ lies on $D$. With at least two surface branches this follows from those pairwise intersections. With one surface branch it follows by taking the finite inverse image of either conductor-curve branch through $p$. The conductor purity of \cref{lem:II:conductor-duality} also excludes an isolated conductor component. For each normalization point record the nonempty subset of $\{+,-\}$ consisting of the image branches of its local conductor curves. The pairwise surface intersections make these subsets pairwise intersect. Such a family has a common element: a singleton forces its element into all subsets, and in the absence of a singleton every subset is $\{+,-\}$. Interchange the labels to make the common element $+$.

Let $r_+$ and $r_-$ be the numbers of points of $D^\nu$ above $p_+$ and $p_-$ under $\phi$, and put $r_q=|\kappa^{-1}(q)|$. Every normalization point over $p$ has a plus branch, so $r_+\ge n$. Surjectivity on each of the $c$ normalized components gives $r_-\ge c$. Therefore
\[
 \sum_{q\in\nu^{-1}(p)}(r_q-1)=r_++r_--n\ge c.
\]
The normalization-incidence graph of a reduced compact curve with $k$ connected components and $c$ normalized components has cycle rank
\[
 \beta(D)=k-c+\sum_{q\in D}(r_q-1).
\]
Every term outside $\nu^{-1}(p)$ is nonnegative. The preceding inequality gives $\beta(D)\ge k$, proving the assertions.
\end{proof}

'''
prefix=old[:old.index(r'\begin{proof}')]
prefix=prefix.replace(r'\StatementRecord{night:P4.35}{proved}{02X8}{}',r'\StatementRecord{night:P4.35}{proved}{02X8}{\cref{lem:II:conductor-two-branch-cycle,night:P4.26,night:P4.33,night:P4R.6}}')
first=r'''\item Let $\nu:N\to S$ be normalization and $D\subset N$ its reduced conductor. The finite-duality ideal of \cref{lem:II:conductor-duality} and its quotient are pure in the required dimensions, so $D$ has no isolated component. Suppose that its normalization-incidence graph is a forest and its image $C$ is an irreducible rationally normalized curve with exactly one identification cycle. The graph formula gives a unique two-branch point $p\in C$, with every other point unibranch. Apply \cref{lem:II:conductor-two-branch-cycle} to this whole image curve and its same inverse conductor $D$. Its inequality is $\beta(D)\ge b_0(D)\ge1$, contradicting the forest. This proves the general conductor assertion.

'''
new=lemma+prefix+r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
'''+first+''.join(parts[3:])+r'''\end{enumerate}
\end{proof}'''
apply_edit(old,new,'II-C3-CONDUCTOR-TWO-BRANCH-OWNER',['D12','D14','D22'],
 'lem:II:conductor-two-branch-cycle; night:P4.35; night:P4.34',
 'Conductor graph and rational Euler-number proof',
 'Move the full normalization factorization, hypersurface branch intersections, r-plus/r-minus counts and graph inequality into one earlier owner. State its exact componentwise scope at a two-branch point outside the other image components, already used later for D_B over B. The original rational and ruled-forest conclusions apply it on the identical nu,D,C; every rational-exceptional and subtree-contraction proof step remains.',
 'Complete original P4.35 proof and all original local count maps read by root; complete receiving comparison follows.')
apply_edit(r'\subsection{The conductor graph excludes Euler number one in the rational case}',
 r'\subsection{Conductor graphs and rational Euler numbers}',
 'II-C3-CONDUCTOR-GRAPH-TITLE',['D14'],'night:P4.35','Subsection title',
 'Name the common conductor graph calculation and its rational Euler application.',
 'The full original and receiving subsection content was compared.')
anchor=r'\item \SeriesRef{night:P4.35}\quad Acyclic normalization conductors.'
if SOURCE.read_text().count(anchor)==1:
    apply_edit(anchor,r'\item \cref{lem:II:conductor-two-branch-cycle}\quad Two image branches force a conductor cycle.'+'\n'+anchor,
      'II-C3-CONDUCTOR-CYCLE-FURTHER-RESULT',['D24'],'lem:II:conductor-two-branch-cycle','Further results',
      'List the single exact branch-count owner before its conductor-forest application.',
      'Full statement and proof compared.')
path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,rows=read_tsv(path)
for row in rows:
    if row['paper']=='II' and row['unit_id']=='night:P4.35':row['unit_title']='Conductor graphs and rational Euler numbers'
write_tsv(path,fields,rows)
print('P255 inserted with the full local count; all later P4.35 proof steps remain for receiving review.')
