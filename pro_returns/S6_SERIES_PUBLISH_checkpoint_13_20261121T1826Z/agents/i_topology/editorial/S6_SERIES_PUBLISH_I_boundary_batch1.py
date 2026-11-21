from pathlib import Path
import re,json,hashlib,datetime
P=Path(__file__).resolve().parent
initial=(P/'S6_SERIES_PUBLISH_I_boundary_editorial_input.tex').read_text();s=initial;patches=[];removed=[]
def patch(id,old,new,why,ids=[]):
 global s
 assert s.count(old)==1,(id,s.count(old),old[:100])
 patches.append(dict(id=id,old=old,new=new,reason=why,statement_ids=ids));s=s.replace(old,new,1)
def block(lab,text=None):
 text=s if text is None else text;i=text.index('\\label{'+lab+'}');a=text.rfind('\\begin{',0,i);b=text.index('\\end{proof}',i)+len('\\end{proof}');return text[a:b]
def headerbody(bl):
 e=re.match(r'\\begin\{([^}]+)\}',bl).group(1);j=bl.index('\\end{'+e+'}');st=bl[:j];i=st.index('\\StatementRecord');rec_end=st.index('\n',i);head=st[:rec_end];body=st[rec_end:];return e,head,body

def steps(bl):
 st=bl.index('\\begin{enumerate}');st=bl.index('\n',st)+1;en=bl.rfind('\\end{enumerate}');return re.split(r'(?m)^\\item ',bl[st:en])[1:]
def proofs_removed(lab):removed.append({'statement_id':lab,'original_block':block(lab,initial)})
# Preserve the old independent long proof and aliases in the check evidence.
for lab in ['push:src:B.4.33','push:src:B.4.1','push:src:B.5.1','push:src:B.4.4','night:P2.11','push:src:B.2.3']:
 proofs_removed(lab)
# Merge P2.2 and P2.3 into one dependency-ordered theorem/proof.
p22=block('night:P2.2');p23=block('night:P2.3');e,h22,b22=headerbody(p22);e,h23,b23=headerbody(p23)
h23=h23.replace('\\begin{theorem}','\\begin{theorem}[Partial filling and extending origins]',1)
h22=h22.replace('\\begin{theorem}','',1)
b22=b22.replace(' The proposed $+pn\\widehat\\gamma$ has the opposite sign in the fixed conventions.','')
st23=steps(p23);st22=steps(p22)
st22[0]=st22[0].replace('in the rank-one charts of P2.3 below','in the node charts \\eqref{eq:P2chain}')
st22[1]=re.sub(r'The general-\$N\$ origin subtraction and both covered deck differences are checked coefficient by coefficient in\n\\path\{[^}]+\}, with output \\path\{[^}]+\}\. ', '',st22[1])
st22[1]=st22[1].replace(' and \\eqref{eq:P2F} is the function printed in the prompt','')
st22[1]=st22[1].replace('For every admissible twist $p\\ne0$, and the difference between the two proposed classes is $2pn\\widehat\\gamma\\ne0$ in the free quotient lattice.','For every admissible twist $p\\ne0$, so the radial class is nonzero in the free quotient lattice.')
st23[3]=st23[3].replace('P2.2 identifies the overlap','The displayed origin formulas identify the overlap')
combined=h23+'\n'+h22+'\n'+b23+b22+'\\end{theorem}\n\\begin{proof}\n\\begin{enumerate}[label=\\arabic*.,leftmargin=*]\n'+''.join('\\item '+z for z in st23[:3]+st22+[st23[3]])+'\\end{enumerate}\n\\end{proof}'
old=p22+'\n\n\\subsection{The partial parameter filling}\n'+p23
patch('I-topology-01',old,'\\subsection{The partial filling and its origins}\n'+combined,'Combine the two assertions and order local construction before the extending-origin use.', ['night:P2.2','night:P2.3'])
# One marked-base extension proof, retaining the longer explicit graph/cross-ratio argument.
p24=block('night:P2.4');b44=block('push:src:B.4.4');e,h24,b24=headerbody(p24);e,h44,b44body=headerbody(b44)
h24=h24.replace('\\begin{theorem}','\\begin{theorem}[Extension of the marked base map]',1)
h24+='\n'+h44.replace('\\begin{proposition}[extension of the marked fibration]','',1)
b24=b24.replace('A proper modification carries a holomorphic marked map to $\\Pp^1$, and hence a proper map to $\\Pp^1\\times\\Delta$.','For a smooth given total space, its graph is a proper projective modification carrying the marked map. In general, a smooth proper modification carries a holomorphic marked map to $\\Pp^1$, and hence a proper map to $\\Pp^1\\times\\Delta$.')
oldsteps=steps(b44)
first=steps(p24)[0]
# The long proof is used on the smooth resolved model from the first step.
newproof='\\begin{proof}\n\\begin{enumerate}[label=\\arabic*.,leftmargin=*]\n\\item '+first+''.join('\\item '+q for q in oldsteps)+'\\end{enumerate}\n\\end{proof}'
newproof=newproof.replace('Write $p:Z\\to\\Delta$ for the smooth result.','Write $g:\\mathcal Z\\to\\Delta_s$ for the smooth result. The following argument also applies directly to a smooth given total space.')
newproof=newproof.replace('the analytic base-change theorem checked\nin E.3','the analytic base-change theorem of Proposition~\\ref{push:src:E.3.1}')
newproof=newproof.replace('\\citep[Section 6, Hauptsatz I]{Grauert1960D}','\\citep[\\S6, Hauptsatz~I, p.~59]{Grauert1960D}')
newp24=h24+'\n'+b24+'\\end{theorem}\n'+newproof
patch('I-topology-02',p24,newp24,'Retain one canonical-pencil, explicit projective-graph and labelled-cross-ratio proof for the same marked extension.', ['night:P2.4','push:src:B.4.4'])
patch('I-topology-03',b44,'','Remove the duplicate marked-extension block after aliasing its statement label.', ['push:src:B.4.4'])
# Merge the global nonfilling repetitions, with all original semantic scope in P2.7.
p27=block('night:P2.7');h_end=p27.index('\n\\StatementRecord');extra=''
for lab in ['push:src:B.4.33','push:src:B.4.1','push:src:B.5.1']:
 oldb=block(lab);e,h,b=headerbody(oldb);h=re.sub(r'^\\begin\{[^}]+\}(?:\[[^\]]*\])?','',h);extra+='\n'+h
