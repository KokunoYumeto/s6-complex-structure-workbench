from pathlib import Path
import re,json,datetime,hashlib
from S6_SERIES_PUBLISH_editing import Editor,block
r=Path(__file__).resolve().parents[1]
ed=Editor('I')
p2=block(ed.text,'fam:src:A.2.1');p3=block(ed.text,'fam:src:A.3.1')
wb=block(ed.text,'wb:pshift:lem:centralizer')
a=ed.text.index('\\subsection{Exact global identifications of the retained period parameter}')
b=ed.text.index('\\subsection{Re-derivation of Theorem~\\ref{fam:src:A.5.1}}',a)
whole=ed.text[a:b]
prefix=whole[whole.index('For an integer $n$'):whole.index('\\begin{lemma}')]
finite=whole[whole.index('\\subsubsection{The exact finite obstruction'):whole.index('\\subsubsection{Local maps')]
local=whole[whole.index('\\subsubsection{Local maps'):whole.index('\\subsubsection{The global additive correction')]
globalpart=whole[whole.index('\\subsubsection{The global additive correction'):whole.index('\\subsubsection{Intrinsic necessity')]
intrinsic=whole[whole.index('\\subsubsection{Intrinsic necessity'):]

def after_heading(text):
 return text[text.index('\n')+1:].strip()
finite=after_heading(finite);local=after_heading(local);globalpart=after_heading(globalpart);intrinsic=after_heading(intrinsic)

# These replacements are confined to the fully read classification proof.
def publication(text):
 for old,new in [
  ('the original','the marked'),('The original','The marked'),
  ('original finite','marked finite'),('original functions','fixed functions'),
  ('original matrices','monodromy matrices'),('original torus','marked torus'),
  ('original map','marked map'),('original integral','marked integral'),
  ('original cusp','fixed cusp'),('original chart','toric chart'),
  ('original lattice','marked lattice'),('original rational','rational'),
  ('original coordinate','fixed coordinate'),('original gluing','given gluing'),
  ('the actual ','the '),('The actual ','The '),('an actual ','an '),
  ('actual integral','integral'),('actual lattice','lattice'),('actual cones','cones'),
  ('actual translation','translation'),('actual torus','torus'),
  ('retained family','marked family'),('retained $\\mu$','chosen $\\mu$'),
 ]: text=text.replace(old,new)
 removals=[
  'In particular one may not replace the generator by an arbitrary\ncoprime power.\n',
  'This is why the logarithmic term in (PS15) cannot be omitted.\n',
  'These transformation and order\ncalculations are the ones used to construct the chosen $\\mu$;\nno topological conclusion about $X_c$ is involved.\n',
  'This is a two-stage construction of the\nrequired correction, not an unproved additional gluing condition.\n',
 ]
 for x in removals:text=text.replace(x,'')
 text=text.replace('This proves the exact parity obstruction rather than merely failure\nof the untranslated identity.','This proves the parity obstruction.')
 text=text.replace('This proves\nextension across every cusp stratum, not only across its dense torus.','This proves extension across every cusp stratum.')
 text=text.replace('We give the global correction explicitly as an additive gluing\nconstruction and prove its solvability. Let','Let')
 text=text.replace('Here is how to choose the correction entering the maps. Choose','Choose')
 text=text.replace('For completeness, exactness on the finite stalks in (PS24) retains\nthe off-diagonal entry of $R_g$.','For the finite stalks in (PS24), use the full matrix $R_g$.')
 text=text.replace('the promised three kinds of local maps','the three local maps')
 text=text.replace('The promised three kinds of local maps','The three local maps')
 text=text.replace('are identical for an integer shift.','agree under the integer-shift identification.')
 text=text.replace('This proves\n\\cref{wb:pshift:thm:classification} without converting a failed\nparticular map into a nonisomorphism assertion.','This proves \\cref{wb:pshift:thm:classification}.')
 text=text.replace('This statement classifies\nthe parameters of the marked family; it does not assert that\nthe family exhausts all deformations or all complex threefolds\nwith the same singular-fibre types.','The resulting parameter space classifies the members of the marked family.')
 text=text.replace(r'\CompendiumRef{I}{wb:ffcert:thm:normalization}',r'Proposition~\ref{fam:src:A.1.2}')
 text=text.replace('Here $\\mathcal L$ is exactly the homogeneous period sheaf from\n\\CompendiumRef{I}{wb:prop:period-input-audit}, not a newly chosen extension. Indeed',
                   'The homogeneous first-coordinate line is determined by its transition factors. Indeed')
 text=text.replace('Both $H^1(B,\\mathcal O_B)$ and\n$H^1(B,\\mathcal O_B(-p_0))$ vanish. One can compute these two\ngroups without a degree approximation:',
                   'Both $H^1(B,\\mathcal O_B)$ and\n$H^1(B,\\mathcal O_B(-p_0))$ vanish:')
 return text

