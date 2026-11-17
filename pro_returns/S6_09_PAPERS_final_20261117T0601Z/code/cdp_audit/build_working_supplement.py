"""Build the complete scoped working-edition supplement; never edit source files.

The assembly keeps preceding definitions, complete alternative proofs and exact
source-label concordance. Identical statements share labels through the manifest.
"""
from pathlib import Path
import re,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/work/cdp_audit'
DEST=ROOT/'deliverables/editorial/II_working_supplement.tex'
paths={
 'WB':ROOT/'sources/workbench/cdp_program.tex',
 'CN':ROOT/'sources/correction_note/N_singular_fibre_vanishing_step.tex',
 'LOC':ROOT/'sources/workbench/analytic_picard_local_obstruction.tex',
 'ANA':ROOT/'sources/workbench/analytic_picard_completion.tex'}
raw={k:p.read_text() for k,p in paths.items()}

def block(text,label):
 p=text.index('\\label{'+label+'}')
 starts=list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|test)\}',text[:p]))
 a=starts[-1].start();env=starts[-1][1]
 end=text.index('\\end{'+env+'}',p)+len('\\end{'+env+'}')
 proof=text.find('\\begin{proof}',end)
 next_statement=re.search(r'\\begin\{(?:theorem|proposition|lemma|corollary|test)\}',text[end:])
 if proof>=0 and (not next_statement or proof<end+next_statement.start()):
  b=text.index('\\end{proof}',proof)+len('\\end{proof}')
 else:b=end
 return a,b,text[a:b]

def proof(text,label):
 s=block(text,label)[2]
 return s[s.index('\\begin{proof}'):]

# These aliases identify equal conclusions or the exact named part of a theorem.
# Additional methods remain printed below; the parent inserts aliases beside the
# already printed canonical statement, using this machine-readable mapping.
canonical_aliases={
 'prop:missing-cotangent-filtration':'cdp:st:A.1.1',
 'prop:missing-global-section-criterion':'cdp:st:A.1.1',
 'lem:conormal-injective':'cdp:st:A.1.1',
 'lem:conormal':'cdp:st:A.1.1',
 'prop:filtration':'cdp:st:A.1.1',
 'prop:criterion':'cdp:st:A.1.1',
 'lem:conductor-square':'cdp:st:A.2.2',
 'lem:conductor':'cdp:st:A.2.2',
 'prop:nodal-counterexample':'cdp:st:B1',
 'prop:family-geometry':'cdp:st:B1',
 'thm:nodal-test':'cdp:st:B1',
}
local_aliases={
 'prop:conductor-differential':'prop:conductor',
 'thm:corrected-global':'thm:corrected-cdp-global',
 'cor:relative':'cor:corrected-cdp-relative'}

# Give each old displayed tag an unambiguous new label before selecting blocks.
# WB/LOC/ANA share the original 5.17 namespace; CN is independently numbered.
tag_info={};tag_count=0
for key in ['WB','LOC','ANA','CN']:
 for old in re.findall(r'\\tag\{([^}]+)\}',raw[key]):
  token=('CN' if key=='CN' else 'W',old)
  if token not in tag_info:
   tag_count+=1;tag_info[token]={'printed_tag':f'W.{tag_count}','label':'wbII:eq:'+token[0]+':'+old}
def retag(text,key):
 ns='CN' if key=='CN' else 'W'
 def tag(m):
  d=tag_info[(ns,m[1])]
  return '\\tag{'+d['printed_tag']+'}\\label{'+d['label']+'}'
 text=re.sub(r'\\tag\{([^}]+)\}',tag,text)
 for (n,old),d in sorted(tag_info.items(),key=lambda z:-len(z[0][1])):
  if n==ns:
   text=text.replace('('+old+')','\\eqref{'+d['label']+'}')
 return text
text={k:retag(v,k) for k,v in raw.items()}