p27new=p27[:h_end]+extra+p27[h_end:]
p27new=p27new.replace('\\begin{theorem}','\\begin{theorem}[Nonexistence of proper fillings]',1)
for lab in ['push:src:B.4.33','push:src:B.4.1','push:src:B.5.1']:
 patch('I-topology-delete-'+lab,block(lab),'','The admissible-datum theorem includes this exact family and all finite covers; preserve its alternate proof in check evidence.',[lab])
patch('I-topology-04',p27,p27new,'Keep one theorem for nonexistence, with all four statement tags and labels.', ['night:P2.7','push:src:B.4.33','push:src:B.4.1','push:src:B.5.1'])
# Merge the identical plain-cusp corollaries.
b22=block('push:src:B.2.2');b23=block('push:src:B.2.3');e,h23,b23body=headerbody(b23)
newb22=b22.replace('\\begin{corollary}[general plain-cusp normalization]','\\begin{corollary}[Base-changed cusp refinements]',1)
pos=newb22.index('\n\\StatementRecord');newb22=newb22[:pos]+'\n'+re.sub(r'^\\begin\{corollary\}\[[^\]]*\]','',h23)+newb22[pos:]
newb22=newb22.replace('These statements concern the plain\nuntwisted cusp. They assert no compatibility with\nthe finite logarithmic-transform pieces of B.1.','Reducedness is exactly the restriction $\\ell=1$ on every positive-height ray.')
patch('I-topology-05',b22,newb22,'Combine literally identical proofs, retaining the reducedness assertion and both aliases.', ['push:src:B.2.2','push:src:B.2.3'])
patch('I-topology-06',b23,'','Remove the duplicate plain-cusp statement and proof.', ['push:src:B.2.3'])
# Merge the two virtual Euler obstruction statements; keep the unique actual Euler-zero smoothing.
a32=block('push:src:A.3.2');p211=block('night:P2.11');e,h211,b211=headerbody(p211)
a32new=a32.replace('\\begin{theorem}[Conjecture 8.2 refuted]','\\begin{theorem}[Virtual Euler obstruction to the prescribed pinching]',1)
pos=a32new.index('\n\\StatementRecord');a32new=a32new[:pos]+'\n'+h211.replace('\\begin{theorem}','',1)+a32new[pos:]
a32new=a32new.replace('For the specified pinching $Q$ one has $e_{\\mathrm{vir}}(Q)=0$.','For the pinching $Q$ of Proposition~\\ref{fam:src:E.1.1},\none has $e_{\\mathrm{vir}}(Q)=0$, whereas $e(X(u))=2$.')
a32new=a32new.replace('even if no map to $B$ is required. Thus Conjecture 8.2\nof the attached \\cite{Engel2026} is false as worded.','This disproves the central-fibre assertion in\n\\cite[Conjecture~8.2, p.~22]{Engel2026}.')
a32new=a32new.replace('$Q$, This disproves', '$Q$. This disproves')
a32new=a32new.replace('The proper nodal\nfilling of \\ref{push:src:A.1.2} and the two natural semistable fillings of\n\\ref{push:src:A.2.2} are precise replacements, with different central fibres.', 'Theorem~\\ref{push:src:A.1.2} constructs a nodal family with central fibre $Q$; Theorem~\\ref{push:src:A.2.2} constructs the two smooth total spaces with central fibres $Q^\\pm$.')
a32new=a32new.replace('The projective-bundle calculation is independently checked\nin \\texttt{ab\\_push\\_local\\_checks.py}, using\n$H(H+m)=0$, $d_0=H+m$, $d_\\infty=H$.','In the projective-bundle presentation, the same calculation uses\n$H(H+m)=0$, $d_0=H+m$, $d_\\infty=H$.')
a32new=a32new.replace('The same number follows independently from the\nsemistable nearby-cycle count in \\ref{push:src:A.4.3} below. ','')
a32new=a32new.replace('No requirement\non its leading smoothing section, and no extension of $f$,\nentered this argument.','')
a32steps=steps(a32new);last=a32steps[-1]
last=last.replace('There is also a direct check that zero is the correct smooth\nnumber. ','')
a32new=a32new[:a32new.index('\\begin{proof}')]+ '\\begin{proof}\n\\begin{enumerate}[label=\\arabic*.,leftmargin=*]\n'+''.join('\\item '+q for q in a32steps[:-1])+'\\end{enumerate}\n\\end{proof}\n\n'+r'''\begin{proposition}[An Euler-zero smoothing of the pinching]
\hypertarget{tag-PT02}{}\label{I:Euler-zero-pinching-smoothing}
\StatementRecord{I:Euler-zero-pinching-smoothing}{proved}{PT02}{}
The pinching $Q$ admits a proper flat smoothing with smooth fibres of Euler number zero, obtained by choosing the zero of its smoothing section on a smooth elliptic fibre of $S$.
\end{proposition}
\begin{proof}
'''+last+'\\end{proof}'
patch('I-topology-07',a32,a32new,'Keep one virtual Euler proof and promote the unique actual zero-Euler smoothing construction to a titled proposition.', ['push:src:A.3.2','night:P2.11','I:Euler-zero-pinching-smoothing'])
patch('I-topology-08',p211,'','Its exact central space, conclusion and proof are now consolidated with A.3.2.', ['night:P2.11'])
# Put the untwisted explicit construction after the two toroidal models, where S,L and the cusp exist.
p210=block('night:P2.10');p210new=p210.replace('\\begin{theorem}','\\begin{theorem}[A proper filling of the untwisted family]',1)
p210new=p210new.replace('supplied rational elliptic surface','rational elliptic surface of Definition~\\ref{I:def:pinching-data}')
p210new=re.sub(r'The four chart substitutions, both overlap inverse identities and the determinants of the two original cusp cones are checked exactly in\n\\path\{[^}]+\}, with all results recorded in\n\\path\{[^}]+\}\.','The displayed substitutions verify the four charts and their inverse overlaps.',p210new)
patch('I-topology-09', '\\subsection{The untwisted control}\n'+p210, '', 'Move the explicit untwisted filling after its geometric data and local toroidal models.', ['night:P2.10'])
a22=block('push:src:A.2.2');patch('I-topology-10',a22,a22+'\n\n\\subsection{An explicit two-bundle plumbing}\n'+p210new,'Place the complete alternative construction with the untwisted models.', ['night:P2.10'])
# Number the untwisted datum, preserve exact mathematical conventions.
start=s.index('In this section $S$ is the smooth minimal rational elliptic surface');end=s.index('\\begin{proposition}',start);datum=s[start:end]
newdatum='\\begin{definition}[The elliptic surface and the pinching datum]\n\\hypertarget{tag-PT01}{}\\label{I:def:pinching-data}\n\\StatementRecord{I:def:pinching-data}{proved}{PT01}{}\n'+datum.replace('In this section $S$ is','$S$ is',1).rstrip()+'\n\\end{definition}\n\n'
patch('I-topology-11',datum,newdatum,'Number the geometric datum with its exact zero/infinity normal conventions.', ['I:def:pinching-data'])
# Remove the duplicate restatement/proof E1.5, retaining the numbered comparison and every label/tag.
i=s.index('\\paragraph{Local obstruction and the precise gluing requirement}');j=s.index('\\subsection{Finite bielliptic limits',i);old=s[i:j]
new=r'''\begin{remark}[The local modification and the compact central fibre]\hypertarget{tag-01R5}{}\label{fam:src:E.1.5}\label{fam:st:E.1.5}
\StatementRecord{fam:src:E.1.5}{proved}{01R5}{}
The blow-up charts of Proposition~\ref{fam:src:E.1.3} resolve the ordinary double point of $xy=uzv$ for $u\ne0$ and change one branch of the central normalization by the stated blow-up along $(x,z)$. The compact pinching $Q$ has the virtual Euler obstruction of Theorem~\ref{push:src:A.3.2}. The periodic modifications in Theorem~\ref{push:src:A.2.2} give the two smooth total spaces with central normalizations obtained by the explicitly described blow-up and small resolution.
\end{remark}

'''
patch('I-topology-12',old,new,'Replace the duplicate synthesis and repeated proof by one numbered remark citing the exact morphisms.', ['fam:src:E.1.5'])
# Clean and title the uniform argument, without changing mathematical formulas.
a=s.index('\\section{The uniform corner obstruction}');b=s.index('\\section{The cotangent direct images',a);uniform=s[a:b]
# The moved control block and merged Euler block are gone, so this is P2.1--P2.9 only.
for num,title in [(1,'Parameter descent and cusp transport'),(5,'Vanishing of finite monodromy orbits'),(6,'Vanishing of horizontal meridians'),(8,'The logarithmic datum $(0,2,-1)$'),(9,'The obstruction for coprime multiplicities')]:
 uniform=uniform.replace('\\begin{theorem}\\hypertarget{tag-'+{1:'02R9',5:'02RF',6:'02RG',8:'02RI',9:'02RJ'}[num]+'}', '\\begin{theorem}['+title+']\\hypertarget{tag-'+{1:'02R9',5:'02RF',6:'02RG',8:'02RI',9:'02RJ'}[num]+'}',1)