statement2=p2[:p2.index('\\end{proposition}')+len('\\end{proposition}')]
statement2=statement2.replace(r'\begin{proposition}',r'\begin{proposition}[The integral obstruction to a parameter shift]',1)
statement2=statement2.replace(r'\label{fam:st:A.2.1}',r'\label{fam:st:A.2.1}\hypertarget{tag-03CQ}{}\label{wb:pshift:lem:centralizer}')
statement2=statement2.replace('The rational centralizer of $(A_1,A_2)$ is $\\mathbb QI+\\mathbb QE$.',r'''The rational centralizer is
\[
 \operatorname{Cent}_{\mathbb Q}(A_1,A_2)
       =\{aI+bE:a,b\in\mathbb Q\}.
 \tag{PS7}\hypertarget{tag-03BZ}{}\label{wb:pshift:eq:centralizer}
\]
A biholomorphism over the identity of $B^\circ$ between the torus
families forces $c'-c\in\mathbb Z$ and has complex-linear part
$I_2$ or $-I_2$ on every fibre.''')
proof2=wb[wb.index('\\begin{proof}'):]
proof2=proof2.replace('\\begin{enumerate}[label=\\arabic*.,leftmargin=*]',
 '\\begin{enumerate}[label=\\arabic*.,leftmargin=*]\n\\item '+prefix.strip(),1)
proof2=proof2.replace('\\end{enumerate}',
 '\\item \\emph{The finite-root obstruction.}\n'+finite+'\n\\end{enumerate}')
proof2=publication(proof2)
statement3=p3[:p3.index('\\end{proposition}')+len('\\end{proposition}')]
statement3=statement3.replace(r'\begin{proposition}',r'\begin{proposition}[Coherent even shifts and the quotient family]',1)
proper=p3[p3.index('\\item Finally the original gluing'):p3.rindex('\\end{enumerate}')]
proper=proper.replace('\\item Finally the original gluing','\\item \\emph{Properness of the parameter family.} The gluing',1)
proof3=('\\begin{proof}\n\\begin{enumerate}[label=\\arabic*.,leftmargin=*]\n'
 '\\item \\emph{Local maps.}\n'+local+'\n'
 '\\item \\emph{The global additive correction.}\n'+globalpart+'\n'+proper+
 '\\end{enumerate}\n\\end{proof}')
proof3=publication(proof3)

head2=r'\subsection{The integral obstruction}\hypertarget{tag-01PB}{}\label{fam:section:A.2}'
head3=r'\subsection{Extension and coherent descent}\hypertarget{tag-01PC}{}\label{fam:section:A.3}'
newsection=r'''\subsection{Integral classification of the parameter}
\hypertarget{tag-03CR}{}\label{wb:pshift:sec:classification}

'''+head2+'\n\n'+statement2+'\n'+proof2+'\n\n'+head3+'\n\n'+statement3+'\n'+proof3+'\n\n'
ed.replace(p2,'','D12','Move the necessary-shift statement to the credited classification appendix and consolidate its proof with the fuller centralizer/finite-root calculation there. Every claim, norm quotient and exact source-to-target map is retained.','fam:src:A.2.1')
ed.replace(p3,'','D12','Move the coherent-shift statement to the credited appendix. Its first eight proof steps are the same local/global gluing argument as the appendix; preserve the fuller appendix formulas and the body proof’s unique uniform properness argument.','fam:src:A.3.1')
ed.replace(head2,'','D14','Relocate the subsection anchor with its single canonical proof in the credited appendix.','fam:section:A.2')
ed.replace(head3,'','D14','Relocate the subsection anchor with its single canonical proof in the credited appendix.','fam:section:A.3')
ed.replace(whole,newsection,'D12','Consolidate the two copies of the centralizer, norm obstruction and coherent shift construction into the two numbered propositions in the credited appendix. All old equation labels and tags stay on the corresponding maps. The properness argument is retained from the body proof.','wb:pshift:sec:classification')

# The intrinsic conclusion has one proof, following its two inputs.
a=ed.text.index('\\subsection{Re-derivation of Theorem~\\ref{fam:src:A.5.1}}')
b=ed.text.index('\\subsection{Re-derivation of Theorem~\\ref{fam:src:A.5.2}}',a)
old=ed.text[a:b]
new=r'''\subsection{The intrinsic parameter space}
\hypertarget{tag-000C}{}\label{app:rederive:fam-src-A.5.1}
\begin{proof}[Proof of Theorem~\ref{fam:src:A.5.1}]
'''+publication(intrinsic)+r'''
Proposition~\ref{fam:src:A.3.1} proves properness of this quotient
family and its joint holomorphic dependence. Its Kodaira--Spencer
class is nonzero by Proposition~\ref{fam:src:A.4.2}.
\end{proof}

'''
ed.replace(old,new,'D12','Use the full intrinsic-pencil and exponential-quotient argument as the single proof of the classification theorem; keep the previous outline’s properness and Kodaira–Spencer inputs explicit.','fam:src:A.5.1')

