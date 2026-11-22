from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re
W=Path('/workspace/scratch/653608133b22/work');O=W/'agents/i_provenance'
P=W/'S6_SERIES_PUBLISH_I.tex';T=P.read_text();H=hashlib.sha256(P.read_bytes()).hexdigest()
assert H=='7479a42f0c18cb2853e483ba3b0b222087e800a6a720ca5f2a21313ff6706cc6'
def h(t):return hashlib.sha256(t.encode()).hexdigest()
def proof_after(label):
 i=T.index('\\label{'+label+'}');a=T.index('\\begin{proof}',i);b=T.index('\\end{proof}',a)+len('\\end{proof}');return T[a:b]
proper=proof_after('fam:src:A.3.1')
sa=T.index('\\subsection{Coherent even shifts and quotient descent}')
sb=T.index('\\subsection{The effective period parameter}',sa)
coherent_section=T[sa:sb]
coherent_proof=coherent_section[coherent_section.index('\\begin{proof}'):coherent_section.index('\\end{proof}')+len('\\end{proof}')]
begin='\\begin{enumerate}[label=\\arabic*.,leftmargin=*]\n'
coherent_body=coherent_proof.split(begin,1)[1].rsplit('\\end{enumerate}',1)[0]
coherent_new=coherent_body.replace('(PS3)','\\eqref{wb:pshift:eq:finite-data}').replace('(PS4)','\\eqref{wb:pshift:eq:covariance}')
coherent_new=coherent_new.replace('the universal cover of the three-punctured base. Its fundamental group\nis free on the marked two negative peripheral generators.', 'the universal cover of the three-punctured base. The fundamental group\nof $B^\\circ$ is free on the marked two negative peripheral generators.')
old=r'''they are $(0,n/2,0,-n/4)$. Pairing with the full $\Pi_c(g_jz)$
shows that $b_j$ satisfies \eqref{wb:pshift:eq:finite-equation} for $a=1$.
Translation by $b_j$ is therefore already an isomorphism of the
two finite local fillings. The remaining issue is its exact overlap
with the fixed middle identification.'''
new=r'''they are $(0,n/2,0,-n/4)$. Since both $r_j$ and
$n\epsilon_j\widehat\delta/m_j+\ell_j$ lie in $\ker\gamma$,
the period covariance gives
\[
 b_j(g_jz)-R_{g_j}(z)b_j(z)
 =\Pi_{c+n}(g_jz)
       \left(\frac{n\epsilon_j}{m_j}\widehat\delta+\ell_j\right).
\]
This is the deck-equivariance identity for translation by $b_j$
between the finite fillings at $c$ and $c+n$. Its overlap with
the fixed middle identification is as follows.'''
assert coherent_new.count(old)==1;coherent_new=coherent_new.replace(old,new)
old=r'''The finite maps descend by
\eqref{wb:pshift:eq:finite-equation}, \eqref{wb:pshift:eq:local-matrix-identity}, and the exact covariance of $\eta_j$.'''
if old not in coherent_new:
 old=r'''The finite maps descend
by \eqref{wb:pshift:eq:finite-equation}, \eqref{wb:pshift:eq:local-matrix-identity}, and the exact covariance of $\eta_j$.'''
if old not in coherent_new:
 old=r'''The finite maps descend by \eqref{wb:pshift:eq:finite-equation}, \eqref{wb:pshift:eq:local-matrix-identity}, and the exact
covariance of $\eta_j$.'''
assert coherent_new.count(old)==1,repr(coherent_new[coherent_new.index('The finite maps'):coherent_new.index('The finite maps')+230])
new=r'''The finite maps descend by
\eqref{wb:pshift:eq:local-matrix-identity}, the finite
deck-equivariance identity above, and the exact covariance of $\eta_j$.'''
coherent_new=coherent_new.replace(old,new)
old=r'''\item The proper holomorphic family has been constructed in the proof of
\cref{fam:src:A.3.1}. The coherent $2\mathbb Z$ action is properly'''
new=r'''\item The local families constructed above are proper and holomorphic.
The coherent $2\mathbb Z$ action is properly'''
assert coherent_new.count(old)==1;coherent_new=coherent_new.replace(old,new)
new_proper=proper.replace('\\begin{proof}[Proof of the proper-family assertion; coherent descent in \\cref{I:coherent-descent-proof}]','\\begin{proof}')
assert new_proper.count('\\end{enumerate}')==1
new_proper=new_proper.replace('\\end{enumerate}',coherent_new+'\\end{enumerate}')