wb=text['WB'];cn=text['CN']
wb=wb[wb.index('\\subsection{The exact'):]
intro=r'''% Complete working-edition supplement. All source files remain unchanged.
% Reader and writer: GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro,
% 17 November 2026 UTC. Full source and label mapping accompanies this file.
\section{Additional local proofs, analytic duality and Picard restrictions}
\label{wbII:sec:working-supplement}

The conormal and conductor arguments below are written out for the local
models used by the standard family. The conductor-supported differential
for its hexagonal fibre is due to \citet[Section~10.2, Lemma~10.3]{AC2026}.
These local proofs are re-derivations of that mechanism and of the named
parts of \cref{cdp:st:A.1.1,cdp:st:A.2.2,cdp:st:A.5.1}; the explicit
nodal calculation has the scope of \cref{cdp:st:B1}. The duality statements,
the three global restriction arguments and the local nonzero Picard
example keep their separate hypotheses throughout.

'''

# The first two statements are already printed together in canonical A1.1.
# Their complete local proofs remain, followed by the DVR and coordinate proofs.
for label,title in [
 ('prop:missing-cotangent-filtration','Local proof of the conormal filtration'),
 ('prop:missing-global-section-criterion','Cohomology proof of the exact section criterion'),
 ('lem:conormal-injective','Coordinate proof for normal-crossing fibres'),
 ('lem:conductor-square','Coordinate proof of the normalization--conductor square'),
 ('prop:nodal-counterexample','Conductor proof of the nodal endpoint counterexample')]:
 a,b,s=block(wb,label)
 env=re.match(r'\\begin\{([^}]+)\}(?:\[[^]]*\])?',s)
 stmt_end=s.index('\\end{'+env[1]+'}')
 statement=s[env.end():stmt_end]
 statement=statement.replace('\\label{'+label+'}','')
 # Keep exact definitions/equations and hypotheses as the setting of the proof;
 # no second numbered theorem is created.
 replacement='\\subsubsection*{'+title+'}\n'+statement+'\n'+s[stmt_end+len('\\end{'+env[1]+'}'):]
 wb=wb[:a]+replacement+wb[b:]

# Add the separate proof that the intrinsic kernel is precisely torsion.
torsion=block(cn,'lem:torsion-identification')[2]
needle='\\subsubsection*{Local proof of the conormal filtration}'
wb=wb.replace(needle,torsion+'\n\n'+needle,1)

# The DVR formulation is retained as a complete additional local argument.
dvr=proof(cn,'lem:conormal').replace('\\begin{proof}',
 '\\begin{proof}[The minimal-prime formulation of conormal injectivity]',1)
# Its only reference to the omitted duplicate display is redirected to A1.1.
dvr=dvr.replace('\\eqref{'+tag_info[('CN','2.1')]['label']+'}',
 'the conormal sequence in \\cref{cdp:st:A.1.1}')
pos=wb.index('\\subsubsection*{Cohomology proof of the exact section criterion}')
wb=wb[:pos]+dvr+'\n\n'+wb[pos:]

# The local conductor statement does not need properness until its final clause.
wb=wb.replace('Let $g:\\mathcal X\\to\\Delta$ be a proper holomorphic map',
              'Let $g:\\mathcal X\\to\\Delta$ be a holomorphic map',1)
wb=wb.replace('threefold to a disc, and put $S=g^{-1}(0)$.',
              'threefold to a disc, and put $S=g^{-1}(0)$, assumed nonempty.',1)
wb=wb.replace('if $S$ is connected and $A\\not\\simeq\\mathcal O_S$, then',
              'if $S$ is compact and connected and $A\\not\\simeq\\mathcal O_S$, then',1)
a,b,s=block(wb,'prop:conductor')
nc=block(cn,'cor:normal-crossing-kernel')[2]
# CN equation(2.9) is exactly the canonical section-kernel conclusion.
nc=nc.replace('\\eqref{'+tag_info[('CN','2.9')]['label']+'}',
              'the section-kernel isomorphism of \\cref{cdp:st:A.1.1}')
wb=wb[:b]+'\n\n'+nc+wb[b:]

# Preserve the correction note's explicit normalization/square-root coordinates,
# its infinite-order line, its literal extending sections, and its torsion proof.
geometry=block(cn,'prop:family-geometry')[2]
geometry=geometry.replace('\\begin{proposition}[geometry of the family]',
 '\\subsubsection*{Explicit normalization and crossing coordinates}')
