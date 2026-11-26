"""Split and edit the wholly read universal sphere pairing owner only."""
import csv
import hashlib
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation

root = Path(__file__).resolve().parent.parent
folder = root / 'agents/continuation8_iii_integration/units/root'
lane = root / 'agents/continuation8_iii_weighted_units'
source = folder / 'full_sphere_nullity.tex'
target = folder / 'sphere_smash_pairing.tex'
original = source.read_text()
assert hashlib.sha256(source.read_bytes()).hexdigest() == 'e67048a3698b30ddf13eee200894dd8603e4191dedf27dfbdc4e8ce49edb1673'
assert not target.exists()
start = original.index(r'\begin{theorem}[The full external smash pairing is zero]')
end = original.index(r'\paragraph{The one-copy coefficient and the framed fibre.}')
block = original[start:end].rstrip() + '\n'
rows = []
fields = ['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
statement = 'wb:cusp-s12-full-carrier-null'

def record(number, kinds, old, new, reason, oldloc, newloc, owner=statement):
    for kind in kinds:
        rows.append([f'III-C8-SPHERE-PUB-{number:03}-{kind}',kind,owner,oldloc,'pending page concordance',newloc,'pending final build',old,new,reason,'whole input/receiving/comparison read; candidate readback pending; global gates open'])

definition = r'''\subsection{External smash products of sphere maps}

\begin{definition}[Ordered cube spheres]\hypertarget{tag-Q253}{}\label{wb:def:ordered-cube-spheres}
{\normalfont\scriptsize tag Q253}\par
For every integer $d\geq1$, put $C_d=I^d/\partial I^d$, with the
collapsed boundary as basepoint. The based homeomorphism
$h_d:C_d\longrightarrow(S^d,N)$, where $N=(0,\ldots,0,1)$, is
\[
 v_j=\tan\bigl(\pi(u_j-\tfrac12)\bigr),\qquad
 h_d([u])=\left(\frac{2v}{1+\lVert v\rVert^2},
                  \frac{\lVert v\rVert^2-1}{1+\lVert v\rVert^2}\right)
 \quad(u\in(0,1)^d),\qquad h_d(*)=N.
\]
Its inverse off $N$ sends $z=(z',z_{d+1})$ to the class of
\[
 u_j=\tfrac12+\frac1\pi\arctan\frac{z'_j}{1-z_{d+1}};
\]
it sends $N$ to $*$. Approaching the cube boundary makes
$\lVert v\rVert$ tend to infinity, so $h_d$ is continuous there.
The two formulas are inverse on the open cells; compactness of $C_d$
and the Hausdorff property of $S^d$ give continuity of the inverse.

For positive integers $d_1,\ldots,d_k$, define the ordered based
homeomorphism
\[
 \mu_{d_1,\ldots,d_k}:
 C_{d_1}\wedge\cdots\wedge C_{d_k}\longrightarrow C_{d_1+\cdots+d_k},
 \qquad [[u^{(1)}],\ldots,[u^{(k)}]]\longmapsto
 [u^{(1)},\ldots,u^{(k)}].
\]
Its inverse splits an interior point into the displayed blocks and
sends the basepoint to the smash basepoint. The product cube boundary
is exactly the inverse image of the fat wedge, so these maps descend
from the same compact quotient and are inverse homeomorphisms.
The first-coordinate pinch $p_d:C_d\to C_d\vee C_d$ sends
$u_1\leq\tfrac12$ to the first copy with coordinate $2u_1$ and
$u_1\geq\tfrac12$ to the second copy with coordinate $2u_1-1$.
The middle face and boundary map to the basepoint.
Thus $(f\vee g)p_d$ is the representative of addition in
$\pi_d$ in these coordinates \cite[pp.~340--341]{Hatcher2002}.
\end{definition}

'''
record(1,['D13','D20','D22'],'',definition,
       'Give the cube model, explicit sphere map/inverse, ordered block map/inverse and actual pinch before the universal statement. This replaces the construction prerequisite in later 036J by the complete local definition.',
       'full_sphere_nullity.tex before original 038V','root/sphere_smash_pairing.tex input definition','wb:def:ordered-cube-spheres')

native_statement = r'''In particular, the continuous surjective quotient
$\widehat q_3^{\wedge2}:S^{12}\twoheadrightarrow S^6$ of
\cref{wb:cusp-cone-sphere-to-sphere-maps} is based null-homotopic.
'''
assert block.count(native_statement) == 1
candidate = block.replace(native_statement, '')
native_proof = r'''Taking $x=y=\widehat q_3$ in the based sphere identifications proves
the asserted null-homotopy.  Its continuity, surjectivity and quotient
property follow from
\cref{wb:cusp-cone-angle-forgotten-sphere-carriers}.
'''
assert candidate.count(native_proof) == 1
candidate = candidate.replace(native_proof, '')
old_cube = candidate[candidate.index('Use the cube sphere identifications of'):candidate.index('For $x,y:C_6')]
new_cube = r'''Use the based sphere models, concatenation maps and pinch maps of
Definition~\ref{wb:def:ordered-cube-spheres}.

'''
candidate = candidate.replace(old_cube,new_cube,1)
old_higher = r'''Use the cube models $C_d=[0,1]^d/\partial[0,1]^d$ and the ordered
concatenation homeomorphisms of
\cref{wb:cusp-cone-angle-forgotten-sphere-carriers}.
Write $\mu_{d_1,\ldots,d_k}$ for concatenation of these blocks;
its inverse splits the nonboundary coordinates into the same blocks
and sends the quotient basepoint to the smash basepoint.
'''
new_higher = r'''Use $C_d$ and the ordered block homeomorphisms
$\mu_{d_1,\ldots,d_k}$ of Definition~\ref{wb:def:ordered-cube-spheres}.
'''
assert candidate.count(old_higher)==1
candidate = candidate.replace(old_higher,new_higher)
record(2,['D12','D14','D20','D22'],old_cube+old_higher,new_cube+new_higher,
       'Both proofs use the same locally defined C_d, ordered concatenation and first-coordinate pinch. Exact block maps/inverses and all fat-wedge arguments remain; the removed repetitions correspond term-for-term to Q253.',
       'full_sphere_nullity.tex 038V/038T cube paragraphs','root/sphere_smash_pairing.tex two proofs')
for tag,label in [('038V','wb:cusp-s12-full-carrier-null'),('038T','wb:cusp-s12-all-higher-smashes-null')]:
    old='\\hypertarget{tag-'+tag+'}{}\\label{'+label+'}\n'
    new=old+'{\\normalfont\\scriptsize tag '+tag+'}\\par\n'
    assert candidate.count(old)==1
    candidate=candidate.replace(old,new)
    record(3 if tag=='038V' else 4,['D10'],old,new,'Show the existing permanent result identifier in a small tag; preserve its label and target multiplicity.',
           'full_sphere_nullity.tex '+tag+' header','root/sphere_smash_pairing.tex '+tag+' header',label)
early = definition + candidate

application = r'''\begin{corollary}[The two-copy sphere carrier]\hypertarget{tag-Q254}{}\label{wb:cusp-s12-native-smash-null}
{\normalfont\scriptsize tag Q254}\par
The specified continuous surjective based quotient
$\widehat q_3^{\wedge2}:S^{12}\twoheadrightarrow S^6$ of
\cref{wb:cusp-cone-sphere-to-sphere-maps} is based null-homotopic.
\end{corollary}

\begin{proof}
Let $d:C_6\to(X,x_0)$ and $\phi:\Sigma_r S^2\to C_3$ be the fixed
based identifications in
\cref{wb:cusp-cone-angle-forgotten-sphere-carriers}, and set
$g_C=\phi\widehat q_3d$. The displayed two-copy quotient, in those
coordinates, is exactly
\[
 \mu_{3,3}(g_C\wedge g_C)\mu_{6,6}^{-1}:C_{12}\longrightarrow C_6.
\]
The inverse coordinate maps are $d^{-1}$, $\phi^{-1}$ and the block
splittings in Definition~\ref{wb:def:ordered-cube-spheres}.
Apply \cref{wb:cusp-s12-full-carrier-null} to $x=y=g_C$.
The original quotient's continuity, surjectivity and quotient property
are those proved in \cref{wb:cusp-cone-angle-forgotten-sphere-carriers};
the displayed based homeomorphisms transport its based null-homotopy.
\end{proof}

'''
remaining = original[:start] + application + original[end:]
record(5,['D13','D14','D26'],block,early+application,
       'Relocate the complete universal 038V/038T results and proofs before carriers. Their sole geometric application remains after 035X/036J/037L as Q254, with the exact coordinate transport and inverses. Equations0390/0392/0391 remain in the universal proof. All original conclusions remain in the union of the two owners.',
       'full_sphere_nullity.tex original complete 038V and 038T blocks',
       'root/sphere_smash_pairing.tex complete unit; root/full_sphere_nullity.tex Q254')
for text in [early,remaining]:
    assert '\r' not in text
    _,changes,issues = presentation.statement_records_to_small_tags(text)
    assert not changes and not issues
    _,changes,issues,aliases = presentation.remove_manual_equation_tags(text)
    assert not changes and not issues and not aliases
    assert not presentation.unresolved_literal_equation_references(text)
allowed_labels=['wb:def:ordered-cube-spheres','wb:cusp-s12-native-smash-null']
allowed_targets=['tag-Q253','tag-Q254']
units.check_permanent_identifiers(original,early+remaining,allowed_labels,allowed_targets)
target.write_text(early,encoding='utf-8',newline='\n')
source.write_text(remaining,encoding='utf-8',newline='\n')
with (lane/'S6_SERIES_PUBLISH_SPHERE_PAIRING_publication_defects.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(fields);w.writerows(rows)
print('ORIGINAL',len(original.splitlines()),hashlib.sha256(original.encode()).hexdigest())
print('EARLY',len(early.splitlines()),hashlib.sha256(early.encode()).hexdigest())
print('NATIVE_REMAINDER',len(remaining.splitlines()),hashlib.sha256(remaining.encode()).hexdigest())
print('EXACT_EDITS',5,'DEFECT_ROWS',len(rows),'NEW_IDS','Q253,Q254')
print('ALL_OLD_LABEL_AND_TARGET_MULTIPLICITIES_PRESERVED_ACROSS_THE_TWO_OWNERS')
print('NO_CANONICAL_OR_SHARED_TABLE_WRITES; NO_CRITERION_OR_INDEPENDENT_CHECK_CREDIT')