ca=T.index('\\subsection{The intrinsic parameter space}')
cb=T.index('\\clearpage',ca)
parameter_section=T[ca:cb]
parameter_body=parameter_section[parameter_section.index('\\hypertarget{tag-000C}'):]
parameter_new=parameter_body.replace('\\begin{proof}[Proof of Theorem~\\ref{fam:src:A.5.1}]','\\begin{proof}')
old=r'''For the standard twist data, Theorem~\ref{night:P5.6}
gives $X_c\simeq X_{c'}$ exactly when $c-c'\in2\mathbb Z$.
The explicit maps on the regular, finite, and cusp charts are
those in \cref{wb:pshift:lem:centralizer}.'''
new=r'''For the standard twist data, the classification of
\cite[Theorem~1.4, p.~3]{DuEtAl2026v1}, with the exact parameter
identification of \cref{night:P5.7}, is re-derived in
\cref{night:P5.6}. It gives $X_c\simeq X_{c'}$ exactly when
$c-c'\in2\mathbb Z$. The explicit maps on the regular, finite,
and cusp charts are those of \cref{fam:src:A.3.1}, displayed in
\eqref{wb:pshift:eq:full-isomorphism} and satisfying
\eqref{wb:pshift:eq:coherent-shift-action}.'''
assert parameter_new.count(old)==1;parameter_new=parameter_new.replace(old,new)
i=T.index('\\label{fam:src:A.5.1}');e=T.index('\\end{theorem}',i)+len('\\end{theorem}')
classification=T[T.rfind('\\begin{theorem}',0,i):e]

changes=[]
def guard(id,old,new,reason,scope):
 assert T.count(old)==1,(id,T.count(old))
 changes.append({'id':id,'old':old,'new':new,'reason':reason,'statement_scope':scope,'source_sha256':H})
guard('IP-C11-S01',proper,new_proper,'Place the complete local/cusp/coherent-shift construction and quotient descent inside the first proper-family proof; retain every original proof step and equation anchor. Replace the only forward finite-covariance dependency by its exact a=1 identity derived from the already displayed matrices.','fam:src:A.3.1')
guard('IP-C11-S02',coherent_section,'','The complete proof has moved into the first proper-family proof, eliminating the forward construction dependency and duplicate proof location. The known standard classification re-derivation remains in the credited appendix in A.2 and night:P5.6.','fam:src:A.3.1')
old=r'\subsection{The proper holomorphic family and coherent descent}\hypertarget{tag-01PC}{}\label{fam:section:A.3}'
guard('IP-C11-S03',old,old+r'\label{I:coherent-descent-proof}','Retain the former coherent-proof section anchor as an alias of the early construction section.','section anchor only')
guard('IP-C11-S04',classification,classification+'\n'+parameter_new,'Place the complete short proof of the headline classification theorem immediately after its statement, with explicit primary credit and the corrected supplying chart-map reference.','fam:src:A.5.1')
guard('IP-C11-S05',parameter_section,'','Remove the now-relocated deferred proof and its empty source section while preserving tag000C, its label and parameter-disc equation in the moved proof.','fam:src:A.5.1')
guard('IP-C11-S06','\\subsection{Integral classification of the parameter}\n\\hypertarget{tag-03CR}{}\\label{wb:pshift:sec:classification}\n\n\\subsection{The integral obstruction}\\hypertarget{tag-01PB}{}\\label{fam:section:A.2}', '\\subsection{The integral obstruction}\\hypertarget{tag-01PB}{}\\label{fam:section:A.2}\\hypertarget{tag-03CR}{}\\label{wb:pshift:sec:classification}', 'Remove the empty subsection and preserve its tag/label as aliases of the surviving integral-obstruction subsection, so both section references retain the correct numbered target.','section headings and retained aliases only')
guard('IP-C11-S07','\\item Solving the two fixed-vector systems from (PS3) gives','\\item Solving the two fixed-vector systems from \\eqref{wb:pshift:eq:finite-data} gives','Resolve the retained manual equation key to its exact current label.','fam:src:A.2.1')
guard('IP-C11-S08','The two cyclic norm matrices are, by multiplication of (PS3),','The two cyclic norm matrices are, by multiplication of \\eqref{wb:pshift:eq:finite-data},','Resolve the retained manual equation key to its exact current label.','fam:src:A.2.1')
guard('IP-C11-S09','The centralizer proof gives $c\'=c+n$ and $aI_2$ exactly as before.','The centralizer computation of \\cref{fam:src:A.2.1} and its period equation \\eqref{wb:pshift:eq:period-morphism} give $c\'=c+n$ and fibre-linear part $aI_2$.','Replace an unnumbered backward comparison with its exact supplying proposition/equation. The concrete morphism remains unchanged.','fam:src:B.2.1')
old=next(x for x in T.splitlines() if 'linear difference sheaf precisely' in x)
new=old.replace('linear difference sheaf precisely $\\mathcal V$ of \\ref{fam:src:A.3.1}','linear difference sheaf $\\mathscr V$ defined by \\eqref{wb:pshift:eq:vector-sheaf} in the proof of \\cref{fam:src:A.3.1}').replace('H^1(B,\\mathcal V)','H^1(B,\\mathscr V)')
guard('IP-C11-S10',old,new,'Identify the exact difference-sheaf sequence and use the same symbol as its supplying construction, now placed before this proof.','fam:src:B.2.1')