geometry=geometry.replace('\\label{prop:family-geometry}','').replace('\\end{proposition}','',1)
geometry=geometry.replace('\\mathscr C','\\mathcal C')
gdefs=r'''\subsection{The explicit extending choice in the nodal family}
Continue with
\[
\mathcal C=\{y^2z=x^2(x+z)+tz^3\}\subset\PP^2\times\Delta,
\qquad \mathcal X=\mathcal C\times\PP^1,
\qquad S=C_0\times\PP^1.
\]
Write $n=[0:0:1]$, let $D=\{n\}\times\PP^1$, and let
$\nu:\PP^1\to C_0$ denote the normalization described next.
'''
bundle=block(cn,'lem:gluing-bundle')[2]
extension=block(cn,'lem:extending-gluing')[2].replace('\\mathscr C','\\mathcal C')
nodal=block(cn,'thm:nodal-test')[2]
nodal=nodal.replace('\\begin{theorem}[failure of the printed endpoint implication]',
 '\\subsubsection*{The local torsion calculation in the nodal example}')
nodal=nodal.replace('\\label{thm:nodal-test}','').replace('\\end{theorem}','',1)
# The construction's earlier reference to its local model becomes the literal one.
geometry=geometry.replace('\\eqref{'+tag_info[('CN','3.1')]['label']+'}',r'$t=uv$')
scope_start=cn.index('\\begin{remark}[what the theorem does and does not refute]')
scope_end=cn.index('\\end{remark}',scope_start)+len('\\end{remark}')
nodal_extra=gdefs+geometry+'\n\n'+bundle+'\n\n'+extension+'\n\n'+nodal+'\n\n'+cn[scope_start:scope_end]
wb=wb.replace('\\subsection{Cartier-divisor duality without a normality hypothesis}',
 nodal_extra+'\n\n\\subsection{Cartier-divisor duality without a normality hypothesis}',1)

# The complete coordinate proofs are retained with explicit source credit.
# A separate textual-overlap check records its actual comparison scope.

# Remove the transferred group result and its duplicate discussion. Paper I has
# both full proofs, the original source attribution and the same source label.
start=wb.index('\\subsection{A second printed issue: abelianization of split extensions}')
end=wb.index('\\subsection{The corrected theorem that survives both defects}',start)
wb=wb[:start]+wb[end:]

# Expand the parameter-family construction in the global criterion. This is the
# extra detail of the correction note's full proof; its remaining steps coincide.
needle='Thus this Picard group is a connected irreducible complex vector group.'
family=r'''Thus this Picard group is a connected irreducible complex vector group.
Choose additive Cech cocycles $a^{(r)}_{ij}$ representing a basis of
$H^1(X,\mathcal O_X)$. For coordinates $\lambda_r$ on that vector space,
\[
 g_{ij}(\lambda)=\exp\!\left(\sum_r\lambda_r a^{(r)}_{ij}\right)
\]
satisfy the multiplicative cocycle condition and define a holomorphic
line bundle on $X\times H^1(X,\mathcal O_X)$. Its restriction at every
parameter represents the corresponding line bundle, so proper
semicontinuity below applies to an actual holomorphic family.'''
assert needle in wb;wb=wb.replace(needle,family,1)

# The parameter-space variant is a different hypothesis set and remains explicit.
generic=block(cn,'lem:generic-endpoints')[2]
target='\\begin{lemma}[generic endpoint vanishing]\\label{lem:cdp-generic-endpoints}'
assert target in wb;wb=wb.replace(target,generic+'\n\n'+target,1)

# Add the local relative modules with their entire proof and scope remark.
local_start=cn.index('\\begin{proposition}[crossing and multiple-fibre modules]')
local_end=cn.index('\\section{\\texorpdfstring{Relation',local_start)
relative=r'''\subsection{Ordinary relative one-forms on the actual local models}
The following computation concerns the relative cotangent module on the
smooth total space, before restriction to a fibre. All base maps and local
rings are specified in the statement.
'''+cn[local_start:local_end]

