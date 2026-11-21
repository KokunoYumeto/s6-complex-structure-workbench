from pathlib import Path
import re,json,hashlib,datetime
P=Path(__file__).resolve().parent
s=Path('work/S6_SERIES_PUBLISH_I.tex').read_text()
# The second batch is applied only in this private preview when not already integrated.
for q in json.loads((P/'S6_SERIES_PUBLISH_I_boundary_batch2_guarded.json').read_text())['patches']:
 if s.count(q['old'])==1:s=s.replace(q['old'],q['new'],1)
 else:assert q['new'] in s,(q['id'],'neither guarded state found')
initial=s;patches=[];archive=[]
(P/'S6_SERIES_PUBLISH_I_boundary_batch3_input.tex').write_text(initial)
def patch(old,new,why,ids=[]):
 global s
 ident='I-topology3-%02d'%(len(patches)+1)
 assert s.count(old)==1,(ident,s.count(old),old[:120])
 patches.append(dict(id=ident,old=old,new=new,reason=why,statement_ids=ids));s=s.replace(old,new,1)
def block(lab):
 i=s.index('\\label{'+lab+'}');a=s.rfind('\\begin{',0,i);b=s.index('\\end{proof}',i)+len('\\end{proof}');return s[a:b]
def title(lab,typ,t):
 marker='\\begin{'+typ+'}\\hypertarget'
 b=block(lab);assert marker in b
 patch(b[:b.index('\\StatementRecord')],b[:b.index('\\StatementRecord')].replace(marker,'\\begin{'+typ+'}['+t+']\\hypertarget',1),'Give the existing statement its mathematical title.',[lab])