candidate=T
for g in changes:
 assert candidate.count(g['old'])==1,(g['id'],candidate.count(g['old']))
 candidate=candidate.replace(g['old'],g['new'])
oldlabels=re.findall(r'\\label\{([^}]+)\}',T);newlabels=re.findall(r'\\label\{([^}]+)\}',candidate)
oldtags=re.findall(r'\\hypertarget\{([^}]+)\}',T);newtags=re.findall(r'\\hypertarget\{([^}]+)\}',candidate)
assert sorted(oldlabels)==sorted(newlabels)
assert sorted(oldtags)==sorted(newtags)
assert '(PS3)' not in candidate and '(PS4)' not in candidate
proofs={'proper_family_old':proper,'coherent_old':coherent_proof,'proper_family_proposed':new_proper,'classification_old':parameter_body,'classification_proposed':parameter_new,'discrete_old':proof_after('fam:src:B.2.1')}
discrete=proofs['discrete_old']
for g in changes:
 if g['statement_scope']=='fam:src:B.2.1':discrete=discrete.replace(g['old'],g['new'])
proofs['discrete_proposed']=discrete
files={}
for key,value in proofs.items():
 p=O/f'S6_SERIES_PUBLISH_I_candidate11_structure_{key}.tex';p.write_text(value+'\n');files[key]={'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
out={'created_utc':datetime.now(timezone.utc).isoformat(),'source':str(P),'source_sha256':H,'source_writes':False,'changes':changes,'preservation':{'labels_same_multiset':True,'hypertargets_same_multiset':True,'mathematical_statements_unchanged':True,'no_new_theorem_environment':True,'coherent_proof_steps_retained':'All three former steps retained: local maps; global correction/coherence; proper quotient and inequivalence consequence.','credited_appendix_retained':'night:P5.7 source/history comparison, A.2 integral-obstruction proof, all tangent/deformation/Aut re-derivations, and night:P5.6 integral classification remain in the appendix.'},'complete_proof_archives':files,'reading_status':'Original complete printed proofs read. Proposed complete-text rereading pending before readiness notice.','math_events_added':0}
p=O/'S6_SERIES_PUBLISH_I_candidate11_structure_guards.json';p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'guards':len(changes),'path':str(p),'source_sha256':H,'proposed_proof_chars':len(new_proper),'labels_and_tags_preserved':True}))