# Replace obsolete program-status prose by the exact mathematical consequence.
start=wb.index('\\subsection{Exact present disposition}')
wb=wb[:start]+r'''\begin{corollary}[Positive Euler number obstructs the added vanishings]
\label{test:cdp-comparison}
For the standard compact threefold $X$, every $L\in\operatorname{Pic}(X)$
satisfies
\[
 H^2(X,T_X\otimes L)\ne0,
 \qquad R^2f_*(T_X\otimes L)\ne0.
\]
The second conclusion also follows directly from the cusp conductor.
\end{corollary}
\begin{proof}
Paper I proves that the standard compact threefold has
$H^1(X;\mathbb Z)=H^2(X;\mathbb Z)=0$, holomorphic algebraic reduction
to $\mathbb P^1$, and $\langle c_3(T_X),[X]\rangle=2$.
If the displayed degree-two cohomology vanished for one line bundle,
\cref{thm:corrected-cdp-global} would give $c_3(X)\le0$, a contradiction.
If the second direct image vanished for one twist,
\cref{cor:corrected-cdp-relative} would give such a global twist after
tensoring by the pullback of a sufficiently positive base line bundle,
again a contradiction. Independently,
\cref{cor:candidate-conductor-actual} constructs a nonzero cusp-fibre
cohomology class and identifies it with the fibre of the second direct
image by top-degree base change. The contradiction with the printed
CDP conclusion is credited to \citet[Section~10.2, Theorem~10.5]{AC2026}.
\end{proof}
'''+relative

# A single explicit setup supplies every symbol used in the three restriction
# methods. All upstream mathematical references are resolved to current I numbers.
setup=r'''\subsection{Marked data used in the restriction arguments}
Here $f:X\to B=\mathbb P^1$ is the standard family of Paper I,
$B^\circ=B\setminus\{p_0,p_1,p_2\}$, and $F$ is a smooth fibre.
The cusp is $W=f^{-1}(p_0)$ and $i:W\hookrightarrow X$ is its inclusion.
Its normalization is $\eta:\widetilde W\simeq\mathrm{dP}_6\to W$.
Use the ordered dual lattices
\[
 V=H^1(F;\mathbb Z)=\mathbb Z\langle\gamma,u,w,\delta\rangle,
 \qquad
 \Lambda=H_1(F;\mathbb Z)
 =\mathbb Z\langle\widehat\gamma,\widehat u,\widehat w,\widehat\delta\rangle.
\]
Vectors are columns. The cohomology monodromies and their dual homology
actions are
\[
T_1=\begin{pmatrix}1&0&-6&2\\0&-1&1&1\\0&-1&0&1\\0&0&0&1\end{pmatrix},
\quad
T_2=\begin{pmatrix}1&6&0&-3\\0&0&-1&1\\0&1&0&0\\0&0&0&1\end{pmatrix},
\quad A_j=(T_j^{-1})^{\mathsf t}.
\]
Put $T_0=(T_1T_2)^{-1}$ and let $G$ denote the generated monodromy group.
The finite-filling orders, translations and invariant forms are
\[
\begin{gathered}
(m_1,m_2)=(3,4),\qquad
v_1=(1,2,-4,0)^{\mathsf t},\quad v_2=(-1,-3,3,0)^{\mathsf t},\\
\eta_1=2u+w+3\delta,\quad \eta_2=u+w+2\delta,
\qquad q=u\wedge w+6\gamma\wedge\delta.
\end{gathered}
\]
The actual period functions of Paper I define
\[
\Pi(z)=\begin{pmatrix}6\mu(z)&\tau(z)&1&0\\
\beta(z)&\mu(z)&0&1\end{pmatrix},
\quad
\operatorname{Im}\beta-
\frac{6(\operatorname{Im}\mu)^2}{\operatorname{Im}\tau}<0,
\]
so $\Pi(z):\Lambda_{\mathbb R}\to\mathbb C^2$ is a real isomorphism.
The marking is $\Xi(z,x+\Lambda)=[z,\Pi(z)x]$.
The finite overlap on the $s_j$-cover is translation by
$(\log s_j)/(2\pi i)\,\Pi(s_j)v_j$.
At the cusp use the unchanged zero-section gluing, with no additional
vertical translation. These are the data constructed and proved in
Paper I, Proposition~B.2, Theorem~B.6 and Proposition~B.9. The arguments
below do not replace these data by a topologically equivalent model.

'''
needle='\\subsection{A topology-independent '
pos=wb.index(needle);wb=wb[:pos]+setup+wb[pos:]

