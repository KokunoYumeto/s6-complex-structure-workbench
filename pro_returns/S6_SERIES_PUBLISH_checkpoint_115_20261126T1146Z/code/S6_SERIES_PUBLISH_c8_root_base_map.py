"""Give the base map one complete divisor-root nullhomotopy proof."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
path=u.WORK/'root/base_map.tex'
before=path.read_text(encoding='utf-8')
after=r'''\subsection{The holomorphic map to the base}

\begin{theorem}[Null-homotopy of the base map]
\hypertarget{tag-02J6}{}\label{maps:src:B.2.1}
{\normalfont\scriptsize tag 02J6}\par
The holomorphic map $f:X\to\mathbb P^1$ of the original
sphere construction is null-homotopic.
\end{theorem}

\begin{proof}
The two reduced multiple fibres satisfy
$f^*(0)=3S_1$ and $f^*(1)=4S_2$.
Use the base isomorphism
\[
 M[x:y]=[x:y-x],\qquad M^{-1}[a:b]=[a:a+b],
 \qquad \widetilde f=M\circ f.
\]
The two displayed composites are the identity.
For $L=\widetilde f^*\mathcal O_{\mathbb P^1}(1)$,
the coordinate sections have divisors $3S_1$ and $4S_2$.
The divisor identifications are bundle isomorphisms
\[
 \phi_j:\mathcal O_X(S_j)^{\otimes m_j}\longrightarrow L,
 \qquad (m_1,m_2)=(3,4),
\]
taking the powers of the canonical divisor sections to those
coordinate sections.

The smooth sphere $X$ has $H^1(X;\mathbb Z)=H^2(X;\mathbb Z)=0$.
The first Chern class classification
\cite[Proposition~3.10, p.~86]{CuspInvariantHatcherVB}
therefore gives trivializations of $L$ and both divisor line bundles.
Choose smooth nonvanishing frames $\ell,e_1,e_2$.
Such frames follow from continuous ones by smooth approximation:
in a Hermitian norm keep the error below half the positive minimum
norm of the continuous frame on compact $X$.
Define $u_j:X\to\mathbb C^*$ by
$\phi_j(e_j^{\otimes m_j})=u_j\ell$.
The induced map $\pi_1(X)\to\pi_1(\mathbb C^*)=\mathbb Z$
is zero, so the exponential covering has a lift
$b_j:X\to\mathbb C$ with $e^{b_j}=u_j$
\cite[Proposition~1.33, pp.~61--62]{Hatcher2002}.
Local inverse branches of the exponential make the lift smooth.
The compatible frames and their inverse changes are
\[
 e'_j=e^{-b_j/m_j}e_j,\qquad e_j=e^{b_j/m_j}e'_j,
 \qquad \phi_j((e'_j)^{\otimes m_j})=\ell.
\]
Write the canonical divisor sections as $a e'_1$ and $b e'_2$.
They have no common zero, and the two coordinate sections of $L$
give $\widetilde f=[a^3:b^4]$.

Put $r=(|a|^2+|b|^2)^{1/2}>0$ and $G=(a,b)/r:X\to S^3$.
Let $\eta_2:S^3\to\mathbb P^1$ be the Hopf map and set
\begin{equation}
 P_{3,4}(z_1,z_2)=
 \frac{(z_1^3,z_2^4)}{\sqrt{|z_1|^6+|z_2|^8}}.
 \hypertarget{tag-01UY}{}\label{maps:eq:B.2.1}
\end{equation}
The denominator is positive on $S^3$.
The everywhere-defined smooth homotopy
\[
 F_s(x)=[a(x)^3e^{-3s\log r(x)}:
          b(x)^4e^{-4s\log r(x)}],\qquad 0\le s\le1,
\]
has $F_0=\widetilde f$ and $F_1=\eta_2P_{3,4}G$.

For $t=|z_1|^2$, the first squared radius under $P_{3,4}$ is
\[
 R(t)=\frac{t^3}{t^3+(1-t)^4},\qquad
 R'(t)=\frac{t^2(1-t)^3(3+t)}{(t^3+(1-t)^4)^2}>0
 \quad(0<t<1).
\]
Since $R(0)=0$ and $R(1)=1$, a target with both coordinates
nonzero has one source radius and $3\cdot4=12$ phase preimages.
Every local degree is positive, with sign
$\operatorname{sgn}(3\cdot4\,R'(t))$ in the same oriented
radius-and-phase coordinates on source and target. Thus
$\deg P_{3,4}=12$.

For quaternionic multiplication $m:S^3\times S^3\to S^3$
and a generator $\omega\in H^3(S^3;\mathbb Z)$,
the K\"unneth decomposition and the two unit inclusions give
$m^*\omega=\operatorname{pr}_1^*\omega+
\operatorname{pr}_2^*\omega$.
Iteration and pullback along the diagonal show that
$p_{12}(q)=q^{12}$ has degree twelve.
Degree classification
\cite[Corollary~4.25, p.~361]{Hatcher2002}
gives $P_{3,4}\simeq p_{12}$.
On based cube maps to $S^3$, concatenation and pointwise
multiplication have the same unit and satisfy the interchange identity;
hence the latter gives addition in $\pi_6(S^3)$.
Consequently $(p_{12})_*$ is multiplication by twelve and vanishes
on $\pi_6(S^3)=\mathbb Z/12$
\cite[Theorem~5.41(b), p.~573]{HatcherSpectralSequences}.
To pass from $G$ to a based representative, choose $x_0\in X$
and use $G_0(x)=G(x_0)^{-1}G(x)$, with inverse change
$G(x)=G(x_0)G_0(x)$.
A path from $1$ to $G(x_0)^{-1}$ gives a homotopy from $G$ to $G_0$.
It follows that $\eta_2P_{3,4}G$ is null-homotopic.
The homotopy $F_s$ and the displayed inverse $M^{-1}$ prove
that $f$ is null-homotopic.
\end{proof}

'''
u.check_permanent_identifiers(before,after)
source=u.repairs.SOURCE.read_text(encoding='utf-8')
assert source.count(before)==1
candidate=source.replace(before,after,1)
u.check_permanent_identifiers(source,candidate)
df,rows=r.table(r.DEFECTS)
edits=[
 ('ONE-PROOF','D12',before[before.index(r'\begin{proof}'):],after[after.index(r'\begin{proof}'):],'Keep the full divisor-root proof and the shared degree/power calculation as the sole proof; retain both entire predecessor arguments and their exact correspondence in the c4 comparison and this defect record.'),
 ('TITLE','D16',r'\begin{theorem}',r'\begin{theorem}[Null-homotopy of the base map]','Give the theorem its mathematical title.'),
 ('TAG','D10',r'\StatementRecord{maps:src:B.2.1}{proved}{02J6}{the definitions and constructions stated in the proof}',r'{\normalfont\scriptsize tag 02J6}\par','Preserve the existing label and target; print only its small tag.'),
 ('STATEMENT','D02','This conclusion does not\nrequire the choice of $e$.','The holomorphic map of the original sphere construction is null-homotopic.','The single direct proof uses only the divisors and sphere cohomology; remove the defensive methodological sentence without changing the conclusion or its scope.'),
 ('FRAME-INVERSES','D20','Choose frames whose powers equal the chosen frame.',after[after.index('The two reduced'):after.index('Put $r=')],'Write the actual base isomorphism and inverse, divisor-line maps, smooth exponential lift, compatible frame map and inverse, and the resulting coordinate sections.'),
 ('DEGREE-REASONS','D22','Its radial coordinate is strictly increasing; a degree-k map acts by k.',after[after.index('For $t='):after.index('To pass from')],'Print the exact radial derivative, all twelve positive local degrees, multiplication pullback, degree classification and interchange argument.'),
 ('BASED-MAP','D20','The latter map is zero by the exponent twelve.',after[after.index('To pass from'):after.index(r'\end{proof}')],'Specify the based representative, inverse translation and path homotopy before applying pi6.'),
 ('SOURCES','D18','Unlocated line-bundle, logarithm and degree facts.','Hatcher VB Prop.3.10 p.86; AT Prop.1.33 pp.61–62; Cor.4.25 p.361; Spectral Sequences Thm.5.41(b) p.573.','Read the complete VB classification and AT degree-classification proofs at the author source in this continuation; preserve the exact recorded lifting and homotopy-group source scopes.'),
 ('EQUATION','D19',r'\tag{B.2.1}',r'\begin{equation}...\end{equation}','Use automatic section numbering at the same P34 expression with its original label and target.'),
 ('ENUMERATION','D23',r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]','One continuous proof.','Remove the obsolete two-proof machine enumeration with both delimiters.')
]
for key,kind,old,new,reason in edits:
 ident='III-C8-BASE-MAP-'+key
 assert not any(x['change_id']==ident for x in rows)
 rows.append(dict(change_id=ident,type=kind,statement_id='maps:src:B.2.1',old_location='base-map subsection before single-proof consolidation',old_page='pending page concordance',new_location='The holomorphic map to the base',new_page='pending final PDF',old_text=old,new_text=new,reason=reason,review_status='applied; complete readback and final PDF pending'))
path.write_text(after,encoding='utf-8',newline='\n')
u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,rows)
print('UTC',datetime.now(timezone.utc).isoformat())
print('EXACT_DEFECT_ROWS',len(edits))
print('OLD_LINES',len(before.splitlines()),'NEW_LINES',len(after.splitlines()))
print('ONE_DIVISOR_ROOT_PROOF; ALL_OLD_IDENTITIES_PRESERVED; NO_NEW_CREDIT')
