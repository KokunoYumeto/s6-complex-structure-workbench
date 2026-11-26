from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

p=Package('curve','The reduced resolved-conductor case / before night:P4.25')
source=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
old_owner=block(source,'lem:II:plane-branch-conductor')
fragment=r'''\begin{lemma}[Conductor exponents of plane branches]\hypertarget{tag-P282}{}\label{lem:II:plane-branch-conductor}
\StatementRecord{lem:II:plane-branch-conductor}{proved}{P282}{\cite[Tag~0A7M, Lemmas~47.16.1, 47.16.4 and~47.16.7]{StacksProject}}
Let $h=u\prod_{j=1}^r f_j$ be a reduced plane-curve equation, with $u$ a unit and $f_j$ the equations of its distinct irreducible branches. On the normalization of branch $C_i$, let $c_i$ be the exponent of the conductor of the whole curve and let $c_i^{\rm int}$ be the conductor exponent of that branch alone. Then
\[
 c_i=c_i^{\rm int}+\sum_{j\ne i}I(C_i,C_j),\qquad
 c_i^{\rm int}=2\delta(C_i),\qquad
 \sum_i c_i=2\delta(h).
\]
In particular, $c_i=1$ implies that $C_i$ is smooth and meets precisely one other branch, smoothly and transversely. If $c_i=2$, the other branches, counted with their positive intersection multiplicities, number at most two.
\end{lemma}
\begin{proof}
Put $A=\mathbb C\{x,y\}/(h)$, let $B=\prod_i\mathbb C\{t_i\}$ be its finite normalization, and put $Q=B/A$. The one-dimensional hypersurface ring $A$ is Gorenstein, with normalized dualizing complex $A[1]$. A nonzerodivisor of $A$ acts injectively on $B$, so $B$ is a maximal Cohen--Macaulay $A$-module. Lemma~47.16.7 of \cite[Tag~0A7M]{StacksProject}, applied with this dualizing complex, gives $\operatorname{Ext}^1_A(B,A)=0$.

Inside the total quotient ring of $A$, every $A$-linear map $B\to A$ is multiplication by its value at $1$. Thus
\[
 I=\operatorname{Hom}_A(B,A)=\{a\in A:aB\subset A\}
\]
is the conductor. Since $Q$ has finite length and $A$ has depth one, $\operatorname{Hom}_A(Q,A)=0$. Applying $\operatorname{Hom}_A(-,A)$ to $0\to A\to B\to Q\to0$ gives
\[
 0\longrightarrow I\longrightarrow A\longrightarrow
 \operatorname{Ext}^1_A(Q,A)\longrightarrow0.
\]
For the normalized complex $A[1]$, Lemma~47.16.4 of \cite[Tag~0A7M]{StacksProject} identifies $\operatorname{Ext}^1_A(Q,A)$ with the Matlis dual of $Q$. This exact duality preserves length: it sends the unique simple module $\mathbb C$ to $\mathbb C$ and reverses a composition series. Hence
\[
 \operatorname{length}(A/I)=\operatorname{length}(B/A)=\delta(h),
 \qquad \operatorname{length}(B/I)=2\delta(h).
\]
The conductor is the product of the ideals $(t_i^{c_i})$ in the normalization, so the second length is $\sum_i c_i$. Applying the same argument to the individual branch ring gives $c_i^{\rm int}=2\delta(C_i)$.

Choose a linear coordinate $x$ nonconstant on every branch and a complementary coordinate $y$ generically. Hypersurface adjunction gives the residue generators $dx/h_y$ for $\omega_A$ and $dx/(f_i)_y$ for $\omega_{C_i}$. The finite duality of \cite[Tag~0A7M, Lemma~47.16.1]{StacksProject}, applied to each local finite map $A\to\mathbb C\{t_i\}$ and then taking their product, identifies
\[
 \omega_B=\operatorname{Hom}_A(B,\omega_A)=I\omega_A.
\]
These are submodules of the meromorphic differentials on the normalized branches: the birational normalization identifies them at the generic points, where the finite-duality trace is the identity. On $C_i$ one has
\[
 h_y|_{C_i}=u|_{C_i}\,(f_i)_y|_{C_i}\prod_{j\ne i}f_j|_{C_i}.
\]
The additional pole of $dx/h_y$ relative to $dx/(f_i)_y$ therefore has order $\sum_{j\ne i}I(C_i,C_j)$. The displayed conductor-module identity gives the claimed branch formula. Intersection multiplicities of distinct plane branches are positive integers. The cases $c_i=1,2$ follow; intersection multiplicity one makes both branches smooth and transverse.
\end{proof}
'''