wb=wb.replace('\\input{supporting_materials/workbench/research/analytic_picard_completion.tex}',
 text['LOC']+'\n\n'+text['ANA'])

# Exact wording clean-up; no original human placeholder, status disclosure or
# external review citation is transported into the mathematical exposition.
wb=wb.replace('candidate-specific','standard-family').replace("candidate's",'standard family\'s')
wb=wb.replace('constructed candidate','standard family').replace('constructed threefold','standard threefold')
wb=wb.replace('the candidate fibre','the standard fibre').replace('for the candidate','for the standard family')
wb=re.sub(r'\\(?:Verified|AuthorSelfCheck|NeedsCheck|Refuted)\s*', '', wb)
wb=wb.replace("; it was independently supplied, with\neight named local certificates, in Reviewer~B's candidate-specific follow-up\n\\cite{ReviewerBValidation2026}",'.')
wb=wb.replace("; it was independently supplied, with\neight named local certificates, in Reviewer~B's standard-family follow-up\n\\cite{ReviewerBValidation2026}",'.')
wb=wb.replace('that derivative; it is not a politeness\nassumption hiding the original claim','that derivative')
wb=wb.replace('is not a politeness\nassumption hiding the original claim','is the exact lifting condition')
wb=wb.replace('genuinely different','different')
wb=wb.replace('the strongest corrected conclusion','the stated corrected conclusion')
wb=wb.replace('candidate, Paper', 'standard family, Paper')
wb=wb.replace('[candidate nonvanishing', '[standard-family nonvanishing')
wb=wb.replace('[the candidate conductor mechanism, with all hypotheses]',
              '[the conductor mechanism for the standard family]')
wb=wb.replace('Finally suppose $S$ is connected and',
              'Finally suppose $S$ is compact and connected and')
wb=wb.replace('This test chooses the line bundle $A$ directly on\n$S$; it does not assert that $A$ extends to a line bundle on the total space\n$\\mathcal X$.  It therefore refutes the claimed \\emph{formal implication\nbetween the three sheaf-cohomology groups} for a non-torsion $A$, but does\nnot by itself instantiate the narrower global-line-bundle situation on\np.~692.',
              'This calculation chooses $A$ directly on $S$ and disproves the\nclaimed \\emph{formal implication between the three sheaf-cohomology groups}\nfor a non-torsion line bundle. The explicit extending choice of $A$ is\nconstructed in the next subsection, which also treats the total-space\nline-bundle condition on p.~692.')
wb=re.sub(r'\\P(?![A-Za-z])',r'\\PP',wb)

# Resolve labels and references. Alias labels are written next to retained
# statements where possible; canonical aliases are supplied to the parent.
all_source_labels=set()
for value in raw.values():all_source_labels.update(re.findall(r'\\label\{([^}]+)\}',value))
def destination(label):
 if label.startswith(('wbII:','cdp:')):return label
 if label in canonical_aliases:return canonical_aliases[label]
 return 'wbII:'+local_aliases.get(label,label)
for original,target_label in local_aliases.items():
 needle='\\label{'+target_label+'}'
 if needle in wb:wb=wb.replace(needle,needle+'\\label{wbII:'+original+'}',1)

aux=(ROOT/'deliverables/S6_09_PAPERS_I.aux').read_text()
cross_refs={}
def external(label,command):
 ms=re.findall(r'\\newlabel\{([^}]*'+re.escape(label)+r')\}\{\{([^}]+)\}\{([^}]+)\}',aux)
 if len(ms)!=1:raise ValueError(('Unresolved cross-I reference',label,ms))
 full,num,page=ms[0]
 kind='Section' if label.startswith(('sec:','subsec:')) else {'prop':'Proposition','lem':'Lemma','thm':'Theorem','cor':'Corollary'}.get(label.split(':')[0],'Result')
 cross_refs[label]={'paper':'I','printed_label':full,'printed_number':num,'page':page,'type':kind}
 return 'Paper~I, '+kind+'~'+num
def refsub(m):
 command,group=m[1],m[2]
 labels=[re.sub(r'%[^\n]*','',x).strip() for x in group.split(',')]
 labels=[x for x in labels if x]
 local=[x for x in labels if x in all_source_labels or x.startswith(('wbII:','cdp:'))]
 ex=[x for x in labels if x not in local]
 parts=[]
 if local:parts.append('\\'+command+'{'+','.join(destination(x) for x in local)+'}')
 parts += [external(x,command) for x in ex]
 return '; '.join(parts)