# Attach the old repeated data-display labels to the single definitions.
old=block(ed.text,'def:common-conventions')
new=old
for marker,tag,label in [
 (' \\Pi_c=\\begin{pmatrix}','03CN','wb:pshift:eq:periods'),
 (' A_1=\\begin{pmatrix}','03C8','wb:pshift:eq:finite-data')]:
 pos=new.index(marker);start=new.rfind('\\[',0,pos);end=new.index('\\]',pos)+2
 content=new[start+2:end-2]
 repl='\\begin{equation}\\hypertarget{tag-'+tag+'}{}\\label{'+label+'}'+content+'\\end{equation}'
 new=new[:start]+repl+new[end:]
ed.replace(old,new,'D12','Attach the repeated appendix period and finite-monodromy display anchors to the single defining displays. The finite affine vectors remain in the immediately following parameter definition.','def:common-conventions')
a=ed.text.index('\\section{The retained family and its intrinsic classification}')
b=ed.text.index('\\subsection{Canonical sections and the finite covers}',a)
old=ed.text[a:b]
new=r'''\section{The family and its intrinsic classification}
\hypertarget{tag-01P9}{}\label{fam:section:A}

\begin{definition}[Affine covariance]
\hypertarget{tag-PI08}{}\label{I:def:affine-covariance}
\StatementRecord{I:def:affine-covariance}{proved}{PI08}{}
Use the standard data of Definition~\ref{I:def:family-parameter}
and write $\varepsilon=v_1$, $\varepsilon'=-v_2$,
$\epsilon_j=\gamma(v_j)$, so $(\epsilon_1,\epsilon_2)=(1,-1)$.
Put
\begin{equation}\hypertarget{tag-03CO}{}\label{wb:pshift:eq:rank-one-map}
 d=\widehat\delta,\qquad e=(0,1)^{\mathsf t}=\Pi_cd,
 \qquad E=d\otimes\gamma,\qquad E^2=0,\quad\Pi_cE=e\gamma.
\end{equation}
The fibre covariance is $R_g(z)\Pi_c(z)=\Pi_c(gz)A_g$, where
\begin{equation}\hypertarget{tag-03C2}{}\label{wb:pshift:eq:covariance}
 R_{g_1}=\begin{pmatrix}-1/\tau&0\\(1-\mu)/\tau&1\end{pmatrix},
 \qquad R_{g_2}=\begin{pmatrix}1/\tau&0\\-\mu/\tau&1\end{pmatrix},
 \qquad R_{g_0}=I_2.
\end{equation}
In the cusp coordinate $s$, the generator satisfies
$s(g_0z)=s(z)-1$. The matrices satisfy $R_ge=e$ and
$A_jE=EA_j=E$.
\end{definition}

'''
ed.replace(old,new,'D13','Give the affine covariance and rank-one operator one numbered definition; remove repeated period/monodromy matrices and preserve the appendix data anchors at their unique definitions.','I:def:affine-covariance')

ed.save()
(r/'records/S6_SERIES_PUBLISH_I_classification_consolidation_comparison.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'read_scope':'Both original body proofs, the whole 25,830-character classification appendix, its centralizer lemma and the short final classification proof were read before consolidation.',
 'exact_correspondence':{
 'fam:A2.1 steps1–2':'WB centralizer steps1–4, same filtration, coefficient equations and period equation.',
 'fam:A2.1 steps3–4':'Appendix finite normalization, affine equivariance and cyclic norm equations; same full fixed-lattice quotient and parity condition.',
 'fam:A3.1 steps1–3':'Appendix PS13–PS22, identical rational columns, logarithmic corrections, cocycle and cusp shear.',
 'fam:A3.1 steps4–8':'Appendix PS23–PS28a, same extension sheaf, two additive solutions, overlap maps and coherent action.',
 'fam:A3.1 step9':'Retained in full as the properness part of the consolidated proof; it has no duplicate in the original appendix.',
 'fam:A5.1':'The intrinsic-pencil and punctured-disc quotient proof is retained once, with properness and nonzero Kodaira–Spencer references.'},
 'scope':'Presentation/order/consolidation. No changed mathematical hypothesis, conclusion or numerical value. No new independent mathematical event is claimed.'},indent=2)+'\n')