p.guard('remove later P282 owner',old_owner,'','The complete plane-curve owner moves before its earliest consumer P4.25.')
p425=block(source,'night:P4.25')
firstline=p425.splitlines()[0]
p.guard('place P282 before P4.25',firstline,fragment+'\n'+firstline,'This insertion precedes both P4.25 and P4.34 and preserves the existing subsection boundary.')
p.record('D12,D14','lem:II:plane-branch-conductor',old_owner,fragment,'Transfer the complete one-dimensional Hom/Ext conductor calculation from P4.34 into P282, together with its total-conductor conclusion; retain the intrinsic-branch and intersection formulas. The same plane ring, normalization, conductor ideal and residue modules are used. Remove the P4.34 forward dependency and put this owner before P4.25.')
p.record('D17,D18,D25','lem:II:plane-branch-conductor','Gorenstein duality gives length(A/I)=delta; finite duality identifies regular differentials.','A[1], the explicit Hom/Ext exact sequence, Matlis composition-series length, and finite duality on each normalized branch are written in the proof.','Opened and read Stacks 0A7M Lemmas47.16.1,47.16.4,47.16.7 and their complete proofs. Their Noetherian local and finite-module hypotheses apply directly to the convergent plane hypersurface ring. No surface-conductor lemma is applied to a curve.')

old='ordinary node. Indeed the conductor exponent on\nbranch $i$ is\n$2\\delta_i+\\sum_{j\\ne i}I_{ij}$; positivity of\nintersection multiplicities leaves exactly two\nsmooth transverse branches.'
new='ordinary node by \\cref{lem:II:plane-branch-conductor}, applied to the reduced transverse plane equation and its normalization branches.'
assert old in p425
p.guard('P4.25 plane-branch application',old,new,'The exponent-one conclusion is exactly the c_i=1 clause of P282 at the same reduced transverse curve.')
p.record('D12,D14','night:P4.25',old,new,'The transverse slice of the Cartier surface support gives the reduced plane ring of P282. Conductor exponent one forces precisely the same two smooth transverse branches; the complete later log-canonical, normalization and vanishing-cycle arguments stay in this owner.')

p434=block(source,'night:P4.34')
a=p434.index('The identity $\\sum_i(v_i-r_i)=2\\delta(C,p)$ follows from')
b=p434.index('Choose a generic plane coordinate $x$',a)
old=p434[a:b]
new=r'''Apply \cref{lem:II:plane-branch-conductor} to $A=\mathbb C\{x,y\}/(h)$ and its finite normalization $B$. For its conductor $I=\operatorname{Hom}_A(B,A)$ and branch exponents $c_i$, the lemma gives $\sum_i c_i=\operatorname{length}(B/I)=2\delta(C,p)$ and the identity $\omega_B=I\omega_A$ inside the meromorphic differentials.
'''
p.guard('P4.34 finite-curve-duality application',old,new,'The full conductor-length proof is now at P282; retain the derivative valuations and conormal calculation here.')
p.record('D12,D14','night:P4.34',old,new,'Map A, B, I and delta identically to P282. The subsequent primitive-kernel valuation v_i, ramification r_i, residue order r_i−v_i, equality c_i=v_i−r_i and tau_p−r_p=4delta remain unchanged. Thus the stronger conormal-defect conclusion retains its original owner.')

for row in p.rows:
    if row['statement_id'].startswith('night:'):
        row['old_location']=row['statement_id']+' / complete current proof'
p.write(fragment)