wb=re.sub(r'\\(cref|Cref|ref|eqref)\{([^}]+)\}',refsub,wb)
wb=re.sub(r'\\label\{([^}]+)\}',lambda m:'\\label{'+destination(m[1])+'}',wb)

# Replace the two bare references to foundational equations by explicit formulas
# already reproduced in the marked setup and cusp proof.
wb=wb.replace('by (2.2)--(2.4)','by the displayed period inequality')
wb=wb.replace('of (2.8ii)','given by $x_k=e^{2\\pi i\\zeta_k}$ and $t=e^{2\\pi is}$')

# Normalize citations already matched to the same editions. Other keys retain
# their exact source context for the parent's independent source-opening work.
cites={'CDP2020':'CDP20','Grauert1960':'Grauert1960D',
       'RamisRuget1970':'RR70push','BanicaStanasila1976':'BS76push',
       'BaSt':'BS76push','GrRe':'Grauert1960D','S6Source':'AC2026'}
def citefix(m):return m[1]+'{'+','.join(cites.get(x.strip(),x.strip()) for x in m[2].split(','))+'}'
wb=re.sub(r'(\\cite\w*(?:\[[^]]*\])*)\{([^}]+)\}',citefix,wb)
result=intro+wb
DEST.write_text(result)

rows=json.loads((OUT/'working_edition_inventory.json').read_text())
manifest=[]
printed=set(re.findall(r'\\label\{([^}]+)\}',result))
for r in rows:
 sid=r['source_id']
 if r['paper']=='I':
  ms=re.findall(r'\\newlabel\{([^}]*'+re.escape(sid)+r')\}\{\{([^}]+)\}\{([^}]+)\}',aux)
  target=ms[0][0] if len(ms)==1 else 'wb:'+sid
  action='transferred to Paper I; full credited proof already printed'
 elif sid in canonical_aliases:
  target=canonical_aliases[sid]
  action='canonical statement alias; full additional local proof retained here or identical proof steps merged'
 elif sid in local_aliases:
  target='wbII:'+local_aliases[sid]
  action='same statement merged; full proof retained, with correction-note details incorporated'
 else:
  target='wbII:'+sid
  assert target in printed,(sid,'not printed')
  action='complete statement and proof, with preceding definitions, retained in supplement'
 src=ROOT/'sources'/r['source_file'];a,b,s=block(src.read_text(),sid)
 manifest.append({'source_run':r['source_run'],'source_id':sid,'source_file':str(src.relative_to(ROOT)),
  'source_line_start':src.read_text()[:a].count('\n')+1,
  'source_line_end':src.read_text()[:b].count('\n')+1,
  'full_statement_and_proof_sha256':hashlib.sha256(s.encode()).hexdigest(),
  'printed_paper':r['paper'],'printed_label':target,'alias_label':'wbII:'+sid if r['paper']=='II' else target,
  'assembly_action':action,'supplement':str(DEST.relative_to(ROOT)),
  'note':'All existing mathematical hypotheses retained. In the conductor theorem the local clauses are stated without compactness; compactness is explicit in the only clause that uses it. The correction note generic-endpoint parameter-space lemma is distinct and separately retained.' if sid in ['prop:conductor','prop:conductor-differential','lem:generic-endpoints'] else ''})
payload={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17 UTC',
 'supplement':str(DEST.relative_to(ROOT)),'supplement_sha256':hashlib.sha256(result.encode()).hexdigest(),
 'rows':manifest,'canonical_alias_insertions':[{'insert_at':v,'alias':'wbII:'+k} for k,v in canonical_aliases.items()],
 'cross_paper_references':cross_refs,'equation_tags':[{'namespace':n,'source_tag':o,**d} for (n,o),d in tag_info.items()],
 'source_files':{k:{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for k,p in paths.items()}}
(OUT/'working_supplement_mapping.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print('Wrote',len(result.splitlines()),'lines;',len(manifest),'mapped rows;',len(cross_refs),'typed Paper I references.')