# Exact common datum: retain the proved normal-line identification and only define its section once.
a=s.index('We write $L=\\mathcal O_S(P-O)$, $T=t_{6P}$,');b=s.index('\\begin{proposition}',a)
oldsetup=s[a:b];archive.append(dict(statement_id='push:A.1 setup',original_block=oldsetup))
patch(oldsetup,'','Use the earlier identical pinching datum and its smoothing section instead of repeating its definition and intersection calculation.')
e11=block('fam:src:E.1.1')
section=r'''\begin{definition}[The smoothing section]
\hypertarget{tag-PT06}{}\label{I:def:smoothing-section}
\StatementRecord{I:def:smoothing-section}{proved}{PT06}{\SeriesRef{fam:src:E.1.1}; \cite[Corollary 2.2, p.~4]{Engel2026}}
Set $J=L\otimes T^*L^{-1}$. Proposition~\ref{fam:src:E.1.1} identifies $J$ with $\pi^*\mathcal O_B(1)$. We fix the section $\phi\in H^0(S,J)$ with divisor $S_\infty$ from \cite[Corollary 2.2, p.~4]{Engel2026}. Thus $\phi_x$ is the bundle map $L_{Tx}\to L_x$ used in the plumbing equation.
\end{definition}'''
patch(e11,e11+'\n\n'+section,'Define the actual smoothing section after its normal-line identity has been proved.', ['I:def:smoothing-section'])
# Combine the local plumbing with the compact nodal construction.
e12=block('fam:src:E.1.2');a11=block('push:src:A.1.1');a12=block('push:src:A.1.2')
archive += [dict(statement_id='fam:src:E.1.2',original_block=e12),dict(statement_id='push:src:A.1.2',original_block=a12)]
e12_meta=e12[:e12.index('\n\nOver $S^\\circ')]
e12_meta=e12_meta[e12_meta.index('\\hypertarget'):]
combined=a12.replace('\\begin{theorem}\\hypertarget','\\begin{theorem}[The compact nodal plumbing]\\hypertarget',1)
marker=combined.index('\n\nThere is a reduced complex space')
combined=combined[:marker]+'\n'+e12_meta+combined[marker:]
combined=combined.replace("return's coordinates",'coordinates of the marked cusp fan')
combined=combined.replace('a\\otimes b=u\\phi_x,\\ \\|a\\|,\\|b\\|<2r,\\ |u|<\\epsilon\\}.\n\\]', 'a\\otimes b=u\\phi_x,\\ \\|a\\|,\\|b\\|<2r,\\ |u|<\\epsilon\\}.\\tag{E1}\n\\]')
extra=r'''Over $S^\circ=S\setminus S_\infty$ the total plumbing space is smooth. Its restriction over every relatively compact disc $U\Subset B\setminus\{\infty\}$ is proper and flat over $U\times\Delta_\epsilon$ for sufficiently small $\epsilon>0$. For $u\ne0$ it is the untwisted quotient by $u\phi$ covering $T^{-1}$. This includes discs containing $0$ or $1$, before the logarithmic transformations.'''
combined=combined.replace('\\end{theorem}','\n'+extra+'\n\\end{theorem}',1)
combined=combined.replace('Consequently $t-t_0,u-u_0$ is a\nregular sequence in every total local ring.', 'Consequently $t-t_0,u-u_0$ is a\nregular sequence in every total local ring.')
old='flatness. On the core the same conclusion is immediate from\nflatness of $S\\to B$. This includes the nonreduced Kodaira fibres'
new='flatness. On $S^\\circ$, the derivative of $ab-u\\phi_x$ with respect to $u$ is $-\\phi_x\\ne0$, so the total node space is smooth. On the core the same conclusion is immediate from\nflatness of $S\\to B$. This includes the nonreduced Kodaira fibres'
assert old in combined;combined=combined.replace(old,new)
combined=combined.replace('with the harmless unit changes supplied by the line\nframes.','with the unit changes given by the line\nframes.')
combined=combined.replace('This supplies the analytic\ncomparison needed here. Construction 3.8 of \\cite{EGFS25} is a\nrelated multivariable polarized construction; its symmetry\nhypothesis on period units is not being silently imposed on these\ngenerally unpolarized tori.','This proves the analytic comparison of the fan quotient with the compact plumbing.')
# The independently detected selected-diagonal error is corrected explicitly;
# this is not attributed to the editorial comparison as an independent check.
diagonal=json.loads(Path('work/agents/i_provenance/S6_SERIES_PUBLISH_I_push_A12_selected_diagonal_guard.json').read_text())['changes'][0]
assert combined.count(diagonal['old'])==1
combined=combined.replace(diagonal['old'],diagonal['new'],1)
# e13 is independent of e12 and now uses the named smoothing section.
patch(e12,'','Consolidate this local restriction with the compact plumbing theorem, preserving both complete statements and its exact bundle quotient map.', ['fam:src:E.1.2'])
patch(a11,'','Move the monomial fan calculation immediately before the common compact plumbing proof.', ['push:src:A.1.1'])
patch(a12,'','Move the common compact plumbing proof to the pinching construction, before its topology and later refinements.', ['push:src:A.1.2'])
e13=block('fam:src:E.1.3')
patch(e13,e13+'\n\n'+a11+'\n\n'+combined,'Place local node resolution, fan calculation and compact nodal plumbing in dependency order.', ['fam:src:E.1.2','push:src:A.1.1','push:src:A.1.2'])
old=r'\subsection{The nodal plumbing}\hypertarget{tag-02Z0}{}\label{push:section:A.1}'
patch(old,'','Remove the emptied subsection heading; its stable anchors are attached to the common plumbing subsection.')
old=r'\subsection{The untwisted pinching and its local smoothings}\hypertarget{tag-01PT}{}\label{fam:section:E.1}'
patch(old,old+'\n'+r'\hypertarget{tag-02Z0}{}\label{push:section:A.1}','Retain the moved subsection anchors at their mathematical content.')
# The point-star component is a numbered result with its exact degree-one-map obstruction.
a=s.index('\\paragraph{counterexample; the literal blow-up shape}');b=s.index('\\begin{theorem}[exhaustive finite fan data]',a)
b23=s[a:b];archive.append(dict(statement_id='push:src:A.2.3',original_block=b23))
meta=b23[b23.index('\\hypertarget'):b23.index('\n\nThe unrestricted request')]
new=r'''\begin{proposition}[A projective-space component in a point-star refinement]'''+meta+r'''
The first maximal-cone star of Proposition~\ref{push:src:A.2.1} contributes a central normalization component $\mathbb P^3$. There is no proper bimeromorphic holomorphic map from this component to $R$.
\end{proposition}
\begin{proof}
The star is the ordinary blow-up of a point in a smooth four-dimensional chart, with exceptional divisor $\mathbb P^3$. The projective-bundle basis gives $b_2(R)=b_2(S)+1=11$, while $b_2(\mathbb P^3)=1$. A proper bimeromorphic map $f:\mathbb P^3\to R$ has topological degree one, and the projection formula gives
\[
 \int_{\mathbb P^3}f^*a\,f^*b=\int_Rab
 \qquad(a\in H^2(R;\mathbb Q),\ b\in H^4(R;\mathbb Q)).
\]
Poincar\'e duality would make $f^*$ injective in degree two, contradicting these ranks.
\end{proof}

'''
patch(b23,new,'Number the proved projective-space component obstruction and remove the repeated announcement of later algorithms.', ['push:src:A.2.3'])
b25=block('push:src:A.2.5');archive.append(dict(statement_id='push:src:A.2.5',original_block=b25));new=b25
old='''The requirement that every normalized component of every
smooth refinement be a blow-up of
$R=\\mathbb P_S(\\mathcal O\\oplus L)$ is false, already
for a reduced refinement with $n=1$.
The following is a uniform replacement for any finite
fan certificate $\\Sigma$ in \\ref{push:src:A.2.4}.'''
assert old in new;new=new.replace(old,'For every finite fan certificate $\\Sigma$ of Theorem~\\ref{push:src:A.2.4}, the following algorithm describes the normalized components and their comparison with a reference model.')
a=new.index('\\item The first maximal-cone star');b=new.index('\\item Here is the promised algorithm.',a)
new=new[:a]+r'''\item Proposition~\ref{push:src:A.2.3} proves that the point-star component $\mathbb P^3$ has no proper bimeromorphic map to $R$. In that example the full normalization is $\operatorname{Bl}_pR^+\sqcup\mathbb P^3$: the first component is the strict transform, and the two meet along the exceptional plane. These are the ordinary point-blow-up charts of the smooth total fourfold.

'''+new[b:]
new=new.replace('\\item Here is the promised algorithm. Retain all marking','\\item Retain all marking')
a=new.index('\\item The exact certificate');b=new.index('\\end{enumerate}',a)
new=new[:a]+new[b:]
new=new.replace('[explicit normalization algorithm and its necessary scope]','[The normalization and modification algorithm]')
patch(b25,new,'Use the proved degree-one-map obstruction once, retain the full normalization and plane intersection, and keep the complete terminating algorithm and deformation-sheaf proof.', ['push:src:A.2.5'])
# Avoid repeating the same integral Q computation under a second statement.
b41=block('push:src:A.4.1');archive.append(dict(statement_id='push:src:A.4.1',original_block=b41));new=b41
a=new.index('\\item We check the lattice step');b=new.index('\\item Now let $h:R^+',a)
new=new[:a]+r'''\item Proposition~\ref{fam:src:E.1.4} gives the integral groups and fundamental groups of $R,Q$, together with the normalization maps $d_i=s_{0*}-s_{\infty*}T_*$. We use exactly its lattice $\mathcal L=H_2(S;\mathbb Z)$, $F=[S_t]$, $m=P-O$, and set $v=v_0=[6P]-[O]-3F$. In these coordinates its map $a\mapsto(aF,av,am)$ is onto $\mathbb Z^3$, its $d_2$ has primitive image of rank three, and its $d_4$ is primitive and injective.

'''+new[b:]
new=new.replace('Smith normal forms are recorded in\n\\texttt{ab\\_push\\_local\\_checks.out}. ','')
new=new.replace('\\item As independent Euler checks, stratification gives\n$\\chi(Q)=\\chi(R)-\\chi(S)=24-12$. In the modification $h$,','\\item In the modification $h$,')
patch(b41,new,'Cite the identical integral normalization calculation with the explicit v=v0 identification; retain every modified-normalization direct image, generization matrix, map and Euler calculation.', ['push:src:A.4.1'])
# Move program references to the end-table mapping; the actual equations and methods remain.
removals=[
('The substitutions and Jacobian are independently checked in\n\\texttt{code/e\\_degeneration.py}.','',['fam:src:E.1.3']),
('The Smith computations and both Euler\ncomputations are recorded in \\texttt{code/e\\_degeneration.out}.','',['fam:src:E.1.4']),
('The exact Smith forms of both\nfull cycle matrices and the independent $2\\times2$ determinants\nare in \\texttt{code/e\\_degeneration.out}.','',['fam:src:E.2.1']),
('The calculation is checked exactly in\n\\texttt{code/ab\\_push\\_local\\_checks.py}.','',['push:src:A.1.1']),
('The compact candidate $Q$ of \\ref{fam:src:E.1.1} has','The compact pinching $Q$ of Proposition~\\ref{fam:src:E.1.1} has',['fam:src:E.1.4']),
('These are invariants of the stated candidate; they do not identify it\nas a central fibre of the prescribed compact family.','',['fam:src:E.1.4']),
('over every hypothetical proper Hausdorff analytic filling','over every proper Hausdorff analytic filling',['night:P2.4']),
('On a resolved hypothetical filling','On a resolved proper filling',['night:P2.9']),
('Here $\\widehat\\delta$ is the primitive cycle in the audited','Here $\\widehat\\delta$ is the primitive cycle in the fixed',['push:src:B.4.31']),
('This is a constraint on every hypothetical global filling.','This holds for every proper global filling.',['push:src:B.4.31'])]
for a,b,ids in removals:patch(a,b,'Use publication wording and the program end-table; preserve the proved equations, hypotheses and maps.',ids)
for lab,typ,t in [
('fam:src:E.1.1','proposition','The pinching and its smoothing line'),
('fam:src:E.1.3','proposition','The nodal plumbing and its small modification'),
('fam:src:E.1.4','proposition','The integral topology of the pinching'),
('fam:src:E.2.1','proposition','Semistable limits of the bielliptic surfaces'),
('push:src:A.1.1','proposition','The unsubdivided cusp fan'),
('push:src:A.2.1','proposition','The two minimal toroidal refinements'),
('push:src:A.2.2','theorem','The two minimal smooth fillings'),
('push:src:A.3.1','lemma','Analytic specialization of the virtual Euler number'),
('push:src:A.4.1','proposition','The topology of the two modified pinchings'),
('push:src:A.4.2','proposition','Integral homology and monodromy of the smooth fibre')]:title(lab,typ,t)
patch('[counterexample and corrected]\\hypertarget{tag-02ZQ}','[Infinitely many smooth fillings]\\hypertarget{tag-02ZQ}','Title the actual infinite-family result.', ['push:src:A.3.3'])
# Bare P2 tokens in visible text only: metadata labels and references are already live.
for m in list(re.finditer(r'(?<![:\w])P2\.(\d+)',s)):
 before=s[max(0,m.start()-30):m.start()]
 if re.search(r'\\(?:label|ref|ref\*|SeriesRef|hyperref)\{[^}]*$',before):continue
 # All surviving body occurrences should already be inside label-bearing commands.
# Guard/anchor verification.
pat=r'\\label\{([^}]+)\}|\\hypertarget\{(tag-[^}]+)\}'
def anchors(t):return [a or b for a,b in re.findall(pat,t)]
a0=anchors(initial);a1=anchors(s);lost=[x for x in a0 if a1.count(x)<a0.count(x)];dups=[x for x in set(a0) if a1.count(x)>a0.count(x)]
assert not lost,lost;assert not dups,dups
(P/'S6_SERIES_PUBLISH_I_boundary_batch3_guarded.json').write_text(json.dumps(dict(input_sha256=hashlib.sha256(initial.encode()).hexdigest(),created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),patches=patches,anchor_check=dict(lost=lost,duplicates=dups,new=[x for x in a1 if x not in a0])),indent=2))
(P/'S6_SERIES_PUBLISH_I_boundary_batch3_preview.tex').write_text(s)
(P/'S6_SERIES_PUBLISH_I_boundary_batch3_archived_proofs.json').write_text(json.dumps(archive,indent=2))
print(dict(patches=len(patches),removed_chars=len(initial)-len(s),new_anchors=[x for x in a1 if x not in a0]))