uniform=uniform.replace('For the prescribed $(3,4)$ construction with integral twists $(l_0,l_1,l_2)$, put','For an admissible $(3,4)$ datum with integral twists $(l_0,l_1,l_2)$, where $3\\nmid l_1$ and $l_2$ is odd, use $w=r^6$,\n$c=-12v$, $r=e^{2\\pi iv}$ and $q=e^{2\\pi is}$, and put')
uniform=uniform.replace('the supplied period matrix','the period matrix \\eqref{wb:pshift:eq:periods}')
uniform=uniform.replace('the supplied Viaclovsky construction',"Viaclovsky's logarithmic construction")
uniform=uniform.replace('The determinant calculation in Part~5','Proposition~\\ref{fam:src:A.1.1}')
# Current source proof programs become a separate mapping manifest, while exact operations remain.
uniform=re.sub(r'The full collar coefficient and the four origin-descent identities are verified by rational polynomial cancellation in\n\\path\{[^}]+\}; the exact inputs and output are recorded in\n\\path\{[^}]+\}\.','The displayed formulas verify the collar coefficient by direct substitution.',uniform)
uniform=re.sub(r'; its exact value is also recorded by\n\\path\{[^}]+\}\.','.',uniform)
uniform=re.sub(r' The specialization \$N=12\$, \$b=5\$, \$l_0=0\$ of the universal origin identities is checked in\n\\path\{[^}]+\}\.','',uniform)
uniform=re.sub(r'Rational polynomial cancellation in\n\\path\{[^}]+\} verifies the general-\$N\$ origin subtraction, all four descent identities and both covered differences;\n\\path\{[^}]+\} records these exact calculations\.','Expanding the two quadratic expressions gives the origin subtraction, the four descent identities and both covered differences.',uniform)
# Replace every compendium-only P2.x reference in this moved block by a live statement reference.
uniform=re.sub(r'(?<![A-Za-z:])P2\.(\d+)',lambda m:'\\ref{night:P2.'+m.group(1)+'}',uniform)
patch('I-topology-13',s[a:b],'','Move the uniform proof before the subsidiary filling material; its proof no longer depends forward on the partial chain.', ['night:P2.1','night:P2.2','night:P2.3','night:P2.4','night:P2.5','night:P2.6','night:P2.7','night:P2.8','night:P2.9'])
# Move and lightly clean the outer boundary section next, before the local filling supplement.
a=s.index('\\section{The boundary of the parameter disc}');b=s.index('\\section{The cotangent direct images',a);boundary=s[a:b]
# after deletion of uniform only whitespace separates the boundary and cotangent section
boundary=boundary.replace('(Cornulier, Theorem~3.1)','\\cite[Theorem~3.1, p.~2017; proof, p.~2018]{Cornulier2011}')
boundary=boundary.replace('Cornulier, Theorem~3.1','\\cite[Theorem~3.1, p.~2017; proof, p.~2018]{Cornulier2011}')
patch('I-topology-14',s[a:b],'','Move the outer boundary theorem before the lengthy subsidiary local constructions.', [])
anchor='\\section{The limit at the puncture}\\hypertarget{tag-01PS}{}\\label{fam:section:E}'
patch('I-topology-15',anchor,uniform.rstrip()+'\n\n'+boundary.rstrip()+'\n\n'+anchor,'Order the headline puncture and outer-boundary conclusions before the untwisted and local-model supplement.', [])
# Repair descriptions of the replaced proof and its deleted internal equation.
old=r"""its affine torsor obstruction. \ref{push:src:B.4.33} derives an associated torsor
from traces in a hypothetical cap; it does not identify that cap
with a proper fan model."""
new=r"""its affine torsor obstruction. Theorem~\ref{night:P2.7} proves unrestricted
nonexistence by the horizontal-meridian vanishing and the commuting-meridian
identity \eqref{eq:P2ratio}."""
patch('I-topology-16',old,new,'Update the proof mechanism to the retained uniform argument.')
old=r"""proves the conclusion of \ref{push:src:B.4.33}, whose argument instead uses
extending-section differences and the global affine loop invariant."""
new=r"""is used in Theorem~\ref{night:P2.7}, whose contradiction is the equality
of the zero horizontal-meridian ratio and the nonzero cusp ratio."""
patch('I-topology-17',old,new,'Retain the actual scope discussion with the current proof mechanism.')
start=s.index('The final step uses two separate facts: a\ncap-derived origin')
end=s.index('\\section{The cotangent direct images',start)
patch('I-topology-18',s[start:end],'','Remove the duplicated closing summary of the archived independent proof.')
old='\\subsection{No proper analytic filling of the actual punctured family}\n'
patch('I-topology-19',old,'','Remove the empty heading after consolidation of the global theorem.')
# A range ending in the moved alias would print backwards. Spell out its members.
for pre in [30,31]:
 old='\\ref{push:src:B.4.'+str(pre)+'}--\\ref{push:src:B.4.33}'
 new='\\cref{'+','.join('push:src:B.4.'+str(n) for n in range(pre,33))+',night:P2.7}'
 count=s.count(old)
 for n in range(count):
  pos=s.index(old);lo=s.rfind('\n',0,pos)+1;hi=s.find('\n',pos)
  line=s[lo:hi];patch('I-topology-range-'+str(pre)+'-'+str(n),line,line.replace(old,new),'Preserve the complete reference list after moving the global theorem.')
# Exact label and tag preservation.
pat=r'\\label\{([^}]+)\}|\\hypertarget\{(tag-[^}]+)\}'
def anchors(t):return sorted(a or b for a,b in re.findall(pat,t))
oldset=anchors(initial);newset=anchors(s);lost=[v for v in oldset if v not in newset];dups=[v for v in set(newset) if newset.count(v)>oldset.count(v) and v in oldset]
assert not lost, lost;assert not dups,dups
(P/'S6_SERIES_PUBLISH_I_boundary_batch1_guarded.json').write_text(json.dumps({'input_sha256':hashlib.sha256(initial.encode()).hexdigest(),'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'patches':patches,'anchor_check':{'lost':lost,'new_duplicates':dups,'added':[v for v in newset if v not in oldset]}},indent=2))
(P/'S6_SERIES_PUBLISH_I_boundary_batch1_preview.tex').write_text(s)
(P/'S6_SERIES_PUBLISH_I_consolidated_independent_proofs.json').write_text(json.dumps(removed,indent=2))
print(json.dumps({'patch_count':len(patches),'input_chars':len(initial),'preview_chars':len(s),'removed_chars':len(initial)-len(s),'added_anchors':[v for v in newset if v not in oldset]},indent=2))
